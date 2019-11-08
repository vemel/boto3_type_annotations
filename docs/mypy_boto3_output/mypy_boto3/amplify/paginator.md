# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.amplify.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Amplify](index.md#amplify) / Paginator
    - [ListApps](#listapps)
        - [ListApps().paginate](#listappspaginate)
    - [ListBranches](#listbranches)
        - [ListBranches().paginate](#listbranchespaginate)
    - [ListDomainAssociations](#listdomainassociations)
        - [ListDomainAssociations().paginate](#listdomainassociationspaginate)
    - [ListJobs](#listjobs)
        - [ListJobs().paginate](#listjobspaginate)

## ListApps

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/paginator.py#L9)

```python
class ListApps(Paginator):
```

### ListApps().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListBranches

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/paginator.py#L16)

```python
class ListBranches(Paginator):
```

### ListBranches().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/paginator.py#L19)

```python
def paginate(
    appId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDomainAssociations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/paginator.py#L25)

```python
class ListDomainAssociations(Paginator):
```

### ListDomainAssociations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/paginator.py#L28)

```python
def paginate(
    appId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/paginator.py#L34)

```python
class ListJobs(Paginator):
```

### ListJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/paginator.py#L37)

```python
def paginate(
    appId: str,
    branchName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
