# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.workmail.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Workmail](index.md#workmail) / Paginator
    - [ListAliases](#listaliases)
        - [ListAliases().paginate](#listaliasespaginate)
    - [ListGroupMembers](#listgroupmembers)
        - [ListGroupMembers().paginate](#listgroupmemberspaginate)
    - [ListGroups](#listgroups)
        - [ListGroups().paginate](#listgroupspaginate)
    - [ListMailboxPermissions](#listmailboxpermissions)
        - [ListMailboxPermissions().paginate](#listmailboxpermissionspaginate)
    - [ListOrganizations](#listorganizations)
        - [ListOrganizations().paginate](#listorganizationspaginate)
    - [ListResourceDelegates](#listresourcedelegates)
        - [ListResourceDelegates().paginate](#listresourcedelegatespaginate)
    - [ListResources](#listresources)
        - [ListResources().paginate](#listresourcespaginate)
    - [ListUsers](#listusers)
        - [ListUsers().paginate](#listuserspaginate)

## ListAliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L9)

```python
class ListAliases(Paginator):
```

### ListAliases().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L12)

```python
def paginate(
    OrganizationId: str,
    EntityId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListGroupMembers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L21)

```python
class ListGroupMembers(Paginator):
```

### ListGroupMembers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L24)

```python
def paginate(
    OrganizationId: str,
    GroupId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L30)

```python
class ListGroups(Paginator):
```

### ListGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L33)

```python
def paginate(
    OrganizationId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListMailboxPermissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L39)

```python
class ListMailboxPermissions(Paginator):
```

### ListMailboxPermissions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L42)

```python
def paginate(
    OrganizationId: str,
    EntityId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListOrganizations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L51)

```python
class ListOrganizations(Paginator):
```

### ListOrganizations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L54)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListResourceDelegates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L58)

```python
class ListResourceDelegates(Paginator):
```

### ListResourceDelegates().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L61)

```python
def paginate(
    OrganizationId: str,
    ResourceId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L70)

```python
class ListResources(Paginator):
```

### ListResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L73)

```python
def paginate(
    OrganizationId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUsers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L79)

```python
class ListUsers(Paginator):
```

### ListUsers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/paginator.py#L82)

```python
def paginate(
    OrganizationId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
