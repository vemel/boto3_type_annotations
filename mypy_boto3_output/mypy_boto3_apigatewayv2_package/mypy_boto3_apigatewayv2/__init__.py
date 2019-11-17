"Main interface for apigatewayv2 service"

from mypy_boto3_apigatewayv2.client import Client
from mypy_boto3_apigatewayv2.helpers import (
    boto3_client,
    get_get_apis_paginator,
    get_get_authorizers_paginator,
    get_get_deployments_paginator,
    get_get_domain_names_paginator,
    get_get_integration_responses_paginator,
    get_get_integrations_paginator,
    get_get_models_paginator,
    get_get_route_responses_paginator,
    get_get_routes_paginator,
    get_get_stages_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_get_apis_paginator",
    "get_get_authorizers_paginator",
    "get_get_deployments_paginator",
    "get_get_domain_names_paginator",
    "get_get_integration_responses_paginator",
    "get_get_integrations_paginator",
    "get_get_models_paginator",
    "get_get_route_responses_paginator",
    "get_get_routes_paginator",
    "get_get_stages_paginator",
)
