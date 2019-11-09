from pathlib import Path
from typing import IO, Set, Union, List, Generator, Dict, Iterable, Optional

from boto3.session import Session

from mypy_boto3_builder.version import __version__ as version
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
)
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_record_renderer import (
    ImportRecordRenderer,
)
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.nice_path import NicePath
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils import (
    clean_doc,
    render_template,
    black_reformat,
)
from mypy_boto3_builder.constants import WITH_DOCS_PYPI_POSTFIX, PYPI_NAME, MODULE_NAME


logger = get_logger()


def format_arguments(method: Method) -> Generator[str, None, None]:
    arguments = sorted(method.arguments, key=lambda m: m.required, reverse=True)
    for argument in arguments:
        default = ""
        argument_type = argument.type
        if not argument.required:
            # argument_type = Optional[argument_type]
            default = " = None"

        type_repr = argument_type.render()
        yield f"{argument.name}: {type_repr}{default}"


def generate_attributes(attributes: List[Attribute]) -> Generator[str, None, None]:
    for attribute in attributes:
        yield f"    {attribute.name}: {attribute.type.render()}"


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
        yield f") -> {method.return_type.render()}:"
    else:
        yield "):"

    if include_doc:
        docstring = clean_doc(method.docstring)
        if docstring:
            yield '    """'
            for line in docstring.split("\n"):
                yield f"    {line}"
            yield '    """'
    yield f"    {method_body}"


def write_service_resource(
    service_resource: ServiceResource,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool,
) -> None:
    with open(output_path, "w") as output:
        for import_line in import_record_renderer.generate_lines(
            service_resource.get_types()
        ):
            output.write(f"{import_line}\n")

        output.write("\n\n")
        write_resource(
            service_resource, "ServiceResource", output, include_doc=include_doc
        )
        for resource in service_resource.sub_resources:
            output.write("\n\n")
            write_resource(resource, resource.name, output, include_doc=include_doc)

        added_collection_names: Set[str] = set()
        for collection in service_resource.collections:
            if collection.name in added_collection_names:
                continue
            added_collection_names.add(collection.name)
            output.write("\n\n")
            write_collection(collection, output, include_doc=include_doc)

        for resource in service_resource.sub_resources:
            for collection in resource.collections:
                if collection.name in added_collection_names:
                    continue
                added_collection_names.add(collection.name)
                output.write("\n\n")
                write_collection(collection, output, include_doc=include_doc)


def write_collection(
    collection: Collection, file_object: IO, include_doc: bool = False
) -> None:
    file_object.write(f"class {collection.name}(ResourceCollection):\n")
    if include_doc and collection.docstring:
        file_object.write('    """\n')
        for line in collection.docstring.split("\n"):
            file_object.write(f"    {line}\n")
        file_object.write('    """\n')

    for line in generate_methods(
        collection.methods,
        first_arg="cls",
        decorator="@classmethod",
        include_doc=include_doc,
    ):
        file_object.write(line)
        file_object.write("\n")


def write_resource(
    resource: Union[Resource, ServiceResource],
    name: str,
    file_object: IO,
    include_doc: bool = False,
) -> None:

    file_object.write(f"class {name}(Boto3ServiceResource):\n")

    if include_doc and resource.docstring:
        file_object.write('    """\n')
        for line in resource.docstring.split("\n"):
            file_object.write(f"    {line}\n")
        file_object.write('    """\n')

    attributes = resource.attributes
    for collection in resource.collections:
        attributes.append(Attribute(collection.name, collection.type))

    if attributes:
        for line in generate_attributes(attributes):
            file_object.write(line)
            file_object.write("\n")

    if resource.methods:
        for line in generate_methods(resource.methods, include_doc=include_doc):
            file_object.write(line)
            file_object.write("\n")


def write_service_waiter(
    service_waiter: ServiceWaiter,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool = False,
) -> None:
    with open(output_path, "w") as output:
        for import_line in import_record_renderer.generate_lines(
            service_waiter.get_types()
        ):
            output.write(f"{import_line}\n")

        for waiter in service_waiter.waiters:
            output.write(f"class {waiter.name}(Waiter):\n")

            if include_doc and waiter.docstring:
                output.write('    """\n')
                for line in waiter.docstring.split("\n"):
                    output.write(f"    {line}\n")
                output.write('    """\n')

            for line in generate_methods(waiter.methods, include_doc=include_doc):
                output.write(line)
                output.write("\n")

            output.write("\n")


