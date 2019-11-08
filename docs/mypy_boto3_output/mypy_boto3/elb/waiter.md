# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elb.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elb](index.md#elb) / Waiter
    - [AnyInstanceInService](#anyinstanceinservice)
        - [AnyInstanceInService().wait](#anyinstanceinservicewait)
    - [InstanceDeregistered](#instancederegistered)
        - [InstanceDeregistered().wait](#instancederegisteredwait)
    - [InstanceInService](#instanceinservice)
        - [InstanceInService().wait](#instanceinservicewait)

## AnyInstanceInService

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/waiter.py#L10)

```python
class AnyInstanceInService(Waiter):
```

### AnyInstanceInService().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/waiter.py#L13)

```python
def wait(
    LoadBalancerName: str,
    Instances: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceDeregistered

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/waiter.py#L22)

```python
class InstanceDeregistered(Waiter):
```

### InstanceDeregistered().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/waiter.py#L25)

```python
def wait(
    LoadBalancerName: str,
    Instances: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceInService

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/waiter.py#L34)

```python
class InstanceInService(Waiter):
```

### InstanceInService().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elb/waiter.py#L37)

```python
def wait(
    LoadBalancerName: str,
    Instances: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
