"Main interface for codestar-notifications service"

from mypy_boto3_codestar_notifications.client import Client
from mypy_boto3_codestar_notifications.helpers import (
    boto3_client,
    get_list_event_types_paginator,
    get_list_notification_rules_paginator,
    get_list_targets_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_event_types_paginator",
    "get_list_notification_rules_paginator",
    "get_list_targets_paginator",
)
