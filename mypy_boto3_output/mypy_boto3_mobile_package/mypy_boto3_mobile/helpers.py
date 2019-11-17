"Helper functions for mobile service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_mobile.client import Client
from mypy_boto3_mobile.paginator import ListBundlesPaginator, ListProjectsPaginator

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
    Equivalent of `boto3.client('mobile')`, returns a correct type.
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
        return session.client("mobile", **kwargs)
    return boto3.client("mobile", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_bundles_paginator(client: Client) -> ListBundlesPaginator:
    """
    Equivalent of `client.get_paginator('list_bundles')`, returns a correct type.
    """
    return client.get_waiter("list_bundles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_projects_paginator(client: Client) -> ListProjectsPaginator:
    """
    Equivalent of `client.get_paginator('list_projects')`, returns a correct type.
    """
    return client.get_waiter("list_projects")