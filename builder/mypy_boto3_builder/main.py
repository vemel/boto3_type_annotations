"""
Main entrypoint for builder.
"""
from typing import List

from boto3.session import Session

from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_master,
    process_service,
)
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.cli_parser import get_cli_parser
from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.constants import MODULE_NAME, DUMMY_REGION, BOTO3_STUBS_NAME


def main() -> None:
    """
    Main entrypoint for builder.
    """
    parser = get_cli_parser()
    args = parser.parse_args()
    logger = get_logger(verbose=args.debug)
    session = Session(region_name=DUMMY_REGION)
    args.output_path.mkdir(exist_ok=True)
    service_names: List[ServiceName] = []
    available_services = session.get_available_services()
    for service_name in args.service_names:
        if service_name.value not in available_services:
            logger.warning(f"Service {service_name.value} is not avaialble, skipping.")
            continue

        service_names.append(service_name)

    if not args.skip_services:
        for service_name in service_names:
            logger.info(f"Generating {service_name.module_name} module")
            output_path = args.output_path / f"{service_name.module_name}_package"
            process_service(
                session=session, output_path=output_path, service_name=service_name
            )

    if not args.skip_master:
        logger.info(f"Generating {MODULE_NAME} module")
        output_path = args.output_path / "master_package"
        process_master(
            session=session, output_path=output_path, service_names=service_names
        )

    if not args.skip_stubs:
        logger.info(f"Generating {BOTO3_STUBS_NAME} module")
        output_path = args.output_path / "boto3_stubs_package"
        process_boto3_stubs(
            session=session, output_path=output_path, service_names=service_names
        )


if __name__ == "__main__":
    main()
