from __future__ import annotations

from typing import Iterable, Set

from mypy_boto3_builder.constants import TYPE_DEFS_NAME
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypedDictAttribute:
    def __init__(self, name: str, type_annotation: FakeAnnotation, required: bool):
        self.name = name
        self.type_annotation = type_annotation
        self.required = required

    def render(self) -> str:
        return f"{self.name}: {self.type_annotation.render()}"


class TypeTypedDict(FakeAnnotation):
    def __init__(self, name: str, children: Iterable[TypedDictAttribute] = ()) -> None:
        self.name = name
        self.children = list(children)

    def render(self) -> str:
        return f"{TYPE_DEFS_NAME}.{self.name}"

    def get_import_record(self) -> ImportRecord:
        return ImportRecord(source=TYPE_DEFS_NAME)

    def get_types(self) -> Set[FakeAnnotation]:
        return {self}

    def add_attribute(
        self, name: str, type_annotation: FakeAnnotation, required: bool
    ) -> None:
        self.children.append(TypedDictAttribute(name, type_annotation, required))

    def is_dict(self) -> bool:
        return True

    def render_class(self) -> str:
        children = "\n".join([f"     {i.render()}" for i in self.children])
        return f"class {self.name}:\n{children}"

    def has_optional(self) -> bool:
        for child in self.children:
            if not child.required:
                return True
        return False

    def has_required(self) -> bool:
        for child in self.children:
            if child.required:
                return True
        return False

    def copy(self) -> TypeTypedDict:
        return TypeTypedDict(self.name, list(self.children))
