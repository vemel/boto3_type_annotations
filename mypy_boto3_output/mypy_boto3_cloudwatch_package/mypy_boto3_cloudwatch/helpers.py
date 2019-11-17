"Helper functions for cloudwatch service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_cloudwatch.client import Client
from mypy_boto3_cloudwatch.paginator import (
    DescribeAlarmHistoryPaginator,
    DescribeAlarmsPaginator,
    GetMetricDataPaginator,
    ListDashboardsPaginator,
    ListMetricsPaginator,
)
from mypy_boto3_cloudwatch.service_resource import ServiceResource
from mypy_boto3_cloudwatch.waiter import AlarmExistsWaiter

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
    Equivalent of `boto3.client('cloudwatch')`, returns a correct type.
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
        return session.client("cloudwatch", **kwargs)
    return boto3.client("cloudwatch", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_resource(
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
) -> ServiceResource:
    """
    Equivalent of `boto3.resource('cloudwatch')`, returns a correct type.
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
        return session.resource("cloudwatch", **kwargs)
    return boto3.resource("cloudwatch", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_alarm_history_paginator(
    client: Client,
) -> DescribeAlarmHistoryPaginator:
    """
    Equivalent of `client.get_paginator('describe_alarm_history')`, returns a correct type.
    """
    return client.get_paginator("describe_alarm_history")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_alarms_paginator(client: Client) -> DescribeAlarmsPaginator:
    """
    Equivalent of `client.get_paginator('describe_alarms')`, returns a correct type.
    """
    return client.get_paginator("describe_alarms")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_metric_data_paginator(client: Client) -> GetMetricDataPaginator:
    """
    Equivalent of `client.get_paginator('get_metric_data')`, returns a correct type.
    """
    return client.get_paginator("get_metric_data")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_dashboards_paginator(client: Client) -> ListDashboardsPaginator:
    """
    Equivalent of `client.get_paginator('list_dashboards')`, returns a correct type.
    """
    return client.get_paginator("list_dashboards")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_metrics_paginator(client: Client) -> ListMetricsPaginator:
    """
    Equivalent of `client.get_paginator('list_metrics')`, returns a correct type.
    """
    return client.get_paginator("list_metrics")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_alarm_exists_waiter(client: Client) -> AlarmExistsWaiter:
    """
    Equivalent of `client.get_waiter('alarm_exists')`, returns a correct type.
    """
    return client.get_waiter("alarm_exists")
