"Main interface for fsx service"

from mypy_boto3_fsx.client import Client
from mypy_boto3_fsx.helpers import (
    boto3_client,
    get_describe_backups_paginator,
    get_describe_file_systems_paginator,
    get_list_tags_for_resource_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_backups_paginator",
    "get_describe_file_systems_paginator",
    "get_list_tags_for_resource_paginator",
)
