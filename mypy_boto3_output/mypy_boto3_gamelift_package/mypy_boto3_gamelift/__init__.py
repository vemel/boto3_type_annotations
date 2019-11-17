"Main interface for gamelift service"

from mypy_boto3_gamelift.client import Client
from mypy_boto3_gamelift.helpers import (
    boto3_client,
    get_describe_fleet_attributes_paginator,
    get_describe_fleet_capacity_paginator,
    get_describe_fleet_events_paginator,
    get_describe_fleet_utilization_paginator,
    get_describe_game_session_details_paginator,
    get_describe_game_session_queues_paginator,
    get_describe_game_sessions_paginator,
    get_describe_instances_paginator,
    get_describe_matchmaking_configurations_paginator,
    get_describe_matchmaking_rule_sets_paginator,
    get_describe_player_sessions_paginator,
    get_describe_scaling_policies_paginator,
    get_list_aliases_paginator,
    get_list_builds_paginator,
    get_list_fleets_paginator,
    get_search_game_sessions_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_fleet_attributes_paginator",
    "get_describe_fleet_capacity_paginator",
    "get_describe_fleet_events_paginator",
    "get_describe_fleet_utilization_paginator",
    "get_describe_game_session_details_paginator",
    "get_describe_game_session_queues_paginator",
    "get_describe_game_sessions_paginator",
    "get_describe_instances_paginator",
    "get_describe_matchmaking_configurations_paginator",
    "get_describe_matchmaking_rule_sets_paginator",
    "get_describe_player_sessions_paginator",
    "get_describe_scaling_policies_paginator",
    "get_list_aliases_paginator",
    "get_list_builds_paginator",
    "get_list_fleets_paginator",
    "get_search_game_sessions_paginator",
)
