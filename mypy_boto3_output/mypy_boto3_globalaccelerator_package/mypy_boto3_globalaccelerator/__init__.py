"Main interface for globalaccelerator service"

from mypy_boto3_globalaccelerator.client import Client
from mypy_boto3_globalaccelerator.helpers import (
    boto3_client,
    get_list_accelerators_paginator,
    get_list_endpoint_groups_paginator,
    get_list_listeners_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_accelerators_paginator",
    "get_list_endpoint_groups_paginator",
    "get_list_listeners_paginator",
)
