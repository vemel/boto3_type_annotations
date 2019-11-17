"Helper functions for ecs service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_ecs.client import Client
from mypy_boto3_ecs.paginator import (
    ListAccountSettingsPaginator,
    ListAttributesPaginator,
    ListClustersPaginator,
    ListContainerInstancesPaginator,
    ListServicesPaginator,
    ListTaskDefinitionFamiliesPaginator,
    ListTaskDefinitionsPaginator,
    ListTasksPaginator,
)
from mypy_boto3_ecs.waiter import (
    ServicesInactiveWaiter,
    ServicesStableWaiter,
    TasksRunningWaiter,
    TasksStoppedWaiter,
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
    Equivalent of `boto3.client('ecs')`, returns a correct type.
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
        return session.client("ecs", **kwargs)
    return boto3.client("ecs", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_account_settings_paginator(client: Client) -> ListAccountSettingsPaginator:
    """
    Equivalent of `client.get_paginator('list_account_settings')`, returns a correct type.
    """
    return client.get_paginator("list_account_settings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_attributes_paginator(client: Client) -> ListAttributesPaginator:
    """
    Equivalent of `client.get_paginator('list_attributes')`, returns a correct type.
    """
    return client.get_paginator("list_attributes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_clusters_paginator(client: Client) -> ListClustersPaginator:
    """
    Equivalent of `client.get_paginator('list_clusters')`, returns a correct type.
    """
    return client.get_paginator("list_clusters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_container_instances_paginator(
    client: Client,
) -> ListContainerInstancesPaginator:
    """
    Equivalent of `client.get_paginator('list_container_instances')`, returns a correct type.
    """
    return client.get_paginator("list_container_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_services_paginator(client: Client) -> ListServicesPaginator:
    """
    Equivalent of `client.get_paginator('list_services')`, returns a correct type.
    """
    return client.get_paginator("list_services")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_task_definition_families_paginator(
    client: Client,
) -> ListTaskDefinitionFamiliesPaginator:
    """
    Equivalent of `client.get_paginator('list_task_definition_families')`, returns a correct type.
    """
    return client.get_paginator("list_task_definition_families")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_task_definitions_paginator(client: Client) -> ListTaskDefinitionsPaginator:
    """
    Equivalent of `client.get_paginator('list_task_definitions')`, returns a correct type.
    """
    return client.get_paginator("list_task_definitions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tasks_paginator(client: Client) -> ListTasksPaginator:
    """
    Equivalent of `client.get_paginator('list_tasks')`, returns a correct type.
    """
    return client.get_paginator("list_tasks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_services_inactive_waiter(client: Client) -> ServicesInactiveWaiter:
    """
    Equivalent of `client.get_waiter('services_inactive')`, returns a correct type.
    """
    return client.get_waiter("services_inactive")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_services_stable_waiter(client: Client) -> ServicesStableWaiter:
    """
    Equivalent of `client.get_waiter('services_stable')`, returns a correct type.
    """
    return client.get_waiter("services_stable")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_tasks_running_waiter(client: Client) -> TasksRunningWaiter:
    """
    Equivalent of `client.get_waiter('tasks_running')`, returns a correct type.
    """
    return client.get_waiter("tasks_running")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_tasks_stopped_waiter(client: Client) -> TasksStoppedWaiter:
    """
    Equivalent of `client.get_waiter('tasks_stopped')`, returns a correct type.
    """
    return client.get_waiter("tasks_stopped")
