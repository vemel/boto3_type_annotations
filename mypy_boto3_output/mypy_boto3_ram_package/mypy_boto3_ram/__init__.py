"Main interface for ram service"

from mypy_boto3_ram.client import Client
from mypy_boto3_ram.helpers import (
    boto3_client,
    get_get_resource_policies_paginator,
    get_get_resource_share_associations_paginator,
    get_get_resource_share_invitations_paginator,
    get_get_resource_shares_paginator,
    get_list_principals_paginator,
    get_list_resources_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_get_resource_policies_paginator",
    "get_get_resource_share_associations_paginator",
    "get_get_resource_share_invitations_paginator",
    "get_get_resource_shares_paginator",
    "get_list_principals_paginator",
    "get_list_resources_paginator",
)
