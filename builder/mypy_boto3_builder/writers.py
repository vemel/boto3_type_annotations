import builtins
import re
from collections import defaultdict
import inspect
from pathlib import Path
from typing import IO, Set, Union, List, Generator, Dict, Optional, Iterable

from boto3.resources.collection import ResourceCollection
from boto3.session import Session
from botocore.client import BaseClient

from mypy_boto3_builder.parsers import (
    parse_service_resource,
    parse_client,
    parse_service_waiter,
    parse_service_paginator,
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
    TypeAnnotation,
    FakeAnnotation,
    ImportString,
    ImportRecord,
)
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.nice_path import NicePath
from mypy_boto3_builder.service_name import ServiceName


logger = get_logger()


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


def create_module_directory(module_path: Path) -> None:
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


def normalize_type_name(
    type_annotation: TypeAnnotation, render_args: bool = False
) -> str:
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
        yield "# pylint: disable=import-self"
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
        yield ""
        for line in generate_method(
            method, method_body, first_arg, decorator, include_doc
        ):
            if line.strip():
                yield f"    {line}"
            else:
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
    yield "# pylint: disable=arguments-differ"
    yield f"def {method.name}("
    formatted_arguments = [first_arg]
    for formatted_argument in format_arguments(method):
        formatted_arguments.append(formatted_argument)

    for argument_index, formatted_argument in enumerate(formatted_arguments):
        comma = ","
        if argument_index == len(formatted_arguments) - 1:
            comma = ""
        yield f"    {formatted_argument}{comma}"
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
    service_resource: ServiceResource,
    output_path: Path,
    module_name: str,
    with_docs: bool = False,
) -> None:
    with open(output_path, "w") as file_object:
        types = {ResourceCollection}
        types.update(service_resource.get_types())
        for import_line in generate_import_statements(
            types,
            module_name=module_name,
            import_records=[
                ImportRecord(
                    source=ImportString("boto3.resources.base"),
                    name="ServiceResource",
                    alias="Boto3ServiceResource",
                ),
            ],
        ):
            file_object.write(f"{import_line}\n")

        file_object.write("\n\n")
        write_resource(
            service_resource, "ServiceResource", file_object, with_docs=with_docs
        )
        for resource in service_resource.sub_resources:
            file_object.write("\n\n")
            write_resource(resource, resource.name, file_object, with_docs=with_docs)

        added_collection_names: Set[str] = set()
        for collection in service_resource.collections:
            if collection.name in added_collection_names:
                continue
            added_collection_names.add(collection.name)
            file_object.write("\n\n")
            write_collection(collection, file_object, with_docs=with_docs)

        for resource in service_resource.sub_resources:
            for collection in resource.collections:
                if collection.name in added_collection_names:
                    continue
                added_collection_names.add(collection.name)
                file_object.write("\n\n")
                write_collection(collection, file_object, with_docs=with_docs)


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


def write_resource(
    resource: Union[Resource, ServiceResource],
    name: str,
    file_object: IO,
    with_docs: bool = False,
) -> None:

    file_object.write(f"class {name}(Boto3ServiceResource):\n")
    attributes = resource.attributes
    for collection in resource.collections:
        attributes.append(Attribute(collection.name, collection.type))

    if attributes:
        for line in generate_attributes(attributes):
            file_object.write(line)
            file_object.write("\n")

    if resource.methods:
        for line in generate_methods(resource.methods, include_doc=with_docs):
            file_object.write(line)
            file_object.write("\n")


def write_service_waiter(
    service_waiter: ServiceWaiter,
    output_path: Path,
    module_name: str,
    with_docs: bool = False,
) -> None:
    with open(output_path, "w") as file_object:
        types = service_waiter.get_types()
        for import_line in generate_import_statements(
            types,
            module_name=module_name,
            import_records=[
                ImportRecord(source=ImportString("botocore.waiter"), name="Waiter",),
            ],
        ):
            file_object.write(f"{import_line}\n")

        for waiter in service_waiter.waiters:
            file_object.write(f"class {waiter.name}(Waiter):\n")
            for line in generate_methods(waiter.methods, include_doc=with_docs):
                file_object.write(line)
                file_object.write("\n")

            file_object.write("\n")


