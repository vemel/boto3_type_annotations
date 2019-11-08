# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.securityhub.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Securityhub](index.md#securityhub) / Paginator
    - [GetEnabledStandards](#getenabledstandards)
        - [GetEnabledStandards().paginate](#getenabledstandardspaginate)
    - [GetFindings](#getfindings)
        - [GetFindings().paginate](#getfindingspaginate)
    - [GetInsights](#getinsights)
        - [GetInsights().paginate](#getinsightspaginate)
    - [ListEnabledProductsForImport](#listenabledproductsforimport)
        - [ListEnabledProductsForImport().paginate](#listenabledproductsforimportpaginate)
    - [ListInvitations](#listinvitations)
        - [ListInvitations().paginate](#listinvitationspaginate)
    - [ListMembers](#listmembers)
        - [ListMembers().paginate](#listmemberspaginate)

## GetEnabledStandards

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L10)

```python
class GetEnabledStandards(Paginator):
```

### GetEnabledStandards().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L13)

```python
def paginate(
    StandardsSubscriptionArns: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetFindings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L21)

```python
class GetFindings(Paginator):
```

### GetFindings().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L24)

```python
def paginate(
    Filters: Dict[str, Any] = None,
    SortCriteria: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetInsights

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L33)

```python
class GetInsights(Paginator):
```

### GetInsights().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L36)

```python
def paginate(
    InsightArns: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListEnabledProductsForImport

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L42)

```python
class ListEnabledProductsForImport(Paginator):
```

### ListEnabledProductsForImport().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L45)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListInvitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L49)

```python
class ListInvitations(Paginator):
```

### ListInvitations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L52)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListMembers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L56)

```python
class ListMembers(Paginator):
```

### ListMembers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/securityhub/paginator.py#L59)

```python
def paginate(
    OnlyAssociated: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
