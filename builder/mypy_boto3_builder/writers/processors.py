"""
Processors for parsing and writing modules.
"""
from pathlib import Path
from typing import Iterable

from boto3.session import Session

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.parsers.master_package import parse_master_package
from mypy_boto3_builder.parsers.boto3_stubs_package import parse_boto3_stubs_package
from mypy_boto3_builder.parsers.service_package import parse_service_package
from mypy_boto3_builder.structures.boto3_stubs_package import Boto3StubsPackage
from mypy_boto3_builder.structures.master_package import MasterPackage
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.writers.boto3_stubs_package import write_boto3_stubs_package
from mypy_boto3_builder.writers.master_package import write_master_package
from mypy_boto3_builder.writers.service_package import write_service_package


logger = get_logger()


def process_boto3_stubs(
    session: Session, service_names: Iterable[ServiceName], output_path: Path
) -> Boto3StubsPackage:
    logger.debug(f"Parsing boto3 stubs")
    boto3_module = parse_boto3_stubs_package(session, service_names)
    logger.debug(f"Writing boto3 stubs to {NicePath(output_path)}")

    modified_paths = write_boto3_stubs_package(boto3_module, output_path)
    for modified_path in modified_paths:
        logger.debug(f"Updated {NicePath(modified_path)}")

    return boto3_module


def process_master(
    session: Session, service_names: Iterable[ServiceName], output_path: Path
) -> MasterPackage:
    logger.debug(f"Parsing master")
    master_module = parse_master_package(session, service_names)
    logger.debug(f"Writing master to {NicePath(output_path)}")

    modified_paths = write_master_package(master_module, output_path)
    for modified_path in modified_paths:
        logger.debug(f"Updated {NicePath(modified_path)}")

    return master_module


def process_service(
    session: Session, service_name: ServiceName, output_path: Path
) -> ServicePackage:
    logger.debug(f"Parsing {service_name.boto3_name}")
    service_module = parse_service_package(session, service_name)
    logger.debug(f"Writing {service_name.boto3_name} to {NicePath(output_path)}")

    modified_paths = write_service_package(service_module, output_path)
    module_file_names = [i.value for i in ServiceModuleName]
    for modified_path in modified_paths:
        if modified_path.stem in module_file_names:
            logger.info(f"Updated {NicePath(modified_path)}")
        else:
            logger.debug(f"Updated {NicePath(modified_path)}")

    return service_module
