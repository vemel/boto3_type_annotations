# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.elasticache.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Elasticache](index.md#elasticache) / Waiter
    - [CacheClusterAvailable](#cacheclusteravailable)
        - [CacheClusterAvailable().wait](#cacheclusteravailablewait)
    - [CacheClusterDeleted](#cacheclusterdeleted)
        - [CacheClusterDeleted().wait](#cacheclusterdeletedwait)
    - [ReplicationGroupAvailable](#replicationgroupavailable)
        - [ReplicationGroupAvailable().wait](#replicationgroupavailablewait)
    - [ReplicationGroupDeleted](#replicationgroupdeleted)
        - [ReplicationGroupDeleted().wait](#replicationgroupdeletedwait)

## CacheClusterAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/waiter.py#L9)

```python
class CacheClusterAvailable(Waiter):
```

### CacheClusterAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/waiter.py#L12)

```python
def wait(
    CacheClusterId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    ShowCacheNodeInfo: bool = None,
    ShowCacheClustersNotInReplicationGroups: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## CacheClusterDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/waiter.py#L24)

```python
class CacheClusterDeleted(Waiter):
```

### CacheClusterDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/waiter.py#L27)

```python
def wait(
    CacheClusterId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    ShowCacheNodeInfo: bool = None,
    ShowCacheClustersNotInReplicationGroups: bool = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ReplicationGroupAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/waiter.py#L39)

```python
class ReplicationGroupAvailable(Waiter):
```

### ReplicationGroupAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/waiter.py#L42)

```python
def wait(
    ReplicationGroupId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## ReplicationGroupDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/waiter.py#L52)

```python
class ReplicationGroupDeleted(Waiter):
```

### ReplicationGroupDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/elasticache/waiter.py#L55)

```python
def wait(
    ReplicationGroupId: str = None,
    MaxRecords: int = None,
    Marker: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
