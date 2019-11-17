"Main interface for ds service"

from mypy_boto3_ds.client import Client
from mypy_boto3_ds.helpers import (
    boto3_client,
    get_describe_directories_paginator,
    get_describe_domain_controllers_paginator,
    get_describe_shared_directories_paginator,
    get_describe_snapshots_paginator,
    get_describe_trusts_paginator,
    get_list_ip_routes_paginator,
    get_list_log_subscriptions_paginator,
    get_list_schema_extensions_paginator,
    get_list_tags_for_resource_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_directories_paginator",
    "get_describe_domain_controllers_paginator",
    "get_describe_shared_directories_paginator",
    "get_describe_snapshots_paginator",
    "get_describe_trusts_paginator",
    "get_list_ip_routes_paginator",
    "get_list_log_subscriptions_paginator",
    "get_list_schema_extensions_paginator",
    "get_list_tags_for_resource_paginator",
)
