# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.fms.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Fms](index.md#fms) / Paginator
    - [ListComplianceStatus](#listcompliancestatus)
        - [ListComplianceStatus().paginate](#listcompliancestatuspaginate)
    - [ListMemberAccounts](#listmemberaccounts)
        - [ListMemberAccounts().paginate](#listmemberaccountspaginate)
    - [ListPolicies](#listpolicies)
        - [ListPolicies().paginate](#listpoliciespaginate)

## ListComplianceStatus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/paginator.py#L9)

```python
class ListComplianceStatus(Paginator):
```

### ListComplianceStatus().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/paginator.py#L12)

```python
def paginate(
    PolicyId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListMemberAccounts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/paginator.py#L18)

```python
class ListMemberAccounts(Paginator):
```

### ListMemberAccounts().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/paginator.py#L21)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/paginator.py#L25)

```python
class ListPolicies(Paginator):
```

### ListPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/paginator.py#L28)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```
