# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.opsworks.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Opsworks](index.md#opsworks) / Waiter
    - [AppExists](#appexists)
        - [AppExists().wait](#appexistswait)
    - [DeploymentSuccessful](#deploymentsuccessful)
        - [DeploymentSuccessful().wait](#deploymentsuccessfulwait)
    - [InstanceOnline](#instanceonline)
        - [InstanceOnline().wait](#instanceonlinewait)
    - [InstanceRegistered](#instanceregistered)
        - [InstanceRegistered().wait](#instanceregisteredwait)
    - [InstanceStopped](#instancestopped)
        - [InstanceStopped().wait](#instancestoppedwait)
    - [InstanceTerminated](#instanceterminated)
        - [InstanceTerminated().wait](#instanceterminatedwait)

## AppExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L10)

```python
class AppExists(Waiter):
```

### AppExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L13)

```python
def wait(
    StackId: str = None,
    AppIds: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## DeploymentSuccessful

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L22)

```python
class DeploymentSuccessful(Waiter):
```

### DeploymentSuccessful().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L25)

```python
def wait(
    StackId: str = None,
    AppId: str = None,
    DeploymentIds: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceOnline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L35)

```python
class InstanceOnline(Waiter):
```

### InstanceOnline().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L38)

```python
def wait(
    StackId: str = None,
    LayerId: str = None,
    InstanceIds: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceRegistered

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L48)

```python
class InstanceRegistered(Waiter):
```

### InstanceRegistered().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L51)

```python
def wait(
    StackId: str = None,
    LayerId: str = None,
    InstanceIds: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceStopped

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L61)

```python
class InstanceStopped(Waiter):
```

### InstanceStopped().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L64)

```python
def wait(
    StackId: str = None,
    LayerId: str = None,
    InstanceIds: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## InstanceTerminated

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L74)

```python
class InstanceTerminated(Waiter):
```

### InstanceTerminated().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworks/waiter.py#L77)

```python
def wait(
    StackId: str = None,
    LayerId: str = None,
    InstanceIds: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
