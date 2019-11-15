"Main interface for s3 type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


_RequiredBucketAclPutAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_RequiredBucketAclPutAccessControlPolicyGrantsGranteeTypeDef", {"Type": str}
)
_OptionalBucketAclPutAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_OptionalBucketAclPutAccessControlPolicyGrantsGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "URI": str},
    total=False,
)


class BucketAclPutAccessControlPolicyGrantsGranteeTypeDef(
    _RequiredBucketAclPutAccessControlPolicyGrantsGranteeTypeDef,
    _OptionalBucketAclPutAccessControlPolicyGrantsGranteeTypeDef,
):
    """
    Type definition for `BucketAclPutAccessControlPolicyGrants` `Grantee`

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
    """


_BucketAclPutAccessControlPolicyGrantsTypeDef = TypedDict(
    "_BucketAclPutAccessControlPolicyGrantsTypeDef",
    {"Grantee": BucketAclPutAccessControlPolicyGrantsGranteeTypeDef, "Permission": str},
    total=False,
)


class BucketAclPutAccessControlPolicyGrantsTypeDef(
    _BucketAclPutAccessControlPolicyGrantsTypeDef
):
    """
    Type definition for `BucketAclPutAccessControlPolicy` `Grants`

    - **Grantee** *(dict) --*

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
    """


_BucketAclPutAccessControlPolicyOwnerTypeDef = TypedDict(
    "_BucketAclPutAccessControlPolicyOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class BucketAclPutAccessControlPolicyOwnerTypeDef(
    _BucketAclPutAccessControlPolicyOwnerTypeDef
):
    """
    Type definition for `BucketAclPutAccessControlPolicy` `Owner`

    Container for the bucket owner's display name and ID.

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_BucketAclPutAccessControlPolicyTypeDef = TypedDict(
    "_BucketAclPutAccessControlPolicyTypeDef",
    {
        "Grants": List[BucketAclPutAccessControlPolicyGrantsTypeDef],
        "Owner": BucketAclPutAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)


class BucketAclPutAccessControlPolicyTypeDef(_BucketAclPutAccessControlPolicyTypeDef):
    """
    Type definition for `BucketAclPut` `AccessControlPolicy`

    Contains the elements that set the ACL permissions for an object per grantee.

    - **Grants** *(list) --*

      A list of grants.

      - *(dict) --*

        - **Grantee** *(dict) --*

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

      - **ID** *(string) --*
    """


_BucketCreateCreateBucketConfigurationTypeDef = TypedDict(
    "_BucketCreateCreateBucketConfigurationTypeDef",
    {"LocationConstraint": str},
    total=False,
)


class BucketCreateCreateBucketConfigurationTypeDef(
    _BucketCreateCreateBucketConfigurationTypeDef
):
    """
    Type definition for `BucketCreate` `CreateBucketConfiguration`

    - **LocationConstraint** *(string) --*

      Specifies the region where the bucket will be created. If you don't specify a region, the
      bucket is created in US East (N. Virginia) Region (us-east-1).
    """


_BucketCreateResponseTypeDef = TypedDict(
    "_BucketCreateResponseTypeDef", {"Location": str}, total=False
)


class BucketCreateResponseTypeDef(_BucketCreateResponseTypeDef):
    """
    Type definition for `BucketCreate` `Response`

    - **Location** *(string) --*
    """


_RequiredBucketDeleteObjectsDeleteObjectsTypeDef = TypedDict(
    "_RequiredBucketDeleteObjectsDeleteObjectsTypeDef", {"Key": str}
)
_OptionalBucketDeleteObjectsDeleteObjectsTypeDef = TypedDict(
    "_OptionalBucketDeleteObjectsDeleteObjectsTypeDef", {"VersionId": str}, total=False
)


class BucketDeleteObjectsDeleteObjectsTypeDef(
    _RequiredBucketDeleteObjectsDeleteObjectsTypeDef,
    _OptionalBucketDeleteObjectsDeleteObjectsTypeDef,
):
    """
    Type definition for `BucketDeleteObjectsDelete` `Objects`

    - **Key** *(string) --* **[REQUIRED]**

      Key name of the object to delete.

    - **VersionId** *(string) --*

      VersionId for the specific version of the object to delete.
    """


_RequiredBucketDeleteObjectsDeleteTypeDef = TypedDict(
    "_RequiredBucketDeleteObjectsDeleteTypeDef",
    {"Objects": List[BucketDeleteObjectsDeleteObjectsTypeDef]},
)
_OptionalBucketDeleteObjectsDeleteTypeDef = TypedDict(
    "_OptionalBucketDeleteObjectsDeleteTypeDef", {"Quiet": bool}, total=False
)


class BucketDeleteObjectsDeleteTypeDef(
    _RequiredBucketDeleteObjectsDeleteTypeDef, _OptionalBucketDeleteObjectsDeleteTypeDef
):
    """
    Type definition for `BucketDeleteObjects` `Delete`

    - **Objects** *(list) --* **[REQUIRED]**

      - *(dict) --*

        - **Key** *(string) --* **[REQUIRED]**

          Key name of the object to delete.

        - **VersionId** *(string) --*

          VersionId for the specific version of the object to delete.

    - **Quiet** *(boolean) --*

      Element to enable quiet mode for the request. When you add this element, you must set its value
      to true.
    """


_BucketDeleteObjectsResponseDeletedTypeDef = TypedDict(
    "_BucketDeleteObjectsResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)


class BucketDeleteObjectsResponseDeletedTypeDef(
    _BucketDeleteObjectsResponseDeletedTypeDef
):
    """
    Type definition for `BucketDeleteObjectsResponse` `Deleted`

    - **Key** *(string) --*

    - **VersionId** *(string) --*

    - **DeleteMarker** *(boolean) --*

    - **DeleteMarkerVersionId** *(string) --*
    """


_BucketDeleteObjectsResponseErrorsTypeDef = TypedDict(
    "_BucketDeleteObjectsResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)


class BucketDeleteObjectsResponseErrorsTypeDef(
    _BucketDeleteObjectsResponseErrorsTypeDef
):
    """
    Type definition for `BucketDeleteObjectsResponse` `Errors`

    - **Key** *(string) --*

    - **VersionId** *(string) --*

    - **Code** *(string) --*

    - **Message** *(string) --*
    """


_BucketDeleteObjectsResponseTypeDef = TypedDict(
    "_BucketDeleteObjectsResponseTypeDef",
    {
        "Deleted": List[BucketDeleteObjectsResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[BucketDeleteObjectsResponseErrorsTypeDef],
    },
    total=False,
)


class BucketDeleteObjectsResponseTypeDef(_BucketDeleteObjectsResponseTypeDef):
    """
    Type definition for `BucketDeleteObjects` `Response`

    - **Deleted** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **VersionId** *(string) --*

        - **DeleteMarker** *(boolean) --*

        - **DeleteMarkerVersionId** *(string) --*

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **Errors** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **VersionId** *(string) --*

        - **Code** *(string) --*

        - **Message** *(string) --*
    """


_ClientAbortMultipartUploadResponseTypeDef = TypedDict(
    "_ClientAbortMultipartUploadResponseTypeDef", {"RequestCharged": str}, total=False
)


class ClientAbortMultipartUploadResponseTypeDef(
    _ClientAbortMultipartUploadResponseTypeDef
):
    """
    Type definition for `ClientAbortMultipartUpload` `Response`

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientCompleteMultipartUploadMultipartUploadPartsTypeDef = TypedDict(
    "_ClientCompleteMultipartUploadMultipartUploadPartsTypeDef",
    {"ETag": str, "PartNumber": int},
    total=False,
)


class ClientCompleteMultipartUploadMultipartUploadPartsTypeDef(
    _ClientCompleteMultipartUploadMultipartUploadPartsTypeDef
):
    """
    Type definition for `ClientCompleteMultipartUploadMultipartUpload` `Parts`

    - **ETag** *(string) --*

      Entity tag returned when the part was uploaded.

    - **PartNumber** *(integer) --*

      Part number that identifies the part. This is a positive integer between 1 and 10,000.
    """


_ClientCompleteMultipartUploadMultipartUploadTypeDef = TypedDict(
    "_ClientCompleteMultipartUploadMultipartUploadTypeDef",
    {"Parts": List[ClientCompleteMultipartUploadMultipartUploadPartsTypeDef]},
    total=False,
)


class ClientCompleteMultipartUploadMultipartUploadTypeDef(
    _ClientCompleteMultipartUploadMultipartUploadTypeDef
):
    """
    Type definition for `ClientCompleteMultipartUpload` `MultipartUpload`

    - **Parts** *(list) --*

      - *(dict) --*

        - **ETag** *(string) --*

          Entity tag returned when the part was uploaded.

        - **PartNumber** *(integer) --*

          Part number that identifies the part. This is a positive integer between 1 and 10,000.
    """


_ClientCompleteMultipartUploadResponseTypeDef = TypedDict(
    "_ClientCompleteMultipartUploadResponseTypeDef",
    {
        "Location": str,
        "Bucket": str,
        "Key": str,
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": str,
        "VersionId": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)


class ClientCompleteMultipartUploadResponseTypeDef(
    _ClientCompleteMultipartUploadResponseTypeDef
):
    """
    Type definition for `ClientCompleteMultipartUpload` `Response`

    - **Location** *(string) --*

    - **Bucket** *(string) --*

    - **Key** *(string) --*

    - **Expiration** *(string) --*

      If the object expiration is configured, this will contain the expiration date (expiry-date)
      and rule ID (rule-id). The value of rule-id is URL encoded.

    - **ETag** *(string) --*

      Entity tag of the object.

    - **ServerSideEncryption** *(string) --*

      The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256,
      aws:kms).

    - **VersionId** *(string) --*

      Version of the object.

    - **SSEKMSKeyId** *(string) --*

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientCopyObjectResponseCopyObjectResultTypeDef = TypedDict(
    "_ClientCopyObjectResponseCopyObjectResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)


class ClientCopyObjectResponseCopyObjectResultTypeDef(
    _ClientCopyObjectResponseCopyObjectResultTypeDef
):
    """
    Type definition for `ClientCopyObjectResponse` `CopyObjectResult`

    - **ETag** *(string) --*

    - **LastModified** *(datetime) --*
    """


_ClientCopyObjectResponseTypeDef = TypedDict(
    "_ClientCopyObjectResponseTypeDef",
    {
        "CopyObjectResult": ClientCopyObjectResponseCopyObjectResultTypeDef,
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)


class ClientCopyObjectResponseTypeDef(_ClientCopyObjectResponseTypeDef):
    """
    Type definition for `ClientCopyObject` `Response`

    - **CopyObjectResult** *(dict) --*

      - **ETag** *(string) --*

      - **LastModified** *(datetime) --*

    - **Expiration** *(string) --*

      If the object expiration is configured, the response includes this header.

    - **CopySourceVersionId** *(string) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **SSEKMSEncryptionContext** *(string) --*

      If present, specifies the AWS KMS Encryption Context to use for object encryption. The value
      of this header is a base64-encoded UTF-8 string holding JSON with the encryption context
      key-value pairs.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientCreateBucketCreateBucketConfigurationTypeDef = TypedDict(
    "_ClientCreateBucketCreateBucketConfigurationTypeDef",
    {"LocationConstraint": str},
    total=False,
)


class ClientCreateBucketCreateBucketConfigurationTypeDef(
    _ClientCreateBucketCreateBucketConfigurationTypeDef
):
    """
    Type definition for `ClientCreateBucket` `CreateBucketConfiguration`

    - **LocationConstraint** *(string) --*

      Specifies the region where the bucket will be created. If you don't specify a region, the
      bucket is created in US East (N. Virginia) Region (us-east-1).
    """


_ClientCreateBucketResponseTypeDef = TypedDict(
    "_ClientCreateBucketResponseTypeDef", {"Location": str}, total=False
)


class ClientCreateBucketResponseTypeDef(_ClientCreateBucketResponseTypeDef):
    """
    Type definition for `ClientCreateBucket` `Response`

    - **Location** *(string) --*
    """


_ClientCreateMultipartUploadResponseTypeDef = TypedDict(
    "_ClientCreateMultipartUploadResponseTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "ServerSideEncryption": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)


class ClientCreateMultipartUploadResponseTypeDef(
    _ClientCreateMultipartUploadResponseTypeDef
):
    """
    Type definition for `ClientCreateMultipartUpload` `Response`

    - **AbortDate** *(datetime) --*

      Date when multipart upload will become eligible for abort operation by lifecycle.

    - **AbortRuleId** *(string) --*

      Id of the lifecycle rule that makes a multipart upload eligible for abort operation.

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **SSEKMSEncryptionContext** *(string) --*

      If present, specifies the AWS KMS Encryption Context to use for object encryption. The value
      of this header is a base64-encoded UTF-8 string holding JSON with the encryption context
      key-value pairs.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientDeleteObjectResponseTypeDef = TypedDict(
    "_ClientDeleteObjectResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)


class ClientDeleteObjectResponseTypeDef(_ClientDeleteObjectResponseTypeDef):
    """
    Type definition for `ClientDeleteObject` `Response`

    - **DeleteMarker** *(boolean) --*

      Specifies whether the versioned object that was permanently deleted was (true) or was not
      (false) a delete marker.

    - **VersionId** *(string) --*

      Returns the version ID of the delete marker created as a result of the DELETE operation.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientDeleteObjectTaggingResponseTypeDef = TypedDict(
    "_ClientDeleteObjectTaggingResponseTypeDef", {"VersionId": str}, total=False
)


class ClientDeleteObjectTaggingResponseTypeDef(
    _ClientDeleteObjectTaggingResponseTypeDef
):
    """
    Type definition for `ClientDeleteObjectTagging` `Response`

    - **VersionId** *(string) --*

      The versionId of the object the tag-set was removed from.
    """


_RequiredClientDeleteObjectsDeleteObjectsTypeDef = TypedDict(
    "_RequiredClientDeleteObjectsDeleteObjectsTypeDef", {"Key": str}
)
_OptionalClientDeleteObjectsDeleteObjectsTypeDef = TypedDict(
    "_OptionalClientDeleteObjectsDeleteObjectsTypeDef", {"VersionId": str}, total=False
)


class ClientDeleteObjectsDeleteObjectsTypeDef(
    _RequiredClientDeleteObjectsDeleteObjectsTypeDef,
    _OptionalClientDeleteObjectsDeleteObjectsTypeDef,
):
    """
    Type definition for `ClientDeleteObjectsDelete` `Objects`

    - **Key** *(string) --* **[REQUIRED]**

      Key name of the object to delete.

    - **VersionId** *(string) --*

      VersionId for the specific version of the object to delete.
    """


_RequiredClientDeleteObjectsDeleteTypeDef = TypedDict(
    "_RequiredClientDeleteObjectsDeleteTypeDef",
    {"Objects": List[ClientDeleteObjectsDeleteObjectsTypeDef]},
)
_OptionalClientDeleteObjectsDeleteTypeDef = TypedDict(
    "_OptionalClientDeleteObjectsDeleteTypeDef", {"Quiet": bool}, total=False
)


class ClientDeleteObjectsDeleteTypeDef(
    _RequiredClientDeleteObjectsDeleteTypeDef, _OptionalClientDeleteObjectsDeleteTypeDef
):
    """
    Type definition for `ClientDeleteObjects` `Delete`

    - **Objects** *(list) --* **[REQUIRED]**

      - *(dict) --*

        - **Key** *(string) --* **[REQUIRED]**

          Key name of the object to delete.

        - **VersionId** *(string) --*

          VersionId for the specific version of the object to delete.

    - **Quiet** *(boolean) --*

      Element to enable quiet mode for the request. When you add this element, you must set its value
      to true.
    """


_ClientDeleteObjectsResponseDeletedTypeDef = TypedDict(
    "_ClientDeleteObjectsResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)


class ClientDeleteObjectsResponseDeletedTypeDef(
    _ClientDeleteObjectsResponseDeletedTypeDef
):
    """
    Type definition for `ClientDeleteObjectsResponse` `Deleted`

    - **Key** *(string) --*

    - **VersionId** *(string) --*

    - **DeleteMarker** *(boolean) --*

    - **DeleteMarkerVersionId** *(string) --*
    """


_ClientDeleteObjectsResponseErrorsTypeDef = TypedDict(
    "_ClientDeleteObjectsResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)


class ClientDeleteObjectsResponseErrorsTypeDef(
    _ClientDeleteObjectsResponseErrorsTypeDef
):
    """
    Type definition for `ClientDeleteObjectsResponse` `Errors`

    - **Key** *(string) --*

    - **VersionId** *(string) --*

    - **Code** *(string) --*

    - **Message** *(string) --*
    """


_ClientDeleteObjectsResponseTypeDef = TypedDict(
    "_ClientDeleteObjectsResponseTypeDef",
    {
        "Deleted": List[ClientDeleteObjectsResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[ClientDeleteObjectsResponseErrorsTypeDef],
    },
    total=False,
)


class ClientDeleteObjectsResponseTypeDef(_ClientDeleteObjectsResponseTypeDef):
    """
    Type definition for `ClientDeleteObjects` `Response`

    - **Deleted** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **VersionId** *(string) --*

        - **DeleteMarker** *(boolean) --*

        - **DeleteMarkerVersionId** *(string) --*

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **Errors** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **VersionId** *(string) --*

        - **Code** *(string) --*

        - **Message** *(string) --*
    """


_ClientGetBucketAccelerateConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketAccelerateConfigurationResponseTypeDef",
    {"Status": str},
    total=False,
)


class ClientGetBucketAccelerateConfigurationResponseTypeDef(
    _ClientGetBucketAccelerateConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetBucketAccelerateConfiguration` `Response`

    - **Status** *(string) --*

      The accelerate configuration of the bucket.
    """


_ClientGetBucketAclResponseGrantsGranteeTypeDef = TypedDict(
    "_ClientGetBucketAclResponseGrantsGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "Type": str, "URI": str},
    total=False,
)


class ClientGetBucketAclResponseGrantsGranteeTypeDef(
    _ClientGetBucketAclResponseGrantsGranteeTypeDef
):
    """
    Type definition for `ClientGetBucketAclResponseGrants` `Grantee`

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
    """


_ClientGetBucketAclResponseGrantsTypeDef = TypedDict(
    "_ClientGetBucketAclResponseGrantsTypeDef",
    {"Grantee": ClientGetBucketAclResponseGrantsGranteeTypeDef, "Permission": str},
    total=False,
)


class ClientGetBucketAclResponseGrantsTypeDef(_ClientGetBucketAclResponseGrantsTypeDef):
    """
    Type definition for `ClientGetBucketAclResponse` `Grants`

    - **Grantee** *(dict) --*

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


_ClientGetBucketAclResponseOwnerTypeDef = TypedDict(
    "_ClientGetBucketAclResponseOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientGetBucketAclResponseOwnerTypeDef(_ClientGetBucketAclResponseOwnerTypeDef):
    """
    Type definition for `ClientGetBucketAclResponse` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientGetBucketAclResponseTypeDef = TypedDict(
    "_ClientGetBucketAclResponseTypeDef",
    {
        "Owner": ClientGetBucketAclResponseOwnerTypeDef,
        "Grants": List[ClientGetBucketAclResponseGrantsTypeDef],
    },
    total=False,
)


class ClientGetBucketAclResponseTypeDef(_ClientGetBucketAclResponseTypeDef):
    """
    Type definition for `ClientGetBucketAcl` `Response`

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*

    - **Grants** *(list) --*

      A list of grants.

      - *(dict) --*

        - **Grantee** *(dict) --*

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


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef
):
    """
    Type definition for `ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAnd` `Tags`

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef
):
    """
    Type definition for `ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilter` `And`

    A conjunction (logical AND) of predicates, which is used in evaluating an analytics
    filter. The operator must have at least two predicates.

    - **Prefix** *(string) --*

      The prefix to use when evaluating an AND predicate: The prefix that an object must have
      to be included in the metrics results.

    - **Tags** *(list) --*

      The list of tags to use when evaluating an AND predicate.

      - *(dict) --*

        - **Key** *(string) --*

          Name of the tag.

        - **Value** *(string) --*

          Value of the tag.
    """


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef
):
    """
    Type definition for `ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilter` `Tag`

    The tag to use when evaluating an analytics filter.

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef,
        "And": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef,
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef
):
    """
    Type definition for `ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfiguration` `Filter`

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

          - **Key** *(string) --*

            Name of the tag.

          - **Value** *(string) --*

            Value of the tag.
    """


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
):
    """
    Type definition for `ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestination` `S3BucketDestination`

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


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef
):
    """
    Type definition for `ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExport` `Destination`

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


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef
):
    """
    Type definition for `ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysis` `DataExport`

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


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef
):
    """
    Type definition for `ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfiguration` `StorageClassAnalysis`

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


_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef",
    {
        "Id": str,
        "Filter": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef,
        "StorageClassAnalysis": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef,
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef
):
    """
    Type definition for `ClientGetBucketAnalyticsConfigurationResponse` `AnalyticsConfiguration`

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


_ClientGetBucketAnalyticsConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketAnalyticsConfigurationResponseTypeDef",
    {
        "AnalyticsConfiguration": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef
    },
    total=False,
)


class ClientGetBucketAnalyticsConfigurationResponseTypeDef(
    _ClientGetBucketAnalyticsConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetBucketAnalyticsConfiguration` `Response`

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


_ClientGetBucketCorsResponseCORSRulesTypeDef = TypedDict(
    "_ClientGetBucketCorsResponseCORSRulesTypeDef",
    {
        "AllowedHeaders": List[str],
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)


class ClientGetBucketCorsResponseCORSRulesTypeDef(
    _ClientGetBucketCorsResponseCORSRulesTypeDef
):
    """
    Type definition for `ClientGetBucketCorsResponse` `CORSRules`

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


_ClientGetBucketCorsResponseTypeDef = TypedDict(
    "_ClientGetBucketCorsResponseTypeDef",
    {"CORSRules": List[ClientGetBucketCorsResponseCORSRulesTypeDef]},
    total=False,
)


class ClientGetBucketCorsResponseTypeDef(_ClientGetBucketCorsResponseTypeDef):
    """
    Type definition for `ClientGetBucketCors` `Response`

    - **CORSRules** *(list) --*

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


_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    {"SSEAlgorithm": str, "KMSMasterKeyID": str},
    total=False,
)


class ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef(
    _ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef
):
    """
    Type definition for `ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRules` `ApplyServerSideEncryptionByDefault`

    Specifies the default server-side encryption to apply to new objects in the bucket. If
    a PUT Object request doesn't specify any server-side encryption, this default
    encryption will be applied.

    - **SSEAlgorithm** *(string) --*

      Server-side encryption algorithm to use for the default encryption.

    - **KMSMasterKeyID** *(string) --*

      KMS master key ID to use for the default encryption. This parameter is allowed if and
      only if ``SSEAlgorithm`` is set to ``aws:kms`` .
    """


_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef = TypedDict(
    "_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef
    },
    total=False,
)


class ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef(
    _ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef
):
    """
    Type definition for `ClientGetBucketEncryptionResponseServerSideEncryptionConfiguration` `Rules`

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


_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef = TypedDict(
    "_ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef",
    {
        "Rules": List[
            ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef
        ]
    },
    total=False,
)


class ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef(
    _ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientGetBucketEncryptionResponse` `ServerSideEncryptionConfiguration`

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


_ClientGetBucketEncryptionResponseTypeDef = TypedDict(
    "_ClientGetBucketEncryptionResponseTypeDef",
    {
        "ServerSideEncryptionConfiguration": ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef
    },
    total=False,
)


class ClientGetBucketEncryptionResponseTypeDef(
    _ClientGetBucketEncryptionResponseTypeDef
):
    """
    Type definition for `ClientGetBucketEncryption` `Response`

    - **ServerSideEncryptionConfiguration** *(dict) --*

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


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef
):
    """
    Type definition for `ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryption` `SSEKMS`

    Specifies the use of SSE-KMS to encrypt delivered Inventory reports.

    - **KeyId** *(string) --*

      Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
      use for encrypting Inventory reports.
    """


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict,
        "SSEKMS": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef
):
    """
    Type definition for `ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestination` `Encryption`

    Contains the type of server-side encryption used to encrypt the inventory results.

    - **SSES3** *(dict) --*

      Specifies the use of SSE-S3 to encrypt delivered Inventory reports.

    - **SSEKMS** *(dict) --*

      Specifies the use of SSE-KMS to encrypt delivered Inventory reports.

      - **KeyId** *(string) --*

        Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
        use for encrypting Inventory reports.
    """


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": str,
        "Prefix": str,
        "Encryption": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef
):
    """
    Type definition for `ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestination` `S3BucketDestination`

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

          Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
          use for encrypting Inventory reports.
    """


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef",
    {
        "S3BucketDestination": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef
    },
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef
):
    """
    Type definition for `ClientGetBucketInventoryConfigurationResponseInventoryConfiguration` `Destination`

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

            Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
            use for encrypting Inventory reports.
    """


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef",
    {"Prefix": str},
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef
):
    """
    Type definition for `ClientGetBucketInventoryConfigurationResponseInventoryConfiguration` `Filter`

    Specifies an inventory filter. The inventory only includes objects that meet the filter's
    criteria.

    - **Prefix** *(string) --*

      The prefix that an object must have to be included in the inventory results.
    """


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef",
    {"Frequency": str},
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef
):
    """
    Type definition for `ClientGetBucketInventoryConfigurationResponseInventoryConfiguration` `Schedule`

    Specifies the schedule for generating inventory results.

    - **Frequency** *(string) --*

      Specifies how frequently inventory results are produced.
    """


_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef",
    {
        "Destination": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef,
        "IsEnabled": bool,
        "Filter": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef,
        "Id": str,
        "IncludedObjectVersions": str,
        "OptionalFields": List[str],
        "Schedule": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef,
    },
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef(
    _ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef
):
    """
    Type definition for `ClientGetBucketInventoryConfigurationResponse` `InventoryConfiguration`

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

              Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
              use for encrypting Inventory reports.

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


_ClientGetBucketInventoryConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketInventoryConfigurationResponseTypeDef",
    {
        "InventoryConfiguration": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef
    },
    total=False,
)


class ClientGetBucketInventoryConfigurationResponseTypeDef(
    _ClientGetBucketInventoryConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetBucketInventoryConfiguration` `Response`

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

                Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
                use for encrypting Inventory reports.

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


_ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfigurationResponseRules` `AbortIncompleteMultipartUpload`

    - **DaysAfterInitiation** *(integer) --*

      Specifies the number of days after which Amazon S3 aborts an incomplete multipart
      upload.
    """


_ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfigurationResponseRules` `Expiration`

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
    """


_ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfigurationResponseRulesFilterAnd` `Tags`

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfigurationResponseRulesFilter` `And`

    - **Prefix** *(string) --*

    - **Tags** *(list) --*

      All of these tags must exist in the object's tag set in order for the rule to apply.

      - *(dict) --*

        - **Key** *(string) --*

          Name of the tag.

        - **Value** *(string) --*

          Value of the tag.
    """


_ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfigurationResponseRulesFilter` `Tag`

    This tag must exist in the object's tag set in order for the rule to apply.

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef,
        "And": ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef,
    },
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfigurationResponseRules` `Filter`

    - **Prefix** *(string) --*

      Prefix identifying one or more objects to which the rule applies.

    - **Tag** *(dict) --*

      This tag must exist in the object's tag set in order for the rule to apply.

      - **Key** *(string) --*

        Name of the tag.

      - **Value** *(string) --*

        Value of the tag.

    - **And** *(dict) --*

      - **Prefix** *(string) --*

      - **Tags** *(list) --*

        All of these tags must exist in the object's tag set in order for the rule to apply.

        - *(dict) --*

          - **Key** *(string) --*

            Name of the tag.

          - **Value** *(string) --*

            Value of the tag.
    """


_ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfigurationResponseRules` `NoncurrentVersionExpiration`

    - **NoncurrentDays** *(integer) --*

      Specifies the number of days an object is noncurrent before Amazon S3 can perform the
      associated action. For information about the noncurrent days calculations, see `How
      Amazon S3 Calculates When an Object Became Noncurrent
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__
      in the Amazon Simple Storage Service Developer Guide.
    """


_ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef",
    {"NoncurrentDays": int, "StorageClass": str},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfigurationResponseRules` `NoncurrentVersionTransitions`

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
    """


_ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef",
    {"Date": datetime, "Days": int, "StorageClass": str},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfigurationResponseRules` `Transitions`

    Specifies when an object transitions to a specified storage class.

    - **Date** *(datetime) --*

      Indicates when objects are transitioned to the specified storage class. The date
      value must be in ISO 8601 format. The time is always midnight UTC.

    - **Days** *(integer) --*

      Indicates the number of days after creation when objects are transitioned to the
      specified storage class. The value must be a positive integer.

    - **StorageClass** *(string) --*

      The storage class to which you want the object to transition.
    """


_ClientGetBucketLifecycleConfigurationResponseRulesTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseRulesTypeDef",
    {
        "Expiration": ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Filter": ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef,
        "Status": str,
        "Transitions": List[
            ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef
        ],
        "NoncurrentVersionTransitions": List[
            ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef
        ],
        "NoncurrentVersionExpiration": ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseRulesTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseRulesTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfigurationResponse` `Rules`

    - **Expiration** *(dict) --*

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

      - **Prefix** *(string) --*

        Prefix identifying one or more objects to which the rule applies.

      - **Tag** *(dict) --*

        This tag must exist in the object's tag set in order for the rule to apply.

        - **Key** *(string) --*

          Name of the tag.

        - **Value** *(string) --*

          Value of the tag.

      - **And** *(dict) --*

        - **Prefix** *(string) --*

        - **Tags** *(list) --*

          All of these tags must exist in the object's tag set in order for the rule to apply.

          - *(dict) --*

            - **Key** *(string) --*

              Name of the tag.

            - **Value** *(string) --*

              Value of the tag.

    - **Status** *(string) --*

      If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not
      currently being applied.

    - **Transitions** *(list) --*

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

      - **NoncurrentDays** *(integer) --*

        Specifies the number of days an object is noncurrent before Amazon S3 can perform the
        associated action. For information about the noncurrent days calculations, see `How
        Amazon S3 Calculates When an Object Became Noncurrent
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__
        in the Amazon Simple Storage Service Developer Guide.

    - **AbortIncompleteMultipartUpload** *(dict) --*

      - **DaysAfterInitiation** *(integer) --*

        Specifies the number of days after which Amazon S3 aborts an incomplete multipart
        upload.
    """


_ClientGetBucketLifecycleConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketLifecycleConfigurationResponseTypeDef",
    {"Rules": List[ClientGetBucketLifecycleConfigurationResponseRulesTypeDef]},
    total=False,
)


class ClientGetBucketLifecycleConfigurationResponseTypeDef(
    _ClientGetBucketLifecycleConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleConfiguration` `Response`

    - **Rules** *(list) --*

      - *(dict) --*

        - **Expiration** *(dict) --*

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

          - **Prefix** *(string) --*

            Prefix identifying one or more objects to which the rule applies.

          - **Tag** *(dict) --*

            This tag must exist in the object's tag set in order for the rule to apply.

            - **Key** *(string) --*

              Name of the tag.

            - **Value** *(string) --*

              Value of the tag.

          - **And** *(dict) --*

            - **Prefix** *(string) --*

            - **Tags** *(list) --*

              All of these tags must exist in the object's tag set in order for the rule to apply.

              - *(dict) --*

                - **Key** *(string) --*

                  Name of the tag.

                - **Value** *(string) --*

                  Value of the tag.

        - **Status** *(string) --*

          If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not
          currently being applied.

        - **Transitions** *(list) --*

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

          - **NoncurrentDays** *(integer) --*

            Specifies the number of days an object is noncurrent before Amazon S3 can perform the
            associated action. For information about the noncurrent days calculations, see `How
            Amazon S3 Calculates When an Object Became Noncurrent
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__
            in the Amazon Simple Storage Service Developer Guide.

        - **AbortIncompleteMultipartUpload** *(dict) --*

          - **DaysAfterInitiation** *(integer) --*

            Specifies the number of days after which Amazon S3 aborts an incomplete multipart
            upload.
    """


_ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)


class ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef(
    _ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleResponseRules` `AbortIncompleteMultipartUpload`

    - **DaysAfterInitiation** *(integer) --*

      Specifies the number of days after which Amazon S3 aborts an incomplete multipart
      upload.
    """


_ClientGetBucketLifecycleResponseRulesExpirationTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)


class ClientGetBucketLifecycleResponseRulesExpirationTypeDef(
    _ClientGetBucketLifecycleResponseRulesExpirationTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleResponseRules` `Expiration`

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
    """


_ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)


class ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef(
    _ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleResponseRules` `NoncurrentVersionExpiration`

    - **NoncurrentDays** *(integer) --*

      Specifies the number of days an object is noncurrent before Amazon S3 can perform the
      associated action. For information about the noncurrent days calculations, see `How
      Amazon S3 Calculates When an Object Became Noncurrent
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__
      in the Amazon Simple Storage Service Developer Guide.
    """


_ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef",
    {"NoncurrentDays": int, "StorageClass": str},
    total=False,
)


class ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef(
    _ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleResponseRules` `NoncurrentVersionTransition`

    - **NoncurrentDays** *(integer) --*

      Specifies the number of days an object is noncurrent before Amazon S3 can perform the
      associated action. For information about the noncurrent days calculations, see `How
      Amazon S3 Calculates When an Object Became Noncurrent
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the
      *Amazon Simple Storage Service Developer Guide* .

    - **StorageClass** *(string) --*

      The class of storage used to store the object.
    """


_ClientGetBucketLifecycleResponseRulesTransitionTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesTransitionTypeDef",
    {"Date": datetime, "Days": int, "StorageClass": str},
    total=False,
)


class ClientGetBucketLifecycleResponseRulesTransitionTypeDef(
    _ClientGetBucketLifecycleResponseRulesTransitionTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleResponseRules` `Transition`

    - **Date** *(datetime) --*

      Indicates when objects are transitioned to the specified storage class. The date value
      must be in ISO 8601 format. The time is always midnight UTC.

    - **Days** *(integer) --*

      Indicates the number of days after creation when objects are transitioned to the
      specified storage class. The value must be a positive integer.

    - **StorageClass** *(string) --*

      The storage class to which you want the object to transition.
    """


_ClientGetBucketLifecycleResponseRulesTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseRulesTypeDef",
    {
        "Expiration": ClientGetBucketLifecycleResponseRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Status": str,
        "Transition": ClientGetBucketLifecycleResponseRulesTransitionTypeDef,
        "NoncurrentVersionTransition": ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef,
        "NoncurrentVersionExpiration": ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)


class ClientGetBucketLifecycleResponseRulesTypeDef(
    _ClientGetBucketLifecycleResponseRulesTypeDef
):
    """
    Type definition for `ClientGetBucketLifecycleResponse` `Rules`

    Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket
    lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__
    in the *Amazon Simple Storage Service API Reference* .

    - **Expiration** *(dict) --*

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

      - **Date** *(datetime) --*

        Indicates when objects are transitioned to the specified storage class. The date value
        must be in ISO 8601 format. The time is always midnight UTC.

      - **Days** *(integer) --*

        Indicates the number of days after creation when objects are transitioned to the
        specified storage class. The value must be a positive integer.

      - **StorageClass** *(string) --*

        The storage class to which you want the object to transition.

    - **NoncurrentVersionTransition** *(dict) --*

      - **NoncurrentDays** *(integer) --*

        Specifies the number of days an object is noncurrent before Amazon S3 can perform the
        associated action. For information about the noncurrent days calculations, see `How
        Amazon S3 Calculates When an Object Became Noncurrent
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the
        *Amazon Simple Storage Service Developer Guide* .

      - **StorageClass** *(string) --*

        The class of storage used to store the object.

    - **NoncurrentVersionExpiration** *(dict) --*

      - **NoncurrentDays** *(integer) --*

        Specifies the number of days an object is noncurrent before Amazon S3 can perform the
        associated action. For information about the noncurrent days calculations, see `How
        Amazon S3 Calculates When an Object Became Noncurrent
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__
        in the Amazon Simple Storage Service Developer Guide.

    - **AbortIncompleteMultipartUpload** *(dict) --*

      - **DaysAfterInitiation** *(integer) --*

        Specifies the number of days after which Amazon S3 aborts an incomplete multipart
        upload.
    """


_ClientGetBucketLifecycleResponseTypeDef = TypedDict(
    "_ClientGetBucketLifecycleResponseTypeDef",
    {"Rules": List[ClientGetBucketLifecycleResponseRulesTypeDef]},
    total=False,
)


class ClientGetBucketLifecycleResponseTypeDef(_ClientGetBucketLifecycleResponseTypeDef):
    """
    Type definition for `ClientGetBucketLifecycle` `Response`

    - **Rules** *(list) --*

      - *(dict) --*

        Specifies lifecycle rules for an Amazon S3 bucket. For more information, see `PUT Bucket
        lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html>`__
        in the *Amazon Simple Storage Service API Reference* .

        - **Expiration** *(dict) --*

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

          - **Date** *(datetime) --*

            Indicates when objects are transitioned to the specified storage class. The date value
            must be in ISO 8601 format. The time is always midnight UTC.

          - **Days** *(integer) --*

            Indicates the number of days after creation when objects are transitioned to the
            specified storage class. The value must be a positive integer.

          - **StorageClass** *(string) --*

            The storage class to which you want the object to transition.

        - **NoncurrentVersionTransition** *(dict) --*

          - **NoncurrentDays** *(integer) --*

            Specifies the number of days an object is noncurrent before Amazon S3 can perform the
            associated action. For information about the noncurrent days calculations, see `How
            Amazon S3 Calculates When an Object Became Noncurrent
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html>`__ in the
            *Amazon Simple Storage Service Developer Guide* .

          - **StorageClass** *(string) --*

            The class of storage used to store the object.

        - **NoncurrentVersionExpiration** *(dict) --*

          - **NoncurrentDays** *(integer) --*

            Specifies the number of days an object is noncurrent before Amazon S3 can perform the
            associated action. For information about the noncurrent days calculations, see `How
            Amazon S3 Calculates When an Object Became Noncurrent
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations>`__
            in the Amazon Simple Storage Service Developer Guide.

        - **AbortIncompleteMultipartUpload** *(dict) --*

          - **DaysAfterInitiation** *(integer) --*

            Specifies the number of days after which Amazon S3 aborts an incomplete multipart
            upload.
    """


_ClientGetBucketLocationResponseTypeDef = TypedDict(
    "_ClientGetBucketLocationResponseTypeDef", {"LocationConstraint": str}, total=False
)


class ClientGetBucketLocationResponseTypeDef(_ClientGetBucketLocationResponseTypeDef):
    """
    Type definition for `ClientGetBucketLocation` `Response`

    - **LocationConstraint** *(string) --*
    """


_ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef = TypedDict(
    "_ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "Type": str, "URI": str},
    total=False,
)


class ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef(
    _ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef
):
    """
    Type definition for `ClientGetBucketLoggingResponseLoggingEnabledTargetGrants` `Grantee`

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
    """


_ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef = TypedDict(
    "_ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef",
    {
        "Grantee": ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef(
    _ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef
):
    """
    Type definition for `ClientGetBucketLoggingResponseLoggingEnabled` `TargetGrants`

    - **Grantee** *(dict) --*

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
    """


_ClientGetBucketLoggingResponseLoggingEnabledTypeDef = TypedDict(
    "_ClientGetBucketLoggingResponseLoggingEnabledTypeDef",
    {
        "TargetBucket": str,
        "TargetGrants": List[
            ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef
        ],
        "TargetPrefix": str,
    },
    total=False,
)


class ClientGetBucketLoggingResponseLoggingEnabledTypeDef(
    _ClientGetBucketLoggingResponseLoggingEnabledTypeDef
):
    """
    Type definition for `ClientGetBucketLoggingResponse` `LoggingEnabled`

    - **TargetBucket** *(string) --*

      Specifies the bucket where you want Amazon S3 to store server access logs. You can have
      your logs delivered to any bucket that you own, including the same bucket that is being
      logged. You can also configure multiple buckets to deliver their logs to the same target
      bucket. In this case you should choose a different TargetPrefix for each source bucket so
      that the delivered log files can be distinguished by key.

    - **TargetGrants** *(list) --*

      - *(dict) --*

        - **Grantee** *(dict) --*

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


_ClientGetBucketLoggingResponseTypeDef = TypedDict(
    "_ClientGetBucketLoggingResponseTypeDef",
    {"LoggingEnabled": ClientGetBucketLoggingResponseLoggingEnabledTypeDef},
    total=False,
)


class ClientGetBucketLoggingResponseTypeDef(_ClientGetBucketLoggingResponseTypeDef):
    """
    Type definition for `ClientGetBucketLogging` `Response`

    - **LoggingEnabled** *(dict) --*

      - **TargetBucket** *(string) --*

        Specifies the bucket where you want Amazon S3 to store server access logs. You can have
        your logs delivered to any bucket that you own, including the same bucket that is being
        logged. You can also configure multiple buckets to deliver their logs to the same target
        bucket. In this case you should choose a different TargetPrefix for each source bucket so
        that the delivered log files can be distinguished by key.

      - **TargetGrants** *(list) --*

        - *(dict) --*

          - **Grantee** *(dict) --*

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


_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef(
    _ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef
):
    """
    Type definition for `ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAnd` `Tags`

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef(
    _ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef
):
    """
    Type definition for `ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilter` `And`

    A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter.
    The operator must have at least two predicates, and an object must match all of the
    predicates in order for the filter to apply.

    - **Prefix** *(string) --*

      The prefix used when evaluating an AND predicate.

    - **Tags** *(list) --*

      The list of tags used when evaluating an AND predicate.

      - *(dict) --*

        - **Key** *(string) --*

          Name of the tag.

        - **Value** *(string) --*

          Value of the tag.
    """


_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef(
    _ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef
):
    """
    Type definition for `ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilter` `Tag`

    The tag used when evaluating a metrics filter.

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef,
        "And": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef,
    },
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef(
    _ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef
):
    """
    Type definition for `ClientGetBucketMetricsConfigurationResponseMetricsConfiguration` `Filter`

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

          - **Key** *(string) --*

            Name of the tag.

          - **Value** *(string) --*

            Value of the tag.
    """


_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef",
    {
        "Id": str,
        "Filter": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef,
    },
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef(
    _ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef
):
    """
    Type definition for `ClientGetBucketMetricsConfigurationResponse` `MetricsConfiguration`

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

            - **Key** *(string) --*

              Name of the tag.

            - **Value** *(string) --*

              Value of the tag.
    """


_ClientGetBucketMetricsConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketMetricsConfigurationResponseTypeDef",
    {
        "MetricsConfiguration": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef
    },
    total=False,
)


class ClientGetBucketMetricsConfigurationResponseTypeDef(
    _ClientGetBucketMetricsConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetBucketMetricsConfiguration` `Response`

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

              - **Key** *(string) --*

                Name of the tag.

              - **Value** *(string) --*

                Value of the tag.
    """


_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef(
    _ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKey` `FilterRules`

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


_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef(
    _ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilter` `Key`

    - **FilterRules** *(list) --*

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


_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef",
    {
        "Key": ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef(
    _ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurations` `Filter`

    - **Key** *(dict) --*

      - **FilterRules** *(list) --*

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


_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef",
    {
        "Id": str,
        "LambdaFunctionArn": str,
        "Events": List[str],
        "Filter": ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef,
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef(
    _ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponse` `LambdaFunctionConfigurations`

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

      - **Key** *(dict) --*

        - **FilterRules** *(list) --*

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


_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef(
    _ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKey` `FilterRules`

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


_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef(
    _ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilter` `Key`

    - **FilterRules** *(list) --*

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


_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef",
    {
        "Key": ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef(
    _ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponseQueueConfigurations` `Filter`

    - **Key** *(dict) --*

      - **FilterRules** *(list) --*

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


_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef",
    {
        "Id": str,
        "QueueArn": str,
        "Events": List[str],
        "Filter": ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef,
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef(
    _ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponse` `QueueConfigurations`

    Specifies the configuration for publishing messages to an Amazon Simple Queue Service
    (Amazon SQS) queue when Amazon S3 detects specified events.

    - **Id** *(string) --*

      An optional unique identifier for configurations in a notification configuration. If you
      don't provide one, Amazon S3 will assign an ID.

    - **QueueArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a
      message when it detects events of the specified type.

    - **Events** *(list) --*

      - *(string) --*

        The bucket event for which to send notifications.

    - **Filter** *(dict) --*

      - **Key** *(dict) --*

        - **FilterRules** *(list) --*

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


_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef(
    _ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKey` `FilterRules`

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


_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef(
    _ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilter` `Key`

    - **FilterRules** *(list) --*

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


_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef",
    {
        "Key": ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef(
    _ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponseTopicConfigurations` `Filter`

    - **Key** *(dict) --*

      - **FilterRules** *(list) --*

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


_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef",
    {
        "Id": str,
        "TopicArn": str,
        "Events": List[str],
        "Filter": ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef,
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef(
    _ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfigurationResponse` `TopicConfigurations`

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

      - **Key** *(dict) --*

        - **FilterRules** *(list) --*

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


_ClientGetBucketNotificationConfigurationResponseTypeDef = TypedDict(
    "_ClientGetBucketNotificationConfigurationResponseTypeDef",
    {
        "TopicConfigurations": List[
            ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef
        ],
        "QueueConfigurations": List[
            ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef
        ],
        "LambdaFunctionConfigurations": List[
            ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientGetBucketNotificationConfigurationResponseTypeDef(
    _ClientGetBucketNotificationConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationConfiguration` `Response`

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

          - **Key** *(dict) --*

            - **FilterRules** *(list) --*

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

          - *(string) --*

            The bucket event for which to send notifications.

        - **Filter** *(dict) --*

          - **Key** *(dict) --*

            - **FilterRules** *(list) --*

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

          - **Key** *(dict) --*

            - **FilterRules** *(list) --*

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


_ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef = TypedDict(
    "_ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef",
    {
        "Id": str,
        "Event": str,
        "Events": List[str],
        "CloudFunction": str,
        "InvocationRole": str,
    },
    total=False,
)


class ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef(
    _ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationResponse` `CloudFunctionConfiguration`

    - **Id** *(string) --*

      An optional unique identifier for configurations in a notification configuration. If you
      don't provide one, Amazon S3 will assign an ID.

    - **Event** *(string) --*

      The bucket event for which to send notifications.

    - **Events** *(list) --*

      - *(string) --*

        The bucket event for which to send notifications.

    - **CloudFunction** *(string) --*

    - **InvocationRole** *(string) --*
    """


_ClientGetBucketNotificationResponseQueueConfigurationTypeDef = TypedDict(
    "_ClientGetBucketNotificationResponseQueueConfigurationTypeDef",
    {"Id": str, "Event": str, "Events": List[str], "Queue": str},
    total=False,
)


class ClientGetBucketNotificationResponseQueueConfigurationTypeDef(
    _ClientGetBucketNotificationResponseQueueConfigurationTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationResponse` `QueueConfiguration`

    - **Id** *(string) --*

      An optional unique identifier for configurations in a notification configuration. If you
      don't provide one, Amazon S3 will assign an ID.

    - **Event** *(string) --*

      The bucket event for which to send notifications.

    - **Events** *(list) --*

      - *(string) --*

        The bucket event for which to send notifications.

    - **Queue** *(string) --*
    """


_ClientGetBucketNotificationResponseTopicConfigurationTypeDef = TypedDict(
    "_ClientGetBucketNotificationResponseTopicConfigurationTypeDef",
    {"Id": str, "Events": List[str], "Event": str, "Topic": str},
    total=False,
)


class ClientGetBucketNotificationResponseTopicConfigurationTypeDef(
    _ClientGetBucketNotificationResponseTopicConfigurationTypeDef
):
    """
    Type definition for `ClientGetBucketNotificationResponse` `TopicConfiguration`

    - **Id** *(string) --*

      An optional unique identifier for configurations in a notification configuration. If you
      don't provide one, Amazon S3 will assign an ID.

    - **Events** *(list) --*

      - *(string) --*

        The bucket event for which to send notifications.

    - **Event** *(string) --*

      Bucket event for which to send notifications.

    - **Topic** *(string) --*

      Amazon SNS topic to which Amazon S3 will publish a message to report the specified events
      for the bucket.
    """


_ClientGetBucketNotificationResponseTypeDef = TypedDict(
    "_ClientGetBucketNotificationResponseTypeDef",
    {
        "TopicConfiguration": ClientGetBucketNotificationResponseTopicConfigurationTypeDef,
        "QueueConfiguration": ClientGetBucketNotificationResponseQueueConfigurationTypeDef,
        "CloudFunctionConfiguration": ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef,
    },
    total=False,
)


class ClientGetBucketNotificationResponseTypeDef(
    _ClientGetBucketNotificationResponseTypeDef
):
    """
    Type definition for `ClientGetBucketNotification` `Response`

    - **TopicConfiguration** *(dict) --*

      - **Id** *(string) --*

        An optional unique identifier for configurations in a notification configuration. If you
        don't provide one, Amazon S3 will assign an ID.

      - **Events** *(list) --*

        - *(string) --*

          The bucket event for which to send notifications.

      - **Event** *(string) --*

        Bucket event for which to send notifications.

      - **Topic** *(string) --*

        Amazon SNS topic to which Amazon S3 will publish a message to report the specified events
        for the bucket.

    - **QueueConfiguration** *(dict) --*

      - **Id** *(string) --*

        An optional unique identifier for configurations in a notification configuration. If you
        don't provide one, Amazon S3 will assign an ID.

      - **Event** *(string) --*

        The bucket event for which to send notifications.

      - **Events** *(list) --*

        - *(string) --*

          The bucket event for which to send notifications.

      - **Queue** *(string) --*

    - **CloudFunctionConfiguration** *(dict) --*

      - **Id** *(string) --*

        An optional unique identifier for configurations in a notification configuration. If you
        don't provide one, Amazon S3 will assign an ID.

      - **Event** *(string) --*

        The bucket event for which to send notifications.

      - **Events** *(list) --*

        - *(string) --*

          The bucket event for which to send notifications.

      - **CloudFunction** *(string) --*

      - **InvocationRole** *(string) --*
    """


_ClientGetBucketPolicyResponseTypeDef = TypedDict(
    "_ClientGetBucketPolicyResponseTypeDef", {"Policy": str}, total=False
)


class ClientGetBucketPolicyResponseTypeDef(_ClientGetBucketPolicyResponseTypeDef):
    """
    Type definition for `ClientGetBucketPolicy` `Response`

    - **Policy** *(string) --*

      The bucket policy as a JSON document.
    """


_ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef = TypedDict(
    "_ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef",
    {"IsPublic": bool},
    total=False,
)


class ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef(
    _ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef
):
    """
    Type definition for `ClientGetBucketPolicyStatusResponse` `PolicyStatus`

    The policy status for the specified bucket.

    - **IsPublic** *(boolean) --*

      The policy status for this bucket. ``TRUE`` indicates that this bucket is public. ``FALSE``
      indicates that the bucket is not public.
    """


_ClientGetBucketPolicyStatusResponseTypeDef = TypedDict(
    "_ClientGetBucketPolicyStatusResponseTypeDef",
    {"PolicyStatus": ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef},
    total=False,
)


class ClientGetBucketPolicyStatusResponseTypeDef(
    _ClientGetBucketPolicyStatusResponseTypeDef
):
    """
    Type definition for `ClientGetBucketPolicyStatus` `Response`

    - **PolicyStatus** *(dict) --*

      The policy status for the specified bucket.

      - **IsPublic** *(boolean) --*

        The policy status for this bucket. ``TRUE`` indicates that this bucket is public. ``FALSE``
        indicates that the bucket is not public.
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    {"Status": str},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfigurationRules` `DeleteMarkerReplication`

    - **Status** *(string) --*

      The status of the delete marker replication.

      .. note::

        In the current implementation, Amazon S3 doesn't replicate the delete markers. The
        status must be ``Disabled`` .
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    {"Owner": str},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfigurationRulesDestination` `AccessControlTranslation`

    Specify this only in a cross-account scenario (where source and destination bucket
    owners are not the same), and you want to change replica ownership to the AWS account
    that owns the destination bucket. If this is not specified in the replication
    configuration, the replicas are owned by same AWS account that owns the source object.

    - **Owner** *(string) --*

      Specifies the replica ownership. For default and valid values, see `PUT bucket
      replication
      <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html>`__
      in the *Amazon Simple Storage Service API Reference* .
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    {"ReplicaKmsKeyID": str},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfigurationRulesDestination` `EncryptionConfiguration`

    A container that provides information about encryption. If
    ``SourceSelectionCriteria`` is specified, you must specify this element.

    - **ReplicaKmsKeyID** *(string) --*

      Specifies the AWS KMS Key ID (Key ARN or Alias ARN) for the destination bucket.
      Amazon S3 uses this key to encrypt replica objects.
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef",
    {
        "Bucket": str,
        "Account": str,
        "StorageClass": str,
        "AccessControlTranslation": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef,
        "EncryptionConfiguration": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfigurationRules` `Destination`

    A container for information about the replication destination.

    - **Bucket** *(string) --*

      The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store
      replicas of the object identified by the rule.

      A replication configuration can replicate objects to only one destination bucket. If
      there are multiple rules in your replication configuration, all rules must specify
      the same destination bucket.

    - **Account** *(string) --*

      Destination bucket owner account ID. In a cross-account scenario, if you direct
      Amazon S3 to change replica ownership to the AWS account that owns the destination
      bucket by specifying the ``AccessControlTranslation`` property, this is the account
      ID of the destination bucket owner. For more information, see `Cross-Region
      Replication Additional Configuration: Change Replica Owner
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-change-owner.html>`__ in the
      *Amazon Simple Storage Service Developer Guide* .

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
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAnd` `Tags`

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfigurationRulesFilter` `And`

    A container for specifying rule filters. The filters determine the subset of objects
    to which the rule applies. This element is required only if you specify more than one
    filter. For example:

    * If you specify both a ``Prefix`` and a ``Tag`` filter, wrap these filters in an
    ``And`` tag.

    * If you specify a filter based on multiple tags, wrap the ``Tag`` elements in an
    ``And`` tag.

    - **Prefix** *(string) --*

    - **Tags** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

          Name of the tag.

        - **Value** *(string) --*

          Value of the tag.
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfigurationRulesFilter` `Tag`

    A container for specifying a tag key and value.

    The rule applies only to objects that have the tag in their tag set.

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef,
        "And": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfigurationRules` `Filter`

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

      - **Tags** *(list) --*

        - *(dict) --*

          - **Key** *(string) --*

            Name of the tag.

          - **Value** *(string) --*

            Value of the tag.
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    {"Status": str},
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteria` `SseKmsEncryptedObjects`

    A container for filter information for the selection of Amazon S3 objects encrypted
    with AWS KMS. If you include ``SourceSelectionCriteria`` in the replication
    configuration, this element is required.

    - **Status** *(string) --*

      Specifies whether Amazon S3 replicates objects created with server-side encryption
      using an AWS KMS-managed key.
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfigurationRules` `SourceSelectionCriteria`

    A container that describes additional filters for identifying the source objects that
    you want to replicate. You can choose to enable or disable the replication of these
    objects. Currently, Amazon S3 supports only the filter that you can specify for objects
    created with server-side encryption using an AWS KMS-Managed Key (SSE-KMS).

    - **SseKmsEncryptedObjects** *(dict) --*

      A container for filter information for the selection of Amazon S3 objects encrypted
      with AWS KMS. If you include ``SourceSelectionCriteria`` in the replication
      configuration, this element is required.

      - **Status** *(string) --*

        Specifies whether Amazon S3 replicates objects created with server-side encryption
        using an AWS KMS-managed key.
    """


_ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef,
        "Status": str,
        "SourceSelectionCriteria": ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef,
        "Destination": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef,
        "DeleteMarkerReplication": ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef,
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponseReplicationConfiguration` `Rules`

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

      For more information, see `Cross-Region Replication (CRR)
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html>`__ in the *Amazon S3
      Developer Guide* .

    - **Prefix** *(string) --*

      An object keyname prefix that identifies the object or objects to which the rule
      applies. The maximum prefix length is 1,024 characters. To include all objects in a
      bucket, specify an empty string.

    - **Filter** *(dict) --*

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

        - **Tags** *(list) --*

          - *(dict) --*

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
      created with server-side encryption using an AWS KMS-Managed Key (SSE-KMS).

      - **SseKmsEncryptedObjects** *(dict) --*

        A container for filter information for the selection of Amazon S3 objects encrypted
        with AWS KMS. If you include ``SourceSelectionCriteria`` in the replication
        configuration, this element is required.

        - **Status** *(string) --*

          Specifies whether Amazon S3 replicates objects created with server-side encryption
          using an AWS KMS-managed key.

    - **Destination** *(dict) --*

      A container for information about the replication destination.

      - **Bucket** *(string) --*

        The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store
        replicas of the object identified by the rule.

        A replication configuration can replicate objects to only one destination bucket. If
        there are multiple rules in your replication configuration, all rules must specify
        the same destination bucket.

      - **Account** *(string) --*

        Destination bucket owner account ID. In a cross-account scenario, if you direct
        Amazon S3 to change replica ownership to the AWS account that owns the destination
        bucket by specifying the ``AccessControlTranslation`` property, this is the account
        ID of the destination bucket owner. For more information, see `Cross-Region
        Replication Additional Configuration: Change Replica Owner
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-change-owner.html>`__ in the
        *Amazon Simple Storage Service Developer Guide* .

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

      - **Status** *(string) --*

        The status of the delete marker replication.

        .. note::

          In the current implementation, Amazon S3 doesn't replicate the delete markers. The
          status must be ``Disabled`` .
    """


_ClientGetBucketReplicationResponseReplicationConfigurationTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseReplicationConfigurationTypeDef",
    {
        "Role": str,
        "Rules": List[
            ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef
        ],
    },
    total=False,
)


class ClientGetBucketReplicationResponseReplicationConfigurationTypeDef(
    _ClientGetBucketReplicationResponseReplicationConfigurationTypeDef
):
    """
    Type definition for `ClientGetBucketReplicationResponse` `ReplicationConfiguration`

    - **Role** *(string) --*

      The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
      Amazon S3 assumes when replicating objects. For more information, see `How to Set Up
      Cross-Region Replication
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-how-setup.html>`__ in the *Amazon
      Simple Storage Service Developer Guide* .

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

          For more information, see `Cross-Region Replication (CRR)
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html>`__ in the *Amazon S3
          Developer Guide* .

        - **Prefix** *(string) --*

          An object keyname prefix that identifies the object or objects to which the rule
          applies. The maximum prefix length is 1,024 characters. To include all objects in a
          bucket, specify an empty string.

        - **Filter** *(dict) --*

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

            - **Tags** *(list) --*

              - *(dict) --*

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
          created with server-side encryption using an AWS KMS-Managed Key (SSE-KMS).

          - **SseKmsEncryptedObjects** *(dict) --*

            A container for filter information for the selection of Amazon S3 objects encrypted
            with AWS KMS. If you include ``SourceSelectionCriteria`` in the replication
            configuration, this element is required.

            - **Status** *(string) --*

              Specifies whether Amazon S3 replicates objects created with server-side encryption
              using an AWS KMS-managed key.

        - **Destination** *(dict) --*

          A container for information about the replication destination.

          - **Bucket** *(string) --*

            The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store
            replicas of the object identified by the rule.

            A replication configuration can replicate objects to only one destination bucket. If
            there are multiple rules in your replication configuration, all rules must specify
            the same destination bucket.

          - **Account** *(string) --*

            Destination bucket owner account ID. In a cross-account scenario, if you direct
            Amazon S3 to change replica ownership to the AWS account that owns the destination
            bucket by specifying the ``AccessControlTranslation`` property, this is the account
            ID of the destination bucket owner. For more information, see `Cross-Region
            Replication Additional Configuration: Change Replica Owner
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-change-owner.html>`__ in the
            *Amazon Simple Storage Service Developer Guide* .

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

          - **Status** *(string) --*

            The status of the delete marker replication.

            .. note::

              In the current implementation, Amazon S3 doesn't replicate the delete markers. The
              status must be ``Disabled`` .
    """


_ClientGetBucketReplicationResponseTypeDef = TypedDict(
    "_ClientGetBucketReplicationResponseTypeDef",
    {
        "ReplicationConfiguration": ClientGetBucketReplicationResponseReplicationConfigurationTypeDef
    },
    total=False,
)


class ClientGetBucketReplicationResponseTypeDef(
    _ClientGetBucketReplicationResponseTypeDef
):
    """
    Type definition for `ClientGetBucketReplication` `Response`

    - **ReplicationConfiguration** *(dict) --*

      - **Role** *(string) --*

        The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
        Amazon S3 assumes when replicating objects. For more information, see `How to Set Up
        Cross-Region Replication
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-how-setup.html>`__ in the *Amazon
        Simple Storage Service Developer Guide* .

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

            For more information, see `Cross-Region Replication (CRR)
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html>`__ in the *Amazon S3
            Developer Guide* .

          - **Prefix** *(string) --*

            An object keyname prefix that identifies the object or objects to which the rule
            applies. The maximum prefix length is 1,024 characters. To include all objects in a
            bucket, specify an empty string.

          - **Filter** *(dict) --*

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

              - **Tags** *(list) --*

                - *(dict) --*

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
            created with server-side encryption using an AWS KMS-Managed Key (SSE-KMS).

            - **SseKmsEncryptedObjects** *(dict) --*

              A container for filter information for the selection of Amazon S3 objects encrypted
              with AWS KMS. If you include ``SourceSelectionCriteria`` in the replication
              configuration, this element is required.

              - **Status** *(string) --*

                Specifies whether Amazon S3 replicates objects created with server-side encryption
                using an AWS KMS-managed key.

          - **Destination** *(dict) --*

            A container for information about the replication destination.

            - **Bucket** *(string) --*

              The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store
              replicas of the object identified by the rule.

              A replication configuration can replicate objects to only one destination bucket. If
              there are multiple rules in your replication configuration, all rules must specify
              the same destination bucket.

            - **Account** *(string) --*

              Destination bucket owner account ID. In a cross-account scenario, if you direct
              Amazon S3 to change replica ownership to the AWS account that owns the destination
              bucket by specifying the ``AccessControlTranslation`` property, this is the account
              ID of the destination bucket owner. For more information, see `Cross-Region
              Replication Additional Configuration: Change Replica Owner
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-change-owner.html>`__ in the
              *Amazon Simple Storage Service Developer Guide* .

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

            - **Status** *(string) --*

              The status of the delete marker replication.

              .. note::

                In the current implementation, Amazon S3 doesn't replicate the delete markers. The
                status must be ``Disabled`` .
    """


_ClientGetBucketRequestPaymentResponseTypeDef = TypedDict(
    "_ClientGetBucketRequestPaymentResponseTypeDef", {"Payer": str}, total=False
)


class ClientGetBucketRequestPaymentResponseTypeDef(
    _ClientGetBucketRequestPaymentResponseTypeDef
):
    """
    Type definition for `ClientGetBucketRequestPayment` `Response`

    - **Payer** *(string) --*

      Specifies who pays for the download and request fees.
    """


_ClientGetBucketTaggingResponseTagSetTypeDef = TypedDict(
    "_ClientGetBucketTaggingResponseTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetBucketTaggingResponseTagSetTypeDef(
    _ClientGetBucketTaggingResponseTagSetTypeDef
):
    """
    Type definition for `ClientGetBucketTaggingResponse` `TagSet`

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientGetBucketTaggingResponseTypeDef = TypedDict(
    "_ClientGetBucketTaggingResponseTypeDef",
    {"TagSet": List[ClientGetBucketTaggingResponseTagSetTypeDef]},
    total=False,
)


class ClientGetBucketTaggingResponseTypeDef(_ClientGetBucketTaggingResponseTypeDef):
    """
    Type definition for `ClientGetBucketTagging` `Response`

    - **TagSet** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

          Name of the tag.

        - **Value** *(string) --*

          Value of the tag.
    """


_ClientGetBucketVersioningResponseTypeDef = TypedDict(
    "_ClientGetBucketVersioningResponseTypeDef",
    {"Status": str, "MFADelete": str},
    total=False,
)


class ClientGetBucketVersioningResponseTypeDef(
    _ClientGetBucketVersioningResponseTypeDef
):
    """
    Type definition for `ClientGetBucketVersioning` `Response`

    - **Status** *(string) --*

      The versioning state of the bucket.

    - **MFADelete** *(string) --*

      Specifies whether MFA delete is enabled in the bucket versioning configuration. This element
      is only returned if the bucket has been configured with MFA delete. If the bucket has never
      been so configured, this element is not returned.
    """


_ClientGetBucketWebsiteResponseErrorDocumentTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseErrorDocumentTypeDef", {"Key": str}, total=False
)


class ClientGetBucketWebsiteResponseErrorDocumentTypeDef(
    _ClientGetBucketWebsiteResponseErrorDocumentTypeDef
):
    """
    Type definition for `ClientGetBucketWebsiteResponse` `ErrorDocument`

    - **Key** *(string) --*

      The object key name to use when a 4XX class error occurs.
    """


_ClientGetBucketWebsiteResponseIndexDocumentTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseIndexDocumentTypeDef", {"Suffix": str}, total=False
)


class ClientGetBucketWebsiteResponseIndexDocumentTypeDef(
    _ClientGetBucketWebsiteResponseIndexDocumentTypeDef
):
    """
    Type definition for `ClientGetBucketWebsiteResponse` `IndexDocument`

    - **Suffix** *(string) --*

      A suffix that is appended to a request that is for a directory on the website endpoint
      (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data
      that is returned will be for the object with the key name images/index.html) The suffix
      must not be empty and must not include a slash character.
    """


_ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef",
    {"HostName": str, "Protocol": str},
    total=False,
)


class ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef(
    _ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef
):
    """
    Type definition for `ClientGetBucketWebsiteResponse` `RedirectAllRequestsTo`

    - **HostName** *(string) --*

      Name of the host where requests are redirected.

    - **Protocol** *(string) --*

      Protocol to use when redirecting requests. The default is the protocol that is used in the
      original request.
    """


_ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef",
    {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str},
    total=False,
)


class ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef(
    _ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef
):
    """
    Type definition for `ClientGetBucketWebsiteResponseRoutingRules` `Condition`

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
    """


_ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": str,
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)


class ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef(
    _ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef
):
    """
    Type definition for `ClientGetBucketWebsiteResponseRoutingRules` `Redirect`

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


_ClientGetBucketWebsiteResponseRoutingRulesTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseRoutingRulesTypeDef",
    {
        "Condition": ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef,
        "Redirect": ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef,
    },
    total=False,
)


class ClientGetBucketWebsiteResponseRoutingRulesTypeDef(
    _ClientGetBucketWebsiteResponseRoutingRulesTypeDef
):
    """
    Type definition for `ClientGetBucketWebsiteResponse` `RoutingRules`

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


_ClientGetBucketWebsiteResponseTypeDef = TypedDict(
    "_ClientGetBucketWebsiteResponseTypeDef",
    {
        "RedirectAllRequestsTo": ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef,
        "IndexDocument": ClientGetBucketWebsiteResponseIndexDocumentTypeDef,
        "ErrorDocument": ClientGetBucketWebsiteResponseErrorDocumentTypeDef,
        "RoutingRules": List[ClientGetBucketWebsiteResponseRoutingRulesTypeDef],
    },
    total=False,
)


class ClientGetBucketWebsiteResponseTypeDef(_ClientGetBucketWebsiteResponseTypeDef):
    """
    Type definition for `ClientGetBucketWebsite` `Response`

    - **RedirectAllRequestsTo** *(dict) --*

      - **HostName** *(string) --*

        Name of the host where requests are redirected.

      - **Protocol** *(string) --*

        Protocol to use when redirecting requests. The default is the protocol that is used in the
        original request.

    - **IndexDocument** *(dict) --*

      - **Suffix** *(string) --*

        A suffix that is appended to a request that is for a directory on the website endpoint
        (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data
        that is returned will be for the object with the key name images/index.html) The suffix
        must not be empty and must not include a slash character.

    - **ErrorDocument** *(dict) --*

      - **Key** *(string) --*

        The object key name to use when a 4XX class error occurs.

    - **RoutingRules** *(list) --*

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


_ClientGetObjectAclResponseGrantsGranteeTypeDef = TypedDict(
    "_ClientGetObjectAclResponseGrantsGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "Type": str, "URI": str},
    total=False,
)


class ClientGetObjectAclResponseGrantsGranteeTypeDef(
    _ClientGetObjectAclResponseGrantsGranteeTypeDef
):
    """
    Type definition for `ClientGetObjectAclResponseGrants` `Grantee`

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
    """


_ClientGetObjectAclResponseGrantsTypeDef = TypedDict(
    "_ClientGetObjectAclResponseGrantsTypeDef",
    {"Grantee": ClientGetObjectAclResponseGrantsGranteeTypeDef, "Permission": str},
    total=False,
)


class ClientGetObjectAclResponseGrantsTypeDef(_ClientGetObjectAclResponseGrantsTypeDef):
    """
    Type definition for `ClientGetObjectAclResponse` `Grants`

    - **Grantee** *(dict) --*

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


_ClientGetObjectAclResponseOwnerTypeDef = TypedDict(
    "_ClientGetObjectAclResponseOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientGetObjectAclResponseOwnerTypeDef(_ClientGetObjectAclResponseOwnerTypeDef):
    """
    Type definition for `ClientGetObjectAclResponse` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientGetObjectAclResponseTypeDef = TypedDict(
    "_ClientGetObjectAclResponseTypeDef",
    {
        "Owner": ClientGetObjectAclResponseOwnerTypeDef,
        "Grants": List[ClientGetObjectAclResponseGrantsTypeDef],
        "RequestCharged": str,
    },
    total=False,
)


class ClientGetObjectAclResponseTypeDef(_ClientGetObjectAclResponseTypeDef):
    """
    Type definition for `ClientGetObjectAcl` `Response`

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*

    - **Grants** *(list) --*

      A list of grants.

      - *(dict) --*

        - **Grantee** *(dict) --*

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


_ClientGetObjectLegalHoldResponseLegalHoldTypeDef = TypedDict(
    "_ClientGetObjectLegalHoldResponseLegalHoldTypeDef", {"Status": str}, total=False
)


class ClientGetObjectLegalHoldResponseLegalHoldTypeDef(
    _ClientGetObjectLegalHoldResponseLegalHoldTypeDef
):
    """
    Type definition for `ClientGetObjectLegalHoldResponse` `LegalHold`

    The current Legal Hold status for the specified object.

    - **Status** *(string) --*

      Indicates whether the specified object has a Legal Hold in place.
    """


_ClientGetObjectLegalHoldResponseTypeDef = TypedDict(
    "_ClientGetObjectLegalHoldResponseTypeDef",
    {"LegalHold": ClientGetObjectLegalHoldResponseLegalHoldTypeDef},
    total=False,
)


class ClientGetObjectLegalHoldResponseTypeDef(_ClientGetObjectLegalHoldResponseTypeDef):
    """
    Type definition for `ClientGetObjectLegalHold` `Response`

    - **LegalHold** *(dict) --*

      The current Legal Hold status for the specified object.

      - **Status** *(string) --*

        Indicates whether the specified object has a Legal Hold in place.
    """


_ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef = TypedDict(
    "_ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef",
    {"Mode": str, "Days": int, "Years": int},
    total=False,
)


class ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef(
    _ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef
):
    """
    Type definition for `ClientGetObjectLockConfigurationResponseObjectLockConfigurationRule` `DefaultRetention`

    The default retention period that you want to apply to new objects placed in the
    specified bucket.

    - **Mode** *(string) --*

      The default object lock retention mode you want to apply to new objects placed in the
      specified bucket.

    - **Days** *(integer) --*

      The number of days that you want to specify for the default retention period.

    - **Years** *(integer) --*

      The number of years that you want to specify for the default retention period.
    """


_ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef = TypedDict(
    "_ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef",
    {
        "DefaultRetention": ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef
    },
    total=False,
)


class ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef(
    _ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef
):
    """
    Type definition for `ClientGetObjectLockConfigurationResponseObjectLockConfiguration` `Rule`

    The object lock rule in place for the specified object.

    - **DefaultRetention** *(dict) --*

      The default retention period that you want to apply to new objects placed in the
      specified bucket.

      - **Mode** *(string) --*

        The default object lock retention mode you want to apply to new objects placed in the
        specified bucket.

      - **Days** *(integer) --*

        The number of days that you want to specify for the default retention period.

      - **Years** *(integer) --*

        The number of years that you want to specify for the default retention period.
    """


_ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef = TypedDict(
    "_ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": str,
        "Rule": ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef,
    },
    total=False,
)


class ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef(
    _ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef
):
    """
    Type definition for `ClientGetObjectLockConfigurationResponse` `ObjectLockConfiguration`

    The specified bucket's object lock configuration.

    - **ObjectLockEnabled** *(string) --*

      Indicates whether this bucket has an object lock configuration enabled.

    - **Rule** *(dict) --*

      The object lock rule in place for the specified object.

      - **DefaultRetention** *(dict) --*

        The default retention period that you want to apply to new objects placed in the
        specified bucket.

        - **Mode** *(string) --*

          The default object lock retention mode you want to apply to new objects placed in the
          specified bucket.

        - **Days** *(integer) --*

          The number of days that you want to specify for the default retention period.

        - **Years** *(integer) --*

          The number of years that you want to specify for the default retention period.
    """


_ClientGetObjectLockConfigurationResponseTypeDef = TypedDict(
    "_ClientGetObjectLockConfigurationResponseTypeDef",
    {
        "ObjectLockConfiguration": ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef
    },
    total=False,
)


class ClientGetObjectLockConfigurationResponseTypeDef(
    _ClientGetObjectLockConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetObjectLockConfiguration` `Response`

    - **ObjectLockConfiguration** *(dict) --*

      The specified bucket's object lock configuration.

      - **ObjectLockEnabled** *(string) --*

        Indicates whether this bucket has an object lock configuration enabled.

      - **Rule** *(dict) --*

        The object lock rule in place for the specified object.

        - **DefaultRetention** *(dict) --*

          The default retention period that you want to apply to new objects placed in the
          specified bucket.

          - **Mode** *(string) --*

            The default object lock retention mode you want to apply to new objects placed in the
            specified bucket.

          - **Days** *(integer) --*

            The number of days that you want to specify for the default retention period.

          - **Years** *(integer) --*

            The number of years that you want to specify for the default retention period.
    """


_ClientGetObjectResponseTypeDef = TypedDict(
    "_ClientGetObjectResponseTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": str,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": str,
        "RequestCharged": str,
        "ReplicationStatus": str,
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": str,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": str,
    },
    total=False,
)


class ClientGetObjectResponseTypeDef(_ClientGetObjectResponseTypeDef):
    """
    Type definition for `ClientGetObject` `Response`

    - **Body** (:class:`.StreamingBody`) --

      Object data.

    - **DeleteMarker** *(boolean) --*

      Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If
      false, this response header does not appear in the response.

    - **AcceptRanges** *(string) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **StorageClass** *(string) --*

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **ReplicationStatus** *(string) --*

    - **PartsCount** *(integer) --*

      The count of parts this object has.

    - **TagCount** *(integer) --*

      The number of tags, if any, on the object.

    - **ObjectLockMode** *(string) --*

      The object lock mode currently in place for this object.

    - **ObjectLockRetainUntilDate** *(datetime) --*

      The date and time when this object's object lock will expire.

    - **ObjectLockLegalHoldStatus** *(string) --*

      Indicates whether this object has an active legal hold. This field is only returned if you
      have permission to view an object's legal hold status.
    """


_ClientGetObjectRetentionResponseRetentionTypeDef = TypedDict(
    "_ClientGetObjectRetentionResponseRetentionTypeDef",
    {"Mode": str, "RetainUntilDate": datetime},
    total=False,
)


class ClientGetObjectRetentionResponseRetentionTypeDef(
    _ClientGetObjectRetentionResponseRetentionTypeDef
):
    """
    Type definition for `ClientGetObjectRetentionResponse` `Retention`

    The container element for an object's retention settings.

    - **Mode** *(string) --*

      Indicates the Retention mode for the specified object.

    - **RetainUntilDate** *(datetime) --*

      The date on which this object lock retention expires.
    """


_ClientGetObjectRetentionResponseTypeDef = TypedDict(
    "_ClientGetObjectRetentionResponseTypeDef",
    {"Retention": ClientGetObjectRetentionResponseRetentionTypeDef},
    total=False,
)


class ClientGetObjectRetentionResponseTypeDef(_ClientGetObjectRetentionResponseTypeDef):
    """
    Type definition for `ClientGetObjectRetention` `Response`

    - **Retention** *(dict) --*

      The container element for an object's retention settings.

      - **Mode** *(string) --*

        Indicates the Retention mode for the specified object.

      - **RetainUntilDate** *(datetime) --*

        The date on which this object lock retention expires.
    """


_ClientGetObjectTaggingResponseTagSetTypeDef = TypedDict(
    "_ClientGetObjectTaggingResponseTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetObjectTaggingResponseTagSetTypeDef(
    _ClientGetObjectTaggingResponseTagSetTypeDef
):
    """
    Type definition for `ClientGetObjectTaggingResponse` `TagSet`

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientGetObjectTaggingResponseTypeDef = TypedDict(
    "_ClientGetObjectTaggingResponseTypeDef",
    {"VersionId": str, "TagSet": List[ClientGetObjectTaggingResponseTagSetTypeDef]},
    total=False,
)


class ClientGetObjectTaggingResponseTypeDef(_ClientGetObjectTaggingResponseTypeDef):
    """
    Type definition for `ClientGetObjectTagging` `Response`

    - **VersionId** *(string) --*

    - **TagSet** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

          Name of the tag.

        - **Value** *(string) --*

          Value of the tag.
    """


_ClientGetObjectTorrentResponseTypeDef = TypedDict(
    "_ClientGetObjectTorrentResponseTypeDef", {"RequestCharged": str}, total=False
)


class ClientGetObjectTorrentResponseTypeDef(_ClientGetObjectTorrentResponseTypeDef):
    """
    Type definition for `ClientGetObjectTorrent` `Response`

    - **Body** (:class:`.StreamingBody`) --

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef = TypedDict(
    "_ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)


class ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef(
    _ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef
):
    """
    Type definition for `ClientGetPublicAccessBlockResponse` `PublicAccessBlockConfiguration`

    The ``PublicAccessBlock`` configuration currently in effect for this Amazon S3 bucket.

    - **BlockPublicAcls** *(boolean) --*

      Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket
      and objects in this bucket. Setting this element to ``TRUE`` causes the following behavior:

      * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.

      * PUT Object calls fail if the request includes a public ACL.

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


_ClientGetPublicAccessBlockResponseTypeDef = TypedDict(
    "_ClientGetPublicAccessBlockResponseTypeDef",
    {
        "PublicAccessBlockConfiguration": ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef
    },
    total=False,
)


class ClientGetPublicAccessBlockResponseTypeDef(
    _ClientGetPublicAccessBlockResponseTypeDef
):
    """
    Type definition for `ClientGetPublicAccessBlock` `Response`

    - **PublicAccessBlockConfiguration** *(dict) --*

      The ``PublicAccessBlock`` configuration currently in effect for this Amazon S3 bucket.

      - **BlockPublicAcls** *(boolean) --*

        Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket
        and objects in this bucket. Setting this element to ``TRUE`` causes the following behavior:

        * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.

        * PUT Object calls fail if the request includes a public ACL.

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


_ClientHeadObjectResponseTypeDef = TypedDict(
    "_ClientHeadObjectResponseTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": str,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": str,
        "RequestCharged": str,
        "ReplicationStatus": str,
        "PartsCount": int,
        "ObjectLockMode": str,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": str,
    },
    total=False,
)


class ClientHeadObjectResponseTypeDef(_ClientHeadObjectResponseTypeDef):
    """
    Type definition for `ClientHeadObject` `Response`

    - **DeleteMarker** *(boolean) --*

      Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If
      false, this response header does not appear in the response.

    - **AcceptRanges** *(string) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **StorageClass** *(string) --*

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **ReplicationStatus** *(string) --*

    - **PartsCount** *(integer) --*

      The count of parts this object has.

    - **ObjectLockMode** *(string) --*

      The object lock mode currently in place for this object.

    - **ObjectLockRetainUntilDate** *(datetime) --*

      The date and time when this object's object lock expires.

    - **ObjectLockLegalHoldStatus** *(string) --*

      The Legal Hold status for the specified object.
    """


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef
):
    """
    Type definition for `ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAnd` `Tags`

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef
):
    """
    Type definition for `ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilter` `And`

    A conjunction (logical AND) of predicates, which is used in evaluating an analytics
    filter. The operator must have at least two predicates.

    - **Prefix** *(string) --*

      The prefix to use when evaluating an AND predicate: The prefix that an object must
      have to be included in the metrics results.

    - **Tags** *(list) --*

      The list of tags to use when evaluating an AND predicate.

      - *(dict) --*

        - **Key** *(string) --*

          Name of the tag.

        - **Value** *(string) --*

          Value of the tag.
    """


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef
):
    """
    Type definition for `ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilter` `Tag`

    The tag to use when evaluating an analytics filter.

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef,
        "And": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef,
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef
):
    """
    Type definition for `ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationList` `Filter`

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

          - **Key** *(string) --*

            Name of the tag.

          - **Value** *(string) --*

            Value of the tag.
    """


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
):
    """
    Type definition for `ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestination` `S3BucketDestination`

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


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef
):
    """
    Type definition for `ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExport` `Destination`

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


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef
):
    """
    Type definition for `ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysis` `DataExport`

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


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef
):
    """
    Type definition for `ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationList` `StorageClassAnalysis`

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


_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef",
    {
        "Id": str,
        "Filter": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef,
        "StorageClassAnalysis": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef,
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef
):
    """
    Type definition for `ClientListBucketAnalyticsConfigurationsResponse` `AnalyticsConfigurationList`

    Specifies the configuration and any analyses for the analytics filter of an Amazon S3
    bucket.

    For more information, see `GET Bucket analytics
    <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETAnalyticsConfig.html>`__ in
    the *Amazon Simple Storage Service API Reference* .

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


_ClientListBucketAnalyticsConfigurationsResponseTypeDef = TypedDict(
    "_ClientListBucketAnalyticsConfigurationsResponseTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "AnalyticsConfigurationList": List[
            ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef
        ],
    },
    total=False,
)


class ClientListBucketAnalyticsConfigurationsResponseTypeDef(
    _ClientListBucketAnalyticsConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientListBucketAnalyticsConfigurations` `Response`

    - **IsTruncated** *(boolean) --*

      Indicates whether the returned list of analytics configurations is complete. A value of true
      indicates that the list is not complete and the NextContinuationToken will be provided for a
      subsequent request.

    - **ContinuationToken** *(string) --*

      The ContinuationToken that represents where this request began.

    - **NextContinuationToken** *(string) --*

      NextContinuationToken is sent when isTruncated is true, which indicates that there are more
      analytics configurations to list. The next request must include this NextContinuationToken.
      The token is obfuscated and is not a usable value.

    - **AnalyticsConfigurationList** *(list) --*

      The list of analytics configurations for a bucket.

      - *(dict) --*

        Specifies the configuration and any analyses for the analytics filter of an Amazon S3
        bucket.

        For more information, see `GET Bucket analytics
        <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETAnalyticsConfig.html>`__ in
        the *Amazon Simple Storage Service API Reference* .

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


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef
):
    """
    Type definition for `ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryption` `SSEKMS`

    Specifies the use of SSE-KMS to encrypt delivered Inventory reports.

    - **KeyId** *(string) --*

      Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
      use for encrypting Inventory reports.
    """


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict,
        "SSEKMS": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef
):
    """
    Type definition for `ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestination` `Encryption`

    Contains the type of server-side encryption used to encrypt the inventory results.

    - **SSES3** *(dict) --*

      Specifies the use of SSE-S3 to encrypt delivered Inventory reports.

    - **SSEKMS** *(dict) --*

      Specifies the use of SSE-KMS to encrypt delivered Inventory reports.

      - **KeyId** *(string) --*

        Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
        use for encrypting Inventory reports.
    """


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": str,
        "Prefix": str,
        "Encryption": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef
):
    """
    Type definition for `ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestination` `S3BucketDestination`

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

          Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
          use for encrypting Inventory reports.
    """


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef",
    {
        "S3BucketDestination": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef
    },
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef
):
    """
    Type definition for `ClientListBucketInventoryConfigurationsResponseInventoryConfigurationList` `Destination`

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

            Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
            use for encrypting Inventory reports.
    """


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef",
    {"Prefix": str},
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef
):
    """
    Type definition for `ClientListBucketInventoryConfigurationsResponseInventoryConfigurationList` `Filter`

    Specifies an inventory filter. The inventory only includes objects that meet the filter's
    criteria.

    - **Prefix** *(string) --*

      The prefix that an object must have to be included in the inventory results.
    """


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef",
    {"Frequency": str},
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef
):
    """
    Type definition for `ClientListBucketInventoryConfigurationsResponseInventoryConfigurationList` `Schedule`

    Specifies the schedule for generating inventory results.

    - **Frequency** *(string) --*

      Specifies how frequently inventory results are produced.
    """


_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef",
    {
        "Destination": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef,
        "IsEnabled": bool,
        "Filter": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef,
        "Id": str,
        "IncludedObjectVersions": str,
        "OptionalFields": List[str],
        "Schedule": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef,
    },
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef(
    _ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef
):
    """
    Type definition for `ClientListBucketInventoryConfigurationsResponse` `InventoryConfigurationList`

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

              Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
              use for encrypting Inventory reports.

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
    """


_ClientListBucketInventoryConfigurationsResponseTypeDef = TypedDict(
    "_ClientListBucketInventoryConfigurationsResponseTypeDef",
    {
        "ContinuationToken": str,
        "InventoryConfigurationList": List[
            ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef
        ],
        "IsTruncated": bool,
        "NextContinuationToken": str,
    },
    total=False,
)


class ClientListBucketInventoryConfigurationsResponseTypeDef(
    _ClientListBucketInventoryConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientListBucketInventoryConfigurations` `Response`

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

                  Specifies the ID of the AWS Key Management Service (KMS) master encryption key to
                  use for encrypting Inventory reports.

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

      Indicates whether the returned list of inventory configurations is truncated in this
      response. A value of true indicates that the list is truncated.

    - **NextContinuationToken** *(string) --*

      The marker used to continue this inventory configuration listing. Use the
      NextContinuationToken from this response to continue the listing in a subsequent request. The
      continuation token is an opaque value that Amazon S3 understands.
    """


_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef(
    _ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef
):
    """
    Type definition for `ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAnd` `Tags`

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef(
    _ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef
):
    """
    Type definition for `ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilter` `And`

    A conjunction (logical AND) of predicates, which is used in evaluating a metrics
    filter. The operator must have at least two predicates, and an object must match all of
    the predicates in order for the filter to apply.

    - **Prefix** *(string) --*

      The prefix used when evaluating an AND predicate.

    - **Tags** *(list) --*

      The list of tags used when evaluating an AND predicate.

      - *(dict) --*

        - **Key** *(string) --*

          Name of the tag.

        - **Value** *(string) --*

          Value of the tag.
    """


_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef(
    _ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef
):
    """
    Type definition for `ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilter` `Tag`

    The tag used when evaluating a metrics filter.

    - **Key** *(string) --*

      Name of the tag.

    - **Value** *(string) --*

      Value of the tag.
    """


_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef,
        "And": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef,
    },
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef(
    _ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef
):
    """
    Type definition for `ClientListBucketMetricsConfigurationsResponseMetricsConfigurationList` `Filter`

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

          - **Key** *(string) --*

            Name of the tag.

          - **Value** *(string) --*

            Value of the tag.
    """


_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef",
    {
        "Id": str,
        "Filter": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef,
    },
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef(
    _ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef
):
    """
    Type definition for `ClientListBucketMetricsConfigurationsResponse` `MetricsConfigurationList`

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

            - **Key** *(string) --*

              Name of the tag.

            - **Value** *(string) --*

              Value of the tag.
    """


_ClientListBucketMetricsConfigurationsResponseTypeDef = TypedDict(
    "_ClientListBucketMetricsConfigurationsResponseTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "MetricsConfigurationList": List[
            ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef
        ],
    },
    total=False,
)


class ClientListBucketMetricsConfigurationsResponseTypeDef(
    _ClientListBucketMetricsConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientListBucketMetricsConfigurations` `Response`

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

                - **Key** *(string) --*

                  Name of the tag.

                - **Value** *(string) --*

                  Value of the tag.
    """


_ClientListBucketsResponseBucketsTypeDef = TypedDict(
    "_ClientListBucketsResponseBucketsTypeDef",
    {"Name": str, "CreationDate": datetime},
    total=False,
)


class ClientListBucketsResponseBucketsTypeDef(_ClientListBucketsResponseBucketsTypeDef):
    """
    Type definition for `ClientListBucketsResponse` `Buckets`

    - **Name** *(string) --*

      The name of the bucket.

    - **CreationDate** *(datetime) --*

      Date the bucket was created.
    """


_ClientListBucketsResponseOwnerTypeDef = TypedDict(
    "_ClientListBucketsResponseOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientListBucketsResponseOwnerTypeDef(_ClientListBucketsResponseOwnerTypeDef):
    """
    Type definition for `ClientListBucketsResponse` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientListBucketsResponseTypeDef = TypedDict(
    "_ClientListBucketsResponseTypeDef",
    {
        "Buckets": List[ClientListBucketsResponseBucketsTypeDef],
        "Owner": ClientListBucketsResponseOwnerTypeDef,
    },
    total=False,
)


class ClientListBucketsResponseTypeDef(_ClientListBucketsResponseTypeDef):
    """
    Type definition for `ClientListBuckets` `Response`

    - **Buckets** *(list) --*

      - *(dict) --*

        - **Name** *(string) --*

          The name of the bucket.

        - **CreationDate** *(datetime) --*

          Date the bucket was created.

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*
    """


_ClientListMultipartUploadsResponseCommonPrefixesTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseCommonPrefixesTypeDef",
    {"Prefix": str},
    total=False,
)


class ClientListMultipartUploadsResponseCommonPrefixesTypeDef(
    _ClientListMultipartUploadsResponseCommonPrefixesTypeDef
):
    """
    Type definition for `ClientListMultipartUploadsResponse` `CommonPrefixes`

    - **Prefix** *(string) --*
    """


_ClientListMultipartUploadsResponseUploadsInitiatorTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseUploadsInitiatorTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)


class ClientListMultipartUploadsResponseUploadsInitiatorTypeDef(
    _ClientListMultipartUploadsResponseUploadsInitiatorTypeDef
):
    """
    Type definition for `ClientListMultipartUploadsResponseUploads` `Initiator`

    Identifies who initiated the multipart upload.

    - **ID** *(string) --*

      If the principal is an AWS account, it provides the Canonical User ID. If the principal
      is an IAM User, it provides a user ARN value.

    - **DisplayName** *(string) --*

      Name of the Principal.
    """


_ClientListMultipartUploadsResponseUploadsOwnerTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseUploadsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientListMultipartUploadsResponseUploadsOwnerTypeDef(
    _ClientListMultipartUploadsResponseUploadsOwnerTypeDef
):
    """
    Type definition for `ClientListMultipartUploadsResponseUploads` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientListMultipartUploadsResponseUploadsTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseUploadsTypeDef",
    {
        "UploadId": str,
        "Key": str,
        "Initiated": datetime,
        "StorageClass": str,
        "Owner": ClientListMultipartUploadsResponseUploadsOwnerTypeDef,
        "Initiator": ClientListMultipartUploadsResponseUploadsInitiatorTypeDef,
    },
    total=False,
)


class ClientListMultipartUploadsResponseUploadsTypeDef(
    _ClientListMultipartUploadsResponseUploadsTypeDef
):
    """
    Type definition for `ClientListMultipartUploadsResponse` `Uploads`

    - **UploadId** *(string) --*

      Upload ID that identifies the multipart upload.

    - **Key** *(string) --*

      Key of the object for which the multipart upload was initiated.

    - **Initiated** *(datetime) --*

      Date and time at which the multipart upload was initiated.

    - **StorageClass** *(string) --*

      The class of storage used to store the object.

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*

    - **Initiator** *(dict) --*

      Identifies who initiated the multipart upload.

      - **ID** *(string) --*

        If the principal is an AWS account, it provides the Canonical User ID. If the principal
        is an IAM User, it provides a user ARN value.

      - **DisplayName** *(string) --*

        Name of the Principal.
    """


_ClientListMultipartUploadsResponseTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseTypeDef",
    {
        "Bucket": str,
        "KeyMarker": str,
        "UploadIdMarker": str,
        "NextKeyMarker": str,
        "Prefix": str,
        "Delimiter": str,
        "NextUploadIdMarker": str,
        "MaxUploads": int,
        "IsTruncated": bool,
        "Uploads": List[ClientListMultipartUploadsResponseUploadsTypeDef],
        "CommonPrefixes": List[ClientListMultipartUploadsResponseCommonPrefixesTypeDef],
        "EncodingType": str,
    },
    total=False,
)


class ClientListMultipartUploadsResponseTypeDef(
    _ClientListMultipartUploadsResponseTypeDef
):
    """
    Type definition for `ClientListMultipartUploads` `Response`

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

      - *(dict) --*

        - **UploadId** *(string) --*

          Upload ID that identifies the multipart upload.

        - **Key** *(string) --*

          Key of the object for which the multipart upload was initiated.

        - **Initiated** *(datetime) --*

          Date and time at which the multipart upload was initiated.

        - **StorageClass** *(string) --*

          The class of storage used to store the object.

        - **Owner** *(dict) --*

          - **DisplayName** *(string) --*

          - **ID** *(string) --*

        - **Initiator** *(dict) --*

          Identifies who initiated the multipart upload.

          - **ID** *(string) --*

            If the principal is an AWS account, it provides the Canonical User ID. If the principal
            is an IAM User, it provides a user ARN value.

          - **DisplayName** *(string) --*

            Name of the Principal.

    - **CommonPrefixes** *(list) --*

      - *(dict) --*

        - **Prefix** *(string) --*

    - **EncodingType** *(string) --*

      Encoding type used by Amazon S3 to encode object keys in the response.
    """


_ClientListObjectVersionsResponseCommonPrefixesTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseCommonPrefixesTypeDef",
    {"Prefix": str},
    total=False,
)


class ClientListObjectVersionsResponseCommonPrefixesTypeDef(
    _ClientListObjectVersionsResponseCommonPrefixesTypeDef
):
    """
    Type definition for `ClientListObjectVersionsResponse` `CommonPrefixes`

    - **Prefix** *(string) --*
    """


_ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef(
    _ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef
):
    """
    Type definition for `ClientListObjectVersionsResponseDeleteMarkers` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientListObjectVersionsResponseDeleteMarkersTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseDeleteMarkersTypeDef",
    {
        "Owner": ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)


class ClientListObjectVersionsResponseDeleteMarkersTypeDef(
    _ClientListObjectVersionsResponseDeleteMarkersTypeDef
):
    """
    Type definition for `ClientListObjectVersionsResponse` `DeleteMarkers`

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*

    - **Key** *(string) --*

      The object key.

    - **VersionId** *(string) --*

      Version ID of an object.

    - **IsLatest** *(boolean) --*

      Specifies whether the object is (true) or is not (false) the latest version of an object.

    - **LastModified** *(datetime) --*

      Date and time the object was last modified.
    """


_ClientListObjectVersionsResponseVersionsOwnerTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseVersionsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientListObjectVersionsResponseVersionsOwnerTypeDef(
    _ClientListObjectVersionsResponseVersionsOwnerTypeDef
):
    """
    Type definition for `ClientListObjectVersionsResponseVersions` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientListObjectVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseVersionsTypeDef",
    {
        "ETag": str,
        "Size": int,
        "StorageClass": str,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
        "Owner": ClientListObjectVersionsResponseVersionsOwnerTypeDef,
    },
    total=False,
)


class ClientListObjectVersionsResponseVersionsTypeDef(
    _ClientListObjectVersionsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListObjectVersionsResponse` `Versions`

    - **ETag** *(string) --*

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

      - **DisplayName** *(string) --*

      - **ID** *(string) --*
    """


_ClientListObjectVersionsResponseTypeDef = TypedDict(
    "_ClientListObjectVersionsResponseTypeDef",
    {
        "IsTruncated": bool,
        "KeyMarker": str,
        "VersionIdMarker": str,
        "NextKeyMarker": str,
        "NextVersionIdMarker": str,
        "Versions": List[ClientListObjectVersionsResponseVersionsTypeDef],
        "DeleteMarkers": List[ClientListObjectVersionsResponseDeleteMarkersTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ClientListObjectVersionsResponseCommonPrefixesTypeDef],
        "EncodingType": str,
    },
    total=False,
)


class ClientListObjectVersionsResponseTypeDef(_ClientListObjectVersionsResponseTypeDef):
    """
    Type definition for `ClientListObjectVersions` `Response`

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the
      search criteria. If your results were truncated, you can make a follow-up paginated request
      using the NextKeyMarker and NextVersionIdMarker response parameters as a starting place in
      another request to return the rest of the results.

    - **KeyMarker** *(string) --*

      Marks the last Key returned in a truncated response.

    - **VersionIdMarker** *(string) --*

    - **NextKeyMarker** *(string) --*

      Use this value for the key marker request parameter in a subsequent request.

    - **NextVersionIdMarker** *(string) --*

      Use this value for the next version id marker parameter in a subsequent request.

    - **Versions** *(list) --*

      - *(dict) --*

        - **ETag** *(string) --*

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

          - **DisplayName** *(string) --*

          - **ID** *(string) --*

    - **DeleteMarkers** *(list) --*

      - *(dict) --*

        - **Owner** *(dict) --*

          - **DisplayName** *(string) --*

          - **ID** *(string) --*

        - **Key** *(string) --*

          The object key.

        - **VersionId** *(string) --*

          Version ID of an object.

        - **IsLatest** *(boolean) --*

          Specifies whether the object is (true) or is not (false) the latest version of an object.

        - **LastModified** *(datetime) --*

          Date and time the object was last modified.

    - **Name** *(string) --*

    - **Prefix** *(string) --*

    - **Delimiter** *(string) --*

    - **MaxKeys** *(integer) --*

    - **CommonPrefixes** *(list) --*

      - *(dict) --*

        - **Prefix** *(string) --*

    - **EncodingType** *(string) --*

      Encoding type used by Amazon S3 to encode object keys in the response.
    """


_ClientListObjectsResponseCommonPrefixesTypeDef = TypedDict(
    "_ClientListObjectsResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ClientListObjectsResponseCommonPrefixesTypeDef(
    _ClientListObjectsResponseCommonPrefixesTypeDef
):
    """
    Type definition for `ClientListObjectsResponse` `CommonPrefixes`

    - **Prefix** *(string) --*
    """


_ClientListObjectsResponseContentsOwnerTypeDef = TypedDict(
    "_ClientListObjectsResponseContentsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientListObjectsResponseContentsOwnerTypeDef(
    _ClientListObjectsResponseContentsOwnerTypeDef
):
    """
    Type definition for `ClientListObjectsResponseContents` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientListObjectsResponseContentsTypeDef = TypedDict(
    "_ClientListObjectsResponseContentsTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": str,
        "Owner": ClientListObjectsResponseContentsOwnerTypeDef,
    },
    total=False,
)


class ClientListObjectsResponseContentsTypeDef(
    _ClientListObjectsResponseContentsTypeDef
):
    """
    Type definition for `ClientListObjectsResponse` `Contents`

    - **Key** *(string) --*

    - **LastModified** *(datetime) --*

    - **ETag** *(string) --*

    - **Size** *(integer) --*

    - **StorageClass** *(string) --*

      The class of storage used to store the object.

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*
    """


_ClientListObjectsResponseTypeDef = TypedDict(
    "_ClientListObjectsResponseTypeDef",
    {
        "IsTruncated": bool,
        "Marker": str,
        "NextMarker": str,
        "Contents": List[ClientListObjectsResponseContentsTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ClientListObjectsResponseCommonPrefixesTypeDef],
        "EncodingType": str,
    },
    total=False,
)


class ClientListObjectsResponseTypeDef(_ClientListObjectsResponseTypeDef):
    """
    Type definition for `ClientListObjects` `Response`

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the
      search criteria.

    - **Marker** *(string) --*

    - **NextMarker** *(string) --*

      When response is truncated (the IsTruncated element value in the response is true), you can
      use the key name in this field as marker in the subsequent request to get next set of
      objects. Amazon S3 lists objects in alphabetical order Note: This element is returned only if
      you have delimiter request parameter specified. If response does not include the NextMaker
      and it is truncated, you can use the value of the last Key in the response as the marker in
      the subsequent request to get the next set of object keys.

    - **Contents** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **LastModified** *(datetime) --*

        - **ETag** *(string) --*

        - **Size** *(integer) --*

        - **StorageClass** *(string) --*

          The class of storage used to store the object.

        - **Owner** *(dict) --*

          - **DisplayName** *(string) --*

          - **ID** *(string) --*

    - **Name** *(string) --*

    - **Prefix** *(string) --*

    - **Delimiter** *(string) --*

    - **MaxKeys** *(integer) --*

    - **CommonPrefixes** *(list) --*

      - *(dict) --*

        - **Prefix** *(string) --*

    - **EncodingType** *(string) --*

      Encoding type used by Amazon S3 to encode object keys in the response.
    """


_ClientListObjectsV2ResponseCommonPrefixesTypeDef = TypedDict(
    "_ClientListObjectsV2ResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ClientListObjectsV2ResponseCommonPrefixesTypeDef(
    _ClientListObjectsV2ResponseCommonPrefixesTypeDef
):
    """
    Type definition for `ClientListObjectsV2Response` `CommonPrefixes`

    - **Prefix** *(string) --*
    """


_ClientListObjectsV2ResponseContentsOwnerTypeDef = TypedDict(
    "_ClientListObjectsV2ResponseContentsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientListObjectsV2ResponseContentsOwnerTypeDef(
    _ClientListObjectsV2ResponseContentsOwnerTypeDef
):
    """
    Type definition for `ClientListObjectsV2ResponseContents` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientListObjectsV2ResponseContentsTypeDef = TypedDict(
    "_ClientListObjectsV2ResponseContentsTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": str,
        "Owner": ClientListObjectsV2ResponseContentsOwnerTypeDef,
    },
    total=False,
)


class ClientListObjectsV2ResponseContentsTypeDef(
    _ClientListObjectsV2ResponseContentsTypeDef
):
    """
    Type definition for `ClientListObjectsV2Response` `Contents`

    - **Key** *(string) --*

    - **LastModified** *(datetime) --*

    - **ETag** *(string) --*

    - **Size** *(integer) --*

    - **StorageClass** *(string) --*

      The class of storage used to store the object.

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*
    """


_ClientListObjectsV2ResponseTypeDef = TypedDict(
    "_ClientListObjectsV2ResponseTypeDef",
    {
        "IsTruncated": bool,
        "Contents": List[ClientListObjectsV2ResponseContentsTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ClientListObjectsV2ResponseCommonPrefixesTypeDef],
        "EncodingType": str,
        "KeyCount": int,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "StartAfter": str,
    },
    total=False,
)


class ClientListObjectsV2ResponseTypeDef(_ClientListObjectsV2ResponseTypeDef):
    """
    Type definition for `ClientListObjectsV2` `Response`

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the
      search criteria.

    - **Contents** *(list) --*

      Metadata about each object returned.

      - *(dict) --*

        - **Key** *(string) --*

        - **LastModified** *(datetime) --*

        - **ETag** *(string) --*

        - **Size** *(integer) --*

        - **StorageClass** *(string) --*

          The class of storage used to store the object.

        - **Owner** *(dict) --*

          - **DisplayName** *(string) --*

          - **ID** *(string) --*

    - **Name** *(string) --*

      Name of the bucket to list.

    - **Prefix** *(string) --*

      Limits the response to keys that begin with the specified prefix.

    - **Delimiter** *(string) --*

      A delimiter is a character you use to group keys.

    - **MaxKeys** *(integer) --*

      Sets the maximum number of keys returned in the response. The response might contain fewer
      keys but will never contain more.

    - **CommonPrefixes** *(list) --*

      CommonPrefixes contains all (if there are any) keys between Prefix and the next occurrence of
      the string specified by delimiter

      - *(dict) --*

        - **Prefix** *(string) --*

    - **EncodingType** *(string) --*

      Encoding type used by Amazon S3 to encode object keys in the response.

    - **KeyCount** *(integer) --*

      KeyCount is the number of keys returned with this request. KeyCount will always be less than
      equals to MaxKeys field. Say you ask for 50 keys, your result will include less than equals
      50 keys

    - **ContinuationToken** *(string) --*

      ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a
      token. ContinuationToken is obfuscated and is not a real key

    - **NextContinuationToken** *(string) --*

      NextContinuationToken is sent when isTruncated is true which means there are more keys in the
      bucket that can be listed. The next list requests to Amazon S3 can be continued with this
      NextContinuationToken. NextContinuationToken is obfuscated and is not a real key

    - **StartAfter** *(string) --*

      StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after
      this specified key. StartAfter can be any key in the bucket
    """


_ClientListPartsResponseInitiatorTypeDef = TypedDict(
    "_ClientListPartsResponseInitiatorTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)


class ClientListPartsResponseInitiatorTypeDef(_ClientListPartsResponseInitiatorTypeDef):
    """
    Type definition for `ClientListPartsResponse` `Initiator`

    Identifies who initiated the multipart upload.

    - **ID** *(string) --*

      If the principal is an AWS account, it provides the Canonical User ID. If the principal is
      an IAM User, it provides a user ARN value.

    - **DisplayName** *(string) --*

      Name of the Principal.
    """


_ClientListPartsResponseOwnerTypeDef = TypedDict(
    "_ClientListPartsResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)


class ClientListPartsResponseOwnerTypeDef(_ClientListPartsResponseOwnerTypeDef):
    """
    Type definition for `ClientListPartsResponse` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientListPartsResponsePartsTypeDef = TypedDict(
    "_ClientListPartsResponsePartsTypeDef",
    {"PartNumber": int, "LastModified": datetime, "ETag": str, "Size": int},
    total=False,
)


class ClientListPartsResponsePartsTypeDef(_ClientListPartsResponsePartsTypeDef):
    """
    Type definition for `ClientListPartsResponse` `Parts`

    - **PartNumber** *(integer) --*

      Part number identifying the part. This is a positive integer between 1 and 10,000.

    - **LastModified** *(datetime) --*

      Date and time at which the part was uploaded.

    - **ETag** *(string) --*

      Entity tag returned when the part was uploaded.

    - **Size** *(integer) --*

      Size in bytes of the uploaded part data.
    """


_ClientListPartsResponseTypeDef = TypedDict(
    "_ClientListPartsResponseTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "PartNumberMarker": int,
        "NextPartNumberMarker": int,
        "MaxParts": int,
        "IsTruncated": bool,
        "Parts": List[ClientListPartsResponsePartsTypeDef],
        "Initiator": ClientListPartsResponseInitiatorTypeDef,
        "Owner": ClientListPartsResponseOwnerTypeDef,
        "StorageClass": str,
        "RequestCharged": str,
    },
    total=False,
)


class ClientListPartsResponseTypeDef(_ClientListPartsResponseTypeDef):
    """
    Type definition for `ClientListParts` `Response`

    - **AbortDate** *(datetime) --*

      Date when multipart upload will become eligible for abort operation by lifecycle.

    - **AbortRuleId** *(string) --*

      Id of the lifecycle rule that makes a multipart upload eligible for abort operation.

    - **Bucket** *(string) --*

      Name of the bucket to which the multipart upload was initiated.

    - **Key** *(string) --*

      Object key for which the multipart upload was initiated.

    - **UploadId** *(string) --*

      Upload ID identifying the multipart upload whose parts are being listed.

    - **PartNumberMarker** *(integer) --*

      Part number after which listing begins.

    - **NextPartNumberMarker** *(integer) --*

      When a list is truncated, this element specifies the last part in the list, as well as the
      value to use for the part-number-marker request parameter in a subsequent request.

    - **MaxParts** *(integer) --*

      Maximum number of parts that were allowed in the response.

    - **IsTruncated** *(boolean) --*

      Indicates whether the returned list of parts is truncated.

    - **Parts** *(list) --*

      - *(dict) --*

        - **PartNumber** *(integer) --*

          Part number identifying the part. This is a positive integer between 1 and 10,000.

        - **LastModified** *(datetime) --*

          Date and time at which the part was uploaded.

        - **ETag** *(string) --*

          Entity tag returned when the part was uploaded.

        - **Size** *(integer) --*

          Size in bytes of the uploaded part data.

    - **Initiator** *(dict) --*

      Identifies who initiated the multipart upload.

      - **ID** *(string) --*

        If the principal is an AWS account, it provides the Canonical User ID. If the principal is
        an IAM User, it provides a user ARN value.

      - **DisplayName** *(string) --*

        Name of the Principal.

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*

    - **StorageClass** *(string) --*

      The class of storage used to store the object.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_RequiredClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_RequiredClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef", {"Type": str}
)
_OptionalClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_OptionalClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "URI": str},
    total=False,
)


class ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef(
    _RequiredClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef,
    _OptionalClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef,
):
    """
    Type definition for `ClientPutBucketAclAccessControlPolicyGrants` `Grantee`

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
    """


_ClientPutBucketAclAccessControlPolicyGrantsTypeDef = TypedDict(
    "_ClientPutBucketAclAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientPutBucketAclAccessControlPolicyGrantsTypeDef(
    _ClientPutBucketAclAccessControlPolicyGrantsTypeDef
):
    """
    Type definition for `ClientPutBucketAclAccessControlPolicy` `Grants`

    - **Grantee** *(dict) --*

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
    """


_ClientPutBucketAclAccessControlPolicyOwnerTypeDef = TypedDict(
    "_ClientPutBucketAclAccessControlPolicyOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientPutBucketAclAccessControlPolicyOwnerTypeDef(
    _ClientPutBucketAclAccessControlPolicyOwnerTypeDef
):
    """
    Type definition for `ClientPutBucketAclAccessControlPolicy` `Owner`

    Container for the bucket owner's display name and ID.

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientPutBucketAclAccessControlPolicyTypeDef = TypedDict(
    "_ClientPutBucketAclAccessControlPolicyTypeDef",
    {
        "Grants": List[ClientPutBucketAclAccessControlPolicyGrantsTypeDef],
        "Owner": ClientPutBucketAclAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)


class ClientPutBucketAclAccessControlPolicyTypeDef(
    _ClientPutBucketAclAccessControlPolicyTypeDef
):
    """
    Type definition for `ClientPutBucketAcl` `AccessControlPolicy`

    Contains the elements that set the ACL permissions for an object per grantee.

    - **Grants** *(list) --*

      A list of grants.

      - *(dict) --*

        - **Grantee** *(dict) --*

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

      - **ID** *(string) --*
    """


_ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    {"Status": str},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfigurationRules` `DeleteMarkerReplication`

    - **Status** *(string) --*

      The status of the delete marker replication.

      .. note::

        In the current implementation, Amazon S3 doesn't replicate the delete markers. The
        status must be ``Disabled`` .
    """


_ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    {"Owner": str},
)


class ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfigurationRulesDestination` `AccessControlTranslation`

    Specify this only in a cross-account scenario (where source and destination bucket owners
    are not the same), and you want to change replica ownership to the AWS account that owns
    the destination bucket. If this is not specified in the replication configuration, the
    replicas are owned by same AWS account that owns the source object.

    - **Owner** *(string) --* **[REQUIRED]**

      Specifies the replica ownership. For default and valid values, see `PUT bucket
      replication
      <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html>`__ in
      the *Amazon Simple Storage Service API Reference* .
    """


_ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    {"ReplicaKmsKeyID": str},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfigurationRulesDestination` `EncryptionConfiguration`

    A container that provides information about encryption. If ``SourceSelectionCriteria`` is
    specified, you must specify this element.

    - **ReplicaKmsKeyID** *(string) --*

      Specifies the AWS KMS Key ID (Key ARN or Alias ARN) for the destination bucket. Amazon
      S3 uses this key to encrypt replica objects.
    """


_RequiredClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef = TypedDict(
    "_RequiredClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef",
    {"Bucket": str},
)
_OptionalClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef = TypedDict(
    "_OptionalClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef",
    {
        "Account": str,
        "StorageClass": str,
        "AccessControlTranslation": ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef,
        "EncryptionConfiguration": ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef(
    _RequiredClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef,
    _OptionalClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef,
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfigurationRules` `Destination`

    A container for information about the replication destination.

    - **Bucket** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store replicas
      of the object identified by the rule.

      A replication configuration can replicate objects to only one destination bucket. If
      there are multiple rules in your replication configuration, all rules must specify the
      same destination bucket.

    - **Account** *(string) --*

      Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3
      to change replica ownership to the AWS account that owns the destination bucket by
      specifying the ``AccessControlTranslation`` property, this is the account ID of the
      destination bucket owner. For more information, see `Cross-Region Replication Additional
      Configuration: Change Replica Owner
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-change-owner.html>`__ in the *Amazon
      Simple Storage Service Developer Guide* .

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
    """


_ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
)


class ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfigurationRulesFilterAnd` `Tags`

    - **Key** *(string) --* **[REQUIRED]**

      Name of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag.
    """


_ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfigurationRulesFilter` `And`

    A container for specifying rule filters. The filters determine the subset of objects to
    which the rule applies. This element is required only if you specify more than one
    filter. For example:

    * If you specify both a ``Prefix`` and a ``Tag`` filter, wrap these filters in an ``And``
    tag.

    * If you specify a filter based on multiple tags, wrap the ``Tag`` elements in an ``And``
    tag.

    - **Prefix** *(string) --*

    - **Tags** *(list) --*

      - *(dict) --*

        - **Key** *(string) --* **[REQUIRED]**

          Name of the tag.

        - **Value** *(string) --* **[REQUIRED]**

          Value of the tag.
    """


_ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
)


class ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfigurationRulesFilter` `Tag`

    A container for specifying a tag key and value.

    The rule applies only to objects that have the tag in their tag set.

    - **Key** *(string) --* **[REQUIRED]**

      Name of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag.
    """


_ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef,
        "And": ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfigurationRules` `Filter`

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

      - **Tags** *(list) --*

        - *(dict) --*

          - **Key** *(string) --* **[REQUIRED]**

            Name of the tag.

          - **Value** *(string) --* **[REQUIRED]**

            Value of the tag.
    """


_ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    {"Status": str},
)


class ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteria` `SseKmsEncryptedObjects`

    A container for filter information for the selection of Amazon S3 objects encrypted with
    AWS KMS. If you include ``SourceSelectionCriteria`` in the replication configuration,
    this element is required.

    - **Status** *(string) --* **[REQUIRED]**

      Specifies whether Amazon S3 replicates objects created with server-side encryption
      using an AWS KMS-managed key.
    """


_ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
    },
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfigurationRules` `SourceSelectionCriteria`

    A container that describes additional filters for identifying the source objects that you
    want to replicate. You can choose to enable or disable the replication of these objects.
    Currently, Amazon S3 supports only the filter that you can specify for objects created with
    server-side encryption using an AWS KMS-Managed Key (SSE-KMS).

    - **SseKmsEncryptedObjects** *(dict) --*

      A container for filter information for the selection of Amazon S3 objects encrypted with
      AWS KMS. If you include ``SourceSelectionCriteria`` in the replication configuration,
      this element is required.

      - **Status** *(string) --* **[REQUIRED]**

        Specifies whether Amazon S3 replicates objects created with server-side encryption
        using an AWS KMS-managed key.
    """


_RequiredClientPutBucketReplicationReplicationConfigurationRulesTypeDef = TypedDict(
    "_RequiredClientPutBucketReplicationReplicationConfigurationRulesTypeDef",
    {
        "Status": str,
        "Destination": ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef,
    },
)
_OptionalClientPutBucketReplicationReplicationConfigurationRulesTypeDef = TypedDict(
    "_OptionalClientPutBucketReplicationReplicationConfigurationRulesTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef,
        "SourceSelectionCriteria": ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef,
        "DeleteMarkerReplication": ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef,
    },
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationRulesTypeDef(
    _RequiredClientPutBucketReplicationReplicationConfigurationRulesTypeDef,
    _OptionalClientPutBucketReplicationReplicationConfigurationRulesTypeDef,
):
    """
    Type definition for `ClientPutBucketReplicationReplicationConfiguration` `Rules`

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

      For more information, see `Cross-Region Replication (CRR)
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html>`__ in the *Amazon S3 Developer
      Guide* .

    - **Prefix** *(string) --*

      An object keyname prefix that identifies the object or objects to which the rule applies.
      The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify
      an empty string.

    - **Filter** *(dict) --*

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

        - **Tags** *(list) --*

          - *(dict) --*

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
      server-side encryption using an AWS KMS-Managed Key (SSE-KMS).

      - **SseKmsEncryptedObjects** *(dict) --*

        A container for filter information for the selection of Amazon S3 objects encrypted with
        AWS KMS. If you include ``SourceSelectionCriteria`` in the replication configuration,
        this element is required.

        - **Status** *(string) --* **[REQUIRED]**

          Specifies whether Amazon S3 replicates objects created with server-side encryption
          using an AWS KMS-managed key.

    - **Destination** *(dict) --* **[REQUIRED]**

      A container for information about the replication destination.

      - **Bucket** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store replicas
        of the object identified by the rule.

        A replication configuration can replicate objects to only one destination bucket. If
        there are multiple rules in your replication configuration, all rules must specify the
        same destination bucket.

      - **Account** *(string) --*

        Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3
        to change replica ownership to the AWS account that owns the destination bucket by
        specifying the ``AccessControlTranslation`` property, this is the account ID of the
        destination bucket owner. For more information, see `Cross-Region Replication Additional
        Configuration: Change Replica Owner
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-change-owner.html>`__ in the *Amazon
        Simple Storage Service Developer Guide* .

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

      - **Status** *(string) --*

        The status of the delete marker replication.

        .. note::

          In the current implementation, Amazon S3 doesn't replicate the delete markers. The
          status must be ``Disabled`` .
    """


_ClientPutBucketReplicationReplicationConfigurationTypeDef = TypedDict(
    "_ClientPutBucketReplicationReplicationConfigurationTypeDef",
    {
        "Role": str,
        "Rules": List[ClientPutBucketReplicationReplicationConfigurationRulesTypeDef],
    },
)


class ClientPutBucketReplicationReplicationConfigurationTypeDef(
    _ClientPutBucketReplicationReplicationConfigurationTypeDef
):
    """
    Type definition for `ClientPutBucketReplication` `ReplicationConfiguration`

    - **Role** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that Amazon
      S3 assumes when replicating objects. For more information, see `How to Set Up Cross-Region
      Replication <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-how-setup.html>`__ in the
      *Amazon Simple Storage Service Developer Guide* .

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

          For more information, see `Cross-Region Replication (CRR)
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html>`__ in the *Amazon S3 Developer
          Guide* .

        - **Prefix** *(string) --*

          An object keyname prefix that identifies the object or objects to which the rule applies.
          The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify
          an empty string.

        - **Filter** *(dict) --*

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

            - **Tags** *(list) --*

              - *(dict) --*

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
          server-side encryption using an AWS KMS-Managed Key (SSE-KMS).

          - **SseKmsEncryptedObjects** *(dict) --*

            A container for filter information for the selection of Amazon S3 objects encrypted with
            AWS KMS. If you include ``SourceSelectionCriteria`` in the replication configuration,
            this element is required.

            - **Status** *(string) --* **[REQUIRED]**

              Specifies whether Amazon S3 replicates objects created with server-side encryption
              using an AWS KMS-managed key.

        - **Destination** *(dict) --* **[REQUIRED]**

          A container for information about the replication destination.

          - **Bucket** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the bucket where you want Amazon S3 to store replicas
            of the object identified by the rule.

            A replication configuration can replicate objects to only one destination bucket. If
            there are multiple rules in your replication configuration, all rules must specify the
            same destination bucket.

          - **Account** *(string) --*

            Destination bucket owner account ID. In a cross-account scenario, if you direct Amazon S3
            to change replica ownership to the AWS account that owns the destination bucket by
            specifying the ``AccessControlTranslation`` property, this is the account ID of the
            destination bucket owner. For more information, see `Cross-Region Replication Additional
            Configuration: Change Replica Owner
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-change-owner.html>`__ in the *Amazon
            Simple Storage Service Developer Guide* .

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

          - **Status** *(string) --*

            The status of the delete marker replication.

            .. note::

              In the current implementation, Amazon S3 doesn't replicate the delete markers. The
              status must be ``Disabled`` .
    """


_RequiredClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_RequiredClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef", {"Type": str}
)
_OptionalClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_OptionalClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "URI": str},
    total=False,
)


class ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef(
    _RequiredClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef,
    _OptionalClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef,
):
    """
    Type definition for `ClientPutObjectAclAccessControlPolicyGrants` `Grantee`

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
    """


_ClientPutObjectAclAccessControlPolicyGrantsTypeDef = TypedDict(
    "_ClientPutObjectAclAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientPutObjectAclAccessControlPolicyGrantsTypeDef(
    _ClientPutObjectAclAccessControlPolicyGrantsTypeDef
):
    """
    Type definition for `ClientPutObjectAclAccessControlPolicy` `Grants`

    - **Grantee** *(dict) --*

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
    """


_ClientPutObjectAclAccessControlPolicyOwnerTypeDef = TypedDict(
    "_ClientPutObjectAclAccessControlPolicyOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ClientPutObjectAclAccessControlPolicyOwnerTypeDef(
    _ClientPutObjectAclAccessControlPolicyOwnerTypeDef
):
    """
    Type definition for `ClientPutObjectAclAccessControlPolicy` `Owner`

    Container for the bucket owner's display name and ID.

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ClientPutObjectAclAccessControlPolicyTypeDef = TypedDict(
    "_ClientPutObjectAclAccessControlPolicyTypeDef",
    {
        "Grants": List[ClientPutObjectAclAccessControlPolicyGrantsTypeDef],
        "Owner": ClientPutObjectAclAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)


class ClientPutObjectAclAccessControlPolicyTypeDef(
    _ClientPutObjectAclAccessControlPolicyTypeDef
):
    """
    Type definition for `ClientPutObjectAcl` `AccessControlPolicy`

    Contains the elements that set the ACL permissions for an object per grantee.

    - **Grants** *(list) --*

      A list of grants.

      - *(dict) --*

        - **Grantee** *(dict) --*

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

      - **ID** *(string) --*
    """


_ClientPutObjectAclResponseTypeDef = TypedDict(
    "_ClientPutObjectAclResponseTypeDef", {"RequestCharged": str}, total=False
)


class ClientPutObjectAclResponseTypeDef(_ClientPutObjectAclResponseTypeDef):
    """
    Type definition for `ClientPutObjectAcl` `Response`

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientPutObjectLegalHoldLegalHoldTypeDef = TypedDict(
    "_ClientPutObjectLegalHoldLegalHoldTypeDef", {"Status": str}, total=False
)


class ClientPutObjectLegalHoldLegalHoldTypeDef(
    _ClientPutObjectLegalHoldLegalHoldTypeDef
):
    """
    Type definition for `ClientPutObjectLegalHold` `LegalHold`

    Container element for the Legal Hold configuration you want to apply to the specified object.

    - **Status** *(string) --*

      Indicates whether the specified object has a Legal Hold in place.
    """


_ClientPutObjectLegalHoldResponseTypeDef = TypedDict(
    "_ClientPutObjectLegalHoldResponseTypeDef", {"RequestCharged": str}, total=False
)


class ClientPutObjectLegalHoldResponseTypeDef(_ClientPutObjectLegalHoldResponseTypeDef):
    """
    Type definition for `ClientPutObjectLegalHold` `Response`

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef = TypedDict(
    "_ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef",
    {"Mode": str, "Days": int, "Years": int},
    total=False,
)


class ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef(
    _ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef
):
    """
    Type definition for `ClientPutObjectLockConfigurationObjectLockConfigurationRule` `DefaultRetention`

    The default retention period that you want to apply to new objects placed in the specified
    bucket.

    - **Mode** *(string) --*

      The default object lock retention mode you want to apply to new objects placed in the
      specified bucket.

    - **Days** *(integer) --*

      The number of days that you want to specify for the default retention period.

    - **Years** *(integer) --*

      The number of years that you want to specify for the default retention period.
    """


_ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef = TypedDict(
    "_ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef",
    {
        "DefaultRetention": ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef
    },
    total=False,
)


class ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef(
    _ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef
):
    """
    Type definition for `ClientPutObjectLockConfigurationObjectLockConfiguration` `Rule`

    The object lock rule in place for the specified object.

    - **DefaultRetention** *(dict) --*

      The default retention period that you want to apply to new objects placed in the specified
      bucket.

      - **Mode** *(string) --*

        The default object lock retention mode you want to apply to new objects placed in the
        specified bucket.

      - **Days** *(integer) --*

        The number of days that you want to specify for the default retention period.

      - **Years** *(integer) --*

        The number of years that you want to specify for the default retention period.
    """


_ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef = TypedDict(
    "_ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": str,
        "Rule": ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef,
    },
    total=False,
)


class ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef(
    _ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef
):
    """
    Type definition for `ClientPutObjectLockConfiguration` `ObjectLockConfiguration`

    The object lock configuration that you want to apply to the specified bucket.

    - **ObjectLockEnabled** *(string) --*

      Indicates whether this bucket has an object lock configuration enabled.

    - **Rule** *(dict) --*

      The object lock rule in place for the specified object.

      - **DefaultRetention** *(dict) --*

        The default retention period that you want to apply to new objects placed in the specified
        bucket.

        - **Mode** *(string) --*

          The default object lock retention mode you want to apply to new objects placed in the
          specified bucket.

        - **Days** *(integer) --*

          The number of days that you want to specify for the default retention period.

        - **Years** *(integer) --*

          The number of years that you want to specify for the default retention period.
    """


_ClientPutObjectLockConfigurationResponseTypeDef = TypedDict(
    "_ClientPutObjectLockConfigurationResponseTypeDef",
    {"RequestCharged": str},
    total=False,
)


class ClientPutObjectLockConfigurationResponseTypeDef(
    _ClientPutObjectLockConfigurationResponseTypeDef
):
    """
    Type definition for `ClientPutObjectLockConfiguration` `Response`

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientPutObjectResponseTypeDef = TypedDict(
    "_ClientPutObjectResponseTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": str,
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)


class ClientPutObjectResponseTypeDef(_ClientPutObjectResponseTypeDef):
    """
    Type definition for `ClientPutObject` `Response`

    - **Expiration** *(string) --*

      If the object expiration is configured, this will contain the expiration date (expiry-date)
      and rule ID (rule-id). The value of rule-id is URL encoded.

    - **ETag** *(string) --*

      Entity tag for the uploaded object.

    - **ServerSideEncryption** *(string) --*

      The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256,
      aws:kms).

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **SSEKMSEncryptionContext** *(string) --*

      If present, specifies the AWS KMS Encryption Context to use for object encryption. The value
      of this header is a base64-encoded UTF-8 string holding JSON with the encryption context
      key-value pairs.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientPutObjectRetentionResponseTypeDef = TypedDict(
    "_ClientPutObjectRetentionResponseTypeDef", {"RequestCharged": str}, total=False
)


class ClientPutObjectRetentionResponseTypeDef(_ClientPutObjectRetentionResponseTypeDef):
    """
    Type definition for `ClientPutObjectRetention` `Response`

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientPutObjectRetentionRetentionTypeDef = TypedDict(
    "_ClientPutObjectRetentionRetentionTypeDef",
    {"Mode": str, "RetainUntilDate": datetime},
    total=False,
)


class ClientPutObjectRetentionRetentionTypeDef(
    _ClientPutObjectRetentionRetentionTypeDef
):
    """
    Type definition for `ClientPutObjectRetention` `Retention`

    The container element for the Object Retention configuration.

    - **Mode** *(string) --*

      Indicates the Retention mode for the specified object.

    - **RetainUntilDate** *(datetime) --*

      The date on which this object lock retention expires.
    """


_ClientPutObjectTaggingResponseTypeDef = TypedDict(
    "_ClientPutObjectTaggingResponseTypeDef", {"VersionId": str}, total=False
)


class ClientPutObjectTaggingResponseTypeDef(_ClientPutObjectTaggingResponseTypeDef):
    """
    Type definition for `ClientPutObjectTagging` `Response`

    - **VersionId** *(string) --*
    """


_ClientPutObjectTaggingTaggingTagSetTypeDef = TypedDict(
    "_ClientPutObjectTaggingTaggingTagSetTypeDef", {"Key": str, "Value": str}
)


class ClientPutObjectTaggingTaggingTagSetTypeDef(
    _ClientPutObjectTaggingTaggingTagSetTypeDef
):
    """
    Type definition for `ClientPutObjectTaggingTagging` `TagSet`

    - **Key** *(string) --* **[REQUIRED]**

      Name of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag.
    """


_ClientPutObjectTaggingTaggingTypeDef = TypedDict(
    "_ClientPutObjectTaggingTaggingTypeDef",
    {"TagSet": List[ClientPutObjectTaggingTaggingTagSetTypeDef]},
)


class ClientPutObjectTaggingTaggingTypeDef(_ClientPutObjectTaggingTaggingTypeDef):
    """
    Type definition for `ClientPutObjectTagging` `Tagging`

    - **TagSet** *(list) --* **[REQUIRED]**

      - *(dict) --*

        - **Key** *(string) --* **[REQUIRED]**

          Name of the tag.

        - **Value** *(string) --* **[REQUIRED]**

          Value of the tag.
    """


_ClientRestoreObjectResponseTypeDef = TypedDict(
    "_ClientRestoreObjectResponseTypeDef",
    {"RequestCharged": str, "RestoreOutputPath": str},
    total=False,
)


class ClientRestoreObjectResponseTypeDef(_ClientRestoreObjectResponseTypeDef):
    """
    Type definition for `ClientRestoreObject` `Response`

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **RestoreOutputPath** *(string) --*

      Indicates the path in the provided S3 output location where Select results will be restored
      to.
    """


_ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef", {"Tier": str}
)


class ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef(
    _ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequest` `GlacierJobParameters`

    Glacier related parameters pertaining to this job. Do not use with restores that specify
    OutputLocation.

    - **Tier** *(string) --* **[REQUIRED]**

      Glacier retrieval tier at which the restore will be processed.
    """


_RequiredClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_RequiredClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {"Type": str},
)
_OptionalClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_OptionalClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "URI": str},
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef(
    _RequiredClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
    _OptionalClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlList` `Grantee`

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
    """


_ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestOutputLocationS3` `AccessControlList`

    - **Grantee** *(dict) --*

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
    """


_RequiredClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "_RequiredClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": str},
)
_OptionalClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "_OptionalClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef(
    _RequiredClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
    _OptionalClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestOutputLocationS3` `Encryption`

    - **EncryptionType** *(string) --* **[REQUIRED]**

      The server-side encryption algorithm used when storing job results in Amazon S3 (e.g.,
      AES256, aws:kms).

    - **KMSKeyId** *(string) --*

      If the encryption type is aws:kms, this optional value specifies the AWS KMS key ID to
      use for encryption of job results.

    - **KMSContext** *(string) --*

      If the encryption type is aws:kms, this optional value can be used to specify the
      encryption context for the restore results.
    """


_ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    {"Key": str, "Value": str},
)


class ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestOutputLocationS3Tagging` `TagSet`

    - **Key** *(string) --* **[REQUIRED]**

      Name of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag.
    """


_ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    {
        "TagSet": List[
            ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef
        ]
    },
)


class ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestOutputLocationS3` `Tagging`

    The tag-set that is applied to the restore results.

    - **TagSet** *(list) --* **[REQUIRED]**

      - *(dict) --*

        - **Key** *(string) --* **[REQUIRED]**

          Name of the tag.

        - **Value** *(string) --* **[REQUIRED]**

          Value of the tag.
    """


_ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestOutputLocationS3` `UserMetadata`

    A metadata key-value pair to store with an object.

    - **Name** *(string) --*

    - **Value** *(string) --*
    """


_RequiredClientRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "_RequiredClientRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    {"BucketName": str, "Prefix": str},
)
_OptionalClientRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "_OptionalClientRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    {
        "Encryption": ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
        "CannedACL": str,
        "AccessControlList": List[
            ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef,
        "UserMetadata": List[
            ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef
        ],
        "StorageClass": str,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef(
    _RequiredClientRestoreObjectRestoreRequestOutputLocationS3TypeDef,
    _OptionalClientRestoreObjectRestoreRequestOutputLocationS3TypeDef,
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestOutputLocation` `S3`

    Describes an S3 location that will receive the results of the restore request.

    - **BucketName** *(string) --* **[REQUIRED]**

      The name of the bucket where the restore results will be placed.

    - **Prefix** *(string) --* **[REQUIRED]**

      The prefix that is prepended to the restore results for this request.

    - **Encryption** *(dict) --*

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

        - **Grantee** *(dict) --*

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

        - *(dict) --*

          - **Key** *(string) --* **[REQUIRED]**

            Name of the tag.

          - **Value** *(string) --* **[REQUIRED]**

            Value of the tag.

    - **UserMetadata** *(list) --*

      A list of metadata to store with the restore results in S3.

      - *(dict) --*

        A metadata key-value pair to store with an object.

        - **Name** *(string) --*

        - **Value** *(string) --*

    - **StorageClass** *(string) --*

      The class of storage used to store the restore results.
    """


_ClientRestoreObjectRestoreRequestOutputLocationTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestOutputLocationTypeDef",
    {"S3": ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef},
    total=False,
)


class ClientRestoreObjectRestoreRequestOutputLocationTypeDef(
    _ClientRestoreObjectRestoreRequestOutputLocationTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequest` `OutputLocation`

    Describes the location where the restore job's output is stored.

    - **S3** *(dict) --*

      Describes an S3 location that will receive the results of the restore request.

      - **BucketName** *(string) --* **[REQUIRED]**

        The name of the bucket where the restore results will be placed.

      - **Prefix** *(string) --* **[REQUIRED]**

        The prefix that is prepended to the restore results for this request.

      - **Encryption** *(dict) --*

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

          - **Grantee** *(dict) --*

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

          - *(dict) --*

            - **Key** *(string) --* **[REQUIRED]**

              Name of the tag.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag.

      - **UserMetadata** *(list) --*

        A list of metadata to store with the restore results in S3.

        - *(dict) --*

          A metadata key-value pair to store with an object.

          - **Name** *(string) --*

          - **Value** *(string) --*

      - **StorageClass** *(string) --*

        The class of storage used to store the restore results.
    """


_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    {
        "FileHeaderInfo": str,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestSelectParametersInputSerialization` `CSV`

    Describes the serialization of a CSV-encoded object.

    - **FileHeaderInfo** *(string) --*

      Describes the first line of input. Valid values: None, Ignore, Use.

    - **Comments** *(string) --*

      The single character used to indicate a row should be ignored when present at the start
      of a row.

    - **QuoteEscapeCharacter** *(string) --*

      The single character used for escaping the quote character inside an already escaped
      value.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records.

    - **FieldDelimiter** *(string) --*

      The value used to separate individual fields in a record.

    - **QuoteCharacter** *(string) --*

      Value used for escaping where the field delimiter is part of the value.

    - **AllowQuotedRecordDelimiter** *(boolean) --*

      Specifies that CSV field values may contain quoted record delimiters and such records
      should be allowed. Default value is FALSE. Setting this value to TRUE may lower
      performance.
    """


_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    {"Type": str},
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestSelectParametersInputSerialization` `JSON`

    Specifies JSON as object's input serialization format.

    - **Type** *(string) --*

      The type of JSON. Valid values: Document, Lines.
    """


_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    {
        "CSV": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef,
        "CompressionType": str,
        "JSON": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef,
        "Parquet": Dict,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestSelectParameters` `InputSerialization`

    Describes the serialization format of the object.

    - **CSV** *(dict) --*

      Describes the serialization of a CSV-encoded object.

      - **FileHeaderInfo** *(string) --*

        Describes the first line of input. Valid values: None, Ignore, Use.

      - **Comments** *(string) --*

        The single character used to indicate a row should be ignored when present at the start
        of a row.

      - **QuoteEscapeCharacter** *(string) --*

        The single character used for escaping the quote character inside an already escaped
        value.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records.

      - **FieldDelimiter** *(string) --*

        The value used to separate individual fields in a record.

      - **QuoteCharacter** *(string) --*

        Value used for escaping where the field delimiter is part of the value.

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
    """


_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    {
        "QuoteFields": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestSelectParametersOutputSerialization` `CSV`

    Describes the serialization of CSV-encoded Select results.

    - **QuoteFields** *(string) --*

      Indicates whether or not all output fields should be quoted.

    - **QuoteEscapeCharacter** *(string) --*

      Th single character used for escaping the quote character inside an already escaped value.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records.

    - **FieldDelimiter** *(string) --*

      The value used to separate individual fields in a record.

    - **QuoteCharacter** *(string) --*

      The value used for escaping where the field delimiter is part of the value.
    """


_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestSelectParametersOutputSerialization` `JSON`

    Specifies JSON as request's output serialization format.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records in the output.
    """


_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    {
        "CSV": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef,
        "JSON": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequestSelectParameters` `OutputSerialization`

    Describes how the results of the Select job are serialized.

    - **CSV** *(dict) --*

      Describes the serialization of CSV-encoded Select results.

      - **QuoteFields** *(string) --*

        Indicates whether or not all output fields should be quoted.

      - **QuoteEscapeCharacter** *(string) --*

        Th single character used for escaping the quote character inside an already escaped value.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records.

      - **FieldDelimiter** *(string) --*

        The value used to separate individual fields in a record.

      - **QuoteCharacter** *(string) --*

        The value used for escaping where the field delimiter is part of the value.

    - **JSON** *(dict) --*

      Specifies JSON as request's output serialization format.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records in the output.
    """


_ClientRestoreObjectRestoreRequestSelectParametersTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestSelectParametersTypeDef",
    {
        "InputSerialization": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef,
    },
)


class ClientRestoreObjectRestoreRequestSelectParametersTypeDef(
    _ClientRestoreObjectRestoreRequestSelectParametersTypeDef
):
    """
    Type definition for `ClientRestoreObjectRestoreRequest` `SelectParameters`

    Describes the parameters for Select job types.

    - **InputSerialization** *(dict) --* **[REQUIRED]**

      Describes the serialization format of the object.

      - **CSV** *(dict) --*

        Describes the serialization of a CSV-encoded object.

        - **FileHeaderInfo** *(string) --*

          Describes the first line of input. Valid values: None, Ignore, Use.

        - **Comments** *(string) --*

          The single character used to indicate a row should be ignored when present at the start
          of a row.

        - **QuoteEscapeCharacter** *(string) --*

          The single character used for escaping the quote character inside an already escaped
          value.

        - **RecordDelimiter** *(string) --*

          The value used to separate individual records.

        - **FieldDelimiter** *(string) --*

          The value used to separate individual fields in a record.

        - **QuoteCharacter** *(string) --*

          Value used for escaping where the field delimiter is part of the value.

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

          Indicates whether or not all output fields should be quoted.

        - **QuoteEscapeCharacter** *(string) --*

          Th single character used for escaping the quote character inside an already escaped value.

        - **RecordDelimiter** *(string) --*

          The value used to separate individual records.

        - **FieldDelimiter** *(string) --*

          The value used to separate individual fields in a record.

        - **QuoteCharacter** *(string) --*

          The value used for escaping where the field delimiter is part of the value.

      - **JSON** *(dict) --*

        Specifies JSON as request's output serialization format.

        - **RecordDelimiter** *(string) --*

          The value used to separate individual records in the output.
    """


_ClientRestoreObjectRestoreRequestTypeDef = TypedDict(
    "_ClientRestoreObjectRestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef,
        "Type": str,
        "Tier": str,
        "Description": str,
        "SelectParameters": ClientRestoreObjectRestoreRequestSelectParametersTypeDef,
        "OutputLocation": ClientRestoreObjectRestoreRequestOutputLocationTypeDef,
    },
    total=False,
)


class ClientRestoreObjectRestoreRequestTypeDef(
    _ClientRestoreObjectRestoreRequestTypeDef
):
    """
    Type definition for `ClientRestoreObject` `RestoreRequest`

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

            Describes the first line of input. Valid values: None, Ignore, Use.

          - **Comments** *(string) --*

            The single character used to indicate a row should be ignored when present at the start
            of a row.

          - **QuoteEscapeCharacter** *(string) --*

            The single character used for escaping the quote character inside an already escaped
            value.

          - **RecordDelimiter** *(string) --*

            The value used to separate individual records.

          - **FieldDelimiter** *(string) --*

            The value used to separate individual fields in a record.

          - **QuoteCharacter** *(string) --*

            Value used for escaping where the field delimiter is part of the value.

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

            Indicates whether or not all output fields should be quoted.

          - **QuoteEscapeCharacter** *(string) --*

            Th single character used for escaping the quote character inside an already escaped value.

          - **RecordDelimiter** *(string) --*

            The value used to separate individual records.

          - **FieldDelimiter** *(string) --*

            The value used to separate individual fields in a record.

          - **QuoteCharacter** *(string) --*

            The value used for escaping where the field delimiter is part of the value.

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

            - **Grantee** *(dict) --*

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

            - *(dict) --*

              - **Key** *(string) --* **[REQUIRED]**

                Name of the tag.

              - **Value** *(string) --* **[REQUIRED]**

                Value of the tag.

        - **UserMetadata** *(list) --*

          A list of metadata to store with the restore results in S3.

          - *(dict) --*

            A metadata key-value pair to store with an object.

            - **Name** *(string) --*

            - **Value** *(string) --*

        - **StorageClass** *(string) --*

          The class of storage used to store the restore results.
    """


_ClientSelectObjectContentInputSerializationCSVTypeDef = TypedDict(
    "_ClientSelectObjectContentInputSerializationCSVTypeDef",
    {
        "FileHeaderInfo": str,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)


class ClientSelectObjectContentInputSerializationCSVTypeDef(
    _ClientSelectObjectContentInputSerializationCSVTypeDef
):
    """
    Type definition for `ClientSelectObjectContentInputSerialization` `CSV`

    Describes the serialization of a CSV-encoded object.

    - **FileHeaderInfo** *(string) --*

      Describes the first line of input. Valid values: None, Ignore, Use.

    - **Comments** *(string) --*

      The single character used to indicate a row should be ignored when present at the start of a
      row.

    - **QuoteEscapeCharacter** *(string) --*

      The single character used for escaping the quote character inside an already escaped value.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records.

    - **FieldDelimiter** *(string) --*

      The value used to separate individual fields in a record.

    - **QuoteCharacter** *(string) --*

      Value used for escaping where the field delimiter is part of the value.

    - **AllowQuotedRecordDelimiter** *(boolean) --*

      Specifies that CSV field values may contain quoted record delimiters and such records should
      be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.
    """


_ClientSelectObjectContentInputSerializationJSONTypeDef = TypedDict(
    "_ClientSelectObjectContentInputSerializationJSONTypeDef",
    {"Type": str},
    total=False,
)


class ClientSelectObjectContentInputSerializationJSONTypeDef(
    _ClientSelectObjectContentInputSerializationJSONTypeDef
):
    """
    Type definition for `ClientSelectObjectContentInputSerialization` `JSON`

    Specifies JSON as object's input serialization format.

    - **Type** *(string) --*

      The type of JSON. Valid values: Document, Lines.
    """


_ClientSelectObjectContentInputSerializationTypeDef = TypedDict(
    "_ClientSelectObjectContentInputSerializationTypeDef",
    {
        "CSV": ClientSelectObjectContentInputSerializationCSVTypeDef,
        "CompressionType": str,
        "JSON": ClientSelectObjectContentInputSerializationJSONTypeDef,
        "Parquet": Dict,
    },
    total=False,
)


class ClientSelectObjectContentInputSerializationTypeDef(
    _ClientSelectObjectContentInputSerializationTypeDef
):
    """
    Type definition for `ClientSelectObjectContent` `InputSerialization`

    Describes the format of the data in the object that is being queried.

    - **CSV** *(dict) --*

      Describes the serialization of a CSV-encoded object.

      - **FileHeaderInfo** *(string) --*

        Describes the first line of input. Valid values: None, Ignore, Use.

      - **Comments** *(string) --*

        The single character used to indicate a row should be ignored when present at the start of a
        row.

      - **QuoteEscapeCharacter** *(string) --*

        The single character used for escaping the quote character inside an already escaped value.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records.

      - **FieldDelimiter** *(string) --*

        The value used to separate individual fields in a record.

      - **QuoteCharacter** *(string) --*

        Value used for escaping where the field delimiter is part of the value.

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
    """


_ClientSelectObjectContentOutputSerializationCSVTypeDef = TypedDict(
    "_ClientSelectObjectContentOutputSerializationCSVTypeDef",
    {
        "QuoteFields": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientSelectObjectContentOutputSerializationCSVTypeDef(
    _ClientSelectObjectContentOutputSerializationCSVTypeDef
):
    """
    Type definition for `ClientSelectObjectContentOutputSerialization` `CSV`

    Describes the serialization of CSV-encoded Select results.

    - **QuoteFields** *(string) --*

      Indicates whether or not all output fields should be quoted.

    - **QuoteEscapeCharacter** *(string) --*

      Th single character used for escaping the quote character inside an already escaped value.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records.

    - **FieldDelimiter** *(string) --*

      The value used to separate individual fields in a record.

    - **QuoteCharacter** *(string) --*

      The value used for escaping where the field delimiter is part of the value.
    """


_ClientSelectObjectContentOutputSerializationJSONTypeDef = TypedDict(
    "_ClientSelectObjectContentOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)


class ClientSelectObjectContentOutputSerializationJSONTypeDef(
    _ClientSelectObjectContentOutputSerializationJSONTypeDef
):
    """
    Type definition for `ClientSelectObjectContentOutputSerialization` `JSON`

    Specifies JSON as request's output serialization format.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records in the output.
    """


_ClientSelectObjectContentOutputSerializationTypeDef = TypedDict(
    "_ClientSelectObjectContentOutputSerializationTypeDef",
    {
        "CSV": ClientSelectObjectContentOutputSerializationCSVTypeDef,
        "JSON": ClientSelectObjectContentOutputSerializationJSONTypeDef,
    },
    total=False,
)


class ClientSelectObjectContentOutputSerializationTypeDef(
    _ClientSelectObjectContentOutputSerializationTypeDef
):
    """
    Type definition for `ClientSelectObjectContent` `OutputSerialization`

    Describes the format of the data that you want Amazon S3 to return in response.

    - **CSV** *(dict) --*

      Describes the serialization of CSV-encoded Select results.

      - **QuoteFields** *(string) --*

        Indicates whether or not all output fields should be quoted.

      - **QuoteEscapeCharacter** *(string) --*

        Th single character used for escaping the quote character inside an already escaped value.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records.

      - **FieldDelimiter** *(string) --*

        The value used to separate individual fields in a record.

      - **QuoteCharacter** *(string) --*

        The value used for escaping where the field delimiter is part of the value.

    - **JSON** *(dict) --*

      Specifies JSON as request's output serialization format.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records in the output.
    """


_ClientSelectObjectContentRequestProgressTypeDef = TypedDict(
    "_ClientSelectObjectContentRequestProgressTypeDef", {"Enabled": bool}, total=False
)


class ClientSelectObjectContentRequestProgressTypeDef(
    _ClientSelectObjectContentRequestProgressTypeDef
):
    """
    Type definition for `ClientSelectObjectContent` `RequestProgress`

    Specifies if periodic request progress information should be enabled.

    - **Enabled** *(boolean) --*

      Specifies whether periodic QueryProgress frames should be sent. Valid values: TRUE, FALSE.
      Default value: FALSE.
    """


_ClientSelectObjectContentScanRangeTypeDef = TypedDict(
    "_ClientSelectObjectContentScanRangeTypeDef",
    {"Start": int, "End": int},
    total=False,
)


class ClientSelectObjectContentScanRangeTypeDef(
    _ClientSelectObjectContentScanRangeTypeDef
):
    """
    Type definition for `ClientSelectObjectContent` `ScanRange`

    Specifies the byte range of the object to get the records from. A record is processed when its
    first byte is contained by the range. This parameter is optional, but when specified, it must not
    be empty. See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.

    - **Start** *(integer) --*

      Specifies the start of the byte range. This parameter is optional. Valid values: non-negative
      integers. The default value is 0.

    - **End** *(integer) --*

      Specifies the end of the byte range. This parameter is optional. Valid values: non-negative
      integers. The default value is one less than the size of the object being queried.
    """


_ClientUploadPartCopyResponseCopyPartResultTypeDef = TypedDict(
    "_ClientUploadPartCopyResponseCopyPartResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)


class ClientUploadPartCopyResponseCopyPartResultTypeDef(
    _ClientUploadPartCopyResponseCopyPartResultTypeDef
):
    """
    Type definition for `ClientUploadPartCopyResponse` `CopyPartResult`

    - **ETag** *(string) --*

      Entity tag of the object.

    - **LastModified** *(datetime) --*

      Date and time at which the object was uploaded.
    """


_ClientUploadPartCopyResponseTypeDef = TypedDict(
    "_ClientUploadPartCopyResponseTypeDef",
    {
        "CopySourceVersionId": str,
        "CopyPartResult": ClientUploadPartCopyResponseCopyPartResultTypeDef,
        "ServerSideEncryption": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)


class ClientUploadPartCopyResponseTypeDef(_ClientUploadPartCopyResponseTypeDef):
    """
    Type definition for `ClientUploadPartCopy` `Response`

    - **CopySourceVersionId** *(string) --*

      The version of the source object that was copied, if you have enabled versioning on the
      source bucket.

    - **CopyPartResult** *(dict) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ClientUploadPartResponseTypeDef = TypedDict(
    "_ClientUploadPartResponseTypeDef",
    {
        "ServerSideEncryption": str,
        "ETag": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)


class ClientUploadPartResponseTypeDef(_ClientUploadPartResponseTypeDef):
    """
    Type definition for `ClientUploadPart` `Response`

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ListMultipartUploadsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMultipartUploadsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMultipartUploadsPaginatePaginationConfigTypeDef(
    _ListMultipartUploadsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListMultipartUploadsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef",
    {"Prefix": str},
    total=False,
)


class ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef(
    _ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef
):
    """
    Type definition for `ListMultipartUploadsPaginateResponse` `CommonPrefixes`

    - **Prefix** *(string) --*
    """


_ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)


class ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef(
    _ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef
):
    """
    Type definition for `ListMultipartUploadsPaginateResponseUploads` `Initiator`

    Identifies who initiated the multipart upload.

    - **ID** *(string) --*

      If the principal is an AWS account, it provides the Canonical User ID. If the principal
      is an IAM User, it provides a user ARN value.

    - **DisplayName** *(string) --*

      Name of the Principal.
    """


_ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef(
    _ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef
):
    """
    Type definition for `ListMultipartUploadsPaginateResponseUploads` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ListMultipartUploadsPaginateResponseUploadsTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseUploadsTypeDef",
    {
        "UploadId": str,
        "Key": str,
        "Initiated": datetime,
        "StorageClass": str,
        "Owner": ListMultipartUploadsPaginateResponseUploadsOwnerTypeDef,
        "Initiator": ListMultipartUploadsPaginateResponseUploadsInitiatorTypeDef,
    },
    total=False,
)


class ListMultipartUploadsPaginateResponseUploadsTypeDef(
    _ListMultipartUploadsPaginateResponseUploadsTypeDef
):
    """
    Type definition for `ListMultipartUploadsPaginateResponse` `Uploads`

    - **UploadId** *(string) --*

      Upload ID that identifies the multipart upload.

    - **Key** *(string) --*

      Key of the object for which the multipart upload was initiated.

    - **Initiated** *(datetime) --*

      Date and time at which the multipart upload was initiated.

    - **StorageClass** *(string) --*

      The class of storage used to store the object.

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*

    - **Initiator** *(dict) --*

      Identifies who initiated the multipart upload.

      - **ID** *(string) --*

        If the principal is an AWS account, it provides the Canonical User ID. If the principal
        is an IAM User, it provides a user ARN value.

      - **DisplayName** *(string) --*

        Name of the Principal.
    """


_ListMultipartUploadsPaginateResponseTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseTypeDef",
    {
        "Bucket": str,
        "KeyMarker": str,
        "UploadIdMarker": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxUploads": int,
        "IsTruncated": bool,
        "Uploads": List[ListMultipartUploadsPaginateResponseUploadsTypeDef],
        "CommonPrefixes": List[
            ListMultipartUploadsPaginateResponseCommonPrefixesTypeDef
        ],
        "EncodingType": str,
        "NextToken": str,
    },
    total=False,
)


class ListMultipartUploadsPaginateResponseTypeDef(
    _ListMultipartUploadsPaginateResponseTypeDef
):
    """
    Type definition for `ListMultipartUploadsPaginate` `Response`

    - **Bucket** *(string) --*

      Name of the bucket to which the multipart upload was initiated.

    - **KeyMarker** *(string) --*

      The key at or after which the listing began.

    - **UploadIdMarker** *(string) --*

      Upload ID after which listing began.

    - **Prefix** *(string) --*

      When a prefix is provided in the request, this field contains the specified prefix. The
      result contains only keys starting with the specified prefix.

    - **Delimiter** *(string) --*

    - **MaxUploads** *(integer) --*

      Maximum number of multipart uploads that could have been included in the response.

    - **IsTruncated** *(boolean) --*

      Indicates whether the returned list of multipart uploads is truncated. A value of true
      indicates that the list was truncated. The list can be truncated if the number of multipart
      uploads exceeds the limit allowed or specified by max uploads.

    - **Uploads** *(list) --*

      - *(dict) --*

        - **UploadId** *(string) --*

          Upload ID that identifies the multipart upload.

        - **Key** *(string) --*

          Key of the object for which the multipart upload was initiated.

        - **Initiated** *(datetime) --*

          Date and time at which the multipart upload was initiated.

        - **StorageClass** *(string) --*

          The class of storage used to store the object.

        - **Owner** *(dict) --*

          - **DisplayName** *(string) --*

          - **ID** *(string) --*

        - **Initiator** *(dict) --*

          Identifies who initiated the multipart upload.

          - **ID** *(string) --*

            If the principal is an AWS account, it provides the Canonical User ID. If the principal
            is an IAM User, it provides a user ARN value.

          - **DisplayName** *(string) --*

            Name of the Principal.

    - **CommonPrefixes** *(list) --*

      - *(dict) --*

        - **Prefix** *(string) --*

    - **EncodingType** *(string) --*

      Encoding type used by Amazon S3 to encode object keys in the response.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListObjectVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectVersionsPaginatePaginationConfigTypeDef(
    _ListObjectVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListObjectVersionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListObjectVersionsPaginateResponseCommonPrefixesTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseCommonPrefixesTypeDef",
    {"Prefix": str},
    total=False,
)


class ListObjectVersionsPaginateResponseCommonPrefixesTypeDef(
    _ListObjectVersionsPaginateResponseCommonPrefixesTypeDef
):
    """
    Type definition for `ListObjectVersionsPaginateResponse` `CommonPrefixes`

    - **Prefix** *(string) --*
    """


_ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef(
    _ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef
):
    """
    Type definition for `ListObjectVersionsPaginateResponseDeleteMarkers` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ListObjectVersionsPaginateResponseDeleteMarkersTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseDeleteMarkersTypeDef",
    {
        "Owner": ListObjectVersionsPaginateResponseDeleteMarkersOwnerTypeDef,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)


class ListObjectVersionsPaginateResponseDeleteMarkersTypeDef(
    _ListObjectVersionsPaginateResponseDeleteMarkersTypeDef
):
    """
    Type definition for `ListObjectVersionsPaginateResponse` `DeleteMarkers`

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*

    - **Key** *(string) --*

      The object key.

    - **VersionId** *(string) --*

      Version ID of an object.

    - **IsLatest** *(boolean) --*

      Specifies whether the object is (true) or is not (false) the latest version of an object.

    - **LastModified** *(datetime) --*

      Date and time the object was last modified.
    """


_ListObjectVersionsPaginateResponseVersionsOwnerTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseVersionsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ListObjectVersionsPaginateResponseVersionsOwnerTypeDef(
    _ListObjectVersionsPaginateResponseVersionsOwnerTypeDef
):
    """
    Type definition for `ListObjectVersionsPaginateResponseVersions` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ListObjectVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseVersionsTypeDef",
    {
        "ETag": str,
        "Size": int,
        "StorageClass": str,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
        "Owner": ListObjectVersionsPaginateResponseVersionsOwnerTypeDef,
    },
    total=False,
)


class ListObjectVersionsPaginateResponseVersionsTypeDef(
    _ListObjectVersionsPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListObjectVersionsPaginateResponse` `Versions`

    - **ETag** *(string) --*

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

      - **DisplayName** *(string) --*

      - **ID** *(string) --*
    """


_ListObjectVersionsPaginateResponseTypeDef = TypedDict(
    "_ListObjectVersionsPaginateResponseTypeDef",
    {
        "IsTruncated": bool,
        "KeyMarker": str,
        "VersionIdMarker": str,
        "Versions": List[ListObjectVersionsPaginateResponseVersionsTypeDef],
        "DeleteMarkers": List[ListObjectVersionsPaginateResponseDeleteMarkersTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ListObjectVersionsPaginateResponseCommonPrefixesTypeDef],
        "EncodingType": str,
        "NextToken": str,
    },
    total=False,
)


class ListObjectVersionsPaginateResponseTypeDef(
    _ListObjectVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListObjectVersionsPaginate` `Response`

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the
      search criteria. If your results were truncated, you can make a follow-up paginated request
      using the NextKeyMarker and NextVersionIdMarker response parameters as a starting place in
      another request to return the rest of the results.

    - **KeyMarker** *(string) --*

      Marks the last Key returned in a truncated response.

    - **VersionIdMarker** *(string) --*

    - **Versions** *(list) --*

      - *(dict) --*

        - **ETag** *(string) --*

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

          - **DisplayName** *(string) --*

          - **ID** *(string) --*

    - **DeleteMarkers** *(list) --*

      - *(dict) --*

        - **Owner** *(dict) --*

          - **DisplayName** *(string) --*

          - **ID** *(string) --*

        - **Key** *(string) --*

          The object key.

        - **VersionId** *(string) --*

          Version ID of an object.

        - **IsLatest** *(boolean) --*

          Specifies whether the object is (true) or is not (false) the latest version of an object.

        - **LastModified** *(datetime) --*

          Date and time the object was last modified.

    - **Name** *(string) --*

    - **Prefix** *(string) --*

    - **Delimiter** *(string) --*

    - **MaxKeys** *(integer) --*

    - **CommonPrefixes** *(list) --*

      - *(dict) --*

        - **Prefix** *(string) --*

    - **EncodingType** *(string) --*

      Encoding type used by Amazon S3 to encode object keys in the response.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListObjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectsPaginatePaginationConfigTypeDef(
    _ListObjectsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListObjectsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListObjectsPaginateResponseCommonPrefixesTypeDef = TypedDict(
    "_ListObjectsPaginateResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ListObjectsPaginateResponseCommonPrefixesTypeDef(
    _ListObjectsPaginateResponseCommonPrefixesTypeDef
):
    """
    Type definition for `ListObjectsPaginateResponse` `CommonPrefixes`

    - **Prefix** *(string) --*
    """


_ListObjectsPaginateResponseContentsOwnerTypeDef = TypedDict(
    "_ListObjectsPaginateResponseContentsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ListObjectsPaginateResponseContentsOwnerTypeDef(
    _ListObjectsPaginateResponseContentsOwnerTypeDef
):
    """
    Type definition for `ListObjectsPaginateResponseContents` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ListObjectsPaginateResponseContentsTypeDef = TypedDict(
    "_ListObjectsPaginateResponseContentsTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": str,
        "Owner": ListObjectsPaginateResponseContentsOwnerTypeDef,
    },
    total=False,
)


class ListObjectsPaginateResponseContentsTypeDef(
    _ListObjectsPaginateResponseContentsTypeDef
):
    """
    Type definition for `ListObjectsPaginateResponse` `Contents`

    - **Key** *(string) --*

    - **LastModified** *(datetime) --*

    - **ETag** *(string) --*

    - **Size** *(integer) --*

    - **StorageClass** *(string) --*

      The class of storage used to store the object.

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*
    """


_ListObjectsPaginateResponseTypeDef = TypedDict(
    "_ListObjectsPaginateResponseTypeDef",
    {
        "IsTruncated": bool,
        "Marker": str,
        "NextMarker": str,
        "Contents": List[ListObjectsPaginateResponseContentsTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ListObjectsPaginateResponseCommonPrefixesTypeDef],
        "EncodingType": str,
        "NextToken": str,
    },
    total=False,
)


class ListObjectsPaginateResponseTypeDef(_ListObjectsPaginateResponseTypeDef):
    """
    Type definition for `ListObjectsPaginate` `Response`

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the
      search criteria.

    - **Marker** *(string) --*

    - **NextMarker** *(string) --*

      When response is truncated (the IsTruncated element value in the response is true), you can
      use the key name in this field as marker in the subsequent request to get next set of
      objects. Amazon S3 lists objects in alphabetical order Note: This element is returned only if
      you have delimiter request parameter specified. If response does not include the NextMaker
      and it is truncated, you can use the value of the last Key in the response as the marker in
      the subsequent request to get the next set of object keys.

    - **Contents** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **LastModified** *(datetime) --*

        - **ETag** *(string) --*

        - **Size** *(integer) --*

        - **StorageClass** *(string) --*

          The class of storage used to store the object.

        - **Owner** *(dict) --*

          - **DisplayName** *(string) --*

          - **ID** *(string) --*

    - **Name** *(string) --*

    - **Prefix** *(string) --*

    - **Delimiter** *(string) --*

    - **MaxKeys** *(integer) --*

    - **CommonPrefixes** *(list) --*

      - *(dict) --*

        - **Prefix** *(string) --*

    - **EncodingType** *(string) --*

      Encoding type used by Amazon S3 to encode object keys in the response.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListObjectsV2PaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectsV2PaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectsV2PaginatePaginationConfigTypeDef(
    _ListObjectsV2PaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListObjectsV2Paginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListObjectsV2PaginateResponseCommonPrefixesTypeDef = TypedDict(
    "_ListObjectsV2PaginateResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)


class ListObjectsV2PaginateResponseCommonPrefixesTypeDef(
    _ListObjectsV2PaginateResponseCommonPrefixesTypeDef
):
    """
    Type definition for `ListObjectsV2PaginateResponse` `CommonPrefixes`

    - **Prefix** *(string) --*
    """


_ListObjectsV2PaginateResponseContentsOwnerTypeDef = TypedDict(
    "_ListObjectsV2PaginateResponseContentsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ListObjectsV2PaginateResponseContentsOwnerTypeDef(
    _ListObjectsV2PaginateResponseContentsOwnerTypeDef
):
    """
    Type definition for `ListObjectsV2PaginateResponseContents` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ListObjectsV2PaginateResponseContentsTypeDef = TypedDict(
    "_ListObjectsV2PaginateResponseContentsTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": str,
        "Owner": ListObjectsV2PaginateResponseContentsOwnerTypeDef,
    },
    total=False,
)


class ListObjectsV2PaginateResponseContentsTypeDef(
    _ListObjectsV2PaginateResponseContentsTypeDef
):
    """
    Type definition for `ListObjectsV2PaginateResponse` `Contents`

    - **Key** *(string) --*

    - **LastModified** *(datetime) --*

    - **ETag** *(string) --*

    - **Size** *(integer) --*

    - **StorageClass** *(string) --*

      The class of storage used to store the object.

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*
    """


_ListObjectsV2PaginateResponseTypeDef = TypedDict(
    "_ListObjectsV2PaginateResponseTypeDef",
    {
        "IsTruncated": bool,
        "Contents": List[ListObjectsV2PaginateResponseContentsTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ListObjectsV2PaginateResponseCommonPrefixesTypeDef],
        "EncodingType": str,
        "KeyCount": int,
        "ContinuationToken": str,
        "StartAfter": str,
        "NextToken": str,
    },
    total=False,
)


class ListObjectsV2PaginateResponseTypeDef(_ListObjectsV2PaginateResponseTypeDef):
    """
    Type definition for `ListObjectsV2Paginate` `Response`

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the
      search criteria.

    - **Contents** *(list) --*

      Metadata about each object returned.

      - *(dict) --*

        - **Key** *(string) --*

        - **LastModified** *(datetime) --*

        - **ETag** *(string) --*

        - **Size** *(integer) --*

        - **StorageClass** *(string) --*

          The class of storage used to store the object.

        - **Owner** *(dict) --*

          - **DisplayName** *(string) --*

          - **ID** *(string) --*

    - **Name** *(string) --*

      Name of the bucket to list.

    - **Prefix** *(string) --*

      Limits the response to keys that begin with the specified prefix.

    - **Delimiter** *(string) --*

      A delimiter is a character you use to group keys.

    - **MaxKeys** *(integer) --*

      Sets the maximum number of keys returned in the response. The response might contain fewer
      keys but will never contain more.

    - **CommonPrefixes** *(list) --*

      CommonPrefixes contains all (if there are any) keys between Prefix and the next occurrence of
      the string specified by delimiter

      - *(dict) --*

        - **Prefix** *(string) --*

    - **EncodingType** *(string) --*

      Encoding type used by Amazon S3 to encode object keys in the response.

    - **KeyCount** *(integer) --*

      KeyCount is the number of keys returned with this request. KeyCount will always be less than
      equals to MaxKeys field. Say you ask for 50 keys, your result will include less than equals
      50 keys

    - **ContinuationToken** *(string) --*

      ContinuationToken indicates Amazon S3 that the list is being continued on this bucket with a
      token. ContinuationToken is obfuscated and is not a real key

    - **StartAfter** *(string) --*

      StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after
      this specified key. StartAfter can be any key in the bucket

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPartsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPartsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPartsPaginatePaginationConfigTypeDef(
    _ListPartsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPartsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListPartsPaginateResponseInitiatorTypeDef = TypedDict(
    "_ListPartsPaginateResponseInitiatorTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)


class ListPartsPaginateResponseInitiatorTypeDef(
    _ListPartsPaginateResponseInitiatorTypeDef
):
    """
    Type definition for `ListPartsPaginateResponse` `Initiator`

    Identifies who initiated the multipart upload.

    - **ID** *(string) --*

      If the principal is an AWS account, it provides the Canonical User ID. If the principal is
      an IAM User, it provides a user ARN value.

    - **DisplayName** *(string) --*

      Name of the Principal.
    """


_ListPartsPaginateResponseOwnerTypeDef = TypedDict(
    "_ListPartsPaginateResponseOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ListPartsPaginateResponseOwnerTypeDef(_ListPartsPaginateResponseOwnerTypeDef):
    """
    Type definition for `ListPartsPaginateResponse` `Owner`

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ListPartsPaginateResponsePartsTypeDef = TypedDict(
    "_ListPartsPaginateResponsePartsTypeDef",
    {"PartNumber": int, "LastModified": datetime, "ETag": str, "Size": int},
    total=False,
)


class ListPartsPaginateResponsePartsTypeDef(_ListPartsPaginateResponsePartsTypeDef):
    """
    Type definition for `ListPartsPaginateResponse` `Parts`

    - **PartNumber** *(integer) --*

      Part number identifying the part. This is a positive integer between 1 and 10,000.

    - **LastModified** *(datetime) --*

      Date and time at which the part was uploaded.

    - **ETag** *(string) --*

      Entity tag returned when the part was uploaded.

    - **Size** *(integer) --*

      Size in bytes of the uploaded part data.
    """


_ListPartsPaginateResponseTypeDef = TypedDict(
    "_ListPartsPaginateResponseTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "PartNumberMarker": int,
        "MaxParts": int,
        "IsTruncated": bool,
        "Parts": List[ListPartsPaginateResponsePartsTypeDef],
        "Initiator": ListPartsPaginateResponseInitiatorTypeDef,
        "Owner": ListPartsPaginateResponseOwnerTypeDef,
        "StorageClass": str,
        "RequestCharged": str,
        "NextToken": str,
    },
    total=False,
)


class ListPartsPaginateResponseTypeDef(_ListPartsPaginateResponseTypeDef):
    """
    Type definition for `ListPartsPaginate` `Response`

    - **AbortDate** *(datetime) --*

      Date when multipart upload will become eligible for abort operation by lifecycle.

    - **AbortRuleId** *(string) --*

      Id of the lifecycle rule that makes a multipart upload eligible for abort operation.

    - **Bucket** *(string) --*

      Name of the bucket to which the multipart upload was initiated.

    - **Key** *(string) --*

      Object key for which the multipart upload was initiated.

    - **UploadId** *(string) --*

      Upload ID identifying the multipart upload whose parts are being listed.

    - **PartNumberMarker** *(integer) --*

      Part number after which listing begins.

    - **MaxParts** *(integer) --*

      Maximum number of parts that were allowed in the response.

    - **IsTruncated** *(boolean) --*

      Indicates whether the returned list of parts is truncated.

    - **Parts** *(list) --*

      - *(dict) --*

        - **PartNumber** *(integer) --*

          Part number identifying the part. This is a positive integer between 1 and 10,000.

        - **LastModified** *(datetime) --*

          Date and time at which the part was uploaded.

        - **ETag** *(string) --*

          Entity tag returned when the part was uploaded.

        - **Size** *(integer) --*

          Size in bytes of the uploaded part data.

    - **Initiator** *(dict) --*

      Identifies who initiated the multipart upload.

      - **ID** *(string) --*

        If the principal is an AWS account, it provides the Canonical User ID. If the principal is
        an IAM User, it provides a user ARN value.

      - **DisplayName** *(string) --*

        Name of the Principal.

    - **Owner** *(dict) --*

      - **DisplayName** *(string) --*

      - **ID** *(string) --*

    - **StorageClass** *(string) --*

      The class of storage used to store the object.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_MultipartUploadAbortResponseTypeDef = TypedDict(
    "_MultipartUploadAbortResponseTypeDef", {"RequestCharged": str}, total=False
)


class MultipartUploadAbortResponseTypeDef(_MultipartUploadAbortResponseTypeDef):
    """
    Type definition for `MultipartUploadAbort` `Response`

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_MultipartUploadCompleteMultipartUploadPartsTypeDef = TypedDict(
    "_MultipartUploadCompleteMultipartUploadPartsTypeDef",
    {"ETag": str, "PartNumber": int},
    total=False,
)


class MultipartUploadCompleteMultipartUploadPartsTypeDef(
    _MultipartUploadCompleteMultipartUploadPartsTypeDef
):
    """
    Type definition for `MultipartUploadCompleteMultipartUpload` `Parts`

    - **ETag** *(string) --*

      Entity tag returned when the part was uploaded.

    - **PartNumber** *(integer) --*

      Part number that identifies the part. This is a positive integer between 1 and 10,000.
    """


_MultipartUploadCompleteMultipartUploadTypeDef = TypedDict(
    "_MultipartUploadCompleteMultipartUploadTypeDef",
    {"Parts": List[MultipartUploadCompleteMultipartUploadPartsTypeDef]},
    total=False,
)


class MultipartUploadCompleteMultipartUploadTypeDef(
    _MultipartUploadCompleteMultipartUploadTypeDef
):
    """
    Type definition for `MultipartUploadComplete` `MultipartUpload`

    - **Parts** *(list) --*

      - *(dict) --*

        - **ETag** *(string) --*

          Entity tag returned when the part was uploaded.

        - **PartNumber** *(integer) --*

          Part number that identifies the part. This is a positive integer between 1 and 10,000.
    """


_MultipartUploadPartCopyFromResponseCopyPartResultTypeDef = TypedDict(
    "_MultipartUploadPartCopyFromResponseCopyPartResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)


class MultipartUploadPartCopyFromResponseCopyPartResultTypeDef(
    _MultipartUploadPartCopyFromResponseCopyPartResultTypeDef
):
    """
    Type definition for `MultipartUploadPartCopyFromResponse` `CopyPartResult`

    - **ETag** *(string) --*

      Entity tag of the object.

    - **LastModified** *(datetime) --*

      Date and time at which the object was uploaded.
    """


_MultipartUploadPartCopyFromResponseTypeDef = TypedDict(
    "_MultipartUploadPartCopyFromResponseTypeDef",
    {
        "CopySourceVersionId": str,
        "CopyPartResult": MultipartUploadPartCopyFromResponseCopyPartResultTypeDef,
        "ServerSideEncryption": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)


class MultipartUploadPartCopyFromResponseTypeDef(
    _MultipartUploadPartCopyFromResponseTypeDef
):
    """
    Type definition for `MultipartUploadPartCopyFrom` `Response`

    - **CopySourceVersionId** *(string) --*

      The version of the source object that was copied, if you have enabled versioning on the
      source bucket.

    - **CopyPartResult** *(dict) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_MultipartUploadPartUploadResponseTypeDef = TypedDict(
    "_MultipartUploadPartUploadResponseTypeDef",
    {
        "ServerSideEncryption": str,
        "ETag": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)


class MultipartUploadPartUploadResponseTypeDef(
    _MultipartUploadPartUploadResponseTypeDef
):
    """
    Type definition for `MultipartUploadPartUpload` `Response`

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_RequiredObjectAclPutAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_RequiredObjectAclPutAccessControlPolicyGrantsGranteeTypeDef", {"Type": str}
)
_OptionalObjectAclPutAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "_OptionalObjectAclPutAccessControlPolicyGrantsGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "URI": str},
    total=False,
)


class ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef(
    _RequiredObjectAclPutAccessControlPolicyGrantsGranteeTypeDef,
    _OptionalObjectAclPutAccessControlPolicyGrantsGranteeTypeDef,
):
    """
    Type definition for `ObjectAclPutAccessControlPolicyGrants` `Grantee`

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
    """


_ObjectAclPutAccessControlPolicyGrantsTypeDef = TypedDict(
    "_ObjectAclPutAccessControlPolicyGrantsTypeDef",
    {"Grantee": ObjectAclPutAccessControlPolicyGrantsGranteeTypeDef, "Permission": str},
    total=False,
)


class ObjectAclPutAccessControlPolicyGrantsTypeDef(
    _ObjectAclPutAccessControlPolicyGrantsTypeDef
):
    """
    Type definition for `ObjectAclPutAccessControlPolicy` `Grants`

    - **Grantee** *(dict) --*

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
    """


_ObjectAclPutAccessControlPolicyOwnerTypeDef = TypedDict(
    "_ObjectAclPutAccessControlPolicyOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)


class ObjectAclPutAccessControlPolicyOwnerTypeDef(
    _ObjectAclPutAccessControlPolicyOwnerTypeDef
):
    """
    Type definition for `ObjectAclPutAccessControlPolicy` `Owner`

    Container for the bucket owner's display name and ID.

    - **DisplayName** *(string) --*

    - **ID** *(string) --*
    """


_ObjectAclPutAccessControlPolicyTypeDef = TypedDict(
    "_ObjectAclPutAccessControlPolicyTypeDef",
    {
        "Grants": List[ObjectAclPutAccessControlPolicyGrantsTypeDef],
        "Owner": ObjectAclPutAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)


class ObjectAclPutAccessControlPolicyTypeDef(_ObjectAclPutAccessControlPolicyTypeDef):
    """
    Type definition for `ObjectAclPut` `AccessControlPolicy`

    Contains the elements that set the ACL permissions for an object per grantee.

    - **Grants** *(list) --*

      A list of grants.

      - *(dict) --*

        - **Grantee** *(dict) --*

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

      - **ID** *(string) --*
    """


_ObjectAclPutResponseTypeDef = TypedDict(
    "_ObjectAclPutResponseTypeDef", {"RequestCharged": str}, total=False
)


class ObjectAclPutResponseTypeDef(_ObjectAclPutResponseTypeDef):
    """
    Type definition for `ObjectAclPut` `Response`

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ObjectCopyFromResponseCopyObjectResultTypeDef = TypedDict(
    "_ObjectCopyFromResponseCopyObjectResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)


class ObjectCopyFromResponseCopyObjectResultTypeDef(
    _ObjectCopyFromResponseCopyObjectResultTypeDef
):
    """
    Type definition for `ObjectCopyFromResponse` `CopyObjectResult`

    - **ETag** *(string) --*

    - **LastModified** *(datetime) --*
    """


_ObjectCopyFromResponseTypeDef = TypedDict(
    "_ObjectCopyFromResponseTypeDef",
    {
        "CopyObjectResult": ObjectCopyFromResponseCopyObjectResultTypeDef,
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)


class ObjectCopyFromResponseTypeDef(_ObjectCopyFromResponseTypeDef):
    """
    Type definition for `ObjectCopyFrom` `Response`

    - **CopyObjectResult** *(dict) --*

      - **ETag** *(string) --*

      - **LastModified** *(datetime) --*

    - **Expiration** *(string) --*

      If the object expiration is configured, the response includes this header.

    - **CopySourceVersionId** *(string) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **SSEKMSEncryptionContext** *(string) --*

      If present, specifies the AWS KMS Encryption Context to use for object encryption. The value
      of this header is a base64-encoded UTF-8 string holding JSON with the encryption context
      key-value pairs.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ObjectDeleteResponseTypeDef = TypedDict(
    "_ObjectDeleteResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)


class ObjectDeleteResponseTypeDef(_ObjectDeleteResponseTypeDef):
    """
    Type definition for `ObjectDelete` `Response`

    - **DeleteMarker** *(boolean) --*

      Specifies whether the versioned object that was permanently deleted was (true) or was not
      (false) a delete marker.

    - **VersionId** *(string) --*

      Returns the version ID of the delete marker created as a result of the DELETE operation.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ObjectGetResponseTypeDef = TypedDict(
    "_ObjectGetResponseTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": str,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": str,
        "RequestCharged": str,
        "ReplicationStatus": str,
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": str,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": str,
    },
    total=False,
)


class ObjectGetResponseTypeDef(_ObjectGetResponseTypeDef):
    """
    Type definition for `ObjectGet` `Response`

    - **Body** (:class:`.StreamingBody`) --

      Object data.

    - **DeleteMarker** *(boolean) --*

      Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If
      false, this response header does not appear in the response.

    - **AcceptRanges** *(string) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **StorageClass** *(string) --*

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **ReplicationStatus** *(string) --*

    - **PartsCount** *(integer) --*

      The count of parts this object has.

    - **TagCount** *(integer) --*

      The number of tags, if any, on the object.

    - **ObjectLockMode** *(string) --*

      The object lock mode currently in place for this object.

    - **ObjectLockRetainUntilDate** *(datetime) --*

      The date and time when this object's object lock will expire.

    - **ObjectLockLegalHoldStatus** *(string) --*

      Indicates whether this object has an active legal hold. This field is only returned if you
      have permission to view an object's legal hold status.
    """


_ObjectPutResponseTypeDef = TypedDict(
    "_ObjectPutResponseTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": str,
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)


class ObjectPutResponseTypeDef(_ObjectPutResponseTypeDef):
    """
    Type definition for `ObjectPut` `Response`

    - **Expiration** *(string) --*

      If the object expiration is configured, this will contain the expiration date (expiry-date)
      and rule ID (rule-id). The value of rule-id is URL encoded.

    - **ETag** *(string) --*

      Entity tag for the uploaded object.

    - **ServerSideEncryption** *(string) --*

      The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256,
      aws:kms).

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **SSEKMSEncryptionContext** *(string) --*

      If present, specifies the AWS KMS Encryption Context to use for object encryption. The value
      of this header is a base64-encoded UTF-8 string holding JSON with the encryption context
      key-value pairs.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ObjectRestoreObjectResponseTypeDef = TypedDict(
    "_ObjectRestoreObjectResponseTypeDef",
    {"RequestCharged": str, "RestoreOutputPath": str},
    total=False,
)


class ObjectRestoreObjectResponseTypeDef(_ObjectRestoreObjectResponseTypeDef):
    """
    Type definition for `ObjectRestoreObject` `Response`

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **RestoreOutputPath** *(string) --*

      Indicates the path in the provided S3 output location where Select results will be restored
      to.
    """


_ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef", {"Tier": str}
)


class ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef(
    _ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequest` `GlacierJobParameters`

    Glacier related parameters pertaining to this job. Do not use with restores that specify
    OutputLocation.

    - **Tier** *(string) --* **[REQUIRED]**

      Glacier retrieval tier at which the restore will be processed.
    """


_RequiredObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_RequiredObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {"Type": str},
)
_OptionalObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_OptionalObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "URI": str},
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef(
    _RequiredObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
    _OptionalObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlList` `Grantee`

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
    """


_ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestOutputLocationS3` `AccessControlList`

    - **Grantee** *(dict) --*

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
    """


_RequiredObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "_RequiredObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": str},
)
_OptionalObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "_OptionalObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef(
    _RequiredObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
    _OptionalObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestOutputLocationS3` `Encryption`

    - **EncryptionType** *(string) --* **[REQUIRED]**

      The server-side encryption algorithm used when storing job results in Amazon S3 (e.g.,
      AES256, aws:kms).

    - **KMSKeyId** *(string) --*

      If the encryption type is aws:kms, this optional value specifies the AWS KMS key ID to
      use for encryption of job results.

    - **KMSContext** *(string) --*

      If the encryption type is aws:kms, this optional value can be used to specify the
      encryption context for the restore results.
    """


_ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    {"Key": str, "Value": str},
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestOutputLocationS3Tagging` `TagSet`

    - **Key** *(string) --* **[REQUIRED]**

      Name of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag.
    """


_ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    {
        "TagSet": List[
            ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef
        ]
    },
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestOutputLocationS3` `Tagging`

    The tag-set that is applied to the restore results.

    - **TagSet** *(list) --* **[REQUIRED]**

      - *(dict) --*

        - **Key** *(string) --* **[REQUIRED]**

          Name of the tag.

        - **Value** *(string) --* **[REQUIRED]**

          Value of the tag.
    """


_ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestOutputLocationS3` `UserMetadata`

    A metadata key-value pair to store with an object.

    - **Name** *(string) --*

    - **Value** *(string) --*
    """


_RequiredObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "_RequiredObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    {"BucketName": str, "Prefix": str},
)
_OptionalObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "_OptionalObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    {
        "Encryption": ObjectRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
        "CannedACL": str,
        "AccessControlList": List[
            ObjectRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": ObjectRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef,
        "UserMetadata": List[
            ObjectRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef
        ],
        "StorageClass": str,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef(
    _RequiredObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef,
    _OptionalObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef,
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestOutputLocation` `S3`

    Describes an S3 location that will receive the results of the restore request.

    - **BucketName** *(string) --* **[REQUIRED]**

      The name of the bucket where the restore results will be placed.

    - **Prefix** *(string) --* **[REQUIRED]**

      The prefix that is prepended to the restore results for this request.

    - **Encryption** *(dict) --*

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

        - **Grantee** *(dict) --*

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

        - *(dict) --*

          - **Key** *(string) --* **[REQUIRED]**

            Name of the tag.

          - **Value** *(string) --* **[REQUIRED]**

            Value of the tag.

    - **UserMetadata** *(list) --*

      A list of metadata to store with the restore results in S3.

      - *(dict) --*

        A metadata key-value pair to store with an object.

        - **Name** *(string) --*

        - **Value** *(string) --*

    - **StorageClass** *(string) --*

      The class of storage used to store the restore results.
    """


_ObjectRestoreObjectRestoreRequestOutputLocationTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestOutputLocationTypeDef",
    {"S3": ObjectRestoreObjectRestoreRequestOutputLocationS3TypeDef},
    total=False,
)


class ObjectRestoreObjectRestoreRequestOutputLocationTypeDef(
    _ObjectRestoreObjectRestoreRequestOutputLocationTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequest` `OutputLocation`

    Describes the location where the restore job's output is stored.

    - **S3** *(dict) --*

      Describes an S3 location that will receive the results of the restore request.

      - **BucketName** *(string) --* **[REQUIRED]**

        The name of the bucket where the restore results will be placed.

      - **Prefix** *(string) --* **[REQUIRED]**

        The prefix that is prepended to the restore results for this request.

      - **Encryption** *(dict) --*

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

          - **Grantee** *(dict) --*

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

          - *(dict) --*

            - **Key** *(string) --* **[REQUIRED]**

              Name of the tag.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag.

      - **UserMetadata** *(list) --*

        A list of metadata to store with the restore results in S3.

        - *(dict) --*

          A metadata key-value pair to store with an object.

          - **Name** *(string) --*

          - **Value** *(string) --*

      - **StorageClass** *(string) --*

        The class of storage used to store the restore results.
    """


_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    {
        "FileHeaderInfo": str,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestSelectParametersInputSerialization` `CSV`

    Describes the serialization of a CSV-encoded object.

    - **FileHeaderInfo** *(string) --*

      Describes the first line of input. Valid values: None, Ignore, Use.

    - **Comments** *(string) --*

      The single character used to indicate a row should be ignored when present at the start
      of a row.

    - **QuoteEscapeCharacter** *(string) --*

      The single character used for escaping the quote character inside an already escaped
      value.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records.

    - **FieldDelimiter** *(string) --*

      The value used to separate individual fields in a record.

    - **QuoteCharacter** *(string) --*

      Value used for escaping where the field delimiter is part of the value.

    - **AllowQuotedRecordDelimiter** *(boolean) --*

      Specifies that CSV field values may contain quoted record delimiters and such records
      should be allowed. Default value is FALSE. Setting this value to TRUE may lower
      performance.
    """


_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    {"Type": str},
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestSelectParametersInputSerialization` `JSON`

    Specifies JSON as object's input serialization format.

    - **Type** *(string) --*

      The type of JSON. Valid values: Document, Lines.
    """


_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    {
        "CSV": ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef,
        "CompressionType": str,
        "JSON": ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef,
        "Parquet": Dict,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestSelectParameters` `InputSerialization`

    Describes the serialization format of the object.

    - **CSV** *(dict) --*

      Describes the serialization of a CSV-encoded object.

      - **FileHeaderInfo** *(string) --*

        Describes the first line of input. Valid values: None, Ignore, Use.

      - **Comments** *(string) --*

        The single character used to indicate a row should be ignored when present at the start
        of a row.

      - **QuoteEscapeCharacter** *(string) --*

        The single character used for escaping the quote character inside an already escaped
        value.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records.

      - **FieldDelimiter** *(string) --*

        The value used to separate individual fields in a record.

      - **QuoteCharacter** *(string) --*

        Value used for escaping where the field delimiter is part of the value.

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
    """


_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    {
        "QuoteFields": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestSelectParametersOutputSerialization` `CSV`

    Describes the serialization of CSV-encoded Select results.

    - **QuoteFields** *(string) --*

      Indicates whether or not all output fields should be quoted.

    - **QuoteEscapeCharacter** *(string) --*

      Th single character used for escaping the quote character inside an already escaped value.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records.

    - **FieldDelimiter** *(string) --*

      The value used to separate individual fields in a record.

    - **QuoteCharacter** *(string) --*

      The value used for escaping where the field delimiter is part of the value.
    """


_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestSelectParametersOutputSerialization` `JSON`

    Specifies JSON as request's output serialization format.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records in the output.
    """


_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    {
        "CSV": ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef,
        "JSON": ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequestSelectParameters` `OutputSerialization`

    Describes how the results of the Select job are serialized.

    - **CSV** *(dict) --*

      Describes the serialization of CSV-encoded Select results.

      - **QuoteFields** *(string) --*

        Indicates whether or not all output fields should be quoted.

      - **QuoteEscapeCharacter** *(string) --*

        Th single character used for escaping the quote character inside an already escaped value.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records.

      - **FieldDelimiter** *(string) --*

        The value used to separate individual fields in a record.

      - **QuoteCharacter** *(string) --*

        The value used for escaping where the field delimiter is part of the value.

    - **JSON** *(dict) --*

      Specifies JSON as request's output serialization format.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records in the output.
    """


_ObjectRestoreObjectRestoreRequestSelectParametersTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestSelectParametersTypeDef",
    {
        "InputSerialization": ObjectRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ObjectRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef,
    },
)


class ObjectRestoreObjectRestoreRequestSelectParametersTypeDef(
    _ObjectRestoreObjectRestoreRequestSelectParametersTypeDef
):
    """
    Type definition for `ObjectRestoreObjectRestoreRequest` `SelectParameters`

    Describes the parameters for Select job types.

    - **InputSerialization** *(dict) --* **[REQUIRED]**

      Describes the serialization format of the object.

      - **CSV** *(dict) --*

        Describes the serialization of a CSV-encoded object.

        - **FileHeaderInfo** *(string) --*

          Describes the first line of input. Valid values: None, Ignore, Use.

        - **Comments** *(string) --*

          The single character used to indicate a row should be ignored when present at the start
          of a row.

        - **QuoteEscapeCharacter** *(string) --*

          The single character used for escaping the quote character inside an already escaped
          value.

        - **RecordDelimiter** *(string) --*

          The value used to separate individual records.

        - **FieldDelimiter** *(string) --*

          The value used to separate individual fields in a record.

        - **QuoteCharacter** *(string) --*

          Value used for escaping where the field delimiter is part of the value.

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

          Indicates whether or not all output fields should be quoted.

        - **QuoteEscapeCharacter** *(string) --*

          Th single character used for escaping the quote character inside an already escaped value.

        - **RecordDelimiter** *(string) --*

          The value used to separate individual records.

        - **FieldDelimiter** *(string) --*

          The value used to separate individual fields in a record.

        - **QuoteCharacter** *(string) --*

          The value used for escaping where the field delimiter is part of the value.

      - **JSON** *(dict) --*

        Specifies JSON as request's output serialization format.

        - **RecordDelimiter** *(string) --*

          The value used to separate individual records in the output.
    """


_ObjectRestoreObjectRestoreRequestTypeDef = TypedDict(
    "_ObjectRestoreObjectRestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": ObjectRestoreObjectRestoreRequestGlacierJobParametersTypeDef,
        "Type": str,
        "Tier": str,
        "Description": str,
        "SelectParameters": ObjectRestoreObjectRestoreRequestSelectParametersTypeDef,
        "OutputLocation": ObjectRestoreObjectRestoreRequestOutputLocationTypeDef,
    },
    total=False,
)


class ObjectRestoreObjectRestoreRequestTypeDef(
    _ObjectRestoreObjectRestoreRequestTypeDef
):
    """
    Type definition for `ObjectRestoreObject` `RestoreRequest`

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

            Describes the first line of input. Valid values: None, Ignore, Use.

          - **Comments** *(string) --*

            The single character used to indicate a row should be ignored when present at the start
            of a row.

          - **QuoteEscapeCharacter** *(string) --*

            The single character used for escaping the quote character inside an already escaped
            value.

          - **RecordDelimiter** *(string) --*

            The value used to separate individual records.

          - **FieldDelimiter** *(string) --*

            The value used to separate individual fields in a record.

          - **QuoteCharacter** *(string) --*

            Value used for escaping where the field delimiter is part of the value.

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

            Indicates whether or not all output fields should be quoted.

          - **QuoteEscapeCharacter** *(string) --*

            Th single character used for escaping the quote character inside an already escaped value.

          - **RecordDelimiter** *(string) --*

            The value used to separate individual records.

          - **FieldDelimiter** *(string) --*

            The value used to separate individual fields in a record.

          - **QuoteCharacter** *(string) --*

            The value used for escaping where the field delimiter is part of the value.

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

            - **Grantee** *(dict) --*

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

            - *(dict) --*

              - **Key** *(string) --* **[REQUIRED]**

                Name of the tag.

              - **Value** *(string) --* **[REQUIRED]**

                Value of the tag.

        - **UserMetadata** *(list) --*

          A list of metadata to store with the restore results in S3.

          - *(dict) --*

            A metadata key-value pair to store with an object.

            - **Name** *(string) --*

            - **Value** *(string) --*

        - **StorageClass** *(string) --*

          The class of storage used to store the restore results.
    """


_ObjectSummaryCopyFromResponseCopyObjectResultTypeDef = TypedDict(
    "_ObjectSummaryCopyFromResponseCopyObjectResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)


class ObjectSummaryCopyFromResponseCopyObjectResultTypeDef(
    _ObjectSummaryCopyFromResponseCopyObjectResultTypeDef
):
    """
    Type definition for `ObjectSummaryCopyFromResponse` `CopyObjectResult`

    - **ETag** *(string) --*

    - **LastModified** *(datetime) --*
    """


_ObjectSummaryCopyFromResponseTypeDef = TypedDict(
    "_ObjectSummaryCopyFromResponseTypeDef",
    {
        "CopyObjectResult": ObjectSummaryCopyFromResponseCopyObjectResultTypeDef,
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)


class ObjectSummaryCopyFromResponseTypeDef(_ObjectSummaryCopyFromResponseTypeDef):
    """
    Type definition for `ObjectSummaryCopyFrom` `Response`

    - **CopyObjectResult** *(dict) --*

      - **ETag** *(string) --*

      - **LastModified** *(datetime) --*

    - **Expiration** *(string) --*

      If the object expiration is configured, the response includes this header.

    - **CopySourceVersionId** *(string) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **SSEKMSEncryptionContext** *(string) --*

      If present, specifies the AWS KMS Encryption Context to use for object encryption. The value
      of this header is a base64-encoded UTF-8 string holding JSON with the encryption context
      key-value pairs.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ObjectSummaryDeleteResponseTypeDef = TypedDict(
    "_ObjectSummaryDeleteResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)


class ObjectSummaryDeleteResponseTypeDef(_ObjectSummaryDeleteResponseTypeDef):
    """
    Type definition for `ObjectSummaryDelete` `Response`

    - **DeleteMarker** *(boolean) --*

      Specifies whether the versioned object that was permanently deleted was (true) or was not
      (false) a delete marker.

    - **VersionId** *(string) --*

      Returns the version ID of the delete marker created as a result of the DELETE operation.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ObjectSummaryGetResponseTypeDef = TypedDict(
    "_ObjectSummaryGetResponseTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": str,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": str,
        "RequestCharged": str,
        "ReplicationStatus": str,
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": str,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": str,
    },
    total=False,
)


class ObjectSummaryGetResponseTypeDef(_ObjectSummaryGetResponseTypeDef):
    """
    Type definition for `ObjectSummaryGet` `Response`

    - **Body** (:class:`.StreamingBody`) --

      Object data.

    - **DeleteMarker** *(boolean) --*

      Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If
      false, this response header does not appear in the response.

    - **AcceptRanges** *(string) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **StorageClass** *(string) --*

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **ReplicationStatus** *(string) --*

    - **PartsCount** *(integer) --*

      The count of parts this object has.

    - **TagCount** *(integer) --*

      The number of tags, if any, on the object.

    - **ObjectLockMode** *(string) --*

      The object lock mode currently in place for this object.

    - **ObjectLockRetainUntilDate** *(datetime) --*

      The date and time when this object's object lock will expire.

    - **ObjectLockLegalHoldStatus** *(string) --*

      Indicates whether this object has an active legal hold. This field is only returned if you
      have permission to view an object's legal hold status.
    """


_ObjectSummaryPutResponseTypeDef = TypedDict(
    "_ObjectSummaryPutResponseTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": str,
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)


class ObjectSummaryPutResponseTypeDef(_ObjectSummaryPutResponseTypeDef):
    """
    Type definition for `ObjectSummaryPut` `Response`

    - **Expiration** *(string) --*

      If the object expiration is configured, this will contain the expiration date (expiry-date)
      and rule ID (rule-id). The value of rule-id is URL encoded.

    - **ETag** *(string) --*

      Entity tag for the uploaded object.

    - **ServerSideEncryption** *(string) --*

      The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256,
      aws:kms).

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **SSEKMSEncryptionContext** *(string) --*

      If present, specifies the AWS KMS Encryption Context to use for object encryption. The value
      of this header is a base64-encoded UTF-8 string holding JSON with the encryption context
      key-value pairs.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ObjectSummaryRestoreObjectResponseTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectResponseTypeDef",
    {"RequestCharged": str, "RestoreOutputPath": str},
    total=False,
)


class ObjectSummaryRestoreObjectResponseTypeDef(
    _ObjectSummaryRestoreObjectResponseTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObject` `Response`

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **RestoreOutputPath** *(string) --*

      Indicates the path in the provided S3 output location where Select results will be restored
      to.
    """


_ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    {"Tier": str},
)


class ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequest` `GlacierJobParameters`

    Glacier related parameters pertaining to this job. Do not use with restores that specify
    OutputLocation.

    - **Tier** *(string) --* **[REQUIRED]**

      Glacier retrieval tier at which the restore will be processed.
    """


_RequiredObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_RequiredObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {"Type": str},
)
_OptionalObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_OptionalObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "URI": str},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef(
    _RequiredObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
    _OptionalObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlList` `Grantee`

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
    """


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3` `AccessControlList`

    - **Grantee** *(dict) --*

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
    """


_RequiredObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "_RequiredObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": str},
)
_OptionalObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "_OptionalObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef(
    _RequiredObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
    _OptionalObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3` `Encryption`

    - **EncryptionType** *(string) --* **[REQUIRED]**

      The server-side encryption algorithm used when storing job results in Amazon S3 (e.g.,
      AES256, aws:kms).

    - **KMSKeyId** *(string) --*

      If the encryption type is aws:kms, this optional value specifies the AWS KMS key ID to
      use for encryption of job results.

    - **KMSContext** *(string) --*

      If the encryption type is aws:kms, this optional value can be used to specify the
      encryption context for the restore results.
    """


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    {"Key": str, "Value": str},
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3Tagging` `TagSet`

    - **Key** *(string) --* **[REQUIRED]**

      Name of the tag.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag.
    """


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    {
        "TagSet": List[
            ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef
        ]
    },
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3` `Tagging`

    The tag-set that is applied to the restore results.

    - **TagSet** *(list) --* **[REQUIRED]**

      - *(dict) --*

        - **Key** *(string) --* **[REQUIRED]**

          Name of the tag.

        - **Value** *(string) --* **[REQUIRED]**

          Value of the tag.
    """


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3` `UserMetadata`

    A metadata key-value pair to store with an object.

    - **Name** *(string) --*

    - **Value** *(string) --*
    """


_RequiredObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "_RequiredObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    {"BucketName": str, "Prefix": str},
)
_OptionalObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "_OptionalObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    {
        "Encryption": ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
        "CannedACL": str,
        "AccessControlList": List[
            ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef,
        "UserMetadata": List[
            ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef
        ],
        "StorageClass": str,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef(
    _RequiredObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef,
    _OptionalObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef,
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestOutputLocation` `S3`

    Describes an S3 location that will receive the results of the restore request.

    - **BucketName** *(string) --* **[REQUIRED]**

      The name of the bucket where the restore results will be placed.

    - **Prefix** *(string) --* **[REQUIRED]**

      The prefix that is prepended to the restore results for this request.

    - **Encryption** *(dict) --*

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

        - **Grantee** *(dict) --*

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

        - *(dict) --*

          - **Key** *(string) --* **[REQUIRED]**

            Name of the tag.

          - **Value** *(string) --* **[REQUIRED]**

            Value of the tag.

    - **UserMetadata** *(list) --*

      A list of metadata to store with the restore results in S3.

      - *(dict) --*

        A metadata key-value pair to store with an object.

        - **Name** *(string) --*

        - **Value** *(string) --*

    - **StorageClass** *(string) --*

      The class of storage used to store the restore results.
    """


_ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef",
    {"S3": ObjectSummaryRestoreObjectRestoreRequestOutputLocationS3TypeDef},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequest` `OutputLocation`

    Describes the location where the restore job's output is stored.

    - **S3** *(dict) --*

      Describes an S3 location that will receive the results of the restore request.

      - **BucketName** *(string) --* **[REQUIRED]**

        The name of the bucket where the restore results will be placed.

      - **Prefix** *(string) --* **[REQUIRED]**

        The prefix that is prepended to the restore results for this request.

      - **Encryption** *(dict) --*

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

          - **Grantee** *(dict) --*

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

          - *(dict) --*

            - **Key** *(string) --* **[REQUIRED]**

              Name of the tag.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag.

      - **UserMetadata** *(list) --*

        A list of metadata to store with the restore results in S3.

        - *(dict) --*

          A metadata key-value pair to store with an object.

          - **Name** *(string) --*

          - **Value** *(string) --*

      - **StorageClass** *(string) --*

        The class of storage used to store the restore results.
    """


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    {
        "FileHeaderInfo": str,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerialization` `CSV`

    Describes the serialization of a CSV-encoded object.

    - **FileHeaderInfo** *(string) --*

      Describes the first line of input. Valid values: None, Ignore, Use.

    - **Comments** *(string) --*

      The single character used to indicate a row should be ignored when present at the start
      of a row.

    - **QuoteEscapeCharacter** *(string) --*

      The single character used for escaping the quote character inside an already escaped
      value.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records.

    - **FieldDelimiter** *(string) --*

      The value used to separate individual fields in a record.

    - **QuoteCharacter** *(string) --*

      Value used for escaping where the field delimiter is part of the value.

    - **AllowQuotedRecordDelimiter** *(boolean) --*

      Specifies that CSV field values may contain quoted record delimiters and such records
      should be allowed. Default value is FALSE. Setting this value to TRUE may lower
      performance.
    """


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    {"Type": str},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerialization` `JSON`

    Specifies JSON as object's input serialization format.

    - **Type** *(string) --*

      The type of JSON. Valid values: Document, Lines.
    """


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    {
        "CSV": ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef,
        "CompressionType": str,
        "JSON": ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef,
        "Parquet": Dict,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestSelectParameters` `InputSerialization`

    Describes the serialization format of the object.

    - **CSV** *(dict) --*

      Describes the serialization of a CSV-encoded object.

      - **FileHeaderInfo** *(string) --*

        Describes the first line of input. Valid values: None, Ignore, Use.

      - **Comments** *(string) --*

        The single character used to indicate a row should be ignored when present at the start
        of a row.

      - **QuoteEscapeCharacter** *(string) --*

        The single character used for escaping the quote character inside an already escaped
        value.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records.

      - **FieldDelimiter** *(string) --*

        The value used to separate individual fields in a record.

      - **QuoteCharacter** *(string) --*

        Value used for escaping where the field delimiter is part of the value.

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
    """


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    {
        "QuoteFields": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerialization` `CSV`

    Describes the serialization of CSV-encoded Select results.

    - **QuoteFields** *(string) --*

      Indicates whether or not all output fields should be quoted.

    - **QuoteEscapeCharacter** *(string) --*

      Th single character used for escaping the quote character inside an already escaped value.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records.

    - **FieldDelimiter** *(string) --*

      The value used to separate individual fields in a record.

    - **QuoteCharacter** *(string) --*

      The value used for escaping where the field delimiter is part of the value.
    """


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerialization` `JSON`

    Specifies JSON as request's output serialization format.

    - **RecordDelimiter** *(string) --*

      The value used to separate individual records in the output.
    """


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    {
        "CSV": ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef,
        "JSON": ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequestSelectParameters` `OutputSerialization`

    Describes how the results of the Select job are serialized.

    - **CSV** *(dict) --*

      Describes the serialization of CSV-encoded Select results.

      - **QuoteFields** *(string) --*

        Indicates whether or not all output fields should be quoted.

      - **QuoteEscapeCharacter** *(string) --*

        Th single character used for escaping the quote character inside an already escaped value.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records.

      - **FieldDelimiter** *(string) --*

        The value used to separate individual fields in a record.

      - **QuoteCharacter** *(string) --*

        The value used for escaping where the field delimiter is part of the value.

    - **JSON** *(dict) --*

      Specifies JSON as request's output serialization format.

      - **RecordDelimiter** *(string) --*

        The value used to separate individual records in the output.
    """


_ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef",
    {
        "InputSerialization": ObjectSummaryRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ObjectSummaryRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef,
    },
)


class ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObjectRestoreRequest` `SelectParameters`

    Describes the parameters for Select job types.

    - **InputSerialization** *(dict) --* **[REQUIRED]**

      Describes the serialization format of the object.

      - **CSV** *(dict) --*

        Describes the serialization of a CSV-encoded object.

        - **FileHeaderInfo** *(string) --*

          Describes the first line of input. Valid values: None, Ignore, Use.

        - **Comments** *(string) --*

          The single character used to indicate a row should be ignored when present at the start
          of a row.

        - **QuoteEscapeCharacter** *(string) --*

          The single character used for escaping the quote character inside an already escaped
          value.

        - **RecordDelimiter** *(string) --*

          The value used to separate individual records.

        - **FieldDelimiter** *(string) --*

          The value used to separate individual fields in a record.

        - **QuoteCharacter** *(string) --*

          Value used for escaping where the field delimiter is part of the value.

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

          Indicates whether or not all output fields should be quoted.

        - **QuoteEscapeCharacter** *(string) --*

          Th single character used for escaping the quote character inside an already escaped value.

        - **RecordDelimiter** *(string) --*

          The value used to separate individual records.

        - **FieldDelimiter** *(string) --*

          The value used to separate individual fields in a record.

        - **QuoteCharacter** *(string) --*

          The value used for escaping where the field delimiter is part of the value.

      - **JSON** *(dict) --*

        Specifies JSON as request's output serialization format.

        - **RecordDelimiter** *(string) --*

          The value used to separate individual records in the output.
    """


_ObjectSummaryRestoreObjectRestoreRequestTypeDef = TypedDict(
    "_ObjectSummaryRestoreObjectRestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": ObjectSummaryRestoreObjectRestoreRequestGlacierJobParametersTypeDef,
        "Type": str,
        "Tier": str,
        "Description": str,
        "SelectParameters": ObjectSummaryRestoreObjectRestoreRequestSelectParametersTypeDef,
        "OutputLocation": ObjectSummaryRestoreObjectRestoreRequestOutputLocationTypeDef,
    },
    total=False,
)


class ObjectSummaryRestoreObjectRestoreRequestTypeDef(
    _ObjectSummaryRestoreObjectRestoreRequestTypeDef
):
    """
    Type definition for `ObjectSummaryRestoreObject` `RestoreRequest`

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

            Describes the first line of input. Valid values: None, Ignore, Use.

          - **Comments** *(string) --*

            The single character used to indicate a row should be ignored when present at the start
            of a row.

          - **QuoteEscapeCharacter** *(string) --*

            The single character used for escaping the quote character inside an already escaped
            value.

          - **RecordDelimiter** *(string) --*

            The value used to separate individual records.

          - **FieldDelimiter** *(string) --*

            The value used to separate individual fields in a record.

          - **QuoteCharacter** *(string) --*

            Value used for escaping where the field delimiter is part of the value.

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

            Indicates whether or not all output fields should be quoted.

          - **QuoteEscapeCharacter** *(string) --*

            Th single character used for escaping the quote character inside an already escaped value.

          - **RecordDelimiter** *(string) --*

            The value used to separate individual records.

          - **FieldDelimiter** *(string) --*

            The value used to separate individual fields in a record.

          - **QuoteCharacter** *(string) --*

            The value used for escaping where the field delimiter is part of the value.

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

            - **Grantee** *(dict) --*

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

            - *(dict) --*

              - **Key** *(string) --* **[REQUIRED]**

                Name of the tag.

              - **Value** *(string) --* **[REQUIRED]**

                Value of the tag.

        - **UserMetadata** *(list) --*

          A list of metadata to store with the restore results in S3.

          - *(dict) --*

            A metadata key-value pair to store with an object.

            - **Name** *(string) --*

            - **Value** *(string) --*

        - **StorageClass** *(string) --*

          The class of storage used to store the restore results.
    """


_ObjectVersionDeleteResponseTypeDef = TypedDict(
    "_ObjectVersionDeleteResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)


class ObjectVersionDeleteResponseTypeDef(_ObjectVersionDeleteResponseTypeDef):
    """
    Type definition for `ObjectVersionDelete` `Response`

    - **DeleteMarker** *(boolean) --*

      Specifies whether the versioned object that was permanently deleted was (true) or was not
      (false) a delete marker.

    - **VersionId** *(string) --*

      Returns the version ID of the delete marker created as a result of the DELETE operation.

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.
    """


_ObjectVersionGetResponseTypeDef = TypedDict(
    "_ObjectVersionGetResponseTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": str,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": str,
        "RequestCharged": str,
        "ReplicationStatus": str,
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": str,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": str,
    },
    total=False,
)


class ObjectVersionGetResponseTypeDef(_ObjectVersionGetResponseTypeDef):
    """
    Type definition for `ObjectVersionGet` `Response`

    - **Body** (:class:`.StreamingBody`) --

      Object data.

    - **DeleteMarker** *(boolean) --*

      Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If
      false, this response header does not appear in the response.

    - **AcceptRanges** *(string) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **StorageClass** *(string) --*

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **ReplicationStatus** *(string) --*

    - **PartsCount** *(integer) --*

      The count of parts this object has.

    - **TagCount** *(integer) --*

      The number of tags, if any, on the object.

    - **ObjectLockMode** *(string) --*

      The object lock mode currently in place for this object.

    - **ObjectLockRetainUntilDate** *(datetime) --*

      The date and time when this object's object lock will expire.

    - **ObjectLockLegalHoldStatus** *(string) --*

      Indicates whether this object has an active legal hold. This field is only returned if you
      have permission to view an object's legal hold status.
    """


_ObjectVersionHeadResponseTypeDef = TypedDict(
    "_ObjectVersionHeadResponseTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": str,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": str,
        "RequestCharged": str,
        "ReplicationStatus": str,
        "PartsCount": int,
        "ObjectLockMode": str,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": str,
    },
    total=False,
)


class ObjectVersionHeadResponseTypeDef(_ObjectVersionHeadResponseTypeDef):
    """
    Type definition for `ObjectVersionHead` `Response`

    - **DeleteMarker** *(boolean) --*

      Specifies whether the object retrieved was (true) or was not (false) a Delete Marker. If
      false, this response header does not appear in the response.

    - **AcceptRanges** *(string) --*

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

      If present, specifies the ID of the AWS Key Management Service (KMS) master encryption key
      that was used for the object.

    - **StorageClass** *(string) --*

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **ReplicationStatus** *(string) --*

    - **PartsCount** *(integer) --*

      The count of parts this object has.

    - **ObjectLockMode** *(string) --*

      The object lock mode currently in place for this object.

    - **ObjectLockRetainUntilDate** *(datetime) --*

      The date and time when this object's object lock expires.

    - **ObjectLockLegalHoldStatus** *(string) --*

      The Legal Hold status for the specified object.
    """


_ObjectVersionsDeleteResponseDeletedTypeDef = TypedDict(
    "_ObjectVersionsDeleteResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)


class ObjectVersionsDeleteResponseDeletedTypeDef(
    _ObjectVersionsDeleteResponseDeletedTypeDef
):
    """
    Type definition for `ObjectVersionsDeleteResponse` `Deleted`

    - **Key** *(string) --*

    - **VersionId** *(string) --*

    - **DeleteMarker** *(boolean) --*

    - **DeleteMarkerVersionId** *(string) --*
    """


_ObjectVersionsDeleteResponseErrorsTypeDef = TypedDict(
    "_ObjectVersionsDeleteResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)


class ObjectVersionsDeleteResponseErrorsTypeDef(
    _ObjectVersionsDeleteResponseErrorsTypeDef
):
    """
    Type definition for `ObjectVersionsDeleteResponse` `Errors`

    - **Key** *(string) --*

    - **VersionId** *(string) --*

    - **Code** *(string) --*

    - **Message** *(string) --*
    """


_ObjectVersionsDeleteResponseTypeDef = TypedDict(
    "_ObjectVersionsDeleteResponseTypeDef",
    {
        "Deleted": List[ObjectVersionsDeleteResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[ObjectVersionsDeleteResponseErrorsTypeDef],
    },
    total=False,
)


class ObjectVersionsDeleteResponseTypeDef(_ObjectVersionsDeleteResponseTypeDef):
    """
    Type definition for `ObjectVersionsDelete` `Response`

    - **Deleted** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **VersionId** *(string) --*

        - **DeleteMarker** *(boolean) --*

        - **DeleteMarkerVersionId** *(string) --*

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **Errors** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **VersionId** *(string) --*

        - **Code** *(string) --*

        - **Message** *(string) --*
    """


_ObjectsDeleteResponseDeletedTypeDef = TypedDict(
    "_ObjectsDeleteResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)


class ObjectsDeleteResponseDeletedTypeDef(_ObjectsDeleteResponseDeletedTypeDef):
    """
    Type definition for `ObjectsDeleteResponse` `Deleted`

    - **Key** *(string) --*

    - **VersionId** *(string) --*

    - **DeleteMarker** *(boolean) --*

    - **DeleteMarkerVersionId** *(string) --*
    """


_ObjectsDeleteResponseErrorsTypeDef = TypedDict(
    "_ObjectsDeleteResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)


class ObjectsDeleteResponseErrorsTypeDef(_ObjectsDeleteResponseErrorsTypeDef):
    """
    Type definition for `ObjectsDeleteResponse` `Errors`

    - **Key** *(string) --*

    - **VersionId** *(string) --*

    - **Code** *(string) --*

    - **Message** *(string) --*
    """


_ObjectsDeleteResponseTypeDef = TypedDict(
    "_ObjectsDeleteResponseTypeDef",
    {
        "Deleted": List[ObjectsDeleteResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[ObjectsDeleteResponseErrorsTypeDef],
    },
    total=False,
)


class ObjectsDeleteResponseTypeDef(_ObjectsDeleteResponseTypeDef):
    """
    Type definition for `ObjectsDelete` `Response`

    - **Deleted** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **VersionId** *(string) --*

        - **DeleteMarker** *(boolean) --*

        - **DeleteMarkerVersionId** *(string) --*

    - **RequestCharged** *(string) --*

      If present, indicates that the requester was successfully charged for the request.

    - **Errors** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **VersionId** *(string) --*

        - **Code** *(string) --*

        - **Message** *(string) --*
    """


_ServiceResourceCreateBucketCreateBucketConfigurationTypeDef = TypedDict(
    "_ServiceResourceCreateBucketCreateBucketConfigurationTypeDef",
    {"LocationConstraint": str},
    total=False,
)


class ServiceResourceCreateBucketCreateBucketConfigurationTypeDef(
    _ServiceResourceCreateBucketCreateBucketConfigurationTypeDef
):
    """
    Type definition for `ServiceResourceCreateBucket` `CreateBucketConfiguration`

    - **LocationConstraint** *(string) --*

      Specifies the region where the bucket will be created. If you don't specify a region, the
      bucket is created in US East (N. Virginia) Region (us-east-1).
    """
