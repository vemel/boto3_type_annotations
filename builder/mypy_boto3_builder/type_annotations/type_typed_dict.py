from __future__ import annotations

from typing import Iterable, Set, List

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
    def __init__(
        self,
        name: str,
        children: Iterable[TypedDictAttribute] = (),
        docstring: str = "",
    ) -> None:
        self.name = name
        self.children = list(children)
        self.docstring = docstring

    def render(self) -> str:
        return self.name

    def get_import_record(self) -> ImportRecord:
        return ImportRecord(source=TYPE_DEFS_NAME, name=self.name)

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

    def has_both(self) -> bool:
        return self.has_required() and self.has_optional()

    def get_required(self) -> List[TypedDictAttribute]:
        result: List[TypedDictAttribute] = []
        for child in self.children:
            if child.required:
                result.append(child)
        return result

    def get_optional(self) -> List[TypedDictAttribute]:
        result: List[TypedDictAttribute] = []
        for child in self.children:
            if not child.required:
                result.append(child)
        return result

    def copy(self) -> TypeTypedDict:
        return TypeTypedDict(self.name, list(self.children), docstring=self.docstring)

    def is_same(self, other: TypeTypedDict) -> bool:
        children = [i.render() for i in self.children]
        other_children = [i.render() for i in other.children]
        return other_children == children

    def get_children_types(self) -> Set[FakeAnnotation]:
        result: Set[FakeAnnotation] = set()
        for child in self.children:
            result.update(child.type_annotation.get_types())
        return result
