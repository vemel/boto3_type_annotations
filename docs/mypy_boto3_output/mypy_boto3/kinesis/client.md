# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kinesis.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kinesis](index.md#kinesis) / Client
    - [Client](#client)
        - [Client().add_tags_to_stream](#clientadd_tags_to_stream)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_stream](#clientcreate_stream)
        - [Client().decrease_stream_retention_period](#clientdecrease_stream_retention_period)
        - [Client().delete_stream](#clientdelete_stream)
        - [Client().deregister_stream_consumer](#clientderegister_stream_consumer)
        - [Client().describe_limits](#clientdescribe_limits)
        - [Client().describe_stream](#clientdescribe_stream)
        - [Client().describe_stream_consumer](#clientdescribe_stream_consumer)
        - [Client().describe_stream_summary](#clientdescribe_stream_summary)
        - [Client().disable_enhanced_monitoring](#clientdisable_enhanced_monitoring)
        - [Client().enable_enhanced_monitoring](#clientenable_enhanced_monitoring)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_records](#clientget_records)
        - [Client().get_shard_iterator](#clientget_shard_iterator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().increase_stream_retention_period](#clientincrease_stream_retention_period)
        - [Client().list_shards](#clientlist_shards)
        - [Client().list_stream_consumers](#clientlist_stream_consumers)
        - [Client().list_streams](#clientlist_streams)
        - [Client().list_tags_for_stream](#clientlist_tags_for_stream)
        - [Client().merge_shards](#clientmerge_shards)
        - [Client().put_record](#clientput_record)
        - [Client().put_records](#clientput_records)
        - [Client().register_stream_consumer](#clientregister_stream_consumer)
        - [Client().remove_tags_from_stream](#clientremove_tags_from_stream)
        - [Client().split_shard](#clientsplit_shard)
        - [Client().start_stream_encryption](#clientstart_stream_encryption)
        - [Client().stop_stream_encryption](#clientstop_stream_encryption)
        - [Client().subscribe_to_shard](#clientsubscribe_to_shard)
        - [Client().update_shard_count](#clientupdate_shard_count)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_tags_to_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L16)

```python
def add_tags_to_stream(StreamName: str, Tags: Dict[str, Any]) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L20)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L24)

```python
def create_stream(StreamName: str, ShardCount: int) -> None:
```

### Client().decrease_stream_retention_period

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L28)

```python
def decrease_stream_retention_period(
    StreamName: str,
    RetentionPeriodHours: int,
) -> None:
```

### Client().delete_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L34)

```python
def delete_stream(
    StreamName: str,
    EnforceConsumerDeletion: bool = None,
) -> None:
```

### Client().deregister_stream_consumer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L40)

```python
def deregister_stream_consumer(
    StreamARN: str = None,
    ConsumerName: str = None,
    ConsumerARN: str = None,
) -> None:
```

### Client().describe_limits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L46)

```python
def describe_limits() -> Dict[str, Any]:
```

### Client().describe_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L50)

```python
def describe_stream(
    StreamName: str,
    Limit: int = None,
    ExclusiveStartShardId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_stream_consumer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L56)

```python
def describe_stream_consumer(
    StreamARN: str = None,
    ConsumerName: str = None,
    ConsumerARN: str = None,
) -> Dict[str, Any]:
```

### Client().describe_stream_summary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L62)

```python
def describe_stream_summary(StreamName: str) -> Dict[str, Any]:
```

### Client().disable_enhanced_monitoring

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L66)

```python
def disable_enhanced_monitoring(
    StreamName: str,
    ShardLevelMetrics: List[Any],
) -> Dict[str, Any]:
```

### Client().enable_enhanced_monitoring

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L72)

```python
def enable_enhanced_monitoring(
    StreamName: str,
    ShardLevelMetrics: List[Any],
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L78)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L88)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L92)

```python
def get_records(ShardIterator: str, Limit: int = None) -> Dict[str, Any]:
```

### Client().get_shard_iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L96)

```python
def get_shard_iterator(
    StreamName: str,
    ShardId: str,
    ShardIteratorType: str,
    StartingSequenceNumber: str = None,
    Timestamp: datetime = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L107)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().increase_stream_retention_period

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L111)

```python
def increase_stream_retention_period(
    StreamName: str,
    RetentionPeriodHours: int,
) -> None:
```

### Client().list_shards

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L117)

```python
def list_shards(
    StreamName: str = None,
    NextToken: str = None,
    ExclusiveStartShardId: str = None,
    MaxResults: int = None,
    StreamCreationTimestamp: datetime = None,
) -> Dict[str, Any]:
```

### Client().list_stream_consumers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L128)

```python
def list_stream_consumers(
    StreamARN: str,
    NextToken: str = None,
    MaxResults: int = None,
    StreamCreationTimestamp: datetime = None,
) -> Dict[str, Any]:
```

### Client().list_streams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L138)

```python
def list_streams(
    Limit: int = None,
    ExclusiveStartStreamName: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L144)

```python
def list_tags_for_stream(
    StreamName: str,
    ExclusiveStartTagKey: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().merge_shards

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L150)

```python
def merge_shards(
    StreamName: str,
    ShardToMerge: str,
    AdjacentShardToMerge: str,
) -> None:
```

### Client().put_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L156)

```python
def put_record(
    StreamName: str,
    Data: bytes,
    PartitionKey: str,
    ExplicitHashKey: str = None,
    SequenceNumberForOrdering: str = None,
) -> Dict[str, Any]:
```

### Client().put_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L167)

```python
def put_records(Records: List[Any], StreamName: str) -> Dict[str, Any]:
```

### Client().register_stream_consumer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L171)

```python
def register_stream_consumer(
    StreamARN: str,
    ConsumerName: str,
) -> Dict[str, Any]:
```

### Client().remove_tags_from_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L177)

```python
def remove_tags_from_stream(StreamName: str, TagKeys: List[Any]) -> None:
```

### Client().split_shard

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L181)

```python
def split_shard(
    StreamName: str,
    ShardToSplit: str,
    NewStartingHashKey: str,
) -> None:
```

### Client().start_stream_encryption

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L187)

```python
def start_stream_encryption(
    StreamName: str,
    EncryptionType: str,
    KeyId: str,
) -> None:
```

### Client().stop_stream_encryption

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L193)

```python
def stop_stream_encryption(
    StreamName: str,
    EncryptionType: str,
    KeyId: str,
) -> None:
```

### Client().subscribe_to_shard

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L199)

```python
def subscribe_to_shard(
    ConsumerARN: str,
    ShardId: str,
    StartingPosition: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_shard_count

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/client.py#L205)

```python
def update_shard_count(
    StreamName: str,
    TargetShardCount: int,
    ScalingType: str,
) -> Dict[str, Any]:
```
