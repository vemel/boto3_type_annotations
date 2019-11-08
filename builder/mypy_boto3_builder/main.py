from boto3.session import Session

from mypy_boto3_builder.writers import write_service, write_master_module, format_path
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.cli_parser import get_cli_parser


def main() -> None:
    parser = get_cli_parser()
    args = parser.parse_args()
    if args.version:
        print(version)
        return

    get_logger(verbose=args.debug)
    session = Session()
    args.output_path.mkdir(exist_ok=True)
    # available_services = session.get_available_services()

    if not args.skip_services:
        service_name_postfix = "" if args.no_docs else "_with_docs"
        for service_name in args.service_names:
            service_output_path = (
                args.output_path
                / f"{args.module_name}_{service_name.name}_package{service_name_postfix}"
                / f"{args.module_name}_{service_name.name}{service_name_postfix}"
            )
            service_output_path.parent.mkdir(exist_ok=True)
            service_output_path.mkdir(exist_ok=True)
            write_service(
                session,
                service_name=service_name,
                include_doc=not args.no_docs,
                output_path=service_output_path,
            )
            if args.format:
                format_path(service_output_path)

    if not args.skip_master:
        master_output_path = (
            args.output_path / f"{args.module_name}_package" / args.module_name
        )
        master_output_path.parent.mkdir(exist_ok=True)
        master_output_path.mkdir(exist_ok=True)
        write_master_module(
            output_path=master_output_path, service_names=args.service_names,
        )
        if args.format:
            format_path(master_output_path.parent)


if __name__ == "__main__":
    main()
