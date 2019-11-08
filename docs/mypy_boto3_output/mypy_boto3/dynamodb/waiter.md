# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.dynamodb.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Dynamodb](index.md#dynamodb) / Waiter
    - [TableExists](#tableexists)
        - [TableExists().wait](#tableexistswait)
    - [TableNotExists](#tablenotexists)
        - [TableNotExists().wait](#tablenotexistswait)

## TableExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/waiter.py#L9)

```python
class TableExists(Waiter):
```

### TableExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/waiter.py#L12)

```python
def wait(TableName: str, WaiterConfig: Dict[str, Any] = None) -> None:
```

## TableNotExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/waiter.py#L16)

```python
class TableNotExists(Waiter):
```

### TableNotExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/dynamodb/waiter.py#L19)

```python
def wait(TableName: str, WaiterConfig: Dict[str, Any] = None) -> None:
```
