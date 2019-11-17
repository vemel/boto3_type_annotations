"Main interface for appsync service"

from mypy_boto3_appsync.client import Client
from mypy_boto3_appsync.helpers import (
    boto3_client,
    get_list_api_keys_paginator,
    get_list_data_sources_paginator,
    get_list_functions_paginator,
    get_list_graphql_apis_paginator,
    get_list_resolvers_by_function_paginator,
    get_list_resolvers_paginator,
    get_list_types_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_api_keys_paginator",
    "get_list_data_sources_paginator",
    "get_list_functions_paginator",
    "get_list_graphql_apis_paginator",
    "get_list_resolvers_paginator",
    "get_list_resolvers_by_function_paginator",
    "get_list_types_paginator",
)
