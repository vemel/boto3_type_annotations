"Helper functions for codecommit service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_codecommit.client import Client
from mypy_boto3_codecommit.paginator import (
    DescribePullRequestEventsPaginator,
    GetCommentsForComparedCommitPaginator,
    GetCommentsForPullRequestPaginator,
    GetDifferencesPaginator,
    ListBranchesPaginator,
    ListPullRequestsPaginator,
    ListRepositoriesPaginator,
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
    Equivalent of `boto3.client('codecommit')`, returns a correct type.
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
        return session.client("codecommit", **kwargs)
    return boto3.client("codecommit", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_pull_request_events_paginator(
    client: Client,
) -> DescribePullRequestEventsPaginator:
    """
    Equivalent of `client.get_paginator('describe_pull_request_events')`, returns a correct type.
    """
    return client.get_paginator("describe_pull_request_events")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_comments_for_compared_commit_paginator(
    client: Client,
) -> GetCommentsForComparedCommitPaginator:
    """
    Equivalent of `client.get_paginator('get_comments_for_compared_commit')`, returns a correct type.
    """
    return client.get_paginator("get_comments_for_compared_commit")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_comments_for_pull_request_paginator(
    client: Client,
) -> GetCommentsForPullRequestPaginator:
    """
    Equivalent of `client.get_paginator('get_comments_for_pull_request')`, returns a correct type.
    """
    return client.get_paginator("get_comments_for_pull_request")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_differences_paginator(client: Client) -> GetDifferencesPaginator:
    """
    Equivalent of `client.get_paginator('get_differences')`, returns a correct type.
    """
    return client.get_paginator("get_differences")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_branches_paginator(client: Client) -> ListBranchesPaginator:
    """
    Equivalent of `client.get_paginator('list_branches')`, returns a correct type.
    """
    return client.get_paginator("list_branches")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_pull_requests_paginator(client: Client) -> ListPullRequestsPaginator:
    """
    Equivalent of `client.get_paginator('list_pull_requests')`, returns a correct type.
    """
    return client.get_paginator("list_pull_requests")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_repositories_paginator(client: Client) -> ListRepositoriesPaginator:
    """
    Equivalent of `client.get_paginator('list_repositories')`, returns a correct type.
    """
    return client.get_paginator("list_repositories")
