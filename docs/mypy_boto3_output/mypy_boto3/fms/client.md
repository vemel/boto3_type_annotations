# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.fms.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Fms](index.md#fms) / Client
    - [Client](#client)
        - [Client().associate_admin_account](#clientassociate_admin_account)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().delete_notification_channel](#clientdelete_notification_channel)
        - [Client().delete_policy](#clientdelete_policy)
        - [Client().disassociate_admin_account](#clientdisassociate_admin_account)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_admin_account](#clientget_admin_account)
        - [Client().get_compliance_detail](#clientget_compliance_detail)
        - [Client().get_notification_channel](#clientget_notification_channel)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_policy](#clientget_policy)
        - [Client().get_protection_status](#clientget_protection_status)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_compliance_status](#clientlist_compliance_status)
        - [Client().list_member_accounts](#clientlist_member_accounts)
        - [Client().list_policies](#clientlist_policies)
        - [Client().put_notification_channel](#clientput_notification_channel)
        - [Client().put_policy](#clientput_policy)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_admin_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L15)

```python
def associate_admin_account(AdminAccount: str) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().delete_notification_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L23)

```python
def delete_notification_channel() -> None:
```

### Client().delete_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L27)

```python
def delete_policy(
    PolicyId: str,
    DeleteAllPolicyResources: bool = None,
) -> None:
```

### Client().disassociate_admin_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L33)

```python
def disassociate_admin_account() -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L37)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_admin_account

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L47)

```python
def get_admin_account() -> Dict[str, Any]:
```

### Client().get_compliance_detail

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L51)

```python
def get_compliance_detail(
    PolicyId: str,
    MemberAccount: str,
) -> Dict[str, Any]:
```

### Client().get_notification_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L57)

```python
def get_notification_channel() -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L61)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L65)

```python
def get_policy(PolicyId: str) -> Dict[str, Any]:
```

### Client().get_protection_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L69)

```python
def get_protection_status(
    PolicyId: str,
    MemberAccountId: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L81)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_compliance_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L85)

```python
def list_compliance_status(
    PolicyId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_member_accounts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L91)

```python
def list_member_accounts(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L97)

```python
def list_policies(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().put_notification_channel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L103)

```python
def put_notification_channel(SnsTopicArn: str, SnsRoleName: str) -> None:
```

### Client().put_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/fms/client.py#L107)

```python
def put_policy(Policy: Dict[str, Any]) -> Dict[str, Any]:
```
