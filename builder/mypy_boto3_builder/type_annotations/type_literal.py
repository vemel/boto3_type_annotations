"""
Wrapper for `Literal` type annotations like `Literal['a', 'b']`
"""
from __future__ import annotations

from typing import Any

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeLiteral(FakeAnnotation):
    """
    Wrapper for `Literal` type annotations like `Literal['a', 'b']`

    Arguments:
        children -- Literal values.
    """

    def __init__(self, *children: Any) -> None:
        if not children:
            raise ValueError(f"Empty children for literal: {children}")
        self.children = children

    def render(self) -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        children = ", ".join([repr(i) for i in self.children])
        return f"Literal[{children}]"

    def get_import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """
        return ImportRecord(source=ImportString("typing_extensions"), name="Literal")

    def copy(self) -> TypeLiteral:
        """
        Create a copy of type annotation wrapper.
        """
        return TypeLiteral(*self.children)
