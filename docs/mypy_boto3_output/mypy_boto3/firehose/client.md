# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.firehose.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Firehose](index.md#firehose) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_delivery_stream](#clientcreate_delivery_stream)
        - [Client().delete_delivery_stream](#clientdelete_delivery_stream)
        - [Client().describe_delivery_stream](#clientdescribe_delivery_stream)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_delivery_streams](#clientlist_delivery_streams)
        - [Client().list_tags_for_delivery_stream](#clientlist_tags_for_delivery_stream)
        - [Client().put_record](#clientput_record)
        - [Client().put_record_batch](#clientput_record_batch)
        - [Client().start_delivery_stream_encryption](#clientstart_delivery_stream_encryption)
        - [Client().stop_delivery_stream_encryption](#clientstop_delivery_stream_encryption)
        - [Client().tag_delivery_stream](#clienttag_delivery_stream)
        - [Client().untag_delivery_stream](#clientuntag_delivery_stream)
        - [Client().update_destination](#clientupdate_destination)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_delivery_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L19)

```python
def create_delivery_stream(
    DeliveryStreamName: str,
    DeliveryStreamType: str = None,
    KinesisStreamSourceConfiguration: Dict[str, Any] = None,
    S3DestinationConfiguration: Dict[str, Any] = None,
    ExtendedS3DestinationConfiguration: Dict[str, Any] = None,
    RedshiftDestinationConfiguration: Dict[str, Any] = None,
    ElasticsearchDestinationConfiguration: Dict[str, Any] = None,
    SplunkDestinationConfiguration: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_delivery_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L34)

```python
def delete_delivery_stream(DeliveryStreamName: str) -> Dict[str, Any]:
```

### Client().describe_delivery_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L38)

```python
def describe_delivery_stream(
    DeliveryStreamName: str,
    Limit: int = None,
    ExclusiveStartDestinationId: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L47)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L57)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L61)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_delivery_streams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L65)

```python
def list_delivery_streams(
    Limit: int = None,
    DeliveryStreamType: str = None,
    ExclusiveStartDeliveryStreamName: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_delivery_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L74)

```python
def list_tags_for_delivery_stream(
    DeliveryStreamName: str,
    ExclusiveStartTagKey: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().put_record

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L83)

```python
def put_record(
    DeliveryStreamName: str,
    Record: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().put_record_batch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L89)

```python
def put_record_batch(
    DeliveryStreamName: str,
    Records: List[Any],
) -> Dict[str, Any]:
```

### Client().start_delivery_stream_encryption

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L95)

```python
def start_delivery_stream_encryption(
    DeliveryStreamName: str,
) -> Dict[str, Any]:
```

### Client().stop_delivery_stream_encryption

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L101)

```python
def stop_delivery_stream_encryption(
    DeliveryStreamName: str,
) -> Dict[str, Any]:
```

### Client().tag_delivery_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L107)

```python
def tag_delivery_stream(
    DeliveryStreamName: str,
    Tags: List[Any],
) -> Dict[str, Any]:
```

### Client().untag_delivery_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L113)

```python
def untag_delivery_stream(
    DeliveryStreamName: str,
    TagKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().update_destination

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/firehose/client.py#L119)

```python
def update_destination(
    DeliveryStreamName: str,
    CurrentDeliveryStreamVersionId: str,
    DestinationId: str,
    S3DestinationUpdate: Dict[str, Any] = None,
    ExtendedS3DestinationUpdate: Dict[str, Any] = None,
    RedshiftDestinationUpdate: Dict[str, Any] = None,
    ElasticsearchDestinationUpdate: Dict[str, Any] = None,
    SplunkDestinationUpdate: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
