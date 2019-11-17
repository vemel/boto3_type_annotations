"Main interface for personalize service"

from mypy_boto3_personalize.client import Client
from mypy_boto3_personalize.helpers import (
    boto3_client,
    get_list_batch_inference_jobs_paginator,
    get_list_campaigns_paginator,
    get_list_dataset_groups_paginator,
    get_list_dataset_import_jobs_paginator,
    get_list_datasets_paginator,
    get_list_event_trackers_paginator,
    get_list_recipes_paginator,
    get_list_schemas_paginator,
    get_list_solution_versions_paginator,
    get_list_solutions_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_batch_inference_jobs_paginator",
    "get_list_campaigns_paginator",
    "get_list_dataset_groups_paginator",
    "get_list_dataset_import_jobs_paginator",
    "get_list_datasets_paginator",
    "get_list_event_trackers_paginator",
    "get_list_recipes_paginator",
    "get_list_schemas_paginator",
    "get_list_solution_versions_paginator",
    "get_list_solutions_paginator",
)
