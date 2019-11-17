"Helper functions for logs service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_logs.client import Client
from mypy_boto3_logs.paginator import (
    DescribeDestinationsPaginator,
    DescribeExportTasksPaginator,
    DescribeLogGroupsPaginator,
    DescribeLogStreamsPaginator,
    DescribeMetricFiltersPaginator,
    DescribeQueriesPaginator,
    DescribeResourcePoliciesPaginator,
    DescribeSubscriptionFiltersPaginator,
    FilterLogEventsPaginator,
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
    Equivalent of `boto3.client('logs')`, returns a correct type.
    """
    kwargs = {}
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
        return session.client("logs", **kwargs)
    return boto3.client("logs", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_destinations_paginator(
    client: Client,
) -> DescribeDestinationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_destinations')`, returns a correct type.
    """
    return client.get_waiter("describe_destinations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_export_tasks_paginator(client: Client) -> DescribeExportTasksPaginator:
    """
    Equivalent of `client.get_paginator('describe_export_tasks')`, returns a correct type.
    """
    return client.get_waiter("describe_export_tasks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_log_groups_paginator(client: Client) -> DescribeLogGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_log_groups')`, returns a correct type.
    """
    return client.get_waiter("describe_log_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_log_streams_paginator(client: Client) -> DescribeLogStreamsPaginator:
    """
    Equivalent of `client.get_paginator('describe_log_streams')`, returns a correct type.
    """
    return client.get_waiter("describe_log_streams")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_metric_filters_paginator(
    client: Client,
) -> DescribeMetricFiltersPaginator:
    """
    Equivalent of `client.get_paginator('describe_metric_filters')`, returns a correct type.
    """
    return client.get_waiter("describe_metric_filters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_queries_paginator(client: Client) -> DescribeQueriesPaginator:
    """
    Equivalent of `client.get_paginator('describe_queries')`, returns a correct type.
    """
    return client.get_waiter("describe_queries")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_resource_policies_paginator(
    client: Client,
) -> DescribeResourcePoliciesPaginator:
    """
    Equivalent of `client.get_paginator('describe_resource_policies')`, returns a correct type.
    """
    return client.get_waiter("describe_resource_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_subscription_filters_paginator(
    client: Client,
) -> DescribeSubscriptionFiltersPaginator:
    """
    Equivalent of `client.get_paginator('describe_subscription_filters')`, returns a correct type.
    """
    return client.get_waiter("describe_subscription_filters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_filter_log_events_paginator(client: Client) -> FilterLogEventsPaginator:
    """
    Equivalent of `client.get_paginator('filter_log_events')`, returns a correct type.
    """
    return client.get_waiter("filter_log_events")