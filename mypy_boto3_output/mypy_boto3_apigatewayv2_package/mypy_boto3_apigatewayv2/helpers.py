"Helper functions for apigatewayv2 service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_apigatewayv2.client import Client
from mypy_boto3_apigatewayv2.paginator import (
    GetApisPaginator,
    GetAuthorizersPaginator,
    GetDeploymentsPaginator,
    GetDomainNamesPaginator,
    GetIntegrationResponsesPaginator,
    GetIntegrationsPaginator,
    GetModelsPaginator,
    GetRouteResponsesPaginator,
    GetRoutesPaginator,
    GetStagesPaginator,
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
    Equivalent of `boto3.client('apigatewayv2')`, returns a correct type.
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
        return session.client("apigatewayv2", **kwargs)
    return boto3.client("apigatewayv2", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_apis_paginator(client: Client) -> GetApisPaginator:
    """
    Equivalent of `client.get_paginator('get_apis')`, returns a correct type.
    """
    return client.get_paginator("get_apis")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_authorizers_paginator(client: Client) -> GetAuthorizersPaginator:
    """
    Equivalent of `client.get_paginator('get_authorizers')`, returns a correct type.
    """
    return client.get_paginator("get_authorizers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_deployments_paginator(client: Client) -> GetDeploymentsPaginator:
    """
    Equivalent of `client.get_paginator('get_deployments')`, returns a correct type.
    """
    return client.get_paginator("get_deployments")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_domain_names_paginator(client: Client) -> GetDomainNamesPaginator:
    """
    Equivalent of `client.get_paginator('get_domain_names')`, returns a correct type.
    """
    return client.get_paginator("get_domain_names")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_integration_responses_paginator(
    client: Client,
) -> GetIntegrationResponsesPaginator:
    """
    Equivalent of `client.get_paginator('get_integration_responses')`, returns a correct type.
    """
    return client.get_paginator("get_integration_responses")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_integrations_paginator(client: Client) -> GetIntegrationsPaginator:
    """
    Equivalent of `client.get_paginator('get_integrations')`, returns a correct type.
    """
    return client.get_paginator("get_integrations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_models_paginator(client: Client) -> GetModelsPaginator:
    """
    Equivalent of `client.get_paginator('get_models')`, returns a correct type.
    """
    return client.get_paginator("get_models")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_route_responses_paginator(client: Client) -> GetRouteResponsesPaginator:
    """
    Equivalent of `client.get_paginator('get_route_responses')`, returns a correct type.
    """
    return client.get_paginator("get_route_responses")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_routes_paginator(client: Client) -> GetRoutesPaginator:
    """
    Equivalent of `client.get_paginator('get_routes')`, returns a correct type.
    """
    return client.get_paginator("get_routes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_stages_paginator(client: Client) -> GetStagesPaginator:
    """
    Equivalent of `client.get_paginator('get_stages')`, returns a correct type.
    """
    return client.get_paginator("get_stages")
