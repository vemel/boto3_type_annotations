# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dms.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dms](index.md#dms) / Client
    - [Client](#client)
        - [Client().add_tags_to_resource](#clientadd_tags_to_resource)
        - [Client().apply_pending_maintenance_action](#clientapply_pending_maintenance_action)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_endpoint](#clientcreate_endpoint)
        - [Client().create_event_subscription](#clientcreate_event_subscription)
        - [Client().create_replication_instance](#clientcreate_replication_instance)
        - [Client().create_replication_subnet_group](#clientcreate_replication_subnet_group)
        - [Client().create_replication_task](#clientcreate_replication_task)
        - [Client().delete_certificate](#clientdelete_certificate)
        - [Client().delete_connection](#clientdelete_connection)
        - [Client().delete_endpoint](#clientdelete_endpoint)
        - [Client().delete_event_subscription](#clientdelete_event_subscription)
        - [Client().delete_replication_instance](#clientdelete_replication_instance)
        - [Client().delete_replication_subnet_group](#clientdelete_replication_subnet_group)
        - [Client().delete_replication_task](#clientdelete_replication_task)
        - [Client().describe_account_attributes](#clientdescribe_account_attributes)
        - [Client().describe_certificates](#clientdescribe_certificates)
        - [Client().describe_connections](#clientdescribe_connections)
        - [Client().describe_endpoint_types](#clientdescribe_endpoint_types)
        - [Client().describe_endpoints](#clientdescribe_endpoints)
        - [Client().describe_event_categories](#clientdescribe_event_categories)
        - [Client().describe_event_subscriptions](#clientdescribe_event_subscriptions)
        - [Client().describe_events](#clientdescribe_events)
        - [Client().describe_orderable_replication_instances](#clientdescribe_orderable_replication_instances)
        - [Client().describe_pending_maintenance_actions](#clientdescribe_pending_maintenance_actions)
        - [Client().describe_refresh_schemas_status](#clientdescribe_refresh_schemas_status)
        - [Client().describe_replication_instance_task_logs](#clientdescribe_replication_instance_task_logs)
        - [Client().describe_replication_instances](#clientdescribe_replication_instances)
        - [Client().describe_replication_subnet_groups](#clientdescribe_replication_subnet_groups)
        - [Client().describe_replication_task_assessment_results](#clientdescribe_replication_task_assessment_results)
        - [Client().describe_replication_tasks](#clientdescribe_replication_tasks)
        - [Client().describe_schemas](#clientdescribe_schemas)
        - [Client().describe_table_statistics](#clientdescribe_table_statistics)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_certificate](#clientimport_certificate)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().modify_endpoint](#clientmodify_endpoint)
        - [Client().modify_event_subscription](#clientmodify_event_subscription)
        - [Client().modify_replication_instance](#clientmodify_replication_instance)
        - [Client().modify_replication_subnet_group](#clientmodify_replication_subnet_group)
        - [Client().modify_replication_task](#clientmodify_replication_task)
        - [Client().reboot_replication_instance](#clientreboot_replication_instance)
        - [Client().refresh_schemas](#clientrefresh_schemas)
        - [Client().reload_tables](#clientreload_tables)
        - [Client().remove_tags_from_resource](#clientremove_tags_from_resource)
        - [Client().start_replication_task](#clientstart_replication_task)
        - [Client().start_replication_task_assessment](#clientstart_replication_task_assessment)
        - [Client().stop_replication_task](#clientstop_replication_task)
        - [Client().test_connection](#clienttest_connection)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_tags_to_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L16)

```python
def add_tags_to_resource(ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().apply_pending_maintenance_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L20)

```python
def apply_pending_maintenance_action(
    ReplicationInstanceArn: str,
    ApplyAction: str,
    OptInType: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L26)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L30)

```python
def create_endpoint(
    EndpointIdentifier: str,
    EndpointType: str,
    EngineName: str,
    Username: str = None,
    Password: str = None,
    ServerName: str = None,
    Port: int = None,
    DatabaseName: str = None,
    ExtraConnectionAttributes: str = None,
    KmsKeyId: str = None,
    Tags: List[Any] = None,
    CertificateArn: str = None,
    SslMode: str = None,
    ServiceAccessRoleArn: str = None,
    ExternalTableDefinition: str = None,
    DynamoDbSettings: Dict[str, Any] = None,
    S3Settings: Dict[str, Any] = None,
    DmsTransferSettings: Dict[str, Any] = None,
    MongoDbSettings: Dict[str, Any] = None,
    KinesisSettings: Dict[str, Any] = None,
    ElasticsearchSettings: Dict[str, Any] = None,
    RedshiftSettings: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L58)

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

### Client().create_replication_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L71)

```python
def create_replication_instance(
    ReplicationInstanceIdentifier: str,
    ReplicationInstanceClass: str,
    AllocatedStorage: int = None,
    VpcSecurityGroupIds: List[Any] = None,
    AvailabilityZone: str = None,
    ReplicationSubnetGroupIdentifier: str = None,
    PreferredMaintenanceWindow: str = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AutoMinorVersionUpgrade: bool = None,
    Tags: List[Any] = None,
    KmsKeyId: str = None,
    PubliclyAccessible: bool = None,
    DnsNameServers: str = None,
) -> Dict[str, Any]:
```

### Client().create_replication_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L91)

```python
def create_replication_subnet_group(
    ReplicationSubnetGroupIdentifier: str,
    ReplicationSubnetGroupDescription: str,
    SubnetIds: List[Any],
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_replication_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L101)

```python
def create_replication_task(
    ReplicationTaskIdentifier: str,
    SourceEndpointArn: str,
    TargetEndpointArn: str,
    ReplicationInstanceArn: str,
    MigrationType: str,
    TableMappings: str,
    ReplicationTaskSettings: str = None,
    CdcStartTime: datetime = None,
    CdcStartPosition: str = None,
    CdcStopPosition: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L118)

```python
def delete_certificate(CertificateArn: str) -> Dict[str, Any]:
```

### Client().delete_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L122)

```python
def delete_connection(
    EndpointArn: str,
    ReplicationInstanceArn: str,
) -> Dict[str, Any]:
```

### Client().delete_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L128)

```python
def delete_endpoint(EndpointArn: str) -> Dict[str, Any]:
```

### Client().delete_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L132)

```python
def delete_event_subscription(SubscriptionName: str) -> Dict[str, Any]:
```

### Client().delete_replication_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L136)

```python
def delete_replication_instance(
    ReplicationInstanceArn: str,
) -> Dict[str, Any]:
```

### Client().delete_replication_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L142)

```python
def delete_replication_subnet_group(
    ReplicationSubnetGroupIdentifier: str,
) -> Dict[str, Any]:
```

### Client().delete_replication_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L148)

```python
def delete_replication_task(ReplicationTaskArn: str) -> Dict[str, Any]:
```

### Client().describe_account_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L152)

```python
def describe_account_attributes() -> Dict[str, Any]:
```

### Client().describe_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L156)

```python
def describe_certificates(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L162)

```python
def describe_connections(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_endpoint_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L168)

```python
def describe_endpoint_types(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L174)

```python
def describe_endpoints(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_event_categories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L180)

```python
def describe_event_categories(
    SourceType: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_event_subscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L186)

```python
def describe_event_subscriptions(
    SubscriptionName: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L196)

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

### Client().describe_orderable_replication_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L211)

```python
def describe_orderable_replication_instances(
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_pending_maintenance_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L217)

```python
def describe_pending_maintenance_actions(
    ReplicationInstanceArn: str = None,
    Filters: List[Any] = None,
    Marker: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_refresh_schemas_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L227)

```python
def describe_refresh_schemas_status(EndpointArn: str) -> Dict[str, Any]:
```

### Client().describe_replication_instance_task_logs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L231)

```python
def describe_replication_instance_task_logs(
    ReplicationInstanceArn: str,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_replication_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L237)

```python
def describe_replication_instances(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_replication_subnet_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L243)

```python
def describe_replication_subnet_groups(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_replication_task_assessment_results

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L249)

```python
def describe_replication_task_assessment_results(
    ReplicationTaskArn: str = None,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_replication_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L255)

```python
def describe_replication_tasks(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WithoutSettings: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_schemas

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L265)

```python
def describe_schemas(
    EndpointArn: str,
    MaxRecords: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_table_statistics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L271)

```python
def describe_table_statistics(
    ReplicationTaskArn: str,
    MaxRecords: int = None,
    Marker: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L281)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L291)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L295)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L299)

```python
def import_certificate(
    CertificateIdentifier: str,
    CertificatePem: str = None,
    CertificateWallet: bytes = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L309)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().modify_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L313)

```python
def modify_endpoint(
    EndpointArn: str,
    EndpointIdentifier: str = None,
    EndpointType: str = None,
    EngineName: str = None,
    Username: str = None,
    Password: str = None,
    ServerName: str = None,
    Port: int = None,
    DatabaseName: str = None,
    ExtraConnectionAttributes: str = None,
    CertificateArn: str = None,
    SslMode: str = None,
    ServiceAccessRoleArn: str = None,
    ExternalTableDefinition: str = None,
    DynamoDbSettings: Dict[str, Any] = None,
    S3Settings: Dict[str, Any] = None,
    DmsTransferSettings: Dict[str, Any] = None,
    MongoDbSettings: Dict[str, Any] = None,
    KinesisSettings: Dict[str, Any] = None,
    ElasticsearchSettings: Dict[str, Any] = None,
    RedshiftSettings: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().modify_event_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L340)

```python
def modify_event_subscription(
    SubscriptionName: str,
    SnsTopicArn: str = None,
    SourceType: str = None,
    EventCategories: List[Any] = None,
    Enabled: bool = None,
) -> Dict[str, Any]:
```

### Client().modify_replication_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L351)

```python
def modify_replication_instance(
    ReplicationInstanceArn: str,
    AllocatedStorage: int = None,
    ApplyImmediately: bool = None,
    ReplicationInstanceClass: str = None,
    VpcSecurityGroupIds: List[Any] = None,
    PreferredMaintenanceWindow: str = None,
    MultiAZ: bool = None,
    EngineVersion: str = None,
    AllowMajorVersionUpgrade: bool = None,
    AutoMinorVersionUpgrade: bool = None,
    ReplicationInstanceIdentifier: str = None,
) -> Dict[str, Any]:
```

### Client().modify_replication_subnet_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L368)

```python
def modify_replication_subnet_group(
    ReplicationSubnetGroupIdentifier: str,
    SubnetIds: List[Any],
    ReplicationSubnetGroupDescription: str = None,
) -> Dict[str, Any]:
```

### Client().modify_replication_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L377)

```python
def modify_replication_task(
    ReplicationTaskArn: str,
    ReplicationTaskIdentifier: str = None,
    MigrationType: str = None,
    TableMappings: str = None,
    ReplicationTaskSettings: str = None,
    CdcStartTime: datetime = None,
    CdcStartPosition: str = None,
    CdcStopPosition: str = None,
) -> Dict[str, Any]:
```

### Client().reboot_replication_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L391)

```python
def reboot_replication_instance(
    ReplicationInstanceArn: str,
    ForceFailover: bool = None,
) -> Dict[str, Any]:
```

### Client().refresh_schemas

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L397)

```python
def refresh_schemas(
    EndpointArn: str,
    ReplicationInstanceArn: str,
) -> Dict[str, Any]:
```

### Client().reload_tables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L403)

```python
def reload_tables(
    ReplicationTaskArn: str,
    TablesToReload: List[Any],
    ReloadOption: str = None,
) -> Dict[str, Any]:
```

### Client().remove_tags_from_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L412)

```python
def remove_tags_from_resource(
    ResourceArn: str,
    TagKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().start_replication_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L418)

```python
def start_replication_task(
    ReplicationTaskArn: str,
    StartReplicationTaskType: str,
    CdcStartTime: datetime = None,
    CdcStartPosition: str = None,
    CdcStopPosition: str = None,
) -> Dict[str, Any]:
```

### Client().start_replication_task_assessment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L429)

```python
def start_replication_task_assessment(
    ReplicationTaskArn: str,
) -> Dict[str, Any]:
```

### Client().stop_replication_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L435)

```python
def stop_replication_task(ReplicationTaskArn: str) -> Dict[str, Any]:
```

### Client().test_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/client.py#L439)

```python
def test_connection(
    ReplicationInstanceArn: str,
    EndpointArn: str,
) -> Dict[str, Any]:
```
