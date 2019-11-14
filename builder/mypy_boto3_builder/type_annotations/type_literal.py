from __future__ import annotations

from typing_extensions import Literal

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation


class TypeLiteral(FakeAnnotation):
    def __init__(self, *children: str) -> None:
        self.parent = TypeAnnotation(Literal)
        self.children = children

    def render(self) -> str:
        children = ", ".join([repr(i) for i in self.children])
        return f"{self.parent.render()}[{children}]"

    def get_import_record(self) -> ImportRecord:
        return self.parent.get_import_record()

    def copy(self) -> TypeLiteral:
        return TypeLiteral(*self.children)
