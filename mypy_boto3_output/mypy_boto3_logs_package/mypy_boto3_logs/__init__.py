"Main interface for logs service"

from mypy_boto3_logs.client import Client
from mypy_boto3_logs.helpers import (
    boto3_client,
    get_describe_destinations_paginator,
    get_describe_export_tasks_paginator,
    get_describe_log_groups_paginator,
    get_describe_log_streams_paginator,
    get_describe_metric_filters_paginator,
    get_describe_queries_paginator,
    get_describe_resource_policies_paginator,
    get_describe_subscription_filters_paginator,
    get_filter_log_events_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_destinations_paginator",
    "get_describe_export_tasks_paginator",
    "get_describe_log_groups_paginator",
    "get_describe_log_streams_paginator",
    "get_describe_metric_filters_paginator",
    "get_describe_queries_paginator",
    "get_describe_resource_policies_paginator",
    "get_describe_subscription_filters_paginator",
    "get_filter_log_events_paginator",
)
