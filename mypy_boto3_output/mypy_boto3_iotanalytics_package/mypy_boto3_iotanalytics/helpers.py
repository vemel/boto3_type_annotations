"Helper functions for iotanalytics service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_iotanalytics.client import Client
from mypy_boto3_iotanalytics.paginator import (
    ListChannelsPaginator,
    ListDatasetContentsPaginator,
    ListDatasetsPaginator,
    ListDatastoresPaginator,
    ListPipelinesPaginator,
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
    Equivalent of `boto3.client('iotanalytics')`, returns a correct type.
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
        return session.client("iotanalytics", **kwargs)
    return boto3.client("iotanalytics", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_channels_paginator(client: Client) -> ListChannelsPaginator:
    """
    Equivalent of `client.get_paginator('list_channels')`, returns a correct type.
    """
    return client.get_paginator("list_channels")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_dataset_contents_paginator(client: Client) -> ListDatasetContentsPaginator:
    """
    Equivalent of `client.get_paginator('list_dataset_contents')`, returns a correct type.
    """
    return client.get_paginator("list_dataset_contents")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_datasets_paginator(client: Client) -> ListDatasetsPaginator:
    """
    Equivalent of `client.get_paginator('list_datasets')`, returns a correct type.
    """
    return client.get_paginator("list_datasets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_datastores_paginator(client: Client) -> ListDatastoresPaginator:
    """
    Equivalent of `client.get_paginator('list_datastores')`, returns a correct type.
    """
    return client.get_paginator("list_datastores")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_pipelines_paginator(client: Client) -> ListPipelinesPaginator:
    """
    Equivalent of `client.get_paginator('list_pipelines')`, returns a correct type.
    """
    return client.get_paginator("list_pipelines")
