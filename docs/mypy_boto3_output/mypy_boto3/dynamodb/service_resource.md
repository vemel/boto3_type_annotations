# ServiceResource

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dynamodb.service_resource](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dynamodb](index.md#dynamodb) / ServiceResource
    - [ServiceResource](#serviceresource)
        - [ServiceResource().Table](#serviceresourcetable)
        - [ServiceResource().batch_get_item](#serviceresourcebatch_get_item)
        - [ServiceResource().batch_write_item](#serviceresourcebatch_write_item)
        - [ServiceResource().create_table](#serviceresourcecreate_table)
        - [ServiceResource().get_available_subresources](#serviceresourceget_available_subresources)
    - [Table](#table)
        - [Table().batch_writer](#tablebatch_writer)
        - [Table().delete](#tabledelete)
        - [Table().delete_item](#tabledelete_item)
        - [Table().get_available_subresources](#tableget_available_subresources)
        - [Table().get_item](#tableget_item)
        - [Table().load](#tableload)
        - [Table().put_item](#tableput_item)
        - [Table().query](#tablequery)
        - [Table().reload](#tablereload)
        - [Table().scan](#tablescan)
        - [Table().update](#tableupdate)
        - [Table().update_item](#tableupdate_item)
        - [Table().wait_until_exists](#tablewait_until_exists)
        - [Table().wait_until_not_exists](#tablewait_until_not_exists)
    - [tables](#tables)
        - [tables.all](#tablesall)
        - [tables.filter](#tablesfilter)
        - [tables.iterator](#tablesiterator)
        - [tables.limit](#tableslimit)
        - [tables.page_size](#tablespage_size)
        - [tables.pages](#tablespages)

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L15)

```python
class ServiceResource(Boto3ServiceResource):
```

### ServiceResource().Table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L19)

```python
def Table(name: str = None) -> dynamodb_service_resource_scope.Table:
```

### ServiceResource().batch_get_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L23)

```python
def batch_get_item(
    RequestItems: Dict[str, Any],
    ReturnConsumedCapacity: str = None,
) -> Dict[str, Any]:
```

### ServiceResource().batch_write_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L29)

```python
def batch_write_item(
    RequestItems: Dict[str, Any],
    ReturnConsumedCapacity: str = None,
    ReturnItemCollectionMetrics: str = None,
) -> Dict[str, Any]:
```

### ServiceResource().create_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L38)

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
) -> dynamodb_service_resource_scope.Table:
```

### ServiceResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L54)

```python
def get_available_subresources() -> List[str]:
```

## Table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L58)

```python
class Table(Boto3ServiceResource):
```

### Table().batch_writer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L80)

```python
def batch_writer(overwrite_by_pkeys: List[str] = None) -> None:
```

### Table().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L84)

```python
def delete() -> Dict[str, Any]:
```

### Table().delete_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L88)

```python
def delete_item(
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

### Table().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L103)

```python
def get_available_subresources() -> List[str]:
```

### Table().get_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L107)

```python
def get_item(
    Key: Dict[str, Any],
    AttributesToGet: List[Any] = None,
    ConsistentRead: bool = None,
    ReturnConsumedCapacity: str = None,
    ProjectionExpression: str = None,
    ExpressionAttributeNames: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Table().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L119)

```python
def load() -> None:
```

### Table().put_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L123)

```python
def put_item(
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

### Table().query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L138)

```python
def query(
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

### Table().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L160)

```python
def reload() -> None:
```

### Table().scan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L164)

```python
def scan(
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

### Table().update

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L185)

```python
def update(
    AttributeDefinitions: List[Any] = None,
    BillingMode: str = None,
    ProvisionedThroughput: Dict[str, Any] = None,
    GlobalSecondaryIndexUpdates: List[Any] = None,
    StreamSpecification: Dict[str, Any] = None,
    SSESpecification: Dict[str, Any] = None,
) -> dynamodb_service_resource_scope.Table:
```

### Table().update_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L197)

```python
def update_item(
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

### Table().wait_until_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L214)

```python
def wait_until_exists() -> None:
```

### Table().wait_until_not_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L218)

```python
def wait_until_not_exists() -> None:
```

## tables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L222)

```python
class tables(ResourceCollection):
```

### tables.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L223)

```python
@classmethod
def all() -> List[dynamodb_service_resource_scope.Table]:
```

### tables.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L228)

```python
@classmethod
def filter(
    ExclusiveStartTableName: str = None,
    Limit: int = None,
) -> List[dynamodb_service_resource_scope.Table]:
```

### tables.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L235)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### tables.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L240)

```python
@classmethod
def limit(count: int = None) -> List[dynamodb_service_resource_scope.Table]:
```

### tables.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L245)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[dynamodb_service_resource_scope.Table]:
```

### tables.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/service_resource.py#L252)

```python
@classmethod
def pages() -> List[ServiceResource]:
```
