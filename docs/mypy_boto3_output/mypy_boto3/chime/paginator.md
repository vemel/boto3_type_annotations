# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.chime.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Chime](index.md#chime) / Paginator
    - [ListAccounts](#listaccounts)
        - [ListAccounts().paginate](#listaccountspaginate)
    - [ListUsers](#listusers)
        - [ListUsers().paginate](#listuserspaginate)

## ListAccounts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/paginator.py#L9)

```python
class ListAccounts(Paginator):
```

### ListAccounts().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/paginator.py#L12)

```python
def paginate(
    Name: str = None,
    UserEmail: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUsers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/paginator.py#L21)

```python
class ListUsers(Paginator):
```

### ListUsers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/chime/paginator.py#L24)

```python
def paginate(
    AccountId: str,
    UserEmail: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
