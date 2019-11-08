# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.efs.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Efs](index.md#efs) / Paginator
    - [DescribeFileSystems](#describefilesystems)
        - [DescribeFileSystems().paginate](#describefilesystemspaginate)
    - [DescribeMountTargets](#describemounttargets)
        - [DescribeMountTargets().paginate](#describemounttargetspaginate)
    - [DescribeTags](#describetags)
        - [DescribeTags().paginate](#describetagspaginate)

## DescribeFileSystems

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/paginator.py#L9)

```python
class DescribeFileSystems(Paginator):
```

### DescribeFileSystems().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/paginator.py#L12)

```python
def paginate(
    CreationToken: str = None,
    FileSystemId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeMountTargets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/paginator.py#L21)

```python
class DescribeMountTargets(Paginator):
```

### DescribeMountTargets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/paginator.py#L24)

```python
def paginate(
    FileSystemId: str = None,
    MountTargetId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeTags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/paginator.py#L33)

```python
class DescribeTags(Paginator):
```

### DescribeTags().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/efs/paginator.py#L36)

```python
def paginate(
    FileSystemId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
