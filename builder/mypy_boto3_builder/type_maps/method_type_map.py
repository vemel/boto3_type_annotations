"""
String to type annotation map that find type annotation by method and argument name.
"""
from typing import Dict

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_class import TypeClass


METHOD_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "page_size: count": TypeClass(int),
    "limit: count": TypeClass(int),
}
