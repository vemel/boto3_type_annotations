"Helper functions for eks service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_eks.client import Client
from mypy_boto3_eks.paginator import (
    ListClustersPaginator,
    ListNodegroupsPaginator,
    ListUpdatesPaginator,
)
from mypy_boto3_eks.waiter import (
    ClusterActiveWaiter,
    ClusterDeletedWaiter,
    NodegroupActiveWaiter,
    NodegroupDeletedWaiter,
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
    Equivalent of `boto3.client('eks')`, returns a correct type.
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
        return session.client("eks", **kwargs)
    return boto3.client("eks", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_clusters_paginator(client: Client) -> ListClustersPaginator:
    """
    Equivalent of `client.get_paginator('list_clusters')`, returns a correct type.
    """
    return client.get_paginator("list_clusters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_nodegroups_paginator(client: Client) -> ListNodegroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_nodegroups')`, returns a correct type.
    """
    return client.get_paginator("list_nodegroups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_updates_paginator(client: Client) -> ListUpdatesPaginator:
    """
    Equivalent of `client.get_paginator('list_updates')`, returns a correct type.
    """
    return client.get_paginator("list_updates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_cluster_active_waiter(client: Client) -> ClusterActiveWaiter:
    """
    Equivalent of `client.get_waiter('cluster_active')`, returns a correct type.
    """
    return client.get_waiter("cluster_active")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_cluster_deleted_waiter(client: Client) -> ClusterDeletedWaiter:
    """
    Equivalent of `client.get_waiter('cluster_deleted')`, returns a correct type.
    """
    return client.get_waiter("cluster_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_nodegroup_active_waiter(client: Client) -> NodegroupActiveWaiter:
    """
    Equivalent of `client.get_waiter('nodegroup_active')`, returns a correct type.
    """
    return client.get_waiter("nodegroup_active")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_nodegroup_deleted_waiter(client: Client) -> NodegroupDeletedWaiter:
    """
    Equivalent of `client.get_waiter('nodegroup_deleted')`, returns a correct type.
    """
    return client.get_waiter("nodegroup_deleted")
