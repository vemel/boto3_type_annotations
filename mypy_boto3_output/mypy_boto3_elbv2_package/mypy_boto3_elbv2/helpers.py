"Helper functions for elbv2 service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_elbv2.client import Client
from mypy_boto3_elbv2.paginator import (
    DescribeAccountLimitsPaginator,
    DescribeListenerCertificatesPaginator,
    DescribeListenersPaginator,
    DescribeLoadBalancersPaginator,
    DescribeRulesPaginator,
    DescribeSSLPoliciesPaginator,
    DescribeTargetGroupsPaginator,
)
from mypy_boto3_elbv2.waiter import (
    LoadBalancerAvailableWaiter,
    LoadBalancerExistsWaiter,
    LoadBalancersDeletedWaiter,
    TargetDeregisteredWaiter,
    TargetInServiceWaiter,
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
    Equivalent of `boto3.client('elbv2')`, returns a correct type.
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
        return session.client("elbv2", **kwargs)
    return boto3.client("elbv2", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_account_limits_paginator(
    client: Client,
) -> DescribeAccountLimitsPaginator:
    """
    Equivalent of `client.get_paginator('describe_account_limits')`, returns a correct type.
    """
    return client.get_waiter("describe_account_limits")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_listener_certificates_paginator(
    client: Client,
) -> DescribeListenerCertificatesPaginator:
    """
    Equivalent of `client.get_paginator('describe_listener_certificates')`, returns a correct type.
    """
    return client.get_waiter("describe_listener_certificates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_listeners_paginator(client: Client) -> DescribeListenersPaginator:
    """
    Equivalent of `client.get_paginator('describe_listeners')`, returns a correct type.
    """
    return client.get_waiter("describe_listeners")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_load_balancers_paginator(
    client: Client,
) -> DescribeLoadBalancersPaginator:
    """
    Equivalent of `client.get_paginator('describe_load_balancers')`, returns a correct type.
    """
    return client.get_waiter("describe_load_balancers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_rules_paginator(client: Client) -> DescribeRulesPaginator:
    """
    Equivalent of `client.get_paginator('describe_rules')`, returns a correct type.
    """
    return client.get_waiter("describe_rules")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_ssl_policies_paginator(client: Client) -> DescribeSSLPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('describe_ssl_policies')`, returns a correct type.
    """
    return client.get_waiter("describe_ssl_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_target_groups_paginator(
    client: Client,
) -> DescribeTargetGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_target_groups')`, returns a correct type.
    """
    return client.get_waiter("describe_target_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_load_balancer_available_waiter(client: Client) -> LoadBalancerAvailableWaiter:
    """
    Equivalent of `client.get_waiter('load_balancer_available')`, returns a correct type.
    """
    return client.get_waiter("load_balancer_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_load_balancer_exists_waiter(client: Client) -> LoadBalancerExistsWaiter:
    """
    Equivalent of `client.get_waiter('load_balancer_exists')`, returns a correct type.
    """
    return client.get_waiter("load_balancer_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_load_balancers_deleted_waiter(client: Client) -> LoadBalancersDeletedWaiter:
    """
    Equivalent of `client.get_waiter('load_balancers_deleted')`, returns a correct type.
    """
    return client.get_waiter("load_balancers_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_target_deregistered_waiter(client: Client) -> TargetDeregisteredWaiter:
    """
    Equivalent of `client.get_waiter('target_deregistered')`, returns a correct type.
    """
    return client.get_waiter("target_deregistered")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_target_in_service_waiter(client: Client) -> TargetInServiceWaiter:
    """
    Equivalent of `client.get_waiter('target_in_service')`, returns a correct type.
    """
    return client.get_waiter("target_in_service")