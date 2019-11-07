import argparse
from pathlib import Path

import yaml
from boto3.session import Session
import black

from structures import Config
from writers import write_services
from version import __version__ as version
from logger import get_logger


ROOT_PATH = Path(__file__).absolute().parent.parent


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
        "config",
        nargs="?",
        metavar="PATH",
        help="Path to config file",
        default=Path(__file__).parent.parent / "configs" / "main.yaml",
    )
    return parser


def load(path: Path, session_: Session) -> Config:
    file_contents = yaml.safe_load(path.open())
    available_services = session_.get_available_services()
    if file_contents.get("services") == "all":
        file_contents["services"] = available_services
    for service in file_contents.get("services"):
        if service not in available_services:
            raise ValueError(f"Unknown service name: {service}")

    return Config(
        file_contents.get("services", available_services),
        file_contents.get("with_docs", False),
        file_contents.get("with_clients", True),
        file_contents.get("with_service_resources", True),
        file_contents.get("with_paginators", True),
        file_contents.get("with_waiters", True),
        file_contents.get("package_name", "mypy_boto3"),
        file_contents.get("module_name", "mypy_boto3"),
    )


def main():
    parser = get_cli_parser()
    args = parser.parse_args()
    if args.version:
        print(version)
        return

    logger = get_logger(verbose=args.debug)
    session = Session()
    config = load(args.config, session)
    write_services(session, config)

    module_path = ROOT_PATH / config.package_name / config.module_name

    logger.info("Applying black formatting")
    for service_name in config.services:
        service_path = module_path / service_name
        for source_path in service_path.glob("**/*.py"):
            black_result = black.format_file_in_place(
                source_path,
                fast=False,
                mode=black.FileMode(),
                write_back=black.WriteBack.YES,
            )
            if black_result:
                logger.debug(f"Reformatted {source_path.relative_to(ROOT_PATH)}")


if __name__ == "__main__":
    main()
