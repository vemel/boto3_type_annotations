"Main interface for health service"

from mypy_boto3_health.client import Client
from mypy_boto3_health.helpers import (
    boto3_client,
    get_describe_affected_entities_paginator,
    get_describe_event_aggregates_paginator,
    get_describe_event_types_paginator,
    get_describe_events_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_affected_entities_paginator",
    "get_describe_event_aggregates_paginator",
    "get_describe_event_types_paginator",
    "get_describe_events_paginator",
)
