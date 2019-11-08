# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.appstream.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Appstream](index.md#appstream) / Waiter
    - [FleetStarted](#fleetstarted)
        - [FleetStarted().wait](#fleetstartedwait)
    - [FleetStopped](#fleetstopped)
        - [FleetStopped().wait](#fleetstoppedwait)

## FleetStarted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/waiter.py#L10)

```python
class FleetStarted(Waiter):
```

### FleetStarted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/waiter.py#L13)

```python
def wait(
    Names: List[Any] = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## FleetStopped

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/waiter.py#L22)

```python
class FleetStopped(Waiter):
```

### FleetStopped().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appstream/waiter.py#L25)

```python
def wait(
    Names: List[Any] = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
