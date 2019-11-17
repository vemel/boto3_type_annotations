"Helper functions for iot1click-projects service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_iot1click_projects.client import Client
from mypy_boto3_iot1click_projects.paginator import (
    ListPlacementsPaginator,
    ListProjectsPaginator,
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
    Equivalent of `boto3.client('iot1click-projects')`, returns a correct type.
    """
    kwargs = {}
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
        return session.client("iot1click-projects", **kwargs)
    return boto3.client("iot1click-projects", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_placements_paginator(client: Client) -> ListPlacementsPaginator:
    """
    Equivalent of `client.get_paginator('list_placements')`, returns a correct type.
    """
    return client.get_waiter("list_placements")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_projects_paginator(client: Client) -> ListProjectsPaginator:
    """
    Equivalent of `client.get_paginator('list_projects')`, returns a correct type.
    """
    return client.get_waiter("list_projects")