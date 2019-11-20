"Helper functions for cloudformation service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_cloudformation.client import Client
from mypy_boto3_cloudformation.paginator import (
    DescribeAccountLimitsPaginator,
    DescribeChangeSetPaginator,
    DescribeStackEventsPaginator,
    DescribeStacksPaginator,
    ListChangeSetsPaginator,
    ListExportsPaginator,
    ListImportsPaginator,
    ListStackInstancesPaginator,
    ListStackResourcesPaginator,
    ListStackSetOperationResultsPaginator,
    ListStackSetOperationsPaginator,
    ListStackSetsPaginator,
    ListStacksPaginator,
)
from mypy_boto3_cloudformation.service_resource import ServiceResource
from mypy_boto3_cloudformation.waiter import (
    ChangeSetCreateCompleteWaiter,
    StackCreateCompleteWaiter,
    StackDeleteCompleteWaiter,
    StackExistsWaiter,
    StackImportCompleteWaiter,
    StackUpdateCompleteWaiter,
    TypeRegistrationCompleteWaiter,
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
    Equivalent of `boto3.client('cloudformation')`, returns a correct type.
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
        return session.client("cloudformation", **kwargs)
    return boto3.client("cloudformation", **kwargs)


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
    Equivalent of `boto3.resource('cloudformation')`, returns a correct type.
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
        return session.resource("cloudformation", **kwargs)
    return boto3.resource("cloudformation", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_account_limits_paginator(
    client: Client,
) -> DescribeAccountLimitsPaginator:
    """
    Equivalent of `client.get_paginator('describe_account_limits')`, returns a correct type.
    """
    return client.get_paginator("describe_account_limits")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_change_set_paginator(client: Client) -> DescribeChangeSetPaginator:
    """
    Equivalent of `client.get_paginator('describe_change_set')`, returns a correct type.
    """
    return client.get_paginator("describe_change_set")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_stack_events_paginator(client: Client) -> DescribeStackEventsPaginator:
    """
    Equivalent of `client.get_paginator('describe_stack_events')`, returns a correct type.
    """
    return client.get_paginator("describe_stack_events")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_stacks_paginator(client: Client) -> DescribeStacksPaginator:
    """
    Equivalent of `client.get_paginator('describe_stacks')`, returns a correct type.
    """
    return client.get_paginator("describe_stacks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_change_sets_paginator(client: Client) -> ListChangeSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_change_sets')`, returns a correct type.
    """
    return client.get_paginator("list_change_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_exports_paginator(client: Client) -> ListExportsPaginator:
    """
    Equivalent of `client.get_paginator('list_exports')`, returns a correct type.
    """
    return client.get_paginator("list_exports")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_imports_paginator(client: Client) -> ListImportsPaginator:
    """
    Equivalent of `client.get_paginator('list_imports')`, returns a correct type.
    """
    return client.get_paginator("list_imports")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_stack_instances_paginator(client: Client) -> ListStackInstancesPaginator:
    """
    Equivalent of `client.get_paginator('list_stack_instances')`, returns a correct type.
    """
    return client.get_paginator("list_stack_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_stack_resources_paginator(client: Client) -> ListStackResourcesPaginator:
    """
    Equivalent of `client.get_paginator('list_stack_resources')`, returns a correct type.
    """
    return client.get_paginator("list_stack_resources")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_stack_set_operation_results_paginator(
    client: Client,
) -> ListStackSetOperationResultsPaginator:
    """
    Equivalent of `client.get_paginator('list_stack_set_operation_results')`, returns a correct type.
    """
    return client.get_paginator("list_stack_set_operation_results")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_stack_set_operations_paginator(
    client: Client,
) -> ListStackSetOperationsPaginator:
    """
    Equivalent of `client.get_paginator('list_stack_set_operations')`, returns a correct type.
    """
    return client.get_paginator("list_stack_set_operations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_stack_sets_paginator(client: Client) -> ListStackSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_stack_sets')`, returns a correct type.
    """
    return client.get_paginator("list_stack_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_stacks_paginator(client: Client) -> ListStacksPaginator:
    """
    Equivalent of `client.get_paginator('list_stacks')`, returns a correct type.
    """
    return client.get_paginator("list_stacks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_change_set_create_complete_waiter(
    client: Client,
) -> ChangeSetCreateCompleteWaiter:
    """
    Equivalent of `client.get_waiter('change_set_create_complete')`, returns a correct type.
    """
    return client.get_waiter("change_set_create_complete")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_stack_create_complete_waiter(client: Client) -> StackCreateCompleteWaiter:
    """
    Equivalent of `client.get_waiter('stack_create_complete')`, returns a correct type.
    """
    return client.get_waiter("stack_create_complete")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_stack_delete_complete_waiter(client: Client) -> StackDeleteCompleteWaiter:
    """
    Equivalent of `client.get_waiter('stack_delete_complete')`, returns a correct type.
    """
    return client.get_waiter("stack_delete_complete")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_stack_exists_waiter(client: Client) -> StackExistsWaiter:
    """
    Equivalent of `client.get_waiter('stack_exists')`, returns a correct type.
    """
    return client.get_waiter("stack_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_stack_import_complete_waiter(client: Client) -> StackImportCompleteWaiter:
    """
    Equivalent of `client.get_waiter('stack_import_complete')`, returns a correct type.
    """
    return client.get_waiter("stack_import_complete")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_stack_update_complete_waiter(client: Client) -> StackUpdateCompleteWaiter:
    """
    Equivalent of `client.get_waiter('stack_update_complete')`, returns a correct type.
    """
    return client.get_waiter("stack_update_complete")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_type_registration_complete_waiter(
    client: Client,
) -> TypeRegistrationCompleteWaiter:
    """
    Equivalent of `client.get_waiter('type_registration_complete')`, returns a correct type.
    """
    return client.get_waiter("type_registration_complete")
