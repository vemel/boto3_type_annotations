"Helper functions for connect service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_connect.client import Client
from mypy_boto3_connect.paginator import (
    GetMetricDataPaginator,
    ListContactFlowsPaginator,
    ListHoursOfOperationsPaginator,
    ListPhoneNumbersPaginator,
    ListQueuesPaginator,
    ListRoutingProfilesPaginator,
    ListSecurityProfilesPaginator,
    ListUserHierarchyGroupsPaginator,
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
    Equivalent of `boto3.client('connect')`, returns a correct type.
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
        return session.client("connect", **kwargs)
    return boto3.client("connect", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_metric_data_paginator(client: Client) -> GetMetricDataPaginator:
    """
    Equivalent of `client.get_paginator('get_metric_data')`, returns a correct type.
    """
    return client.get_paginator("get_metric_data")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_contact_flows_paginator(client: Client) -> ListContactFlowsPaginator:
    """
    Equivalent of `client.get_paginator('list_contact_flows')`, returns a correct type.
    """
    return client.get_paginator("list_contact_flows")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_hours_of_operations_paginator(
    client: Client,
) -> ListHoursOfOperationsPaginator:
    """
    Equivalent of `client.get_paginator('list_hours_of_operations')`, returns a correct type.
    """
    return client.get_paginator("list_hours_of_operations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_phone_numbers_paginator(client: Client) -> ListPhoneNumbersPaginator:
    """
    Equivalent of `client.get_paginator('list_phone_numbers')`, returns a correct type.
    """
    return client.get_paginator("list_phone_numbers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_queues_paginator(client: Client) -> ListQueuesPaginator:
    """
    Equivalent of `client.get_paginator('list_queues')`, returns a correct type.
    """
    return client.get_paginator("list_queues")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_routing_profiles_paginator(client: Client) -> ListRoutingProfilesPaginator:
    """
    Equivalent of `client.get_paginator('list_routing_profiles')`, returns a correct type.
    """
    return client.get_paginator("list_routing_profiles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_security_profiles_paginator(
    client: Client,
) -> ListSecurityProfilesPaginator:
    """
    Equivalent of `client.get_paginator('list_security_profiles')`, returns a correct type.
    """
    return client.get_paginator("list_security_profiles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_user_hierarchy_groups_paginator(
    client: Client,
) -> ListUserHierarchyGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_user_hierarchy_groups')`, returns a correct type.
    """
    return client.get_paginator("list_user_hierarchy_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_users_paginator(client: Client) -> ListUsersPaginator:
    """
    Equivalent of `client.get_paginator('list_users')`, returns a correct type.
    """
    return client.get_paginator("list_users")
