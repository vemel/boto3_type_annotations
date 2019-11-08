# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.macie.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Macie](index.md#macie) / Paginator
    - [ListMemberAccounts](#listmemberaccounts)
        - [ListMemberAccounts().paginate](#listmemberaccountspaginate)
    - [ListS3Resources](#lists3resources)
        - [ListS3Resources().paginate](#lists3resourcespaginate)

## ListMemberAccounts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/paginator.py#L9)

```python
class ListMemberAccounts(Paginator):
```

### ListMemberAccounts().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListS3Resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/paginator.py#L16)

```python
class ListS3Resources(Paginator):
```

### ListS3Resources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/paginator.py#L19)

```python
def paginate(
    memberAccountId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
