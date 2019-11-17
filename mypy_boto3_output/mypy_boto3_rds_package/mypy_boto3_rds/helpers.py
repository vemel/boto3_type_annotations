"Helper functions for rds service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_rds.client import Client
from mypy_boto3_rds.paginator import (
    DescribeCertificatesPaginator,
    DescribeCustomAvailabilityZonesPaginator,
    DescribeDBClusterBacktracksPaginator,
    DescribeDBClusterEndpointsPaginator,
    DescribeDBClusterParameterGroupsPaginator,
    DescribeDBClusterParametersPaginator,
    DescribeDBClusterSnapshotsPaginator,
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstanceAutomatedBackupsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBLogFilesPaginator,
    DescribeDBParameterGroupsPaginator,
    DescribeDBParametersPaginator,
    DescribeDBSecurityGroupsPaginator,
    DescribeDBSnapshotsPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEngineDefaultClusterParametersPaginator,
    DescribeEngineDefaultParametersPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeEventsPaginator,
    DescribeGlobalClustersPaginator,
    DescribeInstallationMediaPaginator,
    DescribeOptionGroupOptionsPaginator,
    DescribeOptionGroupsPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
    DescribePendingMaintenanceActionsPaginator,
    DescribeReservedDBInstancesOfferingsPaginator,
    DescribeReservedDBInstancesPaginator,
    DescribeSourceRegionsPaginator,
    DownloadDBLogFilePortionPaginator,
)
from mypy_boto3_rds.waiter import (
    DBClusterSnapshotAvailableWaiter,
    DBClusterSnapshotDeletedWaiter,
    DBInstanceAvailableWaiter,
    DBInstanceDeletedWaiter,
    DBSnapshotAvailableWaiter,
    DBSnapshotCompletedWaiter,
    DBSnapshotDeletedWaiter,
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
    Equivalent of `boto3.client('rds')`, returns a correct type.
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
        return session.client("rds", **kwargs)
    return boto3.client("rds", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_certificates_paginator(
    client: Client,
) -> DescribeCertificatesPaginator:
    """
    Equivalent of `client.get_paginator('describe_certificates')`, returns a correct type.
    """
    return client.get_paginator("describe_certificates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_custom_availability_zones_paginator(
    client: Client,
) -> DescribeCustomAvailabilityZonesPaginator:
    """
    Equivalent of `client.get_paginator('describe_custom_availability_zones')`, returns a correct type.
    """
    return client.get_paginator("describe_custom_availability_zones")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_cluster_backtracks_paginator(
    client: Client,
) -> DescribeDBClusterBacktracksPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_cluster_backtracks')`, returns a correct type.
    """
    return client.get_paginator("describe_db_cluster_backtracks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_cluster_endpoints_paginator(
    client: Client,
) -> DescribeDBClusterEndpointsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_cluster_endpoints')`, returns a correct type.
    """
    return client.get_paginator("describe_db_cluster_endpoints")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_cluster_parameter_groups_paginator(
    client: Client,
) -> DescribeDBClusterParameterGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_cluster_parameter_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_db_cluster_parameter_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_cluster_parameters_paginator(
    client: Client,
) -> DescribeDBClusterParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_cluster_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_db_cluster_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_cluster_snapshots_paginator(
    client: Client,
) -> DescribeDBClusterSnapshotsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_cluster_snapshots')`, returns a correct type.
    """
    return client.get_paginator("describe_db_cluster_snapshots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_clusters_paginator(client: Client) -> DescribeDBClustersPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_clusters')`, returns a correct type.
    """
    return client.get_paginator("describe_db_clusters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_engine_versions_paginator(
    client: Client,
) -> DescribeDBEngineVersionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_engine_versions')`, returns a correct type.
    """
    return client.get_paginator("describe_db_engine_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_instance_automated_backups_paginator(
    client: Client,
) -> DescribeDBInstanceAutomatedBackupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_instance_automated_backups')`, returns a correct type.
    """
    return client.get_paginator("describe_db_instance_automated_backups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_instances_paginator(client: Client) -> DescribeDBInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_db_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_log_files_paginator(client: Client) -> DescribeDBLogFilesPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_log_files')`, returns a correct type.
    """
    return client.get_paginator("describe_db_log_files")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_parameter_groups_paginator(
    client: Client,
) -> DescribeDBParameterGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_parameter_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_db_parameter_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_parameters_paginator(
    client: Client,
) -> DescribeDBParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_db_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_security_groups_paginator(
    client: Client,
) -> DescribeDBSecurityGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_security_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_db_security_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_snapshots_paginator(client: Client) -> DescribeDBSnapshotsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_snapshots')`, returns a correct type.
    """
    return client.get_paginator("describe_db_snapshots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_subnet_groups_paginator(
    client: Client,
) -> DescribeDBSubnetGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_subnet_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_db_subnet_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_engine_default_cluster_parameters_paginator(
    client: Client,
) -> DescribeEngineDefaultClusterParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_engine_default_cluster_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_engine_default_cluster_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_engine_default_parameters_paginator(
    client: Client,
) -> DescribeEngineDefaultParametersPaginator:
    """
    Equivalent of `client.get_paginator('describe_engine_default_parameters')`, returns a correct type.
    """
    return client.get_paginator("describe_engine_default_parameters")


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
def get_describe_global_clusters_paginator(
    client: Client,
) -> DescribeGlobalClustersPaginator:
    """
    Equivalent of `client.get_paginator('describe_global_clusters')`, returns a correct type.
    """
    return client.get_paginator("describe_global_clusters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_installation_media_paginator(
    client: Client,
) -> DescribeInstallationMediaPaginator:
    """
    Equivalent of `client.get_paginator('describe_installation_media')`, returns a correct type.
    """
    return client.get_paginator("describe_installation_media")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_option_group_options_paginator(
    client: Client,
) -> DescribeOptionGroupOptionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_option_group_options')`, returns a correct type.
    """
    return client.get_paginator("describe_option_group_options")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_option_groups_paginator(
    client: Client,
) -> DescribeOptionGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_option_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_option_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_orderable_db_instance_options_paginator(
    client: Client,
) -> DescribeOrderableDBInstanceOptionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_orderable_db_instance_options')`, returns a correct type.
    """
    return client.get_paginator("describe_orderable_db_instance_options")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_pending_maintenance_actions_paginator(
    client: Client,
) -> DescribePendingMaintenanceActionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_pending_maintenance_actions')`, returns a correct type.
    """
    return client.get_paginator("describe_pending_maintenance_actions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_reserved_db_instances_paginator(
    client: Client,
) -> DescribeReservedDBInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_reserved_db_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_reserved_db_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_reserved_db_instances_offerings_paginator(
    client: Client,
) -> DescribeReservedDBInstancesOfferingsPaginator:
    """
    Equivalent of `client.get_paginator('describe_reserved_db_instances_offerings')`, returns a correct type.
    """
    return client.get_paginator("describe_reserved_db_instances_offerings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_source_regions_paginator(
    client: Client,
) -> DescribeSourceRegionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_source_regions')`, returns a correct type.
    """
    return client.get_paginator("describe_source_regions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_download_db_log_file_portion_paginator(
    client: Client,
) -> DownloadDBLogFilePortionPaginator:
    """
    Equivalent of `client.get_paginator('download_db_log_file_portion')`, returns a correct type.
    """
    return client.get_paginator("download_db_log_file_portion")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_db_cluster_snapshot_available_waiter(
    client: Client,
) -> DBClusterSnapshotAvailableWaiter:
    """
    Equivalent of `client.get_waiter('db_cluster_snapshot_available')`, returns a correct type.
    """
    return client.get_waiter("db_cluster_snapshot_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_db_cluster_snapshot_deleted_waiter(
    client: Client,
) -> DBClusterSnapshotDeletedWaiter:
    """
    Equivalent of `client.get_waiter('db_cluster_snapshot_deleted')`, returns a correct type.
    """
    return client.get_waiter("db_cluster_snapshot_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_db_instance_available_waiter(client: Client) -> DBInstanceAvailableWaiter:
    """
    Equivalent of `client.get_waiter('db_instance_available')`, returns a correct type.
    """
    return client.get_waiter("db_instance_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_db_instance_deleted_waiter(client: Client) -> DBInstanceDeletedWaiter:
    """
    Equivalent of `client.get_waiter('db_instance_deleted')`, returns a correct type.
    """
    return client.get_waiter("db_instance_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_db_snapshot_available_waiter(client: Client) -> DBSnapshotAvailableWaiter:
    """
    Equivalent of `client.get_waiter('db_snapshot_available')`, returns a correct type.
    """
    return client.get_waiter("db_snapshot_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_db_snapshot_completed_waiter(client: Client) -> DBSnapshotCompletedWaiter:
    """
    Equivalent of `client.get_waiter('db_snapshot_completed')`, returns a correct type.
    """
    return client.get_waiter("db_snapshot_completed")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_db_snapshot_deleted_waiter(client: Client) -> DBSnapshotDeletedWaiter:
    """
    Equivalent of `client.get_waiter('db_snapshot_deleted')`, returns a correct type.
    """
    return client.get_waiter("db_snapshot_deleted")
