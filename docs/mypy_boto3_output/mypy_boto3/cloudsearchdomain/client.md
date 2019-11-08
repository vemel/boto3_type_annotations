# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudsearchdomain.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearchdomain/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudsearchdomain](index.md#cloudsearchdomain) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().search](#clientsearch)
        - [Client().suggest](#clientsuggest)
        - [Client().upload_documents](#clientupload_documents)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearchdomain/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearchdomain/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearchdomain/client.py#L20)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearchdomain/client.py#L30)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearchdomain/client.py#L34)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().search

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearchdomain/client.py#L38)

```python
def search(
    query: str,
    cursor: str = None,
    expr: str = None,
    facet: str = None,
    filterQuery: str = None,
    highlight: str = None,
    partial: bool = None,
    queryOptions: str = None,
    queryParser: str = None,
    returnFields: str = None,
    size: int = None,
    sort: str = None,
    start: int = None,
    stats: str = None,
) -> Dict[str, Any]:
```

### Client().suggest

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearchdomain/client.py#L58)

```python
def suggest(query: str, suggester: str, size: int = None) -> Dict[str, Any]:
```

### Client().upload_documents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearchdomain/client.py#L62)

```python
def upload_documents(
    documents: Union[bytes, IO],
    contentType: str,
) -> Dict[str, Any]:
```
