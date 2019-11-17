"Main interface for workspaces service"

from mypy_boto3_workspaces.client import Client
from mypy_boto3_workspaces.helpers import (
    boto3_client,
    get_describe_account_modifications_paginator,
    get_describe_ip_groups_paginator,
    get_describe_workspace_bundles_paginator,
    get_describe_workspace_directories_paginator,
    get_describe_workspace_images_paginator,
    get_describe_workspaces_connection_status_paginator,
    get_describe_workspaces_paginator,
    get_list_available_management_cidr_ranges_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_account_modifications_paginator",
    "get_describe_ip_groups_paginator",
    "get_describe_workspace_bundles_paginator",
    "get_describe_workspace_directories_paginator",
    "get_describe_workspace_images_paginator",
    "get_describe_workspaces_paginator",
    "get_describe_workspaces_connection_status_paginator",
    "get_list_available_management_cidr_ranges_paginator",
)
