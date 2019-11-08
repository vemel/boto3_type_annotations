# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sdb.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sdb](index.md#sdb) / Paginator
    - [ListDomains](#listdomains)
        - [ListDomains().paginate](#listdomainspaginate)
    - [Select](#select)
        - [Select().paginate](#selectpaginate)

## ListDomains

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/paginator.py#L9)

```python
class ListDomains(Paginator):
```

### ListDomains().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## Select

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/paginator.py#L16)

```python
class Select(Paginator):
```

### Select().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sdb/paginator.py#L19)

```python
def paginate(
    SelectExpression: str,
    ConsistentRead: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
