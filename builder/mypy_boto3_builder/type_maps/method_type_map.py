"""
String to type annotation map that find type annotation by method and argument name.
"""
from typing import Dict, List

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_def import TypeDef


METHOD_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "page_size: count": TypeClass(int),
    "limit: count": TypeClass(int),
    "create_tags: Resources": TypeSubscript(List, [TypeAnnotation.Any()]),
    "create_tags: Tags": TypeSubscript(List, [TypeDef("EC2Tag")]),
    "create_tags: DryRun": TypeClass(bool),
}
