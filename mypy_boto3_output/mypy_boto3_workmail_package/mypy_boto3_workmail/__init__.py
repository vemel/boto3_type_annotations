"Main interface for workmail service"

from mypy_boto3_workmail.client import Client
from mypy_boto3_workmail.helpers import (
    boto3_client,
    get_list_aliases_paginator,
    get_list_group_members_paginator,
    get_list_groups_paginator,
    get_list_mailbox_permissions_paginator,
    get_list_organizations_paginator,
    get_list_resource_delegates_paginator,
    get_list_resources_paginator,
    get_list_users_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_aliases_paginator",
    "get_list_group_members_paginator",
    "get_list_groups_paginator",
    "get_list_mailbox_permissions_paginator",
    "get_list_organizations_paginator",
    "get_list_resource_delegates_paginator",
    "get_list_resources_paginator",
    "get_list_users_paginator",
)
