"""
Parser for Boto3 ServiceResource sub-resource, produces `structures.Resource`
"""
import inspect
from typing import Dict, Type
from types import FunctionType


from boto3.docs.utils import is_resource_action
from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.resource import Resource
from mypy_boto3_builder.parsers.helpers import parse_attributes, parse_method
from mypy_boto3_builder.parsers.identifiers import parse_identifiers
from mypy_boto3_builder.parsers.parse_collections import parse_collections


def parse_resource(
    name: str, resource: Boto3ServiceResource, service_name: ServiceName
) -> Resource:
    """
    Parse boto3 sub Resource data.

    Arguments:
        resource -- Original boto3 resource.

    Returns:
        Resource structure.
    """
    result = Resource(
        name=name,
        docstring=(
            f"[{name} documentation]"
            f"({service_name.doc_link}.ServiceResource.{name})"
        ),
    )

    public_methods = get_resource_public_methods(resource.__class__)
    for method_name, public_method in public_methods.items():
        method = parse_method(name, method_name, public_method)
        result.methods.append(method)

    result.attributes.extend(parse_attributes(resource))
    result.attributes.extend(parse_identifiers(resource))

    collections = parse_collections(name, resource, service_name)
    for collection in collections:
        result.collections.append(collection)
        result.attributes.append(
            Attribute(
                collection.attribute_name, InternalImport(collection.name, service_name)
            )
        )

    return result


def get_resource_public_methods(
    resource_class: Type[Boto3ServiceResource],
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
