"Helper functions for autoscaling service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_autoscaling.client import Client
from mypy_boto3_autoscaling.paginator import (
    DescribeAutoScalingGroupsPaginator,
    DescribeAutoScalingInstancesPaginator,
    DescribeLaunchConfigurationsPaginator,
    DescribeLoadBalancerTargetGroupsPaginator,
    DescribeLoadBalancersPaginator,
    DescribeNotificationConfigurationsPaginator,
    DescribePoliciesPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScheduledActionsPaginator,
    DescribeTagsPaginator,
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
    Equivalent of `boto3.client('autoscaling')`, returns a correct type.
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
        return session.client("autoscaling", **kwargs)
    return boto3.client("autoscaling", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_auto_scaling_groups_paginator(
    client: Client,
) -> DescribeAutoScalingGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_auto_scaling_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_auto_scaling_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_auto_scaling_instances_paginator(
    client: Client,
) -> DescribeAutoScalingInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_auto_scaling_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_auto_scaling_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_launch_configurations_paginator(
    client: Client,
) -> DescribeLaunchConfigurationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_launch_configurations')`, returns a correct type.
    """
    return client.get_paginator("describe_launch_configurations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_load_balancer_target_groups_paginator(
    client: Client,
) -> DescribeLoadBalancerTargetGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_load_balancer_target_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_load_balancer_target_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_load_balancers_paginator(
    client: Client,
) -> DescribeLoadBalancersPaginator:
    """
    Equivalent of `client.get_paginator('describe_load_balancers')`, returns a correct type.
    """
    return client.get_paginator("describe_load_balancers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_notification_configurations_paginator(
    client: Client,
) -> DescribeNotificationConfigurationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_notification_configurations')`, returns a correct type.
    """
    return client.get_paginator("describe_notification_configurations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_policies_paginator(client: Client) -> DescribePoliciesPaginator:
    """
    Equivalent of `client.get_paginator('describe_policies')`, returns a correct type.
    """
    return client.get_paginator("describe_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_scaling_activities_paginator(
    client: Client,
) -> DescribeScalingActivitiesPaginator:
    """
    Equivalent of `client.get_paginator('describe_scaling_activities')`, returns a correct type.
    """
    return client.get_paginator("describe_scaling_activities")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_scheduled_actions_paginator(
    client: Client,
) -> DescribeScheduledActionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_scheduled_actions')`, returns a correct type.
    """
    return client.get_paginator("describe_scheduled_actions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_tags_paginator(client: Client) -> DescribeTagsPaginator:
    """
    Equivalent of `client.get_paginator('describe_tags')`, returns a correct type.
    """
    return client.get_paginator("describe_tags")
