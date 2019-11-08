# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cognito_idp.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cognito Idp](index.md#cognito-idp) / Paginator
    - [AdminListGroupsForUser](#adminlistgroupsforuser)
        - [AdminListGroupsForUser().paginate](#adminlistgroupsforuserpaginate)
    - [AdminListUserAuthEvents](#adminlistuserauthevents)
        - [AdminListUserAuthEvents().paginate](#adminlistuserautheventspaginate)
    - [ListGroups](#listgroups)
        - [ListGroups().paginate](#listgroupspaginate)
    - [ListIdentityProviders](#listidentityproviders)
        - [ListIdentityProviders().paginate](#listidentityproviderspaginate)
    - [ListResourceServers](#listresourceservers)
        - [ListResourceServers().paginate](#listresourceserverspaginate)
    - [ListUserPoolClients](#listuserpoolclients)
        - [ListUserPoolClients().paginate](#listuserpoolclientspaginate)
    - [ListUserPools](#listuserpools)
        - [ListUserPools().paginate](#listuserpoolspaginate)
    - [ListUsers](#listusers)
        - [ListUsers().paginate](#listuserspaginate)
    - [ListUsersInGroup](#listusersingroup)
        - [ListUsersInGroup().paginate](#listusersingrouppaginate)

## AdminListGroupsForUser

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L10)

```python
class AdminListGroupsForUser(Paginator):
```

### AdminListGroupsForUser().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L13)

```python
def paginate(
    Username: str,
    UserPoolId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## AdminListUserAuthEvents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L19)

```python
class AdminListUserAuthEvents(Paginator):
```

### AdminListUserAuthEvents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L22)

```python
def paginate(
    UserPoolId: str,
    Username: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L28)

```python
class ListGroups(Paginator):
```

### ListGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L31)

```python
def paginate(
    UserPoolId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListIdentityProviders

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L37)

```python
class ListIdentityProviders(Paginator):
```

### ListIdentityProviders().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L40)

```python
def paginate(
    UserPoolId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListResourceServers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L46)

```python
class ListResourceServers(Paginator):
```

### ListResourceServers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L49)

```python
def paginate(
    UserPoolId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUserPoolClients

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L55)

```python
class ListUserPoolClients(Paginator):
```

### ListUserPoolClients().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L58)

```python
def paginate(
    UserPoolId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUserPools

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L64)

```python
class ListUserPools(Paginator):
```

### ListUserPools().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L67)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListUsers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L71)

```python
class ListUsers(Paginator):
```

### ListUsers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L74)

```python
def paginate(
    UserPoolId: str,
    AttributesToGet: List[Any] = None,
    Filter: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListUsersInGroup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L84)

```python
class ListUsersInGroup(Paginator):
```

### ListUsersInGroup().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_idp/paginator.py#L87)

```python
def paginate(
    UserPoolId: str,
    GroupName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
