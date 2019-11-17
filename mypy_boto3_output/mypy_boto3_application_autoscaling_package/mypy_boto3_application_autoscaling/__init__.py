"Main interface for application-autoscaling service"

from mypy_boto3_application_autoscaling.client import Client
from mypy_boto3_application_autoscaling.helpers import (
    boto3_client,
    get_describe_scalable_targets_paginator,
    get_describe_scaling_activities_paginator,
    get_describe_scaling_policies_paginator,
    get_describe_scheduled_actions_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_scalable_targets_paginator",
    "get_describe_scaling_activities_paginator",
    "get_describe_scaling_policies_paginator",
    "get_describe_scheduled_actions_paginator",
)
