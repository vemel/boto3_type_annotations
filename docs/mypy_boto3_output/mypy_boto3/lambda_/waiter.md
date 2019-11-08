# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.lambda_.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Lambda](index.md#lambda) / Waiter
    - [FunctionExists](#functionexists)
        - [FunctionExists().wait](#functionexistswait)

## FunctionExists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/waiter.py#L9)

```python
class FunctionExists(Waiter):
```

### FunctionExists().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lambda_/waiter.py#L12)

```python
def wait(
    FunctionName: str,
    Qualifier: str = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
