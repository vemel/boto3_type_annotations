# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.eks.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Eks](index.md#eks) / Paginator
    - [ListClusters](#listclusters)
        - [ListClusters().paginate](#listclusterspaginate)
    - [ListUpdates](#listupdates)
        - [ListUpdates().paginate](#listupdatespaginate)

## ListClusters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/paginator.py#L9)

```python
class ListClusters(Paginator):
```

### ListClusters().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListUpdates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/paginator.py#L16)

```python
class ListUpdates(Paginator):
```

### ListUpdates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/eks/paginator.py#L19)

```python
def paginate(
    name: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
