# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ram.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ram](index.md#ram) / Paginator
    - [GetResourcePolicies](#getresourcepolicies)
        - [GetResourcePolicies().paginate](#getresourcepoliciespaginate)
    - [GetResourceShareAssociations](#getresourceshareassociations)
        - [GetResourceShareAssociations().paginate](#getresourceshareassociationspaginate)
    - [GetResourceShareInvitations](#getresourceshareinvitations)
        - [GetResourceShareInvitations().paginate](#getresourceshareinvitationspaginate)
    - [GetResourceShares](#getresourceshares)
        - [GetResourceShares().paginate](#getresourcesharespaginate)
    - [ListPrincipals](#listprincipals)
        - [ListPrincipals().paginate](#listprincipalspaginate)
    - [ListResources](#listresources)
        - [ListResources().paginate](#listresourcespaginate)

## GetResourcePolicies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L10)

```python
class GetResourcePolicies(Paginator):
```

### GetResourcePolicies().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L13)

```python
def paginate(
    resourceArns: List[Any],
    principal: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetResourceShareAssociations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L22)

```python
class GetResourceShareAssociations(Paginator):
```

### GetResourceShareAssociations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L25)

```python
def paginate(
    associationType: str,
    resourceShareArns: List[Any] = None,
    resourceArn: str = None,
    principal: str = None,
    associationStatus: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetResourceShareInvitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L37)

```python
class GetResourceShareInvitations(Paginator):
```

### GetResourceShareInvitations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L40)

```python
def paginate(
    resourceShareInvitationArns: List[Any] = None,
    resourceShareArns: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetResourceShares

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L49)

```python
class GetResourceShares(Paginator):
```

### GetResourceShares().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L52)

```python
def paginate(
    resourceOwner: str,
    resourceShareArns: List[Any] = None,
    resourceShareStatus: str = None,
    name: str = None,
    tagFilters: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListPrincipals

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L64)

```python
class ListPrincipals(Paginator):
```

### ListPrincipals().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L67)

```python
def paginate(
    resourceOwner: str,
    resourceArn: str = None,
    principals: List[Any] = None,
    resourceType: str = None,
    resourceShareArns: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L79)

```python
class ListResources(Paginator):
```

### ListResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/paginator.py#L82)

```python
def paginate(
    resourceOwner: str,
    principal: str = None,
    resourceType: str = None,
    resourceArns: List[Any] = None,
    resourceShareArns: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
