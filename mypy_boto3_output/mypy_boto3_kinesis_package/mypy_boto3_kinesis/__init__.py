"Main interface for kinesis service"

from mypy_boto3_kinesis.client import Client
from mypy_boto3_kinesis.helpers import (
    boto3_client,
    get_describe_stream_paginator,
    get_list_shards_paginator,
    get_list_stream_consumers_paginator,
    get_list_streams_paginator,
    get_stream_exists_waiter,
    get_stream_not_exists_waiter,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_stream_paginator",
    "get_list_shards_paginator",
    "get_list_stream_consumers_paginator",
    "get_list_streams_paginator",
    "get_stream_exists_waiter",
    "get_stream_not_exists_waiter",
)
