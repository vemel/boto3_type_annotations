"Helper functions for mturk service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_mturk.client import Client
from mypy_boto3_mturk.paginator import (
    ListAssignmentsForHITPaginator,
    ListBonusPaymentsPaginator,
    ListHITsForQualificationTypePaginator,
    ListHITsPaginator,
    ListQualificationRequestsPaginator,
    ListQualificationTypesPaginator,
    ListReviewableHITsPaginator,
    ListWorkerBlocksPaginator,
    ListWorkersWithQualificationTypePaginator,
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
    Equivalent of `boto3.client('mturk')`, returns a correct type.
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
        return session.client("mturk", **kwargs)
    return boto3.client("mturk", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_assignments_for_hit_paginator(
    client: Client,
) -> ListAssignmentsForHITPaginator:
    """
    Equivalent of `client.get_paginator('list_assignments_for_hit')`, returns a correct type.
    """
    return client.get_paginator("list_assignments_for_hit")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_bonus_payments_paginator(client: Client) -> ListBonusPaymentsPaginator:
    """
    Equivalent of `client.get_paginator('list_bonus_payments')`, returns a correct type.
    """
    return client.get_paginator("list_bonus_payments")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_hits_paginator(client: Client) -> ListHITsPaginator:
    """
    Equivalent of `client.get_paginator('list_hits')`, returns a correct type.
    """
    return client.get_paginator("list_hits")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_hits_for_qualification_type_paginator(
    client: Client,
) -> ListHITsForQualificationTypePaginator:
    """
    Equivalent of `client.get_paginator('list_hits_for_qualification_type')`, returns a correct type.
    """
    return client.get_paginator("list_hits_for_qualification_type")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_qualification_requests_paginator(
    client: Client,
) -> ListQualificationRequestsPaginator:
    """
    Equivalent of `client.get_paginator('list_qualification_requests')`, returns a correct type.
    """
    return client.get_paginator("list_qualification_requests")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_qualification_types_paginator(
    client: Client,
) -> ListQualificationTypesPaginator:
    """
    Equivalent of `client.get_paginator('list_qualification_types')`, returns a correct type.
    """
    return client.get_paginator("list_qualification_types")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_reviewable_hits_paginator(client: Client) -> ListReviewableHITsPaginator:
    """
    Equivalent of `client.get_paginator('list_reviewable_hits')`, returns a correct type.
    """
    return client.get_paginator("list_reviewable_hits")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_worker_blocks_paginator(client: Client) -> ListWorkerBlocksPaginator:
    """
    Equivalent of `client.get_paginator('list_worker_blocks')`, returns a correct type.
    """
    return client.get_paginator("list_worker_blocks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_workers_with_qualification_type_paginator(
    client: Client,
) -> ListWorkersWithQualificationTypePaginator:
    """
    Equivalent of `client.get_paginator('list_workers_with_qualification_type')`, returns a correct type.
    """
    return client.get_paginator("list_workers_with_qualification_type")
