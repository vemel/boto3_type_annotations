"""
String to type annotation map that find type annotation by argument name and type.
"""
from typing import Dict

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_maps.typed_dicts import s3_copy_source_type, ec2_tag_type


ARGUMENT_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "DryRun: bool": TypeConstant(False),
    "Tags: dict": TypeSubscript(Type.List, [ec2_tag_type]),
    "Tags: list": TypeSubscript(Type.List, [ec2_tag_type]),
    "CopySource: dict": s3_copy_source_type,
    "CopySource: str or dict": TypeSubscript(
        Type.Union, [s3_copy_source_type, Type.str]
    ),
}
