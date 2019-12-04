"""
String to type annotation map that find type annotation by argument name and type.
"""
from typing import Dict

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_typed_dict import (
    TypeTypedDict,
    TypedDictAttribute,
)


s3_copy_source_type = TypeTypedDict(
    "CopySourceTypeDef",
    [
        TypedDictAttribute("Bucket", Type.str, True),
        TypedDictAttribute("Key", Type.str, True),
        TypedDictAttribute("VersionId", Type.str, False),
    ],
)


ec2_tag_type = TypeTypedDict(
    "TagTypeDef",
    [
        TypedDictAttribute("Key", Type.str, True),
        TypedDictAttribute("Value", Type.str, False),
    ],
)


ARGUMENT_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "DryRun: bool": TypeConstant(False),
    "Tags: dict": TypeSubscript(Type.List, [ec2_tag_type]),
    "Tags: list": TypeSubscript(Type.List, [ec2_tag_type]),
    "CopySource: dict": s3_copy_source_type,
    "CopySource: str or dict": TypeSubscript(
        Type.Union, [s3_copy_source_type, Type.str]
    ),
}
