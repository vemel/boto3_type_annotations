"Main interface for efs service"

from mypy_boto3_efs.client import Client
from mypy_boto3_efs.helpers import (
    boto3_client,
    get_describe_file_systems_paginator,
    get_describe_mount_targets_paginator,
    get_describe_tags_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_file_systems_paginator",
    "get_describe_mount_targets_paginator",
    "get_describe_tags_paginator",
)
