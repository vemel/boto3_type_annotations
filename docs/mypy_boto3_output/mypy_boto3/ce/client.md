# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ce.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ce](index.md#ce) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_cost_and_usage](#clientget_cost_and_usage)
        - [Client().get_cost_forecast](#clientget_cost_forecast)
        - [Client().get_dimension_values](#clientget_dimension_values)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_reservation_coverage](#clientget_reservation_coverage)
        - [Client().get_reservation_purchase_recommendation](#clientget_reservation_purchase_recommendation)
        - [Client().get_reservation_utilization](#clientget_reservation_utilization)
        - [Client().get_rightsizing_recommendation](#clientget_rightsizing_recommendation)
        - [Client().get_savings_plans_coverage](#clientget_savings_plans_coverage)
        - [Client().get_savings_plans_purchase_recommendation](#clientget_savings_plans_purchase_recommendation)
        - [Client().get_savings_plans_utilization](#clientget_savings_plans_utilization)
        - [Client().get_savings_plans_utilization_details](#clientget_savings_plans_utilization_details)
        - [Client().get_tags](#clientget_tags)
        - [Client().get_usage_forecast](#clientget_usage_forecast)
        - [Client().get_waiter](#clientget_waiter)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L19)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_cost_and_usage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L29)

```python
def get_cost_and_usage(
    TimePeriod: Dict[str, Any],
    Granularity: str = None,
    Filter: Dict[str, Any] = None,
    Metrics: List[Any] = None,
    GroupBy: List[Any] = None,
    NextPageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_cost_forecast

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L41)

```python
def get_cost_forecast(
    TimePeriod: Dict[str, Any],
    Metric: str,
    Granularity: str,
    Filter: Dict[str, Any] = None,
    PredictionIntervalLevel: int = None,
) -> Dict[str, Any]:
```

### Client().get_dimension_values

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L52)

```python
def get_dimension_values(
    TimePeriod: Dict[str, Any],
    Dimension: str,
    SearchString: str = None,
    Context: str = None,
    NextPageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L63)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_reservation_coverage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L67)

```python
def get_reservation_coverage(
    TimePeriod: Dict[str, Any],
    GroupBy: List[Any] = None,
    Granularity: str = None,
    Filter: Dict[str, Any] = None,
    Metrics: List[Any] = None,
    NextPageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_reservation_purchase_recommendation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L79)

```python
def get_reservation_purchase_recommendation(
    Service: str,
    AccountId: str = None,
    AccountScope: str = None,
    LookbackPeriodInDays: str = None,
    TermInYears: str = None,
    PaymentOption: str = None,
    ServiceSpecification: Dict[str, Any] = None,
    PageSize: int = None,
    NextPageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_reservation_utilization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L94)

```python
def get_reservation_utilization(
    TimePeriod: Dict[str, Any],
    GroupBy: List[Any] = None,
    Granularity: str = None,
    Filter: Dict[str, Any] = None,
    NextPageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_rightsizing_recommendation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L105)

```python
def get_rightsizing_recommendation(
    Service: str,
    Filter: Dict[str, Any] = None,
    PageSize: int = None,
    NextPageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_savings_plans_coverage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L115)

```python
def get_savings_plans_coverage(
    TimePeriod: Dict[str, Any],
    GroupBy: List[Any] = None,
    Granularity: str = None,
    Filter: Dict[str, Any] = None,
    Metrics: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_savings_plans_purchase_recommendation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L128)

```python
def get_savings_plans_purchase_recommendation(
    SavingsPlansType: str,
    TermInYears: str,
    PaymentOption: str,
    LookbackPeriodInDays: str,
    NextPageToken: str = None,
    PageSize: int = None,
) -> Dict[str, Any]:
```

### Client().get_savings_plans_utilization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L140)

```python
def get_savings_plans_utilization(
    TimePeriod: Dict[str, Any],
    Granularity: str = None,
    Filter: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_savings_plans_utilization_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L149)

```python
def get_savings_plans_utilization_details(
    TimePeriod: Dict[str, Any],
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L159)

```python
def get_tags(
    TimePeriod: Dict[str, Any],
    SearchString: str = None,
    TagKey: str = None,
    NextPageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_usage_forecast

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L169)

```python
def get_usage_forecast(
    TimePeriod: Dict[str, Any],
    Metric: str,
    Granularity: str,
    Filter: Dict[str, Any] = None,
    PredictionIntervalLevel: int = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ce/client.py#L180)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```