def write_service_paginator(
    service_paginator: ServicePaginator,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool,
) -> None:
    with open(output_path, "w") as output:
        for import_line in import_record_renderer.generate_lines(
            service_paginator.get_types(),
        ):
            output.write(f"{import_line}\n")

        output.write("\n")
        for paginator in service_paginator.paginators:
            output.write(f"class {paginator.name}(Paginator):\n")

            if include_doc and paginator.docstring:
                output.write('    """\n')
                for line in paginator.docstring.split("\n"):
                    output.write(f"    {line}\n")
                output.write('    """\n')

            for line in generate_methods(paginator.methods, include_doc=include_doc):
                output.write(line)
                output.write("\n")
            output.write("\n")


def write_client(
    client: Client,
    output_path: Path,
    import_record_renderer: ImportRecordRenderer,
    include_doc: bool,
) -> None:
    with open(output_path, "w") as output:
        for import_line in import_record_renderer.generate_lines(client.get_types()):
            output.write(f"{import_line}\n")

        output.write("\n")
        output.write(f"class Client(BaseClient):\n")

        if include_doc and client.docstring:
            output.write('    """\n')
            for line in client.docstring.split("\n"):
                output.write(f"    {line}\n")
            output.write('    """\n')

        for line in generate_methods(client.methods, include_doc=include_doc):
            output.write(line)
            output.write("\n")
        output.write("\n")


