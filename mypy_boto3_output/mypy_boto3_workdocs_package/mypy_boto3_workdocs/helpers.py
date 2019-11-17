"Helper functions for workdocs service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_workdocs.client import Client
from mypy_boto3_workdocs.paginator import (
    DescribeActivitiesPaginator,
    DescribeCommentsPaginator,
    DescribeDocumentVersionsPaginator,
    DescribeFolderContentsPaginator,
    DescribeGroupsPaginator,
    DescribeNotificationSubscriptionsPaginator,
    DescribeResourcePermissionsPaginator,
    DescribeRootFoldersPaginator,
    DescribeUsersPaginator,
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
    Equivalent of `boto3.client('workdocs')`, returns a correct type.
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
        return session.client("workdocs", **kwargs)
    return boto3.client("workdocs", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_activities_paginator(client: Client) -> DescribeActivitiesPaginator:
    """
    Equivalent of `client.get_paginator('describe_activities')`, returns a correct type.
    """
    return client.get_paginator("describe_activities")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_comments_paginator(client: Client) -> DescribeCommentsPaginator:
    """
    Equivalent of `client.get_paginator('describe_comments')`, returns a correct type.
    """
    return client.get_paginator("describe_comments")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_document_versions_paginator(
    client: Client,
) -> DescribeDocumentVersionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_document_versions')`, returns a correct type.
    """
    return client.get_paginator("describe_document_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_folder_contents_paginator(
    client: Client,
) -> DescribeFolderContentsPaginator:
    """
    Equivalent of `client.get_paginator('describe_folder_contents')`, returns a correct type.
    """
    return client.get_paginator("describe_folder_contents")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_groups_paginator(client: Client) -> DescribeGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_notification_subscriptions_paginator(
    client: Client,
) -> DescribeNotificationSubscriptionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_notification_subscriptions')`, returns a correct type.
    """
    return client.get_paginator("describe_notification_subscriptions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_resource_permissions_paginator(
    client: Client,
) -> DescribeResourcePermissionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_resource_permissions')`, returns a correct type.
    """
    return client.get_paginator("describe_resource_permissions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_root_folders_paginator(client: Client) -> DescribeRootFoldersPaginator:
    """
    Equivalent of `client.get_paginator('describe_root_folders')`, returns a correct type.
    """
    return client.get_paginator("describe_root_folders")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_users_paginator(client: Client) -> DescribeUsersPaginator:
    """
    Equivalent of `client.get_paginator('describe_users')`, returns a correct type.
    """
    return client.get_paginator("describe_users")
