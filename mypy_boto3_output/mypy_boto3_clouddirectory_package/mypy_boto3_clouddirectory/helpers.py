"Helper functions for clouddirectory service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_clouddirectory.client import Client
from mypy_boto3_clouddirectory.paginator import (
    ListAppliedSchemaArnsPaginator,
    ListAttachedIndicesPaginator,
    ListDevelopmentSchemaArnsPaginator,
    ListDirectoriesPaginator,
    ListFacetAttributesPaginator,
    ListFacetNamesPaginator,
    ListIncomingTypedLinksPaginator,
    ListIndexPaginator,
    ListManagedSchemaArnsPaginator,
    ListObjectAttributesPaginator,
    ListObjectParentPathsPaginator,
    ListObjectPoliciesPaginator,
    ListOutgoingTypedLinksPaginator,
    ListPolicyAttachmentsPaginator,
    ListPublishedSchemaArnsPaginator,
    ListTagsForResourcePaginator,
    ListTypedLinkFacetAttributesPaginator,
    ListTypedLinkFacetNamesPaginator,
    LookupPolicyPaginator,
)

# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_client(
    session: Session = None,
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Client:
    """
    Equivalent of `boto3.client('clouddirectory')`, returns a correct type.
    """
    kwargs: Dict[str, Any] = {}
    if region_name is not None:
        kwargs["region_name"] = region_name
    if api_version is not None:
        kwargs["api_version"] = api_version
    if use_ssl is not None:
        kwargs["use_ssl"] = use_ssl
    if verify is not None:
        kwargs["verify"] = verify
    if endpoint_url is not None:
        kwargs["endpoint_url"] = endpoint_url
    if aws_access_key_id is not None:
        kwargs["aws_access_key_id"] = aws_access_key_id
    if aws_secret_access_key is not None:
        kwargs["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token is not None:
        kwargs["aws_session_token"] = aws_session_token
    if config is not None:
        kwargs["config"] = config
    if session is not None:
        return session.client("clouddirectory", **kwargs)
    return boto3.client("clouddirectory", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_applied_schema_arns_paginator(
    client: Client,
) -> ListAppliedSchemaArnsPaginator:
    """
    Equivalent of `client.get_paginator('list_applied_schema_arns')`, returns a correct type.
    """
    return client.get_paginator("list_applied_schema_arns")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_attached_indices_paginator(client: Client) -> ListAttachedIndicesPaginator:
    """
    Equivalent of `client.get_paginator('list_attached_indices')`, returns a correct type.
    """
    return client.get_paginator("list_attached_indices")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_development_schema_arns_paginator(
    client: Client,
) -> ListDevelopmentSchemaArnsPaginator:
    """
    Equivalent of `client.get_paginator('list_development_schema_arns')`, returns a correct type.
    """
    return client.get_paginator("list_development_schema_arns")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_directories_paginator(client: Client) -> ListDirectoriesPaginator:
    """
    Equivalent of `client.get_paginator('list_directories')`, returns a correct type.
    """
    return client.get_paginator("list_directories")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_facet_attributes_paginator(client: Client) -> ListFacetAttributesPaginator:
    """
    Equivalent of `client.get_paginator('list_facet_attributes')`, returns a correct type.
    """
    return client.get_paginator("list_facet_attributes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_facet_names_paginator(client: Client) -> ListFacetNamesPaginator:
    """
    Equivalent of `client.get_paginator('list_facet_names')`, returns a correct type.
    """
    return client.get_paginator("list_facet_names")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_incoming_typed_links_paginator(
    client: Client,
) -> ListIncomingTypedLinksPaginator:
    """
    Equivalent of `client.get_paginator('list_incoming_typed_links')`, returns a correct type.
    """
    return client.get_paginator("list_incoming_typed_links")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_index_paginator(client: Client) -> ListIndexPaginator:
    """
    Equivalent of `client.get_paginator('list_index')`, returns a correct type.
    """
    return client.get_paginator("list_index")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_managed_schema_arns_paginator(
    client: Client,
) -> ListManagedSchemaArnsPaginator:
    """
    Equivalent of `client.get_paginator('list_managed_schema_arns')`, returns a correct type.
    """
    return client.get_paginator("list_managed_schema_arns")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_object_attributes_paginator(
    client: Client,
) -> ListObjectAttributesPaginator:
    """
    Equivalent of `client.get_paginator('list_object_attributes')`, returns a correct type.
    """
    return client.get_paginator("list_object_attributes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_object_parent_paths_paginator(
    client: Client,
) -> ListObjectParentPathsPaginator:
    """
    Equivalent of `client.get_paginator('list_object_parent_paths')`, returns a correct type.
    """
    return client.get_paginator("list_object_parent_paths")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_object_policies_paginator(client: Client) -> ListObjectPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_object_policies')`, returns a correct type.
    """
    return client.get_paginator("list_object_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_outgoing_typed_links_paginator(
    client: Client,
) -> ListOutgoingTypedLinksPaginator:
    """
    Equivalent of `client.get_paginator('list_outgoing_typed_links')`, returns a correct type.
    """
    return client.get_paginator("list_outgoing_typed_links")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_policy_attachments_paginator(
    client: Client,
) -> ListPolicyAttachmentsPaginator:
    """
    Equivalent of `client.get_paginator('list_policy_attachments')`, returns a correct type.
    """
    return client.get_paginator("list_policy_attachments")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_published_schema_arns_paginator(
    client: Client,
) -> ListPublishedSchemaArnsPaginator:
    """
    Equivalent of `client.get_paginator('list_published_schema_arns')`, returns a correct type.
    """
    return client.get_paginator("list_published_schema_arns")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_for_resource_paginator(
    client: Client,
) -> ListTagsForResourcePaginator:
    """
    Equivalent of `client.get_paginator('list_tags_for_resource')`, returns a correct type.
    """
    return client.get_paginator("list_tags_for_resource")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_typed_link_facet_attributes_paginator(
    client: Client,
) -> ListTypedLinkFacetAttributesPaginator:
    """
    Equivalent of `client.get_paginator('list_typed_link_facet_attributes')`, returns a correct type.
    """
    return client.get_paginator("list_typed_link_facet_attributes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_typed_link_facet_names_paginator(
    client: Client,
) -> ListTypedLinkFacetNamesPaginator:
    """
    Equivalent of `client.get_paginator('list_typed_link_facet_names')`, returns a correct type.
    """
    return client.get_paginator("list_typed_link_facet_names")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_lookup_policy_paginator(client: Client) -> LookupPolicyPaginator:
    """
    Equivalent of `client.get_paginator('lookup_policy')`, returns a correct type.
    """
    return client.get_paginator("lookup_policy")
