from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Callable
from typing import Dict
from typing import IO
from typing import List
from typing import Union

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient

# pylint: disable=import-self
import mypy_boto3.s3.service_resource as s3_service_resource_scope


class ServiceResource(Boto3ServiceResource):
    buckets: s3_service_resource_scope.buckets

    # pylint: disable=arguments-differ
    def Bucket(self, name: str = None) -> s3_service_resource_scope.Bucket:
        pass

    # pylint: disable=arguments-differ
    def BucketAcl(self, bucket_name: str = None) -> s3_service_resource_scope.BucketAcl:
        pass

    # pylint: disable=arguments-differ
    def BucketCors(
        self, bucket_name: str = None
    ) -> s3_service_resource_scope.BucketCors:
        pass

    # pylint: disable=arguments-differ
    def BucketLifecycle(
        self, bucket_name: str = None
    ) -> s3_service_resource_scope.BucketLifecycle:
        pass

    # pylint: disable=arguments-differ
    def BucketLifecycleConfiguration(
        self, bucket_name: str = None
    ) -> s3_service_resource_scope.BucketLifecycleConfiguration:
        pass

    # pylint: disable=arguments-differ
    def BucketLogging(
        self, bucket_name: str = None
    ) -> s3_service_resource_scope.BucketLogging:
        pass

    # pylint: disable=arguments-differ
    def BucketNotification(
        self, bucket_name: str = None
    ) -> s3_service_resource_scope.BucketNotification:
        pass

    # pylint: disable=arguments-differ
    def BucketPolicy(
        self, bucket_name: str = None
    ) -> s3_service_resource_scope.BucketPolicy:
        pass

    # pylint: disable=arguments-differ
    def BucketRequestPayment(
        self, bucket_name: str = None
    ) -> s3_service_resource_scope.BucketRequestPayment:
        pass

    # pylint: disable=arguments-differ
    def BucketTagging(
        self, bucket_name: str = None
    ) -> s3_service_resource_scope.BucketTagging:
        pass

    # pylint: disable=arguments-differ
    def BucketVersioning(
        self, bucket_name: str = None
    ) -> s3_service_resource_scope.BucketVersioning:
        pass

    # pylint: disable=arguments-differ
    def BucketWebsite(
        self, bucket_name: str = None
    ) -> s3_service_resource_scope.BucketWebsite:
        pass

    # pylint: disable=arguments-differ
    def MultipartUpload(
        self, bucket_name: str = None, object_key: str = None, id: str = None
    ) -> s3_service_resource_scope.MultipartUpload:
        pass

    # pylint: disable=arguments-differ
    def MultipartUploadPart(
        self,
        bucket_name: str = None,
        object_key: str = None,
        multipart_upload_id: str = None,
        part_number: str = None,
    ) -> s3_service_resource_scope.MultipartUploadPart:
        pass

    # pylint: disable=arguments-differ
    def Object(
        self, bucket_name: str = None, key: str = None
    ) -> s3_service_resource_scope.Object:
        pass

    # pylint: disable=arguments-differ
    def ObjectAcl(
        self, bucket_name: str = None, object_key: str = None
    ) -> s3_service_resource_scope.ObjectAcl:
        pass

    # pylint: disable=arguments-differ
    def ObjectSummary(
        self, bucket_name: str = None, key: str = None
    ) -> s3_service_resource_scope.ObjectSummary:
        pass

    # pylint: disable=arguments-differ
    def ObjectVersion(
        self, bucket_name: str = None, object_key: str = None, id: str = None
    ) -> s3_service_resource_scope.ObjectVersion:
        pass

    # pylint: disable=arguments-differ
    def create_bucket(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class Bucket(Boto3ServiceResource):
    creation_date: datetime
    name: str
    multipart_uploads: s3_service_resource_scope.multipart_uploads
    object_versions: s3_service_resource_scope.object_versions
    objects: s3_service_resource_scope.objects

    # pylint: disable=arguments-differ
    def copy(
        self,
        CopySource: Dict[str, Any] = None,
        Key: str = None,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def create(
        self,
        ACL: str = None,
        CreateBucketConfiguration: Dict[str, Any] = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_objects(
        self,
        Delete: Dict[str, Any],
        MFA: str = None,
        RequestPayer: str = None,
        BypassGovernanceRetention: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def download_file(
        self,
        Key: str = None,
        Filename: str = None,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def download_fileobj(
        self,
        Fileobj: Union[Any] = None,
        Key: str = None,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put_object(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def upload_file(
        self,
        Filename: str = None,
        Key: str = None,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def upload_fileobj(
        self,
        Fileobj: Union[Any] = None,
        Key: str = None,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_exists(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_not_exists(self) -> None:
        pass


class BucketAcl(Boto3ServiceResource):
    owner: Dict
    grants: List
    bucket_name: str

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(
        self,
        ACL: str = None,
        AccessControlPolicy: Dict[str, Any] = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class BucketCors(Boto3ServiceResource):
    cors_rules: List
    bucket_name: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(self, CORSConfiguration: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class BucketLifecycle(Boto3ServiceResource):
    rules: List
    bucket_name: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(self, LifecycleConfiguration: Dict[str, Any] = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class BucketLifecycleConfiguration(Boto3ServiceResource):
    rules: List
    bucket_name: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(self, LifecycleConfiguration: Dict[str, Any] = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class BucketLogging(Boto3ServiceResource):
    logging_enabled: Dict
    bucket_name: str

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(self, BucketLoggingStatus: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class BucketNotification(Boto3ServiceResource):
    topic_configurations: List
    queue_configurations: List
    lambda_function_configurations: List
    bucket_name: str

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(self, NotificationConfiguration: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class BucketPolicy(Boto3ServiceResource):
    policy: str
    bucket_name: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(self, Policy: str, ConfirmRemoveSelfBucketAccess: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class BucketRequestPayment(Boto3ServiceResource):
    payer: str
    bucket_name: str

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(self, RequestPaymentConfiguration: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class BucketTagging(Boto3ServiceResource):
    tag_set: List
    bucket_name: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(self, Tagging: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class BucketVersioning(Boto3ServiceResource):
    status: str
    mfa_delete: str
    bucket_name: str

    # pylint: disable=arguments-differ
    def enable(self, MFA: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(self, VersioningConfiguration: Dict[str, Any], MFA: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def suspend(self, MFA: str = None) -> None:
        pass


class BucketWebsite(Boto3ServiceResource):
    redirect_all_requests_to: Dict
    index_document: Dict
    error_document: Dict
    routing_rules: List
    bucket_name: str

    # pylint: disable=arguments-differ
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(self, WebsiteConfiguration: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class MultipartUpload(Boto3ServiceResource):
    upload_id: str
    key: str
    initiated: datetime
    storage_class: str
    owner: Dict
    initiator: Dict
    bucket_name: str
    object_key: str
    id: str
    parts: s3_service_resource_scope.parts

    # pylint: disable=arguments-differ
    def abort(self, RequestPayer: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def complete(
        self, MultipartUpload: Dict[str, Any] = None, RequestPayer: str = None
    ) -> s3_service_resource_scope.Object:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class MultipartUploadPart(Boto3ServiceResource):
    last_modified: datetime
    e_tag: str
    size: int
    bucket_name: str
    object_key: str
    multipart_upload_id: str
    part_number: str

    # pylint: disable=arguments-differ
    def copy_from(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def upload(
        self,
        Body: Union[bytes, IO] = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: str = None,
    ) -> Dict[str, Any]:
        pass


class Object(Boto3ServiceResource):
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

    # pylint: disable=arguments-differ
    def copy(
        self,
        CopySource: Dict[str, Any] = None,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def copy_from(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def delete(
        self,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: str = None,
        BypassGovernanceRetention: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def download_file(
        self,
        Filename: str = None,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def download_fileobj(
        self,
        Fileobj: Union[Any] = None,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def initiate_multipart_upload(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def restore_object(
        self,
        VersionId: str = None,
        RestoreRequest: Dict[str, Any] = None,
        RequestPayer: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def upload_file(
        self,
        Filename: str = None,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def upload_fileobj(
        self,
        Fileobj: Union[Any] = None,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_exists(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def wait_until_not_exists(
        self,
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
        pass


class ObjectAcl(Boto3ServiceResource):
    owner: Dict
    grants: List
    request_charged: str
    bucket_name: str
    object_key: str

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class ObjectSummary(Boto3ServiceResource):
    last_modified: datetime
    e_tag: str
    size: int
    storage_class: str
    owner: Dict
    bucket_name: str
    key: str

    # pylint: disable=arguments-differ
    def copy_from(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def delete(
        self,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: str = None,
        BypassGovernanceRetention: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def initiate_multipart_upload(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def restore_object(
        self,
        VersionId: str = None,
        RestoreRequest: Dict[str, Any] = None,
        RequestPayer: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def wait_until_exists(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def wait_until_not_exists(
        self,
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
        pass


class ObjectVersion(Boto3ServiceResource):
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

    # pylint: disable=arguments-differ
    def delete(
        self,
        MFA: str = None,
        RequestPayer: str = None,
        BypassGovernanceRetention: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def head(
        self,
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
        pass


class buckets(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[s3_service_resource_scope.Bucket]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(cls) -> List[s3_service_resource_scope.Bucket]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls) -> List[s3_service_resource_scope.Bucket]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls) -> List[s3_service_resource_scope.Bucket]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class multipart_uploads(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[s3_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> List[s3_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[s3_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[s3_service_resource_scope.MultipartUpload]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class object_versions(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[s3_service_resource_scope.ObjectVersion]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def delete(
        cls,
        MFA: str = None,
        RequestPayer: str = None,
        BypassGovernanceRetention: bool = None,
    ) -> Dict[str, Any]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        VersionIdMarker: str = None,
    ) -> List[s3_service_resource_scope.ObjectVersion]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[s3_service_resource_scope.ObjectVersion]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[s3_service_resource_scope.ObjectVersion]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class objects(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[s3_service_resource_scope.ObjectSummary]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def delete(
        cls,
        MFA: str = None,
        RequestPayer: str = None,
        BypassGovernanceRetention: bool = None,
    ) -> Dict[str, Any]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        Marker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        RequestPayer: str = None,
    ) -> List[s3_service_resource_scope.ObjectSummary]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[s3_service_resource_scope.ObjectSummary]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[s3_service_resource_scope.ObjectSummary]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class parts(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[s3_service_resource_scope.MultipartUploadPart]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        MaxParts: int = None,
        PartNumberMarker: int = None,
        RequestPayer: str = None,
    ) -> List[s3_service_resource_scope.MultipartUploadPart]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[s3_service_resource_scope.MultipartUploadPart]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[s3_service_resource_scope.MultipartUploadPart]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass
