from __future__ import annotations

from typing import List, Set, Union, Tuple, Optional, Any
from dataclasses import dataclass
from pathlib import Path

from mypy_boto3_builder.service_name import ServiceName


class ImportString:
    def __init__(self, import_string: str) -> None:
        self.parts = import_string.split(".")

    def __str__(self) -> str:
        return ".".join(self.parts)

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Any) -> bool:
        return str(self) == str(other)

    def __gt__(self, other: Any) -> bool:
        return str(self) > str(other)

    def startswith(self, other: ImportString) -> bool:
        for part_index, part in enumerate(other.parts):
            try:
                self_part = self.parts[part_index]
            except IndexError:
                return False

            if self_part != part:
                return False

        return True


@dataclass
class ImportRecord:
    source: ImportString
    name: str = ""
    alias: str = ""

    def __str__(self) -> str:
        if self.name and self.alias:
            return f"from {self.source} import {self.name} as {self.alias}"
        if self.name:
            return f"from {self.source} import {self.name}"
        if self.alias:
            return f"import {self.source} as {self.alias}"
        return f"import {self.source}"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Any) -> bool:
        return str(self) == str(other)

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, ImportRecord):
            return self.source > other.source

        return str(self) > str(other)

    def render(self) -> str:
        return str(self)


class FakeAnnotation:
    @property
    def __name__(self) -> str:
        return str(self)

    def get_import_record(self, module_name: str) -> ImportRecord:
        return ImportRecord(source=ImportString(module_name), name=str(self))


TypeAnnotation = Union[FakeAnnotation, type]


@dataclass
class InternalImport(FakeAnnotation):
    name: str
    service_name: ServiceName
    module_name: str = "service_resource"

    def __hash__(self) -> int:
        return hash(f"{self.scope}.{self.name}")

    def __str__(self) -> str:
        return f"{self.scope}.{self.name}"

    @property
    def scope(self) -> str:
        return f"{self.service_name.value}_{self.module_name}_scope"

    def get_import_record(self, module_name: str) -> ImportRecord:
        source = ImportString(
            f"{module_name}.{self.service_name.name}.{self.module_name}"
        )
        return ImportRecord(source=source, alias=self.scope)


@dataclass
class AnnotationWrapper(FakeAnnotation):
    parent: type
    children: Tuple[TypeAnnotation, ...] = ()

    def __hash__(self) -> int:
        return hash(f"{self.parent}.{self.children}")

    def __str__(self) -> str:
        if getattr(self.parent, "__name__", None):
            return getattr(self.parent, "__name__")
        if hasattr(self.parent, "_name"):
            return getattr(self.parent, "_name") or "Union"
        if self.parent == Union:
            return "Union"
        if self.parent == Optional:
            return "Optional"
        return self.parent.__class__.__name__

    @property
    def __args__(self) -> Tuple[TypeAnnotation, ...]:
        return self.children

    def get_import_record(self, _module_name: str) -> ImportRecord:
        return ImportRecord(source=ImportString("typing"), name=str(self))


@dataclass
class Attribute:
    name: str
    type: TypeAnnotation

    def get_types(self) -> Set[TypeAnnotation]:
        types = set()
        types.add(self.type)
        if hasattr(self.type, "__args__"):
            for arg in getattr(self.type, "__args__"):
                types.add(arg)
        return types


@dataclass
class Argument:
    name: str
    type: TypeAnnotation
    required: bool

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        types.add(self.type)
        if hasattr(self.type, "__args__"):
            for arg in getattr(self.type, "__args__"):
                types.add(arg)
        return types


@dataclass
class Method:
    name: str
    arguments: List[Argument]
    docstring: str
    return_type: TypeAnnotation

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        for argument in self.arguments:
            types.update(argument.get_types())
        types.add(self.return_type)

        return types


@dataclass
class TypeCollector:
    def get_types(self) -> Set[TypeAnnotation]:
        raise TypeError("TypeCollector cannot collect types")

    def get_import_records(self, module_name: str) -> Set[ImportRecord]:
        raise TypeError("TypeCollector cannot collect import records")


@dataclass
class Collection(TypeCollector):
    name: str
    type: InternalImport
    methods: List[Method]

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        types.add(self.type)
        for method in self.methods:
            types.update(method.get_types())
        return types


@dataclass
class Resource(TypeCollector):
    name: str
    methods: List[Method]
    attributes: List[Attribute]
    collections: List[Collection]

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        for method in self.methods:
            types.update(method.get_types())
        for attribute in self.attributes:
            types.update(attribute.get_types())
        for collection in self.collections:
            types.update(collection.get_types())
        return types


@dataclass
class Waiter(TypeCollector):
    name: str
    methods: List[Method]

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        for method in self.methods:
            types.update(method.get_types())
        return types


@dataclass
class Paginator(TypeCollector):
    name: str
    methods: List[Method]

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        for method in self.methods:
            types.update(method.get_types())
        return types


@dataclass
class ServiceResource(TypeCollector):
    service_name: ServiceName
    methods: List[Method]
    attributes: List[Attribute]
    collections: List[Collection]
    sub_resources: List[Resource]

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        for method in self.methods:
            types.update(method.get_types())
        for attribute in self.attributes:
            types.update(attribute.get_types())
        for collection in self.collections:
            types.update(collection.get_types())
        for sub_resource in self.sub_resources:
            types.update(sub_resource.get_types())
        return types

    def get_import_records(self, module_name: str) -> Set[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        source = ImportString(
            f"{module_name}.{self.service_name.name}.service_resource"
        )

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
class Client(TypeCollector):
    service_name: ServiceName
    methods: List[Method]

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        for method in self.methods:
            types.update(method.get_types())
        return types

    def get_import_records(self, module_name: str) -> Set[ImportRecord]:
        source = ImportString(f"{module_name}.{self.service_name.name}.client")
        return {ImportRecord(source, "Client")}


@dataclass
class ServiceWaiter(TypeCollector):
    service_name: ServiceName
    waiters: List[Waiter]

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        for waiter in self.waiters:
            types.update(waiter.get_types())
        return types

    def get_import_records(self, module_name: str) -> Set[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        source = ImportString(f"{module_name}.{self.service_name.name}.waiter")

        for waiter in self.waiters:
            import_records.add(ImportRecord(source, waiter.name))

        return import_records


@dataclass
class ServicePaginator(TypeCollector):
    service_name: ServiceName
    paginators: List[Paginator]

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        for paginator in self.paginators:
            types.update(paginator.get_types())
        return types

    def get_import_records(self, module_name: str) -> Set[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        source = ImportString(f"{module_name}.{self.service_name.name}.paginator")

        for paginator in self.paginators:
            import_records.add(ImportRecord(source, paginator.name))

        return import_records


@dataclass
class Config:
    services: List[ServiceName]
    with_docs: bool
    module_name: str
    output: Path
