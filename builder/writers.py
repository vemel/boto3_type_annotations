import builtins
import re
from collections import defaultdict
from inspect import getmodule
from keyword import kwlist
from pathlib import Path
import shutil
from typing import IO, Set, Union, Tuple, List, Generator, Dict, Optional

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.session import Session
from botocore.client import BaseClient

from parsers import (
    parse_service_resources,
    parse_clients,
    parse_service_waiters,
    parse_service_paginators,
)
from structures import (
    Method,
    Client,
    ServiceResource,
    Resource,
    Attribute,
    Collection,
    ServiceWaiter,
    ServicePaginator,
    Config,
)


ROOT_PATH = Path(__file__).absolute().parent.parent


def add_indentation_to_docstring(docstring: str, levels: int) -> str:
    indention = "".join(["    " for _ in range(levels)])
    return "\n".join([f"{indention}{line}" for line in docstring.split("\n")])


def clean_doc(doc: str) -> str:
    def append_line(section: List, next_line: str):
        section.append(next_line.replace("'", "\\'").replace('"', '\\"').rstrip())

    parameters = []
    preamble = []
    indices_to_remove = []
    parameter_regex = re.compile("^:(.*[a-zA-Z]):")
    lines = doc.split("\n")
    for i, line in enumerate(lines):
        if parameter_regex.search(line.strip()):
            append_line(parameters, line)
            indices_to_remove.append(i)
            n = i + 1
            while (
                n < len(lines)
                and not parameter_regex.search(lines[n].strip())
                and line.strip() != ":returns:"
            ):
                if lines[n].strip():
                    append_line(parameters, lines[n])
                    indices_to_remove.append(n)
                n += 1
    for i in reversed(indices_to_remove):
        del lines[i]
    for i, line in enumerate(lines):
        if (
            "::" == line.strip()
            or line.strip().startswith("**")
            and line.strip().endswith("**")
        ):
            lines[i] = line.strip()
    for line in lines:
        if line.strip():
            if line.strip().startswith("**") and line.strip().endswith("**"):
                preamble.append("")
            preamble.append(line)
    return "\n".join(preamble + parameters)


def create_import_statements(types: Set[type]) -> Generator[str, None, None]:
    for _type in types:
        if getmodule(_type) != builtins and getmodule(_type) is not None:
            yield f"from {normalize_type_name(getmodule(_type))} import {normalize_type_name(_type)}"


def create_module_directory(config: Config):
    package_path = ROOT_PATH / config.package_name
    package_path.mkdir(exist_ok=True)

    module_path = package_path / config.module_name
    if module_path.exists():
        shutil.rmtree(module_path)

    module_path.mkdir(exist_ok=True)

    init_path = module_path / "__init__.py"
    init_path.write_text("\n")


def format_arguments(method) -> Generator[str, None, None]:
    for argument in sorted(method.arguments, key=lambda m: m.required, reverse=True):
        type_name = normalize_type_name(argument.type)
        default = ""
        if not argument.required:
            type_name = f"Optional[{type_name}]"
            default = " = None"
        yield f"{argument.name}: {type_name}{default}"


def normalize_module_name(name: str) -> str:
    name = name.replace("-", "_")
    if name in kwlist:
        name = f"{name}_"
    return name


def normalize_type_name(type_: Union[type, Tuple, str]):
    if isinstance(type_, tuple):
        return f'Union[{", ".join([normalize_type_name(t) for t in type_])}]'
    if isinstance(type_, str):
        return type_
    if type_ == Union:
        return "Union"
    if type_ == Optional:
        return "Optional"

    if hasattr(type_, "__name__"):
        return type_.__name__

    return getattr(type_, "_name", "Any")


def write_attributes(attributes: List[Attribute], file_object: IO):
    for attribute in attributes:
        file_object.write(
            f"\n    {attribute.name}: {normalize_type_name(attribute.type)}"
        )


