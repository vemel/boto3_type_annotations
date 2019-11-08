# mypy_boto3

Mypy-friendly type annotations for boto3.

- [mypy_boto3](#mypyboto3)
  - [Installation](#installation)
    - [Usage](#usage)
    - [How it works](#how-it-works)
    - [Differences from boto3-type-annotations](#differences-from-boto3-type-annotations)
    - [What's next](#whats-next)
    - [Thank you](#thank-you)

## Installation

```bash
# install only `mypy_boto3.s3` for S3 service annotations
pip install mypy-boto3[s3]

# or install multiple services
pip install mypy-boto3[s3][ec2]

# or install S3 service with docs
pip install mypy-boto3[s3-with-docs]

# or install all services
pip install mypy-boto3[all]

# or even install all boto3 services annotations
# WARNING: this will eat ~70 MB of space
pip install mypy-boto3[all-with-docs]
```

### Usage

- Install [mypy](https://github.com/python/mypy) and optionally enable it in your IDE
- Install [boto3](https://github.com/boto/boto3)
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

### Differences from boto3-type-annotations

- Fully type annotated
- `mypy` compatibility
- Generated types for return values and arguments
- Added ServiceResource sub-collections
- Support service-specific sub-modules (in progress)
- CLI interface for `builder`
- Modules documentation

### What's next

- Add `TypedDict` types for arguments and return types to check keys and values
- Allow installation of sub-modules
- Always include docs and support them in generated documentation

### Thank you

- Guys behind [boto3-type-annotations](https://pypi.org/project/boto3-type-annotations/),
  this package is based on top of their work
- [black](https://github.com/psf/black) developers for awesome formatting tool
- [mypy](https://github.com/python/mypy) for doing all dirty work for us
