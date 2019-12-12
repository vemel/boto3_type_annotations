# install `pip install boto3-stubs[emr]`

import boto3
from mypy_boto3.emr import Client


def emr_client_example() -> None:
    # equivalent of `boto3.client('s3')`
    client: Client = boto3.client("emr")
    client.cancel_steps("cluster_id", [123])


def main() -> None:
    emr_client_example()


if __name__ == "__main__":
    main()
