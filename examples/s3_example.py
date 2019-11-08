import boto3

from botocore.session import Session
from mypy_boto3.s3 import Client, ServiceResource


def s3_resource_example() -> None:
    # optionally use Session type from botocore
    session: Session = boto3.Session(region_name="us-west-1")

    # explicitly set type to S3 ServiceResource
    resource: ServiceResource = session.resource("s3")

    # IDE autocomplete suggests function name and arguments here
    bucket = resource.Bucket("bucket")

    # (mypy) error: Unexpected keyword argument "key" for "upload_file" of "Bucket"
    bucket.upload_file(Filename="my.txt", key="my-txt")

    # TODO: add TypedDict support to check key names
    bucket.copy({"Bucket": "bucket", "key": "my-txt"}, "new-my-txt")


def s3_client_example() -> None:
    # explicitly set type to S3 Client
    client: Client = boto3.client("s3")

    # IDE autocomplete suggests function name and arguemnts here
    client.create_bucket(Bucket="bucket")

    # (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
    client.get_object(Bucket="bucket")

    # (mypy) error: Argument "Key" to "get_object" of "Client" has incompatible type "None"; expected "str"
    client.get_object(Bucket="bucket", Key=None)


def main() -> None:
    s3_resource_example()
    s3_client_example()


if __name__ == "__main__":
    main()
