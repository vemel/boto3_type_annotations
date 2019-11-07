import argparse
from pathlib import Path
from typing import List

from boto3.session import Session
import black

from mypy_boto3_builder.writers import write_services
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.structures import Config


def absolute_path(path: str) -> Path:
    return Path(path).absolute()


def get_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        "mypy_boto3_builder", description="Builder for mypy-boto3."
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Show debug messages"
    )
    parser.add_argument(
        "-v", "--version", action="store_true", help="Show package version"
    )
    parser.add_argument(
        "-f", "--format", action="store_true", help="Format output with black"
    )
    parser.add_argument(
        "-m", "--module-name", help="Output module name", default="mypy_boto3"
    )
    parser.add_argument("--with-docs", action="store_true", help="Add boto3 docs")
    parser.add_argument(
        "output", metavar="OUTPUT_PATH", help="Output path", type=absolute_path
    )
    parser.add_argument(
        "-s",
        "--services",
        nargs="*",
        metavar="SERVICE_NAME",
        help="List of AWS services, use `all` to cover all",
        default=["all"],
    )
    return parser


def main() -> None:
    parser = get_cli_parser()
    args = parser.parse_args()
    if args.version:
        print(version)
        return

    logger = get_logger(verbose=args.debug)
    session = Session()
    available_services = session.get_available_services()

    selected_services: List[str] = []
    for service_name in args.services:
        if service_name == "all":
            selected_services.extend(available_services)
            continue
        if service_name not in available_services:
            raise ValueError(f"Unknown service: {service_name}")

        selected_services.append(service_name)

    args.services = selected_services

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
                    logger.debug(f"Reformatted {source_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