def write_client(client: Client, config: Config):
    print(f"Writing: {client.name}")
    normalized_module_name = normalize_module_name(client.name)
    normalized_module_path = (
        ROOT_PATH / config.package_name / config.module_name / normalized_module_name
    )
    if normalized_module_path.exists() and not normalized_module_path.is_dir():
        normalized_module_path.unlink()

    normalized_module_path.mkdir(exist_ok=True)
    file_path = normalized_module_path / "client.py"
    with open(file_path, "w") as file_object:
        types = {Optional, BaseClient, Union}
        types.update(client.get_types())
        write_import_statements(file_object, types)
        file_object.write(f"\n\n\nclass Client(BaseClient):")
        write_methods(client.methods, file_object, include_doc=config.with_docs)

    return [
        {
            "import_statement": f"from {config.module_name}.{normalized_module_name}.client import Client",
            "name": "Client",
        }
    ]


def write_import_statements(file_object, types: Set[type]):
    file_object.write("\n".join(list(create_import_statements(types))))


def write_methods(
    methods: List[Method],
    file_object: IO,
    method_body: str = "pass",
    first_arg: str = "self",
    decorator: str = None,
    include_doc: bool = False,
):
    for method in methods:
        write_method(
            method, file_object, method_body, first_arg, decorator, include_doc
        )


def write_method(
    method: Method,
    file_object: IO,
    method_body: str = "pass",
    first_arg: str = "self",
    decorator: str = None,
    include_doc: bool = False,
):
    file_object.write("\n")
    if decorator:
        file_object.write(f"    {decorator}\n")
    file_object.write(f"    def {method.name}(\n")
    file_object.write(f"        {first_arg},\n")
    for argument_fmt in format_arguments(method):
        file_object.write(f"        {argument_fmt},\n")
    file_object.write("    )")
    if method.return_type:
        file_object.write(f" -> {normalize_type_name(method.return_type)}")
    file_object.write(":\n")
    if include_doc:
        file_object.write('        """\n')
        file_object.write(add_indentation_to_docstring(clean_doc(method.docstring), 2))
        file_object.write('\n        """\n')
    file_object.write(f"        {method_body}\n\n")


def write_service_resource(
    service_resource: ServiceResource, config: Config
) -> List[Dict]:

    print(f"Writing: {service_resource.name}")
    defined_objects = []
    normalized_module_name = normalize_module_name(service_resource.name)
    normalized_module_path = (
        ROOT_PATH / config.package_name / config.module_name / normalized_module_name
    )
    if normalized_module_path.exists() and not normalized_module_path.is_dir():
        normalized_module_path.unlink()

    normalized_module_path.mkdir(exist_ok=True)
    file_path = normalized_module_path / "service_resource.py"
    with open(file_path, "w") as file_object:
        types = {List, Dict, ResourceCollection, Optional, Union, Boto3ServiceResource}
        types.update(service_resource.get_types())
        write_import_statements(file_object, types)
        write_resource(
            service_resource, "ServiceResource", file_object, config.with_docs
        )
        defined_objects.append(
            {
                "import_statement": f"from {config.module_name}.{normalized_module_name}"
                f".service_resource import ServiceResource",
                "name": "ServiceResource",
            }
        )
        for resource in service_resource.sub_resources:
            write_resource(resource, resource.name, file_object, config.with_docs)
            defined_objects.append(
                {
                    "import_statement": f"from {config.module_name}.{normalized_module_name}"
                    f".service_resource import {resource.name}",
                    "name": resource.name,
                }
            )
        for collection in service_resource.collections:
            write_collection(collection, file_object, config.with_docs)
            defined_objects.append(
                {
                    "import_statement": f"from {config.module_name}.{normalized_module_name}"
                    f".service_resource import {collection.name}",
                    "name": collection.name,
                }
            )
    return defined_objects


def write_collection(collection: Collection, file_object: IO, with_docs: bool = False):
    file_object.write(f"\n\nclass {collection.name}(ResourceCollection):")
    write_methods(
        collection.methods,
        file_object,
        first_arg="cls",
        decorator="@classmethod",
        include_doc=with_docs,
    )


def write_resource(
    resource: Union[Resource, ServiceResource],
    name: str,
    file_object: IO,
    with_docs: bool = False,
):

    file_object.write(f"\n\nclass {name}(base.ServiceResource):")
    attributes = resource.attributes
    attributes += [Attribute(c.name, f"'{c.name}'") for c in resource.collections]
    write_attributes(attributes, file_object)
    file_object.write("\n")
    write_methods(resource.methods, file_object, include_doc=with_docs)


