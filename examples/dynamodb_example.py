# install `pip install boto3-stubs[dynamodb]`

import boto3
from mypy_boto3.dynamodb import Client


def dynamodb_client_example() -> None:
    client: Client = boto3.client("dynamodb")
    try:
        client.list_backups(TableName=123)
    except client.exceptions.BackupInUseException as e:
        print(e)


def main() -> None:
    dynamodb_client_example()


if __name__ == "__main__":
    main()
