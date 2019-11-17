"Main interface for amplify service"

from mypy_boto3_amplify.client import Client
from mypy_boto3_amplify.helpers import (
    boto3_client,
    get_list_apps_paginator,
    get_list_branches_paginator,
    get_list_domain_associations_paginator,
    get_list_jobs_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_apps_paginator",
    "get_list_branches_paginator",
    "get_list_domain_associations_paginator",
    "get_list_jobs_paginator",
)
