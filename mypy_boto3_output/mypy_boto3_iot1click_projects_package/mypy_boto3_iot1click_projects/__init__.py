"Main interface for iot1click-projects service"

from mypy_boto3_iot1click_projects.client import Client
from mypy_boto3_iot1click_projects.helpers import (
    boto3_client,
    get_list_placements_paginator,
    get_list_projects_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_placements_paginator",
    "get_list_projects_paginator",
)
