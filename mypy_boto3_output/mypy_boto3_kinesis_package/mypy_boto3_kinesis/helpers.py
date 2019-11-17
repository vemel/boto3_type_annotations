"Helper functions for kinesis service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_kinesis.client import Client
from mypy_boto3_kinesis.paginator import (
    DescribeStreamPaginator,
    ListShardsPaginator,
    ListStreamConsumersPaginator,
    ListStreamsPaginator,
)
from mypy_boto3_kinesis.waiter import StreamExistsWaiter, StreamNotExistsWaiter

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
    Equivalent of `boto3.client('kinesis')`, returns a correct type.
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
        return session.client("kinesis", **kwargs)
    return boto3.client("kinesis", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_stream_paginator(client: Client) -> DescribeStreamPaginator:
    """
    Equivalent of `client.get_paginator('describe_stream')`, returns a correct type.
    """
    return client.get_paginator("describe_stream")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_shards_paginator(client: Client) -> ListShardsPaginator:
    """
    Equivalent of `client.get_paginator('list_shards')`, returns a correct type.
    """
    return client.get_paginator("list_shards")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_stream_consumers_paginator(client: Client) -> ListStreamConsumersPaginator:
    """
    Equivalent of `client.get_paginator('list_stream_consumers')`, returns a correct type.
    """
    return client.get_paginator("list_stream_consumers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_streams_paginator(client: Client) -> ListStreamsPaginator:
    """
    Equivalent of `client.get_paginator('list_streams')`, returns a correct type.
    """
    return client.get_paginator("list_streams")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_stream_exists_waiter(client: Client) -> StreamExistsWaiter:
    """
    Equivalent of `client.get_waiter('stream_exists')`, returns a correct type.
    """
    return client.get_waiter("stream_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_stream_not_exists_waiter(client: Client) -> StreamNotExistsWaiter:
    """
    Equivalent of `client.get_waiter('stream_not_exists')`, returns a correct type.
    """
    return client.get_waiter("stream_not_exists")
