# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.lex_runtime.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Lex Runtime](index.md#lex-runtime) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_session](#clientdelete_session)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_session](#clientget_session)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().post_content](#clientpost_content)
        - [Client().post_text](#clientpost_text)
        - [Client().put_session](#clientput_session)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py#L14)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py#L17)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py#L21)

```python
def delete_session(
    botName: str,
    botAlias: str,
    userId: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py#L27)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py#L37)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py#L41)

```python
def get_session(
    botName: str,
    botAlias: str,
    userId: str,
    checkpointLabelFilter: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py#L51)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().post_content

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py#L55)

```python
def post_content(
    botName: str,
    botAlias: str,
    userId: str,
    contentType: str,
    inputStream: Union[bytes, IO],
    sessionAttributes: str = None,
    requestAttributes: str = None,
    accept: str = None,
) -> Dict[str, Any]:
```

### Client().post_text

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py#L69)

```python
def post_text(
    botName: str,
    botAlias: str,
    userId: str,
    inputText: str,
    sessionAttributes: Dict[str, Any] = None,
    requestAttributes: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().put_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_runtime/client.py#L81)

```python
def put_session(
    botName: str,
    botAlias: str,
    userId: str,
    sessionAttributes: Dict[str, Any] = None,
    dialogAction: Dict[str, Any] = None,
    recentIntentSummaryView: List[Any] = None,
    accept: str = None,
) -> Dict[str, Any]:
```
