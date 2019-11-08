# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sdb.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sdb](index.md#sdb) / Client
    - [Client](#client)
        - [Client().batch_delete_attributes](#clientbatch_delete_attributes)
        - [Client().batch_put_attributes](#clientbatch_put_attributes)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_domain](#clientcreate_domain)
        - [Client().delete_attributes](#clientdelete_attributes)
        - [Client().delete_domain](#clientdelete_domain)
        - [Client().domain_metadata](#clientdomain_metadata)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_attributes](#clientget_attributes)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_domains](#clientlist_domains)
        - [Client().put_attributes](#clientput_attributes)
        - [Client().select](#clientselect)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_delete_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L15)

```python
def batch_delete_attributes(DomainName: str, Items: List[Any]) -> None:
```

### Client().batch_put_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L19)

```python
def batch_put_attributes(DomainName: str, Items: List[Any]) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L23)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L27)

```python
def create_domain(DomainName: str) -> None:
```

### Client().delete_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L31)

```python
def delete_attributes(
    DomainName: str,
    ItemName: str,
    Attributes: List[Any] = None,
    Expected: Dict[str, Any] = None,
) -> None:
```

### Client().delete_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L41)

```python
def delete_domain(DomainName: str) -> None:
```

### Client().domain_metadata

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L45)

```python
def domain_metadata(DomainName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L49)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L59)

```python
def get_attributes(
    DomainName: str,
    ItemName: str,
    AttributeNames: List[Any] = None,
    ConsistentRead: bool = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L69)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L73)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_domains

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L77)

```python
def list_domains(
    MaxNumberOfDomains: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L83)

```python
def put_attributes(
    DomainName: str,
    ItemName: str,
    Attributes: List[Any],
    Expected: Dict[str, Any] = None,
) -> None:
```

### Client().select

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/client.py#L93)

```python
def select(
    SelectExpression: str,
    NextToken: str = None,
    ConsistentRead: bool = None,
) -> Dict[str, Any]:
```
