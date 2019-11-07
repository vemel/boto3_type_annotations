import inspect
from inspect import getdoc
from typing import List, Dict, Generator, Any, Optional

import boto3
from boto3.docs.utils import is_resource_action
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.base import ResourceMeta as Boto3ResourceMeta
from boto3.session import Session
from boto3.utils import ServiceContext
from botocore import xform_name
from botocore.client import BaseClient
from botocore.docs.method import get_instance_public_methods
from botocore.exceptions import UnknownServiceError
from botocore.paginate import PaginatorModel
from docstring_parser import parse
from docstring_parser.parser.common import DocstringMeta, Docstring

from mypy_boto3_builder.structures import (
    Argument,
    Method,
    Client,
    Attribute,
    Resource,
    Collection,
    ServiceResource,
    Waiter,
    ServiceWaiter,
    Paginator,
    ServicePaginator,
    TypeAnnotation,
    InternalImport,
)
from mypy_boto3_builder.type_map import TYPE_MAP
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName


logger = get_logger()


def get_resource_public_actions(resource_class: Resource) -> Dict[str, Any]:
    resource_class_members = inspect.getmembers(resource_class)
    resource_methods = {}
    for name, member in resource_class_members:
        if not name.startswith("_"):
            if not name[0].isupper():
                if is_resource_action(member):
                    resource_methods[name] = member
    return resource_methods


def manually_set_method(name: str) -> Method:
    if name == "create_tags":
        return Method(
            "create_tags",
            [
                Argument("DryRun", bool, False),
                Argument("Resources", List[Any], True),
                Argument("Tags", List[Any], True),
            ],
            "",
            type(None),
        )

    logger.warning(f"Unknown method: {name}")
    return Method(name, [], "", type(None))


def parse_arguments(parsed_doc: Docstring) -> Generator[Argument, None, None]:
    types_map = {}
    for meta_item in parsed_doc.meta:
        if meta_item.args[0] == "type":
            types_map[meta_item.args[1]] = parse_type_from_str(meta_item.description)
    for arg in parsed_doc.params:
        yield Argument(
            arg.arg_name,
            types_map[arg.arg_name],
            arg.description.startswith("**[REQUIRED]**"),
        )


def parse_attributes(
    resource: Boto3ServiceResource,
) -> Generator[Attribute, None, None]:
    service_model = resource.meta.client.meta.service_model
    if resource.meta.resource_model.shape:
        shape = service_model.shape_for(resource.meta.resource_model.shape)
        attributes = resource.meta.resource_model.get_attributes(shape)
        for name, attribute in attributes.items():
            yield Attribute(name, parse_type_from_str(attribute[1].type_name))


def parse_client(session: Session, service_name: ServiceName) -> Client:
    client = session.client(service_name.value)
    return Client(
        service_name, list(parse_methods(get_instance_public_methods(client)))
    )


def parse_collections(
    resource: Boto3ServiceResource,
) -> Generator[Collection, None, None]:
    for collection in resource.meta.resource_model.collections:
        yield Collection(
            name=collection.name,
            type=InternalImport(
                name=collection.name,
                service_name=ServiceName(resource.meta.service_name),
            ),
            methods=list(
                parse_methods(
                    get_instance_public_methods(getattr(resource, collection.name))
                )
            ),
        )


def parse_identifiers(
    resource: Boto3ServiceResource,
) -> Generator[Attribute, None, None]:
    identifiers = resource.meta.resource_model.identifiers
    for identifier in identifiers:
        yield Attribute(identifier.name, parse_type_from_str("string"))


def parse_methods(public_methods: Dict) -> Generator[Method, None, None]:
    for name, method in public_methods.items():
        doc = getdoc(method)
        if doc is None:
            logger.debug(f"Docless method: {name}")
            yield manually_set_method(name)
        else:
            parsed_doc = parse(doc.replace("::", ""))
            yield Method(
                name,
                list(parse_arguments(parsed_doc)),
                doc,
                parse_return_type(parsed_doc.meta),
            )


