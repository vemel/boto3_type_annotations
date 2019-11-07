from abc import abstractmethod
from typing import List, Set, Union, Tuple, Optional
from dataclasses import dataclass
from pathlib import Path


class FakeAnnotation:
    @property
    def __name__(self) -> str:
        return str(self)

    @abstractmethod
    def get_import_statement(self, module_name: str) -> str:
        pass


TypeAnnotation = Union[FakeAnnotation, type, str, None]


@dataclass
class InternalImport(FakeAnnotation):
    name: str
    service_name: str
    module_name: str = "service_resource"

    def __hash__(self) -> int:
        return hash(f"{self.scope}.{self.name}")

    def __str__(self) -> str:
        return f"{self.scope}.{self.name}"

    @property
    def scope(self) -> str:
        return f"{self.service_name}_{self.module_name}_scope"

    def get_import_statement(self, module_name: str) -> str:
        return f"import {module_name}.{self.service_name}.{self.module_name} as {self.scope}"


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
    def __args__(self):
        return self.children

    def get_import_statement(self, module_name: str) -> str:
        return f"from typing import {self}"


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


class TypeCollector:
    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        if hasattr(self, "methods"):
            for method in getattr(self, "methods"):
                types.update(method.get_types())
        if hasattr(self, "attributes"):
            for attribute in getattr(self, "attributes"):
                types.update(attribute.get_types())
        if hasattr(self, "sub_resources"):
            for sub_resource in getattr(self, "sub_resources"):
                types.update(sub_resource.get_types())
        if hasattr(self, "collections"):
            for collection in getattr(self, "collections"):
                types.update(collection.get_types())
        if hasattr(self, "waiters"):
            for waiter in getattr(self, "waiters"):
                types.update(waiter.get_types())
        if hasattr(self, "paginators"):
            for paginator in getattr(self, "paginators"):
                types.update(paginator.get_types())
        return types


@dataclass
class Collection(TypeCollector):
    name: str
    type: InternalImport
    methods: List[Method]


@dataclass
class Resource(TypeCollector):
    name: str
    methods: List[Method]
    attributes: List[Attribute]
    collections: List[Collection]


@dataclass
class Waiter(TypeCollector):
    name: str
    methods: List[Method]


@dataclass
class Paginator(TypeCollector):
    name: str
    methods: List[Method]


@dataclass
class ServiceResource(TypeCollector):
    name: str
    methods: List[Method]
    attributes: List[Attribute]
    collections: List[Collection]
    sub_resources: List[Resource]


@dataclass
class Client(TypeCollector):
    name: str
    methods: List[Method]


@dataclass
class ServiceWaiter(TypeCollector):
    name: str
    waiters: List[Waiter]


@dataclass
class ServicePaginator(TypeCollector):
    name: str
    paginators: List[Paginator]


@dataclass
class Config:
    services: List
    with_docs: bool
    module_name: str
    output: Path
