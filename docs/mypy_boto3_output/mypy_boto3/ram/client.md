# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ram.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ram](index.md#ram) / Client
    - [Client](#client)
        - [Client().accept_resource_share_invitation](#clientaccept_resource_share_invitation)
        - [Client().associate_resource_share](#clientassociate_resource_share)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_resource_share](#clientcreate_resource_share)
        - [Client().delete_resource_share](#clientdelete_resource_share)
        - [Client().disassociate_resource_share](#clientdisassociate_resource_share)
        - [Client().enable_sharing_with_aws_organization](#clientenable_sharing_with_aws_organization)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_resource_policies](#clientget_resource_policies)
        - [Client().get_resource_share_associations](#clientget_resource_share_associations)
        - [Client().get_resource_share_invitations](#clientget_resource_share_invitations)
        - [Client().get_resource_shares](#clientget_resource_shares)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_pending_invitation_resources](#clientlist_pending_invitation_resources)
        - [Client().list_principals](#clientlist_principals)
        - [Client().list_resources](#clientlist_resources)
        - [Client().reject_resource_share_invitation](#clientreject_resource_share_invitation)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_resource_share](#clientupdate_resource_share)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L12)

```python
class Client(BaseClient):
```

### Client().accept_resource_share_invitation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L15)

```python
def accept_resource_share_invitation(
    resourceShareInvitationArn: str,
    clientToken: str = None,
) -> Dict[str, Any]:
```

### Client().associate_resource_share

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L21)

```python
def associate_resource_share(
    resourceShareArn: str,
    resourceArns: List[Any] = None,
    principals: List[Any] = None,
    clientToken: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L31)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_resource_share

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L35)

```python
def create_resource_share(
    name: str,
    resourceArns: List[Any] = None,
    principals: List[Any] = None,
    tags: List[Any] = None,
    allowExternalPrincipals: bool = None,
    clientToken: str = None,
) -> Dict[str, Any]:
```

### Client().delete_resource_share

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L47)

```python
def delete_resource_share(
    resourceShareArn: str,
    clientToken: str = None,
) -> Dict[str, Any]:
```

### Client().disassociate_resource_share

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L53)

```python
def disassociate_resource_share(
    resourceShareArn: str,
    resourceArns: List[Any] = None,
    principals: List[Any] = None,
    clientToken: str = None,
) -> Dict[str, Any]:
```

### Client().enable_sharing_with_aws_organization

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L63)

```python
def enable_sharing_with_aws_organization() -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L67)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L77)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_resource_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L81)

```python
def get_resource_policies(
    resourceArns: List[Any],
    principal: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_resource_share_associations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L91)

```python
def get_resource_share_associations(
    associationType: str,
    resourceShareArns: List[Any] = None,
    resourceArn: str = None,
    principal: str = None,
    associationStatus: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_resource_share_invitations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L104)

```python
def get_resource_share_invitations(
    resourceShareInvitationArns: List[Any] = None,
    resourceShareArns: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_resource_shares

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L114)

```python
def get_resource_shares(
    resourceOwner: str,
    resourceShareArns: List[Any] = None,
    resourceShareStatus: str = None,
    name: str = None,
    tagFilters: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L127)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_pending_invitation_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L131)

```python
def list_pending_invitation_resources(
    resourceShareInvitationArn: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_principals

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L140)

```python
def list_principals(
    resourceOwner: str,
    resourceArn: str = None,
    principals: List[Any] = None,
    resourceType: str = None,
    resourceShareArns: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L153)

```python
def list_resources(
    resourceOwner: str,
    principal: str = None,
    resourceType: str = None,
    resourceArns: List[Any] = None,
    resourceShareArns: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().reject_resource_share_invitation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L166)

```python
def reject_resource_share_invitation(
    resourceShareInvitationArn: str,
    clientToken: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L172)

```python
def tag_resource(resourceShareArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L176)

```python
def untag_resource(
    resourceShareArn: str,
    tagKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().update_resource_share

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ram/client.py#L182)

```python
def update_resource_share(
    resourceShareArn: str,
    name: str = None,
    allowExternalPrincipals: bool = None,
    clientToken: str = None,
) -> Dict[str, Any]:
```
