"Helper functions for redshift service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_redshift.client import Client
from mypy_boto3_redshift.paginator import (
    DescribeClusterDbRevisionsPaginator,
    DescribeClusterParameterGroupsPaginator,
    DescribeClusterParametersPaginator,
    DescribeClusterSecurityGroupsPaginator,
    DescribeClusterSnapshotsPaginator,
    DescribeClusterSubnetGroupsPaginator,
    DescribeClusterTracksPaginator,
    DescribeClusterVersionsPaginator,
    DescribeClustersPaginator,
    DescribeDefaultClusterParametersPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeEventsPaginator,
    DescribeHsmClientCertificatesPaginator,
    DescribeHsmConfigurationsPaginator,
    DescribeNodeConfigurationOptionsPaginator,
    DescribeOrderableClusterOptionsPaginator,
    DescribeReservedNodeOfferingsPaginator,
    DescribeReservedNodesPaginator,
    DescribeSnapshotCopyGrantsPaginator,
    DescribeSnapshotSchedulesPaginator,
    DescribeTableRestoreStatusPaginator,
    DescribeTagsPaginator,
    GetReservedNodeExchangeOfferingsPaginator,
)
from mypy_boto3_redshift.waiter import (
    ClusterAvailableWaiter,
    ClusterDeletedWaiter,
    ClusterRestoredWaiter,
    SnapshotAvailableWaiter,
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
    Equivalent of `boto3.client('redshift')`, returns a correct type.
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
        return session.client("redshift", **kwargs)
    return boto3.client("redshift", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cluster_db_revisions_paginator(
    client: Client,
) -> DescribeClusterDbRevisionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_cluster_db_revisions')`, returns a correct type.
    """
    return client.get_paginator("describe_cluster_db_revisions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cluster_parameter_groups_paginator(
    client: Client,
) -> DescribeClusterParameterGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_cluster_parameter_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_cluster_parameter_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cluster_parameters_paginator(
    client: Client,
) -> DescribeClusterParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_cluster_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_cluster_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cluster_security_groups_paginator(
    client: Client,
) -> DescribeClusterSecurityGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_cluster_security_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_cluster_security_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cluster_snapshots_paginator(
    client: Client,
) -> DescribeClusterSnapshotsPaginator:
    """
    Equivalent of `client.get_paginator('describe_cluster_snapshots')`, returns a correct type.
    """
    return client.get_paginator("describe_cluster_snapshots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cluster_subnet_groups_paginator(
    client: Client,
) -> DescribeClusterSubnetGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_cluster_subnet_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_cluster_subnet_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cluster_tracks_paginator(
    client: Client,
) -> DescribeClusterTracksPaginator:
    """
    Equivalent of `client.get_paginator('describe_cluster_tracks')`, returns a correct type.
    """
    return client.get_paginator("describe_cluster_tracks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_cluster_versions_paginator(
    client: Client,
) -> DescribeClusterVersionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_cluster_versions')`, returns a correct type.
    """
    return client.get_paginator("describe_cluster_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_clusters_paginator(client: Client) -> DescribeClustersPaginator:
    """
    Equivalent of `client.get_paginator('describe_clusters')`, returns a correct type.
    """
    return client.get_paginator("describe_clusters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_default_cluster_parameters_paginator(
    client: Client,
) -> DescribeDefaultClusterParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_default_cluster_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_default_cluster_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_event_subscriptions_paginator(
    client: Client,
) -> DescribeEventSubscriptionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_event_subscriptions')`, returns a correct type.
    """
    return client.get_paginator("describe_event_subscriptions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_events_paginator(client: Client) -> DescribeEventsPaginator:
    """
    Equivalent of `client.get_paginator('describe_events')`, returns a correct type.
    """
    return client.get_paginator("describe_events")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_hsm_client_certificates_paginator(
    client: Client,
) -> DescribeHsmClientCertificatesPaginator:
    """
    Equivalent of `client.get_paginator('describe_hsm_client_certificates')`, returns a correct type.
    """
    return client.get_paginator("describe_hsm_client_certificates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_hsm_configurations_paginator(
    client: Client,
) -> DescribeHsmConfigurationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_hsm_configurations')`, returns a correct type.
    """
    return client.get_paginator("describe_hsm_configurations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_node_configuration_options_paginator(
    client: Client,
) -> DescribeNodeConfigurationOptionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_node_configuration_options')`, returns a correct type.
    """
    return client.get_paginator("describe_node_configuration_options")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_orderable_cluster_options_paginator(
    client: Client,
) -> DescribeOrderableClusterOptionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_orderable_cluster_options')`, returns a correct type.
    """
    return client.get_paginator("describe_orderable_cluster_options")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_reserved_node_offerings_paginator(
    client: Client,
) -> DescribeReservedNodeOfferingsPaginator:
    """
    Equivalent of `client.get_paginator('describe_reserved_node_offerings')`, returns a correct type.
    """
    return client.get_paginator("describe_reserved_node_offerings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_reserved_nodes_paginator(
    client: Client,
) -> DescribeReservedNodesPaginator:
    """
    Equivalent of `client.get_paginator('describe_reserved_nodes')`, returns a correct type.
    """
    return client.get_paginator("describe_reserved_nodes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_snapshot_copy_grants_paginator(
    client: Client,
) -> DescribeSnapshotCopyGrantsPaginator:
    """
    Equivalent of `client.get_paginator('describe_snapshot_copy_grants')`, returns a correct type.
    """
    return client.get_paginator("describe_snapshot_copy_grants")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_snapshot_schedules_paginator(
    client: Client,
) -> DescribeSnapshotSchedulesPaginator:
    """
    Equivalent of `client.get_paginator('describe_snapshot_schedules')`, returns a correct type.
    """
    return client.get_paginator("describe_snapshot_schedules")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_table_restore_status_paginator(
    client: Client,
) -> DescribeTableRestoreStatusPaginator:
    """
    Equivalent of `client.get_paginator('describe_table_restore_status')`, returns a correct type.
    """
    return client.get_paginator("describe_table_restore_status")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_tags_paginator(client: Client) -> DescribeTagsPaginator:
    """
    Equivalent of `client.get_paginator('describe_tags')`, returns a correct type.
    """
    return client.get_paginator("describe_tags")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_reserved_node_exchange_offerings_paginator(
    client: Client,
) -> GetReservedNodeExchangeOfferingsPaginator:
    """
    Equivalent of `client.get_paginator('get_reserved_node_exchange_offerings')`, returns a correct type.
    """
    return client.get_paginator("get_reserved_node_exchange_offerings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_cluster_available_waiter(client: Client) -> ClusterAvailableWaiter:
    """
    Equivalent of `client.get_waiter('cluster_available')`, returns a correct type.
    """
    return client.get_waiter("cluster_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_cluster_deleted_waiter(client: Client) -> ClusterDeletedWaiter:
    """
    Equivalent of `client.get_waiter('cluster_deleted')`, returns a correct type.
    """
    return client.get_waiter("cluster_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_cluster_restored_waiter(client: Client) -> ClusterRestoredWaiter:
    """
    Equivalent of `client.get_waiter('cluster_restored')`, returns a correct type.
    """
    return client.get_waiter("cluster_restored")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_snapshot_available_waiter(client: Client) -> SnapshotAvailableWaiter:
    """
    Equivalent of `client.get_waiter('snapshot_available')`, returns a correct type.
    """
    return client.get_waiter("snapshot_available")
