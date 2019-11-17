"Main interface for dax service"

from mypy_boto3_dax.client import Client
from mypy_boto3_dax.helpers import (
    boto3_client,
    get_describe_clusters_paginator,
    get_describe_default_parameters_paginator,
    get_describe_events_paginator,
    get_describe_parameter_groups_paginator,
    get_describe_parameters_paginator,
    get_describe_subnet_groups_paginator,
    get_list_tags_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_clusters_paginator",
    "get_describe_default_parameters_paginator",
    "get_describe_events_paginator",
    "get_describe_parameter_groups_paginator",
    "get_describe_parameters_paginator",
    "get_describe_subnet_groups_paginator",
    "get_list_tags_paginator",
)
