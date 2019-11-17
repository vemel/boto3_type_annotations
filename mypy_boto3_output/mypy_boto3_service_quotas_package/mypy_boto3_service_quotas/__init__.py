"Main interface for service-quotas service"

from mypy_boto3_service_quotas.client import Client
from mypy_boto3_service_quotas.helpers import (
    boto3_client,
    get_list_aws_default_service_quotas_paginator,
    get_list_requested_service_quota_change_history_by_quota_paginator,
    get_list_requested_service_quota_change_history_paginator,
    get_list_service_quota_increase_requests_in_template_paginator,
    get_list_service_quotas_paginator,
    get_list_services_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_aws_default_service_quotas_paginator",
    "get_list_requested_service_quota_change_history_paginator",
    "get_list_requested_service_quota_change_history_by_quota_paginator",
    "get_list_service_quota_increase_requests_in_template_paginator",
    "get_list_service_quotas_paginator",
    "get_list_services_paginator",
)
