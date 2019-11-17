"Main interface for athena service"

from mypy_boto3_athena.client import Client
from mypy_boto3_athena.helpers import (
    boto3_client,
    get_get_query_results_paginator,
    get_list_named_queries_paginator,
    get_list_query_executions_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_get_query_results_paginator",
    "get_list_named_queries_paginator",
    "get_list_query_executions_paginator",
)
