import builtins
import re
from collections import defaultdict
from inspect import getmodule
from keyword import kwlist
from pathlib import Path
from typing import IO, Set, Union, List, Generator, Dict, Optional, Any, Tuple

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
from logger import get_logger
from type_map import TypeAnnotation


ROOT_PATH = Path(__file__).absolute().parent.parent
logger = get_logger()


def add_indentation_to_docstring(docstring: str, levels: int) -> str:
    indention = "".join(["    " for _ in range(levels)])
    return "\n".join([f"{indention}{line}" for line in docstring.split("\n")])


def clean_doc(doc: str) -> str:
    def append_line(section: List[str], next_line: str):
        section.append(next_line.replace("'", "\\'").replace('"', '\\"').rstrip())

    parameters: List[str] = []
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
        line = line.strip()
        if line == "::" or (line.startswith("**") and line.endswith("**")):
            lines[i] = line
    for line in lines:
        if line.strip():
            if line.strip().startswith("**") and line.strip().endswith("**"):
                preamble.append("")
            preamble.append(line)
    return "\n".join(preamble + parameters)


def create_import_statements(types: Set[type]) -> Set[str]:
    result: Set[str] = set()
    for type_annotation in types:
        module = getmodule(type_annotation)
        if module != builtins and module is not None:
            result.add(
                f"from {normalize_type_name(module)} import {normalize_type_name(type_annotation)}"
            )

    return result


def create_module_directory(config: Config):
    package_path = ROOT_PATH / config.package_name
    package_path.mkdir(exist_ok=True)

    module_path = package_path / config.module_name
    module_path.mkdir(exist_ok=True)

    init_path = module_path / "__init__.py"
    init_path.write_text("\n")


def format_arguments(method) -> Generator[str, None, None]:
    arguments = sorted(method.arguments, key=lambda m: m.required, reverse=True)
    for argument in arguments:
        type_repr = normalize_type_name(argument.type, render_args=True)
        default = ""
        if not argument.required:
            type_repr = f"Optional[{type_repr}]"
            default = " = None"

        yield f"{argument.name}: {type_repr}{default}"


def normalize_module_name(name: str) -> str:
    name = name.replace("-", "_")
    if name in kwlist:
        name = f"{name}_"
    return name


def normalize_type_name(
    type_annotation: TypeAnnotation, render_args: bool = False
) -> str:
    if isinstance(type_annotation, str):
        return type_annotation

    name = type_annotation.__class__.__name__
    if hasattr(type_annotation, "_name"):
        name = getattr(type_annotation, "_name") or "Union"
    if getattr(type_annotation, "__name__", None):
        name = type_annotation.__name__
    if type_annotation == Union:
        name = "Union"
    if type_annotation == Optional:
        name = "Optional"
    if type_annotation == Ellipsis:
        name = "..."
    if name == "NoneType":
        name = "None"

    args_rendered = []
    if render_args and hasattr(type_annotation, "__args__"):
        for arg in type_annotation.__args__:
            args_rendered.append(normalize_type_name(arg, render_args=True))
        return f'{name}[{", ".join(args_rendered)}]'

    return name


def write_attributes(attributes: List[Attribute], file_object: IO):
    for attribute in attributes:
        file_object.write(
            f"\n    {attribute.name}: {normalize_type_name(attribute.type)}"
        )


def write_client(client: Client, config: Config):
    logger.debug(f"Writing: {client.name}")
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


def write_import_statements(
    file_object, types: Set[type], import_strings: Tuple[str, ...] = ()
):
    builtin_import_strings: List[str] = []
    boto_import_strings: List[str] = []
    import_statements = create_import_statements(types)
    import_statements.update(import_strings)

    for import_string in import_statements:
        if import_string.startswith("from boto"):
            boto_import_strings.append(import_string)
        else:
            builtin_import_strings.append(import_string)

    file_object.write("from __future__ import annotations\n\n")
    for import_string in sorted(builtin_import_strings):
        file_object.write(f"{import_string}\n")
    for import_string in sorted(boto_import_strings):
        file_object.write(f"{import_string}\n")


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

    logger.debug(f"Writing: {service_resource.name}")
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
        types = {List, Dict, ResourceCollection, Optional, Union}
        types.update(service_resource.get_types())
        write_import_statements(
            file_object,
            types,
            import_strings=(
                "from boto3.resources.base import ServiceResource as Boto3ServiceResource",
            ),
        )

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

    file_object.write(f"\n\nclass {name}(Boto3ServiceResource):")
    attributes = resource.attributes
    attributes += [Attribute(c.name, f"'{c.name}'") for c in resource.collections]
    write_attributes(attributes, file_object)
    file_object.write("\n")
    write_methods(resource.methods, file_object, include_doc=with_docs)


def write_service_waiter(service_waiter: ServiceWaiter, config: Config) -> List[Dict]:
    defined_objects = []
    logger.debug(f"Writing: {service_waiter.name}")
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
            types: Set[TypeAnnotation] = set()
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
            types: Set[TypeAnnotation] = set()
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
    init_files: Dict[str, List[Any]] = defaultdict(list)

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
    logger.info("Writing Service Paginators")
    for service_paginator in parse_service_paginators(session, config):
        write_service_paginator(service_paginator, config)


def write_service_waiters(session: Session, config: Config):
    logger.info("Writing Waiters")
    for service_waiter in parse_service_waiters(session, config):
        write_service_waiter(service_waiter, config)


def write_service_resources(
    init_files: Dict, session: Session, config: Config
) -> Dict[str, List]:
    logger.info("Writing Service Resources")
    for service_resource in parse_service_resources(session, config):
        init_files[service_resource.name] += write_service_resource(
            service_resource, config
        )
    return init_files


def write_clients(
    init_files: Dict, session: Session, config: Config
) -> Dict[str, List]:
    logger.info("Writing Clients")
    for client in parse_clients(session, config):
        init_files[client.name] += write_client(client, config)
    return init_files
