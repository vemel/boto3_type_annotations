"Main interface for resource-groups service"

from mypy_boto3_resource_groups.client import Client
from mypy_boto3_resource_groups.helpers import (
    boto3_client,
    get_list_group_resources_paginator,
    get_list_groups_paginator,
    get_search_resources_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_group_resources_paginator",
    "get_list_groups_paginator",
    "get_search_resources_paginator",
)
