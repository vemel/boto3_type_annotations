from pathlib import Path
from typing import Set

from boto3.session import Session

from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_record_renderer import (
    ImportRecordRenderer,
)
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.nice_path import NicePath
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.writers.utils import write_asset
from mypy_boto3_builder.writers.processors import (
    process_service_waiter,
    process_service_client,
    process_service_resource,
    process_service_paginator,
)


logger = get_logger()


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
