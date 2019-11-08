# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kinesisvideo.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kinesisvideo](index.md#kinesisvideo) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_stream](#clientcreate_stream)
        - [Client().delete_stream](#clientdelete_stream)
        - [Client().describe_stream](#clientdescribe_stream)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_data_endpoint](#clientget_data_endpoint)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_streams](#clientlist_streams)
        - [Client().list_tags_for_stream](#clientlist_tags_for_stream)
        - [Client().tag_stream](#clienttag_stream)
        - [Client().untag_stream](#clientuntag_stream)
        - [Client().update_data_retention](#clientupdate_data_retention)
        - [Client().update_stream](#clientupdate_stream)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L19)

```python
def create_stream(
    StreamName: str,
    DeviceName: str = None,
    MediaType: str = None,
    KmsKeyId: str = None,
    DataRetentionInHours: int = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L31)

```python
def delete_stream(
    StreamARN: str,
    CurrentVersion: str = None,
) -> Dict[str, Any]:
```

### Client().describe_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L37)

```python
def describe_stream(
    StreamName: str = None,
    StreamARN: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L43)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_data_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L53)

```python
def get_data_endpoint(
    APIName: str,
    StreamName: str = None,
    StreamARN: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L59)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L63)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_streams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L67)

```python
def list_streams(
    MaxResults: int = None,
    NextToken: str = None,
    StreamNameCondition: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L76)

```python
def list_tags_for_stream(
    NextToken: str = None,
    StreamARN: str = None,
    StreamName: str = None,
) -> Dict[str, Any]:
```

### Client().tag_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L82)

```python
def tag_stream(
    Tags: Dict[str, Any],
    StreamARN: str = None,
    StreamName: str = None,
) -> Dict[str, Any]:
```

### Client().untag_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L88)

```python
def untag_stream(
    TagKeyList: List[Any],
    StreamARN: str = None,
    StreamName: str = None,
) -> Dict[str, Any]:
```

### Client().update_data_retention

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L94)

```python
def update_data_retention(
    CurrentVersion: str,
    Operation: str,
    DataRetentionChangeInHours: int,
    StreamName: str = None,
    StreamARN: str = None,
) -> Dict[str, Any]:
```

### Client().update_stream

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisvideo/client.py#L105)

```python
def update_stream(
    CurrentVersion: str,
    StreamName: str = None,
    StreamARN: str = None,
    DeviceName: str = None,
    MediaType: str = None,
) -> Dict[str, Any]:
```
