# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.batch.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Batch](index.md#batch) / Paginator
    - [DescribeComputeEnvironments](#describecomputeenvironments)
        - [DescribeComputeEnvironments().paginate](#describecomputeenvironmentspaginate)
    - [DescribeJobDefinitions](#describejobdefinitions)
        - [DescribeJobDefinitions().paginate](#describejobdefinitionspaginate)
    - [DescribeJobQueues](#describejobqueues)
        - [DescribeJobQueues().paginate](#describejobqueuespaginate)
    - [ListJobs](#listjobs)
        - [ListJobs().paginate](#listjobspaginate)

## DescribeComputeEnvironments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/paginator.py#L10)

```python
class DescribeComputeEnvironments(Paginator):
```

### DescribeComputeEnvironments().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/paginator.py#L13)

```python
def paginate(
    computeEnvironments: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeJobDefinitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/paginator.py#L21)

```python
class DescribeJobDefinitions(Paginator):
```

### DescribeJobDefinitions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/paginator.py#L24)

```python
def paginate(
    jobDefinitions: List[Any] = None,
    jobDefinitionName: str = None,
    status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeJobQueues

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/paginator.py#L34)

```python
class DescribeJobQueues(Paginator):
```

### DescribeJobQueues().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/paginator.py#L37)

```python
def paginate(
    jobQueues: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/paginator.py#L43)

```python
class ListJobs(Paginator):
```

### ListJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/batch/paginator.py#L46)

```python
def paginate(
    jobQueue: str = None,
    arrayJobId: str = None,
    multiNodeJobId: str = None,
    jobStatus: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
