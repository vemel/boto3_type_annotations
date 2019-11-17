"Helper functions for ecr service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_ecr.client import Client
from mypy_boto3_ecr.paginator import (
    DescribeImageScanFindingsPaginator,
    DescribeImagesPaginator,
    DescribeRepositoriesPaginator,
    GetLifecyclePolicyPreviewPaginator,
    ListImagesPaginator,
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
    Equivalent of `boto3.client('ecr')`, returns a correct type.
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
        return session.client("ecr", **kwargs)
    return boto3.client("ecr", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_image_scan_findings_paginator(
    client: Client,
) -> DescribeImageScanFindingsPaginator:
    """
    Equivalent of `client.get_paginator('describe_image_scan_findings')`, returns a correct type.
    """
    return client.get_waiter("describe_image_scan_findings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_images_paginator(client: Client) -> DescribeImagesPaginator:
    """
    Equivalent of `client.get_paginator('describe_images')`, returns a correct type.
    """
    return client.get_waiter("describe_images")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_repositories_paginator(
    client: Client,
) -> DescribeRepositoriesPaginator:
    """
    Equivalent of `client.get_paginator('describe_repositories')`, returns a correct type.
    """
    return client.get_waiter("describe_repositories")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_lifecycle_policy_preview_paginator(
    client: Client,
) -> GetLifecyclePolicyPreviewPaginator:
    """
    Equivalent of `client.get_paginator('get_lifecycle_policy_preview')`, returns a correct type.
    """
    return client.get_waiter("get_lifecycle_policy_preview")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_images_paginator(client: Client) -> ListImagesPaginator:
    """
    Equivalent of `client.get_paginator('list_images')`, returns a correct type.
    """
    return client.get_waiter("list_images")