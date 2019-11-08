# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.iot_data.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_data/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Iot Data](index.md#iot-data) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_thing_shadow](#clientdelete_thing_shadow)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_thing_shadow](#clientget_thing_shadow)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().publish](#clientpublish)
        - [Client().update_thing_shadow](#clientupdate_thing_shadow)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_data/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_data/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_thing_shadow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_data/client.py#L20)

```python
def delete_thing_shadow(thingName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_data/client.py#L24)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_data/client.py#L34)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_thing_shadow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_data/client.py#L38)

```python
def get_thing_shadow(thingName: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_data/client.py#L42)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().publish

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_data/client.py#L46)

```python
def publish(
    topic: str,
    qos: int = None,
    payload: Union[bytes, IO] = None,
) -> None:
```

### Client().update_thing_shadow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/iot_data/client.py#L52)

```python
def update_thing_shadow(
    thingName: str,
    payload: Union[bytes, IO],
) -> Dict[str, Any]:
```
