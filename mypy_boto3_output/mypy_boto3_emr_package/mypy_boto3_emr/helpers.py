"Helper functions for emr service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_emr.client import Client
from mypy_boto3_emr.paginator import (
    ListBootstrapActionsPaginator,
    ListClustersPaginator,
    ListInstanceFleetsPaginator,
    ListInstanceGroupsPaginator,
    ListInstancesPaginator,
    ListSecurityConfigurationsPaginator,
    ListStepsPaginator,
)
from mypy_boto3_emr.waiter import (
    ClusterRunningWaiter,
    ClusterTerminatedWaiter,
    StepCompleteWaiter,
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
    Equivalent of `boto3.client('emr')`, returns a correct type.
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
        return session.client("emr", **kwargs)
    return boto3.client("emr", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_bootstrap_actions_paginator(
    client: Client,
) -> ListBootstrapActionsPaginator:
    """
    Equivalent of `client.get_paginator('list_bootstrap_actions')`, returns a correct type.
    """
    return client.get_paginator("list_bootstrap_actions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_clusters_paginator(client: Client) -> ListClustersPaginator:
    """
    Equivalent of `client.get_paginator('list_clusters')`, returns a correct type.
    """
    return client.get_paginator("list_clusters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_instance_fleets_paginator(client: Client) -> ListInstanceFleetsPaginator:
    """
    Equivalent of `client.get_paginator('list_instance_fleets')`, returns a correct type.
    """
    return client.get_paginator("list_instance_fleets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_instance_groups_paginator(client: Client) -> ListInstanceGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_instance_groups')`, returns a correct type.
    """
    return client.get_paginator("list_instance_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_instances_paginator(client: Client) -> ListInstancesPaginator:
    """
    Equivalent of `client.get_paginator('list_instances')`, returns a correct type.
    """
    return client.get_paginator("list_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_security_configurations_paginator(
    client: Client,
) -> ListSecurityConfigurationsPaginator:
    """
    Equivalent of `client.get_paginator('list_security_configurations')`, returns a correct type.
    """
    return client.get_paginator("list_security_configurations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_steps_paginator(client: Client) -> ListStepsPaginator:
    """
    Equivalent of `client.get_paginator('list_steps')`, returns a correct type.
    """
    return client.get_paginator("list_steps")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_cluster_running_waiter(client: Client) -> ClusterRunningWaiter:
    """
    Equivalent of `client.get_waiter('cluster_running')`, returns a correct type.
    """
    return client.get_waiter("cluster_running")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_cluster_terminated_waiter(client: Client) -> ClusterTerminatedWaiter:
    """
    Equivalent of `client.get_waiter('cluster_terminated')`, returns a correct type.
    """
    return client.get_waiter("cluster_terminated")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_step_complete_waiter(client: Client) -> StepCompleteWaiter:
    """
    Equivalent of `client.get_waiter('step_complete')`, returns a correct type.
    """
    return client.get_waiter("step_complete")
