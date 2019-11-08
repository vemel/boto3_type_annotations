# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kinesis.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kinesis](index.md#kinesis) / Waiter
    - [StreamExists](#streamexists)
        - [StreamExists().wait](#streamexistswait)
    - [StreamNotExists](#streamnotexists)
        - [StreamNotExists().wait](#streamnotexistswait)

## StreamExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/waiter.py#L9)

```python
class StreamExists(Waiter):
```

### StreamExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/waiter.py#L12)

```python
def wait(
    StreamName: str,
    Limit: int = None,
    ExclusiveStartShardId: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## StreamNotExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/waiter.py#L22)

```python
class StreamNotExists(Waiter):
```

### StreamNotExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesis/waiter.py#L25)

```python
def wait(
    StreamName: str,
    Limit: int = None,
    ExclusiveStartShardId: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
