"""
Wrapper for simple type annotation like `str` or `Dict`.
"""
from __future__ import annotations

from typing import Union, Optional, Any, Dict, List, Callable, IO

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeAnnotation(FakeAnnotation):
    """
    Wrapper for simple type annotation like `str` or `Dict`.

    Arguments:
        wrapped_type -- Original type annotation.
    """

    supported_types = [
        Union,
        Any,
        Dict,
        List,
        Optional,
        Callable,
        IO,
    ]

    def __init__(self, wrapped_type: Any) -> None:
        if isinstance(wrapped_type, FakeAnnotation):
            raise ValueError(f"Cannot wrap FakeAnnotation: {wrapped_type}")
        if wrapped_type not in self.supported_types:
            raise ValueError(f"Cannot wrap {wrapped_type}")

        self.wrapped_type = wrapped_type

    def render(self) -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        return self.get_import_name()

    def get_import_name(self) -> str:
        if self.wrapped_type == IO:
            return "IO"
        if self.wrapped_type == Callable:
            return "Callable"
        return getattr(self.wrapped_type, "_name", "Any")

    def get_import_record(self) -> ImportRecord:
        return ImportRecord(source="typing", name=self.get_import_name())

    def is_dict(self) -> bool:
        return self.wrapped_type == Dict

    def is_list(self) -> bool:
        return self.wrapped_type == List

    def copy(self) -> TypeAnnotation:
        """
        Create a copy of type annotation wrapper.
        """
        return TypeAnnotation(self.wrapped_type)
