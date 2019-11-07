import argparse
from pathlib import Path

import yaml
from boto3.session import Session

from structures import Config
from writers import write_services
from version import __version__ as version
from logger import get_logger


def get_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        "mypy_boto3_builder", description="Builder for mypy-boto3."
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Show debug messages"
    )
    parser.add_argument(
        "-v", "--version", action="store_true", help="Show pacakge version"
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

    get_logger(verbose=args.debug)
    session = Session()
    write_services(session, load(args.config, session))


if __name__ == "__main__":
    main()