def write_service_waiter(service_waiter: ServiceWaiter, config: Config) -> List[Dict]:
    defined_objects = []
    print(f"Writing: {service_waiter.name}")
    normalized_module_name = normalize_module_name(service_waiter.name)
    normalized_module_path = (
        ROOT_PATH / config.package_name / config.module_name / normalized_module_name
    )
    if normalized_module_path.exists() and not normalized_module_path.is_dir():
        normalized_module_path.unlink()

    normalized_module_path.mkdir(exist_ok=True)
    file_path = normalized_module_path / "waiter.py"
    if service_waiter.waiters:
        with open(file_path, "w") as file_object:
            types = set()
            for waiter in service_waiter.waiters:
                types = types.union(waiter.get_types())
            write_import_statements(file_object, types)
            file_object.write("\nfrom botocore.waiter import Waiter\n")
            for waiter in service_waiter.waiters:
                file_object.write(f"\n\nclass {waiter.name}(Waiter):")
                write_methods(waiter.methods, file_object, include_doc=config.with_docs)
                defined_objects.append(
                    {
                        "import_statement": (
                            f"from {config.module_name}.{normalized_module_name}.waiter "
                            f"import {waiter.name}"
                        ),
                        "name": waiter.name,
                    }
                )
    return defined_objects


def write_service_paginator(service_paginator: ServicePaginator, config: Config):
    defined_objects = []
    normalized_module_name = normalize_module_name(service_paginator.name)
    normalized_module_path = (
        ROOT_PATH / config.package_name / config.module_name / normalized_module_name
    )
    if normalized_module_path.exists() and not normalized_module_path.is_dir():
        normalized_module_path.unlink()

    normalized_module_path.mkdir(exist_ok=True)
    file_path = normalized_module_path / "paginator.py"

    if service_paginator.paginators:
        with open(file_path, "w") as file_object:
            types = set()
            for paginator in service_paginator.paginators:
                types = types.union(paginator.get_types())
            write_import_statements(file_object, types)
            file_object.write("\nfrom botocore.paginate import Paginator\n")
            for paginator in service_paginator.paginators:
                file_object.write(f"\n\nclass {paginator.name}(Paginator):")
                write_methods(
                    paginator.methods, file_object, include_doc=config.with_docs
                )
                defined_objects.append(
                    {
                        "import_statement": f"from {config.module_name}.{normalized_module_name}"
                        f".paginator import {paginator.name}",
                        "name": paginator.name,
                    }
                )
    return defined_objects


def write_services(session: Session, config: Config):
    create_module_directory(config)
    init_files = defaultdict(list)

    if config.with_clients:
        init_files = write_clients(init_files, session, config)
    if config.with_service_resources:
        init_files = write_service_resources(init_files, session, config)
    if config.with_waiters:
        write_service_waiters(session, config)
    if config.with_paginators:
        write_service_paginators(session, config)
    write_init_files(init_files, config)


def write_init_files(init_files: Dict[str, List], config: Config):
    for module, imports in init_files.items():
        if imports:
            file_path = (
                ROOT_PATH
                / config.package_name
                / config.module_name
                / normalize_module_name(module)
                / "__init__.py"
            )
            with open(file_path, "w") as file_object:
                file_object.write(
                    "\n".join([i.get("import_statement") for i in imports])
                )
                all_objects = ",\n".join(f'    \'{i.get("name")}\'' for i in imports)
                file_object.write(f"\n\n__all__ = (\n{all_objects}\n)\n")


def write_service_paginators(session: Session, config: Config):
    print("\n\nWriting Clients\n\n")
    for service_paginator in parse_service_paginators(session, config):
        write_service_paginator(service_paginator, config)


def write_service_waiters(session: Session, config: Config):
    print("\n\nWriting Waiters\n\n")
    for service_waiter in parse_service_waiters(session, config):
        write_service_waiter(service_waiter, config)


def write_service_resources(
    init_files: Dict, session: Session, config: Config
) -> Dict[str, List]:
    print("\n\nWriting Service Resources\n\n")
    for service_resource in parse_service_resources(session, config):
        init_files[service_resource.name] += write_service_resource(
            service_resource, config
        )
    return init_files


def write_clients(
    init_files: Dict, session: Session, config: Config
) -> Dict[str, List]:
    print("\n\nWriting Clients\n\n")
    for client in parse_clients(session, config):
        init_files[client.name] += write_client(client, config)
    return init_files
