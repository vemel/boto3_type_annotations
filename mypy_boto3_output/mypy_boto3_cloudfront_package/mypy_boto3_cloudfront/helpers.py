"Helper functions for cloudfront service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_cloudfront.client import Client
from mypy_boto3_cloudfront.paginator import (
    ListCloudFrontOriginAccessIdentitiesPaginator,
    ListDistributionsPaginator,
    ListInvalidationsPaginator,
    ListStreamingDistributionsPaginator,
)
from mypy_boto3_cloudfront.waiter import (
    DistributionDeployedWaiter,
    InvalidationCompletedWaiter,
    StreamingDistributionDeployedWaiter,
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
    Equivalent of `boto3.client('cloudfront')`, returns a correct type.
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
        return session.client("cloudfront", **kwargs)
    return boto3.client("cloudfront", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_cloud_front_origin_access_identities_paginator(
    client: Client,
) -> ListCloudFrontOriginAccessIdentitiesPaginator:
    """
    Equivalent of `client.get_paginator('list_cloud_front_origin_access_identities')`, returns a correct type.
    """
    return client.get_paginator("list_cloud_front_origin_access_identities")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_distributions_paginator(client: Client) -> ListDistributionsPaginator:
    """
    Equivalent of `client.get_paginator('list_distributions')`, returns a correct type.
    """
    return client.get_paginator("list_distributions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_invalidations_paginator(client: Client) -> ListInvalidationsPaginator:
    """
    Equivalent of `client.get_paginator('list_invalidations')`, returns a correct type.
    """
    return client.get_paginator("list_invalidations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_streaming_distributions_paginator(
    client: Client,
) -> ListStreamingDistributionsPaginator:
    """
    Equivalent of `client.get_paginator('list_streaming_distributions')`, returns a correct type.
    """
    return client.get_paginator("list_streaming_distributions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_distribution_deployed_waiter(client: Client) -> DistributionDeployedWaiter:
    """
    Equivalent of `client.get_waiter('distribution_deployed')`, returns a correct type.
    """
    return client.get_waiter("distribution_deployed")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_invalidation_completed_waiter(client: Client) -> InvalidationCompletedWaiter:
    """
    Equivalent of `client.get_waiter('invalidation_completed')`, returns a correct type.
    """
    return client.get_waiter("invalidation_completed")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_streaming_distribution_deployed_waiter(
    client: Client,
) -> StreamingDistributionDeployedWaiter:
    """
    Equivalent of `client.get_waiter('streaming_distribution_deployed')`, returns a correct type.
    """
    return client.get_waiter("streaming_distribution_deployed")
