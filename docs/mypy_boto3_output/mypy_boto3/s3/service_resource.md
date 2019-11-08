# ServiceResource

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.s3.service_resource](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [S3](index.md#s3) / ServiceResource
    - [Bucket](#bucket)
        - [Bucket().copy](#bucketcopy)
        - [Bucket().create](#bucketcreate)
        - [Bucket().delete](#bucketdelete)
        - [Bucket().delete_objects](#bucketdelete_objects)
        - [Bucket().download_file](#bucketdownload_file)
        - [Bucket().download_fileobj](#bucketdownload_fileobj)
        - [Bucket().get_available_subresources](#bucketget_available_subresources)
        - [Bucket().load](#bucketload)
        - [Bucket().put_object](#bucketput_object)
        - [Bucket().upload_file](#bucketupload_file)
        - [Bucket().upload_fileobj](#bucketupload_fileobj)
        - [Bucket().wait_until_exists](#bucketwait_until_exists)
        - [Bucket().wait_until_not_exists](#bucketwait_until_not_exists)
    - [BucketAcl](#bucketacl)
        - [BucketAcl().get_available_subresources](#bucketaclget_available_subresources)
        - [BucketAcl().load](#bucketaclload)
        - [BucketAcl().put](#bucketaclput)
        - [BucketAcl().reload](#bucketaclreload)
    - [BucketCors](#bucketcors)
        - [BucketCors().delete](#bucketcorsdelete)
        - [BucketCors().get_available_subresources](#bucketcorsget_available_subresources)
        - [BucketCors().load](#bucketcorsload)
        - [BucketCors().put](#bucketcorsput)
        - [BucketCors().reload](#bucketcorsreload)
    - [BucketLifecycle](#bucketlifecycle)
        - [BucketLifecycle().delete](#bucketlifecycledelete)
        - [BucketLifecycle().get_available_subresources](#bucketlifecycleget_available_subresources)
        - [BucketLifecycle().load](#bucketlifecycleload)
        - [BucketLifecycle().put](#bucketlifecycleput)
        - [BucketLifecycle().reload](#bucketlifecyclereload)
    - [BucketLifecycleConfiguration](#bucketlifecycleconfiguration)
        - [BucketLifecycleConfiguration().delete](#bucketlifecycleconfigurationdelete)
        - [BucketLifecycleConfiguration().get_available_subresources](#bucketlifecycleconfigurationget_available_subresources)
        - [BucketLifecycleConfiguration().load](#bucketlifecycleconfigurationload)
        - [BucketLifecycleConfiguration().put](#bucketlifecycleconfigurationput)
        - [BucketLifecycleConfiguration().reload](#bucketlifecycleconfigurationreload)
    - [BucketLogging](#bucketlogging)
        - [BucketLogging().get_available_subresources](#bucketloggingget_available_subresources)
        - [BucketLogging().load](#bucketloggingload)
        - [BucketLogging().put](#bucketloggingput)
        - [BucketLogging().reload](#bucketloggingreload)
    - [BucketNotification](#bucketnotification)
        - [BucketNotification().get_available_subresources](#bucketnotificationget_available_subresources)
        - [BucketNotification().load](#bucketnotificationload)
        - [BucketNotification().put](#bucketnotificationput)
        - [BucketNotification().reload](#bucketnotificationreload)
    - [BucketPolicy](#bucketpolicy)
        - [BucketPolicy().delete](#bucketpolicydelete)
        - [BucketPolicy().get_available_subresources](#bucketpolicyget_available_subresources)
        - [BucketPolicy().load](#bucketpolicyload)
        - [BucketPolicy().put](#bucketpolicyput)
        - [BucketPolicy().reload](#bucketpolicyreload)
    - [BucketRequestPayment](#bucketrequestpayment)
        - [BucketRequestPayment().get_available_subresources](#bucketrequestpaymentget_available_subresources)
        - [BucketRequestPayment().load](#bucketrequestpaymentload)
        - [BucketRequestPayment().put](#bucketrequestpaymentput)
        - [BucketRequestPayment().reload](#bucketrequestpaymentreload)
    - [BucketTagging](#buckettagging)
        - [BucketTagging().delete](#buckettaggingdelete)
        - [BucketTagging().get_available_subresources](#buckettaggingget_available_subresources)
        - [BucketTagging().load](#buckettaggingload)
        - [BucketTagging().put](#buckettaggingput)
        - [BucketTagging().reload](#buckettaggingreload)
    - [BucketVersioning](#bucketversioning)
        - [BucketVersioning().enable](#bucketversioningenable)
        - [BucketVersioning().get_available_subresources](#bucketversioningget_available_subresources)
        - [BucketVersioning().load](#bucketversioningload)
        - [BucketVersioning().put](#bucketversioningput)
        - [BucketVersioning().reload](#bucketversioningreload)
        - [BucketVersioning().suspend](#bucketversioningsuspend)
    - [BucketWebsite](#bucketwebsite)
        - [BucketWebsite().delete](#bucketwebsitedelete)
        - [BucketWebsite().get_available_subresources](#bucketwebsiteget_available_subresources)
        - [BucketWebsite().load](#bucketwebsiteload)
        - [BucketWebsite().put](#bucketwebsiteput)
        - [BucketWebsite().reload](#bucketwebsitereload)
    - [MultipartUpload](#multipartupload)
        - [MultipartUpload().abort](#multipartuploadabort)
        - [MultipartUpload().complete](#multipartuploadcomplete)
        - [MultipartUpload().get_available_subresources](#multipartuploadget_available_subresources)
    - [MultipartUploadPart](#multipartuploadpart)
        - [MultipartUploadPart().copy_from](#multipartuploadpartcopy_from)
        - [MultipartUploadPart().get_available_subresources](#multipartuploadpartget_available_subresources)
        - [MultipartUploadPart().upload](#multipartuploadpartupload)
    - [Object](#object)
        - [Object().copy](#objectcopy)
        - [Object().copy_from](#objectcopy_from)
        - [Object().delete](#objectdelete)
        - [Object().download_file](#objectdownload_file)
        - [Object().download_fileobj](#objectdownload_fileobj)
        - [Object().get](#objectget)
        - [Object().get_available_subresources](#objectget_available_subresources)
        - [Object().initiate_multipart_upload](#objectinitiate_multipart_upload)
        - [Object().load](#objectload)
        - [Object().put](#objectput)
        - [Object().reload](#objectreload)
        - [Object().restore_object](#objectrestore_object)
        - [Object().upload_file](#objectupload_file)
        - [Object().upload_fileobj](#objectupload_fileobj)
        - [Object().wait_until_exists](#objectwait_until_exists)
        - [Object().wait_until_not_exists](#objectwait_until_not_exists)
    - [ObjectAcl](#objectacl)
        - [ObjectAcl().get_available_subresources](#objectaclget_available_subresources)
        - [ObjectAcl().load](#objectaclload)
        - [ObjectAcl().put](#objectaclput)
        - [ObjectAcl().reload](#objectaclreload)
    - [ObjectSummary](#objectsummary)
        - [ObjectSummary().copy_from](#objectsummarycopy_from)
        - [ObjectSummary().delete](#objectsummarydelete)
        - [ObjectSummary().get](#objectsummaryget)
        - [ObjectSummary().get_available_subresources](#objectsummaryget_available_subresources)
        - [ObjectSummary().initiate_multipart_upload](#objectsummaryinitiate_multipart_upload)
        - [ObjectSummary().load](#objectsummaryload)
        - [ObjectSummary().put](#objectsummaryput)
        - [ObjectSummary().restore_object](#objectsummaryrestore_object)
        - [ObjectSummary().wait_until_exists](#objectsummarywait_until_exists)
        - [ObjectSummary().wait_until_not_exists](#objectsummarywait_until_not_exists)
    - [ObjectVersion](#objectversion)
        - [ObjectVersion().delete](#objectversiondelete)
        - [ObjectVersion().get](#objectversionget)
        - [ObjectVersion().get_available_subresources](#objectversionget_available_subresources)
        - [ObjectVersion().head](#objectversionhead)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().Bucket](#serviceresourcebucket)
        - [ServiceResource().BucketAcl](#serviceresourcebucketacl)
        - [ServiceResource().BucketCors](#serviceresourcebucketcors)
        - [ServiceResource().BucketLifecycle](#serviceresourcebucketlifecycle)
        - [ServiceResource().BucketLifecycleConfiguration](#serviceresourcebucketlifecycleconfiguration)
        - [ServiceResource().BucketLogging](#serviceresourcebucketlogging)
        - [ServiceResource().BucketNotification](#serviceresourcebucketnotification)
        - [ServiceResource().BucketPolicy](#serviceresourcebucketpolicy)
        - [ServiceResource().BucketRequestPayment](#serviceresourcebucketrequestpayment)
        - [ServiceResource().BucketTagging](#serviceresourcebuckettagging)
        - [ServiceResource().BucketVersioning](#serviceresourcebucketversioning)
        - [ServiceResource().BucketWebsite](#serviceresourcebucketwebsite)
        - [ServiceResource().MultipartUpload](#serviceresourcemultipartupload)
        - [ServiceResource().MultipartUploadPart](#serviceresourcemultipartuploadpart)
        - [ServiceResource().Object](#serviceresourceobject)
        - [ServiceResource().ObjectAcl](#serviceresourceobjectacl)
        - [ServiceResource().ObjectSummary](#serviceresourceobjectsummary)
        - [ServiceResource().ObjectVersion](#serviceresourceobjectversion)
        - [ServiceResource().create_bucket](#serviceresourcecreate_bucket)
        - [ServiceResource().get_available_subresources](#serviceresourceget_available_subresources)
    - [buckets](#buckets)
        - [buckets.all](#bucketsall)
        - [buckets.filter](#bucketsfilter)
        - [buckets.iterator](#bucketsiterator)
        - [buckets.limit](#bucketslimit)
        - [buckets.page_size](#bucketspage_size)
        - [buckets.pages](#bucketspages)
    - [multipart_uploads](#multipart_uploads)
        - [multipart_uploads.all](#multipart_uploadsall)
        - [multipart_uploads.filter](#multipart_uploadsfilter)
        - [multipart_uploads.iterator](#multipart_uploadsiterator)
        - [multipart_uploads.limit](#multipart_uploadslimit)
        - [multipart_uploads.page_size](#multipart_uploadspage_size)
        - [multipart_uploads.pages](#multipart_uploadspages)
    - [object_versions](#object_versions)
        - [object_versions.all](#object_versionsall)
        - [object_versions.delete](#object_versionsdelete)
        - [object_versions.filter](#object_versionsfilter)
        - [object_versions.iterator](#object_versionsiterator)
        - [object_versions.limit](#object_versionslimit)
        - [object_versions.page_size](#object_versionspage_size)
        - [object_versions.pages](#object_versionspages)
    - [objects](#objects)
        - [objects.all](#objectsall)
        - [objects.delete](#objectsdelete)
        - [objects.filter](#objectsfilter)
        - [objects.iterator](#objectsiterator)
        - [objects.limit](#objectslimit)
        - [objects.page_size](#objectspage_size)
        - [objects.pages](#objectspages)
    - [parts](#parts)
        - [parts.all](#partsall)
        - [parts.filter](#partsfilter)
        - [parts.iterator](#partsiterator)
        - [parts.limit](#partslimit)
        - [parts.page_size](#partspage_size)
        - [parts.pages](#partspages)

## Bucket

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L151)

```python
class Bucket(Boto3ServiceResource):
```

### Bucket().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L159)

```python
def copy(
    CopySource: Dict[str, Any] = None,
    Key: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    SourceClient: BaseClient = None,
    Config: TransferConfig = None,
) -> None:
```

### Bucket().create

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L171)

```python
def create(
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

### Bucket().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L185)

```python
def delete() -> None:
```

### Bucket().delete_objects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L189)

```python
def delete_objects(
    Delete: Dict[str, Any],
    MFA: str = None,
    RequestPayer: str = None,
    BypassGovernanceRetention: bool = None,
) -> Dict[str, Any]:
```

### Bucket().download_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L199)

```python
def download_file(
    Key: str = None,
    Filename: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Bucket().download_fileobj

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L210)

```python
def download_fileobj(
    Fileobj: Union[Any] = None,
    Key: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Bucket().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L221)

```python
def get_available_subresources() -> List[str]:
```

### Bucket().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L225)

```python
def load() -> None:
```

### Bucket().put_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L229)

```python
def put_object(
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
) -> s3_service_resource_scope.Object:
```

### Bucket().upload_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L264)

```python
def upload_file(
    Filename: str = None,
    Key: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Bucket().upload_fileobj

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L275)

```python
def upload_fileobj(
    Fileobj: Union[Any] = None,
    Key: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Bucket().wait_until_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L286)

```python
def wait_until_exists() -> None:
```

### Bucket().wait_until_not_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L290)

```python
def wait_until_not_exists() -> None:
```

## BucketAcl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L294)

```python
class BucketAcl(Boto3ServiceResource):
```

### BucketAcl().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L300)

```python
def get_available_subresources() -> List[str]:
```

### BucketAcl().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L304)

```python
def load() -> None:
```

### BucketAcl().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L308)

```python
def put(
    ACL: str = None,
    AccessControlPolicy: Dict[str, Any] = None,
    GrantFullControl: str = None,
    GrantRead: str = None,
    GrantReadACP: str = None,
    GrantWrite: str = None,
    GrantWriteACP: str = None,
) -> None:
```

### BucketAcl().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L321)

```python
def reload() -> None:
```

## BucketCors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L325)

```python
class BucketCors(Boto3ServiceResource):
```

### BucketCors().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L330)

```python
def delete() -> None:
```

### BucketCors().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L334)

```python
def get_available_subresources() -> List[str]:
```

### BucketCors().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L338)

```python
def load() -> None:
```

### BucketCors().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L342)

```python
def put(CORSConfiguration: Dict[str, Any]) -> None:
```

### BucketCors().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L346)

```python
def reload() -> None:
```

## BucketLifecycle

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L350)

```python
class BucketLifecycle(Boto3ServiceResource):
```

### BucketLifecycle().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L355)

```python
def delete() -> None:
```

### BucketLifecycle().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L359)

```python
def get_available_subresources() -> List[str]:
```

### BucketLifecycle().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L363)

```python
def load() -> None:
```

### BucketLifecycle().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L367)

```python
def put(LifecycleConfiguration: Dict[str, Any] = None) -> None:
```

### BucketLifecycle().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L371)

```python
def reload() -> None:
```

## BucketLifecycleConfiguration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L375)

```python
class BucketLifecycleConfiguration(Boto3ServiceResource):
```

### BucketLifecycleConfiguration().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L380)

```python
def delete() -> None:
```

### BucketLifecycleConfiguration().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L384)

```python
def get_available_subresources() -> List[str]:
```

### BucketLifecycleConfiguration().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L388)

```python
def load() -> None:
```

### BucketLifecycleConfiguration().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L392)

```python
def put(LifecycleConfiguration: Dict[str, Any] = None) -> None:
```

### BucketLifecycleConfiguration().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L396)

```python
def reload() -> None:
```

## BucketLogging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L400)

```python
class BucketLogging(Boto3ServiceResource):
```

### BucketLogging().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L405)

```python
def get_available_subresources() -> List[str]:
```

### BucketLogging().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L409)

```python
def load() -> None:
```

### BucketLogging().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L413)

```python
def put(BucketLoggingStatus: Dict[str, Any]) -> None:
```

### BucketLogging().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L417)

```python
def reload() -> None:
```

## BucketNotification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L421)

```python
class BucketNotification(Boto3ServiceResource):
```

### BucketNotification().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L428)

```python
def get_available_subresources() -> List[str]:
```

### BucketNotification().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L432)

```python
def load() -> None:
```

### BucketNotification().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L436)

```python
def put(NotificationConfiguration: Dict[str, Any]) -> None:
```

### BucketNotification().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L440)

```python
def reload() -> None:
```

## BucketPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L444)

```python
class BucketPolicy(Boto3ServiceResource):
```

### BucketPolicy().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L449)

```python
def delete() -> None:
```

### BucketPolicy().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L453)

```python
def get_available_subresources() -> List[str]:
```

### BucketPolicy().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L457)

```python
def load() -> None:
```

### BucketPolicy().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L461)

```python
def put(Policy: str, ConfirmRemoveSelfBucketAccess: bool = None) -> None:
```

### BucketPolicy().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L465)

```python
def reload() -> None:
```

## BucketRequestPayment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L469)

```python
class BucketRequestPayment(Boto3ServiceResource):
```

### BucketRequestPayment().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L474)

```python
def get_available_subresources() -> List[str]:
```

### BucketRequestPayment().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L478)

```python
def load() -> None:
```

### BucketRequestPayment().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L482)

```python
def put(RequestPaymentConfiguration: Dict[str, Any]) -> None:
```

### BucketRequestPayment().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L486)

```python
def reload() -> None:
```

## BucketTagging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L490)

```python
class BucketTagging(Boto3ServiceResource):
```

### BucketTagging().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L495)

```python
def delete() -> None:
```

### BucketTagging().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L499)

```python
def get_available_subresources() -> List[str]:
```

### BucketTagging().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L503)

```python
def load() -> None:
```

### BucketTagging().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L507)

```python
def put(Tagging: Dict[str, Any]) -> None:
```

### BucketTagging().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L511)

```python
def reload() -> None:
```

## BucketVersioning

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L515)

```python
class BucketVersioning(Boto3ServiceResource):
```

### BucketVersioning().enable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L521)

```python
def enable(MFA: str = None) -> None:
```

### BucketVersioning().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L525)

```python
def get_available_subresources() -> List[str]:
```

### BucketVersioning().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L529)

```python
def load() -> None:
```

### BucketVersioning().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L533)

```python
def put(VersioningConfiguration: Dict[str, Any], MFA: str = None) -> None:
```

### BucketVersioning().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L537)

```python
def reload() -> None:
```

### BucketVersioning().suspend

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L541)

```python
def suspend(MFA: str = None) -> None:
```

## BucketWebsite

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L545)

```python
class BucketWebsite(Boto3ServiceResource):
```

### BucketWebsite().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L553)

```python
def delete() -> None:
```

### BucketWebsite().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L557)

```python
def get_available_subresources() -> List[str]:
```

### BucketWebsite().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L561)

```python
def load() -> None:
```

### BucketWebsite().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L565)

```python
def put(WebsiteConfiguration: Dict[str, Any]) -> None:
```

### BucketWebsite().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L569)

```python
def reload() -> None:
```

## MultipartUpload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L573)

```python
class MultipartUpload(Boto3ServiceResource):
```

### MultipartUpload().abort

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L586)

```python
def abort(RequestPayer: str = None) -> Dict[str, Any]:
```

### MultipartUpload().complete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L590)

```python
def complete(
    MultipartUpload: Dict[str, Any] = None,
    RequestPayer: str = None,
) -> s3_service_resource_scope.Object:
```

### MultipartUpload().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L596)

```python
def get_available_subresources() -> List[str]:
```

## MultipartUploadPart

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L600)

```python
class MultipartUploadPart(Boto3ServiceResource):
```

### MultipartUploadPart().copy_from

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L610)

```python
def copy_from(
    CopySource: Union[str, Dict[Any, Any]],
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

### MultipartUploadPart().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L629)

```python
def get_available_subresources() -> List[str]:
```

### MultipartUploadPart().upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L633)

```python
def upload(
    Body: Union[bytes, IO] = None,
    ContentLength: int = None,
    ContentMD5: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

## Object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L646)

```python
class Object(Boto3ServiceResource):
```

### Object().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L679)

```python
def copy(
    CopySource: Dict[str, Any] = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    SourceClient: BaseClient = None,
    Config: TransferConfig = None,
) -> None:
```

### Object().copy_from

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L690)

```python
def copy_from(
    CopySource: Union[str, Dict[Any, Any]],
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

### Object().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L731)

```python
def delete(
    MFA: str = None,
    VersionId: str = None,
    RequestPayer: str = None,
    BypassGovernanceRetention: bool = None,
) -> Dict[str, Any]:
```

### Object().download_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L741)

```python
def download_file(
    Filename: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Object().download_fileobj

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L751)

```python
def download_fileobj(
    Fileobj: Union[Any] = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Object().get

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L761)

```python
def get(
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

### Object().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L784)

```python
def get_available_subresources() -> List[str]:
```

### Object().initiate_multipart_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L788)

```python
def initiate_multipart_upload(
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
) -> s3_service_resource_scope.MultipartUpload:
```

### Object().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L819)

```python
def load() -> None:
```

### Object().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L823)

```python
def put(
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

### Object().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L857)

```python
def reload() -> None:
```

### Object().restore_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L861)

```python
def restore_object(
    VersionId: str = None,
    RestoreRequest: Dict[str, Any] = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### Object().upload_file

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L870)

```python
def upload_file(
    Filename: str = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Object().upload_fileobj

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L880)

```python
def upload_fileobj(
    Fileobj: Union[Any] = None,
    ExtraArgs: Dict[str, Any] = None,
    Callback: Callable[..., Any] = None,
    Config: TransferConfig = None,
) -> None:
```

### Object().wait_until_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L890)

```python
def wait_until_exists(
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
) -> None:
```

### Object().wait_until_not_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L907)

```python
def wait_until_not_exists(
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
) -> None:
```

## ObjectAcl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L924)

```python
class ObjectAcl(Boto3ServiceResource):
```

### ObjectAcl().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L932)

```python
def get_available_subresources() -> List[str]:
```

### ObjectAcl().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L936)

```python
def load() -> None:
```

### ObjectAcl().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L940)

```python
def put(
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

### ObjectAcl().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L955)

```python
def reload() -> None:
```

## ObjectSummary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L959)

```python
class ObjectSummary(Boto3ServiceResource):
```

### ObjectSummary().copy_from

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L969)

```python
def copy_from(
    CopySource: Union[str, Dict[Any, Any]],
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

### ObjectSummary().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1010)

```python
def delete(
    MFA: str = None,
    VersionId: str = None,
    RequestPayer: str = None,
    BypassGovernanceRetention: bool = None,
) -> Dict[str, Any]:
```

### ObjectSummary().get

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1020)

```python
def get(
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

### ObjectSummary().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1043)

```python
def get_available_subresources() -> List[str]:
```

### ObjectSummary().initiate_multipart_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1047)

```python
def initiate_multipart_upload(
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
) -> s3_service_resource_scope.MultipartUpload:
```

### ObjectSummary().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1078)

```python
def load() -> None:
```

### ObjectSummary().put

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1082)

```python
def put(
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

### ObjectSummary().restore_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1116)

```python
def restore_object(
    VersionId: str = None,
    RestoreRequest: Dict[str, Any] = None,
    RequestPayer: str = None,
) -> Dict[str, Any]:
```

### ObjectSummary().wait_until_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1125)

```python
def wait_until_exists(
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
) -> None:
```

### ObjectSummary().wait_until_not_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1142)

```python
def wait_until_not_exists(
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
) -> None:
```

## ObjectVersion

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1159)

```python
class ObjectVersion(Boto3ServiceResource):
```

### ObjectVersion().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1173)

```python
def delete(
    MFA: str = None,
    RequestPayer: str = None,
    BypassGovernanceRetention: bool = None,
) -> Dict[str, Any]:
```

### ObjectVersion().get

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1182)

```python
def get(
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
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: str = None,
    PartNumber: int = None,
) -> Dict[str, Any]:
```

### ObjectVersion().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1204)

```python
def get_available_subresources() -> List[str]:
```

### ObjectVersion().head

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1208)

```python
def head(
    IfMatch: str = None,
    IfModifiedSince: datetime = None,
    IfNoneMatch: str = None,
    IfUnmodifiedSince: datetime = None,
    Range: str = None,
    SSECustomerAlgorithm: str = None,
    SSECustomerKey: str = None,
    SSECustomerKeyMD5: str = None,
    RequestPayer: str = None,
    PartNumber: int = None,
) -> Dict[str, Any]:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L20)

```python
class ServiceResource(Boto3ServiceResource):
```

### ServiceResource().Bucket

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L24)

```python
def Bucket(name: str = None) -> s3_service_resource_scope.Bucket:
```

### ServiceResource().BucketAcl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L28)

```python
def BucketAcl(bucket_name: str = None) -> s3_service_resource_scope.BucketAcl:
```

### ServiceResource().BucketCors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L32)

```python
def BucketCors(
    bucket_name: str = None,
) -> s3_service_resource_scope.BucketCors:
```

### ServiceResource().BucketLifecycle

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L38)

```python
def BucketLifecycle(
    bucket_name: str = None,
) -> s3_service_resource_scope.BucketLifecycle:
```

### ServiceResource().BucketLifecycleConfiguration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L44)

```python
def BucketLifecycleConfiguration(
    bucket_name: str = None,
) -> s3_service_resource_scope.BucketLifecycleConfiguration:
```

### ServiceResource().BucketLogging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L50)

```python
def BucketLogging(
    bucket_name: str = None,
) -> s3_service_resource_scope.BucketLogging:
```

### ServiceResource().BucketNotification

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L56)

```python
def BucketNotification(
    bucket_name: str = None,
) -> s3_service_resource_scope.BucketNotification:
```

### ServiceResource().BucketPolicy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L62)

```python
def BucketPolicy(
    bucket_name: str = None,
) -> s3_service_resource_scope.BucketPolicy:
```

### ServiceResource().BucketRequestPayment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L68)

```python
def BucketRequestPayment(
    bucket_name: str = None,
) -> s3_service_resource_scope.BucketRequestPayment:
```

### ServiceResource().BucketTagging

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L74)

```python
def BucketTagging(
    bucket_name: str = None,
) -> s3_service_resource_scope.BucketTagging:
```

### ServiceResource().BucketVersioning

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L80)

```python
def BucketVersioning(
    bucket_name: str = None,
) -> s3_service_resource_scope.BucketVersioning:
```

### ServiceResource().BucketWebsite

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L86)

```python
def BucketWebsite(
    bucket_name: str = None,
) -> s3_service_resource_scope.BucketWebsite:
```

### ServiceResource().MultipartUpload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L92)

```python
def MultipartUpload(
    bucket_name: str = None,
    object_key: str = None,
    id: str = None,
) -> s3_service_resource_scope.MultipartUpload:
```

### ServiceResource().MultipartUploadPart

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L98)

```python
def MultipartUploadPart(
    bucket_name: str = None,
    object_key: str = None,
    multipart_upload_id: str = None,
    part_number: str = None,
) -> s3_service_resource_scope.MultipartUploadPart:
```

### ServiceResource().Object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L108)

```python
def Object(
    bucket_name: str = None,
    key: str = None,
) -> s3_service_resource_scope.Object:
```

### ServiceResource().ObjectAcl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L114)

```python
def ObjectAcl(
    bucket_name: str = None,
    object_key: str = None,
) -> s3_service_resource_scope.ObjectAcl:
```

### ServiceResource().ObjectSummary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L120)

```python
def ObjectSummary(
    bucket_name: str = None,
    key: str = None,
) -> s3_service_resource_scope.ObjectSummary:
```

### ServiceResource().ObjectVersion

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L126)

```python
def ObjectVersion(
    bucket_name: str = None,
    object_key: str = None,
    id: str = None,
) -> s3_service_resource_scope.ObjectVersion:
```

### ServiceResource().create_bucket

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L132)

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
) -> s3_service_resource_scope.Bucket:
```

### ServiceResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L147)

```python
def get_available_subresources() -> List[str]:
```

## buckets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1224)

```python
class buckets(ResourceCollection):
```

### buckets.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1225)

```python
@classmethod
def all() -> List[s3_service_resource_scope.Bucket]:
```

### buckets.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1230)

```python
@classmethod
def filter() -> List[s3_service_resource_scope.Bucket]:
```

### buckets.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1235)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### buckets.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1240)

```python
@classmethod
def limit() -> List[s3_service_resource_scope.Bucket]:
```

### buckets.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1245)

```python
@classmethod
def page_size() -> List[s3_service_resource_scope.Bucket]:
```

### buckets.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1250)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## multipart_uploads

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1256)

```python
class multipart_uploads(ResourceCollection):
```

### multipart_uploads.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1257)

```python
@classmethod
def all() -> List[s3_service_resource_scope.MultipartUpload]:
```

### multipart_uploads.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1262)

```python
@classmethod
def filter(
    Delimiter: str = None,
    EncodingType: str = None,
    KeyMarker: str = None,
    MaxUploads: int = None,
    Prefix: str = None,
    UploadIdMarker: str = None,
) -> List[s3_service_resource_scope.MultipartUpload]:
```

### multipart_uploads.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1275)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### multipart_uploads.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1280)

```python
@classmethod
def limit(
    count: int = None,
) -> List[s3_service_resource_scope.MultipartUpload]:
```

### multipart_uploads.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1287)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[s3_service_resource_scope.MultipartUpload]:
```

### multipart_uploads.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1294)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## object_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1300)

```python
class object_versions(ResourceCollection):
```

### object_versions.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1301)

```python
@classmethod
def all() -> List[s3_service_resource_scope.ObjectVersion]:
```

### object_versions.delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1306)

```python
@classmethod
def delete(
    MFA: str = None,
    RequestPayer: str = None,
    BypassGovernanceRetention: bool = None,
) -> Dict[str, Any]:
```

### object_versions.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1316)

```python
@classmethod
def filter(
    Delimiter: str = None,
    EncodingType: str = None,
    KeyMarker: str = None,
    MaxKeys: int = None,
    Prefix: str = None,
    VersionIdMarker: str = None,
) -> List[s3_service_resource_scope.ObjectVersion]:
```

### object_versions.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1329)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### object_versions.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1334)

```python
@classmethod
def limit(count: int = None) -> List[s3_service_resource_scope.ObjectVersion]:
```

### object_versions.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1339)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[s3_service_resource_scope.ObjectVersion]:
```

### object_versions.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1346)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## objects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1352)

```python
class objects(ResourceCollection):
```

### objects.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1353)

```python
@classmethod
def all() -> List[s3_service_resource_scope.ObjectSummary]:
```

### objects.delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1358)

```python
@classmethod
def delete(
    MFA: str = None,
    RequestPayer: str = None,
    BypassGovernanceRetention: bool = None,
) -> Dict[str, Any]:
```

### objects.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1368)

```python
@classmethod
def filter(
    Delimiter: str = None,
    EncodingType: str = None,
    Marker: str = None,
    MaxKeys: int = None,
    Prefix: str = None,
    RequestPayer: str = None,
) -> List[s3_service_resource_scope.ObjectSummary]:
```

### objects.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1381)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### objects.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1386)

```python
@classmethod
def limit(count: int = None) -> List[s3_service_resource_scope.ObjectSummary]:
```

### objects.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1391)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[s3_service_resource_scope.ObjectSummary]:
```

### objects.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1398)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## parts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1404)

```python
class parts(ResourceCollection):
```

### parts.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1405)

```python
@classmethod
def all() -> List[s3_service_resource_scope.MultipartUploadPart]:
```

### parts.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1410)

```python
@classmethod
def filter(
    MaxParts: int = None,
    PartNumberMarker: int = None,
    RequestPayer: str = None,
) -> List[s3_service_resource_scope.MultipartUploadPart]:
```

### parts.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1420)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### parts.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1425)

```python
@classmethod
def limit(
    count: int = None,
) -> List[s3_service_resource_scope.MultipartUploadPart]:
```

### parts.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1432)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[s3_service_resource_scope.MultipartUploadPart]:
```

### parts.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/s3/service_resource.py#L1439)

```python
@classmethod
def pages() -> List[ServiceResource]:
```
