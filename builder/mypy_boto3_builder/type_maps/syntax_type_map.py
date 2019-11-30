"""
String to type annotation map that find type annotation in botocore syntax
"""
from typing import Dict

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_class import TypeClass


SYNTAX_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "'string'": TypeClass(str),
    "b'bytes'": TypeClass(bytes),
    "123": TypeClass(int),
    "123.0": TypeClass(float),
}
