# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.kms.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Kms](index.md#kms) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_key_deletion](#clientcancel_key_deletion)
        - [Client().connect_custom_key_store](#clientconnect_custom_key_store)
        - [Client().create_alias](#clientcreate_alias)
        - [Client().create_custom_key_store](#clientcreate_custom_key_store)
        - [Client().create_grant](#clientcreate_grant)
        - [Client().create_key](#clientcreate_key)
        - [Client().decrypt](#clientdecrypt)
        - [Client().delete_alias](#clientdelete_alias)
        - [Client().delete_custom_key_store](#clientdelete_custom_key_store)
        - [Client().delete_imported_key_material](#clientdelete_imported_key_material)
        - [Client().describe_custom_key_stores](#clientdescribe_custom_key_stores)
        - [Client().describe_key](#clientdescribe_key)
        - [Client().disable_key](#clientdisable_key)
        - [Client().disable_key_rotation](#clientdisable_key_rotation)
        - [Client().disconnect_custom_key_store](#clientdisconnect_custom_key_store)
        - [Client().enable_key](#clientenable_key)
        - [Client().enable_key_rotation](#clientenable_key_rotation)
        - [Client().encrypt](#clientencrypt)
        - [Client().generate_data_key](#clientgenerate_data_key)
        - [Client().generate_data_key_without_plaintext](#clientgenerate_data_key_without_plaintext)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().generate_random](#clientgenerate_random)
        - [Client().get_key_policy](#clientget_key_policy)
        - [Client().get_key_rotation_status](#clientget_key_rotation_status)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_parameters_for_import](#clientget_parameters_for_import)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_key_material](#clientimport_key_material)
        - [Client().list_aliases](#clientlist_aliases)
        - [Client().list_grants](#clientlist_grants)
        - [Client().list_key_policies](#clientlist_key_policies)
        - [Client().list_keys](#clientlist_keys)
        - [Client().list_resource_tags](#clientlist_resource_tags)
        - [Client().list_retirable_grants](#clientlist_retirable_grants)
        - [Client().put_key_policy](#clientput_key_policy)
        - [Client().re_encrypt](#clientre_encrypt)
        - [Client().retire_grant](#clientretire_grant)
        - [Client().revoke_grant](#clientrevoke_grant)
        - [Client().schedule_key_deletion](#clientschedule_key_deletion)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_alias](#clientupdate_alias)
        - [Client().update_custom_key_store](#clientupdate_custom_key_store)
        - [Client().update_key_description](#clientupdate_key_description)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_key_deletion

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L20)

```python
def cancel_key_deletion(KeyId: str) -> Dict[str, Any]:
```

### Client().connect_custom_key_store

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L24)

```python
def connect_custom_key_store(CustomKeyStoreId: str) -> Dict[str, Any]:
```

### Client().create_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L28)

```python
def create_alias(AliasName: str, TargetKeyId: str) -> None:
```

### Client().create_custom_key_store

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L32)

```python
def create_custom_key_store(
    CustomKeyStoreName: str,
    CloudHsmClusterId: str,
    TrustAnchorCertificate: str,
    KeyStorePassword: str,
) -> Dict[str, Any]:
```

### Client().create_grant

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L42)

```python
def create_grant(
    KeyId: str,
    GranteePrincipal: str,
    Operations: List[Any],
    RetiringPrincipal: str = None,
    Constraints: Dict[str, Any] = None,
    GrantTokens: List[Any] = None,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().create_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L55)

```python
def create_key(
    Policy: str = None,
    Description: str = None,
    KeyUsage: str = None,
    Origin: str = None,
    CustomKeyStoreId: str = None,
    BypassPolicyLockoutSafetyCheck: bool = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().decrypt

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L68)

```python
def decrypt(
    CiphertextBlob: bytes,
    EncryptionContext: Dict[str, Any] = None,
    GrantTokens: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L77)

```python
def delete_alias(AliasName: str) -> None:
```

### Client().delete_custom_key_store

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L81)

```python
def delete_custom_key_store(CustomKeyStoreId: str) -> Dict[str, Any]:
```

### Client().delete_imported_key_material

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L85)

```python
def delete_imported_key_material(KeyId: str) -> None:
```

### Client().describe_custom_key_stores

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L89)

```python
def describe_custom_key_stores(
    CustomKeyStoreId: str = None,
    CustomKeyStoreName: str = None,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().describe_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L99)

```python
def describe_key(KeyId: str, GrantTokens: List[Any] = None) -> Dict[str, Any]:
```

### Client().disable_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L103)

```python
def disable_key(KeyId: str) -> None:
```

### Client().disable_key_rotation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L107)

```python
def disable_key_rotation(KeyId: str) -> None:
```

### Client().disconnect_custom_key_store

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L111)

```python
def disconnect_custom_key_store(CustomKeyStoreId: str) -> Dict[str, Any]:
```

### Client().enable_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L115)

```python
def enable_key(KeyId: str) -> None:
```

### Client().enable_key_rotation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L119)

```python
def enable_key_rotation(KeyId: str) -> None:
```

### Client().encrypt

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L123)

```python
def encrypt(
    KeyId: str,
    Plaintext: bytes,
    EncryptionContext: Dict[str, Any] = None,
    GrantTokens: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_data_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L133)

```python
def generate_data_key(
    KeyId: str,
    EncryptionContext: Dict[str, Any] = None,
    NumberOfBytes: int = None,
    KeySpec: str = None,
    GrantTokens: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_data_key_without_plaintext

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L144)

```python
def generate_data_key_without_plaintext(
    KeyId: str,
    EncryptionContext: Dict[str, Any] = None,
    KeySpec: str = None,
    NumberOfBytes: int = None,
    GrantTokens: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L155)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().generate_random

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L165)

```python
def generate_random(
    NumberOfBytes: int = None,
    CustomKeyStoreId: str = None,
) -> Dict[str, Any]:
```

### Client().get_key_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L171)

```python
def get_key_policy(KeyId: str, PolicyName: str) -> Dict[str, Any]:
```

### Client().get_key_rotation_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L175)

```python
def get_key_rotation_status(KeyId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L179)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_parameters_for_import

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L183)

```python
def get_parameters_for_import(
    KeyId: str,
    WrappingAlgorithm: str,
    WrappingKeySpec: str,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L189)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_key_material

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L193)

```python
def import_key_material(
    KeyId: str,
    ImportToken: bytes,
    EncryptedKeyMaterial: bytes,
    ValidTo: datetime = None,
    ExpirationModel: str = None,
) -> Dict[str, Any]:
```

### Client().list_aliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L204)

```python
def list_aliases(
    KeyId: str = None,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_grants

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L210)

```python
def list_grants(
    KeyId: str,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_key_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L216)

```python
def list_key_policies(
    KeyId: str,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L222)

```python
def list_keys(Limit: int = None, Marker: str = None) -> Dict[str, Any]:
```

### Client().list_resource_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L226)

```python
def list_resource_tags(
    KeyId: str,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_retirable_grants

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L232)

```python
def list_retirable_grants(
    RetiringPrincipal: str,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().put_key_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L238)

```python
def put_key_policy(
    KeyId: str,
    PolicyName: str,
    Policy: str,
    BypassPolicyLockoutSafetyCheck: bool = None,
) -> None:
```

### Client().re_encrypt

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L248)

```python
def re_encrypt(
    CiphertextBlob: bytes,
    DestinationKeyId: str,
    SourceEncryptionContext: Dict[str, Any] = None,
    DestinationEncryptionContext: Dict[str, Any] = None,
    GrantTokens: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().retire_grant

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L259)

```python
def retire_grant(
    GrantToken: str = None,
    KeyId: str = None,
    GrantId: str = None,
) -> None:
```

### Client().revoke_grant

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L265)

```python
def revoke_grant(KeyId: str, GrantId: str) -> None:
```

### Client().schedule_key_deletion

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L269)

```python
def schedule_key_deletion(
    KeyId: str,
    PendingWindowInDays: int = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L275)

```python
def tag_resource(KeyId: str, Tags: List[Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L279)

```python
def untag_resource(KeyId: str, TagKeys: List[Any]) -> None:
```

### Client().update_alias

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L283)

```python
def update_alias(AliasName: str, TargetKeyId: str) -> None:
```

### Client().update_custom_key_store

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L287)

```python
def update_custom_key_store(
    CustomKeyStoreId: str,
    NewCustomKeyStoreName: str = None,
    KeyStorePassword: str = None,
    CloudHsmClusterId: str = None,
) -> Dict[str, Any]:
```

### Client().update_key_description

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/kms/client.py#L297)

```python
def update_key_description(KeyId: str, Description: str) -> None:
```
