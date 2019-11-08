# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sts.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sts](index.md#sts) / Client
    - [Client](#client)
        - [Client().assume_role](#clientassume_role)
        - [Client().assume_role_with_saml](#clientassume_role_with_saml)
        - [Client().assume_role_with_web_identity](#clientassume_role_with_web_identity)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().decode_authorization_message](#clientdecode_authorization_message)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_access_key_info](#clientget_access_key_info)
        - [Client().get_caller_identity](#clientget_caller_identity)
        - [Client().get_federation_token](#clientget_federation_token)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_session_token](#clientget_session_token)
        - [Client().get_waiter](#clientget_waiter)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L12)

```python
class Client(BaseClient):
```

### Client().assume_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L15)

```python
def assume_role(
    RoleArn: str,
    RoleSessionName: str,
    PolicyArns: List[Any] = None,
    Policy: str = None,
    DurationSeconds: int = None,
    ExternalId: str = None,
    SerialNumber: str = None,
    TokenCode: str = None,
) -> Dict[str, Any]:
```

### Client().assume_role_with_saml

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L29)

```python
def assume_role_with_saml(
    RoleArn: str,
    PrincipalArn: str,
    SAMLAssertion: str,
    PolicyArns: List[Any] = None,
    Policy: str = None,
    DurationSeconds: int = None,
) -> Dict[str, Any]:
```

### Client().assume_role_with_web_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L41)

```python
def assume_role_with_web_identity(
    RoleArn: str,
    RoleSessionName: str,
    WebIdentityToken: str,
    ProviderId: str = None,
    PolicyArns: List[Any] = None,
    Policy: str = None,
    DurationSeconds: int = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L54)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().decode_authorization_message

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L58)

```python
def decode_authorization_message(EncodedMessage: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L62)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_access_key_info

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L72)

```python
def get_access_key_info(AccessKeyId: str) -> Dict[str, Any]:
```

### Client().get_caller_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L76)

```python
def get_caller_identity() -> Dict[str, Any]:
```

### Client().get_federation_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L80)

```python
def get_federation_token(
    Name: str,
    Policy: str = None,
    PolicyArns: List[Any] = None,
    DurationSeconds: int = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L90)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_session_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L94)

```python
def get_session_token(
    DurationSeconds: int = None,
    SerialNumber: str = None,
    TokenCode: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sts/client.py#L103)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```
