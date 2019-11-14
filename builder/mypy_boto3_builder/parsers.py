import inspect
from inspect import getdoc
from typing import List, Dict, Generator, Any, Optional, Iterable

import boto3
from boto3.docs.utils import is_resource_action
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.base import ResourceMeta as Boto3ResourceMeta
from boto3.session import Session
from boto3.utils import ServiceContext
from botocore import xform_name
from botocore.docs.method import get_instance_public_methods
from botocore.exceptions import UnknownServiceError
from botocore.client import BaseClient

from mypy_boto3_builder.structures import (
    Method,
    Client,
    Attribute,
    Resource,
    Collection,
    ServiceResource,
    Waiter,
    Paginator,
    Boto3Module,
    ServiceModule,
    MasterModule,
)
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils import clean_doc
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.docstring_parser import DocstringParser


logger = get_logger()


def get_boto3_client(session: Session, service_name: ServiceName) -> BaseClient:
    return session.client(service_name.boto3_name)  # type: ignore


def get_boto3_resource(
    session: Session, service_name: ServiceName
) -> Boto3ServiceResource:
    return session.resource(service_name.boto3_name)  # type: ignore


def get_resource_public_actions(resource_class: Resource) -> Dict[str, Any]:
    resource_class_members = inspect.getmembers(resource_class)
    resource_methods = {}
    for name, member in resource_class_members:
        if not name.startswith("_"):
            if not name[0].isupper():
                if is_resource_action(member):
                    resource_methods[name] = member
    return resource_methods


def parse_attributes(
    resource: Boto3ServiceResource,
) -> Generator[Attribute, None, None]:
    service_model = resource.meta.client.meta.service_model
    if resource.meta.resource_model.shape:
        shape = service_model.shape_for(resource.meta.resource_model.shape)
        attributes = resource.meta.resource_model.get_attributes(shape)
        for name, attribute in attributes.items():
            yield Attribute(name, DocstringParser.parse_type(attribute[1].type_name))


def parse_client(session: Session, service_name: ServiceName) -> Client:
    client = get_boto3_client(session, service_name)
    return Client(
        service_name=service_name,
        boto3_client=client,
        docstring=clean_doc(getdoc(client)),
        methods=list(parse_methods(get_instance_public_methods(client))),
    )


def parse_collections(
    resource: Boto3ServiceResource,
) -> Generator[Collection, None, None]:
    for collection in resource.meta.resource_model.collections:
        methods = list(
            parse_methods(
                get_instance_public_methods(getattr(resource, collection.name))
            )
        )
        for method in methods:
            method.decorators.append(TypeAnnotation(classmethod))
        yield Collection(
            name=collection.name,
            docstring=clean_doc(getdoc(collection)),
            type=InternalImport(
                name=collection.name,
                service_name=ServiceName(resource.meta.service_name),
            ),
            methods=methods,
        )


def parse_identifiers(
    resource: Boto3ServiceResource,
) -> Generator[Attribute, None, None]:
    identifiers = resource.meta.resource_model.identifiers
    for identifier in identifiers:
        yield Attribute(identifier.name, type=TypeAnnotation(str))


def parse_methods(public_methods: Dict[str, Any]) -> Generator[Method, None, None]:
    docstring_parser = DocstringParser()
    for name, method in public_methods.items():
        doc = getdoc(method)
        arguments = docstring_parser.get_function_arguments(method)
        return_type = DocstringParser.NONE_ANNOTATION
        if doc:
            docstring_parser.enrich_arguments(method, doc, arguments)
            return_type = DocstringParser.get_return_type(doc)
        else:
            docless_arguments = docstring_parser.get_docless_method_arguments(name)
            if docless_arguments:
                arguments = docless_arguments

        yield Method(
            name=name,
            arguments=arguments,
            docstring=clean_doc(doc),
            return_type=return_type,
        )


def parse_resource(resource: Boto3ServiceResource) -> Resource:
    name = resource.__class__.__name__.split(".", 1)[-1]

    methods = list(parse_methods(get_resource_public_actions(resource.__class__)))

    attributes: List[Attribute] = []
    for attribute in parse_attributes(resource):
        attributes.append(attribute)
    for attribute in parse_identifiers(resource):
        attributes.append(attribute)

    collections = list(parse_collections(resource))

    return Resource(
        name=name,
        docstring=clean_doc(getdoc(resource)),
        methods=methods,
        attributes=attributes,
        collections=collections,
    )


