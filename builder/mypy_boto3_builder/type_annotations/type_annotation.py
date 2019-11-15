"""
Wrapper for simple type annotation like `str` or `Dict`.
"""
from __future__ import annotations

import inspect
from typing import Union, Optional, Any, Dict, List

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeAnnotation(FakeAnnotation):
    """
    Wrapper for simple type annotation like `str` or `Dict`.

    Arguments:
        wrapped_type -- Original type annotation.
    """

    def __init__(self, wrapped_type: Any) -> None:
        if isinstance(wrapped_type, FakeAnnotation):
            raise ValueError(f"Cannot wrap FakeAnnotation: {wrapped_type}")

        self.wrapped_type = wrapped_type

    def render(self) -> str:
        type_annotation = self.wrapped_type
        if isinstance(type_annotation, str):
            return type_annotation
        if isinstance(type_annotation, bool):
            return str(type_annotation)

        name = str(type_annotation)
        if hasattr(type_annotation, "_name"):
            name = getattr(type_annotation, "_name") or "Union"
        if getattr(type_annotation, "__name__", None):
            name = getattr(type_annotation, "__name__")
        if type_annotation == Union:
            name = "Union"
        if type_annotation == Optional:
            name = "Optional"
        if type_annotation == Ellipsis:
            name = "..."
        if name == "NoneType":
            name = "None"

        return name

    def get_import_record(self) -> ImportRecord:
        module = inspect.getmodule(self.wrapped_type)
        source = module.__name__ if module else "builtins"
        return ImportRecord(source=source, name=self.render(),)

    def is_dict(self) -> bool:
        return self.wrapped_type == Dict

    def is_list(self) -> bool:
        return self.wrapped_type == List

    def copy(self) -> TypeAnnotation:
        return TypeAnnotation(self.wrapped_type)
