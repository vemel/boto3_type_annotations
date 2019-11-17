"Helper functions for gamelift service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_gamelift.client import Client
from mypy_boto3_gamelift.paginator import (
    DescribeFleetAttributesPaginator,
    DescribeFleetCapacityPaginator,
    DescribeFleetEventsPaginator,
    DescribeFleetUtilizationPaginator,
    DescribeGameSessionDetailsPaginator,
    DescribeGameSessionQueuesPaginator,
    DescribeGameSessionsPaginator,
    DescribeInstancesPaginator,
    DescribeMatchmakingConfigurationsPaginator,
    DescribeMatchmakingRuleSetsPaginator,
    DescribePlayerSessionsPaginator,
    DescribeScalingPoliciesPaginator,
    ListAliasesPaginator,
    ListBuildsPaginator,
    ListFleetsPaginator,
    SearchGameSessionsPaginator,
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
    Equivalent of `boto3.client('gamelift')`, returns a correct type.
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
        return session.client("gamelift", **kwargs)
    return boto3.client("gamelift", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_fleet_attributes_paginator(
    client: Client,
) -> DescribeFleetAttributesPaginator:
    """
    Equivalent of `client.get_paginator('describe_fleet_attributes')`, returns a correct type.
    """
    return client.get_paginator("describe_fleet_attributes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_fleet_capacity_paginator(
    client: Client,
) -> DescribeFleetCapacityPaginator:
    """
    Equivalent of `client.get_paginator('describe_fleet_capacity')`, returns a correct type.
    """
    return client.get_paginator("describe_fleet_capacity")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_fleet_events_paginator(client: Client) -> DescribeFleetEventsPaginator:
    """
    Equivalent of `client.get_paginator('describe_fleet_events')`, returns a correct type.
    """
    return client.get_paginator("describe_fleet_events")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_fleet_utilization_paginator(
    client: Client,
) -> DescribeFleetUtilizationPaginator:
    """
    Equivalent of `client.get_paginator('describe_fleet_utilization')`, returns a correct type.
    """
    return client.get_paginator("describe_fleet_utilization")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_game_session_details_paginator(
    client: Client,
) -> DescribeGameSessionDetailsPaginator:
    """
    Equivalent of `client.get_paginator('describe_game_session_details')`, returns a correct type.
    """
    return client.get_paginator("describe_game_session_details")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_game_session_queues_paginator(
    client: Client,
) -> DescribeGameSessionQueuesPaginator:
    """
    Equivalent of `client.get_paginator('describe_game_session_queues')`, returns a correct type.
    """
    return client.get_paginator("describe_game_session_queues")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_game_sessions_paginator(
    client: Client,
) -> DescribeGameSessionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_game_sessions')`, returns a correct type.
    """
    return client.get_paginator("describe_game_sessions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_instances_paginator(client: Client) -> DescribeInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_matchmaking_configurations_paginator(
    client: Client,
) -> DescribeMatchmakingConfigurationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_matchmaking_configurations')`, returns a correct type.
    """
    return client.get_paginator("describe_matchmaking_configurations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_matchmaking_rule_sets_paginator(
    client: Client,
) -> DescribeMatchmakingRuleSetsPaginator:
    """
    Equivalent of `client.get_paginator('describe_matchmaking_rule_sets')`, returns a correct type.
    """
    return client.get_paginator("describe_matchmaking_rule_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_player_sessions_paginator(
    client: Client,
) -> DescribePlayerSessionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_player_sessions')`, returns a correct type.
    """
    return client.get_paginator("describe_player_sessions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_scaling_policies_paginator(
    client: Client,
) -> DescribeScalingPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('describe_scaling_policies')`, returns a correct type.
    """
    return client.get_paginator("describe_scaling_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_aliases_paginator(client: Client) -> ListAliasesPaginator:
    """
    Equivalent of `client.get_paginator('list_aliases')`, returns a correct type.
    """
    return client.get_paginator("list_aliases")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_builds_paginator(client: Client) -> ListBuildsPaginator:
    """
    Equivalent of `client.get_paginator('list_builds')`, returns a correct type.
    """
    return client.get_paginator("list_builds")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_fleets_paginator(client: Client) -> ListFleetsPaginator:
    """
    Equivalent of `client.get_paginator('list_fleets')`, returns a correct type.
    """
    return client.get_paginator("list_fleets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_game_sessions_paginator(client: Client) -> SearchGameSessionsPaginator:
    """
    Equivalent of `client.get_paginator('search_game_sessions')`, returns a correct type.
    """
    return client.get_paginator("search_game_sessions")
