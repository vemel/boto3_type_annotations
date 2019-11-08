# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.glacier.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Glacier](index.md#glacier) / Client
    - [Client](#client)
        - [Client().abort_multipart_upload](#clientabort_multipart_upload)
        - [Client().abort_vault_lock](#clientabort_vault_lock)
        - [Client().add_tags_to_vault](#clientadd_tags_to_vault)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().complete_multipart_upload](#clientcomplete_multipart_upload)
        - [Client().complete_vault_lock](#clientcomplete_vault_lock)
        - [Client().create_vault](#clientcreate_vault)
        - [Client().delete_archive](#clientdelete_archive)
        - [Client().delete_vault](#clientdelete_vault)
        - [Client().delete_vault_access_policy](#clientdelete_vault_access_policy)
        - [Client().delete_vault_notifications](#clientdelete_vault_notifications)
        - [Client().describe_job](#clientdescribe_job)
        - [Client().describe_vault](#clientdescribe_vault)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_data_retrieval_policy](#clientget_data_retrieval_policy)
        - [Client().get_job_output](#clientget_job_output)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_vault_access_policy](#clientget_vault_access_policy)
        - [Client().get_vault_lock](#clientget_vault_lock)
        - [Client().get_vault_notifications](#clientget_vault_notifications)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().initiate_job](#clientinitiate_job)
        - [Client().initiate_multipart_upload](#clientinitiate_multipart_upload)
        - [Client().initiate_vault_lock](#clientinitiate_vault_lock)
        - [Client().list_jobs](#clientlist_jobs)
        - [Client().list_multipart_uploads](#clientlist_multipart_uploads)
        - [Client().list_parts](#clientlist_parts)
        - [Client().list_provisioned_capacity](#clientlist_provisioned_capacity)
        - [Client().list_tags_for_vault](#clientlist_tags_for_vault)
        - [Client().list_vaults](#clientlist_vaults)
        - [Client().purchase_provisioned_capacity](#clientpurchase_provisioned_capacity)
        - [Client().remove_tags_from_vault](#clientremove_tags_from_vault)
        - [Client().set_data_retrieval_policy](#clientset_data_retrieval_policy)
        - [Client().set_vault_access_policy](#clientset_vault_access_policy)
        - [Client().set_vault_notifications](#clientset_vault_notifications)
        - [Client().upload_archive](#clientupload_archive)
        - [Client().upload_multipart_part](#clientupload_multipart_part)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L14)

```python
class Client(BaseClient):
```

### Client().abort_multipart_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L17)

```python
def abort_multipart_upload(
    vaultName: str,
    uploadId: str,
    accountId: str = None,
) -> None:
```

### Client().abort_vault_lock

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L23)

```python
def abort_vault_lock(vaultName: str, accountId: str = None) -> None:
```

### Client().add_tags_to_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L27)

```python
def add_tags_to_vault(
    vaultName: str,
    accountId: str = None,
    Tags: Dict[str, Any] = None,
) -> None:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L33)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().complete_multipart_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L37)

```python
def complete_multipart_upload(
    vaultName: str,
    uploadId: str,
    accountId: str = None,
    archiveSize: str = None,
    checksum: str = None,
) -> Dict[str, Any]:
```

### Client().complete_vault_lock

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L48)

```python
def complete_vault_lock(
    vaultName: str,
    lockId: str,
    accountId: str = None,
) -> None:
```

### Client().create_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L54)

```python
def create_vault(vaultName: str, accountId: str = None) -> Dict[str, Any]:
```

### Client().delete_archive

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L58)

```python
def delete_archive(
    vaultName: str,
    archiveId: str,
    accountId: str = None,
) -> None:
```

### Client().delete_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L64)

```python
def delete_vault(vaultName: str, accountId: str = None) -> None:
```

### Client().delete_vault_access_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L68)

```python
def delete_vault_access_policy(vaultName: str, accountId: str = None) -> None:
```

### Client().delete_vault_notifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L72)

```python
def delete_vault_notifications(vaultName: str, accountId: str = None) -> None:
```

### Client().describe_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L76)

```python
def describe_job(
    vaultName: str,
    jobId: str,
    accountId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L82)

```python
def describe_vault(vaultName: str, accountId: str = None) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L86)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_data_retrieval_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L96)

```python
def get_data_retrieval_policy(accountId: str = None) -> Dict[str, Any]:
```

### Client().get_job_output

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L100)

```python
def get_job_output(
    vaultName: str,
    jobId: str,
    accountId: str = None,
    range: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L106)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_vault_access_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L110)

```python
def get_vault_access_policy(
    vaultName: str,
    accountId: str = None,
) -> Dict[str, Any]:
```

### Client().get_vault_lock

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L116)

```python
def get_vault_lock(vaultName: str, accountId: str = None) -> Dict[str, Any]:
```

### Client().get_vault_notifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L120)

```python
def get_vault_notifications(
    vaultName: str,
    accountId: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L126)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().initiate_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L130)

```python
def initiate_job(
    vaultName: str,
    accountId: str = None,
    jobParameters: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().initiate_multipart_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L139)

```python
def initiate_multipart_upload(
    vaultName: str,
    accountId: str = None,
    archiveDescription: str = None,
    partSize: str = None,
) -> Dict[str, Any]:
```

### Client().initiate_vault_lock

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L149)

```python
def initiate_vault_lock(
    vaultName: str,
    accountId: str = None,
    policy: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L155)

```python
def list_jobs(
    vaultName: str,
    accountId: str = None,
    limit: str = None,
    marker: str = None,
    statuscode: str = None,
    completed: str = None,
) -> Dict[str, Any]:
```

### Client().list_multipart_uploads

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L167)

```python
def list_multipart_uploads(
    vaultName: str,
    accountId: str = None,
    marker: str = None,
    limit: str = None,
) -> Dict[str, Any]:
```

### Client().list_parts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L177)

```python
def list_parts(
    vaultName: str,
    uploadId: str,
    accountId: str = None,
    marker: str = None,
    limit: str = None,
) -> Dict[str, Any]:
```

### Client().list_provisioned_capacity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L188)

```python
def list_provisioned_capacity(accountId: str = None) -> Dict[str, Any]:
```

### Client().list_tags_for_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L192)

```python
def list_tags_for_vault(
    vaultName: str,
    accountId: str = None,
) -> Dict[str, Any]:
```

### Client().list_vaults

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L198)

```python
def list_vaults(
    accountId: str = None,
    marker: str = None,
    limit: str = None,
) -> Dict[str, Any]:
```

### Client().purchase_provisioned_capacity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L204)

```python
def purchase_provisioned_capacity(accountId: str = None) -> Dict[str, Any]:
```

### Client().remove_tags_from_vault

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L208)

```python
def remove_tags_from_vault(
    vaultName: str,
    accountId: str = None,
    TagKeys: List[Any] = None,
) -> None:
```

### Client().set_data_retrieval_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L214)

```python
def set_data_retrieval_policy(
    accountId: str = None,
    Policy: Dict[str, Any] = None,
) -> None:
```

### Client().set_vault_access_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L220)

```python
def set_vault_access_policy(
    vaultName: str,
    accountId: str = None,
    policy: Dict[str, Any] = None,
) -> None:
```

### Client().set_vault_notifications

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L226)

```python
def set_vault_notifications(
    vaultName: str,
    accountId: str = None,
    vaultNotificationConfig: Dict[str, Any] = None,
) -> None:
```

### Client().upload_archive

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L235)

```python
def upload_archive(
    vaultName: str,
    accountId: str = None,
    archiveDescription: str = None,
    checksum: str = None,
    body: Union[bytes, IO] = None,
) -> Dict[str, Any]:
```

### Client().upload_multipart_part

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glacier/client.py#L246)

```python
def upload_multipart_part(
    vaultName: str,
    uploadId: str,
    accountId: str = None,
    checksum: str = None,
    range: str = None,
    body: Union[bytes, IO] = None,
) -> Dict[str, Any]:
```
