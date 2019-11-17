"Helper functions for appmesh service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_appmesh.client import Client
from mypy_boto3_appmesh.paginator import (
    ListMeshesPaginator,
    ListRoutesPaginator,
    ListTagsForResourcePaginator,
    ListVirtualNodesPaginator,
    ListVirtualRoutersPaginator,
    ListVirtualServicesPaginator,
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
    Equivalent of `boto3.client('appmesh')`, returns a correct type.
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
        return session.client("appmesh", **kwargs)
    return boto3.client("appmesh", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_meshes_paginator(client: Client) -> ListMeshesPaginator:
    """
    Equivalent of `client.get_paginator('list_meshes')`, returns a correct type.
    """
    return client.get_paginator("list_meshes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_routes_paginator(client: Client) -> ListRoutesPaginator:
    """
    Equivalent of `client.get_paginator('list_routes')`, returns a correct type.
    """
    return client.get_paginator("list_routes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_for_resource_paginator(
    client: Client,
) -> ListTagsForResourcePaginator:
    """
    Equivalent of `client.get_paginator('list_tags_for_resource')`, returns a correct type.
    """
    return client.get_paginator("list_tags_for_resource")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_virtual_nodes_paginator(client: Client) -> ListVirtualNodesPaginator:
    """
    Equivalent of `client.get_paginator('list_virtual_nodes')`, returns a correct type.
    """
    return client.get_paginator("list_virtual_nodes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_virtual_routers_paginator(client: Client) -> ListVirtualRoutersPaginator:
    """
    Equivalent of `client.get_paginator('list_virtual_routers')`, returns a correct type.
    """
    return client.get_paginator("list_virtual_routers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_virtual_services_paginator(client: Client) -> ListVirtualServicesPaginator:
    """
    Equivalent of `client.get_paginator('list_virtual_services')`, returns a correct type.
    """
    return client.get_paginator("list_virtual_services")
