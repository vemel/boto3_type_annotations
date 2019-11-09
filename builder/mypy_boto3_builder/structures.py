from __future__ import annotations

from dataclasses import dataclass
from typing import List, Set, Iterable, Optional

from boto3.resources.collection import ResourceCollection
from botocore.client import BaseClient
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.constants import MODULE_NAME
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.external_import import ExternalImport


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
    type: FakeAnnotation
    required: bool
    default: FakeAnnotation = TypeAnnotation(None)

    def get_types(self) -> Set[FakeAnnotation]:
        types = self.type.get_types()
        if not self.required:
            types.update(self.default.get_types())

        return types

    def render(self) -> str:
        if self.required:
            return f"{self.name}: {self.type.render()}"

        return f"{self.name}: {self.type.render()} = {self.default.render()}"


@dataclass
class Function:
    name: str
    arguments: List[Argument]
    docstring: str
    return_type: FakeAnnotation
    decorators: Iterable[str] = ()
    body: str = "pass"
    arguments_differ: bool = True

    def get_types(self) -> Set[FakeAnnotation]:
        types = self.return_type.get_types()
        for argument in self.arguments:
            types.update(argument.get_types())

        return types

    @property
    def first_arg(self) -> Optional[str]:
        return None

    def render_lines(self, include_doc: bool = True) -> List[str]:
        result: List[str] = []
        for decorator in self.decorators:
            result.append(f"@{decorator}")

        arguments: List[str] = []
        if self.first_arg:
            arguments.append(self.first_arg)
        for argument in sorted(self.arguments, key=lambda m: not m.required):
            arguments.append(argument.render())

        result.append("# pylint: disable=arguments-differ")
        result.append(f"def {self.name}(")

        for index, formatted_argument in enumerate(arguments):
            trail = "," if index < len(arguments) - 1 else ""
            result.append(f"    {formatted_argument}{trail}")

        result.append(f") -> {self.return_type.render()}:")
        if include_doc and self.docstring:
            result.append('    """')
            for line in self.docstring.split("\n"):
                result.append(f"    {line}")
            result.append('    """')
        result.append(f"    {self.body}")
        return result


@dataclass
class Method(Function):
    @property
    def first_arg(self) -> Optional[str]:
        if "classmethod" in self.decorators:
            return "cls"
        if "staticmethod" in self.decorators:
            return None

        return "self"


@dataclass
class Collection:
    name: str
    docstring: str
    type: FakeAnnotation
    methods: List[Method]

    def get_types(self) -> Set[FakeAnnotation]:
        types = self.type.get_types()
        for method in self.methods:
            types.update(method.get_types())
        return types


@dataclass
class Resource:
    name: str
    docstring: str
    methods: List[Method]
    attributes: List[Attribute]
    collections: List[Collection]

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        for method in self.methods:
            types.update(method.get_types())
        for attribute in self.attributes:
            types.update(attribute.get_types())
        for collection in self.collections:
            types.update(collection.get_types())
        return types


@dataclass
class Waiter:
    name: str
    docstring: str
    methods: List[Method]

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        for method in self.methods:
            types.update(method.get_types())
        return types


@dataclass
class Paginator:
    name: str
    docstring: str
    methods: List[Method]

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        for method in self.methods:
            types.update(method.get_types())
        return types


@dataclass
class ServiceResource:
    service_name: ServiceName
    docstring: str
    methods: List[Method]
    attributes: List[Attribute]
    collections: List[Collection]
    sub_resources: List[Resource]

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        types.add(
            ExternalImport(
                source="boto3.resources.base",
                name="ServiceResource",
                alias="Boto3ServiceResource",
            )
        )
        types.add(TypeAnnotation(ResourceCollection))
        for method in self.methods:
            types.update(method.get_types())
        for attribute in self.attributes:
            types.update(attribute.get_types())
        for collection in self.collections:
            types.update(collection.get_types())
        for sub_resource in self.sub_resources:
            types.update(sub_resource.get_types())

        for type_annotation in types:
            if isinstance(type_annotation, InternalImport):
                type_annotation.localize(self.service_name)

        return types

    def get_import_records(self) -> Set[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        source = f"{MODULE_NAME}_{self.service_name.name}.service_resource"

        import_records.add(ImportRecord(source, "ServiceResource"))
        for resource in self.sub_resources:
            import_records.add(ImportRecord(source, resource.name))

        for collection in self.collections:
            import_records.add(ImportRecord(source, collection.name))

        for resource in self.sub_resources:
            for collection in resource.collections:
                import_records.add(ImportRecord(source, collection.name))
        return import_records


@dataclass
class Client:
    service_name: ServiceName
    docstring: str
    methods: List[Method]

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        types.add(TypeAnnotation(BaseClient))
        for method in self.methods:
            types.update(method.get_types())

        for type_annotation in types:
            if isinstance(type_annotation, InternalImport):
                type_annotation.localize(self.service_name)

        return types

    def get_import_records(self) -> Set[ImportRecord]:
        source = f"{MODULE_NAME}_{self.service_name.name}.client"
        return {ImportRecord(source, "Client")}


@dataclass
class ServiceWaiter:
    service_name: ServiceName
    waiters: List[Waiter]

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        types.add(TypeAnnotation(Boto3Waiter))
        for waiter in self.waiters:
            types.update(waiter.get_types())

        for type_annotation in types:
            if isinstance(type_annotation, InternalImport):
                type_annotation.localize(self.service_name)

        return types

    def get_import_records(self) -> Set[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        source = f"{MODULE_NAME}_{self.service_name.name}.waiter"

        for waiter in self.waiters:
            import_records.add(ImportRecord(source, waiter.name))

        return import_records


@dataclass
class ServicePaginator:
    service_name: ServiceName
    paginators: List[Paginator]

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        types.add(TypeAnnotation(Boto3Paginator))
        for paginator in self.paginators:
            types.update(paginator.get_types())

        for type_annotation in types:
            if isinstance(type_annotation, InternalImport):
                type_annotation.localize(self.service_name)

        return types

    def get_import_records(self) -> Set[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        source = f"{MODULE_NAME}_{self.service_name.name}.paginator"

        for paginator in self.paginators:
            import_records.add(ImportRecord(source, paginator.name))

        return import_records
