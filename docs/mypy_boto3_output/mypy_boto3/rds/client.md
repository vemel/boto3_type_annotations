# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.rds.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Rds](index.md#rds) / Client
    - [Client](#client)
        - [Client().add_role_to_db_cluster](#clientadd_role_to_db_cluster)
        - [Client().add_role_to_db_instance](#clientadd_role_to_db_instance)
        - [Client().add_source_identifier_to_subscription](#clientadd_source_identifier_to_subscription)
        - [Client().add_tags_to_resource](#clientadd_tags_to_resource)
        - [Client().apply_pending_maintenance_action](#clientapply_pending_maintenance_action)
        - [Client().authorize_db_security_group_ingress](#clientauthorize_db_security_group_ingress)
        - [Client().backtrack_db_cluster](#clientbacktrack_db_cluster)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().copy_db_cluster_parameter_group](#clientcopy_db_cluster_parameter_group)
        - [Client().copy_db_cluster_snapshot](#clientcopy_db_cluster_snapshot)
        - [Client().copy_db_parameter_group](#clientcopy_db_parameter_group)
        - [Client().copy_db_snapshot](#clientcopy_db_snapshot)
        - [Client().copy_option_group](#clientcopy_option_group)
        - [Client().create_custom_availability_zone](#clientcreate_custom_availability_zone)
        - [Client().create_db_cluster](#clientcreate_db_cluster)
        - [Client().create_db_cluster_endpoint](#clientcreate_db_cluster_endpoint)
        - [Client().create_db_cluster_parameter_group](#clientcreate_db_cluster_parameter_group)
        - [Client().create_db_cluster_snapshot](#clientcreate_db_cluster_snapshot)
        - [Client().create_db_instance](#clientcreate_db_instance)
        - [Client().create_db_instance_read_replica](#clientcreate_db_instance_read_replica)
        - [Client().create_db_parameter_group](#clientcreate_db_parameter_group)
        - [Client().create_db_security_group](#clientcreate_db_security_group)
        - [Client().create_db_snapshot](#clientcreate_db_snapshot)
        - [Client().create_db_subnet_group](#clientcreate_db_subnet_group)
        - [Client().create_event_subscription](#clientcreate_event_subscription)
        - [Client().create_global_cluster](#clientcreate_global_cluster)
        - [Client().create_option_group](#clientcreate_option_group)
        - [Client().delete_custom_availability_zone](#clientdelete_custom_availability_zone)
        - [Client().delete_db_cluster](#clientdelete_db_cluster)
        - [Client().delete_db_cluster_endpoint](#clientdelete_db_cluster_endpoint)
        - [Client().delete_db_cluster_parameter_group](#clientdelete_db_cluster_parameter_group)
        - [Client().delete_db_cluster_snapshot](#clientdelete_db_cluster_snapshot)
        - [Client().delete_db_instance](#clientdelete_db_instance)
        - [Client().delete_db_instance_automated_backup](#clientdelete_db_instance_automated_backup)
        - [Client().delete_db_parameter_group](#clientdelete_db_parameter_group)
        - [Client().delete_db_security_group](#clientdelete_db_security_group)
        - [Client().delete_db_snapshot](#clientdelete_db_snapshot)
        - [Client().delete_db_subnet_group](#clientdelete_db_subnet_group)
        - [Client().delete_event_subscription](#clientdelete_event_subscription)
        - [Client().delete_global_cluster](#clientdelete_global_cluster)
        - [Client().delete_installation_media](#clientdelete_installation_media)
        - [Client().delete_option_group](#clientdelete_option_group)
        - [Client().describe_account_attributes](#clientdescribe_account_attributes)
        - [Client().describe_certificates](#clientdescribe_certificates)
        - [Client().describe_custom_availability_zones](#clientdescribe_custom_availability_zones)
        - [Client().describe_db_cluster_backtracks](#clientdescribe_db_cluster_backtracks)
        - [Client().describe_db_cluster_endpoints](#clientdescribe_db_cluster_endpoints)
        - [Client().describe_db_cluster_parameter_groups](#clientdescribe_db_cluster_parameter_groups)
        - [Client().describe_db_cluster_parameters](#clientdescribe_db_cluster_parameters)
        - [Client().describe_db_cluster_snapshot_attributes](#clientdescribe_db_cluster_snapshot_attributes)
        - [Client().describe_db_cluster_snapshots](#clientdescribe_db_cluster_snapshots)
        - [Client().describe_db_clusters](#clientdescribe_db_clusters)
        - [Client().describe_db_engine_versions](#clientdescribe_db_engine_versions)
        - [Client().describe_db_instance_automated_backups](#clientdescribe_db_instance_automated_backups)
        - [Client().describe_db_instances](#clientdescribe_db_instances)
        - [Client().describe_db_log_files](#clientdescribe_db_log_files)
        - [Client().describe_db_parameter_groups](#clientdescribe_db_parameter_groups)
        - [Client().describe_db_parameters](#clientdescribe_db_parameters)
        - [Client().describe_db_security_groups](#clientdescribe_db_security_groups)
        - [Client().describe_db_snapshot_attributes](#clientdescribe_db_snapshot_attributes)
        - [Client().describe_db_snapshots](#clientdescribe_db_snapshots)
        - [Client().describe_db_subnet_groups](#clientdescribe_db_subnet_groups)
        - [Client().describe_engine_default_cluster_parameters](#clientdescribe_engine_default_cluster_parameters)
        - [Client().describe_engine_default_parameters](#clientdescribe_engine_default_parameters)
        - [Client().describe_event_categories](#clientdescribe_event_categories)
        - [Client().describe_event_subscriptions](#clientdescribe_event_subscriptions)
        - [Client().describe_events](#clientdescribe_events)
        - [Client().describe_global_clusters](#clientdescribe_global_clusters)
        - [Client().describe_installation_media](#clientdescribe_installation_media)
        - [Client().describe_option_group_options](#clientdescribe_option_group_options)
        - [Client().describe_option_groups](#clientdescribe_option_groups)
        - [Client().describe_orderable_db_instance_options](#clientdescribe_orderable_db_instance_options)
        - [Client().describe_pending_maintenance_actions](#clientdescribe_pending_maintenance_actions)
        - [Client().describe_reserved_db_instances](#clientdescribe_reserved_db_instances)
        - [Client().describe_reserved_db_instances_offerings](#clientdescribe_reserved_db_instances_offerings)
        - [Client().describe_source_regions](#clientdescribe_source_regions)
        - [Client().describe_valid_db_instance_modifications](#clientdescribe_valid_db_instance_modifications)
        - [Client().download_db_log_file_portion](#clientdownload_db_log_file_portion)
        - [Client().failover_db_cluster](#clientfailover_db_cluster)
        - [Client().generate_db_auth_token](#clientgenerate_db_auth_token)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_installation_media](#clientimport_installation_media)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().modify_current_db_cluster_capacity](#clientmodify_current_db_cluster_capacity)
        - [Client().modify_db_cluster](#clientmodify_db_cluster)
        - [Client().modify_db_cluster_endpoint](#clientmodify_db_cluster_endpoint)
        - [Client().modify_db_cluster_parameter_group](#clientmodify_db_cluster_parameter_group)
        - [Client().modify_db_cluster_snapshot_attribute](#clientmodify_db_cluster_snapshot_attribute)
        - [Client().modify_db_instance](#clientmodify_db_instance)
        - [Client().modify_db_parameter_group](#clientmodify_db_parameter_group)
        - [Client().modify_db_snapshot](#clientmodify_db_snapshot)
        - [Client().modify_db_snapshot_attribute](#clientmodify_db_snapshot_attribute)
        - [Client().modify_db_subnet_group](#clientmodify_db_subnet_group)
        - [Client().modify_event_subscription](#clientmodify_event_subscription)
        - [Client().modify_global_cluster](#clientmodify_global_cluster)
        - [Client().modify_option_group](#clientmodify_option_group)
        - [Client().promote_read_replica](#clientpromote_read_replica)
        - [Client().promote_read_replica_db_cluster](#clientpromote_read_replica_db_cluster)
        - [Client().purchase_reserved_db_instances_offering](#clientpurchase_reserved_db_instances_offering)
        - [Client().reboot_db_instance](#clientreboot_db_instance)
        - [Client().remove_from_global_cluster](#clientremove_from_global_cluster)
        - [Client().remove_role_from_db_cluster](#clientremove_role_from_db_cluster)
        - [Client().remove_role_from_db_instance](#clientremove_role_from_db_instance)
        - [Client().remove_source_identifier_from_subscription](#clientremove_source_identifier_from_subscription)
        - [Client().remove_tags_from_resource](#clientremove_tags_from_resource)
        - [Client().reset_db_cluster_parameter_group](#clientreset_db_cluster_parameter_group)
        - [Client().reset_db_parameter_group](#clientreset_db_parameter_group)
        - [Client().restore_db_cluster_from_s3](#clientrestore_db_cluster_from_s3)
        - [Client().restore_db_cluster_from_snapshot](#clientrestore_db_cluster_from_snapshot)
        - [Client().restore_db_cluster_to_point_in_time](#clientrestore_db_cluster_to_point_in_time)
        - [Client().restore_db_instance_from_db_snapshot](#clientrestore_db_instance_from_db_snapshot)
        - [Client().restore_db_instance_from_s3](#clientrestore_db_instance_from_s3)
        - [Client().restore_db_instance_to_point_in_time](#clientrestore_db_instance_to_point_in_time)
        - [Client().revoke_db_security_group_ingress](#clientrevoke_db_security_group_ingress)
        - [Client().start_activity_stream](#clientstart_activity_stream)
        - [Client().start_db_cluster](#clientstart_db_cluster)
        - [Client().start_db_instance](#clientstart_db_instance)
        - [Client().stop_activity_stream](#clientstop_activity_stream)
        - [Client().stop_db_cluster](#clientstop_db_cluster)
        - [Client().stop_db_instance](#clientstop_db_instance)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_role_to_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L16)

```python
def add_role_to_db_cluster(
    DBClusterIdentifier: str,
    RoleArn: str,
    FeatureName: str = None,
) -> None:
```

### Client().add_role_to_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L22)

```python
def add_role_to_db_instance(
    DBInstanceIdentifier: str,
    RoleArn: str,
    FeatureName: str,
) -> None:
```

### Client().add_source_identifier_to_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L28)

```python
def add_source_identifier_to_subscription(
    SubscriptionName: str,
    SourceIdentifier: str,
) -> Dict[str, Any]:
```

### Client().add_tags_to_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L34)

```python
def add_tags_to_resource(ResourceName: str, Tags: List[Any]) -> None:
```

### Client().apply_pending_maintenance_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L38)

```python
def apply_pending_maintenance_action(
    ResourceIdentifier: str,
    ApplyAction: str,
    OptInType: str,
) -> Dict[str, Any]:
```

### Client().authorize_db_security_group_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L44)

```python
def authorize_db_security_group_ingress(
    DBSecurityGroupName: str,
    CIDRIP: str = None,
    EC2SecurityGroupName: str = None,
    EC2SecurityGroupId: str = None,
    EC2SecurityGroupOwnerId: str = None,
) -> Dict[str, Any]:
```

### Client().backtrack_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L55)

```python
def backtrack_db_cluster(
    DBClusterIdentifier: str,
    BacktrackTo: datetime,
    Force: bool = None,
    UseEarliestTimeOnPointInTimeUnavailable: bool = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L65)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().copy_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L69)

```python
def copy_db_cluster_parameter_group(
    SourceDBClusterParameterGroupIdentifier: str,
    TargetDBClusterParameterGroupIdentifier: str,
    TargetDBClusterParameterGroupDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().copy_db_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L79)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L92)

```python
def copy_db_parameter_group(
    SourceDBParameterGroupIdentifier: str,
    TargetDBParameterGroupIdentifier: str,
    TargetDBParameterGroupDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().copy_db_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L102)

```python
def copy_db_snapshot(
    SourceDBSnapshotIdentifier: str,
    TargetDBSnapshotIdentifier: str,
    KmsKeyId: str = None,
    Tags: List[Any] = None,
    CopyTags: bool = None,
    PreSignedUrl: str = None,
    OptionGroupName: str = None,
    SourceRegion: str = None,
) -> Dict[str, Any]:
```

### Client().copy_option_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L116)

```python
def copy_option_group(
    SourceOptionGroupIdentifier: str,
    TargetOptionGroupIdentifier: str,
    TargetOptionGroupDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_custom_availability_zone

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L126)

```python
def create_custom_availability_zone(
    CustomAvailabilityZoneName: str,
    ExistingVpnId: str = None,
    NewVpnTunnelName: str = None,
    VpnTunnelOriginatorIP: str = None,
) -> Dict[str, Any]:
```

### Client().create_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L136)

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
    BacktrackWindow: int = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    EngineMode: str = None,
    ScalingConfiguration: Dict[str, Any] = None,
    DeletionProtection: bool = None,
    GlobalClusterIdentifier: str = None,
    EnableHttpEndpoint: bool = None,
    CopyTagsToSnapshot: bool = None,
    SourceRegion: str = None,
) -> Dict[str, Any]:
```

### Client().create_db_cluster_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L173)

```python
def create_db_cluster_endpoint(
    DBClusterIdentifier: str,
    DBClusterEndpointIdentifier: str,
    EndpointType: str,
    StaticMembers: List[Any] = None,
    ExcludedMembers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L184)

```python
def create_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
    DBParameterGroupFamily: str,
    Description: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L194)

```python
def create_db_cluster_snapshot(
    DBClusterSnapshotIdentifier: str,
    DBClusterIdentifier: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L203)

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
    PerformanceInsightsRetentionPeriod: int = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    ProcessorFeatures: List[Any] = None,
    DeletionProtection: bool = None,
    MaxAllocatedStorage: int = None,
) -> Dict[str, Any]:
```

### Client().create_db_instance_read_replica

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L255)

```python
def create_db_instance_read_replica(
    DBInstanceIdentifier: str,
    SourceDBInstanceIdentifier: str,
    DBInstanceClass: str = None,
    AvailabilityZone: str = None,
    Port: int = None,
    MultiAZ: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    Iops: int = None,
    OptionGroupName: str = None,
    DBParameterGroupName: str = None,
    PubliclyAccessible: bool = None,
    Tags: List[Any] = None,
    DBSubnetGroupName: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    StorageType: str = None,
    CopyTagsToSnapshot: bool = None,
    MonitoringInterval: int = None,
    MonitoringRoleArn: str = None,
    KmsKeyId: str = None,
    PreSignedUrl: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnablePerformanceInsights: bool = None,
    PerformanceInsightsKMSKeyId: str = None,
    PerformanceInsightsRetentionPeriod: int = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    ProcessorFeatures: List[Any] = None,
    UseDefaultProcessorFeatures: bool = None,
    DeletionProtection: bool = None,
    Domain: str = None,
    DomainIAMRoleName: str = None,
    SourceRegion: str = None,
) -> Dict[str, Any]:
```

### Client().create_db_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L292)

```python
def create_db_parameter_group(
    DBParameterGroupName: str,
    DBParameterGroupFamily: str,
    Description: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L302)

```python
def create_db_security_group(
    DBSecurityGroupName: str,
    DBSecurityGroupDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L311)

```python
def create_db_snapshot(
    DBSnapshotIdentifier: str,
    DBInstanceIdentifier: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L320)

```python
def create_db_subnet_group(
    DBSubnetGroupName: str,
    DBSubnetGroupDescription: str,
    SubnetIds: List[Any],
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L330)

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

### Client().create_global_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L343)

```python
def create_global_cluster(
    GlobalClusterIdentifier: str = None,
    SourceDBClusterIdentifier: str = None,
    Engine: str = None,
    EngineVersion: str = None,
    DeletionProtection: bool = None,
    DatabaseName: str = None,
    StorageEncrypted: bool = None,
) -> Dict[str, Any]:
```

### Client().create_option_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L356)

```python
def create_option_group(
    OptionGroupName: str,
    EngineName: str,
    MajorEngineVersion: str,
    OptionGroupDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_custom_availability_zone

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L367)

```python
def delete_custom_availability_zone(
    CustomAvailabilityZoneId: str,
) -> Dict[str, Any]:
```

### Client().delete_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L373)

```python
def delete_db_cluster(
    DBClusterIdentifier: str,
    SkipFinalSnapshot: bool = None,
    FinalDBSnapshotIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().delete_db_cluster_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L382)

```python
def delete_db_cluster_endpoint(
    DBClusterEndpointIdentifier: str,
) -> Dict[str, Any]:
```

### Client().delete_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L388)

```python
def delete_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
) -> None:
```

### Client().delete_db_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L394)

```python
def delete_db_cluster_snapshot(
    DBClusterSnapshotIdentifier: str,
) -> Dict[str, Any]:
```

### Client().delete_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L400)

```python
def delete_db_instance(
    DBInstanceIdentifier: str,
    SkipFinalSnapshot: bool = None,
    FinalDBSnapshotIdentifier: str = None,
    DeleteAutomatedBackups: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_db_instance_automated_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L410)

```python
def delete_db_instance_automated_backup(DbiResourceId: str) -> Dict[str, Any]:
```

### Client().delete_db_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L414)

```python
def delete_db_parameter_group(DBParameterGroupName: str) -> None:
```

### Client().delete_db_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L418)

```python
def delete_db_security_group(DBSecurityGroupName: str) -> None:
```

### Client().delete_db_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L422)

```python
def delete_db_snapshot(DBSnapshotIdentifier: str) -> Dict[str, Any]:
```

### Client().delete_db_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L426)

```python
def delete_db_subnet_group(DBSubnetGroupName: str) -> None:
```

### Client().delete_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L430)

```python
def delete_event_subscription(SubscriptionName: str) -> Dict[str, Any]:
```

### Client().delete_global_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L434)

```python
def delete_global_cluster(GlobalClusterIdentifier: str) -> Dict[str, Any]:
```

### Client().delete_installation_media

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L438)

```python
def delete_installation_media(InstallationMediaId: str) -> Dict[str, Any]:
```

### Client().delete_option_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L442)

```python
def delete_option_group(OptionGroupName: str) -> None:
```

### Client().describe_account_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L446)

```python
def describe_account_attributes() -> Dict[str, Any]:
```

### Client().describe_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L450)

```python
def describe_certificates(
    CertificateIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_custom_availability_zones

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L460)

```python
def describe_custom_availability_zones(
    CustomAvailabilityZoneId: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_backtracks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L470)

```python
def describe_db_cluster_backtracks(
    DBClusterIdentifier: str,
    BacktrackIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L481)

```python
def describe_db_cluster_endpoints(
    DBClusterIdentifier: str = None,
    DBClusterEndpointIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_parameter_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L492)

```python
def describe_db_cluster_parameter_groups(
    DBClusterParameterGroupName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L502)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L513)

```python
def describe_db_cluster_snapshot_attributes(
    DBClusterSnapshotIdentifier: str,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L519)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L533)

```python
def describe_db_clusters(
    DBClusterIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_db_engine_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L544)

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
    IncludeAll: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_db_instance_automated_backups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L560)

```python
def describe_db_instance_automated_backups(
    DbiResourceId: str = None,
    DBInstanceIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L571)

```python
def describe_db_instances(
    DBInstanceIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_log_files

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L581)

```python
def describe_db_log_files(
    DBInstanceIdentifier: str,
    FilenameContains: str = None,
    FileLastWritten: int = None,
    FileSize: int = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_parameter_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L594)

```python
def describe_db_parameter_groups(
    DBParameterGroupName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L604)

```python
def describe_db_parameters(
    DBParameterGroupName: str,
    Source: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_security_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L615)

```python
def describe_db_security_groups(
    DBSecurityGroupName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_snapshot_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L625)

```python
def describe_db_snapshot_attributes(
    DBSnapshotIdentifier: str,
) -> Dict[str, Any]:
```

### Client().describe_db_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L631)

```python
def describe_db_snapshots(
    DBInstanceIdentifier: str = None,
    DBSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None,
    DbiResourceId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_subnet_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L646)

```python
def describe_db_subnet_groups(
    DBSubnetGroupName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_engine_default_cluster_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L656)

```python
def describe_engine_default_cluster_parameters(
    DBParameterGroupFamily: str,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_engine_default_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L666)

```python
def describe_engine_default_parameters(
    DBParameterGroupFamily: str,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_event_categories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L676)

```python
def describe_event_categories(
    SourceType: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_event_subscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L682)

```python
def describe_event_subscriptions(
    SubscriptionName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L692)

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

### Client().describe_global_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L707)

```python
def describe_global_clusters(
    GlobalClusterIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_installation_media

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L717)

```python
def describe_installation_media(
    InstallationMediaId: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_option_group_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L727)

```python
def describe_option_group_options(
    EngineName: str,
    MajorEngineVersion: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_option_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L738)

```python
def describe_option_groups(
    OptionGroupName: str = None,
    Filters: List[Any] = None,
    Marker: str = None,
    MaxRecords: int = None,
    EngineName: str = None,
    MajorEngineVersion: str = None,
) -> Dict[str, Any]:
```

### Client().describe_orderable_db_instance_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L750)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L764)

```python
def describe_pending_maintenance_actions(
    ResourceIdentifier: str = None,
    Filters: List[Any] = None,
    Marker: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_db_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L774)

```python
def describe_reserved_db_instances(
    ReservedDBInstanceId: str = None,
    ReservedDBInstancesOfferingId: str = None,
    DBInstanceClass: str = None,
    Duration: str = None,
    ProductDescription: str = None,
    OfferingType: str = None,
    MultiAZ: bool = None,
    LeaseId: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_db_instances_offerings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L791)

```python
def describe_reserved_db_instances_offerings(
    ReservedDBInstancesOfferingId: str = None,
    DBInstanceClass: str = None,
    Duration: str = None,
    ProductDescription: str = None,
    OfferingType: str = None,
    MultiAZ: bool = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_source_regions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L806)

```python
def describe_source_regions(
    RegionName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_valid_db_instance_modifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L816)

```python
def describe_valid_db_instance_modifications(
    DBInstanceIdentifier: str,
) -> Dict[str, Any]:
```

### Client().download_db_log_file_portion

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L822)

```python
def download_db_log_file_portion(
    DBInstanceIdentifier: str,
    LogFileName: str,
    Marker: str = None,
    NumberOfLines: int = None,
) -> Dict[str, Any]:
```

### Client().failover_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L832)

```python
def failover_db_cluster(
    DBClusterIdentifier: str,
    TargetDBInstanceIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().generate_db_auth_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L838)

```python
def generate_db_auth_token(
    DBHostname: str = None,
    Port: int = None,
    DBUsername: str = None,
    Region: str = None,
) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L848)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L858)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L862)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_installation_media

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L866)

```python
def import_installation_media(
    CustomAvailabilityZoneId: str,
    Engine: str,
    EngineVersion: str,
    EngineInstallationMediaPath: str,
    OSInstallationMediaPath: str,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L877)

```python
def list_tags_for_resource(
    ResourceName: str,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_current_db_cluster_capacity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L883)

```python
def modify_current_db_cluster_capacity(
    DBClusterIdentifier: str,
    Capacity: int = None,
    SecondsBeforeTimeout: int = None,
    TimeoutAction: str = None,
) -> Dict[str, Any]:
```

### Client().modify_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L893)

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
    BacktrackWindow: int = None,
    CloudwatchLogsExportConfiguration: Dict[str, Any] = None,
    EngineVersion: str = None,
    AllowMajorVersionUpgrade: bool = None,
    DBInstanceParameterGroupName: str = None,
    ScalingConfiguration: Dict[str, Any] = None,
    DeletionProtection: bool = None,
    EnableHttpEndpoint: bool = None,
    CopyTagsToSnapshot: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_db_cluster_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L920)

```python
def modify_db_cluster_endpoint(
    DBClusterEndpointIdentifier: str,
    EndpointType: str = None,
    StaticMembers: List[Any] = None,
    ExcludedMembers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L930)

```python
def modify_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
    Parameters: List[Any],
) -> Dict[str, Any]:
```

### Client().modify_db_cluster_snapshot_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L936)

```python
def modify_db_cluster_snapshot_attribute(
    DBClusterSnapshotIdentifier: str,
    AttributeName: str,
    ValuesToAdd: List[Any] = None,
    ValuesToRemove: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L946)

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
    PerformanceInsightsRetentionPeriod: int = None,
    CloudwatchLogsExportConfiguration: Dict[str, Any] = None,
    ProcessorFeatures: List[Any] = None,
    UseDefaultProcessorFeatures: bool = None,
    DeletionProtection: bool = None,
    MaxAllocatedStorage: int = None,
) -> Dict[str, Any]:
```

### Client().modify_db_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L993)

```python
def modify_db_parameter_group(
    DBParameterGroupName: str,
    Parameters: List[Any],
) -> Dict[str, Any]:
```

### Client().modify_db_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L999)

```python
def modify_db_snapshot(
    DBSnapshotIdentifier: str,
    EngineVersion: str = None,
    OptionGroupName: str = None,
) -> Dict[str, Any]:
```

### Client().modify_db_snapshot_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1008)

```python
def modify_db_snapshot_attribute(
    DBSnapshotIdentifier: str,
    AttributeName: str,
    ValuesToAdd: List[Any] = None,
    ValuesToRemove: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_db_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1018)

```python
def modify_db_subnet_group(
    DBSubnetGroupName: str,
    SubnetIds: List[Any],
    DBSubnetGroupDescription: str = None,
) -> Dict[str, Any]:
```

### Client().modify_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1027)

```python
def modify_event_subscription(
    SubscriptionName: str,
    SnsTopicArn: str = None,
    SourceType: str = None,
    EventCategories: List[Any] = None,
    Enabled: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_global_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1038)

```python
def modify_global_cluster(
    GlobalClusterIdentifier: str = None,
    NewGlobalClusterIdentifier: str = None,
    DeletionProtection: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_option_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1047)

```python
def modify_option_group(
    OptionGroupName: str,
    OptionsToInclude: List[Any] = None,
    OptionsToRemove: List[Any] = None,
    ApplyImmediately: bool = None,
) -> Dict[str, Any]:
```

### Client().promote_read_replica

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1057)

```python
def promote_read_replica(
    DBInstanceIdentifier: str,
    BackupRetentionPeriod: int = None,
    PreferredBackupWindow: str = None,
) -> Dict[str, Any]:
```

### Client().promote_read_replica_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1066)

```python
def promote_read_replica_db_cluster(
    DBClusterIdentifier: str,
) -> Dict[str, Any]:
```

### Client().purchase_reserved_db_instances_offering

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1072)

```python
def purchase_reserved_db_instances_offering(
    ReservedDBInstancesOfferingId: str,
    ReservedDBInstanceId: str = None,
    DBInstanceCount: int = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().reboot_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1082)

```python
def reboot_db_instance(
    DBInstanceIdentifier: str,
    ForceFailover: bool = None,
) -> Dict[str, Any]:
```

### Client().remove_from_global_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1088)

```python
def remove_from_global_cluster(
    GlobalClusterIdentifier: str = None,
    DbClusterIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().remove_role_from_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1094)

```python
def remove_role_from_db_cluster(
    DBClusterIdentifier: str,
    RoleArn: str,
    FeatureName: str = None,
) -> None:
```

### Client().remove_role_from_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1100)

```python
def remove_role_from_db_instance(
    DBInstanceIdentifier: str,
    RoleArn: str,
    FeatureName: str,
) -> None:
```

### Client().remove_source_identifier_from_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1106)

```python
def remove_source_identifier_from_subscription(
    SubscriptionName: str,
    SourceIdentifier: str,
) -> Dict[str, Any]:
```

### Client().remove_tags_from_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1112)

```python
def remove_tags_from_resource(ResourceName: str, TagKeys: List[Any]) -> None:
```

### Client().reset_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1116)

```python
def reset_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().reset_db_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1125)

```python
def reset_db_parameter_group(
    DBParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().restore_db_cluster_from_s3

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1134)

```python
def restore_db_cluster_from_s3(
    DBClusterIdentifier: str,
    Engine: str,
    MasterUsername: str,
    MasterUserPassword: str,
    SourceEngine: str,
    SourceEngineVersion: str,
    S3BucketName: str,
    S3IngestionRoleArn: str,
    AvailabilityZones: List[Any] = None,
    BackupRetentionPeriod: int = None,
    CharacterSetName: str = None,
    DatabaseName: str = None,
    DBClusterParameterGroupName: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    DBSubnetGroupName: str = None,
    EngineVersion: str = None,
    Port: int = None,
    OptionGroupName: str = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    Tags: List[Any] = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    S3Prefix: str = None,
    BacktrackWindow: int = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    DeletionProtection: bool = None,
    CopyTagsToSnapshot: bool = None,
) -> Dict[str, Any]:
```

### Client().restore_db_cluster_from_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1169)

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
    BacktrackWindow: int = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    EngineMode: str = None,
    ScalingConfiguration: Dict[str, Any] = None,
    DBClusterParameterGroupName: str = None,
    DeletionProtection: bool = None,
    CopyTagsToSnapshot: bool = None,
) -> Dict[str, Any]:
```

### Client().restore_db_cluster_to_point_in_time

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1195)

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
    BacktrackWindow: int = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    DBClusterParameterGroupName: str = None,
    DeletionProtection: bool = None,
    CopyTagsToSnapshot: bool = None,
) -> Dict[str, Any]:
```

### Client().restore_db_instance_from_db_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1218)

```python
def restore_db_instance_from_db_snapshot(
    DBInstanceIdentifier: str,
    DBSnapshotIdentifier: str,
    DBInstanceClass: str = None,
    Port: int = None,
    AvailabilityZone: str = None,
    DBSubnetGroupName: str = None,
    MultiAZ: bool = None,
    PubliclyAccessible: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    DBName: str = None,
    Engine: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    Tags: List[Any] = None,
    StorageType: str = None,
    TdeCredentialArn: str = None,
    TdeCredentialPassword: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    Domain: str = None,
    CopyTagsToSnapshot: bool = None,
    DomainIAMRoleName: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    ProcessorFeatures: List[Any] = None,
    UseDefaultProcessorFeatures: bool = None,
    DBParameterGroupName: str = None,
    DeletionProtection: bool = None,
) -> Dict[str, Any]:
```

### Client().restore_db_instance_from_s3

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1252)

```python
def restore_db_instance_from_s3(
    DBInstanceIdentifier: str,
    DBInstanceClass: str,
    Engine: str,
    SourceEngine: str,
    SourceEngineVersion: str,
    S3BucketName: str,
    S3IngestionRoleArn: str,
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
    PubliclyAccessible: bool = None,
    Tags: List[Any] = None,
    StorageType: str = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    CopyTagsToSnapshot: bool = None,
    MonitoringInterval: int = None,
    MonitoringRoleArn: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    S3Prefix: str = None,
    EnablePerformanceInsights: bool = None,
    PerformanceInsightsKMSKeyId: str = None,
    PerformanceInsightsRetentionPeriod: int = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    ProcessorFeatures: List[Any] = None,
    UseDefaultProcessorFeatures: bool = None,
    DeletionProtection: bool = None,
) -> Dict[str, Any]:
```

### Client().restore_db_instance_to_point_in_time

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1301)

```python
def restore_db_instance_to_point_in_time(
    TargetDBInstanceIdentifier: str,
    SourceDBInstanceIdentifier: str = None,
    RestoreTime: datetime = None,
    UseLatestRestorableTime: bool = None,
    DBInstanceClass: str = None,
    Port: int = None,
    AvailabilityZone: str = None,
    DBSubnetGroupName: str = None,
    MultiAZ: bool = None,
    PubliclyAccessible: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    LicenseModel: str = None,
    DBName: str = None,
    Engine: str = None,
    Iops: int = None,
    OptionGroupName: str = None,
    CopyTagsToSnapshot: bool = None,
    Tags: List[Any] = None,
    StorageType: str = None,
    TdeCredentialArn: str = None,
    TdeCredentialPassword: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    Domain: str = None,
    DomainIAMRoleName: str = None,
    EnableIAMDatabaseAuthentication: bool = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    ProcessorFeatures: List[Any] = None,
    UseDefaultProcessorFeatures: bool = None,
    DBParameterGroupName: str = None,
    DeletionProtection: bool = None,
    SourceDbiResourceId: str = None,
) -> Dict[str, Any]:
```

### Client().revoke_db_security_group_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1338)

```python
def revoke_db_security_group_ingress(
    DBSecurityGroupName: str,
    CIDRIP: str = None,
    EC2SecurityGroupName: str = None,
    EC2SecurityGroupId: str = None,
    EC2SecurityGroupOwnerId: str = None,
) -> Dict[str, Any]:
```

### Client().start_activity_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1349)

```python
def start_activity_stream(
    ResourceArn: str,
    Mode: str,
    KmsKeyId: str,
    ApplyImmediately: bool = None,
) -> Dict[str, Any]:
```

### Client().start_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1355)

```python
def start_db_cluster(DBClusterIdentifier: str) -> Dict[str, Any]:
```

### Client().start_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1359)

```python
def start_db_instance(DBInstanceIdentifier: str) -> Dict[str, Any]:
```

### Client().stop_activity_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1363)

```python
def stop_activity_stream(
    ResourceArn: str,
    ApplyImmediately: bool = None,
) -> Dict[str, Any]:
```

### Client().stop_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1369)

```python
def stop_db_cluster(DBClusterIdentifier: str) -> Dict[str, Any]:
```

### Client().stop_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/client.py#L1373)

```python
def stop_db_instance(
    DBInstanceIdentifier: str,
    DBSnapshotIdentifier: str = None,
) -> Dict[str, Any]:
```
