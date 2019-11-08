# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.shield.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Shield](index.md#shield) / Paginator
    - [ListAttacks](#listattacks)
        - [ListAttacks().paginate](#listattackspaginate)
    - [ListProtections](#listprotections)
        - [ListProtections().paginate](#listprotectionspaginate)

## ListAttacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/paginator.py#L10)

```python
class ListAttacks(Paginator):
```

### ListAttacks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/paginator.py#L13)

```python
def paginate(
    ResourceArns: List[Any] = None,
    StartTime: Dict[str, Any] = None,
    EndTime: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListProtections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/paginator.py#L23)

```python
class ListProtections(Paginator):
```

### ListProtections().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/paginator.py#L26)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
