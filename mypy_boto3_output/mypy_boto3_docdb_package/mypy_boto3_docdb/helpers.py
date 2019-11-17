"Helper functions for docdb service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_docdb.client import Client
from mypy_boto3_docdb.paginator import (
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEventsPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
)
from mypy_boto3_docdb.waiter import DBInstanceAvailableWaiter, DBInstanceDeletedWaiter

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
    Equivalent of `boto3.client('docdb')`, returns a correct type.
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
        return session.client("docdb", **kwargs)
    return boto3.client("docdb", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_clusters_paginator(client: Client) -> DescribeDBClustersPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_clusters')`, returns a correct type.
    """
    return client.get_paginator("describe_db_clusters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_engine_versions_paginator(
    client: Client,
) -> DescribeDBEngineVersionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_engine_versions')`, returns a correct type.
    """
    return client.get_paginator("describe_db_engine_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_instances_paginator(client: Client) -> DescribeDBInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_db_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_db_subnet_groups_paginator(
    client: Client,
) -> DescribeDBSubnetGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_db_subnet_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_db_subnet_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_events_paginator(client: Client) -> DescribeEventsPaginator:
    """
    Equivalent of `client.get_paginator('describe_events')`, returns a correct type.
    """
    return client.get_paginator("describe_events")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_orderable_db_instance_options_paginator(
    client: Client,
) -> DescribeOrderableDBInstanceOptionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_orderable_db_instance_options')`, returns a correct type.
    """
    return client.get_paginator("describe_orderable_db_instance_options")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_db_instance_available_waiter(client: Client) -> DBInstanceAvailableWaiter:
    """
    Equivalent of `client.get_waiter('db_instance_available')`, returns a correct type.
    """
    return client.get_waiter("db_instance_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_db_instance_deleted_waiter(client: Client) -> DBInstanceDeletedWaiter:
    """
    Equivalent of `client.get_waiter('db_instance_deleted')`, returns a correct type.
    """
    return client.get_waiter("db_instance_deleted")
