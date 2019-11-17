"Main interface for workdocs service"

from mypy_boto3_workdocs.client import Client
from mypy_boto3_workdocs.helpers import (
    boto3_client,
    get_describe_activities_paginator,
    get_describe_comments_paginator,
    get_describe_document_versions_paginator,
    get_describe_folder_contents_paginator,
    get_describe_groups_paginator,
    get_describe_notification_subscriptions_paginator,
    get_describe_resource_permissions_paginator,
    get_describe_root_folders_paginator,
    get_describe_users_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_activities_paginator",
    "get_describe_comments_paginator",
    "get_describe_document_versions_paginator",
    "get_describe_folder_contents_paginator",
    "get_describe_groups_paginator",
    "get_describe_notification_subscriptions_paginator",
    "get_describe_resource_permissions_paginator",
    "get_describe_root_folders_paginator",
    "get_describe_users_paginator",
)
