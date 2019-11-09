from pathlib import Path
from typing import IO, Set, Union

from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.structures import (
    Client,
    ServiceResource,
    Resource,
    Attribute,
    Collection,
    ServiceWaiter,
    ServicePaginator,
)
from mypy_boto3_builder.import_helpers.import_record_renderer import (
    ImportRecordRenderer,
)
from mypy_boto3_builder.logger import get_logger


logger = get_logger()


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

    for method in collection.methods:
        method.decorators = ["classmethod"]
        for line in method.render_lines(include_doc):
            file_object.write(f"    {line}")
            file_object.write("\n")
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
        for attribute in attributes:
            file_object.write(f"    {attribute.render()}")
            file_object.write("\n")

    for method in resource.methods:
        for line in method.render_lines(include_doc):
            file_object.write(f"    {line}")
            file_object.write("\n")
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

            for method in waiter.methods:
                for line in method.render_lines(include_doc):
                    output.write(f"    {line}")
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

            for method in paginator.methods:
                for line in method.render_lines(include_doc):
                    output.write(f"    {line}")
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

        for method in client.methods:
            for line in method.render_lines(include_doc):
                output.write(f"    {line}")
                output.write("\n")
            output.write("\n")
