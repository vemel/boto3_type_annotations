from typing import List, Optional, Set
from dataclasses import dataclass

from type_map import TypeAnnotation


@dataclass
class Attribute:
    name: str
    type: TypeAnnotation

    def get_types(self) -> Set[TypeAnnotation]:
        types = set()
        types.add(self.type)
        if hasattr(self.type, "__args__"):
            for arg in self.type.__args__:
                types.add(arg)
        return types


@dataclass
class Argument:
    name: str
    type: TypeAnnotation
    required: bool

    def get_types(self) -> Set[TypeAnnotation]:
        types: Set[TypeAnnotation] = set()
        if not self.required:
            types.add(Optional)
        types.add(self.type)
        if hasattr(self.type, "__args__"):
            for arg in self.type.__args__:
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
    with_clients: bool
    with_service_resources: bool
    with_paginators: bool
    with_waiters: bool
    package_name: str
    module_name: str
