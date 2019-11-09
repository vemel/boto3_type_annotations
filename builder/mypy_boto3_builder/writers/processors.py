from pathlib import Path
from typing import Optional

from boto3.session import Session

from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.parsers import (
    parse_service_resource,
    parse_client,
    parse_service_waiter,
    parse_service_paginator,
)
from mypy_boto3_builder.structures import (
    Client,
    ServiceResource,
    ServiceWaiter,
    ServicePaginator,
)
from mypy_boto3_builder.import_helpers.import_record_renderer import (
    ImportRecordRenderer,
)
from mypy_boto3_builder.nice_path import NicePath
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.writers.line_generators import (
    write_service_resource,
    write_client,
    write_service_waiter,
    write_service_paginator,
)


logger = get_logger()


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
