# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.eks.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Eks](index.md#eks) / Waiter
    - [ClusterActive](#clusteractive)
        - [ClusterActive().wait](#clusteractivewait)
    - [ClusterDeleted](#clusterdeleted)
        - [ClusterDeleted().wait](#clusterdeletedwait)

## ClusterActive

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/waiter.py#L9)

```python
class ClusterActive(Waiter):
```

### ClusterActive().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/waiter.py#L12)

```python
def wait(name: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## ClusterDeleted

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/waiter.py#L16)

```python
class ClusterDeleted(Waiter):
```

### ClusterDeleted().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/waiter.py#L19)

```python
def wait(name: str, WaiterConfig: Dict[str, Any] = None) -> None:
```
