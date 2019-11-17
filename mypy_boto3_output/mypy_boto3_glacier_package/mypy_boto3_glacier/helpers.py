"Helper functions for glacier service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_glacier.client import Client
from mypy_boto3_glacier.paginator import (
    ListJobsPaginator,
    ListMultipartUploadsPaginator,
    ListPartsPaginator,
    ListVaultsPaginator,
)
from mypy_boto3_glacier.service_resource import ServiceResource
from mypy_boto3_glacier.waiter import VaultExistsWaiter, VaultNotExistsWaiter

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
    Equivalent of `boto3.client('glacier')`, returns a correct type.
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
        return session.client("glacier", **kwargs)
    return boto3.client("glacier", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_resource(
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
) -> ServiceResource:
    """
    Equivalent of `boto3.resource('glacier')`, returns a correct type.
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
        return session.resource("glacier", **kwargs)
    return boto3.resource("glacier", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_jobs_paginator(client: Client) -> ListJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_multipart_uploads_paginator(
    client: Client,
) -> ListMultipartUploadsPaginator:
    """
    Equivalent of `client.get_paginator('list_multipart_uploads')`, returns a correct type.
    """
    return client.get_paginator("list_multipart_uploads")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_parts_paginator(client: Client) -> ListPartsPaginator:
    """
    Equivalent of `client.get_paginator('list_parts')`, returns a correct type.
    """
    return client.get_paginator("list_parts")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_vaults_paginator(client: Client) -> ListVaultsPaginator:
    """
    Equivalent of `client.get_paginator('list_vaults')`, returns a correct type.
    """
    return client.get_paginator("list_vaults")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_vault_exists_waiter(client: Client) -> VaultExistsWaiter:
    """
    Equivalent of `client.get_waiter('vault_exists')`, returns a correct type.
    """
    return client.get_waiter("vault_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_vault_not_exists_waiter(client: Client) -> VaultNotExistsWaiter:
    """
    Equivalent of `client.get_waiter('vault_not_exists')`, returns a correct type.
    """
    return client.get_waiter("vault_not_exists")
