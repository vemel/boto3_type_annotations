# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dynamodb.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dynamodb](index.md#dynamodb) / Client
    - [Client](#client)
        - [Client().batch_get_item](#clientbatch_get_item)
        - [Client().batch_write_item](#clientbatch_write_item)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_backup](#clientcreate_backup)
        - [Client().create_global_table](#clientcreate_global_table)
        - [Client().create_table](#clientcreate_table)
        - [Client().delete_backup](#clientdelete_backup)
        - [Client().delete_item](#clientdelete_item)
        - [Client().delete_table](#clientdelete_table)
        - [Client().describe_backup](#clientdescribe_backup)
        - [Client().describe_continuous_backups](#clientdescribe_continuous_backups)
        - [Client().describe_endpoints](#clientdescribe_endpoints)
        - [Client().describe_global_table](#clientdescribe_global_table)
        - [Client().describe_global_table_settings](#clientdescribe_global_table_settings)
        - [Client().describe_limits](#clientdescribe_limits)
        - [Client().describe_table](#clientdescribe_table)
        - [Client().describe_time_to_live](#clientdescribe_time_to_live)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_item](#clientget_item)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_backups](#clientlist_backups)
        - [Client().list_global_tables](#clientlist_global_tables)
        - [Client().list_tables](#clientlist_tables)
        - [Client().list_tags_of_resource](#clientlist_tags_of_resource)
        - [Client().put_item](#clientput_item)
        - [Client().query](#clientquery)
        - [Client().restore_table_from_backup](#clientrestore_table_from_backup)
        - [Client().restore_table_to_point_in_time](#clientrestore_table_to_point_in_time)
        - [Client().scan](#clientscan)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().transact_get_items](#clienttransact_get_items)
        - [Client().transact_write_items](#clienttransact_write_items)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_continuous_backups](#clientupdate_continuous_backups)
        - [Client().update_global_table](#clientupdate_global_table)
        - [Client().update_global_table_settings](#clientupdate_global_table_settings)
        - [Client().update_item](#clientupdate_item)
        - [Client().update_table](#clientupdate_table)
        - [Client().update_time_to_live](#clientupdate_time_to_live)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L13)

```python
class Client(BaseClient):
```

### Client().batch_get_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L16)

```python
def batch_get_item(
    RequestItems: Dict[str, Any],
    ReturnConsumedCapacity: str = None,
) -> Dict[str, Any]:
```

### Client().batch_write_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L22)

```python
def batch_write_item(
    RequestItems: Dict[str, Any],
    ReturnConsumedCapacity: str = None,
    ReturnItemCollectionMetrics: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L31)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L35)

```python
def create_backup(TableName: str, BackupName: str) -> Dict[str, Any]:
```

### Client().create_global_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L39)

```python
def create_global_table(
    GlobalTableName: str,
    ReplicationGroup: List[Any],
) -> Dict[str, Any]:
```

### Client().create_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L45)

```python
def create_table(
    AttributeDefinitions: List[Any],
    TableName: str,
    KeySchema: List[Any],
    LocalSecondaryIndexes: List[Any] = None,
    GlobalSecondaryIndexes: List[Any] = None,
    BillingMode: str = None,
    ProvisionedThroughput: Dict[str, Any] = None,
    StreamSpecification: Dict[str, Any] = None,
    SSESpecification: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L61)

```python
def delete_backup(BackupArn: str) -> Dict[str, Any]:
```

### Client().delete_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L65)

```python
def delete_item(
    TableName: str,
    Key: Dict[str, Any],
    Expected: Dict[str, Any] = None,
    ConditionalOperator: str = None,
    ReturnValues: str = None,
    ReturnConsumedCapacity: str = None,
    ReturnItemCollectionMetrics: str = None,
    ConditionExpression: str = None,
    ExpressionAttributeNames: Dict[str, Any] = None,
    ExpressionAttributeValues: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L81)

```python
def delete_table(TableName: str) -> Dict[str, Any]:
```

### Client().describe_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L85)

```python
def describe_backup(BackupArn: str) -> Dict[str, Any]:
```

### Client().describe_continuous_backups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L89)

```python
def describe_continuous_backups(TableName: str) -> Dict[str, Any]:
```

### Client().describe_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L93)

```python
def describe_endpoints() -> Dict[str, Any]:
```

### Client().describe_global_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L97)

```python
def describe_global_table(GlobalTableName: str) -> Dict[str, Any]:
```

### Client().describe_global_table_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L101)

```python
def describe_global_table_settings(GlobalTableName: str) -> Dict[str, Any]:
```

### Client().describe_limits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L105)

```python
def describe_limits() -> Dict[str, Any]:
```

### Client().describe_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L109)

```python
def describe_table(TableName: str) -> Dict[str, Any]:
```

### Client().describe_time_to_live

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L113)

```python
def describe_time_to_live(TableName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L117)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L127)

```python
def get_item(
    TableName: str,
    Key: Dict[str, Any],
    AttributesToGet: List[Any] = None,
    ConsistentRead: bool = None,
    ReturnConsumedCapacity: str = None,
    ProjectionExpression: str = None,
    ExpressionAttributeNames: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L140)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L144)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_backups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L148)

```python
def list_backups(
    TableName: str = None,
    Limit: int = None,
    TimeRangeLowerBound: datetime = None,
    TimeRangeUpperBound: datetime = None,
    ExclusiveStartBackupArn: str = None,
    BackupType: str = None,
) -> Dict[str, Any]:
```

### Client().list_global_tables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L160)

```python
def list_global_tables(
    ExclusiveStartGlobalTableName: str = None,
    Limit: int = None,
    RegionName: str = None,
) -> Dict[str, Any]:
```

### Client().list_tables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L169)

```python
def list_tables(
    ExclusiveStartTableName: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_of_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L175)

```python
def list_tags_of_resource(
    ResourceArn: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L181)

```python
def put_item(
    TableName: str,
    Item: Dict[str, Any],
    Expected: Dict[str, Any] = None,
    ReturnValues: str = None,
    ReturnConsumedCapacity: str = None,
    ReturnItemCollectionMetrics: str = None,
    ConditionalOperator: str = None,
    ConditionExpression: str = None,
    ExpressionAttributeNames: Dict[str, Any] = None,
    ExpressionAttributeValues: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L197)

```python
def query(
    TableName: str,
    IndexName: str = None,
    Select: str = None,
    AttributesToGet: List[Any] = None,
    Limit: int = None,
    ConsistentRead: bool = None,
    KeyConditions: Dict[str, Any] = None,
    QueryFilter: Dict[str, Any] = None,
    ConditionalOperator: str = None,
    ScanIndexForward: bool = None,
    ExclusiveStartKey: Dict[str, Any] = None,
    ReturnConsumedCapacity: str = None,
    ProjectionExpression: str = None,
    FilterExpression: str = None,
    KeyConditionExpression: str = None,
    ExpressionAttributeNames: Dict[str, Any] = None,
    ExpressionAttributeValues: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().restore_table_from_backup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L220)

```python
def restore_table_from_backup(
    TargetTableName: str,
    BackupArn: str,
) -> Dict[str, Any]:
```

### Client().restore_table_to_point_in_time

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L226)

```python
def restore_table_to_point_in_time(
    SourceTableName: str,
    TargetTableName: str,
    UseLatestRestorableTime: bool = None,
    RestoreDateTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().scan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L236)

```python
def scan(
    TableName: str,
    IndexName: str = None,
    AttributesToGet: List[Any] = None,
    Limit: int = None,
    Select: str = None,
    ScanFilter: Dict[str, Any] = None,
    ConditionalOperator: str = None,
    ExclusiveStartKey: Dict[str, Any] = None,
    ReturnConsumedCapacity: str = None,
    TotalSegments: int = None,
    Segment: int = None,
    ProjectionExpression: str = None,
    FilterExpression: str = None,
    ExpressionAttributeNames: Dict[str, Any] = None,
    ExpressionAttributeValues: Dict[str, Any] = None,
    ConsistentRead: bool = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L258)

```python
def tag_resource(ResourceArn: str, Tags: List[Any]) -> None:
```

### Client().transact_get_items

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L262)

```python
def transact_get_items(
    TransactItems: List[Any],
    ReturnConsumedCapacity: str = None,
) -> Dict[str, Any]:
```

### Client().transact_write_items

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L268)

```python
def transact_write_items(
    TransactItems: List[Any],
    ReturnConsumedCapacity: str = None,
    ReturnItemCollectionMetrics: str = None,
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L278)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> None:
```

### Client().update_continuous_backups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L282)

```python
def update_continuous_backups(
    TableName: str,
    PointInTimeRecoverySpecification: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_global_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L288)

```python
def update_global_table(
    GlobalTableName: str,
    ReplicaUpdates: List[Any],
) -> Dict[str, Any]:
```

### Client().update_global_table_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L294)

```python
def update_global_table_settings(
    GlobalTableName: str,
    GlobalTableBillingMode: str = None,
    GlobalTableProvisionedWriteCapacityUnits: int = None,
    GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: Dict[str, Any] = None,
    GlobalTableGlobalSecondaryIndexSettingsUpdate: List[Any] = None,
    ReplicaSettingsUpdate: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L308)

```python
def update_item(
    TableName: str,
    Key: Dict[str, Any],
    AttributeUpdates: Dict[str, Any] = None,
    Expected: Dict[str, Any] = None,
    ConditionalOperator: str = None,
    ReturnValues: str = None,
    ReturnConsumedCapacity: str = None,
    ReturnItemCollectionMetrics: str = None,
    UpdateExpression: str = None,
    ConditionExpression: str = None,
    ExpressionAttributeNames: Dict[str, Any] = None,
    ExpressionAttributeValues: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L326)

```python
def update_table(
    TableName: str,
    AttributeDefinitions: List[Any] = None,
    BillingMode: str = None,
    ProvisionedThroughput: Dict[str, Any] = None,
    GlobalSecondaryIndexUpdates: List[Any] = None,
    StreamSpecification: Dict[str, Any] = None,
    SSESpecification: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_time_to_live

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/client.py#L339)

```python
def update_time_to_live(
    TableName: str,
    TimeToLiveSpecification: Dict[str, Any],
) -> Dict[str, Any]:
```
