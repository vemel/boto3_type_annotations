"Main interface for apigateway service"

from mypy_boto3_apigateway.client import Client
from mypy_boto3_apigateway.helpers import (
    boto3_client,
    get_get_api_keys_paginator,
    get_get_authorizers_paginator,
    get_get_base_path_mappings_paginator,
    get_get_client_certificates_paginator,
    get_get_deployments_paginator,
    get_get_documentation_parts_paginator,
    get_get_documentation_versions_paginator,
    get_get_domain_names_paginator,
    get_get_gateway_responses_paginator,
    get_get_models_paginator,
    get_get_request_validators_paginator,
    get_get_resources_paginator,
    get_get_rest_apis_paginator,
    get_get_sdk_types_paginator,
    get_get_usage_paginator,
    get_get_usage_plan_keys_paginator,
    get_get_usage_plans_paginator,
    get_get_vpc_links_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_get_api_keys_paginator",
    "get_get_authorizers_paginator",
    "get_get_base_path_mappings_paginator",
    "get_get_client_certificates_paginator",
    "get_get_deployments_paginator",
    "get_get_documentation_parts_paginator",
    "get_get_documentation_versions_paginator",
    "get_get_domain_names_paginator",
    "get_get_gateway_responses_paginator",
    "get_get_models_paginator",
    "get_get_request_validators_paginator",
    "get_get_resources_paginator",
    "get_get_rest_apis_paginator",
    "get_get_sdk_types_paginator",
    "get_get_usage_paginator",
    "get_get_usage_plan_keys_paginator",
    "get_get_usage_plans_paginator",
    "get_get_vpc_links_paginator",
)
