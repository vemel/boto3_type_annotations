from __future__ import annotations

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class ExternalImport(FakeAnnotation):
    def __init__(self, source: str, name: str = "", alias: str = "") -> None:
        self.source = source
        self.name = name
        self.alias = alias
        self.import_record = ImportRecord(source=source, name=name, alias=alias)

    def render(self) -> str:
        return self.import_record.get_local_name()

    def get_import_record(self) -> ImportRecord:
        return self.import_record

    def copy(self) -> ExternalImport:
        return ExternalImport(self.source, self.name, self.alias)
