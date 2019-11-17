"Main interface for s3 service"

from mypy_boto3_s3.client import Client
from mypy_boto3_s3.helpers import (
    boto3_client,
    boto3_resource,
    get_bucket_exists_waiter,
    get_bucket_not_exists_waiter,
    get_list_multipart_uploads_paginator,
    get_list_object_versions_paginator,
    get_list_objects_paginator,
    get_list_objects_v2_paginator,
    get_list_parts_paginator,
    get_object_exists_waiter,
    get_object_not_exists_waiter,
)
from mypy_boto3_s3.service_resource import ServiceResource


__all__ = (
    "Client",
    "ServiceResource",
    "boto3_client",
    "boto3_resource",
    "get_list_multipart_uploads_paginator",
    "get_list_object_versions_paginator",
    "get_list_objects_paginator",
    "get_list_objects_v2_paginator",
    "get_list_parts_paginator",
    "get_bucket_exists_waiter",
    "get_bucket_not_exists_waiter",
    "get_object_exists_waiter",
    "get_object_not_exists_waiter",
)
