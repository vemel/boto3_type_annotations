# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudwatch.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudwatch](index.md#cloudwatch) / Waiter
    - [AlarmExists](#alarmexists)
        - [AlarmExists().wait](#alarmexistswait)

## AlarmExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/waiter.py#L10)

```python
class AlarmExists(Waiter):
```

### AlarmExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudwatch/waiter.py#L13)

```python
def wait(
    AlarmNames: List[Any] = None,
    AlarmNamePrefix: str = None,
    StateValue: str = None,
    ActionPrefix: str = None,
    MaxRecords: int = None,
    NextToken: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
