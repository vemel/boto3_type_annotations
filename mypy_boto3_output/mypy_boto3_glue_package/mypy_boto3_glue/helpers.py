"Helper functions for glue service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_glue.client import Client
from mypy_boto3_glue.paginator import (
    GetClassifiersPaginator,
    GetConnectionsPaginator,
    GetCrawlerMetricsPaginator,
    GetCrawlersPaginator,
    GetDatabasesPaginator,
    GetDevEndpointsPaginator,
    GetJobRunsPaginator,
    GetJobsPaginator,
    GetPartitionsPaginator,
    GetSecurityConfigurationsPaginator,
    GetTableVersionsPaginator,
    GetTablesPaginator,
    GetTriggersPaginator,
    GetUserDefinedFunctionsPaginator,
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
    Equivalent of `boto3.client('glue')`, returns a correct type.
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
        return session.client("glue", **kwargs)
    return boto3.client("glue", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_classifiers_paginator(client: Client) -> GetClassifiersPaginator:
    """
    Equivalent of `client.get_paginator('get_classifiers')`, returns a correct type.
    """
    return client.get_paginator("get_classifiers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_connections_paginator(client: Client) -> GetConnectionsPaginator:
    """
    Equivalent of `client.get_paginator('get_connections')`, returns a correct type.
    """
    return client.get_paginator("get_connections")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_crawler_metrics_paginator(client: Client) -> GetCrawlerMetricsPaginator:
    """
    Equivalent of `client.get_paginator('get_crawler_metrics')`, returns a correct type.
    """
    return client.get_paginator("get_crawler_metrics")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_crawlers_paginator(client: Client) -> GetCrawlersPaginator:
    """
    Equivalent of `client.get_paginator('get_crawlers')`, returns a correct type.
    """
    return client.get_paginator("get_crawlers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_databases_paginator(client: Client) -> GetDatabasesPaginator:
    """
    Equivalent of `client.get_paginator('get_databases')`, returns a correct type.
    """
    return client.get_paginator("get_databases")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_dev_endpoints_paginator(client: Client) -> GetDevEndpointsPaginator:
    """
    Equivalent of `client.get_paginator('get_dev_endpoints')`, returns a correct type.
    """
    return client.get_paginator("get_dev_endpoints")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_job_runs_paginator(client: Client) -> GetJobRunsPaginator:
    """
    Equivalent of `client.get_paginator('get_job_runs')`, returns a correct type.
    """
    return client.get_paginator("get_job_runs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_jobs_paginator(client: Client) -> GetJobsPaginator:
    """
    Equivalent of `client.get_paginator('get_jobs')`, returns a correct type.
    """
    return client.get_paginator("get_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_partitions_paginator(client: Client) -> GetPartitionsPaginator:
    """
    Equivalent of `client.get_paginator('get_partitions')`, returns a correct type.
    """
    return client.get_paginator("get_partitions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_security_configurations_paginator(
    client: Client,
) -> GetSecurityConfigurationsPaginator:
    """
    Equivalent of `client.get_paginator('get_security_configurations')`, returns a correct type.
    """
    return client.get_paginator("get_security_configurations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_table_versions_paginator(client: Client) -> GetTableVersionsPaginator:
    """
    Equivalent of `client.get_paginator('get_table_versions')`, returns a correct type.
    """
    return client.get_paginator("get_table_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_tables_paginator(client: Client) -> GetTablesPaginator:
    """
    Equivalent of `client.get_paginator('get_tables')`, returns a correct type.
    """
    return client.get_paginator("get_tables")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_triggers_paginator(client: Client) -> GetTriggersPaginator:
    """
    Equivalent of `client.get_paginator('get_triggers')`, returns a correct type.
    """
    return client.get_paginator("get_triggers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_user_defined_functions_paginator(
    client: Client,
) -> GetUserDefinedFunctionsPaginator:
    """
    Equivalent of `client.get_paginator('get_user_defined_functions')`, returns a correct type.
    """
    return client.get_paginator("get_user_defined_functions")
