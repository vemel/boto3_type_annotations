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


def get_resource_public_methods(
    resource_class: Boto3ResourceMeta,
) -> Dict[str, FunctionType]:
    """
    Extract public methods from boto3 sub resource.

    Arguments:
        resource_class -- boto3 resource meta.

    Returns:
        A dictionary of method name and method.
    """
    class_members = inspect.getmembers(resource_class)
    methods: Dict[str, FunctionType] = {}
    for name, member in class_members:
        if name.startswith("_"):
            continue

        if name[0].isupper():
            continue

        if not is_resource_action(member):
            continue

        methods[name] = member

    return methods


def get_public_methods(inspect_class: Any) -> Dict[str, FunctionType]:
    """
    Extract public methods from any class.

    Arguments:
        inspect_class -- Inspect class.

    Returns:
        A dictionary of method name and method.
    """
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
    """
    Extract attributes from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Attribute structures.
    """
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
    """
    Parse boto3 client to a structure.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        Client structure.
    """
    client = get_boto3_client(session, service_name)
    public_methods = get_public_methods(client)
    methods = [
        parse_method("Client", method_name, method)
        for method_name, method in public_methods.items()
    ]
    return Client(
        service_name=service_name,
        boto3_client=client,
        docstring=clean_doc(getdoc(client)),
        methods=methods,
    )


def parse_collections(resource: Boto3ServiceResource) -> List[Collection]:
    """
    Extract collections from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Collection structures.
    """
    result: List[Collection] = []
    for collection in resource.meta.resource_model.collections:
        collection_class = getattr(resource, collection.name)
        public_methods = get_public_methods(collection_class)
        methods = [
            parse_method(collection.name, method_name, method)
            for method_name, method in public_methods.items()
        ]

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


def parse_identifiers(resource: Boto3ServiceResource) -> List[Attribute]:
    """
    Extract collections from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Attribute structures.
    """
    result: List[Attribute] = []
    identifiers = resource.meta.resource_model.identifiers
    for identifier in identifiers:
        result.append(Attribute(identifier.name, type=TypeAnnotation(str)))
    return result


def parse_method(parent_name: str, name: str, method: FunctionType) -> Method:
    """
    Parse method to a structure.

    Arguments:
        parent_name -- Parent class name.
        method -- Inspect method.

    Returns:
        Method structure.
    """
    prefix = f"{get_class_prefix(parent_name)}{get_class_prefix(name)}"
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

    return Method(
        name=name, arguments=arguments, docstring=doc, return_type=return_type,
    )


def parse_resource(resource: Boto3ServiceResource) -> Resource:
    """
    Parse boto3 sub Resource data.

    Arguments:
        resource -- Original boto3 resource.

    Returns:
        Resource structure.
    """
    name = resource.__class__.__name__.split(".", 1)[-1]

    public_methods = get_resource_public_methods(resource.__class__)
    methods = [
        parse_method(name, method_name, method)
        for method_name, method in public_methods.items()
    ]

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
    """
    Parse boto3 ServiceResource data.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        ServiceResource structure or None if service does not have a resource.
    """
    try:
        service_resource = get_boto3_resource(session, service_name)
    except ResourceNotExistsError:
        return None

    public_methods = get_public_methods(service_resource)
    methods = [
        parse_method("ServiceResource", method_name, method)
        for method_name, method in public_methods.items()
    ]

    attributes: List[Attribute] = []
    attributes.extend(parse_attributes(service_resource))
    attributes.extend(parse_identifiers(service_resource))

    collections = parse_collections(service_resource)

    sub_resources: List[Resource] = []
    for sub_resource in get_sub_resources(session, service_name, service_resource):
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


def get_sub_resources(
    session: Session, service_name: ServiceName, resource: Boto3ResourceMeta
) -> List[Boto3ServiceResource]:
    """
    Initialize ServiceResource sub-resources with fake data.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.
        resource -- Parent ServiceResource.

    Returns:
        A list of initialized `Boto3ServiceResource`.
    """
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
        args = ["foo"] * len(identifiers)
        result.append(
            resource_class(*args, client=get_boto3_client(session, service_name))
        )

    return result


def parse_service_module(session: Session, service_name: ServiceName) -> ServiceModule:
    """
    Extract all data from boto3 service meodule.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        ServiceModule structure.
    """
    client = parse_client(session, service_name)
    result = ServiceModule(
        service_name=service_name,
        client=client,
        service_resource=parse_service_resource(session, service_name),
    )

    for waiter_name in client.boto3_client.waiter_names:
        waiter = client.boto3_client.get_waiter(waiter_name)
        public_methods = get_public_methods(waiter)
        methods = [
            parse_method(waiter_name, method_name, method)
            for method_name, method in public_methods.items()
        ]
        result.waiters.append(
            Waiter(
                name=waiter.name,
                boto3_waiter=waiter,
                docstring=clean_doc(getdoc(waiter)),
                methods=methods,
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
            public_methods = get_public_methods(paginator)
            methods = [
                parse_method(paginator_name, method_name, method)
                for method_name, method in public_methods.items()
            ]
            paginator_model = paginator._model  # pylint: disable=protected-access
            result.paginators.append(
                Paginator(
                    name=paginator_model.name,
                    boto3_paginator=paginator,
                    docstring=clean_doc(getdoc(paginator)),
                    methods=methods,
                )
            )

    result.typed_dicts = result.extract_typed_dicts(result.get_types(), {})
    return result


def parse_fake_service_module(
    session: Session, service_name: ServiceName
) -> ServiceModule:
    """
    Create fake boto3 service module structure.

    Used by stubs and master package.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        ServiceModule structure.
    """
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
    """
    Parse data for master module.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        MasterModule structure.
    """
    result = MasterModule()
    for service_name in service_names:
        result.service_modules.append(parse_fake_service_module(session, service_name))
        result.service_names.append(service_name)

    return result


def parse_boto3_module(
    session: Session, service_names: Iterable[ServiceName]
) -> Boto3Module:
    """
    Parse data for boto3-stubs module.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        MasterModule structure.
    """
    result = Boto3Module()
    for service_name in service_names:
        result.service_modules.append(parse_fake_service_module(session, service_name))
        result.service_names.append(service_name)

    return result
