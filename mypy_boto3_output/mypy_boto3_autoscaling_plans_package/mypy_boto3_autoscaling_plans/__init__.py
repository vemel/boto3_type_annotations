"Main interface for autoscaling-plans service"

from mypy_boto3_autoscaling_plans.client import Client
from mypy_boto3_autoscaling_plans.helpers import (
    boto3_client,
    get_describe_scaling_plan_resources_paginator,
    get_describe_scaling_plans_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_scaling_plan_resources_paginator",
    "get_describe_scaling_plans_paginator",
)
