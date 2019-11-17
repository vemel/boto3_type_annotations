"Helper functions for ds service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_ds.client import Client
from mypy_boto3_ds.paginator import (
    DescribeDirectoriesPaginator,
    DescribeDomainControllersPaginator,
    DescribeSharedDirectoriesPaginator,
    DescribeSnapshotsPaginator,
    DescribeTrustsPaginator,
    ListIpRoutesPaginator,
    ListLogSubscriptionsPaginator,
    ListSchemaExtensionsPaginator,
    ListTagsForResourcePaginator,
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
    Equivalent of `boto3.client('ds')`, returns a correct type.
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
        return session.client("ds", **kwargs)
    return boto3.client("ds", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_directories_paginator(client: Client) -> DescribeDirectoriesPaginator:
    """
    Equivalent of `client.get_paginator('describe_directories')`, returns a correct type.
    """
    return client.get_paginator("describe_directories")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_domain_controllers_paginator(
    client: Client,
) -> DescribeDomainControllersPaginator:
    """
    Equivalent of `client.get_paginator('describe_domain_controllers')`, returns a correct type.
    """
    return client.get_paginator("describe_domain_controllers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_shared_directories_paginator(
    client: Client,
) -> DescribeSharedDirectoriesPaginator:
    """
    Equivalent of `client.get_paginator('describe_shared_directories')`, returns a correct type.
    """
    return client.get_paginator("describe_shared_directories")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_snapshots_paginator(client: Client) -> DescribeSnapshotsPaginator:
    """
    Equivalent of `client.get_paginator('describe_snapshots')`, returns a correct type.
    """
    return client.get_paginator("describe_snapshots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_trusts_paginator(client: Client) -> DescribeTrustsPaginator:
    """
    Equivalent of `client.get_paginator('describe_trusts')`, returns a correct type.
    """
    return client.get_paginator("describe_trusts")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_ip_routes_paginator(client: Client) -> ListIpRoutesPaginator:
    """
    Equivalent of `client.get_paginator('list_ip_routes')`, returns a correct type.
    """
    return client.get_paginator("list_ip_routes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_log_subscriptions_paginator(
    client: Client,
) -> ListLogSubscriptionsPaginator:
    """
    Equivalent of `client.get_paginator('list_log_subscriptions')`, returns a correct type.
    """
    return client.get_paginator("list_log_subscriptions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_schema_extensions_paginator(
    client: Client,
) -> ListSchemaExtensionsPaginator:
    """
    Equivalent of `client.get_paginator('list_schema_extensions')`, returns a correct type.
    """
    return client.get_paginator("list_schema_extensions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_for_resource_paginator(
    client: Client,
) -> ListTagsForResourcePaginator:
    """
    Equivalent of `client.get_paginator('list_tags_for_resource')`, returns a correct type.
    """
    return client.get_paginator("list_tags_for_resource")
