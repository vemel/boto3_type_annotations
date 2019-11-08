# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.gamelift.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Gamelift](index.md#gamelift) / Client
    - [Client](#client)
        - [Client().accept_match](#clientaccept_match)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_alias](#clientcreate_alias)
        - [Client().create_build](#clientcreate_build)
        - [Client().create_fleet](#clientcreate_fleet)
        - [Client().create_game_session](#clientcreate_game_session)
        - [Client().create_game_session_queue](#clientcreate_game_session_queue)
        - [Client().create_matchmaking_configuration](#clientcreate_matchmaking_configuration)
        - [Client().create_matchmaking_rule_set](#clientcreate_matchmaking_rule_set)
        - [Client().create_player_session](#clientcreate_player_session)
        - [Client().create_player_sessions](#clientcreate_player_sessions)
        - [Client().create_script](#clientcreate_script)
        - [Client().create_vpc_peering_authorization](#clientcreate_vpc_peering_authorization)
        - [Client().create_vpc_peering_connection](#clientcreate_vpc_peering_connection)
        - [Client().delete_alias](#clientdelete_alias)
        - [Client().delete_build](#clientdelete_build)
        - [Client().delete_fleet](#clientdelete_fleet)
        - [Client().delete_game_session_queue](#clientdelete_game_session_queue)
        - [Client().delete_matchmaking_configuration](#clientdelete_matchmaking_configuration)
        - [Client().delete_matchmaking_rule_set](#clientdelete_matchmaking_rule_set)
        - [Client().delete_scaling_policy](#clientdelete_scaling_policy)
        - [Client().delete_script](#clientdelete_script)
        - [Client().delete_vpc_peering_authorization](#clientdelete_vpc_peering_authorization)
        - [Client().delete_vpc_peering_connection](#clientdelete_vpc_peering_connection)
        - [Client().describe_alias](#clientdescribe_alias)
        - [Client().describe_build](#clientdescribe_build)
        - [Client().describe_ec2_instance_limits](#clientdescribe_ec2_instance_limits)
        - [Client().describe_fleet_attributes](#clientdescribe_fleet_attributes)
        - [Client().describe_fleet_capacity](#clientdescribe_fleet_capacity)
        - [Client().describe_fleet_events](#clientdescribe_fleet_events)
        - [Client().describe_fleet_port_settings](#clientdescribe_fleet_port_settings)
        - [Client().describe_fleet_utilization](#clientdescribe_fleet_utilization)
        - [Client().describe_game_session_details](#clientdescribe_game_session_details)
        - [Client().describe_game_session_placement](#clientdescribe_game_session_placement)
        - [Client().describe_game_session_queues](#clientdescribe_game_session_queues)
        - [Client().describe_game_sessions](#clientdescribe_game_sessions)
        - [Client().describe_instances](#clientdescribe_instances)
        - [Client().describe_matchmaking](#clientdescribe_matchmaking)
        - [Client().describe_matchmaking_configurations](#clientdescribe_matchmaking_configurations)
        - [Client().describe_matchmaking_rule_sets](#clientdescribe_matchmaking_rule_sets)
        - [Client().describe_player_sessions](#clientdescribe_player_sessions)
        - [Client().describe_runtime_configuration](#clientdescribe_runtime_configuration)
        - [Client().describe_scaling_policies](#clientdescribe_scaling_policies)
        - [Client().describe_script](#clientdescribe_script)
        - [Client().describe_vpc_peering_authorizations](#clientdescribe_vpc_peering_authorizations)
        - [Client().describe_vpc_peering_connections](#clientdescribe_vpc_peering_connections)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_game_session_log_url](#clientget_game_session_log_url)
        - [Client().get_instance_access](#clientget_instance_access)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_aliases](#clientlist_aliases)
        - [Client().list_builds](#clientlist_builds)
        - [Client().list_fleets](#clientlist_fleets)
        - [Client().list_scripts](#clientlist_scripts)
        - [Client().put_scaling_policy](#clientput_scaling_policy)
        - [Client().request_upload_credentials](#clientrequest_upload_credentials)
        - [Client().resolve_alias](#clientresolve_alias)
        - [Client().search_game_sessions](#clientsearch_game_sessions)
        - [Client().start_fleet_actions](#clientstart_fleet_actions)
        - [Client().start_game_session_placement](#clientstart_game_session_placement)
        - [Client().start_match_backfill](#clientstart_match_backfill)
        - [Client().start_matchmaking](#clientstart_matchmaking)
        - [Client().stop_fleet_actions](#clientstop_fleet_actions)
        - [Client().stop_game_session_placement](#clientstop_game_session_placement)
        - [Client().stop_matchmaking](#clientstop_matchmaking)
        - [Client().update_alias](#clientupdate_alias)
        - [Client().update_build](#clientupdate_build)
        - [Client().update_fleet_attributes](#clientupdate_fleet_attributes)
        - [Client().update_fleet_capacity](#clientupdate_fleet_capacity)
        - [Client().update_fleet_port_settings](#clientupdate_fleet_port_settings)
        - [Client().update_game_session](#clientupdate_game_session)
        - [Client().update_game_session_queue](#clientupdate_game_session_queue)
        - [Client().update_matchmaking_configuration](#clientupdate_matchmaking_configuration)
        - [Client().update_runtime_configuration](#clientupdate_runtime_configuration)
        - [Client().update_script](#clientupdate_script)
        - [Client().validate_matchmaking_rule_set](#clientvalidate_matchmaking_rule_set)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L13)

```python
class Client(BaseClient):
```

### Client().accept_match

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L16)

```python
def accept_match(
    TicketId: str,
    PlayerIds: List[Any],
    AcceptanceType: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L22)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L26)

```python
def create_alias(
    Name: str,
    RoutingStrategy: Dict[str, Any],
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().create_build

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L32)

```python
def create_build(
    Name: str = None,
    Version: str = None,
    StorageLocation: Dict[str, Any] = None,
    OperatingSystem: str = None,
) -> Dict[str, Any]:
```

### Client().create_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L42)

```python
def create_fleet(
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
```

### Client().create_game_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L66)

```python
def create_game_session(
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
```

### Client().create_game_session_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L81)

```python
def create_game_session_queue(
    Name: str,
    TimeoutInSeconds: int = None,
    PlayerLatencyPolicies: List[Any] = None,
    Destinations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_matchmaking_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L91)

```python
def create_matchmaking_configuration(
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
```

### Client().create_matchmaking_rule_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L110)

```python
def create_matchmaking_rule_set(
    Name: str,
    RuleSetBody: str,
) -> Dict[str, Any]:
```

### Client().create_player_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L116)

```python
def create_player_session(
    GameSessionId: str,
    PlayerId: str,
    PlayerData: str = None,
) -> Dict[str, Any]:
```

### Client().create_player_sessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L122)

```python
def create_player_sessions(
    GameSessionId: str,
    PlayerIds: List[Any],
    PlayerDataMap: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_script

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L131)

```python
def create_script(
    Name: str = None,
    Version: str = None,
    StorageLocation: Dict[str, Any] = None,
    ZipFile: bytes = None,
) -> Dict[str, Any]:
```

### Client().create_vpc_peering_authorization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L141)

```python
def create_vpc_peering_authorization(
    GameLiftAwsAccountId: str,
    PeerVpcId: str,
) -> Dict[str, Any]:
```

### Client().create_vpc_peering_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L147)

```python
def create_vpc_peering_connection(
    FleetId: str,
    PeerVpcAwsAccountId: str,
    PeerVpcId: str,
) -> Dict[str, Any]:
```

### Client().delete_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L153)

```python
def delete_alias(AliasId: str) -> None:
```

### Client().delete_build

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L157)

```python
def delete_build(BuildId: str) -> None:
```

### Client().delete_fleet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L161)

```python
def delete_fleet(FleetId: str) -> None:
```

### Client().delete_game_session_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L165)

```python
def delete_game_session_queue(Name: str) -> Dict[str, Any]:
```

### Client().delete_matchmaking_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L169)

```python
def delete_matchmaking_configuration(Name: str) -> Dict[str, Any]:
```

### Client().delete_matchmaking_rule_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L173)

```python
def delete_matchmaking_rule_set(Name: str) -> Dict[str, Any]:
```

### Client().delete_scaling_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L177)

```python
def delete_scaling_policy(Name: str, FleetId: str) -> None:
```

### Client().delete_script

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L181)

```python
def delete_script(ScriptId: str) -> None:
```

### Client().delete_vpc_peering_authorization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L185)

```python
def delete_vpc_peering_authorization(
    GameLiftAwsAccountId: str,
    PeerVpcId: str,
) -> Dict[str, Any]:
```

### Client().delete_vpc_peering_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L191)

```python
def delete_vpc_peering_connection(
    FleetId: str,
    VpcPeeringConnectionId: str,
) -> Dict[str, Any]:
```

### Client().describe_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L197)

```python
def describe_alias(AliasId: str) -> Dict[str, Any]:
```

### Client().describe_build

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L201)

```python
def describe_build(BuildId: str) -> Dict[str, Any]:
```

### Client().describe_ec2_instance_limits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L205)

```python
def describe_ec2_instance_limits(
    EC2InstanceType: str = None,
) -> Dict[str, Any]:
```

### Client().describe_fleet_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L211)

```python
def describe_fleet_attributes(
    FleetIds: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_fleet_capacity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L217)

```python
def describe_fleet_capacity(
    FleetIds: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_fleet_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L223)

```python
def describe_fleet_events(
    FleetId: str,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_fleet_port_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L234)

```python
def describe_fleet_port_settings(FleetId: str) -> Dict[str, Any]:
```

### Client().describe_fleet_utilization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L238)

```python
def describe_fleet_utilization(
    FleetIds: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_game_session_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L244)

```python
def describe_game_session_details(
    FleetId: str = None,
    GameSessionId: str = None,
    AliasId: str = None,
    StatusFilter: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_game_session_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L256)

```python
def describe_game_session_placement(PlacementId: str) -> Dict[str, Any]:
```

### Client().describe_game_session_queues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L260)

```python
def describe_game_session_queues(
    Names: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_game_sessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L266)

```python
def describe_game_sessions(
    FleetId: str = None,
    GameSessionId: str = None,
    AliasId: str = None,
    StatusFilter: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L278)

```python
def describe_instances(
    FleetId: str,
    InstanceId: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_matchmaking

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L288)

```python
def describe_matchmaking(TicketIds: List[Any]) -> Dict[str, Any]:
```

### Client().describe_matchmaking_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L292)

```python
def describe_matchmaking_configurations(
    Names: List[Any] = None,
    RuleSetName: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_matchmaking_rule_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L302)

```python
def describe_matchmaking_rule_sets(
    Names: List[Any] = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_player_sessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L308)

```python
def describe_player_sessions(
    GameSessionId: str = None,
    PlayerId: str = None,
    PlayerSessionId: str = None,
    PlayerSessionStatusFilter: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_runtime_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L320)

```python
def describe_runtime_configuration(FleetId: str) -> Dict[str, Any]:
```

### Client().describe_scaling_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L324)

```python
def describe_scaling_policies(
    FleetId: str,
    StatusFilter: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_script

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L334)

```python
def describe_script(ScriptId: str) -> Dict[str, Any]:
```

### Client().describe_vpc_peering_authorizations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L338)

```python
def describe_vpc_peering_authorizations() -> Dict[str, Any]:
```

### Client().describe_vpc_peering_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L342)

```python
def describe_vpc_peering_connections(FleetId: str = None) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L346)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_game_session_log_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L356)

```python
def get_game_session_log_url(GameSessionId: str) -> Dict[str, Any]:
```

### Client().get_instance_access

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L360)

```python
def get_instance_access(FleetId: str, InstanceId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L364)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L368)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_aliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L372)

```python
def list_aliases(
    RoutingStrategyType: str = None,
    Name: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_builds

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L382)

```python
def list_builds(
    Status: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_fleets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L388)

```python
def list_fleets(
    BuildId: str = None,
    ScriptId: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_scripts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L398)

```python
def list_scripts(Limit: int = None, NextToken: str = None) -> Dict[str, Any]:
```

### Client().put_scaling_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L402)

```python
def put_scaling_policy(
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
```

### Client().request_upload_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L418)

```python
def request_upload_credentials(BuildId: str) -> Dict[str, Any]:
```

### Client().resolve_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L422)

```python
def resolve_alias(AliasId: str) -> Dict[str, Any]:
```

### Client().search_game_sessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L426)

```python
def search_game_sessions(
    FleetId: str = None,
    AliasId: str = None,
    FilterExpression: str = None,
    SortExpression: str = None,
    Limit: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().start_fleet_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L438)

```python
def start_fleet_actions(FleetId: str, Actions: List[Any]) -> Dict[str, Any]:
```

### Client().start_game_session_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L442)

```python
def start_game_session_placement(
    PlacementId: str,
    GameSessionQueueName: str,
    MaximumPlayerSessionCount: int,
    GameProperties: List[Any] = None,
    GameSessionName: str = None,
    PlayerLatencies: List[Any] = None,
    DesiredPlayerSessions: List[Any] = None,
    GameSessionData: str = None,
) -> Dict[str, Any]:
```

### Client().start_match_backfill

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L456)

```python
def start_match_backfill(
    ConfigurationName: str,
    GameSessionArn: str,
    Players: List[Any],
    TicketId: str = None,
) -> Dict[str, Any]:
```

### Client().start_matchmaking

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L466)

```python
def start_matchmaking(
    ConfigurationName: str,
    Players: List[Any],
    TicketId: str = None,
) -> Dict[str, Any]:
```

### Client().stop_fleet_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L472)

```python
def stop_fleet_actions(FleetId: str, Actions: List[Any]) -> Dict[str, Any]:
```

### Client().stop_game_session_placement

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L476)

```python
def stop_game_session_placement(PlacementId: str) -> Dict[str, Any]:
```

### Client().stop_matchmaking

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L480)

```python
def stop_matchmaking(TicketId: str) -> Dict[str, Any]:
```

### Client().update_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L484)

```python
def update_alias(
    AliasId: str,
    Name: str = None,
    Description: str = None,
    RoutingStrategy: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_build

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L494)

```python
def update_build(
    BuildId: str,
    Name: str = None,
    Version: str = None,
) -> Dict[str, Any]:
```

### Client().update_fleet_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L500)

```python
def update_fleet_attributes(
    FleetId: str,
    Name: str = None,
    Description: str = None,
    NewGameSessionProtectionPolicy: str = None,
    ResourceCreationLimitPolicy: Dict[str, Any] = None,
    MetricGroups: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_fleet_capacity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L512)

```python
def update_fleet_capacity(
    FleetId: str,
    DesiredInstances: int = None,
    MinSize: int = None,
    MaxSize: int = None,
) -> Dict[str, Any]:
```

### Client().update_fleet_port_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L522)

```python
def update_fleet_port_settings(
    FleetId: str,
    InboundPermissionAuthorizations: List[Any] = None,
    InboundPermissionRevocations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_game_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L531)

```python
def update_game_session(
    GameSessionId: str,
    MaximumPlayerSessionCount: int = None,
    Name: str = None,
    PlayerSessionCreationPolicy: str = None,
    ProtectionPolicy: str = None,
) -> Dict[str, Any]:
```

### Client().update_game_session_queue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L542)

```python
def update_game_session_queue(
    Name: str,
    TimeoutInSeconds: int = None,
    PlayerLatencyPolicies: List[Any] = None,
    Destinations: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_matchmaking_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L552)

```python
def update_matchmaking_configuration(
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
```

### Client().update_runtime_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L571)

```python
def update_runtime_configuration(
    FleetId: str,
    RuntimeConfiguration: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_script

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L577)

```python
def update_script(
    ScriptId: str,
    Name: str = None,
    Version: str = None,
    StorageLocation: Dict[str, Any] = None,
    ZipFile: bytes = None,
) -> Dict[str, Any]:
```

### Client().validate_matchmaking_rule_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/gamelift/client.py#L588)

```python
def validate_matchmaking_rule_set(RuleSetBody: str) -> Dict[str, Any]:
```
