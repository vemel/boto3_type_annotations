# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.marketplacecommerceanalytics.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplacecommerceanalytics/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Marketplacecommerceanalytics](index.md#marketplacecommerceanalytics) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().generate_data_set](#clientgenerate_data_set)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().start_support_data_export](#clientstart_support_data_export)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplacecommerceanalytics/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplacecommerceanalytics/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().generate_data_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplacecommerceanalytics/client.py#L19)

```python
def generate_data_set(
    dataSetType: str,
    dataSetPublicationDate: datetime,
    roleNameArn: str,
    destinationS3BucketName: str,
    snsTopicArn: str,
    destinationS3Prefix: str = None,
    customerDefinedValues: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplacecommerceanalytics/client.py#L32)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplacecommerceanalytics/client.py#L42)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplacecommerceanalytics/client.py#L46)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().start_support_data_export

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/marketplacecommerceanalytics/client.py#L50)

```python
def start_support_data_export(
    dataSetType: str,
    fromDate: datetime,
    roleNameArn: str,
    destinationS3BucketName: str,
    snsTopicArn: str,
    destinationS3Prefix: str = None,
    customerDefinedValues: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
