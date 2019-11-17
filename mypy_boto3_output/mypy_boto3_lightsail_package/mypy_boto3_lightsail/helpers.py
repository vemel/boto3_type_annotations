"Helper functions for lightsail service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_lightsail.client import Client
from mypy_boto3_lightsail.paginator import (
    GetActiveNamesPaginator,
    GetBlueprintsPaginator,
    GetBundlesPaginator,
    GetCloudFormationStackRecordsPaginator,
    GetDiskSnapshotsPaginator,
    GetDisksPaginator,
    GetDomainsPaginator,
    GetExportSnapshotRecordsPaginator,
    GetInstanceSnapshotsPaginator,
    GetInstancesPaginator,
    GetKeyPairsPaginator,
    GetLoadBalancersPaginator,
    GetOperationsPaginator,
    GetRelationalDatabaseBlueprintsPaginator,
    GetRelationalDatabaseBundlesPaginator,
    GetRelationalDatabaseEventsPaginator,
    GetRelationalDatabaseParametersPaginator,
    GetRelationalDatabaseSnapshotsPaginator,
    GetRelationalDatabasesPaginator,
    GetStaticIpsPaginator,
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
    Equivalent of `boto3.client('lightsail')`, returns a correct type.
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
        return session.client("lightsail", **kwargs)
    return boto3.client("lightsail", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_active_names_paginator(client: Client) -> GetActiveNamesPaginator:
    """
    Equivalent of `client.get_paginator('get_active_names')`, returns a correct type.
    """
    return client.get_paginator("get_active_names")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_blueprints_paginator(client: Client) -> GetBlueprintsPaginator:
    """
    Equivalent of `client.get_paginator('get_blueprints')`, returns a correct type.
    """
    return client.get_paginator("get_blueprints")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_bundles_paginator(client: Client) -> GetBundlesPaginator:
    """
    Equivalent of `client.get_paginator('get_bundles')`, returns a correct type.
    """
    return client.get_paginator("get_bundles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_cloud_formation_stack_records_paginator(
    client: Client,
) -> GetCloudFormationStackRecordsPaginator:
    """
    Equivalent of `client.get_paginator('get_cloud_formation_stack_records')`, returns a correct type.
    """
    return client.get_paginator("get_cloud_formation_stack_records")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_disk_snapshots_paginator(client: Client) -> GetDiskSnapshotsPaginator:
    """
    Equivalent of `client.get_paginator('get_disk_snapshots')`, returns a correct type.
    """
    return client.get_paginator("get_disk_snapshots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_disks_paginator(client: Client) -> GetDisksPaginator:
    """
    Equivalent of `client.get_paginator('get_disks')`, returns a correct type.
    """
    return client.get_paginator("get_disks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_domains_paginator(client: Client) -> GetDomainsPaginator:
    """
    Equivalent of `client.get_paginator('get_domains')`, returns a correct type.
    """
    return client.get_paginator("get_domains")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_export_snapshot_records_paginator(
    client: Client,
) -> GetExportSnapshotRecordsPaginator:
    """
    Equivalent of `client.get_paginator('get_export_snapshot_records')`, returns a correct type.
    """
    return client.get_paginator("get_export_snapshot_records")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_instance_snapshots_paginator(
    client: Client,
) -> GetInstanceSnapshotsPaginator:
    """
    Equivalent of `client.get_paginator('get_instance_snapshots')`, returns a correct type.
    """
    return client.get_paginator("get_instance_snapshots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_instances_paginator(client: Client) -> GetInstancesPaginator:
    """
    Equivalent of `client.get_paginator('get_instances')`, returns a correct type.
    """
    return client.get_paginator("get_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_key_pairs_paginator(client: Client) -> GetKeyPairsPaginator:
    """
    Equivalent of `client.get_paginator('get_key_pairs')`, returns a correct type.
    """
    return client.get_paginator("get_key_pairs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_load_balancers_paginator(client: Client) -> GetLoadBalancersPaginator:
    """
    Equivalent of `client.get_paginator('get_load_balancers')`, returns a correct type.
    """
    return client.get_paginator("get_load_balancers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_operations_paginator(client: Client) -> GetOperationsPaginator:
    """
    Equivalent of `client.get_paginator('get_operations')`, returns a correct type.
    """
    return client.get_paginator("get_operations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_relational_database_blueprints_paginator(
    client: Client,
) -> GetRelationalDatabaseBlueprintsPaginator:
    """
    Equivalent of `client.get_paginator('get_relational_database_blueprints')`, returns a correct type.
    """
    return client.get_paginator("get_relational_database_blueprints")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_relational_database_bundles_paginator(
    client: Client,
) -> GetRelationalDatabaseBundlesPaginator:
    """
    Equivalent of `client.get_paginator('get_relational_database_bundles')`, returns a correct type.
    """
    return client.get_paginator("get_relational_database_bundles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_relational_database_events_paginator(
    client: Client,
) -> GetRelationalDatabaseEventsPaginator:
    """
    Equivalent of `client.get_paginator('get_relational_database_events')`, returns a correct type.
    """
    return client.get_paginator("get_relational_database_events")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_relational_database_parameters_paginator(
    client: Client,
) -> GetRelationalDatabaseParametersPaginator:
    """
    Equivalent of `client.get_paginator('get_relational_database_parameters')`, returns a correct type.
    """
    return client.get_paginator("get_relational_database_parameters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_relational_database_snapshots_paginator(
    client: Client,
) -> GetRelationalDatabaseSnapshotsPaginator:
    """
    Equivalent of `client.get_paginator('get_relational_database_snapshots')`, returns a correct type.
    """
    return client.get_paginator("get_relational_database_snapshots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_relational_databases_paginator(
    client: Client,
) -> GetRelationalDatabasesPaginator:
    """
    Equivalent of `client.get_paginator('get_relational_databases')`, returns a correct type.
    """
    return client.get_paginator("get_relational_databases")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_static_ips_paginator(client: Client) -> GetStaticIpsPaginator:
    """
    Equivalent of `client.get_paginator('get_static_ips')`, returns a correct type.
    """
    return client.get_paginator("get_static_ips")
