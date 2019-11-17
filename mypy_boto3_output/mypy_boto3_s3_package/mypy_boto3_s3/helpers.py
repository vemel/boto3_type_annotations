"Helper functions for s3 service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_s3.client import Client
from mypy_boto3_s3.paginator import (
    ListMultipartUploadsPaginator,
    ListObjectVersionsPaginator,
    ListObjectsPaginator,
    ListObjectsV2Paginator,
    ListPartsPaginator,
)
from mypy_boto3_s3.service_resource import ServiceResource
from mypy_boto3_s3.waiter import (
    BucketExistsWaiter,
    BucketNotExistsWaiter,
    ObjectExistsWaiter,
    ObjectNotExistsWaiter,
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
    Equivalent of `boto3.client('s3')`, returns a correct type.
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
        return session.client("s3", **kwargs)
    return boto3.client("s3", **kwargs)


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
    Equivalent of `boto3.resource('s3')`, returns a correct type.
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
        return session.resource("s3", **kwargs)
    return boto3.resource("s3", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_multipart_uploads_paginator(
    client: Client,
) -> ListMultipartUploadsPaginator:
    """
    Equivalent of `client.get_paginator('list_multipart_uploads')`, returns a correct type.
    """
    return client.get_paginator("list_multipart_uploads")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_object_versions_paginator(client: Client) -> ListObjectVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_object_versions')`, returns a correct type.
    """
    return client.get_paginator("list_object_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_objects_paginator(client: Client) -> ListObjectsPaginator:
    """
    Equivalent of `client.get_paginator('list_objects')`, returns a correct type.
    """
    return client.get_paginator("list_objects")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_objects_v2_paginator(client: Client) -> ListObjectsV2Paginator:
    """
    Equivalent of `client.get_paginator('list_objects_v2')`, returns a correct type.
    """
    return client.get_paginator("list_objects_v2")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_parts_paginator(client: Client) -> ListPartsPaginator:
    """
    Equivalent of `client.get_paginator('list_parts')`, returns a correct type.
    """
    return client.get_paginator("list_parts")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_bucket_exists_waiter(client: Client) -> BucketExistsWaiter:
    """
    Equivalent of `client.get_waiter('bucket_exists')`, returns a correct type.
    """
    return client.get_waiter("bucket_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_bucket_not_exists_waiter(client: Client) -> BucketNotExistsWaiter:
    """
    Equivalent of `client.get_waiter('bucket_not_exists')`, returns a correct type.
    """
    return client.get_waiter("bucket_not_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_object_exists_waiter(client: Client) -> ObjectExistsWaiter:
    """
    Equivalent of `client.get_waiter('object_exists')`, returns a correct type.
    """
    return client.get_waiter("object_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_object_not_exists_waiter(client: Client) -> ObjectNotExistsWaiter:
    """
    Equivalent of `client.get_waiter('object_not_exists')`, returns a correct type.
    """
    return client.get_waiter("object_not_exists")
