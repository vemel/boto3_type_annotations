"""
String to type annotation map that find type annotation in botocore syntax
"""
from typing import Dict, IO

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation


SYNTAX_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "'string'": TypeClass(str),
    "b'bytes'": TypeClass(bytes),
    "123": TypeClass(int),
    "123.0": TypeClass(float),
    "123.4": TypeClass(float),
    "None": TypeConstant(None),
    "True": TypeClass(bool),
    "False": TypeClass(bool),
    "file": TypeAnnotation(IO),
}
