# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dynamodbstreams.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodbstreams/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dynamodbstreams](index.md#dynamodbstreams) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().describe_stream](#clientdescribe_stream)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_records](#clientget_records)
        - [Client().get_shard_iterator](#clientget_shard_iterator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_streams](#clientlist_streams)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodbstreams/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodbstreams/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().describe_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodbstreams/client.py#L18)

```python
def describe_stream(
    StreamArn: str,
    Limit: int = None,
    ExclusiveStartShardId: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodbstreams/client.py#L24)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodbstreams/client.py#L34)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodbstreams/client.py#L38)

```python
def get_records(ShardIterator: str, Limit: int = None) -> Dict[str, Any]:
```

### Client().get_shard_iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodbstreams/client.py#L42)

```python
def get_shard_iterator(
    StreamArn: str,
    ShardId: str,
    ShardIteratorType: str,
    SequenceNumber: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodbstreams/client.py#L52)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_streams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodbstreams/client.py#L56)

```python
def list_streams(
    TableName: str = None,
    Limit: int = None,
    ExclusiveStartStreamArn: str = None,
) -> Dict[str, Any]:
```
