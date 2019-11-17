"Main interface for shield service"

from mypy_boto3_shield.client import Client
from mypy_boto3_shield.helpers import (
    boto3_client,
    get_list_attacks_paginator,
    get_list_protections_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_attacks_paginator",
    "get_list_protections_paginator",
)
