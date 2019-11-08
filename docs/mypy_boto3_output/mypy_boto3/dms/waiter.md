# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dms.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dms](index.md#dms) / Waiter
    - [EndpointDeleted](#endpointdeleted)
        - [EndpointDeleted().wait](#endpointdeletedwait)
    - [ReplicationInstanceAvailable](#replicationinstanceavailable)
        - [ReplicationInstanceAvailable().wait](#replicationinstanceavailablewait)
    - [ReplicationInstanceDeleted](#replicationinstancedeleted)
        - [ReplicationInstanceDeleted().wait](#replicationinstancedeletedwait)
    - [ReplicationTaskDeleted](#replicationtaskdeleted)
        - [ReplicationTaskDeleted().wait](#replicationtaskdeletedwait)
    - [ReplicationTaskReady](#replicationtaskready)
        - [ReplicationTaskReady().wait](#replicationtaskreadywait)
    - [ReplicationTaskRunning](#replicationtaskrunning)
        - [ReplicationTaskRunning().wait](#replicationtaskrunningwait)
    - [ReplicationTaskStopped](#replicationtaskstopped)
        - [ReplicationTaskStopped().wait](#replicationtaskstoppedwait)
    - [TestConnectionSucceeds](#testconnectionsucceeds)
        - [TestConnectionSucceeds().wait](#testconnectionsucceedswait)

## EndpointDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L10)

```python
class EndpointDeleted(Waiter):
```

### EndpointDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L13)

```python
def wait(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ReplicationInstanceAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L23)

```python
class ReplicationInstanceAvailable(Waiter):
```

### ReplicationInstanceAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L26)

```python
def wait(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ReplicationInstanceDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L36)

```python
class ReplicationInstanceDeleted(Waiter):
```

### ReplicationInstanceDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L39)

```python
def wait(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ReplicationTaskDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L49)

```python
class ReplicationTaskDeleted(Waiter):
```

### ReplicationTaskDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L52)

```python
def wait(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WithoutSettings: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ReplicationTaskReady

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L63)

```python
class ReplicationTaskReady(Waiter):
```

### ReplicationTaskReady().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L66)

```python
def wait(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WithoutSettings: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ReplicationTaskRunning

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L77)

```python
class ReplicationTaskRunning(Waiter):
```

### ReplicationTaskRunning().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L80)

```python
def wait(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WithoutSettings: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ReplicationTaskStopped

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L91)

```python
class ReplicationTaskStopped(Waiter):
```

### ReplicationTaskStopped().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L94)

```python
def wait(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WithoutSettings: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## TestConnectionSucceeds

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L105)

```python
class TestConnectionSucceeds(Waiter):
```

### TestConnectionSucceeds().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dms/waiter.py#L108)

```python
def wait(
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
