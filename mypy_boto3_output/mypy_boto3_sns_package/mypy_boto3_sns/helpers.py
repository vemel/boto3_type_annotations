"Helper functions for sns service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_sns.client import Client
from mypy_boto3_sns.paginator import (
    ListEndpointsByPlatformApplicationPaginator,
    ListPhoneNumbersOptedOutPaginator,
    ListPlatformApplicationsPaginator,
    ListSubscriptionsByTopicPaginator,
    ListSubscriptionsPaginator,
    ListTopicsPaginator,
)
from mypy_boto3_sns.service_resource import ServiceResource

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
    Equivalent of `boto3.client('sns')`, returns a correct type.
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
        return session.client("sns", **kwargs)
    return boto3.client("sns", **kwargs)


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
    Equivalent of `boto3.resource('sns')`, returns a correct type.
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
        return session.resource("sns", **kwargs)
    return boto3.resource("sns", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_endpoints_by_platform_application_paginator(
    client: Client,
) -> ListEndpointsByPlatformApplicationPaginator:
    """
    Equivalent of `client.get_paginator('list_endpoints_by_platform_application')`, returns a correct type.
    """
    return client.get_paginator("list_endpoints_by_platform_application")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_phone_numbers_opted_out_paginator(
    client: Client,
) -> ListPhoneNumbersOptedOutPaginator:
    """
    Equivalent of `client.get_paginator('list_phone_numbers_opted_out')`, returns a correct type.
    """
    return client.get_paginator("list_phone_numbers_opted_out")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_platform_applications_paginator(
    client: Client,
) -> ListPlatformApplicationsPaginator:
    """
    Equivalent of `client.get_paginator('list_platform_applications')`, returns a correct type.
    """
    return client.get_paginator("list_platform_applications")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_subscriptions_paginator(client: Client) -> ListSubscriptionsPaginator:
    """
    Equivalent of `client.get_paginator('list_subscriptions')`, returns a correct type.
    """
    return client.get_paginator("list_subscriptions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_subscriptions_by_topic_paginator(
    client: Client,
) -> ListSubscriptionsByTopicPaginator:
    """
    Equivalent of `client.get_paginator('list_subscriptions_by_topic')`, returns a correct type.
    """
    return client.get_paginator("list_subscriptions_by_topic")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_topics_paginator(client: Client) -> ListTopicsPaginator:
    """
    Equivalent of `client.get_paginator('list_topics')`, returns a correct type.
    """
    return client.get_paginator("list_topics")
