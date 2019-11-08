# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elasticache.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elasticache](index.md#elasticache) / Client
    - [Client](#client)
        - [Client().add_tags_to_resource](#clientadd_tags_to_resource)
        - [Client().authorize_cache_security_group_ingress](#clientauthorize_cache_security_group_ingress)
        - [Client().batch_apply_update_action](#clientbatch_apply_update_action)
        - [Client().batch_stop_update_action](#clientbatch_stop_update_action)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().complete_migration](#clientcomplete_migration)
        - [Client().copy_snapshot](#clientcopy_snapshot)
        - [Client().create_cache_cluster](#clientcreate_cache_cluster)
        - [Client().create_cache_parameter_group](#clientcreate_cache_parameter_group)
        - [Client().create_cache_security_group](#clientcreate_cache_security_group)
        - [Client().create_cache_subnet_group](#clientcreate_cache_subnet_group)
        - [Client().create_replication_group](#clientcreate_replication_group)
        - [Client().create_snapshot](#clientcreate_snapshot)
        - [Client().decrease_replica_count](#clientdecrease_replica_count)
        - [Client().delete_cache_cluster](#clientdelete_cache_cluster)
        - [Client().delete_cache_parameter_group](#clientdelete_cache_parameter_group)
        - [Client().delete_cache_security_group](#clientdelete_cache_security_group)
        - [Client().delete_cache_subnet_group](#clientdelete_cache_subnet_group)
        - [Client().delete_replication_group](#clientdelete_replication_group)
        - [Client().delete_snapshot](#clientdelete_snapshot)
        - [Client().describe_cache_clusters](#clientdescribe_cache_clusters)
        - [Client().describe_cache_engine_versions](#clientdescribe_cache_engine_versions)
        - [Client().describe_cache_parameter_groups](#clientdescribe_cache_parameter_groups)
        - [Client().describe_cache_parameters](#clientdescribe_cache_parameters)
        - [Client().describe_cache_security_groups](#clientdescribe_cache_security_groups)
        - [Client().describe_cache_subnet_groups](#clientdescribe_cache_subnet_groups)
        - [Client().describe_engine_default_parameters](#clientdescribe_engine_default_parameters)
        - [Client().describe_events](#clientdescribe_events)
        - [Client().describe_replication_groups](#clientdescribe_replication_groups)
        - [Client().describe_reserved_cache_nodes](#clientdescribe_reserved_cache_nodes)
        - [Client().describe_reserved_cache_nodes_offerings](#clientdescribe_reserved_cache_nodes_offerings)
        - [Client().describe_service_updates](#clientdescribe_service_updates)
        - [Client().describe_snapshots](#clientdescribe_snapshots)
        - [Client().describe_update_actions](#clientdescribe_update_actions)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().increase_replica_count](#clientincrease_replica_count)
        - [Client().list_allowed_node_type_modifications](#clientlist_allowed_node_type_modifications)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().modify_cache_cluster](#clientmodify_cache_cluster)
        - [Client().modify_cache_parameter_group](#clientmodify_cache_parameter_group)
        - [Client().modify_cache_subnet_group](#clientmodify_cache_subnet_group)
        - [Client().modify_replication_group](#clientmodify_replication_group)
        - [Client().modify_replication_group_shard_configuration](#clientmodify_replication_group_shard_configuration)
        - [Client().purchase_reserved_cache_nodes_offering](#clientpurchase_reserved_cache_nodes_offering)
        - [Client().reboot_cache_cluster](#clientreboot_cache_cluster)
        - [Client().remove_tags_from_resource](#clientremove_tags_from_resource)
        - [Client().reset_cache_parameter_group](#clientreset_cache_parameter_group)
        - [Client().revoke_cache_security_group_ingress](#clientrevoke_cache_security_group_ingress)
        - [Client().start_migration](#clientstart_migration)
        - [Client().test_failover](#clienttest_failover)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_tags_to_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L16)

```python
def add_tags_to_resource(
    ResourceName: str,
    Tags: List[Any],
) -> Dict[str, Any]:
```

### Client().authorize_cache_security_group_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L22)

```python
def authorize_cache_security_group_ingress(
    CacheSecurityGroupName: str,
    EC2SecurityGroupName: str,
    EC2SecurityGroupOwnerId: str,
) -> Dict[str, Any]:
```

### Client().batch_apply_update_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L31)

```python
def batch_apply_update_action(
    ServiceUpdateName: str,
    ReplicationGroupIds: List[Any] = None,
    CacheClusterIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().batch_stop_update_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L40)

```python
def batch_stop_update_action(
    ServiceUpdateName: str,
    ReplicationGroupIds: List[Any] = None,
    CacheClusterIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L49)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().complete_migration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L53)

```python
def complete_migration(
    ReplicationGroupId: str,
    Force: bool = None,
) -> Dict[str, Any]:
```

### Client().copy_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L59)

```python
def copy_snapshot(
    SourceSnapshotName: str,
    TargetSnapshotName: str,
    TargetBucket: str = None,
    KmsKeyId: str = None,
) -> Dict[str, Any]:
```

### Client().create_cache_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L69)

```python
def create_cache_cluster(
    CacheClusterId: str,
    ReplicationGroupId: str = None,
    AZMode: str = None,
    PreferredAvailabilityZone: str = None,
    PreferredAvailabilityZones: List[Any] = None,
    NumCacheNodes: int = None,
    CacheNodeType: str = None,
    Engine: str = None,
    EngineVersion: str = None,
    CacheParameterGroupName: str = None,
    CacheSubnetGroupName: str = None,
    CacheSecurityGroupNames: List[Any] = None,
    SecurityGroupIds: List[Any] = None,
    Tags: List[Any] = None,
    SnapshotArns: List[Any] = None,
    SnapshotName: str = None,
    PreferredMaintenanceWindow: str = None,
    Port: int = None,
    NotificationTopicArn: str = None,
    AutoMinorVersionUpgrade: bool = None,
    SnapshotRetentionLimit: int = None,
    SnapshotWindow: str = None,
    AuthToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_cache_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L98)

```python
def create_cache_parameter_group(
    CacheParameterGroupName: str,
    CacheParameterGroupFamily: str,
    Description: str,
) -> Dict[str, Any]:
```

### Client().create_cache_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L107)

```python
def create_cache_security_group(
    CacheSecurityGroupName: str,
    Description: str,
) -> Dict[str, Any]:
```

### Client().create_cache_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L113)

```python
def create_cache_subnet_group(
    CacheSubnetGroupName: str,
    CacheSubnetGroupDescription: str,
    SubnetIds: List[Any],
) -> Dict[str, Any]:
```

### Client().create_replication_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L122)

```python
def create_replication_group(
    ReplicationGroupId: str,
    ReplicationGroupDescription: str,
    PrimaryClusterId: str = None,
    AutomaticFailoverEnabled: bool = None,
    NumCacheClusters: int = None,
    PreferredCacheClusterAZs: List[Any] = None,
    NumNodeGroups: int = None,
    ReplicasPerNodeGroup: int = None,
    NodeGroupConfiguration: List[Any] = None,
    CacheNodeType: str = None,
    Engine: str = None,
    EngineVersion: str = None,
    CacheParameterGroupName: str = None,
    CacheSubnetGroupName: str = None,
    CacheSecurityGroupNames: List[Any] = None,
    SecurityGroupIds: List[Any] = None,
    Tags: List[Any] = None,
    SnapshotArns: List[Any] = None,
    SnapshotName: str = None,
    PreferredMaintenanceWindow: str = None,
    Port: int = None,
    NotificationTopicArn: str = None,
    AutoMinorVersionUpgrade: bool = None,
    SnapshotRetentionLimit: int = None,
    SnapshotWindow: str = None,
    AuthToken: str = None,
    TransitEncryptionEnabled: bool = None,
    AtRestEncryptionEnabled: bool = None,
    KmsKeyId: str = None,
) -> Dict[str, Any]:
```

### Client().create_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L157)

```python
def create_snapshot(
    SnapshotName: str,
    ReplicationGroupId: str = None,
    CacheClusterId: str = None,
    KmsKeyId: str = None,
) -> Dict[str, Any]:
```

### Client().decrease_replica_count

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L167)

```python
def decrease_replica_count(
    ReplicationGroupId: str,
    ApplyImmediately: bool,
    NewReplicaCount: int = None,
    ReplicaConfiguration: List[Any] = None,
    ReplicasToRemove: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_cache_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L178)

```python
def delete_cache_cluster(
    CacheClusterId: str,
    FinalSnapshotIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().delete_cache_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L184)

```python
def delete_cache_parameter_group(CacheParameterGroupName: str) -> None:
```

### Client().delete_cache_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L188)

```python
def delete_cache_security_group(CacheSecurityGroupName: str) -> None:
```

### Client().delete_cache_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L192)

```python
def delete_cache_subnet_group(CacheSubnetGroupName: str) -> None:
```

### Client().delete_replication_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L196)

```python
def delete_replication_group(
    ReplicationGroupId: str,
    RetainPrimaryCluster: bool = None,
    FinalSnapshotIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().delete_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L205)

```python
def delete_snapshot(SnapshotName: str) -> Dict[str, Any]:
```

### Client().describe_cache_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L209)

```python
def describe_cache_clusters(
    CacheClusterId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    ShowCacheNodeInfo: bool = None,
    ShowCacheClustersNotInReplicationGroups: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_cache_engine_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L220)

```python
def describe_cache_engine_versions(
    Engine: str = None,
    EngineVersion: str = None,
    CacheParameterGroupFamily: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    DefaultOnly: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_cache_parameter_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L232)

```python
def describe_cache_parameter_groups(
    CacheParameterGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_cache_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L241)

```python
def describe_cache_parameters(
    CacheParameterGroupName: str,
    Source: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_cache_security_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L251)

```python
def describe_cache_security_groups(
    CacheSecurityGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_cache_subnet_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L260)

```python
def describe_cache_subnet_groups(
    CacheSubnetGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_engine_default_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L269)

```python
def describe_engine_default_parameters(
    CacheParameterGroupFamily: str,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L275)

```python
def describe_events(
    SourceIdentifier: str = None,
    SourceType: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_replication_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L288)

```python
def describe_replication_groups(
    ReplicationGroupId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_cache_nodes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L294)

```python
def describe_reserved_cache_nodes(
    ReservedCacheNodeId: str = None,
    ReservedCacheNodesOfferingId: str = None,
    CacheNodeType: str = None,
    Duration: str = None,
    ProductDescription: str = None,
    OfferingType: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_cache_nodes_offerings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L308)

```python
def describe_reserved_cache_nodes_offerings(
    ReservedCacheNodesOfferingId: str = None,
    CacheNodeType: str = None,
    Duration: str = None,
    ProductDescription: str = None,
    OfferingType: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_service_updates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L321)

```python
def describe_service_updates(
    ServiceUpdateName: str = None,
    ServiceUpdateStatus: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L331)

```python
def describe_snapshots(
    ReplicationGroupId: str = None,
    CacheClusterId: str = None,
    SnapshotName: str = None,
    SnapshotSource: str = None,
    Marker: str = None,
    MaxRecords: int = None,
    ShowNodeGroupConfig: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_update_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L344)

```python
def describe_update_actions(
    ServiceUpdateName: str = None,
    ReplicationGroupIds: List[Any] = None,
    CacheClusterIds: List[Any] = None,
    Engine: str = None,
    ServiceUpdateStatus: List[Any] = None,
    ServiceUpdateTimeRange: Dict[str, Any] = None,
    UpdateActionStatus: List[Any] = None,
    ShowNodeLevelUpdateStatus: bool = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L360)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L370)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L374)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().increase_replica_count

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L378)

```python
def increase_replica_count(
    ReplicationGroupId: str,
    ApplyImmediately: bool,
    NewReplicaCount: int = None,
    ReplicaConfiguration: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_allowed_node_type_modifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L388)

```python
def list_allowed_node_type_modifications(
    CacheClusterId: str = None,
    ReplicationGroupId: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L394)

```python
def list_tags_for_resource(ResourceName: str) -> Dict[str, Any]:
```

### Client().modify_cache_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L398)

```python
def modify_cache_cluster(
    CacheClusterId: str,
    NumCacheNodes: int = None,
    CacheNodeIdsToRemove: List[Any] = None,
    AZMode: str = None,
    NewAvailabilityZones: List[Any] = None,
    CacheSecurityGroupNames: List[Any] = None,
    SecurityGroupIds: List[Any] = None,
    PreferredMaintenanceWindow: str = None,
    NotificationTopicArn: str = None,
    CacheParameterGroupName: str = None,
    NotificationTopicStatus: str = None,
    ApplyImmediately: bool = None,
    EngineVersion: str = None,
    AutoMinorVersionUpgrade: bool = None,
    SnapshotRetentionLimit: int = None,
    SnapshotWindow: str = None,
    CacheNodeType: str = None,
    AuthToken: str = None,
    AuthTokenUpdateStrategy: str = None,
) -> Dict[str, Any]:
```

### Client().modify_cache_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L423)

```python
def modify_cache_parameter_group(
    CacheParameterGroupName: str,
    ParameterNameValues: List[Any],
) -> Dict[str, Any]:
```

### Client().modify_cache_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L429)

```python
def modify_cache_subnet_group(
    CacheSubnetGroupName: str,
    CacheSubnetGroupDescription: str = None,
    SubnetIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_replication_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L438)

```python
def modify_replication_group(
    ReplicationGroupId: str,
    ReplicationGroupDescription: str = None,
    PrimaryClusterId: str = None,
    SnapshottingClusterId: str = None,
    AutomaticFailoverEnabled: bool = None,
    NodeGroupId: str = None,
    CacheSecurityGroupNames: List[Any] = None,
    SecurityGroupIds: List[Any] = None,
    PreferredMaintenanceWindow: str = None,
    NotificationTopicArn: str = None,
    CacheParameterGroupName: str = None,
    NotificationTopicStatus: str = None,
    ApplyImmediately: bool = None,
    EngineVersion: str = None,
    AutoMinorVersionUpgrade: bool = None,
    SnapshotRetentionLimit: int = None,
    SnapshotWindow: str = None,
    CacheNodeType: str = None,
    AuthToken: str = None,
    AuthTokenUpdateStrategy: str = None,
) -> Dict[str, Any]:
```

### Client().modify_replication_group_shard_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L464)

```python
def modify_replication_group_shard_configuration(
    ReplicationGroupId: str,
    NodeGroupCount: int,
    ApplyImmediately: bool,
    ReshardingConfiguration: List[Any] = None,
    NodeGroupsToRemove: List[Any] = None,
    NodeGroupsToRetain: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().purchase_reserved_cache_nodes_offering

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L476)

```python
def purchase_reserved_cache_nodes_offering(
    ReservedCacheNodesOfferingId: str,
    ReservedCacheNodeId: str = None,
    CacheNodeCount: int = None,
) -> Dict[str, Any]:
```

### Client().reboot_cache_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L485)

```python
def reboot_cache_cluster(
    CacheClusterId: str,
    CacheNodeIdsToReboot: List[Any],
) -> Dict[str, Any]:
```

### Client().remove_tags_from_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L491)

```python
def remove_tags_from_resource(
    ResourceName: str,
    TagKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().reset_cache_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L497)

```python
def reset_cache_parameter_group(
    CacheParameterGroupName: str,
    ResetAllParameters: bool = None,
    ParameterNameValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().revoke_cache_security_group_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L506)

```python
def revoke_cache_security_group_ingress(
    CacheSecurityGroupName: str,
    EC2SecurityGroupName: str,
    EC2SecurityGroupOwnerId: str,
) -> Dict[str, Any]:
```

### Client().start_migration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L515)

```python
def start_migration(
    ReplicationGroupId: str,
    CustomerNodeEndpointList: List[Any],
) -> Dict[str, Any]:
```

### Client().test_failover

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/client.py#L521)

```python
def test_failover(
    ReplicationGroupId: str,
    NodeGroupId: str,
) -> Dict[str, Any]:
```
