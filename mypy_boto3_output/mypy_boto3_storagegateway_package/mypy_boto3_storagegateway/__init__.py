"Main interface for storagegateway service"

from mypy_boto3_storagegateway.client import Client
from mypy_boto3_storagegateway.helpers import (
    boto3_client,
    get_describe_tape_archives_paginator,
    get_describe_tape_recovery_points_paginator,
    get_describe_tapes_paginator,
    get_describe_vtl_devices_paginator,
    get_list_file_shares_paginator,
    get_list_gateways_paginator,
    get_list_tags_for_resource_paginator,
    get_list_tapes_paginator,
    get_list_volumes_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_tape_archives_paginator",
    "get_describe_tape_recovery_points_paginator",
    "get_describe_tapes_paginator",
    "get_describe_vtl_devices_paginator",
    "get_list_file_shares_paginator",
    "get_list_gateways_paginator",
    "get_list_tags_for_resource_paginator",
    "get_list_tapes_paginator",
    "get_list_volumes_paginator",
)
