# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.organizations.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Organizations](index.md#organizations) / Client
    - [Client](#client)
        - [Client().accept_handshake](#clientaccept_handshake)
        - [Client().attach_policy](#clientattach_policy)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_handshake](#clientcancel_handshake)
        - [Client().create_account](#clientcreate_account)
        - [Client().create_gov_cloud_account](#clientcreate_gov_cloud_account)
        - [Client().create_organization](#clientcreate_organization)
        - [Client().create_organizational_unit](#clientcreate_organizational_unit)
        - [Client().create_policy](#clientcreate_policy)
        - [Client().decline_handshake](#clientdecline_handshake)
        - [Client().delete_organization](#clientdelete_organization)
        - [Client().delete_organizational_unit](#clientdelete_organizational_unit)
        - [Client().delete_policy](#clientdelete_policy)
        - [Client().describe_account](#clientdescribe_account)
        - [Client().describe_create_account_status](#clientdescribe_create_account_status)
        - [Client().describe_handshake](#clientdescribe_handshake)
        - [Client().describe_organization](#clientdescribe_organization)
        - [Client().describe_organizational_unit](#clientdescribe_organizational_unit)
        - [Client().describe_policy](#clientdescribe_policy)
        - [Client().detach_policy](#clientdetach_policy)
        - [Client().disable_aws_service_access](#clientdisable_aws_service_access)
        - [Client().disable_policy_type](#clientdisable_policy_type)
        - [Client().enable_all_features](#clientenable_all_features)
        - [Client().enable_aws_service_access](#clientenable_aws_service_access)
        - [Client().enable_policy_type](#clientenable_policy_type)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().invite_account_to_organization](#clientinvite_account_to_organization)
        - [Client().leave_organization](#clientleave_organization)
        - [Client().list_accounts](#clientlist_accounts)
        - [Client().list_accounts_for_parent](#clientlist_accounts_for_parent)
        - [Client().list_aws_service_access_for_organization](#clientlist_aws_service_access_for_organization)
        - [Client().list_children](#clientlist_children)
        - [Client().list_create_account_status](#clientlist_create_account_status)
        - [Client().list_handshakes_for_account](#clientlist_handshakes_for_account)
        - [Client().list_handshakes_for_organization](#clientlist_handshakes_for_organization)
        - [Client().list_organizational_units_for_parent](#clientlist_organizational_units_for_parent)
        - [Client().list_parents](#clientlist_parents)
        - [Client().list_policies](#clientlist_policies)
        - [Client().list_policies_for_target](#clientlist_policies_for_target)
        - [Client().list_roots](#clientlist_roots)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_targets_for_policy](#clientlist_targets_for_policy)
        - [Client().move_account](#clientmove_account)
        - [Client().remove_account_from_organization](#clientremove_account_from_organization)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_organizational_unit](#clientupdate_organizational_unit)
        - [Client().update_policy](#clientupdate_policy)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L12)

```python
class Client(BaseClient):
```

### Client().accept_handshake

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L15)

```python
def accept_handshake(HandshakeId: str) -> Dict[str, Any]:
```

### Client().attach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L19)

```python
def attach_policy(PolicyId: str, TargetId: str) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L23)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_handshake

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L27)

```python
def cancel_handshake(HandshakeId: str) -> Dict[str, Any]:
```

### Client().create_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L31)

```python
def create_account(
    Email: str,
    AccountName: str,
    RoleName: str = None,
    IamUserAccessToBilling: str = None,
) -> Dict[str, Any]:
```

### Client().create_gov_cloud_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L41)

```python
def create_gov_cloud_account(
    Email: str,
    AccountName: str,
    RoleName: str = None,
    IamUserAccessToBilling: str = None,
) -> Dict[str, Any]:
```

### Client().create_organization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L51)

```python
def create_organization(FeatureSet: str = None) -> Dict[str, Any]:
```

### Client().create_organizational_unit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L55)

```python
def create_organizational_unit(ParentId: str, Name: str) -> Dict[str, Any]:
```

### Client().create_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L59)

```python
def create_policy(
    Content: str,
    Description: str,
    Name: str,
    Type: str,
) -> Dict[str, Any]:
```

### Client().decline_handshake

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L65)

```python
def decline_handshake(HandshakeId: str) -> Dict[str, Any]:
```

### Client().delete_organization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L69)

```python
def delete_organization() -> None:
```

### Client().delete_organizational_unit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L73)

```python
def delete_organizational_unit(OrganizationalUnitId: str) -> None:
```

### Client().delete_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L77)

```python
def delete_policy(PolicyId: str) -> None:
```

### Client().describe_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L81)

```python
def describe_account(AccountId: str) -> Dict[str, Any]:
```

### Client().describe_create_account_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L85)

```python
def describe_create_account_status(
    CreateAccountRequestId: str,
) -> Dict[str, Any]:
```

### Client().describe_handshake

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L91)

```python
def describe_handshake(HandshakeId: str) -> Dict[str, Any]:
```

### Client().describe_organization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L95)

```python
def describe_organization() -> Dict[str, Any]:
```

### Client().describe_organizational_unit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L99)

```python
def describe_organizational_unit(OrganizationalUnitId: str) -> Dict[str, Any]:
```

### Client().describe_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L103)

```python
def describe_policy(PolicyId: str) -> Dict[str, Any]:
```

### Client().detach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L107)

```python
def detach_policy(PolicyId: str, TargetId: str) -> None:
```

### Client().disable_aws_service_access

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L111)

```python
def disable_aws_service_access(ServicePrincipal: str) -> None:
```

### Client().disable_policy_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L115)

```python
def disable_policy_type(RootId: str, PolicyType: str) -> Dict[str, Any]:
```

### Client().enable_all_features

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L119)

```python
def enable_all_features() -> Dict[str, Any]:
```

### Client().enable_aws_service_access

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L123)

```python
def enable_aws_service_access(ServicePrincipal: str) -> None:
```

### Client().enable_policy_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L127)

```python
def enable_policy_type(RootId: str, PolicyType: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L131)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L141)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L145)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().invite_account_to_organization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L149)

```python
def invite_account_to_organization(
    Target: Dict[str, Any],
    Notes: str = None,
) -> Dict[str, Any]:
```

### Client().leave_organization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L155)

```python
def leave_organization() -> None:
```

### Client().list_accounts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L159)

```python
def list_accounts(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_accounts_for_parent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L165)

```python
def list_accounts_for_parent(
    ParentId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_aws_service_access_for_organization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L171)

```python
def list_aws_service_access_for_organization(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_children

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L177)

```python
def list_children(
    ParentId: str,
    ChildType: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_create_account_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L187)

```python
def list_create_account_status(
    States: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_handshakes_for_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L193)

```python
def list_handshakes_for_account(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_handshakes_for_organization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L202)

```python
def list_handshakes_for_organization(
    Filter: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_organizational_units_for_parent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L211)

```python
def list_organizational_units_for_parent(
    ParentId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_parents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L217)

```python
def list_parents(
    ChildId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L223)

```python
def list_policies(
    Filter: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_policies_for_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L229)

```python
def list_policies_for_target(
    TargetId: str,
    Filter: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_roots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L235)

```python
def list_roots(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L241)

```python
def list_tags_for_resource(
    ResourceId: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_targets_for_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L247)

```python
def list_targets_for_policy(
    PolicyId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().move_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L253)

```python
def move_account(
    AccountId: str,
    SourceParentId: str,
    DestinationParentId: str,
) -> None:
```

### Client().remove_account_from_organization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L259)

```python
def remove_account_from_organization(AccountId: str) -> None:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L263)

```python
def tag_resource(ResourceId: str, Tags: List[Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L267)

```python
def untag_resource(ResourceId: str, TagKeys: List[Any]) -> None:
```

### Client().update_organizational_unit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L271)

```python
def update_organizational_unit(
    OrganizationalUnitId: str,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().update_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/organizations/client.py#L277)

```python
def update_policy(
    PolicyId: str,
    Name: str = None,
    Description: str = None,
    Content: str = None,
) -> Dict[str, Any]:
```
