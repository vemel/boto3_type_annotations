# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.application_autoscaling.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Application Autoscaling](index.md#application-autoscaling) / Paginator
    - [DescribeScalableTargets](#describescalabletargets)
        - [DescribeScalableTargets().paginate](#describescalabletargetspaginate)
    - [DescribeScalingActivities](#describescalingactivities)
        - [DescribeScalingActivities().paginate](#describescalingactivitiespaginate)
    - [DescribeScalingPolicies](#describescalingpolicies)
        - [DescribeScalingPolicies().paginate](#describescalingpoliciespaginate)
    - [DescribeScheduledActions](#describescheduledactions)
        - [DescribeScheduledActions().paginate](#describescheduledactionspaginate)

## DescribeScalableTargets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/paginator.py#L10)

```python
class DescribeScalableTargets(Paginator):
```

### DescribeScalableTargets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/paginator.py#L13)

```python
def paginate(
    ServiceNamespace: str,
    ResourceIds: List[Any] = None,
    ScalableDimension: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeScalingActivities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/paginator.py#L23)

```python
class DescribeScalingActivities(Paginator):
```

### DescribeScalingActivities().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/paginator.py#L26)

```python
def paginate(
    ServiceNamespace: str,
    ResourceId: str = None,
    ScalableDimension: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeScalingPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/paginator.py#L36)

```python
class DescribeScalingPolicies(Paginator):
```

### DescribeScalingPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/paginator.py#L39)

```python
def paginate(
    ServiceNamespace: str,
    PolicyNames: List[Any] = None,
    ResourceId: str = None,
    ScalableDimension: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeScheduledActions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/paginator.py#L50)

```python
class DescribeScheduledActions(Paginator):
```

### DescribeScheduledActions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/paginator.py#L53)

```python
def paginate(
    ServiceNamespace: str,
    ScheduledActionNames: List[Any] = None,
    ResourceId: str = None,
    ScalableDimension: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
