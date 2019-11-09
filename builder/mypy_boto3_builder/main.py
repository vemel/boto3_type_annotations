from boto3.session import Session

from mypy_boto3_builder.writers import (
    write_submodule,
    write_submodule_assets,
    write_master_module,
    write_master_module_service_stub,
    format_path,
)
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.cli_parser import get_cli_parser
from mypy_boto3_builder.constants import MODULE_NAME, DUMMY_REGION


def main() -> None:
    parser = get_cli_parser()
    args = parser.parse_args()
    if args.version:
        print(version)
        return

    get_logger(verbose=args.debug)
    session = Session(region_name=DUMMY_REGION)
    args.output_path.mkdir(exist_ok=True)
    # available_services = session.get_available_services()

    if not args.skip_services:
        for service_name in args.service_names:
            service_output_path = (
                args.output_path
                / f"{service_name.module_name}_package"
                / service_name.module_name
            )
            service_output_path.parent.mkdir(exist_ok=True)
            service_output_path.mkdir(exist_ok=True)
            write_submodule(
                session, service_name=service_name, output_path=service_output_path,
            )
            write_submodule_assets(
                service_output_path=service_output_path, service_name=service_name,
            )
            if args.format:
                format_path(service_output_path)

    if not args.skip_master:
        master_output_path = args.output_path / f"{MODULE_NAME}_package" / MODULE_NAME
        master_output_path.parent.mkdir(exist_ok=True)
        master_output_path.mkdir(exist_ok=True)
        write_master_module(
            output_path=master_output_path, service_names=args.service_names,
        )
        for service_name in args.service_names:
            if not service_name.is_with_docs():
                continue

            service_output_path = (
                args.output_path
                / f"{service_name.module_name}_package"
                / service_name.module_name
            )
            write_master_module_service_stub(
                master_output_path, service_name, service_output_path,
            )

        if args.format:
            format_path(master_output_path.parent)


if __name__ == "__main__":
    main()
