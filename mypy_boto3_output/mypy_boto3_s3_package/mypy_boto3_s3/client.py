"Main interface for s3 Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Callable, Dict, IO, List, Union
from typing_extensions import Literal, overload
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3.type_defs import S3CopySource

# pylint: disable=import-self
import mypy_boto3_s3.client as client_scope

# pylint: disable=import-self
import mypy_boto3_s3.paginator as paginator_scope
from mypy_boto3_s3.type_defs import (
    ClientAbortMultipartUploadResponseTypeDef,
    ClientCompleteMultipartUploadMultipartUploadTypeDef,
    ClientCompleteMultipartUploadResponseTypeDef,
    ClientCopyObjectResponseTypeDef,
    ClientCreateBucketCreateBucketConfigurationTypeDef,
    ClientCreateBucketResponseTypeDef,
    ClientCreateMultipartUploadResponseTypeDef,
    ClientDeleteObjectResponseTypeDef,
    ClientDeleteObjectTaggingResponseTypeDef,
    ClientDeleteObjectsDeleteTypeDef,
    ClientDeleteObjectsResponseTypeDef,
    ClientGetBucketAccelerateConfigurationResponseTypeDef,
    ClientGetBucketAclResponseTypeDef,
    ClientGetBucketAnalyticsConfigurationResponseTypeDef,
    ClientGetBucketCorsResponseTypeDef,
    ClientGetBucketEncryptionResponseTypeDef,
    ClientGetBucketInventoryConfigurationResponseTypeDef,
    ClientGetBucketLifecycleConfigurationResponseTypeDef,
    ClientGetBucketLifecycleResponseTypeDef,
    ClientGetBucketLocationResponseTypeDef,
    ClientGetBucketLoggingResponseTypeDef,
    ClientGetBucketMetricsConfigurationResponseTypeDef,
    ClientGetBucketNotificationConfigurationResponseTypeDef,
    ClientGetBucketNotificationResponseTypeDef,
    ClientGetBucketPolicyResponseTypeDef,
    ClientGetBucketPolicyStatusResponseTypeDef,
    ClientGetBucketReplicationResponseTypeDef,
    ClientGetBucketRequestPaymentResponseTypeDef,
    ClientGetBucketTaggingResponseTypeDef,
    ClientGetBucketVersioningResponseTypeDef,
    ClientGetBucketWebsiteResponseTypeDef,
    ClientGetObjectAclResponseTypeDef,
    ClientGetObjectLegalHoldResponseTypeDef,
    ClientGetObjectLockConfigurationResponseTypeDef,
    ClientGetObjectResponseTypeDef,
    ClientGetObjectRetentionResponseTypeDef,
    ClientGetObjectTaggingResponseTypeDef,
    ClientGetObjectTorrentResponseTypeDef,
    ClientGetPublicAccessBlockResponseTypeDef,
    ClientHeadObjectResponseTypeDef,
    ClientListBucketAnalyticsConfigurationsResponseTypeDef,
    ClientListBucketInventoryConfigurationsResponseTypeDef,
    ClientListBucketMetricsConfigurationsResponseTypeDef,
    ClientListBucketsResponseTypeDef,
    ClientListMultipartUploadsResponseTypeDef,
    ClientListObjectVersionsResponseTypeDef,
    ClientListObjectsResponseTypeDef,
    ClientListObjectsV2ResponseTypeDef,
    ClientListPartsResponseTypeDef,
    ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef,
    ClientPutBucketAclAccessControlPolicyTypeDef,
    ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef,
    ClientPutBucketCorsCORSConfigurationTypeDef,
    ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef,
    ClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef,
    ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef,
    ClientPutBucketLifecycleLifecycleConfigurationTypeDef,
    ClientPutBucketLoggingBucketLoggingStatusTypeDef,
    ClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef,
    ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef,
    ClientPutBucketNotificationNotificationConfigurationTypeDef,
    ClientPutBucketReplicationReplicationConfigurationTypeDef,
    ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef,
    ClientPutBucketTaggingTaggingTypeDef,
    ClientPutBucketVersioningVersioningConfigurationTypeDef,
    ClientPutBucketWebsiteWebsiteConfigurationTypeDef,
    ClientPutObjectAclAccessControlPolicyTypeDef,
    ClientPutObjectAclResponseTypeDef,
    ClientPutObjectLegalHoldLegalHoldTypeDef,
    ClientPutObjectLegalHoldResponseTypeDef,
    ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef,
    ClientPutObjectLockConfigurationResponseTypeDef,
    ClientPutObjectResponseTypeDef,
    ClientPutObjectRetentionResponseTypeDef,
    ClientPutObjectRetentionRetentionTypeDef,
    ClientPutObjectTaggingResponseTypeDef,
    ClientPutObjectTaggingTaggingTypeDef,
    ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef,
    ClientRestoreObjectResponseTypeDef,
    ClientRestoreObjectRestoreRequestTypeDef,
    ClientSelectObjectContentInputSerializationTypeDef,
    ClientSelectObjectContentOutputSerializationTypeDef,
    ClientSelectObjectContentRequestProgressTypeDef,
    ClientSelectObjectContentScanRangeTypeDef,
    ClientUploadPartCopyResponseTypeDef,
    ClientUploadPartResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_s3.waiter as waiter_scope


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def abort_multipart_upload(
        self, Bucket: str, Key: str, UploadId: str, RequestPayer: str = None
    ) -> ClientAbortMultipartUploadResponseTypeDef:
        """
        This operation aborts a multipart upload. After a multipart upload is aborted, no additional parts
        can be uploaded using that upload ID. The storage consumed by any previously uploaded parts will be
        freed. However, if any part uploads are currently in progress, those part uploads might or might
        not succeed. As a result, it might be necessary to abort a given multipart upload multiple times in
        order to completely free all storage consumed by all parts.

        To verify that all parts have been removed, so you don't get charged for the part storage, you
        should call the  ListParts operation and ensure the parts list is empty.

        For information on permissions required to use the multipart upload API, see `Multipart Upload API
        and Permissions <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html>`__ .

        The following operations are related to ``AbortMultipartUpload``

        *  CreateMultipartUpload

        *  UploadPart

        *  CompleteMultipartUpload

        *  ListParts

        *  ListMultipartUploads

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/AbortMultipartUpload>`_

        **Request Syntax**
        ::

          response = client.abort_multipart_upload(
              Bucket='string',
              Key='string',
              UploadId='string',
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket to which the upload was taking place.

        :type Key: string
        :param Key: **[REQUIRED]**

          Key of the object for which the multipart upload was initiated.

        :type UploadId: string
        :param UploadId: **[REQUIRED]**

          Upload ID that identifies the multipart upload.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def complete_multipart_upload(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        MultipartUpload: ClientCompleteMultipartUploadMultipartUploadTypeDef = None,
        RequestPayer: str = None,
    ) -> ClientCompleteMultipartUploadResponseTypeDef:
        """
        Completes a multipart upload by assembling previously uploaded parts.

        You first initiate the multipart upload and then upload all parts using the  UploadPart operation.
        After successfully uploading all relevant parts of an upload, you call this operation to complete
        the upload. Upon receiving this request, Amazon S3 concatenates all the parts in ascending order by
        part number to create a new object. In the Complete Multipart Upload request, you must provide the
        parts list. You must ensure the parts list is complete, this operation concatenates the parts you
        provide in the list. For each part in the list, you must provide the part number and the ``ETag``
        value, returned after that part was uploaded.

        Processing of a Complete Multipart Upload request could take several minutes to complete. After
        Amazon S3 begins processing the request, it sends an HTTP response header that specifies a 200 OK
        response. While processing is in progress, Amazon S3 periodically sends whitespace characters to
        keep the connection from timing out. Because a request could fail after the initial 200 OK response
        has been sent, it is important that you check the response body to determine whether the request
        succeeded.

        Note that if ``CompleteMultipartUpload`` fails, applications should be prepared to retry the failed
        requests. For more information, see `Amazon S3 Error Best Practices
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/ErrorBestPractices.html>`__ .

        For more information on multipart uploads, see `Uploading Objects Using Multipart Upload
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html>`__ .

        For information on permissions required to use the multipart upload API, see `Multipart Upload API
        and Permissions <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html>`__ .

         ``GetBucketLifecycle`` has the following special errors:

        * Error code: ``EntityTooSmall``

          * Description: Your proposed upload is smaller than the minimum allowed object size. Each part
          must be at least 5 MB in size, except the last part.

          * 400 Bad Request

        * Error code: ``InvalidPart``

          * Description: One or more of the specified parts could not be found. The part might not have
          been uploaded, or the specified entity tag might not have matched the part's entity tag.

          * 400 Bad Request

        * Error code: ``InvalidPartOrder``

          * Description: The list of parts was not in ascending order. The parts list must be specified in
          order by part number.

          * 400 Bad Request

        * Error code: ``NoSuchUpload``

          * Description: The specified multipart upload does not exist. The upload ID might be invalid, or
          the multipart upload might have been aborted or completed.

          * 404 Not Found

        The following operations are related to ``DeleteBucketMetricsConfiguration`` :

        *  CreateMultipartUpload

        *  UploadPart

        *  AbortMultipartUpload

        *  ListParts

        *  ListMultipartUploads

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CompleteMultipartUpload>`_

        **Request Syntax**
        ::

          response = client.complete_multipart_upload(
              Bucket='string',
              Key='string',
              MultipartUpload={
                  'Parts': [
                      {
                          'ETag': 'string',
                          'PartNumber': 123
                      },
                  ]
              },
              UploadId='string',
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket to which the multipart upload was initiated.

        :type Key: string
        :param Key: **[REQUIRED]**

          Object key for which the multipart upload was initiated.

        :type MultipartUpload: dict
        :param MultipartUpload:

          The container for the multipart upload request information.

          - **Parts** *(list) --*

            Array of CompletedPart data types.

            - *(dict) --*

              Details of the parts that were uploaded.

              - **ETag** *(string) --*

                Entity tag returned when the part was uploaded.

              - **PartNumber** *(integer) --*

                Part number that identifies the part. This is a positive integer between 1 and 10,000.

        :type UploadId: string
        :param UploadId: **[REQUIRED]**

          ID for the initiated multipart upload.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Location': 'string',
                'Bucket': 'string',
                'Key': 'string',
                'Expiration': 'string',
                'ETag': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'VersionId': 'string',
                'SSEKMSKeyId': 'string',
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **Location** *(string) --*

              The URI that identifies the newly created object.

            - **Bucket** *(string) --*

              The name of the bucket that contains the newly created object.

            - **Key** *(string) --*

              The object key of the newly created object.

            - **Expiration** *(string) --*

              If the object expiration is configured, this will contain the expiration date (expiry-date)
              and rule ID (rule-id). The value of rule-id is URL encoded.

            - **ETag** *(string) --*

              Entity tag that identifies the newly created object's data. Objects with different object
              data will have different entity tags. The entity tag is an opaque string. The entity tag may
              or may not be an MD5 digest of the object data. If the entity tag is not an MD5 digest of the
              object data, it will contain one or more nonhexadecimal characters and/or will consist of
              less than 32 or more than 32 hexadecimal digits.

            - **ServerSideEncryption** *(string) --*

              If you specified server-side encryption either with an Amazon S3-managed encryption key or an
              AWS KMS customer master key (CMK) in your initiate multipart upload request, the response
              includes this header. It confirms the encryption algorithm that Amazon S3 used to encrypt the
              object.

            - **VersionId** *(string) --*

              Version ID of the newly created object, in case the bucket has versioning turned on.

            - **SSEKMSKeyId** *(string) --*

              If present, specifies the ID of the AWS Key Management Service (KMS) customer master key
              (CMK) that was used for the object.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy(
        self,
        CopySource: S3CopySource,
        Bucket: str,
        Key: str,
        ExtraArgs: Dict = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Copy an object from one S3 location to another.

        This is a managed transfer which will perform a multipart copy in
        multiple threads if necessary.

        Usage::

            import boto3
            s3 = boto3.resource('s3')
            copy_source = {
                'Bucket': 'mybucket',
                'Key': 'mykey'
            }
            s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')

        :type CopySource: dict
        :param CopySource: The name of the source bucket, key name of the
            source object, and optional version ID of the source object. The
            dictionary format is:
            ``{'Bucket': 'bucket', 'Key': 'key', 'VersionId': 'id'}``. Note
            that the ``VersionId`` key is optional and may be omitted.

        :type Bucket: str
        :param Bucket: The name of the bucket to copy to

        :type Key: str
        :param Key: The name of the key to copy to

        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation

        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the copy.

        :type SourceClient: botocore or boto3 Client
        :param SourceClient: The client to be used for operation that
            may happen at the source object. For example, this client is
            used for the head_object that determines the size of the copy.
            If no client is provided, the current client is used as the client
            for the source object.

        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            copy.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_object(
        self,
        Bucket: str,
        CopySource: Union[S3CopySource, str],
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
        Metadata: Dict[str, str] = None,
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
    ) -> ClientCopyObjectResponseTypeDef:
        """
        Creates a copy of an object that is already stored in Amazon S3.

        .. note::

          You can store individual objects of up to 5 TB in Amazon S3. You create a copy of your object up
          to 5 GB in size in a single atomic operation using this API. However, for copying an object
          greater than 5 GB, you must use the multipart upload Upload Part - Copy API. For conceptual
          information, see `Copy Object Using the REST Multipart Upload API
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/CopyingObjctsUsingRESTMPUapi.html>`__ .

        When copying an object, you can preserve all metadata (default) or specify new metadata. However,
        the ACL is not preserved and is set to private for the user making the request. To override the
        default ACL setting, specify a new ACL when generating a copy request. For more information, see
        `Using ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html>`__ .

        .. warning::

          Amazon S3 Transfer Acceleration does not support cross-region copies. If you request a
          cross-region copy using a Transfer Acceleration endpoint, you get a 400 ``Bad Request`` error.
          For more information about transfer acceleration, see `Transfer Acceleration
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html>`__ .

        All copy requests must be authenticated. Additionally, you must have *read* access to the source
        object and *write* access to the destination bucket. For more information, see `REST Authentication
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html>`__ . Both the Region that
        you want to copy the object from and the Region that you want to copy the object to must be enabled
        for your account.

        To only copy an object under certain conditions, such as whether the Etag matches or whether the
        object was modified before or after a specified date, use the request parameters
        ``x-amz-copy-source-if-match`` , ``x-amz-copy-source-if-none-match`` ,
        ``x-amz-copy-source-if-unmodified-since`` , or ``x-amz-copy-source-if-modified-since`` .

        .. note::

          All headers with the x-amz- prefix, including x-amz-copy-source, must be signed.

        You can use this operation to change the storage class of an object that is already stored in
        Amazon S3 using the StorageClass parameter. For more information, see `Storage Classes
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html>`__ .

        The source object that you are copying can be encrypted or unencrypted. If the source object is
        encrypted, it can be encrypted by server-side encryption using AWS-managed encryption keys or by
        using a customer-provided encryption key. When copying an object, you can request that Amazon S3
        encrypt the target object by using either the AWS-managed encryption keys or by using your own
        encryption key. You can do this regardless of the form of server-side encryption that was used to
        encrypt the source, or even if the source object was not encrypted. For more information about
        server-side encryption, see `Using Server-Side Encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html>`__ .

        A copy request might return an error when Amazon S3 receives the copy request or while Amazon S3 is
        copying the files. If the error occurs before the copy operation starts, you receive a standard
        Amazon S3 error. If the error occurs during the copy operation, the error response is embedded in
        the 200 OK response. This means that a ``200 OK`` response can contain either a success or an
        error. Design your application to parse the contents of the response and handle it appropriately.

        If the copy is successful, you receive a response with information about the copied object.

        .. note::

          If the request is an HTTP 1.1 request, the response is chunk encoded. If it were not, it would
          not contain the content-length, and you would need to read the entire body.

        Consider the following when using request headers:

        * Consideration 1 – If both the x-amz-copy-source-if-match and
        x-amz-copy-source-if-unmodified-since headers are present in the request and evaluate as follows,
        Amazon S3 returns 200 OK and copies the data:

          * x-amz-copy-source-if-match condition evaluates to true

          * x-amz-copy-source-if-unmodified-since condition evaluates to false

        * Consideration 2 – If both of the x-amz-copy-source-if-none-match and
        x-amz-copy-source-if-modified-since headers are present in the request and evaluate as follows,
        Amazon S3 returns the 412 Precondition Failed response code:

          * x-amz-copy-source-if-none-match condition evaluates to false

          * x-amz-copy-source-if-modified-since condition evaluates to true

        The copy request charge is based on the storage class and Region you specify for the destination
        object. For pricing information, see `Amazon S3 Pricing <https://aws.amazon.com/s3/pricing/>`__ .

        Following are other considerations when using ``CopyObject`` :

          Versioning

        By default, ``x-amz-copy-source`` identifies the current version of an object to copy. (If the
        current version is a delete marker, Amazon S3 behaves as if the object was deleted.) To copy a
        different version, use the ``versionId`` subresource.

        If you enable versioning on the target bucket, Amazon S3 generates a unique version ID for the
        object being copied. This version ID is different from the version ID of the source object. Amazon
        S3 returns the version ID of the copied object in the x-amz-version-id response header in the
        response.

        If you do not enable versioning or suspend it on the target bucket, the version ID that Amazon S3
        generates is always null.

        If the source object's storage class is GLACIER, then you must restore a copy of this object before
        you can use it as a source object for the copy operation. For more information, see .

          Access Permissions

        When copying an object, you can optionally specify the accounts or groups that should be granted
        specific permissions on the new object. There are two ways to grant the permissions using the
        request headers:

        * Specify a canned ACL with the ``x-amz-acl`` request header. For more information, see `Canned ACL
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__ .

        * Specify access permissions explicitly with the ``x-amz-grant-read`` , ``x-amz-grant-read-acp`` ,
        ``x-amz-grant-write-acp`` , and ``x-amz-grant-full-control`` headers. These parameters map to the
        set of permissions that Amazon S3 supports in an ACL. For more information, see `Access Control
        List (ACL) Overview <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html>`__ .

        You can use either a canned ACL or specify access permissions explicitly. You cannot do both.

          Server-Side- Encryption-Specific Request Headers

        To encrypt the target object, you must provide the appropriate encryption-related request headers.
        The one you use depends on whether you want to use AWS-managed encryption keys or provide your own
        encryption key.

        * To encrypt the target object using server-side encryption with an AWS-managed encryption key,
        provide the following request headers, as appropriate.

          * x-amz-server-side​-encryption

          * x-amz-server-side-encryption-aws-kms-key-id

          * x-amz-server-side-encryption-context

        .. note::

          If you specify x-amz-server-side-encryption:aws:kms, but don't provide x-amz-server-side-
          encryption-aws-kms-key-id, Amazon S3 uses the AWS managed customer master key (CMK) in KMS to
          protect the data.

        .. warning::

          All GET and PUT requests for an object protected by AWS KMS fail if you don't make them with SSL
          or by using SigV4.

        For more information on Server-Side Encryption with CMKs stored in Amazon KMS (SSE-KMS), see
        `Protecting Data Using Server-Side Encryption with CMKs stored in KMS
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ .

        * To encrypt the target object using server-side encryption with an encryption key that you
        provide, use the following headers.

          * x-amz-server-side​-encryption​-customer-algorithm

          * x-amz-server-side​-encryption​-customer-key

          * x-amz-server-side​-encryption​-customer-key-MD5

        * If the source object is encrypted using server-side encryption with customer-provided encryption
        keys, you must use the following headers.

          * x-amz-copy-source​-server-side​-encryption​-customer-algorithm

          * x-amz-copy-source​-server-side​-encryption​-customer-key

          * x-amz-copy-source-​server-side​-encryption​-customer-key-MD5

        For more information on Server-Side Encryption with CMKs stored in Amazon KMS (SSE-KMS), see
        `Protecting Data Using Server-Side Encryption with CMKs stored in Amazon KMS
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ .

          Access-Control-List (ACL)-Specific Request Headers

        You also can use the following access control–related headers with this operation. By default, all
        objects are private. Only the owner has full access control. When adding a new object, you can
        grant permissions to individual AWS accounts or to predefined groups defined by Amazon S3. These
        permissions are then added to the Access Control List (ACL) on the object. For more information,
        see `Using ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html>`__ . With
        this operation, you can grant access permissions using one of the following two methods:

        * Specify a canned ACL (x-amz-acl) — Amazon S3 supports a set of predefined ACLs, known as canned
        ACLs. Each canned ACL has a predefined set of grantees and permissions. For more information, see
        `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__ .

        * Specify access permissions explicitly — To explicitly grant access permissions to specific AWS
        accounts or groups, use the following headers. Each header maps to specific permissions that Amazon
        S3 supports in an ACL. For more information, see `Access Control List (ACL) Overview
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html>`__ . In the header, you specify
        a list of grantees who get the specific permission. To grant permissions explicitly use:

          * x-amz-grant-read

          * x-amz-grant-write

          * x-amz-grant-read-acp

          * x-amz-grant-write-acp

          * x-amz-grant-full-control

        You specify each grantee as a type=value pair, where the type is one of the following:

          * emailAddress – if the value specified is the email address of an AWS account

          * id – if the value specified is the canonical user ID of an AWS account

          * uri – if you are granting permissions to a predefined group

        For example, the following x-amz-grant-read header grants the AWS accounts identified by email
        addresses permissions to read object data and its metadata:

         ``x-amz-grant-read: emailAddress="xyz@amazon.com", emailAddress="abc@amazon.com"``

        The following operation are related to ``CopyObject``

        *  PutObject

        *  GetObject

        For more information, see `Copying Objects
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/CopyingObjectsExamples.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CopyObject>`_

        **Request Syntax**
        ::

          response = client.copy_object(
              ACL=
                  'private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'
                  |'bucket-owner-read'|'bucket-owner-full-control',
              Bucket='string',
              CacheControl='string',
              ContentDisposition='string',
              ContentEncoding='string',
              ContentLanguage='string',
              ContentType='string',
              CopySource='string' or {'Bucket': 'string', 'Key': 'string', 'VersionId': 'string'},
              CopySourceIfMatch='string',
              CopySourceIfModifiedSince=datetime(2015, 1, 1),
              CopySourceIfNoneMatch='string',
              CopySourceIfUnmodifiedSince=datetime(2015, 1, 1),
              Expires=datetime(2015, 1, 1),
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWriteACP='string',
              Key='string',
              Metadata={
                  'string': 'string'
              },
              MetadataDirective='COPY'|'REPLACE',
              TaggingDirective='COPY'|'REPLACE',
              ServerSideEncryption='AES256'|'aws:kms',
              StorageClass=
                  'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'
                  |'GLACIER'|'DEEP_ARCHIVE',
              WebsiteRedirectLocation='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              SSEKMSKeyId='string',
              SSEKMSEncryptionContext='string',
              CopySourceSSECustomerAlgorithm='string',
              CopySourceSSECustomerKey='string',
              RequestPayer='requester',
              Tagging='string',
              ObjectLockMode='GOVERNANCE'|'COMPLIANCE',
              ObjectLockRetainUntilDate=datetime(2015, 1, 1),
              ObjectLockLegalHoldStatus='ON'|'OFF'
          )
        :type ACL: string
        :param ACL:

          The canned ACL to apply to the object.

        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the destination bucket.

        :type CacheControl: string
        :param CacheControl:

          Specifies caching behavior along the request/reply chain.

        :type ContentDisposition: string
        :param ContentDisposition:

          Specifies presentational information for the object.

        :type ContentEncoding: string
        :param ContentEncoding:

          Specifies what content encodings have been applied to the object and thus what decoding
          mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

        :type ContentLanguage: string
        :param ContentLanguage:

          The language the content is in.

        :type ContentType: string
        :param ContentType:

          A standard MIME type describing the format of the object data.

        :type CopySource: str or dict
        :param CopySource: **[REQUIRED]** The name of the source bucket, key name of the source object, and
        optional version ID of the source object.  You can either provide this value as a string or a
        dictionary.  The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want
        to copy a specific version.  You can also provide this value as a dictionary.  The dictionary
        format is recommended over the string format because it is more explicit.  The dictionary format
        is: {'Bucket': 'bucket', 'Key': 'key', 'VersionId': 'id'}.  Note that the VersionId key is optional
        and may be omitted.

        :type CopySourceIfMatch: string
        :param CopySourceIfMatch:

          Copies the object if its entity tag (ETag) matches the specified tag.

        :type CopySourceIfModifiedSince: datetime
        :param CopySourceIfModifiedSince:

          Copies the object if it has been modified since the specified time.

        :type CopySourceIfNoneMatch: string
        :param CopySourceIfNoneMatch:

          Copies the object if its entity tag (ETag) is different than the specified ETag.

        :type CopySourceIfUnmodifiedSince: datetime
        :param CopySourceIfUnmodifiedSince:

          Copies the object if it hasn't been modified since the specified time.

        :type Expires: datetime
        :param Expires:

          The date and time at which the object is no longer cacheable.

        :type GrantFullControl: string
        :param GrantFullControl:

          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

        :type GrantRead: string
        :param GrantRead:

          Allows grantee to read the object data and its metadata.

        :type GrantReadACP: string
        :param GrantReadACP:

          Allows grantee to read the object ACL.

        :type GrantWriteACP: string
        :param GrantWriteACP:

          Allows grantee to write the ACL for the applicable object.

        :type Key: string
        :param Key: **[REQUIRED]**

          The key of the destination object.

        :type Metadata: dict
        :param Metadata:

          A map of metadata to store with the object in S3.

          - *(string) --*

            - *(string) --*

        :type MetadataDirective: string
        :param MetadataDirective:

          Specifies whether the metadata is copied from the source object or replaced with metadata
          provided in the request.

        :type TaggingDirective: string
        :param TaggingDirective:

          Specifies whether the object tag-set are copied from the source object or replaced with tag-set
          provided in the request.

        :type ServerSideEncryption: string
        :param ServerSideEncryption:

          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).

        :type StorageClass: string
        :param StorageClass:

          The type of storage to use for the object. Defaults to 'STANDARD'.

        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation:

          If the bucket is configured as a website, redirects requests for this object to another object in
          the same bucket or to an external URL. Amazon S3 stores the value of this header in the object
          metadata.

        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:

          Specifies the algorithm to use to when encrypting the object (e.g., AES256).

        :type SSECustomerKey: string
        :param SSECustomerKey:

          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This
          value is used to store the object and then it is discarded; Amazon does not store the encryption
          key. The key must be appropriate for use with the algorithm specified in the
          x-amz-server-side​-encryption​-customer-algorithm header.

        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:

          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this
          header for a message integrity check to ensure the encryption key was transmitted without error.

            Please note that this parameter is automatically populated if it is not provided. Including
            this parameter is not required

        :type SSEKMSKeyId: string
        :param SSEKMSKeyId:

          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object
          protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring
          any of the officially supported AWS SDKs and CLI can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version

        :type SSEKMSEncryptionContext: string
        :param SSEKMSEncryptionContext:

          Specifies the AWS KMS Encryption Context to use for object encryption. The value of this header
          is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

        :type CopySourceSSECustomerAlgorithm: string
        :param CopySourceSSECustomerAlgorithm:

          Specifies the algorithm to use when decrypting the source object (e.g., AES256).

        :type CopySourceSSECustomerKey: string
        :param CopySourceSSECustomerKey:

          Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object.
          The encryption key provided in this header must be one that was used when the source object was
          created.

        :type CopySourceSSECustomerKeyMD5: string
        :param CopySourceSSECustomerKeyMD5:

          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this
          header for a message integrity check to ensure the encryption key was transmitted without error.

            Please note that this parameter is automatically populated if it is not provided. Including
            this parameter is not required

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type Tagging: string
        :param Tagging:

          The tag-set for the object destination object this value must be used in conjunction with the
          TaggingDirective. The tag-set must be encoded as URL Query parameters

        :type ObjectLockMode: string
        :param ObjectLockMode:

          The Object Lock mode that you want to apply to the copied object.

        :type ObjectLockRetainUntilDate: datetime
        :param ObjectLockRetainUntilDate:

          The date and time when you want the copied object's Object Lock to expire.

        :type ObjectLockLegalHoldStatus: string
        :param ObjectLockLegalHoldStatus:

          Specifies whether you want to apply a Legal Hold to the copied object.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CopyObjectResult': {
                    'ETag': 'string',
                    'LastModified': datetime(2015, 1, 1)
                },
                'Expiration': 'string',
                'CopySourceVersionId': 'string',
                'VersionId': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'SSEKMSEncryptionContext': 'string',
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **CopyObjectResult** *(dict) --*

              Container for all response elements.

              - **ETag** *(string) --*

                Returns the ETag of the new object. The ETag reflects only changes to the contents of an
                object, not its metadata. The source and destination ETag is identical for a successfully
                copied object.

              - **LastModified** *(datetime) --*

                Returns the date that the object was last modified.

            - **Expiration** *(string) --*

              If the object expiration is configured, the response includes this header.

            - **CopySourceVersionId** *(string) --*

              Version of the copied object in the destination bucket.

            - **VersionId** *(string) --*

              Version ID of the newly created copy.

            - **ServerSideEncryption** *(string) --*

              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256,
              aws:kms).

            - **SSECustomerAlgorithm** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header confirming the encryption algorithm used.

            - **SSECustomerKeyMD5** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header to provide round trip message integrity verification of the
              customer-provided encryption key.

            - **SSEKMSKeyId** *(string) --*

              If present, specifies the ID of the AWS Key Management Service (KMS) customer master key
              (CMK) that was used for the object.

            - **SSEKMSEncryptionContext** *(string) --*

              If present, specifies the AWS KMS Encryption Context to use for object encryption. The value
              of this header is a base64-encoded UTF-8 string holding JSON with the encryption context
              key-value pairs.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_bucket(
        self,
        Bucket: str,
        ACL: str = None,
        CreateBucketConfiguration: ClientCreateBucketCreateBucketConfigurationTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None,
    ) -> ClientCreateBucketResponseTypeDef:
        """
        Creates a new bucket. To create a bucket, you must register with Amazon S3 and have a valid AWS
        Access Key ID to authenticate requests. Anonymous requests are never allowed to create buckets. By
        creating the bucket, you become the bucket owner.

        Not every string is an acceptable bucket name. For information on bucket naming restrictions, see
        `Working with Amazon S3 Buckets
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html>`__ .

        By default, the bucket is created in the US East (N. Virginia) region. You can optionally specify a
        region in the request body. You might choose a region to optimize latency, minimize costs, or
        address regulatory requirements. For example, if you reside in Europe, you will probably find it
        advantageous to create buckets in the EU (Ireland) region. For more information, see `How to Select
        a Region for Your Buckets
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#access-bucket-intro>`__ .

        .. note::

          If you send your create bucket request to the s3.amazonaws.com endpoint, the request go to the
          us-east-1 region. Accordingly, the signature calculations in Signature Version 4 must use
          us-east-1 as region, even if the location constraint in the request specifies another region
          where the bucket is to be created. If you create a bucket in a region other than US East (N.
          Virginia) region, your application must be able to handle 307 redirect. For more information, see
          `Virtual Hosting of Buckets
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html>`__ .

        When creating a bucket using this operation, you can optionally specify the accounts or groups that
        should be granted specific permissions on the bucket. There are two ways to grant the appropriate
        permissions using the request headers.

        * Specify a canned ACL using the ``x-amz-acl`` request header. Amazon S3 supports a set of
        predefined ACLs, known as canned ACLs. Each canned ACL has a predefined set of grantees and
        permissions. For more information, see `Canned ACL
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__ .

        * Specify access permissions explicitly using the ``x-amz-grant-read`` , ``x-amz-grant-write`` ,
        ``x-amz-grant-read-acp`` , ``x-amz-grant-write-acp`` , ``x-amz-grant-full-control`` headers. These
        headers map to the set of permissions Amazon S3 supports in an ACL. For more information, see
        `Access Control List (ACL) Overview
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html>`__ . You specify each grantee
        as a type=value pair, where the type is one of the following:

          * emailAddress – if the value specified is the email address of an AWS account

          * id – if the value specified is the canonical user ID of an AWS account

          * uri – if you are granting permissions to a predefined group

        For example, the following x-amz-grant-read header grants the AWS accounts identified by email
        addresses permissions to read object data and its metadata:

         ``x-amz-grant-read: emailAddress="xyz@amazon.com", emailAddress="abc@amazon.com"``

        .. note::

          You can use either a canned ACL or specify access permissions explicitly. You cannot do both.

        The following operations are related to ``CreateBucket`` :

        *  PutObject

        *  DeleteBucket

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CreateBucket>`_

        **Request Syntax**
        ::

          response = client.create_bucket(
              ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
              Bucket='string',
              CreateBucketConfiguration={
                  'LocationConstraint':
                  'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'
                  |'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
              },
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWrite='string',
              GrantWriteACP='string',
              ObjectLockEnabledForBucket=True|False
          )
        :type ACL: string
        :param ACL:

          The canned ACL to apply to the bucket.

        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket to create.

        :type CreateBucketConfiguration: dict
        :param CreateBucketConfiguration:

          The configuration information for the bucket.

          - **LocationConstraint** *(string) --*

            Specifies the region where the bucket will be created. If you don't specify a region, the
            bucket is created in US East (N. Virginia) Region (us-east-1).

        :type GrantFullControl: string
        :param GrantFullControl:

          Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

        :type GrantRead: string
        :param GrantRead:

          Allows grantee to list the objects in the bucket.

        :type GrantReadACP: string
        :param GrantReadACP:

          Allows grantee to read the bucket ACL.

        :type GrantWrite: string
        :param GrantWrite:

          Allows grantee to create, overwrite, and delete any object in the bucket.

        :type GrantWriteACP: string
        :param GrantWriteACP:

          Allows grantee to write the ACL for the applicable bucket.

        :type ObjectLockEnabledForBucket: boolean
        :param ObjectLockEnabledForBucket:

          Specifies whether you want S3 Object Lock to be enabled for the new bucket.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Location': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Location** *(string) --*

              Specifies the region where the bucket will be created. If you are creating a bucket on the US
              East (N. Virginia) region (us-east-1), you do not need to specify the location.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_multipart_upload(
        self,
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
        Metadata: Dict[str, str] = None,
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
    ) -> ClientCreateMultipartUploadResponseTypeDef:
        """
        This operation initiates a multipart upload and returns an upload ID. This upload ID is used to
        associate all of the parts in the specific multipart upload. You specify this upload ID in each of
        your subsequent upload part requests (see  UploadPart ). You also include this upload ID in the
        final request to either complete or abort the multipart upload request.

        For more information about multipart uploads, see `Multipart Upload Overview
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>`__ .

        If you have configured a lifecycle rule to abort incomplete multipart uploads, the upload must
        complete within the number of days specified in the bucket lifecycle configuration. Otherwise, the
        incomplete multipart upload becomes eligible for an abort operation and Amazon S3 aborts the
        multipart upload. For more information, see `Aborting Incomplete Multipart Uploads Using a Bucket
        Lifecycle Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
        .

        For information about the permissions required to use the multipart upload API, see `Multipart
        Upload API and Permissions
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html>`__ .

        For request signing, multipart upload is just a series of regular requests. You initiate a
        multipart upload, send one or more requests to upload parts, and then complete the multipart upload
        process. You sign each request individually. There is nothing special about signing multipart
        upload requests. For more information about signing, see `Authenticating Requests (AWS Signature
        Version 4) <https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html>`__
        .

        .. note::

          After you initiate a multipart upload and upload one or more parts, to stop being charged for
          storing the uploaded parts, you must either complete or abort the multipart upload. Amazon S3
          frees up the space used to store the parts and stop charging you for storing them only after you
          either complete or abort a multipart upload.

        You can optionally request server-side encryption. For server-side encryption, Amazon S3 encrypts
        your data as it writes it to disks in its data centers and decrypts it when you access it. You can
        provide your own encryption key, or use AWS Key Management Service (AWS KMS) customer master keys
        (CMKs) or Amazon S3-managed encryption keys. If you choose to provide your own encryption key, the
        request headers you provide in  UploadPart ) and  UploadPartCopy ) requests must match the headers
        you used in the request to initiate the upload by using ``CreateMultipartUpload`` .

        To perform a multipart upload with encryption using an AWS KMS CMK, the requester must have
        permission to the ``kms:Encrypt`` , ``kms:Decrypt`` , ``kms:ReEncrypt*`` , ``kms:GenerateDataKey*``
        , and ``kms:DescribeKey`` actions on the key. These permissions are required because Amazon S3 must
        decrypt and read data from the encrypted file parts before it completes the multipart upload.

        If your AWS Identity and Access Management (IAM) user or role is in the same AWS account as the AWS
        KMS CMK, then you must have these permissions on the key policy. If your IAM user or role belongs
        to a different account than the key, then you must have the permissions on both the key policy and
        your IAM user or role.

        For more information, see `Protecting Data Using Server-Side Encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ .

          Access Permissions

        When copying an object, you can optionally specify the accounts or groups that should be granted
        specific permissions on the new object. There are two ways to grant the permissions using the
        request headers:

        * Specify a canned ACL with the ``x-amz-acl`` request header. For more information, see `Canned ACL
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__ .

        * Specify access permissions explicitly with the ``x-amz-grant-read`` , ``x-amz-grant-read-acp`` ,
        ``x-amz-grant-write-acp`` , and ``x-amz-grant-full-control`` headers. These parameters map to the
        set of permissions that Amazon S3 supports in an ACL. For more information, see `Access Control
        List (ACL) Overview <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html>`__ .

        You can use either a canned ACL or specify access permissions explicitly. You cannot do both.

          Server-Side- Encryption-Specific Request Headers

        You can optionally tell Amazon S3 to encrypt data at rest using server-side encryption. Server-side
        encryption is for data encryption at rest. Amazon S3 encrypts your data as it writes it to disks in
        its data centers and decrypts it when you access it. The option you use depends on whether you want
        to use AWS-managed encryption keys or provide your own encryption key.

        * Use encryption keys managed by Amazon S3 or customer master keys (CMKs) stored in Amazon Key
        Management Service (KMS) – If you want AWS to manage the keys used to encrypt data, specify the
        following headers in the request.

          * x-amz-server-side​-encryption

          * x-amz-server-side-encryption-aws-kms-key-id

          * x-amz-server-side-encryption-context

        .. note::

          If you specify x-amz-server-side-encryption:aws:kms, but don't provide x-amz-server-side-
          encryption-aws-kms-key-id, Amazon S3 uses the AWS managed CMK in AWS KMS to protect the data.

        .. warning::

          All GET and PUT requests for an object protected by AWS KMS fail if you don't make them with SSL
          or by using SigV4.

        For more information on Server-Side Encryption with CMKs Stored in Amazon KMS (SSE-KMS), see
        `Protecting Data Using Server-Side Encryption with CMKs stored in AWS KMS
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ .

        * Use customer-provided encryption keys – If you want to manage your own encryption keys, provide
        all the following headers in the request.

          * x-amz-server-side​-encryption​-customer-algorithm

          * x-amz-server-side​-encryption​-customer-key

          * x-amz-server-side​-encryption​-customer-key-MD5

        For more information on Server-Side Encryption with CMKs stored in AWS KMS (SSE-KMS), see
        `Protecting Data Using Server-Side Encryption with CMKs stored in AWS KMS
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ .

          Access-Control-List (ACL)-Specific Request Headers

        You also can use the following access control–related headers with this operation. By default, all
        objects are private. Only the owner has full access control. When adding a new object, you can
        grant permissions to individual AWS accounts or to predefined groups defined by Amazon S3. These
        permissions are then added to the Access Control List (ACL) on the object. For more information,
        see `Using ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html>`__ . With
        this operation, you can grant access permissions using one of the following two methods:

        * Specify a canned ACL (x-amz-acl) — Amazon S3 supports a set of predefined ACLs, known as canned
        ACLs. Each canned ACL has a predefined set of grantees and permissions. For more information, see
        `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__ .

        * Specify access permissions explicitly — To explicitly grant access permissions to specific AWS
        accounts or groups, use the following headers. Each header maps to specific permissions that Amazon
        S3 supports in an ACL. For more information, see `Access Control List (ACL) Overview
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html>`__ . In the header, you specify
        a list of grantees who get the specific permission. To grant permissions explicitly use:

          * x-amz-grant-read

          * x-amz-grant-write

          * x-amz-grant-read-acp

          * x-amz-grant-write-acp

          * x-amz-grant-full-control

        You specify each grantee as a type=value pair, where the type is one of the following:

          * emailAddress – if the value specified is the email address of an AWS account

          * id – if the value specified is the canonical user ID of an AWS account

          * uri – if you are granting permissions to a predefined group

        For example, the following x-amz-grant-read header grants the AWS accounts identified by email
        addresses permissions to read object data and its metadata:

         ``x-amz-grant-read: emailAddress="xyz@amazon.com", emailAddress="abc@amazon.com"``

        The following operations are related to ``CreateMultipartUpload`` :

        *  UploadPart

        *  CompleteMultipartUpload

        *  AbortMultipartUpload

        *  ListParts

        *  ListMultipartUploads

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CreateMultipartUpload>`_

        **Request Syntax**
        ::

          response = client.create_multipart_upload(
              ACL=
                  'private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'
                  |'bucket-owner-read'|'bucket-owner-full-control',
              Bucket='string',
              CacheControl='string',
              ContentDisposition='string',
              ContentEncoding='string',
              ContentLanguage='string',
              ContentType='string',
              Expires=datetime(2015, 1, 1),
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWriteACP='string',
              Key='string',
              Metadata={
                  'string': 'string'
              },
              ServerSideEncryption='AES256'|'aws:kms',
              StorageClass=
                  'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'
                  |'GLACIER'|'DEEP_ARCHIVE',
              WebsiteRedirectLocation='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              SSEKMSKeyId='string',
              SSEKMSEncryptionContext='string',
              RequestPayer='requester',
              Tagging='string',
              ObjectLockMode='GOVERNANCE'|'COMPLIANCE',
              ObjectLockRetainUntilDate=datetime(2015, 1, 1),
              ObjectLockLegalHoldStatus='ON'|'OFF'
          )
        :type ACL: string
        :param ACL:

          The canned ACL to apply to the object.

        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket to which to initiate the upload

        :type CacheControl: string
        :param CacheControl:

          Specifies caching behavior along the request/reply chain.

        :type ContentDisposition: string
        :param ContentDisposition:

          Specifies presentational information for the object.

        :type ContentEncoding: string
        :param ContentEncoding:

          Specifies what content encodings have been applied to the object and thus what decoding
          mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

        :type ContentLanguage: string
        :param ContentLanguage:

          The language the content is in.

        :type ContentType: string
        :param ContentType:

          A standard MIME type describing the format of the object data.

        :type Expires: datetime
        :param Expires:

          The date and time at which the object is no longer cacheable.

        :type GrantFullControl: string
        :param GrantFullControl:

          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

        :type GrantRead: string
        :param GrantRead:

          Allows grantee to read the object data and its metadata.

        :type GrantReadACP: string
        :param GrantReadACP:

          Allows grantee to read the object ACL.

        :type GrantWriteACP: string
        :param GrantWriteACP:

          Allows grantee to write the ACL for the applicable object.

        :type Key: string
        :param Key: **[REQUIRED]**

          Object key for which the multipart upload is to be initiated.

        :type Metadata: dict
        :param Metadata:

          A map of metadata to store with the object in S3.

          - *(string) --*

            - *(string) --*

        :type ServerSideEncryption: string
        :param ServerSideEncryption:

          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).

        :type StorageClass: string
        :param StorageClass:

          The type of storage to use for the object. Defaults to 'STANDARD'.

        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation:

          If the bucket is configured as a website, redirects requests for this object to another object in
          the same bucket or to an external URL. Amazon S3 stores the value of this header in the object
          metadata.

        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:

          Specifies the algorithm to use to when encrypting the object (e.g., AES256).

        :type SSECustomerKey: string
        :param SSECustomerKey:

          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This
          value is used to store the object and then it is discarded; Amazon does not store the encryption
          key. The key must be appropriate for use with the algorithm specified in the
          x-amz-server-side​-encryption​-customer-algorithm header.

        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:

          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this
          header for a message integrity check to ensure the encryption key was transmitted without error.

            Please note that this parameter is automatically populated if it is not provided. Including
            this parameter is not required

        :type SSEKMSKeyId: string
        :param SSEKMSKeyId:

          Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object
          protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring
          any of the officially supported AWS SDKs and CLI can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version

        :type SSEKMSEncryptionContext: string
        :param SSEKMSEncryptionContext:

          Specifies the AWS KMS Encryption Context to use for object encryption. The value of this header
          is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type Tagging: string
        :param Tagging:

          The tag-set for the object. The tag-set must be encoded as URL Query parameters

        :type ObjectLockMode: string
        :param ObjectLockMode:

          Specifies the Object Lock mode that you want to apply to the uploaded object.

        :type ObjectLockRetainUntilDate: datetime
        :param ObjectLockRetainUntilDate:

          Specifies the date and time when you want the Object Lock to expire.

        :type ObjectLockLegalHoldStatus: string
        :param ObjectLockLegalHoldStatus:

          Specifies whether you want to apply a Legal Hold to the uploaded object.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AbortDate': datetime(2015, 1, 1),
                'AbortRuleId': 'string',
                'Bucket': 'string',
                'Key': 'string',
                'UploadId': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'SSEKMSEncryptionContext': 'string',
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **AbortDate** *(datetime) --*

              If the bucket has a lifecycle rule configured with an action to abort incomplete multipart
              uploads and the prefix in the lifecycle rule matches the object name in the request, the
              response includes this header. The header indicates when the initiated multipart upload
              becomes eligible for an abort operation. For more information, see `Aborting Incomplete
              Multipart Uploads Using a Bucket Lifecycle Policy
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
              .

              The response also includes the x-amz-abort-rule-id header that provides the ID of the
              lifecycle configuration rule that defines this action.

            - **AbortRuleId** *(string) --*

              This header is returned along with the x-amz-abort-date header. It identifies the applicable
              lifecycle configuration rule that defines the action to abort incomplete multipart uploads.

            - **Bucket** *(string) --*

              Name of the bucket to which the multipart upload was initiated.

            - **Key** *(string) --*

              Object key for which the multipart upload was initiated.

            - **UploadId** *(string) --*

              ID for the initiated multipart upload.

            - **ServerSideEncryption** *(string) --*

              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256,
              aws:kms).

            - **SSECustomerAlgorithm** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header confirming the encryption algorithm used.

            - **SSECustomerKeyMD5** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header to provide round trip message integrity verification of the
              customer-provided encryption key.

            - **SSEKMSKeyId** *(string) --*

              If present, specifies the ID of the AWS Key Management Service (KMS) customer master key
              (CMK) that was used for the object.

            - **SSEKMSEncryptionContext** *(string) --*

              If present, specifies the AWS KMS Encryption Context to use for object encryption. The value
              of this header is a base64-encoded UTF-8 string holding JSON with the encryption context
              key-value pairs.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket(self, Bucket: str) -> None:
        """
        Deletes the bucket. All objects (including all object versions and Delete Markers) in the bucket
        must be deleted before the bucket itself can be deleted.

         **Related Resources**

        *

        *

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucket>`_

        **Request Syntax**
        ::

          response = client.delete_bucket(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Specifies the bucket being deleted.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket_analytics_configuration(self, Bucket: str, Id: str) -> None:
        """
        Deletes an analytics configuration for the bucket (specified by the analytics configuration ID).

        To use this operation, you must have permissions to perform the s3:PutAnalyticsConfiguration
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        For information about Amazon S3 analytics feature, see `Amazon S3 Analytics – Storage Class
        Analysis <https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html>`__ .

        The following operations are related to ``DeleteBucketAnalyticsConfiguration`` :

        *

        *

        *

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketAnalyticsConfiguration>`_

        **Request Syntax**
        ::

          response = client.delete_bucket_analytics_configuration(
              Bucket='string',
              Id='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket from which an analytics configuration is deleted.

        :type Id: string
        :param Id: **[REQUIRED]**

          The ID that identifies the analytics configuration.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket_cors(self, Bucket: str) -> None:
        """
        Deletes the ``cors`` configuration information set for the bucket.

        To use this operation, you must have permission to perform the ``s3:PutBucketCORS`` action. The
        bucket owner has this permission by default and can grant this permission to others.

        For information more about ``cors`` , go to `Enabling Cross-Origin Resource Sharing
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html>`__ in the *Amazon Simple Storage
        Service Developer Guide* .

         **Related Resources:**

        *

        *  RESTOPTIONSobject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketCors>`_

        **Request Syntax**
        ::

          response = client.delete_bucket_cors(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Specifies the bucket whose ``cors`` configuration is being deleted.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket_encryption(self, Bucket: str) -> None:
        """
        This implementation of the DELETE operation removes default encryption from the bucket. For
        information about the Amazon S3 default encryption feature, see `Amazon S3 Default Bucket
        Encryption <https://docs.aws.amazon.com/AmazonS3/latest/dev//bucket-encryption.html>`__ in the
        *Amazon Simple Storage Service Developer Guide* .

        To use this operation, you must have permissions to perform the ``s3:PutEncryptionConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//s3-access-control.html>`__ in the *Amazon Simple
        Storage Service Developer Guide* .

         **Related Resources**

        *  PutBucketEncryption

        *  GetBucketEncryption

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketEncryption>`_

        **Request Syntax**
        ::

          response = client.delete_bucket_encryption(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the server-side encryption configuration to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket_inventory_configuration(self, Bucket: str, Id: str) -> None:
        """
        Deletes an inventory configuration (identified by the inventory ID) from the bucket.

        To use this operation, you must have permissions to perform the ``s3:PutInventoryConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        For information about the Amazon S3 inventory feature, see `Amazon S3 Inventory
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html>`__ .

        Operation related to ``DeleteBucketInventoryConfiguration`` include:

        *  GetBucketInventoryConfiguration

        *  PutBucketInventoryConfiguration

        *  ListBucketInventoryConfigurations

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketInventoryConfiguration>`_

        **Request Syntax**
        ::

          response = client.delete_bucket_inventory_configuration(
              Bucket='string',
              Id='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the inventory configuration to delete.

        :type Id: string
        :param Id: **[REQUIRED]**

          The ID used to identify the inventory configuration.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket_lifecycle(self, Bucket: str) -> None:
        """
        Deletes the lifecycle configuration from the specified bucket. Amazon S3 removes all the lifecycle
        configuration rules in the lifecycle subresource associated with the bucket. Your objects never
        expire, and Amazon S3 no longer automatically deletes any objects on the basis of rules contained
        in the deleted lifecycle configuration.

        To use this operation, you must have permission to perform the ``s3:PutLifecycleConfiguration``
        action. By default, the bucket owner has this permission and the bucket owner can grant this
        permission to others.

        There is usually some time lag before lifecycle configuration deletion is fully propagated to all
        the Amazon S3 systems.

        For more information about the object expiration, see `Elements to Describe Lifecycle Actions
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#intro-lifecycle-rules-actions>`__
        .

        Related actions include:

        *  PutBucketLifecycleConfiguration

        *  GetBucketLifecycleConfiguration

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketLifecycle>`_

        **Request Syntax**
        ::

          response = client.delete_bucket_lifecycle(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name of the lifecycle to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket_metrics_configuration(self, Bucket: str, Id: str) -> None:
        """
        Deletes a metrics configuration for the Amazon CloudWatch request metrics (specified by the metrics
        configuration ID) from the bucket. Note that this doesn't include the daily storage metrics.

        To use this operation, you must have permissions to perform the ``s3:PutMetricsConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        For information about CloudWatch request metrics for Amazon S3, see `Monitoring Metrics with Amazon
        CloudWatch <https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html>`__ .

        The following operations are related to ``DeleteBucketMetricsConfiguration``

        *  GetBucketMetricsConfiguration

        *  PutBucketMetricsConfiguration

        *  ListBucketMetricsConfigurations

        * `Monitoring Metrics with Amazon CloudWatch
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html>`__

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketMetricsConfiguration>`_

        **Request Syntax**
        ::

          response = client.delete_bucket_metrics_configuration(
              Bucket='string',
              Id='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the metrics configuration to delete.

        :type Id: string
        :param Id: **[REQUIRED]**

          The ID used to identify the metrics configuration.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket_policy(self, Bucket: str) -> None:
        """
        This implementation of the DELETE operation uses the policysubresource to delete the policy of a
        specified bucket. If you are using an identity other than the root user of the AWS account that
        owns the bucket, the calling identity must have the ``DeleteBucketPolicy`` permissions on the
        specified bucket and belong to the bucket owner's account in order to use this operation.

        If you don't have ``DeleteBucketPolicy`` permissions, Amazon S3 returns a ``403 Access Denied``
        error. If you have the correct permissions, but you're notusing an identity that belongs to the
        bucket owner's account, Amazon S3 returns a ``405 Method Not Allowed`` error.

        .. warning::

          As a security precaution, the root user of the AWS account that owns a bucket can always use this
          operation, even if the policy explicitly denies the root user the ability to perform this action.

        For more information about bucket policies, see `Using Bucket Policies and UserPolicies <
        https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html>`__ .

        The following operations are related to ``DeleteBucketPolicy``

        *  CreateBucket

        *  DeleteObject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketPolicy>`_

        **Request Syntax**
        ::

          response = client.delete_bucket_policy(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket_replication(self, Bucket: str) -> None:
        """
        Deletes the replication configuration from the bucket.

        To use this operation, you must have permissions to perform the ``s3:PutReplicationConfiguration``
        action. The bucket owner has these permissions by default and can grant it to others. For more
        information about permissions, see `Permissions Related to Bucket Subresource Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        .. note::

          It can take a while for the deletion of a replication configuration to fully propagate.

        For information about replication configuration, see `Replication <
        https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html>`__ in the *Amazon S3 Developer
        Guide* .

        The following operations are related to ``DeleteBucketReplication``

        *  PutBucketReplication

        *  GetBucketReplication

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketReplication>`_

        **Request Syntax**
        ::

          response = client.delete_bucket_replication(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket_tagging(self, Bucket: str) -> None:
        """
        Deletes the tags from the bucket.

        To use this operation, you must have permission to perform the ``s3:PutBucketTagging`` action. By
        default, the bucket owner has this permission and can grant this permission to others.

        The following operations are related to ``DeleteBucketTagging``

        *  GetBucketTagging

        *  PutBucketTagging

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketTagging>`_

        **Request Syntax**
        ::

          response = client.delete_bucket_tagging(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket that has the tag set to be removed.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bucket_website(self, Bucket: str) -> None:
        """
        This operation removes the website configuration for a bucket. Amazon S3 returns a ``200 OK``
        response upon successfully deleting a website configuration on the specified bucket. You will get a
        ``200 OK`` response if the website configuration you are trying to delete does not exist on the
        bucket. Amazon S3 returns a ``404`` response if the bucket specified in the request does not exist.

        This DELETE operation requires the ``S3:DeleteBucketWebsite`` permission. By default, only the
        bucket owner can delete the website configuration attached to a bucket. However, bucket owners can
        grant other users permission to delete the website configuration by writing a bucket policy
        granting them the ``S3:DeleteBucketWebsite`` permission.

        For more information about hosting websites, see `Hosting Websites on Amazon S3
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html>`__ .

        The following operations are related to ``DeleteBucketWebsite``

        *  GetBucketWebsite

        *  PutBucketWebsite

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteBucketWebsite>`_

        **Request Syntax**
        ::

          response = client.delete_bucket_website(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name for which you want to remove the website configuration.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_object(
        self,
        Bucket: str,
        Key: str,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: str = None,
        BypassGovernanceRetention: bool = None,
    ) -> ClientDeleteObjectResponseTypeDef:
        """
        Removes the null version (if there is one) of an object and inserts a delete marker, which becomes
        the latest version of the object. If there isn't a null version, Amazon S3 does not remove any
        objects.

        To remove a specific version, you must be the bucket owner and you must use the version Id
        subresource. Using this subresource permanently deletes the version. If the object deleted is a
        delete marker, Amazon S3 sets the response header, x-amz-delete-marker, to true.

        If the object you want to delete is in a bucket where the bucket versioning configurationis MFA
        Delete enabled, you must include the x-amz-mfa request header in the DELETE versionId request.
        Requests that include x-amz-mfa must use HTTPS.

        For more information about MFA Delete, see `Using MFA Delete
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMFADelete.html>`__ . To see sample requests
        that use versioning, see `Sample Request
        <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectDELETE.html#ExampleVersionObjectDelete>`__
        .

        You can delete objects by explicitly calling the DELETE Object API or configure its lifecycle (
        PutBucketLifecycle ) to enable Amazon S3 to remove them for you. If you want to block users or
        accounts from removing or deleting objects from your bucket you must deny them the s3:DeleteObject,
        s3:DeleteObjectVersion and s3:PutLifeCycleConfiguration actions.

        The following operation is related to ``DeleteObject``

        *  PutObject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObject>`_

        **Request Syntax**
        ::

          response = client.delete_object(
              Bucket='string',
              Key='string',
              MFA='string',
              VersionId='string',
              RequestPayer='requester',
              BypassGovernanceRetention=True|False
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name of the bucket containing the object.

        :type Key: string
        :param Key: **[REQUIRED]**

          Key name of the object to delete.

        :type MFA: string
        :param MFA:

          The concatenation of the authentication device's serial number, a space, and the value that is
          displayed on your authentication device. Required to permanently delete a versionedobject if
          versioning is configured with MFA Deleteenabled.

        :type VersionId: string
        :param VersionId:

          VersionId used to reference a specific version of the object.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type BypassGovernanceRetention: boolean
        :param BypassGovernanceRetention:

          Indicates whether S3 Object Lock should bypass Governance-mode restrictions to process this
          operation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DeleteMarker': True|False,
                'VersionId': 'string',
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **DeleteMarker** *(boolean) --*

              Specifies whether the versioned object that was permanently deleted was (true) or was not
              (false) a delete marker.

            - **VersionId** *(string) --*

              Returns the version ID of the delete marker created as a result of the DELETE operation.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_object_tagging(
        self, Bucket: str, Key: str, VersionId: str = None
    ) -> ClientDeleteObjectTaggingResponseTypeDef:
        """
        Removes the entire tag set from the specified object. For more information about managing object
        tags, see `Object Tagging
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html#MultiFactorAuthenticationDelete>`__
        .

        To use this operation, you must have permission to perform the s3:DeleteObjectTagging action.

        To delete tags of a specific object version, add the versionId query parameter in the request. You
        will need permission for the s3:DeleteObjectVersionTagging action.

        The following operations are related to ``DeleteBucketMetricsConfiguration``

        *  PutObjectTagging

        *  GetObjectTagging

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObjectTagging>`_

        **Request Syntax**
        ::

          response = client.delete_object_tagging(
              Bucket='string',
              Key='string',
              VersionId='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket containing the objects from which to remove the tags.

        :type Key: string
        :param Key: **[REQUIRED]**

          Name of the tag.

        :type VersionId: string
        :param VersionId:

          The versionId of the object that the tag-set will be removed from.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VersionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **VersionId** *(string) --*

              The versionId of the object the tag-set was removed from.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_objects(
        self,
        Bucket: str,
        Delete: ClientDeleteObjectsDeleteTypeDef,
        MFA: str = None,
        RequestPayer: str = None,
        BypassGovernanceRetention: bool = None,
    ) -> ClientDeleteObjectsResponseTypeDef:
        """
        This operation enables you to delete multiple objects from a bucket using a single HTTP request. If
        you know the object keys that you want to delete, then this operation provides a suitable
        alternative to sending individual delete requests, reducing per-request overhead.

        The request contains a list of up to 1000 keys that you want to delete. In the XML, you provide the
        object key names, and optionally, version IDs if you want to delete a specific version of the
        object from a versioning-enabled bucket. For each key, Amazon S3 performs a delete operation and
        returns the result of that delete, success, or failure, in the response. Note that, if the object
        specified in the request is not found, Amazon S3 returns the result as deleted.

        The operation supports two modes for the response; verbose and quiet. By default, the operation
        uses verbose mode in which the response includes the result of deletion of each key in your
        request. In quiet mode the response includes only keys where the delete operation encountered an
        error. For a successful deletion, the operation does not return any information about the delete in
        the response body.

        When performing this operation on an MFA Delete enabled bucket, that attempts to delete any
        versioned objects, you must include an MFA token. If you do not provide one, the entire request
        will fail, even if there are non versioned objects you are attempting to delete. If you provide an
        invalid token, whether there are versioned keys in the request or not, the entire Multi-Object
        Delete request will fail. For information about MFA Delete, see `MFA Delete
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html#MultiFactorAuthenticationDelete>`__
        .

        Finally, the Content-MD5 header is required for all Multi-Object Delete requests. Amazon S3 uses
        the header value to ensure that your request body has not be altered in transit.

        The following operations are related to ``DeleteObjects``

        *  CreateMultipartUpload

        *  UploadPart

        *  CompleteMultipartUpload

        *  ListParts

        *  AbortMultipartUpload

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeleteObjects>`_

        **Request Syntax**
        ::

          response = client.delete_objects(
              Bucket='string',
              Delete={
                  'Objects': [
                      {
                          'Key': 'string',
                          'VersionId': 'string'
                      },
                  ],
                  'Quiet': True|False
              },
              MFA='string',
              RequestPayer='requester',
              BypassGovernanceRetention=True|False
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name containing the objects to delete.

        :type Delete: dict
        :param Delete: **[REQUIRED]**

          Container for the request.

          - **Objects** *(list) --* **[REQUIRED]**

            The objects to delete.

            - *(dict) --*

              Object Identifier is unique value to identify objects.

              - **Key** *(string) --* **[REQUIRED]**

                Key name of the object to delete.

              - **VersionId** *(string) --*

                VersionId for the specific version of the object to delete.

          - **Quiet** *(boolean) --*

            Element to enable quiet mode for the request. When you add this element, you must set its value
            to true.

        :type MFA: string
        :param MFA:

          The concatenation of the authentication device's serial number, a space, and the value that is
          displayed on your authentication device. Required to permanently delete a versioned object if
          versioning is configured with MFA Delete enabled.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type BypassGovernanceRetention: boolean
        :param BypassGovernanceRetention:

          Specifies whether you want to delete this object even if it has a Governance-type Object Lock in
          place. You must have sufficient permissions to perform this operation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Deleted': [
                    {
                        'Key': 'string',
                        'VersionId': 'string',
                        'DeleteMarker': True|False,
                        'DeleteMarkerVersionId': 'string'
                    },
                ],
                'RequestCharged': 'requester',
                'Errors': [
                    {
                        'Key': 'string',
                        'VersionId': 'string',
                        'Code': 'string',
                        'Message': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Deleted** *(list) --*

              Container element for a successful delete. It identifies the object that was successfully
              deleted.

              - *(dict) --*

                Information about the deleted object.

                - **Key** *(string) --*

                  The name of the deleted object.

                - **VersionId** *(string) --*

                  The version ID of the deleted object.

                - **DeleteMarker** *(boolean) --*

                  Specifies whether the versioned object that was permanently deleted was (true) or was not
                  (false) a delete marker. In a simple DELETE, this header indicates whether (true) or not
                  (false) a delete marker was created.

                - **DeleteMarkerVersionId** *(string) --*

                  The version ID of the delete marker created as a result of the DELETE operation. If you
                  delete a specific object version, the value returned by this header is the version ID of
                  the object version deleted.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

            - **Errors** *(list) --*

              Container for a failed delete operation that describes the object that Amazon S3 attempted to
              delete and the error it encountered.

              - *(dict) --*

                Container for all error elements.

                - **Key** *(string) --*

                  The error key.

                - **VersionId** *(string) --*

                  The version ID of the error.

                - **Code** *(string) --*

                  The error code is a string that uniquely identifies an error condition. It is meant to be
                  read and understood by programs that detect and handle errors by type.

                   **Amazon S3 error codes**

                  *

                    * *Code:* AccessDenied

                    * *Description:* Access Denied

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* AccountProblem

                    * *Description:* There is a problem with your AWS account that prevents the operation
                    from completing successfully. Contact AWS Support for further assistance.

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* AllAccessDisabled

                    * *Description:* All access to this Amazon S3 resource has been disabled. Contact AWS
                    Support for further assistance.

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* AmbiguousGrantByEmailAddress

                    * *Description:* The email address you provided is associated with more than one
                    account.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* AuthorizationHeaderMalformed

                    * *Description:* The authorization header you provided is invalid.

                    * *HTTP Status Code:* 400 Bad Request

                    * *HTTP Status Code:* N/A

                  *

                    * *Code:* BadDigest

                    * *Description:* The Content-MD5 you specified did not match what we received.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* BucketAlreadyExists

                    * *Description:* The requested bucket name is not available. The bucket namespace is
                    shared by all users of the system. Please select a different name and try again.

                    * *HTTP Status Code:* 409 Conflict

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* BucketAlreadyOwnedByYou

                    * *Description:* The bucket you tried to create already exists, and you own it. Amazon
                    S3 returns this error in all AWS Regions except in the North Virginia region. For
                    legacy compatibility, if you re-create an existing bucket that you already own in the
                    North Virginia region, Amazon S3 returns 200 OK and resets the bucket access control
                    lists (ACLs).

                    * *Code:* 409 Conflict (in all regions except the North Virginia region)

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* BucketNotEmpty

                    * *Description:* The bucket you tried to delete is not empty.

                    * *HTTP Status Code:* 409 Conflict

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* CredentialsNotSupported

                    * *Description:* This request does not support credentials.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* CrossLocationLoggingProhibited

                    * *Description:* Cross-location logging not allowed. Buckets in one geographic location
                    cannot log information to a bucket in another location.

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* EntityTooSmall

                    * *Description:* Your proposed upload is smaller than the minimum allowed object size.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* EntityTooLarge

                    * *Description:* Your proposed upload exceeds the maximum allowed object size.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* ExpiredToken

                    * *Description:* The provided token has expired.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* IllegalVersioningConfigurationException

                    * *Description:* Indicates that the versioning configuration specified in the request
                    is invalid.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* IncompleteBody

                    * *Description:* You did not provide the number of bytes specified by the
                    Content-Length HTTP header

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* IncorrectNumberOfFilesInPostRequest

                    * *Description:* POST requires exactly one file upload per request.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InlineDataTooLarge

                    * *Description:* Inline data exceeds the maximum allowed size.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InternalError

                    * *Description:* We encountered an internal error. Please try again.

                    * *HTTP Status Code:* 500 Internal Server Error

                    * *SOAP Fault Code Prefix:* Server

                  *

                    * *Code:* InvalidAccessKeyId

                    * *Description:* The AWS access key ID you provided does not exist in our records.

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidAddressingHeader

                    * *Description:* You must specify the Anonymous role.

                    * *HTTP Status Code:* N/A

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidArgument

                    * *Description:* Invalid Argument

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidBucketName

                    * *Description:* The specified bucket is not valid.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidBucketState

                    * *Description:* The request is not valid with the current state of the bucket.

                    * *HTTP Status Code:* 409 Conflict

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidDigest

                    * *Description:* The Content-MD5 you specified is not valid.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidEncryptionAlgorithmError

                    * *Description:* The encryption request you specified is not valid. The valid value is
                    AES256.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidLocationConstraint

                    * *Description:* The specified location constraint is not valid. For more information
                    about Regions, see `How to Select a Region for Your Buckets
                    <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#access-bucket-intro>`__
                    .

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidObjectState

                    * *Description:* The operation is not valid for the current state of the object.

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidPart

                    * *Description:* One or more of the specified parts could not be found. The part might
                    not have been uploaded, or the specified entity tag might not have matched the part's
                    entity tag.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidPartOrder

                    * *Description:* The list of parts was not in ascending order. Parts list must be
                    specified in order by part number.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidPayer

                    * *Description:* All access to this object has been disabled. Please contact AWS
                    Support for further assistance.

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidPolicyDocument

                    * *Description:* The content of the form does not meet the conditions specified in the
                    policy document.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidRange

                    * *Description:* The requested range cannot be satisfied.

                    * *HTTP Status Code:* 416 Requested Range Not Satisfiable

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidRequest

                    * *Description:* Please use AWS4-HMAC-SHA256.

                    * *HTTP Status Code:* 400 Bad Request

                    * *Code:* N/A

                  *

                    * *Code:* InvalidRequest

                    * *Description:* SOAP requests must be made over an HTTPS connection.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidRequest

                    * *Description:* Amazon S3 Transfer Acceleration is not supported for buckets with
                    non-DNS compliant names.

                    * *HTTP Status Code:* 400 Bad Request

                    * *Code:* N/A

                  *

                    * *Code:* InvalidRequest

                    * *Description:* Amazon S3 Transfer Acceleration is not supported for buckets with
                    periods (.) in their names.

                    * *HTTP Status Code:* 400 Bad Request

                    * *Code:* N/A

                  *

                    * *Code:* InvalidRequest

                    * *Description:* Amazon S3 Transfer Accelerate endpoint only supports virtual style
                    requests.

                    * *HTTP Status Code:* 400 Bad Request

                    * *Code:* N/A

                  *

                    * *Code:* InvalidRequest

                    * *Description:* Amazon S3 Transfer Accelerate is not configured on this bucket.

                    * *HTTP Status Code:* 400 Bad Request

                    * *Code:* N/A

                  *

                    * *Code:* InvalidRequest

                    * *Description:* Amazon S3 Transfer Accelerate is disabled on this bucket.

                    * *HTTP Status Code:* 400 Bad Request

                    * *Code:* N/A

                  *

                    * *Code:* InvalidRequest

                    * *Description:* Amazon S3 Transfer Acceleration is not supported on this bucket.
                    Contact AWS Support for more information.

                    * *HTTP Status Code:* 400 Bad Request

                    * *Code:* N/A

                  *

                    * *Code:* InvalidRequest

                    * *Description:* Amazon S3 Transfer Acceleration cannot be enabled on this bucket.
                    Contact AWS Support for more information.

                    * *HTTP Status Code:* 400 Bad Request

                    * *Code:* N/A

                  *

                    * *Code:* InvalidSecurity

                    * *Description:* The provided security credentials are not valid.

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidSOAPRequest

                    * *Description:* The SOAP request body is invalid.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidStorageClass

                    * *Description:* The storage class you specified is not valid.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidTargetBucketForLogging

                    * *Description:* The target bucket for logging does not exist, is not owned by you, or
                    does not have the appropriate grants for the log-delivery group.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidToken

                    * *Description:* The provided token is malformed or otherwise invalid.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* InvalidURI

                    * *Description:* Couldn't parse the specified URI.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* KeyTooLongError

                    * *Description:* Your key is too long.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MalformedACLError

                    * *Description:* The XML you provided was not well-formed or did not validate against
                    our published schema.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MalformedPOSTRequest

                    * *Description:* The body of your POST request is not well-formed multipart/form-data.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MalformedXML

                    * *Description:* This happens when the user sends malformed XML (XML that doesn't
                    conform to the published XSD) for the configuration. The error message is, "The XML you
                    provided was not well-formed or did not validate against our published schema."

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MaxMessageLengthExceeded

                    * *Description:* Your request was too big.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MaxPostPreDataLengthExceededError

                    * *Description:* Your POST request fields preceding the upload file were too large.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MetadataTooLarge

                    * *Description:* Your metadata headers exceed the maximum allowed metadata size.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MethodNotAllowed

                    * *Description:* The specified method is not allowed against this resource.

                    * *HTTP Status Code:* 405 Method Not Allowed

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MissingAttachment

                    * *Description:* A SOAP attachment was expected, but none were found.

                    * *HTTP Status Code:* N/A

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MissingContentLength

                    * *Description:* You must provide the Content-Length HTTP header.

                    * *HTTP Status Code:* 411 Length Required

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MissingRequestBodyError

                    * *Description:* This happens when the user sends an empty XML document as a request.
                    The error message is, "Request body is empty."

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MissingSecurityElement

                    * *Description:* The SOAP 1.1 request is missing a security element.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* MissingSecurityHeader

                    * *Description:* Your request is missing a required header.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* NoLoggingStatusForKey

                    * *Description:* There is no such thing as a logging status subresource for a key.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* NoSuchBucket

                    * *Description:* The specified bucket does not exist.

                    * *HTTP Status Code:* 404 Not Found

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* NoSuchBucketPolicy

                    * *Description:* The specified bucket does not have a bucket policy.

                    * *HTTP Status Code:* 404 Not Found

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* NoSuchKey

                    * *Description:* The specified key does not exist.

                    * *HTTP Status Code:* 404 Not Found

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* NoSuchLifecycleConfiguration

                    * *Description:* The lifecycle configuration does not exist.

                    * *HTTP Status Code:* 404 Not Found

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* NoSuchUpload

                    * *Description:* The specified multipart upload does not exist. The upload ID might be
                    invalid, or the multipart upload might have been aborted or completed.

                    * *HTTP Status Code:* 404 Not Found

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* NoSuchVersion

                    * *Description:* Indicates that the version ID specified in the request does not match
                    an existing version.

                    * *HTTP Status Code:* 404 Not Found

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* NotImplemented

                    * *Description:* A header you provided implies functionality that is not implemented.

                    * *HTTP Status Code:* 501 Not Implemented

                    * *SOAP Fault Code Prefix:* Server

                  *

                    * *Code:* NotSignedUp

                    * *Description:* Your account is not signed up for the Amazon S3 service. You must sign
                    up before you can use Amazon S3. You can sign up at the following URL:
                    https://aws.amazon.com/s3

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* OperationAborted

                    * *Description:* A conflicting conditional operation is currently in progress against
                    this resource. Try again.

                    * *HTTP Status Code:* 409 Conflict

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* PermanentRedirect

                    * *Description:* The bucket you are attempting to access must be addressed using the
                    specified endpoint. Send all future requests to this endpoint.

                    * *HTTP Status Code:* 301 Moved Permanently

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* PreconditionFailed

                    * *Description:* At least one of the preconditions you specified did not hold.

                    * *HTTP Status Code:* 412 Precondition Failed

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* Redirect

                    * *Description:* Temporary redirect.

                    * *HTTP Status Code:* 307 Moved Temporarily

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* RestoreAlreadyInProgress

                    * *Description:* Object restore is already in progress.

                    * *HTTP Status Code:* 409 Conflict

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* RequestIsNotMultiPartContent

                    * *Description:* Bucket POST must be of the enclosure-type multipart/form-data.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* RequestTimeout

                    * *Description:* Your socket connection to the server was not read from or written to
                    within the timeout period.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* RequestTimeTooSkewed

                    * *Description:* The difference between the request time and the server's time is too
                    large.

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* RequestTorrentOfBucketError

                    * *Description:* Requesting the torrent file of a bucket is not permitted.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* SignatureDoesNotMatch

                    * *Description:* The request signature we calculated does not match the signature you
                    provided. Check your AWS secret access key and signing method. For more information,
                    see `REST Authentication
                    <https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html>`__ and `SOAP
                    Authentication
                    <https://docs.aws.amazon.com/AmazonS3/latest/dev/SOAPAuthentication.html>`__ for
                    details.

                    * *HTTP Status Code:* 403 Forbidden

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* ServiceUnavailable

                    * *Description:* Reduce your request rate.

                    * *HTTP Status Code:* 503 Service Unavailable

                    * *SOAP Fault Code Prefix:* Server

                  *

                    * *Code:* SlowDown

                    * *Description:* Reduce your request rate.

                    * *HTTP Status Code:* 503 Slow Down

                    * *SOAP Fault Code Prefix:* Server

                  *

                    * *Code:* TemporaryRedirect

                    * *Description:* You are being redirected to the bucket while DNS updates.

                    * *HTTP Status Code:* 307 Moved Temporarily

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* TokenRefreshRequired

                    * *Description:* The provided token must be refreshed.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* TooManyBuckets

                    * *Description:* You have attempted to create more buckets than allowed.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* UnexpectedContent

                    * *Description:* This request does not support content.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* UnresolvableGrantByEmailAddress

                    * *Description:* The email address you provided does not match any account on record.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                  *

                    * *Code:* UserKeyMustBeSpecified

                    * *Description:* The bucket POST must contain the specified field name. If it is
                    specified, check the order of the fields.

                    * *HTTP Status Code:* 400 Bad Request

                    * *SOAP Fault Code Prefix:* Client

                - **Message** *(string) --*

                  The error message contains a generic description of the error condition in English. It is
                  intended for a human audience. Simple programs display the message directly to the end
                  user if they encounter an error condition they don't know how or don't care to handle.
                  Sophisticated programs with more exhaustive error handling and proper
                  internationalization are more likely to ignore the error message.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_public_access_block(self, Bucket: str) -> None:
        """
        Removes the PublicAccessBlock configuration for an Amazon S3 bucket. In order to use this
        operation, you must have the s3:PutBucketPublicAccessBlock permission. For more information about
        permissions, see `Permissions Related to Bucket Subresource Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        The following operations are related to ``DeleteBucketMetricsConfiguration`` :

        * `Using Amazon S3 Block Public Access
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html>`__

        *  GetPublicAccessBlock

        *  PutPublicAccessBlock

        *  GetBucketPolicyStatus

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/DeletePublicAccessBlock>`_

        **Request Syntax**
        ::

          response = client.delete_public_access_block(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The Amazon S3 bucket whose ``PublicAccessBlock`` configuration you want to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def download_file(
        self,
        Bucket: str,
        Key: str,
        Filename: str,
        ExtraArgs: Dict = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Download an S3 object to a file.

        Usage::

            import boto3
            s3 = boto3.resource('s3')
            s3.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')

        Similar behavior as S3Transfer's download_file() method,
        except that parameters are capitalized. Detailed examples can be found at
        :ref:`S3Transfer's Usage <ref_s3transfer_usage>`.

        :type Bucket: str
        :param Bucket: The name of the bucket to download from.

        :type Key: str
        :param Key: The name of the key to download from.

        :type Filename: str
        :param Filename: The path to the file to download to.

        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.

        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the download.

        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            transfer.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def download_fileobj(
        self,
        Bucket: str,
        Key: str,
        Fileobj: IO[Any],
        ExtraArgs: Dict = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Download an object from S3 to a file-like object.

        The file-like object must be in binary mode.

        This is a managed transfer which will perform a multipart download in
        multiple threads if necessary.

        Usage::

            import boto3
            s3 = boto3.client('s3')

            with open('filename', 'wb') as data:
                s3.download_fileobj('mybucket', 'mykey', data)

        :type Fileobj: a file-like object
        :param Fileobj: A file-like object to download into. At a minimum, it must
            implement the `write` method and must accept bytes.

        :type Bucket: str
        :param Bucket: The name of the bucket to download from.

        :type Key: str
        :param Key: The name of the key to download from.

        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.

        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the download.

        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            download.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_post(
        self,
        Bucket: str,
        Key: str,
        Fields: Dict = None,
        Conditions: List[Any] = None,
        ExpiresIn: int = 3600,
    ) -> Dict[str, Any]:
        """
        Builds the url and the form fields used for a presigned s3 post

        :type Bucket: string
        :param Bucket: The name of the bucket to presign the post to. Note that
            bucket related conditions should not be included in the
            ``conditions`` parameter.

        :type Key: string
        :param Key: Key name, optionally add ${filename} to the end to
            attach the submitted filename. Note that key related conditions and
            fields are filled out for you and should not be included in the
            ``Fields`` or ``Conditions`` parameter.

        :type Fields: dict
        :param Fields: A dictionary of prefilled form fields to build on top
            of. Elements that may be included are acl, Cache-Control,
            Content-Type, Content-Disposition, Content-Encoding, Expires,
            success_action_redirect, redirect, success_action_status,
            and x-amz-meta-.

            Note that if a particular element is included in the fields
            dictionary it will not be automatically added to the conditions
            list. You must specify a condition for the element as well.

        :type Conditions: list
        :param Conditions: A list of conditions to include in the policy. Each
            element can be either a list or a structure. For example:

            [
             {"acl": "public-read"},
             ["content-length-range", 2, 5],
             ["starts-with", "$success_action_redirect", ""]
            ]

            Conditions that are included may pertain to acl,
            content-length-range, Cache-Control, Content-Type,
            Content-Disposition, Content-Encoding, Expires,
            success_action_redirect, redirect, success_action_status,
            and/or x-amz-meta-.

            Note that if you include a condition, you must specify
            the a valid value in the fields dictionary as well. A value will
            not be added automatically to the fields dictionary based on the
            conditions.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned post
            is valid for.

        :rtype: dict
        :returns: A dictionary with two elements: ``url`` and ``fields``.
            Url is the url to post to. Fields is a dictionary filled with
            the form fields and respective values to use when submitting the
            post. For example:

            {'url': 'https://mybucket.s3.amazonaws.com
             'fields': {'acl': 'public-read',
                        'key': 'mykey',
                        'signature': 'mysignature',
                        'policy': 'mybase64 encoded policy'}
            }
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_accelerate_configuration(
        self, Bucket: str
    ) -> ClientGetBucketAccelerateConfigurationResponseTypeDef:
        """
        This implementation of the GET operation uses the ``accelerate`` subresource to return the Transfer
        Acceleration state of a bucket, which is either ``Enabled`` or ``Suspended`` . Amazon S3 Transfer
        Acceleration is a bucket-level feature that enables you to perform faster data transfers to and
        from Amazon S3.

        To use this operation, you must have permission to perform the ``s3:GetAccelerateConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//s3-access-control.html>`__ in the Amazon Simple
        Storage Service Developer Guide.

        You set the Transfer Acceleration state of an existing bucket to ``Enabled`` or ``Suspended`` by
        using the  PutBucketAccelerateConfiguration operation.

        A GET ``accelerate`` request does not return a state value for a bucket that has no transfer
        acceleration state. A bucket has no Transfer Acceleration state, if a state has never been set on
        the bucket.

        For more information on transfer acceleration, see `Transfer Acceleration
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//transfer-acceleration.html>`__ in the Amazon
        Simple Storage Service Developer Guide.

         **Related Resources**

        *  PutBucketAccelerateConfiguration

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketAccelerateConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_bucket_accelerate_configuration(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket for which the accelerate configuration is retrieved.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Status': 'Enabled'|'Suspended'
            }
          **Response Structure**

          - *(dict) --*

            - **Status** *(string) --*

              The accelerate configuration of the bucket.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_acl(self, Bucket: str) -> ClientGetBucketAclResponseTypeDef:
        """
        This implementation of the ``GET`` operation uses the ``acl`` subresource to return the access
        control list (ACL) of a bucket. To use ``GET`` to return the ACL of the bucket, you must have
        ``READ_ACP`` access to the bucket. If ``READ_ACP`` permission is granted to the anonymous user, you
        can return the ACL of the bucket without using an authorization header.

         **Related Resources**

        *

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketAcl>`_

        **Request Syntax**
        ::

          response = client.get_bucket_acl(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Specifies the S3 bucket whose ACL is being requested.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                },
                'Grants': [
                    {
                        'Grantee': {
                            'DisplayName': 'string',
                            'EmailAddress': 'string',
                            'ID': 'string',
                            'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                            'URI': 'string'
                        },
                        'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Owner** *(dict) --*

              Container for the bucket owner's display name and ID.

              - **DisplayName** *(string) --*

                Container for the display name of the owner

              - **ID** *(string) --*

                Container for the ID of the owner

            - **Grants** *(list) --*

              A list of grants.

              - *(dict) --*

                Container for grant information.

                - **Grantee** *(dict) --*

                  The person being granted permissions.

                  - **DisplayName** *(string) --*

                    Screen name of the grantee.

                  - **EmailAddress** *(string) --*

                    Email address of the grantee.

                  - **ID** *(string) --*

                    The canonical user ID of the grantee.

                  - **Type** *(string) --*

                    Type of grantee

                  - **URI** *(string) --*

                    URI of the grantee group.

                - **Permission** *(string) --*

                  Specifies the permission given to the grantee.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_analytics_configuration(
        self, Bucket: str, Id: str
    ) -> ClientGetBucketAnalyticsConfigurationResponseTypeDef:
        """
        This implementation of the GET operation returns an analytics configuration (identified by the
        analytics configuration ID) from the bucket.

        To use this operation, you must have permissions to perform the ``s3:GetAnalyticsConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the *Amazon Simple
        Storage Service Developer Guide* .

        For information about Amazon S3 analytics feature, see `Amazon S3 Analytics – Storage Class
        Analysis <https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html>`__ in the
        *Amazon Simple Storage Service Developer Guide* .

         **Related Resources**

        *

        *

        *

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketAnalyticsConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_bucket_analytics_configuration(
              Bucket='string',
              Id='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket from which an analytics configuration is retrieved.

        :type Id: string
        :param Id: **[REQUIRED]**

          The ID that identifies the analytics configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AnalyticsConfiguration': {
                    'Id': 'string',
                    'Filter': {
                        'Prefix': 'string',
                        'Tag': {
                            'Key': 'string',
                            'Value': 'string'
                        },
                        'And': {
                            'Prefix': 'string',
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        }
                    },
                    'StorageClassAnalysis': {
                        'DataExport': {
                            'OutputSchemaVersion': 'V_1',
                            'Destination': {
                                'S3BucketDestination': {
                                    'Format': 'CSV',
                                    'BucketAccountId': 'string',
                                    'Bucket': 'string',
                                    'Prefix': 'string'
                                }
                            }
                        }
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **AnalyticsConfiguration** *(dict) --*

              The configuration and any analyses for the analytics filter.

              - **Id** *(string) --*

                The ID that identifies the analytics configuration.

              - **Filter** *(dict) --*

                The filter used to describe a set of objects for analyses. A filter must have exactly one
                prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all
                objects will be considered in any analysis.

                - **Prefix** *(string) --*

                  The prefix to use when evaluating an analytics filter.

                - **Tag** *(dict) --*

                  The tag to use when evaluating an analytics filter.

                  - **Key** *(string) --*

                    Name of the tag.

                  - **Value** *(string) --*

                    Value of the tag.

                - **And** *(dict) --*

                  A conjunction (logical AND) of predicates, which is used in evaluating an analytics
                  filter. The operator must have at least two predicates.

                  - **Prefix** *(string) --*

                    The prefix to use when evaluating an AND predicate: The prefix that an object must have
                    to be included in the metrics results.

                  - **Tags** *(list) --*

                    The list of tags to use when evaluating an AND predicate.

                    - *(dict) --*

                      A container of a key value name pair.

                      - **Key** *(string) --*

                        Name of the tag.

                      - **Value** *(string) --*

                        Value of the tag.

              - **StorageClassAnalysis** *(dict) --*

                Contains data related to access patterns to be collected and made available to analyze the
                tradeoffs between different storage classes.

                - **DataExport** *(dict) --*

                  Specifies how data related to the storage class analysis for an Amazon S3 bucket should
                  be exported.

                  - **OutputSchemaVersion** *(string) --*

                    The version of the output schema to use when exporting data. Must be ``V_1`` .

                  - **Destination** *(dict) --*

                    The place to store the data for an analysis.

                    - **S3BucketDestination** *(dict) --*

                      A destination signifying output to an S3 bucket.

                      - **Format** *(string) --*

                        Specifies the file format used when exporting data to Amazon S3.

                      - **BucketAccountId** *(string) --*

                        The account ID that owns the destination bucket. If no account ID is provided, the
                        owner will not be validated prior to exporting data.

                      - **Bucket** *(string) --*

                        The Amazon Resource Name (ARN) of the bucket to which data is exported.

                      - **Prefix** *(string) --*

                        The prefix to use when exporting data. The prefix is prepended to all results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_cors(self, Bucket: str) -> ClientGetBucketCorsResponseTypeDef:
        """
        Returns the cors configuration information set for the bucket.

        To use this operation, you must have permission to perform the s3:GetBucketCORS action. By default,
        the bucket owner has this permission and can grant it to others.

        To learn more cors, see `Enabling Cross-Origin Resource Sharing
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html>`__ Enabling Cross-Origin Resource
        Sharing.

        The following operations are related to ``GetBucketCors`` :

        *  PutBucketCors

        *  DeleteBucketCors

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketCors>`_

        **Request Syntax**
        ::

          response = client.get_bucket_cors(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name for which to get the cors configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CORSRules': [
                    {
                        'AllowedHeaders': [
                            'string',
                        ],
                        'AllowedMethods': [
                            'string',
                        ],
                        'AllowedOrigins': [
                            'string',
                        ],
                        'ExposeHeaders': [
                            'string',
                        ],
                        'MaxAgeSeconds': 123
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **CORSRules** *(list) --*

              A set of origins and methods (cross-origin access that you want to allow). You can add up to
              100 rules to the configuration.

              - *(dict) --*

                Specifies a cross-origin access rule for an Amazon S3 bucket.

                - **AllowedHeaders** *(list) --*

                  Headers that are specified in the ``Access-Control-Request-Headers`` header. These
                  headers are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS
                  request, Amazon S3 returns any requested headers that are allowed.

                  - *(string) --*

                - **AllowedMethods** *(list) --*

                  An HTTP method that you allow the origin to execute. Valid values are ``GET`` , ``PUT`` ,
                  ``HEAD`` , ``POST`` , and ``DELETE`` .

                  - *(string) --*

                - **AllowedOrigins** *(list) --*

                  One or more origins you want customers to be able to access the bucket from.

                  - *(string) --*

                - **ExposeHeaders** *(list) --*

                  One or more headers in the response that you want customers to be able to access from
                  their applications (for example, from a JavaScript ``XMLHttpRequest`` object).

                  - *(string) --*

                - **MaxAgeSeconds** *(integer) --*

                  The time in seconds that your browser is to cache the preflight response for the
                  specified resource.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_encryption(
        self, Bucket: str
    ) -> ClientGetBucketEncryptionResponseTypeDef:
        """
        Returns the default encryption configuration for an Amazon S3 bucket. For information about the
        Amazon S3 default encryption feature, see `Amazon S3 Default Bucket Encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html>`__ .

        To use this operation, you must have permission to perform the ``s3:GetEncryptionConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        The following operations are related to ``GetBucketEncryption`` :

        *  PutBucketEncryption

        *  DeleteBucketEncryption

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketEncryption>`_

        **Request Syntax**
        ::

          response = client.get_bucket_encryption(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket from which the server-side encryption configuration is retrieved.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ServerSideEncryptionConfiguration': {
                    'Rules': [
                        {
                            'ApplyServerSideEncryptionByDefault': {
                                'SSEAlgorithm': 'AES256'|'aws:kms',
                                'KMSMasterKeyID': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ServerSideEncryptionConfiguration** *(dict) --*

              Specifies the default server-side-encryption configuration.

              - **Rules** *(list) --*

                Container for information about a particular server-side encryption configuration rule.

                - *(dict) --*

                  Specifies the default server-side encryption configuration.

                  - **ApplyServerSideEncryptionByDefault** *(dict) --*

                    Specifies the default server-side encryption to apply to new objects in the bucket. If
                    a PUT Object request doesn't specify any server-side encryption, this default
                    encryption will be applied.

                    - **SSEAlgorithm** *(string) --*

                      Server-side encryption algorithm to use for the default encryption.

                    - **KMSMasterKeyID** *(string) --*

                      KMS master key ID to use for the default encryption. This parameter is allowed if and
                      only if ``SSEAlgorithm`` is set to ``aws:kms`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_inventory_configuration(
        self, Bucket: str, Id: str
    ) -> ClientGetBucketInventoryConfigurationResponseTypeDef:
        """
        Returns an inventory configuration (identified by the inventory configuration ID) from the bucket.

        To use this operation, you must have permissions to perform the ``s3:GetInventoryConfiguration``
        action. The bucket owner has this permission by default and can grant this permission to others.
        For more information about permissions, see `Permissions Related to Bucket Subresource Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        For information about the Amazon S3 inventory feature, see `Amazon S3 Inventory
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html>`__ .

        The following operations are related to ``GetBucketInventoryConfiguration`` :

        *  DeleteBucketInventoryConfiguration

        *  ListBucketInventoryConfigurations

        *  PutBucketInventoryConfiguration

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketInventoryConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_bucket_inventory_configuration(
              Bucket='string',
              Id='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the inventory configuration to retrieve.

        :type Id: string
        :param Id: **[REQUIRED]**

          The ID used to identify the inventory configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'InventoryConfiguration': {
                    'Destination': {
                        'S3BucketDestination': {
                            'AccountId': 'string',
                            'Bucket': 'string',
                            'Format': 'CSV'|'ORC'|'Parquet',
                            'Prefix': 'string',
                            'Encryption': {
                                'SSES3': {},
                                'SSEKMS': {
                                    'KeyId': 'string'
                                }
                            }
                        }
                    },
                    'IsEnabled': True|False,
                    'Filter': {
                        'Prefix': 'string'
                    },
                    'Id': 'string',
                    'IncludedObjectVersions': 'All'|'Current',
                    'OptionalFields': [
                        'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'
                        |'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'
                        |'ObjectLockMode'|'ObjectLockLegalHoldStatus'|'IntelligentTieringAccessTier',
                    ],
                    'Schedule': {
                        'Frequency': 'Daily'|'Weekly'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **InventoryConfiguration** *(dict) --*

              Specifies the inventory configuration.

              - **Destination** *(dict) --*

                Contains information about where to publish the inventory results.

                - **S3BucketDestination** *(dict) --*

                  Contains the bucket name, file format, bucket owner (optional), and prefix (optional)
                  where inventory results are published.

                  - **AccountId** *(string) --*

                    The ID of the account that owns the destination bucket.

                  - **Bucket** *(string) --*

                    The Amazon resource name (ARN) of the bucket where inventory results will be published.

                  - **Format** *(string) --*

                    Specifies the output format of the inventory results.

                  - **Prefix** *(string) --*

                    The prefix that is prepended to all inventory results.

                  - **Encryption** *(dict) --*

                    Contains the type of server-side encryption used to encrypt the inventory results.

                    - **SSES3** *(dict) --*

                      Specifies the use of SSE-S3 to encrypt delivered Inventory reports.

                    - **SSEKMS** *(dict) --*

                      Specifies the use of SSE-KMS to encrypt delivered Inventory reports.

                      - **KeyId** *(string) --*

                        Specifies the ID of the AWS Key Management Service (KMS) customer master key (CMK)
                        to use for encrypting Inventory reports.

              - **IsEnabled** *(boolean) --*

                Specifies whether the inventory is enabled or disabled. If set to ``True`` , an inventory
                list is generated. If set to ``False`` , no inventory list is generated.

              - **Filter** *(dict) --*

                Specifies an inventory filter. The inventory only includes objects that meet the filter's
                criteria.

                - **Prefix** *(string) --*

                  The prefix that an object must have to be included in the inventory results.

              - **Id** *(string) --*

                The ID used to identify the inventory configuration.

              - **IncludedObjectVersions** *(string) --*

                Object versions to include in the inventory list. If set to ``All`` , the list includes all
                the object versions, which adds the version-related fields ``VersionId`` , ``IsLatest`` ,
                and ``DeleteMarker`` to the list. If set to ``Current`` , the list does not contain these
                version-related fields.

              - **OptionalFields** *(list) --*

                Contains the optional fields that are included in the inventory results.

                - *(string) --*

              - **Schedule** *(dict) --*

                Specifies the schedule for generating inventory results.

                - **Frequency** *(string) --*

                  Specifies how frequently inventory results are produced.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_lifecycle(
        self, Bucket: str
    ) -> ClientGetBucketLifecycleResponseTypeDef:
        """
        .. warning::

          For an updated version of this API, see  GetBucketLifecycleConfiguration . If you configured a
          bucket lifecycle using the ``filter`` element, you should the updated version of this topic. This
          topic is provided for backward compatibility.

        Returns the lifecycle configuration information set on the bucket. For information about lifecycle
        configuration, see `Object Lifecycle Management
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html>`__ .

        To use this operation, you must have permission to perform the ``s3:GetLifecycleConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

         ``GetBucketLifecycle`` has the following special error:

        * Error code: ``NoSuchLifecycleConfiguration``

          * Description: The lifecycle configuration does not exist.

          * HTTP Status Code: 404 Not Found

          * SOAP Fault Code Prefix: Client

        The following operations are related to ``GetBucketLifecycle`` :

        *  GetBucketLifecycleConfiguration

        *  PutBucketLifecycle

        *  DeleteBucketLifecycle

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not be
            used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketLifecycle>`_

        **Request Syntax**
        ::

          response = client.get_bucket_lifecycle(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket for which to the the lifecycle information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Rules': [
                    {
                        'Expiration': {
                            'Date': datetime(2015, 1, 1),
                            'Days': 123,
                            'ExpiredObjectDeleteMarker': True|False
                        },
                        'ID': 'string',
                        'Prefix': 'string',
                        'Status': 'Enabled'|'Disabled',
                        'Transition': {
                            'Date': datetime(2015, 1, 1),
                            'Days': 123,
                            'StorageClass':
                            'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                        },
                        'NoncurrentVersionTransition': {
                            'NoncurrentDays': 123,
                            'StorageClass':
                            'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                        },
                        'NoncurrentVersionExpiration': {
                            'NoncurrentDays': 123
                        },
                        'AbortIncompleteMultipartUpload': {
                            'DaysAfterInitiation': 123
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Rules** *(list) --*

              Container for a lifecycle rule.

              - *(dict) --*

                Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket
                lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__
                in the *Amazon Simple Storage Service API Reference* .

                - **Expiration** *(dict) --*

                  Specifies the expiration for the lifecycle of the object.

                  - **Date** *(datetime) --*

                    Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
                    Format.

                  - **Days** *(integer) --*

                    Indicates the lifetime, in days, of the objects that are subject to the rule. The value
                    must be a non-zero positive integer.

                  - **ExpiredObjectDeleteMarker** *(boolean) --*

                    Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If
                    set to true, the delete marker will be expired; if set to false the policy takes no
                    action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.

                - **ID** *(string) --*

                  Unique identifier for the rule. The value can't be longer than 255 characters.

                - **Prefix** *(string) --*

                  Object key prefix that identifies one or more objects to which this rule applies.

                - **Status** *(string) --*

                  If ``Enabled`` , the rule is currently being applied. If ``Disabled`` , the rule is not
                  currently being applied.

                - **Transition** *(dict) --*

                  Specifies when an object transitions to a specified storage class.

                  - **Date** *(datetime) --*

                    Indicates when objects are transitioned to the specified storage class. The date value
                    must be in ISO 8601 format. The time is always midnight UTC.

                  - **Days** *(integer) --*

                    Indicates the number of days after creation when objects are transitioned to the
                    specified storage class. The value must be a positive integer.

                  - **StorageClass** *(string) --*

                    The storage class to which you want the object to transition.

                - **NoncurrentVersionTransition** *(dict) --*

                  Container for the transition rule that describes when noncurrent objects transition to
                  the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` , ``GLACIER`` , or
                  ``DEEP_ARCHIVE`` storage class. If your bucket is versioning-enabled (or versioning is
                  suspended), you can set this action to request that Amazon S3 transition noncurrent
                  object versions to the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` ,
                  ``GLACIER`` , or ``DEEP_ARCHIVE`` storage class at a specific period in the object's
                  lifetime.

                  - **NoncurrentDays** *(integer) --*

                    Specifies the number of days an object is noncurrent before Amazon S3 can perform the
                    associated action. For information about the noncurrent days calculations, see `How
                    Amazon S3 Calculates When an Object Became Noncurrent
                    <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the
                    *Amazon Simple Storage Service Developer Guide* .

                  - **StorageClass** *(string) --*

                    The class of storage used to store the object.

                - **NoncurrentVersionExpiration** *(dict) --*

                  Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently
                  deletes the noncurrent object versions. You set this lifecycle configuration action on a
                  bucket that has versioning enabled (or suspended) to request that Amazon S3 delete
                  noncurrent object versions at a specific period in the object's lifetime.

                  - **NoncurrentDays** *(integer) --*

                    Specifies the number of days an object is noncurrent before Amazon S3 can perform the
                    associated action. For information about the noncurrent days calculations, see `How
                    Amazon S3 Calculates When an Object Became Noncurrent
                    <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__
                    in the Amazon Simple Storage Service Developer Guide.

                - **AbortIncompleteMultipartUpload** *(dict) --*

                  Specifies the days since the initiation of an incomplete multipart upload that Amazon S3
                  will wait before permanently removing all parts of the upload. For more information, see
                  `Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
                  in the *Amazon Simple Storage Service Developer Guide* .

                  - **DaysAfterInitiation** *(integer) --*

                    Specifies the number of days after which Amazon S3 aborts an incomplete multipart
                    upload.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_lifecycle_configuration(
        self, Bucket: str
    ) -> ClientGetBucketLifecycleConfigurationResponseTypeDef:
        """
        .. note::

          Bucket lifecycle configuration now supports specifying a lifecycle rule using an object key name
          prefix, one or more object tags, or a combination of both. Accordingly, this section describes
          the latest API. The response describes the new filter element that you can use to specify a
          filter to select a subset of objects to which the rule applies. If you are still using previous
          version of the lifecycle configuration, it works. For the earlier API description, see
          GetBucketLifecycle .

        Returns the lifecycle configuration information set on the bucket. For information about lifecycle
        configuration, see `Object Lifecycle Management
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html>`__ .

        To use this operation, you must have permission to perform the ``s3:GetLifecycleConfiguration``
        action. The bucket owner has this permission, by default. The bucket owner can grant this
        permission to others. For more information about permissions, see `Permissions Related to Bucket
        Subresource Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

         ``GetBucketLifecycleConfiguration`` has the following special error:

        * Error code: ``NoSuchLifecycleConfiguration``

          * Description: The lifecycle configuration does not exist.

          * HTTP Status Code: 404 Not Found

          * SOAP Fault Code Prefix: Client

        The following operations are related to ``DeleteBucketMetricsConfiguration`` :

        *  GetBucketLifecycle

        *  PutBucketLifecycle

        *  DeleteBucketLifecycle

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketLifecycleConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_bucket_lifecycle_configuration(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket for which to the the lifecycle information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Rules': [
                    {
                        'Expiration': {
                            'Date': datetime(2015, 1, 1),
                            'Days': 123,
                            'ExpiredObjectDeleteMarker': True|False
                        },
                        'ID': 'string',
                        'Prefix': 'string',
                        'Filter': {
                            'Prefix': 'string',
                            'Tag': {
                                'Key': 'string',
                                'Value': 'string'
                            },
                            'And': {
                                'Prefix': 'string',
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        },
                        'Status': 'Enabled'|'Disabled',
                        'Transitions': [
                            {
                                'Date': datetime(2015, 1, 1),
                                'Days': 123,
                                'StorageClass':
                                'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                            },
                        ],
                        'NoncurrentVersionTransitions': [
                            {
                                'NoncurrentDays': 123,
                                'StorageClass':
                                'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                            },
                        ],
                        'NoncurrentVersionExpiration': {
                            'NoncurrentDays': 123
                        },
                        'AbortIncompleteMultipartUpload': {
                            'DaysAfterInitiation': 123
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Rules** *(list) --*

              Container for a lifecycle rule.

              - *(dict) --*

                A lifecycle rule for individual objects in an Amazon S3 bucket.

                - **Expiration** *(dict) --*

                  Specifies the expiration for the lifecycle of the object in the form of date, days and,
                  whether the object has a delete marker.

                  - **Date** *(datetime) --*

                    Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
                    Format.

                  - **Days** *(integer) --*

                    Indicates the lifetime, in days, of the objects that are subject to the rule. The value
                    must be a non-zero positive integer.

                  - **ExpiredObjectDeleteMarker** *(boolean) --*

                    Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If
                    set to true, the delete marker will be expired; if set to false the policy takes no
                    action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.

                - **ID** *(string) --*

                  Unique identifier for the rule. The value cannot be longer than 255 characters.

                - **Prefix** *(string) --*

                  Prefix identifying one or more objects to which the rule applies. This is No longer used;
                  use Filter instead.

                - **Filter** *(dict) --*

                  The Filter is used to identify objects that a Lifecycle Rule applies to. A Filter must
                  have exactly one of Prefix, Tag, or And specified.

                  - **Prefix** *(string) --*

                    Prefix identifying one or more objects to which the rule applies.

                  - **Tag** *(dict) --*

                    This tag must exist in the object's tag set in order for the rule to apply.

                    - **Key** *(string) --*

                      Name of the tag.

                    - **Value** *(string) --*

                      Value of the tag.

                  - **And** *(dict) --*

                    This is used in a Lifecycle Rule Filter to apply a logical AND to two or more
                    predicates. The Lifecycle Rule will apply to any object matching all of the predicates
                    configured inside the And operator.

                    - **Prefix** *(string) --*

                      Prefix identifying one or more objects to which the rule applies.

                    - **Tags** *(list) --*

                      All of these tags must exist in the object's tag set in order for the rule to apply.

                      - *(dict) --*

                        A container of a key value name pair.

                        - **Key** *(string) --*

                          Name of the tag.

                        - **Value** *(string) --*

                          Value of the tag.

                - **Status** *(string) --*

                  If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not
                  currently being applied.

                - **Transitions** *(list) --*

                  Specifies when an Amazon S3 object transitions to a specified storage class.

                  - *(dict) --*

                    Specifies when an object transitions to a specified storage class.

                    - **Date** *(datetime) --*

                      Indicates when objects are transitioned to the specified storage class. The date
                      value must be in ISO 8601 format. The time is always midnight UTC.

                    - **Days** *(integer) --*

                      Indicates the number of days after creation when objects are transitioned to the
                      specified storage class. The value must be a positive integer.

                    - **StorageClass** *(string) --*

                      The storage class to which you want the object to transition.

                - **NoncurrentVersionTransitions** *(list) --*

                  Specifies the transition rule for the lifecycle rule that describes when noncurrent
                  objects transition to the a specific storage class. If your bucket is versioning-enabled
                  (or versioning is suspended), you can set this action to request that Amazon S3
                  transition noncurrent object versions to the a specifc storage class at a set period in
                  the object's lifetime.

                  - *(dict) --*

                    Container for the transition rule that describes when noncurrent objects transition to
                    the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` , ``GLACIER`` , or
                    ``DEEP_ARCHIVE`` storage class. If your bucket is versioning-enabled (or versioning is
                    suspended), you can set this action to request that Amazon S3 transition noncurrent
                    object versions to the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` ,
                    ``GLACIER`` , or ``DEEP_ARCHIVE`` storage class at a specific period in the object's
                    lifetime.

                    - **NoncurrentDays** *(integer) --*

                      Specifies the number of days an object is noncurrent before Amazon S3 can perform the
                      associated action. For information about the noncurrent days calculations, see `How
                      Amazon S3 Calculates When an Object Became Noncurrent
                      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the
                      *Amazon Simple Storage Service Developer Guide* .

                    - **StorageClass** *(string) --*

                      The class of storage used to store the object.

                - **NoncurrentVersionExpiration** *(dict) --*

                  Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently
                  deletes the noncurrent object versions. You set this lifecycle configuration action on a
                  bucket that has versioning enabled (or suspended) to request that Amazon S3 delete
                  noncurrent object versions at a specific period in the object's lifetime.

                  - **NoncurrentDays** *(integer) --*

                    Specifies the number of days an object is noncurrent before Amazon S3 can perform the
                    associated action. For information about the noncurrent days calculations, see `How
                    Amazon S3 Calculates When an Object Became Noncurrent
                    <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__
                    in the Amazon Simple Storage Service Developer Guide.

                - **AbortIncompleteMultipartUpload** *(dict) --*

                  Specifies the days since the initiation of an incomplete multipart upload that Amazon S3
                  will wait before permanently removing all parts of the upload. For more information, see
                  `Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
                  in the *Amazon Simple Storage Service Developer Guide* .

                  - **DaysAfterInitiation** *(integer) --*

                    Specifies the number of days after which Amazon S3 aborts an incomplete multipart
                    upload.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_location(
        self, Bucket: str
    ) -> ClientGetBucketLocationResponseTypeDef:
        """
        Returns the region the bucket resides in. You set the bucket's region using the
        ``LocationConstraint`` request parameter in a ``CreateBucket`` request. For more information, see
        CreateBucket .

        To use this implementation of the operation, you must be the bucket owner.

        The following operations are related to ``GetBucketLocation`` :

        *  GetObject

        *  CreateBucket

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketLocation>`_

        **Request Syntax**
        ::

          response = client.get_bucket_location(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket for which to get the location.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LocationConstraint':
                'EU'|'eu-west-1'|'us-west-1'|'us-west-2'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'
                |'ap-northeast-1'|'sa-east-1'|'cn-north-1'|'eu-central-1'
            }
          **Response Structure**

          - *(dict) --*

            - **LocationConstraint** *(string) --*

              Specifies the region where the bucket resides. For a list of all the Amazon S3 supported
              location constraints by region, see `Regions and Endpoints
              <https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_logging(self, Bucket: str) -> ClientGetBucketLoggingResponseTypeDef:
        """
        Returns the logging status of a bucket and the permissions users have to view and modify that
        status. To use GET, you must be the bucket owner.

        The following operations are related to ``GetBucketLogging`` :

        *  CreateBucket

        *  PutBucketLogging

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketLogging>`_

        **Request Syntax**
        ::

          response = client.get_bucket_logging(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name for which to get the logging information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LoggingEnabled': {
                    'TargetBucket': 'string',
                    'TargetGrants': [
                        {
                            'Grantee': {
                                'DisplayName': 'string',
                                'EmailAddress': 'string',
                                'ID': 'string',
                                'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                                'URI': 'string'
                            },
                            'Permission': 'FULL_CONTROL'|'READ'|'WRITE'
                        },
                    ],
                    'TargetPrefix': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **LoggingEnabled** *(dict) --*

              Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys
              for a bucket. For more information, see `PUT Bucket logging
              <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html>`__ in the *Amazon
              Simple Storage Service API Reference* .

              - **TargetBucket** *(string) --*

                Specifies the bucket where you want Amazon S3 to store server access logs. You can have
                your logs delivered to any bucket that you own, including the same bucket that is being
                logged. You can also configure multiple buckets to deliver their logs to the same target
                bucket. In this case you should choose a different TargetPrefix for each source bucket so
                that the delivered log files can be distinguished by key.

              - **TargetGrants** *(list) --*

                Container for granting information.

                - *(dict) --*

                  Container for granting information.

                  - **Grantee** *(dict) --*

                    Container for the person being granted permissions.

                    - **DisplayName** *(string) --*

                      Screen name of the grantee.

                    - **EmailAddress** *(string) --*

                      Email address of the grantee.

                    - **ID** *(string) --*

                      The canonical user ID of the grantee.

                    - **Type** *(string) --*

                      Type of grantee

                    - **URI** *(string) --*

                      URI of the grantee group.

                  - **Permission** *(string) --*

                    Logging permissions assigned to the Grantee for the bucket.

              - **TargetPrefix** *(string) --*

                A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in
                a single bucket, you can use a prefix to distinguish which log files came from which bucket.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_metrics_configuration(
        self, Bucket: str, Id: str
    ) -> ClientGetBucketMetricsConfigurationResponseTypeDef:
        """
        Gets a metrics configuration (specified by the metrics configuration ID) from the bucket. Note that
        this doesn't include the daily storage metrics.

        To use this operation, you must have permissions to perform the ``s3:GetMetricsConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        For information about CloudWatch request metrics for Amazon S3, see `Monitoring Metrics with Amazon
        CloudWatch <https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html>`__ .

        The following operations are related to ``GetBucketMetricsConfiguration`` :

        *  PutBucketMetricsConfiguration

        *  DeleteBucketMetricsConfiguration

        *  ListBucketMetricsConfigurations

        * `Monitoring Metrics with Amazon CloudWatch
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html>`__

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketMetricsConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_bucket_metrics_configuration(
              Bucket='string',
              Id='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the metrics configuration to retrieve.

        :type Id: string
        :param Id: **[REQUIRED]**

          The ID used to identify the metrics configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MetricsConfiguration': {
                    'Id': 'string',
                    'Filter': {
                        'Prefix': 'string',
                        'Tag': {
                            'Key': 'string',
                            'Value': 'string'
                        },
                        'And': {
                            'Prefix': 'string',
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        }
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **MetricsConfiguration** *(dict) --*

              Specifies the metrics configuration.

              - **Id** *(string) --*

                The ID used to identify the metrics configuration.

              - **Filter** *(dict) --*

                Specifies a metrics configuration filter. The metrics configuration will only include
                objects that meet the filter's criteria. A filter must be a prefix, a tag, or a conjunction
                (MetricsAndOperator).

                - **Prefix** *(string) --*

                  The prefix used when evaluating a metrics filter.

                - **Tag** *(dict) --*

                  The tag used when evaluating a metrics filter.

                  - **Key** *(string) --*

                    Name of the tag.

                  - **Value** *(string) --*

                    Value of the tag.

                - **And** *(dict) --*

                  A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter.
                  The operator must have at least two predicates, and an object must match all of the
                  predicates in order for the filter to apply.

                  - **Prefix** *(string) --*

                    The prefix used when evaluating an AND predicate.

                  - **Tags** *(list) --*

                    The list of tags used when evaluating an AND predicate.

                    - *(dict) --*

                      A container of a key value name pair.

                      - **Key** *(string) --*

                        Name of the tag.

                      - **Value** *(string) --*

                        Value of the tag.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_notification(
        self, Bucket: str
    ) -> ClientGetBucketNotificationResponseTypeDef:
        """
        No longer used, see  GetBucketNotificationConfiguration .

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not be
            used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketNotification>`_

        **Request Syntax**
        ::

          response = client.get_bucket_notification(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket for which to get the notification configuration

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TopicConfiguration': {
                    'Id': 'string',
                    'Events': [
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                        |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                        |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                        |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                        |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    ],
                    'Event':
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                    |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                    |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                    |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                    |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    'Topic': 'string'
                },
                'QueueConfiguration': {
                    'Id': 'string',
                    'Event':
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                    |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                    |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                    |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                    |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    'Events': [
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                        |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                        |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                        |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                        |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    ],
                    'Queue': 'string'
                },
                'CloudFunctionConfiguration': {
                    'Id': 'string',
                    'Event':
                    's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                    |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                    |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                    |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                    |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    'Events': [
                        's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                        |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                        |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                        |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                        |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                    ],
                    'CloudFunction': 'string',
                    'InvocationRole': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **TopicConfiguration** *(dict) --*

              This data type is deperecated. A container for specifying the configuration for publication
              of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3
              detects specified events.

              - **Id** *(string) --*

                An optional unique identifier for configurations in a notification configuration. If you
                don't provide one, Amazon S3 will assign an ID.

              - **Events** *(list) --*

                A collection of events related to objects

                - *(string) --*

                  The bucket event for which to send notifications.

              - **Event** *(string) --*

                Bucket event for which to send notifications.

              - **Topic** *(string) --*

                Amazon SNS topic to which Amazon S3 will publish a message to report the specified events
                for the bucket.

            - **QueueConfiguration** *(dict) --*

              This data type is deprecated. This data type specifies the configuration for publishing
              messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects
              specified events.

              - **Id** *(string) --*

                An optional unique identifier for configurations in a notification configuration. If you
                don't provide one, Amazon S3 will assign an ID.

              - **Event** *(string) --*

                The bucket event for which to send notifications.

              - **Events** *(list) --*

                A collection of bucket events for which to send notiications

                - *(string) --*

                  The bucket event for which to send notifications.

              - **Queue** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a
                message when it detects events of the specified type.

            - **CloudFunctionConfiguration** *(dict) --*

              Container for specifying the AWS Lambda notification configuration.

              - **Id** *(string) --*

                An optional unique identifier for configurations in a notification configuration. If you
                don't provide one, Amazon S3 will assign an ID.

              - **Event** *(string) --*

                The bucket event for which to send notifications.

              - **Events** *(list) --*

                Bucket events for which to send notifications.

                - *(string) --*

                  The bucket event for which to send notifications.

              - **CloudFunction** *(string) --*

                Lambda cloud function ARN that Amazon S3 can invoke when it detects events of the specified
                type.

              - **InvocationRole** *(string) --*

                The role supporting the invocation of the lambda function

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_notification_configuration(
        self, Bucket: str
    ) -> ClientGetBucketNotificationConfigurationResponseTypeDef:
        """
        Returns the notification configuration of a bucket.

        If notifications are not enabled on the bucket, the operation returns an empty
        ``NotificationConfiguration`` element.

        By default, you must be the bucket owner to read the notification configuration of a bucket.
        However, the bucket owner can use a bucket policy to grant permission to other users to read this
        configuration with the ``s3:GetBucketNotification`` permission.

        For more information about setting and reading the notification configuration on a bucket, see
        `Setting Up Notification of Bucket Events
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ . For more information
        about bucket policies, see `Using Bucket Policies
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html>`__ .

        The following operation is related to ``GetBucketNotification`` :

        *  PutBucketNotification

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketNotificationConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_bucket_notification_configuration(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket for which to get the notification configuration

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TopicConfigurations': [
                    {
                        'Id': 'string',
                        'TopicArn': 'string',
                        'Events': [
                            's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                            |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                            |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                            |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                            |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                        ],
                        'Filter': {
                            'Key': {
                                'FilterRules': [
                                    {
                                        'Name': 'prefix'|'suffix',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ],
                'QueueConfigurations': [
                    {
                        'Id': 'string',
                        'QueueArn': 'string',
                        'Events': [
                            's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                            |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                            |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                            |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                            |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                        ],
                        'Filter': {
                            'Key': {
                                'FilterRules': [
                                    {
                                        'Name': 'prefix'|'suffix',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ],
                'LambdaFunctionConfigurations': [
                    {
                        'Id': 'string',
                        'LambdaFunctionArn': 'string',
                        'Events': [
                            's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                            |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                            |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                            |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                            |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                        ],
                        'Filter': {
                            'Key': {
                                'FilterRules': [
                                    {
                                        'Name': 'prefix'|'suffix',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            A container for specifying the notification configuration of the bucket. If this element is
            empty, notifications are turned off for the bucket.

            - **TopicConfigurations** *(list) --*

              The topic to which notifications are sent and the events for which notifications are
              generated.

              - *(dict) --*

                A container for specifying the configuration for publication of messages to an Amazon
                Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.

                - **Id** *(string) --*

                  An optional unique identifier for configurations in a notification configuration. If you
                  don't provide one, Amazon S3 will assign an ID.

                - **TopicArn** *(string) --*

                  The Amazon Resource Name (ARN) of the Amazon SNS topic to which Amazon S3 publishes a
                  message when it detects events of the specified type.

                - **Events** *(list) --*

                  The Amazon S3 bucket event about which to send notifications. For more information, see
                  `Supported Event Types
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the
                  *Amazon Simple Storage Service Developer Guide* .

                  - *(string) --*

                    The bucket event for which to send notifications.

                - **Filter** *(dict) --*

                  Specifies object key name filtering rules. For information about key name filtering, see
                  `Configuring Event Notifications
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the
                  *Amazon Simple Storage Service Developer Guide* .

                  - **Key** *(dict) --*

                    A container for object key name prefix and suffix filtering rules.

                    - **FilterRules** *(list) --*

                      A list of containers for the key value pair that defines the criteria for the filter
                      rule.

                      - *(dict) --*

                        Specifies the Amazon S3 object key name to filter on and whether to filter on the
                        suffix or prefix of the key name.

                        - **Name** *(string) --*

                          The object key name prefix or suffix identifying one or more objects to which the
                          filtering rule applies. The maximum length is 1,024 characters. Overlapping
                          prefixes and suffixes are not supported. For more information, see `Configuring
                          Event Notifications
                          <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in
                          the *Amazon Simple Storage Service Developer Guide* .

                        - **Value** *(string) --*

                          The value that the filter searches for in object key names.

            - **QueueConfigurations** *(list) --*

              The Amazon Simple Queue Service queues to publish messages to and the events for which to
              publish messages.

              - *(dict) --*

                Specifies the configuration for publishing messages to an Amazon Simple Queue Service
                (Amazon SQS) queue when Amazon S3 detects specified events.

                - **Id** *(string) --*

                  An optional unique identifier for configurations in a notification configuration. If you
                  don't provide one, Amazon S3 will assign an ID.

                - **QueueArn** *(string) --*

                  The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a
                  message when it detects events of the specified type.

                - **Events** *(list) --*

                  A collection of bucket events for which to send notiications

                  - *(string) --*

                    The bucket event for which to send notifications.

                - **Filter** *(dict) --*

                  Specifies object key name filtering rules. For information about key name filtering, see
                  `Configuring Event Notifications
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the
                  *Amazon Simple Storage Service Developer Guide* .

                  - **Key** *(dict) --*

                    A container for object key name prefix and suffix filtering rules.

                    - **FilterRules** *(list) --*

                      A list of containers for the key value pair that defines the criteria for the filter
                      rule.

                      - *(dict) --*

                        Specifies the Amazon S3 object key name to filter on and whether to filter on the
                        suffix or prefix of the key name.

                        - **Name** *(string) --*

                          The object key name prefix or suffix identifying one or more objects to which the
                          filtering rule applies. The maximum length is 1,024 characters. Overlapping
                          prefixes and suffixes are not supported. For more information, see `Configuring
                          Event Notifications
                          <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in
                          the *Amazon Simple Storage Service Developer Guide* .

                        - **Value** *(string) --*

                          The value that the filter searches for in object key names.

            - **LambdaFunctionConfigurations** *(list) --*

              Describes the AWS Lambda functions to invoke and the events for which to invoke them.

              - *(dict) --*

                A container for specifying the configuration for AWS Lambda notifications.

                - **Id** *(string) --*

                  An optional unique identifier for configurations in a notification configuration. If you
                  don't provide one, Amazon S3 will assign an ID.

                - **LambdaFunctionArn** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS Lambda function that Amazon S3 invokes when the
                  specified event type occurs.

                - **Events** *(list) --*

                  The Amazon S3 bucket event for which to invoke the AWS Lambda function. For more
                  information, see `Supported Event Types
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the
                  *Amazon Simple Storage Service Developer Guide* .

                  - *(string) --*

                    The bucket event for which to send notifications.

                - **Filter** *(dict) --*

                  Specifies object key name filtering rules. For information about key name filtering, see
                  `Configuring Event Notifications
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the
                  *Amazon Simple Storage Service Developer Guide* .

                  - **Key** *(dict) --*

                    A container for object key name prefix and suffix filtering rules.

                    - **FilterRules** *(list) --*

                      A list of containers for the key value pair that defines the criteria for the filter
                      rule.

                      - *(dict) --*

                        Specifies the Amazon S3 object key name to filter on and whether to filter on the
                        suffix or prefix of the key name.

                        - **Name** *(string) --*

                          The object key name prefix or suffix identifying one or more objects to which the
                          filtering rule applies. The maximum length is 1,024 characters. Overlapping
                          prefixes and suffixes are not supported. For more information, see `Configuring
                          Event Notifications
                          <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in
                          the *Amazon Simple Storage Service Developer Guide* .

                        - **Value** *(string) --*

                          The value that the filter searches for in object key names.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_policy(self, Bucket: str) -> ClientGetBucketPolicyResponseTypeDef:
        """
        Returns the policy of a specified bucket. If you are using an identity other than the root user of
        the AWS account that owns the bucket, the calling identity must have the ``GetBucketPolicy``
        permissions on the specified bucket and belong to the bucket owner's account in order to use this
        operation.

        If you don't have ``GetBucketPolicy`` permissions, Amazon S3 returns a ``403 Access Denied`` error.
        If you have the correct permissions, but you're not using an identity that belongs to the bucket
        owner's account, Amazon S3 returns a ``405 Method Not Allowed`` error.

        .. warning::

          As a security precaution, the root user of the AWS account that owns a bucket can always use this
          operation, even if the policy explicitly denies the root user the ability to perform this action.

        For more information about bucket policies, see `Using Bucket Policies and User Policies
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html>`__ .

        The following operation is related to ``GetBucketPolicy`` :

        *  GetObject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketPolicy>`_

        **Request Syntax**
        ::

          response = client.get_bucket_policy(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name for which to get the bucket policy.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Policy': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Policy** *(string) --*

              The bucket policy as a JSON document.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_policy_status(
        self, Bucket: str
    ) -> ClientGetBucketPolicyStatusResponseTypeDef:
        """
        Retrieves the policy status for an Amazon S3 bucket, indicating whether the bucket is public. In
        order to use this operation, you must have the ``s3:GetBucketPolicyStatus`` permission. For more
        information about Amazon S3 permissions, see `Specifying Permissions in a Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html>`__ .

        For more information about when Amazon S3 considers a bucket public, see `The Meaning of "Public"
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status>`__
        .

        The following operations are related to ``GetBucketPolicyStatus`` :

        * `Using Amazon S3 Block Public Access
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html>`__

        *  GetPublicAccessBlock

        *  PutPublicAccessBlock

        *  DeletePublicAccessBlock

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketPolicyStatus>`_

        **Request Syntax**
        ::

          response = client.get_bucket_policy_status(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the Amazon S3 bucket whose policy status you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PolicyStatus': {
                    'IsPublic': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **PolicyStatus** *(dict) --*

              The policy status for the specified bucket.

              - **IsPublic** *(boolean) --*

                The policy status for this bucket. ``TRUE`` indicates that this bucket is public. ``FALSE``
                indicates that the bucket is not public.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_replication(
        self, Bucket: str
    ) -> ClientGetBucketReplicationResponseTypeDef:
        """
        Returns the replication configuration of a bucket.

        .. note::

          It can take a while to propagate the put or delete a replication configuration to all Amazon S3
          systems. Therefore, a get request soon after put or delete can return a wrong result.

        For information about replication configuration, see `Replication
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html>`__ .

        This operation requires permissions for the ``s3:GetReplicationConfiguration`` action. For more
        information about permissions, see `Using Bucket Policies and User Policies
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html>`__ .

        If you include the ``Filter`` element in a replication configuration, you must also include the
        ``DeleteMarkerReplication`` and ``Priority`` elements. The response also returns those elements.

         ``GetBucketReplication`` has the following special error:

        * Error code: ``NoSuchReplicationConfiguration``

          * Description: There is no replication configuration with that name.

          * HTTP Status Code: 404 Not Found

          * SOAP Fault Code Prefix: Client

        The following operations are related to ``GetBucketReplication`` :

        *  PutBucketReplication

        *  DeleteBucketReplication

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketReplication>`_

        **Request Syntax**
        ::

          response = client.get_bucket_replication(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name for which to get the replication information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationConfiguration': {
                    'Role': 'string',
                    'Rules': [
                        {
                            'ID': 'string',
                            'Priority': 123,
                            'Prefix': 'string',
                            'Filter': {
                                'Prefix': 'string',
                                'Tag': {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                                'And': {
                                    'Prefix': 'string',
                                    'Tags': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                }
                            },
                            'Status': 'Enabled'|'Disabled',
                            'SourceSelectionCriteria': {
                                'SseKmsEncryptedObjects': {
                                    'Status': 'Enabled'|'Disabled'
                                }
                            },
                            'ExistingObjectReplication': {
                                'Status': 'Enabled'|'Disabled'
                            },
                            'Destination': {
                                'Bucket': 'string',
                                'Account': 'string',
                                'StorageClass':
                                'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'
                                |'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                                'AccessControlTranslation': {
                                    'Owner': 'Destination'
                                },
                                'EncryptionConfiguration': {
                                    'ReplicaKmsKeyID': 'string'
                                }
                            },
                            'DeleteMarkerReplication': {
                                'Status': 'Enabled'|'Disabled'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationConfiguration** *(dict) --*

              A container for replication rules. You can add up to 1,000 rules. The maximum size of a
              replication configuration is 2 MB.

              - **Role** *(string) --*

                The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
                Amazon S3 assumes when replicating objects. For more information, see `How to Set Up
                Replication <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html>`__
                in the *Amazon Simple Storage Service Developer Guide* .

              - **Rules** *(list) --*

                A container for one or more replication rules. A replication configuration must have at
                least one rule and can contain a maximum of 1,000 rules.

                - *(dict) --*

                  Specifies which Amazon S3 objects to replicate and where to store the replicas.

                  - **ID** *(string) --*

                    A unique identifier for the rule. The maximum value is 255 characters.

                  - **Priority** *(integer) --*

                    The priority associated with the rule. If you specify multiple rules in a replication
                    configuration, Amazon S3 prioritizes the rules to prevent conflicts when filtering. If
                    two or more rules identify the same object based on a specified filter, the rule with
                    higher priority takes precedence. For example:

                    * Same object quality prefix based filter criteria If prefixes you specified in
                    multiple rules overlap

                    * Same object qualify tag based filter criteria specified in multiple rules

                    For more information, see `Replication <
                    https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html>`__ in the *Amazon S3
                    Developer Guide* .

                  - **Prefix** *(string) --*

                    An object keyname prefix that identifies the object or objects to which the rule
                    applies. The maximum prefix length is 1,024 characters. To include all objects in a
                    bucket, specify an empty string.

                  - **Filter** *(dict) --*

                    A filter that identifies the subset of objects to which the replication rule applies. A
                    ``Filter`` must specify exactly one ``Prefix`` , ``Tag`` , or an ``And`` child element.

                    - **Prefix** *(string) --*

                      An object keyname prefix that identifies the subset of objects to which the rule
                      applies.

                    - **Tag** *(dict) --*

                      A container for specifying a tag key and value.

                      The rule applies only to objects that have the tag in their tag set.

                      - **Key** *(string) --*

                        Name of the tag.

                      - **Value** *(string) --*

                        Value of the tag.

                    - **And** *(dict) --*

                      A container for specifying rule filters. The filters determine the subset of objects
                      to which the rule applies. This element is required only if you specify more than one
                      filter. For example:

                      * If you specify both a ``Prefix`` and a ``Tag`` filter, wrap these filters in an
                      ``And`` tag.

                      * If you specify a filter based on multiple tags, wrap the ``Tag`` elements in an
                      ``And`` tag.

                      - **Prefix** *(string) --*

                        An object keyname prefix that identifies the subset of objects to which the rule
                        applies.

                      - **Tags** *(list) --*

                        An array of tags containing key and value pairs.

                        - *(dict) --*

                          A container of a key value name pair.

                          - **Key** *(string) --*

                            Name of the tag.

                          - **Value** *(string) --*

                            Value of the tag.

                  - **Status** *(string) --*

                    Specifies whether the rule is enabled.

                  - **SourceSelectionCriteria** *(dict) --*

                    A container that describes additional filters for identifying the source objects that
                    you want to replicate. You can choose to enable or disable the replication of these
                    objects. Currently, Amazon S3 supports only the filter that you can specify for objects
                    created with server-side encryption using a customer master key (CMK) stored in AWS Key
                    Management Service (SSE-KMS).

                    - **SseKmsEncryptedObjects** *(dict) --*

                      A container for filter information for the selection of Amazon S3 objects encrypted
                      with AWS KMS. If you include ``SourceSelectionCriteria`` in the replication
                      configuration, this element is required.

                      - **Status** *(string) --*

                        Specifies whether Amazon S3 replicates objects created with server-side encryption
                        using a customer master key (CMK) stored in AWS Key Management Service.

                  - **ExistingObjectReplication** *(dict) --*

                    A container that specifies information about existing object replication. You can
                    choose whether to enable or disable the replication of existing objects.

                    - **Status** *(string) --*

                      Specifies whether existing object replication is enabled.

                  - **Destination** *(dict) --*

                    A container for information about the replication destination.

                    - **Bucket** *(string) --*

                      The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store the
                      results.

                    - **Account** *(string) --*

                      Destination bucket owner account ID. In a cross-account scenario, if you direct
                      Amazon S3 to change replica ownership to the AWS account that owns the destination
                      bucket by specifying the ``AccessControlTranslation`` property, this is the account
                      ID of the destination bucket owner. For more information, see `Replication Additional
                      Configuration\\: Change Replica Owner
                      <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-change-owner.html>`__ in
                      the *Amazon Simple Storage Service Developer Guide* .

                    - **StorageClass** *(string) --*

                      The storage class to use when replicating objects, such as standard or reduced
                      redundancy. By default, Amazon S3 uses the storage class of the source object to
                      create the object replica.

                      For valid values, see the ``StorageClass`` element of the `PUT Bucket replication
                      <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html>`__
                      action in the *Amazon Simple Storage Service API Reference* .

                    - **AccessControlTranslation** *(dict) --*

                      Specify this only in a cross-account scenario (where source and destination bucket
                      owners are not the same), and you want to change replica ownership to the AWS account
                      that owns the destination bucket. If this is not specified in the replication
                      configuration, the replicas are owned by same AWS account that owns the source object.

                      - **Owner** *(string) --*

                        Specifies the replica ownership. For default and valid values, see `PUT bucket
                        replication
                        <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html>`__
                        in the *Amazon Simple Storage Service API Reference* .

                    - **EncryptionConfiguration** *(dict) --*

                      A container that provides information about encryption. If
                      ``SourceSelectionCriteria`` is specified, you must specify this element.

                      - **ReplicaKmsKeyID** *(string) --*

                        Specifies the AWS KMS Key ID (Key ARN or Alias ARN) for the destination bucket.
                        Amazon S3 uses this key to encrypt replica objects.

                  - **DeleteMarkerReplication** *(dict) --*

                    Specifies whether Amazon S3 replicates the delete markers. If you specify a ``Filter``
                    , you must specify this element. However, in the latest version of replication
                    configuration (when ``Filter`` is specified), Amazon S3 doesn't replicate delete
                    markers. Therefore, the ``DeleteMarkerReplication`` element can contain only
                    <Status>Disabled</Status>. For an example configuration, see `Basic Rule Configuration
                    <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-config-min-rule-config>`__
                    .

                    .. note::

                      If you don't specify the Filter element, Amazon S3 assumes the replication
                      configuration is the earlier version, V1. In the earlier version, Amazon S3 handled
                      replication of delete markers differently. For more information, see `Backward
                      Compatibility
                      <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations>`__
                      .

                    - **Status** *(string) --*

                      Indicates whether to replicate delete markers.

                      .. note::

                        In the current implementation, Amazon S3 doesn't replicate the delete markers. The
                        status must be ``Disabled`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_request_payment(
        self, Bucket: str
    ) -> ClientGetBucketRequestPaymentResponseTypeDef:
        """
        Returns the request payment configuration of a bucket. To use this version of the operation, you
        must be the bucket owner. For more information, see `Requester Pays Buckets
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`__ .

        The following operations are related to ``GetBucketRequestPayment`` :

        *  ListObjects

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketRequestPayment>`_

        **Request Syntax**
        ::

          response = client.get_bucket_request_payment(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket for which to get the payment request configuration

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Payer': 'Requester'|'BucketOwner'
            }
          **Response Structure**

          - *(dict) --*

            - **Payer** *(string) --*

              Specifies who pays for the download and request fees.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_tagging(self, Bucket: str) -> ClientGetBucketTaggingResponseTypeDef:
        """
        Returns the tag set associated with the bucket.

        To use this operation, you must have permission to perform the ``s3:GetBucketTagging`` action. By
        default, the bucket owner has this permission and can grant this permission to others.

         ``GetBucketTagging`` has the following special error:

        * Error code: ``NoSuchTagSetError``

          * Description: There is no tag set associated with the bucket.

        The following operations are related to ``GetBucketTagging`` :

        *  PutBucketTagging

        *  DeleteBucketTagging

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketTagging>`_

        **Request Syntax**
        ::

          response = client.get_bucket_tagging(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket for which to get the tagging information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TagSet': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **TagSet** *(list) --*

              Contains the tag set.

              - *(dict) --*

                A container of a key value name pair.

                - **Key** *(string) --*

                  Name of the tag.

                - **Value** *(string) --*

                  Value of the tag.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_versioning(
        self, Bucket: str
    ) -> ClientGetBucketVersioningResponseTypeDef:
        """
        Returns the versioning state of a bucket.

        To retrieve the versioning state of a bucket, you must be the bucket owner.

        This implementation also returns the MFA Delete status of the versioning state, i.e., if the MFA
        Delete status is ``enabled`` , the bucket owner must use an authentication device to change the
        versioning state of the bucket.

        The following operations are related to ``GetBucketVersioning`` :

        *  GetObject

        *  PutObject

        *  DeleteObject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketVersioning>`_

        **Request Syntax**
        ::

          response = client.get_bucket_versioning(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket for which to get the versioning information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Status': 'Enabled'|'Suspended',
                'MFADelete': 'Enabled'|'Disabled'
            }
          **Response Structure**

          - *(dict) --*

            - **Status** *(string) --*

              The versioning state of the bucket.

            - **MFADelete** *(string) --*

              Specifies whether MFA delete is enabled in the bucket versioning configuration. This element
              is only returned if the bucket has been configured with MFA delete. If the bucket has never
              been so configured, this element is not returned.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bucket_website(self, Bucket: str) -> ClientGetBucketWebsiteResponseTypeDef:
        """
        Returns the website configuration for a bucket. To host website on Amazon S3, you can configure a
        bucket as website by adding a website configuration. For more information about hosting websites,
        see `Hosting Websites on Amazon S3
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html>`__ .

        This GET operation requires the ``S3:GetBucketWebsite`` permission. By default, only the bucket
        owner can read the bucket website configuration. However, bucket owners can allow other users to
        read the website configuration by writing a bucket policy granting them the ``S3:GetBucketWebsite``
        permission.

        The following operations are related to ``DeleteBucketWebsite``

        *  DeleteBucketWebsite

        *  PutBucketWebsite

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetBucketWebsite>`_

        **Request Syntax**
        ::

          response = client.get_bucket_website(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name for which to get the website configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RedirectAllRequestsTo': {
                    'HostName': 'string',
                    'Protocol': 'http'|'https'
                },
                'IndexDocument': {
                    'Suffix': 'string'
                },
                'ErrorDocument': {
                    'Key': 'string'
                },
                'RoutingRules': [
                    {
                        'Condition': {
                            'HttpErrorCodeReturnedEquals': 'string',
                            'KeyPrefixEquals': 'string'
                        },
                        'Redirect': {
                            'HostName': 'string',
                            'HttpRedirectCode': 'string',
                            'Protocol': 'http'|'https',
                            'ReplaceKeyPrefixWith': 'string',
                            'ReplaceKeyWith': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **RedirectAllRequestsTo** *(dict) --*

              Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.

              - **HostName** *(string) --*

                Name of the host where requests are redirected.

              - **Protocol** *(string) --*

                Protocol to use when redirecting requests. The default is the protocol that is used in the
                original request.

            - **IndexDocument** *(dict) --*

              The name of the index document for the website.

              - **Suffix** *(string) --*

                A suffix that is appended to a request that is for a directory on the website endpoint
                (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data
                that is returned will be for the object with the key name images/index.html) The suffix
                must not be empty and must not include a slash character.

            - **ErrorDocument** *(dict) --*

              The name of the error document for the website.

              - **Key** *(string) --*

                The object key name to use when a 4XX class error occurs.

            - **RoutingRules** *(list) --*

              Rules that define when a redirect is applied and the redirect behavior.

              - *(dict) --*

                Specifies the redirect behavior and when a redirect is applied.

                - **Condition** *(dict) --*

                  A container for describing a condition that must be met for the specified redirect to
                  apply. For example, 1. If request is for pages in the ``/docs`` folder, redirect to the
                  ``/documents`` folder. 2. If request results in HTTP error 4xx, redirect request to
                  another host where you might process the error.

                  - **HttpErrorCodeReturnedEquals** *(string) --*

                    The HTTP error code when the redirect is applied. In the event of an error, if the
                    error code equals this value, then the specified redirect is applied. Required when
                    parent element ``Condition`` is specified and sibling ``KeyPrefixEquals`` is not
                    specified. If both are specified, then both must be true for the redirect to be applied.

                  - **KeyPrefixEquals** *(string) --*

                    The object key name prefix when the redirect is applied. For example, to redirect
                    requests for ``ExamplePage.html`` , the key prefix will be ``ExamplePage.html`` . To
                    redirect request for all pages with the prefix ``docs/`` , the key prefix will be
                    ``/docs`` , which identifies all objects in the docs/ folder. Required when the parent
                    element ``Condition`` is specified and sibling ``HttpErrorCodeReturnedEquals`` is not
                    specified. If both conditions are specified, both must be true for the redirect to be
                    applied.

                - **Redirect** *(dict) --*

                  Container for redirect information. You can redirect requests to another host, to another
                  page, or with another protocol. In the event of an error, you can specify a different
                  error code to return.

                  - **HostName** *(string) --*

                    The host name to use in the redirect request.

                  - **HttpRedirectCode** *(string) --*

                    The HTTP redirect code to use on the response. Not required if one of the siblings is
                    present.

                  - **Protocol** *(string) --*

                    Protocol to use when redirecting requests. The default is the protocol that is used in
                    the original request.

                  - **ReplaceKeyPrefixWith** *(string) --*

                    The object key prefix to use in the redirect request. For example, to redirect requests
                    for all pages with prefix ``docs/`` (objects in the ``docs/`` folder) to ``documents/``
                    , you can set a condition block with ``KeyPrefixEquals`` set to ``docs/`` and in the
                    Redirect set ``ReplaceKeyPrefixWith`` to ``/documents`` . Not required if one of the
                    siblings is present. Can be present only if ``ReplaceKeyWith`` is not provided.

                  - **ReplaceKeyWith** *(string) --*

                    The specific object key to use in the redirect request. For example, redirect request
                    to ``error.html`` . Not required if one of the siblings is present. Can be present only
                    if ``ReplaceKeyPrefixWith`` is not provided.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_object(
        self,
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
    ) -> ClientGetObjectResponseTypeDef:
        """
        Retrieves objects from Amazon S3. To use ``GET`` , you must have ``READ`` access to the object. If
        you grant ``READ`` access to the anonymous user, you can return the object without using an
        authorization header.

        An Amazon S3 bucket has no directory hierarchy such as you would find in a typical computer file
        system. You can, however, create a logical hierarchy by using object key names that imply a folder
        structure. For example, instead of naming an object ``sample.jpg`` , you can name it
        ``photos/2006/February/sample.jpg`` .

        To get an object from such a logical hierarchy, specify the full key name for the object in the
        ``GET`` operation. For a virtual hosted-style request example, if you have the object
        ``photos/2006/February/sample.jpg`` , specify the resource as ``/photos/2006/February/sample.jpg``
        . For a path-style request example, if you have the object ``photos/2006/February/sample.jpg`` in
        the bucket named examplebucket, specify the resource as
        ``/examplebucket/photos/2006/February/sample.jpg`` . For more information about request types, see
        `HTTP Host Header Bucket Specification
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html#VirtualHostingSpecifyBucket>`__
        .

        To distribute large files to many people, you can save bandwidth costs by using BitTorrent. For
        more information, see `Amazon S3 Torrent
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/S3Torrent.html>`__ . For more information about
        returning the ACL of an object, see  GetObjectAcl .

        If the object you are retrieving is stored in the GLACIER or DEEP_ARCHIVE storage classes, before
        you can retrieve the object you must first restore a copy using . Otherwise, this operation returns
        an ``InvalidObjectStateError`` error. For information about restoring archived objects, see
        `Restoring Archived Objects
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/restoring-objects.html>`__ .

        Encryption request headers, like ``x-amz-server-side-encryption`` , should not be sent for GET
        requests if your object uses server-side encryption with CMKs stored in AWS KMS (SSE-KMS) or
        server-side encryption with Amazon S3–managed encryption keys (SSE-S3). If your object does use
        these types of keys, you’ll get an HTTP 400 BadRequest error.

        If you encrypt an object by using server-side encryption with customer-provided encryption keys
        (SSE-C) when you store the object in Amazon S3, then when you GET the object, you must use the
        following headers:

        * x-amz-server-side​-encryption​-customer-algorithm

        * x-amz-server-side​-encryption​-customer-key

        * x-amz-server-side​-encryption​-customer-key-MD5

        For more information about SSE-C, see `Server-Side Encryption (Using Customer-Provided Encryption
        Keys) <https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html>`__ .

        Assuming you have permission to read object tags (permission for the ``s3:GetObjectVersionTagging``
        action), the response also returns the ``x-amz-tagging-count`` header that provides the count of
        number of tags associated with the object. You can use  GetObjectTagging to retrieve the tag set
        associated with an object.

         **Permissions**

        You need the ``s3:GetObject`` permission for this operation. For more information, see `Specifying
        Permissions in a Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html>`__ . If the object you
        request does not exist, the error Amazon S3 returns depends on whether you also have the
        ``s3:ListBucket`` permission.

        * If you have the ``s3:ListBucket`` permission on the bucket, Amazon S3 will return an HTTP status
        code 404 ("no such key") error.

        * If you don’t have the ``s3:ListBucket`` permission, Amazon S3 will return an HTTP status code 403
        ("access denied") error.

         **Versioning**

        By default, the GET operation returns the current version of an object. To return a different
        version, use the ``versionId`` subresource.

        .. note::

          If the current version of the object is a delete marker, Amazon S3 behaves as if the object was
          deleted and includes ``x-amz-delete-marker: true`` in the response.

        For more information about versioning, see  PutBucketVersioning .

         **Overriding Response Header Values**

        There are times when you want to override certain response header values in a GET response. For
        example, you might override the Content-Disposition response header value in your GET request.

        You can override values for a set of response headers using the following query parameters. These
        response header values are sent only on a successful request, that is, when status code 200 OK is
        returned. The set of headers you can override using these parameters is a subset of the headers
        that Amazon S3 accepts when you create an object. The response headers that you can override for
        the GET response are ``Content-Type`` , ``Content-Language`` , ``Expires`` , ``Cache-Control`` ,
        ``Content-Disposition`` , and ``Content-Encoding`` . To override these header values in the GET
        response, you use the following request parameters.

        .. note::

          You must sign the request, either using an Authorization header or a presigned URL, when using
          these parameters. They cannot be used with an unsigned (anonymous) request.

        * ``response-content-type``

        * ``response-content-language``

        * ``response-expires``

        * ``response-cache-control``

        * ``response-content-disposition``

        * ``response-content-encoding``

         **Additional Considerations about Request Headers**

        If both of the ``If-Match`` and ``If-Unmodified-Since`` headers are present in the request as
        follows: ``If-Match`` condition evaluates to ``true`` , and; ``If-Unmodified-Since`` condition
        evaluates to ``false`` ; then, S3 returns 200 OK and the data requested.

        If both of the ``If-None-Match`` and ``If-Modified-Since`` headers are present in the request as
        follows:``If-None-Match`` condition evaluates to ``false`` , and; ``If-Modified-Since`` condition
        evaluates to ``true`` ; then, S3 returns 304 Not Modified response code.

        For more information about conditional requests, see `RFC 7232
        <https://tools.ietf.org/html/rfc7232>`__ .

        The following operations are related to ``GetObject`` :

        *  ListBuckets

        *  GetObjectAcl

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObject>`_

        **Request Syntax**
        ::

          response = client.get_object(
              Bucket='string',
              IfMatch='string',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch='string',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Key='string',
              Range='string',
              ResponseCacheControl='string',
              ResponseContentDisposition='string',
              ResponseContentEncoding='string',
              ResponseContentLanguage='string',
              ResponseContentType='string',
              ResponseExpires=datetime(2015, 1, 1),
              VersionId='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              RequestPayer='requester',
              PartNumber=123
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name containing the object.

        :type IfMatch: string
        :param IfMatch:

          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise
          return a 412 (precondition failed).

        :type IfModifiedSince: datetime
        :param IfModifiedSince:

          Return the object only if it has been modified since the specified time, otherwise return a 304
          (not modified).

        :type IfNoneMatch: string
        :param IfNoneMatch:

          Return the object only if its entity tag (ETag) is different from the one specified, otherwise
          return a 304 (not modified).

        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince:

          Return the object only if it has not been modified since the specified time, otherwise return a
          412 (precondition failed).

        :type Key: string
        :param Key: **[REQUIRED]**

          Key of the object to get.

        :type Range: string
        :param Range:

          Downloads the specified range bytes of an object. For more information about the HTTP Range
          header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.

        :type ResponseCacheControl: string
        :param ResponseCacheControl:

          Sets the Cache-Control header of the response.

        :type ResponseContentDisposition: string
        :param ResponseContentDisposition:

          Sets the Content-Disposition header of the response

        :type ResponseContentEncoding: string
        :param ResponseContentEncoding:

          Sets the Content-Encoding header of the response.

        :type ResponseContentLanguage: string
        :param ResponseContentLanguage:

          Sets the Content-Language header of the response.

        :type ResponseContentType: string
        :param ResponseContentType:

          Sets the Content-Type header of the response.

        :type ResponseExpires: datetime
        :param ResponseExpires:

          Sets the Expires header of the response.

        :type VersionId: string
        :param VersionId:

          VersionId used to reference a specific version of the object.

        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:

          Specifies the algorithm to use to when encrypting the object (e.g., AES256).

        :type SSECustomerKey: string
        :param SSECustomerKey:

          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This
          value is used to store the object and then it is discarded; Amazon does not store the encryption
          key. The key must be appropriate for use with the algorithm specified in the
          x-amz-server-side​-encryption​-customer-algorithm header.

        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:

          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this
          header for a message integrity check to ensure the encryption key was transmitted without error.

            Please note that this parameter is automatically populated if it is not provided. Including
            this parameter is not required

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type PartNumber: integer
        :param PartNumber:

          Part number of the object being read. This is a positive integer between 1 and 10,000.
          Effectively performs a 'ranged' GET request for the part specified. Useful for downloading just a
          part of an object.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Body': StreamingBody(),
                'DeleteMarker': True|False,
                'AcceptRanges': 'string',
                'Expiration': 'string',
                'Restore': 'string',
                'LastModified': datetime(2015, 1, 1),
                'ContentLength': 123,
                'ETag': 'string',
                'MissingMeta': 123,
                'VersionId': 'string',
                'CacheControl': 'string',
                'ContentDisposition': 'string',
                'ContentEncoding': 'string',
                'ContentLanguage': 'string',
                'ContentRange': 'string',
                'ContentType': 'string',
                'Expires': datetime(2015, 1, 1),
                'WebsiteRedirectLocation': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'Metadata': {
                    'string': 'string'
                },
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'StorageClass':
                'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'
                |'DEEP_ARCHIVE',
                'RequestCharged': 'requester',
                'ReplicationStatus': 'COMPLETE'|'PENDING'|'FAILED'|'REPLICA',
                'PartsCount': 123,
                'TagCount': 123,
                'ObjectLockMode': 'GOVERNANCE'|'COMPLIANCE',
                'ObjectLockRetainUntilDate': datetime(2015, 1, 1),
                'ObjectLockLegalHoldStatus': 'ON'|'OFF'
            }
          **Response Structure**

          - *(dict) --*

            - **Body** (:class:`.StreamingBody`) --

              Object data.

            - **DeleteMarker** *(boolean) --*

              Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If
              false, this response header does not appear in the response.

            - **AcceptRanges** *(string) --*

              Indicates that a range of bytes was specifed.

            - **Expiration** *(string) --*

              If the object expiration is configured (see PUT Bucket lifecycle), the response includes this
              header. It includes the expiry-date and rule-id key value pairs providing object expiration
              information. The value of the rule-id is URL encoded.

            - **Restore** *(string) --*

              Provides information about object restoration operation and expiration time of the restored
              object copy.

            - **LastModified** *(datetime) --*

              Last modified date of the object

            - **ContentLength** *(integer) --*

              Size of the body in bytes.

            - **ETag** *(string) --*

              An ETag is an opaque identifier assigned by a web server to a specific version of a resource
              found at a URL

            - **MissingMeta** *(integer) --*

              This is set to the number of metadata entries not returned in x-amz-meta headers. This can
              happen if you create metadata using an API like SOAP that supports more flexible metadata
              than the REST API. For example, using SOAP, you can create metadata whose values are not
              legal HTTP headers.

            - **VersionId** *(string) --*

              Version of the object.

            - **CacheControl** *(string) --*

              Specifies caching behavior along the request/reply chain.

            - **ContentDisposition** *(string) --*

              Specifies presentational information for the object.

            - **ContentEncoding** *(string) --*

              Specifies what content encodings have been applied to the object and thus what decoding
              mechanisms must be applied to obtain the media-type referenced by the Content-Type header
              field.

            - **ContentLanguage** *(string) --*

              The language the content is in.

            - **ContentRange** *(string) --*

              The portion of the object returned in the response.

            - **ContentType** *(string) --*

              A standard MIME type describing the format of the object data.

            - **Expires** *(datetime) --*

              The date and time at which the object is no longer cacheable.

            - **WebsiteRedirectLocation** *(string) --*

              If the bucket is configured as a website, redirects requests for this object to another
              object in the same bucket or to an external URL. Amazon S3 stores the value of this header in
              the object metadata.

            - **ServerSideEncryption** *(string) --*

              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256,
              aws:kms).

            - **Metadata** *(dict) --*

              A map of metadata to store with the object in S3.

              - *(string) --*

                - *(string) --*

            - **SSECustomerAlgorithm** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header confirming the encryption algorithm used.

            - **SSECustomerKeyMD5** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header to provide round trip message integrity verification of the
              customer-provided encryption key.

            - **SSEKMSKeyId** *(string) --*

              If present, specifies the ID of the AWS Key Management Service (KMS) customer master key
              (CMK) that was used for the object.

            - **StorageClass** *(string) --*

              Provides storage class information of the object. Amazon S3 returns this header for all
              objects except for Standard storage class objects.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

            - **ReplicationStatus** *(string) --*

              Amazon S3 can return this if your request involves a bucket that is either a source or
              destination in a replication rule.

            - **PartsCount** *(integer) --*

              The count of parts this object has.

            - **TagCount** *(integer) --*

              The number of tags, if any, on the object.

            - **ObjectLockMode** *(string) --*

              The Object Lock mode currently in place for this object.

            - **ObjectLockRetainUntilDate** *(datetime) --*

              The date and time when this object's Object Lock will expire.

            - **ObjectLockLegalHoldStatus** *(string) --*

              Indicates whether this object has an active legal hold. This field is only returned if you
              have permission to view an object's legal hold status.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_object_acl(
        self, Bucket: str, Key: str, VersionId: str = None, RequestPayer: str = None
    ) -> ClientGetObjectAclResponseTypeDef:
        """
        Returns the access control list (ACL) of an object. To use this operation, you must have READ_ACP
        access to the object.

         **Versioning**

        By default, GET returns ACL information about the current version of an object. To return ACL
        information about a different version, use the versionId subresource.

        The following operations are related to ``GetObjectAcl`` :

        *  GetObject

        *  DeleteObject

        *  PutObject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectAcl>`_

        **Request Syntax**
        ::

          response = client.get_object_acl(
              Bucket='string',
              Key='string',
              VersionId='string',
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name of the object for which to get the ACL information.

        :type Key: string
        :param Key: **[REQUIRED]**

          The key of the object for which to get the ACL information.

        :type VersionId: string
        :param VersionId:

          VersionId used to reference a specific version of the object.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                },
                'Grants': [
                    {
                        'Grantee': {
                            'DisplayName': 'string',
                            'EmailAddress': 'string',
                            'ID': 'string',
                            'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                            'URI': 'string'
                        },
                        'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                    },
                ],
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **Owner** *(dict) --*

              Container for the bucket owner's display name and ID.

              - **DisplayName** *(string) --*

                Container for the display name of the owner

              - **ID** *(string) --*

                Container for the ID of the owner

            - **Grants** *(list) --*

              A list of grants.

              - *(dict) --*

                Container for grant information.

                - **Grantee** *(dict) --*

                  The person being granted permissions.

                  - **DisplayName** *(string) --*

                    Screen name of the grantee.

                  - **EmailAddress** *(string) --*

                    Email address of the grantee.

                  - **ID** *(string) --*

                    The canonical user ID of the grantee.

                  - **Type** *(string) --*

                    Type of grantee

                  - **URI** *(string) --*

                    URI of the grantee group.

                - **Permission** *(string) --*

                  Specifies the permission given to the grantee.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_object_legal_hold(
        self, Bucket: str, Key: str, VersionId: str = None, RequestPayer: str = None
    ) -> ClientGetObjectLegalHoldResponseTypeDef:
        """
        Gets an object's current Legal Hold status. For more information, see `Locking Objects
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectLegalHold>`_

        **Request Syntax**
        ::

          response = client.get_object_legal_hold(
              Bucket='string',
              Key='string',
              VersionId='string',
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket containing the object whose Legal Hold status you want to retrieve.

        :type Key: string
        :param Key: **[REQUIRED]**

          The key name for the object whose Legal Hold status you want to retrieve.

        :type VersionId: string
        :param VersionId:

          The version ID of the object whose Legal Hold status you want to retrieve.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LegalHold': {
                    'Status': 'ON'|'OFF'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **LegalHold** *(dict) --*

              The current Legal Hold status for the specified object.

              - **Status** *(string) --*

                Indicates whether the specified object has a Legal Hold in place.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_object_lock_configuration(
        self, Bucket: str
    ) -> ClientGetObjectLockConfigurationResponseTypeDef:
        """
        Gets the Object Lock configuration for a bucket. The rule specified in the Object Lock
        configuration will be applied by default to every new object placed in the specified bucket. For
        more information, see `Locking Objects
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectLockConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_object_lock_configuration(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket whose Object Lock configuration you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ObjectLockConfiguration': {
                    'ObjectLockEnabled': 'Enabled',
                    'Rule': {
                        'DefaultRetention': {
                            'Mode': 'GOVERNANCE'|'COMPLIANCE',
                            'Days': 123,
                            'Years': 123
                        }
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ObjectLockConfiguration** *(dict) --*

              The specified bucket's Object Lock configuration.

              - **ObjectLockEnabled** *(string) --*

                Indicates whether this bucket has an Object Lock configuration enabled.

              - **Rule** *(dict) --*

                The Object Lock rule in place for the specified object.

                - **DefaultRetention** *(dict) --*

                  The default retention period that you want to apply to new objects placed in the
                  specified bucket.

                  - **Mode** *(string) --*

                    The default Object Lock retention mode you want to apply to new objects placed in the
                    specified bucket.

                  - **Days** *(integer) --*

                    The number of days that you want to specify for the default retention period.

                  - **Years** *(integer) --*

                    The number of years that you want to specify for the default retention period.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_object_retention(
        self, Bucket: str, Key: str, VersionId: str = None, RequestPayer: str = None
    ) -> ClientGetObjectRetentionResponseTypeDef:
        """
        Retrieves an object's retention settings. For more information, see `Locking Objects
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectRetention>`_

        **Request Syntax**
        ::

          response = client.get_object_retention(
              Bucket='string',
              Key='string',
              VersionId='string',
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket containing the object whose retention settings you want to retrieve.

        :type Key: string
        :param Key: **[REQUIRED]**

          The key name for the object whose retention settings you want to retrieve.

        :type VersionId: string
        :param VersionId:

          The version ID for the object whose retention settings you want to retrieve.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Retention': {
                    'Mode': 'GOVERNANCE'|'COMPLIANCE',
                    'RetainUntilDate': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Retention** *(dict) --*

              The container element for an object's retention settings.

              - **Mode** *(string) --*

                Indicates the Retention mode for the specified object.

              - **RetainUntilDate** *(datetime) --*

                The date on which this Object Lock Retention will expire.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_object_tagging(
        self, Bucket: str, Key: str, VersionId: str = None
    ) -> ClientGetObjectTaggingResponseTypeDef:
        """
        Returns the tag-set of an object. You send the GET request against the tagging subresource
        associated with the object.

        To use this operation, you must have permission to perform the ``s3:GetObjectTagging`` action. By
        default, the GET operation returns information about current version of an object. For a versioned
        bucket, you can have multiple versions of an object in your bucket. To retrieve tags of any other
        version, use the versionId query parameter. You also need permission for the
        ``s3:GetObjectVersionTagging`` action.

        By default, the bucket owner has this permission and can grant this permission to others.

        For information about the Amazon S3 object tagging feature, see `Object Tagging
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html>`__ .

        The following operation is related to ``GetObjectTagging`` :

        *  PutObjectTagging

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectTagging>`_

        **Request Syntax**
        ::

          response = client.get_object_tagging(
              Bucket='string',
              Key='string',
              VersionId='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name containing the object for which to get the tagging information.

        :type Key: string
        :param Key: **[REQUIRED]**

          Object key for which to get the tagging information.

        :type VersionId: string
        :param VersionId:

          The versionId of the object for which to get the tagging information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VersionId': 'string',
                'TagSet': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **VersionId** *(string) --*

              The versionId of the object for which you got the tagging information.

            - **TagSet** *(list) --*

              Contains the tag set.

              - *(dict) --*

                A container of a key value name pair.

                - **Key** *(string) --*

                  Name of the tag.

                - **Value** *(string) --*

                  Value of the tag.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_object_torrent(
        self, Bucket: str, Key: str, RequestPayer: str = None
    ) -> ClientGetObjectTorrentResponseTypeDef:
        """
        Return torrent files from a bucket. BitTorrent can save you bandwidth when you're distributing
        large files. For more information about BitTorrent, see `Amazon S3 Torrent
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/S3Torrent.html>`__ .

        .. note::

          You can get torrent only for objects that are less than 5 GB in size and that are not encrypted
          using server-side encryption with customer-provided encryption key.

        To use GET, you must have READ access to the object.

        The following operation is related to ``GetObjectTorrent`` :

        *  GetObject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetObjectTorrent>`_

        **Request Syntax**
        ::

          response = client.get_object_torrent(
              Bucket='string',
              Key='string',
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the object for which to get the torrent files.

        :type Key: string
        :param Key: **[REQUIRED]**

          The object key for which to get the information.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Body': StreamingBody(),
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **Body** (:class:`.StreamingBody`) --

              A Bencoded dictionary as defined by the BitTorrent specification

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_public_access_block(
        self, Bucket: str
    ) -> ClientGetPublicAccessBlockResponseTypeDef:
        """
        Retrieves the ``PublicAccessBlock`` configuration for an Amazon S3 bucket. In order to use this
        operation, you must have the ``s3:GetBucketPublicAccessBlock`` permission. For more information
        about Amazon S3 permissions, see `Specifying Permissions in a Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html>`__ .

        .. warning::

          When Amazon S3 evaluates the ``PublicAccessBlock`` configuration for a bucket or an object, it
          checks the ``PublicAccessBlock`` configuration for both the bucket (or the bucket that contains
          the object) and the bucket owner's account. If the ``PublicAccessBlock`` settings are different
          between the bucket and the account, Amazon S3 uses the most restrictive combination of the
          bucket-level and account-level settings.

        For more information about when Amazon S3 considers a bucket or an object public, see `The Meaning
        of "Public"
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status>`__
        .

        The following operations are related to ``GetPublicAccessBlock`` :

        * `Using Amazon S3 Block Public Access
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html>`__

        *  PutPublicAccessBlock

        *  GetPublicAccessBlock

        *  DeletePublicAccessBlock

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/GetPublicAccessBlock>`_

        **Request Syntax**
        ::

          response = client.get_public_access_block(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the Amazon S3 bucket whose ``PublicAccessBlock`` configuration you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PublicAccessBlockConfiguration': {
                    'BlockPublicAcls': True|False,
                    'IgnorePublicAcls': True|False,
                    'BlockPublicPolicy': True|False,
                    'RestrictPublicBuckets': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **PublicAccessBlockConfiguration** *(dict) --*

              The ``PublicAccessBlock`` configuration currently in effect for this Amazon S3 bucket.

              - **BlockPublicAcls** *(boolean) --*

                Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket
                and objects in this bucket. Setting this element to ``TRUE`` causes the following behavior:

                * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.

                * PUT Object calls fail if the request includes a public ACL.

                * PUT Bucket calls fail if the request includes a public ACL.

                Enabling this setting doesn't affect existing policies or ACLs.

              - **IgnorePublicAcls** *(boolean) --*

                Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this
                bucket. Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on this
                bucket and objects in this bucket.

                Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't
                prevent new public ACLs from being set.

              - **BlockPublicPolicy** *(boolean) --*

                Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting
                this element to ``TRUE`` causes Amazon S3 to reject calls to PUT Bucket policy if the
                specified bucket policy allows public access.

                Enabling this setting doesn't affect existing bucket policies.

              - **RestrictPublicBuckets** *(boolean) --*

                Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting
                this element to ``TRUE`` restricts access to this bucket to only AWS services and
                authorized users within this account if the bucket has a public policy.

                Enabling this setting doesn't affect previously stored bucket policies, except that public
                and cross-account access within any public bucket policy, including non-public delegation
                to specific accounts, is blocked.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def head_bucket(self, Bucket: str) -> None:
        """
        This operation is useful to determine if a bucket exists and you have permission to access it. The
        operation returns a ``200 OK`` if the bucket exists and you have permission to access it.
        Otherwise, the operation might return responses such as ``404 Not Found`` and ``403 Forbidden`` .

        To use this operation, you must have permissions to perform the ``s3:ListBucket`` action. The
        bucket owner has this permission by default and can grant this permission to others. For more
        information about permissions, see `Permissions Related to Bucket Subresource Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadBucket>`_

        **Request Syntax**
        ::

          response = client.head_bucket(
              Bucket='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def head_object(
        self,
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
    ) -> ClientHeadObjectResponseTypeDef:
        """
        The HEAD operation retrieves metadata from an object without returning the object itself. This
        operation is useful if you're only interested in an object's metadata. To use HEAD, you must have
        READ access to the object.

        A ``HEAD`` request has the same options as a ``GET`` operation on an object. The response is
        identical to the ``GET`` response except that there is no response body.

        If you encrypt an object by using server-side encryption with customer-provided encryption keys
        (SSE-C) when you store the object in Amazon S3, then when you retrieve the metadata from the
        object, you must use the following headers:

        * x-amz-server-side​-encryption​-customer-algorithm

        * x-amz-server-side​-encryption​-customer-key

        * x-amz-server-side​-encryption​-customer-key-MD5

        For more information about SSE-C, see `Server-Side Encryption (Using Customer-Provided Encryption
        Keys) <https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html>`__ .

        .. note::

          Encryption request headers, like ``x-amz-server-side-encryption`` , should not be sent for GET
          requests if your object uses server-side encryption with CMKs stored in AWS KMS (SSE-KMS) or
          server-side encryption with Amazon S3–managed encryption keys (SSE-S3). If your object does use
          these types of keys, you’ll get an HTTP 400 BadRequest error.

        Request headers are limited to 8 KB in size. For more information, see `Common Request Headers
        <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonRequestHeaders.html>`__ .

        Consider the following when using request headers:

        * Consideration 1 – If both of the ``If-Match`` and ``If-Unmodified-Since`` headers are present in
        the request as follows:

          * ``If-Match`` condition evaluates to ``true`` , and;

          * ``If-Unmodified-Since`` condition evaluates to ``false`` ;

        Then Amazon S3 returns ``200 OK`` and the data requested.

        * Consideration 2 – If both of the ``If-None-Match`` and ``If-Modified-Since`` headers are present
        in the request as follows:

          * ``If-None-Match`` condition evaluates to ``false`` , and;

          * ``If-Modified-Since`` condition evaluates to ``true`` ;

        Then Amazon S3 returns the ``304 Not Modified`` response code.

        For more information about conditional requests, see `RFC 7232
        <https://tools.ietf.org/html/rfc7232>`__ .

         **Permissions**

        You need the ``s3:GetObject`` permission for this operation. For more information, see `Specifying
        Permissions in a Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html>`__ . If the object you
        request does not exist, the error Amazon S3 returns depends on whether you also have the
        s3:ListBucket permission.

        * If you have the ``s3:ListBucket`` permission on the bucket, Amazon S3 will return a HTTP status
        code 404 ("no such key") error.

        * If you don’t have the ``s3:ListBucket`` permission, Amazon S3 will return a HTTP status code 403
        ("access denied") error.

        The following operation is related to ``HeadObject`` :

        *  GetObject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/HeadObject>`_

        **Request Syntax**
        ::

          response = client.head_object(
              Bucket='string',
              IfMatch='string',
              IfModifiedSince=datetime(2015, 1, 1),
              IfNoneMatch='string',
              IfUnmodifiedSince=datetime(2015, 1, 1),
              Key='string',
              Range='string',
              VersionId='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              RequestPayer='requester',
              PartNumber=123
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the object.

        :type IfMatch: string
        :param IfMatch:

          Return the object only if its entity tag (ETag) is the same as the one specified, otherwise
          return a 412 (precondition failed).

        :type IfModifiedSince: datetime
        :param IfModifiedSince:

          Return the object only if it has been modified since the specified time, otherwise return a 304
          (not modified).

        :type IfNoneMatch: string
        :param IfNoneMatch:

          Return the object only if its entity tag (ETag) is different from the one specified, otherwise
          return a 304 (not modified).

        :type IfUnmodifiedSince: datetime
        :param IfUnmodifiedSince:

          Return the object only if it has not been modified since the specified time, otherwise return a
          412 (precondition failed).

        :type Key: string
        :param Key: **[REQUIRED]**

          The object key.

        :type Range: string
        :param Range:

          Downloads the specified range bytes of an object. For more information about the HTTP Range
          header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.

        :type VersionId: string
        :param VersionId:

          VersionId used to reference a specific version of the object.

        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:

          Specifies the algorithm to use to when encrypting the object (e.g., AES256).

        :type SSECustomerKey: string
        :param SSECustomerKey:

          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This
          value is used to store the object and then it is discarded; Amazon does not store the encryption
          key. The key must be appropriate for use with the algorithm specified in the
          x-amz-server-side​-encryption​-customer-algorithm header.

        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:

          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this
          header for a message integrity check to ensure the encryption key was transmitted without error.

            Please note that this parameter is automatically populated if it is not provided. Including
            this parameter is not required

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type PartNumber: integer
        :param PartNumber:

          Part number of the object being read. This is a positive integer between 1 and 10,000.
          Effectively performs a 'ranged' HEAD request for the part specified. Useful querying about the
          size of the part and the number of parts in this object.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DeleteMarker': True|False,
                'AcceptRanges': 'string',
                'Expiration': 'string',
                'Restore': 'string',
                'LastModified': datetime(2015, 1, 1),
                'ContentLength': 123,
                'ETag': 'string',
                'MissingMeta': 123,
                'VersionId': 'string',
                'CacheControl': 'string',
                'ContentDisposition': 'string',
                'ContentEncoding': 'string',
                'ContentLanguage': 'string',
                'ContentType': 'string',
                'Expires': datetime(2015, 1, 1),
                'WebsiteRedirectLocation': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'Metadata': {
                    'string': 'string'
                },
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'StorageClass':
                'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'
                |'DEEP_ARCHIVE',
                'RequestCharged': 'requester',
                'ReplicationStatus': 'COMPLETE'|'PENDING'|'FAILED'|'REPLICA',
                'PartsCount': 123,
                'ObjectLockMode': 'GOVERNANCE'|'COMPLIANCE',
                'ObjectLockRetainUntilDate': datetime(2015, 1, 1),
                'ObjectLockLegalHoldStatus': 'ON'|'OFF'
            }
          **Response Structure**

          - *(dict) --*

            - **DeleteMarker** *(boolean) --*

              Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If
              false, this response header does not appear in the response.

            - **AcceptRanges** *(string) --*

              Indicates that a range of bytes was specifed.

            - **Expiration** *(string) --*

              If the object expiration is configured (see PUT Bucket lifecycle), the response includes this
              header. It includes the expiry-date and rule-id key value pairs providing object expiration
              information. The value of the rule-id is URL encoded.

            - **Restore** *(string) --*

              If the object is an archived object (an object whose storage class is GLACIER), the response
              includes this header if either the archive restoration is in progress (see  RestoreObject or
              an archive copy is already restored.

              If an archive copy is already restored, the header value indicates when Amazon S3 is
              scheduled to delete the object copy. For example:

               ``x-amz-restore: ongoing-request="false", expiry-date="Fri, 23 Dec 2012 00:00:00 GMT"``

              If the object restoration is in progress, the header returns the value
              ``ongoing-request="true"`` .

              For more information about archiving objects, see `Transitioning Objects\\: General
              Considerations
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html#lifecycle-transition-general-considerations>`__
              .

            - **LastModified** *(datetime) --*

              Last modified date of the object

            - **ContentLength** *(integer) --*

              Size of the body in bytes.

            - **ETag** *(string) --*

              An ETag is an opaque identifier assigned by a web server to a specific version of a resource
              found at a URL

            - **MissingMeta** *(integer) --*

              This is set to the number of metadata entries not returned in x-amz-meta headers. This can
              happen if you create metadata using an API like SOAP that supports more flexible metadata
              than the REST API. For example, using SOAP, you can create metadata whose values are not
              legal HTTP headers.

            - **VersionId** *(string) --*

              Version of the object.

            - **CacheControl** *(string) --*

              Specifies caching behavior along the request/reply chain.

            - **ContentDisposition** *(string) --*

              Specifies presentational information for the object.

            - **ContentEncoding** *(string) --*

              Specifies what content encodings have been applied to the object and thus what decoding
              mechanisms must be applied to obtain the media-type referenced by the Content-Type header
              field.

            - **ContentLanguage** *(string) --*

              The language the content is in.

            - **ContentType** *(string) --*

              A standard MIME type describing the format of the object data.

            - **Expires** *(datetime) --*

              The date and time at which the object is no longer cacheable.

            - **WebsiteRedirectLocation** *(string) --*

              If the bucket is configured as a website, redirects requests for this object to another
              object in the same bucket or to an external URL. Amazon S3 stores the value of this header in
              the object metadata.

            - **ServerSideEncryption** *(string) --*

              If the object is stored using server-side encryption either with an AWS KMS customer master
              key (CMK) or an Amazon S3-managed encryption key, the response includes this header with the
              value of the Server-side encryption algorithm used when storing this object in S3 (e.g.,
              AES256, aws:kms).

            - **Metadata** *(dict) --*

              A map of metadata to store with the object in S3.

              - *(string) --*

                - *(string) --*

            - **SSECustomerAlgorithm** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header confirming the encryption algorithm used.

            - **SSECustomerKeyMD5** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header to provide round trip message integrity verification of the
              customer-provided encryption key.

            - **SSEKMSKeyId** *(string) --*

              If present, specifies the ID of the AWS Key Management Service (KMS) customer master key
              (CMK) that was used for the object.

            - **StorageClass** *(string) --*

              Provides storage class information of the object. Amazon S3 returns this header for all
              objects except for Standard storage class objects.

              For more information, see `Storage Classes
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html>`__ .

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

            - **ReplicationStatus** *(string) --*

              Amazon S3 can return this header if your request involves a bucket that is either a source or
              destination in a replication rule.

              In replication you have a source bucket on which you configure replication and destination
              bucket where Amazon S3 stores object replicas. When you request an object (GetObject) or
              object metadata (HeadObject) from these buckets, Amazon S3 will return the
              x-amz-replication-status header in the response as follows:

              * If requesting object from the source bucket — Amazon S3 will return the
              x-amz-replication-status header if object in your request is eligible for replication. For
              example, suppose in your replication configuration you specify object prefix "TaxDocs"
              requesting Amazon S3 to replicate objects with key prefix "TaxDocs". Then any objects you
              upload with this key name prefix, for example "TaxDocs/document1.pdf", is eligible for
              replication. For any object request with this key name prefix Amazon S3 will return the
              x-amz-replication-status header with value PENDING, COMPLETED or FAILED indicating object
              replication status.

              * If requesting object from the destination bucket — Amazon S3 will return the
              x-amz-replication-status header with value REPLICA if object in your request is a replica
              that Amazon S3 created.

              For more information, see `Replication
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ .

            - **PartsCount** *(integer) --*

              The count of parts this object has.

            - **ObjectLockMode** *(string) --*

              The Object Lock mode, if any, that's in effect for this object. This header is only returned
              if the requester has the ``s3:GetObjectRetention`` permission. For more information about S3
              Object Lock, see `Object Lock
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`__ .

            - **ObjectLockRetainUntilDate** *(datetime) --*

              The date and time when the Object Lock retention period expires. This header is only returned
              if the requester has the ``s3:GetObjectRetention`` permission.

            - **ObjectLockLegalHoldStatus** *(string) --*

              Specifies whether a legal hold is in effect for this object. This header is only returned if
              the requester has the ``s3:GetObjectLegalHold`` permission. This header is not returned if
              the specified version of this object has never had a legal hold applied. For more information
              about S3 Object Lock, see `Object Lock
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`__ .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bucket_analytics_configurations(
        self, Bucket: str, ContinuationToken: str = None
    ) -> ClientListBucketAnalyticsConfigurationsResponseTypeDef:
        """
        Lists the analytics configurations for the bucket. You can have up to 1,000 analytics
        configurations per bucket.

        This operation supports list pagination and does not return more than 100 configurations at a time.
        You should always check the ``IsTruncated`` element in the response. If there are no more
        configurations to list, ``IsTruncated`` is set to false. If there are more configurations to list,
        ``IsTruncated`` is set to true, and there will be a value in ``NextContinuationToken`` . You use
        the ``NextContinuationToken`` value to continue the pagination of the list by passing the value in
        continuation-token in the request to ``GET`` the next page.

        To use this operation, you must have permissions to perform the ``s3:GetAnalyticsConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        For information about Amazon S3 analytics feature, see `Amazon S3 Analytics – Storage Class
        Analysis <https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html>`__ .

        The following operations are related to ``ListBucketAnalyticsConfigurations`` :

        *  GetBucketAnalyticsConfiguration

        *  DeleteBucketAnalyticsConfiguration

        *  PutBucketAnalyticsConfiguration

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBucketAnalyticsConfigurations>`_

        **Request Syntax**
        ::

          response = client.list_bucket_analytics_configurations(
              Bucket='string',
              ContinuationToken='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket from which analytics configurations are retrieved.

        :type ContinuationToken: string
        :param ContinuationToken:

          The ContinuationToken that represents a placeholder from where this request should begin.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IsTruncated': True|False,
                'ContinuationToken': 'string',
                'NextContinuationToken': 'string',
                'AnalyticsConfigurationList': [
                    {
                        'Id': 'string',
                        'Filter': {
                            'Prefix': 'string',
                            'Tag': {
                                'Key': 'string',
                                'Value': 'string'
                            },
                            'And': {
                                'Prefix': 'string',
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        },
                        'StorageClassAnalysis': {
                            'DataExport': {
                                'OutputSchemaVersion': 'V_1',
                                'Destination': {
                                    'S3BucketDestination': {
                                        'Format': 'CSV',
                                        'BucketAccountId': 'string',
                                        'Bucket': 'string',
                                        'Prefix': 'string'
                                    }
                                }
                            }
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **IsTruncated** *(boolean) --*

              Indicates whether the returned list of analytics configurations is complete. A value of true
              indicates that the list is not complete and the NextContinuationToken will be provided for a
              subsequent request.

            - **ContinuationToken** *(string) --*

              The marker that is used as a starting point for this analytics configuration list response.
              This value is present if it was sent in the request.

            - **NextContinuationToken** *(string) --*

              NextContinuationToken is sent when isTruncated is true, which indicates that there are more
              analytics configurations to list. The next request must include this NextContinuationToken.
              The token is obfuscated and is not a usable value.

            - **AnalyticsConfigurationList** *(list) --*

              The list of analytics configurations for a bucket.

              - *(dict) --*

                Specifies the configuration and any analyses for the analytics filter of an Amazon S3
                bucket.

                - **Id** *(string) --*

                  The ID that identifies the analytics configuration.

                - **Filter** *(dict) --*

                  The filter used to describe a set of objects for analyses. A filter must have exactly one
                  prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all
                  objects will be considered in any analysis.

                  - **Prefix** *(string) --*

                    The prefix to use when evaluating an analytics filter.

                  - **Tag** *(dict) --*

                    The tag to use when evaluating an analytics filter.

                    - **Key** *(string) --*

                      Name of the tag.

                    - **Value** *(string) --*

                      Value of the tag.

                  - **And** *(dict) --*

                    A conjunction (logical AND) of predicates, which is used in evaluating an analytics
                    filter. The operator must have at least two predicates.

                    - **Prefix** *(string) --*

                      The prefix to use when evaluating an AND predicate: The prefix that an object must
                      have to be included in the metrics results.

                    - **Tags** *(list) --*

                      The list of tags to use when evaluating an AND predicate.

                      - *(dict) --*

                        A container of a key value name pair.

                        - **Key** *(string) --*

                          Name of the tag.

                        - **Value** *(string) --*

                          Value of the tag.

                - **StorageClassAnalysis** *(dict) --*

                  Contains data related to access patterns to be collected and made available to analyze
                  the tradeoffs between different storage classes.

                  - **DataExport** *(dict) --*

                    Specifies how data related to the storage class analysis for an Amazon S3 bucket should
                    be exported.

                    - **OutputSchemaVersion** *(string) --*

                      The version of the output schema to use when exporting data. Must be ``V_1`` .

                    - **Destination** *(dict) --*

                      The place to store the data for an analysis.

                      - **S3BucketDestination** *(dict) --*

                        A destination signifying output to an S3 bucket.

                        - **Format** *(string) --*

                          Specifies the file format used when exporting data to Amazon S3.

                        - **BucketAccountId** *(string) --*

                          The account ID that owns the destination bucket. If no account ID is provided,
                          the owner will not be validated prior to exporting data.

                        - **Bucket** *(string) --*

                          The Amazon Resource Name (ARN) of the bucket to which data is exported.

                        - **Prefix** *(string) --*

                          The prefix to use when exporting data. The prefix is prepended to all results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bucket_inventory_configurations(
        self, Bucket: str, ContinuationToken: str = None
    ) -> ClientListBucketInventoryConfigurationsResponseTypeDef:
        """
        Returns a list of inventory configurations for the bucket. You can have up to 1,000 analytics
        configurations per bucket.

        This operation supports list pagination and does not return more than 100 configurations at a time.
        Always check the ``IsTruncated`` element in the response. If there are no more configurations to
        list, ``IsTruncated`` is set to false. If there are more configurations to list, ``IsTruncated`` is
        set to true, and there is a value in ``NextContinuationToken`` . You use the
        ``NextContinuationToken`` value to continue the pagination of the list by passing the value in
        continuation-token in the request to ``GET`` the next page.

        To use this operation, you must have permissions to perform the ``s3:GetInventoryConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        For information about the Amazon S3 inventory feature, see `Amazon S3 Inventory
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html>`__

        The following operations are related to ``ListBucketInventoryConfigurations`` :

        *  GetBucketInventoryConfiguration

        *  DeleteBucketInventoryConfiguration

        *  PutBucketInventoryConfiguration

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBucketInventoryConfigurations>`_

        **Request Syntax**
        ::

          response = client.list_bucket_inventory_configurations(
              Bucket='string',
              ContinuationToken='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the inventory configurations to retrieve.

        :type ContinuationToken: string
        :param ContinuationToken:

          The marker used to continue an inventory configuration listing that has been truncated. Use the
          NextContinuationToken from a previously truncated list response to continue the listing. The
          continuation token is an opaque value that Amazon S3 understands.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ContinuationToken': 'string',
                'InventoryConfigurationList': [
                    {
                        'Destination': {
                            'S3BucketDestination': {
                                'AccountId': 'string',
                                'Bucket': 'string',
                                'Format': 'CSV'|'ORC'|'Parquet',
                                'Prefix': 'string',
                                'Encryption': {
                                    'SSES3': {},
                                    'SSEKMS': {
                                        'KeyId': 'string'
                                    }
                                }
                            }
                        },
                        'IsEnabled': True|False,
                        'Filter': {
                            'Prefix': 'string'
                        },
                        'Id': 'string',
                        'IncludedObjectVersions': 'All'|'Current',
                        'OptionalFields': [
                            'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'
                            |'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'
                            |'ObjectLockMode'|'ObjectLockLegalHoldStatus'|'IntelligentTieringAccessTier',
                        ],
                        'Schedule': {
                            'Frequency': 'Daily'|'Weekly'
                        }
                    },
                ],
                'IsTruncated': True|False,
                'NextContinuationToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ContinuationToken** *(string) --*

              If sent in the request, the marker that is used as a starting point for this inventory
              configuration list response.

            - **InventoryConfigurationList** *(list) --*

              The list of inventory configurations for a bucket.

              - *(dict) --*

                Specifies the inventory configuration for an Amazon S3 bucket. For more information, see
                `GET Bucket inventory
                <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETInventoryConfig.html>`__ in
                the *Amazon Simple Storage Service API Reference* .

                - **Destination** *(dict) --*

                  Contains information about where to publish the inventory results.

                  - **S3BucketDestination** *(dict) --*

                    Contains the bucket name, file format, bucket owner (optional), and prefix (optional)
                    where inventory results are published.

                    - **AccountId** *(string) --*

                      The ID of the account that owns the destination bucket.

                    - **Bucket** *(string) --*

                      The Amazon resource name (ARN) of the bucket where inventory results will be
                      published.

                    - **Format** *(string) --*

                      Specifies the output format of the inventory results.

                    - **Prefix** *(string) --*

                      The prefix that is prepended to all inventory results.

                    - **Encryption** *(dict) --*

                      Contains the type of server-side encryption used to encrypt the inventory results.

                      - **SSES3** *(dict) --*

                        Specifies the use of SSE-S3 to encrypt delivered Inventory reports.

                      - **SSEKMS** *(dict) --*

                        Specifies the use of SSE-KMS to encrypt delivered Inventory reports.

                        - **KeyId** *(string) --*

                          Specifies the ID of the AWS Key Management Service (KMS) customer master key
                          (CMK) to use for encrypting Inventory reports.

                - **IsEnabled** *(boolean) --*

                  Specifies whether the inventory is enabled or disabled. If set to ``True`` , an inventory
                  list is generated. If set to ``False`` , no inventory list is generated.

                - **Filter** *(dict) --*

                  Specifies an inventory filter. The inventory only includes objects that meet the filter's
                  criteria.

                  - **Prefix** *(string) --*

                    The prefix that an object must have to be included in the inventory results.

                - **Id** *(string) --*

                  The ID used to identify the inventory configuration.

                - **IncludedObjectVersions** *(string) --*

                  Object versions to include in the inventory list. If set to ``All`` , the list includes
                  all the object versions, which adds the version-related fields ``VersionId`` ,
                  ``IsLatest`` , and ``DeleteMarker`` to the list. If set to ``Current`` , the list does
                  not contain these version-related fields.

                - **OptionalFields** *(list) --*

                  Contains the optional fields that are included in the inventory results.

                  - *(string) --*

                - **Schedule** *(dict) --*

                  Specifies the schedule for generating inventory results.

                  - **Frequency** *(string) --*

                    Specifies how frequently inventory results are produced.

            - **IsTruncated** *(boolean) --*

              Tells whether the returned list of inventory configurations is complete. A value of true
              indicates that the list is not complete and the NextContinuationToken is provided for a
              subsequent request.

            - **NextContinuationToken** *(string) --*

              The marker used to continue this inventory configuration listing. Use the
              NextContinuationToken from this response to continue the listing in a subsequent request. The
              continuation token is an opaque value that Amazon S3 understands.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bucket_metrics_configurations(
        self, Bucket: str, ContinuationToken: str = None
    ) -> ClientListBucketMetricsConfigurationsResponseTypeDef:
        """
        Lists the metrics configurations for the bucket. The metrics configurations are only for the
        request metrics of the bucket and do not provide information on daily storage metrics. You can have
        up to 1,000 configurations per bucket.

        This operation supports list pagination and does not return more than 100 configurations at a time.
        Always check the ``IsTruncated`` element in the response. If there are no more configurations to
        list, ``IsTruncated`` is set to false. If there are more configurations to list, ``IsTruncated`` is
        set to true, and there is a value in ``NextContinuationToken`` . You use the
        ``NextContinuationToken`` value to continue the pagination of the list by passing the value in
        ``continuation-token`` in the request to ``GET`` the next page.

        To use this operation, you must have permissions to perform the ``s3:GetMetricsConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        For more information about metrics configurations and CloudWatch request metrics, see `Monitoring
        Metrics with Amazon CloudWatch
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html>`__ .

        The following operations are related to ``ListBucketMetricsConfigurations`` :

        *  PutBucketMetricsConfiguration

        *  GetBucketMetricsConfiguration

        *  DeleteBucketMetricsConfiguration

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBucketMetricsConfigurations>`_

        **Request Syntax**
        ::

          response = client.list_bucket_metrics_configurations(
              Bucket='string',
              ContinuationToken='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the metrics configurations to retrieve.

        :type ContinuationToken: string
        :param ContinuationToken:

          The marker that is used to continue a metrics configuration listing that has been truncated. Use
          the NextContinuationToken from a previously truncated list response to continue the listing. The
          continuation token is an opaque value that Amazon S3 understands.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IsTruncated': True|False,
                'ContinuationToken': 'string',
                'NextContinuationToken': 'string',
                'MetricsConfigurationList': [
                    {
                        'Id': 'string',
                        'Filter': {
                            'Prefix': 'string',
                            'Tag': {
                                'Key': 'string',
                                'Value': 'string'
                            },
                            'And': {
                                'Prefix': 'string',
                                'Tags': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **IsTruncated** *(boolean) --*

              Indicates whether the returned list of metrics configurations is complete. A value of true
              indicates that the list is not complete and the NextContinuationToken will be provided for a
              subsequent request.

            - **ContinuationToken** *(string) --*

              The marker that is used as a starting point for this metrics configuration list response.
              This value is present if it was sent in the request.

            - **NextContinuationToken** *(string) --*

              The marker used to continue a metrics configuration listing that has been truncated. Use the
              NextContinuationToken from a previously truncated list response to continue the listing. The
              continuation token is an opaque value that Amazon S3 understands.

            - **MetricsConfigurationList** *(list) --*

              The list of metrics configurations for a bucket.

              - *(dict) --*

                Specifies a metrics configuration for the CloudWatch request metrics (specified by the
                metrics configuration ID) from an Amazon S3 bucket. If you're updating an existing metrics
                configuration, note that this is a full replacement of the existing metrics configuration.
                If you don't include the elements you want to keep, they are erased. For more information,
                see `PUT Bucket metrics
                <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTMetricConfiguration.html>`__
                in the *Amazon Simple Storage Service API Reference* .

                - **Id** *(string) --*

                  The ID used to identify the metrics configuration.

                - **Filter** *(dict) --*

                  Specifies a metrics configuration filter. The metrics configuration will only include
                  objects that meet the filter's criteria. A filter must be a prefix, a tag, or a
                  conjunction (MetricsAndOperator).

                  - **Prefix** *(string) --*

                    The prefix used when evaluating a metrics filter.

                  - **Tag** *(dict) --*

                    The tag used when evaluating a metrics filter.

                    - **Key** *(string) --*

                      Name of the tag.

                    - **Value** *(string) --*

                      Value of the tag.

                  - **And** *(dict) --*

                    A conjunction (logical AND) of predicates, which is used in evaluating a metrics
                    filter. The operator must have at least two predicates, and an object must match all of
                    the predicates in order for the filter to apply.

                    - **Prefix** *(string) --*

                      The prefix used when evaluating an AND predicate.

                    - **Tags** *(list) --*

                      The list of tags used when evaluating an AND predicate.

                      - *(dict) --*

                        A container of a key value name pair.

                        - **Key** *(string) --*

                          Name of the tag.

                        - **Value** *(string) --*

                          Value of the tag.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_buckets(
        self, *args: Any, **kwargs: Any
    ) -> ClientListBucketsResponseTypeDef:
        """
        Returns a list of all buckets owned by the authenticated sender of the request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListBuckets>`_

        **Request Syntax**

        ::

          response = client.list_buckets()
        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Buckets': [
                    {
                        'Name': 'string',
                        'CreationDate': datetime(2015, 1, 1)
                    },
                ],
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Buckets** *(list) --*

              The list of buckets owned by the requestor.

              - *(dict) --*

                In terms of implementation, a Bucket is a resource. An Amazon S3 bucket name is globally
                unique, and the namespace is shared by all AWS accounts.

                - **Name** *(string) --*

                  The name of the bucket.

                - **CreationDate** *(datetime) --*

                  Date the bucket was created.

            - **Owner** *(dict) --*

              The owner of the buckets listed.

              - **DisplayName** *(string) --*

                Container for the display name of the owner

              - **ID** *(string) --*

                Container for the ID of the owner

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_multipart_uploads(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> ClientListMultipartUploadsResponseTypeDef:
        """
        This operation lists in-progress multipart uploads. An in-progress multipart upload is a multipart
        upload that has been initiated using the Initiate Multipart Upload request, but has not yet been
        completed or aborted.

        This operation returns at most 1,000 multipart uploads in the response. 1,000 multipart uploads is
        the maximum number of uploads a response can include, which is also the default value. You can
        further limit the number of uploads in a response by specifying the ``max-uploads`` parameter in
        the response. If additional multipart uploads satisfy the list criteria, the response will contain
        an ``IsTruncated`` element with the value true. To list the additional multipart uploads, use the
        ``key-marker`` and ``upload-id-marker`` request parameters.

        In the response, the uploads are sorted by key. If your application has initiated more than one
        multipart upload using the same object key, then uploads in the response are first sorted by key.
        Additionally, uploads are sorted in ascending order within each key by the upload initiation time.

        For more information on multipart uploads, see `Uploading Objects Using Multipart Upload
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html>`__ .

        For information on permissions required to use the multipart upload API, see `Multipart Upload API
        and Permissions <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html>`__ .

        The following operations are related to ``ListMultipartUploads`` :

        *  CreateMultipartUpload

        *  UploadPart

        *  CompleteMultipartUpload

        *  ListParts

        *  AbortMultipartUpload

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListMultipartUploads>`_

        **Request Syntax**
        ::

          response = client.list_multipart_uploads(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              KeyMarker='string',
              MaxUploads=123,
              Prefix='string',
              UploadIdMarker='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket to which the multipart upload was initiated.

        :type Delimiter: string
        :param Delimiter:

          Character you use to group keys.

          All keys that contain the same string between the prefix, if specified, and the first occurrence
          of the delimiter after the prefix are grouped under a single result element, ``CommonPrefixes`` .
          If you don't specify the prefix parameter, then the substring starts at the beginning of the key.
          The keys that are grouped under ``CommonPrefixes`` result element are not returned elsewhere in
          the response.

        :type EncodingType: string
        :param EncodingType:

          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to
          use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some
          characters, such as characters with an ASCII value from 0 to 10. For characters that are not
          supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the
          response.

        :type KeyMarker: string
        :param KeyMarker:

          Together with upload-id-marker, this parameter specifies the multipart upload after which listing
          should begin.

          If ``upload-id-marker`` is not specified, only the keys lexicographically greater than the
          specified ``key-marker`` will be included in the list.

          If ``upload-id-marker`` is specified, any multipart uploads for a key equal to the ``key-marker``
          might also be included, provided those multipart uploads have upload IDs lexicographically
          greater than the specified ``upload-id-marker`` .

        :type MaxUploads: integer
        :param MaxUploads:

          Sets the maximum number of multipart uploads, from 1 to 1,000, to return in the response body.
          1,000 is the maximum number of uploads that can be returned in a response.

        :type Prefix: string
        :param Prefix:

          Lists in-progress uploads only for those keys that begin with the specified prefix. You can use
          prefixes to separate a bucket into different grouping of keys. (You can think of using prefix to
          make groups in the same way you'd use a folder in a file system.)

        :type UploadIdMarker: string
        :param UploadIdMarker:

          Together with key-marker, specifies the multipart upload after which listing should begin. If
          key-marker is not specified, the upload-id-marker parameter is ignored. Otherwise, any multipart
          uploads for a key equal to the key-marker might be included in the list only if they have an
          upload ID lexicographically greater than the specified upload-id-marker.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Bucket': 'string',
                'KeyMarker': 'string',
                'UploadIdMarker': 'string',
                'NextKeyMarker': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'NextUploadIdMarker': 'string',
                'MaxUploads': 123,
                'IsTruncated': True|False,
                'Uploads': [
                    {
                        'UploadId': 'string',
                        'Key': 'string',
                        'Initiated': datetime(2015, 1, 1),
                        'StorageClass':
                        'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'
                        |'GLACIER'|'DEEP_ARCHIVE',
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        },
                        'Initiator': {
                            'ID': 'string',
                            'DisplayName': 'string'
                        }
                    },
                ],
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url'
            }
          **Response Structure**

          - *(dict) --*

            - **Bucket** *(string) --*

              Name of the bucket to which the multipart upload was initiated.

            - **KeyMarker** *(string) --*

              The key at or after which the listing began.

            - **UploadIdMarker** *(string) --*

              Upload ID after which listing began.

            - **NextKeyMarker** *(string) --*

              When a list is truncated, this element specifies the value that should be used for the
              key-marker request parameter in a subsequent request.

            - **Prefix** *(string) --*

              When a prefix is provided in the request, this field contains the specified prefix. The
              result contains only keys starting with the specified prefix.

            - **Delimiter** *(string) --*

              Contains the delimiter you specified in the request. If you don't specify a delimiter in your
              request, this element is absent from the response.

            - **NextUploadIdMarker** *(string) --*

              When a list is truncated, this element specifies the value that should be used for the
              upload-id-marker request parameter in a subsequent request.

            - **MaxUploads** *(integer) --*

              Maximum number of multipart uploads that could have been included in the response.

            - **IsTruncated** *(boolean) --*

              Indicates whether the returned list of multipart uploads is truncated. A value of true
              indicates that the list was truncated. The list can be truncated if the number of multipart
              uploads exceeds the limit allowed or specified by max uploads.

            - **Uploads** *(list) --*

              Container for elements related to a particular multipart upload. A response can contain zero
              or more Upload elements.

              - *(dict) --*

                Container for the MultipartUpload for the Amazon S3 object.

                - **UploadId** *(string) --*

                  Upload ID that identifies the multipart upload.

                - **Key** *(string) --*

                  Key of the object for which the multipart upload was initiated.

                - **Initiated** *(datetime) --*

                  Date and time at which the multipart upload was initiated.

                - **StorageClass** *(string) --*

                  The class of storage used to store the object.

                - **Owner** *(dict) --*

                  Specifies the owner of the object that is part of the multipart upload.

                  - **DisplayName** *(string) --*

                    Container for the display name of the owner

                  - **ID** *(string) --*

                    Container for the ID of the owner

                - **Initiator** *(dict) --*

                  Identifies who initiated the multipart upload.

                  - **ID** *(string) --*

                    If the principal is an AWS account, it provides the Canonical User ID. If the principal
                    is an IAM User, it provides a user ARN value.

                  - **DisplayName** *(string) --*

                    Name of the Principal.

            - **CommonPrefixes** *(list) --*

              If you specify a delimiter in the request, then the result returns each distinct key prefix
              containing the delimiter in a CommonPrefixes element. The distinct key prefixes are returned
              in the Prefix child element.

              - *(dict) --*

                Container for all (if there are any) keys between Prefix and the next occurrence of the
                string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in
                the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter
                is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

                - **Prefix** *(string) --*

                  Container for the specified common prefix.

            - **EncodingType** *(string) --*

              Encoding type used by Amazon S3 to encode object keys in the response.

              If you specify ``encoding-type`` request parameter, Amazon S3 includes this element in the
              response, and returns encoded key name values in the following response elements:

               ``Delimiter`` , ``KeyMarker`` , ``Prefix`` , ``NextKeyMarker`` , ``Key`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_object_versions(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        VersionIdMarker: str = None,
    ) -> ClientListObjectVersionsResponseTypeDef:
        """
        Returns metadata about all of the versions of objects in a bucket. You can also use request
        parameters as selection criteria to return metadata about a subset of all the object versions.

        .. note::

          A 200 OK response can contain valid or invalid XML. Make sure to design your application to parse
          the contents of the response and handle it appropriately.

        To use this operation, you must have READ access to the bucket.

        The following operations are related to ``ListObjectVersions`` :

        *  ListObjectsV2

        *  GetObject

        *  PutObject

        *  DeleteObject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjectVersions>`_

        **Request Syntax**
        ::

          response = client.list_object_versions(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              KeyMarker='string',
              MaxKeys=123,
              Prefix='string',
              VersionIdMarker='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket that contains the objects.

        :type Delimiter: string
        :param Delimiter:

          A delimiter is a character that you specify to group keys. All keys that contain the same string
          between the ``prefix`` and the first occurrence of the delimiter are grouped under a single
          result element in CommonPrefixes. These groups are counted as one result against the max-keys
          limitation. These keys are not returned elsewhere in the response.

        :type EncodingType: string
        :param EncodingType:

          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to
          use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some
          characters, such as characters with an ASCII value from 0 to 10. For characters that are not
          supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the
          response.

        :type KeyMarker: string
        :param KeyMarker:

          Specifies the key to start with when listing objects in a bucket.

        :type MaxKeys: integer
        :param MaxKeys:

          Sets the maximum number of keys returned in the response. The response might contain fewer keys
          but will never contain more. If additional keys satisfy the search criteria, but were not
          returned because max-keys was exceeded, the response contains <isTruncated>true</isTruncated>. To
          return the additional keys, see key-marker and version-id-marker.

        :type Prefix: string
        :param Prefix:

          Use this parameter to select only those keys that begin with the specified prefix. You can use
          prefixes to separate a bucket into different groupings of keys. (You can think of using prefix to
          make groups in the same way you'd use a folder in a file system.) You can use prefix with
          delimiter to roll up numerous objects into a single result under CommonPrefixes.

        :type VersionIdMarker: string
        :param VersionIdMarker:

          Specifies the object version you want to start listing from.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IsTruncated': True|False,
                'KeyMarker': 'string',
                'VersionIdMarker': 'string',
                'NextKeyMarker': 'string',
                'NextVersionIdMarker': 'string',
                'Versions': [
                    {
                        'ETag': 'string',
                        'Size': 123,
                        'StorageClass': 'STANDARD',
                        'Key': 'string',
                        'VersionId': 'string',
                        'IsLatest': True|False,
                        'LastModified': datetime(2015, 1, 1),
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        }
                    },
                ],
                'DeleteMarkers': [
                    {
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        },
                        'Key': 'string',
                        'VersionId': 'string',
                        'IsLatest': True|False,
                        'LastModified': datetime(2015, 1, 1)
                    },
                ],
                'Name': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'MaxKeys': 123,
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url'
            }
          **Response Structure**

          - *(dict) --*

            - **IsTruncated** *(boolean) --*

              A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the
              search criteria. If your results were truncated, you can make a follow-up paginated request
              using the NextKeyMarker and NextVersionIdMarker response parameters as a starting place in
              another request to return the rest of the results.

            - **KeyMarker** *(string) --*

              Marks the last Key returned in a truncated response.

            - **VersionIdMarker** *(string) --*

              Marks the last version of the Key returned in a truncated response.

            - **NextKeyMarker** *(string) --*

              When the number of responses exceeds the value of MaxKeys, NextKeyMarker specifies the first
              key not returned that satisfies the search criteria. Use this value for the key-marker
              request parameter in a subsequent request.

            - **NextVersionIdMarker** *(string) --*

              When the number of responses exceeds the value of MaxKeys, NextVersionIdMarker specifies the
              first object version not returned that satisfies the search criteria. Use this value for the
              version-id-marker request parameter in a subsequent request.

            - **Versions** *(list) --*

              Container for version information.

              - *(dict) --*

                The version of an object.

                - **ETag** *(string) --*

                  The entity tag is an MD5 hash of that version of the object

                - **Size** *(integer) --*

                  Size in bytes of the object.

                - **StorageClass** *(string) --*

                  The class of storage used to store the object.

                - **Key** *(string) --*

                  The object key.

                - **VersionId** *(string) --*

                  Version ID of an object.

                - **IsLatest** *(boolean) --*

                  Specifies whether the object is (true) or is not (false) the latest version of an object.

                - **LastModified** *(datetime) --*

                  Date and time the object was last modified.

                - **Owner** *(dict) --*

                  Specifies the Owner of the object.

                  - **DisplayName** *(string) --*

                    Container for the display name of the owner

                  - **ID** *(string) --*

                    Container for the ID of the owner

            - **DeleteMarkers** *(list) --*

              Container for an object that is a delete marker.

              - *(dict) --*

                Information about the delete marker.

                - **Owner** *(dict) --*

                  The account that created the delete marker.>

                  - **DisplayName** *(string) --*

                    Container for the display name of the owner

                  - **ID** *(string) --*

                    Container for the ID of the owner

                - **Key** *(string) --*

                  The object key.

                - **VersionId** *(string) --*

                  Version ID of an object.

                - **IsLatest** *(boolean) --*

                  Specifies whether the object is (true) or is not (false) the latest version of an object.

                - **LastModified** *(datetime) --*

                  Date and time the object was last modified.

            - **Name** *(string) --*

              Bucket owner's name.

            - **Prefix** *(string) --*

              Selects objects that start with the value supplied by this parameter.

            - **Delimiter** *(string) --*

              The delimeter grouping the included keys. A delimiter is a character that you specify to
              group keys. All keys that contain the same string between the prefix and the first occurrence
              of the delimiter are grouped under a single result element in CommonPrefixes. These groups
              are counted as one result against the max-keys limitation. These keys are not returned
              elsewhere in the response.

            - **MaxKeys** *(integer) --*

              Specifies the maximum number of objects to return.

            - **CommonPrefixes** *(list) --*

              All of the keys rolled up into a common prefix count as a single return when calculating the
              number of returns.

              - *(dict) --*

                Container for all (if there are any) keys between Prefix and the next occurrence of the
                string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in
                the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter
                is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

                - **Prefix** *(string) --*

                  Container for the specified common prefix.

            - **EncodingType** *(string) --*

              Encoding type used by Amazon S3 to encode object key names in the XML response.

              If you specify encoding-type request parameter, Amazon S3 includes this element in the
              response, and returns encoded key name values in the following response elements:

               ``KeyMarker, NextKeyMarker, Prefix, Key`` , and ``Delimiter`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_objects(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Marker: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        RequestPayer: str = None,
    ) -> ClientListObjectsResponseTypeDef:
        """
        Returns some or all (up to 1000) of the objects in a bucket. You can use the request parameters as
        selection criteria to return a subset of the objects in a bucket. A 200 OK response can contain
        valid or invalid XML. Be sure to design your application to parse the contents of the response and
        handle it appropriately.

        .. warning::

          This API has been revised. We recommend that you use the newer version,  ListObjectsV2 , when
          developing applications. For backward compatibility, Amazon S3 continues to support
          ``ListObjects`` .

        The following operations are related to ``ListObjects`` :

        *  ListObjectsV2

        *  GetObject

        *  PutObject

        *  CreateBucket

        *  ListBuckets

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjects>`_

        **Request Syntax**
        ::

          response = client.list_objects(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              Marker='string',
              MaxKeys=123,
              Prefix='string',
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the objects.

        :type Delimiter: string
        :param Delimiter:

          A delimiter is a character you use to group keys.

        :type EncodingType: string
        :param EncodingType:

          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to
          use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some
          characters, such as characters with an ASCII value from 0 to 10. For characters that are not
          supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the
          response.

        :type Marker: string
        :param Marker:

          Specifies the key to start with when listing objects in a bucket.

        :type MaxKeys: integer
        :param MaxKeys:

          Sets the maximum number of keys returned in the response. The response might contain fewer keys
          but will never contain more.

        :type Prefix: string
        :param Prefix:

          Limits the response to keys that begin with the specified prefix.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the list objects request.
          Bucket owners need not specify this parameter in their requests.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IsTruncated': True|False,
                'Marker': 'string',
                'NextMarker': 'string',
                'Contents': [
                    {
                        'Key': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'ETag': 'string',
                        'Size': 123,
                        'StorageClass':
                        'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'
                        |'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        }
                    },
                ],
                'Name': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'MaxKeys': 123,
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url'
            }
          **Response Structure**

          - *(dict) --*

            - **IsTruncated** *(boolean) --*

              A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the
              search criteria.

            - **Marker** *(string) --*

              Indicates where in the bucket listing begins. Marker is included in the response if it was
              sent with the request.

            - **NextMarker** *(string) --*

              When response is truncated (the IsTruncated element value in the response is true), you can
              use the key name in this field as marker in the subsequent request to get next set of
              objects. Amazon S3 lists objects in alphabetical order Note: This element is returned only if
              you have delimiter request parameter specified. If response does not include the NextMaker
              and it is truncated, you can use the value of the last Key in the response as the marker in
              the subsequent request to get the next set of object keys.

            - **Contents** *(list) --*

              Metadata about each object returned.

              - *(dict) --*

                An object consists of data and its descriptive metadata.

                - **Key** *(string) --*

                  The name that you assign to an object. You use the object key to retrieve the object.

                - **LastModified** *(datetime) --*

                  The date the Object was Last Modified

                - **ETag** *(string) --*

                  The entity tag is an MD5 hash of the object. ETag reflects only changes to the contents
                  of an object, not its metadata.

                - **Size** *(integer) --*

                  Size in bytes of the object

                - **StorageClass** *(string) --*

                  The class of storage used to store the object.

                - **Owner** *(dict) --*

                  The owner of the object

                  - **DisplayName** *(string) --*

                    Container for the display name of the owner

                  - **ID** *(string) --*

                    Container for the ID of the owner

            - **Name** *(string) --*

              Name of the bucket.

            - **Prefix** *(string) --*

              Keys that begin with the indicated prefix.

            - **Delimiter** *(string) --*

              Causes keys that contain the same string between the prefix and the first occurrence of the
              delimiter to be rolled up into a single result element in the CommonPrefixes collection.
              These rolled-up keys are not returned elsewhere in the response. Each rolled-up result counts
              as only one return against the MaxKeys value.

            - **MaxKeys** *(integer) --*

              The maximum number of keys returned in the response body.

            - **CommonPrefixes** *(list) --*

              All of the keys rolled up in a common prefix count as a single return when calculating the
              number of returns.

              A response can contain CommonPrefixes only if you specify a delimiter.

              CommonPrefixes contains all (if there are any) keys between Prefix and the next occurrence of
              the string specified by the delimiter.

              CommonPrefixes lists keys that act like subdirectories in the directory specified by Prefix.

              For example, if the prefix is notes/ and the delimiter is a slash (/) as in
              notes/summer/july, the common prefix is notes/summer/. All of the keys that roll up into a
              common prefix count as a single return when calculating the number of returns.

              - *(dict) --*

                Container for all (if there are any) keys between Prefix and the next occurrence of the
                string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in
                the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter
                is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

                - **Prefix** *(string) --*

                  Container for the specified common prefix.

            - **EncodingType** *(string) --*

              Encoding type used by Amazon S3 to encode object keys in the response.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_objects_v2(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        MaxKeys: int = None,
        Prefix: str = None,
        ContinuationToken: str = None,
        FetchOwner: bool = None,
        StartAfter: str = None,
        RequestPayer: str = None,
    ) -> ClientListObjectsV2ResponseTypeDef:
        """
        Returns some or all (up to 1,000) of the objects in a bucket. You can use the request parameters as
        selection criteria to return a subset of the objects in a bucket. A ``200 OK`` response can contain
        valid or invalid XML. Make sure to design your application to parse the contents of the response
        and handle it appropriately.

        To use thisoperation, you must have READ access to the bucket.

        To use this operation in an AWS Identity and Access Management (IAM) policy, you must have
        permissions to perform the ``s3:ListBucket`` action. The bucket owner has this permission by
        default and can grant this permission to others. For more information about permissions, see
        `Permissions Related to Bucket Subresource Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        .. warning::

          This section describes the latest revision of the API. We recommend that you use this revised API
          for application development. For backward compatibility, Amazon S3 continues to support the prior
          version of this API,  ListObjects .

        To get a list of your buckets, see  ListBuckets .

        The following operations are related to ``ListObjectsV2`` :

        *  GetObject

        *  PutObject

        *  CreateBucket

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjectsV2>`_

        **Request Syntax**
        ::

          response = client.list_objects_v2(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              MaxKeys=123,
              Prefix='string',
              ContinuationToken='string',
              FetchOwner=True|False,
              StartAfter='string',
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket to list.

        :type Delimiter: string
        :param Delimiter:

          A delimiter is a character you use to group keys.

        :type EncodingType: string
        :param EncodingType:

          Encoding type used by Amazon S3 to encode object keys in the response.

        :type MaxKeys: integer
        :param MaxKeys:

          Sets the maximum number of keys returned in the response. The response might contain fewer keys
          but will never contain more.

        :type Prefix: string
        :param Prefix:

          Limits the response to keys that begin with the specified prefix.

        :type ContinuationToken: string
        :param ContinuationToken:

          ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a
          token. ContinuationToken is obfuscated and is not a real key.

        :type FetchOwner: boolean
        :param FetchOwner:

          The owner field is not present in listV2 by default, if you want to return owner field with each
          key in the result then set the fetch owner field to true

        :type StartAfter: string
        :param StartAfter:

          StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this
          specified key. StartAfter can be any key in the bucket.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the list objects request in
          V2 style. Bucket owners need not specify this parameter in their requests.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IsTruncated': True|False,
                'Contents': [
                    {
                        'Key': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'ETag': 'string',
                        'Size': 123,
                        'StorageClass':
                        'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'
                        |'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        }
                    },
                ],
                'Name': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'MaxKeys': 123,
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url',
                'KeyCount': 123,
                'ContinuationToken': 'string',
                'NextContinuationToken': 'string',
                'StartAfter': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **IsTruncated** *(boolean) --*

              Set to false if all of the results were returned. Set to true if more keys are available to
              return. If the number of results exceeds that specified by MaxKeys, all of the results might
              not be returned.

            - **Contents** *(list) --*

              Metadata about each object returned.

              - *(dict) --*

                An object consists of data and its descriptive metadata.

                - **Key** *(string) --*

                  The name that you assign to an object. You use the object key to retrieve the object.

                - **LastModified** *(datetime) --*

                  The date the Object was Last Modified

                - **ETag** *(string) --*

                  The entity tag is an MD5 hash of the object. ETag reflects only changes to the contents
                  of an object, not its metadata.

                - **Size** *(integer) --*

                  Size in bytes of the object

                - **StorageClass** *(string) --*

                  The class of storage used to store the object.

                - **Owner** *(dict) --*

                  The owner of the object

                  - **DisplayName** *(string) --*

                    Container for the display name of the owner

                  - **ID** *(string) --*

                    Container for the ID of the owner

            - **Name** *(string) --*

              Name of the bucket.

            - **Prefix** *(string) --*

              Keys that begin with the indicated prefix.

            - **Delimiter** *(string) --*

              Causes keys that contain the same string between the prefix and the first occurrence of the
              delimiter to be rolled up into a single result element in the CommonPrefixes collection.
              These rolled-up keys are not returned elsewhere in the response. Each rolled-up result counts
              as only one return against the MaxKeys value.

            - **MaxKeys** *(integer) --*

              Sets the maximum number of keys returned in the response. The response might contain fewer
              keys but will never contain more.

            - **CommonPrefixes** *(list) --*

              All of the keys rolled up into a common prefix count as a single return when calculating the
              number of returns.

              A response can contain ``CommonPrefixes`` only if you specify a delimiter.

               ``CommonPrefixes`` contains all (if there are any) keys between ``Prefix`` and the next
               occurrence of the string specified by a delimiter.

               ``CommonPrefixes`` lists keys that act like subdirectories in the directory specified by
               ``Prefix`` .

              For example, if the prefix is ``notes/`` and the delimiter is a slash (``/`` ) as in
              ``notes/summer/july`` , the common prefix is ``notes/summer/`` . All of the keys that roll up
              into a common prefix count as a single return when calculating the number of returns.

              - *(dict) --*

                Container for all (if there are any) keys between Prefix and the next occurrence of the
                string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in
                the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter
                is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

                - **Prefix** *(string) --*

                  Container for the specified common prefix.

            - **EncodingType** *(string) --*

              Encoding type used by Amazon S3 to encode object key names in the XML response.

              If you specify the encoding-type request parameter, Amazon S3 includes this element in the
              response, and returns encoded key name values in the following response elements:

               ``Delimiter, Prefix, Key,`` and ``StartAfter`` .

            - **KeyCount** *(integer) --*

              KeyCount is the number of keys returned with this request. KeyCount will always be less than
              equals to MaxKeys field. Say you ask for 50 keys, your result will include less than equals
              50 keys

            - **ContinuationToken** *(string) --*

              If ContinuationToken was sent with the request, it is included in the response.

            - **NextContinuationToken** *(string) --*

              NextContinuationToken is sent when isTruncated is true which means there are more keys in the
              bucket that can be listed. The next list requests to Amazon S3 can be continued with this
              NextContinuationToken. NextContinuationToken is obfuscated and is not a real key

            - **StartAfter** *(string) --*

              If StartAfter was sent with the request, it is included in the response.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_parts(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        MaxParts: int = None,
        PartNumberMarker: int = None,
        RequestPayer: str = None,
    ) -> ClientListPartsResponseTypeDef:
        """
        Lists the parts that have been uploaded for a specific multipart upload. This operation must
        include the upload ID, which you obtain by sending the initiate multipart upload request (see
        CreateMultipartUpload ). This request returns a maximum of 1,000 uploaded parts. The default number
        of parts returned is 1,000 parts. You can restrict the number of parts returned by specifying the
        ``max-parts`` request parameter. If your multipart upload consists of more than 1,000 parts, the
        response returns an ``IsTruncated`` field with the value of true, and a ``NextPartNumberMarker``
        element. In subsequent ``ListParts`` requests you can include the part-number-marker query string
        parameter and set its value to the ``NextPartNumberMarker`` field value from the previous response.

        For more information on multipart uploads, see `Uploading Objects Using Multipart Upload
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html>`__ .

        For information on permissions required to use the multipart upload API, see `Multipart Upload API
        and Permissions <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html>`__ .

        The following operations are related to ``ListParts`` :

        *  CreateMultipartUpload

        *  UploadPart

        *  CompleteMultipartUpload

        *  AbortMultipartUpload

        *  ListMultipartUploads

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListParts>`_

        **Request Syntax**
        ::

          response = client.list_parts(
              Bucket='string',
              Key='string',
              MaxParts=123,
              PartNumberMarker=123,
              UploadId='string',
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket to which the parts are being uploaded.->

        :type Key: string
        :param Key: **[REQUIRED]**

          Object key for which the multipart upload was initiated.

        :type MaxParts: integer
        :param MaxParts:

          Sets the maximum number of parts to return.

        :type PartNumberMarker: integer
        :param PartNumberMarker:

          Specifies the part after which listing should begin. Only parts with higher part numbers will be
          listed.

        :type UploadId: string
        :param UploadId: **[REQUIRED]**

          Upload ID identifying the multipart upload whose parts are being listed.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AbortDate': datetime(2015, 1, 1),
                'AbortRuleId': 'string',
                'Bucket': 'string',
                'Key': 'string',
                'UploadId': 'string',
                'PartNumberMarker': 123,
                'NextPartNumberMarker': 123,
                'MaxParts': 123,
                'IsTruncated': True|False,
                'Parts': [
                    {
                        'PartNumber': 123,
                        'LastModified': datetime(2015, 1, 1),
                        'ETag': 'string',
                        'Size': 123
                    },
                ],
                'Initiator': {
                    'ID': 'string',
                    'DisplayName': 'string'
                },
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                },
                'StorageClass':
                'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'
                |'DEEP_ARCHIVE',
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **AbortDate** *(datetime) --*

              If the bucket has a lifecycle rule configured with an action to abort incomplete multipart
              uploads and the prefix in the lifecycle rule matches the object name in the request, then the
              response includes this header indicating when the initiated multipart upload will become
              eligible for abort operation. For more information, see `Aborting Incomplete Multipart
              Uploads Using a Bucket Lifecycle Policy
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
              .

              The response will also include the x-amz-abort-rule-id header that will provide the ID of the
              lifecycle configuration rule that defines this action.

            - **AbortRuleId** *(string) --*

              This header is returned along with the x-amz-abort-date header. It identifies applicable
              lifecycle configuration rule that defines the action to abort incomplete multipart uploads.

            - **Bucket** *(string) --*

              Name of the bucket to which the multipart upload was initiated.

            - **Key** *(string) --*

              Object key for which the multipart upload was initiated.

            - **UploadId** *(string) --*

              Upload ID identifying the multipart upload whose parts are being listed.

            - **PartNumberMarker** *(integer) --*

              When a list is truncated, this element specifies the last part in the list, as well as the
              value to use for the part-number-marker request parameter in a subsequent request.

            - **NextPartNumberMarker** *(integer) --*

              When a list is truncated, this element specifies the last part in the list, as well as the
              value to use for the part-number-marker request parameter in a subsequent request.

            - **MaxParts** *(integer) --*

              Maximum number of parts that were allowed in the response.

            - **IsTruncated** *(boolean) --*

              Indicates whether the returned list of parts is truncated. A true value indicates that the
              list was truncated. A list can be truncated if the number of parts exceeds the limit returned
              in the MaxParts element.

            - **Parts** *(list) --*

              Container for elements related to a particular part. A response can contain zero or more Part
              elements.

              - *(dict) --*

                Container for elements related to a part.

                - **PartNumber** *(integer) --*

                  Part number identifying the part. This is a positive integer between 1 and 10,000.

                - **LastModified** *(datetime) --*

                  Date and time at which the part was uploaded.

                - **ETag** *(string) --*

                  Entity tag returned when the part was uploaded.

                - **Size** *(integer) --*

                  Size in bytes of the uploaded part data.

            - **Initiator** *(dict) --*

              Container element that identifies who initiated the multipart upload. If the initiator is an
              AWS account, this element provides the same information as the Owner element. If the
              initiator is an IAM User, then this element provides the user ARN and display name.

              - **ID** *(string) --*

                If the principal is an AWS account, it provides the Canonical User ID. If the principal is
                an IAM User, it provides a user ARN value.

              - **DisplayName** *(string) --*

                Name of the Principal.

            - **Owner** *(dict) --*

              Container element that identifies the object owner, after the object is created. If multipart
              upload is initiated by an IAM user, this element provides the parent account ID and display
              name.

              - **DisplayName** *(string) --*

                Container for the display name of the owner

              - **ID** *(string) --*

                Container for the ID of the owner

            - **StorageClass** *(string) --*

              Class of storage (STANDARD or REDUCED_REDUNDANCY) used to store the uploaded object.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_accelerate_configuration(
        self,
        Bucket: str,
        AccelerateConfiguration: ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef,
    ) -> None:
        """
        Sets the accelerate configuration of an existing bucket. Amazon S3 Transfer Acceleration is a
        bucket-level feature that enables you to perform faster data transfers to Amazon S3.

        To use this operation, you must have permission to perform the s3:PutAccelerateConfiguration
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        The Transfer Acceleration state of a bucket can be set to one of the following two values:

        * Enabled – Enables accelerated data transfers to the bucket.

        * Suspended – Disables accelerated data transfers to the bucket.

        The  GetBucketAccelerateConfiguration operation returns the transfer acceleration state of a bucket.

        After setting the Transfer Acceleration state of a bucket to Enabled, it might take up to thirty
        minutes before the data transfer rates to the bucket increase.

        The name of the bucket used for Transfer Acceleration must be DNS-compliant and must not contain
        periods (".").

        For more information about transfer acceleration, see `Transfer Acceleration
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html>`__ .

        The following operations are related to ``PutBucketAccelerateConfiguration`` :

        *  GetBucketAccelerateConfiguration

        *  CreateBucket

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketAccelerateConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_bucket_accelerate_configuration(
              Bucket='string',
              AccelerateConfiguration={
                  'Status': 'Enabled'|'Suspended'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket for which the accelerate configuration is set.

        :type AccelerateConfiguration: dict
        :param AccelerateConfiguration: **[REQUIRED]**

          Container for setting the transfer acceleration state.

          - **Status** *(string) --*

            Specifies the transfer acceleration status of the bucket.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_acl(
        self,
        Bucket: str,
        ACL: str = None,
        AccessControlPolicy: ClientPutBucketAclAccessControlPolicyTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
    ) -> None:
        """
        Sets the permissions on an existing bucket using access control lists (ACL). For more information,
        see `Using ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html>`__ . To
        set the ACL of a bucket, you must have WRITE_ACP permission.

        You can use one of the following two ways to set a bucket's permissions:

        * Specify the ACL in the request body

        * Specify permissions using request headers

        .. note::

          You cannot specify access permission using both the body and the request headers.

        Depending on your application needs, you may choose to set the ACL on a bucket using either the
        request body or the headers. For example, if you have an existing application that updates a bucket
        ACL using the request body, then you can continue to use that approach.

         **Access Permissions**

        You can set access permissions using one of the following methods:

        * Specify a canned ACL with the ``x-amz-acl`` request header. Amazon S3 supports a set of
        predefined ACLs, known as canned ACLs. Each canned ACL has a predefined set of grantees and
        permissions. Specify the canned ACL name as the value of x-amz-acl. If you use this header, you
        cannot use other access control specific headers in your request. For more information, see `Canned
        ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__ .

        * Specify access permissions explicitly with the ``x-amz-grant-read`` , ``x-amz-grant-read-acp`` ,
        ``x-amz-grant-write-acp`` , and ``x-amz-grant-full-control`` headers. When using these headers you
        specify explicit access permissions and grantees (AWS accounts or a Amazon S3 groups) who will
        receive the permission. If you use these ACL specific headers, you cannot use x-amz-acl header to
        set a canned ACL. These parameters map to the set of permissions that Amazon S3 supports in an ACL.
        For more information, see `Access Control List (ACL) Overview
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html>`__ . You specify each grantee
        as a type=value pair, where the type is one of the following:

          * emailAddress – if the value specified is the email address of an AWS account

          * id – if the value specified is the canonical user ID of an AWS account

          * uri – if you are granting permissions to a predefined group

        For example, the following x-amz-grant-write header grants create, overwrite, and delete objects
        permission to LogDelivery group predefined by Amazon S3 and two AWS accounts identified by their
        email addresses.

         ``x-amz-grant-write: uri="http://acs.amazonaws.com/groups/s3/LogDelivery",
         emailAddress="xyz@amazon.com", emailAddress="abc@amazon.com"``

        You can use either a canned ACL or specify access permissions explicitly. You cannot do both.

         **Grantee Values**

        You can specify the person (grantee) to whom you're assigning access rights (using request
        elements) in the following ways:

        * By Email address:  ``<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:type="AmazonCustomerByEmail"><EmailAddress><>Grantees@email.com<></EmailAddress>lt;/Grantee>``
         The grantee is resolved to the CanonicalUser and, in a response to a GET Object acl request,
         appears as the CanonicalUser.

        * By the person's ID:  ``<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:type="CanonicalUser"><ID><>ID<></ID><DisplayName><>GranteesEmail<></DisplayName> </Grantee>``
        DisplayName is optional and ignored in the request

        * By URI:  ``<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:type=
            "Group"><URI><>http://acs.amazonaws.com/groups/global/AuthenticatedUsers<></URI></Grantee>``

         **Related Resources**

        *  CreateBucket

        *  DeleteBucket

        *  GetObjectAcl

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketAcl>`_

        **Request Syntax**
        ::

          response = client.put_bucket_acl(
              ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
              AccessControlPolicy={
                  'Grants': [
                      {
                          'Grantee': {
                              'DisplayName': 'string',
                              'EmailAddress': 'string',
                              'ID': 'string',
                              'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                              'URI': 'string'
                          },
                          'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                      },
                  ],
                  'Owner': {
                      'DisplayName': 'string',
                      'ID': 'string'
                  }
              },
              Bucket='string',
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWrite='string',
              GrantWriteACP='string'
          )
        :type ACL: string
        :param ACL:

          The canned ACL to apply to the bucket.

        :type AccessControlPolicy: dict
        :param AccessControlPolicy:

          Contains the elements that set the ACL permissions for an object per grantee.

          - **Grants** *(list) --*

            A list of grants.

            - *(dict) --*

              Container for grant information.

              - **Grantee** *(dict) --*

                The person being granted permissions.

                - **DisplayName** *(string) --*

                  Screen name of the grantee.

                - **EmailAddress** *(string) --*

                  Email address of the grantee.

                - **ID** *(string) --*

                  The canonical user ID of the grantee.

                - **Type** *(string) --* **[REQUIRED]**

                  Type of grantee

                - **URI** *(string) --*

                  URI of the grantee group.

              - **Permission** *(string) --*

                Specifies the permission given to the grantee.

          - **Owner** *(dict) --*

            Container for the bucket owner's display name and ID.

            - **DisplayName** *(string) --*

              Container for the display name of the owner

            - **ID** *(string) --*

              Container for the ID of the owner

        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket to which to apply the ACL.

        :type GrantFullControl: string
        :param GrantFullControl:

          Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

        :type GrantRead: string
        :param GrantRead:

          Allows grantee to list the objects in the bucket.

        :type GrantReadACP: string
        :param GrantReadACP:

          Allows grantee to read the bucket ACL.

        :type GrantWrite: string
        :param GrantWrite:

          Allows grantee to create, overwrite, and delete any object in the bucket.

        :type GrantWriteACP: string
        :param GrantWriteACP:

          Allows grantee to write the ACL for the applicable bucket.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_analytics_configuration(
        self,
        Bucket: str,
        Id: str,
        AnalyticsConfiguration: ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef,
    ) -> None:
        """
        Sets an analytics configuration for the bucket (specified by the analytics configuration ID). You
        can have up to 1,000 analytics configurations per bucket.

        You can choose to have storage class analysis export analysis reports to a comma-separated values
        (CSV) flat file, see the DataExport request element. Reports are updated daily and are based on the
        object filters you configure. When selecting data export you specify a destination bucket and
        optional destination prefix where the file is written. You can export the data to a destination
        bucket in a different account. However, the destination bucket must be in the same region as the
        bucket that you are making the PUT analytics configuration to. For more information, see `Amazon S3
        Analytics – Storage Class Analysis
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html>`__ .

        .. warning::

          You must create a bucket policy on the destination bucket where the exported file is written to
          grant permissions to Amazon S3 to write objects to the bucket. For an example policy, see
          `Granting Permissions for Amazon S3 Inventory and Storage Class Analysis
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9>`__
          .

        To use this operation, you must have permissions to perform the ``s3:PutAnalyticsConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

         **Special Errors**

        *

          * *HTTP Error: HTTP 400 Bad Request*

          * *Code: InvalidArgument*

          * *Cause: Invalid argument.*

        *

          * *HTTP Error: HTTP 400 Bad Request*

          * *Code: TooManyConfigurations*

          * *Cause: You are attempting to create a new configuration but have already reached the
          1,000-configuration limit.*

        *

          * *HTTP Error: HTTP 403 Forbidden*

          * *Code: AccessDenied*

          * *Cause: You are not the owner of the specified bucket, or you do not have the
          s3:PutAnalyticsConfiguration bucket permission to set the configuration on the bucket.*

         **Related Resources**

        *

        *

        *

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketAnalyticsConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_bucket_analytics_configuration(
              Bucket='string',
              Id='string',
              AnalyticsConfiguration={
                  'Id': 'string',
                  'Filter': {
                      'Prefix': 'string',
                      'Tag': {
                          'Key': 'string',
                          'Value': 'string'
                      },
                      'And': {
                          'Prefix': 'string',
                          'Tags': [
                              {
                                  'Key': 'string',
                                  'Value': 'string'
                              },
                          ]
                      }
                  },
                  'StorageClassAnalysis': {
                      'DataExport': {
                          'OutputSchemaVersion': 'V_1',
                          'Destination': {
                              'S3BucketDestination': {
                                  'Format': 'CSV',
                                  'BucketAccountId': 'string',
                                  'Bucket': 'string',
                                  'Prefix': 'string'
                              }
                          }
                      }
                  }
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket to which an analytics configuration is stored.

        :type Id: string
        :param Id: **[REQUIRED]**

          The ID that identifies the analytics configuration.

        :type AnalyticsConfiguration: dict
        :param AnalyticsConfiguration: **[REQUIRED]**

          The configuration and any analyses for the analytics filter.

          - **Id** *(string) --* **[REQUIRED]**

            The ID that identifies the analytics configuration.

          - **Filter** *(dict) --*

            The filter used to describe a set of objects for analyses. A filter must have exactly one
            prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all
            objects will be considered in any analysis.

            - **Prefix** *(string) --*

              The prefix to use when evaluating an analytics filter.

            - **Tag** *(dict) --*

              The tag to use when evaluating an analytics filter.

              - **Key** *(string) --* **[REQUIRED]**

                Name of the tag.

              - **Value** *(string) --* **[REQUIRED]**

                Value of the tag.

            - **And** *(dict) --*

              A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter.
              The operator must have at least two predicates.

              - **Prefix** *(string) --*

                The prefix to use when evaluating an AND predicate: The prefix that an object must have to
                be included in the metrics results.

              - **Tags** *(list) --*

                The list of tags to use when evaluating an AND predicate.

                - *(dict) --*

                  A container of a key value name pair.

                  - **Key** *(string) --* **[REQUIRED]**

                    Name of the tag.

                  - **Value** *(string) --* **[REQUIRED]**

                    Value of the tag.

          - **StorageClassAnalysis** *(dict) --* **[REQUIRED]**

            Contains data related to access patterns to be collected and made available to analyze the
            tradeoffs between different storage classes.

            - **DataExport** *(dict) --*

              Specifies how data related to the storage class analysis for an Amazon S3 bucket should be
              exported.

              - **OutputSchemaVersion** *(string) --* **[REQUIRED]**

                The version of the output schema to use when exporting data. Must be ``V_1`` .

              - **Destination** *(dict) --* **[REQUIRED]**

                The place to store the data for an analysis.

                - **S3BucketDestination** *(dict) --* **[REQUIRED]**

                  A destination signifying output to an S3 bucket.

                  - **Format** *(string) --* **[REQUIRED]**

                    Specifies the file format used when exporting data to Amazon S3.

                  - **BucketAccountId** *(string) --*

                    The account ID that owns the destination bucket. If no account ID is provided, the
                    owner will not be validated prior to exporting data.

                  - **Bucket** *(string) --* **[REQUIRED]**

                    The Amazon Resource Name (ARN) of the bucket to which data is exported.

                  - **Prefix** *(string) --*

                    The prefix to use when exporting data. The prefix is prepended to all results.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_cors(
        self,
        Bucket: str,
        CORSConfiguration: ClientPutBucketCorsCORSConfigurationTypeDef,
    ) -> None:
        """
        Sets the ``cors`` configuration for your bucket. If the configuration exists, Amazon S3 replaces it.

        To use this operation, you must be allowed to perform the ``s3:PutBucketCORS`` action. By default,
        the bucket owner has this permission and can grant it to others.

        You set this configuration on a bucket so that the bucket can service cross-origin requests. For
        example, you might want to enable a request whose origin is ``http://www.example.com`` to access
        your Amazon S3 bucket at ``my.example.bucket.com`` by using the browser's ``XMLHttpRequest``
        capability.

        To enable cross-origin resource sharing (CORS) on a bucket, you add the ``cors`` subresource to the
        bucket. The ``cors`` subresource is an XML document in which you configure rules that identify
        origins and the HTTP methods that can be executed on your bucket. The document is limited to 64 KB
        in size.

        When Amazon S3 receives a cross-origin request (or a pre-flight OPTIONS request) against a bucket,
        it evaluates the ``cors`` configuration on the bucket and uses the first ``CORSRule`` rule that
        matches the incoming browser request to enable a cross-origin request. For a rule to match, the
        following conditions must be met:

        * The request's ``Origin`` header must match ``AllowedOrigin`` elements.

        * The request method (for example, GET, PUT, HEAD and so on) or the
        ``Access-Control-Request-Method`` header in case of a pre-flight ``OPTIONS`` request must be one of
        the ``AllowedMethod`` elements.

        * Every header specified in the ``Access-Control-Request-Headers`` request header of a pre-flight
        request must match an ``AllowedHeader`` element.

        For more information about CORS, go to `Enabling Cross-Origin Resource Sharing
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html>`__ in the *Amazon Simple Storage
        Service Developer Guide* .

         **Related Resources**

        *  GetBucketCors

        *  DeleteBucketCors

        *  RESTOPTIONSobject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketCors>`_

        **Request Syntax**
        ::

          response = client.put_bucket_cors(
              Bucket='string',
              CORSConfiguration={
                  'CORSRules': [
                      {
                          'AllowedHeaders': [
                              'string',
                          ],
                          'AllowedMethods': [
                              'string',
                          ],
                          'AllowedOrigins': [
                              'string',
                          ],
                          'ExposeHeaders': [
                              'string',
                          ],
                          'MaxAgeSeconds': 123
                      },
                  ]
              },

          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Specifies the bucket impacted by the ``cors`` configuration.

        :type CORSConfiguration: dict
        :param CORSConfiguration: **[REQUIRED]**

          Describes the cross-origin access configuration for objects in an Amazon S3 bucket. For more
          information, see `Enabling Cross-Origin Resource Sharing
          <https://docs.aws.amazon.com/AmazonS3/latest/dev//cors.html>`__ in the Amazon Simple Storage
          Service Developer Guide.

          - **CORSRules** *(list) --* **[REQUIRED]**

            A set of origins and methods (cross-origin access that you want to allow). You can add up to
            100 rules to the configuration.

            - *(dict) --*

              Specifies a cross-origin access rule for an Amazon S3 bucket.

              - **AllowedHeaders** *(list) --*

                Headers that are specified in the ``Access-Control-Request-Headers`` header. These headers
                are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request,
                Amazon S3 returns any requested headers that are allowed.

                - *(string) --*

              - **AllowedMethods** *(list) --* **[REQUIRED]**

                An HTTP method that you allow the origin to execute. Valid values are ``GET`` , ``PUT`` ,
                ``HEAD`` , ``POST`` , and ``DELETE`` .

                - *(string) --*

              - **AllowedOrigins** *(list) --* **[REQUIRED]**

                One or more origins you want customers to be able to access the bucket from.

                - *(string) --*

              - **ExposeHeaders** *(list) --*

                One or more headers in the response that you want customers to be able to access from their
                applications (for example, from a JavaScript ``XMLHttpRequest`` object).

                - *(string) --*

              - **MaxAgeSeconds** *(integer) --*

                The time in seconds that your browser is to cache the preflight response for the specified
                resource.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_encryption(
        self,
        Bucket: str,
        ServerSideEncryptionConfiguration: ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef,
        ContentMD5: str = None,
    ) -> None:
        """
        This implementation of the ``PUT`` operation uses the ``encryption`` subresource to set the default
        encryption state of an existing bucket.

        This implementation of the ``PUT`` operation sets default encryption for a buckets using
        server-side encryption with Amazon S3-managed keys SSE-S3 or AWS KMS customer master keys (CMKs)
        (SSE-KMS) bucket. For information about the Amazon S3 default encryption feature, see As a security
        precaution, the root user of the AWS account that owns a bucket can always use this operation, even
        if the policy explicitly denies the root user the ability to perform this action. in the *Amazon
        Simple Storage Service Developer Guide* .

        .. warning::

          This operation requires AWS Signature Version 4. For more information, see `Authenticating
          Requests (AWS Signature Version 4) <sig-v4-authenticating-requests.html>`__ .

        To use this operation, you must have permissions to perform the ``s3:PutEncryptionConfiguration``
        action. The bucket owner has this permission by default. The bucket owner can grant this permission
        to others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the Amazon Simple
        Storage Service Developer Guide.

         **Related Resources**

        *  GetBucketEncryption

        *  DeleteBucketEncryption

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketEncryption>`_

        **Request Syntax**
        ::

          response = client.put_bucket_encryption(
              Bucket='string',
              ContentMD5='string',
              ServerSideEncryptionConfiguration={
                  'Rules': [
                      {
                          'ApplyServerSideEncryptionByDefault': {
                              'SSEAlgorithm': 'AES256'|'aws:kms',
                              'KMSMasterKeyID': 'string'
                          }
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Specifies default encryption for a bucket using server-side encryption with Amazon S3-managed
          keys (SSE-S3) or customer master keys stored in AWS KMS (SSE-KMS). For information about the
          Amazon S3 default encryption feature, see `Amazon S3 Default Bucket Encryption
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html>`__ in the *Amazon Simple
          Storage Service Developer Guide* .

        :type ContentMD5: string
        :param ContentMD5:

          The base64-encoded 128-bit MD5 digest of the server-side encryption configuration. This parameter
          is auto-populated when using the command from the CLI.

        :type ServerSideEncryptionConfiguration: dict
        :param ServerSideEncryptionConfiguration: **[REQUIRED]**

          Specifies the default server-side-encryption configuration.

          - **Rules** *(list) --* **[REQUIRED]**

            Container for information about a particular server-side encryption configuration rule.

            - *(dict) --*

              Specifies the default server-side encryption configuration.

              - **ApplyServerSideEncryptionByDefault** *(dict) --*

                Specifies the default server-side encryption to apply to new objects in the bucket. If a
                PUT Object request doesn't specify any server-side encryption, this default encryption will
                be applied.

                - **SSEAlgorithm** *(string) --* **[REQUIRED]**

                  Server-side encryption algorithm to use for the default encryption.

                - **KMSMasterKeyID** *(string) --*

                  KMS master key ID to use for the default encryption. This parameter is allowed if and
                  only if ``SSEAlgorithm`` is set to ``aws:kms`` .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_inventory_configuration(
        self,
        Bucket: str,
        Id: str,
        InventoryConfiguration: ClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef,
    ) -> None:
        """
        This implementation of the ``PUT`` operation adds an inventory configuration (identified by the
        inventory ID) to the bucket. You can have up to 1,000 inventory configurations per bucket.

        Amazon S3 inventory generates inventories of the objects in the bucket on a daily or weekly basis,
        and the results are published to a flat file. The bucket that is inventoried is called the *source*
        bucket, and the bucket where the inventory flat file is stored is called the *destination* bucket.
        The *destination* bucket must be in the same AWS Region as the *source* bucket.

        When you configure an inventory for a *source* bucket, you specify the *destination* bucket where
        you want the inventory to be stored, and whether to generate the inventory daily or weekly. You can
        also configure what object metadata to include and whether to inventory all object versions or only
        current versions. For more information, see `Amazon S3 Inventory
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//storage-inventory.html>`__ in the Amazon Simple
        Storage Service Developer Guide.

        .. warning::

          You must create a bucket policy on the *destination* bucket to grant permissions to Amazon S3 to
          write objects to the bucket in the defined location. For an example policy, see `Granting
          Permissions for Amazon S3 Inventory and Storage Class Analysis.
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9>`__
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9>`__

        To use this operation, you must have permissions to perform the ``s3:PutInventoryConfiguration``
        action. The bucket owner has this permission by default and can grant this permission to others.
        For more information about permissions, see `Permissions Related to Bucket Subresource Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//s3-access-control.html>`__ in the Amazon Simple
        Storage Service Developer Guide.

         **Special Errors**

        * **HTTP 400 Bad Request Error**

          * *Code:* InvalidArgument

          * *Cause:* Invalid Argument

        * **HTTP 400 Bad Request Error**

          * *Code:* TooManyConfigurations

          * *Cause:* You are attempting to create a new configuration but have already reached the
          1,000-configuration limit.

        * **HTTP 403 Forbidden Error**

          * *Code:* AccessDenied

          * *Cause:* You are not the owner of the specified bucket, or you do not have the
          ``s3:PutInventoryConfiguration`` bucket permission to set the configuration on the bucket

         **Related Resources**

        *  GetBucketInventoryConfiguration

        *  DeleteBucketInventoryConfiguration

        *  ListBucketInventoryConfigurations

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketInventoryConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_bucket_inventory_configuration(
              Bucket='string',
              Id='string',
              InventoryConfiguration={
                  'Destination': {
                      'S3BucketDestination': {
                          'AccountId': 'string',
                          'Bucket': 'string',
                          'Format': 'CSV'|'ORC'|'Parquet',
                          'Prefix': 'string',
                          'Encryption': {
                              'SSES3': {}
                              ,
                              'SSEKMS': {
                                  'KeyId': 'string'
                              }
                          }
                      }
                  },
                  'IsEnabled': True|False,
                  'Filter': {
                      'Prefix': 'string'
                  },
                  'Id': 'string',
                  'IncludedObjectVersions': 'All'|'Current',
                  'OptionalFields': [
                      'Size'|'LastModifiedDate'|'StorageClass'|'ETag'|'IsMultipartUploaded'
                      |'ReplicationStatus'|'EncryptionStatus'|'ObjectLockRetainUntilDate'|'ObjectLockMode'
                      |'ObjectLockLegalHoldStatus'|'IntelligentTieringAccessTier',
                  ],
                  'Schedule': {
                      'Frequency': 'Daily'|'Weekly'
                  }
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket where the inventory configuration will be stored.

        :type Id: string
        :param Id: **[REQUIRED]**

          The ID used to identify the inventory configuration.

        :type InventoryConfiguration: dict
        :param InventoryConfiguration: **[REQUIRED]**

          Specifies the inventory configuration.

          - **Destination** *(dict) --* **[REQUIRED]**

            Contains information about where to publish the inventory results.

            - **S3BucketDestination** *(dict) --* **[REQUIRED]**

              Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where
              inventory results are published.

              - **AccountId** *(string) --*

                The ID of the account that owns the destination bucket.

              - **Bucket** *(string) --* **[REQUIRED]**

                The Amazon resource name (ARN) of the bucket where inventory results will be published.

              - **Format** *(string) --* **[REQUIRED]**

                Specifies the output format of the inventory results.

              - **Prefix** *(string) --*

                The prefix that is prepended to all inventory results.

              - **Encryption** *(dict) --*

                Contains the type of server-side encryption used to encrypt the inventory results.

                - **SSES3** *(dict) --*

                  Specifies the use of SSE-S3 to encrypt delivered Inventory reports.

                - **SSEKMS** *(dict) --*

                  Specifies the use of SSE-KMS to encrypt delivered Inventory reports.

                  - **KeyId** *(string) --* **[REQUIRED]**

                    Specifies the ID of the AWS Key Management Service (KMS) customer master key (CMK) to
                    use for encrypting Inventory reports.

          - **IsEnabled** *(boolean) --* **[REQUIRED]**

            Specifies whether the inventory is enabled or disabled. If set to ``True`` , an inventory list
            is generated. If set to ``False`` , no inventory list is generated.

          - **Filter** *(dict) --*

            Specifies an inventory filter. The inventory only includes objects that meet the filter's
            criteria.

            - **Prefix** *(string) --* **[REQUIRED]**

              The prefix that an object must have to be included in the inventory results.

          - **Id** *(string) --* **[REQUIRED]**

            The ID used to identify the inventory configuration.

          - **IncludedObjectVersions** *(string) --* **[REQUIRED]**

            Object versions to include in the inventory list. If set to ``All`` , the list includes all the
            object versions, which adds the version-related fields ``VersionId`` , ``IsLatest`` , and
            ``DeleteMarker`` to the list. If set to ``Current`` , the list does not contain these
            version-related fields.

          - **OptionalFields** *(list) --*

            Contains the optional fields that are included in the inventory results.

            - *(string) --*

          - **Schedule** *(dict) --* **[REQUIRED]**

            Specifies the schedule for generating inventory results.

            - **Frequency** *(string) --* **[REQUIRED]**

              Specifies how frequently inventory results are produced.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_lifecycle(
        self,
        Bucket: str,
        LifecycleConfiguration: ClientPutBucketLifecycleLifecycleConfigurationTypeDef = None,
    ) -> None:
        """
        .. warning::

          For an updated version of this API, see  PutBucketLifecycleConfiguration . This version has been
          deprecated. Existing lifecycle configurations will work. For new lifecycle configurations, use
          the updated API.

        Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle
        configuration. For information about lifecycle configuration, see `Object Lifecycle Management
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//object-lifecycle-mgmt.html>`__ in the *Amazon
        Simple Storage Service Developer Guide* .

        By default, all Amazon S3 resources, including buckets, objects, and related subresources (for
        example, lifecycle configuration and website configuration) are private. Only the resource owner,
        the AWS account that created the resource, can access it. The resource owner can optionally grant
        access permissions to others by writing an access policy. For this operation, users must get the
        ``s3:PutLifecycleConfiguration`` permission.

        You can also explicitly deny permissions. Explicit denial also supersedes any other permissions. If
        you want to prevent users or accounts from removing or deleting objects from your bucket, you must
        deny them permissions for the following actions:

        * ``s3:DeleteObject``

        * ``s3:DeleteObjectVersion``

        * ``s3:PutLifecycleConfiguration``

        For more information about permissions, see `Managing Access Permissions to your Amazon S3
        Resources <https://docs.aws.amazon.com/AmazonS3/latest/dev//s3-access-control.html>`__ in the
        *Amazon Simple Storage Service Developer Guide* .

        For more examples of transitioning objects to storage classes such as STANDARD_IA or ONEZONE_IA,
        see `Examples of Lifecycle Configuration
        <https://docs.aws.amazon.com/AmazonS3/latest/dev//intro-lifecycle-rules.html#lifecycle-configuration-examples>`__
        .

         **Related Resources**

        *  GetBucketLifecycle (Deprecated)

        *  GetBucketLifecycleConfiguration

        *

        * By default, a resource owner—in this case, a bucket owner, which is the AWS account that created
        the bucket—can perform any of the operations. A resource owner can also grant others permission to
        perform the operation. For more information, see the following topics in the Amazon Simple Storage
        Service Developer Guide:

          * `Specifying Permissions in a Policy
          <https://docs.aws.amazon.com/AmazonS3/latest/dev//using-with-s3-actions.html>`__

          * `Managing Access Permissions to your Amazon S3 Resources
          <https://docs.aws.amazon.com/AmazonS3/latest/dev//s3-access-control.html>`__

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not be
            used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketLifecycle>`_

        **Request Syntax**
        ::

          response = client.put_bucket_lifecycle(
              Bucket='string',
              LifecycleConfiguration={
                  'Rules': [
                      {
                          'Expiration': {
                              'Date': datetime(2015, 1, 1),
                              'Days': 123,
                              'ExpiredObjectDeleteMarker': True|False
                          },
                          'ID': 'string',
                          'Prefix': 'string',
                          'Status': 'Enabled'|'Disabled',
                          'Transition': {
                              'Date': datetime(2015, 1, 1),
                              'Days': 123,
                              'StorageClass':
                              'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                          },
                          'NoncurrentVersionTransition': {
                              'NoncurrentDays': 123,
                              'StorageClass':
                              'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                          },
                          'NoncurrentVersionExpiration': {
                              'NoncurrentDays': 123
                          },
                          'AbortIncompleteMultipartUpload': {
                              'DaysAfterInitiation': 123
                          }
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

        :type LifecycleConfiguration: dict
        :param LifecycleConfiguration:

          - **Rules** *(list) --* **[REQUIRED]**

            Specifies lifecycle configuration rules for an Amazon S3 bucket.

            - *(dict) --*

              Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket
              lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__ in
              the *Amazon Simple Storage Service API Reference* .

              - **Expiration** *(dict) --*

                Specifies the expiration for the lifecycle of the object.

                - **Date** *(datetime) --*

                  Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
                  Format.

                - **Days** *(integer) --*

                  Indicates the lifetime, in days, of the objects that are subject to the rule. The value
                  must be a non-zero positive integer.

                - **ExpiredObjectDeleteMarker** *(boolean) --*

                  Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If
                  set to true, the delete marker will be expired; if set to false the policy takes no
                  action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.

              - **ID** *(string) --*

                Unique identifier for the rule. The value can't be longer than 255 characters.

              - **Prefix** *(string) --* **[REQUIRED]**

                Object key prefix that identifies one or more objects to which this rule applies.

              - **Status** *(string) --* **[REQUIRED]**

                If ``Enabled`` , the rule is currently being applied. If ``Disabled`` , the rule is not
                currently being applied.

              - **Transition** *(dict) --*

                Specifies when an object transitions to a specified storage class.

                - **Date** *(datetime) --*

                  Indicates when objects are transitioned to the specified storage class. The date value
                  must be in ISO 8601 format. The time is always midnight UTC.

                - **Days** *(integer) --*

                  Indicates the number of days after creation when objects are transitioned to the
                  specified storage class. The value must be a positive integer.

                - **StorageClass** *(string) --*

                  The storage class to which you want the object to transition.

              - **NoncurrentVersionTransition** *(dict) --*

                Container for the transition rule that describes when noncurrent objects transition to the
                ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` , ``GLACIER`` , or
                ``DEEP_ARCHIVE`` storage class. If your bucket is versioning-enabled (or versioning is
                suspended), you can set this action to request that Amazon S3 transition noncurrent object
                versions to the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` , ``GLACIER`` ,
                or ``DEEP_ARCHIVE`` storage class at a specific period in the object's lifetime.

                - **NoncurrentDays** *(integer) --*

                  Specifies the number of days an object is noncurrent before Amazon S3 can perform the
                  associated action. For information about the noncurrent days calculations, see `How
                  Amazon S3 Calculates When an Object Became Noncurrent
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the
                  *Amazon Simple Storage Service Developer Guide* .

                - **StorageClass** *(string) --*

                  The class of storage used to store the object.

              - **NoncurrentVersionExpiration** *(dict) --*

                Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently
                deletes the noncurrent object versions. You set this lifecycle configuration action on a
                bucket that has versioning enabled (or suspended) to request that Amazon S3 delete
                noncurrent object versions at a specific period in the object's lifetime.

                - **NoncurrentDays** *(integer) --*

                  Specifies the number of days an object is noncurrent before Amazon S3 can perform the
                  associated action. For information about the noncurrent days calculations, see `How
                  Amazon S3 Calculates When an Object Became Noncurrent
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__
                  in the Amazon Simple Storage Service Developer Guide.

              - **AbortIncompleteMultipartUpload** *(dict) --*

                Specifies the days since the initiation of an incomplete multipart upload that Amazon S3
                will wait before permanently removing all parts of the upload. For more information, see
                `Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy
                <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
                in the *Amazon Simple Storage Service Developer Guide* .

                - **DaysAfterInitiation** *(integer) --*

                  Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_lifecycle_configuration(
        self,
        Bucket: str,
        LifecycleConfiguration: ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef = None,
    ) -> None:
        """
        Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle
        configuration. For information about lifecycle configuration, see `Managing Access Permissions to
        Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        .. note::

          Bucket lifecycle configuration now supports specifying a lifecycle rule using an object key name
          prefix, one or more object tags, or a combination of both. Accordingly, this section describes
          the latest API. The previous version of the API supported filtering based only on an object key
          name prefix, which is supported for backward compatibility. For the related API description, see
          PutBucketLifecycle .

         **Rules**

        You specify the lifecycle configuration in your request body. The lifecycle configuration is
        specified as XML consisting of one or more rules. Each rule consists of the following:

        * Filter identifying a subset of objects to which the rule applies. The filter can be based on a
        key name prefix, object tags, or a combination of both.

        * Status whether the rule is in effect.

        * One or more lifecycle transition and expiration actions that you want Amazon S3 to perform on the
        objects identified by the filter. If the state of your bucket is versioning-enabled or
        versioning-suspended, you can have many versions of the same object (one current version and zero
        or more noncurrent versions). Amazon S3 provides predefined actions that you can specify for
        current and noncurrent object versions.

        For more information, see `Object Lifecycle Management
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html>`__ and `Lifecycle
        Configuration Elements
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html>`__ .

         **Permissions**

        By default, all Amazon S3 resources are private, including buckets, objects, and related
        subresources (for example, lifecycle configuration and website configuration). Only the resource
        owner (that is, the AWS account that created it) can access the resource. The resource owner can
        optionally grant access permissions to others by writing an access policy. For this operation, a
        user must get the s3:PutLifecycleConfiguration permission.

        You can also explicitly deny permissions. Explicit deny also supersedes any other permissions. If
        you want to block users or accounts from removing or deleting objects from your bucket, you must
        deny them permissions for the following actions:

        * s3:DeleteObject

        * s3:DeleteObjectVersion

        * s3:PutLifecycleConfiguration

        For more information about permissions, see `Managing Access Permissions to Your Amazon S3
        Resources <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        The following are related to ``PutBucketLifecycleConfiguration`` :

        * `Examples of Lifecycle Configuration
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-configuration-examples.html>`__

        *  GetBucketLifecycleConfiguration

        *  DeleteBucketLifecycle

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketLifecycleConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_bucket_lifecycle_configuration(
              Bucket='string',
              LifecycleConfiguration={
                  'Rules': [
                      {
                          'Expiration': {
                              'Date': datetime(2015, 1, 1),
                              'Days': 123,
                              'ExpiredObjectDeleteMarker': True|False
                          },
                          'ID': 'string',
                          'Prefix': 'string',
                          'Filter': {
                              'Prefix': 'string',
                              'Tag': {
                                  'Key': 'string',
                                  'Value': 'string'
                              },
                              'And': {
                                  'Prefix': 'string',
                                  'Tags': [
                                      {
                                          'Key': 'string',
                                          'Value': 'string'
                                      },
                                  ]
                              }
                          },
                          'Status': 'Enabled'|'Disabled',
                          'Transitions': [
                              {
                                  'Date': datetime(2015, 1, 1),
                                  'Days': 123,
                                  'StorageClass':
                                  'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                              },
                          ],
                          'NoncurrentVersionTransitions': [
                              {
                                  'NoncurrentDays': 123,
                                  'StorageClass':
                                  'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'
                              },
                          ],
                          'NoncurrentVersionExpiration': {
                              'NoncurrentDays': 123
                          },
                          'AbortIncompleteMultipartUpload': {
                              'DaysAfterInitiation': 123
                          }
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket for which to set the configuration.

        :type LifecycleConfiguration: dict
        :param LifecycleConfiguration:

          Container for lifecycle rules. You can add as many as 1,000 rules.

          - **Rules** *(list) --* **[REQUIRED]**

            A lifecycle rule for individual objects in an Amazon S3 bucket.

            - *(dict) --*

              A lifecycle rule for individual objects in an Amazon S3 bucket.

              - **Expiration** *(dict) --*

                Specifies the expiration for the lifecycle of the object in the form of date, days and,
                whether the object has a delete marker.

                - **Date** *(datetime) --*

                  Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601
                  Format.

                - **Days** *(integer) --*

                  Indicates the lifetime, in days, of the objects that are subject to the rule. The value
                  must be a non-zero positive integer.

                - **ExpiredObjectDeleteMarker** *(boolean) --*

                  Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If
                  set to true, the delete marker will be expired; if set to false the policy takes no
                  action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.

              - **ID** *(string) --*

                Unique identifier for the rule. The value cannot be longer than 255 characters.

              - **Prefix** *(string) --*

                Prefix identifying one or more objects to which the rule applies. This is No longer used;
                use Filter instead.

              - **Filter** *(dict) --*

                The Filter is used to identify objects that a Lifecycle Rule applies to. A Filter must have
                exactly one of Prefix, Tag, or And specified.

                - **Prefix** *(string) --*

                  Prefix identifying one or more objects to which the rule applies.

                - **Tag** *(dict) --*

                  This tag must exist in the object's tag set in order for the rule to apply.

                  - **Key** *(string) --* **[REQUIRED]**

                    Name of the tag.

                  - **Value** *(string) --* **[REQUIRED]**

                    Value of the tag.

                - **And** *(dict) --*

                  This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates.
                  The Lifecycle Rule will apply to any object matching all of the predicates configured
                  inside the And operator.

                  - **Prefix** *(string) --*

                    Prefix identifying one or more objects to which the rule applies.

                  - **Tags** *(list) --*

                    All of these tags must exist in the object's tag set in order for the rule to apply.

                    - *(dict) --*

                      A container of a key value name pair.

                      - **Key** *(string) --* **[REQUIRED]**

                        Name of the tag.

                      - **Value** *(string) --* **[REQUIRED]**

                        Value of the tag.

              - **Status** *(string) --* **[REQUIRED]**

                If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently
                being applied.

              - **Transitions** *(list) --*

                Specifies when an Amazon S3 object transitions to a specified storage class.

                - *(dict) --*

                  Specifies when an object transitions to a specified storage class.

                  - **Date** *(datetime) --*

                    Indicates when objects are transitioned to the specified storage class. The date value
                    must be in ISO 8601 format. The time is always midnight UTC.

                  - **Days** *(integer) --*

                    Indicates the number of days after creation when objects are transitioned to the
                    specified storage class. The value must be a positive integer.

                  - **StorageClass** *(string) --*

                    The storage class to which you want the object to transition.

              - **NoncurrentVersionTransitions** *(list) --*

                Specifies the transition rule for the lifecycle rule that describes when noncurrent objects
                transition to the a specific storage class. If your bucket is versioning-enabled (or
                versioning is suspended), you can set this action to request that Amazon S3 transition
                noncurrent object versions to the a specifc storage class at a set period in the object's
                lifetime.

                - *(dict) --*

                  Container for the transition rule that describes when noncurrent objects transition to
                  the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` , ``GLACIER`` , or
                  ``DEEP_ARCHIVE`` storage class. If your bucket is versioning-enabled (or versioning is
                  suspended), you can set this action to request that Amazon S3 transition noncurrent
                  object versions to the ``STANDARD_IA`` , ``ONEZONE_IA`` , ``INTELLIGENT_TIERING`` ,
                  ``GLACIER`` , or ``DEEP_ARCHIVE`` storage class at a specific period in the object's
                  lifetime.

                  - **NoncurrentDays** *(integer) --*

                    Specifies the number of days an object is noncurrent before Amazon S3 can perform the
                    associated action. For information about the noncurrent days calculations, see `How
                    Amazon S3 Calculates When an Object Became Noncurrent
                    <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the
                    *Amazon Simple Storage Service Developer Guide* .

                  - **StorageClass** *(string) --*

                    The class of storage used to store the object.

              - **NoncurrentVersionExpiration** *(dict) --*

                Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently
                deletes the noncurrent object versions. You set this lifecycle configuration action on a
                bucket that has versioning enabled (or suspended) to request that Amazon S3 delete
                noncurrent object versions at a specific period in the object's lifetime.

                - **NoncurrentDays** *(integer) --*

                  Specifies the number of days an object is noncurrent before Amazon S3 can perform the
                  associated action. For information about the noncurrent days calculations, see `How
                  Amazon S3 Calculates When an Object Became Noncurrent
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__
                  in the Amazon Simple Storage Service Developer Guide.

              - **AbortIncompleteMultipartUpload** *(dict) --*

                Specifies the days since the initiation of an incomplete multipart upload that Amazon S3
                will wait before permanently removing all parts of the upload. For more information, see
                `Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy
                <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
                in the *Amazon Simple Storage Service Developer Guide* .

                - **DaysAfterInitiation** *(integer) --*

                  Specifies the number of days after which Amazon S3 aborts an incomplete multipart upload.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_logging(
        self,
        Bucket: str,
        BucketLoggingStatus: ClientPutBucketLoggingBucketLoggingStatusTypeDef,
    ) -> None:
        """
        Set the logging parameters for a bucket and to specify permissions for who can view and modify the
        logging parameters. All logs are saved to buckets in the same AWS Region as the source bucket. To
        set the logging status of a bucket, you must be the bucket owner.

        The bucket owner is automatically granted FULL_CONTROL to all logs. You use the Grantee request
        element to grant access to other people. The Permissions request element specifies the kind of
        access the grantee has to the logs.

         **Grantee Values**

        You can specify the person (grantee) to whom you're assigning access rights (using request
        elements) in the following ways:

        * By the person's ID:  ``<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:type="CanonicalUser"><ID><>ID<></ID><DisplayName><>GranteesEmail<></DisplayName> </Grantee>``
        DisplayName is optional and ignored in the request.

        * By Email address:  ``<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:type="AmazonCustomerByEmail"><EmailAddress><>Grantees@email.com<></EmailAddress></Grantee>``
        The grantee is resolved to the CanonicalUser and, in a response to a GET Object acl request,
        appears as the CanonicalUser.

        * By URI:  ``<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:type=
            "Group"><URI><>http://acs.amazonaws.com/groups/global/AuthenticatedUsers<></URI></Grantee>``

        To enable logging, you use LoggingEnabled and its children request elements. To disable logging,
        you use an empty BucketLoggingStatus request element:

         ``<BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01" />``

        For more information about server access logging, see `Server Access Logging
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html>`__ .

        For more information about creating a bucket, see  CreateBucket . For more information about
        returning the logging status of a bucket, see  GetBucketLogging .

        The following operations are related to ``PutBucketLogging`` :

        *  PutObject

        *  DeleteBucket

        *  CreateBucket

        *  GetBucketLogging

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketLogging>`_

        **Request Syntax**
        ::

          response = client.put_bucket_logging(
              Bucket='string',
              BucketLoggingStatus={
                  'LoggingEnabled': {
                      'TargetBucket': 'string',
                      'TargetGrants': [
                          {
                              'Grantee': {
                                  'DisplayName': 'string',
                                  'EmailAddress': 'string',
                                  'ID': 'string',
                                  'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                                  'URI': 'string'
                              },
                              'Permission': 'FULL_CONTROL'|'READ'|'WRITE'
                          },
                      ],
                      'TargetPrefix': 'string'
                  }
              },

          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket for which to set the logging parameters.

        :type BucketLoggingStatus: dict
        :param BucketLoggingStatus: **[REQUIRED]**

          Container for logging status information.

          - **LoggingEnabled** *(dict) --*

            Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys
            for a bucket. For more information, see `PUT Bucket logging
            <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html>`__ in the *Amazon
            Simple Storage Service API Reference* .

            - **TargetBucket** *(string) --* **[REQUIRED]**

              Specifies the bucket where you want Amazon S3 to store server access logs. You can have your
              logs delivered to any bucket that you own, including the same bucket that is being logged.
              You can also configure multiple buckets to deliver their logs to the same target bucket. In
              this case you should choose a different TargetPrefix for each source bucket so that the
              delivered log files can be distinguished by key.

            - **TargetGrants** *(list) --*

              Container for granting information.

              - *(dict) --*

                Container for granting information.

                - **Grantee** *(dict) --*

                  Container for the person being granted permissions.

                  - **DisplayName** *(string) --*

                    Screen name of the grantee.

                  - **EmailAddress** *(string) --*

                    Email address of the grantee.

                  - **ID** *(string) --*

                    The canonical user ID of the grantee.

                  - **Type** *(string) --* **[REQUIRED]**

                    Type of grantee

                  - **URI** *(string) --*

                    URI of the grantee group.

                - **Permission** *(string) --*

                  Logging permissions assigned to the Grantee for the bucket.

            - **TargetPrefix** *(string) --* **[REQUIRED]**

              A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a
              single bucket, you can use a prefix to distinguish which log files came from which bucket.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_metrics_configuration(
        self,
        Bucket: str,
        Id: str,
        MetricsConfiguration: ClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef,
    ) -> None:
        """
        Sets a metrics configuration (specified by the metrics configuration ID) for the bucket. You can
        have up to 1,000 metrics configurations per bucket. If you're updating an existing metrics
        configuration, note that this is a full replacement of the existing metrics configuration. If you
        don't include the elements you want to keep, they are erased.

        To use this operation, you must have permissions to perform the s3:PutMetricsConfiguration action.
        The bucket owner has this permission by default. The bucket owner can grant this permission to
        others. For more information about permissions, see `Permissions Related to Bucket Subresource
        Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

        For information about CloudWatch request metrics for Amazon S3, see `Monitoring Metrics with Amazon
        CloudWatch <https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html>`__ .

        The following operations are related to ``PutBucketMetricsConfiguration`` :

        *  DeleteBucketMetricsConfiguration

        *  PutBucketMetricsConfiguration

        *  ListBucketMetricsConfigurations

         ``GetBucketLifecycle`` has the following special error:

        * Error code: ``TooManyConfigurations``

          * Description:You are attempting to create a new configuration but have already reached the
          1,000-configuration limit.

          * HTTP Status Code: HTTP 400 Bad Request

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketMetricsConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_bucket_metrics_configuration(
              Bucket='string',
              Id='string',
              MetricsConfiguration={
                  'Id': 'string',
                  'Filter': {
                      'Prefix': 'string',
                      'Tag': {
                          'Key': 'string',
                          'Value': 'string'
                      },
                      'And': {
                          'Prefix': 'string',
                          'Tags': [
                              {
                                  'Key': 'string',
                                  'Value': 'string'
                              },
                          ]
                      }
                  }
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket for which the metrics configuration is set.

        :type Id: string
        :param Id: **[REQUIRED]**

          The ID used to identify the metrics configuration.

        :type MetricsConfiguration: dict
        :param MetricsConfiguration: **[REQUIRED]**

          Specifies the metrics configuration.

          - **Id** *(string) --* **[REQUIRED]**

            The ID used to identify the metrics configuration.

          - **Filter** *(dict) --*

            Specifies a metrics configuration filter. The metrics configuration will only include objects
            that meet the filter's criteria. A filter must be a prefix, a tag, or a conjunction
            (MetricsAndOperator).

            - **Prefix** *(string) --*

              The prefix used when evaluating a metrics filter.

            - **Tag** *(dict) --*

              The tag used when evaluating a metrics filter.

              - **Key** *(string) --* **[REQUIRED]**

                Name of the tag.

              - **Value** *(string) --* **[REQUIRED]**

                Value of the tag.

            - **And** *(dict) --*

              A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter. The
              operator must have at least two predicates, and an object must match all of the predicates in
              order for the filter to apply.

              - **Prefix** *(string) --*

                The prefix used when evaluating an AND predicate.

              - **Tags** *(list) --*

                The list of tags used when evaluating an AND predicate.

                - *(dict) --*

                  A container of a key value name pair.

                  - **Key** *(string) --* **[REQUIRED]**

                    Name of the tag.

                  - **Value** *(string) --* **[REQUIRED]**

                    Value of the tag.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_notification(
        self,
        Bucket: str,
        NotificationConfiguration: ClientPutBucketNotificationNotificationConfigurationTypeDef,
    ) -> None:
        """
        No longer used, see the  PutBucketNotificationConfiguration operation.

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not be
            used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketNotification>`_

        **Request Syntax**
        ::

          response = client.put_bucket_notification(
              Bucket='string',
              NotificationConfiguration={
                  'TopicConfiguration': {
                      'Id': 'string',
                      'Events': [
                          's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                          |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                          |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                          |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                          |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      ],
                      'Event':
                      's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                      |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                      |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                      |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                      |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      'Topic': 'string'
                  },
                  'QueueConfiguration': {
                      'Id': 'string',
                      'Event':
                      's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                      |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                      |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                      |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                      |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      'Events': [
                          's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                          |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                          |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                          |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                          |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      ],
                      'Queue': 'string'
                  },
                  'CloudFunctionConfiguration': {
                      'Id': 'string',
                      'Event':
                      's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                      |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                      |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                      |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                      |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      'Events': [
                          's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                          |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                          |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                          |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                          |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                      ],
                      'CloudFunction': 'string',
                      'InvocationRole': 'string'
                  }
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket.

        :type NotificationConfiguration: dict
        :param NotificationConfiguration: **[REQUIRED]**

          The container for the configuration.

          - **TopicConfiguration** *(dict) --*

            This data type is deperecated. A container for specifying the configuration for publication of
            messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects
            specified events.

            - **Id** *(string) --*

              An optional unique identifier for configurations in a notification configuration. If you
              don't provide one, Amazon S3 will assign an ID.

            - **Events** *(list) --*

              A collection of events related to objects

              - *(string) --*

                The bucket event for which to send notifications.

            - **Event** *(string) --*

              Bucket event for which to send notifications.

            - **Topic** *(string) --*

              Amazon SNS topic to which Amazon S3 will publish a message to report the specified events for
              the bucket.

          - **QueueConfiguration** *(dict) --*

            This data type is deprecated. This data type specifies the configuration for publishing
            messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified
            events.

            - **Id** *(string) --*

              An optional unique identifier for configurations in a notification configuration. If you
              don't provide one, Amazon S3 will assign an ID.

            - **Event** *(string) --*

              The bucket event for which to send notifications.

            - **Events** *(list) --*

              A collection of bucket events for which to send notiications

              - *(string) --*

                The bucket event for which to send notifications.

            - **Queue** *(string) --*

              The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message
              when it detects events of the specified type.

          - **CloudFunctionConfiguration** *(dict) --*

            Container for specifying the AWS Lambda notification configuration.

            - **Id** *(string) --*

              An optional unique identifier for configurations in a notification configuration. If you
              don't provide one, Amazon S3 will assign an ID.

            - **Event** *(string) --*

              The bucket event for which to send notifications.

            - **Events** *(list) --*

              Bucket events for which to send notifications.

              - *(string) --*

                The bucket event for which to send notifications.

            - **CloudFunction** *(string) --*

              Lambda cloud function ARN that Amazon S3 can invoke when it detects events of the specified
              type.

            - **InvocationRole** *(string) --*

              The role supporting the invocation of the lambda function

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_notification_configuration(
        self,
        Bucket: str,
        NotificationConfiguration: ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef,
    ) -> None:
        """
        Enables notifications of specified events for a bucket. For more information about event
        notifications, see `Configuring Event Notifications
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ .

        Using this API, you can replace an existing notification configuration. The configuration is an XML
        file that defines the event types that you want Amazon S3 to publish and the destination where you
        want Amazon S3 to publish an event notification when it detects an event of the specified type.

        By default, your bucket has no event notifications configured. That is, the notification
        configuration will be an empty ``NotificationConfiguration`` .

         ``<NotificationConfiguration>``

         ``</NotificationConfiguration>``

        This operation replaces the existing notification configuration with the configuration you include
        in the request body.

        After Amazon S3 receives this request, it first verifies that any Amazon Simple Notification
        Service (Amazon SNS) or Amazon Simple Queue Service (Amazon SQS) destination exists, and that the
        bucket owner has permission to publish to it by sending a test notification. In the case of AWS
        Lambda destinations, Amazon S3 verifies that the Lambda function permissions grant Amazon S3
        permission to invoke the function from the Amazon S3 bucket. For more information, see `Configuring
        Notifications for Amazon S3 Events
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ .

        You can disable notifications by adding the empty NotificationConfiguration element.

        By default, only the bucket owner can configure notifications on a bucket. However, bucket owners
        can use a bucket policy to grant permission to other users to set this configuration with
        ``s3:PutBucketNotification`` permission.

        .. note::

          The PUT notification is an atomic operation. For example, suppose your notification configuration
          includes SNS topic, SQS queue, and Lambda function configurations. When you send a PUT request
          with this configuration, Amazon S3 sends test messages to your SNS topic. If the message fails,
          the entire PUT operation will fail, and Amazon S3 will not add the configuration to your bucket.

         **Responses**

        If the configuration in the request body includes only one ``TopicConfiguration`` specifying only
        the *s3:ReducedRedundancyLostObject* event type, the response will also include the
        *x-amz-sns-test-message-id* header containing the message ID of the test notification sent to topic.

        The following operations is related to ``PutBucketNotificationConfiguration`` :

        *  GetBucketNotificationConfiguration

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketNotificationConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_bucket_notification_configuration(
              Bucket='string',
              NotificationConfiguration={
                  'TopicConfigurations': [
                      {
                          'Id': 'string',
                          'TopicArn': 'string',
                          'Events': [
                              's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                              |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                              |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                              |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                              |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                          ],
                          'Filter': {
                              'Key': {
                                  'FilterRules': [
                                      {
                                          'Name': 'prefix'|'suffix',
                                          'Value': 'string'
                                      },
                                  ]
                              }
                          }
                      },
                  ],
                  'QueueConfigurations': [
                      {
                          'Id': 'string',
                          'QueueArn': 'string',
                          'Events': [
                              's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                              |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                              |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                              |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                              |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                          ],
                          'Filter': {
                              'Key': {
                                  'FilterRules': [
                                      {
                                          'Name': 'prefix'|'suffix',
                                          'Value': 'string'
                                      },
                                  ]
                              }
                          }
                      },
                  ],
                  'LambdaFunctionConfigurations': [
                      {
                          'Id': 'string',
                          'LambdaFunctionArn': 'string',
                          'Events': [
                              's3:ReducedRedundancyLostObject'|'s3:ObjectCreated:*'|'s3:ObjectCreated:Put'
                              |'s3:ObjectCreated:Post'|'s3:ObjectCreated:Copy'
                              |'s3:ObjectCreated:CompleteMultipartUpload'|'s3:ObjectRemoved:*'
                              |'s3:ObjectRemoved:Delete'|'s3:ObjectRemoved:DeleteMarkerCreated'
                              |'s3:ObjectRestore:Post'|'s3:ObjectRestore:Completed',
                          ],
                          'Filter': {
                              'Key': {
                                  'FilterRules': [
                                      {
                                          'Name': 'prefix'|'suffix',
                                          'Value': 'string'
                                      },
                                  ]
                              }
                          }
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket.

        :type NotificationConfiguration: dict
        :param NotificationConfiguration: **[REQUIRED]**

          A container for specifying the notification configuration of the bucket. If this element is
          empty, notifications are turned off for the bucket.

          - **TopicConfigurations** *(list) --*

            The topic to which notifications are sent and the events for which notifications are generated.

            - *(dict) --*

              A container for specifying the configuration for publication of messages to an Amazon Simple
              Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.

              - **Id** *(string) --*

                An optional unique identifier for configurations in a notification configuration. If you
                don't provide one, Amazon S3 will assign an ID.

              - **TopicArn** *(string) --* **[REQUIRED]**

                The Amazon Resource Name (ARN) of the Amazon SNS topic to which Amazon S3 publishes a
                message when it detects events of the specified type.

              - **Events** *(list) --* **[REQUIRED]**

                The Amazon S3 bucket event about which to send notifications. For more information, see
                `Supported Event Types
                <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon
                Simple Storage Service Developer Guide* .

                - *(string) --*

                  The bucket event for which to send notifications.

              - **Filter** *(dict) --*

                Specifies object key name filtering rules. For information about key name filtering, see
                `Configuring Event Notifications
                <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon
                Simple Storage Service Developer Guide* .

                - **Key** *(dict) --*

                  A container for object key name prefix and suffix filtering rules.

                  - **FilterRules** *(list) --*

                    A list of containers for the key value pair that defines the criteria for the filter
                    rule.

                    - *(dict) --*

                      Specifies the Amazon S3 object key name to filter on and whether to filter on the
                      suffix or prefix of the key name.

                      - **Name** *(string) --*

                        The object key name prefix or suffix identifying one or more objects to which the
                        filtering rule applies. The maximum length is 1,024 characters. Overlapping
                        prefixes and suffixes are not supported. For more information, see `Configuring
                        Event Notifications
                        <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the
                        *Amazon Simple Storage Service Developer Guide* .

                      - **Value** *(string) --*

                        The value that the filter searches for in object key names.

          - **QueueConfigurations** *(list) --*

            The Amazon Simple Queue Service queues to publish messages to and the events for which to
            publish messages.

            - *(dict) --*

              Specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon
              SQS) queue when Amazon S3 detects specified events.

              - **Id** *(string) --*

                An optional unique identifier for configurations in a notification configuration. If you
                don't provide one, Amazon S3 will assign an ID.

              - **QueueArn** *(string) --* **[REQUIRED]**

                The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a
                message when it detects events of the specified type.

              - **Events** *(list) --* **[REQUIRED]**

                A collection of bucket events for which to send notiications

                - *(string) --*

                  The bucket event for which to send notifications.

              - **Filter** *(dict) --*

                Specifies object key name filtering rules. For information about key name filtering, see
                `Configuring Event Notifications
                <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon
                Simple Storage Service Developer Guide* .

                - **Key** *(dict) --*

                  A container for object key name prefix and suffix filtering rules.

                  - **FilterRules** *(list) --*

                    A list of containers for the key value pair that defines the criteria for the filter
                    rule.

                    - *(dict) --*

                      Specifies the Amazon S3 object key name to filter on and whether to filter on the
                      suffix or prefix of the key name.

                      - **Name** *(string) --*

                        The object key name prefix or suffix identifying one or more objects to which the
                        filtering rule applies. The maximum length is 1,024 characters. Overlapping
                        prefixes and suffixes are not supported. For more information, see `Configuring
                        Event Notifications
                        <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the
                        *Amazon Simple Storage Service Developer Guide* .

                      - **Value** *(string) --*

                        The value that the filter searches for in object key names.

          - **LambdaFunctionConfigurations** *(list) --*

            Describes the AWS Lambda functions to invoke and the events for which to invoke them.

            - *(dict) --*

              A container for specifying the configuration for AWS Lambda notifications.

              - **Id** *(string) --*

                An optional unique identifier for configurations in a notification configuration. If you
                don't provide one, Amazon S3 will assign an ID.

              - **LambdaFunctionArn** *(string) --* **[REQUIRED]**

                The Amazon Resource Name (ARN) of the AWS Lambda function that Amazon S3 invokes when the
                specified event type occurs.

              - **Events** *(list) --* **[REQUIRED]**

                The Amazon S3 bucket event for which to invoke the AWS Lambda function. For more
                information, see `Supported Event Types
                <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon
                Simple Storage Service Developer Guide* .

                - *(string) --*

                  The bucket event for which to send notifications.

              - **Filter** *(dict) --*

                Specifies object key name filtering rules. For information about key name filtering, see
                `Configuring Event Notifications
                <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon
                Simple Storage Service Developer Guide* .

                - **Key** *(dict) --*

                  A container for object key name prefix and suffix filtering rules.

                  - **FilterRules** *(list) --*

                    A list of containers for the key value pair that defines the criteria for the filter
                    rule.

                    - *(dict) --*

                      Specifies the Amazon S3 object key name to filter on and whether to filter on the
                      suffix or prefix of the key name.

                      - **Name** *(string) --*

                        The object key name prefix or suffix identifying one or more objects to which the
                        filtering rule applies. The maximum length is 1,024 characters. Overlapping
                        prefixes and suffixes are not supported. For more information, see `Configuring
                        Event Notifications
                        <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the
                        *Amazon Simple Storage Service Developer Guide* .

                      - **Value** *(string) --*

                        The value that the filter searches for in object key names.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_policy(
        self, Bucket: str, Policy: str, ConfirmRemoveSelfBucketAccess: bool = None
    ) -> None:
        """
        Applies an Amazon S3 bucket policy to an Amazon S3 bucket. If you are using an identity other than
        the root user of the AWS account that owns the bucket, the calling identity must have the
        ``PutBucketPolicy`` permissions on the specified bucket and belong to the bucket owner's account in
        order to use this operation.

        If you don't have ``PutBucketPolic`` y permissions, Amazon S3 returns a ``403 Access Denied``
        error. If you have the correct permissions, but you're not using an identity that belongs to the
        bucket owner's account, Amazon S3 returns a ``405 Method Not Allowed`` error.

        .. warning::

          As a security precaution, the root user of the AWS account that owns a bucket can always use this
          operation, even if the policy explicitly denies the root user the ability to perform this action.

        For more information about bucket policies, see `Using Bucket Policies and User Policies
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html>`__ .

        The following operations are related to ``PutBucketPolicy`` :

        *  CreateBucket

        *  DeleteBucket

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketPolicy>`_

        **Request Syntax**
        ::

          response = client.put_bucket_policy(
              Bucket='string',
              ConfirmRemoveSelfBucketAccess=True|False,
              Policy='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket.

        :type ConfirmRemoveSelfBucketAccess: boolean
        :param ConfirmRemoveSelfBucketAccess:

          Set this parameter to true to confirm that you want to remove your permissions to change this
          bucket policy in the future.

        :type Policy: string
        :param Policy: **[REQUIRED]**

          The bucket policy as a JSON document.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_replication(
        self,
        Bucket: str,
        ReplicationConfiguration: ClientPutBucketReplicationReplicationConfigurationTypeDef,
        Token: str = None,
    ) -> None:
        """
        Creates a replication configuration or replaces an existing one. For more information, see
        `Replication <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html>`__ in the *Amazon
        S3 Developer Guide* .

        .. note::

          To perform this operation, the user or role performing the operation must have the
          `iam\\:PassRole <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html>`__
          permission.

        Specify the replication configuration in the request body. In the replication configuration, you
        provide the name of the destination bucket where you want Amazon S3 to replicate objects, the IAM
        role that Amazon S3 can assume to replicate objects on your behalf, and other relevant information.

        A replication configuration must include at least one rule, and can contain a maximum of 1,000.
        Each rule identifies a subset of objects to replicate by filtering the objects in the source
        bucket. To choose additional subsets of objects to replicate, add a rule for each subset. All rules
        must specify the same destination bucket.

        To specify a subset of the objects in the source bucket to apply a replication rule to, add the
        Filter element as a child of the Rule element. You can filter objects based on an object key
        prefix, one or more object tags, or both. When you add the Filter element in the configuration, you
        must also add the following elements: ``DeleteMarkerReplication`` , ``Status`` , and ``Priority`` .

        For information about enabling versioning on a bucket, see `Using Versioning
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html>`__ .

        By default, a resource owner, in this case the AWS account that created the bucket, can perform
        this operation. The resource owner can also grant others permissions to perform the operation. For
        more information about permissions, see `Specifying Permissions in a Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html>`__ and `Managing
        Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

         **Handling Replication of Encrypted Objects**

        By default, Amazon S3 doesn't replicate objects that are stored at rest using server-side
        encryption with CMKs stored in AWS KMS. To replicate AWS KMS-encrypted objects, add the following:
        ``SourceSelectionCriteria`` , ``SseKmsEncryptedObjects`` , ``Status`` , ``EncryptionConfiguration``
        , and ``ReplicaKmsKeyID`` . For information about replication configuration, see `Replicating
        Objects Created with SSE Using CMKs stored in AWS KMS
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-config-for-kms-objects.html>`__ .

         ``PutBucketReplication`` has the following special errors:

        * Error code: ``InvalidRequest``

          * Description: If the <Owner> in <AccessControlTranslation> has a value, the <Account> element
          must be specified.

          * HTTP 400

        * Error code: ``InvalidArgument``

          * Description: The <Account> element is empty. It must contain a valid account ID.

          * HTTP 400

        * Error code: ``InvalidArgument``

          * Description: The AWS account specified in the <Account> element must match the destination
          bucket owner.

          * HTTP 400

        The following operations are related to ``PutBucketReplication`` :

        *  GetBucketReplication

        *  DeleteBucketReplication

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketReplication>`_

        **Request Syntax**
        ::

          response = client.put_bucket_replication(
              Bucket='string',
              ReplicationConfiguration={
                  'Role': 'string',
                  'Rules': [
                      {
                          'ID': 'string',
                          'Priority': 123,
                          'Prefix': 'string',
                          'Filter': {
                              'Prefix': 'string',
                              'Tag': {
                                  'Key': 'string',
                                  'Value': 'string'
                              },
                              'And': {
                                  'Prefix': 'string',
                                  'Tags': [
                                      {
                                          'Key': 'string',
                                          'Value': 'string'
                                      },
                                  ]
                              }
                          },
                          'Status': 'Enabled'|'Disabled',
                          'SourceSelectionCriteria': {
                              'SseKmsEncryptedObjects': {
                                  'Status': 'Enabled'|'Disabled'
                              }
                          },
                          'ExistingObjectReplication': {
                              'Status': 'Enabled'|'Disabled'
                          },
                          'Destination': {
                              'Bucket': 'string',
                              'Account': 'string',
                              'StorageClass':
                              'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'
                              |'INTELLIGENT_TIERING'|'GLACIER'|'DEEP_ARCHIVE',
                              'AccessControlTranslation': {
                                  'Owner': 'Destination'
                              },
                              'EncryptionConfiguration': {
                                  'ReplicaKmsKeyID': 'string'
                              }
                          },
                          'DeleteMarkerReplication': {
                              'Status': 'Enabled'|'Disabled'
                          }
                      },
                  ]
              },
              Token='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket

        :type ReplicationConfiguration: dict
        :param ReplicationConfiguration: **[REQUIRED]**

          A container for replication rules. You can add up to 1,000 rules. The maximum size of a
          replication configuration is 2 MB.

          - **Role** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon
            S3 assumes when replicating objects. For more information, see `How to Set Up Replication
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html>`__ in the *Amazon
            Simple Storage Service Developer Guide* .

          - **Rules** *(list) --* **[REQUIRED]**

            A container for one or more replication rules. A replication configuration must have at least
            one rule and can contain a maximum of 1,000 rules.

            - *(dict) --*

              Specifies which Amazon S3 objects to replicate and where to store the replicas.

              - **ID** *(string) --*

                A unique identifier for the rule. The maximum value is 255 characters.

              - **Priority** *(integer) --*

                The priority associated with the rule. If you specify multiple rules in a replication
                configuration, Amazon S3 prioritizes the rules to prevent conflicts when filtering. If two
                or more rules identify the same object based on a specified filter, the rule with higher
                priority takes precedence. For example:

                * Same object quality prefix based filter criteria If prefixes you specified in multiple
                rules overlap

                * Same object qualify tag based filter criteria specified in multiple rules

                For more information, see `Replication <
                https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html>`__ in the *Amazon S3
                Developer Guide* .

              - **Prefix** *(string) --*

                An object keyname prefix that identifies the object or objects to which the rule applies.
                The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify
                an empty string.

              - **Filter** *(dict) --*

                A filter that identifies the subset of objects to which the replication rule applies. A
                ``Filter`` must specify exactly one ``Prefix`` , ``Tag`` , or an ``And`` child element.

                - **Prefix** *(string) --*

                  An object keyname prefix that identifies the subset of objects to which the rule applies.

                - **Tag** *(dict) --*

                  A container for specifying a tag key and value.

                  The rule applies only to objects that have the tag in their tag set.

                  - **Key** *(string) --* **[REQUIRED]**

                    Name of the tag.

                  - **Value** *(string) --* **[REQUIRED]**

                    Value of the tag.

                - **And** *(dict) --*

                  A container for specifying rule filters. The filters determine the subset of objects to
                  which the rule applies. This element is required only if you specify more than one
                  filter. For example:

                  * If you specify both a ``Prefix`` and a ``Tag`` filter, wrap these filters in an ``And``
                  tag.

                  * If you specify a filter based on multiple tags, wrap the ``Tag`` elements in an ``And``
                  tag.

                  - **Prefix** *(string) --*

                    An object keyname prefix that identifies the subset of objects to which the rule
                    applies.

                  - **Tags** *(list) --*

                    An array of tags containing key and value pairs.

                    - *(dict) --*

                      A container of a key value name pair.

                      - **Key** *(string) --* **[REQUIRED]**

                        Name of the tag.

                      - **Value** *(string) --* **[REQUIRED]**

                        Value of the tag.

              - **Status** *(string) --* **[REQUIRED]**

                Specifies whether the rule is enabled.

              - **SourceSelectionCriteria** *(dict) --*

                A container that describes additional filters for identifying the source objects that you
                want to replicate. You can choose to enable or disable the replication of these objects.
                Currently, Amazon S3 supports only the filter that you can specify for objects created with
                server-side encryption using a customer master key (CMK) stored in AWS Key Management
                Service (SSE-KMS).

                - **SseKmsEncryptedObjects** *(dict) --*

                  A container for filter information for the selection of Amazon S3 objects encrypted with
                  AWS KMS. If you include ``SourceSelectionCriteria`` in the replication configuration,
                  this element is required.

                  - **Status** *(string) --* **[REQUIRED]**

                    Specifies whether Amazon S3 replicates objects created with server-side encryption
                    using a customer master key (CMK) stored in AWS Key Management Service.

              - **ExistingObjectReplication** *(dict) --*

                A container that specifies information about existing object replication. You can choose
                whether to enable or disable the replication of existing objects.

                - **Status** *(string) --* **[REQUIRED]**

                  Specifies whether existing object replication is enabled.

              - **Destination** *(dict) --* **[REQUIRED]**

                A container for information about the replication destination.

                - **Bucket** *(string) --* **[REQUIRED]**

                  The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store the
                  results.

                - **Account** *(string) --*

                  Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3
                  to change replica ownership to the AWS account that owns the destination bucket by
                  specifying the ``AccessControlTranslation`` property, this is the account ID of the
                  destination bucket owner. For more information, see `Replication Additional
                  Configuration\\: Change Replica Owner
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-change-owner.html>`__ in the
                  *Amazon Simple Storage Service Developer Guide* .

                - **StorageClass** *(string) --*

                  The storage class to use when replicating objects, such as standard or reduced
                  redundancy. By default, Amazon S3 uses the storage class of the source object to create
                  the object replica.

                  For valid values, see the ``StorageClass`` element of the `PUT Bucket replication
                  <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html>`__ action
                  in the *Amazon Simple Storage Service API Reference* .

                - **AccessControlTranslation** *(dict) --*

                  Specify this only in a cross-account scenario (where source and destination bucket owners
                  are not the same), and you want to change replica ownership to the AWS account that owns
                  the destination bucket. If this is not specified in the replication configuration, the
                  replicas are owned by same AWS account that owns the source object.

                  - **Owner** *(string) --* **[REQUIRED]**

                    Specifies the replica ownership. For default and valid values, see `PUT bucket
                    replication
                    <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html>`__ in
                    the *Amazon Simple Storage Service API Reference* .

                - **EncryptionConfiguration** *(dict) --*

                  A container that provides information about encryption. If ``SourceSelectionCriteria`` is
                  specified, you must specify this element.

                  - **ReplicaKmsKeyID** *(string) --*

                    Specifies the AWS KMS Key ID (Key ARN or Alias ARN) for the destination bucket. Amazon
                    S3 uses this key to encrypt replica objects.

              - **DeleteMarkerReplication** *(dict) --*

                Specifies whether Amazon S3 replicates the delete markers. If you specify a ``Filter`` ,
                you must specify this element. However, in the latest version of replication configuration
                (when ``Filter`` is specified), Amazon S3 doesn't replicate delete markers. Therefore, the
                ``DeleteMarkerReplication`` element can contain only <Status>Disabled</Status>. For an
                example configuration, see `Basic Rule Configuration
                <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-config-min-rule-config>`__
                .

                .. note::

                  If you don't specify the Filter element, Amazon S3 assumes the replication configuration
                  is the earlier version, V1. In the earlier version, Amazon S3 handled replication of
                  delete markers differently. For more information, see `Backward Compatibility
                  <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations>`__
                  .

                - **Status** *(string) --*

                  Indicates whether to replicate delete markers.

                  .. note::

                    In the current implementation, Amazon S3 doesn't replicate the delete markers. The
                    status must be ``Disabled`` .

        :type Token: string
        :param Token:

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_request_payment(
        self,
        Bucket: str,
        RequestPaymentConfiguration: ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef,
    ) -> None:
        """
        Sets the request payment configuration for a bucket. By default, the bucket owner pays for
        downloads from the bucket. This configuration parameter enables the bucket owner (only) to specify
        that the person requesting the download will be charged for the download. For more information, see
        `Requester Pays Buckets
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html>`__ .

        The following operations are related to ``PutBucketRequestPayment`` :

        *  CreateBucket

        *  GetBucketRequestPayment

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketRequestPayment>`_

        **Request Syntax**
        ::

          response = client.put_bucket_request_payment(
              Bucket='string',
              RequestPaymentConfiguration={
                  'Payer': 'Requester'|'BucketOwner'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name.

        :type RequestPaymentConfiguration: dict
        :param RequestPaymentConfiguration: **[REQUIRED]**

          Container for Payer.

          - **Payer** *(string) --* **[REQUIRED]**

            Specifies who pays for the download and request fees.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_tagging(
        self, Bucket: str, Tagging: ClientPutBucketTaggingTaggingTypeDef
    ) -> None:
        """
        Sets the tags for a bucket.

        Use tags to organize your AWS bill to reflect your own cost structure. To do this, sign up to get
        your AWS account bill with tag key values included. Then, to see the cost of combined resources,
        organize your billing information according to resources with the same tag key values. For example,
        you can tag several resources with a specific application name, and then organize your billing
        information to see the total cost of that application across several services. For more
        information, see `Cost Allocation and Tagging
        <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ .

        .. note::

          Within a bucket, if you add a tag that has the same key as an existing tag, the new value
          overwrites the old value. For more information, see `Using Cost Allocation in Amazon S3 Bucket
          Tags <https://docs.aws.amazon.com/AmazonS3/latest/dev/CostAllocTagging.html>`__ .

        To use this operation, you must have permissions to perform the ``s3:PutBucketTagging`` action. The
        bucket owner has this permission by default and can grant this permission to others. For more
        information about permissions, see `Permissions Related to Bucket Subresource Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ .

         ``PutBucketTagging`` has the following special errors:

        * Error code: ``InvalidTagError``

          * Description: The tag provided was not a valid tag. This error can occur if the tag did not pass
          input validation. For information about tag restrictions, see `User-Defined Tag Restrictions
          <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2//allocation-tag-restrictions.html>`__
          and `AWS-Generated Cost Allocation Tag Restrictions
          <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2//aws-tag-restrictions.html>`__ .

        * Error code: ``MalformedXMLError``

          * Description: The XML provided does not match the schema.

        * Error code: ``OperationAbortedError``

          * Description: A conflicting conditional operation is currently in progress against this
          resource. Please try again.

        * Error code: ``InternalError``

          * Description: The service was unable to apply the provided tag to the bucket.

        The following operations are related to ``PutBucketTagging`` :

        *  GetBucketTagging

        *  DeleteBucketTagging

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketTagging>`_

        **Request Syntax**
        ::

          response = client.put_bucket_tagging(
              Bucket='string',
              Tagging={
                  'TagSet': [
                      {
                          'Key': 'string',
                          'Value': 'string'
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name.

        :type Tagging: dict
        :param Tagging: **[REQUIRED]**

          Container for the TagSet and Tag elements.

          - **TagSet** *(list) --* **[REQUIRED]**

            A collection for a a set of tags

            - *(dict) --*

              A container of a key value name pair.

              - **Key** *(string) --* **[REQUIRED]**

                Name of the tag.

              - **Value** *(string) --* **[REQUIRED]**

                Value of the tag.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_versioning(
        self,
        Bucket: str,
        VersioningConfiguration: ClientPutBucketVersioningVersioningConfigurationTypeDef,
        MFA: str = None,
    ) -> None:
        """
        Sets the versioning state of an existing bucket. To set the versioning state, you must be the
        bucket owner.

        You can set the versioning state with one of the following values:

         **Enabled** —Enables versioning for the objects in the bucket. All objects added to the bucket
         receive a unique version ID.

         **Suspended** —Disables versioning for the objects in the bucket. All objects added to the bucket
         receive the version ID null.

        If the versioning state has never been set on a bucket, it has no versioning state; a
        GetBucketVersioning request does not return a versioning state value.

        If the bucket owner enables MFA Delete in the bucket versioning configuration, the bucket owner
        must include the ``x-amz-mfa request`` header and the Status and the ``MfaDelete`` request elements
        in a request to set the versioning state of the bucket.

        .. warning::

          If you have an object expiration lifecycle policy in your non-versioned bucket and you want to
          maintain the same permanent delete behavior when you enable versioning, you must add a noncurrent
          expiration policy. The noncurrent expiration lifecycle policy will manage the deletes of the
          noncurrent object versions in the version-enabled bucket. (A version-enabled bucket maintains one
          current and zero or more noncurrent object versions.) For more information, see `Lifecycle and
          Versioning
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html#lifecycle-and-other-bucket-config>`__
          .

         **Related Resources**

        *  CreateBucket

        *  DeleteBucket

        *  GetBucketVersioning

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketVersioning>`_

        **Request Syntax**
        ::

          response = client.put_bucket_versioning(
              Bucket='string',
              MFA='string',
              VersioningConfiguration={
                  'MFADelete': 'Enabled'|'Disabled',
                  'Status': 'Enabled'|'Suspended'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name.

        :type MFA: string
        :param MFA:

          The concatenation of the authentication device's serial number, a space, and the value that is
          displayed on your authentication device.

        :type VersioningConfiguration: dict
        :param VersioningConfiguration: **[REQUIRED]**

          Container for setting the versioning state.

          - **MFADelete** *(string) --*

            Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is
            only returned if the bucket has been configured with MFA delete. If the bucket has never been
            so configured, this element is not returned.

          - **Status** *(string) --*

            The versioning state of the bucket.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_bucket_website(
        self,
        Bucket: str,
        WebsiteConfiguration: ClientPutBucketWebsiteWebsiteConfigurationTypeDef,
    ) -> None:
        """
        Sets the configuration of the website that is specified in the ``website`` subresource. To
        configure a bucket as a website, you can add this subresource on the bucket with website
        configuration information such as the file name of the index document and any redirect rules. For
        more information, see `Hosting Websites on Amazon S3
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html>`__ .

        This PUT operation requires the ``S3:PutBucketWebsite`` permission. By default, only the bucket
        owner can configure the website attached to a bucket; however, bucket owners can allow other users
        to set the website configuration by writing a bucket policy that grants them the
        ``S3:PutBucketWebsite`` permission.

        To redirect all website requests sent to the bucket's website endpoint, you add a website
        configuration with the following elements. Because all requests are sent to another website, you
        don't need to provide index document name for the bucket.

        * WebsiteConfiguration

        * RedirectAllRequestsTo

        * HostName

        * Protocol

        If you want granular control over redirects, you can use the following elements to add routing
        rules that describe conditions for redirecting requests and information about the redirect
        destination. In this case, the website configuration must provide an index document for the bucket,
        because some requests might not be redirected.

        * WebsiteConfiguration

        * IndexDocument

        * Suffix

        * ErrorDocument

        * Key

        * RoutingRules

        * RoutingRule

        * Condition

        * HttpErrorCodeReturnedEquals

        * KeyPrefixEquals

        * Redirect

        * Protocol

        * HostName

        * ReplaceKeyPrefixWith

        * ReplaceKeyWith

        * HttpRedirectCode

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketWebsite>`_

        **Request Syntax**
        ::

          response = client.put_bucket_website(
              Bucket='string',
              WebsiteConfiguration={
                  'ErrorDocument': {
                      'Key': 'string'
                  },
                  'IndexDocument': {
                      'Suffix': 'string'
                  },
                  'RedirectAllRequestsTo': {
                      'HostName': 'string',
                      'Protocol': 'http'|'https'
                  },
                  'RoutingRules': [
                      {
                          'Condition': {
                              'HttpErrorCodeReturnedEquals': 'string',
                              'KeyPrefixEquals': 'string'
                          },
                          'Redirect': {
                              'HostName': 'string',
                              'HttpRedirectCode': 'string',
                              'Protocol': 'http'|'https',
                              'ReplaceKeyPrefixWith': 'string',
                              'ReplaceKeyWith': 'string'
                          }
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name.

        :type WebsiteConfiguration: dict
        :param WebsiteConfiguration: **[REQUIRED]**

          Container for the request.

          - **ErrorDocument** *(dict) --*

            The name of the error document for the website.

            - **Key** *(string) --* **[REQUIRED]**

              The object key name to use when a 4XX class error occurs.

          - **IndexDocument** *(dict) --*

            The name of the index document for the website.

            - **Suffix** *(string) --* **[REQUIRED]**

              A suffix that is appended to a request that is for a directory on the website endpoint (e.g.
              if the suffix is index.html and you make a request to samplebucket/images/ the data that is
              returned will be for the object with the key name images/index.html) The suffix must not be
              empty and must not include a slash character.

          - **RedirectAllRequestsTo** *(dict) --*

            The redirect behavior for every request to this bucket's website endpoint.

            .. warning::

              If you specify this property, you can't specify any other property.

            - **HostName** *(string) --* **[REQUIRED]**

              Name of the host where requests are redirected.

            - **Protocol** *(string) --*

              Protocol to use when redirecting requests. The default is the protocol that is used in the
              original request.

          - **RoutingRules** *(list) --*

            Rules that define when a redirect is applied and the redirect behavior.

            - *(dict) --*

              Specifies the redirect behavior and when a redirect is applied.

              - **Condition** *(dict) --*

                A container for describing a condition that must be met for the specified redirect to
                apply. For example, 1. If request is for pages in the ``/docs`` folder, redirect to the
                ``/documents`` folder. 2. If request results in HTTP error 4xx, redirect request to another
                host where you might process the error.

                - **HttpErrorCodeReturnedEquals** *(string) --*

                  The HTTP error code when the redirect is applied. In the event of an error, if the error
                  code equals this value, then the specified redirect is applied. Required when parent
                  element ``Condition`` is specified and sibling ``KeyPrefixEquals`` is not specified. If
                  both are specified, then both must be true for the redirect to be applied.

                - **KeyPrefixEquals** *(string) --*

                  The object key name prefix when the redirect is applied. For example, to redirect
                  requests for ``ExamplePage.html`` , the key prefix will be ``ExamplePage.html`` . To
                  redirect request for all pages with the prefix ``docs/`` , the key prefix will be
                  ``/docs`` , which identifies all objects in the docs/ folder. Required when the parent
                  element ``Condition`` is specified and sibling ``HttpErrorCodeReturnedEquals`` is not
                  specified. If both conditions are specified, both must be true for the redirect to be
                  applied.

              - **Redirect** *(dict) --* **[REQUIRED]**

                Container for redirect information. You can redirect requests to another host, to another
                page, or with another protocol. In the event of an error, you can specify a different error
                code to return.

                - **HostName** *(string) --*

                  The host name to use in the redirect request.

                - **HttpRedirectCode** *(string) --*

                  The HTTP redirect code to use on the response. Not required if one of the siblings is
                  present.

                - **Protocol** *(string) --*

                  Protocol to use when redirecting requests. The default is the protocol that is used in
                  the original request.

                - **ReplaceKeyPrefixWith** *(string) --*

                  The object key prefix to use in the redirect request. For example, to redirect requests
                  for all pages with prefix ``docs/`` (objects in the ``docs/`` folder) to ``documents/`` ,
                  you can set a condition block with ``KeyPrefixEquals`` set to ``docs/`` and in the
                  Redirect set ``ReplaceKeyPrefixWith`` to ``/documents`` . Not required if one of the
                  siblings is present. Can be present only if ``ReplaceKeyWith`` is not provided.

                - **ReplaceKeyWith** *(string) --*

                  The specific object key to use in the redirect request. For example, redirect request to
                  ``error.html`` . Not required if one of the siblings is present. Can be present only if
                  ``ReplaceKeyPrefixWith`` is not provided.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_object(
        self,
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
        Metadata: Dict[str, str] = None,
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
    ) -> ClientPutObjectResponseTypeDef:
        """
        Adds an object to a bucket. You must have WRITE permissions on a bucket to add an object to it.

        Amazon S3 never adds partial objects; if you receive a success response, Amazon S3 added the entire
        object to the bucket.

        Amazon S3 is a distributed system. If it receives multiple write requests for the same object
        simultaneously, it overwrites all but the last object written. Amazon S3 does not provide object
        locking; if you need this, make sure to build it into your application layer or use versioning
        instead.

        To ensure that data is not corrupted traversing the network, use the ``Content-MD5`` header. When
        you use this header, Amazon S3 checks the object against the provided MD5 value and, if they do not
        match, returns an error. Additionally, you can calculate the MD5 while putting an object to Amazon
        S3 and compare the returned ETag to the calculated MD5 value.

        .. note::

          To configure your application to send the request headers before sending the request body, use
          the ``100-continue`` HTTP status code. For PUT operations, this helps you avoid sending the
          message body if the message is rejected based on the headers (for example, because authentication
          fails or a redirect occurs). For more information on the ``100-continue`` HTTP status code, see
          Section 8.2.3 of `http\\://www.ietf.org/rfc/rfc2616.txt <http://www.ietf.org/rfc/rfc2616.txt>`__ .

        You can optionally request server-side encryption. With server-side encryption, Amazon S3 encrypts
        your data as it writes it to disks in its data centers and decrypts the data when you access it.
        You have the option to provide your own encryption key or use AWS-managed encryption keys. For more
        information, see `Using Server-Side Encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html>`__ .

          Access Permissions

        You can optionally specify the accounts or groups that should be granted specific permissions on
        the new object. There are two ways to grant the permissions using the request headers:

        * Specify a canned ACL with the ``x-amz-acl`` request header. For more information, see `Canned ACL
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__ .

        * Specify access permissions explicitly with the ``x-amz-grant-read`` , ``x-amz-grant-read-acp`` ,
        ``x-amz-grant-write-acp`` , and ``x-amz-grant-full-control`` headers. These parameters map to the
        set of permissions that Amazon S3 supports in an ACL. For more information, see `Access Control
        List (ACL) Overview <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html>`__ .

        You can use either a canned ACL or specify access permissions explicitly. You cannot do both.

          Server-Side- Encryption-Specific Request Headers

        You can optionally tell Amazon S3 to encrypt data at rest using server-side encryption. Server-side
        encryption is for data encryption at rest. Amazon S3 encrypts your data as it writes it to disks in
        its data centers and decrypts it when you access it. The option you use depends on whether you want
        to use AWS-managed encryption keys or provide your own encryption key.

        * Use encryption keys managed Amazon S3 or customer master keys (CMKs) stored in AWS Key Management
        Service (KMS) – If you want AWS to manage the keys used to encrypt data, specify the following
        headers in the request.

          * x-amz-server-side​-encryption

          * x-amz-server-side-encryption-aws-kms-key-id

          * x-amz-server-side-encryption-context

        .. note::

          If you specify x-amz-server-side-encryption:aws:kms, but don't provide x-amz-server-side-
          encryption-aws-kms-key-id, Amazon S3 uses the AWS managed CMK in AWS KMS to protect the data.

        .. warning::

          All GET and PUT requests for an object protected by AWS KMS fail if you don't make them with SSL
          or by using SigV4.

        For more information on Server-Side Encryption with CMKs stored in AWS KMS (SSE-KMS), see
        `Protecting Data Using Server-Side Encryption with CMKs stored in AWS
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ .

        * Use customer-provided encryption keys – If you want to manage your own encryption keys, provide
        all the following headers in the request.

          * x-amz-server-side​-encryption​-customer-algorithm

          * x-amz-server-side​-encryption​-customer-key

          * x-amz-server-side​-encryption​-customer-key-MD5

        For more information on Server-Side Encryption with CMKs stored in KMS (SSE-KMS), see `Protecting
        Data Using Server-Side Encryption with CMKs stored in AWS KMS
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ .

          Access-Control-List (ACL)-Specific Request Headers

        You also can use the following access control–related headers with this operation. By default, all
        objects are private. Only the owner has full access control. When adding a new object, you can
        grant permissions to individual AWS accounts or to predefined groups defined by Amazon S3. These
        permissions are then added to the Access Control List (ACL) on the object. For more information,
        see `Using ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html>`__ . With
        this operation, you can grant access permissions using one of the following two methods:

        * Specify a canned ACL (x-amz-acl) — Amazon S3 supports a set of predefined ACLs, known as canned
        ACLs. Each canned ACL has a predefined set of grantees and permissions. For more information, see
        `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__ .

        * Specify access permissions explicitly — To explicitly grant access permissions to specific AWS
        accounts or groups, use the following headers. Each header maps to specific permissions that Amazon
        S3 supports in an ACL. For more information, see `Access Control List (ACL) Overview
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html>`__ . In the header, you specify
        a list of grantees who get the specific permission. To grant permissions explicitly use:

          * x-amz-grant-read

          * x-amz-grant-write

          * x-amz-grant-read-acp

          * x-amz-grant-write-acp

          * x-amz-grant-full-control

        You specify each grantee as a type=value pair, where the type is one of the following:

          * emailAddress – if the value specified is the email address of an AWS account

          .. warning::

             Using email addresses to specify a grantee is only supported in the following AWS Regions:

              * US East (N. Virginia)

              * US West (N. California)

              * US West (Oregon)

              * Asia Pacific (Singapore)

              * Asia Pacific (Sydney)

              * Asia Pacific (Tokyo)

              * EU (Ireland)

              * South America (São Paulo)

            For a list of all the Amazon S3 supported regions and endpoints, see `Regions and Endpoints
            <https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ in the AWS General
            Reference

          * id – if the value specified is the canonical user ID of an AWS account

          * uri – if you are granting permissions to a predefined group

        For example, the following x-amz-grant-read header grants the AWS accounts identified by email
        addresses permissions to read object data and its metadata:

         ``x-amz-grant-read: emailAddress="xyz@amazon.com", emailAddress="abc@amazon.com"``

          Server-Side- Encryption-Specific Request Headers

        You can optionally tell Amazon S3 to encrypt data at rest using server-side encryption. Server-side
        encryption is for data encryption at rest. Amazon S3 encrypts your data as it writes it to disks in
        its data centers and decrypts it when you access it. The option you use depends on whether you want
        to use AWS-managed encryption keys or provide your own encryption key.

        * Use encryption keys managed by Amazon S3 or customer master keys (CMKs) stored in AWS Key
        Management Service (KMS) – If you want AWS to manage the keys used to encrypt data, specify the
        following headers in the request.

          * x-amz-server-side​-encryption

          * x-amz-server-side-encryption-aws-kms-key-id

          * x-amz-server-side-encryption-context

        .. note::

          If you specify x-amz-server-side-encryption:aws:kms, but don't provide x-amz-server-side-
          encryption-aws-kms-key-id, Amazon S3 uses the default AWS KMS CMK to protect the data.

        .. warning::

          All GET and PUT requests for an object protected by AWS KMS fail if you don't make them with SSL
          or by using SigV4.

        For more information on Server-Side Encryption with CMKs stored in AWS KMS (SSE-KMS), see
        `Protecting Data Using Server-Side Encryption with CMKs stored in AWS KMS
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ .

        * Use customer-provided encryption keys – If you want to manage your own encryption keys, provide
        all the following headers in the request.

        .. note::

           If you use this feature, the ETag value that Amazon S3 returns in the response is not the MD5 of
           the object.

          * x-amz-server-side​-encryption​-customer-algorithm

          * x-amz-server-side​-encryption​-customer-key

          * x-amz-server-side​-encryption​-customer-key-MD5

        For more information on Server-Side Encryption with CMKs stored in AWS KMS (SSE-KMS), see
        `Protecting Data Using Server-Side Encryption with CMKs stored in AWS KMS
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ .

         **Storage Class Options**

        By default, Amazon S3 uses the Standard storage class to store newly created objects. The Standard
        storage class provides high durability and high availability. You can specify other storage classes
        depending on the performance needs. For more information, see `Storage Classes
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html>`__ in the Amazon Simple
        Storage Service Developer Guide.

         **Versioning**

        If you enable versioning for a bucket, Amazon S3 automatically generates a unique version ID for
        the object being stored. Amazon S3 returns this ID in the response using the ``x-amz-version-id
        response`` header. If versioning is suspended, Amazon S3 always uses null as the version ID for the
        object stored. For more information about returning the versioning state of a bucket, see
        GetBucketVersioning . If you enable versioning for a bucket, when Amazon S3 receives multiple write
        requests for the same object simultaneously, it stores all of the objects.

         **Related Resources**

        *  CopyObject

        *  DeleteObject

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObject>`_

        **Request Syntax**
        ::

          response = client.put_object(
              ACL=
                  'private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'
                  |'bucket-owner-read'|'bucket-owner-full-control',
              Body=b'bytes'|file,
              Bucket='string',
              CacheControl='string',
              ContentDisposition='string',
              ContentEncoding='string',
              ContentLanguage='string',
              ContentLength=123,
              ContentMD5='string',
              ContentType='string',
              Expires=datetime(2015, 1, 1),
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWriteACP='string',
              Key='string',
              Metadata={
                  'string': 'string'
              },
              ServerSideEncryption='AES256'|'aws:kms',
              StorageClass=
                  'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'
                  |'GLACIER'|'DEEP_ARCHIVE',
              WebsiteRedirectLocation='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              SSEKMSKeyId='string',
              SSEKMSEncryptionContext='string',
              RequestPayer='requester',
              Tagging='string',
              ObjectLockMode='GOVERNANCE'|'COMPLIANCE',
              ObjectLockRetainUntilDate=datetime(2015, 1, 1),
              ObjectLockLegalHoldStatus='ON'|'OFF'
          )
        :type ACL: string
        :param ACL:

          The canned ACL to apply to the object. For more information, see `Canned ACL
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__ .

        :type Body: bytes or seekable file-like object
        :param Body:

          Object data.

        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket to which the PUT operation was initiated.

        :type CacheControl: string
        :param CacheControl:

          Can be used to specify caching behavior along the request/reply chain. For more information, see
          `http\\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9
          <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9>`__ .

        :type ContentDisposition: string
        :param ContentDisposition:

          Specifies presentational information for the object. For more information, see
          `http\\://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1
          <http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1>`__ .

        :type ContentEncoding: string
        :param ContentEncoding:

          Specifies what content encodings have been applied to the object and thus what decoding
          mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
          For more information, see `http\\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11
          <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11>`__ .

        :type ContentLanguage: string
        :param ContentLanguage:

          The language the content is in.

        :type ContentLength: integer
        :param ContentLength:

          Size of the body in bytes. This parameter is useful when the size of the body cannot be
          determined automatically. For more information, see
          `http\\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.13
          <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.13>`__ .

        :type ContentMD5: string
        :param ContentMD5:

          The base64-encoded 128-bit MD5 digest of the message (without the headers) according to RFC 1864.
          This header can be used as a message integrity check to verify that the data is the same data
          that was originally sent. Although it is optional, we recommend using the Content-MD5 mechanism
          as an end-to-end integrity check. For more information about REST request authentication, see
          `REST Authentication <https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html>`__
          .

        :type ContentType: string
        :param ContentType:

          A standard MIME type describing the format of the contents. For more information, see
          `http\\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17
          <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17>`__ .

        :type Expires: datetime
        :param Expires:

          The date and time at which the object is no longer cacheable. For more information, see
          `http\\://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.21
          <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.21>`__ .

        :type GrantFullControl: string
        :param GrantFullControl:

          Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

        :type GrantRead: string
        :param GrantRead:

          Allows grantee to read the object data and its metadata.

        :type GrantReadACP: string
        :param GrantReadACP:

          Allows grantee to read the object ACL.

        :type GrantWriteACP: string
        :param GrantWriteACP:

          Allows grantee to write the ACL for the applicable object.

        :type Key: string
        :param Key: **[REQUIRED]**

          Object key for which the PUT operation was initiated.

        :type Metadata: dict
        :param Metadata:

          A map of metadata to store with the object in S3.

          - *(string) --*

            - *(string) --*

        :type ServerSideEncryption: string
        :param ServerSideEncryption:

          The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).

        :type StorageClass: string
        :param StorageClass:

          If you don't specify, Standard is the default storage class. Amazon S3 supports other storage
          classes.

        :type WebsiteRedirectLocation: string
        :param WebsiteRedirectLocation:

          If the bucket is configured as a website, redirects requests for this object to another object in
          the same bucket or to an external URL. Amazon S3 stores the value of this header in the object
          metadata. For information about object metadata, see .

          In the following example, the request header sets the redirect to an object (anotherPage.html) in
          the same bucket:

           ``x-amz-website-redirect-location: /anotherPage.html``

          In the following example, the request header sets the object redirect to another website:

           ``x-amz-website-redirect-location: http://www.example.com/``

          For more information about website hosting in Amazon S3, see `Hosting Websites on Amazon S3
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html>`__ and `How to Configure
          Website Page Redirects
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html>`__ .

        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:

          Specifies the algorithm to use to when encrypting the object (e.g., AES256).

        :type SSECustomerKey: string
        :param SSECustomerKey:

          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This
          value is used to store the object and then it is discarded; Amazon does not store the encryption
          key. The key must be appropriate for use with the algorithm specified in the
          x-amz-server-side​-encryption​-customer-algorithm header.

        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:

          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this
          header for a message integrity check to ensure the encryption key was transmitted without error.

            Please note that this parameter is automatically populated if it is not provided. Including
            this parameter is not required

        :type SSEKMSKeyId: string
        :param SSEKMSKeyId:

          If the x-amz-server-side-encryption is present and has the value of aws:kms, this header
          specifies the ID of the AWS Key Management Service (AWS KMS) customer master key (CMK) that was
          used for the object.

          If the value of x-amz-server-side-encryption is aws:kms, this header specifies the ID of the AWS
          KMS CMK that will be used for the object. If you specify x-amz-server-side-encryption:aws:kms,
          but do not provide x-amz-server-side-encryption-aws-kms-key-id, Amazon S3 uses the AWS managed
          CMK in AWS to protect the data.

        :type SSEKMSEncryptionContext: string
        :param SSEKMSEncryptionContext:

          Specifies the AWS KMS Encryption Context to use for object encryption. The value of this header
          is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type Tagging: string
        :param Tagging:

          The tag-set for the object. The tag-set must be encoded as URL Query parameters. (For example,
          "Key1=Value1")

        :type ObjectLockMode: string
        :param ObjectLockMode:

          The Object Lock mode that you want to apply to this object.

        :type ObjectLockRetainUntilDate: datetime
        :param ObjectLockRetainUntilDate:

          The date and time when you want this object's Object Lock to expire.

        :type ObjectLockLegalHoldStatus: string
        :param ObjectLockLegalHoldStatus:

          Specifies whether a legal hold will be applied to this object. For more information about S3
          Object Lock, see `Object Lock
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`__ .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Expiration': 'string',
                'ETag': 'string',
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'VersionId': 'string',
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'SSEKMSEncryptionContext': 'string',
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **Expiration** *(string) --*

              If the expiration is configured for the object (see  PutBucketLifecycleConfiguration ), the
              response includes this header. It includes the expiry-date and rule-id key-value pairs that
              provide information about object expiration. The value of the rule-id is URL encoded.

            - **ETag** *(string) --*

              Entity tag for the uploaded object.

            - **ServerSideEncryption** *(string) --*

              If you specified server-side encryption either with an AWS KMS customer master key (CMK) or
              Amazon S3-managed encryption key in your PUT request, the response includes this header. It
              confirms the encryption algorithm that Amazon S3 used to encrypt the object.

            - **VersionId** *(string) --*

              Version of the object.

            - **SSECustomerAlgorithm** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header confirming the encryption algorithm used.

            - **SSECustomerKeyMD5** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header to provide round trip message integrity verification of the
              customer-provided encryption key.

            - **SSEKMSKeyId** *(string) --*

              If the x-amz-server-side-encryption is present and has the value of aws:kms, this header
              specifies the ID of the AWS Key Management Service (KMS) customer master key (CMK) that was
              used for the object.

            - **SSEKMSEncryptionContext** *(string) --*

              If present, specifies the AWS KMS Encryption Context to use for object encryption. The value
              of this header is a base64-encoded UTF-8 string holding JSON with the encryption context
              key-value pairs.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_object_acl(
        self,
        Bucket: str,
        Key: str,
        ACL: str = None,
        AccessControlPolicy: ClientPutObjectAclAccessControlPolicyTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        RequestPayer: str = None,
        VersionId: str = None,
    ) -> ClientPutObjectAclResponseTypeDef:
        """
        uses the acl subresource to set the access control list (ACL) permissions for an object that
        already exists in a bucket. You must have WRITE_ACP permission to set the ACL of an object.

        Depending on your application needs, you may choose to set the ACL on an object using either the
        request body or the headers. For example, if you have an existing application that updates a bucket
        ACL using the request body, then you can continue to use that approach.

         **Access Permissions**

        You can set access permissions using one of the following methods:

        * Specify a canned ACL with the ``x-amz-acl`` request header. Amazon S3 supports a set of
        predefined ACLs, known as canned ACLs. Each canned ACL has a predefined set of grantees and
        permissions. Specify the canned ACL name as the value of x-amz-acl. If you use this header, you
        cannot use other access control specific headers in your request. For more information, see `Canned
        ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__ .

        * Specify access permissions explicitly with the ``x-amz-grant-read`` , ``x-amz-grant-read-acp`` ,
        ``x-amz-grant-write-acp`` , and ``x-amz-grant-full-control`` headers. When using these headers you
        specify explicit access permissions and grantees (AWS accounts or a Amazon S3 groups) who will
        receive the permission. If you use these ACL specific headers, you cannot use x-amz-acl header to
        set a canned ACL. These parameters map to the set of permissions that Amazon S3 supports in an ACL.
        For more information, see `Access Control List (ACL) Overview
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html>`__ . You specify each grantee
        as a type=value pair, where the type is one of the following:

          * emailAddress – if the value specified is the email address of an AWS account

          * id – if the value specified is the canonical user ID of an AWS account

          * uri – if you are granting permissions to a predefined group

        For example, the following x-amz-grant-read header grants list objects permission to the two AWS
        accounts identified by their email addresses.

         ``x-amz-grant-read: emailAddress="xyz@amazon.com", emailAddress="abc@amazon.com"``

        You can use either a canned ACL or specify access permissions explicitly. You cannot do both.

         **Grantee Values**

        You can specify the person (grantee) to whom you're assigning access rights (using request
        elements) in the following ways:

        * By Email address:  ``<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:type="AmazonCustomerByEmail"><EmailAddress><>Grantees@email.com<></EmailAddress>lt;/Grantee>``
         The grantee is resolved to the CanonicalUser and, in a response to a GET Object acl request,
         appears as the CanonicalUser.

        * By the person's ID:  ``<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:type="CanonicalUser"><ID><>ID<></ID><DisplayName><>GranteesEmail<></DisplayName> </Grantee>``
        DisplayName is optional and ignored in the request

        * By URI:  ``<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:type=
            "Group"><URI><>http://acs.amazonaws.com/groups/global/AuthenticatedUsers<></URI></Grantee>``

         **Versioning**

        The ACL of an object is set at the object version level. By default, PUT sets the ACL of the
        current version of an object. To set the ACL of a different version, use the ``versionId``
        subresource.

         **Related Resources**

        *  CopyObject

        *  GetObject

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectAcl>`_

        **Request Syntax**
        ::

          response = client.put_object_acl(
              ACL=
                  'private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'
                  |'bucket-owner-read'|'bucket-owner-full-control',
              AccessControlPolicy={
                  'Grants': [
                      {
                          'Grantee': {
                              'DisplayName': 'string',
                              'EmailAddress': 'string',
                              'ID': 'string',
                              'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                              'URI': 'string'
                          },
                          'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                      },
                  ],
                  'Owner': {
                      'DisplayName': 'string',
                      'ID': 'string'
                  }
              },
              Bucket='string',
              GrantFullControl='string',
              GrantRead='string',
              GrantReadACP='string',
              GrantWrite='string',
              GrantWriteACP='string',
              Key='string',
              RequestPayer='requester',
              VersionId='string'
          )
        :type ACL: string
        :param ACL:

          The canned ACL to apply to the object. For more information, see `Canned ACL
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#CannedACL>`__

        :type AccessControlPolicy: dict
        :param AccessControlPolicy:

          Contains the elements that set the ACL permissions for an object per grantee.

          - **Grants** *(list) --*

            A list of grants.

            - *(dict) --*

              Container for grant information.

              - **Grantee** *(dict) --*

                The person being granted permissions.

                - **DisplayName** *(string) --*

                  Screen name of the grantee.

                - **EmailAddress** *(string) --*

                  Email address of the grantee.

                - **ID** *(string) --*

                  The canonical user ID of the grantee.

                - **Type** *(string) --* **[REQUIRED]**

                  Type of grantee

                - **URI** *(string) --*

                  URI of the grantee group.

              - **Permission** *(string) --*

                Specifies the permission given to the grantee.

          - **Owner** *(dict) --*

            Container for the bucket owner's display name and ID.

            - **DisplayName** *(string) --*

              Container for the display name of the owner

            - **ID** *(string) --*

              Container for the ID of the owner

        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket to which the ACL is being added.

        :type GrantFullControl: string
        :param GrantFullControl:

          Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

        :type GrantRead: string
        :param GrantRead:

          Allows grantee to list the objects in the bucket.

        :type GrantReadACP: string
        :param GrantReadACP:

          Allows grantee to read the bucket ACL.

        :type GrantWrite: string
        :param GrantWrite:

          Allows grantee to create, overwrite, and delete any object in the bucket.

        :type GrantWriteACP: string
        :param GrantWriteACP:

          Allows grantee to write the ACL for the applicable bucket.

        :type Key: string
        :param Key: **[REQUIRED]**

          Key for which the PUT operation was initiated.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type VersionId: string
        :param VersionId:

          VersionId used to reference a specific version of the object.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_object_legal_hold(
        self,
        Bucket: str,
        Key: str,
        LegalHold: ClientPutObjectLegalHoldLegalHoldTypeDef = None,
        RequestPayer: str = None,
        VersionId: str = None,
        ContentMD5: str = None,
    ) -> ClientPutObjectLegalHoldResponseTypeDef:
        """
        Applies a Legal Hold configuration to the specified object.

         **Related Resources**

        * `Locking Objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`__

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectLegalHold>`_

        **Request Syntax**
        ::

          response = client.put_object_legal_hold(
              Bucket='string',
              Key='string',
              LegalHold={
                  'Status': 'ON'|'OFF'
              },
              RequestPayer='requester',
              VersionId='string',
              ContentMD5='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket containing the object that you want to place a Legal Hold on.

        :type Key: string
        :param Key: **[REQUIRED]**

          The key name for the object that you want to place a Legal Hold on.

        :type LegalHold: dict
        :param LegalHold:

          Container element for the Legal Hold configuration you want to apply to the specified object.

          - **Status** *(string) --*

            Indicates whether the specified object has a Legal Hold in place.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type VersionId: string
        :param VersionId:

          The version ID of the object that you want to place a Legal Hold on.

        :type ContentMD5: string
        :param ContentMD5:

          The MD5 hash for the request body.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_object_lock_configuration(
        self,
        Bucket: str,
        ObjectLockConfiguration: ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef = None,
        RequestPayer: str = None,
        Token: str = None,
        ContentMD5: str = None,
    ) -> ClientPutObjectLockConfigurationResponseTypeDef:
        """
        Places an Object Lock configuration on the specified bucket. The rule specified in the Object Lock
        configuration will be applied by default to every new object placed in the specified bucket.

        .. note::

           ``DefaultRetention`` requires either Days or Years. You can't specify both at the same time.

         **Related Resources**

        * `Locking Objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`__

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectLockConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_object_lock_configuration(
              Bucket='string',
              ObjectLockConfiguration={
                  'ObjectLockEnabled': 'Enabled',
                  'Rule': {
                      'DefaultRetention': {
                          'Mode': 'GOVERNANCE'|'COMPLIANCE',
                          'Days': 123,
                          'Years': 123
                      }
                  }
              },
              RequestPayer='requester',
              Token='string',
              ContentMD5='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket whose Object Lock configuration you want to create or replace.

        :type ObjectLockConfiguration: dict
        :param ObjectLockConfiguration:

          The Object Lock configuration that you want to apply to the specified bucket.

          - **ObjectLockEnabled** *(string) --*

            Indicates whether this bucket has an Object Lock configuration enabled.

          - **Rule** *(dict) --*

            The Object Lock rule in place for the specified object.

            - **DefaultRetention** *(dict) --*

              The default retention period that you want to apply to new objects placed in the specified
              bucket.

              - **Mode** *(string) --*

                The default Object Lock retention mode you want to apply to new objects placed in the
                specified bucket.

              - **Days** *(integer) --*

                The number of days that you want to specify for the default retention period.

              - **Years** *(integer) --*

                The number of years that you want to specify for the default retention period.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type Token: string
        :param Token:

          A token to allow Object Lock to be enabled for an existing bucket.

        :type ContentMD5: string
        :param ContentMD5:

          The MD5 hash for the request body.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_object_retention(
        self,
        Bucket: str,
        Key: str,
        Retention: ClientPutObjectRetentionRetentionTypeDef = None,
        RequestPayer: str = None,
        VersionId: str = None,
        BypassGovernanceRetention: bool = None,
        ContentMD5: str = None,
    ) -> ClientPutObjectRetentionResponseTypeDef:
        """
        Places an Object Retention configuration on an object.

         **Related Resources**

        * `Locking Objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html>`__

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectRetention>`_

        **Request Syntax**
        ::

          response = client.put_object_retention(
              Bucket='string',
              Key='string',
              Retention={
                  'Mode': 'GOVERNANCE'|'COMPLIANCE',
                  'RetainUntilDate': datetime(2015, 1, 1)
              },
              RequestPayer='requester',
              VersionId='string',
              BypassGovernanceRetention=True|False,
              ContentMD5='string'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket that contains the object you want to apply this Object Retention configuration to.

        :type Key: string
        :param Key: **[REQUIRED]**

          The key name for the object that you want to apply this Object Retention configuration to.

        :type Retention: dict
        :param Retention:

          The container element for the Object Retention configuration.

          - **Mode** *(string) --*

            Indicates the Retention mode for the specified object.

          - **RetainUntilDate** *(datetime) --*

            The date on which this Object Lock Retention will expire.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type VersionId: string
        :param VersionId:

          The version ID for the object that you want to apply this Object Retention configuration to.

        :type BypassGovernanceRetention: boolean
        :param BypassGovernanceRetention:

          Indicates whether this operation should bypass Governance-mode restrictions.

        :type ContentMD5: string
        :param ContentMD5:

          The MD5 hash for the request body.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_object_tagging(
        self,
        Bucket: str,
        Key: str,
        Tagging: ClientPutObjectTaggingTaggingTypeDef,
        VersionId: str = None,
        ContentMD5: str = None,
    ) -> ClientPutObjectTaggingResponseTypeDef:
        """
        Sets the supplied tag-set to an object that already exists in a bucket

        A tag is a key-value pair. You can associate tags with an object by sending a PUT request against
        the tagging subresource that is associated with the object. You can retrieve tags by sending a GET
        request. For more information, see  GetObjectTagging .

        For tagging-related restrictions related to characters and encodings, see `Tag Restrictions
        <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
        . Note that Amazon S3 limits the maximum number of tags to 10 tags per object.

        To use this operation, you must have permission to perform the ``s3:PutObjectTagging`` action. By
        default, the bucket owner has this permission and can grant this permission to others.

        To put tags of any other version, use the ``versionId`` query parameter. You also need permission
        for the ``s3:PutObjectVersionTagging`` action.

        For information about the Amazon S3 object tagging feature, see `Object Tagging
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html>`__ .

         **Special Errors**

        *

          * *Code: InvalidTagError*

          * *Cause: The tag provided was not a valid tag. This error can occur if the tag did not pass
          input validation. For more information, see `Object Tagging
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html>`__ .*

        *

          * *Code: MalformedXMLError*

          * *Cause: The XML provided does not match the schema.*

        *

          * *Code: OperationAbortedError*

          * *Cause: A conflicting conditional operation is currently in progress against this resource.
          Please try again.*

        *

          * *Code: InternalError*

          * *Cause: The service was unable to apply the provided tag to the object.*

         **Related Resources**

        *  GetObjectTagging

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutObjectTagging>`_

        **Request Syntax**
        ::

          response = client.put_object_tagging(
              Bucket='string',
              Key='string',
              VersionId='string',
              ContentMD5='string',
              Tagging={
                  'TagSet': [
                      {
                          'Key': 'string',
                          'Value': 'string'
                      },
                  ]
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket containing the object.

        :type Key: string
        :param Key: **[REQUIRED]**

          Name of the tag.

        :type VersionId: string
        :param VersionId:

          The versionId of the object that the tag-set will be added to.

        :type ContentMD5: string
        :param ContentMD5:

          The MD5 hash for the request body.

        :type Tagging: dict
        :param Tagging: **[REQUIRED]**

          Container for the TagSet and Tag elements

          - **TagSet** *(list) --* **[REQUIRED]**

            A collection for a a set of tags

            - *(dict) --*

              A container of a key value name pair.

              - **Key** *(string) --* **[REQUIRED]**

                Name of the tag.

              - **Value** *(string) --* **[REQUIRED]**

                Value of the tag.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VersionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **VersionId** *(string) --*

              The versionId of the object the tag-set was added to.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_public_access_block(
        self,
        Bucket: str,
        PublicAccessBlockConfiguration: ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef,
        ContentMD5: str = None,
    ) -> None:
        """
        Creates or modifies the ``PublicAccessBlock`` configuration for an Amazon S3 bucket. In order to
        use this operation, you must have the ``s3:PutBucketPublicAccessBlock`` permission. For more
        information about Amazon S3 permissions, see `Specifying Permissions in a Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html>`__ .

        .. warning::

          When Amazon S3 evaluates the PublicAccessBlock configuration for a bucket or an object, it checks
          the PublicAccessBlock configuration for both the bucket (or the bucket that contains the object)
          and the bucket owner's account. If the PublicAccessBlock configurations are different between the
          bucket and the account, Amazon S3 uses the most restrictive combination of the bucket-level and
          account-level settings.

        For more information about when Amazon S3 considers a bucket or an object public, see `The Meaning
        of "Public"
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status>`__
        .

         **Related Resources**

        *  GetPublicAccessBlock

        *  DeletePublicAccessBlock

        *  GetBucketPolicyStatus

        * `Using Amazon S3 Block Public Access
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html>`__

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutPublicAccessBlock>`_

        **Request Syntax**
        ::

          response = client.put_public_access_block(
              Bucket='string',
              ContentMD5='string',
              PublicAccessBlockConfiguration={
                  'BlockPublicAcls': True|False,
                  'IgnorePublicAcls': True|False,
                  'BlockPublicPolicy': True|False,
                  'RestrictPublicBuckets': True|False
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the Amazon S3 bucket whose ``PublicAccessBlock`` configuration you want to set.

        :type ContentMD5: string
        :param ContentMD5:

          The MD5 hash of the ``PutPublicAccessBlock`` request body.

        :type PublicAccessBlockConfiguration: dict
        :param PublicAccessBlockConfiguration: **[REQUIRED]**

          The ``PublicAccessBlock`` configuration that you want to apply to this Amazon S3 bucket. You can
          enable the configuration options in any combination. For more information about when Amazon S3
          considers a bucket or object public, see `The Meaning of "Public"
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status>`__
          in the *Amazon Simple Storage Service Developer Guide* .

          - **BlockPublicAcls** *(boolean) --*

            Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket and
            objects in this bucket. Setting this element to ``TRUE`` causes the following behavior:

            * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.

            * PUT Object calls fail if the request includes a public ACL.

            * PUT Bucket calls fail if the request includes a public ACL.

            Enabling this setting doesn't affect existing policies or ACLs.

          - **IgnorePublicAcls** *(boolean) --*

            Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this
            bucket. Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on this
            bucket and objects in this bucket.

            Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent
            new public ACLs from being set.

          - **BlockPublicPolicy** *(boolean) --*

            Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting this
            element to ``TRUE`` causes Amazon S3 to reject calls to PUT Bucket policy if the specified
            bucket policy allows public access.

            Enabling this setting doesn't affect existing bucket policies.

          - **RestrictPublicBuckets** *(boolean) --*

            Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting
            this element to ``TRUE`` restricts access to this bucket to only AWS services and authorized
            users within this account if the bucket has a public policy.

            Enabling this setting doesn't affect previously stored bucket policies, except that public and
            cross-account access within any public bucket policy, including non-public delegation to
            specific accounts, is blocked.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_object(
        self,
        Bucket: str,
        Key: str,
        VersionId: str = None,
        RestoreRequest: ClientRestoreObjectRestoreRequestTypeDef = None,
        RequestPayer: str = None,
    ) -> ClientRestoreObjectResponseTypeDef:
        """
        Restores an archived copy of an object back into Amazon S3

        This operation performs the following types of requests:

        * ``select`` - Perform a select query on an archived object

        * ``restore an archive`` - Restore an archived object

        To use this operation, you must have permissions to perform the ``s3:RestoreObject`` and
        ``s3:GetObject`` actions. The bucket owner has this permission by default and can grant this
        permission to others. For more information about permissions, see `Permissions Related to Bucket
        Subresource Operations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`__
        and `Managing Access Permissions to Your Amazon S3 Resources
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the *Amazon Simple
        Storage Service Developer Guide* .

         **Querying Archives with Select Requests**

        You use a select type of request to perform SQL queries on archived objects. The archived objects
        that are being queried by the select request must be formatted as uncompressed comma-separated
        values (CSV) files. You can run queries and custom analytics on your archived data without having
        to restore your data to a hotter Amazon S3 tier. For an overview about select requests, see
        `Querying Archived Objects
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/querying-glacier-archives.html>`__ in the *Amazon
        Simple Storage Service Developer Guide* .

        When making a select request, do the following:

        * Define an output location for the select query's output. This must be an Amazon S3 bucket in the
        same AWS Region as the bucket that contains the archive object that is being queried. The AWS
        account that initiates the job must have permissions to write to the S3 bucket. You can specify the
        storage class and encryption for the output objects stored in the bucket. For more information
        about output, see `Querying Archived Objects
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/querying-glacier-archives.html>`__ in the *Amazon
        Simple Storage Service Developer Guide* . For more information about the ``S3`` structure in the
        request body, see the following:

          *  PutObject

          * `Managing Access with ACLs
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html>`__ in the *Amazon Simple
          Storage Service Developer Guide*

          * `Protecting Data Using Server-Side Encryption
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the *Amazon
          Simple Storage Service Developer Guide*

        * Define the SQL expression for the ``SELECT`` type of restoration for your query in the request
        body's ``SelectParameters`` structure. You can use expressions like the following examples.

          * The following expression returns all records from the specified object.  ``SELECT * FROM
          Object``

          * Assuming that you are not using any headers for data stored in the object, you can specify
          columns with positional headers.  ``SELECT s._1, s._2 FROM Object s WHERE s._3 > 100``

          * If you have headers and you set the ``fileHeaderInfo`` in the ``CSV`` structure in the request
          body to ``USE`` , you can specify headers in the query. (If you set the ``fileHeaderInfo`` field
          to ``IGNORE`` , the first row is skipped for the query.) You cannot mix ordinal positions with
          header column names.   ``SELECT s.Id, s.FirstName, s.SSN FROM S3Object s``

        For more information about using SQL with Glacier Select restore, see `SQL Reference for Amazon S3
        Select and Glacier Select
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-glacier-select-sql-reference.html>`__ in the
        *Amazon Simple Storage Service Developer Guide* .

        When making a select request, you can also do the following:

        * To expedite your queries, specify the ``Expedited`` tier. For more information about tiers, see
        "Restoring Archives," later in this topic.

        * Specify details about the data serialization format of both the input object that is being
        queried and the serialization of the CSV-encoded query results.

        The following are additional important facts about the select feature:

        * The output results are new Amazon S3 objects. Unlike archive retrievals, they are stored until
        explicitly deleted-manually or through a lifecycle policy.

        * You can issue more than one select request on the same Amazon S3 object. Amazon S3 doesn't
        deduplicate requests, so avoid issuing duplicate requests.

        * Amazon S3 accepts a select request even if the object has already been restored. A select request
        doesn’t return error response ``409`` .

         **Restoring Archives**

        Objects in the GLACIER and DEEP_ARCHIVE storage classes are archived. To access an archived object,
        you must first initiate a restore request. This restores a temporary copy of the archived object.
        In a restore request, you specify the number of days that you want the restored copy to exist.
        After the specified period, Amazon S3 deletes the temporary copy but the object remains archived in
        the GLACIER or DEEP_ARCHIVE storage class that object was restored from.

        To restore a specific object version, you can provide a version ID. If you don't provide a version
        ID, Amazon S3 restores the current version.

        The time it takes restore jobs to finish depends on which storage class the object is being
        restored from and which data access tier you specify.

        When restoring an archived object (or using a select request), you can specify one of the following
        data access tier options in the ``Tier`` element of the request body:

        * **``Expedited`` ** - Expedited retrievals allow you to quickly access your data stored in the
        GLACIER storage class when occasional urgent requests for a subset of archives are required. For
        all but the largest archived objects (250 MB+), data accessed using Expedited retrievals are
        typically made available within 1–5 minutes. Provisioned capacity ensures that retrieval capacity
        for Expedited retrievals is available when you need it. Expedited retrievals and provisioned
        capacity are not available for the DEEP_ARCHIVE storage class.

        * **``Standard`` ** - Standard retrievals allow you to access any of your archived objects within
        several hours. This is the default option for the GLACIER and DEEP_ARCHIVE retrieval requests that
        do not specify the retrieval option. Standard retrievals typically complete within 3-5 hours from
        the GLACIER storage class and typically complete within 12 hours from the DEEP_ARCHIVE storage
        class.

        * **``Bulk`` ** - Bulk retrievals are Amazon Glacier’s lowest-cost retrieval option, enabling you
        to retrieve large amounts, even petabytes, of data inexpensively in a day. Bulk retrievals
        typically complete within 5-12 hours from the GLACIER storage class and typically complete within
        48 hours from the DEEP_ARCHIVE storage class.

        For more information about archive retrieval options and provisioned capacity for ``Expedited``
        data access, see `Restoring Archived Objects
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/restoring-objects.html>`__ in the *Amazon Simple
        Storage Service Developer Guide* .

        You can use Amazon S3 restore speed upgrade to change the restore speed to a faster speed while it
        is in progress. You upgrade the speed of an in-progress restoration by issuing another restore
        request to the same object, setting a new ``Tier`` request element. When issuing a request to
        upgrade the restore tier, you must choose a tier that is faster than the tier that the in-progress
        restore is using. You must not change any other parameters, such as the ``Days`` request element.
        For more information, see `Upgrading the Speed of an In-Progress Restore
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/restoring-objects.html#restoring-objects-upgrade-tier.title.html>`__
        in the *Amazon Simple Storage Service Developer Guide* .

        To get the status of object restoration, you can send a ``HEAD`` request. Operations return the
        ``x-amz-restore`` header, which provides information about the restoration status, in the response.
        You can use Amazon S3 event notifications to notify you when a restore is initiated or completed.
        For more information, see `Configuring Amazon S3 Event Notifications
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>`__ in the *Amazon Simple
        Storage Service Developer Guide* .

        After restoring an archived object, you can update the restoration period by reissuing the request
        with a new period. Amazon S3 updates the restoration period relative to the current time and
        charges only for the request-there are no data transfer charges. You cannot update the restoration
        period when Amazon S3 is actively processing your current restore request for the object.

        If your bucket has a lifecycle configuration with a rule that includes an expiration action, the
        object expiration overrides the life span that you specify in a restore request. For example, if
        you restore an object copy for 10 days, but the object is scheduled to expire in 3 days, Amazon S3
        deletes the object in 3 days. For more information about lifecycle configuration, see
        PutBucketLifecycleConfiguration and `Object Lifecycle Management
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html>`__ in *Amazon Simple
        Storage Service Developer Guide* .

         **Responses**

        A successful operation returns either the ``200 OK`` or ``202 Accepted`` status code.

        * If the object copy is not previously restored, then Amazon S3 returns ``202 Accepted`` in the
        response.

        * If the object copy is previously restored, Amazon S3 returns ``200 OK`` in the response.

         **Special Errors**

        *

          * *Code: RestoreAlreadyInProgress*

          * *Cause: Object restore is already in progress. (This error does not apply to SELECT type
          requests.)*

          * *HTTP Status Code: 409 Conflict*

          * *SOAP Fault Code Prefix: Client*

        *

          * *Code: GlacierExpeditedRetrievalNotAvailable*

          * *Cause: Glacier expedited retrievals are currently not available. Try again later. (Returned if
          there is insufficient capacity to process the Expedited request. This error applies only to
          Expedited retrievals and not to Standard or Bulk retrievals.)*

          * *HTTP Status Code: 503*

          * *SOAP Fault Code Prefix: N/A*

         **Related Resources**

        *  PutBucketLifecycleConfiguration

        *  GetBucketNotificationConfiguration

        * `SQL Reference for Amazon S3 Select and Glacier Select
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-glacier-select-sql-reference.html>`__ in the
        *Amazon Simple Storage Service Developer Guide*

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/RestoreObject>`_

        **Request Syntax**
        ::

          response = client.restore_object(
              Bucket='string',
              Key='string',
              VersionId='string',
              RestoreRequest={
                  'Days': 123,
                  'GlacierJobParameters': {
                      'Tier': 'Standard'|'Bulk'|'Expedited'
                  },
                  'Type': 'SELECT',
                  'Tier': 'Standard'|'Bulk'|'Expedited',
                  'Description': 'string',
                  'SelectParameters': {
                      'InputSerialization': {
                          'CSV': {
                              'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                              'Comments': 'string',
                              'QuoteEscapeCharacter': 'string',
                              'RecordDelimiter': 'string',
                              'FieldDelimiter': 'string',
                              'QuoteCharacter': 'string',
                              'AllowQuotedRecordDelimiter': True|False
                          },
                          'CompressionType': 'NONE'|'GZIP'|'BZIP2',
                          'JSON': {
                              'Type': 'DOCUMENT'|'LINES'
                          },
                          'Parquet': {}

                      },
                      'ExpressionType': 'SQL',
                      'Expression': 'string',
                      'OutputSerialization': {
                          'CSV': {
                              'QuoteFields': 'ALWAYS'|'ASNEEDED',
                              'QuoteEscapeCharacter': 'string',
                              'RecordDelimiter': 'string',
                              'FieldDelimiter': 'string',
                              'QuoteCharacter': 'string'
                          },
                          'JSON': {
                              'RecordDelimiter': 'string'
                          }
                      }
                  },
                  'OutputLocation': {
                      'S3': {
                          'BucketName': 'string',
                          'Prefix': 'string',
                          'Encryption': {
                              'EncryptionType': 'AES256'|'aws:kms',
                              'KMSKeyId': 'string',
                              'KMSContext': 'string'
                          },
                          'CannedACL':
                          'private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'
                          |'bucket-owner-read'|'bucket-owner-full-control',
                          'AccessControlList': [
                              {
                                  'Grantee': {
                                      'DisplayName': 'string',
                                      'EmailAddress': 'string',
                                      'ID': 'string',
                                      'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
                                      'URI': 'string'
                                  },
                                  'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                              },
                          ],
                          'Tagging': {
                              'TagSet': [
                                  {
                                      'Key': 'string',
                                      'Value': 'string'
                                  },
                              ]
                          },
                          'UserMetadata': [
                              {
                                  'Name': 'string',
                                  'Value': 'string'
                              },
                          ],
                          'StorageClass':
                          'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'
                          |'GLACIER'|'DEEP_ARCHIVE'
                      }
                  }
              },
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name.

        :type Key: string
        :param Key: **[REQUIRED]**

          Object key for which the operation was initiated.

        :type VersionId: string
        :param VersionId:

          VersionId used to reference a specific version of the object.

        :type RestoreRequest: dict
        :param RestoreRequest:

          Container for restore job parameters.

          - **Days** *(integer) --*

            Lifetime of the active copy in days. Do not use with restores that specify OutputLocation.

          - **GlacierJobParameters** *(dict) --*

            Glacier related parameters pertaining to this job. Do not use with restores that specify
            OutputLocation.

            - **Tier** *(string) --* **[REQUIRED]**

              Glacier retrieval tier at which the restore will be processed.

          - **Type** *(string) --*

            Type of restore request.

          - **Tier** *(string) --*

            Glacier retrieval tier at which the restore will be processed.

          - **Description** *(string) --*

            The optional description for the job.

          - **SelectParameters** *(dict) --*

            Describes the parameters for Select job types.

            - **InputSerialization** *(dict) --* **[REQUIRED]**

              Describes the serialization format of the object.

              - **CSV** *(dict) --*

                Describes the serialization of a CSV-encoded object.

                - **FileHeaderInfo** *(string) --*

                  Describes the first line of input. Valid values are:

                  * ``NONE`` : First line is not a header.

                  * ``IGNORE`` : First line is a header, but you can't use the header values to indicate
                  the column in an expression. You can use column position (such as _1, _2, …) to indicate
                  the column (``SELECT s._1 FROM OBJECT s`` ).

                  * ``Use`` : First line is a header, and you can use the header value to identify a column
                  in an expression (``SELECT "name" FROM OBJECT`` ).

                - **Comments** *(string) --*

                  A single character used to indicate that a row should be ignored when the character is
                  present at the start of that row. You can specify any character to indicate a comment
                  line.

                - **QuoteEscapeCharacter** *(string) --*

                  A single character used for escaping the quotation mark character inside an already
                  escaped value. For example, the value ''' a , b ''' is parsed as " a , b ".

                - **RecordDelimiter** *(string) --*

                  A single character used to separate individual records in the input. Instead of the
                  default value, you can specify an arbitrary delimiter.

                - **FieldDelimiter** *(string) --*

                  A single character used to separate individual fields in a record. You can specify an
                  arbitrary delimiter.

                - **QuoteCharacter** *(string) --*

                  A single character used for escaping when the field delimiter is part of the value. For
                  example, if the value is ``a, b`` , Amazon S3 wraps this field value in quotation marks,
                  as follows: ``" a , b "`` .

                  Type: String

                  Default: ``"``

                  Ancestors: ``CSV``

                - **AllowQuotedRecordDelimiter** *(boolean) --*

                  Specifies that CSV field values may contain quoted record delimiters and such records
                  should be allowed. Default value is FALSE. Setting this value to TRUE may lower
                  performance.

              - **CompressionType** *(string) --*

                Specifies object's compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.

              - **JSON** *(dict) --*

                Specifies JSON as object's input serialization format.

                - **Type** *(string) --*

                  The type of JSON. Valid values: Document, Lines.

              - **Parquet** *(dict) --*

                Specifies Parquet as object's input serialization format.

            - **ExpressionType** *(string) --* **[REQUIRED]**

              The type of the provided expression (e.g., SQL).

            - **Expression** *(string) --* **[REQUIRED]**

              The expression that is used to query the object.

            - **OutputSerialization** *(dict) --* **[REQUIRED]**

              Describes how the results of the Select job are serialized.

              - **CSV** *(dict) --*

                Describes the serialization of CSV-encoded Select results.

                - **QuoteFields** *(string) --*

                  Indicates whether to use quotation marks around output fields.

                  * ``ALWAYS`` : Always use quotation marks for output fields.

                  * ``ASNEEDED`` : Use quotation marks for output fields when needed.

                - **QuoteEscapeCharacter** *(string) --*

                  The single character used for escaping the quote character inside an already escaped
                  value.

                - **RecordDelimiter** *(string) --*

                  A single character used to separate individual records in the output. Instead of the
                  default value, you can specify an arbitrary delimiter.

                - **FieldDelimiter** *(string) --*

                  The value used to separate individual fields in a record. You can specify an arbitrary
                  delimiter.

                - **QuoteCharacter** *(string) --*

                  A single character used for escaping when the field delimiter is part of the value. For
                  example, if the value is ``a, b`` , Amazon S3 wraps this field value in quotation marks,
                  as follows: ``" a , b "`` .

              - **JSON** *(dict) --*

                Specifies JSON as request's output serialization format.

                - **RecordDelimiter** *(string) --*

                  The value used to separate individual records in the output.

          - **OutputLocation** *(dict) --*

            Describes the location where the restore job's output is stored.

            - **S3** *(dict) --*

              Describes an S3 location that will receive the results of the restore request.

              - **BucketName** *(string) --* **[REQUIRED]**

                The name of the bucket where the restore results will be placed.

              - **Prefix** *(string) --* **[REQUIRED]**

                The prefix that is prepended to the restore results for this request.

              - **Encryption** *(dict) --*

                Contains the type of server-side encryption used.

                - **EncryptionType** *(string) --* **[REQUIRED]**

                  The server-side encryption algorithm used when storing job results in Amazon S3 (e.g.,
                  AES256, aws:kms).

                - **KMSKeyId** *(string) --*

                  If the encryption type is aws:kms, this optional value specifies the AWS KMS key ID to
                  use for encryption of job results.

                - **KMSContext** *(string) --*

                  If the encryption type is aws:kms, this optional value can be used to specify the
                  encryption context for the restore results.

              - **CannedACL** *(string) --*

                The canned ACL to apply to the restore results.

              - **AccessControlList** *(list) --*

                A list of grants that control access to the staged results.

                - *(dict) --*

                  Container for grant information.

                  - **Grantee** *(dict) --*

                    The person being granted permissions.

                    - **DisplayName** *(string) --*

                      Screen name of the grantee.

                    - **EmailAddress** *(string) --*

                      Email address of the grantee.

                    - **ID** *(string) --*

                      The canonical user ID of the grantee.

                    - **Type** *(string) --* **[REQUIRED]**

                      Type of grantee

                    - **URI** *(string) --*

                      URI of the grantee group.

                  - **Permission** *(string) --*

                    Specifies the permission given to the grantee.

              - **Tagging** *(dict) --*

                The tag-set that is applied to the restore results.

                - **TagSet** *(list) --* **[REQUIRED]**

                  A collection for a a set of tags

                  - *(dict) --*

                    A container of a key value name pair.

                    - **Key** *(string) --* **[REQUIRED]**

                      Name of the tag.

                    - **Value** *(string) --* **[REQUIRED]**

                      Value of the tag.

              - **UserMetadata** *(list) --*

                A list of metadata to store with the restore results in S3.

                - *(dict) --*

                  A metadata key-value pair to store with an object.

                  - **Name** *(string) --*

                    Name of the Object.

                  - **Value** *(string) --*

                    Value of the Object.

              - **StorageClass** *(string) --*

                The class of storage used to store the restore results.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestCharged': 'requester',
                'RestoreOutputPath': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

            - **RestoreOutputPath** *(string) --*

              Indicates the path in the provided S3 output location where Select results will be restored
              to.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def select_object_content(
        self,
        Bucket: str,
        Key: str,
        Expression: str,
        ExpressionType: str,
        InputSerialization: ClientSelectObjectContentInputSerializationTypeDef,
        OutputSerialization: ClientSelectObjectContentOutputSerializationTypeDef,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestProgress: ClientSelectObjectContentRequestProgressTypeDef = None,
        ScanRange: ClientSelectObjectContentScanRangeTypeDef = None,
    ) -> Dict:
        """
        This operation filters the contents of an Amazon S3 object based on a simple structured query
        language (SQL) statement. In the request, along with the SQL expression, you must also specify a
        data serialization format (JSON, CSV, or Apache Parquet) of the object. Amazon S3 uses this format
        to parse object data into records, and returns only records that match the specified SQL
        expression. You must also specify the data serialization format for the response.

        For more information about Amazon S3 Select, see `Selecting Content from Objects
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/selecting-content-from-objects.html>`__ in the
        *Amazon Simple Storage Service Developer Guide* .

        For more information about using SQL with Amazon S3 Select, see `SQL Reference for Amazon S3 Select
        and Glacier Select
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-glacier-select-sql-reference.html>`__ in the
        *Amazon Simple Storage Service Developer Guide* .

         **Permissions**

        You must have ``s3:GetObject`` permission for this operation. Amazon S3 Select does not support
        anonymous access. For more information about permissions, see `Specifying Permissions in a Policy
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html>`__ in the *Amazon
        Simple Storage Service Developer Guide* .

         *Object Data Formats*

        You can use Amazon S3 Select to query objects that have the following format properties:

        * *CSV, JSON, and Parquet* - Objects must be in CSV, JSON, or Parquet format.

        * *UTF-8* - UTF-8 is the only encoding type Amazon S3 Select supports.

        * *GZIP or BZIP2* - CSV and JSON files can be compressed using GZIP or BZIP2. GZIP and BZIP2 are
        the only compression formats that Amazon S3 Select supports for CSV and JSON files. Amazon S3
        Select supports columnar compression for Parquet using GZIP or Snappy. Amazon S3 Select does not
        support whole-object compression for Parquet objects.

        * *Server-side encryption* - Amazon S3 Select supports querying objects that are protected with
        server-side encryption. For objects that are encrypted with customer-provided encryption keys
        (SSE-C), you must use HTTPS, and you must use the headers that are documented in the  GetObject .
        For more information about SSE-C, see `Server-Side Encryption (Using Customer-Provided Encryption
        Keys) <https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html>`__ in
        the *Amazon Simple Storage Service Developer Guide* . For objects that are encrypted with Amazon S3
        managed encryption keys (SSE-S3) and customer master keys (CMKs) stored in AWS Key Management
        Service (SSE-KMS), server-side encryption is handled transparently, so you don't need to specify
        anything. For more information about server-side encryption, including SSE-S3 and SSE-KMS, see
        `Protecting Data Using Server-Side Encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the *Amazon
        Simple Storage Service Developer Guide* .

         **Working with the Response Body**

        Given the response size is unknown, Amazon S3 Select streams the response as a series of messages
        and includes a ``Transfer-Encoding`` header with ``chunked`` as its value in the response. For more
        information, see  RESTSelectObjectAppendix .

         **GetObject Support**

        The ``SelectObjectContent`` operation does not support the following ``GetObject`` functionality.
        For more information, see  GetObject .

        * ``Range`` : While you can specify a scan range for a Amazon S3 Select request, see
        SelectObjectContentRequest$ScanRange in the request parameters below, you cannot specify the range
        of bytes of an object to return.

        * GLACIER, DEEP_ARCHIVE and REDUCED_REDUNDANCY storage classes: You cannot specify the GLACIER,
        DEEP_ARCHIVE, or ``REDUCED_REDUNDANCY`` storage classes. For more information, about storage
        classes see `Storage Classes
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#storage-class-intro>`__ in the
        *Amazon Simple Storage Service Developer Guide* .

         **Special Errors**

        For a list of special errors for this operation and for general information about Amazon S3 errors
        and a list of error codes, see  ErrorResponses

         **Related Resources**

        *  GetObject

        *  GetBucketLifecycleConfiguration

        *  PutBucketLifecycleConfiguration

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/SelectObjectContent>`_

        **Request Syntax**
        ::

          response = client.select_object_content(
              Bucket='string',
              Key='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              Expression='string',
              ExpressionType='SQL',
              RequestProgress={
                  'Enabled': True|False
              },
              InputSerialization={
                  'CSV': {
                      'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                      'Comments': 'string',
                      'QuoteEscapeCharacter': 'string',
                      'RecordDelimiter': 'string',
                      'FieldDelimiter': 'string',
                      'QuoteCharacter': 'string',
                      'AllowQuotedRecordDelimiter': True|False
                  },
                  'CompressionType': 'NONE'|'GZIP'|'BZIP2',
                  'JSON': {
                      'Type': 'DOCUMENT'|'LINES'
                  },
                  'Parquet': {}

              },
              OutputSerialization={
                  'CSV': {
                      'QuoteFields': 'ALWAYS'|'ASNEEDED',
                      'QuoteEscapeCharacter': 'string',
                      'RecordDelimiter': 'string',
                      'FieldDelimiter': 'string',
                      'QuoteCharacter': 'string'
                  },
                  'JSON': {
                      'RecordDelimiter': 'string'
                  }
              },
              ScanRange={
                  'Start': 123,
                  'End': 123
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The S3 bucket.

        :type Key: string
        :param Key: **[REQUIRED]**

          The object key.

        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:

          The SSE Algorithm used to encrypt the object. For more information, see `Server-Side Encryption
          (Using Customer-Provided Encryption Keys
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html>`__ .

        :type SSECustomerKey: string
        :param SSECustomerKey:

          The SSE Customer Key. For more information, see `Server-Side Encryption (Using Customer-Provided
          Encryption Keys
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html>`__ .

        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:

          The SSE Customer Key MD5. For more information, see `Server-Side Encryption (Using
          Customer-Provided Encryption Keys
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html>`__ .

            Please note that this parameter is automatically populated if it is not provided. Including
            this parameter is not required

        :type Expression: string
        :param Expression: **[REQUIRED]**

          The expression that is used to query the object.

        :type ExpressionType: string
        :param ExpressionType: **[REQUIRED]**

          The type of the provided expression (for example., SQL).

        :type RequestProgress: dict
        :param RequestProgress:

          Specifies if periodic request progress information should be enabled.

          - **Enabled** *(boolean) --*

            Specifies whether periodic QueryProgress frames should be sent. Valid values: TRUE, FALSE.
            Default value: FALSE.

        :type InputSerialization: dict
        :param InputSerialization: **[REQUIRED]**

          Describes the format of the data in the object that is being queried.

          - **CSV** *(dict) --*

            Describes the serialization of a CSV-encoded object.

            - **FileHeaderInfo** *(string) --*

              Describes the first line of input. Valid values are:

              * ``NONE`` : First line is not a header.

              * ``IGNORE`` : First line is a header, but you can't use the header values to indicate the
              column in an expression. You can use column position (such as _1, _2, …) to indicate the
              column (``SELECT s._1 FROM OBJECT s`` ).

              * ``Use`` : First line is a header, and you can use the header value to identify a column in
              an expression (``SELECT "name" FROM OBJECT`` ).

            - **Comments** *(string) --*

              A single character used to indicate that a row should be ignored when the character is
              present at the start of that row. You can specify any character to indicate a comment line.

            - **QuoteEscapeCharacter** *(string) --*

              A single character used for escaping the quotation mark character inside an already escaped
              value. For example, the value ''' a , b ''' is parsed as " a , b ".

            - **RecordDelimiter** *(string) --*

              A single character used to separate individual records in the input. Instead of the default
              value, you can specify an arbitrary delimiter.

            - **FieldDelimiter** *(string) --*

              A single character used to separate individual fields in a record. You can specify an
              arbitrary delimiter.

            - **QuoteCharacter** *(string) --*

              A single character used for escaping when the field delimiter is part of the value. For
              example, if the value is ``a, b`` , Amazon S3 wraps this field value in quotation marks, as
              follows: ``" a , b "`` .

              Type: String

              Default: ``"``

              Ancestors: ``CSV``

            - **AllowQuotedRecordDelimiter** *(boolean) --*

              Specifies that CSV field values may contain quoted record delimiters and such records should
              be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.

          - **CompressionType** *(string) --*

            Specifies object's compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.

          - **JSON** *(dict) --*

            Specifies JSON as object's input serialization format.

            - **Type** *(string) --*

              The type of JSON. Valid values: Document, Lines.

          - **Parquet** *(dict) --*

            Specifies Parquet as object's input serialization format.

        :type OutputSerialization: dict
        :param OutputSerialization: **[REQUIRED]**

          Describes the format of the data that you want Amazon S3 to return in response.

          - **CSV** *(dict) --*

            Describes the serialization of CSV-encoded Select results.

            - **QuoteFields** *(string) --*

              Indicates whether to use quotation marks around output fields.

              * ``ALWAYS`` : Always use quotation marks for output fields.

              * ``ASNEEDED`` : Use quotation marks for output fields when needed.

            - **QuoteEscapeCharacter** *(string) --*

              The single character used for escaping the quote character inside an already escaped value.

            - **RecordDelimiter** *(string) --*

              A single character used to separate individual records in the output. Instead of the default
              value, you can specify an arbitrary delimiter.

            - **FieldDelimiter** *(string) --*

              The value used to separate individual fields in a record. You can specify an arbitrary
              delimiter.

            - **QuoteCharacter** *(string) --*

              A single character used for escaping when the field delimiter is part of the value. For
              example, if the value is ``a, b`` , Amazon S3 wraps this field value in quotation marks, as
              follows: ``" a , b "`` .

          - **JSON** *(dict) --*

            Specifies JSON as request's output serialization format.

            - **RecordDelimiter** *(string) --*

              The value used to separate individual records in the output.

        :type ScanRange: dict
        :param ScanRange:

          Specifies the byte range of the object to get the records from. A record is processed when its
          first byte is contained by the range. This parameter is optional, but when specified, it must not
          be empty. See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.

           ``ScanRange`` may be used in the following ways:

          * ``<scanrange><start>50</start><end>100</end></scanrange>`` - process only the records starting
          between the bytes 50 and 100 (inclusive, counting from zero)

          * ``<scanrange><start>50</start></scanrange>`` - process only the records starting after the byte
          50

          * ``<scanrange><end>50</end></scanrange>`` - process only the records within the last 50 bytes of
          the file.

          - **Start** *(integer) --*

            Specifies the start of the byte range. This parameter is optional. Valid values: non-negative
            integers. The default value is 0. If only start is supplied, it means scan from that point to
            the end of the file.For example; ``<scanrange><start>50</start></scanrange>`` means scan from
            byte 50 until the end of the file.

          - **End** *(integer) --*

            Specifies the end of the byte range. This parameter is optional. Valid values: non-negative
            integers. The default value is one less than the size of the object being queried. If only the
            End parameter is supplied, it is interpreted to mean scan the last N bytes of the file. For
            example; ``<scanrange><end>50</end></scanrange>`` means scan the last 50 bytes.

        :rtype: dict
        :returns:

          The response of this operation contains an :class:`.EventStream` member. When iterated the
          :class:`.EventStream` will yield events based on the structure below, where only one of the top
          level keys will be present for any given event.

          **Response Syntax**

          ::

            {
                'Payload': EventStream({
                    'Records': {
                        'Payload': b'bytes'
                    },
                    'Stats': {
                        'Details': {
                            'BytesScanned': 123,
                            'BytesProcessed': 123,
                            'BytesReturned': 123
                        }
                    },
                    'Progress': {
                        'Details': {
                            'BytesScanned': 123,
                            'BytesProcessed': 123,
                            'BytesReturned': 123
                        }
                    },
                    'Cont': {},
                    'End': {}
                })
            }
          **Response Structure**

          - *(dict) --*

            - **Payload** (:class:`.EventStream`) --

              The array of results.

              - **Records** *(dict) --*

                The Records Event.

                - **Payload** *(bytes) --*

                  The byte array of partial, one or more result records.

              - **Stats** *(dict) --*

                The Stats Event.

                - **Details** *(dict) --*

                  The Stats event details.

                  - **BytesScanned** *(integer) --*

                    The total number of object bytes scanned.

                  - **BytesProcessed** *(integer) --*

                    The total number of uncompressed object bytes processed.

                  - **BytesReturned** *(integer) --*

                    The total number of bytes of records payload data returned.

              - **Progress** *(dict) --*

                The Progress Event.

                - **Details** *(dict) --*

                  The Progress event details.

                  - **BytesScanned** *(integer) --*

                    The current number of object bytes scanned.

                  - **BytesProcessed** *(integer) --*

                    The current number of uncompressed object bytes processed.

                  - **BytesReturned** *(integer) --*

                    The current number of bytes of records payload data returned.

              - **Cont** *(dict) --*

                The Continuation Event.

              - **End** *(dict) --*

                The End Event.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_file(
        self,
        Filename: str,
        Bucket: str,
        Key: str,
        ExtraArgs: Dict = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Upload a file to an S3 object.

        Usage::

            import boto3
            s3 = boto3.resource('s3')
            s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')

        Similar behavior as S3Transfer's upload_file() method,
        except that parameters are capitalized. Detailed examples can be found at
        :ref:`S3Transfer's Usage <ref_s3transfer_usage>`.

        :type Filename: str
        :param Filename: The path to the file to upload.

        :type Bucket: str
        :param Bucket: The name of the bucket to upload to.

        :type Key: str
        :param Key: The name of the key to upload to.

        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.

        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the upload.

        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            transfer.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_fileobj(
        self,
        Fileobj: IO[Any],
        Bucket: str,
        Key: str,
        ExtraArgs: Dict = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Upload a file-like object to S3.

        The file-like object must be in binary mode.

        This is a managed transfer which will perform a multipart upload in
        multiple threads if necessary.

        Usage::

            import boto3
            s3 = boto3.client('s3')

            with open('filename', 'rb') as data:
                s3.upload_fileobj(data, 'mybucket', 'mykey')

        :type Fileobj: a file-like object
        :param Fileobj: A file-like object to upload. At a minimum, it must
            implement the `read` method, and must return bytes.

        :type Bucket: str
        :param Bucket: The name of the bucket to upload to.

        :type Key: str
        :param Key: The name of the key to upload to.

        :type ExtraArgs: dict
        :param ExtraArgs: Extra arguments that may be passed to the
            client operation.

        :type Callback: function
        :param Callback: A method which takes a number of bytes transferred to
            be periodically called during the upload.

        :type Config: boto3.s3.transfer.TransferConfig
        :param Config: The transfer configuration to be used when performing the
            upload.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_part(
        self,
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
    ) -> ClientUploadPartResponseTypeDef:
        """
        Uploads a part in a multipart upload.

        .. note::

          In this operation, you provide part data in your request. However, you have an option to specify
          your existing Amazon S3 object as a data source for the part you are uploading. To upload a part
          from an existing object, you use the  UploadPartCopy operation.

        You must initiate a multipart upload (see  CreateMultipartUpload ) before you can upload any part.
        In response to your initiate request, Amazon S3 returns an upload ID, a unique identifier, that you
        must include in your upload part request.

        Part numbers can be any number from 1 to 10,000, inclusive. A part number uniquely identifies a
        part and also defines its position within the object being created. If you upload a new part using
        the same part number that was used with a previous part, the previously uploaded part is
        overwritten. Each part must be at least 5 MB in size, except the last part. There is no size limit
        on the last part of your multipart upload.

        To ensure that data is not corrupted when traversing the network, specify the ``Content-MD5``
        header in the upload part request. Amazon S3 checks the part data against the provided MD5 value.
        If they do not match, Amazon S3 returns an error.

         **Note:** After you initiate multipart upload and upload one or more parts, you must either
         complete or abort multipart upload in order to stop getting charged for storage of the uploaded
         parts. Only after you either complete or abort multipart upload, Amazon S3 frees up the parts
         storage and stops charging you for the parts storage.

        For more information on multipart uploads, go to `Multipart Upload Overview
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>`__ in the *Amazon Simple Storage
        Service Developer Guide* .

        For information on the permissions required to use the multipart upload API, go to `Multipart
        Upload API and Permissions
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html>`__ in the *Amazon Simple
        Storage Service Developer Guide* .

        You can optionally request server-side encryption where Amazon S3 encrypts your data as it writes
        it to disks in its data centers and decrypts it for you when you access it. You have the option of
        providing your own encryption key, or you can use the AWS-managed encryption keys. If you choose to
        provide your own encryption key, the request headers you provide in the request must match the
        headers you used in the request to initiate the upload by using  CreateMultipartUpload . For more
        information, go to `Using Server-Side Encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html>`__ in the *Amazon
        Simple Storage Service Developer Guide* .

        Server-side encryption is supported by the S3 Multipart Upload actions. Unless you are using a
        customer-provided encryption key, you don't need to specify the encryption parameters in each
        UploadPart request. Instead, you only need to specify the server side encryption parameters in the
        initial Initiate Multipart request. For more information, see  CreateMultipartUpload .

        If you requested server-side encryption using a customer-provided encryption key in your initiate
        multipart upload request, you must provide identical encryption information in each part upload
        using the following headers.

        * x-amz-server-side​-encryption​-customer-algorithm

        * x-amz-server-side​-encryption​-customer-key

        * x-amz-server-side​-encryption​-customer-key-MD5

         **Special Errors**

        *

          * *Code: NoSuchUpload*

          * *Cause: The specified multipart upload does not exist. The upload ID might be invalid, or the
          multipart upload might have been aborted or completed.*

          * *HTTP Status Code: 404 Not Found*

          * *SOAP Fault Code Prefix: Client*

         **Related Resources**

        *  CreateMultipartUpload

        *  CompleteMultipartUpload

        *  AbortMultipartUpload

        *  ListParts

        *  ListMultipartUploads

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/UploadPart>`_

        **Request Syntax**
        ::

          response = client.upload_part(
              Body=b'bytes'|file,
              Bucket='string',
              ContentLength=123,
              ContentMD5='string',
              Key='string',
              PartNumber=123,
              UploadId='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              RequestPayer='requester'
          )
        :type Body: bytes or seekable file-like object
        :param Body:

          Object data.

        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket to which the multipart upload was initiated.

        :type ContentLength: integer
        :param ContentLength:

          Size of the body in bytes. This parameter is useful when the size of the body cannot be
          determined automatically.

        :type ContentMD5: string
        :param ContentMD5:

          The base64-encoded 128-bit MD5 digest of the part data. This parameter is auto-populated when
          using the command from the CLI. This parameted is required if object lock parameters are
          specified.

        :type Key: string
        :param Key: **[REQUIRED]**

          Object key for which the multipart upload was initiated.

        :type PartNumber: integer
        :param PartNumber: **[REQUIRED]**

          Part number of part being uploaded. This is a positive integer between 1 and 10,000.

        :type UploadId: string
        :param UploadId: **[REQUIRED]**

          Upload ID identifying the multipart upload whose part is being uploaded.

        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:

          Specifies the algorithm to use to when encrypting the object (e.g., AES256).

        :type SSECustomerKey: string
        :param SSECustomerKey:

          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This
          value is used to store the object and then it is discarded; Amazon does not store the encryption
          key. The key must be appropriate for use with the algorithm specified in the
          x-amz-server-side​-encryption​-customer-algorithm header. This must be the same encryption key
          specified in the initiate multipart upload request.

        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:

          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this
          header for a message integrity check to ensure the encryption key was transmitted without error.

            Please note that this parameter is automatically populated if it is not provided. Including
            this parameter is not required

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'ETag': 'string',
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **ServerSideEncryption** *(string) --*

              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256,
              aws:kms).

            - **ETag** *(string) --*

              Entity tag for the uploaded object.

            - **SSECustomerAlgorithm** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header confirming the encryption algorithm used.

            - **SSECustomerKeyMD5** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header to provide round trip message integrity verification of the
              customer-provided encryption key.

            - **SSEKMSKeyId** *(string) --*

              If present, specifies the ID of the AWS Key Management Service (KMS) customer master key
              (CMK) was used for the object.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_part_copy(
        self,
        Bucket: str,
        CopySource: Union[S3CopySource, str],
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
    ) -> ClientUploadPartCopyResponseTypeDef:
        """
        Uploads a part by copying data from an existing object as data source. You specify the data source
        by adding the request header ``x-amz-copy-source`` in your request and a byte range by adding the
        request header ``x-amz-copy-source-range`` in your request.

        The minimum allowable part size for a multipart upload is 5 MB. For more information about
        multipart upload limits, go to `Quick Facts
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/qfacts.html>`__ in the *Amazon Simple Storage
        Service Developer Guide* .

        .. note::

          Instead of using an existing object as part data, you might use the  UploadPart operation and
          provide data in your request.

        You must initiate a multipart upload before you can upload any part. In response to your initiate
        request. Amazon S3 returns a unique identifier, the upload ID, that you must include in your upload
        part request.

         **For more information on using the UploadPartCopy operation, see the following topics:**

        * For conceptual information on multipart uploads, go to `Uploading Objects Using Multipart Upload
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html>`__ in the *Amazon Simple
        Storage Service Developer Guide* .

        * For information on permissions required to use the multipart upload API, go to `Multipart Upload
        API and Permissions <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuAndPermissions.html>`__ in
        the *Amazon Simple Storage Service Developer Guide* .

        * For information about copying objects using a single atomic operation vs. the multipart upload,
        go to `Operations on Objects
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectOperations.html>`__ in the *Amazon Simple
        Storage Service Developer Guide* .

        * For information about using server-side encryption with customer-provided encryption keys with
        the UploadPartCopy operation, see  CopyObject and  UploadPart .

        Note the following additional considerations about the request headers
        ``x-amz-copy-source-if-match`` , ``x-amz-copy-source-if-none-match``
        ``x-amz-copy-source-if-unmodified-since``  ``x-amz-copy-source-if-modified-since``

        * **Consideration 1** - If both of the ``x-amz-copy-source-if-match`` and
        ``x-amz-copy-source-if-unmodified-since`` headers are present in the request as follows:
        ``x-amz-copy-source-if-match`` condition evaluates to ``true`` , and;
        ``x-amz-copy-source-if-unmodified-since`` condition evaluates to ``false`` ; then, S3 returns ``200
        OK`` and copies the data.

        * **Consideration 2** - If both of the ``x-amz-copy-source-if-none-match`` and
        ``x-amz-copy-source-if-modified-since`` headers are present in the request as follows:
        ``x-amz-copy-source-if-none-match`` condition evaluates to ``false`` , and;
        ``x-amz-copy-source-if-modified-since`` condition evaluates to ``true`` ; then, S3 returns ``412
        Precondition Failed`` response code.

         **Versioning**

        If your bucket has versioning enabled, you could have multiple versions of the same object. By
        default, ``x-amz-copy-source`` identifies the current version of the object to copy. If the current
        version is a delete marker and you don't specify a versionId in the ``x-amz-copy-source`` , Amazon
        S3 returns a 404 error, because the object does not exist. If you specify versionId in the
        ``x-amz-copy-source`` and the versionId is a delete marker, Amazon S3 returns an HTTP 400 error,
        because you are not allowed to specify a delete marker as a version for the ``x-amz-copy-source`` .

        You can optionally specify a specific version of the source object to copy by adding the
        ``versionId`` subresource as shown in the following example:

         ``x-amz-copy-source: /bucket/object?versionId=version id``

         **Special Errors**

        *

          * *Code: NoSuchUpload*

          * *Cause: The specified multipart upload does not exist. The upload ID might be invalid, or the
          multipart upload might have been aborted or completed.*

          * *HTTP Status Code: 404 Not Found*

        *

          * *Code: InvalidRequest*

          * *Cause: The specified copy source is not supported as a byte-range copy source.*

          * *HTTP Status Code: 400 Bad Request*

         **Related Resources**

        *  CreateMultipartUpload

        *  UploadPart

        *  CompleteMultipartUpload

        *  AbortMultipartUpload

        *  ListParts

        *  ListMultipartUploads

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/UploadPartCopy>`_

        **Request Syntax**
        ::

          response = client.upload_part_copy(
              Bucket='string',
              CopySource='string' or {'Bucket': 'string', 'Key': 'string', 'VersionId': 'string'},
              CopySourceIfMatch='string',
              CopySourceIfModifiedSince=datetime(2015, 1, 1),
              CopySourceIfNoneMatch='string',
              CopySourceIfUnmodifiedSince=datetime(2015, 1, 1),
              CopySourceRange='string',
              Key='string',
              PartNumber=123,
              UploadId='string',
              SSECustomerAlgorithm='string',
              SSECustomerKey='string',
              CopySourceSSECustomerAlgorithm='string',
              CopySourceSSECustomerKey='string',
              RequestPayer='requester'
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The bucket name.

        :type CopySource: str or dict
        :param CopySource: **[REQUIRED]** The name of the source bucket, key name of the source object, and
        optional version ID of the source object.  You can either provide this value as a string or a
        dictionary.  The string form is {bucket}/{key} or {bucket}/{key}?versionId={versionId} if you want
        to copy a specific version.  You can also provide this value as a dictionary.  The dictionary
        format is recommended over the string format because it is more explicit.  The dictionary format
        is: {'Bucket': 'bucket', 'Key': 'key', 'VersionId': 'id'}.  Note that the VersionId key is optional
        and may be omitted.

        :type CopySourceIfMatch: string
        :param CopySourceIfMatch:

          Copies the object if its entity tag (ETag) matches the specified tag.

        :type CopySourceIfModifiedSince: datetime
        :param CopySourceIfModifiedSince:

          Copies the object if it has been modified since the specified time.

        :type CopySourceIfNoneMatch: string
        :param CopySourceIfNoneMatch:

          Copies the object if its entity tag (ETag) is different than the specified ETag.

        :type CopySourceIfUnmodifiedSince: datetime
        :param CopySourceIfUnmodifiedSince:

          Copies the object if it hasn't been modified since the specified time.

        :type CopySourceRange: string
        :param CopySourceRange:

          The range of bytes to copy from the source object. The range value must use the form
          bytes=first-last, where the first and last are the zero-based byte offsets to copy. For example,
          bytes=0-9 indicates that you want to copy the first ten bytes of the source. You can copy a range
          only if the source object is greater than 5 MB.

        :type Key: string
        :param Key: **[REQUIRED]**

          Object key for which the multipart upload was initiated.

        :type PartNumber: integer
        :param PartNumber: **[REQUIRED]**

          Part number of part being copied. This is a positive integer between 1 and 10,000.

        :type UploadId: string
        :param UploadId: **[REQUIRED]**

          Upload ID identifying the multipart upload whose part is being copied.

        :type SSECustomerAlgorithm: string
        :param SSECustomerAlgorithm:

          Specifies the algorithm to use to when encrypting the object (e.g., AES256).

        :type SSECustomerKey: string
        :param SSECustomerKey:

          Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This
          value is used to store the object and then it is discarded; Amazon does not store the encryption
          key. The key must be appropriate for use with the algorithm specified in the
          x-amz-server-side​-encryption​-customer-algorithm header. This must be the same encryption key
          specified in the initiate multipart upload request.

        :type SSECustomerKeyMD5: string
        :param SSECustomerKeyMD5:

          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this
          header for a message integrity check to ensure the encryption key was transmitted without error.

            Please note that this parameter is automatically populated if it is not provided. Including
            this parameter is not required

        :type CopySourceSSECustomerAlgorithm: string
        :param CopySourceSSECustomerAlgorithm:

          Specifies the algorithm to use when decrypting the source object (e.g., AES256).

        :type CopySourceSSECustomerKey: string
        :param CopySourceSSECustomerKey:

          Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object.
          The encryption key provided in this header must be one that was used when the source object was
          created.

        :type CopySourceSSECustomerKeyMD5: string
        :param CopySourceSSECustomerKeyMD5:

          Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this
          header for a message integrity check to ensure the encryption key was transmitted without error.

            Please note that this parameter is automatically populated if it is not provided. Including
            this parameter is not required

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CopySourceVersionId': 'string',
                'CopyPartResult': {
                    'ETag': 'string',
                    'LastModified': datetime(2015, 1, 1)
                },
                'ServerSideEncryption': 'AES256'|'aws:kms',
                'SSECustomerAlgorithm': 'string',
                'SSECustomerKeyMD5': 'string',
                'SSEKMSKeyId': 'string',
                'RequestCharged': 'requester'
            }
          **Response Structure**

          - *(dict) --*

            - **CopySourceVersionId** *(string) --*

              The version of the source object that was copied, if you have enabled versioning on the
              source bucket.

            - **CopyPartResult** *(dict) --*

              Container for all response elements.

              - **ETag** *(string) --*

                Entity tag of the object.

              - **LastModified** *(datetime) --*

                Date and time at which the object was uploaded.

            - **ServerSideEncryption** *(string) --*

              The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256,
              aws:kms).

            - **SSECustomerAlgorithm** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header confirming the encryption algorithm used.

            - **SSECustomerKeyMD5** *(string) --*

              If server-side encryption with a customer-provided encryption key was requested, the response
              will include this header to provide round trip message integrity verification of the
              customer-provided encryption key.

            - **SSEKMSKeyId** *(string) --*

              If present, specifies the ID of the AWS Key Management Service (KMS) customer master key
              (CMK) that was used for the object.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> paginator_scope.ListMultipartUploadsPaginator:
        """
        Get Paginator for `list_multipart_uploads` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_object_versions"]
    ) -> paginator_scope.ListObjectVersionsPaginator:
        """
        Get Paginator for `list_object_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_objects"]
    ) -> paginator_scope.ListObjectsPaginator:
        """
        Get Paginator for `list_objects` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_objects_v2"]
    ) -> paginator_scope.ListObjectsV2Paginator:
        """
        Get Paginator for `list_objects_v2` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_parts"]
    ) -> paginator_scope.ListPartsPaginator:
        """
        Get Paginator for `list_parts` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["bucket_exists"]
    ) -> waiter_scope.BucketExistsWaiter:
        """
        Get Waiter `bucket_exists`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["bucket_not_exists"]
    ) -> waiter_scope.BucketNotExistsWaiter:
        """
        Get Waiter `bucket_not_exists`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["object_exists"]
    ) -> waiter_scope.ObjectExistsWaiter:
        """
        Get Waiter `object_exists`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["object_not_exists"]
    ) -> waiter_scope.ObjectNotExistsWaiter:
        """
        Get Waiter `object_not_exists`.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """


class Exceptions:
    BucketAlreadyExists: Boto3ClientError
    BucketAlreadyOwnedByYou: Boto3ClientError
    ClientError: Boto3ClientError
    NoSuchBucket: Boto3ClientError
    NoSuchKey: Boto3ClientError
    NoSuchUpload: Boto3ClientError
    ObjectAlreadyInActiveTierError: Boto3ClientError
    ObjectNotInActiveTierError: Boto3ClientError
