# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.neptune.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Neptune](index.md#neptune) / Client
    - [Client](#client)
        - [Client().add_role_to_db_cluster](#clientadd_role_to_db_cluster)
        - [Client().add_source_identifier_to_subscription](#clientadd_source_identifier_to_subscription)
        - [Client().add_tags_to_resource](#clientadd_tags_to_resource)
        - [Client().apply_pending_maintenance_action](#clientapply_pending_maintenance_action)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().copy_db_cluster_parameter_group](#clientcopy_db_cluster_parameter_group)
        - [Client().copy_db_cluster_snapshot](#clientcopy_db_cluster_snapshot)
        - [Client().copy_db_parameter_group](#clientcopy_db_parameter_group)
        - [Client().create_db_cluster](#clientcreate_db_cluster)
        - [Client().create_db_cluster_parameter_group](#clientcreate_db_cluster_parameter_group)
        - [Client().create_db_cluster_snapshot](#clientcreate_db_cluster_snapshot)
        - [Client().create_db_instance](#clientcreate_db_instance)
        - [Client().create_db_parameter_group](#clientcreate_db_parameter_group)
        - [Client().create_db_subnet_group](#clientcreate_db_subnet_group)
        - [Client().create_event_subscription](#clientcreate_event_subscription)
        - [Client().delete_db_cluster](#clientdelete_db_cluster)
        - [Client().delete_db_cluster_parameter_group](#clientdelete_db_cluster_parameter_group)
        - [Client().delete_db_cluster_snapshot](#clientdelete_db_cluster_snapshot)
        - [Client().delete_db_instance](#clientdelete_db_instance)
        - [Client().delete_db_parameter_group](#clientdelete_db_parameter_group)
        - [Client().delete_db_subnet_group](#clientdelete_db_subnet_group)
        - [Client().delete_event_subscription](#clientdelete_event_subscription)
        - [Client().describe_db_cluster_parameter_groups](#clientdescribe_db_cluster_parameter_groups)
        - [Client().describe_db_cluster_parameters](#clientdescribe_db_cluster_parameters)
        - [Client().describe_db_cluster_snapshot_attributes](#clientdescribe_db_cluster_snapshot_attributes)
        - [Client().describe_db_cluster_snapshots](#clientdescribe_db_cluster_snapshots)
        - [Client().describe_db_clusters](#clientdescribe_db_clusters)
        - [Client().describe_db_engine_versions](#clientdescribe_db_engine_versions)
        - [Client().describe_db_instances](#clientdescribe_db_instances)
        - [Client().describe_db_parameter_groups](#clientdescribe_db_parameter_groups)
        - [Client().describe_db_parameters](#clientdescribe_db_parameters)
        - [Client().describe_db_subnet_groups](#clientdescribe_db_subnet_groups)
        - [Client().describe_engine_default_cluster_parameters](#clientdescribe_engine_default_cluster_parameters)
        - [Client().describe_engine_default_parameters](#clientdescribe_engine_default_parameters)
        - [Client().describe_event_categories](#clientdescribe_event_categories)
        - [Client().describe_event_subscriptions](#clientdescribe_event_subscriptions)
        - [Client().describe_events](#clientdescribe_events)
        - [Client().describe_orderable_db_instance_options](#clientdescribe_orderable_db_instance_options)
        - [Client().describe_pending_maintenance_actions](#clientdescribe_pending_maintenance_actions)
        - [Client().describe_valid_db_instance_modifications](#clientdescribe_valid_db_instance_modifications)
        - [Client().failover_db_cluster](#clientfailover_db_cluster)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().modify_db_cluster](#clientmodify_db_cluster)
        - [Client().modify_db_cluster_parameter_group](#clientmodify_db_cluster_parameter_group)
        - [Client().modify_db_cluster_snapshot_attribute](#clientmodify_db_cluster_snapshot_attribute)
        - [Client().modify_db_instance](#clientmodify_db_instance)
        - [Client().modify_db_parameter_group](#clientmodify_db_parameter_group)
        - [Client().modify_db_subnet_group](#clientmodify_db_subnet_group)
        - [Client().modify_event_subscription](#clientmodify_event_subscription)
        - [Client().promote_read_replica_db_cluster](#clientpromote_read_replica_db_cluster)
        - [Client().reboot_db_instance](#clientreboot_db_instance)
        - [Client().remove_role_from_db_cluster](#clientremove_role_from_db_cluster)
        - [Client().remove_source_identifier_from_subscription](#clientremove_source_identifier_from_subscription)
        - [Client().remove_tags_from_resource](#clientremove_tags_from_resource)
        - [Client().reset_db_cluster_parameter_group](#clientreset_db_cluster_parameter_group)
        - [Client().reset_db_parameter_group](#clientreset_db_parameter_group)
        - [Client().restore_db_cluster_from_snapshot](#clientrestore_db_cluster_from_snapshot)
        - [Client().restore_db_cluster_to_point_in_time](#clientrestore_db_cluster_to_point_in_time)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_role_to_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L16)

```python
def add_role_to_db_cluster(DBClusterIdentifier: str, RoleArn: str) -> None:
```

### Client().add_source_identifier_to_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L20)

```python
def add_source_identifier_to_subscription(
    SubscriptionName: str,
    SourceIdentifier: str,
) -> Dict[str, Any]:
```

### Client().add_tags_to_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L26)

```python
def add_tags_to_resource(ResourceName: str, Tags: List[Any]) -> None:
```

### Client().apply_pending_maintenance_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L30)

```python
def apply_pending_maintenance_action(
    ResourceIdentifier: str,
    ApplyAction: str,
    OptInType: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L36)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().copy_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L40)

```python
def copy_db_cluster_parameter_group(
    SourceDBClusterParameterGroupIdentifier: str,
    TargetDBClusterParameterGroupIdentifier: str,
    TargetDBClusterParameterGroupDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().copy_db_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L50)

```python
def copy_db_cluster_snapshot(
    SourceDBClusterSnapshotIdentifier: str,
    TargetDBClusterSnapshotIdentifier: str,
    KmsKeyId: str = None,
    PreSignedUrl: str = None,
    CopyTags: bool = None,
    Tags: List[Any] = None,
    SourceRegion: str = None,
) -> Dict[str, Any]:
```

### Client().copy_db_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L63)

```python
def copy_db_parameter_group(
    SourceDBParameterGroupIdentifier: str,
    TargetDBParameterGroupIdentifier: str,
    TargetDBParameterGroupDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L73)

```python
def create_db_cluster(
    DBClusterIdentifier: str,
    Engine: str,
    AvailabilityZones: List[Any] = None,
    BackupRetentionPeriod: int = None,
    CharacterSetName: str = None,
    DatabaseName: str = None,
    DBClusterParameterGroupName: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    DBSubnetGroupName: str = None,
    EngineVersion: str = None,
    Port: int = None,
    MasterUsername: str = None,
    MasterUserPassword: str = None,
    OptionGroupName: str = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    ReplicationSourceIdentifier: str = None,
    Tags: List[Any] = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    PreSignedUrl: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    SourceRegion: str = None,
) -> Dict[str, Any]:
```

### Client().create_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L103)

```python
def create_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
    DBParameterGroupFamily: str,
    Description: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L113)

```python
def create_db_cluster_snapshot(
    DBClusterSnapshotIdentifier: str,
    DBClusterIdentifier: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L122)

```python
def create_db_instance(
    DBInstanceIdentifier: str,
    DBInstanceClass: str,
    Engine: str,
    DBName: str = None,
    AllocatedStorage: int = None,
    MasterUsername: str = None,
    MasterUserPassword: str = None,
    DBSecurityGroups: List[Any] = None,
    VpcSecurityGroupIds: List[Any] = None,
    AvailabilityZone: str = None,
    DBSubnetGroupName: str = None,
    PreferredMaintenanceWindow: str = None,
    DBParameterGroupName: str = None,
    BackupRetentionPeriod: int = None,
    PreferredBackupWindow: str = None,
    Port: int = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    CharacterSetName: str = None,
    PubliclyAccessible: bool = None,
    Tags: List[Any] = None,
    DBClusterIdentifier: str = None,
    StorageType: str = None,
    TdeCredentialArn: str = None,
    TdeCredentialPassword: str = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    Domain: str = None,
    CopyTagsToSnapshot: bool = None,
    MonitoringInterval: int = None,
    MonitoringRoleArn: str = None,
    DomainIAMRoleName: str = None,
    PromotionTier: int = None,
    Timezone: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnablePerformanceInsights: bool = None,
    PerformanceInsightsKMSKeyId: str = None,
    EnableCloudwatchLogsExports: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L170)

```python
def create_db_parameter_group(
    DBParameterGroupName: str,
    DBParameterGroupFamily: str,
    Description: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L180)

```python
def create_db_subnet_group(
    DBSubnetGroupName: str,
    DBSubnetGroupDescription: str,
    SubnetIds: List[Any],
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L190)

```python
def create_event_subscription(
    SubscriptionName: str,
    SnsTopicArn: str,
    SourceType: str = None,
    EventCategories: List[Any] = None,
    SourceIds: List[Any] = None,
    Enabled: bool = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L203)

```python
def delete_db_cluster(
    DBClusterIdentifier: str,
    SkipFinalSnapshot: bool = None,
    FinalDBSnapshotIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().delete_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L212)

```python
def delete_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
) -> None:
```

### Client().delete_db_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L218)

```python
def delete_db_cluster_snapshot(
    DBClusterSnapshotIdentifier: str,
) -> Dict[str, Any]:
```

### Client().delete_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L224)

```python
def delete_db_instance(
    DBInstanceIdentifier: str,
    SkipFinalSnapshot: bool = None,
    FinalDBSnapshotIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().delete_db_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L233)

```python
def delete_db_parameter_group(DBParameterGroupName: str) -> None:
```

### Client().delete_db_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L237)

```python
def delete_db_subnet_group(DBSubnetGroupName: str) -> None:
```

### Client().delete_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L241)

```python
def delete_event_subscription(SubscriptionName: str) -> Dict[str, Any]:
```

### Client().describe_db_cluster_parameter_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L245)

```python
def describe_db_cluster_parameter_groups(
    DBClusterParameterGroupName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L255)

```python
def describe_db_cluster_parameters(
    DBClusterParameterGroupName: str,
    Source: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_snapshot_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L266)

```python
def describe_db_cluster_snapshot_attributes(
    DBClusterSnapshotIdentifier: str,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L272)

```python
def describe_db_cluster_snapshots(
    DBClusterIdentifier: str = None,
    DBClusterSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_db_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L286)

```python
def describe_db_clusters(
    DBClusterIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_engine_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L296)

```python
def describe_db_engine_versions(
    Engine: str = None,
    EngineVersion: str = None,
    DBParameterGroupFamily: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    DefaultOnly: bool = None,
    ListSupportedCharacterSets: bool = None,
    ListSupportedTimezones: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_db_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L311)

```python
def describe_db_instances(
    DBInstanceIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_parameter_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L321)

```python
def describe_db_parameter_groups(
    DBParameterGroupName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L331)

```python
def describe_db_parameters(
    DBParameterGroupName: str,
    Source: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_subnet_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L342)

```python
def describe_db_subnet_groups(
    DBSubnetGroupName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_engine_default_cluster_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L352)

```python
def describe_engine_default_cluster_parameters(
    DBParameterGroupFamily: str,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_engine_default_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L362)

```python
def describe_engine_default_parameters(
    DBParameterGroupFamily: str,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_event_categories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L372)

```python
def describe_event_categories(
    SourceType: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_event_subscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L378)

```python
def describe_event_subscriptions(
    SubscriptionName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L388)

```python
def describe_events(
    SourceIdentifier: str = None,
    SourceType: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    EventCategories: List[Any] = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_orderable_db_instance_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L403)

```python
def describe_orderable_db_instance_options(
    Engine: str,
    EngineVersion: str = None,
    DBInstanceClass: str = None,
    LicenseModel: str = None,
    Vpc: bool = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_pending_maintenance_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L417)

```python
def describe_pending_maintenance_actions(
    ResourceIdentifier: str = None,
    Filters: List[Any] = None,
    Marker: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_valid_db_instance_modifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L427)

```python
def describe_valid_db_instance_modifications(
    DBInstanceIdentifier: str,
) -> Dict[str, Any]:
```

### Client().failover_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L433)

```python
def failover_db_cluster(
    DBClusterIdentifier: str = None,
    TargetDBInstanceIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L439)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L449)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L453)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L457)

```python
def list_tags_for_resource(
    ResourceName: str,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L463)

```python
def modify_db_cluster(
    DBClusterIdentifier: str,
    NewDBClusterIdentifier: str = None,
    ApplyImmediately: bool = None,
    BackupRetentionPeriod: int = None,
    DBClusterParameterGroupName: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    Port: int = None,
    MasterUserPassword: str = None,
    OptionGroupName: str = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    CloudwatchLogsExportConfiguration: Dict[str, Any] = None,
    EngineVersion: str = None,
) -> Dict[str, Any]:
```

### Client().modify_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L483)

```python
def modify_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
    Parameters: List[Any],
) -> Dict[str, Any]:
```

### Client().modify_db_cluster_snapshot_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L489)

```python
def modify_db_cluster_snapshot_attribute(
    DBClusterSnapshotIdentifier: str,
    AttributeName: str,
    ValuesToAdd: List[Any] = None,
    ValuesToRemove: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L499)

```python
def modify_db_instance(
    DBInstanceIdentifier: str,
    AllocatedStorage: int = None,
    DBInstanceClass: str = None,
    DBSubnetGroupName: str = None,
    DBSecurityGroups: List[Any] = None,
    VpcSecurityGroupIds: List[Any] = None,
    ApplyImmediately: bool = None,
    MasterUserPassword: str = None,
    DBParameterGroupName: str = None,
    BackupRetentionPeriod: int = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AllowMajorVersionUpgrade: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    NewDBInstanceIdentifier: str = None,
    StorageType: str = None,
    TdeCredentialArn: str = None,
    TdeCredentialPassword: str = None,
    CACertificateIdentifier: str = None,
    Domain: str = None,
    CopyTagsToSnapshot: bool = None,
    MonitoringInterval: int = None,
    DBPortNumber: int = None,
    PubliclyAccessible: bool = None,
    MonitoringRoleArn: str = None,
    DomainIAMRoleName: str = None,
    PromotionTier: int = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnablePerformanceInsights: bool = None,
    PerformanceInsightsKMSKeyId: str = None,
    CloudwatchLogsExportConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_db_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L541)

```python
def modify_db_parameter_group(
    DBParameterGroupName: str,
    Parameters: List[Any],
) -> Dict[str, Any]:
```

### Client().modify_db_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L547)

```python
def modify_db_subnet_group(
    DBSubnetGroupName: str,
    SubnetIds: List[Any],
    DBSubnetGroupDescription: str = None,
) -> Dict[str, Any]:
```

### Client().modify_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L556)

```python
def modify_event_subscription(
    SubscriptionName: str,
    SnsTopicArn: str = None,
    SourceType: str = None,
    EventCategories: List[Any] = None,
    Enabled: bool = None,
) -> Dict[str, Any]:
```

### Client().promote_read_replica_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L567)

```python
def promote_read_replica_db_cluster(
    DBClusterIdentifier: str,
) -> Dict[str, Any]:
```

### Client().reboot_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L573)

```python
def reboot_db_instance(
    DBInstanceIdentifier: str,
    ForceFailover: bool = None,
) -> Dict[str, Any]:
```

### Client().remove_role_from_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L579)

```python
def remove_role_from_db_cluster(
    DBClusterIdentifier: str,
    RoleArn: str,
) -> None:
```

### Client().remove_source_identifier_from_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L585)

```python
def remove_source_identifier_from_subscription(
    SubscriptionName: str,
    SourceIdentifier: str,
) -> Dict[str, Any]:
```

### Client().remove_tags_from_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L591)

```python
def remove_tags_from_resource(ResourceName: str, TagKeys: List[Any]) -> None:
```

### Client().reset_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L595)

```python
def reset_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().reset_db_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L604)

```python
def reset_db_parameter_group(
    DBParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().restore_db_cluster_from_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L613)

```python
def restore_db_cluster_from_snapshot(
    DBClusterIdentifier: str,
    SnapshotIdentifier: str,
    Engine: str,
    AvailabilityZones: List[Any] = None,
    EngineVersion: str = None,
    Port: int = None,
    DBSubnetGroupName: str = None,
    DatabaseName: str = None,
    OptionGroupName: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    Tags: List[Any] = None,
    KmsKeyId: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    DBClusterParameterGroupName: str = None,
) -> Dict[str, Any]:
```

### Client().restore_db_cluster_to_point_in_time

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/neptune/client.py#L634)

```python
def restore_db_cluster_to_point_in_time(
    DBClusterIdentifier: str,
    SourceDBClusterIdentifier: str,
    RestoreType: str = None,
    RestoreToTime: datetime = None,
    UseLatestRestorableTime: bool = None,
    Port: int = None,
    DBSubnetGroupName: str = None,
    OptionGroupName: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    Tags: List[Any] = None,
    KmsKeyId: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    DBClusterParameterGroupName: str = None,
) -> Dict[str, Any]:
```
