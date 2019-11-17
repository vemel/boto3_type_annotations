"Helper functions for dms service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_dms.client import Client
from mypy_boto3_dms.paginator import (
    DescribeCertificatesPaginator,
    DescribeConnectionsPaginator,
    DescribeEndpointTypesPaginator,
    DescribeEndpointsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeEventsPaginator,
    DescribeOrderableReplicationInstancesPaginator,
    DescribeReplicationInstancesPaginator,
    DescribeReplicationSubnetGroupsPaginator,
    DescribeReplicationTaskAssessmentResultsPaginator,
    DescribeReplicationTasksPaginator,
    DescribeSchemasPaginator,
    DescribeTableStatisticsPaginator,
)
from mypy_boto3_dms.waiter import (
    EndpointDeletedWaiter,
    ReplicationInstanceAvailableWaiter,
    ReplicationInstanceDeletedWaiter,
    ReplicationTaskDeletedWaiter,
    ReplicationTaskReadyWaiter,
    ReplicationTaskRunningWaiter,
    ReplicationTaskStoppedWaiter,
    TestConnectionSucceedsWaiter,
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
    Equivalent of `boto3.client('dms')`, returns a correct type.
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
        return session.client("dms", **kwargs)
    return boto3.client("dms", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_certificates_paginator(
    client: Client,
) -> DescribeCertificatesPaginator:
    """
    Equivalent of `client.get_paginator('describe_certificates')`, returns a correct type.
    """
    return client.get_paginator("describe_certificates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_connections_paginator(client: Client) -> DescribeConnectionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_connections')`, returns a correct type.
    """
    return client.get_paginator("describe_connections")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_endpoint_types_paginator(
    client: Client,
) -> DescribeEndpointTypesPaginator:
    """
    Equivalent of `client.get_paginator('describe_endpoint_types')`, returns a correct type.
    """
    return client.get_paginator("describe_endpoint_types")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_endpoints_paginator(client: Client) -> DescribeEndpointsPaginator:
    """
    Equivalent of `client.get_paginator('describe_endpoints')`, returns a correct type.
    """
    return client.get_paginator("describe_endpoints")


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
def get_describe_orderable_replication_instances_paginator(
    client: Client,
) -> DescribeOrderableReplicationInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_orderable_replication_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_orderable_replication_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_replication_instances_paginator(
    client: Client,
) -> DescribeReplicationInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_replication_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_replication_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_replication_subnet_groups_paginator(
    client: Client,
) -> DescribeReplicationSubnetGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_replication_subnet_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_replication_subnet_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_replication_task_assessment_results_paginator(
    client: Client,
) -> DescribeReplicationTaskAssessmentResultsPaginator:
    """
    Equivalent of `client.get_paginator('describe_replication_task_assessment_results')`, returns a correct type.
    """
    return client.get_paginator("describe_replication_task_assessment_results")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_replication_tasks_paginator(
    client: Client,
) -> DescribeReplicationTasksPaginator:
    """
    Equivalent of `client.get_paginator('describe_replication_tasks')`, returns a correct type.
    """
    return client.get_paginator("describe_replication_tasks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_schemas_paginator(client: Client) -> DescribeSchemasPaginator:
    """
    Equivalent of `client.get_paginator('describe_schemas')`, returns a correct type.
    """
    return client.get_paginator("describe_schemas")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_table_statistics_paginator(
    client: Client,
) -> DescribeTableStatisticsPaginator:
    """
    Equivalent of `client.get_paginator('describe_table_statistics')`, returns a correct type.
    """
    return client.get_paginator("describe_table_statistics")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_endpoint_deleted_waiter(client: Client) -> EndpointDeletedWaiter:
    """
    Equivalent of `client.get_waiter('endpoint_deleted')`, returns a correct type.
    """
    return client.get_waiter("endpoint_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_replication_instance_available_waiter(
    client: Client,
) -> ReplicationInstanceAvailableWaiter:
    """
    Equivalent of `client.get_waiter('replication_instance_available')`, returns a correct type.
    """
    return client.get_waiter("replication_instance_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_replication_instance_deleted_waiter(
    client: Client,
) -> ReplicationInstanceDeletedWaiter:
    """
    Equivalent of `client.get_waiter('replication_instance_deleted')`, returns a correct type.
    """
    return client.get_waiter("replication_instance_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_replication_task_deleted_waiter(client: Client) -> ReplicationTaskDeletedWaiter:
    """
    Equivalent of `client.get_waiter('replication_task_deleted')`, returns a correct type.
    """
    return client.get_waiter("replication_task_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_replication_task_ready_waiter(client: Client) -> ReplicationTaskReadyWaiter:
    """
    Equivalent of `client.get_waiter('replication_task_ready')`, returns a correct type.
    """
    return client.get_waiter("replication_task_ready")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_replication_task_running_waiter(client: Client) -> ReplicationTaskRunningWaiter:
    """
    Equivalent of `client.get_waiter('replication_task_running')`, returns a correct type.
    """
    return client.get_waiter("replication_task_running")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_replication_task_stopped_waiter(client: Client) -> ReplicationTaskStoppedWaiter:
    """
    Equivalent of `client.get_waiter('replication_task_stopped')`, returns a correct type.
    """
    return client.get_waiter("replication_task_stopped")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_test_connection_succeeds_waiter(client: Client) -> TestConnectionSucceedsWaiter:
    """
    Equivalent of `client.get_waiter('test_connection_succeeds')`, returns a correct type.
    """
    return client.get_waiter("test_connection_succeeds")
