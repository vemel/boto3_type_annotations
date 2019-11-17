"Main interface for elasticbeanstalk service"

from mypy_boto3_elasticbeanstalk.client import Client
from mypy_boto3_elasticbeanstalk.helpers import (
    boto3_client,
    get_describe_application_versions_paginator,
    get_describe_environment_managed_action_history_paginator,
    get_describe_environments_paginator,
    get_describe_events_paginator,
    get_list_platform_versions_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_application_versions_paginator",
    "get_describe_environment_managed_action_history_paginator",
    "get_describe_environments_paginator",
    "get_describe_events_paginator",
    "get_list_platform_versions_paginator",
)
