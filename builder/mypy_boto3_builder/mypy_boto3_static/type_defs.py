from typing_extensions import TypedDict

# ec2 type defs


class _EC2Tag(TypedDict):
    Key: str


class EC2Tag(_EC2Tag, total=False):
    Value: str


# s3 type defs


class _S3CopySource(TypedDict):
    Bucket: str
    Key: str


class S3CopySource(_S3CopySource, total=False):
    VersionId: str
