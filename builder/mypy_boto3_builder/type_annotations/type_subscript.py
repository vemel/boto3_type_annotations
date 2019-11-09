from typing import Set, Iterable

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeSubscript(FakeAnnotation):
    def __init__(
        self, parent: FakeAnnotation, children: Iterable[FakeAnnotation] = (),
    ) -> None:
        self.parent = parent
        self.children = children

    def __hash__(self) -> int:
        return hash(f"{self.parent}.{self.children}")

    def render(self) -> str:
        if not self.children:
            return f"{self.parent.render()}"

        children = ", ".join([i.render() for i in self.children])
        return f"{self.parent.render()}[{children}]"

    def get_import_record(self) -> ImportRecord:
        return self.parent.get_import_record()

    def get_types(self) -> Set[FakeAnnotation]:
        result = self.parent.get_types()
        for child in self.children:
            result.update(child.get_types())
        return result
