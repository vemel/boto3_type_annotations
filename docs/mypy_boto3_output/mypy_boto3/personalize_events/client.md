# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.personalize_events.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize_events/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Personalize Events](index.md#personalize-events) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().put_events](#clientput_events)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize_events/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize_events/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize_events/client.py#L19)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize_events/client.py#L29)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize_events/client.py#L33)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().put_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize_events/client.py#L37)

```python
def put_events(
    trackingId: str,
    sessionId: str,
    eventList: List[Any],
    userId: str = None,
) -> None:
```
