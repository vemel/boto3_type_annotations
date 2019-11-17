"Main interface for opsworkscm service"

from mypy_boto3_opsworkscm.client import Client
from mypy_boto3_opsworkscm.helpers import (
    boto3_client,
    get_describe_backups_paginator,
    get_describe_events_paginator,
    get_describe_servers_paginator,
    get_node_associated_waiter,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_backups_paginator",
    "get_describe_events_paginator",
    "get_describe_servers_paginator",
    "get_node_associated_waiter",
)
