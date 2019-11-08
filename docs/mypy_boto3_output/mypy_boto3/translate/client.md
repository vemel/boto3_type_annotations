# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.translate.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Translate](index.md#translate) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_terminology](#clientdelete_terminology)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_terminology](#clientget_terminology)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_terminology](#clientimport_terminology)
        - [Client().list_terminologies](#clientlist_terminologies)
        - [Client().translate_text](#clienttranslate_text)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_terminology

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py#L19)

```python
def delete_terminology(Name: str) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py#L23)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py#L33)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_terminology

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py#L37)

```python
def get_terminology(Name: str, TerminologyDataFormat: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py#L41)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_terminology

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py#L45)

```python
def import_terminology(
    Name: str,
    MergeStrategy: str,
    TerminologyData: Dict[str, Any],
    Description: str = None,
    EncryptionKey: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_terminologies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py#L56)

```python
def list_terminologies(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().translate_text

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/translate/client.py#L62)

```python
def translate_text(
    Text: str,
    SourceLanguageCode: str,
    TargetLanguageCode: str,
    TerminologyNames: List[Any] = None,
) -> Dict[str, Any]:
```
