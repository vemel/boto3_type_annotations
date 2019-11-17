"Main interface for resourcegroupstaggingapi service"

from mypy_boto3_resourcegroupstaggingapi.client import Client
from mypy_boto3_resourcegroupstaggingapi.helpers import (
    boto3_client,
    get_get_resources_paginator,
    get_get_tag_keys_paginator,
    get_get_tag_values_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_get_resources_paginator",
    "get_get_tag_keys_paginator",
    "get_get_tag_values_paginator",
)
