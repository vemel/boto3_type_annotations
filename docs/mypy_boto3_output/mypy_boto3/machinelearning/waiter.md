# Waiter

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.machinelearning.waiter](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/waiter.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Machinelearning](index.md#machinelearning) / Waiter
    - [BatchPredictionAvailable](#batchpredictionavailable)
        - [BatchPredictionAvailable().wait](#batchpredictionavailablewait)
    - [DataSourceAvailable](#datasourceavailable)
        - [DataSourceAvailable().wait](#datasourceavailablewait)
    - [EvaluationAvailable](#evaluationavailable)
        - [EvaluationAvailable().wait](#evaluationavailablewait)
    - [MLModelAvailable](#mlmodelavailable)
        - [MLModelAvailable().wait](#mlmodelavailablewait)

## BatchPredictionAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/waiter.py#L9)

```python
class BatchPredictionAvailable(Waiter):
```

### BatchPredictionAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/waiter.py#L12)

```python
def wait(
    FilterVariable: str = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    Limit: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## DataSourceAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/waiter.py#L30)

```python
class DataSourceAvailable(Waiter):
```

### DataSourceAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/waiter.py#L33)

```python
def wait(
    FilterVariable: str = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    Limit: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## EvaluationAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/waiter.py#L51)

```python
class EvaluationAvailable(Waiter):
```

### EvaluationAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/waiter.py#L54)

```python
def wait(
    FilterVariable: str = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    Limit: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```

## MLModelAvailable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/waiter.py#L72)

```python
class MLModelAvailable(Waiter):
```

### MLModelAvailable().wait

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/waiter.py#L75)

```python
def wait(
    FilterVariable: str = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    Limit: int = None,
    WaiterConfig: Dict[str, Any] = None,
) -> None:
```
