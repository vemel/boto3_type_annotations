# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.secretsmanager.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Secretsmanager](index.md#secretsmanager) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_rotate_secret](#clientcancel_rotate_secret)
        - [Client().create_secret](#clientcreate_secret)
        - [Client().delete_resource_policy](#clientdelete_resource_policy)
        - [Client().delete_secret](#clientdelete_secret)
        - [Client().describe_secret](#clientdescribe_secret)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_random_password](#clientget_random_password)
        - [Client().get_resource_policy](#clientget_resource_policy)
        - [Client().get_secret_value](#clientget_secret_value)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_secret_version_ids](#clientlist_secret_version_ids)
        - [Client().list_secrets](#clientlist_secrets)
        - [Client().put_resource_policy](#clientput_resource_policy)
        - [Client().put_secret_value](#clientput_secret_value)
        - [Client().restore_secret](#clientrestore_secret)
        - [Client().rotate_secret](#clientrotate_secret)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_secret](#clientupdate_secret)
        - [Client().update_secret_version_stage](#clientupdate_secret_version_stage)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_rotate_secret

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L19)

```python
def cancel_rotate_secret(SecretId: str) -> Dict[str, Any]:
```

### Client().create_secret

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L23)

```python
def create_secret(
    Name: str,
    ClientRequestToken: str = None,
    Description: str = None,
    KmsKeyId: str = None,
    SecretBinary: bytes = None,
    SecretString: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_resource_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L36)

```python
def delete_resource_policy(SecretId: str) -> Dict[str, Any]:
```

### Client().delete_secret

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L40)

```python
def delete_secret(
    SecretId: str,
    RecoveryWindowInDays: int = None,
    ForceDeleteWithoutRecovery: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_secret

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L49)

```python
def describe_secret(SecretId: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L53)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L63)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_random_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L67)

```python
def get_random_password(
    PasswordLength: int = None,
    ExcludeCharacters: str = None,
    ExcludeNumbers: bool = None,
    ExcludePunctuation: bool = None,
    ExcludeUppercase: bool = None,
    ExcludeLowercase: bool = None,
    IncludeSpace: bool = None,
    RequireEachIncludedType: bool = None,
) -> Dict[str, Any]:
```

### Client().get_resource_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L81)

```python
def get_resource_policy(SecretId: str) -> Dict[str, Any]:
```

### Client().get_secret_value

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L85)

```python
def get_secret_value(
    SecretId: str,
    VersionId: str = None,
    VersionStage: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L91)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_secret_version_ids

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L95)

```python
def list_secret_version_ids(
    SecretId: str,
    MaxResults: int = None,
    NextToken: str = None,
    IncludeDeprecated: bool = None,
) -> Dict[str, Any]:
```

### Client().list_secrets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L105)

```python
def list_secrets(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().put_resource_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L111)

```python
def put_resource_policy(SecretId: str, ResourcePolicy: str) -> Dict[str, Any]:
```

### Client().put_secret_value

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L115)

```python
def put_secret_value(
    SecretId: str,
    ClientRequestToken: str = None,
    SecretBinary: bytes = None,
    SecretString: str = None,
    VersionStages: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().restore_secret

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L126)

```python
def restore_secret(SecretId: str) -> Dict[str, Any]:
```

### Client().rotate_secret

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L130)

```python
def rotate_secret(
    SecretId: str,
    ClientRequestToken: str = None,
    RotationLambdaARN: str = None,
    RotationRules: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L140)

```python
def tag_resource(SecretId: str, Tags: List[Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L144)

```python
def untag_resource(SecretId: str, TagKeys: List[Any]) -> None:
```

### Client().update_secret

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L148)

```python
def update_secret(
    SecretId: str,
    ClientRequestToken: str = None,
    Description: str = None,
    KmsKeyId: str = None,
    SecretBinary: bytes = None,
    SecretString: str = None,
) -> Dict[str, Any]:
```

### Client().update_secret_version_stage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/secretsmanager/client.py#L160)

```python
def update_secret_version_stage(
    SecretId: str,
    VersionStage: str,
    RemoveFromVersionId: str = None,
    MoveToVersionId: str = None,
) -> Dict[str, Any]:
```
