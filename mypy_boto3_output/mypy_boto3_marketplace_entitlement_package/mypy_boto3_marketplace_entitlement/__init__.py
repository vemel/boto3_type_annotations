"Main interface for marketplace-entitlement service"

from mypy_boto3_marketplace_entitlement.client import Client
from mypy_boto3_marketplace_entitlement.helpers import (
    boto3_client,
    get_get_entitlements_paginator,
)


__all__ = ("Client", "boto3_client", "get_get_entitlements_paginator")
