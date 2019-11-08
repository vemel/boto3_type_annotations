# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.mediastore_data.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Mediastore Data](index.md#mediastore-data) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_object](#clientdelete_object)
        - [Client().describe_object](#clientdescribe_object)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_object](#clientget_object)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_items](#clientlist_items)
        - [Client().put_object](#clientput_object)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py#L20)

```python
def delete_object(Path: str) -> Dict[str, Any]:
```

### Client().describe_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py#L24)

```python
def describe_object(Path: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py#L28)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py#L38)

```python
def get_object(Path: str, Range: str = None) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py#L42)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py#L46)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_items

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py#L50)

```python
def list_items(
    Path: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/mediastore_data/client.py#L56)

```python
def put_object(
    Body: Union[bytes, IO],
    Path: str,
    ContentType: str = None,
    CacheControl: str = None,
    StorageClass: str = None,
    UploadAvailability: str = None,
) -> Dict[str, Any]:
```
