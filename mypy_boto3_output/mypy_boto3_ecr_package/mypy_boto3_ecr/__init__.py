"Main interface for ecr service"

from mypy_boto3_ecr.client import Client
from mypy_boto3_ecr.helpers import (
    boto3_client,
    get_describe_image_scan_findings_paginator,
    get_describe_images_paginator,
    get_describe_repositories_paginator,
    get_get_lifecycle_policy_preview_paginator,
    get_list_images_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_image_scan_findings_paginator",
    "get_describe_images_paginator",
    "get_describe_repositories_paginator",
    "get_get_lifecycle_policy_preview_paginator",
    "get_list_images_paginator",
)
