"Helper functions for organizations service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_organizations.client import Client
from mypy_boto3_organizations.paginator import (
    ListAWSServiceAccessForOrganizationPaginator,
    ListAccountsForParentPaginator,
    ListAccountsPaginator,
    ListChildrenPaginator,
    ListCreateAccountStatusPaginator,
    ListHandshakesForAccountPaginator,
    ListHandshakesForOrganizationPaginator,
    ListOrganizationalUnitsForParentPaginator,
    ListParentsPaginator,
    ListPoliciesForTargetPaginator,
    ListPoliciesPaginator,
    ListRootsPaginator,
    ListTagsForResourcePaginator,
    ListTargetsForPolicyPaginator,
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
    Equivalent of `boto3.client('organizations')`, returns a correct type.
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
        return session.client("organizations", **kwargs)
    return boto3.client("organizations", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_aws_service_access_for_organization_paginator(
    client: Client,
) -> ListAWSServiceAccessForOrganizationPaginator:
    """
    Equivalent of `client.get_paginator('list_aws_service_access_for_organization')`, returns a correct type.
    """
    return client.get_paginator("list_aws_service_access_for_organization")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_accounts_paginator(client: Client) -> ListAccountsPaginator:
    """
    Equivalent of `client.get_paginator('list_accounts')`, returns a correct type.
    """
    return client.get_paginator("list_accounts")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_accounts_for_parent_paginator(
    client: Client,
) -> ListAccountsForParentPaginator:
    """
    Equivalent of `client.get_paginator('list_accounts_for_parent')`, returns a correct type.
    """
    return client.get_paginator("list_accounts_for_parent")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_children_paginator(client: Client) -> ListChildrenPaginator:
    """
    Equivalent of `client.get_paginator('list_children')`, returns a correct type.
    """
    return client.get_paginator("list_children")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_create_account_status_paginator(
    client: Client,
) -> ListCreateAccountStatusPaginator:
    """
    Equivalent of `client.get_paginator('list_create_account_status')`, returns a correct type.
    """
    return client.get_paginator("list_create_account_status")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_handshakes_for_account_paginator(
    client: Client,
) -> ListHandshakesForAccountPaginator:
    """
    Equivalent of `client.get_paginator('list_handshakes_for_account')`, returns a correct type.
    """
    return client.get_paginator("list_handshakes_for_account")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_handshakes_for_organization_paginator(
    client: Client,
) -> ListHandshakesForOrganizationPaginator:
    """
    Equivalent of `client.get_paginator('list_handshakes_for_organization')`, returns a correct type.
    """
    return client.get_paginator("list_handshakes_for_organization")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_organizational_units_for_parent_paginator(
    client: Client,
) -> ListOrganizationalUnitsForParentPaginator:
    """
    Equivalent of `client.get_paginator('list_organizational_units_for_parent')`, returns a correct type.
    """
    return client.get_paginator("list_organizational_units_for_parent")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_parents_paginator(client: Client) -> ListParentsPaginator:
    """
    Equivalent of `client.get_paginator('list_parents')`, returns a correct type.
    """
    return client.get_paginator("list_parents")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_policies_paginator(client: Client) -> ListPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_policies')`, returns a correct type.
    """
    return client.get_paginator("list_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_policies_for_target_paginator(
    client: Client,
) -> ListPoliciesForTargetPaginator:
    """
    Equivalent of `client.get_paginator('list_policies_for_target')`, returns a correct type.
    """
    return client.get_paginator("list_policies_for_target")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_roots_paginator(client: Client) -> ListRootsPaginator:
    """
    Equivalent of `client.get_paginator('list_roots')`, returns a correct type.
    """
    return client.get_paginator("list_roots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_for_resource_paginator(
    client: Client,
) -> ListTagsForResourcePaginator:
    """
    Equivalent of `client.get_paginator('list_tags_for_resource')`, returns a correct type.
    """
    return client.get_paginator("list_tags_for_resource")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_targets_for_policy_paginator(
    client: Client,
) -> ListTargetsForPolicyPaginator:
    """
    Equivalent of `client.get_paginator('list_targets_for_policy')`, returns a correct type.
    """
    return client.get_paginator("list_targets_for_policy")
