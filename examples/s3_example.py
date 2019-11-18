# install `pip install boto3-stubs[s3]`

import boto3

from mypy_boto3.s3 import boto3_client, boto3_resource
from mypy_boto3.s3.helpers import get_bucket_exists_waiter


def s3_resource_example() -> None:
    # optionally use Session type from botocore
    session = boto3.session.Session(region_name="us-west-1")

    # explicitly set type to S3 ServiceResource
    resource = boto3_resource(session)

    # IDE autocomplete suggests function name and arguments here
    bucket = resource.Bucket("bucket")

    # (mypy) error: Unexpected keyword argument "key" for "upload_file" of "Bucket"
    bucket.upload_file(Filename="my.txt", key="my-txt")

    # (mypy) error: Extra key 'key' for TypedDict "S3CopySource"
    bucket.copy({"Bucket": "bucket", "key": "my-txt"}, "new-my-txt")


def s3_client_example() -> None:
    # Use explicit types to help Python extension to get methods correctly
    # mypy works as it should even without explicit types
    client = boto3_client()

    bucket_exists_waiter = get_bucket_exists_waiter(client)

    # (mypy) error: Unexpected keyword argument "bucket" for "wait" of "BucketExistsWaiter"
    bucket_exists_waiter.wait(bucket="bucket")

    # IDE autocomplete suggests function name and arguments here
    client.create_bucket(Bucket="bucket")

    # (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
    client.get_object(Bucket="bucket")

    # (mypy) error: TypedDict "ClientGetObjectResponseTypeDef" has no key 'expiration'
    expiration = client.get_object(Bucket="bucket", Key="key")["expiration"]

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
