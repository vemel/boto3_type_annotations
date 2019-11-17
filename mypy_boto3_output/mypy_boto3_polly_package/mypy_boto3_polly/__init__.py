"Main interface for polly service"

from mypy_boto3_polly.client import Client
from mypy_boto3_polly.helpers import (
    boto3_client,
    get_describe_voices_paginator,
    get_list_lexicons_paginator,
    get_list_speech_synthesis_tasks_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_voices_paginator",
    "get_list_lexicons_paginator",
    "get_list_speech_synthesis_tasks_paginator",
)
