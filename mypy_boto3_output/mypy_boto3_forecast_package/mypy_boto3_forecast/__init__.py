"Main interface for forecast service"

from mypy_boto3_forecast.client import Client
from mypy_boto3_forecast.helpers import (
    boto3_client,
    get_list_dataset_groups_paginator,
    get_list_dataset_import_jobs_paginator,
    get_list_datasets_paginator,
    get_list_forecast_export_jobs_paginator,
    get_list_forecasts_paginator,
    get_list_predictors_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_list_dataset_groups_paginator",
    "get_list_dataset_import_jobs_paginator",
    "get_list_datasets_paginator",
    "get_list_forecast_export_jobs_paginator",
    "get_list_forecasts_paginator",
    "get_list_predictors_paginator",
)
