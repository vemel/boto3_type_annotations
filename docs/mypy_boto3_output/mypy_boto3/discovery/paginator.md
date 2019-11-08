# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.discovery.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Discovery](index.md#discovery) / Paginator
    - [DescribeAgents](#describeagents)
        - [DescribeAgents().paginate](#describeagentspaginate)
    - [DescribeContinuousExports](#describecontinuousexports)
        - [DescribeContinuousExports().paginate](#describecontinuousexportspaginate)
    - [DescribeExportConfigurations](#describeexportconfigurations)
        - [DescribeExportConfigurations().paginate](#describeexportconfigurationspaginate)
    - [DescribeExportTasks](#describeexporttasks)
        - [DescribeExportTasks().paginate](#describeexporttaskspaginate)
    - [DescribeTags](#describetags)
        - [DescribeTags().paginate](#describetagspaginate)
    - [ListConfigurations](#listconfigurations)
        - [ListConfigurations().paginate](#listconfigurationspaginate)

## DescribeAgents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L10)

```python
class DescribeAgents(Paginator):
```

### DescribeAgents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L13)

```python
def paginate(
    agentIds: List[Any] = None,
    filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeContinuousExports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L22)

```python
class DescribeContinuousExports(Paginator):
```

### DescribeContinuousExports().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L25)

```python
def paginate(
    exportIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeExportConfigurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L31)

```python
class DescribeExportConfigurations(Paginator):
```

### DescribeExportConfigurations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L34)

```python
def paginate(
    exportIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeExportTasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L40)

```python
class DescribeExportTasks(Paginator):
```

### DescribeExportTasks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L43)

```python
def paginate(
    exportIds: List[Any] = None,
    filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeTags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L52)

```python
class DescribeTags(Paginator):
```

### DescribeTags().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L55)

```python
def paginate(
    filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListConfigurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L61)

```python
class ListConfigurations(Paginator):
```

### ListConfigurations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/discovery/paginator.py#L64)

```python
def paginate(
    configurationType: str,
    filters: List[Any] = None,
    orderBy: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
