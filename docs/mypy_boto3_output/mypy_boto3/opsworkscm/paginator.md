# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.opsworkscm.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Opsworkscm](index.md#opsworkscm) / Paginator
    - [DescribeBackups](#describebackups)
        - [DescribeBackups().paginate](#describebackupspaginate)
    - [DescribeEvents](#describeevents)
        - [DescribeEvents().paginate](#describeeventspaginate)
    - [DescribeServers](#describeservers)
        - [DescribeServers().paginate](#describeserverspaginate)

## DescribeBackups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/paginator.py#L9)

```python
class DescribeBackups(Paginator):
```

### DescribeBackups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/paginator.py#L12)

```python
def paginate(
    BackupId: str = None,
    ServerName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/paginator.py#L21)

```python
class DescribeEvents(Paginator):
```

### DescribeEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/paginator.py#L24)

```python
def paginate(
    ServerName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeServers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/paginator.py#L30)

```python
class DescribeServers(Paginator):
```

### DescribeServers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/opsworkscm/paginator.py#L33)

```python
def paginate(
    ServerName: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
