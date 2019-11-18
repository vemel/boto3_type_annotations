"""
String to type annotation map that find type annotation by argument name and type.
"""
from typing import List, Union, Dict

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_def import TypeDef


NAMED_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "DryRun: bool": TypeConstant(False),
    "Tags: dict": TypeSubscript(List, [TypeDef("EC2Tag")]),
    "Tags: list": TypeSubscript(List, [TypeDef("EC2Tag")]),
    "CopySource: dict": TypeDef("S3CopySource"),
    "CopySource: str or dict": TypeSubscript(
        Union, [TypeDef("S3CopySource"), TypeClass(str)]
    ),
}
