# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.qldb_session.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb_session/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Qldb Session](index.md#qldb-session) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().send_command](#clientsend_command)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb_session/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb_session/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb_session/client.py#L18)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb_session/client.py#L28)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb_session/client.py#L32)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().send_command

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb_session/client.py#L36)

```python
def send_command(
    SessionToken: str = None,
    StartSession: Dict[str, Any] = None,
    StartTransaction: Dict[str, Any] = None,
    EndSession: Dict[str, Any] = None,
    CommitTransaction: Dict[str, Any] = None,
    AbortTransaction: Dict[str, Any] = None,
    ExecuteStatement: Dict[str, Any] = None,
    FetchPage: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