def parse_resource(resource: Boto3ServiceResource) -> Resource:
    return Resource(
        resource.__class__.__name__.split(".")[1],
        list(parse_methods(get_resource_public_actions(resource.__class__))),
        list(parse_attributes(resource)) + list(parse_identifiers(resource)),
        list(parse_collections(resource)),
    )


def parse_return_type(meta: List[DocstringMeta]) -> TypeAnnotation:
    for docstring_meta in meta:
        if docstring_meta.args[0] == "rtype":
            return parse_type_from_str(docstring_meta.description)

    return type(None)


def parse_service_resource(
    session: Session, service_name: ServiceName
) -> Optional[ServiceResource]:
    try:
        service_resource = session.resource(service_name.value)
    except boto3.exceptions.ResourceNotExistsError:
        return None
    return ServiceResource(
        service_name,
        list(parse_methods(get_instance_public_methods(service_resource))),
        list(parse_attributes(service_resource))
        + list(parse_identifiers(service_resource)),
        list(parse_collections(service_resource)),
        [
            parse_resource(resource)
            for resource in retrieve_sub_resources(session, service_resource)
        ],
    )


def parse_type_from_str(type_str: str) -> TypeAnnotation:
    try:
        return TYPE_MAP[type_str]
    except KeyError:
        raise ValueError(f"Unknown type: {type_str}")


def parse_service_waiter(
    session: Session, service_name: ServiceName
) -> Optional[ServiceWaiter]:
    client = session.client(service_name.value)
    if not client.waiter_names:
        return None

    return ServiceWaiter(service_name, list(parse_waiters(client)))


def parse_waiters(client: BaseClient) -> Generator[Waiter, None, None]:
    for waiter_name in client.waiter_names:
        waiter = client.get_waiter(waiter_name)
        yield Waiter(
            waiter.name, list(parse_methods(get_instance_public_methods(waiter)))
        )


def parse_service_paginator(
    session: Session, service_name: ServiceName
) -> Optional[ServicePaginator]:
    session_loader = session._loader  # pylint: disable=protected-access
    if service_name.value not in session_loader.list_available_services("paginators-1"):
        return None

    client = session.client(service_name.value)

    session_session = session._session  # pylint: disable=protected-access
    service_paginator_model = session_session.get_paginator_model(service_name.value)
    return ServicePaginator(
        service_name, list(parse_paginators(client, service_paginator_model))
    )


def parse_paginators(
    client: BaseClient, service_paginator_model: PaginatorModel
) -> Generator[Paginator, None, None]:
    paginator_config = (
        service_paginator_model._paginator_config  # pylint: disable=protected-access
    )
    for paginator_name in sorted(paginator_config):
        paginator = client.get_paginator(xform_name(paginator_name))
        paginator_model = paginator._model  # pylint: disable=protected-access
        yield Paginator(
            paginator_model.name,
            list(parse_methods(get_instance_public_methods(paginator))),
        )


def retrieve_sub_resources(
    session: Session, resource: Boto3ResourceMeta
) -> Generator[Boto3ServiceResource, None, None]:
    session_session = session._session  # pylint: disable=protected-access
    loader = session_session.get_component("data_loader")
    json_resource_model = loader.load_service_model(
        resource.meta.service_name, "resources-1"
    )
    service_model = resource.meta.client.meta.service_model
    try:
        service_waiter_model = session_session.get_waiter_model(
            service_model.service_name
        )
    except UnknownServiceError:
        service_waiter_model = None
    for name in json_resource_model["resources"]:
        resource_model = json_resource_model["resources"][name]
        cls = session.resource_factory.load_from_definition(
            resource_name=name,
            single_resource_json_definition=resource_model,
            service_context=ServiceContext(
                service_name=resource.meta.service_name,
                resource_json_definitions=json_resource_model["resources"],
                service_model=service_model,
                service_waiter_model=service_waiter_model,
            ),
        )
        identifiers = cls.meta.resource_model.identifiers
        args = []
        for _ in identifiers:
            args.append("foo")
        yield cls(*args, client=boto3.client(resource.meta.service_name))
