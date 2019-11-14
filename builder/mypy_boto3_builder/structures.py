from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Set, Optional, Any, Iterable, Dict
from typing_extensions import TypedDict

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from botocore.client import BaseClient
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.constants import MODULE_NAME, BOTO3_STUBS_NAME, PYPI_NAME
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_record_group import ImportRecordGroup
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict


@dataclass
class Attribute:
    name: str
    type: FakeAnnotation
    value: FakeAnnotation = TypeAnnotation(None)

    def get_types(self) -> Set[FakeAnnotation]:
        return self.type.get_types()

    def render(self) -> str:
        return f"{self.name}: {self.type.render()}"


@dataclass
class Argument:
    name: str
    type: Optional[FakeAnnotation] = None
    default: Optional[FakeAnnotation] = None
    prefix: str = ""

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        if self.type is not None:
            types.update(self.type.get_types())
        if self.default is not None:
            types.update(self.default.get_types())

        return types


@dataclass
class Function:
    name: str
    arguments: List[Argument]
    docstring: str
    return_type: FakeAnnotation
    decorators: List[FakeAnnotation] = field(default_factory=lambda: [])
    body: str = "pass"

    def get_types(self) -> Set[FakeAnnotation]:
        types = self.return_type.get_types()
        for argument in self.arguments:
            types.update(argument.get_types())

        return types


@dataclass
class Method(Function):
    pass


@dataclass
class ClassRecord:
    name: str
    methods: List[Method] = field(default_factory=lambda: [])
    attributes: List[Attribute] = field(default_factory=lambda: [])
    bases: List[FakeAnnotation] = field(default_factory=lambda: [])
    docstring: str = ""

    @classmethod
    def from_typed_dict(cls, typed_dict: TypeTypedDict) -> List[ClassRecord]:
        result: List[ClassRecord] = []
        if typed_dict.has_optional() and typed_dict.has_required():
            class_record = ClassRecord(
                name=f"_{typed_dict.name}",
                bases=[TypeAnnotation(TypedDict)],
                docstring=typed_dict.docstring,
            )
            for attribute in typed_dict.children:
                if attribute.required:
                    class_record.attributes.append(
                        Attribute(attribute.name, attribute.type_annotation)
                    )
            result.append(class_record)
            optional_class_record = ClassRecord(
                name=typed_dict.name,
                bases=[
                    TypeAnnotation(f"_{typed_dict.name}"),
                    TypeAnnotation(f"total=False"),
                ],
                docstring=typed_dict.docstring,
            )
            for attribute in typed_dict.children:
                if not attribute.required:
                    optional_class_record.attributes.append(
                        Attribute(attribute.name, attribute.type_annotation)
                    )
            result.append(optional_class_record)
            return result

        class_record = ClassRecord(
            name=typed_dict.name,
            bases=[TypeAnnotation(TypedDict),],
            docstring=typed_dict.docstring,
        )
        for attribute in typed_dict.children:
            class_record.attributes.append(
                Attribute(attribute.name, attribute.type_annotation)
            )
        if typed_dict.has_optional():
            class_record.bases.append(TypeAnnotation("total=False"))
        result.append(class_record)
        return result

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        for method in self.methods:
            types.update(method.get_types())
        for attribute in self.attributes:
            types.update(attribute.get_types())
        for base in self.bases:
            types.update(base.get_types())
        return types

    def get_required_import_records(self) -> Set[ImportRecord]:
        result: Set[ImportRecord] = set()
        for type_annotation in self.get_types():
            import_record = type_annotation.get_import_record()
            if import_record.is_builtins():
                continue
            result.add(import_record)

        return result


@dataclass
class Collection(ClassRecord):
    type: FakeAnnotation = TypeAnnotation(Any)
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [
            ExternalImport(
                source="boto3.resources.collection", name="ResourceCollection",
            )
        ]
    )

    def get_types(self) -> Set[FakeAnnotation]:
        types = super().get_types()
        types.update(self.type.get_types())
        return types


@dataclass
class Resource(ClassRecord):
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [
            ExternalImport(
                source="boto3.resources.base",
                name="ServiceResource",
                alias="Boto3ServiceResource",
            )
        ]
    )
    collections: List[Collection] = field(default_factory=lambda: [])

    def get_types(self) -> Set[FakeAnnotation]:
        types = super().get_types()
        for collection in self.collections:
            types.update(collection.get_types())
        return types


