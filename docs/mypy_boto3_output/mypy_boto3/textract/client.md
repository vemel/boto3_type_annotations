# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.textract.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Textract](index.md#textract) / Client
    - [Client](#client)
        - [Client().analyze_document](#clientanalyze_document)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().detect_document_text](#clientdetect_document_text)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_document_analysis](#clientget_document_analysis)
        - [Client().get_document_text_detection](#clientget_document_text_detection)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().start_document_analysis](#clientstart_document_analysis)
        - [Client().start_document_text_detection](#clientstart_document_text_detection)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L12)

```python
class Client(BaseClient):
```

### Client().analyze_document

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L15)

```python
def analyze_document(
    Document: Dict[str, Any],
    FeatureTypes: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L21)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().detect_document_text

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L25)

```python
def detect_document_text(Document: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L29)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_document_analysis

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L39)

```python
def get_document_analysis(
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_document_text_detection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L45)

```python
def get_document_text_detection(
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L51)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L55)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().start_document_analysis

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L59)

```python
def start_document_analysis(
    DocumentLocation: Dict[str, Any],
    FeatureTypes: List[Any],
    ClientRequestToken: str = None,
    JobTag: str = None,
    NotificationChannel: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().start_document_text_detection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/textract/client.py#L70)

```python
def start_document_text_detection(
    DocumentLocation: Dict[str, Any],
    ClientRequestToken: str = None,
    JobTag: str = None,
    NotificationChannel: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
