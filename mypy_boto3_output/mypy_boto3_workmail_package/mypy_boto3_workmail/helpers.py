"Helper functions for workmail service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_workmail.client import Client
from mypy_boto3_workmail.paginator import (
    ListAliasesPaginator,
    ListGroupMembersPaginator,
    ListGroupsPaginator,
    ListMailboxPermissionsPaginator,
    ListOrganizationsPaginator,
    ListResourceDelegatesPaginator,
    ListResourcesPaginator,
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
    Equivalent of `boto3.client('workmail')`, returns a correct type.
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
        return session.client("workmail", **kwargs)
    return boto3.client("workmail", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_aliases_paginator(client: Client) -> ListAliasesPaginator:
    """
    Equivalent of `client.get_paginator('list_aliases')`, returns a correct type.
    """
    return client.get_paginator("list_aliases")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_group_members_paginator(client: Client) -> ListGroupMembersPaginator:
    """
    Equivalent of `client.get_paginator('list_group_members')`, returns a correct type.
    """
    return client.get_paginator("list_group_members")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_groups_paginator(client: Client) -> ListGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_groups')`, returns a correct type.
    """
    return client.get_paginator("list_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_mailbox_permissions_paginator(
    client: Client,
) -> ListMailboxPermissionsPaginator:
    """
    Equivalent of `client.get_paginator('list_mailbox_permissions')`, returns a correct type.
    """
    return client.get_paginator("list_mailbox_permissions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_organizations_paginator(client: Client) -> ListOrganizationsPaginator:
    """
    Equivalent of `client.get_paginator('list_organizations')`, returns a correct type.
    """
    return client.get_paginator("list_organizations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resource_delegates_paginator(
    client: Client,
) -> ListResourceDelegatesPaginator:
    """
    Equivalent of `client.get_paginator('list_resource_delegates')`, returns a correct type.
    """
    return client.get_paginator("list_resource_delegates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resources_paginator(client: Client) -> ListResourcesPaginator:
    """
    Equivalent of `client.get_paginator('list_resources')`, returns a correct type.
    """
    return client.get_paginator("list_resources")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_users_paginator(client: Client) -> ListUsersPaginator:
    """
    Equivalent of `client.get_paginator('list_users')`, returns a correct type.
    """
    return client.get_paginator("list_users")
