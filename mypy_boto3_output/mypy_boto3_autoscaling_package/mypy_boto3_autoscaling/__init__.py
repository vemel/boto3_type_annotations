"Main interface for autoscaling service"

from mypy_boto3_autoscaling.client import Client
from mypy_boto3_autoscaling.helpers import (
    boto3_client,
    get_describe_auto_scaling_groups_paginator,
    get_describe_auto_scaling_instances_paginator,
    get_describe_launch_configurations_paginator,
    get_describe_load_balancer_target_groups_paginator,
    get_describe_load_balancers_paginator,
    get_describe_notification_configurations_paginator,
    get_describe_policies_paginator,
    get_describe_scaling_activities_paginator,
    get_describe_scheduled_actions_paginator,
    get_describe_tags_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_auto_scaling_groups_paginator",
    "get_describe_auto_scaling_instances_paginator",
    "get_describe_launch_configurations_paginator",
    "get_describe_load_balancer_target_groups_paginator",
    "get_describe_load_balancers_paginator",
    "get_describe_notification_configurations_paginator",
    "get_describe_policies_paginator",
    "get_describe_scaling_activities_paginator",
    "get_describe_scheduled_actions_paginator",
    "get_describe_tags_paginator",
)
