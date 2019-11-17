"Helper functions for personalize service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_personalize.client import Client
from mypy_boto3_personalize.paginator import (
    ListBatchInferenceJobsPaginator,
    ListCampaignsPaginator,
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListEventTrackersPaginator,
    ListRecipesPaginator,
    ListSchemasPaginator,
    ListSolutionVersionsPaginator,
    ListSolutionsPaginator,
)

# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_client(
    session: Session = None,
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Client:
    """
    Equivalent of `boto3.client('personalize')`, returns a correct type.
    """
    kwargs: Dict[str, Any] = {}
    if region_name is not None:
        kwargs["region_name"] = region_name
    if api_version is not None:
        kwargs["api_version"] = api_version
    if use_ssl is not None:
        kwargs["use_ssl"] = use_ssl
    if verify is not None:
        kwargs["verify"] = verify
    if endpoint_url is not None:
        kwargs["endpoint_url"] = endpoint_url
    if aws_access_key_id is not None:
        kwargs["aws_access_key_id"] = aws_access_key_id
    if aws_secret_access_key is not None:
        kwargs["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token is not None:
        kwargs["aws_session_token"] = aws_session_token
    if config is not None:
        kwargs["config"] = config
    if session is not None:
        return session.client("personalize", **kwargs)
    return boto3.client("personalize", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_batch_inference_jobs_paginator(
    client: Client,
) -> ListBatchInferenceJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_batch_inference_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_batch_inference_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_campaigns_paginator(client: Client) -> ListCampaignsPaginator:
    """
    Equivalent of `client.get_paginator('list_campaigns')`, returns a correct type.
    """
    return client.get_paginator("list_campaigns")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_dataset_groups_paginator(client: Client) -> ListDatasetGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_dataset_groups')`, returns a correct type.
    """
    return client.get_paginator("list_dataset_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_dataset_import_jobs_paginator(
    client: Client,
) -> ListDatasetImportJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_dataset_import_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_dataset_import_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_datasets_paginator(client: Client) -> ListDatasetsPaginator:
    """
    Equivalent of `client.get_paginator('list_datasets')`, returns a correct type.
    """
    return client.get_paginator("list_datasets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_event_trackers_paginator(client: Client) -> ListEventTrackersPaginator:
    """
    Equivalent of `client.get_paginator('list_event_trackers')`, returns a correct type.
    """
    return client.get_paginator("list_event_trackers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_recipes_paginator(client: Client) -> ListRecipesPaginator:
    """
    Equivalent of `client.get_paginator('list_recipes')`, returns a correct type.
    """
    return client.get_paginator("list_recipes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_schemas_paginator(client: Client) -> ListSchemasPaginator:
    """
    Equivalent of `client.get_paginator('list_schemas')`, returns a correct type.
    """
    return client.get_paginator("list_schemas")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_solution_versions_paginator(
    client: Client,
) -> ListSolutionVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_solution_versions')`, returns a correct type.
    """
    return client.get_paginator("list_solution_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_solutions_paginator(client: Client) -> ListSolutionsPaginator:
    """
    Equivalent of `client.get_paginator('list_solutions')`, returns a correct type.
    """
    return client.get_paginator("list_solutions")