@dataclass
class Waiter(ClassRecord):
    boto3_waiter: Boto3Waiter = None
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [
            ExternalImport(
                source="botocore.waiter", name="Waiter", alias="Boto3Waiter",
            )
        ]
    )


@dataclass
class Paginator(ClassRecord):
    boto3_paginator: Boto3Paginator = None
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [
            ExternalImport(
                source="botocore.paginate", name="Paginator", alias="Boto3Paginator",
            )
        ]
    )


@dataclass
class ServiceResource(ClassRecord):
    name: str = "ServiceResource"
    service_name: ServiceName = ServiceName.ec2
    boto3_service_resource: Boto3ServiceResource = None
    collections: List[Collection] = field(default_factory=lambda: [])
    sub_resources: List[Resource] = field(default_factory=lambda: [])
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [
            ExternalImport(
                source="boto3.resources.base",
                name="ServiceResource",
                alias="Boto3ServiceResource",
            )
        ]
    )

    def __hash__(self) -> int:
        return hash(self.service_name)

    def get_types(self) -> Set[FakeAnnotation]:
        types = super().get_types()
        for collection in self.collections:
            types.update(collection.get_types())
        for sub_resource in self.sub_resources:
            types.update(sub_resource.get_types())

        return types

    def get_import_records(self) -> Set[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        source = f"{self.service_name.module_name}.service_resource"

        import_records.add(ImportRecord(source, "ServiceResource"))
        for resource in self.sub_resources:
            import_records.add(ImportRecord(source, resource.name))

        for collection in self.get_collections():
            import_records.add(ImportRecord(source, collection.name))

        return import_records

    def get_collections(self) -> List[Collection]:
        collection_names = [i.name for i in self.collections]
        result = self.collections
        for resource in self.sub_resources:
            for collection in resource.collections:
                if collection.name in collection_names:
                    continue
                collection_names.append(collection.name)
                result.append(collection)

        return result


@dataclass
class Client(ClassRecord):
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


@dataclass
class ServiceModule:
    service_name: ServiceName
    client: Client
    service_resource: Optional[ServiceResource] = None
    waiters: List[Waiter] = field(default_factory=lambda: [])
    paginators: List[Paginator] = field(default_factory=lambda: [])
    type_defs: List[ClassRecord] = field(default_factory=lambda: [])

    def extract_type_defs(
        self, type_annotations: Iterable[FakeAnnotation]
    ) -> List[ClassRecord]:
        result: List[ClassRecord] = []
        added: Dict[str, TypeTypedDict] = {}
        for type_annotation in type_annotations:
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
            class_records = ClassRecord.from_typed_dict(type_annotation)
            for class_record in class_records:
                result.extend(self.extract_type_defs(class_record.get_types()))
            result.extend(class_records)
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
        return ImportRecordGroup.from_import_records(
            self.client.get_required_import_records()
        )

    def get_service_resource_required_import_record_groups(
        self,
    ) -> List[ImportRecordGroup]:
        if self.service_resource is None:
            return []

        return ImportRecordGroup.from_import_records(
            self.service_resource.get_required_import_records()
        )

    def get_paginator_required_import_record_groups(self) -> List[ImportRecordGroup]:
        result: Set[ImportRecord] = set()
        for paginator in self.paginators:
            result.update(paginator.get_required_import_records())

        return ImportRecordGroup.from_import_records(result)

    def get_waiter_required_import_record_groups(self) -> List[ImportRecordGroup]:
        result: Set[ImportRecord] = set()
        for waiter in self.waiters:
            result.update(waiter.get_required_import_records())

        return ImportRecordGroup.from_import_records(result)

    def get_type_defs_required_import_record_groups(self) -> List[ImportRecordGroup]:
        result: Set[ImportRecord] = set()
        for type_def in self.type_defs:
            for import_record in type_def.get_required_import_records():
                if import_record.is_type_defs():
                    continue
                result.add(import_record)

        return ImportRecordGroup.from_import_records(result)


@dataclass
class Boto3Module:
    name: str = BOTO3_STUBS_NAME
    package_name: str = BOTO3_STUBS_NAME
    service_names: List[ServiceName] = field(default_factory=lambda: [])
    service_modules: List[ServiceModule] = field(default_factory=lambda: [])


@dataclass
class MasterModule:
    name: str = PYPI_NAME
    package_name: str = MODULE_NAME
    service_names: List[ServiceName] = field(default_factory=lambda: [])
    service_modules: List[ServiceModule] = field(default_factory=lambda: [])
