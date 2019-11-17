"Main interface for cloudtrail service"

from mypy_boto3_cloudtrail.client import Client
from mypy_boto3_cloudtrail.helpers import (
    boto3_client,
    get_list_public_keys_paginator,
    get_list_tags_paginator,
    get_list_trails_paginator,
    get_lookup_events_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_public_keys_paginator",
    "get_list_tags_paginator",
    "get_list_trails_paginator",
    "get_lookup_events_paginator",
)
