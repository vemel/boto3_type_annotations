"""
String to type annotation map that find type annotation by method and argument name.
"""
from typing import Dict

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation


METHOD_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "page_size: count": TypeAnnotation(int),
    "limit: count": TypeAnnotation(int),
}
