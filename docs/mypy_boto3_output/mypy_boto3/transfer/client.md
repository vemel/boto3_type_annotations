# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.transfer.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Transfer](index.md#transfer) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_server](#clientcreate_server)
        - [Client().create_user](#clientcreate_user)
        - [Client().delete_server](#clientdelete_server)
        - [Client().delete_ssh_public_key](#clientdelete_ssh_public_key)
        - [Client().delete_user](#clientdelete_user)
        - [Client().describe_server](#clientdescribe_server)
        - [Client().describe_user](#clientdescribe_user)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_ssh_public_key](#clientimport_ssh_public_key)
        - [Client().list_servers](#clientlist_servers)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_users](#clientlist_users)
        - [Client().start_server](#clientstart_server)
        - [Client().stop_server](#clientstop_server)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().test_identity_provider](#clienttest_identity_provider)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_server](#clientupdate_server)
        - [Client().update_user](#clientupdate_user)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L19)

```python
def create_server(
    EndpointDetails: Dict[str, Any] = None,
    EndpointType: str = None,
    HostKey: str = None,
    IdentityProviderDetails: Dict[str, Any] = None,
    IdentityProviderType: str = None,
    LoggingRole: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L32)

```python
def create_user(
    Role: str,
    ServerId: str,
    UserName: str,
    HomeDirectory: str = None,
    HomeDirectoryType: str = None,
    HomeDirectoryMappings: List[Any] = None,
    Policy: str = None,
    SshPublicKeyBody: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L47)

```python
def delete_server(ServerId: str) -> None:
```

### Client().delete_ssh_public_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L51)

```python
def delete_ssh_public_key(
    ServerId: str,
    SshPublicKeyId: str,
    UserName: str,
) -> None:
```

### Client().delete_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L57)

```python
def delete_user(ServerId: str, UserName: str) -> None:
```

### Client().describe_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L61)

```python
def describe_server(ServerId: str) -> Dict[str, Any]:
```

### Client().describe_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L65)

```python
def describe_user(ServerId: str, UserName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L69)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L79)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L83)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_ssh_public_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L87)

```python
def import_ssh_public_key(
    ServerId: str,
    SshPublicKeyBody: str,
    UserName: str,
) -> Dict[str, Any]:
```

### Client().list_servers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L93)

```python
def list_servers(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L99)

```python
def list_tags_for_resource(
    Arn: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_users

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L105)

```python
def list_users(
    ServerId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().start_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L111)

```python
def start_server(ServerId: str) -> None:
```

### Client().stop_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L115)

```python
def stop_server(ServerId: str) -> None:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L119)

```python
def tag_resource(Arn: str, Tags: List[Any]) -> None:
```

### Client().test_identity_provider

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L123)

```python
def test_identity_provider(
    ServerId: str,
    UserName: str,
    UserPassword: str = None,
) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L129)

```python
def untag_resource(Arn: str, TagKeys: List[Any]) -> None:
```

### Client().update_server

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L133)

```python
def update_server(
    ServerId: str,
    EndpointDetails: Dict[str, Any] = None,
    EndpointType: str = None,
    HostKey: str = None,
    IdentityProviderDetails: Dict[str, Any] = None,
    LoggingRole: str = None,
) -> Dict[str, Any]:
```

### Client().update_user

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/transfer/client.py#L145)

```python
def update_user(
    ServerId: str,
    UserName: str,
    HomeDirectory: str = None,
    HomeDirectoryType: str = None,
    HomeDirectoryMappings: List[Any] = None,
    Policy: str = None,
    Role: str = None,
) -> Dict[str, Any]:
```
