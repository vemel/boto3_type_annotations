"""
Structures produced by parsers.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Set, Optional, Any, Iterable, Dict
from typing_extensions import overload

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from botocore.client import BaseClient
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.constants import MODULE_NAME, BOTO3_STUBS_NAME, PYPI_NAME
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.internal_import_record import (
    InternalImportRecord,
)
from mypy_boto3_builder.import_helpers.import_record_group import ImportRecordGroup
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.enums import ServiceModuleName


@dataclass
class Attribute:
    """
    Class or module attribute.

    Attributes:
        name -- Attribute name.
        type -- Attribute type annotation.
        value -- Attribute value.
    """

    name: str
    type: FakeAnnotation
    value: FakeAnnotation = TypeConstant(None)

    def get_types(self) -> Set[FakeAnnotation]:
        """
        Return all type annotations used.

        Returns:
            A set of type annotations.
        """
        return self.type.get_types()

    def render(self) -> str:
        """
        Render arguemnt to a string.

        Probably not used.

        Returns:
            A string with rendered attribute.
        """
        return f"{self.name}: {self.type.render()}"


@dataclass
class Argument:
    """
    Method or function argument.

    Attributes:
        name -- Argument name.
        type -- Argument type annotation.
        value -- Default argument value.
        prefix -- Used for starargs.
    """

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
        for decorator in self.decorators:
            types.update(decorator.get_types())

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
            if not import_record:
                continue
            if import_record.is_builtins():
                continue
            result.add(import_record)

        return result


@dataclass
class Collection(ClassRecord):
    attribute_name: str = "collection"
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
    waiter_name: str = "waiter_name"
    boto3_waiter: Boto3Waiter = None
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [TypeClass(Boto3Waiter, alias="Boto3Waiter")]
    )

    def get_import_record(self) -> InternalImportRecord:
        return InternalImportRecord(
            source=ServiceModuleName.waiter.value, name=self.name,
        )

    def get_client_method(self) -> Method:
        return Method(
            name="get_waiter",
            docstring=f"Get Waiter `{self.waiter_name}`.",
            decorators=[TypeClass(overload)],
            arguments=[
                Argument("self"),
                Argument("waiter_name", TypeLiteral(self.waiter_name)),
            ],
            return_type=InternalImport(self.name, module_name=ServiceModuleName.waiter),
        )


@dataclass
class Paginator(ClassRecord):
    operation_name: str = "operation_name"
    boto3_paginator: Boto3Paginator = None
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [TypeClass(Boto3Paginator, alias="Boto3Paginator")]
    )

    def get_import_record(self) -> InternalImportRecord:
        return InternalImportRecord(
            source=ServiceModuleName.paginator.value, name=self.name,
        )

    def get_client_method(self) -> Method:
        return Method(
            name="get_paginator",
            docstring=f"Get Paginator for `{self.operation_name}` operation.",
            decorators=[TypeClass(overload)],
            arguments=[
                Argument("self"),
                Argument("operation_name", TypeLiteral(self.operation_name)),
            ],
            return_type=InternalImport(
                self.name, module_name=ServiceModuleName.paginator
            ),
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

        return import_records

    def get_all_names(self) -> List[str]:
        result = [self.name]
        for resource in self.sub_resources:
            result.append(resource.name)
        for collection in self.get_collections():
            result.append(collection.name)
        return result

    def get_collections(self) -> List[Collection]:
        collection_names = [i.name for i in self.collections]
        result: List[Collection] = []
        result.extend(self.collections)
        for resource in self.sub_resources:
            for collection in resource.collections:
                if collection.name in collection_names:
                    raise ValueError(f"Conflicting collections: {collection.name}")
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

    def get_all_names(self) -> List[str]:
        return [self.name]


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


@dataclass
class Boto3Module:
    name: str = BOTO3_STUBS_NAME
    package_name: str = BOTO3_STUBS_NAME
    service_names: List[ServiceName] = field(default_factory=lambda: [])
    service_modules: List[ServiceModule] = field(default_factory=lambda: [])

    @property
    def essential_service_names(self) -> List[ServiceName]:
        result: List[ServiceName] = []
        for service_name in self.service_names:
            if service_name.is_essential():
                result.append(service_name)
        return result


@dataclass
class MasterModule:
    name: str = PYPI_NAME
    package_name: str = MODULE_NAME
    service_names: List[ServiceName] = field(default_factory=lambda: [])
    service_modules: List[ServiceModule] = field(default_factory=lambda: [])

    @property
    def essential_service_names(self) -> List[ServiceName]:
        result: List[ServiceName] = []
        for service_name in self.service_names:
            if service_name.is_essential():
                result.append(service_name)
        return result
