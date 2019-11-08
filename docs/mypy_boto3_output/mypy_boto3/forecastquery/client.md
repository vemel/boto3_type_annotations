# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.forecastquery.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecastquery/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Forecastquery](index.md#forecastquery) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().query_forecast](#clientquery_forecast)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecastquery/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecastquery/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecastquery/client.py#L18)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecastquery/client.py#L28)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecastquery/client.py#L32)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().query_forecast

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecastquery/client.py#L36)

```python
def query_forecast(
    ForecastArn: str,
    Filters: Dict[str, Any],
    StartDate: str = None,
    EndDate: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```
