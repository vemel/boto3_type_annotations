from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_match(
        self,
        TicketId: str,
        PlayerIds: List,
        AcceptanceType: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_alias(
        self,
        Name: str,
        RoutingStrategy: Dict,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_build(
        self,
        Name: Optional[str] = None,
        Version: Optional[str] = None,
        StorageLocation: Optional[Dict] = None,
        OperatingSystem: Optional[str] = None,
    ) -> Dict:
        pass


    def create_fleet(
        self,
        Name: str,
        EC2InstanceType: str,
        Description: Optional[str] = None,
        BuildId: Optional[str] = None,
        ScriptId: Optional[str] = None,
        ServerLaunchPath: Optional[str] = None,
        ServerLaunchParameters: Optional[str] = None,
        LogPaths: Optional[List] = None,
        EC2InboundPermissions: Optional[List] = None,
        NewGameSessionProtectionPolicy: Optional[str] = None,
        RuntimeConfiguration: Optional[Dict] = None,
        ResourceCreationLimitPolicy: Optional[Dict] = None,
        MetricGroups: Optional[List] = None,
        PeerVpcAwsAccountId: Optional[str] = None,
        PeerVpcId: Optional[str] = None,
        FleetType: Optional[str] = None,
        InstanceRoleArn: Optional[str] = None,
        CertificateConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_game_session(
        self,
        MaximumPlayerSessionCount: int,
        FleetId: Optional[str] = None,
        AliasId: Optional[str] = None,
        Name: Optional[str] = None,
        GameProperties: Optional[List] = None,
        CreatorId: Optional[str] = None,
        GameSessionId: Optional[str] = None,
        IdempotencyToken: Optional[str] = None,
        GameSessionData: Optional[str] = None,
    ) -> Dict:
        pass


    def create_game_session_queue(
        self,
        Name: str,
        TimeoutInSeconds: Optional[int] = None,
        PlayerLatencyPolicies: Optional[List] = None,
        Destinations: Optional[List] = None,
    ) -> Dict:
        pass


    def create_matchmaking_configuration(
        self,
        Name: str,
        GameSessionQueueArns: List,
        RequestTimeoutSeconds: int,
        AcceptanceRequired: bool,
        RuleSetName: str,
        Description: Optional[str] = None,
        AcceptanceTimeoutSeconds: Optional[int] = None,
        NotificationTarget: Optional[str] = None,
        AdditionalPlayerCount: Optional[int] = None,
        CustomEventData: Optional[str] = None,
        GameProperties: Optional[List] = None,
        GameSessionData: Optional[str] = None,
        BackfillMode: Optional[str] = None,
    ) -> Dict:
        pass


    def create_matchmaking_rule_set(
        self,
        Name: str,
        RuleSetBody: str,
    ) -> Dict:
        pass


    def create_player_session(
        self,
        GameSessionId: str,
        PlayerId: str,
        PlayerData: Optional[str] = None,
    ) -> Dict:
        pass


    def create_player_sessions(
        self,
        GameSessionId: str,
        PlayerIds: List,
        PlayerDataMap: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_script(
        self,
        Name: Optional[str] = None,
        Version: Optional[str] = None,
        StorageLocation: Optional[Dict] = None,
        ZipFile: Optional[bytes] = None,
    ) -> Dict:
        pass


    def create_vpc_peering_authorization(
        self,
        GameLiftAwsAccountId: str,
        PeerVpcId: str,
    ) -> Dict:
        pass


    def create_vpc_peering_connection(
        self,
        FleetId: str,
        PeerVpcAwsAccountId: str,
        PeerVpcId: str,
    ) -> Dict:
        pass


    def delete_alias(
        self,
        AliasId: str,
    ):
        pass


    def delete_build(
        self,
        BuildId: str,
    ):
        pass


    def delete_fleet(
        self,
        FleetId: str,
    ):
        pass


    def delete_game_session_queue(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_matchmaking_configuration(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_matchmaking_rule_set(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_scaling_policy(
        self,
        Name: str,
        FleetId: str,
    ):
        pass


    def delete_script(
        self,
        ScriptId: str,
    ):
        pass


    def delete_vpc_peering_authorization(
        self,
        GameLiftAwsAccountId: str,
        PeerVpcId: str,
    ) -> Dict:
        pass


    def delete_vpc_peering_connection(
        self,
        FleetId: str,
        VpcPeeringConnectionId: str,
    ) -> Dict:
        pass


    def describe_alias(
        self,
        AliasId: str,
    ) -> Dict:
        pass


    def describe_build(
        self,
        BuildId: str,
    ) -> Dict:
        pass


    def describe_ec2_instance_limits(
        self,
        EC2InstanceType: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_fleet_attributes(
        self,
        FleetIds: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_fleet_capacity(
        self,
        FleetIds: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_fleet_events(
        self,
        FleetId: str,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_fleet_port_settings(
        self,
        FleetId: str,
    ) -> Dict:
        pass


    def describe_fleet_utilization(
        self,
        FleetIds: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_game_session_details(
        self,
        FleetId: Optional[str] = None,
        GameSessionId: Optional[str] = None,
        AliasId: Optional[str] = None,
        StatusFilter: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_game_session_placement(
        self,
        PlacementId: str,
    ) -> Dict:
        pass


    def describe_game_session_queues(
        self,
        Names: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_game_sessions(
        self,
        FleetId: Optional[str] = None,
        GameSessionId: Optional[str] = None,
        AliasId: Optional[str] = None,
        StatusFilter: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_instances(
        self,
        FleetId: str,
        InstanceId: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_matchmaking(
        self,
        TicketIds: List,
    ) -> Dict:
        pass


    def describe_matchmaking_configurations(
        self,
        Names: Optional[List] = None,
        RuleSetName: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_matchmaking_rule_sets(
        self,
        Names: Optional[List] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_player_sessions(
        self,
        GameSessionId: Optional[str] = None,
        PlayerId: Optional[str] = None,
        PlayerSessionId: Optional[str] = None,
        PlayerSessionStatusFilter: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_runtime_configuration(
        self,
        FleetId: str,
    ) -> Dict:
        pass


    def describe_scaling_policies(
        self,
        FleetId: str,
        StatusFilter: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_script(
        self,
        ScriptId: str,
    ) -> Dict:
        pass


    def describe_vpc_peering_authorizations(
        self,
    ) -> Dict:
        pass


    def describe_vpc_peering_connections(
        self,
        FleetId: Optional[str] = None,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_game_session_log_url(
        self,
        GameSessionId: str,
    ) -> Dict:
        pass


    def get_instance_access(
        self,
        FleetId: str,
        InstanceId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_aliases(
        self,
        RoutingStrategyType: Optional[str] = None,
        Name: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_builds(
        self,
        Status: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_fleets(
        self,
        BuildId: Optional[str] = None,
        ScriptId: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_scripts(
        self,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_scaling_policy(
        self,
        Name: str,
        FleetId: str,
        MetricName: str,
        ScalingAdjustment: Optional[int] = None,
        ScalingAdjustmentType: Optional[str] = None,
        Threshold: Optional[float] = None,
        ComparisonOperator: Optional[str] = None,
        EvaluationPeriods: Optional[int] = None,
        PolicyType: Optional[str] = None,
        TargetConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def request_upload_credentials(
        self,
        BuildId: str,
    ) -> Dict:
        pass


    def resolve_alias(
        self,
        AliasId: str,
    ) -> Dict:
        pass


    def search_game_sessions(
        self,
        FleetId: Optional[str] = None,
        AliasId: Optional[str] = None,
        FilterExpression: Optional[str] = None,
        SortExpression: Optional[str] = None,
        Limit: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def start_fleet_actions(
        self,
        FleetId: str,
        Actions: List,
    ) -> Dict:
        pass


    def start_game_session_placement(
        self,
        PlacementId: str,
        GameSessionQueueName: str,
        MaximumPlayerSessionCount: int,
        GameProperties: Optional[List] = None,
        GameSessionName: Optional[str] = None,
        PlayerLatencies: Optional[List] = None,
        DesiredPlayerSessions: Optional[List] = None,
        GameSessionData: Optional[str] = None,
    ) -> Dict:
        pass


    def start_match_backfill(
        self,
        ConfigurationName: str,
        GameSessionArn: str,
        Players: List,
        TicketId: Optional[str] = None,
    ) -> Dict:
        pass


    def start_matchmaking(
        self,
        ConfigurationName: str,
        Players: List,
        TicketId: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_fleet_actions(
        self,
        FleetId: str,
        Actions: List,
    ) -> Dict:
        pass


    def stop_game_session_placement(
        self,
        PlacementId: str,
    ) -> Dict:
        pass


    def stop_matchmaking(
        self,
        TicketId: str,
    ) -> Dict:
        pass


    def update_alias(
        self,
        AliasId: str,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        RoutingStrategy: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_build(
        self,
        BuildId: str,
        Name: Optional[str] = None,
        Version: Optional[str] = None,
    ) -> Dict:
        pass


    def update_fleet_attributes(
        self,
        FleetId: str,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        NewGameSessionProtectionPolicy: Optional[str] = None,
        ResourceCreationLimitPolicy: Optional[Dict] = None,
        MetricGroups: Optional[List] = None,
    ) -> Dict:
        pass


    def update_fleet_capacity(
        self,
        FleetId: str,
        DesiredInstances: Optional[int] = None,
        MinSize: Optional[int] = None,
        MaxSize: Optional[int] = None,
    ) -> Dict:
        pass


    def update_fleet_port_settings(
        self,
        FleetId: str,
        InboundPermissionAuthorizations: Optional[List] = None,
        InboundPermissionRevocations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_game_session(
        self,
        GameSessionId: str,
        MaximumPlayerSessionCount: Optional[int] = None,
        Name: Optional[str] = None,
        PlayerSessionCreationPolicy: Optional[str] = None,
        ProtectionPolicy: Optional[str] = None,
    ) -> Dict:
        pass


    def update_game_session_queue(
        self,
        Name: str,
        TimeoutInSeconds: Optional[int] = None,
        PlayerLatencyPolicies: Optional[List] = None,
        Destinations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_matchmaking_configuration(
        self,
        Name: str,
        Description: Optional[str] = None,
        GameSessionQueueArns: Optional[List] = None,
        RequestTimeoutSeconds: Optional[int] = None,
        AcceptanceTimeoutSeconds: Optional[int] = None,
        AcceptanceRequired: Optional[bool] = None,
        RuleSetName: Optional[str] = None,
        NotificationTarget: Optional[str] = None,
        AdditionalPlayerCount: Optional[int] = None,
        CustomEventData: Optional[str] = None,
        GameProperties: Optional[List] = None,
        GameSessionData: Optional[str] = None,
        BackfillMode: Optional[str] = None,
    ) -> Dict:
        pass


    def update_runtime_configuration(
        self,
        FleetId: str,
        RuntimeConfiguration: Dict,
    ) -> Dict:
        pass


    def update_script(
        self,
        ScriptId: str,
        Name: Optional[str] = None,
        Version: Optional[str] = None,
        StorageLocation: Optional[Dict] = None,
        ZipFile: Optional[bytes] = None,
    ) -> Dict:
        pass


    def validate_matchmaking_rule_set(
        self,
        RuleSetBody: str,
    ) -> Dict:
        pass

