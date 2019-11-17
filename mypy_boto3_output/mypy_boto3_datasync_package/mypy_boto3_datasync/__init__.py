"Main interface for datasync service"

from mypy_boto3_datasync.client import Client
from mypy_boto3_datasync.helpers import (
    boto3_client,
    get_list_agents_paginator,
    get_list_locations_paginator,
    get_list_tags_for_resource_paginator,
    get_list_task_executions_paginator,
    get_list_tasks_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_agents_paginator",
    "get_list_locations_paginator",
    "get_list_tags_for_resource_paginator",
    "get_list_task_executions_paginator",
    "get_list_tasks_paginator",
)
