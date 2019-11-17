"Helper functions for cognito-idp service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_cognito_idp.client import Client
from mypy_boto3_cognito_idp.paginator import (
    AdminListGroupsForUserPaginator,
    AdminListUserAuthEventsPaginator,
    ListGroupsPaginator,
    ListIdentityProvidersPaginator,
    ListResourceServersPaginator,
    ListUserPoolClientsPaginator,
    ListUserPoolsPaginator,
    ListUsersInGroupPaginator,
    ListUsersPaginator,
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
    Equivalent of `boto3.client('cognito-idp')`, returns a correct type.
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
        return session.client("cognito-idp", **kwargs)
    return boto3.client("cognito-idp", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_admin_list_groups_for_user_paginator(
    client: Client,
) -> AdminListGroupsForUserPaginator:
    """
    Equivalent of `client.get_paginator('admin_list_groups_for_user')`, returns a correct type.
    """
    return client.get_paginator("admin_list_groups_for_user")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_admin_list_user_auth_events_paginator(
    client: Client,
) -> AdminListUserAuthEventsPaginator:
    """
    Equivalent of `client.get_paginator('admin_list_user_auth_events')`, returns a correct type.
    """
    return client.get_paginator("admin_list_user_auth_events")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_groups_paginator(client: Client) -> ListGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_groups')`, returns a correct type.
    """
    return client.get_paginator("list_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_identity_providers_paginator(
    client: Client,
) -> ListIdentityProvidersPaginator:
    """
    Equivalent of `client.get_paginator('list_identity_providers')`, returns a correct type.
    """
    return client.get_paginator("list_identity_providers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resource_servers_paginator(client: Client) -> ListResourceServersPaginator:
    """
    Equivalent of `client.get_paginator('list_resource_servers')`, returns a correct type.
    """
    return client.get_paginator("list_resource_servers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_user_pool_clients_paginator(
    client: Client,
) -> ListUserPoolClientsPaginator:
    """
    Equivalent of `client.get_paginator('list_user_pool_clients')`, returns a correct type.
    """
    return client.get_paginator("list_user_pool_clients")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_user_pools_paginator(client: Client) -> ListUserPoolsPaginator:
    """
    Equivalent of `client.get_paginator('list_user_pools')`, returns a correct type.
    """
    return client.get_paginator("list_user_pools")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_users_paginator(client: Client) -> ListUsersPaginator:
    """
    Equivalent of `client.get_paginator('list_users')`, returns a correct type.
    """
    return client.get_paginator("list_users")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_users_in_group_paginator(client: Client) -> ListUsersInGroupPaginator:
    """
    Equivalent of `client.get_paginator('list_users_in_group')`, returns a correct type.
    """
    return client.get_paginator("list_users_in_group")
