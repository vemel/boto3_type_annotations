# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.shield.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Shield](index.md#shield) / Client
    - [Client](#client)
        - [Client().associate_drt_log_bucket](#clientassociate_drt_log_bucket)
        - [Client().associate_drt_role](#clientassociate_drt_role)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_protection](#clientcreate_protection)
        - [Client().create_subscription](#clientcreate_subscription)
        - [Client().delete_protection](#clientdelete_protection)
        - [Client().delete_subscription](#clientdelete_subscription)
        - [Client().describe_attack](#clientdescribe_attack)
        - [Client().describe_drt_access](#clientdescribe_drt_access)
        - [Client().describe_emergency_contact_settings](#clientdescribe_emergency_contact_settings)
        - [Client().describe_protection](#clientdescribe_protection)
        - [Client().describe_subscription](#clientdescribe_subscription)
        - [Client().disassociate_drt_log_bucket](#clientdisassociate_drt_log_bucket)
        - [Client().disassociate_drt_role](#clientdisassociate_drt_role)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_subscription_state](#clientget_subscription_state)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_attacks](#clientlist_attacks)
        - [Client().list_protections](#clientlist_protections)
        - [Client().update_emergency_contact_settings](#clientupdate_emergency_contact_settings)
        - [Client().update_subscription](#clientupdate_subscription)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L12)

```python
class Client(BaseClient):
```

### Client().associate_drt_log_bucket

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L15)

```python
def associate_drt_log_bucket(LogBucket: str) -> Dict[str, Any]:
```

### Client().associate_drt_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L19)

```python
def associate_drt_role(RoleArn: str) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L23)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_protection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L27)

```python
def create_protection(Name: str, ResourceArn: str) -> Dict[str, Any]:
```

### Client().create_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L31)

```python
def create_subscription() -> Dict[str, Any]:
```

### Client().delete_protection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L35)

```python
def delete_protection(ProtectionId: str) -> Dict[str, Any]:
```

### Client().delete_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L39)

```python
def delete_subscription() -> Dict[str, Any]:
```

### Client().describe_attack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L43)

```python
def describe_attack(AttackId: str) -> Dict[str, Any]:
```

### Client().describe_drt_access

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L47)

```python
def describe_drt_access() -> Dict[str, Any]:
```

### Client().describe_emergency_contact_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L51)

```python
def describe_emergency_contact_settings() -> Dict[str, Any]:
```

### Client().describe_protection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L55)

```python
def describe_protection(
    ProtectionId: str = None,
    ResourceArn: str = None,
) -> Dict[str, Any]:
```

### Client().describe_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L61)

```python
def describe_subscription() -> Dict[str, Any]:
```

### Client().disassociate_drt_log_bucket

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L65)

```python
def disassociate_drt_log_bucket(LogBucket: str) -> Dict[str, Any]:
```

### Client().disassociate_drt_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L69)

```python
def disassociate_drt_role() -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L73)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L83)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_subscription_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L87)

```python
def get_subscription_state() -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L91)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_attacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L95)

```python
def list_attacks(
    ResourceArns: List[Any] = None,
    StartTime: Dict[str, Any] = None,
    EndTime: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_protections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L106)

```python
def list_protections(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().update_emergency_contact_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L112)

```python
def update_emergency_contact_settings(
    EmergencyContactList: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_subscription

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/shield/client.py#L118)

```python
def update_subscription(AutoRenew: str = None) -> Dict[str, Any]:
```
