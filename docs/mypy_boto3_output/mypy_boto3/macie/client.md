# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.macie.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Macie](index.md#macie) / Client
    - [Client](#client)
        - [Client().associate_member_account](#clientassociate_member_account)
        - [Client().associate_s3_resources](#clientassociate_s3_resources)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().disassociate_member_account](#clientdisassociate_member_account)
        - [Client().disassociate_s3_resources](#clientdisassociate_s3_resources)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_member_accounts](#clientlist_member_accounts)
        - [Client().list_s3_resources](#clientlist_s3_resources)
        - [Client().update_s3_resources](#clientupdate_s3_resources)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_member_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L15)

```python
def associate_member_account(memberAccountId: str) -> None:
```

### Client().associate_s3_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L19)

```python
def associate_s3_resources(
    s3Resources: List[Any],
    memberAccountId: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L25)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().disassociate_member_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L29)

```python
def disassociate_member_account(memberAccountId: str) -> None:
```

### Client().disassociate_s3_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L33)

```python
def disassociate_s3_resources(
    associatedS3Resources: List[Any],
    memberAccountId: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L39)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L49)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L53)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_member_accounts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L57)

```python
def list_member_accounts(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_s3_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L63)

```python
def list_s3_resources(
    memberAccountId: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().update_s3_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/macie/client.py#L69)

```python
def update_s3_resources(
    s3ResourcesUpdate: List[Any],
    memberAccountId: str = None,
) -> Dict[str, Any]:
```
