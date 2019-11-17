"Helper functions for lambda service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_lambda.client import Client
from mypy_boto3_lambda.paginator import (
    ListAliasesPaginator,
    ListEventSourceMappingsPaginator,
    ListFunctionsPaginator,
    ListLayerVersionsPaginator,
    ListLayersPaginator,
    ListVersionsByFunctionPaginator,
)
from mypy_boto3_lambda.waiter import FunctionExistsWaiter

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
    Equivalent of `boto3.client('lambda')`, returns a correct type.
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
        return session.client("lambda", **kwargs)
    return boto3.client("lambda", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_aliases_paginator(client: Client) -> ListAliasesPaginator:
    """
    Equivalent of `client.get_paginator('list_aliases')`, returns a correct type.
    """
    return client.get_paginator("list_aliases")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_event_source_mappings_paginator(
    client: Client,
) -> ListEventSourceMappingsPaginator:
    """
    Equivalent of `client.get_paginator('list_event_source_mappings')`, returns a correct type.
    """
    return client.get_paginator("list_event_source_mappings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_functions_paginator(client: Client) -> ListFunctionsPaginator:
    """
    Equivalent of `client.get_paginator('list_functions')`, returns a correct type.
    """
    return client.get_paginator("list_functions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_layer_versions_paginator(client: Client) -> ListLayerVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_layer_versions')`, returns a correct type.
    """
    return client.get_paginator("list_layer_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_layers_paginator(client: Client) -> ListLayersPaginator:
    """
    Equivalent of `client.get_paginator('list_layers')`, returns a correct type.
    """
    return client.get_paginator("list_layers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_versions_by_function_paginator(
    client: Client,
) -> ListVersionsByFunctionPaginator:
    """
    Equivalent of `client.get_paginator('list_versions_by_function')`, returns a correct type.
    """
    return client.get_paginator("list_versions_by_function")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_function_exists_waiter(client: Client) -> FunctionExistsWaiter:
    """
    Equivalent of `client.get_waiter('function_exists')`, returns a correct type.
    """
    return client.get_waiter("function_exists")
