# install `pip install boto3-stubs[dynamodb]`

import boto3
from mypy_boto3.dynamodb import DynamoDBClient, DynamoDBServiceResource
from mypy_boto3.dynamodb.service_resource import Table


def dynamodb_client_example() -> None:
    client: DynamoDBClient = boto3.client("dynamodb")
    resource: DynamoDBServiceResource = boto3.resource("dynamodb")

    my_table: Table = resource.Table("my_table")
    print(my_table.name)
    batch_writer = my_table.batch_writer()
    batch_writer.delete_item(Key="123")

    try:
        client.list_backups(TableName=123)
    except client.exceptions.BackupInUseException as e:
        print(e)


def main() -> None:
    dynamodb_client_example()


if __name__ == "__main__":
    main()
