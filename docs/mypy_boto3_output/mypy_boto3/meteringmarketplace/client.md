# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.meteringmarketplace.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/meteringmarketplace/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Meteringmarketplace](index.md#meteringmarketplace) / Client
    - [Client](#client)
        - [Client().batch_meter_usage](#clientbatch_meter_usage)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().meter_usage](#clientmeter_usage)
        - [Client().register_usage](#clientregister_usage)
        - [Client().resolve_customer](#clientresolve_customer)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/meteringmarketplace/client.py#L13)

```python
class Client(BaseClient):
```

### Client().batch_meter_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/meteringmarketplace/client.py#L16)

```python
def batch_meter_usage(
    UsageRecords: List[Any],
    ProductCode: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/meteringmarketplace/client.py#L22)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/meteringmarketplace/client.py#L26)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/meteringmarketplace/client.py#L36)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/meteringmarketplace/client.py#L40)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().meter_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/meteringmarketplace/client.py#L44)

```python
def meter_usage(
    ProductCode: str,
    Timestamp: datetime,
    UsageDimension: str,
    UsageQuantity: int = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().register_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/meteringmarketplace/client.py#L55)

```python
def register_usage(
    ProductCode: str,
    PublicKeyVersion: int,
    Nonce: str = None,
) -> Dict[str, Any]:
```

### Client().resolve_customer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/meteringmarketplace/client.py#L61)

```python
def resolve_customer(RegistrationToken: str) -> Dict[str, Any]:
```
