"Helper functions for fms service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_fms.client import Client
from mypy_boto3_fms.paginator import (
    ListComplianceStatusPaginator,
    ListMemberAccountsPaginator,
    ListPoliciesPaginator,
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
    Equivalent of `boto3.client('fms')`, returns a correct type.
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
        return session.client("fms", **kwargs)
    return boto3.client("fms", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_compliance_status_paginator(
    client: Client,
) -> ListComplianceStatusPaginator:
    """
    Equivalent of `client.get_paginator('list_compliance_status')`, returns a correct type.
    """
    return client.get_paginator("list_compliance_status")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_member_accounts_paginator(client: Client) -> ListMemberAccountsPaginator:
    """
    Equivalent of `client.get_paginator('list_member_accounts')`, returns a correct type.
    """
    return client.get_paginator("list_member_accounts")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_policies_paginator(client: Client) -> ListPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_policies')`, returns a correct type.
    """
    return client.get_paginator("list_policies")
