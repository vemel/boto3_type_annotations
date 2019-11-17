"""
Boto3 Client.
"""
from dataclasses import dataclass, field
from typing import List, Set

from botocore.client import BaseClient

from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.structures.class_record import ClassRecord


@dataclass
class Client(ClassRecord):
    """
    Boto3 Client.
    """

    name: str = "Client"
    service_name: ServiceName = ServiceName.ec2
    boto3_client: BaseClient = None
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [
            ExternalImport(source="botocore.client", name="BaseClient",)
        ]
    )

    def __hash__(self) -> int:
        return hash(self.service_name)

    def get_import_records(self) -> Set[ImportRecord]:
        source = f"{self.service_name.module_name}.client"
        return {ImportRecord(source, "Client")}

    def get_all_names(self) -> List[str]:
        return [self.name]
