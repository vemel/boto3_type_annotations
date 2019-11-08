# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.autoscaling_plans.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Autoscaling Plans](index.md#autoscaling-plans) / Paginator
    - [DescribeScalingPlanResources](#describescalingplanresources)
        - [DescribeScalingPlanResources().paginate](#describescalingplanresourcespaginate)
    - [DescribeScalingPlans](#describescalingplans)
        - [DescribeScalingPlans().paginate](#describescalingplanspaginate)

## DescribeScalingPlanResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/paginator.py#L10)

```python
class DescribeScalingPlanResources(Paginator):
```

### DescribeScalingPlanResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/paginator.py#L13)

```python
def paginate(
    ScalingPlanName: str,
    ScalingPlanVersion: int,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeScalingPlans

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/paginator.py#L22)

```python
class DescribeScalingPlans(Paginator):
```

### DescribeScalingPlans().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling_plans/paginator.py#L25)

```python
def paginate(
    ScalingPlanNames: List[Any] = None,
    ScalingPlanVersion: int = None,
    ApplicationSources: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
