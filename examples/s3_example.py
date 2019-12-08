# install `pip install boto3-stubs[s3]`

import boto3


def s3_resource_example() -> None:
    # optionally use Session type from botocore
    session = boto3.session.Session(region_name="us-west-1")

    resource = session.resource("s3")
    _resource = boto3.resource("s3")

    # IDE autocomplete suggests function name and arguments here
    bucket = resource.Bucket("bucket")

    # (mypy) error: Unexpected keyword argument "key" for "upload_file" of "Bucket"
    bucket.upload_file(Filename="my.txt", key="my-txt")

    # (mypy) error: Extra key 'key' for TypedDict "S3CopySource"
    bucket.copy({"Bucket": "bucket", "key": "my-txt"}, "new-my-txt")


def s3_client_example() -> None:
    # equivalent of `boto3.client('s3')`
    client = boto3.client("s3")

    bucket_exists_waiter = client.get_waiter("bucket_exists")

    # (mypy) error: Unexpected keyword argument "bucket" for "wait" of "BucketExistsWaiter"
    bucket_exists_waiter.wait(bucket="bucket")

    # IDE autocomplete suggests function name and arguments here
    client.create_bucket(Bucket="bucket")

    # (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
    client.get_object(Bucket="bucket")

    # (mypy) error: TypedDict "GetObjectOutputTypeDef" has no key 'expiration'
    _expiration = client.get_object(Bucket="bucket", Key="key")["expiration"]

    # (mypy) error: Extra key 'Allowedorigins' for TypedDict "CORSRuleTypeDef"
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