def process_service_client(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Client:
    logger.debug(f"Parsing {service_name} Client")
    client = parse_client(session, service_name)
    module_output_path = service_output_path / "client.py"
    logger.debug(
        f"Writing Client for {service_name.boto3_name} to {NicePath(module_output_path)}"
    )
    write_client(
        client,
        module_output_path,
        import_record_renderer,
        include_doc=service_name.is_with_docs(),
    )
    return client


def process_service_resource(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Optional[ServiceResource]:
    logger.debug(f"Parsing {service_name} ServiceResource")
    service_resource = parse_service_resource(session, service_name)
    if service_resource is None:
        logger.debug(f"Skipping {service_name} ServiceResource")
        return None

    module_output_path = service_output_path / "service_resource.py"

    logger.debug(
        f"Writing ServiceResource for {service_name.boto3_name} to {NicePath(module_output_path)}"
    )
    write_service_resource(
        service_resource,
        module_output_path,
        import_record_renderer,
        include_doc=service_name.is_with_docs(),
    )
    return service_resource


def process_service_waiter(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Optional[ServiceWaiter]:
    logger.debug(f"Parsing {service_name} ServiceWaiter")
    service_waiter = parse_service_waiter(session, service_name)
    if service_waiter is None or not service_waiter.waiters:
        logger.debug(f"Skipping {service_name} ServiceWaiter")
        return None

    module_output_path = service_output_path / "waiter.py"

    logger.debug(
        f"Writing ServiceWaiter for {service_name.boto3_name} to {NicePath(module_output_path)}"
    )
    write_service_waiter(
        service_waiter,
        module_output_path,
        import_record_renderer,
        include_doc=service_name.is_with_docs(),
    )
    return service_waiter


def process_service_paginator(
    session: Session,
    service_name: ServiceName,
    service_output_path: Path,
    import_record_renderer: ImportRecordRenderer,
) -> Optional[ServicePaginator]:
    logger.debug(f"Parsing {service_name} ServicePaginator")
    service_paginator = parse_service_paginator(session, service_name)
    if service_paginator is None or not service_paginator.paginators:
        logger.debug(f"Skipping {service_name} ServicePaginator")
        return None

    module_output_path = service_output_path / "paginator.py"

    logger.debug(
        f"Writing {service_name.boto3_name} ServicePaginator to {NicePath(module_output_path)}"
    )

    write_service_paginator(
        service_paginator,
        module_output_path,
        import_record_renderer,
        include_doc=service_name.is_with_docs(),
    )
    return service_paginator


def write_submodule(
    session: Session, service_name: ServiceName, output_path: Path
) -> None:
    init_import_records: Set[ImportRecord] = set()

    import_record_renderer = ImportRecordRenderer(
        [service_name.module_name], [ImportRecord("__future__", "annotations")]
    )

    logger.info(f"Writing {service_name.extras_name} submodule")

    client = process_service_client(
        session, service_name, output_path, import_record_renderer
    )
    init_import_records.update(client.get_import_records())

    service_resource = process_service_resource(
        session, service_name, output_path, import_record_renderer
    )
    if service_resource:
        init_import_records.update(service_resource.get_import_records())

    process_service_waiter(session, service_name, output_path, import_record_renderer)

    process_service_paginator(
        session, service_name, output_path, import_record_renderer
    )

    init_file_path = output_path / "__init__.py"
    logger.debug(f"Writing {NicePath(init_file_path)}")
    write_init_file(init_file_path, init_import_records, service_name)


def format_path(path: Path) -> None:
    logger.debug(f"Applying black formatting to {NicePath(path)}")
    for source_path in path.glob("**/*.py"):
        logger.debug(f"Reformatting {NicePath(source_path)}")
        result = black_reformat(source_path)
        if result:
            logger.debug(f"Reformatted {NicePath(source_path)}")


def write_master_module(
    output_path: Path, service_names: Iterable[ServiceName]
) -> None:
    logger.info(f"Writing master module")
    logger.debug(f"Writing assets")

    write_asset(output_path / "py.typed", "py.typed.template")
    write_asset(output_path / "__main__.py", "__main__.py.template")
    write_asset(output_path / "__init__.py", "__init__.py.template")
    write_asset(output_path / "version.py", "version.py.template", version=version)
    write_asset(output_path.parent / "README.md", "master_readme_md.template")

    extras_require: Dict[str, List[str]] = {
        "all": [],
        f"all{WITH_DOCS_PYPI_POSTFIX}": [],
        "essential": [],
        f"essential{WITH_DOCS_PYPI_POSTFIX}": [],
    }
    for service_name in service_names:
        service_install_string = f"{service_name.pypi_name}=={version}"
        extras_require[service_name.extras_name] = [service_install_string]
        if service_name.is_with_docs():
            extras_require[f"all{WITH_DOCS_PYPI_POSTFIX}"].append(
                service_install_string
            )
        else:
            extras_require[f"all"].append(service_install_string)

        if service_name.is_essential():
            if service_name.is_with_docs():
                extras_require[f"essential{WITH_DOCS_PYPI_POSTFIX}"].append(
                    service_install_string
                )
            else:
                extras_require[f"essential"].append(service_install_string)

    write_asset(
        output_path.parent / "setup.py",
        "setup.py.template",
        module_name=MODULE_NAME,
        name=PYPI_NAME,
        extras_require=str(extras_require),
    )


def write_master_module_service_stub(
    output_path: Path, service_name: ServiceName, service_output_path: Path
) -> None:
    master_service_path = output_path / service_name.import_name
    master_service_path.mkdir(exist_ok=True)

    write_asset(
        master_service_path / "__init__.py",
        "master_service_init.template",
        service_module_name=service_name.module_name,
        fallback_service_module_name=service_name.fallback.module_name,
        module_name=MODULE_NAME,
        import_name=service_name.import_name,
        extras_name=service_name.fallback.extras_name,
    )

    submodule_names = ["client", "paginator", "service_resource", "waiter"]
    for submodule_name in submodule_names:
        submodule_path = service_output_path / f"{submodule_name}.py"
        if not submodule_path.exists():
            continue

        write_asset(
            master_service_path / f"{submodule_name}.py",
            "master_service_submodule.template",
            submodule_name=submodule_name,
            service_module_name=service_name.module_name,
            fallback_service_module_name=service_name.fallback.module_name,
            module_name=MODULE_NAME,
            import_name=service_name.import_name,
            extras_name=service_name.fallback.extras_name,
        )


def write_submodule_assets(
    service_output_path: Path, service_name: ServiceName
) -> None:
    write_asset(service_output_path / "py.typed", "py.typed.template")
    write_asset(service_output_path / "__main__.py", "__main__.py.template")
    write_asset(
        service_output_path / "version.py", "version.py.template", version=version
    )

    write_asset(
        service_output_path.parent / "README.md",
        "service_readme_md.template",
        boto3_name=service_name.boto3_name,
        submodule_name=service_name.name,
        pypi_name=service_name.pypi_name,
        import_name=service_name.import_name,
    )

    write_asset(
        service_output_path.parent / "setup.py",
        "service_setup.py.template",
        boto3_name=service_name.boto3_name,
        package_name=service_name.module_name,
        name=service_name.pypi_name,
    )


def write_asset(file_path: Path, template_name: str, **kwargs: str) -> None:
    rendered = render_template(template_name, **kwargs)
    logger.debug(f"Rendering {template_name} to {NicePath(file_path)}")
    with open(file_path, "w") as file_object:
        file_object.write(rendered)


def write_init_file(
    file_path: Path, import_records: Set[ImportRecord], service_name: ServiceName
) -> None:
    with open(file_path, "w") as file_object:
        file_object.write(
            f""""Main interface for {service_name.boto3_name} service"\n\n"""
        )
        if not import_records:
            return
        for import_record in sorted(import_records):
            file_object.write(f"{import_record}\n")

        file_object.write("\n__all__ = (\n")
        for import_record in sorted(import_records):
            file_object.write(f"    '{import_record.name}',\n")
        file_object.write(")\n")
