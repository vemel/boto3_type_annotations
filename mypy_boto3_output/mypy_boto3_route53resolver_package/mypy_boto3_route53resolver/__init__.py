"Main interface for route53resolver service"

from mypy_boto3_route53resolver.client import Client
from mypy_boto3_route53resolver.helpers import (
    boto3_client,
    get_list_tags_for_resource_paginator,
)


__all__ = ("Client", "boto3_client", "get_list_tags_for_resource_paginator")
