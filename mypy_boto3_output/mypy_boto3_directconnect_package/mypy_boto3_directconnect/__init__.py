"Main interface for directconnect service"

from mypy_boto3_directconnect.client import Client
from mypy_boto3_directconnect.helpers import (
    boto3_client,
    get_describe_direct_connect_gateway_associations_paginator,
    get_describe_direct_connect_gateway_attachments_paginator,
    get_describe_direct_connect_gateways_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_direct_connect_gateway_associations_paginator",
    "get_describe_direct_connect_gateway_attachments_paginator",
    "get_describe_direct_connect_gateways_paginator",
)
