"Helper functions for pricing service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_pricing.client import Client
from mypy_boto3_pricing.paginator import (
    DescribeServicesPaginator,
    GetAttributeValuesPaginator,
    GetProductsPaginator,
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
    Equivalent of `boto3.client('pricing')`, returns a correct type.
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
        return session.client("pricing", **kwargs)
    return boto3.client("pricing", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_services_paginator(client: Client) -> DescribeServicesPaginator:
    """
    Equivalent of `client.get_paginator('describe_services')`, returns a correct type.
    """
    return client.get_paginator("describe_services")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_attribute_values_paginator(client: Client) -> GetAttributeValuesPaginator:
    """
    Equivalent of `client.get_paginator('get_attribute_values')`, returns a correct type.
    """
    return client.get_paginator("get_attribute_values")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_products_paginator(client: Client) -> GetProductsPaginator:
    """
    Equivalent of `client.get_paginator('get_products')`, returns a correct type.
    """
    return client.get_paginator("get_products")
