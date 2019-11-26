"""
Parser for Boto3 ServiceResource, produces `structires.ServiceResource`.
"""
import inspect
from typing import List, Optional

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.session import Session
from boto3.utils import ServiceContext
from botocore.exceptions import UnknownServiceError

from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.resource import Resource
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.parsers.boto3_utils import get_boto3_resource
from mypy_boto3_builder.parsers.helpers import (
    get_public_methods,
    parse_method,
    parse_attributes,
)
from mypy_boto3_builder.parsers.identifiers import parse_identifiers
from mypy_boto3_builder.parsers.collections import parse_collections
from mypy_boto3_builder.parsers.resource import parse_resource
from mypy_boto3_builder.parsers.boto3_utils import get_boto3_client


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
    service_resource = get_boto3_resource(session, service_name)
    if service_resource is None:
        return None

    public_methods = get_public_methods(service_resource)
    methods = [
        parse_method("ServiceResource", method_name, method)
        for method_name, method in public_methods.items()
    ]

    attributes: List[Attribute] = []
    attributes.extend(parse_attributes(service_resource))
    attributes.extend(parse_identifiers(service_resource))

    collections = parse_collections("ServiceResource", service_resource)
    for collection in collections:
        attributes.append(
            Attribute(
                collection.attribute_name, InternalImport(collection.name, service_name)
            )
        )

    sub_resources: List[Resource] = []
    for sub_resource in get_sub_resources(session, service_name, service_resource):
        sub_resources.append(parse_resource(sub_resource, service_name))

    return ServiceResource(
        service_name=service_name,
        boto3_service_resource=service_resource,
        docstring=inspect.getdoc(service_resource) or "",
        methods=methods,
        attributes=attributes,
        collections=collections,
        sub_resources=sub_resources,
    )


def get_sub_resources(
    session: Session, service_name: ServiceName, resource: Boto3ServiceResource
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