def parse_service_resource(
    session: Session, service_name: ServiceName
) -> Optional[ServiceResource]:
    try:
        service_resource = get_boto3_resource(session, service_name)
    except boto3.exceptions.ResourceNotExistsError:
        return None

    methods = list(parse_methods(get_instance_public_methods(service_resource)))

    attributes: List[Attribute] = []
    for attribute in parse_attributes(service_resource):
        attributes.append(attribute)
    for attribute in parse_identifiers(service_resource):
        attributes.append(attribute)

    collections = list(parse_collections(service_resource))

    sub_resources = []
    for sub_resource in retrieve_sub_resources(session, service_name, service_resource):
        sub_resources.append(parse_resource(sub_resource))

    return ServiceResource(
        service_name=service_name,
        boto3_service_resource=service_resource,
        docstring=clean_doc(getdoc(service_resource)),
        methods=methods,
        attributes=attributes,
        collections=collections,
        sub_resources=sub_resources,
    )


def retrieve_sub_resources(
    session: Session, service_name: ServiceName, resource: Boto3ResourceMeta
) -> Generator[Boto3ServiceResource, None, None]:
    session_session = session._session  # pylint: disable=protected-access
    loader = session_session.get_component("data_loader")
    assert resource.meta.service_name == service_name.boto3_name
    json_resource_model = loader.load_service_model(
        service_name.boto3_name, "resources-1"
    )
    service_model = resource.meta.client.meta.service_model
    assert service_model.service_name == service_name.boto3_name
    try:
        service_waiter_model = session_session.get_waiter_model(service_name.boto3_name)
    except UnknownServiceError:
        service_waiter_model = None
    for name in json_resource_model["resources"]:
        resource_model = json_resource_model["resources"][name]
        resource_class = session.resource_factory.load_from_definition(
            resource_name=name,
            single_resource_json_definition=resource_model,
            service_context=ServiceContext(
                service_name=service_name.boto3_name,
                resource_json_definitions=json_resource_model["resources"],
                service_model=service_model,
                service_waiter_model=service_waiter_model,
            ),
        )
        identifiers = resource_class.meta.resource_model.identifiers
        args = []
        for _ in identifiers:
            args.append("foo")
        yield resource_class(*args, client=get_boto3_client(session, service_name))


def parse_service_module(session: Session, service_name: ServiceName) -> ServiceModule:
    client = parse_client(session, service_name)
    result = ServiceModule(
        service_name=service_name,
        client=client,
        service_resource=parse_service_resource(session, service_name),
    )

    for waiter_name in client.boto3_client.waiter_names:
        waiter = client.boto3_client.get_waiter(waiter_name)
        result.waiters.append(
            Waiter(
                name=waiter.name,
                boto3_waiter=waiter,
                docstring=clean_doc(getdoc(waiter)),
                methods=list(parse_methods(get_instance_public_methods(waiter))),
            )
        )

    session_loader = session._loader  # pylint: disable=protected-access
    if service_name.boto3_name in session_loader.list_available_services(
        "paginators-1"
    ):
        session_client = get_boto3_client(session, service_name)

        botocore_session = session._session  # pylint: disable=protected-access
        service_paginator_model = botocore_session.get_paginator_model(
            service_name.boto3_name
        )
        paginator_config = (
            service_paginator_model._paginator_config  # pylint: disable=protected-access
        )
        for paginator_name in sorted(paginator_config):
            paginator = session_client.get_paginator(xform_name(paginator_name))
            paginator_model = paginator._model  # pylint: disable=protected-access
            result.paginators.append(
                Paginator(
                    name=paginator_model.name,
                    boto3_paginator=paginator,
                    docstring=clean_doc(getdoc(paginator)),
                    methods=list(parse_methods(get_instance_public_methods(paginator))),
                )
            )

    result.type_defs = result.extract_type_defs(result.get_types())
    return result


def parse_fake_service_module(
    session: Session, service_name: ServiceName
) -> ServiceModule:
    result = ServiceModule(service_name=service_name, client=Client())

    boto3_client = get_boto3_client(session, service_name)
    boto3_resource: Optional[ServiceResource] = None
    try:
        boto3_resource = get_boto3_resource(session, service_name)
    except boto3.exceptions.ResourceNotExistsError:
        pass

    if boto3_resource:
        result.service_resource = ServiceResource()

    if boto3_client.waiter_names:
        result.waiters.append(Waiter("FakeWaiter"))

    session_loader = session._loader  # pylint: disable=protected-access
    if service_name.boto3_name in session_loader.list_available_services(
        "paginators-1"
    ):
        result.paginators.append(Paginator("FakePaginator"))

    return result


def parse_master_module(
    session: Session, service_names: Iterable[ServiceName]
) -> MasterModule:
    result = MasterModule()
    for service_name in service_names:
        result.service_modules.append(parse_fake_service_module(session, service_name))
        result.service_names.append(service_name)

    return result


def parse_boto3_module(
    session: Session, service_names: Iterable[ServiceName]
) -> Boto3Module:
    result = Boto3Module()
    for service_name in service_names:
        result.service_modules.append(parse_fake_service_module(session, service_name))
        result.service_names.append(service_name)

    return result
