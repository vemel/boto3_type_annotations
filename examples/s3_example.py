# install `pip install boto3-stubs[s3]`

import boto3

from mypy_boto3 import s3
import mypy_boto3.s3.helpers as s3_helpers


def s3_resource_example() -> None:
    # optionally use Session type from botocore
    session = boto3.session.Session(region_name="us-west-1")

    resource: s3.ServiceResource = session.resource("s3")

    # IDE autocomplete suggests function name and arguments here
    bucket = resource.Bucket("bucket")

    # (mypy) error: Unexpected keyword argument "key" for "upload_file" of "Bucket"
    bucket.upload_file(Filename="my.txt", key="my-txt")

    # (mypy) error: Extra key 'key' for TypedDict "S3CopySource"
    bucket.copy({"Bucket": "bucket", "key": "my-txt"}, "new-my-txt")


def s3_client_example() -> None:
    # equivalent of `boto3.client('s3')`
    client: s3.Client = boto3.client("s3")

    bucket_exists_waiter: s3.BucketExistsWaiter = client.get_waiter("bucket_exists")

    # (mypy) error: Unexpected keyword argument "bucket" for "wait" of "BucketExistsWaiter"
    bucket_exists_waiter.wait(bucket="bucket")

    # IDE autocomplete suggests function name and arguments here
    client.create_bucket(Bucket="bucket")

    # (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
    client.get_object(Bucket="bucket")

    # (mypy) error: TypedDict "ClientGetObjectResponseTypeDef" has no key 'expiration'
    _expiration = client.get_object(Bucket="bucket", Key="key")["expiration"]

    # (mypy) error: Extra key 'Allowedorigins' for TypedDict "ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef"
    client.put_bucket_cors(
        "Bucket",
        {"CORSRules": [{"AllowedMethods": ["get"], "Allowedorigins": ["localhost"]}]},
    )

    # (mypy) error: Argument "Key" to "get_object" of "Client" has incompatible type "None"; expected "str"
    client.get_object(Bucket="bucket", Key=None)


def helpers_example() -> None:
    session = boto3.session.Session(region_name="us-west-1")

    # equivalent of `boto3.client('s3')`
    client = s3_helpers.boto3_client()
    resource = s3_helpers.boto3_resource(session)

    _bucket = resource.Bucket("bucket")

    bucket_exists_waiter = s3_helpers.get_bucket_exists_waiter(client)

    # (mypy) error: Unexpected keyword argument "bucket" for "wait" of "BucketExistsWaiter"
    bucket_exists_waiter.wait(bucket="bucket")

    # IDE autocomplete suggests function name and arguments here
    client.create_bucket(Bucket="bucket")

    # (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
    client.get_object(Bucket="bucket")

    # (mypy) error: TypedDict "ClientGetObjectResponseTypeDef" has no key 'expiration'
    _expiration = client.get_object(Bucket="bucket", Key="key")["expiration"]

    # (mypy) error: Extra key 'Allowedorigins' for TypedDict "ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef"
    client.put_bucket_cors(
        "Bucket",
        {"CORSRules": [{"AllowedMethods": ["get"], "Allowedorigins": ["localhost"]}]},
    )

    # (mypy) error: Argument "Key" to "get_object" of "Client" has incompatible type "None"; expected "str"
    client.get_object(Bucket="bucket", Key=None)


def main() -> None:
    s3_resource_example()
    s3_client_example()


if __name__ == "__main__":
    main()
