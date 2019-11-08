# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dynamodb.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dynamodb](index.md#dynamodb) / Paginator
    - [ListBackups](#listbackups)
        - [ListBackups().paginate](#listbackupspaginate)
    - [ListTables](#listtables)
        - [ListTables().paginate](#listtablespaginate)
    - [ListTagsOfResource](#listtagsofresource)
        - [ListTagsOfResource().paginate](#listtagsofresourcepaginate)
    - [Query](#query)
        - [Query().paginate](#querypaginate)
    - [Scan](#scan)
        - [Scan().paginate](#scanpaginate)

## ListBackups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py#L11)

```python
class ListBackups(Paginator):
```

### ListBackups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py#L14)

```python
def paginate(
    TableName: str = None,
    TimeRangeLowerBound: datetime = None,
    TimeRangeUpperBound: datetime = None,
    BackupType: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py#L25)

```python
class ListTables(Paginator):
```

### ListTables().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py#L28)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListTagsOfResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py#L32)

```python
class ListTagsOfResource(Paginator):
```

### ListTagsOfResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py#L35)

```python
def paginate(
    ResourceArn: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## Query

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py#L41)

```python
class Query(Paginator):
```

### Query().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py#L44)

```python
def paginate(
    TableName: str,
    IndexName: str = None,
    Select: str = None,
    AttributesToGet: List[Any] = None,
    ConsistentRead: bool = None,
    KeyConditions: Dict[str, Any] = None,
    QueryFilter: Dict[str, Any] = None,
    ConditionalOperator: str = None,
    ScanIndexForward: bool = None,
    ReturnConsumedCapacity: str = None,
    ProjectionExpression: str = None,
    FilterExpression: str = None,
    KeyConditionExpression: str = None,
    ExpressionAttributeNames: Dict[str, Any] = None,
    ExpressionAttributeValues: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## Scan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py#L66)

```python
class Scan(Paginator):
```

### Scan().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/paginator.py#L69)

```python
def paginate(
    TableName: str,
    IndexName: str = None,
    AttributesToGet: List[Any] = None,
    Select: str = None,
    ScanFilter: Dict[str, Any] = None,
    ConditionalOperator: str = None,
    ReturnConsumedCapacity: str = None,
    TotalSegments: int = None,
    Segment: int = None,
    ProjectionExpression: str = None,
    FilterExpression: str = None,
    ExpressionAttributeNames: Dict[str, Any] = None,
    ExpressionAttributeValues: Dict[str, Any] = None,
    ConsistentRead: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
