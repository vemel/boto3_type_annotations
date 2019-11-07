from typing import Callable
from boto3.resources.base import ServiceResource
from boto3.s3.transfer import TransferConfig
from boto3.resources.collection import ResourceCollection
from typing import Dict
from typing import List
from botocore.client import BaseClient
from typing import IO
from datetime import datetime
from typing import Optional
from typing import Union

class ServiceResource(base.ServiceResource):
    buckets: 'buckets'

    def Bucket(
        self,
        name: Optional[str] = None,
    ) -> 'Bucket':
        pass


    def BucketAcl(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketAcl':
        pass


    def BucketCors(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketCors':
        pass


    def BucketLifecycle(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketLifecycle':
        pass


    def BucketLifecycleConfiguration(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketLifecycleConfiguration':
        pass


    def BucketLogging(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketLogging':
        pass


    def BucketNotification(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketNotification':
        pass


    def BucketPolicy(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketPolicy':
        pass


    def BucketRequestPayment(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketRequestPayment':
        pass


    def BucketTagging(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketTagging':
        pass


    def BucketVersioning(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketVersioning':
        pass


    def BucketWebsite(
        self,
        bucket_name: Optional[str] = None,
    ) -> 'BucketWebsite':
        pass


    def MultipartUpload(
        self,
        bucket_name: Optional[str] = None,
        object_key: Optional[str] = None,
        id: Optional[str] = None,
    ) -> 'MultipartUpload':
        pass


    def MultipartUploadPart(
        self,
        bucket_name: Optional[str] = None,
        object_key: Optional[str] = None,
        multipart_upload_id: Optional[str] = None,
        part_number: Optional[str] = None,
    ) -> 'MultipartUploadPart':
        pass


    def Object(
        self,
        bucket_name: Optional[str] = None,
        key: Optional[str] = None,
    ) -> 'Object':
        pass


    def ObjectAcl(
        self,
        bucket_name: Optional[str] = None,
        object_key: Optional[str] = None,
    ) -> 'ObjectAcl':
        pass


    def ObjectSummary(
        self,
        bucket_name: Optional[str] = None,
        key: Optional[str] = None,
    ) -> 'ObjectSummary':
        pass


    def ObjectVersion(
        self,
        bucket_name: Optional[str] = None,
        object_key: Optional[str] = None,
        id: Optional[str] = None,
    ) -> 'ObjectVersion':
        pass


    def create_bucket(
        self,
        Bucket: str,
        ACL: Optional[str] = None,
        CreateBucketConfiguration: Optional[Dict] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWrite: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        ObjectLockEnabledForBucket: Optional[bool] = None,
    ) -> 'Bucket':
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass



class Bucket(base.ServiceResource):
    creation_date: datetime
    name: str
    multipart_uploads: 'multipart_uploads'
    object_versions: 'object_versions'
    objects: 'objects'

    def copy(
        self,
        CopySource: Optional[Dict] = None,
        Key: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        SourceClient: Optional[BaseClient] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def create(
        self,
        ACL: Optional[str] = None,
        CreateBucketConfiguration: Optional[Dict] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWrite: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        ObjectLockEnabledForBucket: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete(
        self,
    ):
        pass


    def delete_objects(
        self,
        Delete: Dict,
        MFA: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        BypassGovernanceRetention: Optional[bool] = None,
    ) -> Dict:
        pass


    def download_file(
        self,
        Key: Optional[str] = None,
        Filename: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def download_fileobj(
        self,
        Fileobj: Optional[IO] = None,
        Key: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put_object(
        self,
        Key: str,
        ACL: Optional[str] = None,
        Body: Optional[Union[bytes, IO]] = None,
        CacheControl: Optional[str] = None,
        ContentDisposition: Optional[str] = None,
        ContentEncoding: Optional[str] = None,
        ContentLanguage: Optional[str] = None,
        ContentLength: Optional[int] = None,
        ContentMD5: Optional[str] = None,
        ContentType: Optional[str] = None,
        Expires: Optional[datetime] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        Metadata: Optional[Dict] = None,
        ServerSideEncryption: Optional[str] = None,
        StorageClass: Optional[str] = None,
        WebsiteRedirectLocation: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        SSEKMSKeyId: Optional[str] = None,
        SSEKMSEncryptionContext: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        Tagging: Optional[str] = None,
        ObjectLockMode: Optional[str] = None,
        ObjectLockRetainUntilDate: Optional[datetime] = None,
        ObjectLockLegalHoldStatus: Optional[str] = None,
    ) -> 'Object':
        pass


    def upload_file(
        self,
        Filename: Optional[str] = None,
        Key: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def upload_fileobj(
        self,
        Fileobj: Optional[IO] = None,
        Key: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def wait_until_exists(
        self,
    ):
        pass


    def wait_until_not_exists(
        self,
    ):
        pass



class BucketAcl(base.ServiceResource):
    owner: Dict
    grants: List
    bucket_name: str

    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        ACL: Optional[str] = None,
        AccessControlPolicy: Optional[Dict] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWrite: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass



class BucketCors(base.ServiceResource):
    cors_rules: List
    bucket_name: str

    def delete(
        self,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        CORSConfiguration: Dict,
    ):
        pass


    def reload(
        self,
    ):
        pass



class BucketLifecycle(base.ServiceResource):
    rules: List
    bucket_name: str

    def delete(
        self,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        LifecycleConfiguration: Optional[Dict] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass



class BucketLifecycleConfiguration(base.ServiceResource):
    rules: List
    bucket_name: str

    def delete(
        self,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        LifecycleConfiguration: Optional[Dict] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass



class BucketLogging(base.ServiceResource):
    logging_enabled: Dict
    bucket_name: str

    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        BucketLoggingStatus: Dict,
    ):
        pass


    def reload(
        self,
    ):
        pass



class BucketNotification(base.ServiceResource):
    topic_configurations: List
    queue_configurations: List
    lambda_function_configurations: List
    bucket_name: str

    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        NotificationConfiguration: Dict,
    ):
        pass


    def reload(
        self,
    ):
        pass



class BucketPolicy(base.ServiceResource):
    policy: str
    bucket_name: str

    def delete(
        self,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        Policy: str,
        ConfirmRemoveSelfBucketAccess: Optional[bool] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass



class BucketRequestPayment(base.ServiceResource):
    payer: str
    bucket_name: str

    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        RequestPaymentConfiguration: Dict,
    ):
        pass


    def reload(
        self,
    ):
        pass



class BucketTagging(base.ServiceResource):
    tag_set: List
    bucket_name: str

    def delete(
        self,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        Tagging: Dict,
    ):
        pass


    def reload(
        self,
    ):
        pass



class BucketVersioning(base.ServiceResource):
    status: str
    mfa_delete: str
    bucket_name: str

    def enable(
        self,
        MFA: Optional[str] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        VersioningConfiguration: Dict,
        MFA: Optional[str] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass


    def suspend(
        self,
        MFA: Optional[str] = None,
    ):
        pass



class BucketWebsite(base.ServiceResource):
    redirect_all_requests_to: Dict
    index_document: Dict
    error_document: Dict
    routing_rules: List
    bucket_name: str

    def delete(
        self,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        WebsiteConfiguration: Dict,
    ):
        pass


    def reload(
        self,
    ):
        pass



class MultipartUpload(base.ServiceResource):
    upload_id: str
    key: str
    initiated: datetime
    storage_class: str
    owner: Dict
    initiator: Dict
    bucket_name: str
    object_key: str
    id: str
    parts: 'parts'

    def abort(
        self,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def complete(
        self,
        MultipartUpload: Optional[Dict] = None,
        RequestPayer: Optional[str] = None,
    ) -> 'Object':
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass



class MultipartUploadPart(base.ServiceResource):
    last_modified: datetime
    e_tag: str
    size: int
    bucket_name: str
    object_key: str
    multipart_upload_id: str
    part_number: str

    def copy_from(
        self,
        CopySource: Union[str, Dict],
        CopySourceIfMatch: Optional[str] = None,
        CopySourceIfModifiedSince: Optional[datetime] = None,
        CopySourceIfNoneMatch: Optional[str] = None,
        CopySourceIfUnmodifiedSince: Optional[datetime] = None,
        CopySourceRange: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        CopySourceSSECustomerAlgorithm: Optional[str] = None,
        CopySourceSSECustomerKey: Optional[str] = None,
        CopySourceSSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def upload(
        self,
        Body: Optional[Union[bytes, IO]] = None,
        ContentLength: Optional[int] = None,
        ContentMD5: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass



class Object(base.ServiceResource):
    delete_marker: bool
    accept_ranges: str
    expiration: str
    restore: str
    last_modified: datetime
    content_length: int
    e_tag: str
    missing_meta: int
    version_id: str
    cache_control: str
    content_disposition: str
    content_encoding: str
    content_language: str
    content_type: str
    expires: datetime
    website_redirect_location: str
    server_side_encryption: str
    metadata: Dict
    sse_customer_algorithm: str
    sse_customer_key_md5: str
    ssekms_key_id: str
    storage_class: str
    request_charged: str
    replication_status: str
    parts_count: int
    object_lock_mode: str
    object_lock_retain_until_date: datetime
    object_lock_legal_hold_status: str
    bucket_name: str
    key: str

    def copy(
        self,
        CopySource: Optional[Dict] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        SourceClient: Optional[BaseClient] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def copy_from(
        self,
        CopySource: Union[str, Dict],
        ACL: Optional[str] = None,
        CacheControl: Optional[str] = None,
        ContentDisposition: Optional[str] = None,
        ContentEncoding: Optional[str] = None,
        ContentLanguage: Optional[str] = None,
        ContentType: Optional[str] = None,
        CopySourceIfMatch: Optional[str] = None,
        CopySourceIfModifiedSince: Optional[datetime] = None,
        CopySourceIfNoneMatch: Optional[str] = None,
        CopySourceIfUnmodifiedSince: Optional[datetime] = None,
        Expires: Optional[datetime] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        Metadata: Optional[Dict] = None,
        MetadataDirective: Optional[str] = None,
        TaggingDirective: Optional[str] = None,
        ServerSideEncryption: Optional[str] = None,
        StorageClass: Optional[str] = None,
        WebsiteRedirectLocation: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        SSEKMSKeyId: Optional[str] = None,
        SSEKMSEncryptionContext: Optional[str] = None,
        CopySourceSSECustomerAlgorithm: Optional[str] = None,
        CopySourceSSECustomerKey: Optional[str] = None,
        CopySourceSSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        Tagging: Optional[str] = None,
        ObjectLockMode: Optional[str] = None,
        ObjectLockRetainUntilDate: Optional[datetime] = None,
        ObjectLockLegalHoldStatus: Optional[str] = None,
    ) -> Dict:
        pass


    def delete(
        self,
        MFA: Optional[str] = None,
        VersionId: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        BypassGovernanceRetention: Optional[bool] = None,
    ) -> Dict:
        pass


    def download_file(
        self,
        Filename: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def download_fileobj(
        self,
        Fileobj: Optional[IO] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def get(
        self,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        ResponseCacheControl: Optional[str] = None,
        ResponseContentDisposition: Optional[str] = None,
        ResponseContentEncoding: Optional[str] = None,
        ResponseContentLanguage: Optional[str] = None,
        ResponseContentType: Optional[str] = None,
        ResponseExpires: Optional[datetime] = None,
        VersionId: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def initiate_multipart_upload(
        self,
        ACL: Optional[str] = None,
        CacheControl: Optional[str] = None,
        ContentDisposition: Optional[str] = None,
        ContentEncoding: Optional[str] = None,
        ContentLanguage: Optional[str] = None,
        ContentType: Optional[str] = None,
        Expires: Optional[datetime] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        Metadata: Optional[Dict] = None,
        ServerSideEncryption: Optional[str] = None,
        StorageClass: Optional[str] = None,
        WebsiteRedirectLocation: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        SSEKMSKeyId: Optional[str] = None,
        SSEKMSEncryptionContext: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        Tagging: Optional[str] = None,
        ObjectLockMode: Optional[str] = None,
        ObjectLockRetainUntilDate: Optional[datetime] = None,
        ObjectLockLegalHoldStatus: Optional[str] = None,
    ) -> 'MultipartUpload':
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        ACL: Optional[str] = None,
        Body: Optional[Union[bytes, IO]] = None,
        CacheControl: Optional[str] = None,
        ContentDisposition: Optional[str] = None,
        ContentEncoding: Optional[str] = None,
        ContentLanguage: Optional[str] = None,
        ContentLength: Optional[int] = None,
        ContentMD5: Optional[str] = None,
        ContentType: Optional[str] = None,
        Expires: Optional[datetime] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        Metadata: Optional[Dict] = None,
        ServerSideEncryption: Optional[str] = None,
        StorageClass: Optional[str] = None,
        WebsiteRedirectLocation: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        SSEKMSKeyId: Optional[str] = None,
        SSEKMSEncryptionContext: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        Tagging: Optional[str] = None,
        ObjectLockMode: Optional[str] = None,
        ObjectLockRetainUntilDate: Optional[datetime] = None,
        ObjectLockLegalHoldStatus: Optional[str] = None,
    ) -> Dict:
        pass


    def reload(
        self,
    ):
        pass


    def restore_object(
        self,
        VersionId: Optional[str] = None,
        RestoreRequest: Optional[Dict] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def upload_file(
        self,
        Filename: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def upload_fileobj(
        self,
        Fileobj: Optional[IO] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def wait_until_exists(
        self,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        VersionId: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
    ):
        pass


    def wait_until_not_exists(
        self,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        VersionId: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
    ):
        pass



class ObjectAcl(base.ServiceResource):
    owner: Dict
    grants: List
    request_charged: str
    bucket_name: str
    object_key: str

    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        ACL: Optional[str] = None,
        AccessControlPolicy: Optional[Dict] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWrite: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        VersionId: Optional[str] = None,
    ) -> Dict:
        pass


    def reload(
        self,
    ):
        pass



class ObjectSummary(base.ServiceResource):
    last_modified: datetime
    e_tag: str
    size: int
    storage_class: str
    owner: Dict
    bucket_name: str
    key: str

    def copy_from(
        self,
        CopySource: Union[str, Dict],
        ACL: Optional[str] = None,
        CacheControl: Optional[str] = None,
        ContentDisposition: Optional[str] = None,
        ContentEncoding: Optional[str] = None,
        ContentLanguage: Optional[str] = None,
        ContentType: Optional[str] = None,
        CopySourceIfMatch: Optional[str] = None,
        CopySourceIfModifiedSince: Optional[datetime] = None,
        CopySourceIfNoneMatch: Optional[str] = None,
        CopySourceIfUnmodifiedSince: Optional[datetime] = None,
        Expires: Optional[datetime] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        Metadata: Optional[Dict] = None,
        MetadataDirective: Optional[str] = None,
        TaggingDirective: Optional[str] = None,
        ServerSideEncryption: Optional[str] = None,
        StorageClass: Optional[str] = None,
        WebsiteRedirectLocation: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        SSEKMSKeyId: Optional[str] = None,
        SSEKMSEncryptionContext: Optional[str] = None,
        CopySourceSSECustomerAlgorithm: Optional[str] = None,
        CopySourceSSECustomerKey: Optional[str] = None,
        CopySourceSSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        Tagging: Optional[str] = None,
        ObjectLockMode: Optional[str] = None,
        ObjectLockRetainUntilDate: Optional[datetime] = None,
        ObjectLockLegalHoldStatus: Optional[str] = None,
    ) -> Dict:
        pass


    def delete(
        self,
        MFA: Optional[str] = None,
        VersionId: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        BypassGovernanceRetention: Optional[bool] = None,
    ) -> Dict:
        pass


    def get(
        self,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        ResponseCacheControl: Optional[str] = None,
        ResponseContentDisposition: Optional[str] = None,
        ResponseContentEncoding: Optional[str] = None,
        ResponseContentLanguage: Optional[str] = None,
        ResponseContentType: Optional[str] = None,
        ResponseExpires: Optional[datetime] = None,
        VersionId: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def initiate_multipart_upload(
        self,
        ACL: Optional[str] = None,
        CacheControl: Optional[str] = None,
        ContentDisposition: Optional[str] = None,
        ContentEncoding: Optional[str] = None,
        ContentLanguage: Optional[str] = None,
        ContentType: Optional[str] = None,
        Expires: Optional[datetime] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        Metadata: Optional[Dict] = None,
        ServerSideEncryption: Optional[str] = None,
        StorageClass: Optional[str] = None,
        WebsiteRedirectLocation: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        SSEKMSKeyId: Optional[str] = None,
        SSEKMSEncryptionContext: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        Tagging: Optional[str] = None,
        ObjectLockMode: Optional[str] = None,
        ObjectLockRetainUntilDate: Optional[datetime] = None,
        ObjectLockLegalHoldStatus: Optional[str] = None,
    ) -> 'MultipartUpload':
        pass


    def load(
        self,
    ):
        pass


    def put(
        self,
        ACL: Optional[str] = None,
        Body: Optional[Union[bytes, IO]] = None,
        CacheControl: Optional[str] = None,
        ContentDisposition: Optional[str] = None,
        ContentEncoding: Optional[str] = None,
        ContentLanguage: Optional[str] = None,
        ContentLength: Optional[int] = None,
        ContentMD5: Optional[str] = None,
        ContentType: Optional[str] = None,
        Expires: Optional[datetime] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
        Metadata: Optional[Dict] = None,
        ServerSideEncryption: Optional[str] = None,
        StorageClass: Optional[str] = None,
        WebsiteRedirectLocation: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        SSEKMSKeyId: Optional[str] = None,
        SSEKMSEncryptionContext: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        Tagging: Optional[str] = None,
        ObjectLockMode: Optional[str] = None,
        ObjectLockRetainUntilDate: Optional[datetime] = None,
        ObjectLockLegalHoldStatus: Optional[str] = None,
    ) -> Dict:
        pass


    def restore_object(
        self,
        VersionId: Optional[str] = None,
        RestoreRequest: Optional[Dict] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def wait_until_exists(
        self,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        VersionId: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
    ):
        pass


    def wait_until_not_exists(
        self,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        VersionId: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
    ):
        pass



class ObjectVersion(base.ServiceResource):
    e_tag: str
    size: int
    storage_class: str
    key: str
    version_id: str
    is_latest: bool
    last_modified: datetime
    owner: Dict
    bucket_name: str
    object_key: str
    id: str

    def delete(
        self,
        MFA: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        BypassGovernanceRetention: Optional[bool] = None,
    ) -> Dict:
        pass


    def get(
        self,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        ResponseCacheControl: Optional[str] = None,
        ResponseContentDisposition: Optional[str] = None,
        ResponseContentEncoding: Optional[str] = None,
        ResponseContentLanguage: Optional[str] = None,
        ResponseContentType: Optional[str] = None,
        ResponseExpires: Optional[datetime] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def head(
        self,
        IfMatch: Optional[str] = None,
        IfModifiedSince: Optional[datetime] = None,
        IfNoneMatch: Optional[str] = None,
        IfUnmodifiedSince: Optional[datetime] = None,
        Range: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        PartNumber: Optional[int] = None,
    ) -> Dict:
        pass



class buckets(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Bucket']:
        pass


    @classmethod
    def filter(
        cls,
    ) -> List['Bucket']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
    ) -> List['Bucket']:
        pass


    @classmethod
    def page_size(
        cls,
    ) -> List['Bucket']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass

