"Main interface for sdb service"

from mypy_boto3_sdb.client import Client
from mypy_boto3_sdb.helpers import (
    boto3_client,
    get_list_domains_paginator,
    get_select_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_domains_paginator",
    "get_select_paginator",
)
