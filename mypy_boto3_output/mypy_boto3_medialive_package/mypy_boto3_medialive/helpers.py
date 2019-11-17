"Helper functions for medialive service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_medialive.client import Client
from mypy_boto3_medialive.paginator import (
    DescribeSchedulePaginator,
    ListChannelsPaginator,
    ListInputSecurityGroupsPaginator,
    ListInputsPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
)
from mypy_boto3_medialive.waiter import (
    ChannelCreatedWaiter,
    ChannelDeletedWaiter,
    ChannelRunningWaiter,
    ChannelStoppedWaiter,
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
    Equivalent of `boto3.client('medialive')`, returns a correct type.
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
        return session.client("medialive", **kwargs)
    return boto3.client("medialive", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_schedule_paginator(client: Client) -> DescribeSchedulePaginator:
    """
    Equivalent of `client.get_paginator('describe_schedule')`, returns a correct type.
    """
    return client.get_paginator("describe_schedule")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_channels_paginator(client: Client) -> ListChannelsPaginator:
    """
    Equivalent of `client.get_paginator('list_channels')`, returns a correct type.
    """
    return client.get_paginator("list_channels")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_input_security_groups_paginator(
    client: Client,
) -> ListInputSecurityGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_input_security_groups')`, returns a correct type.
    """
    return client.get_paginator("list_input_security_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_inputs_paginator(client: Client) -> ListInputsPaginator:
    """
    Equivalent of `client.get_paginator('list_inputs')`, returns a correct type.
    """
    return client.get_paginator("list_inputs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_offerings_paginator(client: Client) -> ListOfferingsPaginator:
    """
    Equivalent of `client.get_paginator('list_offerings')`, returns a correct type.
    """
    return client.get_paginator("list_offerings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_reservations_paginator(client: Client) -> ListReservationsPaginator:
    """
    Equivalent of `client.get_paginator('list_reservations')`, returns a correct type.
    """
    return client.get_paginator("list_reservations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_channel_created_waiter(client: Client) -> ChannelCreatedWaiter:
    """
    Equivalent of `client.get_waiter('channel_created')`, returns a correct type.
    """
    return client.get_waiter("channel_created")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_channel_deleted_waiter(client: Client) -> ChannelDeletedWaiter:
    """
    Equivalent of `client.get_waiter('channel_deleted')`, returns a correct type.
    """
    return client.get_waiter("channel_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_channel_running_waiter(client: Client) -> ChannelRunningWaiter:
    """
    Equivalent of `client.get_waiter('channel_running')`, returns a correct type.
    """
    return client.get_waiter("channel_running")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_channel_stopped_waiter(client: Client) -> ChannelStoppedWaiter:
    """
    Equivalent of `client.get_waiter('channel_stopped')`, returns a correct type.
    """
    return client.get_waiter("channel_stopped")
