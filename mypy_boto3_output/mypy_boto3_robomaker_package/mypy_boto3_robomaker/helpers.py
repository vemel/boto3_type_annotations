"Helper functions for robomaker service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_robomaker.client import Client
from mypy_boto3_robomaker.paginator import (
    ListDeploymentJobsPaginator,
    ListFleetsPaginator,
    ListRobotApplicationsPaginator,
    ListRobotsPaginator,
    ListSimulationApplicationsPaginator,
    ListSimulationJobsPaginator,
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
    Equivalent of `boto3.client('robomaker')`, returns a correct type.
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
        return session.client("robomaker", **kwargs)
    return boto3.client("robomaker", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_deployment_jobs_paginator(client: Client) -> ListDeploymentJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_deployment_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_deployment_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_fleets_paginator(client: Client) -> ListFleetsPaginator:
    """
    Equivalent of `client.get_paginator('list_fleets')`, returns a correct type.
    """
    return client.get_paginator("list_fleets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_robot_applications_paginator(
    client: Client,
) -> ListRobotApplicationsPaginator:
    """
    Equivalent of `client.get_paginator('list_robot_applications')`, returns a correct type.
    """
    return client.get_paginator("list_robot_applications")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_robots_paginator(client: Client) -> ListRobotsPaginator:
    """
    Equivalent of `client.get_paginator('list_robots')`, returns a correct type.
    """
    return client.get_paginator("list_robots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_simulation_applications_paginator(
    client: Client,
) -> ListSimulationApplicationsPaginator:
    """
    Equivalent of `client.get_paginator('list_simulation_applications')`, returns a correct type.
    """
    return client.get_paginator("list_simulation_applications")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_simulation_jobs_paginator(client: Client) -> ListSimulationJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_simulation_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_simulation_jobs")
