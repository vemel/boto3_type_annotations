"Main interface for cognito-idp service"

from mypy_boto3_cognito_idp.client import Client
from mypy_boto3_cognito_idp.helpers import (
    boto3_client,
    get_admin_list_groups_for_user_paginator,
    get_admin_list_user_auth_events_paginator,
    get_list_groups_paginator,
    get_list_identity_providers_paginator,
    get_list_resource_servers_paginator,
    get_list_user_pool_clients_paginator,
    get_list_user_pools_paginator,
    get_list_users_in_group_paginator,
    get_list_users_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_admin_list_groups_for_user_paginator",
    "get_admin_list_user_auth_events_paginator",
    "get_list_groups_paginator",
    "get_list_identity_providers_paginator",
    "get_list_resource_servers_paginator",
    "get_list_user_pool_clients_paginator",
    "get_list_user_pools_paginator",
    "get_list_users_paginator",
    "get_list_users_in_group_paginator",
)
