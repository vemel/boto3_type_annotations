"Helper functions for xray service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_xray.client import Client
from mypy_boto3_xray.paginator import (
    BatchGetTracesPaginator,
    GetGroupsPaginator,
    GetSamplingRulesPaginator,
    GetSamplingStatisticSummariesPaginator,
    GetServiceGraphPaginator,
    GetTimeSeriesServiceStatisticsPaginator,
    GetTraceGraphPaginator,
    GetTraceSummariesPaginator,
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
    Equivalent of `boto3.client('xray')`, returns a correct type.
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
        return session.client("xray", **kwargs)
    return boto3.client("xray", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_batch_get_traces_paginator(client: Client) -> BatchGetTracesPaginator:
    """
    Equivalent of `client.get_paginator('batch_get_traces')`, returns a correct type.
    """
    return client.get_paginator("batch_get_traces")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_groups_paginator(client: Client) -> GetGroupsPaginator:
    """
    Equivalent of `client.get_paginator('get_groups')`, returns a correct type.
    """
    return client.get_paginator("get_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_sampling_rules_paginator(client: Client) -> GetSamplingRulesPaginator:
    """
    Equivalent of `client.get_paginator('get_sampling_rules')`, returns a correct type.
    """
    return client.get_paginator("get_sampling_rules")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_sampling_statistic_summaries_paginator(
    client: Client,
) -> GetSamplingStatisticSummariesPaginator:
    """
    Equivalent of `client.get_paginator('get_sampling_statistic_summaries')`, returns a correct type.
    """
    return client.get_paginator("get_sampling_statistic_summaries")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_service_graph_paginator(client: Client) -> GetServiceGraphPaginator:
    """
    Equivalent of `client.get_paginator('get_service_graph')`, returns a correct type.
    """
    return client.get_paginator("get_service_graph")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_time_series_service_statistics_paginator(
    client: Client,
) -> GetTimeSeriesServiceStatisticsPaginator:
    """
    Equivalent of `client.get_paginator('get_time_series_service_statistics')`, returns a correct type.
    """
    return client.get_paginator("get_time_series_service_statistics")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_trace_graph_paginator(client: Client) -> GetTraceGraphPaginator:
    """
    Equivalent of `client.get_paginator('get_trace_graph')`, returns a correct type.
    """
    return client.get_paginator("get_trace_graph")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_trace_summaries_paginator(client: Client) -> GetTraceSummariesPaginator:
    """
    Equivalent of `client.get_paginator('get_trace_summaries')`, returns a correct type.
    """
    return client.get_paginator("get_trace_summaries")
