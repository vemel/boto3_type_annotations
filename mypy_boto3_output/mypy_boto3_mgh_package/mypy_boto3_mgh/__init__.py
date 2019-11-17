"Main interface for mgh service"

from mypy_boto3_mgh.client import Client
from mypy_boto3_mgh.helpers import (
    boto3_client,
    get_list_created_artifacts_paginator,
    get_list_discovered_resources_paginator,
    get_list_migration_tasks_paginator,
    get_list_progress_update_streams_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_created_artifacts_paginator",
    "get_list_discovered_resources_paginator",
    "get_list_migration_tasks_paginator",
    "get_list_progress_update_streams_paginator",
)
