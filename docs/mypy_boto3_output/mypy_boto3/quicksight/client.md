# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.quicksight.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Quicksight](index.md#quicksight) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_group](#clientcreate_group)
        - [Client().create_group_membership](#clientcreate_group_membership)
        - [Client().delete_group](#clientdelete_group)
        - [Client().delete_group_membership](#clientdelete_group_membership)
        - [Client().delete_user](#clientdelete_user)
        - [Client().delete_user_by_principal_id](#clientdelete_user_by_principal_id)
        - [Client().describe_group](#clientdescribe_group)
        - [Client().describe_user](#clientdescribe_user)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_dashboard_embed_url](#clientget_dashboard_embed_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_group_memberships](#clientlist_group_memberships)
        - [Client().list_groups](#clientlist_groups)
        - [Client().list_user_groups](#clientlist_user_groups)
        - [Client().list_users](#clientlist_users)
        - [Client().register_user](#clientregister_user)
        - [Client().update_group](#clientupdate_group)
        - [Client().update_user](#clientupdate_user)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L18)

```python
def create_group(
    GroupName: str,
    AwsAccountId: str,
    Namespace: str,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().create_group_membership

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L24)

```python
def create_group_membership(
    MemberName: str,
    GroupName: str,
    AwsAccountId: str,
    Namespace: str,
) -> Dict[str, Any]:
```

### Client().delete_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L30)

```python
def delete_group(
    GroupName: str,
    AwsAccountId: str,
    Namespace: str,
) -> Dict[str, Any]:
```

### Client().delete_group_membership

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L36)

```python
def delete_group_membership(
    MemberName: str,
    GroupName: str,
    AwsAccountId: str,
    Namespace: str,
) -> Dict[str, Any]:
```

### Client().delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L42)

```python
def delete_user(
    UserName: str,
    AwsAccountId: str,
    Namespace: str,
) -> Dict[str, Any]:
```

### Client().delete_user_by_principal_id

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L48)

```python
def delete_user_by_principal_id(
    PrincipalId: str,
    AwsAccountId: str,
    Namespace: str,
) -> Dict[str, Any]:
```

### Client().describe_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L54)

```python
def describe_group(
    GroupName: str,
    AwsAccountId: str,
    Namespace: str,
) -> Dict[str, Any]:
```

### Client().describe_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L60)

```python
def describe_user(
    UserName: str,
    AwsAccountId: str,
    Namespace: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L66)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_dashboard_embed_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L76)

```python
def get_dashboard_embed_url(
    AwsAccountId: str,
    DashboardId: str,
    IdentityType: str,
    SessionLifetimeInMinutes: int = None,
    UndoRedoDisabled: bool = None,
    ResetDisabled: bool = None,
    UserArn: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L89)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L93)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_group_memberships

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L97)

```python
def list_group_memberships(
    GroupName: str,
    AwsAccountId: str,
    Namespace: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L108)

```python
def list_groups(
    AwsAccountId: str,
    Namespace: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_user_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L118)

```python
def list_user_groups(
    UserName: str,
    AwsAccountId: str,
    Namespace: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L129)

```python
def list_users(
    AwsAccountId: str,
    Namespace: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().register_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L139)

```python
def register_user(
    IdentityType: str,
    Email: str,
    UserRole: str,
    AwsAccountId: str,
    Namespace: str,
    IamArn: str = None,
    SessionName: str = None,
    UserName: str = None,
) -> Dict[str, Any]:
```

### Client().update_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L153)

```python
def update_group(
    GroupName: str,
    AwsAccountId: str,
    Namespace: str,
    Description: str = None,
) -> Dict[str, Any]:
```

### Client().update_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/quicksight/client.py#L159)

```python
def update_user(
    UserName: str,
    AwsAccountId: str,
    Namespace: str,
    Email: str,
    Role: str,
) -> Dict[str, Any]:
```
