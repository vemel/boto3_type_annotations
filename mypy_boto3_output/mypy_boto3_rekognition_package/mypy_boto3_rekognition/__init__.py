"Main interface for rekognition service"

from mypy_boto3_rekognition.client import Client
from mypy_boto3_rekognition.helpers import (
    boto3_client,
    get_list_collections_paginator,
    get_list_faces_paginator,
    get_list_stream_processors_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_collections_paginator",
    "get_list_faces_paginator",
    "get_list_stream_processors_paginator",
)
