"""
Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`
"""
from __future__ import annotations

from typing import Any

from mypy_boto3_builder.type_annotations.type_def import TypeDef
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeLiteral(FakeAnnotation):
    """
    Wrapper for `typing/typing_extensions.Literal` type annotations like `Literal['a', 'b']`

    Arguments:
        children -- Literal values.
    """

    def __init__(self, *children: Any) -> None:
        self.children = list(children)

    def render(self) -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if not self.children:
            raise ValueError(f"Empty children for literal")
        children = ", ".join([repr(i) for i in self.children])
        return f"Literal[{children}]"

    def get_import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """
        return TypeDef("Literal").get_import_record()

    def copy(self) -> TypeLiteral:
        """
        Create a copy of type annotation wrapper.
        """
        return TypeLiteral(*self.children)

    def is_literal(self) -> bool:  # pylint: disable=no-self-use
        """
        Whether type annotation is `Literal`.
        """
        return True

    def add_child(self, child: FakeAnnotation) -> None:
        raise ValueError("Use add_literal_child function.")

    def add_literal_child(self, child: Any) -> None:
        """
        Add new child to `TypeLiteral` annotation.
        """
        self.children.append(child)
