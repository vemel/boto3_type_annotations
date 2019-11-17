"Helper functions for groundstation service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_groundstation.client import Client
from mypy_boto3_groundstation.paginator import (
    ListConfigsPaginator,
    ListContactsPaginator,
    ListDataflowEndpointGroupsPaginator,
    ListGroundStationsPaginator,
    ListMissionProfilesPaginator,
    ListSatellitesPaginator,
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
    Equivalent of `boto3.client('groundstation')`, returns a correct type.
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
        return session.client("groundstation", **kwargs)
    return boto3.client("groundstation", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_configs_paginator(client: Client) -> ListConfigsPaginator:
    """
    Equivalent of `client.get_paginator('list_configs')`, returns a correct type.
    """
    return client.get_paginator("list_configs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_contacts_paginator(client: Client) -> ListContactsPaginator:
    """
    Equivalent of `client.get_paginator('list_contacts')`, returns a correct type.
    """
    return client.get_paginator("list_contacts")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_dataflow_endpoint_groups_paginator(
    client: Client,
) -> ListDataflowEndpointGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_dataflow_endpoint_groups')`, returns a correct type.
    """
    return client.get_paginator("list_dataflow_endpoint_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_ground_stations_paginator(client: Client) -> ListGroundStationsPaginator:
    """
    Equivalent of `client.get_paginator('list_ground_stations')`, returns a correct type.
    """
    return client.get_paginator("list_ground_stations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_mission_profiles_paginator(client: Client) -> ListMissionProfilesPaginator:
    """
    Equivalent of `client.get_paginator('list_mission_profiles')`, returns a correct type.
    """
    return client.get_paginator("list_mission_profiles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_satellites_paginator(client: Client) -> ListSatellitesPaginator:
    """
    Equivalent of `client.get_paginator('list_satellites')`, returns a correct type.
    """
    return client.get_paginator("list_satellites")
