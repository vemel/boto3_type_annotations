"Helper functions for dax service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_dax.client import Client
from mypy_boto3_dax.paginator import (
    DescribeClustersPaginator,
    DescribeDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeParameterGroupsPaginator,
    DescribeParametersPaginator,
    DescribeSubnetGroupsPaginator,
    ListTagsPaginator,
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
    Equivalent of `boto3.client('dax')`, returns a correct type.
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
        return session.client("dax", **kwargs)
    return boto3.client("dax", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_clusters_paginator(client: Client) -> DescribeClustersPaginator:
    """
    Equivalent of `client.get_paginator('describe_clusters')`, returns a correct type.
    """
    return client.get_paginator("describe_clusters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_default_parameters_paginator(
    client: Client,
) -> DescribeDefaultParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_default_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_default_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_events_paginator(client: Client) -> DescribeEventsPaginator:
    """
    Equivalent of `client.get_paginator('describe_events')`, returns a correct type.
    """
    return client.get_paginator("describe_events")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_parameter_groups_paginator(
    client: Client,
) -> DescribeParameterGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_parameter_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_parameter_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_parameters_paginator(client: Client) -> DescribeParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_subnet_groups_paginator(
    client: Client,
) -> DescribeSubnetGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_subnet_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_subnet_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_paginator(client: Client) -> ListTagsPaginator:
    """
    Equivalent of `client.get_paginator('list_tags')`, returns a correct type.
    """
    return client.get_paginator("list_tags")
