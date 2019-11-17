"Main interface for dynamodb service"

from mypy_boto3_dynamodb.client import Client
from mypy_boto3_dynamodb.helpers import (
    boto3_client,
    boto3_resource,
    get_list_backups_paginator,
    get_list_tables_paginator,
    get_list_tags_of_resource_paginator,
    get_query_paginator,
    get_scan_paginator,
    get_table_exists_waiter,
    get_table_not_exists_waiter,
)
from mypy_boto3_dynamodb.service_resource import ServiceResource


__all__ = (
    "Client",
    "ServiceResource",
    "boto3_client",
    "boto3_resource",
    "get_list_backups_paginator",
    "get_list_tables_paginator",
    "get_list_tags_of_resource_paginator",
    "get_query_paginator",
    "get_scan_paginator",
    "get_table_exists_waiter",
    "get_table_not_exists_waiter",
)
