"Main interface for cloudwatch service"

from mypy_boto3_cloudwatch.client import Client
from mypy_boto3_cloudwatch.helpers import (
    boto3_client,
    boto3_resource,
    get_alarm_exists_waiter,
    get_describe_alarm_history_paginator,
    get_describe_alarms_paginator,
    get_get_metric_data_paginator,
    get_list_dashboards_paginator,
    get_list_metrics_paginator,
)
from mypy_boto3_cloudwatch.service_resource import ServiceResource


__all__ = (
    "Client",
    "ServiceResource",
    "boto3_client",
    "boto3_resource",
    "get_describe_alarm_history_paginator",
    "get_describe_alarms_paginator",
    "get_get_metric_data_paginator",
    "get_list_dashboards_paginator",
    "get_list_metrics_paginator",
    "get_alarm_exists_waiter",
)
