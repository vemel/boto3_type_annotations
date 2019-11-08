# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.s3.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [S3](index.md#s3) / Client
    - [Client](#client)
        - [Client().abort_multipart_upload](#clientabort_multipart_upload)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().complete_multipart_upload](#clientcomplete_multipart_upload)
        - [Client().copy](#clientcopy)
        - [Client().copy_object](#clientcopy_object)
        - [Client().create_bucket](#clientcreate_bucket)
        - [Client().create_multipart_upload](#clientcreate_multipart_upload)
        - [Client().delete_bucket](#clientdelete_bucket)
        - [Client().delete_bucket_analytics_configuration](#clientdelete_bucket_analytics_configuration)
        - [Client().delete_bucket_cors](#clientdelete_bucket_cors)
        - [Client().delete_bucket_encryption](#clientdelete_bucket_encryption)
        - [Client().delete_bucket_inventory_configuration](#clientdelete_bucket_inventory_configuration)
        - [Client().delete_bucket_lifecycle](#clientdelete_bucket_lifecycle)
        - [Client().delete_bucket_metrics_configuration](#clientdelete_bucket_metrics_configuration)
        - [Client().delete_bucket_policy](#clientdelete_bucket_policy)
        - [Client().delete_bucket_replication](#clientdelete_bucket_replication)
        - [Client().delete_bucket_tagging](#clientdelete_bucket_tagging)
        - [Client().delete_bucket_website](#clientdelete_bucket_website)
        - [Client().delete_object](#clientdelete_object)
        - [Client().delete_object_tagging](#clientdelete_object_tagging)
        - [Client().delete_objects](#clientdelete_objects)
        - [Client().delete_public_access_block](#clientdelete_public_access_block)
        - [Client().download_file](#clientdownload_file)
        - [Client().download_fileobj](#clientdownload_fileobj)
        - [Client().generate_presigned_post](#clientgenerate_presigned_post)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_bucket_accelerate_configuration](#clientget_bucket_accelerate_configuration)
        - [Client().get_bucket_acl](#clientget_bucket_acl)
        - [Client().get_bucket_analytics_configuration](#clientget_bucket_analytics_configuration)
        - [Client().get_bucket_cors](#clientget_bucket_cors)
        - [Client().get_bucket_encryption](#clientget_bucket_encryption)
        - [Client().get_bucket_inventory_configuration](#clientget_bucket_inventory_configuration)
        - [Client().get_bucket_lifecycle](#clientget_bucket_lifecycle)
        - [Client().get_bucket_lifecycle_configuration](#clientget_bucket_lifecycle_configuration)
        - [Client().get_bucket_location](#clientget_bucket_location)
        - [Client().get_bucket_logging](#clientget_bucket_logging)
        - [Client().get_bucket_metrics_configuration](#clientget_bucket_metrics_configuration)
        - [Client().get_bucket_notification](#clientget_bucket_notification)
        - [Client().get_bucket_notification_configuration](#clientget_bucket_notification_configuration)
        - [Client().get_bucket_policy](#clientget_bucket_policy)
        - [Client().get_bucket_policy_status](#clientget_bucket_policy_status)
        - [Client().get_bucket_replication](#clientget_bucket_replication)
        - [Client().get_bucket_request_payment](#clientget_bucket_request_payment)
        - [Client().get_bucket_tagging](#clientget_bucket_tagging)
        - [Client().get_bucket_versioning](#clientget_bucket_versioning)
        - [Client().get_bucket_website](#clientget_bucket_website)
        - [Client().get_object](#clientget_object)
        - [Client().get_object_acl](#clientget_object_acl)
        - [Client().get_object_legal_hold](#clientget_object_legal_hold)
        - [Client().get_object_lock_configuration](#clientget_object_lock_configuration)
        - [Client().get_object_retention](#clientget_object_retention)
        - [Client().get_object_tagging](#clientget_object_tagging)
        - [Client().get_object_torrent](#clientget_object_torrent)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_public_access_block](#clientget_public_access_block)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().head_bucket](#clienthead_bucket)
        - [Client().head_object](#clienthead_object)
        - [Client().list_bucket_analytics_configurations](#clientlist_bucket_analytics_configurations)
        - [Client().list_bucket_inventory_configurations](#clientlist_bucket_inventory_configurations)
        - [Client().list_bucket_metrics_configurations](#clientlist_bucket_metrics_configurations)
        - [Client().list_buckets](#clientlist_buckets)
        - [Client().list_multipart_uploads](#clientlist_multipart_uploads)
        - [Client().list_object_versions](#clientlist_object_versions)
        - [Client().list_objects](#clientlist_objects)
        - [Client().list_objects_v2](#clientlist_objects_v2)
        - [Client().list_parts](#clientlist_parts)
        - [Client().put_bucket_accelerate_configuration](#clientput_bucket_accelerate_configuration)
        - [Client().put_bucket_acl](#clientput_bucket_acl)
        - [Client().put_bucket_analytics_configuration](#clientput_bucket_analytics_configuration)
        - [Client().put_bucket_cors](#clientput_bucket_cors)
        - [Client().put_bucket_encryption](#clientput_bucket_encryption)
        - [Client().put_bucket_inventory_configuration](#clientput_bucket_inventory_configuration)
        - [Client().put_bucket_lifecycle](#clientput_bucket_lifecycle)
        - [Client().put_bucket_lifecycle_configuration](#clientput_bucket_lifecycle_configuration)
        - [Client().put_bucket_logging](#clientput_bucket_logging)
        - [Client().put_bucket_metrics_configuration](#clientput_bucket_metrics_configuration)
        - [Client().put_bucket_notification](#clientput_bucket_notification)
        - [Client().put_bucket_notification_configuration](#clientput_bucket_notification_configuration)
        - [Client().put_bucket_policy](#clientput_bucket_policy)
        - [Client().put_bucket_replication](#clientput_bucket_replication)
        - [Client().put_bucket_request_payment](#clientput_bucket_request_payment)
        - [Client().put_bucket_tagging](#clientput_bucket_tagging)
        - [Client().put_bucket_versioning](#clientput_bucket_versioning)
        - [Client().put_bucket_website](#clientput_bucket_website)
        - [Client().put_object](#clientput_object)
        - [Client().put_object_acl](#clientput_object_acl)
        - [Client().put_object_legal_hold](#clientput_object_legal_hold)
        - [Client().put_object_lock_configuration](#clientput_object_lock_configuration)
        - [Client().put_object_retention](#clientput_object_retention)
        - [Client().put_object_tagging](#clientput_object_tagging)
        - [Client().put_public_access_block](#clientput_public_access_block)
        - [Client().restore_object](#clientrestore_object)
        - [Client().select_object_content](#clientselect_object_content)
        - [Client().upload_file](#clientupload_file)
        - [Client().upload_fileobj](#clientupload_fileobj)
        - [Client().upload_part](#clientupload_part)
        - [Client().upload_part_copy](#clientupload_part_copy)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L17)

```python
class Client(BaseClient):
```

### Client().abort_multipart_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L20)

```python
def abort_multipart_upload(
    Bucket: str,
    Key: str,
    UploadId: str,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L26)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().complete_multipart_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L30)

```python
def complete_multipart_upload(
    Bucket: str,
    Key: str,
    UploadId: str,
    MultipartUpload: Dict[str, Any] = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L41)

```python
def copy(
    CopySource: Dict[str, Any] = None,
    Bucket: str = None,
    Key: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    SourceClient: BaseClient = None,
    Config: TransferConfig = None,
) -> None:
```

### Client().copy_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L54)

```python
def copy_object(
    Bucket: str,
    CopySource: Union[str, Dict[Any, Any]],
    Key: str,
    ACL: str = None,
    CacheControl: str = None,
    ContentDisposition: str = None,
    ContentEncoding: str = None,
    ContentLanguage: str = None,
    ContentType: str = None,
    CopySourceIfMatch: str = None,
    CopySourceIfModifiedSince: datetime = None,
    CopySourceIfNoneMatch: str = None,
    CopySourceIfUnmodifiedSince: datetime = None,
    Expires: datetime = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWriteACP: str = None,
    Metadata: Dict[str, Any] = None,
    MetadataDirective: str = None,
    TaggingDirective: str = None,
    ServerSideEncryption: str = None,
    StorageClass: str = None,
    WebsiteRedirectLocation: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    SSEKMSKeyId: str = None,
    SSEKMSEncryptionContext: str = None,
    CopySourceSSECustomerAlgorithm: str = None,
    CopySourceSSECustomerKey: str = None,
    CopySourceSSECustomerKeyMD5: str = None,
    RequestPayer: str = None,
    Tagging: str = None,
    ObjectLockMode: str = None,
    ObjectLockRetainUntilDate: datetime = None,
    ObjectLockLegalHoldStatus: str = None,
) -> Dict[str, Any]:
```

### Client().create_bucket

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L97)

```python
def create_bucket(
    Bucket: str,
    ACL: str = None,
    CreateBucketConfiguration: Dict[str, Any] = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWrite: str = None,
    GrantWriteACP: str = None,
    ObjectLockEnabledForBucket: bool = None,
) -> Dict[str, Any]:
```

### Client().create_multipart_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L112)

```python
def create_multipart_upload(
    Bucket: str,
    Key: str,
    ACL: str = None,
    CacheControl: str = None,
    ContentDisposition: str = None,
    ContentEncoding: str = None,
    ContentLanguage: str = None,
    ContentType: str = None,
    Expires: datetime = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWriteACP: str = None,
    Metadata: Dict[str, Any] = None,
    ServerSideEncryption: str = None,
    StorageClass: str = None,
    WebsiteRedirectLocation: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    SSEKMSKeyId: str = None,
    SSEKMSEncryptionContext: str = None,
    RequestPayer: str = None,
    Tagging: str = None,
    ObjectLockMode: str = None,
    ObjectLockRetainUntilDate: datetime = None,
    ObjectLockLegalHoldStatus: str = None,
) -> Dict[str, Any]:
```

### Client().delete_bucket

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L145)

```python
def delete_bucket(Bucket: str) -> None:
```

### Client().delete_bucket_analytics_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L149)

```python
def delete_bucket_analytics_configuration(Bucket: str, Id: str) -> None:
```

### Client().delete_bucket_cors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L153)

```python
def delete_bucket_cors(Bucket: str) -> None:
```

### Client().delete_bucket_encryption

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L157)

```python
def delete_bucket_encryption(Bucket: str) -> None:
```

### Client().delete_bucket_inventory_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L161)

```python
def delete_bucket_inventory_configuration(Bucket: str, Id: str) -> None:
```

### Client().delete_bucket_lifecycle

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L165)

```python
def delete_bucket_lifecycle(Bucket: str) -> None:
```

### Client().delete_bucket_metrics_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L169)

```python
def delete_bucket_metrics_configuration(Bucket: str, Id: str) -> None:
```

### Client().delete_bucket_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L173)

```python
def delete_bucket_policy(Bucket: str) -> None:
```

### Client().delete_bucket_replication

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L177)

```python
def delete_bucket_replication(Bucket: str) -> None:
```

### Client().delete_bucket_tagging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L181)

```python
def delete_bucket_tagging(Bucket: str) -> None:
```

### Client().delete_bucket_website

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L185)

```python
def delete_bucket_website(Bucket: str) -> None:
```

### Client().delete_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L189)

```python
def delete_object(
    Bucket: str,
    Key: str,
    MFA: str = None,
    VersionId: str = None,
    RequestPayer: str = None,
    BypassGovernanceRetention: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_object_tagging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L201)

```python
def delete_object_tagging(
    Bucket: str,
    Key: str,
    VersionId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_objects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L207)

```python
def delete_objects(
    Bucket: str,
    Delete: Dict[str, Any],
    MFA: str = None,
    RequestPayer: str = None,
    BypassGovernanceRetention: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_public_access_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L218)

```python
def delete_public_access_block(Bucket: str) -> None:
```

### Client().download_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L222)

```python
def download_file(
    Bucket: str = None,
    Key: str = None,
    Filename: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Client().download_fileobj

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L234)

```python
def download_fileobj(
    Fileobj: Union[Any] = None,
    Bucket: str = None,
    Key: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Client().generate_presigned_post

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L246)

```python
def generate_presigned_post(
    Bucket: str = None,
    Key: str = None,
    Fields: Dict[str, Any] = None,
    Conditions: List[Any] = None,
    ExpiresIn: int = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L257)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_bucket_accelerate_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L267)

```python
def get_bucket_accelerate_configuration(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L271)

```python
def get_bucket_acl(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_analytics_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L275)

```python
def get_bucket_analytics_configuration(
    Bucket: str,
    Id: str,
) -> Dict[str, Any]:
```

### Client().get_bucket_cors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L281)

```python
def get_bucket_cors(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_encryption

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L285)

```python
def get_bucket_encryption(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_inventory_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L289)

```python
def get_bucket_inventory_configuration(
    Bucket: str,
    Id: str,
) -> Dict[str, Any]:
```

### Client().get_bucket_lifecycle

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L295)

```python
def get_bucket_lifecycle(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_lifecycle_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L299)

```python
def get_bucket_lifecycle_configuration(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_location

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L303)

```python
def get_bucket_location(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_logging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L307)

```python
def get_bucket_logging(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_metrics_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L311)

```python
def get_bucket_metrics_configuration(Bucket: str, Id: str) -> Dict[str, Any]:
```

### Client().get_bucket_notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L315)

```python
def get_bucket_notification(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_notification_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L319)

```python
def get_bucket_notification_configuration(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L323)

```python
def get_bucket_policy(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_policy_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L327)

```python
def get_bucket_policy_status(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_replication

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L331)

```python
def get_bucket_replication(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_request_payment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L335)

```python
def get_bucket_request_payment(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_tagging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L339)

```python
def get_bucket_tagging(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_versioning

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L343)

```python
def get_bucket_versioning(Bucket: str) -> Dict[str, Any]:
```

### Client().get_bucket_website

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L347)

```python
def get_bucket_website(Bucket: str) -> Dict[str, Any]:
```

### Client().get_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L351)

```python
def get_object(
    Bucket: str,
    Key: str,
    IfMatch: str = None,
    IfModifiedSince: datetime = None,
    IfNoneMatch: str = None,
    IfUnmodifiedSince: datetime = None,
    Range: str = None,
    ResponseCacheControl: str = None,
    ResponseContentDisposition: str = None,
    ResponseContentEncoding: str = None,
    ResponseContentLanguage: str = None,
    ResponseContentType: str = None,
    ResponseExpires: datetime = None,
    VersionId: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: str = None,
    PartNumber: int = None,
) -> Dict[str, Any]:
```

### Client().get_object_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L376)

```python
def get_object_acl(
    Bucket: str,
    Key: str,
    VersionId: str = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().get_object_legal_hold

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L382)

```python
def get_object_legal_hold(
    Bucket: str,
    Key: str,
    VersionId: str = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().get_object_lock_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L388)

```python
def get_object_lock_configuration(Bucket: str) -> Dict[str, Any]:
```

### Client().get_object_retention

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L392)

```python
def get_object_retention(
    Bucket: str,
    Key: str,
    VersionId: str = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().get_object_tagging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L398)

```python
def get_object_tagging(
    Bucket: str,
    Key: str,
    VersionId: str = None,
) -> Dict[str, Any]:
```

### Client().get_object_torrent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L404)

```python
def get_object_torrent(
    Bucket: str,
    Key: str,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L410)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_public_access_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L414)

```python
def get_public_access_block(Bucket: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L418)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().head_bucket

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L422)

```python
def head_bucket(Bucket: str) -> None:
```

### Client().head_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L426)

```python
def head_object(
    Bucket: str,
    Key: str,
    IfMatch: str = None,
    IfModifiedSince: datetime = None,
    IfNoneMatch: str = None,
    IfUnmodifiedSince: datetime = None,
    Range: str = None,
    VersionId: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: str = None,
    PartNumber: int = None,
) -> Dict[str, Any]:
```

### Client().list_bucket_analytics_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L445)

```python
def list_bucket_analytics_configurations(
    Bucket: str,
    ContinuationToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_bucket_inventory_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L451)

```python
def list_bucket_inventory_configurations(
    Bucket: str,
    ContinuationToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_bucket_metrics_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L457)

```python
def list_bucket_metrics_configurations(
    Bucket: str,
    ContinuationToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_buckets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L463)

```python
def list_buckets() -> Dict[str, Any]:
```

### Client().list_multipart_uploads

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L467)

```python
def list_multipart_uploads(
    Bucket: str,
    Delimiter: str = None,
    EncodingType: str = None,
    KeyMarker: str = None,
    MaxUploads: int = None,
    Prefix: str = None,
    UploadIdMarker: str = None,
) -> Dict[str, Any]:
```

### Client().list_object_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L480)

```python
def list_object_versions(
    Bucket: str,
    Delimiter: str = None,
    EncodingType: str = None,
    KeyMarker: str = None,
    MaxKeys: int = None,
    Prefix: str = None,
    VersionIdMarker: str = None,
) -> Dict[str, Any]:
```

### Client().list_objects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L493)

```python
def list_objects(
    Bucket: str,
    Delimiter: str = None,
    EncodingType: str = None,
    Marker: str = None,
    MaxKeys: int = None,
    Prefix: str = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().list_objects_v2

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L506)

```python
def list_objects_v2(
    Bucket: str,
    Delimiter: str = None,
    EncodingType: str = None,
    MaxKeys: int = None,
    Prefix: str = None,
    ContinuationToken: str = None,
    FetchOwner: bool = None,
    StartAfter: str = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().list_parts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L521)

```python
def list_parts(
    Bucket: str,
    Key: str,
    UploadId: str,
    MaxParts: int = None,
    PartNumberMarker: int = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().put_bucket_accelerate_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L533)

```python
def put_bucket_accelerate_configuration(
    Bucket: str,
    AccelerateConfiguration: Dict[str, Any],
) -> None:
```

### Client().put_bucket_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L539)

```python
def put_bucket_acl(
    Bucket: str,
    ACL: str = None,
    AccessControlPolicy: Dict[str, Any] = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWrite: str = None,
    GrantWriteACP: str = None,
) -> None:
```

### Client().put_bucket_analytics_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L553)

```python
def put_bucket_analytics_configuration(
    Bucket: str,
    Id: str,
    AnalyticsConfiguration: Dict[str, Any],
) -> None:
```

### Client().put_bucket_cors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L559)

```python
def put_bucket_cors(Bucket: str, CORSConfiguration: Dict[str, Any]) -> None:
```

### Client().put_bucket_encryption

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L563)

```python
def put_bucket_encryption(
    Bucket: str,
    ServerSideEncryptionConfiguration: Dict[str, Any],
    ContentMD5: str = None,
) -> None:
```

### Client().put_bucket_inventory_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L572)

```python
def put_bucket_inventory_configuration(
    Bucket: str,
    Id: str,
    InventoryConfiguration: Dict[str, Any],
) -> None:
```

### Client().put_bucket_lifecycle

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L578)

```python
def put_bucket_lifecycle(
    Bucket: str,
    LifecycleConfiguration: Dict[str, Any] = None,
) -> None:
```

### Client().put_bucket_lifecycle_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L584)

```python
def put_bucket_lifecycle_configuration(
    Bucket: str,
    LifecycleConfiguration: Dict[str, Any] = None,
) -> None:
```

### Client().put_bucket_logging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L590)

```python
def put_bucket_logging(
    Bucket: str,
    BucketLoggingStatus: Dict[str, Any],
) -> None:
```

### Client().put_bucket_metrics_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L596)

```python
def put_bucket_metrics_configuration(
    Bucket: str,
    Id: str,
    MetricsConfiguration: Dict[str, Any],
) -> None:
```

### Client().put_bucket_notification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L602)

```python
def put_bucket_notification(
    Bucket: str,
    NotificationConfiguration: Dict[str, Any],
) -> None:
```

### Client().put_bucket_notification_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L608)

```python
def put_bucket_notification_configuration(
    Bucket: str,
    NotificationConfiguration: Dict[str, Any],
) -> None:
```

### Client().put_bucket_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L614)

```python
def put_bucket_policy(
    Bucket: str,
    Policy: str,
    ConfirmRemoveSelfBucketAccess: bool = None,
) -> None:
```

### Client().put_bucket_replication

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L620)

```python
def put_bucket_replication(
    Bucket: str,
    ReplicationConfiguration: Dict[str, Any],
    Token: str = None,
) -> None:
```

### Client().put_bucket_request_payment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L626)

```python
def put_bucket_request_payment(
    Bucket: str,
    RequestPaymentConfiguration: Dict[str, Any],
) -> None:
```

### Client().put_bucket_tagging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L632)

```python
def put_bucket_tagging(Bucket: str, Tagging: Dict[str, Any]) -> None:
```

### Client().put_bucket_versioning

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L636)

```python
def put_bucket_versioning(
    Bucket: str,
    VersioningConfiguration: Dict[str, Any],
    MFA: str = None,
) -> None:
```

### Client().put_bucket_website

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L642)

```python
def put_bucket_website(
    Bucket: str,
    WebsiteConfiguration: Dict[str, Any],
) -> None:
```

### Client().put_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L648)

```python
def put_object(
    Bucket: str,
    Key: str,
    ACL: str = None,
    Body: Union[bytes, IO] = None,
    CacheControl: str = None,
    ContentDisposition: str = None,
    ContentEncoding: str = None,
    ContentLanguage: str = None,
    ContentLength: int = None,
    ContentMD5: str = None,
    ContentType: str = None,
    Expires: datetime = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWriteACP: str = None,
    Metadata: Dict[str, Any] = None,
    ServerSideEncryption: str = None,
    StorageClass: str = None,
    WebsiteRedirectLocation: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    SSEKMSKeyId: str = None,
    SSEKMSEncryptionContext: str = None,
    RequestPayer: str = None,
    Tagging: str = None,
    ObjectLockMode: str = None,
    ObjectLockRetainUntilDate: datetime = None,
    ObjectLockLegalHoldStatus: str = None,
) -> Dict[str, Any]:
```

### Client().put_object_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L684)

```python
def put_object_acl(
    Bucket: str,
    Key: str,
    ACL: str = None,
    AccessControlPolicy: Dict[str, Any] = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWrite: str = None,
    GrantWriteACP: str = None,
    RequestPayer: str = None,
    VersionId: str = None,
) -> Dict[str, Any]:
```

### Client().put_object_legal_hold

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L701)

```python
def put_object_legal_hold(
    Bucket: str,
    Key: str,
    LegalHold: Dict[str, Any] = None,
    RequestPayer: str = None,
    VersionId: str = None,
    ContentMD5: str = None,
) -> Dict[str, Any]:
```

### Client().put_object_lock_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L713)

```python
def put_object_lock_configuration(
    Bucket: str,
    ObjectLockConfiguration: Dict[str, Any] = None,
    RequestPayer: str = None,
    Token: str = None,
    ContentMD5: str = None,
) -> Dict[str, Any]:
```

### Client().put_object_retention

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L724)

```python
def put_object_retention(
    Bucket: str,
    Key: str,
    Retention: Dict[str, Any] = None,
    RequestPayer: str = None,
    VersionId: str = None,
    BypassGovernanceRetention: bool = None,
    ContentMD5: str = None,
) -> Dict[str, Any]:
```

### Client().put_object_tagging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L737)

```python
def put_object_tagging(
    Bucket: str,
    Key: str,
    Tagging: Dict[str, Any],
    VersionId: str = None,
    ContentMD5: str = None,
) -> Dict[str, Any]:
```

### Client().put_public_access_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L748)

```python
def put_public_access_block(
    Bucket: str,
    PublicAccessBlockConfiguration: Dict[str, Any],
    ContentMD5: str = None,
) -> None:
```

### Client().restore_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L757)

```python
def restore_object(
    Bucket: str,
    Key: str,
    VersionId: str = None,
    RestoreRequest: Dict[str, Any] = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().select_object_content

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L768)

```python
def select_object_content(
    Bucket: str,
    Key: str,
    Expression: str,
    ExpressionType: str,
    InputSerialization: Dict[str, Any],
    OutputSerialization: Dict[str, Any],
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestProgress: Dict[str, Any] = None,
    ScanRange: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().upload_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L785)

```python
def upload_file(
    Filename: str = None,
    Bucket: str = None,
    Key: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Client().upload_fileobj

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L797)

```python
def upload_fileobj(
    Fileobj: Union[Any] = None,
    Bucket: str = None,
    Key: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Client().upload_part

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L809)

```python
def upload_part(
    Bucket: str,
    Key: str,
    PartNumber: int,
    UploadId: str,
    Body: Union[bytes, IO] = None,
    ContentLength: int = None,
    ContentMD5: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Client().upload_part_copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/client.py#L826)

```python
def upload_part_copy(
    Bucket: str,
    CopySource: Union[str, Dict[Any, Any]],
    Key: str,
    PartNumber: int,
    UploadId: str,
    CopySourceIfMatch: str = None,
    CopySourceIfModifiedSince: datetime = None,
    CopySourceIfNoneMatch: str = None,
    CopySourceIfUnmodifiedSince: datetime = None,
    CopySourceRange: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    CopySourceSSECustomerAlgorithm: str = None,
    CopySourceSSECustomerKey: str = None,
    CopySourceSSECustomerKeyMD5: str = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```
