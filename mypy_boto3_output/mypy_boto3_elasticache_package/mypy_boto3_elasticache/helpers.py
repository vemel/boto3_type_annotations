"Helper functions for elasticache service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_elasticache.client import Client
from mypy_boto3_elasticache.paginator import (
    DescribeCacheClustersPaginator,
    DescribeCacheEngineVersionsPaginator,
    DescribeCacheParameterGroupsPaginator,
    DescribeCacheParametersPaginator,
    DescribeCacheSecurityGroupsPaginator,
    DescribeCacheSubnetGroupsPaginator,
    DescribeEngineDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeReplicationGroupsPaginator,
    DescribeReservedCacheNodesOfferingsPaginator,
    DescribeReservedCacheNodesPaginator,
    DescribeServiceUpdatesPaginator,
    DescribeSnapshotsPaginator,
    DescribeUpdateActionsPaginator,
)
from mypy_boto3_elasticache.waiter import (
    CacheClusterAvailableWaiter,
    CacheClusterDeletedWaiter,
    ReplicationGroupAvailableWaiter,
    ReplicationGroupDeletedWaiter,
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
    Equivalent of `boto3.client('elasticache')`, returns a correct type.
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
        return session.client("elasticache", **kwargs)
    return boto3.client("elasticache", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cache_clusters_paginator(
    client: Client,
) -> DescribeCacheClustersPaginator:
    """
    Equivalent of `client.get_paginator('describe_cache_clusters')`, returns a correct type.
    """
    return client.get_paginator("describe_cache_clusters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cache_engine_versions_paginator(
    client: Client,
) -> DescribeCacheEngineVersionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_cache_engine_versions')`, returns a correct type.
    """
    return client.get_paginator("describe_cache_engine_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cache_parameter_groups_paginator(
    client: Client,
) -> DescribeCacheParameterGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_cache_parameter_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_cache_parameter_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cache_parameters_paginator(
    client: Client,
) -> DescribeCacheParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_cache_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_cache_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cache_security_groups_paginator(
    client: Client,
) -> DescribeCacheSecurityGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_cache_security_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_cache_security_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cache_subnet_groups_paginator(
    client: Client,
) -> DescribeCacheSubnetGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_cache_subnet_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_cache_subnet_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_engine_default_parameters_paginator(
    client: Client,
) -> DescribeEngineDefaultParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_engine_default_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_engine_default_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_events_paginator(client: Client) -> DescribeEventsPaginator:
    """
    Equivalent of `client.get_paginator('describe_events')`, returns a correct type.
    """
    return client.get_paginator("describe_events")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_replication_groups_paginator(
    client: Client,
) -> DescribeReplicationGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_replication_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_replication_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_reserved_cache_nodes_paginator(
    client: Client,
) -> DescribeReservedCacheNodesPaginator:
    """
    Equivalent of `client.get_paginator('describe_reserved_cache_nodes')`, returns a correct type.
    """
    return client.get_paginator("describe_reserved_cache_nodes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_reserved_cache_nodes_offerings_paginator(
    client: Client,
) -> DescribeReservedCacheNodesOfferingsPaginator:
    """
    Equivalent of `client.get_paginator('describe_reserved_cache_nodes_offerings')`, returns a correct type.
    """
    return client.get_paginator("describe_reserved_cache_nodes_offerings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_service_updates_paginator(
    client: Client,
) -> DescribeServiceUpdatesPaginator:
    """
    Equivalent of `client.get_paginator('describe_service_updates')`, returns a correct type.
    """
    return client.get_paginator("describe_service_updates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_snapshots_paginator(client: Client) -> DescribeSnapshotsPaginator:
    """
    Equivalent of `client.get_paginator('describe_snapshots')`, returns a correct type.
    """
    return client.get_paginator("describe_snapshots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_update_actions_paginator(
    client: Client,
) -> DescribeUpdateActionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_update_actions')`, returns a correct type.
    """
    return client.get_paginator("describe_update_actions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_cache_cluster_available_waiter(client: Client) -> CacheClusterAvailableWaiter:
    """
    Equivalent of `client.get_waiter('cache_cluster_available')`, returns a correct type.
    """
    return client.get_waiter("cache_cluster_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_cache_cluster_deleted_waiter(client: Client) -> CacheClusterDeletedWaiter:
    """
    Equivalent of `client.get_waiter('cache_cluster_deleted')`, returns a correct type.
    """
    return client.get_waiter("cache_cluster_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_replication_group_available_waiter(
    client: Client,
) -> ReplicationGroupAvailableWaiter:
    """
    Equivalent of `client.get_waiter('replication_group_available')`, returns a correct type.
    """
    return client.get_waiter("replication_group_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_replication_group_deleted_waiter(
    client: Client,
) -> ReplicationGroupDeletedWaiter:
    """
    Equivalent of `client.get_waiter('replication_group_deleted')`, returns a correct type.
    """
    return client.get_waiter("replication_group_deleted")
