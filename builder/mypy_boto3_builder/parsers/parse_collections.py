"""
Boto3 ServiceResource collections parser, produces `structures.Collection`.
"""
from inspect import getdoc
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.utils.strings import get_class_prefix
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.parsers.helpers import get_public_methods, parse_method


def parse_collections(
    parent_name: str, resource: Boto3ServiceResource
) -> List[Collection]:
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
                name=f"{parent_name}{get_class_prefix(collection.name)}Collection",
                attribute_name=collection.name,
                docstring=getdoc(collection) or "",
                type=InternalImport(
                    name=collection.name,
                    service_name=ServiceName(resource.meta.service_name),
                ),
                methods=methods,
            )
        )
    return result
