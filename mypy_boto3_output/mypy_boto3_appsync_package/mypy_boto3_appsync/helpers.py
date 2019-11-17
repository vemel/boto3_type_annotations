"Helper functions for appsync service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_appsync.client import Client
from mypy_boto3_appsync.paginator import (
    ListApiKeysPaginator,
    ListDataSourcesPaginator,
    ListFunctionsPaginator,
    ListGraphqlApisPaginator,
    ListResolversByFunctionPaginator,
    ListResolversPaginator,
    ListTypesPaginator,
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
    Equivalent of `boto3.client('appsync')`, returns a correct type.
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
        return session.client("appsync", **kwargs)
    return boto3.client("appsync", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_api_keys_paginator(client: Client) -> ListApiKeysPaginator:
    """
    Equivalent of `client.get_paginator('list_api_keys')`, returns a correct type.
    """
    return client.get_paginator("list_api_keys")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_data_sources_paginator(client: Client) -> ListDataSourcesPaginator:
    """
    Equivalent of `client.get_paginator('list_data_sources')`, returns a correct type.
    """
    return client.get_paginator("list_data_sources")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_functions_paginator(client: Client) -> ListFunctionsPaginator:
    """
    Equivalent of `client.get_paginator('list_functions')`, returns a correct type.
    """
    return client.get_paginator("list_functions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_graphql_apis_paginator(client: Client) -> ListGraphqlApisPaginator:
    """
    Equivalent of `client.get_paginator('list_graphql_apis')`, returns a correct type.
    """
    return client.get_paginator("list_graphql_apis")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resolvers_paginator(client: Client) -> ListResolversPaginator:
    """
    Equivalent of `client.get_paginator('list_resolvers')`, returns a correct type.
    """
    return client.get_paginator("list_resolvers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resolvers_by_function_paginator(
    client: Client,
) -> ListResolversByFunctionPaginator:
    """
    Equivalent of `client.get_paginator('list_resolvers_by_function')`, returns a correct type.
    """
    return client.get_paginator("list_resolvers_by_function")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_types_paginator(client: Client) -> ListTypesPaginator:
    """
    Equivalent of `client.get_paginator('list_types')`, returns a correct type.
    """
    return client.get_paginator("list_types")
