import builtins
import re
from collections import defaultdict
import inspect
from keyword import kwlist
from pathlib import Path
from typing import IO, Set, Union, List, Generator, Dict, Optional, Any, Iterable

from boto3.resources.collection import ResourceCollection
from boto3.session import Session
from botocore.client import BaseClient

from mypy_boto3_builder.parsers import (
    parse_service_resources,
    parse_clients,
    parse_service_waiters,
    parse_service_paginators,
)
from mypy_boto3_builder.structures import (
    Method,
    Client,
    ServiceResource,
    Resource,
    Attribute,
    Collection,
    ServiceWaiter,
    ServicePaginator,
    Config,
    TypeAnnotation,
    FakeAnnotation,
    ImportString,
    ImportRecord,
)
from mypy_boto3_builder.logger import get_logger


logger = get_logger()


def add_indentation_to_docstring(docstring: str, levels: int) -> str:
    indention = "".join(["    " for _ in range(levels)])
    return "\n".join([f"{indention}{line}" for line in docstring.split("\n")])


def clean_doc(doc: str) -> str:
    def append_line(section: List[str], next_line: str) -> None:
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


def create_module_directory(config: Config) -> None:
    module_path = config.output / config.module_name
    module_path.mkdir(exist_ok=True)

    init_path = module_path / "__init__.py"
    init_path.write_text("\n")


def format_arguments(method: Method) -> Generator[str, None, None]:
    arguments = sorted(method.arguments, key=lambda m: m.required, reverse=True)
    for argument in arguments:
        default = ""
        argument_type = argument.type
        if not argument.required:
            # argument_type = Optional[argument_type]
            default = " = None"

        type_repr = normalize_type_name(argument_type, render_args=True)
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

    name = str(type_annotation)
    if hasattr(type_annotation, "_name"):
        name = getattr(type_annotation, "_name") or "Union"
    if getattr(type_annotation, "__name__", None):
        name = getattr(type_annotation, "__name__")
    if type_annotation == Union:
        name = "Union"
    if type_annotation == Optional:
        name = "Optional"
    if type_annotation == Ellipsis:
        name = "..."
    if name == "NoneType":
        name = "None"

    if str(type_annotation).startswith("~"):
        name = "Any"

    args_rendered = []
    if render_args and hasattr(type_annotation, "__args__"):
        for arg in getattr(type_annotation, "__args__"):
            args_rendered.append(normalize_type_name(arg, render_args=True))
        return f'{name}[{", ".join(args_rendered)}]'

    return name


def generate_attributes(attributes: List[Attribute]) -> Generator[str, None, None]:
    for attribute in attributes:
        yield f"    {attribute.name}: {normalize_type_name(attribute.type)}"


def write_client(client: Client, config: Config) -> List[Dict]:
    normalized_module_name = normalize_module_name(client.name)
    normalized_module_path = config.output / config.module_name / normalized_module_name
    if normalized_module_path.exists() and not normalized_module_path.is_dir():
        normalized_module_path.unlink()

    normalized_module_path.mkdir(exist_ok=True)
    file_path = normalized_module_path / "client.py"
    logger.debug(f"Writing: {client.name} to {file_path.relative_to(Path.cwd())}")
    with open(file_path, "w") as file_object:
        types = client.get_types()
        types.add(BaseClient)

        for import_line in generate_import_statements(
            types, module_name=config.module_name,
        ):
            file_object.write(f"{import_line}\n")

        file_object.write("\n")
        file_object.write(f"class Client(BaseClient):\n")
        for line in generate_methods(client.methods, include_doc=config.with_docs):
            file_object.write(line)
            file_object.write("\n")
        file_object.write("\n")

    return [
        {
            "import_statement": f"from {config.module_name}.{normalized_module_name}.client import Client",
            "name": "Client",
        }
    ]


