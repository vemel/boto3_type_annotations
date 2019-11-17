"Main interface for docdb service"

from mypy_boto3_docdb.client import Client
from mypy_boto3_docdb.helpers import (
    boto3_client,
    get_db_instance_available_waiter,
    get_db_instance_deleted_waiter,
    get_describe_db_clusters_paginator,
    get_describe_db_engine_versions_paginator,
    get_describe_db_instances_paginator,
    get_describe_db_subnet_groups_paginator,
    get_describe_events_paginator,
    get_describe_orderable_db_instance_options_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_db_clusters_paginator",
    "get_describe_db_engine_versions_paginator",
    "get_describe_db_instances_paginator",
    "get_describe_db_subnet_groups_paginator",
    "get_describe_events_paginator",
    "get_describe_orderable_db_instance_options_paginator",
    "get_db_instance_available_waiter",
    "get_db_instance_deleted_waiter",
)
