"Helper functions for greengrass service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_greengrass.client import Client
from mypy_boto3_greengrass.paginator import (
    ListBulkDeploymentDetailedReportsPaginator,
    ListBulkDeploymentsPaginator,
    ListConnectorDefinitionVersionsPaginator,
    ListConnectorDefinitionsPaginator,
    ListCoreDefinitionVersionsPaginator,
    ListCoreDefinitionsPaginator,
    ListDeploymentsPaginator,
    ListDeviceDefinitionVersionsPaginator,
    ListDeviceDefinitionsPaginator,
    ListFunctionDefinitionVersionsPaginator,
    ListFunctionDefinitionsPaginator,
    ListGroupVersionsPaginator,
    ListGroupsPaginator,
    ListLoggerDefinitionVersionsPaginator,
    ListLoggerDefinitionsPaginator,
    ListResourceDefinitionVersionsPaginator,
    ListResourceDefinitionsPaginator,
    ListSubscriptionDefinitionVersionsPaginator,
    ListSubscriptionDefinitionsPaginator,
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
    Equivalent of `boto3.client('greengrass')`, returns a correct type.
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
        return session.client("greengrass", **kwargs)
    return boto3.client("greengrass", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_bulk_deployment_detailed_reports_paginator(
    client: Client,
) -> ListBulkDeploymentDetailedReportsPaginator:
    """
    Equivalent of `client.get_paginator('list_bulk_deployment_detailed_reports')`, returns a correct type.
    """
    return client.get_paginator("list_bulk_deployment_detailed_reports")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_bulk_deployments_paginator(client: Client) -> ListBulkDeploymentsPaginator:
    """
    Equivalent of `client.get_paginator('list_bulk_deployments')`, returns a correct type.
    """
    return client.get_paginator("list_bulk_deployments")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_connector_definition_versions_paginator(
    client: Client,
) -> ListConnectorDefinitionVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_connector_definition_versions')`, returns a correct type.
    """
    return client.get_paginator("list_connector_definition_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_connector_definitions_paginator(
    client: Client,
) -> ListConnectorDefinitionsPaginator:
    """
    Equivalent of `client.get_paginator('list_connector_definitions')`, returns a correct type.
    """
    return client.get_paginator("list_connector_definitions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_core_definition_versions_paginator(
    client: Client,
) -> ListCoreDefinitionVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_core_definition_versions')`, returns a correct type.
    """
    return client.get_paginator("list_core_definition_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_core_definitions_paginator(client: Client) -> ListCoreDefinitionsPaginator:
    """
    Equivalent of `client.get_paginator('list_core_definitions')`, returns a correct type.
    """
    return client.get_paginator("list_core_definitions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_deployments_paginator(client: Client) -> ListDeploymentsPaginator:
    """
    Equivalent of `client.get_paginator('list_deployments')`, returns a correct type.
    """
    return client.get_paginator("list_deployments")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_device_definition_versions_paginator(
    client: Client,
) -> ListDeviceDefinitionVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_device_definition_versions')`, returns a correct type.
    """
    return client.get_paginator("list_device_definition_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_device_definitions_paginator(
    client: Client,
) -> ListDeviceDefinitionsPaginator:
    """
    Equivalent of `client.get_paginator('list_device_definitions')`, returns a correct type.
    """
    return client.get_paginator("list_device_definitions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_function_definition_versions_paginator(
    client: Client,
) -> ListFunctionDefinitionVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_function_definition_versions')`, returns a correct type.
    """
    return client.get_paginator("list_function_definition_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_function_definitions_paginator(
    client: Client,
) -> ListFunctionDefinitionsPaginator:
    """
    Equivalent of `client.get_paginator('list_function_definitions')`, returns a correct type.
    """
    return client.get_paginator("list_function_definitions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_group_versions_paginator(client: Client) -> ListGroupVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_group_versions')`, returns a correct type.
    """
    return client.get_paginator("list_group_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_groups_paginator(client: Client) -> ListGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_groups')`, returns a correct type.
    """
    return client.get_paginator("list_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_logger_definition_versions_paginator(
    client: Client,
) -> ListLoggerDefinitionVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_logger_definition_versions')`, returns a correct type.
    """
    return client.get_paginator("list_logger_definition_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_logger_definitions_paginator(
    client: Client,
) -> ListLoggerDefinitionsPaginator:
    """
    Equivalent of `client.get_paginator('list_logger_definitions')`, returns a correct type.
    """
    return client.get_paginator("list_logger_definitions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resource_definition_versions_paginator(
    client: Client,
) -> ListResourceDefinitionVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_resource_definition_versions')`, returns a correct type.
    """
    return client.get_paginator("list_resource_definition_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resource_definitions_paginator(
    client: Client,
) -> ListResourceDefinitionsPaginator:
    """
    Equivalent of `client.get_paginator('list_resource_definitions')`, returns a correct type.
    """
    return client.get_paginator("list_resource_definitions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_subscription_definition_versions_paginator(
    client: Client,
) -> ListSubscriptionDefinitionVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_subscription_definition_versions')`, returns a correct type.
    """
    return client.get_paginator("list_subscription_definition_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_subscription_definitions_paginator(
    client: Client,
) -> ListSubscriptionDefinitionsPaginator:
    """
    Equivalent of `client.get_paginator('list_subscription_definitions')`, returns a correct type.
    """
    return client.get_paginator("list_subscription_definitions")
