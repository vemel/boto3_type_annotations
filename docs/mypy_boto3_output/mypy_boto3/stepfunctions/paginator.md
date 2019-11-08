# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.stepfunctions.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Stepfunctions](index.md#stepfunctions) / Paginator
    - [GetExecutionHistory](#getexecutionhistory)
        - [GetExecutionHistory().paginate](#getexecutionhistorypaginate)
    - [ListActivities](#listactivities)
        - [ListActivities().paginate](#listactivitiespaginate)
    - [ListExecutions](#listexecutions)
        - [ListExecutions().paginate](#listexecutionspaginate)
    - [ListStateMachines](#liststatemachines)
        - [ListStateMachines().paginate](#liststatemachinespaginate)

## GetExecutionHistory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/paginator.py#L9)

```python
class GetExecutionHistory(Paginator):
```

### GetExecutionHistory().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/paginator.py#L12)

```python
def paginate(
    executionArn: str,
    reverseOrder: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListActivities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/paginator.py#L21)

```python
class ListActivities(Paginator):
```

### ListActivities().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/paginator.py#L24)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListExecutions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/paginator.py#L28)

```python
class ListExecutions(Paginator):
```

### ListExecutions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/paginator.py#L31)

```python
def paginate(
    stateMachineArn: str,
    statusFilter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListStateMachines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/paginator.py#L40)

```python
class ListStateMachines(Paginator):
```

### ListStateMachines().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/stepfunctions/paginator.py#L43)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
