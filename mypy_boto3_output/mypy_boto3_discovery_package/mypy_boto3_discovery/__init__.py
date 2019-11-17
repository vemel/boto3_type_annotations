"Main interface for discovery service"

from mypy_boto3_discovery.client import Client
from mypy_boto3_discovery.helpers import (
    boto3_client,
    get_describe_agents_paginator,
    get_describe_continuous_exports_paginator,
    get_describe_export_configurations_paginator,
    get_describe_export_tasks_paginator,
    get_describe_tags_paginator,
    get_list_configurations_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_agents_paginator",
    "get_describe_continuous_exports_paginator",
    "get_describe_export_configurations_paginator",
    "get_describe_export_tasks_paginator",
    "get_describe_tags_paginator",
    "get_list_configurations_paginator",
)
