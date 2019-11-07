from os.path import dirname, abspath
from sys import argv

import yaml
from boto3.session import Session

from structures import Config
from writers import write_services


def load(path: str, session_: Session) -> Config:
    with open(path, "r") as f:
        file_contents = yaml.safe_load(f)
    if file_contents.get("services") == "all":
        file_contents["services"] = session_.get_available_services()
    if not all(
        (
            service in session_.get_available_services()
            for service in file_contents.get("services")
        )
    ):
        raise ValueError("Invalid service name.")
    return Config(
        file_contents.get("services", session_.get_available_services()),
        file_contents.get("with_docs", False),
        file_contents.get("with_clients", True),
        file_contents.get("with_service_resources", True),
        file_contents.get("with_paginators", True),
        file_contents.get("with_waiters", True),
        file_contents.get("package_name", "mypy_boto3"),
        file_contents.get("module_name", "mypy_boto3"),
    )


def main():
    if len(argv) < 2:
        raise ValueError("Missing config path.")
    session = Session()
    write_services(session, load(argv[1], session))


if __name__ == "__main__":
    main()
