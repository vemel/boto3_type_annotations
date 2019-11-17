"Helper functions for storagegateway service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_storagegateway.client import Client
from mypy_boto3_storagegateway.paginator import (
    DescribeTapeArchivesPaginator,
    DescribeTapeRecoveryPointsPaginator,
    DescribeTapesPaginator,
    DescribeVTLDevicesPaginator,
    ListFileSharesPaginator,
    ListGatewaysPaginator,
    ListTagsForResourcePaginator,
    ListTapesPaginator,
    ListVolumesPaginator,
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
    Equivalent of `boto3.client('storagegateway')`, returns a correct type.
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
        return session.client("storagegateway", **kwargs)
    return boto3.client("storagegateway", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_tape_archives_paginator(
    client: Client,
) -> DescribeTapeArchivesPaginator:
    """
    Equivalent of `client.get_paginator('describe_tape_archives')`, returns a correct type.
    """
    return client.get_paginator("describe_tape_archives")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_tape_recovery_points_paginator(
    client: Client,
) -> DescribeTapeRecoveryPointsPaginator:
    """
    Equivalent of `client.get_paginator('describe_tape_recovery_points')`, returns a correct type.
    """
    return client.get_paginator("describe_tape_recovery_points")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_tapes_paginator(client: Client) -> DescribeTapesPaginator:
    """
    Equivalent of `client.get_paginator('describe_tapes')`, returns a correct type.
    """
    return client.get_paginator("describe_tapes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_vtl_devices_paginator(client: Client) -> DescribeVTLDevicesPaginator:
    """
    Equivalent of `client.get_paginator('describe_vtl_devices')`, returns a correct type.
    """
    return client.get_paginator("describe_vtl_devices")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_file_shares_paginator(client: Client) -> ListFileSharesPaginator:
    """
    Equivalent of `client.get_paginator('list_file_shares')`, returns a correct type.
    """
    return client.get_paginator("list_file_shares")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_gateways_paginator(client: Client) -> ListGatewaysPaginator:
    """
    Equivalent of `client.get_paginator('list_gateways')`, returns a correct type.
    """
    return client.get_paginator("list_gateways")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_for_resource_paginator(
    client: Client,
) -> ListTagsForResourcePaginator:
    """
    Equivalent of `client.get_paginator('list_tags_for_resource')`, returns a correct type.
    """
    return client.get_paginator("list_tags_for_resource")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tapes_paginator(client: Client) -> ListTapesPaginator:
    """
    Equivalent of `client.get_paginator('list_tapes')`, returns a correct type.
    """
    return client.get_paginator("list_tapes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_volumes_paginator(client: Client) -> ListVolumesPaginator:
    """
    Equivalent of `client.get_paginator('list_volumes')`, returns a correct type.
    """
    return client.get_paginator("list_volumes")
