"Main interface for pinpoint-email service"

from mypy_boto3_pinpoint_email.client import Client
from mypy_boto3_pinpoint_email.helpers import (
    boto3_client,
    get_get_dedicated_ips_paginator,
    get_list_configuration_sets_paginator,
    get_list_dedicated_ip_pools_paginator,
    get_list_deliverability_test_reports_paginator,
    get_list_email_identities_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_get_dedicated_ips_paginator",
    "get_list_configuration_sets_paginator",
    "get_list_dedicated_ip_pools_paginator",
    "get_list_deliverability_test_reports_paginator",
    "get_list_email_identities_paginator",
)
