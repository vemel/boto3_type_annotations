# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.emr.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Emr](index.md#emr) / Waiter
    - [ClusterRunning](#clusterrunning)
        - [ClusterRunning().wait](#clusterrunningwait)
    - [ClusterTerminated](#clusterterminated)
        - [ClusterTerminated().wait](#clusterterminatedwait)
    - [StepComplete](#stepcomplete)
        - [StepComplete().wait](#stepcompletewait)

## ClusterRunning

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/waiter.py#L9)

```python
class ClusterRunning(Waiter):
```

### ClusterRunning().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/waiter.py#L12)

```python
def wait(ClusterId: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## ClusterTerminated

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/waiter.py#L16)

```python
class ClusterTerminated(Waiter):
```

### ClusterTerminated().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/waiter.py#L19)

```python
def wait(ClusterId: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## StepComplete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/waiter.py#L23)

```python
class StepComplete(Waiter):
```

### StepComplete().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/emr/waiter.py#L26)

```python
def wait(
    ClusterId: str,
    StepId: str,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
