# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.autoscaling_plans.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Autoscaling Plans](index.md#autoscaling-plans) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_scaling_plan](#clientcreate_scaling_plan)
        - [Client().delete_scaling_plan](#clientdelete_scaling_plan)
        - [Client().describe_scaling_plan_resources](#clientdescribe_scaling_plan_resources)
        - [Client().describe_scaling_plans](#clientdescribe_scaling_plans)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_scaling_plan_resource_forecast_data](#clientget_scaling_plan_resource_forecast_data)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().update_scaling_plan](#clientupdate_scaling_plan)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_scaling_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L20)

```python
def create_scaling_plan(
    ScalingPlanName: str,
    ApplicationSource: Dict[str, Any],
    ScalingInstructions: List[Any],
) -> Dict[str, Any]:
```

### Client().delete_scaling_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L29)

```python
def delete_scaling_plan(
    ScalingPlanName: str,
    ScalingPlanVersion: int,
) -> Dict[str, Any]:
```

### Client().describe_scaling_plan_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L35)

```python
def describe_scaling_plan_resources(
    ScalingPlanName: str,
    ScalingPlanVersion: int,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_scaling_plans

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L45)

```python
def describe_scaling_plans(
    ScalingPlanNames: List[Any] = None,
    ScalingPlanVersion: int = None,
    ApplicationSources: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L56)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L66)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_scaling_plan_resource_forecast_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L70)

```python
def get_scaling_plan_resource_forecast_data(
    ScalingPlanName: str,
    ScalingPlanVersion: int,
    ServiceNamespace: str,
    ResourceId: str,
    ScalableDimension: str,
    ForecastDataType: str,
    StartTime: datetime,
    EndTime: datetime,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L84)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().update_scaling_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/client.py#L88)

```python
def update_scaling_plan(
    ScalingPlanName: str,
    ScalingPlanVersion: int,
    ApplicationSource: Dict[str, Any] = None,
    ScalingInstructions: List[Any] = None,
) -> Dict[str, Any]:
```
