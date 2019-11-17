"Helper functions for guardduty service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_guardduty.client import Client
from mypy_boto3_guardduty.paginator import (
    ListDetectorsPaginator,
    ListFiltersPaginator,
    ListFindingsPaginator,
    ListIPSetsPaginator,
    ListInvitationsPaginator,
    ListMembersPaginator,
    ListThreatIntelSetsPaginator,
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
    Equivalent of `boto3.client('guardduty')`, returns a correct type.
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
        return session.client("guardduty", **kwargs)
    return boto3.client("guardduty", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_detectors_paginator(client: Client) -> ListDetectorsPaginator:
    """
    Equivalent of `client.get_paginator('list_detectors')`, returns a correct type.
    """
    return client.get_paginator("list_detectors")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_filters_paginator(client: Client) -> ListFiltersPaginator:
    """
    Equivalent of `client.get_paginator('list_filters')`, returns a correct type.
    """
    return client.get_paginator("list_filters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_findings_paginator(client: Client) -> ListFindingsPaginator:
    """
    Equivalent of `client.get_paginator('list_findings')`, returns a correct type.
    """
    return client.get_paginator("list_findings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_ip_sets_paginator(client: Client) -> ListIPSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_ip_sets')`, returns a correct type.
    """
    return client.get_paginator("list_ip_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_invitations_paginator(client: Client) -> ListInvitationsPaginator:
    """
    Equivalent of `client.get_paginator('list_invitations')`, returns a correct type.
    """
    return client.get_paginator("list_invitations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_members_paginator(client: Client) -> ListMembersPaginator:
    """
    Equivalent of `client.get_paginator('list_members')`, returns a correct type.
    """
    return client.get_paginator("list_members")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_threat_intel_sets_paginator(
    client: Client,
) -> ListThreatIntelSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_threat_intel_sets')`, returns a correct type.
    """
    return client.get_paginator("list_threat_intel_sets")
