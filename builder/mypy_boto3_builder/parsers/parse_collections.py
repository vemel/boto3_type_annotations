"""
Boto3 ServiceResource collections parser, produces `structures.Collection`.
"""
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.strings import get_class_prefix
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.parsers.helpers import get_public_methods, parse_method


def parse_collections(
    parent_name: str, resource: Boto3ServiceResource, service_name: ServiceName
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
        collection_record = Collection(
            name=f"{parent_name}{get_class_prefix(collection.name)}Collection",
            attribute_name=collection.name,
            docstring=(
                f"[{parent_name}.{collection.name} documentation]"
                f"({service_name.doc_link}.{parent_name}.{collection.name})"
            ),
            type=InternalImport(name=collection.name, service_name=service_name),
        )
        public_methods = get_public_methods(collection_class)

        for method_name, public_method in public_methods.items():
            method = parse_method(collection.name, method_name, public_method)
            collection_record.methods.append(method)

        result.append(collection_record)
    return result
