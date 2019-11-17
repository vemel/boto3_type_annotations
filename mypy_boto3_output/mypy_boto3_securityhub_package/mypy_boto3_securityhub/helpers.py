"Helper functions for securityhub service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_securityhub.client import Client
from mypy_boto3_securityhub.paginator import (
    GetEnabledStandardsPaginator,
    GetFindingsPaginator,
    GetInsightsPaginator,
    ListEnabledProductsForImportPaginator,
    ListInvitationsPaginator,
    ListMembersPaginator,
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
    Equivalent of `boto3.client('securityhub')`, returns a correct type.
    """
    kwargs = {}
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
        return session.client("securityhub", **kwargs)
    return boto3.client("securityhub", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_enabled_standards_paginator(client: Client) -> GetEnabledStandardsPaginator:
    """
    Equivalent of `client.get_paginator('get_enabled_standards')`, returns a correct type.
    """
    return client.get_waiter("get_enabled_standards")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_findings_paginator(client: Client) -> GetFindingsPaginator:
    """
    Equivalent of `client.get_paginator('get_findings')`, returns a correct type.
    """
    return client.get_waiter("get_findings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_insights_paginator(client: Client) -> GetInsightsPaginator:
    """
    Equivalent of `client.get_paginator('get_insights')`, returns a correct type.
    """
    return client.get_waiter("get_insights")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_enabled_products_for_import_paginator(
    client: Client,
) -> ListEnabledProductsForImportPaginator:
    """
    Equivalent of `client.get_paginator('list_enabled_products_for_import')`, returns a correct type.
    """
    return client.get_waiter("list_enabled_products_for_import")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_invitations_paginator(client: Client) -> ListInvitationsPaginator:
    """
    Equivalent of `client.get_paginator('list_invitations')`, returns a correct type.
    """
    return client.get_waiter("list_invitations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_members_paginator(client: Client) -> ListMembersPaginator:
    """
    Equivalent of `client.get_paginator('list_members')`, returns a correct type.
    """
    return client.get_waiter("list_members")