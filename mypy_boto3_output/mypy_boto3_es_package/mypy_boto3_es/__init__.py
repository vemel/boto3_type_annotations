"Main interface for es service"

from mypy_boto3_es.client import Client
from mypy_boto3_es.helpers import (
    boto3_client,
    get_describe_reserved_elasticsearch_instance_offerings_paginator,
    get_describe_reserved_elasticsearch_instances_paginator,
    get_get_upgrade_history_paginator,
    get_list_elasticsearch_instance_types_paginator,
    get_list_elasticsearch_versions_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_reserved_elasticsearch_instance_offerings_paginator",
    "get_describe_reserved_elasticsearch_instances_paginator",
    "get_get_upgrade_history_paginator",
    "get_list_elasticsearch_instance_types_paginator",
    "get_list_elasticsearch_versions_paginator",
)
