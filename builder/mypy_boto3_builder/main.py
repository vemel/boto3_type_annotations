from boto3.session import Session
import black

from mypy_boto3_builder.writers import write_services
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.structures import Config
from mypy_boto3_builder.nice_path import NicePath
from mypy_boto3_builder.cli_parser import get_cli_parser


def main() -> None:
    parser = get_cli_parser()
    args = parser.parse_args()
    if args.version:
        print(version)
        return

    logger = get_logger(verbose=args.debug)
    session = Session()
    # available_services = session.get_available_services()

    write_services(
        session,
        Config(
            services=args.services,
            with_docs=args.with_docs,
            module_name=args.module_name,
            output=args.output,
        ),
    )

    module_path = args.output / args.module_name

    if args.format:
        logger.info("Applying black formatting")
        for service_name in args.services:
            service_path = module_path / service_name
            for source_path in service_path.glob("**/*.py"):
                black_result = black.format_file_in_place(
                    source_path,
                    fast=False,
                    mode=black.FileMode(),
                    write_back=black.WriteBack.YES,
                )
                if black_result:
                    logger.debug(f"Reformatted {NicePath(source_path)}")


if __name__ == "__main__":
    main()
