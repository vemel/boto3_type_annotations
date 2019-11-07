from datetime import datetime
from typing import Callable
from typing import Dict
from typing import IO
from typing import List
from typing import Optional
from typing import Union
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient



class Client(BaseClient):
    def abort_multipart_upload(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def complete_multipart_upload(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        MultipartUpload: Optional[Dict] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def copy(
        self,
        CopySource: Optional[Dict] = None,
        Bucket: Optional[str] = None,
        Key: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        SourceClient: Optional[BaseClient] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def copy_object(
        self,
        Bucket: str,
        CopySource: Union[str, Dict],
        Key: str,
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
    ) -> Dict:
        pass


    def create_multipart_upload(
        self,
        Bucket: str,
        Key: str,
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
    ) -> Dict:
        pass


    def delete_bucket(
        self,
        Bucket: str,
    ):
        pass


    def delete_bucket_analytics_configuration(
        self,
        Bucket: str,
        Id: str,
    ):
        pass


    def delete_bucket_cors(
        self,
        Bucket: str,
    ):
        pass


    def delete_bucket_encryption(
        self,
        Bucket: str,
    ):
        pass


    def delete_bucket_inventory_configuration(
        self,
        Bucket: str,
        Id: str,
    ):
        pass


    def delete_bucket_lifecycle(
        self,
        Bucket: str,
    ):
        pass


    def delete_bucket_metrics_configuration(
        self,
        Bucket: str,
        Id: str,
    ):
        pass


    def delete_bucket_policy(
        self,
        Bucket: str,
    ):
        pass


    def delete_bucket_replication(
        self,
        Bucket: str,
    ):
        pass


    def delete_bucket_tagging(
        self,
        Bucket: str,
    ):
        pass


    def delete_bucket_website(
        self,
        Bucket: str,
    ):
        pass


    def delete_object(
        self,
        Bucket: str,
        Key: str,
        MFA: Optional[str] = None,
        VersionId: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        BypassGovernanceRetention: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_object_tagging(
        self,
        Bucket: str,
        Key: str,
        VersionId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_objects(
        self,
        Bucket: str,
        Delete: Dict,
        MFA: Optional[str] = None,
        RequestPayer: Optional[str] = None,
        BypassGovernanceRetention: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_public_access_block(
        self,
        Bucket: str,
    ):
        pass


    def download_file(
        self,
        Bucket: Optional[str] = None,
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
        Bucket: Optional[str] = None,
        Key: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def generate_presigned_post(
        self,
        Bucket: Optional[str] = None,
        Key: Optional[str] = None,
        Fields: Optional[Dict] = None,
        Conditions: Optional[List] = None,
        ExpiresIn: Optional[int] = None,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_bucket_accelerate_configuration(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_acl(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_analytics_configuration(
        self,
        Bucket: str,
        Id: str,
    ) -> Dict:
        pass


    def get_bucket_cors(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_encryption(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_inventory_configuration(
        self,
        Bucket: str,
        Id: str,
    ) -> Dict:
        pass


    def get_bucket_lifecycle(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_lifecycle_configuration(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_location(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_logging(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_metrics_configuration(
        self,
        Bucket: str,
        Id: str,
    ) -> Dict:
        pass


    def get_bucket_notification(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_notification_configuration(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_policy(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_policy_status(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_replication(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_request_payment(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_tagging(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_versioning(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_bucket_website(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_object(
        self,
        Bucket: str,
        Key: str,
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


    def get_object_acl(
        self,
        Bucket: str,
        Key: str,
        VersionId: Optional[str] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def get_object_legal_hold(
        self,
        Bucket: str,
        Key: str,
        VersionId: Optional[str] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def get_object_lock_configuration(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_object_retention(
        self,
        Bucket: str,
        Key: str,
        VersionId: Optional[str] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def get_object_tagging(
        self,
        Bucket: str,
        Key: str,
        VersionId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_object_torrent(
        self,
        Bucket: str,
        Key: str,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_public_access_block(
        self,
        Bucket: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def head_bucket(
        self,
        Bucket: str,
    ):
        pass


    def head_object(
        self,
        Bucket: str,
        Key: str,
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
    ) -> Dict:
        pass


    def list_bucket_analytics_configurations(
        self,
        Bucket: str,
        ContinuationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_bucket_inventory_configurations(
        self,
        Bucket: str,
        ContinuationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_bucket_metrics_configurations(
        self,
        Bucket: str,
        ContinuationToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_buckets(
        self,
    ) -> Dict:
        pass


    def list_multipart_uploads(
        self,
        Bucket: str,
        Delimiter: Optional[str] = None,
        EncodingType: Optional[str] = None,
        KeyMarker: Optional[str] = None,
        MaxUploads: Optional[int] = None,
        Prefix: Optional[str] = None,
        UploadIdMarker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_object_versions(
        self,
        Bucket: str,
        Delimiter: Optional[str] = None,
        EncodingType: Optional[str] = None,
        KeyMarker: Optional[str] = None,
        MaxKeys: Optional[int] = None,
        Prefix: Optional[str] = None,
        VersionIdMarker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_objects(
        self,
        Bucket: str,
        Delimiter: Optional[str] = None,
        EncodingType: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxKeys: Optional[int] = None,
        Prefix: Optional[str] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def list_objects_v2(
        self,
        Bucket: str,
        Delimiter: Optional[str] = None,
        EncodingType: Optional[str] = None,
        MaxKeys: Optional[int] = None,
        Prefix: Optional[str] = None,
        ContinuationToken: Optional[str] = None,
        FetchOwner: Optional[bool] = None,
        StartAfter: Optional[str] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def list_parts(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        MaxParts: Optional[int] = None,
        PartNumberMarker: Optional[int] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def put_bucket_accelerate_configuration(
        self,
        Bucket: str,
        AccelerateConfiguration: Dict,
    ):
        pass


    def put_bucket_acl(
        self,
        Bucket: str,
        ACL: Optional[str] = None,
        AccessControlPolicy: Optional[Dict] = None,
        GrantFullControl: Optional[str] = None,
        GrantRead: Optional[str] = None,
        GrantReadACP: Optional[str] = None,
        GrantWrite: Optional[str] = None,
        GrantWriteACP: Optional[str] = None,
    ):
        pass


    def put_bucket_analytics_configuration(
        self,
        Bucket: str,
        Id: str,
        AnalyticsConfiguration: Dict,
    ):
        pass


    def put_bucket_cors(
        self,
        Bucket: str,
        CORSConfiguration: Dict,
    ):
        pass


    def put_bucket_encryption(
        self,
        Bucket: str,
        ServerSideEncryptionConfiguration: Dict,
        ContentMD5: Optional[str] = None,
    ):
        pass


    def put_bucket_inventory_configuration(
        self,
        Bucket: str,
        Id: str,
        InventoryConfiguration: Dict,
    ):
        pass


    def put_bucket_lifecycle(
        self,
        Bucket: str,
        LifecycleConfiguration: Optional[Dict] = None,
    ):
        pass


    def put_bucket_lifecycle_configuration(
        self,
        Bucket: str,
        LifecycleConfiguration: Optional[Dict] = None,
    ):
        pass


    def put_bucket_logging(
        self,
        Bucket: str,
        BucketLoggingStatus: Dict,
    ):
        pass


    def put_bucket_metrics_configuration(
        self,
        Bucket: str,
        Id: str,
        MetricsConfiguration: Dict,
    ):
        pass


    def put_bucket_notification(
        self,
        Bucket: str,
        NotificationConfiguration: Dict,
    ):
        pass


    def put_bucket_notification_configuration(
        self,
        Bucket: str,
        NotificationConfiguration: Dict,
    ):
        pass


    def put_bucket_policy(
        self,
        Bucket: str,
        Policy: str,
        ConfirmRemoveSelfBucketAccess: Optional[bool] = None,
    ):
        pass


    def put_bucket_replication(
        self,
        Bucket: str,
        ReplicationConfiguration: Dict,
        Token: Optional[str] = None,
    ):
        pass


    def put_bucket_request_payment(
        self,
        Bucket: str,
        RequestPaymentConfiguration: Dict,
    ):
        pass


    def put_bucket_tagging(
        self,
        Bucket: str,
        Tagging: Dict,
    ):
        pass


    def put_bucket_versioning(
        self,
        Bucket: str,
        VersioningConfiguration: Dict,
        MFA: Optional[str] = None,
    ):
        pass


    def put_bucket_website(
        self,
        Bucket: str,
        WebsiteConfiguration: Dict,
    ):
        pass


    def put_object(
        self,
        Bucket: str,
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
    ) -> Dict:
        pass


    def put_object_acl(
        self,
        Bucket: str,
        Key: str,
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


    def put_object_legal_hold(
        self,
        Bucket: str,
        Key: str,
        LegalHold: Optional[Dict] = None,
        RequestPayer: Optional[str] = None,
        VersionId: Optional[str] = None,
        ContentMD5: Optional[str] = None,
    ) -> Dict:
        pass


    def put_object_lock_configuration(
        self,
        Bucket: str,
        ObjectLockConfiguration: Optional[Dict] = None,
        RequestPayer: Optional[str] = None,
        Token: Optional[str] = None,
        ContentMD5: Optional[str] = None,
    ) -> Dict:
        pass


    def put_object_retention(
        self,
        Bucket: str,
        Key: str,
        Retention: Optional[Dict] = None,
        RequestPayer: Optional[str] = None,
        VersionId: Optional[str] = None,
        BypassGovernanceRetention: Optional[bool] = None,
        ContentMD5: Optional[str] = None,
    ) -> Dict:
        pass


    def put_object_tagging(
        self,
        Bucket: str,
        Key: str,
        Tagging: Dict,
        VersionId: Optional[str] = None,
        ContentMD5: Optional[str] = None,
    ) -> Dict:
        pass


    def put_public_access_block(
        self,
        Bucket: str,
        PublicAccessBlockConfiguration: Dict,
        ContentMD5: Optional[str] = None,
    ):
        pass


    def restore_object(
        self,
        Bucket: str,
        Key: str,
        VersionId: Optional[str] = None,
        RestoreRequest: Optional[Dict] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def select_object_content(
        self,
        Bucket: str,
        Key: str,
        Expression: str,
        ExpressionType: str,
        InputSerialization: Dict,
        OutputSerialization: Dict,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestProgress: Optional[Dict] = None,
        ScanRange: Optional[Dict] = None,
    ) -> Dict:
        pass


    def upload_file(
        self,
        Filename: Optional[str] = None,
        Bucket: Optional[str] = None,
        Key: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def upload_fileobj(
        self,
        Fileobj: Optional[IO] = None,
        Bucket: Optional[str] = None,
        Key: Optional[str] = None,
        ExtraArgs: Optional[Dict] = None,
        Callback: Optional[Callable] = None,
        Config: Optional[TransferConfig] = None,
    ):
        pass


    def upload_part(
        self,
        Bucket: str,
        Key: str,
        PartNumber: int,
        UploadId: str,
        Body: Optional[Union[bytes, IO]] = None,
        ContentLength: Optional[int] = None,
        ContentMD5: Optional[str] = None,
        SSECustomerAlgorithm: Optional[str] = None,
        SSECustomerKey: Optional[str] = None,
        SSECustomerKeyMD5: Optional[str] = None,
        RequestPayer: Optional[str] = None,
    ) -> Dict:
        pass


    def upload_part_copy(
        self,
        Bucket: str,
        CopySource: Union[str, Dict],
        Key: str,
        PartNumber: int,
        UploadId: str,
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

