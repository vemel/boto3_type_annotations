# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ecs.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ecs](index.md#ecs) / Waiter
    - [ServicesInactive](#servicesinactive)
        - [ServicesInactive().wait](#servicesinactivewait)
    - [ServicesStable](#servicesstable)
        - [ServicesStable().wait](#servicesstablewait)
    - [TasksRunning](#tasksrunning)
        - [TasksRunning().wait](#tasksrunningwait)
    - [TasksStopped](#tasksstopped)
        - [TasksStopped().wait](#tasksstoppedwait)

## ServicesInactive

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/waiter.py#L10)

```python
class ServicesInactive(Waiter):
```

### ServicesInactive().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/waiter.py#L13)

```python
def wait(
    services: List[Any],
    cluster: str = None,
    include: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ServicesStable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/waiter.py#L23)

```python
class ServicesStable(Waiter):
```

### ServicesStable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/waiter.py#L26)

```python
def wait(
    services: List[Any],
    cluster: str = None,
    include: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## TasksRunning

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/waiter.py#L36)

```python
class TasksRunning(Waiter):
```

### TasksRunning().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/waiter.py#L39)

```python
def wait(
    tasks: List[Any],
    cluster: str = None,
    include: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## TasksStopped

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/waiter.py#L49)

```python
class TasksStopped(Waiter):
```

### TasksStopped().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecs/waiter.py#L52)

```python
def wait(
    tasks: List[Any],
    cluster: str = None,
    include: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
