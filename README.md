# mypy_boto3

Mypy-friendly type annotations for boto3.

- [mypy_boto3](#mypyboto3)
  - [Installation](#installation)
    - [Usage](#usage)
    - [How it works](#how-it-works)
    - [Thank you](#thank-you)

## Installation

```bash
pip install mypy-boto3
```

### Usage

- Install [mypy](https://github.com/python/mypy) and optionally enable it in your IDE
- Use `mypy-boto3` to annotate your code to discover errors

    ```python
    import boto3

    from mypy_boto3.s3 import Client, ServiceResource

    client: Client = boto3.client("s3")

    # IDE autocomplete suggests function name and arguemnts here
    client.create_bucket(Bucket="bucket")

    # (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
    client.get_object(Bucket="bucket")

    # (mypy) error: Argument "Key" to "get_object" of "Client" has incompatible type "None"; expected "str"
    client.get_object(Bucket="bucket", Key=None)

    # explicitly set type to S3 ServiceResource
    resource: ServiceResource = boto3.Session(region_name="us-west-1").resource("s3")

    # IDE autocomplete suggests function name and arguments here
    bucket = resource.Bucket("bucket")

    # (mypy) error: Unexpected keyword argument "key" for "upload_file" of "Bucket"
    bucket.upload_file(Filename="my.txt", key="my-txt")
    ```

### How it works

There is also a package `mypy-boto3-builder` that builds interface files from `boto3` documentation.

### Thank you

- Guys behind [boto3-type-annotations](https://pypi.org/project/boto3-type-annotations/),
  this package is based on top of their work
- [black](https://github.com/psf/black) developers for awesome formatting tool
- [mypy](https://github.com/python/mypy) for doing all dirty work for us
