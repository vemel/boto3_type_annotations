"Main interface for organizations service"

from mypy_boto3_organizations.client import Client
from mypy_boto3_organizations.helpers import (
    boto3_client,
    get_list_accounts_for_parent_paginator,
    get_list_accounts_paginator,
    get_list_aws_service_access_for_organization_paginator,
    get_list_children_paginator,
    get_list_create_account_status_paginator,
    get_list_handshakes_for_account_paginator,
    get_list_handshakes_for_organization_paginator,
    get_list_organizational_units_for_parent_paginator,
    get_list_parents_paginator,
    get_list_policies_for_target_paginator,
    get_list_policies_paginator,
    get_list_roots_paginator,
    get_list_tags_for_resource_paginator,
    get_list_targets_for_policy_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_aws_service_access_for_organization_paginator",
    "get_list_accounts_paginator",
    "get_list_accounts_for_parent_paginator",
    "get_list_children_paginator",
    "get_list_create_account_status_paginator",
    "get_list_handshakes_for_account_paginator",
    "get_list_handshakes_for_organization_paginator",
    "get_list_organizational_units_for_parent_paginator",
    "get_list_parents_paginator",
    "get_list_policies_paginator",
    "get_list_policies_for_target_paginator",
    "get_list_roots_paginator",
    "get_list_tags_for_resource_paginator",
    "get_list_targets_for_policy_paginator",
)
