"Helper functions for codedeploy service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_codedeploy.client import Client
from mypy_boto3_codedeploy.paginator import (
    ListApplicationRevisionsPaginator,
    ListApplicationsPaginator,
    ListDeploymentConfigsPaginator,
    ListDeploymentGroupsPaginator,
    ListDeploymentInstancesPaginator,
    ListDeploymentTargetsPaginator,
    ListDeploymentsPaginator,
    ListGitHubAccountTokenNamesPaginator,
    ListOnPremisesInstancesPaginator,
)
from mypy_boto3_codedeploy.waiter import DeploymentSuccessfulWaiter

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
    Equivalent of `boto3.client('codedeploy')`, returns a correct type.
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
        return session.client("codedeploy", **kwargs)
    return boto3.client("codedeploy", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_application_revisions_paginator(
    client: Client,
) -> ListApplicationRevisionsPaginator:
    """
    Equivalent of `client.get_paginator('list_application_revisions')`, returns a correct type.
    """
    return client.get_paginator("list_application_revisions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_applications_paginator(client: Client) -> ListApplicationsPaginator:
    """
    Equivalent of `client.get_paginator('list_applications')`, returns a correct type.
    """
    return client.get_paginator("list_applications")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_deployment_configs_paginator(
    client: Client,
) -> ListDeploymentConfigsPaginator:
    """
    Equivalent of `client.get_paginator('list_deployment_configs')`, returns a correct type.
    """
    return client.get_paginator("list_deployment_configs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_deployment_groups_paginator(
    client: Client,
) -> ListDeploymentGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_deployment_groups')`, returns a correct type.
    """
    return client.get_paginator("list_deployment_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_deployment_instances_paginator(
    client: Client,
) -> ListDeploymentInstancesPaginator:
    """
    Equivalent of `client.get_paginator('list_deployment_instances')`, returns a correct type.
    """
    return client.get_paginator("list_deployment_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_deployment_targets_paginator(
    client: Client,
) -> ListDeploymentTargetsPaginator:
    """
    Equivalent of `client.get_paginator('list_deployment_targets')`, returns a correct type.
    """
    return client.get_paginator("list_deployment_targets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_deployments_paginator(client: Client) -> ListDeploymentsPaginator:
    """
    Equivalent of `client.get_paginator('list_deployments')`, returns a correct type.
    """
    return client.get_paginator("list_deployments")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_git_hub_account_token_names_paginator(
    client: Client,
) -> ListGitHubAccountTokenNamesPaginator:
    """
    Equivalent of `client.get_paginator('list_git_hub_account_token_names')`, returns a correct type.
    """
    return client.get_paginator("list_git_hub_account_token_names")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_on_premises_instances_paginator(
    client: Client,
) -> ListOnPremisesInstancesPaginator:
    """
    Equivalent of `client.get_paginator('list_on_premises_instances')`, returns a correct type.
    """
    return client.get_paginator("list_on_premises_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_deployment_successful_waiter(client: Client) -> DeploymentSuccessfulWaiter:
    """
    Equivalent of `client.get_waiter('deployment_successful')`, returns a correct type.
    """
    return client.get_waiter("deployment_successful")
