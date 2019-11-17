"Main interface for mediaconnect service"

from mypy_boto3_mediaconnect.client import Client
from mypy_boto3_mediaconnect.helpers import (
    boto3_client,
    get_list_entitlements_paginator,
    get_list_flows_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_entitlements_paginator",
    "get_list_flows_paginator",
)
