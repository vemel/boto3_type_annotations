"Helper functions for apigateway service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_apigateway.client import Client
from mypy_boto3_apigateway.paginator import (
    GetApiKeysPaginator,
    GetAuthorizersPaginator,
    GetBasePathMappingsPaginator,
    GetClientCertificatesPaginator,
    GetDeploymentsPaginator,
    GetDocumentationPartsPaginator,
    GetDocumentationVersionsPaginator,
    GetDomainNamesPaginator,
    GetGatewayResponsesPaginator,
    GetModelsPaginator,
    GetRequestValidatorsPaginator,
    GetResourcesPaginator,
    GetRestApisPaginator,
    GetSdkTypesPaginator,
    GetUsagePaginator,
    GetUsagePlanKeysPaginator,
    GetUsagePlansPaginator,
    GetVpcLinksPaginator,
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
    Equivalent of `boto3.client('apigateway')`, returns a correct type.
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
        return session.client("apigateway", **kwargs)
    return boto3.client("apigateway", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_api_keys_paginator(client: Client) -> GetApiKeysPaginator:
    """
    Equivalent of `client.get_paginator('get_api_keys')`, returns a correct type.
    """
    return client.get_paginator("get_api_keys")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_authorizers_paginator(client: Client) -> GetAuthorizersPaginator:
    """
    Equivalent of `client.get_paginator('get_authorizers')`, returns a correct type.
    """
    return client.get_paginator("get_authorizers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_base_path_mappings_paginator(
    client: Client,
) -> GetBasePathMappingsPaginator:
    """
    Equivalent of `client.get_paginator('get_base_path_mappings')`, returns a correct type.
    """
    return client.get_paginator("get_base_path_mappings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_client_certificates_paginator(
    client: Client,
) -> GetClientCertificatesPaginator:
    """
    Equivalent of `client.get_paginator('get_client_certificates')`, returns a correct type.
    """
    return client.get_paginator("get_client_certificates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_deployments_paginator(client: Client) -> GetDeploymentsPaginator:
    """
    Equivalent of `client.get_paginator('get_deployments')`, returns a correct type.
    """
    return client.get_paginator("get_deployments")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_documentation_parts_paginator(
    client: Client,
) -> GetDocumentationPartsPaginator:
    """
    Equivalent of `client.get_paginator('get_documentation_parts')`, returns a correct type.
    """
    return client.get_paginator("get_documentation_parts")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_documentation_versions_paginator(
    client: Client,
) -> GetDocumentationVersionsPaginator:
    """
    Equivalent of `client.get_paginator('get_documentation_versions')`, returns a correct type.
    """
    return client.get_paginator("get_documentation_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_domain_names_paginator(client: Client) -> GetDomainNamesPaginator:
    """
    Equivalent of `client.get_paginator('get_domain_names')`, returns a correct type.
    """
    return client.get_paginator("get_domain_names")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_gateway_responses_paginator(client: Client) -> GetGatewayResponsesPaginator:
    """
    Equivalent of `client.get_paginator('get_gateway_responses')`, returns a correct type.
    """
    return client.get_paginator("get_gateway_responses")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_models_paginator(client: Client) -> GetModelsPaginator:
    """
    Equivalent of `client.get_paginator('get_models')`, returns a correct type.
    """
    return client.get_paginator("get_models")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_request_validators_paginator(
    client: Client,
) -> GetRequestValidatorsPaginator:
    """
    Equivalent of `client.get_paginator('get_request_validators')`, returns a correct type.
    """
    return client.get_paginator("get_request_validators")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_resources_paginator(client: Client) -> GetResourcesPaginator:
    """
    Equivalent of `client.get_paginator('get_resources')`, returns a correct type.
    """
    return client.get_paginator("get_resources")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_rest_apis_paginator(client: Client) -> GetRestApisPaginator:
    """
    Equivalent of `client.get_paginator('get_rest_apis')`, returns a correct type.
    """
    return client.get_paginator("get_rest_apis")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_sdk_types_paginator(client: Client) -> GetSdkTypesPaginator:
    """
    Equivalent of `client.get_paginator('get_sdk_types')`, returns a correct type.
    """
    return client.get_paginator("get_sdk_types")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_usage_paginator(client: Client) -> GetUsagePaginator:
    """
    Equivalent of `client.get_paginator('get_usage')`, returns a correct type.
    """
    return client.get_paginator("get_usage")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_usage_plan_keys_paginator(client: Client) -> GetUsagePlanKeysPaginator:
    """
    Equivalent of `client.get_paginator('get_usage_plan_keys')`, returns a correct type.
    """
    return client.get_paginator("get_usage_plan_keys")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_usage_plans_paginator(client: Client) -> GetUsagePlansPaginator:
    """
    Equivalent of `client.get_paginator('get_usage_plans')`, returns a correct type.
    """
    return client.get_paginator("get_usage_plans")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_vpc_links_paginator(client: Client) -> GetVpcLinksPaginator:
    """
    Equivalent of `client.get_paginator('get_vpc_links')`, returns a correct type.
    """
    return client.get_paginator("get_vpc_links")
