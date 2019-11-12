from typing import Iterable, List
from typing_extensions import TypedDict

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.structures import ClassRecord, Attribute


class TypeTypedDict(FakeAnnotation):
    def __init__(
        self,
        name: str,
        attributes: Iterable[Attribute],
        optional: Iterable[Attribute] = (),
    ) -> None:
        self.name = name
        self.attributes = list(attributes)
        self.optional = list(optional)

    def render(self) -> str:
        return self.name

    def get_import_record(self) -> ImportRecord:
        return ImportRecord(source="typing_extensions", name="TypedDict")

    def get_classes(self) -> List[ClassRecord]:
        if not self.optional:
            return [
                ClassRecord(
                    self.name,
                    bases=[TypeAnnotation(TypedDict)],
                    attributes=self.attributes,
                )
            ]

        return [
            ClassRecord(
                f"_{self.name}",
                bases=[TypeAnnotation(TypedDict)],
                attributes=self.attributes,
            ),
            ClassRecord(
                self.name,
                bases=[TypeAnnotation(f"_{self.name}")],
                attributes=self.optional,
            ),
        ]
