# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.athena.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Athena](index.md#athena) / Paginator
    - [GetQueryResults](#getqueryresults)
        - [GetQueryResults().paginate](#getqueryresultspaginate)
    - [ListNamedQueries](#listnamedqueries)
        - [ListNamedQueries().paginate](#listnamedqueriespaginate)
    - [ListQueryExecutions](#listqueryexecutions)
        - [ListQueryExecutions().paginate](#listqueryexecutionspaginate)

## GetQueryResults

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/paginator.py#L9)

```python
class GetQueryResults(Paginator):
```

### GetQueryResults().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/paginator.py#L12)

```python
def paginate(
    QueryExecutionId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListNamedQueries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/paginator.py#L18)

```python
class ListNamedQueries(Paginator):
```

### ListNamedQueries().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/paginator.py#L21)

```python
def paginate(
    WorkGroup: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListQueryExecutions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/paginator.py#L27)

```python
class ListQueryExecutions(Paginator):
```

### ListQueryExecutions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/athena/paginator.py#L30)

```python
def paginate(
    WorkGroup: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
