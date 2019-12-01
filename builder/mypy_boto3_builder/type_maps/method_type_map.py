"""
String to type annotation map that find type annotation by method and argument name.
"""
from typing import Dict

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_def import TypeDef


METHOD_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "page_size: count": Type.int,
    "limit: count": Type.int,
    "create_tags: Resources": TypeSubscript(Type.List, [Type.Any]),
    "create_tags: Tags": TypeSubscript(Type.List, [TypeDef("EC2Tag")]),
    "create_tags: DryRun": Type.bool,
}
