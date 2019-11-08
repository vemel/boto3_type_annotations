# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.docdb.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Docdb](index.md#docdb) / Client
    - [Client](#client)
        - [Client().add_tags_to_resource](#clientadd_tags_to_resource)
        - [Client().apply_pending_maintenance_action](#clientapply_pending_maintenance_action)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().copy_db_cluster_parameter_group](#clientcopy_db_cluster_parameter_group)
        - [Client().copy_db_cluster_snapshot](#clientcopy_db_cluster_snapshot)
        - [Client().create_db_cluster](#clientcreate_db_cluster)
        - [Client().create_db_cluster_parameter_group](#clientcreate_db_cluster_parameter_group)
        - [Client().create_db_cluster_snapshot](#clientcreate_db_cluster_snapshot)
        - [Client().create_db_instance](#clientcreate_db_instance)
        - [Client().create_db_subnet_group](#clientcreate_db_subnet_group)
        - [Client().delete_db_cluster](#clientdelete_db_cluster)
        - [Client().delete_db_cluster_parameter_group](#clientdelete_db_cluster_parameter_group)
        - [Client().delete_db_cluster_snapshot](#clientdelete_db_cluster_snapshot)
        - [Client().delete_db_instance](#clientdelete_db_instance)
        - [Client().delete_db_subnet_group](#clientdelete_db_subnet_group)
        - [Client().describe_certificates](#clientdescribe_certificates)
        - [Client().describe_db_cluster_parameter_groups](#clientdescribe_db_cluster_parameter_groups)
        - [Client().describe_db_cluster_parameters](#clientdescribe_db_cluster_parameters)
        - [Client().describe_db_cluster_snapshot_attributes](#clientdescribe_db_cluster_snapshot_attributes)
        - [Client().describe_db_cluster_snapshots](#clientdescribe_db_cluster_snapshots)
        - [Client().describe_db_clusters](#clientdescribe_db_clusters)
        - [Client().describe_db_engine_versions](#clientdescribe_db_engine_versions)
        - [Client().describe_db_instances](#clientdescribe_db_instances)
        - [Client().describe_db_subnet_groups](#clientdescribe_db_subnet_groups)
        - [Client().describe_engine_default_cluster_parameters](#clientdescribe_engine_default_cluster_parameters)
        - [Client().describe_event_categories](#clientdescribe_event_categories)
        - [Client().describe_events](#clientdescribe_events)
        - [Client().describe_orderable_db_instance_options](#clientdescribe_orderable_db_instance_options)
        - [Client().describe_pending_maintenance_actions](#clientdescribe_pending_maintenance_actions)
        - [Client().failover_db_cluster](#clientfailover_db_cluster)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().modify_db_cluster](#clientmodify_db_cluster)
        - [Client().modify_db_cluster_parameter_group](#clientmodify_db_cluster_parameter_group)
        - [Client().modify_db_cluster_snapshot_attribute](#clientmodify_db_cluster_snapshot_attribute)
        - [Client().modify_db_instance](#clientmodify_db_instance)
        - [Client().modify_db_subnet_group](#clientmodify_db_subnet_group)
        - [Client().reboot_db_instance](#clientreboot_db_instance)
        - [Client().remove_tags_from_resource](#clientremove_tags_from_resource)
        - [Client().reset_db_cluster_parameter_group](#clientreset_db_cluster_parameter_group)
        - [Client().restore_db_cluster_from_snapshot](#clientrestore_db_cluster_from_snapshot)
        - [Client().restore_db_cluster_to_point_in_time](#clientrestore_db_cluster_to_point_in_time)
        - [Client().start_db_cluster](#clientstart_db_cluster)
        - [Client().stop_db_cluster](#clientstop_db_cluster)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_tags_to_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L16)

```python
def add_tags_to_resource(ResourceName: str, Tags: List[Any]) -> None:
```

### Client().apply_pending_maintenance_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L20)

```python
def apply_pending_maintenance_action(
    ResourceIdentifier: str,
    ApplyAction: str,
    OptInType: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L26)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().copy_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L30)

```python
def copy_db_cluster_parameter_group(
    SourceDBClusterParameterGroupIdentifier: str,
    TargetDBClusterParameterGroupIdentifier: str,
    TargetDBClusterParameterGroupDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().copy_db_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L40)

```python
def copy_db_cluster_snapshot(
    SourceDBClusterSnapshotIdentifier: str,
    TargetDBClusterSnapshotIdentifier: str,
    KmsKeyId: str = None,
    PreSignedUrl: str = None,
    CopyTags: bool = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L52)

```python
def create_db_cluster(
    DBClusterIdentifier: str,
    Engine: str,
    MasterUsername: str,
    MasterUserPassword: str,
    AvailabilityZones: List[Any] = None,
    BackupRetentionPeriod: int = None,
    DBClusterParameterGroupName: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    DBSubnetGroupName: str = None,
    EngineVersion: str = None,
    Port: int = None,
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    Tags: List[Any] = None,
    StorageEncrypted: bool = None,
    KmsKeyId: str = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    DeletionProtection: bool = None,
) -> Dict[str, Any]:
```

### Client().create_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L76)

```python
def create_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
    DBParameterGroupFamily: str,
    Description: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L86)

```python
def create_db_cluster_snapshot(
    DBClusterSnapshotIdentifier: str,
    DBClusterIdentifier: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L95)

```python
def create_db_instance(
    DBInstanceIdentifier: str,
    DBInstanceClass: str,
    Engine: str,
    DBClusterIdentifier: str,
    AvailabilityZone: str = None,
    PreferredMaintenanceWindow: str = None,
    AutoMinorVersionUpgrade: bool = None,
    Tags: List[Any] = None,
    PromotionTier: int = None,
) -> Dict[str, Any]:
```

### Client().create_db_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L110)

```python
def create_db_subnet_group(
    DBSubnetGroupName: str,
    DBSubnetGroupDescription: str,
    SubnetIds: List[Any],
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L120)

```python
def delete_db_cluster(
    DBClusterIdentifier: str,
    SkipFinalSnapshot: bool = None,
    FinalDBSnapshotIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().delete_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L129)

```python
def delete_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
) -> None:
```

### Client().delete_db_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L135)

```python
def delete_db_cluster_snapshot(
    DBClusterSnapshotIdentifier: str,
) -> Dict[str, Any]:
```

### Client().delete_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L141)

```python
def delete_db_instance(DBInstanceIdentifier: str) -> Dict[str, Any]:
```

### Client().delete_db_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L145)

```python
def delete_db_subnet_group(DBSubnetGroupName: str) -> None:
```

### Client().describe_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L149)

```python
def describe_certificates(
    CertificateIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_parameter_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L159)

```python
def describe_db_cluster_parameter_groups(
    DBClusterParameterGroupName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L169)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L180)

```python
def describe_db_cluster_snapshot_attributes(
    DBClusterSnapshotIdentifier: str,
) -> Dict[str, Any]:
```

### Client().describe_db_cluster_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L186)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L200)

```python
def describe_db_clusters(
    DBClusterIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_engine_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L210)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L225)

```python
def describe_db_instances(
    DBInstanceIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_db_subnet_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L235)

```python
def describe_db_subnet_groups(
    DBSubnetGroupName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_engine_default_cluster_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L245)

```python
def describe_engine_default_cluster_parameters(
    DBParameterGroupFamily: str,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_event_categories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L255)

```python
def describe_event_categories(
    SourceType: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L261)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L276)

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

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L290)

```python
def describe_pending_maintenance_actions(
    ResourceIdentifier: str = None,
    Filters: List[Any] = None,
    Marker: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().failover_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L300)

```python
def failover_db_cluster(
    DBClusterIdentifier: str = None,
    TargetDBInstanceIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L306)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L316)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L320)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L324)

```python
def list_tags_for_resource(
    ResourceName: str,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L330)

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
    PreferredBackupWindow: str = None,
    PreferredMaintenanceWindow: str = None,
    CloudwatchLogsExportConfiguration: Dict[str, Any] = None,
    EngineVersion: str = None,
    DeletionProtection: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L349)

```python
def modify_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
    Parameters: List[Any],
) -> Dict[str, Any]:
```

### Client().modify_db_cluster_snapshot_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L355)

```python
def modify_db_cluster_snapshot_attribute(
    DBClusterSnapshotIdentifier: str,
    AttributeName: str,
    ValuesToAdd: List[Any] = None,
    ValuesToRemove: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L365)

```python
def modify_db_instance(
    DBInstanceIdentifier: str,
    DBInstanceClass: str = None,
    ApplyImmediately: bool = None,
    PreferredMaintenanceWindow: str = None,
    AutoMinorVersionUpgrade: bool = None,
    NewDBInstanceIdentifier: str = None,
    CACertificateIdentifier: str = None,
    PromotionTier: int = None,
) -> Dict[str, Any]:
```

### Client().modify_db_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L379)

```python
def modify_db_subnet_group(
    DBSubnetGroupName: str,
    SubnetIds: List[Any],
    DBSubnetGroupDescription: str = None,
) -> Dict[str, Any]:
```

### Client().reboot_db_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L388)

```python
def reboot_db_instance(
    DBInstanceIdentifier: str,
    ForceFailover: bool = None,
) -> Dict[str, Any]:
```

### Client().remove_tags_from_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L394)

```python
def remove_tags_from_resource(ResourceName: str, TagKeys: List[Any]) -> None:
```

### Client().reset_db_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L398)

```python
def reset_db_cluster_parameter_group(
    DBClusterParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().restore_db_cluster_from_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L407)

```python
def restore_db_cluster_from_snapshot(
    DBClusterIdentifier: str,
    SnapshotIdentifier: str,
    Engine: str,
    AvailabilityZones: List[Any] = None,
    EngineVersion: str = None,
    Port: int = None,
    DBSubnetGroupName: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    Tags: List[Any] = None,
    KmsKeyId: str = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    DeletionProtection: bool = None,
) -> Dict[str, Any]:
```

### Client().restore_db_cluster_to_point_in_time

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L425)

```python
def restore_db_cluster_to_point_in_time(
    DBClusterIdentifier: str,
    SourceDBClusterIdentifier: str,
    RestoreToTime: datetime = None,
    UseLatestRestorableTime: bool = None,
    Port: int = None,
    DBSubnetGroupName: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    Tags: List[Any] = None,
    KmsKeyId: str = None,
    EnableCloudwatchLogsExports: List[Any] = None,
    DeletionProtection: bool = None,
) -> Dict[str, Any]:
```

### Client().start_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L442)

```python
def start_db_cluster(DBClusterIdentifier: str) -> Dict[str, Any]:
```

### Client().stop_db_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/docdb/client.py#L446)

```python
def stop_db_cluster(DBClusterIdentifier: str) -> Dict[str, Any]:
```
