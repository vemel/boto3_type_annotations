"Main interface for servicediscovery service"

from mypy_boto3_servicediscovery.client import Client
from mypy_boto3_servicediscovery.helpers import (
    boto3_client,
    get_list_instances_paginator,
    get_list_namespaces_paginator,
    get_list_operations_paginator,
    get_list_services_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_instances_paginator",
    "get_list_namespaces_paginator",
    "get_list_operations_paginator",
    "get_list_services_paginator",
)
