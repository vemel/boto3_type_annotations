# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.workmail.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Workmail](index.md#workmail) / Client
    - [Client](#client)
        - [Client().associate_delegate_to_resource](#clientassociate_delegate_to_resource)
        - [Client().associate_member_to_group](#clientassociate_member_to_group)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_alias](#clientcreate_alias)
        - [Client().create_group](#clientcreate_group)
        - [Client().create_resource](#clientcreate_resource)
        - [Client().create_user](#clientcreate_user)
        - [Client().delete_alias](#clientdelete_alias)
        - [Client().delete_group](#clientdelete_group)
        - [Client().delete_mailbox_permissions](#clientdelete_mailbox_permissions)
        - [Client().delete_resource](#clientdelete_resource)
        - [Client().delete_user](#clientdelete_user)
        - [Client().deregister_from_work_mail](#clientderegister_from_work_mail)
        - [Client().describe_group](#clientdescribe_group)
        - [Client().describe_organization](#clientdescribe_organization)
        - [Client().describe_resource](#clientdescribe_resource)
        - [Client().describe_user](#clientdescribe_user)
        - [Client().disassociate_delegate_from_resource](#clientdisassociate_delegate_from_resource)
        - [Client().disassociate_member_from_group](#clientdisassociate_member_from_group)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_mailbox_details](#clientget_mailbox_details)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_aliases](#clientlist_aliases)
        - [Client().list_group_members](#clientlist_group_members)
        - [Client().list_groups](#clientlist_groups)
        - [Client().list_mailbox_permissions](#clientlist_mailbox_permissions)
        - [Client().list_organizations](#clientlist_organizations)
        - [Client().list_resource_delegates](#clientlist_resource_delegates)
        - [Client().list_resources](#clientlist_resources)
        - [Client().list_users](#clientlist_users)
        - [Client().put_mailbox_permissions](#clientput_mailbox_permissions)
        - [Client().register_to_work_mail](#clientregister_to_work_mail)
        - [Client().reset_password](#clientreset_password)
        - [Client().update_mailbox_quota](#clientupdate_mailbox_quota)
        - [Client().update_primary_email_address](#clientupdate_primary_email_address)
        - [Client().update_resource](#clientupdate_resource)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_delegate_to_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L15)

```python
def associate_delegate_to_resource(
    OrganizationId: str,
    ResourceId: str,
    EntityId: str,
) -> Dict[str, Any]:
```

### Client().associate_member_to_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L21)

```python
def associate_member_to_group(
    OrganizationId: str,
    GroupId: str,
    MemberId: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L27)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L31)

```python
def create_alias(
    OrganizationId: str,
    EntityId: str,
    Alias: str,
) -> Dict[str, Any]:
```

### Client().create_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L37)

```python
def create_group(OrganizationId: str, Name: str) -> Dict[str, Any]:
```

### Client().create_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L41)

```python
def create_resource(
    OrganizationId: str,
    Name: str,
    Type: str,
) -> Dict[str, Any]:
```

### Client().create_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L47)

```python
def create_user(
    OrganizationId: str,
    Name: str,
    DisplayName: str,
    Password: str,
) -> Dict[str, Any]:
```

### Client().delete_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L53)

```python
def delete_alias(
    OrganizationId: str,
    EntityId: str,
    Alias: str,
) -> Dict[str, Any]:
```

### Client().delete_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L59)

```python
def delete_group(OrganizationId: str, GroupId: str) -> Dict[str, Any]:
```

### Client().delete_mailbox_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L63)

```python
def delete_mailbox_permissions(
    OrganizationId: str,
    EntityId: str,
    GranteeId: str,
) -> Dict[str, Any]:
```

### Client().delete_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L69)

```python
def delete_resource(OrganizationId: str, ResourceId: str) -> Dict[str, Any]:
```

### Client().delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L73)

```python
def delete_user(OrganizationId: str, UserId: str) -> Dict[str, Any]:
```

### Client().deregister_from_work_mail

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L77)

```python
def deregister_from_work_mail(
    OrganizationId: str,
    EntityId: str,
) -> Dict[str, Any]:
```

### Client().describe_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L83)

```python
def describe_group(OrganizationId: str, GroupId: str) -> Dict[str, Any]:
```

### Client().describe_organization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L87)

```python
def describe_organization(OrganizationId: str) -> Dict[str, Any]:
```

### Client().describe_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L91)

```python
def describe_resource(OrganizationId: str, ResourceId: str) -> Dict[str, Any]:
```

### Client().describe_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L95)

```python
def describe_user(OrganizationId: str, UserId: str) -> Dict[str, Any]:
```

### Client().disassociate_delegate_from_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L99)

```python
def disassociate_delegate_from_resource(
    OrganizationId: str,
    ResourceId: str,
    EntityId: str,
) -> Dict[str, Any]:
```

### Client().disassociate_member_from_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L105)

```python
def disassociate_member_from_group(
    OrganizationId: str,
    GroupId: str,
    MemberId: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L111)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_mailbox_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L121)

```python
def get_mailbox_details(OrganizationId: str, UserId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L125)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L129)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_aliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L133)

```python
def list_aliases(
    OrganizationId: str,
    EntityId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_group_members

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L143)

```python
def list_group_members(
    OrganizationId: str,
    GroupId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L153)

```python
def list_groups(
    OrganizationId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_mailbox_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L159)

```python
def list_mailbox_permissions(
    OrganizationId: str,
    EntityId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_organizations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L169)

```python
def list_organizations(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_resource_delegates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L175)

```python
def list_resource_delegates(
    OrganizationId: str,
    ResourceId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L185)

```python
def list_resources(
    OrganizationId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L191)

```python
def list_users(
    OrganizationId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().put_mailbox_permissions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L197)

```python
def put_mailbox_permissions(
    OrganizationId: str,
    EntityId: str,
    GranteeId: str,
    PermissionValues: List[Any],
) -> Dict[str, Any]:
```

### Client().register_to_work_mail

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L207)

```python
def register_to_work_mail(
    OrganizationId: str,
    EntityId: str,
    Email: str,
) -> Dict[str, Any]:
```

### Client().reset_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L213)

```python
def reset_password(
    OrganizationId: str,
    UserId: str,
    Password: str,
) -> Dict[str, Any]:
```

### Client().update_mailbox_quota

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L219)

```python
def update_mailbox_quota(
    OrganizationId: str,
    UserId: str,
    MailboxQuota: int,
) -> Dict[str, Any]:
```

### Client().update_primary_email_address

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L225)

```python
def update_primary_email_address(
    OrganizationId: str,
    EntityId: str,
    Email: str,
) -> Dict[str, Any]:
```

### Client().update_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/workmail/client.py#L231)

```python
def update_resource(
    OrganizationId: str,
    ResourceId: str,
    Name: str = None,
    BookingOptions: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
