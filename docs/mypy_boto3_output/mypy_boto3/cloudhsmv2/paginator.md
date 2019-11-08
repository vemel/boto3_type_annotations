# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudhsmv2.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudhsmv2](index.md#cloudhsmv2) / Paginator
    - [DescribeBackups](#describebackups)
        - [DescribeBackups().paginate](#describebackupspaginate)
    - [DescribeClusters](#describeclusters)
        - [DescribeClusters().paginate](#describeclusterspaginate)
    - [ListTags](#listtags)
        - [ListTags().paginate](#listtagspaginate)

## DescribeBackups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/paginator.py#L9)

```python
class DescribeBackups(Paginator):
```

### DescribeBackups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/paginator.py#L12)

```python
def paginate(
    Filters: Dict[str, Any] = None,
    SortAscending: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/paginator.py#L21)

```python
class DescribeClusters(Paginator):
```

### DescribeClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/paginator.py#L24)

```python
def paginate(
    Filters: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/paginator.py#L30)

```python
class ListTags(Paginator):
```

### ListTags().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudhsmv2/paginator.py#L33)

```python
def paginate(
    ResourceId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
