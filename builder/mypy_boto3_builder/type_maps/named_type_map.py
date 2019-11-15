from typing import List, Union, Dict

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_def import TypeDef


NAMED_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "DryRun: bool": TypeAnnotation(False),
    "Tags: dict": TypeSubscript(TypeAnnotation(List), [TypeDef("EC2Tag")]),
    "Tags: list": TypeSubscript(TypeAnnotation(List), [TypeDef("EC2Tag")]),
    "CopySource: dict": TypeDef("S3CopySource"),
    "CopySource: str or dict": TypeSubscript(
        TypeAnnotation(Union), [TypeDef("S3CopySource"), TypeAnnotation(str)]
    ),
}
