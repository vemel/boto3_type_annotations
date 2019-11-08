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
    # available_services = session.get_available_services()

    for service_name in args.service_names:
        write_service(
            session,
            service_name=service_name,
            with_docs=not args.no_docs,
            module_name=args.module_name,
            output_path=args.output_path,
        )
        if args.format:
            service_output_path = service_name.get_output_path(
                args.output_path, args.module_name
            )
            format_path(service_output_path)

    if not args.skip_master:
        write_master_module(
            output_path=args.output_path,
            module_name=args.module_name,
            service_names=args.service_names,
        )
        if args.format:
            format_path(args.output_path / f"{args.module_name}_package")


if __name__ == "__main__":
    main()
