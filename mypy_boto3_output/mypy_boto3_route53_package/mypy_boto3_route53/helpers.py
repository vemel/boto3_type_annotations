"Helper functions for route53 service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_route53.client import Client
from mypy_boto3_route53.paginator import (
    ListHealthChecksPaginator,
    ListHostedZonesPaginator,
    ListQueryLoggingConfigsPaginator,
    ListResourceRecordSetsPaginator,
    ListVPCAssociationAuthorizationsPaginator,
)
from mypy_boto3_route53.waiter import ResourceRecordSetsChangedWaiter

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
    Equivalent of `boto3.client('route53')`, returns a correct type.
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
        return session.client("route53", **kwargs)
    return boto3.client("route53", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_health_checks_paginator(client: Client) -> ListHealthChecksPaginator:
    """
    Equivalent of `client.get_paginator('list_health_checks')`, returns a correct type.
    """
    return client.get_paginator("list_health_checks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_hosted_zones_paginator(client: Client) -> ListHostedZonesPaginator:
    """
    Equivalent of `client.get_paginator('list_hosted_zones')`, returns a correct type.
    """
    return client.get_paginator("list_hosted_zones")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_query_logging_configs_paginator(
    client: Client,
) -> ListQueryLoggingConfigsPaginator:
    """
    Equivalent of `client.get_paginator('list_query_logging_configs')`, returns a correct type.
    """
    return client.get_paginator("list_query_logging_configs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resource_record_sets_paginator(
    client: Client,
) -> ListResourceRecordSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_resource_record_sets')`, returns a correct type.
    """
    return client.get_paginator("list_resource_record_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_vpc_association_authorizations_paginator(
    client: Client,
) -> ListVPCAssociationAuthorizationsPaginator:
    """
    Equivalent of `client.get_paginator('list_vpc_association_authorizations')`, returns a correct type.
    """
    return client.get_paginator("list_vpc_association_authorizations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_resource_record_sets_changed_waiter(
    client: Client,
) -> ResourceRecordSetsChangedWaiter:
    """
    Equivalent of `client.get_waiter('resource_record_sets_changed')`, returns a correct type.
    """
    return client.get_waiter("resource_record_sets_changed")