def write_service_paginator(
    service_paginator: ServicePaginator,
    output_path: Path,
    module_name: str,
    with_docs: bool = False,
) -> None:
    with open(output_path, "w") as file_object:
        types = service_paginator.get_types()

        for import_line in generate_import_statements(
            types,
            module_name=module_name,
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
            for line in generate_methods(paginator.methods, include_doc=with_docs):
                file_object.write(line)
                file_object.write("\n")
            file_object.write("\n")


def write_client(
    client: Client, output_path: Path, module_name: str, with_docs: bool = False
) -> None:
    output = open(output_path, "w")
    types = client.get_types().union({BaseClient})
    for import_line in generate_import_statements(types, module_name):
        output.write(f"{import_line}\n")

    output.write("\n")
    output.write(f"class Client(BaseClient):\n")
    for line in generate_methods(client.methods, include_doc=with_docs):
        output.write(line)
        output.write("\n")
    output.write("\n")


def write_services(
    session: Session,
    service_names: Iterable[ServiceName],
    output_path: Path,
    module_name: str,
    with_docs: bool,
) -> None:
    create_module_directory(output_path / module_name)
    init_import_records: Dict[ServiceName, Set[ImportRecord]] = defaultdict(set)

    logger.info("Creating directories")
    for service_name in service_names:
        module_path = output_path / module_name / service_name.name
        if module_path.exists() and not module_path.is_dir():
            module_path.unlink()

        module_path.mkdir(exist_ok=True)

    logger.info("Writing Clients")
    for service_name in service_names:
        logger.debug(f"Parsing {service_name} Client")
        client = parse_client(session, service_name)
        module_output_path = output_path / module_name / service_name.name / "client.py"
        logger.debug(
            f"Writing Client for {service_name.value} to {NicePath(module_output_path)}"
        )
        write_client(client, module_output_path, module_name, with_docs=with_docs)

        init_import_records[service_name].update(client.get_import_records(module_name))

    logger.info("Writing ServiceResources")
    for service_name in service_names:
        logger.debug(f"Parsing {service_name} ServiceResource")
        service_resource = parse_service_resource(session, service_name)
        if service_resource is None:
            logger.debug(f"Skipping {service_name} ServiceResource")
            continue

        module_output_path = (
            output_path / module_name / service_name.name / "service_resource.py"
        )
        logger.debug(
            f"Writing ServiceResource for {service_name.value} to {NicePath(module_output_path)}"
        )
        write_service_resource(
            service_resource, module_output_path, module_name, with_docs=with_docs,
        )
        init_import_records[service_name].update(
            service_resource.get_import_records(module_name)
        )

    logger.info("Writing ServiceWaiters")
    for service_name in service_names:
        logger.debug(f"Parsing {service_name} ServiceWaiter")
        service_waiter = parse_service_waiter(session, service_name)
        if service_waiter is None or not service_waiter.waiters:
            logger.debug(f"Skipping {service_name} ServiceWaiter")
            continue

        module_output_path = output_path / module_name / service_name.name / "waiter.py"
        logger.debug(
            f"Writing ServiceWaiter for {service_name.value} to {NicePath(module_output_path)}"
        )
        write_service_waiter(
            service_waiter, module_output_path, module_name, with_docs=with_docs
        )

    logger.info("Writing ServicePaginators")
    for service_name in service_names:
        logger.debug(f"Parsing {service_name} ServicePaginator")
        service_paginator = parse_service_paginator(session, service_name)
        if service_paginator is None or not service_paginator.paginators:
            logger.debug(f"Skipping {service_name} ServicePaginator")
            continue

        module_output_path = (
            output_path / module_name / service_name.name / "paginator.py"
        )

        logger.debug(
            f"Writing {service_name.value} ServicePaginator to {NicePath(module_output_path)}"
        )

        write_service_paginator(
            service_paginator, module_output_path, module_name, with_docs=with_docs,
        )

    logger.info("Writing __init__ files")
    for service_name, import_records in init_import_records.items():
        file_path = output_path / module_name / service_name.name / "__init__.py"
        logger.debug(f"Writing {NicePath(file_path)}")
        write_init_file(file_path, import_records, service_name)


def write_init_file(
    file_path: Path, import_records: Set[ImportRecord], service_name: ServiceName
) -> None:
    with open(file_path, "w") as file_object:
        file_object.write(f""""Main interface for {service_name.value} service"\n\n""")
        if not import_records:
            return
        for import_record in sorted(import_records):
            file_object.write(f"{import_record}\n")

        file_object.write("\n__all__ = (\n")
        for import_record in sorted(import_records):
            file_object.write(f"    '{import_record.name}',\n")
        file_object.write(")\n")
