from __future__ import annotations

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class InternalImport(FakeAnnotation):
    def __init__(
        self,
        name: str,
        service_name: ServiceName,
        module_name: str = "service_resource",
    ) -> None:
        self.name = name
        self.service_name = service_name
        self.module_name = module_name

    def render(self) -> str:
        return f"{self.scope}.{self.name}"

    @property
    def scope(self) -> str:
        return f"{self.module_name}_scope"

    def get_import_record(self) -> ImportRecord:
        return ImportRecord(
            source=f"{self.service_name.module_name}.{self.module_name}",
            alias=self.scope,
        )

    def copy(self) -> InternalImport:
        return InternalImport(self.name, self.service_name, self.module_name)
