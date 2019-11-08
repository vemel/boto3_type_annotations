# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.organizations.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Organizations](index.md#organizations) / Paginator
    - [ListAWSServiceAccessForOrganization](#listawsserviceaccessfororganization)
        - [ListAWSServiceAccessForOrganization().paginate](#listawsserviceaccessfororganizationpaginate)
    - [ListAccounts](#listaccounts)
        - [ListAccounts().paginate](#listaccountspaginate)
    - [ListAccountsForParent](#listaccountsforparent)
        - [ListAccountsForParent().paginate](#listaccountsforparentpaginate)
    - [ListChildren](#listchildren)
        - [ListChildren().paginate](#listchildrenpaginate)
    - [ListCreateAccountStatus](#listcreateaccountstatus)
        - [ListCreateAccountStatus().paginate](#listcreateaccountstatuspaginate)
    - [ListHandshakesForAccount](#listhandshakesforaccount)
        - [ListHandshakesForAccount().paginate](#listhandshakesforaccountpaginate)
    - [ListHandshakesForOrganization](#listhandshakesfororganization)
        - [ListHandshakesForOrganization().paginate](#listhandshakesfororganizationpaginate)
    - [ListOrganizationalUnitsForParent](#listorganizationalunitsforparent)
        - [ListOrganizationalUnitsForParent().paginate](#listorganizationalunitsforparentpaginate)
    - [ListParents](#listparents)
        - [ListParents().paginate](#listparentspaginate)
    - [ListPolicies](#listpolicies)
        - [ListPolicies().paginate](#listpoliciespaginate)
    - [ListPoliciesForTarget](#listpoliciesfortarget)
        - [ListPoliciesForTarget().paginate](#listpoliciesfortargetpaginate)
    - [ListRoots](#listroots)
        - [ListRoots().paginate](#listrootspaginate)
    - [ListTagsForResource](#listtagsforresource)
        - [ListTagsForResource().paginate](#listtagsforresourcepaginate)
    - [ListTargetsForPolicy](#listtargetsforpolicy)
        - [ListTargetsForPolicy().paginate](#listtargetsforpolicypaginate)

## ListAWSServiceAccessForOrganization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L10)

```python
class ListAWSServiceAccessForOrganization(Paginator):
```

### ListAWSServiceAccessForOrganization().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L13)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListAccounts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L17)

```python
class ListAccounts(Paginator):
```

### ListAccounts().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L20)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListAccountsForParent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L24)

```python
class ListAccountsForParent(Paginator):
```

### ListAccountsForParent().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L27)

```python
def paginate(
    ParentId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListChildren

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L33)

```python
class ListChildren(Paginator):
```

### ListChildren().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L36)

```python
def paginate(
    ParentId: str,
    ChildType: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListCreateAccountStatus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L42)

```python
class ListCreateAccountStatus(Paginator):
```

### ListCreateAccountStatus().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L45)

```python
def paginate(
    States: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListHandshakesForAccount

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L51)

```python
class ListHandshakesForAccount(Paginator):
```

### ListHandshakesForAccount().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L54)

```python
def paginate(
    Filter: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListHandshakesForOrganization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L60)

```python
class ListHandshakesForOrganization(Paginator):
```

### ListHandshakesForOrganization().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L63)

```python
def paginate(
    Filter: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListOrganizationalUnitsForParent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L69)

```python
class ListOrganizationalUnitsForParent(Paginator):
```

### ListOrganizationalUnitsForParent().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L72)

```python
def paginate(
    ParentId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListParents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L78)

```python
class ListParents(Paginator):
```

### ListParents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L81)

```python
def paginate(
    ChildId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L87)

```python
class ListPolicies(Paginator):
```

### ListPolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L90)

```python
def paginate(
    Filter: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPoliciesForTarget

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L96)

```python
class ListPoliciesForTarget(Paginator):
```

### ListPoliciesForTarget().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L99)

```python
def paginate(
    TargetId: str,
    Filter: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRoots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L105)

```python
class ListRoots(Paginator):
```

### ListRoots().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L108)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListTagsForResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L112)

```python
class ListTagsForResource(Paginator):
```

### ListTagsForResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L115)

```python
def paginate(
    ResourceId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTargetsForPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L121)

```python
class ListTargetsForPolicy(Paginator):
```

### ListTargetsForPolicy().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/paginator.py#L124)

```python
def paginate(
    PolicyId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