def generate_import_statements(
    types: Set[TypeAnnotation],
    module_name: str,
    import_records: Iterable[ImportRecord] = (),
) -> Generator[str, None, None]:
    builtin_import_strings: Set[ImportRecord] = set()
    boto_import_strings: Set[ImportRecord] = set()
    local_import_strings: Set[ImportRecord] = set()

    import_statements: Set[ImportRecord] = set()
    for type_annotation in types:
        if isinstance(type_annotation, FakeAnnotation):
            import_statements.add(type_annotation.get_import_record(module_name))
            continue

        parent_module = inspect.getmodule(type_annotation)
        if parent_module is None or parent_module == builtins:
            continue

        parent_module_name = parent_module.__name__
        import_statements.add(
            ImportRecord(
                source=ImportString(parent_module_name),
                name=normalize_type_name(type_annotation),
            )
        )

    import_statements.update(import_records)

    boto3_import_string = ImportString("boto3")
    botocore_import_string = ImportString("botocore")
    local_import_string = ImportString(module_name)
    for import_string in import_statements:
        if import_string.source.startswith(boto3_import_string):
            boto_import_strings.add(import_string)
        elif import_string.source.startswith(botocore_import_string):
            boto_import_strings.add(import_string)
        elif import_string.source.startswith(local_import_string):
            local_import_strings.add(import_string)
        else:
            builtin_import_strings.add(import_string)

    yield "from __future__ import annotations"
    yield ""
    if builtin_import_strings:
        yield "# builtin imports"
        for import_string in sorted(builtin_import_strings):
            yield import_string.render()
        yield ""
    if boto_import_strings:
        yield "# boto3 imports"
        for import_string in sorted(boto_import_strings):
            yield import_string.render()
        yield ""
    if local_import_strings:
        yield "# local imports"
        for import_string in sorted(local_import_strings):
            yield import_string.render()
        yield ""


def generate_methods(
    methods: List[Method],
    method_body: str = "pass",
    first_arg: str = "self",
    decorator: str = None,
    include_doc: bool = False,
) -> Generator[str, None, None]:
    for method in methods:
        for line in generate_method(
            method, method_body, first_arg, decorator, include_doc
        ):
            if line.strip():
                yield f"    {line}"
            else:
                yield ""
        yield ""


def generate_method(
    method: Method,
    method_body: str = "pass",
    first_arg: str = "self",
    decorator: str = None,
    include_doc: bool = False,
) -> Generator[str, None, None]:
    if decorator:
        yield decorator
    yield f"def {method.name}("
    yield f"    {first_arg},"
    for argument_fmt in format_arguments(method):
        yield f"    {argument_fmt},"
    if method.return_type:
        yield f") -> {normalize_type_name(method.return_type, render_args=True)}:"
    else:
        yield "):"

    if include_doc:
        docstring = clean_doc(method.docstring)
        if docstring:
            yield '    """'
            for line in clean_doc(method.docstring).split("\n"):
                yield f"    {line}"
            yield '    """'
    yield f"    {method_body}"


def write_service_resource(
    service_resource: ServiceResource, config: Config
) -> List[Dict]:
    defined_objects = []
    normalized_module_name = normalize_module_name(service_resource.name)
    normalized_module_path = config.output / config.module_name / normalized_module_name
    if normalized_module_path.exists() and not normalized_module_path.is_dir():
        normalized_module_path.unlink()

    normalized_module_path.mkdir(exist_ok=True)
    file_path = normalized_module_path / "service_resource.py"
    logger.debug(
        f"Writing: {service_resource.name} to {file_path.relative_to(Path.cwd())}"
    )

    with open(file_path, "w") as file_object:
        types = {List, Dict, ResourceCollection, Union}
        types.update(service_resource.get_types())
        for import_line in generate_import_statements(
            types,
            module_name=config.module_name,
            import_records=[
                ImportRecord(
                    source=ImportString("boto3.resources.base"),
                    name="ServiceResource",
                    alias="Boto3ServiceResource",
                ),
            ],
        ):
            file_object.write(f"{import_line}\n")

        file_object.write("\n")
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

        for resource in service_resource.sub_resources:
            for collection in resource.collections:
                write_collection(collection, file_object, config.with_docs)
                defined_objects.append(
                    {
                        "import_statement": f"from {config.module_name}.{normalized_module_name}"
                        f".service_resource import {collection.name}",
                        "name": collection.name,
                    }
                )
    return defined_objects


def write_collection(
    collection: Collection, file_object: IO, with_docs: bool = False
) -> None:
    file_object.write(f"class {collection.name}(ResourceCollection):\n")
    for line in generate_methods(
        collection.methods,
        first_arg="cls",
        decorator="@classmethod",
        include_doc=with_docs,
    ):
        file_object.write(line)
        file_object.write("\n")
    file_object.write("\n")


