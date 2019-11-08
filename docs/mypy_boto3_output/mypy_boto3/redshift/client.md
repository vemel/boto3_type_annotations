# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.redshift.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Redshift](index.md#redshift) / Client
    - [Client](#client)
        - [Client().accept_reserved_node_exchange](#clientaccept_reserved_node_exchange)
        - [Client().authorize_cluster_security_group_ingress](#clientauthorize_cluster_security_group_ingress)
        - [Client().authorize_snapshot_access](#clientauthorize_snapshot_access)
        - [Client().batch_delete_cluster_snapshots](#clientbatch_delete_cluster_snapshots)
        - [Client().batch_modify_cluster_snapshots](#clientbatch_modify_cluster_snapshots)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_resize](#clientcancel_resize)
        - [Client().copy_cluster_snapshot](#clientcopy_cluster_snapshot)
        - [Client().create_cluster](#clientcreate_cluster)
        - [Client().create_cluster_parameter_group](#clientcreate_cluster_parameter_group)
        - [Client().create_cluster_security_group](#clientcreate_cluster_security_group)
        - [Client().create_cluster_snapshot](#clientcreate_cluster_snapshot)
        - [Client().create_cluster_subnet_group](#clientcreate_cluster_subnet_group)
        - [Client().create_event_subscription](#clientcreate_event_subscription)
        - [Client().create_hsm_client_certificate](#clientcreate_hsm_client_certificate)
        - [Client().create_hsm_configuration](#clientcreate_hsm_configuration)
        - [Client().create_snapshot_copy_grant](#clientcreate_snapshot_copy_grant)
        - [Client().create_snapshot_schedule](#clientcreate_snapshot_schedule)
        - [Client().create_tags](#clientcreate_tags)
        - [Client().delete_cluster](#clientdelete_cluster)
        - [Client().delete_cluster_parameter_group](#clientdelete_cluster_parameter_group)
        - [Client().delete_cluster_security_group](#clientdelete_cluster_security_group)
        - [Client().delete_cluster_snapshot](#clientdelete_cluster_snapshot)
        - [Client().delete_cluster_subnet_group](#clientdelete_cluster_subnet_group)
        - [Client().delete_event_subscription](#clientdelete_event_subscription)
        - [Client().delete_hsm_client_certificate](#clientdelete_hsm_client_certificate)
        - [Client().delete_hsm_configuration](#clientdelete_hsm_configuration)
        - [Client().delete_snapshot_copy_grant](#clientdelete_snapshot_copy_grant)
        - [Client().delete_snapshot_schedule](#clientdelete_snapshot_schedule)
        - [Client().delete_tags](#clientdelete_tags)
        - [Client().describe_account_attributes](#clientdescribe_account_attributes)
        - [Client().describe_cluster_db_revisions](#clientdescribe_cluster_db_revisions)
        - [Client().describe_cluster_parameter_groups](#clientdescribe_cluster_parameter_groups)
        - [Client().describe_cluster_parameters](#clientdescribe_cluster_parameters)
        - [Client().describe_cluster_security_groups](#clientdescribe_cluster_security_groups)
        - [Client().describe_cluster_snapshots](#clientdescribe_cluster_snapshots)
        - [Client().describe_cluster_subnet_groups](#clientdescribe_cluster_subnet_groups)
        - [Client().describe_cluster_tracks](#clientdescribe_cluster_tracks)
        - [Client().describe_cluster_versions](#clientdescribe_cluster_versions)
        - [Client().describe_clusters](#clientdescribe_clusters)
        - [Client().describe_default_cluster_parameters](#clientdescribe_default_cluster_parameters)
        - [Client().describe_event_categories](#clientdescribe_event_categories)
        - [Client().describe_event_subscriptions](#clientdescribe_event_subscriptions)
        - [Client().describe_events](#clientdescribe_events)
        - [Client().describe_hsm_client_certificates](#clientdescribe_hsm_client_certificates)
        - [Client().describe_hsm_configurations](#clientdescribe_hsm_configurations)
        - [Client().describe_logging_status](#clientdescribe_logging_status)
        - [Client().describe_node_configuration_options](#clientdescribe_node_configuration_options)
        - [Client().describe_orderable_cluster_options](#clientdescribe_orderable_cluster_options)
        - [Client().describe_reserved_node_offerings](#clientdescribe_reserved_node_offerings)
        - [Client().describe_reserved_nodes](#clientdescribe_reserved_nodes)
        - [Client().describe_resize](#clientdescribe_resize)
        - [Client().describe_snapshot_copy_grants](#clientdescribe_snapshot_copy_grants)
        - [Client().describe_snapshot_schedules](#clientdescribe_snapshot_schedules)
        - [Client().describe_storage](#clientdescribe_storage)
        - [Client().describe_table_restore_status](#clientdescribe_table_restore_status)
        - [Client().describe_tags](#clientdescribe_tags)
        - [Client().disable_logging](#clientdisable_logging)
        - [Client().disable_snapshot_copy](#clientdisable_snapshot_copy)
        - [Client().enable_logging](#clientenable_logging)
        - [Client().enable_snapshot_copy](#clientenable_snapshot_copy)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_cluster_credentials](#clientget_cluster_credentials)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_reserved_node_exchange_offerings](#clientget_reserved_node_exchange_offerings)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().modify_cluster](#clientmodify_cluster)
        - [Client().modify_cluster_db_revision](#clientmodify_cluster_db_revision)
        - [Client().modify_cluster_iam_roles](#clientmodify_cluster_iam_roles)
        - [Client().modify_cluster_maintenance](#clientmodify_cluster_maintenance)
        - [Client().modify_cluster_parameter_group](#clientmodify_cluster_parameter_group)
        - [Client().modify_cluster_snapshot](#clientmodify_cluster_snapshot)
        - [Client().modify_cluster_snapshot_schedule](#clientmodify_cluster_snapshot_schedule)
        - [Client().modify_cluster_subnet_group](#clientmodify_cluster_subnet_group)
        - [Client().modify_event_subscription](#clientmodify_event_subscription)
        - [Client().modify_snapshot_copy_retention_period](#clientmodify_snapshot_copy_retention_period)
        - [Client().modify_snapshot_schedule](#clientmodify_snapshot_schedule)
        - [Client().purchase_reserved_node_offering](#clientpurchase_reserved_node_offering)
        - [Client().reboot_cluster](#clientreboot_cluster)
        - [Client().reset_cluster_parameter_group](#clientreset_cluster_parameter_group)
        - [Client().resize_cluster](#clientresize_cluster)
        - [Client().restore_from_cluster_snapshot](#clientrestore_from_cluster_snapshot)
        - [Client().restore_table_from_cluster_snapshot](#clientrestore_table_from_cluster_snapshot)
        - [Client().revoke_cluster_security_group_ingress](#clientrevoke_cluster_security_group_ingress)
        - [Client().revoke_snapshot_access](#clientrevoke_snapshot_access)
        - [Client().rotate_encryption_key](#clientrotate_encryption_key)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L13)

```python
class Client(BaseClient):
```

### Client().accept_reserved_node_exchange

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L16)

```python
def accept_reserved_node_exchange(
    ReservedNodeId: str,
    TargetReservedNodeOfferingId: str,
) -> Dict[str, Any]:
```

### Client().authorize_cluster_security_group_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L22)

```python
def authorize_cluster_security_group_ingress(
    ClusterSecurityGroupName: str,
    CIDRIP: str = None,
    EC2SecurityGroupName: str = None,
    EC2SecurityGroupOwnerId: str = None,
) -> Dict[str, Any]:
```

### Client().authorize_snapshot_access

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L32)

```python
def authorize_snapshot_access(
    SnapshotIdentifier: str,
    AccountWithRestoreAccess: str,
    SnapshotClusterIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().batch_delete_cluster_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L41)

```python
def batch_delete_cluster_snapshots(Identifiers: List[Any]) -> Dict[str, Any]:
```

### Client().batch_modify_cluster_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L45)

```python
def batch_modify_cluster_snapshots(
    SnapshotIdentifierList: List[Any],
    ManualSnapshotRetentionPeriod: int = None,
    Force: bool = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L54)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_resize

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L58)

```python
def cancel_resize(ClusterIdentifier: str) -> Dict[str, Any]:
```

### Client().copy_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L62)

```python
def copy_cluster_snapshot(
    SourceSnapshotIdentifier: str,
    TargetSnapshotIdentifier: str,
    SourceSnapshotClusterIdentifier: str = None,
    ManualSnapshotRetentionPeriod: int = None,
) -> Dict[str, Any]:
```

### Client().create_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L72)

```python
def create_cluster(
    ClusterIdentifier: str,
    NodeType: str,
    MasterUsername: str,
    MasterUserPassword: str,
    DBName: str = None,
    ClusterType: str = None,
    ClusterSecurityGroups: List[Any] = None,
    VpcSecurityGroupIds: List[Any] = None,
    ClusterSubnetGroupName: str = None,
    AvailabilityZone: str = None,
    PreferredMaintenanceWindow: str = None,
    ClusterParameterGroupName: str = None,
    AutomatedSnapshotRetentionPeriod: int = None,
    ManualSnapshotRetentionPeriod: int = None,
    Port: int = None,
    ClusterVersion: str = None,
    AllowVersionUpgrade: bool = None,
    NumberOfNodes: int = None,
    PubliclyAccessible: bool = None,
    Encrypted: bool = None,
    HsmClientCertificateIdentifier: str = None,
    HsmConfigurationIdentifier: str = None,
    ElasticIp: str = None,
    Tags: List[Any] = None,
    KmsKeyId: str = None,
    EnhancedVpcRouting: bool = None,
    AdditionalInfo: str = None,
    IamRoles: List[Any] = None,
    MaintenanceTrackName: str = None,
    SnapshotScheduleIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().create_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L108)

```python
def create_cluster_parameter_group(
    ParameterGroupName: str,
    ParameterGroupFamily: str,
    Description: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_cluster_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L118)

```python
def create_cluster_security_group(
    ClusterSecurityGroupName: str,
    Description: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L124)

```python
def create_cluster_snapshot(
    SnapshotIdentifier: str,
    ClusterIdentifier: str,
    ManualSnapshotRetentionPeriod: int = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_cluster_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L134)

```python
def create_cluster_subnet_group(
    ClusterSubnetGroupName: str,
    Description: str,
    SubnetIds: List[Any],
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L144)

```python
def create_event_subscription(
    SubscriptionName: str,
    SnsTopicArn: str,
    SourceType: str = None,
    SourceIds: List[Any] = None,
    EventCategories: List[Any] = None,
    Severity: str = None,
    Enabled: bool = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_hsm_client_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L158)

```python
def create_hsm_client_certificate(
    HsmClientCertificateIdentifier: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_hsm_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L164)

```python
def create_hsm_configuration(
    HsmConfigurationIdentifier: str,
    Description: str,
    HsmIpAddress: str,
    HsmPartitionName: str,
    HsmPartitionPassword: str,
    HsmServerPublicCertificate: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_snapshot_copy_grant

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L177)

```python
def create_snapshot_copy_grant(
    SnapshotCopyGrantName: str,
    KmsKeyId: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_snapshot_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L183)

```python
def create_snapshot_schedule(
    ScheduleDefinitions: List[Any] = None,
    ScheduleIdentifier: str = None,
    ScheduleDescription: str = None,
    Tags: List[Any] = None,
    DryRun: bool = None,
    NextInvocations: int = None,
) -> Dict[str, Any]:
```

### Client().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L195)

```python
def create_tags(ResourceName: str, Tags: List[Any]) -> None:
```

### Client().delete_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L199)

```python
def delete_cluster(
    ClusterIdentifier: str,
    SkipFinalClusterSnapshot: bool = None,
    FinalClusterSnapshotIdentifier: str = None,
    FinalClusterSnapshotRetentionPeriod: int = None,
) -> Dict[str, Any]:
```

### Client().delete_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L209)

```python
def delete_cluster_parameter_group(ParameterGroupName: str) -> None:
```

### Client().delete_cluster_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L213)

```python
def delete_cluster_security_group(ClusterSecurityGroupName: str) -> None:
```

### Client().delete_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L217)

```python
def delete_cluster_snapshot(
    SnapshotIdentifier: str,
    SnapshotClusterIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().delete_cluster_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L223)

```python
def delete_cluster_subnet_group(ClusterSubnetGroupName: str) -> None:
```

### Client().delete_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L227)

```python
def delete_event_subscription(SubscriptionName: str) -> None:
```

### Client().delete_hsm_client_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L231)

```python
def delete_hsm_client_certificate(
    HsmClientCertificateIdentifier: str,
) -> None:
```

### Client().delete_hsm_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L237)

```python
def delete_hsm_configuration(HsmConfigurationIdentifier: str) -> None:
```

### Client().delete_snapshot_copy_grant

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L241)

```python
def delete_snapshot_copy_grant(SnapshotCopyGrantName: str) -> None:
```

### Client().delete_snapshot_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L245)

```python
def delete_snapshot_schedule(ScheduleIdentifier: str) -> None:
```

### Client().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L249)

```python
def delete_tags(ResourceName: str, TagKeys: List[Any]) -> None:
```

### Client().describe_account_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L253)

```python
def describe_account_attributes(
    AttributeNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_cluster_db_revisions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L259)

```python
def describe_cluster_db_revisions(
    ClusterIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_cluster_parameter_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L265)

```python
def describe_cluster_parameter_groups(
    ParameterGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_cluster_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L276)

```python
def describe_cluster_parameters(
    ParameterGroupName: str,
    Source: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_cluster_security_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L286)

```python
def describe_cluster_security_groups(
    ClusterSecurityGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_cluster_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L297)

```python
def describe_cluster_snapshots(
    ClusterIdentifier: str = None,
    SnapshotIdentifier: str = None,
    SnapshotType: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    MaxRecords: int = None,
    Marker: str = None,
    OwnerAccount: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    ClusterExists: bool = None,
    SortingEntities: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_cluster_subnet_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L315)

```python
def describe_cluster_subnet_groups(
    ClusterSubnetGroupName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_cluster_tracks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L326)

```python
def describe_cluster_tracks(
    MaintenanceTrackName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_cluster_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L335)

```python
def describe_cluster_versions(
    ClusterVersion: str = None,
    ClusterParameterGroupFamily: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_clusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L345)

```python
def describe_clusters(
    ClusterIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_default_cluster_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L356)

```python
def describe_default_cluster_parameters(
    ParameterGroupFamily: str,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_event_categories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L362)

```python
def describe_event_categories(SourceType: str = None) -> Dict[str, Any]:
```

### Client().describe_event_subscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L366)

```python
def describe_event_subscriptions(
    SubscriptionName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L377)

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

### Client().describe_hsm_client_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L390)

```python
def describe_hsm_client_certificates(
    HsmClientCertificateIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_hsm_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L401)

```python
def describe_hsm_configurations(
    HsmConfigurationIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_logging_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L412)

```python
def describe_logging_status(ClusterIdentifier: str) -> Dict[str, Any]:
```

### Client().describe_node_configuration_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L416)

```python
def describe_node_configuration_options(
    ActionType: str,
    SnapshotIdentifier: str = None,
    OwnerAccount: str = None,
    Filters: List[Any] = None,
    Marker: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_orderable_cluster_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L428)

```python
def describe_orderable_cluster_options(
    ClusterVersion: str = None,
    NodeType: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_node_offerings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L438)

```python
def describe_reserved_node_offerings(
    ReservedNodeOfferingId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_reserved_nodes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L447)

```python
def describe_reserved_nodes(
    ReservedNodeId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_resize

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L453)

```python
def describe_resize(ClusterIdentifier: str) -> Dict[str, Any]:
```

### Client().describe_snapshot_copy_grants

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L457)

```python
def describe_snapshot_copy_grants(
    SnapshotCopyGrantName: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_snapshot_schedules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L468)

```python
def describe_snapshot_schedules(
    ClusterIdentifier: str = None,
    ScheduleIdentifier: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    Marker: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_storage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L480)

```python
def describe_storage() -> Dict[str, Any]:
```

### Client().describe_table_restore_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L484)

```python
def describe_table_restore_status(
    ClusterIdentifier: str = None,
    TableRestoreRequestId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L494)

```python
def describe_tags(
    ResourceName: str = None,
    ResourceType: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().disable_logging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L506)

```python
def disable_logging(ClusterIdentifier: str) -> Dict[str, Any]:
```

### Client().disable_snapshot_copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L510)

```python
def disable_snapshot_copy(ClusterIdentifier: str) -> Dict[str, Any]:
```

### Client().enable_logging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L514)

```python
def enable_logging(
    ClusterIdentifier: str,
    BucketName: str,
    S3KeyPrefix: str = None,
) -> Dict[str, Any]:
```

### Client().enable_snapshot_copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L520)

```python
def enable_snapshot_copy(
    ClusterIdentifier: str,
    DestinationRegion: str,
    RetentionPeriod: int = None,
    SnapshotCopyGrantName: str = None,
    ManualSnapshotRetentionPeriod: int = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L531)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_cluster_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L541)

```python
def get_cluster_credentials(
    DbUser: str,
    ClusterIdentifier: str,
    DbName: str = None,
    DurationSeconds: int = None,
    AutoCreate: bool = None,
    DbGroups: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L553)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_reserved_node_exchange_offerings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L557)

```python
def get_reserved_node_exchange_offerings(
    ReservedNodeId: str,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L563)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().modify_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L567)

```python
def modify_cluster(
    ClusterIdentifier: str,
    ClusterType: str = None,
    NodeType: str = None,
    NumberOfNodes: int = None,
    ClusterSecurityGroups: List[Any] = None,
    VpcSecurityGroupIds: List[Any] = None,
    MasterUserPassword: str = None,
    ClusterParameterGroupName: str = None,
    AutomatedSnapshotRetentionPeriod: int = None,
    ManualSnapshotRetentionPeriod: int = None,
    PreferredMaintenanceWindow: str = None,
    ClusterVersion: str = None,
    AllowVersionUpgrade: bool = None,
    HsmClientCertificateIdentifier: str = None,
    HsmConfigurationIdentifier: str = None,
    NewClusterIdentifier: str = None,
    PubliclyAccessible: bool = None,
    ElasticIp: str = None,
    EnhancedVpcRouting: bool = None,
    MaintenanceTrackName: str = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
) -> Dict[str, Any]:
```

### Client().modify_cluster_db_revision

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L595)

```python
def modify_cluster_db_revision(
    ClusterIdentifier: str,
    RevisionTarget: str,
) -> Dict[str, Any]:
```

### Client().modify_cluster_iam_roles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L601)

```python
def modify_cluster_iam_roles(
    ClusterIdentifier: str,
    AddIamRoles: List[Any] = None,
    RemoveIamRoles: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_cluster_maintenance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L610)

```python
def modify_cluster_maintenance(
    ClusterIdentifier: str,
    DeferMaintenance: bool = None,
    DeferMaintenanceIdentifier: str = None,
    DeferMaintenanceStartTime: datetime = None,
    DeferMaintenanceEndTime: datetime = None,
    DeferMaintenanceDuration: int = None,
) -> Dict[str, Any]:
```

### Client().modify_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L622)

```python
def modify_cluster_parameter_group(
    ParameterGroupName: str,
    Parameters: List[Any],
) -> Dict[str, Any]:
```

### Client().modify_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L628)

```python
def modify_cluster_snapshot(
    SnapshotIdentifier: str,
    ManualSnapshotRetentionPeriod: int = None,
    Force: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_cluster_snapshot_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L637)

```python
def modify_cluster_snapshot_schedule(
    ClusterIdentifier: str,
    ScheduleIdentifier: str = None,
    DisassociateSchedule: bool = None,
) -> None:
```

### Client().modify_cluster_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L646)

```python
def modify_cluster_subnet_group(
    ClusterSubnetGroupName: str,
    SubnetIds: List[Any],
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().modify_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L652)

```python
def modify_event_subscription(
    SubscriptionName: str,
    SnsTopicArn: str = None,
    SourceType: str = None,
    SourceIds: List[Any] = None,
    EventCategories: List[Any] = None,
    Severity: str = None,
    Enabled: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_snapshot_copy_retention_period

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L665)

```python
def modify_snapshot_copy_retention_period(
    ClusterIdentifier: str,
    RetentionPeriod: int,
    Manual: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_snapshot_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L671)

```python
def modify_snapshot_schedule(
    ScheduleIdentifier: str,
    ScheduleDefinitions: List[Any],
) -> Dict[str, Any]:
```

### Client().purchase_reserved_node_offering

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L677)

```python
def purchase_reserved_node_offering(
    ReservedNodeOfferingId: str,
    NodeCount: int = None,
) -> Dict[str, Any]:
```

### Client().reboot_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L683)

```python
def reboot_cluster(ClusterIdentifier: str) -> Dict[str, Any]:
```

### Client().reset_cluster_parameter_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L687)

```python
def reset_cluster_parameter_group(
    ParameterGroupName: str,
    ResetAllParameters: bool = None,
    Parameters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().resize_cluster

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L696)

```python
def resize_cluster(
    ClusterIdentifier: str,
    NumberOfNodes: int,
    ClusterType: str = None,
    NodeType: str = None,
    Classic: bool = None,
) -> Dict[str, Any]:
```

### Client().restore_from_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L707)

```python
def restore_from_cluster_snapshot(
    ClusterIdentifier: str,
    SnapshotIdentifier: str,
    SnapshotClusterIdentifier: str = None,
    Port: int = None,
    AvailabilityZone: str = None,
    AllowVersionUpgrade: bool = None,
    ClusterSubnetGroupName: str = None,
    PubliclyAccessible: bool = None,
    OwnerAccount: str = None,
    HsmClientCertificateIdentifier: str = None,
    HsmConfigurationIdentifier: str = None,
    ElasticIp: str = None,
    ClusterParameterGroupName: str = None,
    ClusterSecurityGroups: List[Any] = None,
    VpcSecurityGroupIds: List[Any] = None,
    PreferredMaintenanceWindow: str = None,
    AutomatedSnapshotRetentionPeriod: int = None,
    ManualSnapshotRetentionPeriod: int = None,
    KmsKeyId: str = None,
    NodeType: str = None,
    EnhancedVpcRouting: bool = None,
    AdditionalInfo: str = None,
    IamRoles: List[Any] = None,
    MaintenanceTrackName: str = None,
    SnapshotScheduleIdentifier: str = None,
    NumberOfNodes: int = None,
) -> Dict[str, Any]:
```

### Client().restore_table_from_cluster_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L739)

```python
def restore_table_from_cluster_snapshot(
    ClusterIdentifier: str,
    SnapshotIdentifier: str,
    SourceDatabaseName: str,
    SourceTableName: str,
    NewTableName: str,
    SourceSchemaName: str = None,
    TargetDatabaseName: str = None,
    TargetSchemaName: str = None,
) -> Dict[str, Any]:
```

### Client().revoke_cluster_security_group_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L753)

```python
def revoke_cluster_security_group_ingress(
    ClusterSecurityGroupName: str,
    CIDRIP: str = None,
    EC2SecurityGroupName: str = None,
    EC2SecurityGroupOwnerId: str = None,
) -> Dict[str, Any]:
```

### Client().revoke_snapshot_access

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L763)

```python
def revoke_snapshot_access(
    SnapshotIdentifier: str,
    AccountWithRestoreAccess: str,
    SnapshotClusterIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().rotate_encryption_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/client.py#L772)

```python
def rotate_encryption_key(ClusterIdentifier: str) -> Dict[str, Any]:
```
