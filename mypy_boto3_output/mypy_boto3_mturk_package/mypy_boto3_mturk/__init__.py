"Main interface for mturk service"

from mypy_boto3_mturk.client import Client
from mypy_boto3_mturk.helpers import (
    boto3_client,
    get_list_assignments_for_hit_paginator,
    get_list_bonus_payments_paginator,
    get_list_hits_for_qualification_type_paginator,
    get_list_hits_paginator,
    get_list_qualification_requests_paginator,
    get_list_qualification_types_paginator,
    get_list_reviewable_hits_paginator,
    get_list_worker_blocks_paginator,
    get_list_workers_with_qualification_type_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_assignments_for_hit_paginator",
    "get_list_bonus_payments_paginator",
    "get_list_hits_paginator",
    "get_list_hits_for_qualification_type_paginator",
    "get_list_qualification_requests_paginator",
    "get_list_qualification_types_paginator",
    "get_list_reviewable_hits_paginator",
    "get_list_worker_blocks_paginator",
    "get_list_workers_with_qualification_type_paginator",
)
