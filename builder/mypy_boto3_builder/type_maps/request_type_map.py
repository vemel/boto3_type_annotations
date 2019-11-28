"""
String to type annotation map that find type annotation by argument name and type.
"""
from typing import Dict

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


REQUEST_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "{'... recursive ...'}": TypeSubscript(
        Dict, [TypeClass(str), TypeAnnotation.Any()]
    ),
    "'string'": TypeClass(str),
    "b'bytes'": TypeClass(bytes),
    "True|False": TypeClass(bool),
}
