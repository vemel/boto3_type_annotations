# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cognito_identity.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cognito Identity](index.md#cognito-identity) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_identity_pool](#clientcreate_identity_pool)
        - [Client().delete_identities](#clientdelete_identities)
        - [Client().delete_identity_pool](#clientdelete_identity_pool)
        - [Client().describe_identity](#clientdescribe_identity)
        - [Client().describe_identity_pool](#clientdescribe_identity_pool)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_credentials_for_identity](#clientget_credentials_for_identity)
        - [Client().get_id](#clientget_id)
        - [Client().get_identity_pool_roles](#clientget_identity_pool_roles)
        - [Client().get_open_id_token](#clientget_open_id_token)
        - [Client().get_open_id_token_for_developer_identity](#clientget_open_id_token_for_developer_identity)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_identities](#clientlist_identities)
        - [Client().list_identity_pools](#clientlist_identity_pools)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().lookup_developer_identity](#clientlookup_developer_identity)
        - [Client().merge_developer_identities](#clientmerge_developer_identities)
        - [Client().set_identity_pool_roles](#clientset_identity_pool_roles)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().unlink_developer_identity](#clientunlink_developer_identity)
        - [Client().unlink_identity](#clientunlink_identity)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_identity_pool](#clientupdate_identity_pool)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_identity_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L19)

```python
def create_identity_pool(
    IdentityPoolName: str,
    AllowUnauthenticatedIdentities: bool,
    SupportedLoginProviders: Dict[str, Any] = None,
    DeveloperProviderName: str = None,
    OpenIdConnectProviderARNs: List[Any] = None,
    CognitoIdentityProviders: List[Any] = None,
    SamlProviderARNs: List[Any] = None,
    IdentityPoolTags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_identities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L33)

```python
def delete_identities(IdentityIdsToDelete: List[Any]) -> Dict[str, Any]:
```

### Client().delete_identity_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L37)

```python
def delete_identity_pool(IdentityPoolId: str) -> None:
```

### Client().describe_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L41)

```python
def describe_identity(IdentityId: str) -> Dict[str, Any]:
```

### Client().describe_identity_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L45)

```python
def describe_identity_pool(IdentityPoolId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L49)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_credentials_for_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L59)

```python
def get_credentials_for_identity(
    IdentityId: str,
    Logins: Dict[str, Any] = None,
    CustomRoleArn: str = None,
) -> Dict[str, Any]:
```

### Client().get_id

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L65)

```python
def get_id(
    IdentityPoolId: str,
    AccountId: str = None,
    Logins: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_identity_pool_roles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L71)

```python
def get_identity_pool_roles(IdentityPoolId: str) -> Dict[str, Any]:
```

### Client().get_open_id_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L75)

```python
def get_open_id_token(
    IdentityId: str,
    Logins: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_open_id_token_for_developer_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L81)

```python
def get_open_id_token_for_developer_identity(
    IdentityPoolId: str,
    Logins: Dict[str, Any],
    IdentityId: str = None,
    TokenDuration: int = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L91)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L95)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_identities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L99)

```python
def list_identities(
    IdentityPoolId: str,
    MaxResults: int,
    NextToken: str = None,
    HideDisabled: bool = None,
) -> Dict[str, Any]:
```

### Client().list_identity_pools

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L109)

```python
def list_identity_pools(
    MaxResults: int,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L115)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().lookup_developer_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L119)

```python
def lookup_developer_identity(
    IdentityPoolId: str,
    IdentityId: str = None,
    DeveloperUserIdentifier: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().merge_developer_identities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L130)

```python
def merge_developer_identities(
    SourceUserIdentifier: str,
    DestinationUserIdentifier: str,
    DeveloperProviderName: str,
    IdentityPoolId: str,
) -> Dict[str, Any]:
```

### Client().set_identity_pool_roles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L140)

```python
def set_identity_pool_roles(
    IdentityPoolId: str,
    Roles: Dict[str, Any],
    RoleMappings: Dict[str, Any] = None,
) -> None:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L149)

```python
def tag_resource(
    ResourceArn: str,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().unlink_developer_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L155)

```python
def unlink_developer_identity(
    IdentityId: str,
    IdentityPoolId: str,
    DeveloperProviderName: str,
    DeveloperUserIdentifier: str,
) -> None:
```

### Client().unlink_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L165)

```python
def unlink_identity(
    IdentityId: str,
    Logins: Dict[str, Any],
    LoginsToRemove: List[Any],
) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L171)

```python
def untag_resource(
    ResourceArn: str,
    TagKeys: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_identity_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cognito_identity/client.py#L177)

```python
def update_identity_pool(
    IdentityPoolId: str,
    IdentityPoolName: str,
    AllowUnauthenticatedIdentities: bool,
    SupportedLoginProviders: Dict[str, Any] = None,
    DeveloperProviderName: str = None,
    OpenIdConnectProviderARNs: List[Any] = None,
    CognitoIdentityProviders: List[Any] = None,
    SamlProviderARNs: List[Any] = None,
    IdentityPoolTags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```
