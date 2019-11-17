"Helper functions for application-autoscaling service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_application_autoscaling.client import Client
from mypy_boto3_application_autoscaling.paginator import (
    DescribeScalableTargetsPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScalingPoliciesPaginator,
    DescribeScheduledActionsPaginator,
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
    Equivalent of `boto3.client('application-autoscaling')`, returns a correct type.
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
        return session.client("application-autoscaling", **kwargs)
    return boto3.client("application-autoscaling", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_scalable_targets_paginator(
    client: Client,
) -> DescribeScalableTargetsPaginator:
    """
    Equivalent of `client.get_paginator('describe_scalable_targets')`, returns a correct type.
    """
    return client.get_waiter("describe_scalable_targets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_scaling_activities_paginator(
    client: Client,
) -> DescribeScalingActivitiesPaginator:
    """
    Equivalent of `client.get_paginator('describe_scaling_activities')`, returns a correct type.
    """
    return client.get_waiter("describe_scaling_activities")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_scaling_policies_paginator(
    client: Client,
) -> DescribeScalingPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('describe_scaling_policies')`, returns a correct type.
    """
    return client.get_waiter("describe_scaling_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_scheduled_actions_paginator(
    client: Client,
) -> DescribeScheduledActionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_scheduled_actions')`, returns a correct type.
    """
    return client.get_waiter("describe_scheduled_actions")