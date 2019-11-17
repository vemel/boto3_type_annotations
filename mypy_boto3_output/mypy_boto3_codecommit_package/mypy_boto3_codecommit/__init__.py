"Main interface for codecommit service"

from mypy_boto3_codecommit.client import Client
from mypy_boto3_codecommit.helpers import (
    boto3_client,
    get_describe_pull_request_events_paginator,
    get_get_comments_for_compared_commit_paginator,
    get_get_comments_for_pull_request_paginator,
    get_get_differences_paginator,
    get_list_branches_paginator,
    get_list_pull_requests_paginator,
    get_list_repositories_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_pull_request_events_paginator",
    "get_get_comments_for_compared_commit_paginator",
    "get_get_comments_for_pull_request_paginator",
    "get_get_differences_paginator",
    "get_list_branches_paginator",
    "get_list_pull_requests_paginator",
    "get_list_repositories_paginator",
)
