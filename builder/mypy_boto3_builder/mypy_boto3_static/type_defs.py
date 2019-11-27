"""
Provides compatibility between `typing` and `typing_extensions`, defines types
for undocumented methods.
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict, Literal, overload  # pylint: disable=no-name-in-module
else:
    from typing_extensions import TypedDict, Literal, overload


__all__ = (
    "TypedDict",
    "Literal",
    "overload",
    "EC2Tag",
    "S3CopySource",
)


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
