from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Set, Optional, Iterable, Dict

from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_record_group import ImportRecordGroup
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.structures.waiter import Waiter
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.client import Client


@dataclass
class ServiceModule:
    service_name: ServiceName
    client: Client
    service_resource: Optional[ServiceResource] = None
    waiters: List[Waiter] = field(default_factory=lambda: [])
    paginators: List[Paginator] = field(default_factory=lambda: [])
    typed_dicts: List[TypeTypedDict] = field(default_factory=lambda: [])

    def extract_typed_dicts(
        self,
        type_annotations: Iterable[FakeAnnotation],
        added: Dict[str, TypeTypedDict],
    ) -> List[TypeTypedDict]:
        result: List[TypeTypedDict] = []
        for type_annotation in sorted(type_annotations):
            if not isinstance(type_annotation, TypeTypedDict):
                continue
            if type_annotation.name in added:
                try:
                    assert added[type_annotation.name].is_same(type_annotation)
                except AssertionError:
                    print(type_annotation.render_class())
                    print(added[type_annotation.name].render_class())
                    raise ValueError(type_annotation.name)
                continue

            added[type_annotation.name] = type_annotation
            result.extend(
                self.extract_typed_dicts(type_annotation.get_children_types(), added)
            )
            result.append(type_annotation)
        return result

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        types.update(self.client.get_types())
        if self.service_resource:
            types.update(self.service_resource.get_types())
        for waiter in self.waiters:
            types.update(waiter.get_types())
        for paginator in self.paginators:
            types.update(paginator.get_types())
        return types

    def get_import_records(self) -> List[ImportRecord]:
        result: List[ImportRecord] = []
        result.extend(self.client.get_import_records())
        if self.service_resource:
            result.extend(self.service_resource.get_import_records())

        result.sort()
        return result

    def get_client_required_import_record_groups(self) -> List[ImportRecordGroup]:
        class_import_records = self.client.get_required_import_records()
        import_records: Set[ImportRecord] = set()
        for import_record in class_import_records:
            import_records.add(
                import_record.get_external(self.service_name.module_name)
            )

        return ImportRecordGroup.from_import_records(import_records)

    def get_service_resource_required_import_record_groups(
        self,
    ) -> List[ImportRecordGroup]:
        if self.service_resource is None:
            return []

        class_import_records = self.service_resource.get_required_import_records()
        import_records: Set[ImportRecord] = set()
        for import_record in class_import_records:
            import_records.add(
                import_record.get_external(self.service_name.module_name)
            )
        return ImportRecordGroup.from_import_records(import_records)

    def get_paginator_required_import_record_groups(self) -> List[ImportRecordGroup]:
        import_records: Set[ImportRecord] = set()
        for paginator in self.paginators:
            for import_record in paginator.get_required_import_records():
                import_records.add(
                    import_record.get_external(self.service_name.module_name)
                )

        return ImportRecordGroup.from_import_records(import_records)

    def get_waiter_required_import_record_groups(self) -> List[ImportRecordGroup]:
        import_records: Set[ImportRecord] = set()
        for waiter in self.waiters:
            for import_record in waiter.get_required_import_records():
                import_records.add(
                    import_record.get_external(self.service_name.module_name)
                )

        return ImportRecordGroup.from_import_records(import_records)

    def get_type_defs_required_import_record_groups(self) -> List[ImportRecordGroup]:
        import_records: Set[ImportRecord] = set()
        import_records.add(ImportRecord(source="typing_extensions", name="TypedDict"))
        for type_dict in self.typed_dicts:
            for type_annotation in type_dict.get_children_types():
                import_record = type_annotation.get_import_record()
                if import_record.is_type_defs():
                    continue
                import_records.add(import_record)

        return ImportRecordGroup.from_import_records(import_records)