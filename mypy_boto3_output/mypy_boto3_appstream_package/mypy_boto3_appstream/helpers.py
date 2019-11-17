"Helper functions for appstream service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_appstream.client import Client
from mypy_boto3_appstream.paginator import (
    DescribeDirectoryConfigsPaginator,
    DescribeFleetsPaginator,
    DescribeImageBuildersPaginator,
    DescribeImagesPaginator,
    DescribeSessionsPaginator,
    DescribeStacksPaginator,
    DescribeUserStackAssociationsPaginator,
    DescribeUsersPaginator,
    ListAssociatedFleetsPaginator,
    ListAssociatedStacksPaginator,
)
from mypy_boto3_appstream.waiter import FleetStartedWaiter, FleetStoppedWaiter

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
    Equivalent of `boto3.client('appstream')`, returns a correct type.
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
        return session.client("appstream", **kwargs)
    return boto3.client("appstream", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_directory_configs_paginator(
    client: Client,
) -> DescribeDirectoryConfigsPaginator:
    """
    Equivalent of `client.get_paginator('describe_directory_configs')`, returns a correct type.
    """
    return client.get_paginator("describe_directory_configs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_fleets_paginator(client: Client) -> DescribeFleetsPaginator:
    """
    Equivalent of `client.get_paginator('describe_fleets')`, returns a correct type.
    """
    return client.get_paginator("describe_fleets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_image_builders_paginator(
    client: Client,
) -> DescribeImageBuildersPaginator:
    """
    Equivalent of `client.get_paginator('describe_image_builders')`, returns a correct type.
    """
    return client.get_paginator("describe_image_builders")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_images_paginator(client: Client) -> DescribeImagesPaginator:
    """
    Equivalent of `client.get_paginator('describe_images')`, returns a correct type.
    """
    return client.get_paginator("describe_images")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_sessions_paginator(client: Client) -> DescribeSessionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_sessions')`, returns a correct type.
    """
    return client.get_paginator("describe_sessions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_stacks_paginator(client: Client) -> DescribeStacksPaginator:
    """
    Equivalent of `client.get_paginator('describe_stacks')`, returns a correct type.
    """
    return client.get_paginator("describe_stacks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_user_stack_associations_paginator(
    client: Client,
) -> DescribeUserStackAssociationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_user_stack_associations')`, returns a correct type.
    """
    return client.get_paginator("describe_user_stack_associations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_users_paginator(client: Client) -> DescribeUsersPaginator:
    """
    Equivalent of `client.get_paginator('describe_users')`, returns a correct type.
    """
    return client.get_paginator("describe_users")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_associated_fleets_paginator(
    client: Client,
) -> ListAssociatedFleetsPaginator:
    """
    Equivalent of `client.get_paginator('list_associated_fleets')`, returns a correct type.
    """
    return client.get_paginator("list_associated_fleets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_associated_stacks_paginator(
    client: Client,
) -> ListAssociatedStacksPaginator:
    """
    Equivalent of `client.get_paginator('list_associated_stacks')`, returns a correct type.
    """
    return client.get_paginator("list_associated_stacks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_fleet_started_waiter(client: Client) -> FleetStartedWaiter:
    """
    Equivalent of `client.get_waiter('fleet_started')`, returns a correct type.
    """
    return client.get_waiter("fleet_started")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_fleet_stopped_waiter(client: Client) -> FleetStoppedWaiter:
    """
    Equivalent of `client.get_waiter('fleet_stopped')`, returns a correct type.
    """
    return client.get_waiter("fleet_stopped")
