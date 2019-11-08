# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.rds.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Rds](index.md#rds) / Waiter
    - [DBClusterSnapshotAvailable](#dbclustersnapshotavailable)
        - [DBClusterSnapshotAvailable().wait](#dbclustersnapshotavailablewait)
    - [DBClusterSnapshotDeleted](#dbclustersnapshotdeleted)
        - [DBClusterSnapshotDeleted().wait](#dbclustersnapshotdeletedwait)
    - [DBInstanceAvailable](#dbinstanceavailable)
        - [DBInstanceAvailable().wait](#dbinstanceavailablewait)
    - [DBInstanceDeleted](#dbinstancedeleted)
        - [DBInstanceDeleted().wait](#dbinstancedeletedwait)
    - [DBSnapshotAvailable](#dbsnapshotavailable)
        - [DBSnapshotAvailable().wait](#dbsnapshotavailablewait)
    - [DBSnapshotCompleted](#dbsnapshotcompleted)
        - [DBSnapshotCompleted().wait](#dbsnapshotcompletedwait)
    - [DBSnapshotDeleted](#dbsnapshotdeleted)
        - [DBSnapshotDeleted().wait](#dbsnapshotdeletedwait)

## DBClusterSnapshotAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L10)

```python
class DBClusterSnapshotAvailable(Waiter):
```

### DBClusterSnapshotAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L13)

```python
def wait(
    DBClusterIdentifier: str = None,
    DBClusterSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## DBClusterSnapshotDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L28)

```python
class DBClusterSnapshotDeleted(Waiter):
```

### DBClusterSnapshotDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L31)

```python
def wait(
    DBClusterIdentifier: str = None,
    DBClusterSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## DBInstanceAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L46)

```python
class DBInstanceAvailable(Waiter):
```

### DBInstanceAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L49)

```python
def wait(
    DBInstanceIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## DBInstanceDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L60)

```python
class DBInstanceDeleted(Waiter):
```

### DBInstanceDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L63)

```python
def wait(
    DBInstanceIdentifier: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## DBSnapshotAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L74)

```python
class DBSnapshotAvailable(Waiter):
```

### DBSnapshotAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L77)

```python
def wait(
    DBInstanceIdentifier: str = None,
    DBSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None,
    DbiResourceId: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## DBSnapshotCompleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L93)

```python
class DBSnapshotCompleted(Waiter):
```

### DBSnapshotCompleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L96)

```python
def wait(
    DBInstanceIdentifier: str = None,
    DBSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None,
    DbiResourceId: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## DBSnapshotDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L112)

```python
class DBSnapshotDeleted(Waiter):
```

### DBSnapshotDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/rds/waiter.py#L115)

```python
def wait(
    DBInstanceIdentifier: str = None,
    DBSnapshotIdentifier: str = None,
    SnapshotType: str = None,
    Filters: List[Any] = None,
    MaxRecords: int = None,
    Marker: str = None,
    IncludeShared: bool = None,
    IncludePublic: bool = None,
    DbiResourceId: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