def write_resource(
    resource: Union[Resource, ServiceResource],
    name: str,
    file_object: IO,
    with_docs: bool = False,
) -> None:

    file_object.write(f"class {name}(Boto3ServiceResource):\n")
    attributes = resource.attributes
    attributes += [Attribute(c.name, c.type) for c in resource.collections]
    if attributes:
        for line in generate_attributes(attributes):
            file_object.write(line)
            file_object.write("\n")
        file_object.write("\n")
    if resource.methods:
        for line in generate_methods(resource.methods, include_doc=with_docs):
            file_object.write(line)
            file_object.write("\n")
    file_object.write("\n")


def write_service_waiter(service_waiter: ServiceWaiter, config: Config) -> List[Dict]:
    defined_objects: List[Dict] = []
    if not service_waiter.waiters:
        return defined_objects

    normalized_module_name = normalize_module_name(service_waiter.name)
    normalized_module_path = config.output / config.module_name / normalized_module_name
    if normalized_module_path.exists() and not normalized_module_path.is_dir():
        normalized_module_path.unlink()

    normalized_module_path.mkdir(exist_ok=True)
    file_path = normalized_module_path / "waiter.py"
    logger.debug(
        f"Writing: {service_waiter.name} to {file_path.relative_to(Path.cwd())}"
    )

    with open(file_path, "w") as file_object:
        types = service_waiter.get_types()
        for import_line in generate_import_statements(
            types,
            module_name=config.module_name,
            import_records=[
                ImportRecord(source=ImportString("botocore.waiter"), name="Waiter",),
            ],
        ):
            file_object.write(f"{import_line}\n")

        for waiter in service_waiter.waiters:
            file_object.write(f"class {waiter.name}(Waiter):\n")
            for line in generate_methods(waiter.methods, include_doc=config.with_docs):
                file_object.write(line)
                file_object.write("\n")

            file_object.write("\n")
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


def write_service_paginator(
    service_paginator: ServicePaginator, config: Config
) -> List[Dict]:
    defined_objects: List[Dict] = []
    if not service_paginator.paginators:
        return defined_objects

    normalized_module_name = normalize_module_name(service_paginator.name)
    normalized_module_path = config.output / config.module_name / normalized_module_name
    if normalized_module_path.exists() and not normalized_module_path.is_dir():
        normalized_module_path.unlink()

    normalized_module_path.mkdir(exist_ok=True)
    file_path = normalized_module_path / "paginator.py"

    with open(file_path, "w") as file_object:
        types = service_paginator.get_types()

        for import_line in generate_import_statements(
            types,
            module_name=config.module_name,
            import_records=[
                ImportRecord(
                    source=ImportString("botocore.paginate"), name="Paginator",
                ),
            ],
        ):
            file_object.write(f"{import_line}\n")

        file_object.write("\n")
        for paginator in service_paginator.paginators:
            file_object.write(f"class {paginator.name}(Paginator):\n")
            for line in generate_methods(
                paginator.methods, include_doc=config.with_docs
            ):
                file_object.write(line)
                file_object.write("\n")
            file_object.write("\n")
            defined_objects.append(
                {
                    "import_statement": f"from {config.module_name}.{normalized_module_name}"
                    f".paginator import {paginator.name}",
                    "name": paginator.name,
                }
            )
    return defined_objects


def write_services(session: Session, config: Config) -> None:
    create_module_directory(config)
    init_files: Dict[str, List[Any]] = defaultdict(list)

    init_files = write_clients(init_files, session, config)
    init_files = write_service_resources(init_files, session, config)
    write_service_waiters(session, config)
    write_service_paginators(session, config)
    write_init_files(init_files, config)


def write_init_files(init_files: Dict[str, List], config: Config) -> None:
    for module, imports in init_files.items():
        if imports:
            file_path = (
                config.output
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


def write_service_paginators(session: Session, config: Config) -> None:
    logger.info("Writing ServicePaginators")
    for service_paginator in parse_service_paginators(session, config):
        write_service_paginator(service_paginator, config)


def write_service_waiters(session: Session, config: Config) -> None:
    logger.info("Writing ServiceWaiters")
    for service_waiter in parse_service_waiters(session, config):
        write_service_waiter(service_waiter, config)


def write_service_resources(
    init_files: Dict, session: Session, config: Config
) -> Dict[str, List]:
    logger.info("Writing ServiceResources")
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
