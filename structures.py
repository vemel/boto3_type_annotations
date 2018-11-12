from typing import NamedTuple, List, Union, Tuple


class Attribute(NamedTuple):
    name: str
    type: Union[type, Tuple, str]


class Argument(NamedTuple):
    name: str
    type: Union[type, Tuple, str]
    required: bool


class Method(NamedTuple):
    name: str
    arguments: List[Argument]
    docstring: str
    return_type: Union[type, Tuple, str]


class Collection(NamedTuple):
    name: str
    methods: List[Method]


class Resource(NamedTuple):
    name: str
    methods: List[Method]
    attributes: List[Attribute]
    collections: List[Collection]


class ServiceResource(NamedTuple):
    name: str
    methods: List[Method]
    attributes: List[Attribute]
    collections: List[Collection]
    sub_resources: List[Resource]


class Client(NamedTuple):
    name: str
    methods: List[Method]
