"""
String to type annotation map that find type annotation in botocore syntax
"""
from typing import Dict, Union, IO

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


SYNTAX_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "{'... recursive ...'}": TypeSubscript(
        Dict, [TypeClass(str), TypeAnnotation.Any()]
    ),
    "'string'": TypeClass(str),
    "b'bytes'": TypeClass(bytes),
    "True|False": TypeClass(bool),
    "b'bytes'|file": TypeSubscript(Union, [TypeClass(bytes), TypeAnnotation(IO)]),
}
