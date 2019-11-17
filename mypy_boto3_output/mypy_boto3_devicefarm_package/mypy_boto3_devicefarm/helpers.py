"Helper functions for devicefarm service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_devicefarm.client import Client
from mypy_boto3_devicefarm.paginator import (
    GetOfferingStatusPaginator,
    ListArtifactsPaginator,
    ListDeviceInstancesPaginator,
    ListDevicePoolsPaginator,
    ListDevicesPaginator,
    ListInstanceProfilesPaginator,
    ListJobsPaginator,
    ListNetworkProfilesPaginator,
    ListOfferingPromotionsPaginator,
    ListOfferingTransactionsPaginator,
    ListOfferingsPaginator,
    ListProjectsPaginator,
    ListRemoteAccessSessionsPaginator,
    ListRunsPaginator,
    ListSamplesPaginator,
    ListSuitesPaginator,
    ListTestsPaginator,
    ListUniqueProblemsPaginator,
    ListUploadsPaginator,
    ListVPCEConfigurationsPaginator,
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
    Equivalent of `boto3.client('devicefarm')`, returns a correct type.
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
        return session.client("devicefarm", **kwargs)
    return boto3.client("devicefarm", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_offering_status_paginator(client: Client) -> GetOfferingStatusPaginator:
    """
    Equivalent of `client.get_paginator('get_offering_status')`, returns a correct type.
    """
    return client.get_paginator("get_offering_status")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_artifacts_paginator(client: Client) -> ListArtifactsPaginator:
    """
    Equivalent of `client.get_paginator('list_artifacts')`, returns a correct type.
    """
    return client.get_paginator("list_artifacts")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_device_instances_paginator(client: Client) -> ListDeviceInstancesPaginator:
    """
    Equivalent of `client.get_paginator('list_device_instances')`, returns a correct type.
    """
    return client.get_paginator("list_device_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_device_pools_paginator(client: Client) -> ListDevicePoolsPaginator:
    """
    Equivalent of `client.get_paginator('list_device_pools')`, returns a correct type.
    """
    return client.get_paginator("list_device_pools")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_devices_paginator(client: Client) -> ListDevicesPaginator:
    """
    Equivalent of `client.get_paginator('list_devices')`, returns a correct type.
    """
    return client.get_paginator("list_devices")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_instance_profiles_paginator(
    client: Client,
) -> ListInstanceProfilesPaginator:
    """
    Equivalent of `client.get_paginator('list_instance_profiles')`, returns a correct type.
    """
    return client.get_paginator("list_instance_profiles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_jobs_paginator(client: Client) -> ListJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_network_profiles_paginator(client: Client) -> ListNetworkProfilesPaginator:
    """
    Equivalent of `client.get_paginator('list_network_profiles')`, returns a correct type.
    """
    return client.get_paginator("list_network_profiles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_offering_promotions_paginator(
    client: Client,
) -> ListOfferingPromotionsPaginator:
    """
    Equivalent of `client.get_paginator('list_offering_promotions')`, returns a correct type.
    """
    return client.get_paginator("list_offering_promotions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_offering_transactions_paginator(
    client: Client,
) -> ListOfferingTransactionsPaginator:
    """
    Equivalent of `client.get_paginator('list_offering_transactions')`, returns a correct type.
    """
    return client.get_paginator("list_offering_transactions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_offerings_paginator(client: Client) -> ListOfferingsPaginator:
    """
    Equivalent of `client.get_paginator('list_offerings')`, returns a correct type.
    """
    return client.get_paginator("list_offerings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_projects_paginator(client: Client) -> ListProjectsPaginator:
    """
    Equivalent of `client.get_paginator('list_projects')`, returns a correct type.
    """
    return client.get_paginator("list_projects")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_remote_access_sessions_paginator(
    client: Client,
) -> ListRemoteAccessSessionsPaginator:
    """
    Equivalent of `client.get_paginator('list_remote_access_sessions')`, returns a correct type.
    """
    return client.get_paginator("list_remote_access_sessions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_runs_paginator(client: Client) -> ListRunsPaginator:
    """
    Equivalent of `client.get_paginator('list_runs')`, returns a correct type.
    """
    return client.get_paginator("list_runs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_samples_paginator(client: Client) -> ListSamplesPaginator:
    """
    Equivalent of `client.get_paginator('list_samples')`, returns a correct type.
    """
    return client.get_paginator("list_samples")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_suites_paginator(client: Client) -> ListSuitesPaginator:
    """
    Equivalent of `client.get_paginator('list_suites')`, returns a correct type.
    """
    return client.get_paginator("list_suites")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tests_paginator(client: Client) -> ListTestsPaginator:
    """
    Equivalent of `client.get_paginator('list_tests')`, returns a correct type.
    """
    return client.get_paginator("list_tests")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_unique_problems_paginator(client: Client) -> ListUniqueProblemsPaginator:
    """
    Equivalent of `client.get_paginator('list_unique_problems')`, returns a correct type.
    """
    return client.get_paginator("list_unique_problems")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_uploads_paginator(client: Client) -> ListUploadsPaginator:
    """
    Equivalent of `client.get_paginator('list_uploads')`, returns a correct type.
    """
    return client.get_paginator("list_uploads")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_vpce_configurations_paginator(
    client: Client,
) -> ListVPCEConfigurationsPaginator:
    """
    Equivalent of `client.get_paginator('list_vpce_configurations')`, returns a correct type.
    """
    return client.get_paginator("list_vpce_configurations")
