"Main interface for xray service"

from mypy_boto3_xray.client import Client
from mypy_boto3_xray.helpers import (
    boto3_client,
    get_batch_get_traces_paginator,
    get_get_groups_paginator,
    get_get_sampling_rules_paginator,
    get_get_sampling_statistic_summaries_paginator,
    get_get_service_graph_paginator,
    get_get_time_series_service_statistics_paginator,
    get_get_trace_graph_paginator,
    get_get_trace_summaries_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_batch_get_traces_paginator",
    "get_get_groups_paginator",
    "get_get_sampling_rules_paginator",
    "get_get_sampling_statistic_summaries_paginator",
    "get_get_service_graph_paginator",
    "get_get_time_series_service_statistics_paginator",
    "get_get_trace_graph_paginator",
    "get_get_trace_summaries_paginator",
)
