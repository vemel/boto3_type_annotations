"Helper functions for dynamodb service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_dynamodb.client import Client
from mypy_boto3_dynamodb.paginator import (
    ListBackupsPaginator,
    ListTablesPaginator,
    ListTagsOfResourcePaginator,
    QueryPaginator,
    ScanPaginator,
)
from mypy_boto3_dynamodb.service_resource import ServiceResource
from mypy_boto3_dynamodb.waiter import TableExistsWaiter, TableNotExistsWaiter

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
    Equivalent of `boto3.client('dynamodb')`, returns a correct type.
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
        return session.client("dynamodb", **kwargs)
    return boto3.client("dynamodb", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_resource(
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
) -> ServiceResource:
    """
    Equivalent of `boto3.resource('dynamodb')`, returns a correct type.
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
        return session.resource("dynamodb", **kwargs)
    return boto3.resource("dynamodb", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_backups_paginator(client: Client) -> ListBackupsPaginator:
    """
    Equivalent of `client.get_paginator('list_backups')`, returns a correct type.
    """
    return client.get_paginator("list_backups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tables_paginator(client: Client) -> ListTablesPaginator:
    """
    Equivalent of `client.get_paginator('list_tables')`, returns a correct type.
    """
    return client.get_paginator("list_tables")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_of_resource_paginator(client: Client) -> ListTagsOfResourcePaginator:
    """
    Equivalent of `client.get_paginator('list_tags_of_resource')`, returns a correct type.
    """
    return client.get_paginator("list_tags_of_resource")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_query_paginator(client: Client) -> QueryPaginator:
    """
    Equivalent of `client.get_paginator('query')`, returns a correct type.
    """
    return client.get_paginator("query")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_scan_paginator(client: Client) -> ScanPaginator:
    """
    Equivalent of `client.get_paginator('scan')`, returns a correct type.
    """
    return client.get_paginator("scan")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_table_exists_waiter(client: Client) -> TableExistsWaiter:
    """
    Equivalent of `client.get_waiter('table_exists')`, returns a correct type.
    """
    return client.get_waiter("table_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_table_not_exists_waiter(client: Client) -> TableNotExistsWaiter:
    """
    Equivalent of `client.get_waiter('table_not_exists')`, returns a correct type.
    """
    return client.get_waiter("table_not_exists")
