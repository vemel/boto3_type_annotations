# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kinesisanalyticsv2.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kinesisanalyticsv2](index.md#kinesisanalyticsv2) / Paginator
    - [ListApplicationSnapshots](#listapplicationsnapshots)
        - [ListApplicationSnapshots().paginate](#listapplicationsnapshotspaginate)
    - [ListApplications](#listapplications)
        - [ListApplications().paginate](#listapplicationspaginate)

## ListApplicationSnapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/paginator.py#L9)

```python
class ListApplicationSnapshots(Paginator):
```

### ListApplicationSnapshots().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/paginator.py#L12)

```python
def paginate(
    ApplicationName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListApplications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/paginator.py#L18)

```python
class ListApplications(Paginator):
```

### ListApplications().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kinesisanalyticsv2/paginator.py#L21)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
