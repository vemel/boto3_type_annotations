from typing import Optional

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.constants import MODULE_NAME
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class InternalImport(FakeAnnotation):
    is_internal = True

    def __init__(
        self,
        name: str,
        service_name: ServiceName,
        module_name: str = "service_resource",
    ) -> None:
        self.name = name
        self.service_name = service_name
        self.module_name = module_name
        self.real_service_name: Optional[ServiceName] = None

    def render(self) -> str:
        return f"{self.scope}.{self.name}"

    @property
    def scope(self) -> str:
        return f"{self.service_name.module_name}_scope"

    def localize(self, service_name: ServiceName) -> None:
        self.real_service_name = service_name

    def get_import_record(self) -> ImportRecord:
        if self.real_service_name is None:
            raise ValueError("Non-localized ImportString")

        return ImportRecord(
            source=f"{MODULE_NAME}_{self.real_service_name.name}.{self.module_name}",
            alias=self.scope,
        )
