# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.pi.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pi/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Pi](index.md#pi) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().describe_dimension_keys](#clientdescribe_dimension_keys)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_resource_metrics](#clientget_resource_metrics)
        - [Client().get_waiter](#clientget_waiter)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pi/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pi/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().describe_dimension_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pi/client.py#L20)

```python
def describe_dimension_keys(
    ServiceType: str,
    Identifier: str,
    StartTime: datetime,
    EndTime: datetime,
    Metric: str,
    GroupBy: Dict[str, Any],
    PeriodInSeconds: int = None,
    PartitionBy: Dict[str, Any] = None,
    Filter: Dict[str, Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pi/client.py#L37)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pi/client.py#L47)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_resource_metrics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pi/client.py#L51)

```python
def get_resource_metrics(
    ServiceType: str,
    Identifier: str,
    MetricQueries: List[Any],
    StartTime: datetime,
    EndTime: datetime,
    PeriodInSeconds: int = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/pi/client.py#L65)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```
