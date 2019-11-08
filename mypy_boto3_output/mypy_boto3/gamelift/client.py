from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def accept_match(
        self, TicketId: str, PlayerIds: List[Any], AcceptanceType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_alias(
        self, Name: str, RoutingStrategy: Dict[str, Any], Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_build(
        self,
        Name: str = None,
        Version: str = None,
        StorageLocation: Dict[str, Any] = None,
        OperatingSystem: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_fleet(
        self,
        Name: str,
        EC2InstanceType: str,
        Description: str = None,
        BuildId: str = None,
        ScriptId: str = None,
        ServerLaunchPath: str = None,
        ServerLaunchParameters: str = None,
        LogPaths: List[Any] = None,
        EC2InboundPermissions: List[Any] = None,
        NewGameSessionProtectionPolicy: str = None,
        RuntimeConfiguration: Dict[str, Any] = None,
        ResourceCreationLimitPolicy: Dict[str, Any] = None,
        MetricGroups: List[Any] = None,
        PeerVpcAwsAccountId: str = None,
        PeerVpcId: str = None,
        FleetType: str = None,
        InstanceRoleArn: str = None,
        CertificateConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_game_session(
        self,
        MaximumPlayerSessionCount: int,
        FleetId: str = None,
        AliasId: str = None,
        Name: str = None,
        GameProperties: List[Any] = None,
        CreatorId: str = None,
        GameSessionId: str = None,
        IdempotencyToken: str = None,
        GameSessionData: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_game_session_queue(
        self,
        Name: str,
        TimeoutInSeconds: int = None,
        PlayerLatencyPolicies: List[Any] = None,
        Destinations: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_matchmaking_configuration(
        self,
        Name: str,
        GameSessionQueueArns: List[Any],
        RequestTimeoutSeconds: int,
        AcceptanceRequired: bool,
        RuleSetName: str,
        Description: str = None,
        AcceptanceTimeoutSeconds: int = None,
        NotificationTarget: str = None,
        AdditionalPlayerCount: int = None,
        CustomEventData: str = None,
        GameProperties: List[Any] = None,
        GameSessionData: str = None,
        BackfillMode: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_matchmaking_rule_set(
        self, Name: str, RuleSetBody: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_player_session(
        self, GameSessionId: str, PlayerId: str, PlayerData: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_player_sessions(
        self,
        GameSessionId: str,
        PlayerIds: List[Any],
        PlayerDataMap: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_script(
        self,
        Name: str = None,
        Version: str = None,
        StorageLocation: Dict[str, Any] = None,
        ZipFile: bytes = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_vpc_peering_authorization(
        self, GameLiftAwsAccountId: str, PeerVpcId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_vpc_peering_connection(
        self, FleetId: str, PeerVpcAwsAccountId: str, PeerVpcId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_alias(self, AliasId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_build(self, BuildId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_fleet(self, FleetId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_game_session_queue(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_matchmaking_configuration(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_matchmaking_rule_set(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_scaling_policy(self, Name: str, FleetId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_script(self, ScriptId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_vpc_peering_authorization(
        self, GameLiftAwsAccountId: str, PeerVpcId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_vpc_peering_connection(
        self, FleetId: str, VpcPeeringConnectionId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_alias(self, AliasId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_build(self, BuildId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_ec2_instance_limits(
        self, EC2InstanceType: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_fleet_attributes(
        self, FleetIds: List[Any] = None, Limit: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_fleet_capacity(
        self, FleetIds: List[Any] = None, Limit: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_fleet_events(
        self,
        FleetId: str,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_fleet_port_settings(self, FleetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_fleet_utilization(
        self, FleetIds: List[Any] = None, Limit: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_game_session_details(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        StatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_game_session_placement(self, PlacementId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_game_session_queues(
        self, Names: List[Any] = None, Limit: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_game_sessions(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        StatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_instances(
        self,
        FleetId: str,
        InstanceId: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_matchmaking(self, TicketIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_matchmaking_configurations(
        self,
        Names: List[Any] = None,
        RuleSetName: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_matchmaking_rule_sets(
        self, Names: List[Any] = None, Limit: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_player_sessions(
        self,
        GameSessionId: str = None,
        PlayerId: str = None,
        PlayerSessionId: str = None,
        PlayerSessionStatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_runtime_configuration(self, FleetId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_scaling_policies(
        self,
        FleetId: str,
        StatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_script(self, ScriptId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_vpc_peering_authorizations(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_vpc_peering_connections(self, FleetId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_game_session_log_url(self, GameSessionId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_instance_access(self, FleetId: str, InstanceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_aliases(
        self,
        RoutingStrategyType: str = None,
        Name: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_builds(
        self, Status: str = None, Limit: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_fleets(
        self,
        BuildId: str = None,
        ScriptId: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_scripts(self, Limit: int = None, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_scaling_policy(
        self,
        Name: str,
        FleetId: str,
        MetricName: str,
        ScalingAdjustment: int = None,
        ScalingAdjustmentType: str = None,
        Threshold: float = None,
        ComparisonOperator: str = None,
        EvaluationPeriods: int = None,
        PolicyType: str = None,
        TargetConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def request_upload_credentials(self, BuildId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def resolve_alias(self, AliasId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def search_game_sessions(
        self,
        FleetId: str = None,
        AliasId: str = None,
        FilterExpression: str = None,
        SortExpression: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_fleet_actions(self, FleetId: str, Actions: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_game_session_placement(
        self,
        PlacementId: str,
        GameSessionQueueName: str,
        MaximumPlayerSessionCount: int,
        GameProperties: List[Any] = None,
        GameSessionName: str = None,
        PlayerLatencies: List[Any] = None,
        DesiredPlayerSessions: List[Any] = None,
        GameSessionData: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_match_backfill(
        self,
        ConfigurationName: str,
        GameSessionArn: str,
        Players: List[Any],
        TicketId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_matchmaking(
        self, ConfigurationName: str, Players: List[Any], TicketId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_fleet_actions(self, FleetId: str, Actions: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_game_session_placement(self, PlacementId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_matchmaking(self, TicketId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_alias(
        self,
        AliasId: str,
        Name: str = None,
        Description: str = None,
        RoutingStrategy: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_build(
        self, BuildId: str, Name: str = None, Version: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_fleet_attributes(
        self,
        FleetId: str,
        Name: str = None,
        Description: str = None,
        NewGameSessionProtectionPolicy: str = None,
        ResourceCreationLimitPolicy: Dict[str, Any] = None,
        MetricGroups: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_fleet_capacity(
        self,
        FleetId: str,
        DesiredInstances: int = None,
        MinSize: int = None,
        MaxSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_fleet_port_settings(
        self,
        FleetId: str,
        InboundPermissionAuthorizations: List[Any] = None,
        InboundPermissionRevocations: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_game_session(
        self,
        GameSessionId: str,
        MaximumPlayerSessionCount: int = None,
        Name: str = None,
        PlayerSessionCreationPolicy: str = None,
        ProtectionPolicy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_game_session_queue(
        self,
        Name: str,
        TimeoutInSeconds: int = None,
        PlayerLatencyPolicies: List[Any] = None,
        Destinations: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_matchmaking_configuration(
        self,
        Name: str,
        Description: str = None,
        GameSessionQueueArns: List[Any] = None,
        RequestTimeoutSeconds: int = None,
        AcceptanceTimeoutSeconds: int = None,
        AcceptanceRequired: bool = None,
        RuleSetName: str = None,
        NotificationTarget: str = None,
        AdditionalPlayerCount: int = None,
        CustomEventData: str = None,
        GameProperties: List[Any] = None,
        GameSessionData: str = None,
        BackfillMode: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_runtime_configuration(
        self, FleetId: str, RuntimeConfiguration: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_script(
        self,
        ScriptId: str,
        Name: str = None,
        Version: str = None,
        StorageLocation: Dict[str, Any] = None,
        ZipFile: bytes = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def validate_matchmaking_rule_set(self, RuleSetBody: str) -> Dict[str, Any]:
        pass
