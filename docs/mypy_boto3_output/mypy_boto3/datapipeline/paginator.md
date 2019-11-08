# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.datapipeline.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Datapipeline](index.md#datapipeline) / Paginator
    - [DescribeObjects](#describeobjects)
        - [DescribeObjects().paginate](#describeobjectspaginate)
    - [ListPipelines](#listpipelines)
        - [ListPipelines().paginate](#listpipelinespaginate)
    - [QueryObjects](#queryobjects)
        - [QueryObjects().paginate](#queryobjectspaginate)

## DescribeObjects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/paginator.py#L10)

```python
class DescribeObjects(Paginator):
```

### DescribeObjects().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/paginator.py#L13)

```python
def paginate(
    pipelineId: str,
    objectIds: List[Any],
    evaluateExpressions: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPipelines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/paginator.py#L23)

```python
class ListPipelines(Paginator):
```

### ListPipelines().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/paginator.py#L26)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## QueryObjects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/paginator.py#L30)

```python
class QueryObjects(Paginator):
```

### QueryObjects().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/datapipeline/paginator.py#L33)

```python
def paginate(
    pipelineId: str,
    sphere: str,
    query: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
