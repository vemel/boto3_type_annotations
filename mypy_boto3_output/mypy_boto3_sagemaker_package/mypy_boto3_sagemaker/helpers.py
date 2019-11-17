"Helper functions for sagemaker service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_sagemaker.client import Client
from mypy_boto3_sagemaker.paginator import (
    ListAlgorithmsPaginator,
    ListCodeRepositoriesPaginator,
    ListCompilationJobsPaginator,
    ListEndpointConfigsPaginator,
    ListEndpointsPaginator,
    ListHyperParameterTuningJobsPaginator,
    ListLabelingJobsForWorkteamPaginator,
    ListLabelingJobsPaginator,
    ListModelPackagesPaginator,
    ListModelsPaginator,
    ListNotebookInstanceLifecycleConfigsPaginator,
    ListNotebookInstancesPaginator,
    ListSubscribedWorkteamsPaginator,
    ListTagsPaginator,
    ListTrainingJobsForHyperParameterTuningJobPaginator,
    ListTrainingJobsPaginator,
    ListTransformJobsPaginator,
    ListWorkteamsPaginator,
    SearchPaginator,
)
from mypy_boto3_sagemaker.waiter import (
    EndpointDeletedWaiter,
    EndpointInServiceWaiter,
    NotebookInstanceDeletedWaiter,
    NotebookInstanceInServiceWaiter,
    NotebookInstanceStoppedWaiter,
    TrainingJobCompletedOrStoppedWaiter,
    TransformJobCompletedOrStoppedWaiter,
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
    Equivalent of `boto3.client('sagemaker')`, returns a correct type.
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
        return session.client("sagemaker", **kwargs)
    return boto3.client("sagemaker", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_algorithms_paginator(client: Client) -> ListAlgorithmsPaginator:
    """
    Equivalent of `client.get_paginator('list_algorithms')`, returns a correct type.
    """
    return client.get_paginator("list_algorithms")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_code_repositories_paginator(
    client: Client,
) -> ListCodeRepositoriesPaginator:
    """
    Equivalent of `client.get_paginator('list_code_repositories')`, returns a correct type.
    """
    return client.get_paginator("list_code_repositories")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_compilation_jobs_paginator(client: Client) -> ListCompilationJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_compilation_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_compilation_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_endpoint_configs_paginator(client: Client) -> ListEndpointConfigsPaginator:
    """
    Equivalent of `client.get_paginator('list_endpoint_configs')`, returns a correct type.
    """
    return client.get_paginator("list_endpoint_configs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_endpoints_paginator(client: Client) -> ListEndpointsPaginator:
    """
    Equivalent of `client.get_paginator('list_endpoints')`, returns a correct type.
    """
    return client.get_paginator("list_endpoints")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_hyper_parameter_tuning_jobs_paginator(
    client: Client,
) -> ListHyperParameterTuningJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_hyper_parameter_tuning_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_hyper_parameter_tuning_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_labeling_jobs_paginator(client: Client) -> ListLabelingJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_labeling_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_labeling_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_labeling_jobs_for_workteam_paginator(
    client: Client,
) -> ListLabelingJobsForWorkteamPaginator:
    """
    Equivalent of `client.get_paginator('list_labeling_jobs_for_workteam')`, returns a correct type.
    """
    return client.get_paginator("list_labeling_jobs_for_workteam")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_model_packages_paginator(client: Client) -> ListModelPackagesPaginator:
    """
    Equivalent of `client.get_paginator('list_model_packages')`, returns a correct type.
    """
    return client.get_paginator("list_model_packages")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_models_paginator(client: Client) -> ListModelsPaginator:
    """
    Equivalent of `client.get_paginator('list_models')`, returns a correct type.
    """
    return client.get_paginator("list_models")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_notebook_instance_lifecycle_configs_paginator(
    client: Client,
) -> ListNotebookInstanceLifecycleConfigsPaginator:
    """
    Equivalent of `client.get_paginator('list_notebook_instance_lifecycle_configs')`, returns a correct type.
    """
    return client.get_paginator("list_notebook_instance_lifecycle_configs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_notebook_instances_paginator(
    client: Client,
) -> ListNotebookInstancesPaginator:
    """
    Equivalent of `client.get_paginator('list_notebook_instances')`, returns a correct type.
    """
    return client.get_paginator("list_notebook_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_subscribed_workteams_paginator(
    client: Client,
) -> ListSubscribedWorkteamsPaginator:
    """
    Equivalent of `client.get_paginator('list_subscribed_workteams')`, returns a correct type.
    """
    return client.get_paginator("list_subscribed_workteams")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_paginator(client: Client) -> ListTagsPaginator:
    """
    Equivalent of `client.get_paginator('list_tags')`, returns a correct type.
    """
    return client.get_paginator("list_tags")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_training_jobs_paginator(client: Client) -> ListTrainingJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_training_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_training_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_training_jobs_for_hyper_parameter_tuning_job_paginator(
    client: Client,
) -> ListTrainingJobsForHyperParameterTuningJobPaginator:
    """
    Equivalent of `client.get_paginator('list_training_jobs_for_hyper_parameter_tuning_job')`, returns a correct type.
    """
    return client.get_paginator("list_training_jobs_for_hyper_parameter_tuning_job")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_transform_jobs_paginator(client: Client) -> ListTransformJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_transform_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_transform_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_workteams_paginator(client: Client) -> ListWorkteamsPaginator:
    """
    Equivalent of `client.get_paginator('list_workteams')`, returns a correct type.
    """
    return client.get_paginator("list_workteams")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_paginator(client: Client) -> SearchPaginator:
    """
    Equivalent of `client.get_paginator('search')`, returns a correct type.
    """
    return client.get_paginator("search")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_endpoint_deleted_waiter(client: Client) -> EndpointDeletedWaiter:
    """
    Equivalent of `client.get_waiter('endpoint_deleted')`, returns a correct type.
    """
    return client.get_waiter("endpoint_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_endpoint_in_service_waiter(client: Client) -> EndpointInServiceWaiter:
    """
    Equivalent of `client.get_waiter('endpoint_in_service')`, returns a correct type.
    """
    return client.get_waiter("endpoint_in_service")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_notebook_instance_deleted_waiter(
    client: Client,
) -> NotebookInstanceDeletedWaiter:
    """
    Equivalent of `client.get_waiter('notebook_instance_deleted')`, returns a correct type.
    """
    return client.get_waiter("notebook_instance_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_notebook_instance_in_service_waiter(
    client: Client,
) -> NotebookInstanceInServiceWaiter:
    """
    Equivalent of `client.get_waiter('notebook_instance_in_service')`, returns a correct type.
    """
    return client.get_waiter("notebook_instance_in_service")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_notebook_instance_stopped_waiter(
    client: Client,
) -> NotebookInstanceStoppedWaiter:
    """
    Equivalent of `client.get_waiter('notebook_instance_stopped')`, returns a correct type.
    """
    return client.get_waiter("notebook_instance_stopped")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_training_job_completed_or_stopped_waiter(
    client: Client,
) -> TrainingJobCompletedOrStoppedWaiter:
    """
    Equivalent of `client.get_waiter('training_job_completed_or_stopped')`, returns a correct type.
    """
    return client.get_waiter("training_job_completed_or_stopped")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_transform_job_completed_or_stopped_waiter(
    client: Client,
) -> TransformJobCompletedOrStoppedWaiter:
    """
    Equivalent of `client.get_waiter('transform_job_completed_or_stopped')`, returns a correct type.
    """
    return client.get_waiter("transform_job_completed_or_stopped")
