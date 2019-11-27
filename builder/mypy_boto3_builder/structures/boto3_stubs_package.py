"""
Structure for boto3-stubs module.
"""

from dataclasses import dataclass, field
from typing import List, Set

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_record_group import ImportRecordGroup
from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.constants import BOTO3_STUBS_NAME, MODULE_NAME, TYPE_DEFS_NAME
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.method import Method


@dataclass
class Boto3StubsPackage(Package):
    """
    Structure for boto3-stubs module.
    """

    name: str = BOTO3_STUBS_NAME
    pypi_name: str = BOTO3_STUBS_NAME
    service_names: List[ServiceName] = field(default_factory=lambda: [])
    service_packages: List[ServicePackage] = field(default_factory=lambda: [])
    init_functions: List[Function] = field(default_factory=lambda: [])
    session_methods: List[Method] = field(default_factory=lambda: [])

    MASTER_IMPORT_STRING = ImportString(MODULE_NAME)
    MASTER_TYPE_DEFS_IMPORT_STRING = ImportString(MODULE_NAME, TYPE_DEFS_NAME)

    @property
    def essential_service_names(self) -> List[ServiceName]:
        result: List[ServiceName] = []
        for service_name in self.service_names:
            if service_name.is_essential():
                result.append(service_name)
        return result

    def get_init_required_import_record_groups(self) -> List[ImportRecordGroup]:
        import_records: Set[ImportRecord] = {
            ImportRecord(ImportString("logging")),
            ImportRecord(ImportString("typing"), "Optional"),
            ImportRecord(ImportString("typing"), "Any"),
            ImportRecord(ImportString("typing"), "Union"),
            ImportRecord(ImportString("boto3", "session")),
            ImportRecord(ImportString("boto3", "session"), "Session"),
            ImportRecord(ImportString("botocore", "client"), "Client"),
            ImportRecord(ImportString("botocore", "config"), "Config"),
            ImportRecord(
                ImportString("botocore", "service_resource"), "ServiceResource"
            ),
        }
        for init_function in self.init_functions:
            for import_record in init_function.get_required_import_records():
                if import_record.source.startswith(self.MASTER_IMPORT_STRING):
                    if not import_record.source.startswith(
                        self.MASTER_TYPE_DEFS_IMPORT_STRING
                    ):
                        import_record.safe = True
                import_records.add(import_record)

        return ImportRecordGroup.from_import_records(import_records)

    def get_session_required_import_record_groups(self) -> List[ImportRecordGroup]:
        import_records: Set[ImportRecord] = {
            ImportRecord(ImportString("typing"), "List"),
            ImportRecord(ImportString("typing"), "Any"),
            ImportRecord(ImportString("typing"), "Union"),
            ImportRecord(ImportString("boto3")),
            ImportRecord(ImportString("boto3", "utils")),
            ImportRecord(ImportString("boto3", "exceptions"), "ResourceNotExistsError"),
            ImportRecord(ImportString("boto3", "exceptions"), "UnknownAPIVersionError"),
            ImportRecord(
                ImportString("boto3", "resources", "factory"), "ResourceFactory"
            ),
            ImportRecord(ImportString("botocore", "credentials"), "Credentials"),
            ImportRecord(ImportString("botocore", "config"), "Config"),
            ImportRecord(ImportString("botocore", "waiter"), "Waiter"),
            ImportRecord(ImportString("botocore", "loaders"), "Loader"),
            ImportRecord(ImportString("botocore", "model"), "ServiceModel"),
            ImportRecord(ImportString("botocore", "client"), "BaseClient"),
            ImportRecord(ImportString("boto3", "resources", "base"), "ServiceResource"),
        }

        for session_method in self.session_methods:
            for import_record in session_method.get_required_import_records():
                if import_record.source.startswith(self.MASTER_IMPORT_STRING):
                    if not import_record.source.startswith(
                        self.MASTER_TYPE_DEFS_IMPORT_STRING
                    ):
                        import_record.safe = True
                import_records.add(import_record)

        return ImportRecordGroup.from_import_records(import_records)
