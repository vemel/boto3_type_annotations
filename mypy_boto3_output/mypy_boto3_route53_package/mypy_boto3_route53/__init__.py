"Main interface for route53 service"

from mypy_boto3_route53.client import Client
from mypy_boto3_route53.helpers import (
    boto3_client,
    get_list_health_checks_paginator,
    get_list_hosted_zones_paginator,
    get_list_query_logging_configs_paginator,
    get_list_resource_record_sets_paginator,
    get_list_vpc_association_authorizations_paginator,
    get_resource_record_sets_changed_waiter,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_health_checks_paginator",
    "get_list_hosted_zones_paginator",
    "get_list_query_logging_configs_paginator",
    "get_list_resource_record_sets_paginator",
    "get_list_vpc_association_authorizations_paginator",
    "get_resource_record_sets_changed_waiter",
)
