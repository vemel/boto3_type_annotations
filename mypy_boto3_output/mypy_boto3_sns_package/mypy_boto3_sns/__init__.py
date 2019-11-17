"Main interface for sns service"

from mypy_boto3_sns.client import Client
from mypy_boto3_sns.helpers import (
    boto3_client,
    boto3_resource,
    get_list_endpoints_by_platform_application_paginator,
    get_list_phone_numbers_opted_out_paginator,
    get_list_platform_applications_paginator,
    get_list_subscriptions_by_topic_paginator,
    get_list_subscriptions_paginator,
    get_list_topics_paginator,
)
from mypy_boto3_sns.service_resource import ServiceResource


__all__ = (
    "Client",
    "ServiceResource",
    "boto3_client",
    "boto3_resource",
    "get_list_endpoints_by_platform_application_paginator",
    "get_list_phone_numbers_opted_out_paginator",
    "get_list_platform_applications_paginator",
    "get_list_subscriptions_paginator",
    "get_list_subscriptions_by_topic_paginator",
    "get_list_topics_paginator",
)
