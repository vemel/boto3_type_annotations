# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.pricing.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Pricing](index.md#pricing) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().describe_services](#clientdescribe_services)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_attribute_values](#clientget_attribute_values)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_products](#clientget_products)
        - [Client().get_waiter](#clientget_waiter)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().describe_services

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/client.py#L19)

```python
def describe_services(
    ServiceCode: str = None,
    FormatVersion: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/client.py#L29)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_attribute_values

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/client.py#L39)

```python
def get_attribute_values(
    ServiceCode: str,
    AttributeName: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/client.py#L49)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_products

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/client.py#L53)

```python
def get_products(
    ServiceCode: str = None,
    Filters: List[Any] = None,
    FormatVersion: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pricing/client.py#L64)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```
