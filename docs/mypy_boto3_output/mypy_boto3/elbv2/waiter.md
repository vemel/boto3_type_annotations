# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elbv2.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elbv2](index.md#elbv2) / Waiter
    - [LoadBalancerAvailable](#loadbalanceravailable)
        - [LoadBalancerAvailable().wait](#loadbalanceravailablewait)
    - [LoadBalancerExists](#loadbalancerexists)
        - [LoadBalancerExists().wait](#loadbalancerexistswait)
    - [LoadBalancersDeleted](#loadbalancersdeleted)
        - [LoadBalancersDeleted().wait](#loadbalancersdeletedwait)
    - [TargetDeregistered](#targetderegistered)
        - [TargetDeregistered().wait](#targetderegisteredwait)
    - [TargetInService](#targetinservice)
        - [TargetInService().wait](#targetinservicewait)

## LoadBalancerAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py#L10)

```python
class LoadBalancerAvailable(Waiter):
```

### LoadBalancerAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py#L13)

```python
def wait(
    LoadBalancerArns: List[Any] = None,
    Names: List[Any] = None,
    Marker: str = None,
    PageSize: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## LoadBalancerExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py#L24)

```python
class LoadBalancerExists(Waiter):
```

### LoadBalancerExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py#L27)

```python
def wait(
    LoadBalancerArns: List[Any] = None,
    Names: List[Any] = None,
    Marker: str = None,
    PageSize: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## LoadBalancersDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py#L38)

```python
class LoadBalancersDeleted(Waiter):
```

### LoadBalancersDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py#L41)

```python
def wait(
    LoadBalancerArns: List[Any] = None,
    Names: List[Any] = None,
    Marker: str = None,
    PageSize: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## TargetDeregistered

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py#L52)

```python
class TargetDeregistered(Waiter):
```

### TargetDeregistered().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py#L55)

```python
def wait(
    TargetGroupArn: str,
    Targets: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## TargetInService

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py#L64)

```python
class TargetInService(Waiter):
```

### TargetInService().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elbv2/waiter.py#L67)

```python
def wait(
    TargetGroupArn: str,
    Targets: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
