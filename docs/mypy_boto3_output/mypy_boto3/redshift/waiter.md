# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.redshift.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Redshift](index.md#redshift) / Waiter
    - [ClusterAvailable](#clusteravailable)
        - [ClusterAvailable().wait](#clusteravailablewait)
    - [ClusterDeleted](#clusterdeleted)
        - [ClusterDeleted().wait](#clusterdeletedwait)
    - [ClusterRestored](#clusterrestored)
        - [ClusterRestored().wait](#clusterrestoredwait)
    - [SnapshotAvailable](#snapshotavailable)
        - [SnapshotAvailable().wait](#snapshotavailablewait)

## ClusterAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/waiter.py#L11)

```python
class ClusterAvailable(Waiter):
```

### ClusterAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/waiter.py#L14)

```python
def wait(
    ClusterIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ClusterDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/waiter.py#L26)

```python
class ClusterDeleted(Waiter):
```

### ClusterDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/waiter.py#L29)

```python
def wait(
    ClusterIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ClusterRestored

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/waiter.py#L41)

```python
class ClusterRestored(Waiter):
```

### ClusterRestored().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/waiter.py#L44)

```python
def wait(
    ClusterIdentifier: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## SnapshotAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/waiter.py#L56)

```python
class SnapshotAvailable(Waiter):
```

### SnapshotAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/redshift/waiter.py#L59)

```python
def wait(
    ClusterIdentifier: str = None,
    SnapshotIdentifier: str = None,
    SnapshotType: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    MaxRecords: int = None,
    Marker: str = None,
    OwnerAccount: str = None,
    TagKeys: List[Any] = None,
    TagValues: List[Any] = None,
    ClusterExists: bool = None,
    SortingEntities: List[Any] = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
