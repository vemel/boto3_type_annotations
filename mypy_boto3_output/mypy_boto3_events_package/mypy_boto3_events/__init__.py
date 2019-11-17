"Main interface for events service"

from mypy_boto3_events.client import Client
from mypy_boto3_events.helpers import (
    boto3_client,
    get_list_rule_names_by_target_paginator,
    get_list_rules_paginator,
    get_list_targets_by_rule_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_rule_names_by_target_paginator",
    "get_list_rules_paginator",
    "get_list_targets_by_rule_paginator",
)
