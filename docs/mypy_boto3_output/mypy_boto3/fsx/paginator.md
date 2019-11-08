# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.fsx.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Fsx](index.md#fsx) / Paginator
    - [DescribeBackups](#describebackups)
        - [DescribeBackups().paginate](#describebackupspaginate)
    - [DescribeFileSystems](#describefilesystems)
        - [DescribeFileSystems().paginate](#describefilesystemspaginate)
    - [ListTagsForResource](#listtagsforresource)
        - [ListTagsForResource().paginate](#listtagsforresourcepaginate)

## DescribeBackups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/paginator.py#L10)

```python
class DescribeBackups(Paginator):
```

### DescribeBackups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/paginator.py#L13)

```python
def paginate(
    BackupIds: List[Any] = None,
    Filters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeFileSystems

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/paginator.py#L22)

```python
class DescribeFileSystems(Paginator):
```

### DescribeFileSystems().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/paginator.py#L25)

```python
def paginate(
    FileSystemIds: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTagsForResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/paginator.py#L31)

```python
class ListTagsForResource(Paginator):
```

### ListTagsForResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fsx/paginator.py#L34)

```python
def paginate(
    ResourceARN: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
