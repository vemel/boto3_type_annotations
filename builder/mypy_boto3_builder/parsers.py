"""
Parsers for boto3 clients and resources.
"""
import inspect
from inspect import getdoc
from typing import List, Dict, Any, Optional, Iterable
from types import FunctionType

from boto3.exceptions import ResourceNotExistsError
from boto3.docs.utils import is_resource_action
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.base import ResourceMeta as Boto3ResourceMeta
from boto3.session import Session
from boto3.utils import ServiceContext
from botocore import xform_name
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
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.strings import clean_doc, get_class_prefix
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.docstring_parser import DocstringParser


def get_boto3_client(session: Session, service_name: ServiceName) -> BaseClient:
    """
    Get boto3 client from `session`.

    Arguments:
        session -- boto3 session.
        service_name -- ServiceName instance.

    Returns:
        Boto3 client.
    """
    return session.client(service_name.boto3_name)  # type: ignore


def get_boto3_resource(
    session: Session, service_name: ServiceName
) -> Boto3ServiceResource:
    """
    Get boto3 resource from `session`.

    Arguments:
        session -- boto3 session.
        service_name -- ServiceName instance.

    Returns:
        Boto3 resource.

    Raises:
        ResourceNotExistsError -- If service does not have ServiceResource.
    """
    return session.resource(service_name.boto3_name)  # type: ignore


def get_resource_public_methods(resource_class: Resource) -> Dict[str, FunctionType]:
    resource_class_members = inspect.getmembers(resource_class)
    resource_methods: Dict[str, FunctionType] = {}
    for name, member in resource_class_members:
        if name.startswith("_"):
            continue

        if name[0].isupper():
            continue

        if is_resource_action(member):
            resource_methods[name] = member
    return resource_methods


def get_public_methods(inspect_class: Any) -> Dict[str, FunctionType]:
    class_members = inspect.getmembers(inspect_class)
    methods: Dict[str, FunctionType] = {}
    for name, member in class_members:
        if not inspect.ismethod(member):
            continue

        if name.startswith("_"):
            continue

        methods[name] = member

    return methods


def parse_attributes(resource: Boto3ServiceResource) -> List[Attribute]:
    result: List[Attribute] = []
    service_model = resource.meta.client.meta.service_model
    if resource.meta.resource_model.shape:
        shape = service_model.shape_for(resource.meta.resource_model.shape)
        attributes = resource.meta.resource_model.get_attributes(shape)
        for name, attribute in attributes.items():
            result.append(
                Attribute(name, DocstringParser.parse_type(attribute[1].type_name))
            )

    return result


def parse_client(session: Session, service_name: ServiceName) -> Client:
    client = get_boto3_client(session, service_name)
    return Client(
        service_name=service_name,
        boto3_client=client,
        docstring=clean_doc(getdoc(client)),
        methods=parse_methods("Client", get_public_methods(client)),
    )


def parse_collections(resource: Boto3ServiceResource,) -> List[Collection]:
    result: List[Collection] = []
    for collection in resource.meta.resource_model.collections:
        methods = parse_methods(
            collection.name, get_public_methods(getattr(resource, collection.name)),
        )
        # for method in methods:
        #     method.decorators.append(TypeAnnotation(classmethod))
        result.append(
            Collection(
                name=collection.name,
                docstring=clean_doc(getdoc(collection)),
                type=InternalImport(
                    name=collection.name,
                    service_name=ServiceName(resource.meta.service_name),
                ),
                methods=methods,
            )
        )
    return result


def parse_identifiers(resource: Boto3ServiceResource,) -> List[Attribute]:
    result: List[Attribute] = []
    identifiers = resource.meta.resource_model.identifiers
    for identifier in identifiers:
        result.append(Attribute(identifier.name, type=TypeAnnotation(str)))
    return result


def parse_methods(class_name: str, public_methods: Dict[str, Any]) -> List[Method]:
    result: List[Method] = []
    for name, method in public_methods.items():
        prefix = f"{get_class_prefix(class_name)}{get_class_prefix(name)}"
        docstring_parser = DocstringParser()
        doc = getdoc(method) or ""
        arguments = docstring_parser.get_function_arguments(method)
        return_type = docstring_parser.NONE_ANNOTATION
        if doc:
            doc = clean_doc(doc)
            docstring_parser.enrich_arguments(doc, arguments, prefix)
            return_type = docstring_parser.get_return_type(doc, prefix)
        else:
            docless_arguments = docstring_parser.get_docless_method_arguments(name)
            if docless_arguments:
                arguments = docless_arguments

        result.append(
            Method(
                name=name, arguments=arguments, docstring=doc, return_type=return_type,
            )
        )
    return result


def parse_resource(resource: Boto3ServiceResource) -> Resource:
    name = resource.__class__.__name__.split(".", 1)[-1]

    methods = parse_methods(name, get_resource_public_methods(resource.__class__))

    attributes: List[Attribute] = []
    attributes.extend(parse_attributes(resource))
    attributes.extend(parse_identifiers(resource))

    collections = parse_collections(resource)

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
    except ResourceNotExistsError:
        return None

    methods = parse_methods("ServiceResource", get_public_methods(service_resource))

    attributes: List[Attribute] = []
    attributes.extend(parse_attributes(service_resource))
    attributes.extend(parse_identifiers(service_resource))

    collections = parse_collections(service_resource)

    sub_resources: List[Resource] = []
    for sub_resource in parse_sub_resources(session, service_name, service_resource):
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


def parse_sub_resources(
    session: Session, service_name: ServiceName, resource: Boto3ResourceMeta
) -> List[Boto3ServiceResource]:
    result: List[Boto3ServiceResource] = []
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
        result.append(
            resource_class(*args, client=get_boto3_client(session, service_name))
        )

    return result


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
                methods=parse_methods(waiter_name, get_public_methods(waiter)),
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
                    methods=parse_methods(
                        paginator_name, get_public_methods(paginator)
                    ),
                )
            )

    result.typed_dicts = result.extract_typed_dicts(result.get_types(), {})
    return result


def parse_fake_service_module(
    session: Session, service_name: ServiceName
) -> ServiceModule:
    result = ServiceModule(service_name=service_name, client=Client())

    boto3_client = get_boto3_client(session, service_name)
    boto3_resource: Optional[ServiceResource] = None
    try:
        boto3_resource = get_boto3_resource(session, service_name)
    except ResourceNotExistsError:
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
