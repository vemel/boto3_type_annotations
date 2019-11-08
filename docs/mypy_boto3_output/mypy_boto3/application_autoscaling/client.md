# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.application_autoscaling.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Application Autoscaling](index.md#application-autoscaling) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_scaling_policy](#clientdelete_scaling_policy)
        - [Client().delete_scheduled_action](#clientdelete_scheduled_action)
        - [Client().deregister_scalable_target](#clientderegister_scalable_target)
        - [Client().describe_scalable_targets](#clientdescribe_scalable_targets)
        - [Client().describe_scaling_activities](#clientdescribe_scaling_activities)
        - [Client().describe_scaling_policies](#clientdescribe_scaling_policies)
        - [Client().describe_scheduled_actions](#clientdescribe_scheduled_actions)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().put_scaling_policy](#clientput_scaling_policy)
        - [Client().put_scheduled_action](#clientput_scheduled_action)
        - [Client().register_scalable_target](#clientregister_scalable_target)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_scaling_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L20)

```python
def delete_scaling_policy(
    PolicyName: str,
    ServiceNamespace: str,
    ResourceId: str,
    ScalableDimension: str,
) -> Dict[str, Any]:
```

### Client().delete_scheduled_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L30)

```python
def delete_scheduled_action(
    ServiceNamespace: str,
    ScheduledActionName: str,
    ResourceId: str,
    ScalableDimension: str,
) -> Dict[str, Any]:
```

### Client().deregister_scalable_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L40)

```python
def deregister_scalable_target(
    ServiceNamespace: str,
    ResourceId: str,
    ScalableDimension: str,
) -> Dict[str, Any]:
```

### Client().describe_scalable_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L46)

```python
def describe_scalable_targets(
    ServiceNamespace: str,
    ResourceIds: List[Any] = None,
    ScalableDimension: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_scaling_activities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L57)

```python
def describe_scaling_activities(
    ServiceNamespace: str,
    ResourceId: str = None,
    ScalableDimension: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_scaling_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L68)

```python
def describe_scaling_policies(
    ServiceNamespace: str,
    PolicyNames: List[Any] = None,
    ResourceId: str = None,
    ScalableDimension: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_scheduled_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L80)

```python
def describe_scheduled_actions(
    ServiceNamespace: str,
    ScheduledActionNames: List[Any] = None,
    ResourceId: str = None,
    ScalableDimension: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L92)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L102)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L106)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().put_scaling_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L110)

```python
def put_scaling_policy(
    PolicyName: str,
    ServiceNamespace: str,
    ResourceId: str,
    ScalableDimension: str,
    PolicyType: str = None,
    StepScalingPolicyConfiguration: Dict[str, Any] = None,
    TargetTrackingScalingPolicyConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().put_scheduled_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L123)

```python
def put_scheduled_action(
    ServiceNamespace: str,
    ScheduledActionName: str,
    ResourceId: str,
    ScalableDimension: str,
    Schedule: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    ScalableTargetAction: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().register_scalable_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/application_autoscaling/client.py#L137)

```python
def register_scalable_target(
    ServiceNamespace: str,
    ResourceId: str,
    ScalableDimension: str,
    MinCapacity: int = None,
    MaxCapacity: int = None,
    RoleARN: str = None,
    SuspendedState: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
