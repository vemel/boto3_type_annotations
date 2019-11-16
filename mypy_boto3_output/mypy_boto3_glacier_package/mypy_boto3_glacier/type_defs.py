"Main interface for glacier type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCompleteMultipartUploadResponseTypeDef",
    "ClientCreateVaultResponseTypeDef",
    "ClientDescribeJobResponseInventoryRetrievalParametersTypeDef",
    "ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef",
    "ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef",
    "ClientDescribeJobResponseOutputLocationS3TypeDef",
    "ClientDescribeJobResponseOutputLocationTypeDef",
    "ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef",
    "ClientDescribeJobResponseSelectParametersInputSerializationTypeDef",
    "ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef",
    "ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef",
    "ClientDescribeJobResponseSelectParametersTypeDef",
    "ClientDescribeJobResponseTypeDef",
    "ClientDescribeVaultResponseTypeDef",
    "ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef",
    "ClientGetDataRetrievalPolicyResponsePolicyTypeDef",
    "ClientGetDataRetrievalPolicyResponseTypeDef",
    "ClientGetJobOutputResponseTypeDef",
    "ClientGetVaultAccessPolicyResponsepolicyTypeDef",
    "ClientGetVaultAccessPolicyResponseTypeDef",
    "ClientGetVaultLockResponseTypeDef",
    "ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef",
    "ClientGetVaultNotificationsResponseTypeDef",
    "ClientInitiateJobResponseTypeDef",
    "ClientInitiateJobjobParametersInventoryRetrievalParametersTypeDef",
    "ClientInitiateJobjobParametersOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientInitiateJobjobParametersOutputLocationS3AccessControlListTypeDef",
    "ClientInitiateJobjobParametersOutputLocationS3EncryptionTypeDef",
    "ClientInitiateJobjobParametersOutputLocationS3TypeDef",
    "ClientInitiateJobjobParametersOutputLocationTypeDef",
    "ClientInitiateJobjobParametersSelectParametersInputSerializationcsvTypeDef",
    "ClientInitiateJobjobParametersSelectParametersInputSerializationTypeDef",
    "ClientInitiateJobjobParametersSelectParametersOutputSerializationcsvTypeDef",
    "ClientInitiateJobjobParametersSelectParametersOutputSerializationTypeDef",
    "ClientInitiateJobjobParametersSelectParametersTypeDef",
    "ClientInitiateJobjobParametersTypeDef",
    "ClientInitiateMultipartUploadResponseTypeDef",
    "ClientInitiateVaultLockResponseTypeDef",
    "ClientInitiateVaultLockpolicyTypeDef",
    "ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef",
    "ClientListJobsResponseJobListOutputLocationS3TypeDef",
    "ClientListJobsResponseJobListOutputLocationTypeDef",
    "ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef",
    "ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef",
    "ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    "ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef",
    "ClientListJobsResponseJobListSelectParametersTypeDef",
    "ClientListJobsResponseJobListTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientListMultipartUploadsResponseUploadsListTypeDef",
    "ClientListMultipartUploadsResponseTypeDef",
    "ClientListPartsResponsePartsTypeDef",
    "ClientListPartsResponseTypeDef",
    "ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef",
    "ClientListProvisionedCapacityResponseTypeDef",
    "ClientListTagsForVaultResponseTypeDef",
    "ClientListVaultsResponseVaultListTypeDef",
    "ClientListVaultsResponseTypeDef",
    "ClientPurchaseProvisionedCapacityResponseTypeDef",
    "ClientSetDataRetrievalPolicyPolicyRulesTypeDef",
    "ClientSetDataRetrievalPolicyPolicyTypeDef",
    "ClientSetVaultAccessPolicypolicyTypeDef",
    "ClientSetVaultNotificationsvaultNotificationConfigTypeDef",
    "ClientUploadArchiveResponseTypeDef",
    "ClientUploadMultipartPartResponseTypeDef",
    "JobGetOutputResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef",
    "ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    "ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef",
    "ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef",
    "ListJobsPaginateResponseJobListOutputLocationS3TypeDef",
    "ListJobsPaginateResponseJobListOutputLocationTypeDef",
    "ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef",
    "ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef",
    "ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    "ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef",
    "ListJobsPaginateResponseJobListSelectParametersTypeDef",
    "ListJobsPaginateResponseJobListTypeDef",
    "ListJobsPaginateResponseTypeDef",
    "ListMultipartUploadsPaginatePaginationConfigTypeDef",
    "ListMultipartUploadsPaginateResponseUploadsListTypeDef",
    "ListMultipartUploadsPaginateResponseTypeDef",
    "ListPartsPaginatePaginationConfigTypeDef",
    "ListPartsPaginateResponsePartsTypeDef",
    "ListPartsPaginateResponseTypeDef",
    "ListVaultsPaginatePaginationConfigTypeDef",
    "ListVaultsPaginateResponseVaultListTypeDef",
    "ListVaultsPaginateResponseTypeDef",
    "MultipartUploadCompleteResponseTypeDef",
    "MultipartUploadPartsResponsePartsTypeDef",
    "MultipartUploadPartsResponseTypeDef",
    "MultipartUploadUploadPartResponseTypeDef",
    "NotificationSetvaultNotificationConfigTypeDef",
    "VaultCreateResponseTypeDef",
    "VaultExistsWaitWaiterConfigTypeDef",
    "VaultNotExistsWaitWaiterConfigTypeDef",
)


_ClientCompleteMultipartUploadResponseTypeDef = TypedDict(
    "_ClientCompleteMultipartUploadResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)


class ClientCompleteMultipartUploadResponseTypeDef(
    _ClientCompleteMultipartUploadResponseTypeDef
):
    """
    Type definition for `ClientCompleteMultipartUpload` `Response`

    Contains the Amazon S3 Glacier response to your request.

    For information about the underlying REST API, see `Upload Archive
    <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ . For
    conceptual information, see `Working with Archives in Amazon S3 Glacier
    <https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ .

    - **location** *(string) --*

      The relative URI path of the newly added archive resource.

    - **checksum** *(string) --*

      The checksum of the archive computed by Amazon S3 Glacier.

    - **archiveId** *(string) --*

      The ID of the archive. This value is also included as part of the location.
    """


_ClientCreateVaultResponseTypeDef = TypedDict(
    "_ClientCreateVaultResponseTypeDef", {"location": str}, total=False
)


class ClientCreateVaultResponseTypeDef(_ClientCreateVaultResponseTypeDef):
    """
    Type definition for `ClientCreateVault` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **location** *(string) --*

      The URI of the vault that was created.
    """


_ClientDescribeJobResponseInventoryRetrievalParametersTypeDef = TypedDict(
    "_ClientDescribeJobResponseInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)


class ClientDescribeJobResponseInventoryRetrievalParametersTypeDef(
    _ClientDescribeJobResponseInventoryRetrievalParametersTypeDef
):
    """
    Type definition for `ClientDescribeJobResponse` `InventoryRetrievalParameters`

    Parameters used for range inventory retrieval.

    - **Format** *(string) --*

      The output format for the vault inventory list, which is set by the **InitiateJob** request
      when initiating a job to retrieve a vault inventory. Valid values are ``CSV`` and ``JSON`` .

    - **StartDate** *(string) --*

      The start of the date range in Universal Coordinated Time (UTC) for vault inventory
      retrieval that includes archives created on or after this date. This value should be a
      string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

    - **EndDate** *(string) --*

      The end of the date range in UTC for vault inventory retrieval that includes archives
      created before this date. This value should be a string in the ISO 8601 date format, for
      example ``2013-03-20T17:03:43Z`` .

    - **Limit** *(string) --*

      The maximum number of inventory items returned per vault inventory retrieval request. This
      limit is set when initiating the job with the a **InitiateJob** request.

    - **Marker** *(string) --*

      An opaque string that represents where to continue pagination of the vault inventory
      retrieval results. You use the marker in a new **InitiateJob** request to obtain additional
      inventory items. If there are no more inventory items, this value is ``null`` . For more
      information, see `Range Inventory Retrieval
      <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__
      .
    """


_ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef",
    {"Type": str, "DisplayName": str, "URI": str, "ID": str, "EmailAddress": str},
    total=False,
)


class ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef(
    _ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseOutputLocationS3AccessControlList` `Grantee`

    The grantee.

    - **Type** *(string) --*

      Type of grantee

    - **DisplayName** *(string) --*

      Screen name of the grantee.

    - **URI** *(string) --*

      URI of the grantee group.

    - **ID** *(string) --*

      The canonical user ID of the grantee.

    - **EmailAddress** *(string) --*

      Email address of the grantee.
    """


_ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientDescribeJobResponseOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef(
    _ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseOutputLocationS3` `AccessControlList`

    Contains information about a grant.

    - **Grantee** *(dict) --*

      The grantee.

      - **Type** *(string) --*

        Type of grantee

      - **DisplayName** *(string) --*

        Screen name of the grantee.

      - **URI** *(string) --*

        URI of the grantee group.

      - **ID** *(string) --*

        The canonical user ID of the grantee.

      - **EmailAddress** *(string) --*

        Email address of the grantee.

    - **Permission** *(string) --*

      Specifies the permission given to the grantee.
    """


_ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": str, "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef(
    _ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseOutputLocationS3` `Encryption`

    Contains information about the encryption used to store the job results in Amazon S3.

    - **EncryptionType** *(string) --*

      The server-side encryption algorithm used when storing job results in Amazon S3, for
      example ``AES256`` or ``aws:kms`` .

    - **KMSKeyId** *(string) --*

      The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object
      protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature
      Version 4.

    - **KMSContext** *(string) --*

      Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the
      encryption context for the job results.
    """


_ClientDescribeJobResponseOutputLocationS3TypeDef = TypedDict(
    "_ClientDescribeJobResponseOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientDescribeJobResponseOutputLocationS3EncryptionTypeDef,
        "CannedACL": str,
        "AccessControlList": List[
            ClientDescribeJobResponseOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": str,
    },
    total=False,
)


class ClientDescribeJobResponseOutputLocationS3TypeDef(
    _ClientDescribeJobResponseOutputLocationS3TypeDef
):
    """
    Type definition for `ClientDescribeJobResponseOutputLocation` `S3`

    Describes an S3 location that will receive the results of the job request.

    - **BucketName** *(string) --*

      The name of the Amazon S3 bucket where the job results are stored.

    - **Prefix** *(string) --*

      The prefix that is prepended to the results for this request.

    - **Encryption** *(dict) --*

      Contains information about the encryption used to store the job results in Amazon S3.

      - **EncryptionType** *(string) --*

        The server-side encryption algorithm used when storing job results in Amazon S3, for
        example ``AES256`` or ``aws:kms`` .

      - **KMSKeyId** *(string) --*

        The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object
        protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature
        Version 4.

      - **KMSContext** *(string) --*

        Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the
        encryption context for the job results.

    - **CannedACL** *(string) --*

      The canned access control list (ACL) to apply to the job results.

    - **AccessControlList** *(list) --*

      A list of grants that control access to the staged results.

      - *(dict) --*

        Contains information about a grant.

        - **Grantee** *(dict) --*

          The grantee.

          - **Type** *(string) --*

            Type of grantee

          - **DisplayName** *(string) --*

            Screen name of the grantee.

          - **URI** *(string) --*

            URI of the grantee group.

          - **ID** *(string) --*

            The canonical user ID of the grantee.

          - **EmailAddress** *(string) --*

            Email address of the grantee.

        - **Permission** *(string) --*

          Specifies the permission given to the grantee.

    - **Tagging** *(dict) --*

      The tag-set that is applied to the job results.

      - *(string) --*

        - *(string) --*

    - **UserMetadata** *(dict) --*

      A map of metadata to store with the job results in Amazon S3.

      - *(string) --*

        - *(string) --*

    - **StorageClass** *(string) --*

      The storage class used to store the job results.
    """


_ClientDescribeJobResponseOutputLocationTypeDef = TypedDict(
    "_ClientDescribeJobResponseOutputLocationTypeDef",
    {"S3": ClientDescribeJobResponseOutputLocationS3TypeDef},
    total=False,
)


class ClientDescribeJobResponseOutputLocationTypeDef(
    _ClientDescribeJobResponseOutputLocationTypeDef
):
    """
    Type definition for `ClientDescribeJobResponse` `OutputLocation`

    Contains the location where the data from the select job is stored.

    - **S3** *(dict) --*

      Describes an S3 location that will receive the results of the job request.

      - **BucketName** *(string) --*

        The name of the Amazon S3 bucket where the job results are stored.

      - **Prefix** *(string) --*

        The prefix that is prepended to the results for this request.

      - **Encryption** *(dict) --*

        Contains information about the encryption used to store the job results in Amazon S3.

        - **EncryptionType** *(string) --*

          The server-side encryption algorithm used when storing job results in Amazon S3, for
          example ``AES256`` or ``aws:kms`` .

        - **KMSKeyId** *(string) --*

          The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object
          protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature
          Version 4.

        - **KMSContext** *(string) --*

          Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the
          encryption context for the job results.

      - **CannedACL** *(string) --*

        The canned access control list (ACL) to apply to the job results.

      - **AccessControlList** *(list) --*

        A list of grants that control access to the staged results.

        - *(dict) --*

          Contains information about a grant.

          - **Grantee** *(dict) --*

            The grantee.

            - **Type** *(string) --*

              Type of grantee

            - **DisplayName** *(string) --*

              Screen name of the grantee.

            - **URI** *(string) --*

              URI of the grantee group.

            - **ID** *(string) --*

              The canonical user ID of the grantee.

            - **EmailAddress** *(string) --*

              Email address of the grantee.

          - **Permission** *(string) --*

            Specifies the permission given to the grantee.

      - **Tagging** *(dict) --*

        The tag-set that is applied to the job results.

        - *(string) --*

          - *(string) --*

      - **UserMetadata** *(dict) --*

        A map of metadata to store with the job results in Amazon S3.

        - *(string) --*

          - *(string) --*

      - **StorageClass** *(string) --*

        The storage class used to store the job results.
    """


_ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "_ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": str,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef(
    _ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSelectParametersInputSerialization` `csv`

    Describes the serialization of a CSV-encoded object.

    - **FileHeaderInfo** *(string) --*

      Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use``
      .

    - **Comments** *(string) --*

      A single character used to indicate that a row should be ignored when the character is
      present at the start of that row.

    - **QuoteEscapeCharacter** *(string) --*

      A single character used for escaping the quotation-mark character inside an already
      escaped value.

    - **RecordDelimiter** *(string) --*

      A value used to separate individual records from each other.

    - **FieldDelimiter** *(string) --*

      A value used to separate individual fields from each other within a record.

    - **QuoteCharacter** *(string) --*

      A value used as an escape character where the field delimiter is part of the value.
    """


_ClientDescribeJobResponseSelectParametersInputSerializationTypeDef = TypedDict(
    "_ClientDescribeJobResponseSelectParametersInputSerializationTypeDef",
    {"csv": ClientDescribeJobResponseSelectParametersInputSerializationcsvTypeDef},
    total=False,
)


class ClientDescribeJobResponseSelectParametersInputSerializationTypeDef(
    _ClientDescribeJobResponseSelectParametersInputSerializationTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSelectParameters` `InputSerialization`

    Describes the serialization format of the object.

    - **csv** *(dict) --*

      Describes the serialization of a CSV-encoded object.

      - **FileHeaderInfo** *(string) --*

        Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use``
        .

      - **Comments** *(string) --*

        A single character used to indicate that a row should be ignored when the character is
        present at the start of that row.

      - **QuoteEscapeCharacter** *(string) --*

        A single character used for escaping the quotation-mark character inside an already
        escaped value.

      - **RecordDelimiter** *(string) --*

        A value used to separate individual records from each other.

      - **FieldDelimiter** *(string) --*

        A value used to separate individual fields from each other within a record.

      - **QuoteCharacter** *(string) --*

        A value used as an escape character where the field delimiter is part of the value.
    """


_ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "_ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef(
    _ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSelectParametersOutputSerialization` `csv`

    Describes the serialization of CSV-encoded query results.

    - **QuoteFields** *(string) --*

      A value that indicates whether all output fields should be contained within quotation
      marks.

    - **QuoteEscapeCharacter** *(string) --*

      A single character used for escaping the quotation-mark character inside an already
      escaped value.

    - **RecordDelimiter** *(string) --*

      A value used to separate individual records from each other.

    - **FieldDelimiter** *(string) --*

      A value used to separate individual fields from each other within a record.

    - **QuoteCharacter** *(string) --*

      A value used as an escape character where the field delimiter is part of the value.
    """


_ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef",
    {"csv": ClientDescribeJobResponseSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)


class ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef(
    _ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseSelectParameters` `OutputSerialization`

    Describes how the results of the select job are serialized.

    - **csv** *(dict) --*

      Describes the serialization of CSV-encoded query results.

      - **QuoteFields** *(string) --*

        A value that indicates whether all output fields should be contained within quotation
        marks.

      - **QuoteEscapeCharacter** *(string) --*

        A single character used for escaping the quotation-mark character inside an already
        escaped value.

      - **RecordDelimiter** *(string) --*

        A value used to separate individual records from each other.

      - **FieldDelimiter** *(string) --*

        A value used to separate individual fields from each other within a record.

      - **QuoteCharacter** *(string) --*

        A value used as an escape character where the field delimiter is part of the value.
    """


_ClientDescribeJobResponseSelectParametersTypeDef = TypedDict(
    "_ClientDescribeJobResponseSelectParametersTypeDef",
    {
        "InputSerialization": ClientDescribeJobResponseSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientDescribeJobResponseSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseSelectParametersTypeDef(
    _ClientDescribeJobResponseSelectParametersTypeDef
):
    """
    Type definition for `ClientDescribeJobResponse` `SelectParameters`

    Contains the parameters used for a select.

    - **InputSerialization** *(dict) --*

      Describes the serialization format of the object.

      - **csv** *(dict) --*

        Describes the serialization of a CSV-encoded object.

        - **FileHeaderInfo** *(string) --*

          Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use``
          .

        - **Comments** *(string) --*

          A single character used to indicate that a row should be ignored when the character is
          present at the start of that row.

        - **QuoteEscapeCharacter** *(string) --*

          A single character used for escaping the quotation-mark character inside an already
          escaped value.

        - **RecordDelimiter** *(string) --*

          A value used to separate individual records from each other.

        - **FieldDelimiter** *(string) --*

          A value used to separate individual fields from each other within a record.

        - **QuoteCharacter** *(string) --*

          A value used as an escape character where the field delimiter is part of the value.

    - **ExpressionType** *(string) --*

      The type of the provided expression, for example ``SQL`` .

    - **Expression** *(string) --*

      The expression that is used to select the object.

    - **OutputSerialization** *(dict) --*

      Describes how the results of the select job are serialized.

      - **csv** *(dict) --*

        Describes the serialization of CSV-encoded query results.

        - **QuoteFields** *(string) --*

          A value that indicates whether all output fields should be contained within quotation
          marks.

        - **QuoteEscapeCharacter** *(string) --*

          A single character used for escaping the quotation-mark character inside an already
          escaped value.

        - **RecordDelimiter** *(string) --*

          A value used to separate individual records from each other.

        - **FieldDelimiter** *(string) --*

          A value used to separate individual fields from each other within a record.

        - **QuoteCharacter** *(string) --*

          A value used as an escape character where the field delimiter is part of the value.
    """


_ClientDescribeJobResponseTypeDef = TypedDict(
    "_ClientDescribeJobResponseTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": str,
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": str,
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ClientDescribeJobResponseInventoryRetrievalParametersTypeDef,
        "JobOutputPath": str,
        "SelectParameters": ClientDescribeJobResponseSelectParametersTypeDef,
        "OutputLocation": ClientDescribeJobResponseOutputLocationTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseTypeDef(_ClientDescribeJobResponseTypeDef):
    """
    Type definition for `ClientDescribeJob` `Response`

    Contains the description of an Amazon S3 Glacier job.

    - **JobId** *(string) --*

      An opaque string that identifies an Amazon S3 Glacier job.

    - **JobDescription** *(string) --*

      The job description provided when initiating the job.

    - **Action** *(string) --*

      The job type. This value is either ``ArchiveRetrieval`` , ``InventoryRetrieval`` , or
      ``Select`` .

    - **ArchiveId** *(string) --*

      The archive ID requested for a select job or archive retrieval. Otherwise, this field is null.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

    - **CreationDate** *(string) --*

      The UTC date when the job was created. This value is a string representation of ISO 8601 date
      format, for example ``"2012-03-20T17:03:43.221Z"`` .

    - **Completed** *(boolean) --*

      The job status. When a job is completed, you get the job's output using Get Job Output (GET
      output).

    - **StatusCode** *(string) --*

      The status code can be ``InProgress`` , ``Succeeded`` , or ``Failed`` , and indicates the
      status of the job.

    - **StatusMessage** *(string) --*

      A friendly message that describes the job status.

    - **ArchiveSizeInBytes** *(integer) --*

      For an archive retrieval job, this value is the size in bytes of the archive being requested
      for download. For an inventory retrieval or select job, this value is null.

    - **InventorySizeInBytes** *(integer) --*

      For an inventory retrieval job, this value is the size in bytes of the inventory requested
      for download. For an archive retrieval or select job, this value is null.

    - **SNSTopic** *(string) --*

      An Amazon SNS topic that receives notification.

    - **CompletionDate** *(string) --*

      The UTC time that the job request completed. While the job is in progress, the value is null.

    - **SHA256TreeHash** *(string) --*

      For an archive retrieval job, this value is the checksum of the archive. Otherwise, this
      value is null.

      The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob**
      request for an archive specified a tree-hash aligned range, then this field returns a value.

      If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash value.

      This field is null for the following:

      * Archive retrieval jobs that specify a range that is not tree-hash aligned

      * Archival jobs that specify a range that is equal to the whole archive, when the job status
      is ``InProgress``

      * Inventory jobs

      * Select jobs

    - **ArchiveSHA256TreeHash** *(string) --*

      The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval
      or select jobs, this field is null.

    - **RetrievalByteRange** *(string) --*

      The retrieved byte range for archive retrieval jobs in the form *StartByteValue*
      -*EndByteValue* . If no range was specified in the archive retrieval, then the whole archive
      is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals the size of
      the archive minus 1. For inventory retrieval or select jobs, this field is null.

    - **Tier** *(string) --*

      The tier to use for a select or an archive retrieval. Valid values are ``Expedited`` ,
      ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

    - **InventoryRetrievalParameters** *(dict) --*

      Parameters used for range inventory retrieval.

      - **Format** *(string) --*

        The output format for the vault inventory list, which is set by the **InitiateJob** request
        when initiating a job to retrieve a vault inventory. Valid values are ``CSV`` and ``JSON`` .

      - **StartDate** *(string) --*

        The start of the date range in Universal Coordinated Time (UTC) for vault inventory
        retrieval that includes archives created on or after this date. This value should be a
        string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

      - **EndDate** *(string) --*

        The end of the date range in UTC for vault inventory retrieval that includes archives
        created before this date. This value should be a string in the ISO 8601 date format, for
        example ``2013-03-20T17:03:43Z`` .

      - **Limit** *(string) --*

        The maximum number of inventory items returned per vault inventory retrieval request. This
        limit is set when initiating the job with the a **InitiateJob** request.

      - **Marker** *(string) --*

        An opaque string that represents where to continue pagination of the vault inventory
        retrieval results. You use the marker in a new **InitiateJob** request to obtain additional
        inventory items. If there are no more inventory items, this value is ``null`` . For more
        information, see `Range Inventory Retrieval
        <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__
        .

    - **JobOutputPath** *(string) --*

      Contains the job output location.

    - **SelectParameters** *(dict) --*

      Contains the parameters used for a select.

      - **InputSerialization** *(dict) --*

        Describes the serialization format of the object.

        - **csv** *(dict) --*

          Describes the serialization of a CSV-encoded object.

          - **FileHeaderInfo** *(string) --*

            Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use``
            .

          - **Comments** *(string) --*

            A single character used to indicate that a row should be ignored when the character is
            present at the start of that row.

          - **QuoteEscapeCharacter** *(string) --*

            A single character used for escaping the quotation-mark character inside an already
            escaped value.

          - **RecordDelimiter** *(string) --*

            A value used to separate individual records from each other.

          - **FieldDelimiter** *(string) --*

            A value used to separate individual fields from each other within a record.

          - **QuoteCharacter** *(string) --*

            A value used as an escape character where the field delimiter is part of the value.

      - **ExpressionType** *(string) --*

        The type of the provided expression, for example ``SQL`` .

      - **Expression** *(string) --*

        The expression that is used to select the object.

      - **OutputSerialization** *(dict) --*

        Describes how the results of the select job are serialized.

        - **csv** *(dict) --*

          Describes the serialization of CSV-encoded query results.

          - **QuoteFields** *(string) --*

            A value that indicates whether all output fields should be contained within quotation
            marks.

          - **QuoteEscapeCharacter** *(string) --*

            A single character used for escaping the quotation-mark character inside an already
            escaped value.

          - **RecordDelimiter** *(string) --*

            A value used to separate individual records from each other.

          - **FieldDelimiter** *(string) --*

            A value used to separate individual fields from each other within a record.

          - **QuoteCharacter** *(string) --*

            A value used as an escape character where the field delimiter is part of the value.

    - **OutputLocation** *(dict) --*

      Contains the location where the data from the select job is stored.

      - **S3** *(dict) --*

        Describes an S3 location that will receive the results of the job request.

        - **BucketName** *(string) --*

          The name of the Amazon S3 bucket where the job results are stored.

        - **Prefix** *(string) --*

          The prefix that is prepended to the results for this request.

        - **Encryption** *(dict) --*

          Contains information about the encryption used to store the job results in Amazon S3.

          - **EncryptionType** *(string) --*

            The server-side encryption algorithm used when storing job results in Amazon S3, for
            example ``AES256`` or ``aws:kms`` .

          - **KMSKeyId** *(string) --*

            The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object
            protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature
            Version 4.

          - **KMSContext** *(string) --*

            Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the
            encryption context for the job results.

        - **CannedACL** *(string) --*

          The canned access control list (ACL) to apply to the job results.

        - **AccessControlList** *(list) --*

          A list of grants that control access to the staged results.

          - *(dict) --*

            Contains information about a grant.

            - **Grantee** *(dict) --*

              The grantee.

              - **Type** *(string) --*

                Type of grantee

              - **DisplayName** *(string) --*

                Screen name of the grantee.

              - **URI** *(string) --*

                URI of the grantee group.

              - **ID** *(string) --*

                The canonical user ID of the grantee.

              - **EmailAddress** *(string) --*

                Email address of the grantee.

            - **Permission** *(string) --*

              Specifies the permission given to the grantee.

        - **Tagging** *(dict) --*

          The tag-set that is applied to the job results.

          - *(string) --*

            - *(string) --*

        - **UserMetadata** *(dict) --*

          A map of metadata to store with the job results in Amazon S3.

          - *(string) --*

            - *(string) --*

        - **StorageClass** *(string) --*

          The storage class used to store the job results.
    """


_ClientDescribeVaultResponseTypeDef = TypedDict(
    "_ClientDescribeVaultResponseTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
    },
    total=False,
)


class ClientDescribeVaultResponseTypeDef(_ClientDescribeVaultResponseTypeDef):
    """
    Type definition for `ClientDescribeVault` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault.

    - **VaultName** *(string) --*

      The name of the vault.

    - **CreationDate** *(string) --*

      The Universal Coordinated Time (UTC) date when the vault was created. This value should be a
      string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

    - **LastInventoryDate** *(string) --*

      The Universal Coordinated Time (UTC) date when Amazon S3 Glacier completed the last vault
      inventory. This value should be a string in the ISO 8601 date format, for example
      ``2012-03-20T17:03:43.221Z`` .

    - **NumberOfArchives** *(integer) --*

      The number of archives in the vault as of the last inventory date. This field will return
      ``null`` if an inventory has not yet run on the vault, for example if you just created the
      vault.

    - **SizeInBytes** *(integer) --*

      Total size, in bytes, of the archives in the vault as of the last inventory date. This field
      will return null if an inventory has not yet run on the vault, for example if you just
      created the vault.
    """


_ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef = TypedDict(
    "_ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef",
    {"Strategy": str, "BytesPerHour": int},
    total=False,
)


class ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef(
    _ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef
):
    """
    Type definition for `ClientGetDataRetrievalPolicyResponsePolicy` `Rules`

    Data retrieval policy rule.

    - **Strategy** *(string) --*

      The type of data retrieval policy to set.

      Valid values: BytesPerHour|FreeTier|None

    - **BytesPerHour** *(integer) --*

      The maximum number of bytes that can be retrieved in an hour.

      This field is required only if the value of the Strategy field is ``BytesPerHour`` .
      Your PUT operation will be rejected if the Strategy field is not set to
      ``BytesPerHour`` and you set this field.
    """


_ClientGetDataRetrievalPolicyResponsePolicyTypeDef = TypedDict(
    "_ClientGetDataRetrievalPolicyResponsePolicyTypeDef",
    {"Rules": List[ClientGetDataRetrievalPolicyResponsePolicyRulesTypeDef]},
    total=False,
)


class ClientGetDataRetrievalPolicyResponsePolicyTypeDef(
    _ClientGetDataRetrievalPolicyResponsePolicyTypeDef
):
    """
    Type definition for `ClientGetDataRetrievalPolicyResponse` `Policy`

    Contains the returned data retrieval policy in JSON format.

    - **Rules** *(list) --*

      The policy rule. Although this is a list type, currently there must be only one rule, which
      contains a Strategy field and optionally a BytesPerHour field.

      - *(dict) --*

        Data retrieval policy rule.

        - **Strategy** *(string) --*

          The type of data retrieval policy to set.

          Valid values: BytesPerHour|FreeTier|None

        - **BytesPerHour** *(integer) --*

          The maximum number of bytes that can be retrieved in an hour.

          This field is required only if the value of the Strategy field is ``BytesPerHour`` .
          Your PUT operation will be rejected if the Strategy field is not set to
          ``BytesPerHour`` and you set this field.
    """


_ClientGetDataRetrievalPolicyResponseTypeDef = TypedDict(
    "_ClientGetDataRetrievalPolicyResponseTypeDef",
    {"Policy": ClientGetDataRetrievalPolicyResponsePolicyTypeDef},
    total=False,
)


class ClientGetDataRetrievalPolicyResponseTypeDef(
    _ClientGetDataRetrievalPolicyResponseTypeDef
):
    """
    Type definition for `ClientGetDataRetrievalPolicy` `Response`

    Contains the Amazon S3 Glacier response to the ``GetDataRetrievalPolicy`` request.

    - **Policy** *(dict) --*

      Contains the returned data retrieval policy in JSON format.

      - **Rules** *(list) --*

        The policy rule. Although this is a list type, currently there must be only one rule, which
        contains a Strategy field and optionally a BytesPerHour field.

        - *(dict) --*

          Data retrieval policy rule.

          - **Strategy** *(string) --*

            The type of data retrieval policy to set.

            Valid values: BytesPerHour|FreeTier|None

          - **BytesPerHour** *(integer) --*

            The maximum number of bytes that can be retrieved in an hour.

            This field is required only if the value of the Strategy field is ``BytesPerHour`` .
            Your PUT operation will be rejected if the Strategy field is not set to
            ``BytesPerHour`` and you set this field.
    """


_ClientGetJobOutputResponseTypeDef = TypedDict(
    "_ClientGetJobOutputResponseTypeDef",
    {
        "checksum": str,
        "status": int,
        "contentRange": str,
        "acceptRanges": str,
        "contentType": str,
        "archiveDescription": str,
    },
    total=False,
)


class ClientGetJobOutputResponseTypeDef(_ClientGetJobOutputResponseTypeDef):
    """
    Type definition for `ClientGetJobOutput` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **body** (:class:`.StreamingBody`) --

      The job data, either archive data or inventory data.

    - **checksum** *(string) --*

      The checksum of the data in the response. This header is returned only when retrieving the
      output for an archive retrieval job. Furthermore, this header appears only under the
      following conditions:

      * You get the entire range of the archive.

      * You request a range to return of the archive that starts and ends on a multiple of 1 MB.
      For example, if you have an 3.1 MB archive and you specify a range to return that starts at 1
      MB and ends at 2 MB, then the x-amz-sha256-tree-hash is returned as a response header.

      * You request a range of the archive to return that starts on a multiple of 1 MB and goes to
      the end of the archive. For example, if you have a 3.1 MB archive and you specify a range
      that starts at 2 MB and ends at 3.1 MB (the end of the archive), then the
      x-amz-sha256-tree-hash is returned as a response header.

    - **status** *(integer) --*

      The HTTP response code for a job output request. The value depends on whether a range was
      specified in the request.

    - **contentRange** *(string) --*

      The range of bytes returned by Amazon S3 Glacier. If only partial output is downloaded, the
      response provides the range of bytes Amazon S3 Glacier returned. For example, bytes
      0-1048575/8388608 returns the first 1 MB from 8 MB.

    - **acceptRanges** *(string) --*

      Indicates the range units accepted. For more information, see `RFC2616
      <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`__ .

    - **contentType** *(string) --*

      The Content-Type depends on whether the job output is an archive or a vault inventory. For
      archive data, the Content-Type is application/octet-stream. For vault inventory, if you
      requested CSV format when you initiated the job, the Content-Type is text/csv. Otherwise, by
      default, vault inventory is returned as JSON, and the Content-Type is application/json.

    - **archiveDescription** *(string) --*

      The description of an archive.
    """


_ClientGetVaultAccessPolicyResponsepolicyTypeDef = TypedDict(
    "_ClientGetVaultAccessPolicyResponsepolicyTypeDef", {"Policy": str}, total=False
)


class ClientGetVaultAccessPolicyResponsepolicyTypeDef(
    _ClientGetVaultAccessPolicyResponsepolicyTypeDef
):
    """
    Type definition for `ClientGetVaultAccessPolicyResponse` `policy`

    Contains the returned vault access policy as a JSON string.

    - **Policy** *(string) --*

      The vault access policy.
    """


_ClientGetVaultAccessPolicyResponseTypeDef = TypedDict(
    "_ClientGetVaultAccessPolicyResponseTypeDef",
    {"policy": ClientGetVaultAccessPolicyResponsepolicyTypeDef},
    total=False,
)


class ClientGetVaultAccessPolicyResponseTypeDef(
    _ClientGetVaultAccessPolicyResponseTypeDef
):
    """
    Type definition for `ClientGetVaultAccessPolicy` `Response`

    Output for GetVaultAccessPolicy.

    - **policy** *(dict) --*

      Contains the returned vault access policy as a JSON string.

      - **Policy** *(string) --*

        The vault access policy.
    """


_ClientGetVaultLockResponseTypeDef = TypedDict(
    "_ClientGetVaultLockResponseTypeDef",
    {"Policy": str, "State": str, "ExpirationDate": str, "CreationDate": str},
    total=False,
)


class ClientGetVaultLockResponseTypeDef(_ClientGetVaultLockResponseTypeDef):
    """
    Type definition for `ClientGetVaultLock` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **Policy** *(string) --*

      The vault lock policy as a JSON string, which uses "\\" as an escape character.

    - **State** *(string) --*

      The state of the vault lock. ``InProgress`` or ``Locked`` .

    - **ExpirationDate** *(string) --*

      The UTC date and time at which the lock ID expires. This value can be ``null`` if the vault
      lock is in a ``Locked`` state.

    - **CreationDate** *(string) --*

      The UTC date and time at which the vault lock was put into the ``InProgress`` state.
    """


_ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef = TypedDict(
    "_ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)


class ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef(
    _ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef
):
    """
    Type definition for `ClientGetVaultNotificationsResponse` `vaultNotificationConfig`

    Returns the notification configuration set on the vault.

    - **SNSTopic** *(string) --*

      The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).

    - **Events** *(list) --*

      A list of one or more events for which Amazon S3 Glacier will send a notification to the
      specified Amazon SNS topic.

      - *(string) --*
    """


_ClientGetVaultNotificationsResponseTypeDef = TypedDict(
    "_ClientGetVaultNotificationsResponseTypeDef",
    {
        "vaultNotificationConfig": ClientGetVaultNotificationsResponsevaultNotificationConfigTypeDef
    },
    total=False,
)


class ClientGetVaultNotificationsResponseTypeDef(
    _ClientGetVaultNotificationsResponseTypeDef
):
    """
    Type definition for `ClientGetVaultNotifications` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **vaultNotificationConfig** *(dict) --*

      Returns the notification configuration set on the vault.

      - **SNSTopic** *(string) --*

        The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).

      - **Events** *(list) --*

        A list of one or more events for which Amazon S3 Glacier will send a notification to the
        specified Amazon SNS topic.

        - *(string) --*
    """


_ClientInitiateJobResponseTypeDef = TypedDict(
    "_ClientInitiateJobResponseTypeDef",
    {"location": str, "jobId": str, "jobOutputPath": str},
    total=False,
)


class ClientInitiateJobResponseTypeDef(_ClientInitiateJobResponseTypeDef):
    """
    Type definition for `ClientInitiateJob` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **location** *(string) --*

      The relative URI path of the job.

    - **jobId** *(string) --*

      The ID of the job.

    - **jobOutputPath** *(string) --*

      The path to the location of where the select results are stored.
    """


_ClientInitiateJobjobParametersInventoryRetrievalParametersTypeDef = TypedDict(
    "_ClientInitiateJobjobParametersInventoryRetrievalParametersTypeDef",
    {"StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)


class ClientInitiateJobjobParametersInventoryRetrievalParametersTypeDef(
    _ClientInitiateJobjobParametersInventoryRetrievalParametersTypeDef
):
    """
    Type definition for `ClientInitiateJobjobParameters` `InventoryRetrievalParameters`

    Input parameters used for range inventory retrieval.

    - **StartDate** *(string) --*

      The start of the date range in UTC for vault inventory retrieval that includes archives
      created on or after this date. This value should be a string in the ISO 8601 date format, for
      example ``2013-03-20T17:03:43Z`` .

    - **EndDate** *(string) --*

      The end of the date range in UTC for vault inventory retrieval that includes archives created
      before this date. This value should be a string in the ISO 8601 date format, for example
      ``2013-03-20T17:03:43Z`` .

    - **Limit** *(string) --*

      Specifies the maximum number of inventory items returned per vault inventory retrieval
      request. Valid values are greater than or equal to 1.

    - **Marker** *(string) --*

      An opaque string that represents where to continue pagination of the vault inventory
      retrieval results. You use the marker in a new **InitiateJob** request to obtain additional
      inventory items. If there are no more inventory items, this value is ``null`` .
    """


_RequiredClientInitiateJobjobParametersOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_RequiredClientInitiateJobjobParametersOutputLocationS3AccessControlListGranteeTypeDef",
    {"Type": str},
)
_OptionalClientInitiateJobjobParametersOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_OptionalClientInitiateJobjobParametersOutputLocationS3AccessControlListGranteeTypeDef",
    {"DisplayName": str, "URI": str, "ID": str, "EmailAddress": str},
    total=False,
)


class ClientInitiateJobjobParametersOutputLocationS3AccessControlListGranteeTypeDef(
    _RequiredClientInitiateJobjobParametersOutputLocationS3AccessControlListGranteeTypeDef,
    _OptionalClientInitiateJobjobParametersOutputLocationS3AccessControlListGranteeTypeDef,
):
    """
    Type definition for `ClientInitiateJobjobParametersOutputLocationS3AccessControlList` `Grantee`

    The grantee.

    - **Type** *(string) --* **[REQUIRED]**

      Type of grantee

    - **DisplayName** *(string) --*

      Screen name of the grantee.

    - **URI** *(string) --*

      URI of the grantee group.

    - **ID** *(string) --*

      The canonical user ID of the grantee.

    - **EmailAddress** *(string) --*

      Email address of the grantee.
    """


_ClientInitiateJobjobParametersOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ClientInitiateJobjobParametersOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientInitiateJobjobParametersOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientInitiateJobjobParametersOutputLocationS3AccessControlListTypeDef(
    _ClientInitiateJobjobParametersOutputLocationS3AccessControlListTypeDef
):
    """
    Type definition for `ClientInitiateJobjobParametersOutputLocationS3` `AccessControlList`

    Contains information about a grant.

    - **Grantee** *(dict) --*

      The grantee.

      - **Type** *(string) --* **[REQUIRED]**

        Type of grantee

      - **DisplayName** *(string) --*

        Screen name of the grantee.

      - **URI** *(string) --*

        URI of the grantee group.

      - **ID** *(string) --*

        The canonical user ID of the grantee.

      - **EmailAddress** *(string) --*

        Email address of the grantee.

    - **Permission** *(string) --*

      Specifies the permission given to the grantee.
    """


_ClientInitiateJobjobParametersOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ClientInitiateJobjobParametersOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": str, "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ClientInitiateJobjobParametersOutputLocationS3EncryptionTypeDef(
    _ClientInitiateJobjobParametersOutputLocationS3EncryptionTypeDef
):
    """
    Type definition for `ClientInitiateJobjobParametersOutputLocationS3` `Encryption`

    Contains information about the encryption used to store the job results in Amazon S3.

    - **EncryptionType** *(string) --*

      The server-side encryption algorithm used when storing job results in Amazon S3, for
      example ``AES256`` or ``aws:kms`` .

    - **KMSKeyId** *(string) --*

      The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object
      protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature
      Version 4.

    - **KMSContext** *(string) --*

      Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the
      encryption context for the job results.
    """


_ClientInitiateJobjobParametersOutputLocationS3TypeDef = TypedDict(
    "_ClientInitiateJobjobParametersOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientInitiateJobjobParametersOutputLocationS3EncryptionTypeDef,
        "CannedACL": str,
        "AccessControlList": List[
            ClientInitiateJobjobParametersOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": str,
    },
    total=False,
)


class ClientInitiateJobjobParametersOutputLocationS3TypeDef(
    _ClientInitiateJobjobParametersOutputLocationS3TypeDef
):
    """
    Type definition for `ClientInitiateJobjobParametersOutputLocation` `S3`

    Describes an S3 location that will receive the results of the job request.

    - **BucketName** *(string) --*

      The name of the Amazon S3 bucket where the job results are stored.

    - **Prefix** *(string) --*

      The prefix that is prepended to the results for this request.

    - **Encryption** *(dict) --*

      Contains information about the encryption used to store the job results in Amazon S3.

      - **EncryptionType** *(string) --*

        The server-side encryption algorithm used when storing job results in Amazon S3, for
        example ``AES256`` or ``aws:kms`` .

      - **KMSKeyId** *(string) --*

        The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object
        protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature
        Version 4.

      - **KMSContext** *(string) --*

        Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the
        encryption context for the job results.

    - **CannedACL** *(string) --*

      The canned access control list (ACL) to apply to the job results.

    - **AccessControlList** *(list) --*

      A list of grants that control access to the staged results.

      - *(dict) --*

        Contains information about a grant.

        - **Grantee** *(dict) --*

          The grantee.

          - **Type** *(string) --* **[REQUIRED]**

            Type of grantee

          - **DisplayName** *(string) --*

            Screen name of the grantee.

          - **URI** *(string) --*

            URI of the grantee group.

          - **ID** *(string) --*

            The canonical user ID of the grantee.

          - **EmailAddress** *(string) --*

            Email address of the grantee.

        - **Permission** *(string) --*

          Specifies the permission given to the grantee.

    - **Tagging** *(dict) --*

      The tag-set that is applied to the job results.

      - *(string) --*

        - *(string) --*

    - **UserMetadata** *(dict) --*

      A map of metadata to store with the job results in Amazon S3.

      - *(string) --*

        - *(string) --*

    - **StorageClass** *(string) --*

      The storage class used to store the job results.
    """


_ClientInitiateJobjobParametersOutputLocationTypeDef = TypedDict(
    "_ClientInitiateJobjobParametersOutputLocationTypeDef",
    {"S3": ClientInitiateJobjobParametersOutputLocationS3TypeDef},
    total=False,
)


class ClientInitiateJobjobParametersOutputLocationTypeDef(
    _ClientInitiateJobjobParametersOutputLocationTypeDef
):
    """
    Type definition for `ClientInitiateJobjobParameters` `OutputLocation`

    Contains information about the location where the select job results are stored.

    - **S3** *(dict) --*

      Describes an S3 location that will receive the results of the job request.

      - **BucketName** *(string) --*

        The name of the Amazon S3 bucket where the job results are stored.

      - **Prefix** *(string) --*

        The prefix that is prepended to the results for this request.

      - **Encryption** *(dict) --*

        Contains information about the encryption used to store the job results in Amazon S3.

        - **EncryptionType** *(string) --*

          The server-side encryption algorithm used when storing job results in Amazon S3, for
          example ``AES256`` or ``aws:kms`` .

        - **KMSKeyId** *(string) --*

          The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object
          protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature
          Version 4.

        - **KMSContext** *(string) --*

          Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the
          encryption context for the job results.

      - **CannedACL** *(string) --*

        The canned access control list (ACL) to apply to the job results.

      - **AccessControlList** *(list) --*

        A list of grants that control access to the staged results.

        - *(dict) --*

          Contains information about a grant.

          - **Grantee** *(dict) --*

            The grantee.

            - **Type** *(string) --* **[REQUIRED]**

              Type of grantee

            - **DisplayName** *(string) --*

              Screen name of the grantee.

            - **URI** *(string) --*

              URI of the grantee group.

            - **ID** *(string) --*

              The canonical user ID of the grantee.

            - **EmailAddress** *(string) --*

              Email address of the grantee.

          - **Permission** *(string) --*

            Specifies the permission given to the grantee.

      - **Tagging** *(dict) --*

        The tag-set that is applied to the job results.

        - *(string) --*

          - *(string) --*

      - **UserMetadata** *(dict) --*

        A map of metadata to store with the job results in Amazon S3.

        - *(string) --*

          - *(string) --*

      - **StorageClass** *(string) --*

        The storage class used to store the job results.
    """


_ClientInitiateJobjobParametersSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "_ClientInitiateJobjobParametersSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": str,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientInitiateJobjobParametersSelectParametersInputSerializationcsvTypeDef(
    _ClientInitiateJobjobParametersSelectParametersInputSerializationcsvTypeDef
):
    """
    Type definition for `ClientInitiateJobjobParametersSelectParametersInputSerialization` `csv`

    Describes the serialization of a CSV-encoded object.

    - **FileHeaderInfo** *(string) --*

      Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use`` .

    - **Comments** *(string) --*

      A single character used to indicate that a row should be ignored when the character is
      present at the start of that row.

    - **QuoteEscapeCharacter** *(string) --*

      A single character used for escaping the quotation-mark character inside an already
      escaped value.

    - **RecordDelimiter** *(string) --*

      A value used to separate individual records from each other.

    - **FieldDelimiter** *(string) --*

      A value used to separate individual fields from each other within a record.

    - **QuoteCharacter** *(string) --*

      A value used as an escape character where the field delimiter is part of the value.
    """


_ClientInitiateJobjobParametersSelectParametersInputSerializationTypeDef = TypedDict(
    "_ClientInitiateJobjobParametersSelectParametersInputSerializationTypeDef",
    {"csv": ClientInitiateJobjobParametersSelectParametersInputSerializationcsvTypeDef},
    total=False,
)


class ClientInitiateJobjobParametersSelectParametersInputSerializationTypeDef(
    _ClientInitiateJobjobParametersSelectParametersInputSerializationTypeDef
):
    """
    Type definition for `ClientInitiateJobjobParametersSelectParameters` `InputSerialization`

    Describes the serialization format of the object.

    - **csv** *(dict) --*

      Describes the serialization of a CSV-encoded object.

      - **FileHeaderInfo** *(string) --*

        Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use`` .

      - **Comments** *(string) --*

        A single character used to indicate that a row should be ignored when the character is
        present at the start of that row.

      - **QuoteEscapeCharacter** *(string) --*

        A single character used for escaping the quotation-mark character inside an already
        escaped value.

      - **RecordDelimiter** *(string) --*

        A value used to separate individual records from each other.

      - **FieldDelimiter** *(string) --*

        A value used to separate individual fields from each other within a record.

      - **QuoteCharacter** *(string) --*

        A value used as an escape character where the field delimiter is part of the value.
    """


_ClientInitiateJobjobParametersSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "_ClientInitiateJobjobParametersSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientInitiateJobjobParametersSelectParametersOutputSerializationcsvTypeDef(
    _ClientInitiateJobjobParametersSelectParametersOutputSerializationcsvTypeDef
):
    """
    Type definition for `ClientInitiateJobjobParametersSelectParametersOutputSerialization` `csv`

    Describes the serialization of CSV-encoded query results.

    - **QuoteFields** *(string) --*

      A value that indicates whether all output fields should be contained within quotation
      marks.

    - **QuoteEscapeCharacter** *(string) --*

      A single character used for escaping the quotation-mark character inside an already
      escaped value.

    - **RecordDelimiter** *(string) --*

      A value used to separate individual records from each other.

    - **FieldDelimiter** *(string) --*

      A value used to separate individual fields from each other within a record.

    - **QuoteCharacter** *(string) --*

      A value used as an escape character where the field delimiter is part of the value.
    """


_ClientInitiateJobjobParametersSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ClientInitiateJobjobParametersSelectParametersOutputSerializationTypeDef",
    {
        "csv": ClientInitiateJobjobParametersSelectParametersOutputSerializationcsvTypeDef
    },
    total=False,
)


class ClientInitiateJobjobParametersSelectParametersOutputSerializationTypeDef(
    _ClientInitiateJobjobParametersSelectParametersOutputSerializationTypeDef
):
    """
    Type definition for `ClientInitiateJobjobParametersSelectParameters` `OutputSerialization`

    Describes how the results of the select job are serialized.

    - **csv** *(dict) --*

      Describes the serialization of CSV-encoded query results.

      - **QuoteFields** *(string) --*

        A value that indicates whether all output fields should be contained within quotation
        marks.

      - **QuoteEscapeCharacter** *(string) --*

        A single character used for escaping the quotation-mark character inside an already
        escaped value.

      - **RecordDelimiter** *(string) --*

        A value used to separate individual records from each other.

      - **FieldDelimiter** *(string) --*

        A value used to separate individual fields from each other within a record.

      - **QuoteCharacter** *(string) --*

        A value used as an escape character where the field delimiter is part of the value.
    """


_ClientInitiateJobjobParametersSelectParametersTypeDef = TypedDict(
    "_ClientInitiateJobjobParametersSelectParametersTypeDef",
    {
        "InputSerialization": ClientInitiateJobjobParametersSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientInitiateJobjobParametersSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ClientInitiateJobjobParametersSelectParametersTypeDef(
    _ClientInitiateJobjobParametersSelectParametersTypeDef
):
    """
    Type definition for `ClientInitiateJobjobParameters` `SelectParameters`

    Contains the parameters that define a job.

    - **InputSerialization** *(dict) --*

      Describes the serialization format of the object.

      - **csv** *(dict) --*

        Describes the serialization of a CSV-encoded object.

        - **FileHeaderInfo** *(string) --*

          Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use`` .

        - **Comments** *(string) --*

          A single character used to indicate that a row should be ignored when the character is
          present at the start of that row.

        - **QuoteEscapeCharacter** *(string) --*

          A single character used for escaping the quotation-mark character inside an already
          escaped value.

        - **RecordDelimiter** *(string) --*

          A value used to separate individual records from each other.

        - **FieldDelimiter** *(string) --*

          A value used to separate individual fields from each other within a record.

        - **QuoteCharacter** *(string) --*

          A value used as an escape character where the field delimiter is part of the value.

    - **ExpressionType** *(string) --*

      The type of the provided expression, for example ``SQL`` .

    - **Expression** *(string) --*

      The expression that is used to select the object.

    - **OutputSerialization** *(dict) --*

      Describes how the results of the select job are serialized.

      - **csv** *(dict) --*

        Describes the serialization of CSV-encoded query results.

        - **QuoteFields** *(string) --*

          A value that indicates whether all output fields should be contained within quotation
          marks.

        - **QuoteEscapeCharacter** *(string) --*

          A single character used for escaping the quotation-mark character inside an already
          escaped value.

        - **RecordDelimiter** *(string) --*

          A value used to separate individual records from each other.

        - **FieldDelimiter** *(string) --*

          A value used to separate individual fields from each other within a record.

        - **QuoteCharacter** *(string) --*

          A value used as an escape character where the field delimiter is part of the value.
    """


_ClientInitiateJobjobParametersTypeDef = TypedDict(
    "_ClientInitiateJobjobParametersTypeDef",
    {
        "Format": str,
        "Type": str,
        "ArchiveId": str,
        "Description": str,
        "SNSTopic": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ClientInitiateJobjobParametersInventoryRetrievalParametersTypeDef,
        "SelectParameters": ClientInitiateJobjobParametersSelectParametersTypeDef,
        "OutputLocation": ClientInitiateJobjobParametersOutputLocationTypeDef,
    },
    total=False,
)


class ClientInitiateJobjobParametersTypeDef(_ClientInitiateJobjobParametersTypeDef):
    """
    Type definition for `ClientInitiateJob` `jobParameters`

    Provides options for specifying job information.

    - **Format** *(string) --*

      When initiating a job to retrieve a vault inventory, you can optionally add this parameter to
      your request to specify the output format. If you are initiating an inventory job and do not
      specify a Format field, JSON is the default format. Valid values are "CSV" and "JSON".

    - **Type** *(string) --*

      The job type. You can initiate a job to perform a select query on an archive, retrieve an
      archive, or get an inventory of a vault. Valid values are "select", "archive-retrieval" and
      "inventory-retrieval".

    - **ArchiveId** *(string) --*

      The ID of the archive that you want to retrieve. This field is required only if ``Type`` is set
      to ``select`` or ``archive-retrieval`` code>. An error occurs if you specify this request
      parameter for an inventory retrieval job request.

    - **Description** *(string) --*

      The optional description for the job. The description must be less than or equal to 1,024
      bytes. The allowable characters are 7-bit ASCII without control codes-specifically, ASCII
      values 32-126 decimal or 0x20-0x7E hexadecimal.

    - **SNSTopic** *(string) --*

      The Amazon SNS topic ARN to which Amazon S3 Glacier sends a notification when the job is
      completed and the output is ready for you to download. The specified topic publishes the
      notification to its subscribers. The SNS topic must exist.

    - **RetrievalByteRange** *(string) --*

      The byte range to retrieve for an archive retrieval. in the form "*StartByteValue*
      -*EndByteValue* " If not specified, the whole archive is retrieved. If specified, the byte
      range must be megabyte (1024*1024) aligned which means that *StartByteValue* must be divisible
      by 1 MB and *EndByteValue* plus 1 must be divisible by 1 MB or be the end of the archive
      specified as the archive byte size value minus 1. If RetrievalByteRange is not megabyte
      aligned, this operation returns a 400 response.

      An error occurs if you specify this field for an inventory retrieval job request.

    - **Tier** *(string) --*

      The tier to use for a select or an archive retrieval job. Valid values are ``Expedited`` ,
      ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

    - **InventoryRetrievalParameters** *(dict) --*

      Input parameters used for range inventory retrieval.

      - **StartDate** *(string) --*

        The start of the date range in UTC for vault inventory retrieval that includes archives
        created on or after this date. This value should be a string in the ISO 8601 date format, for
        example ``2013-03-20T17:03:43Z`` .

      - **EndDate** *(string) --*

        The end of the date range in UTC for vault inventory retrieval that includes archives created
        before this date. This value should be a string in the ISO 8601 date format, for example
        ``2013-03-20T17:03:43Z`` .

      - **Limit** *(string) --*

        Specifies the maximum number of inventory items returned per vault inventory retrieval
        request. Valid values are greater than or equal to 1.

      - **Marker** *(string) --*

        An opaque string that represents where to continue pagination of the vault inventory
        retrieval results. You use the marker in a new **InitiateJob** request to obtain additional
        inventory items. If there are no more inventory items, this value is ``null`` .

    - **SelectParameters** *(dict) --*

      Contains the parameters that define a job.

      - **InputSerialization** *(dict) --*

        Describes the serialization format of the object.

        - **csv** *(dict) --*

          Describes the serialization of a CSV-encoded object.

          - **FileHeaderInfo** *(string) --*

            Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use`` .

          - **Comments** *(string) --*

            A single character used to indicate that a row should be ignored when the character is
            present at the start of that row.

          - **QuoteEscapeCharacter** *(string) --*

            A single character used for escaping the quotation-mark character inside an already
            escaped value.

          - **RecordDelimiter** *(string) --*

            A value used to separate individual records from each other.

          - **FieldDelimiter** *(string) --*

            A value used to separate individual fields from each other within a record.

          - **QuoteCharacter** *(string) --*

            A value used as an escape character where the field delimiter is part of the value.

      - **ExpressionType** *(string) --*

        The type of the provided expression, for example ``SQL`` .

      - **Expression** *(string) --*

        The expression that is used to select the object.

      - **OutputSerialization** *(dict) --*

        Describes how the results of the select job are serialized.

        - **csv** *(dict) --*

          Describes the serialization of CSV-encoded query results.

          - **QuoteFields** *(string) --*

            A value that indicates whether all output fields should be contained within quotation
            marks.

          - **QuoteEscapeCharacter** *(string) --*

            A single character used for escaping the quotation-mark character inside an already
            escaped value.

          - **RecordDelimiter** *(string) --*

            A value used to separate individual records from each other.

          - **FieldDelimiter** *(string) --*

            A value used to separate individual fields from each other within a record.

          - **QuoteCharacter** *(string) --*

            A value used as an escape character where the field delimiter is part of the value.

    - **OutputLocation** *(dict) --*

      Contains information about the location where the select job results are stored.

      - **S3** *(dict) --*

        Describes an S3 location that will receive the results of the job request.

        - **BucketName** *(string) --*

          The name of the Amazon S3 bucket where the job results are stored.

        - **Prefix** *(string) --*

          The prefix that is prepended to the results for this request.

        - **Encryption** *(dict) --*

          Contains information about the encryption used to store the job results in Amazon S3.

          - **EncryptionType** *(string) --*

            The server-side encryption algorithm used when storing job results in Amazon S3, for
            example ``AES256`` or ``aws:kms`` .

          - **KMSKeyId** *(string) --*

            The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object
            protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature
            Version 4.

          - **KMSContext** *(string) --*

            Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the
            encryption context for the job results.

        - **CannedACL** *(string) --*

          The canned access control list (ACL) to apply to the job results.

        - **AccessControlList** *(list) --*

          A list of grants that control access to the staged results.

          - *(dict) --*

            Contains information about a grant.

            - **Grantee** *(dict) --*

              The grantee.

              - **Type** *(string) --* **[REQUIRED]**

                Type of grantee

              - **DisplayName** *(string) --*

                Screen name of the grantee.

              - **URI** *(string) --*

                URI of the grantee group.

              - **ID** *(string) --*

                The canonical user ID of the grantee.

              - **EmailAddress** *(string) --*

                Email address of the grantee.

            - **Permission** *(string) --*

              Specifies the permission given to the grantee.

        - **Tagging** *(dict) --*

          The tag-set that is applied to the job results.

          - *(string) --*

            - *(string) --*

        - **UserMetadata** *(dict) --*

          A map of metadata to store with the job results in Amazon S3.

          - *(string) --*

            - *(string) --*

        - **StorageClass** *(string) --*

          The storage class used to store the job results.
    """


_ClientInitiateMultipartUploadResponseTypeDef = TypedDict(
    "_ClientInitiateMultipartUploadResponseTypeDef",
    {"location": str, "uploadId": str},
    total=False,
)


class ClientInitiateMultipartUploadResponseTypeDef(
    _ClientInitiateMultipartUploadResponseTypeDef
):
    """
    Type definition for `ClientInitiateMultipartUpload` `Response`

    The Amazon S3 Glacier response to your request.

    - **location** *(string) --*

      The relative URI path of the multipart upload ID Amazon S3 Glacier created.

    - **uploadId** *(string) --*

      The ID of the multipart upload. This value is also included as part of the location.
    """


_ClientInitiateVaultLockResponseTypeDef = TypedDict(
    "_ClientInitiateVaultLockResponseTypeDef", {"lockId": str}, total=False
)


class ClientInitiateVaultLockResponseTypeDef(_ClientInitiateVaultLockResponseTypeDef):
    """
    Type definition for `ClientInitiateVaultLock` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **lockId** *(string) --*

      The lock ID, which is used to complete the vault locking process.
    """


_ClientInitiateVaultLockpolicyTypeDef = TypedDict(
    "_ClientInitiateVaultLockpolicyTypeDef", {"Policy": str}, total=False
)


class ClientInitiateVaultLockpolicyTypeDef(_ClientInitiateVaultLockpolicyTypeDef):
    """
    Type definition for `ClientInitiateVaultLock` `policy`

    The vault lock policy as a JSON string, which uses "\\" as an escape character.

    - **Policy** *(string) --*

      The vault lock policy.
    """


_ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef = TypedDict(
    "_ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)


class ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef(
    _ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobList` `InventoryRetrievalParameters`

    Parameters used for range inventory retrieval.

    - **Format** *(string) --*

      The output format for the vault inventory list, which is set by the **InitiateJob**
      request when initiating a job to retrieve a vault inventory. Valid values are ``CSV``
      and ``JSON`` .

    - **StartDate** *(string) --*

      The start of the date range in Universal Coordinated Time (UTC) for vault inventory
      retrieval that includes archives created on or after this date. This value should be a
      string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

    - **EndDate** *(string) --*

      The end of the date range in UTC for vault inventory retrieval that includes archives
      created before this date. This value should be a string in the ISO 8601 date format,
      for example ``2013-03-20T17:03:43Z`` .

    - **Limit** *(string) --*

      The maximum number of inventory items returned per vault inventory retrieval request.
      This limit is set when initiating the job with the a **InitiateJob** request.

    - **Marker** *(string) --*

      An opaque string that represents where to continue pagination of the vault inventory
      retrieval results. You use the marker in a new **InitiateJob** request to obtain
      additional inventory items. If there are no more inventory items, this value is
      ``null`` . For more information, see `Range Inventory Retrieval
      <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__
      .
    """


_ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    {"Type": str, "DisplayName": str, "URI": str, "ID": str, "EmailAddress": str},
    total=False,
)


class ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef(
    _ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobListOutputLocationS3AccessControlList` `Grantee`

    The grantee.

    - **Type** *(string) --*

      Type of grantee

    - **DisplayName** *(string) --*

      Screen name of the grantee.

    - **URI** *(string) --*

      URI of the grantee group.

    - **ID** *(string) --*

      The canonical user ID of the grantee.

    - **EmailAddress** *(string) --*

      Email address of the grantee.
    """


_ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientListJobsResponseJobListOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef(
    _ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobListOutputLocationS3` `AccessControlList`

    Contains information about a grant.

    - **Grantee** *(dict) --*

      The grantee.

      - **Type** *(string) --*

        Type of grantee

      - **DisplayName** *(string) --*

        Screen name of the grantee.

      - **URI** *(string) --*

        URI of the grantee group.

      - **ID** *(string) --*

        The canonical user ID of the grantee.

      - **EmailAddress** *(string) --*

        Email address of the grantee.

    - **Permission** *(string) --*

      Specifies the permission given to the grantee.
    """


_ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": str, "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef(
    _ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobListOutputLocationS3` `Encryption`

    Contains information about the encryption used to store the job results in Amazon S3.

    - **EncryptionType** *(string) --*

      The server-side encryption algorithm used when storing job results in Amazon S3,
      for example ``AES256`` or ``aws:kms`` .

    - **KMSKeyId** *(string) --*

      The AWS KMS key ID to use for object encryption. All GET and PUT requests for an
      object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or
      Signature Version 4.

    - **KMSContext** *(string) --*

      Optional. If the encryption type is ``aws:kms`` , you can use this value to specify
      the encryption context for the job results.
    """


_ClientListJobsResponseJobListOutputLocationS3TypeDef = TypedDict(
    "_ClientListJobsResponseJobListOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientListJobsResponseJobListOutputLocationS3EncryptionTypeDef,
        "CannedACL": str,
        "AccessControlList": List[
            ClientListJobsResponseJobListOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": str,
    },
    total=False,
)


class ClientListJobsResponseJobListOutputLocationS3TypeDef(
    _ClientListJobsResponseJobListOutputLocationS3TypeDef
):
    """
    Type definition for `ClientListJobsResponseJobListOutputLocation` `S3`

    Describes an S3 location that will receive the results of the job request.

    - **BucketName** *(string) --*

      The name of the Amazon S3 bucket where the job results are stored.

    - **Prefix** *(string) --*

      The prefix that is prepended to the results for this request.

    - **Encryption** *(dict) --*

      Contains information about the encryption used to store the job results in Amazon S3.

      - **EncryptionType** *(string) --*

        The server-side encryption algorithm used when storing job results in Amazon S3,
        for example ``AES256`` or ``aws:kms`` .

      - **KMSKeyId** *(string) --*

        The AWS KMS key ID to use for object encryption. All GET and PUT requests for an
        object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or
        Signature Version 4.

      - **KMSContext** *(string) --*

        Optional. If the encryption type is ``aws:kms`` , you can use this value to specify
        the encryption context for the job results.

    - **CannedACL** *(string) --*

      The canned access control list (ACL) to apply to the job results.

    - **AccessControlList** *(list) --*

      A list of grants that control access to the staged results.

      - *(dict) --*

        Contains information about a grant.

        - **Grantee** *(dict) --*

          The grantee.

          - **Type** *(string) --*

            Type of grantee

          - **DisplayName** *(string) --*

            Screen name of the grantee.

          - **URI** *(string) --*

            URI of the grantee group.

          - **ID** *(string) --*

            The canonical user ID of the grantee.

          - **EmailAddress** *(string) --*

            Email address of the grantee.

        - **Permission** *(string) --*

          Specifies the permission given to the grantee.

    - **Tagging** *(dict) --*

      The tag-set that is applied to the job results.

      - *(string) --*

        - *(string) --*

    - **UserMetadata** *(dict) --*

      A map of metadata to store with the job results in Amazon S3.

      - *(string) --*

        - *(string) --*

    - **StorageClass** *(string) --*

      The storage class used to store the job results.
    """


_ClientListJobsResponseJobListOutputLocationTypeDef = TypedDict(
    "_ClientListJobsResponseJobListOutputLocationTypeDef",
    {"S3": ClientListJobsResponseJobListOutputLocationS3TypeDef},
    total=False,
)


class ClientListJobsResponseJobListOutputLocationTypeDef(
    _ClientListJobsResponseJobListOutputLocationTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobList` `OutputLocation`

    Contains the location where the data from the select job is stored.

    - **S3** *(dict) --*

      Describes an S3 location that will receive the results of the job request.

      - **BucketName** *(string) --*

        The name of the Amazon S3 bucket where the job results are stored.

      - **Prefix** *(string) --*

        The prefix that is prepended to the results for this request.

      - **Encryption** *(dict) --*

        Contains information about the encryption used to store the job results in Amazon S3.

        - **EncryptionType** *(string) --*

          The server-side encryption algorithm used when storing job results in Amazon S3,
          for example ``AES256`` or ``aws:kms`` .

        - **KMSKeyId** *(string) --*

          The AWS KMS key ID to use for object encryption. All GET and PUT requests for an
          object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or
          Signature Version 4.

        - **KMSContext** *(string) --*

          Optional. If the encryption type is ``aws:kms`` , you can use this value to specify
          the encryption context for the job results.

      - **CannedACL** *(string) --*

        The canned access control list (ACL) to apply to the job results.

      - **AccessControlList** *(list) --*

        A list of grants that control access to the staged results.

        - *(dict) --*

          Contains information about a grant.

          - **Grantee** *(dict) --*

            The grantee.

            - **Type** *(string) --*

              Type of grantee

            - **DisplayName** *(string) --*

              Screen name of the grantee.

            - **URI** *(string) --*

              URI of the grantee group.

            - **ID** *(string) --*

              The canonical user ID of the grantee.

            - **EmailAddress** *(string) --*

              Email address of the grantee.

          - **Permission** *(string) --*

            Specifies the permission given to the grantee.

      - **Tagging** *(dict) --*

        The tag-set that is applied to the job results.

        - *(string) --*

          - *(string) --*

      - **UserMetadata** *(dict) --*

        A map of metadata to store with the job results in Amazon S3.

        - *(string) --*

          - *(string) --*

      - **StorageClass** *(string) --*

        The storage class used to store the job results.
    """


_ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "_ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": str,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef(
    _ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobListSelectParametersInputSerialization` `csv`

    Describes the serialization of a CSV-encoded object.

    - **FileHeaderInfo** *(string) --*

      Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and
      ``Use`` .

    - **Comments** *(string) --*

      A single character used to indicate that a row should be ignored when the character
      is present at the start of that row.

    - **QuoteEscapeCharacter** *(string) --*

      A single character used for escaping the quotation-mark character inside an already
      escaped value.

    - **RecordDelimiter** *(string) --*

      A value used to separate individual records from each other.

    - **FieldDelimiter** *(string) --*

      A value used to separate individual fields from each other within a record.

    - **QuoteCharacter** *(string) --*

      A value used as an escape character where the field delimiter is part of the value.
    """


_ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef = TypedDict(
    "_ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef",
    {"csv": ClientListJobsResponseJobListSelectParametersInputSerializationcsvTypeDef},
    total=False,
)


class ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef(
    _ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobListSelectParameters` `InputSerialization`

    Describes the serialization format of the object.

    - **csv** *(dict) --*

      Describes the serialization of a CSV-encoded object.

      - **FileHeaderInfo** *(string) --*

        Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and
        ``Use`` .

      - **Comments** *(string) --*

        A single character used to indicate that a row should be ignored when the character
        is present at the start of that row.

      - **QuoteEscapeCharacter** *(string) --*

        A single character used for escaping the quotation-mark character inside an already
        escaped value.

      - **RecordDelimiter** *(string) --*

        A value used to separate individual records from each other.

      - **FieldDelimiter** *(string) --*

        A value used to separate individual fields from each other within a record.

      - **QuoteCharacter** *(string) --*

        A value used as an escape character where the field delimiter is part of the value.
    """


_ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "_ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef(
    _ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobListSelectParametersOutputSerialization` `csv`

    Describes the serialization of CSV-encoded query results.

    - **QuoteFields** *(string) --*

      A value that indicates whether all output fields should be contained within
      quotation marks.

    - **QuoteEscapeCharacter** *(string) --*

      A single character used for escaping the quotation-mark character inside an already
      escaped value.

    - **RecordDelimiter** *(string) --*

      A value used to separate individual records from each other.

    - **FieldDelimiter** *(string) --*

      A value used to separate individual fields from each other within a record.

    - **QuoteCharacter** *(string) --*

      A value used as an escape character where the field delimiter is part of the value.
    """


_ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef",
    {"csv": ClientListJobsResponseJobListSelectParametersOutputSerializationcsvTypeDef},
    total=False,
)


class ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef(
    _ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobListSelectParameters` `OutputSerialization`

    Describes how the results of the select job are serialized.

    - **csv** *(dict) --*

      Describes the serialization of CSV-encoded query results.

      - **QuoteFields** *(string) --*

        A value that indicates whether all output fields should be contained within
        quotation marks.

      - **QuoteEscapeCharacter** *(string) --*

        A single character used for escaping the quotation-mark character inside an already
        escaped value.

      - **RecordDelimiter** *(string) --*

        A value used to separate individual records from each other.

      - **FieldDelimiter** *(string) --*

        A value used to separate individual fields from each other within a record.

      - **QuoteCharacter** *(string) --*

        A value used as an escape character where the field delimiter is part of the value.
    """


_ClientListJobsResponseJobListSelectParametersTypeDef = TypedDict(
    "_ClientListJobsResponseJobListSelectParametersTypeDef",
    {
        "InputSerialization": ClientListJobsResponseJobListSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientListJobsResponseJobListSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ClientListJobsResponseJobListSelectParametersTypeDef(
    _ClientListJobsResponseJobListSelectParametersTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobList` `SelectParameters`

    Contains the parameters used for a select.

    - **InputSerialization** *(dict) --*

      Describes the serialization format of the object.

      - **csv** *(dict) --*

        Describes the serialization of a CSV-encoded object.

        - **FileHeaderInfo** *(string) --*

          Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and
          ``Use`` .

        - **Comments** *(string) --*

          A single character used to indicate that a row should be ignored when the character
          is present at the start of that row.

        - **QuoteEscapeCharacter** *(string) --*

          A single character used for escaping the quotation-mark character inside an already
          escaped value.

        - **RecordDelimiter** *(string) --*

          A value used to separate individual records from each other.

        - **FieldDelimiter** *(string) --*

          A value used to separate individual fields from each other within a record.

        - **QuoteCharacter** *(string) --*

          A value used as an escape character where the field delimiter is part of the value.

    - **ExpressionType** *(string) --*

      The type of the provided expression, for example ``SQL`` .

    - **Expression** *(string) --*

      The expression that is used to select the object.

    - **OutputSerialization** *(dict) --*

      Describes how the results of the select job are serialized.

      - **csv** *(dict) --*

        Describes the serialization of CSV-encoded query results.

        - **QuoteFields** *(string) --*

          A value that indicates whether all output fields should be contained within
          quotation marks.

        - **QuoteEscapeCharacter** *(string) --*

          A single character used for escaping the quotation-mark character inside an already
          escaped value.

        - **RecordDelimiter** *(string) --*

          A value used to separate individual records from each other.

        - **FieldDelimiter** *(string) --*

          A value used to separate individual fields from each other within a record.

        - **QuoteCharacter** *(string) --*

          A value used as an escape character where the field delimiter is part of the value.
    """


_ClientListJobsResponseJobListTypeDef = TypedDict(
    "_ClientListJobsResponseJobListTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": str,
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": str,
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ClientListJobsResponseJobListInventoryRetrievalParametersTypeDef,
        "JobOutputPath": str,
        "SelectParameters": ClientListJobsResponseJobListSelectParametersTypeDef,
        "OutputLocation": ClientListJobsResponseJobListOutputLocationTypeDef,
    },
    total=False,
)


class ClientListJobsResponseJobListTypeDef(_ClientListJobsResponseJobListTypeDef):
    """
    Type definition for `ClientListJobsResponse` `JobList`

    Contains the description of an Amazon S3 Glacier job.

    - **JobId** *(string) --*

      An opaque string that identifies an Amazon S3 Glacier job.

    - **JobDescription** *(string) --*

      The job description provided when initiating the job.

    - **Action** *(string) --*

      The job type. This value is either ``ArchiveRetrieval`` , ``InventoryRetrieval`` , or
      ``Select`` .

    - **ArchiveId** *(string) --*

      The archive ID requested for a select job or archive retrieval. Otherwise, this field is
      null.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

    - **CreationDate** *(string) --*

      The UTC date when the job was created. This value is a string representation of ISO 8601
      date format, for example ``"2012-03-20T17:03:43.221Z"`` .

    - **Completed** *(boolean) --*

      The job status. When a job is completed, you get the job's output using Get Job Output
      (GET output).

    - **StatusCode** *(string) --*

      The status code can be ``InProgress`` , ``Succeeded`` , or ``Failed`` , and indicates the
      status of the job.

    - **StatusMessage** *(string) --*

      A friendly message that describes the job status.

    - **ArchiveSizeInBytes** *(integer) --*

      For an archive retrieval job, this value is the size in bytes of the archive being
      requested for download. For an inventory retrieval or select job, this value is null.

    - **InventorySizeInBytes** *(integer) --*

      For an inventory retrieval job, this value is the size in bytes of the inventory
      requested for download. For an archive retrieval or select job, this value is null.

    - **SNSTopic** *(string) --*

      An Amazon SNS topic that receives notification.

    - **CompletionDate** *(string) --*

      The UTC time that the job request completed. While the job is in progress, the value is
      null.

    - **SHA256TreeHash** *(string) --*

      For an archive retrieval job, this value is the checksum of the archive. Otherwise, this
      value is null.

      The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob**
      request for an archive specified a tree-hash aligned range, then this field returns a
      value.

      If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash
      value.

      This field is null for the following:

      * Archive retrieval jobs that specify a range that is not tree-hash aligned

      * Archival jobs that specify a range that is equal to the whole archive, when the job
      status is ``InProgress``

      * Inventory jobs

      * Select jobs

    - **ArchiveSHA256TreeHash** *(string) --*

      The SHA256 tree hash of the entire archive for an archive retrieval. For inventory
      retrieval or select jobs, this field is null.

    - **RetrievalByteRange** *(string) --*

      The retrieved byte range for archive retrieval jobs in the form *StartByteValue*
      -*EndByteValue* . If no range was specified in the archive retrieval, then the whole
      archive is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals
      the size of the archive minus 1. For inventory retrieval or select jobs, this field is
      null.

    - **Tier** *(string) --*

      The tier to use for a select or an archive retrieval. Valid values are ``Expedited`` ,
      ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

    - **InventoryRetrievalParameters** *(dict) --*

      Parameters used for range inventory retrieval.

      - **Format** *(string) --*

        The output format for the vault inventory list, which is set by the **InitiateJob**
        request when initiating a job to retrieve a vault inventory. Valid values are ``CSV``
        and ``JSON`` .

      - **StartDate** *(string) --*

        The start of the date range in Universal Coordinated Time (UTC) for vault inventory
        retrieval that includes archives created on or after this date. This value should be a
        string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

      - **EndDate** *(string) --*

        The end of the date range in UTC for vault inventory retrieval that includes archives
        created before this date. This value should be a string in the ISO 8601 date format,
        for example ``2013-03-20T17:03:43Z`` .

      - **Limit** *(string) --*

        The maximum number of inventory items returned per vault inventory retrieval request.
        This limit is set when initiating the job with the a **InitiateJob** request.

      - **Marker** *(string) --*

        An opaque string that represents where to continue pagination of the vault inventory
        retrieval results. You use the marker in a new **InitiateJob** request to obtain
        additional inventory items. If there are no more inventory items, this value is
        ``null`` . For more information, see `Range Inventory Retrieval
        <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__
        .

    - **JobOutputPath** *(string) --*

      Contains the job output location.

    - **SelectParameters** *(dict) --*

      Contains the parameters used for a select.

      - **InputSerialization** *(dict) --*

        Describes the serialization format of the object.

        - **csv** *(dict) --*

          Describes the serialization of a CSV-encoded object.

          - **FileHeaderInfo** *(string) --*

            Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and
            ``Use`` .

          - **Comments** *(string) --*

            A single character used to indicate that a row should be ignored when the character
            is present at the start of that row.

          - **QuoteEscapeCharacter** *(string) --*

            A single character used for escaping the quotation-mark character inside an already
            escaped value.

          - **RecordDelimiter** *(string) --*

            A value used to separate individual records from each other.

          - **FieldDelimiter** *(string) --*

            A value used to separate individual fields from each other within a record.

          - **QuoteCharacter** *(string) --*

            A value used as an escape character where the field delimiter is part of the value.

      - **ExpressionType** *(string) --*

        The type of the provided expression, for example ``SQL`` .

      - **Expression** *(string) --*

        The expression that is used to select the object.

      - **OutputSerialization** *(dict) --*

        Describes how the results of the select job are serialized.

        - **csv** *(dict) --*

          Describes the serialization of CSV-encoded query results.

          - **QuoteFields** *(string) --*

            A value that indicates whether all output fields should be contained within
            quotation marks.

          - **QuoteEscapeCharacter** *(string) --*

            A single character used for escaping the quotation-mark character inside an already
            escaped value.

          - **RecordDelimiter** *(string) --*

            A value used to separate individual records from each other.

          - **FieldDelimiter** *(string) --*

            A value used to separate individual fields from each other within a record.

          - **QuoteCharacter** *(string) --*

            A value used as an escape character where the field delimiter is part of the value.

    - **OutputLocation** *(dict) --*

      Contains the location where the data from the select job is stored.

      - **S3** *(dict) --*

        Describes an S3 location that will receive the results of the job request.

        - **BucketName** *(string) --*

          The name of the Amazon S3 bucket where the job results are stored.

        - **Prefix** *(string) --*

          The prefix that is prepended to the results for this request.

        - **Encryption** *(dict) --*

          Contains information about the encryption used to store the job results in Amazon S3.

          - **EncryptionType** *(string) --*

            The server-side encryption algorithm used when storing job results in Amazon S3,
            for example ``AES256`` or ``aws:kms`` .

          - **KMSKeyId** *(string) --*

            The AWS KMS key ID to use for object encryption. All GET and PUT requests for an
            object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or
            Signature Version 4.

          - **KMSContext** *(string) --*

            Optional. If the encryption type is ``aws:kms`` , you can use this value to specify
            the encryption context for the job results.

        - **CannedACL** *(string) --*

          The canned access control list (ACL) to apply to the job results.

        - **AccessControlList** *(list) --*

          A list of grants that control access to the staged results.

          - *(dict) --*

            Contains information about a grant.

            - **Grantee** *(dict) --*

              The grantee.

              - **Type** *(string) --*

                Type of grantee

              - **DisplayName** *(string) --*

                Screen name of the grantee.

              - **URI** *(string) --*

                URI of the grantee group.

              - **ID** *(string) --*

                The canonical user ID of the grantee.

              - **EmailAddress** *(string) --*

                Email address of the grantee.

            - **Permission** *(string) --*

              Specifies the permission given to the grantee.

        - **Tagging** *(dict) --*

          The tag-set that is applied to the job results.

          - *(string) --*

            - *(string) --*

        - **UserMetadata** *(dict) --*

          A map of metadata to store with the job results in Amazon S3.

          - *(string) --*

            - *(string) --*

        - **StorageClass** *(string) --*

          The storage class used to store the job results.
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"JobList": List[ClientListJobsResponseJobListTypeDef], "Marker": str},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    Type definition for `ClientListJobs` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **JobList** *(list) --*

      A list of job objects. Each job object contains metadata describing the job.

      - *(dict) --*

        Contains the description of an Amazon S3 Glacier job.

        - **JobId** *(string) --*

          An opaque string that identifies an Amazon S3 Glacier job.

        - **JobDescription** *(string) --*

          The job description provided when initiating the job.

        - **Action** *(string) --*

          The job type. This value is either ``ArchiveRetrieval`` , ``InventoryRetrieval`` , or
          ``Select`` .

        - **ArchiveId** *(string) --*

          The archive ID requested for a select job or archive retrieval. Otherwise, this field is
          null.

        - **VaultARN** *(string) --*

          The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

        - **CreationDate** *(string) --*

          The UTC date when the job was created. This value is a string representation of ISO 8601
          date format, for example ``"2012-03-20T17:03:43.221Z"`` .

        - **Completed** *(boolean) --*

          The job status. When a job is completed, you get the job's output using Get Job Output
          (GET output).

        - **StatusCode** *(string) --*

          The status code can be ``InProgress`` , ``Succeeded`` , or ``Failed`` , and indicates the
          status of the job.

        - **StatusMessage** *(string) --*

          A friendly message that describes the job status.

        - **ArchiveSizeInBytes** *(integer) --*

          For an archive retrieval job, this value is the size in bytes of the archive being
          requested for download. For an inventory retrieval or select job, this value is null.

        - **InventorySizeInBytes** *(integer) --*

          For an inventory retrieval job, this value is the size in bytes of the inventory
          requested for download. For an archive retrieval or select job, this value is null.

        - **SNSTopic** *(string) --*

          An Amazon SNS topic that receives notification.

        - **CompletionDate** *(string) --*

          The UTC time that the job request completed. While the job is in progress, the value is
          null.

        - **SHA256TreeHash** *(string) --*

          For an archive retrieval job, this value is the checksum of the archive. Otherwise, this
          value is null.

          The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob**
          request for an archive specified a tree-hash aligned range, then this field returns a
          value.

          If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash
          value.

          This field is null for the following:

          * Archive retrieval jobs that specify a range that is not tree-hash aligned

          * Archival jobs that specify a range that is equal to the whole archive, when the job
          status is ``InProgress``

          * Inventory jobs

          * Select jobs

        - **ArchiveSHA256TreeHash** *(string) --*

          The SHA256 tree hash of the entire archive for an archive retrieval. For inventory
          retrieval or select jobs, this field is null.

        - **RetrievalByteRange** *(string) --*

          The retrieved byte range for archive retrieval jobs in the form *StartByteValue*
          -*EndByteValue* . If no range was specified in the archive retrieval, then the whole
          archive is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals
          the size of the archive minus 1. For inventory retrieval or select jobs, this field is
          null.

        - **Tier** *(string) --*

          The tier to use for a select or an archive retrieval. Valid values are ``Expedited`` ,
          ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

        - **InventoryRetrievalParameters** *(dict) --*

          Parameters used for range inventory retrieval.

          - **Format** *(string) --*

            The output format for the vault inventory list, which is set by the **InitiateJob**
            request when initiating a job to retrieve a vault inventory. Valid values are ``CSV``
            and ``JSON`` .

          - **StartDate** *(string) --*

            The start of the date range in Universal Coordinated Time (UTC) for vault inventory
            retrieval that includes archives created on or after this date. This value should be a
            string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

          - **EndDate** *(string) --*

            The end of the date range in UTC for vault inventory retrieval that includes archives
            created before this date. This value should be a string in the ISO 8601 date format,
            for example ``2013-03-20T17:03:43Z`` .

          - **Limit** *(string) --*

            The maximum number of inventory items returned per vault inventory retrieval request.
            This limit is set when initiating the job with the a **InitiateJob** request.

          - **Marker** *(string) --*

            An opaque string that represents where to continue pagination of the vault inventory
            retrieval results. You use the marker in a new **InitiateJob** request to obtain
            additional inventory items. If there are no more inventory items, this value is
            ``null`` . For more information, see `Range Inventory Retrieval
            <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__
            .

        - **JobOutputPath** *(string) --*

          Contains the job output location.

        - **SelectParameters** *(dict) --*

          Contains the parameters used for a select.

          - **InputSerialization** *(dict) --*

            Describes the serialization format of the object.

            - **csv** *(dict) --*

              Describes the serialization of a CSV-encoded object.

              - **FileHeaderInfo** *(string) --*

                Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and
                ``Use`` .

              - **Comments** *(string) --*

                A single character used to indicate that a row should be ignored when the character
                is present at the start of that row.

              - **QuoteEscapeCharacter** *(string) --*

                A single character used for escaping the quotation-mark character inside an already
                escaped value.

              - **RecordDelimiter** *(string) --*

                A value used to separate individual records from each other.

              - **FieldDelimiter** *(string) --*

                A value used to separate individual fields from each other within a record.

              - **QuoteCharacter** *(string) --*

                A value used as an escape character where the field delimiter is part of the value.

          - **ExpressionType** *(string) --*

            The type of the provided expression, for example ``SQL`` .

          - **Expression** *(string) --*

            The expression that is used to select the object.

          - **OutputSerialization** *(dict) --*

            Describes how the results of the select job are serialized.

            - **csv** *(dict) --*

              Describes the serialization of CSV-encoded query results.

              - **QuoteFields** *(string) --*

                A value that indicates whether all output fields should be contained within
                quotation marks.

              - **QuoteEscapeCharacter** *(string) --*

                A single character used for escaping the quotation-mark character inside an already
                escaped value.

              - **RecordDelimiter** *(string) --*

                A value used to separate individual records from each other.

              - **FieldDelimiter** *(string) --*

                A value used to separate individual fields from each other within a record.

              - **QuoteCharacter** *(string) --*

                A value used as an escape character where the field delimiter is part of the value.

        - **OutputLocation** *(dict) --*

          Contains the location where the data from the select job is stored.

          - **S3** *(dict) --*

            Describes an S3 location that will receive the results of the job request.

            - **BucketName** *(string) --*

              The name of the Amazon S3 bucket where the job results are stored.

            - **Prefix** *(string) --*

              The prefix that is prepended to the results for this request.

            - **Encryption** *(dict) --*

              Contains information about the encryption used to store the job results in Amazon S3.

              - **EncryptionType** *(string) --*

                The server-side encryption algorithm used when storing job results in Amazon S3,
                for example ``AES256`` or ``aws:kms`` .

              - **KMSKeyId** *(string) --*

                The AWS KMS key ID to use for object encryption. All GET and PUT requests for an
                object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or
                Signature Version 4.

              - **KMSContext** *(string) --*

                Optional. If the encryption type is ``aws:kms`` , you can use this value to specify
                the encryption context for the job results.

            - **CannedACL** *(string) --*

              The canned access control list (ACL) to apply to the job results.

            - **AccessControlList** *(list) --*

              A list of grants that control access to the staged results.

              - *(dict) --*

                Contains information about a grant.

                - **Grantee** *(dict) --*

                  The grantee.

                  - **Type** *(string) --*

                    Type of grantee

                  - **DisplayName** *(string) --*

                    Screen name of the grantee.

                  - **URI** *(string) --*

                    URI of the grantee group.

                  - **ID** *(string) --*

                    The canonical user ID of the grantee.

                  - **EmailAddress** *(string) --*

                    Email address of the grantee.

                - **Permission** *(string) --*

                  Specifies the permission given to the grantee.

            - **Tagging** *(dict) --*

              The tag-set that is applied to the job results.

              - *(string) --*

                - *(string) --*

            - **UserMetadata** *(dict) --*

              A map of metadata to store with the job results in Amazon S3.

              - *(string) --*

                - *(string) --*

            - **StorageClass** *(string) --*

              The storage class used to store the job results.

    - **Marker** *(string) --*

      An opaque string used for pagination that specifies the job at which the listing of jobs
      should begin. You get the ``marker`` value from a previous List Jobs response. You only need
      to include the marker if you are continuing the pagination of the results started in a
      previous List Jobs request.
    """


_ClientListMultipartUploadsResponseUploadsListTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseUploadsListTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
    },
    total=False,
)


class ClientListMultipartUploadsResponseUploadsListTypeDef(
    _ClientListMultipartUploadsResponseUploadsListTypeDef
):
    """
    Type definition for `ClientListMultipartUploadsResponse` `UploadsList`

    A list of in-progress multipart uploads for a vault.

    - **MultipartUploadId** *(string) --*

      The ID of a multipart upload.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault that contains the archive.

    - **ArchiveDescription** *(string) --*

      The description of the archive that was specified in the Initiate Multipart Upload
      request.

    - **PartSizeInBytes** *(integer) --*

      The part size, in bytes, specified in the Initiate Multipart Upload request. This is the
      size of all the parts in the upload except the last part, which may be smaller than this
      size.

    - **CreationDate** *(string) --*

      The UTC time at which the multipart upload was initiated.
    """


_ClientListMultipartUploadsResponseTypeDef = TypedDict(
    "_ClientListMultipartUploadsResponseTypeDef",
    {
        "UploadsList": List[ClientListMultipartUploadsResponseUploadsListTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientListMultipartUploadsResponseTypeDef(
    _ClientListMultipartUploadsResponseTypeDef
):
    """
    Type definition for `ClientListMultipartUploads` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **UploadsList** *(list) --*

      A list of in-progress multipart uploads.

      - *(dict) --*

        A list of in-progress multipart uploads for a vault.

        - **MultipartUploadId** *(string) --*

          The ID of a multipart upload.

        - **VaultARN** *(string) --*

          The Amazon Resource Name (ARN) of the vault that contains the archive.

        - **ArchiveDescription** *(string) --*

          The description of the archive that was specified in the Initiate Multipart Upload
          request.

        - **PartSizeInBytes** *(integer) --*

          The part size, in bytes, specified in the Initiate Multipart Upload request. This is the
          size of all the parts in the upload except the last part, which may be smaller than this
          size.

        - **CreationDate** *(string) --*

          The UTC time at which the multipart upload was initiated.

    - **Marker** *(string) --*

      An opaque string that represents where to continue pagination of the results. You use the
      marker in a new List Multipart Uploads request to obtain more uploads in the list. If there
      are no more uploads, this value is ``null`` .
    """


_ClientListPartsResponsePartsTypeDef = TypedDict(
    "_ClientListPartsResponsePartsTypeDef",
    {"RangeInBytes": str, "SHA256TreeHash": str},
    total=False,
)


class ClientListPartsResponsePartsTypeDef(_ClientListPartsResponsePartsTypeDef):
    """
    Type definition for `ClientListPartsResponse` `Parts`

    A list of the part sizes of the multipart upload.

    - **RangeInBytes** *(string) --*

      The byte range of a part, inclusive of the upper value of the range.

    - **SHA256TreeHash** *(string) --*

      The SHA256 tree hash value that Amazon S3 Glacier calculated for the part. This field is
      never ``null`` .
    """


_ClientListPartsResponseTypeDef = TypedDict(
    "_ClientListPartsResponseTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List[ClientListPartsResponsePartsTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientListPartsResponseTypeDef(_ClientListPartsResponseTypeDef):
    """
    Type definition for `ClientListParts` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **MultipartUploadId** *(string) --*

      The ID of the upload to which the parts are associated.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault to which the multipart upload was initiated.

    - **ArchiveDescription** *(string) --*

      The description of the archive that was specified in the Initiate Multipart Upload request.

    - **PartSizeInBytes** *(integer) --*

      The part size in bytes. This is the same value that you specified in the Initiate Multipart
      Upload request.

    - **CreationDate** *(string) --*

      The UTC time at which the multipart upload was initiated.

    - **Parts** *(list) --*

      A list of the part sizes of the multipart upload. Each object in the array contains a
      ``RangeBytes`` and ``sha256-tree-hash`` name/value pair.

      - *(dict) --*

        A list of the part sizes of the multipart upload.

        - **RangeInBytes** *(string) --*

          The byte range of a part, inclusive of the upper value of the range.

        - **SHA256TreeHash** *(string) --*

          The SHA256 tree hash value that Amazon S3 Glacier calculated for the part. This field is
          never ``null`` .

    - **Marker** *(string) --*

      An opaque string that represents where to continue pagination of the results. You use the
      marker in a new List Parts request to obtain more jobs in the list. If there are no more
      parts, this value is ``null`` .
    """


_ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef = TypedDict(
    "_ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef",
    {"CapacityId": str, "StartDate": str, "ExpirationDate": str},
    total=False,
)


class ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef(
    _ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef
):
    """
    Type definition for `ClientListProvisionedCapacityResponse` `ProvisionedCapacityList`

    The definition for a provisioned capacity unit.

    - **CapacityId** *(string) --*

      The ID that identifies the provisioned capacity unit.

    - **StartDate** *(string) --*

      The date that the provisioned capacity unit was purchased, in Universal Coordinated Time
      (UTC).

    - **ExpirationDate** *(string) --*

      The date that the provisioned capacity unit expires, in Universal Coordinated Time (UTC).
    """


_ClientListProvisionedCapacityResponseTypeDef = TypedDict(
    "_ClientListProvisionedCapacityResponseTypeDef",
    {
        "ProvisionedCapacityList": List[
            ClientListProvisionedCapacityResponseProvisionedCapacityListTypeDef
        ]
    },
    total=False,
)


class ClientListProvisionedCapacityResponseTypeDef(
    _ClientListProvisionedCapacityResponseTypeDef
):
    """
    Type definition for `ClientListProvisionedCapacity` `Response`

    - **ProvisionedCapacityList** *(list) --*

      The response body contains the following JSON fields.

      - *(dict) --*

        The definition for a provisioned capacity unit.

        - **CapacityId** *(string) --*

          The ID that identifies the provisioned capacity unit.

        - **StartDate** *(string) --*

          The date that the provisioned capacity unit was purchased, in Universal Coordinated Time
          (UTC).

        - **ExpirationDate** *(string) --*

          The date that the provisioned capacity unit expires, in Universal Coordinated Time (UTC).
    """


_ClientListTagsForVaultResponseTypeDef = TypedDict(
    "_ClientListTagsForVaultResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForVaultResponseTypeDef(_ClientListTagsForVaultResponseTypeDef):
    """
    Type definition for `ClientListTagsForVault` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **Tags** *(dict) --*

      The tags attached to the vault. Each tag is composed of a key and a value.

      - *(string) --*

        - *(string) --*
    """


_ClientListVaultsResponseVaultListTypeDef = TypedDict(
    "_ClientListVaultsResponseVaultListTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
    },
    total=False,
)


class ClientListVaultsResponseVaultListTypeDef(
    _ClientListVaultsResponseVaultListTypeDef
):
    """
    Type definition for `ClientListVaultsResponse` `VaultList`

    Contains the Amazon S3 Glacier response to your request.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault.

    - **VaultName** *(string) --*

      The name of the vault.

    - **CreationDate** *(string) --*

      The Universal Coordinated Time (UTC) date when the vault was created. This value should
      be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

    - **LastInventoryDate** *(string) --*

      The Universal Coordinated Time (UTC) date when Amazon S3 Glacier completed the last vault
      inventory. This value should be a string in the ISO 8601 date format, for example
      ``2012-03-20T17:03:43.221Z`` .

    - **NumberOfArchives** *(integer) --*

      The number of archives in the vault as of the last inventory date. This field will return
      ``null`` if an inventory has not yet run on the vault, for example if you just created
      the vault.

    - **SizeInBytes** *(integer) --*

      Total size, in bytes, of the archives in the vault as of the last inventory date. This
      field will return null if an inventory has not yet run on the vault, for example if you
      just created the vault.
    """


_ClientListVaultsResponseTypeDef = TypedDict(
    "_ClientListVaultsResponseTypeDef",
    {"VaultList": List[ClientListVaultsResponseVaultListTypeDef], "Marker": str},
    total=False,
)


class ClientListVaultsResponseTypeDef(_ClientListVaultsResponseTypeDef):
    """
    Type definition for `ClientListVaults` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **VaultList** *(list) --*

      List of vaults.

      - *(dict) --*

        Contains the Amazon S3 Glacier response to your request.

        - **VaultARN** *(string) --*

          The Amazon Resource Name (ARN) of the vault.

        - **VaultName** *(string) --*

          The name of the vault.

        - **CreationDate** *(string) --*

          The Universal Coordinated Time (UTC) date when the vault was created. This value should
          be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

        - **LastInventoryDate** *(string) --*

          The Universal Coordinated Time (UTC) date when Amazon S3 Glacier completed the last vault
          inventory. This value should be a string in the ISO 8601 date format, for example
          ``2012-03-20T17:03:43.221Z`` .

        - **NumberOfArchives** *(integer) --*

          The number of archives in the vault as of the last inventory date. This field will return
          ``null`` if an inventory has not yet run on the vault, for example if you just created
          the vault.

        - **SizeInBytes** *(integer) --*

          Total size, in bytes, of the archives in the vault as of the last inventory date. This
          field will return null if an inventory has not yet run on the vault, for example if you
          just created the vault.

    - **Marker** *(string) --*

      The vault ARN at which to continue pagination of the results. You use the marker in another
      List Vaults request to obtain more vaults in the list.
    """


_ClientPurchaseProvisionedCapacityResponseTypeDef = TypedDict(
    "_ClientPurchaseProvisionedCapacityResponseTypeDef",
    {"capacityId": str},
    total=False,
)


class ClientPurchaseProvisionedCapacityResponseTypeDef(
    _ClientPurchaseProvisionedCapacityResponseTypeDef
):
    """
    Type definition for `ClientPurchaseProvisionedCapacity` `Response`

    - **capacityId** *(string) --*

      The ID that identifies the provisioned capacity unit.
    """


_ClientSetDataRetrievalPolicyPolicyRulesTypeDef = TypedDict(
    "_ClientSetDataRetrievalPolicyPolicyRulesTypeDef",
    {"Strategy": str, "BytesPerHour": int},
    total=False,
)


class ClientSetDataRetrievalPolicyPolicyRulesTypeDef(
    _ClientSetDataRetrievalPolicyPolicyRulesTypeDef
):
    """
    Type definition for `ClientSetDataRetrievalPolicyPolicy` `Rules`

    Data retrieval policy rule.

    - **Strategy** *(string) --*

      The type of data retrieval policy to set.

      Valid values: BytesPerHour|FreeTier|None

    - **BytesPerHour** *(integer) --*

      The maximum number of bytes that can be retrieved in an hour.

      This field is required only if the value of the Strategy field is ``BytesPerHour`` . Your
      PUT operation will be rejected if the Strategy field is not set to ``BytesPerHour`` and you
      set this field.
    """


_ClientSetDataRetrievalPolicyPolicyTypeDef = TypedDict(
    "_ClientSetDataRetrievalPolicyPolicyTypeDef",
    {"Rules": List[ClientSetDataRetrievalPolicyPolicyRulesTypeDef]},
    total=False,
)


class ClientSetDataRetrievalPolicyPolicyTypeDef(
    _ClientSetDataRetrievalPolicyPolicyTypeDef
):
    """
    Type definition for `ClientSetDataRetrievalPolicy` `Policy`

    The data retrieval policy in JSON format.

    - **Rules** *(list) --*

      The policy rule. Although this is a list type, currently there must be only one rule, which
      contains a Strategy field and optionally a BytesPerHour field.

      - *(dict) --*

        Data retrieval policy rule.

        - **Strategy** *(string) --*

          The type of data retrieval policy to set.

          Valid values: BytesPerHour|FreeTier|None

        - **BytesPerHour** *(integer) --*

          The maximum number of bytes that can be retrieved in an hour.

          This field is required only if the value of the Strategy field is ``BytesPerHour`` . Your
          PUT operation will be rejected if the Strategy field is not set to ``BytesPerHour`` and you
          set this field.
    """


_ClientSetVaultAccessPolicypolicyTypeDef = TypedDict(
    "_ClientSetVaultAccessPolicypolicyTypeDef", {"Policy": str}, total=False
)


class ClientSetVaultAccessPolicypolicyTypeDef(_ClientSetVaultAccessPolicypolicyTypeDef):
    """
    Type definition for `ClientSetVaultAccessPolicy` `policy`

    The vault access policy as a JSON string.

    - **Policy** *(string) --*

      The vault access policy.
    """


_ClientSetVaultNotificationsvaultNotificationConfigTypeDef = TypedDict(
    "_ClientSetVaultNotificationsvaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)


class ClientSetVaultNotificationsvaultNotificationConfigTypeDef(
    _ClientSetVaultNotificationsvaultNotificationConfigTypeDef
):
    """
    Type definition for `ClientSetVaultNotifications` `vaultNotificationConfig`

    Provides options for specifying notification configuration.

    - **SNSTopic** *(string) --*

      The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).

    - **Events** *(list) --*

      A list of one or more events for which Amazon S3 Glacier will send a notification to the
      specified Amazon SNS topic.

      - *(string) --*
    """


_ClientUploadArchiveResponseTypeDef = TypedDict(
    "_ClientUploadArchiveResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)


class ClientUploadArchiveResponseTypeDef(_ClientUploadArchiveResponseTypeDef):
    """
    Type definition for `ClientUploadArchive` `Response`

    Contains the Amazon S3 Glacier response to your request.

    For information about the underlying REST API, see `Upload Archive
    <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ . For
    conceptual information, see `Working with Archives in Amazon S3 Glacier
    <https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ .

    - **location** *(string) --*

      The relative URI path of the newly added archive resource.

    - **checksum** *(string) --*

      The checksum of the archive computed by Amazon S3 Glacier.

    - **archiveId** *(string) --*

      The ID of the archive. This value is also included as part of the location.
    """


_ClientUploadMultipartPartResponseTypeDef = TypedDict(
    "_ClientUploadMultipartPartResponseTypeDef", {"checksum": str}, total=False
)


class ClientUploadMultipartPartResponseTypeDef(
    _ClientUploadMultipartPartResponseTypeDef
):
    """
    Type definition for `ClientUploadMultipartPart` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **checksum** *(string) --*

      The SHA256 tree hash that Amazon S3 Glacier computed for the uploaded part.
    """


_JobGetOutputResponseTypeDef = TypedDict(
    "_JobGetOutputResponseTypeDef",
    {
        "checksum": str,
        "status": int,
        "contentRange": str,
        "acceptRanges": str,
        "contentType": str,
        "archiveDescription": str,
    },
    total=False,
)


class JobGetOutputResponseTypeDef(_JobGetOutputResponseTypeDef):
    """
    Type definition for `JobGetOutput` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **body** (:class:`.StreamingBody`) --

      The job data, either archive data or inventory data.

    - **checksum** *(string) --*

      The checksum of the data in the response. This header is returned only when retrieving the
      output for an archive retrieval job. Furthermore, this header appears only under the
      following conditions:

      * You get the entire range of the archive.

      * You request a range to return of the archive that starts and ends on a multiple of 1 MB.
      For example, if you have an 3.1 MB archive and you specify a range to return that starts at 1
      MB and ends at 2 MB, then the x-amz-sha256-tree-hash is returned as a response header.

      * You request a range of the archive to return that starts on a multiple of 1 MB and goes to
      the end of the archive. For example, if you have a 3.1 MB archive and you specify a range
      that starts at 2 MB and ends at 3.1 MB (the end of the archive), then the
      x-amz-sha256-tree-hash is returned as a response header.

    - **status** *(integer) --*

      The HTTP response code for a job output request. The value depends on whether a range was
      specified in the request.

    - **contentRange** *(string) --*

      The range of bytes returned by Amazon S3 Glacier. If only partial output is downloaded, the
      response provides the range of bytes Amazon S3 Glacier returned. For example, bytes
      0-1048575/8388608 returns the first 1 MB from 8 MB.

    - **acceptRanges** *(string) --*

      Indicates the range units accepted. For more information, see `RFC2616
      <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`__ .

    - **contentType** *(string) --*

      The Content-Type depends on whether the job output is an archive or a vault inventory. For
      archive data, the Content-Type is application/octet-stream. For vault inventory, if you
      requested CSV format when you initiated the job, the Content-Type is text/csv. Otherwise, by
      default, vault inventory is returned as JSON, and the Content-Type is application/json.

    - **archiveDescription** *(string) --*

      The description of an archive.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListJobsPaginate` `PaginationConfig`

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


_ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef",
    {"Format": str, "StartDate": str, "EndDate": str, "Limit": str, "Marker": str},
    total=False,
)


class ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef(
    _ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobList` `InventoryRetrievalParameters`

    Parameters used for range inventory retrieval.

    - **Format** *(string) --*

      The output format for the vault inventory list, which is set by the **InitiateJob**
      request when initiating a job to retrieve a vault inventory. Valid values are ``CSV``
      and ``JSON`` .

    - **StartDate** *(string) --*

      The start of the date range in Universal Coordinated Time (UTC) for vault inventory
      retrieval that includes archives created on or after this date. This value should be a
      string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

    - **EndDate** *(string) --*

      The end of the date range in UTC for vault inventory retrieval that includes archives
      created before this date. This value should be a string in the ISO 8601 date format,
      for example ``2013-03-20T17:03:43Z`` .

    - **Limit** *(string) --*

      The maximum number of inventory items returned per vault inventory retrieval request.
      This limit is set when initiating the job with the a **InitiateJob** request.

    - **Marker** *(string) --*

      An opaque string that represents where to continue pagination of the vault inventory
      retrieval results. You use the marker in a new **InitiateJob** request to obtain
      additional inventory items. If there are no more inventory items, this value is
      ``null`` . For more information, see `Range Inventory Retrieval
      <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__
      .
    """


_ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef",
    {"Type": str, "DisplayName": str, "URI": str, "ID": str, "EmailAddress": str},
    total=False,
)


class ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef(
    _ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobListOutputLocationS3AccessControlList` `Grantee`

    The grantee.

    - **Type** *(string) --*

      Type of grantee

    - **DisplayName** *(string) --*

      Screen name of the grantee.

    - **URI** *(string) --*

      URI of the grantee group.

    - **ID** *(string) --*

      The canonical user ID of the grantee.

    - **EmailAddress** *(string) --*

      Email address of the grantee.
    """


_ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ListJobsPaginateResponseJobListOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef(
    _ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobListOutputLocationS3` `AccessControlList`

    Contains information about a grant.

    - **Grantee** *(dict) --*

      The grantee.

      - **Type** *(string) --*

        Type of grantee

      - **DisplayName** *(string) --*

        Screen name of the grantee.

      - **URI** *(string) --*

        URI of the grantee group.

      - **ID** *(string) --*

        The canonical user ID of the grantee.

      - **EmailAddress** *(string) --*

        Email address of the grantee.

    - **Permission** *(string) --*

      Specifies the permission given to the grantee.
    """


_ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": str, "KMSKeyId": str, "KMSContext": str},
    total=False,
)


class ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef(
    _ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobListOutputLocationS3` `Encryption`

    Contains information about the encryption used to store the job results in Amazon S3.

    - **EncryptionType** *(string) --*

      The server-side encryption algorithm used when storing job results in Amazon S3,
      for example ``AES256`` or ``aws:kms`` .

    - **KMSKeyId** *(string) --*

      The AWS KMS key ID to use for object encryption. All GET and PUT requests for an
      object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or
      Signature Version 4.

    - **KMSContext** *(string) --*

      Optional. If the encryption type is ``aws:kms`` , you can use this value to specify
      the encryption context for the job results.
    """


_ListJobsPaginateResponseJobListOutputLocationS3TypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ListJobsPaginateResponseJobListOutputLocationS3EncryptionTypeDef,
        "CannedACL": str,
        "AccessControlList": List[
            ListJobsPaginateResponseJobListOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": str,
    },
    total=False,
)


class ListJobsPaginateResponseJobListOutputLocationS3TypeDef(
    _ListJobsPaginateResponseJobListOutputLocationS3TypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobListOutputLocation` `S3`

    Describes an S3 location that will receive the results of the job request.

    - **BucketName** *(string) --*

      The name of the Amazon S3 bucket where the job results are stored.

    - **Prefix** *(string) --*

      The prefix that is prepended to the results for this request.

    - **Encryption** *(dict) --*

      Contains information about the encryption used to store the job results in Amazon S3.

      - **EncryptionType** *(string) --*

        The server-side encryption algorithm used when storing job results in Amazon S3,
        for example ``AES256`` or ``aws:kms`` .

      - **KMSKeyId** *(string) --*

        The AWS KMS key ID to use for object encryption. All GET and PUT requests for an
        object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or
        Signature Version 4.

      - **KMSContext** *(string) --*

        Optional. If the encryption type is ``aws:kms`` , you can use this value to specify
        the encryption context for the job results.

    - **CannedACL** *(string) --*

      The canned access control list (ACL) to apply to the job results.

    - **AccessControlList** *(list) --*

      A list of grants that control access to the staged results.

      - *(dict) --*

        Contains information about a grant.

        - **Grantee** *(dict) --*

          The grantee.

          - **Type** *(string) --*

            Type of grantee

          - **DisplayName** *(string) --*

            Screen name of the grantee.

          - **URI** *(string) --*

            URI of the grantee group.

          - **ID** *(string) --*

            The canonical user ID of the grantee.

          - **EmailAddress** *(string) --*

            Email address of the grantee.

        - **Permission** *(string) --*

          Specifies the permission given to the grantee.

    - **Tagging** *(dict) --*

      The tag-set that is applied to the job results.

      - *(string) --*

        - *(string) --*

    - **UserMetadata** *(dict) --*

      A map of metadata to store with the job results in Amazon S3.

      - *(string) --*

        - *(string) --*

    - **StorageClass** *(string) --*

      The storage class used to store the job results.
    """


_ListJobsPaginateResponseJobListOutputLocationTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListOutputLocationTypeDef",
    {"S3": ListJobsPaginateResponseJobListOutputLocationS3TypeDef},
    total=False,
)


class ListJobsPaginateResponseJobListOutputLocationTypeDef(
    _ListJobsPaginateResponseJobListOutputLocationTypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobList` `OutputLocation`

    Contains the location where the data from the select job is stored.

    - **S3** *(dict) --*

      Describes an S3 location that will receive the results of the job request.

      - **BucketName** *(string) --*

        The name of the Amazon S3 bucket where the job results are stored.

      - **Prefix** *(string) --*

        The prefix that is prepended to the results for this request.

      - **Encryption** *(dict) --*

        Contains information about the encryption used to store the job results in Amazon S3.

        - **EncryptionType** *(string) --*

          The server-side encryption algorithm used when storing job results in Amazon S3,
          for example ``AES256`` or ``aws:kms`` .

        - **KMSKeyId** *(string) --*

          The AWS KMS key ID to use for object encryption. All GET and PUT requests for an
          object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or
          Signature Version 4.

        - **KMSContext** *(string) --*

          Optional. If the encryption type is ``aws:kms`` , you can use this value to specify
          the encryption context for the job results.

      - **CannedACL** *(string) --*

        The canned access control list (ACL) to apply to the job results.

      - **AccessControlList** *(list) --*

        A list of grants that control access to the staged results.

        - *(dict) --*

          Contains information about a grant.

          - **Grantee** *(dict) --*

            The grantee.

            - **Type** *(string) --*

              Type of grantee

            - **DisplayName** *(string) --*

              Screen name of the grantee.

            - **URI** *(string) --*

              URI of the grantee group.

            - **ID** *(string) --*

              The canonical user ID of the grantee.

            - **EmailAddress** *(string) --*

              Email address of the grantee.

          - **Permission** *(string) --*

            Specifies the permission given to the grantee.

      - **Tagging** *(dict) --*

        The tag-set that is applied to the job results.

        - *(string) --*

          - *(string) --*

      - **UserMetadata** *(dict) --*

        A map of metadata to store with the job results in Amazon S3.

        - *(string) --*

          - *(string) --*

      - **StorageClass** *(string) --*

        The storage class used to store the job results.
    """


_ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef",
    {
        "FileHeaderInfo": str,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef(
    _ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobListSelectParametersInputSerialization` `csv`

    Describes the serialization of a CSV-encoded object.

    - **FileHeaderInfo** *(string) --*

      Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and
      ``Use`` .

    - **Comments** *(string) --*

      A single character used to indicate that a row should be ignored when the character
      is present at the start of that row.

    - **QuoteEscapeCharacter** *(string) --*

      A single character used for escaping the quotation-mark character inside an already
      escaped value.

    - **RecordDelimiter** *(string) --*

      A value used to separate individual records from each other.

    - **FieldDelimiter** *(string) --*

      A value used to separate individual fields from each other within a record.

    - **QuoteCharacter** *(string) --*

      A value used as an escape character where the field delimiter is part of the value.
    """


_ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef",
    {
        "csv": ListJobsPaginateResponseJobListSelectParametersInputSerializationcsvTypeDef
    },
    total=False,
)


class ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef(
    _ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobListSelectParameters` `InputSerialization`

    Describes the serialization format of the object.

    - **csv** *(dict) --*

      Describes the serialization of a CSV-encoded object.

      - **FileHeaderInfo** *(string) --*

        Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and
        ``Use`` .

      - **Comments** *(string) --*

        A single character used to indicate that a row should be ignored when the character
        is present at the start of that row.

      - **QuoteEscapeCharacter** *(string) --*

        A single character used for escaping the quotation-mark character inside an already
        escaped value.

      - **RecordDelimiter** *(string) --*

        A value used to separate individual records from each other.

      - **FieldDelimiter** *(string) --*

        A value used to separate individual fields from each other within a record.

      - **QuoteCharacter** *(string) --*

        A value used as an escape character where the field delimiter is part of the value.
    """


_ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef",
    {
        "QuoteFields": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)


class ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef(
    _ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobListSelectParametersOutputSerialization` `csv`

    Describes the serialization of CSV-encoded query results.

    - **QuoteFields** *(string) --*

      A value that indicates whether all output fields should be contained within
      quotation marks.

    - **QuoteEscapeCharacter** *(string) --*

      A single character used for escaping the quotation-mark character inside an already
      escaped value.

    - **RecordDelimiter** *(string) --*

      A value used to separate individual records from each other.

    - **FieldDelimiter** *(string) --*

      A value used to separate individual fields from each other within a record.

    - **QuoteCharacter** *(string) --*

      A value used as an escape character where the field delimiter is part of the value.
    """


_ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef",
    {
        "csv": ListJobsPaginateResponseJobListSelectParametersOutputSerializationcsvTypeDef
    },
    total=False,
)


class ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef(
    _ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobListSelectParameters` `OutputSerialization`

    Describes how the results of the select job are serialized.

    - **csv** *(dict) --*

      Describes the serialization of CSV-encoded query results.

      - **QuoteFields** *(string) --*

        A value that indicates whether all output fields should be contained within
        quotation marks.

      - **QuoteEscapeCharacter** *(string) --*

        A single character used for escaping the quotation-mark character inside an already
        escaped value.

      - **RecordDelimiter** *(string) --*

        A value used to separate individual records from each other.

      - **FieldDelimiter** *(string) --*

        A value used to separate individual fields from each other within a record.

      - **QuoteCharacter** *(string) --*

        A value used as an escape character where the field delimiter is part of the value.
    """


_ListJobsPaginateResponseJobListSelectParametersTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListSelectParametersTypeDef",
    {
        "InputSerialization": ListJobsPaginateResponseJobListSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ListJobsPaginateResponseJobListSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)


class ListJobsPaginateResponseJobListSelectParametersTypeDef(
    _ListJobsPaginateResponseJobListSelectParametersTypeDef
):
    """
    Type definition for `ListJobsPaginateResponseJobList` `SelectParameters`

    Contains the parameters used for a select.

    - **InputSerialization** *(dict) --*

      Describes the serialization format of the object.

      - **csv** *(dict) --*

        Describes the serialization of a CSV-encoded object.

        - **FileHeaderInfo** *(string) --*

          Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and
          ``Use`` .

        - **Comments** *(string) --*

          A single character used to indicate that a row should be ignored when the character
          is present at the start of that row.

        - **QuoteEscapeCharacter** *(string) --*

          A single character used for escaping the quotation-mark character inside an already
          escaped value.

        - **RecordDelimiter** *(string) --*

          A value used to separate individual records from each other.

        - **FieldDelimiter** *(string) --*

          A value used to separate individual fields from each other within a record.

        - **QuoteCharacter** *(string) --*

          A value used as an escape character where the field delimiter is part of the value.

    - **ExpressionType** *(string) --*

      The type of the provided expression, for example ``SQL`` .

    - **Expression** *(string) --*

      The expression that is used to select the object.

    - **OutputSerialization** *(dict) --*

      Describes how the results of the select job are serialized.

      - **csv** *(dict) --*

        Describes the serialization of CSV-encoded query results.

        - **QuoteFields** *(string) --*

          A value that indicates whether all output fields should be contained within
          quotation marks.

        - **QuoteEscapeCharacter** *(string) --*

          A single character used for escaping the quotation-mark character inside an already
          escaped value.

        - **RecordDelimiter** *(string) --*

          A value used to separate individual records from each other.

        - **FieldDelimiter** *(string) --*

          A value used to separate individual fields from each other within a record.

        - **QuoteCharacter** *(string) --*

          A value used as an escape character where the field delimiter is part of the value.
    """


_ListJobsPaginateResponseJobListTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": str,
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": str,
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": ListJobsPaginateResponseJobListInventoryRetrievalParametersTypeDef,
        "JobOutputPath": str,
        "SelectParameters": ListJobsPaginateResponseJobListSelectParametersTypeDef,
        "OutputLocation": ListJobsPaginateResponseJobListOutputLocationTypeDef,
    },
    total=False,
)


class ListJobsPaginateResponseJobListTypeDef(_ListJobsPaginateResponseJobListTypeDef):
    """
    Type definition for `ListJobsPaginateResponse` `JobList`

    Contains the description of an Amazon S3 Glacier job.

    - **JobId** *(string) --*

      An opaque string that identifies an Amazon S3 Glacier job.

    - **JobDescription** *(string) --*

      The job description provided when initiating the job.

    - **Action** *(string) --*

      The job type. This value is either ``ArchiveRetrieval`` , ``InventoryRetrieval`` , or
      ``Select`` .

    - **ArchiveId** *(string) --*

      The archive ID requested for a select job or archive retrieval. Otherwise, this field is
      null.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

    - **CreationDate** *(string) --*

      The UTC date when the job was created. This value is a string representation of ISO 8601
      date format, for example ``"2012-03-20T17:03:43.221Z"`` .

    - **Completed** *(boolean) --*

      The job status. When a job is completed, you get the job's output using Get Job Output
      (GET output).

    - **StatusCode** *(string) --*

      The status code can be ``InProgress`` , ``Succeeded`` , or ``Failed`` , and indicates the
      status of the job.

    - **StatusMessage** *(string) --*

      A friendly message that describes the job status.

    - **ArchiveSizeInBytes** *(integer) --*

      For an archive retrieval job, this value is the size in bytes of the archive being
      requested for download. For an inventory retrieval or select job, this value is null.

    - **InventorySizeInBytes** *(integer) --*

      For an inventory retrieval job, this value is the size in bytes of the inventory
      requested for download. For an archive retrieval or select job, this value is null.

    - **SNSTopic** *(string) --*

      An Amazon SNS topic that receives notification.

    - **CompletionDate** *(string) --*

      The UTC time that the job request completed. While the job is in progress, the value is
      null.

    - **SHA256TreeHash** *(string) --*

      For an archive retrieval job, this value is the checksum of the archive. Otherwise, this
      value is null.

      The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob**
      request for an archive specified a tree-hash aligned range, then this field returns a
      value.

      If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash
      value.

      This field is null for the following:

      * Archive retrieval jobs that specify a range that is not tree-hash aligned

      * Archival jobs that specify a range that is equal to the whole archive, when the job
      status is ``InProgress``

      * Inventory jobs

      * Select jobs

    - **ArchiveSHA256TreeHash** *(string) --*

      The SHA256 tree hash of the entire archive for an archive retrieval. For inventory
      retrieval or select jobs, this field is null.

    - **RetrievalByteRange** *(string) --*

      The retrieved byte range for archive retrieval jobs in the form *StartByteValue*
      -*EndByteValue* . If no range was specified in the archive retrieval, then the whole
      archive is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals
      the size of the archive minus 1. For inventory retrieval or select jobs, this field is
      null.

    - **Tier** *(string) --*

      The tier to use for a select or an archive retrieval. Valid values are ``Expedited`` ,
      ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

    - **InventoryRetrievalParameters** *(dict) --*

      Parameters used for range inventory retrieval.

      - **Format** *(string) --*

        The output format for the vault inventory list, which is set by the **InitiateJob**
        request when initiating a job to retrieve a vault inventory. Valid values are ``CSV``
        and ``JSON`` .

      - **StartDate** *(string) --*

        The start of the date range in Universal Coordinated Time (UTC) for vault inventory
        retrieval that includes archives created on or after this date. This value should be a
        string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

      - **EndDate** *(string) --*

        The end of the date range in UTC for vault inventory retrieval that includes archives
        created before this date. This value should be a string in the ISO 8601 date format,
        for example ``2013-03-20T17:03:43Z`` .

      - **Limit** *(string) --*

        The maximum number of inventory items returned per vault inventory retrieval request.
        This limit is set when initiating the job with the a **InitiateJob** request.

      - **Marker** *(string) --*

        An opaque string that represents where to continue pagination of the vault inventory
        retrieval results. You use the marker in a new **InitiateJob** request to obtain
        additional inventory items. If there are no more inventory items, this value is
        ``null`` . For more information, see `Range Inventory Retrieval
        <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__
        .

    - **JobOutputPath** *(string) --*

      Contains the job output location.

    - **SelectParameters** *(dict) --*

      Contains the parameters used for a select.

      - **InputSerialization** *(dict) --*

        Describes the serialization format of the object.

        - **csv** *(dict) --*

          Describes the serialization of a CSV-encoded object.

          - **FileHeaderInfo** *(string) --*

            Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and
            ``Use`` .

          - **Comments** *(string) --*

            A single character used to indicate that a row should be ignored when the character
            is present at the start of that row.

          - **QuoteEscapeCharacter** *(string) --*

            A single character used for escaping the quotation-mark character inside an already
            escaped value.

          - **RecordDelimiter** *(string) --*

            A value used to separate individual records from each other.

          - **FieldDelimiter** *(string) --*

            A value used to separate individual fields from each other within a record.

          - **QuoteCharacter** *(string) --*

            A value used as an escape character where the field delimiter is part of the value.

      - **ExpressionType** *(string) --*

        The type of the provided expression, for example ``SQL`` .

      - **Expression** *(string) --*

        The expression that is used to select the object.

      - **OutputSerialization** *(dict) --*

        Describes how the results of the select job are serialized.

        - **csv** *(dict) --*

          Describes the serialization of CSV-encoded query results.

          - **QuoteFields** *(string) --*

            A value that indicates whether all output fields should be contained within
            quotation marks.

          - **QuoteEscapeCharacter** *(string) --*

            A single character used for escaping the quotation-mark character inside an already
            escaped value.

          - **RecordDelimiter** *(string) --*

            A value used to separate individual records from each other.

          - **FieldDelimiter** *(string) --*

            A value used to separate individual fields from each other within a record.

          - **QuoteCharacter** *(string) --*

            A value used as an escape character where the field delimiter is part of the value.

    - **OutputLocation** *(dict) --*

      Contains the location where the data from the select job is stored.

      - **S3** *(dict) --*

        Describes an S3 location that will receive the results of the job request.

        - **BucketName** *(string) --*

          The name of the Amazon S3 bucket where the job results are stored.

        - **Prefix** *(string) --*

          The prefix that is prepended to the results for this request.

        - **Encryption** *(dict) --*

          Contains information about the encryption used to store the job results in Amazon S3.

          - **EncryptionType** *(string) --*

            The server-side encryption algorithm used when storing job results in Amazon S3,
            for example ``AES256`` or ``aws:kms`` .

          - **KMSKeyId** *(string) --*

            The AWS KMS key ID to use for object encryption. All GET and PUT requests for an
            object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or
            Signature Version 4.

          - **KMSContext** *(string) --*

            Optional. If the encryption type is ``aws:kms`` , you can use this value to specify
            the encryption context for the job results.

        - **CannedACL** *(string) --*

          The canned access control list (ACL) to apply to the job results.

        - **AccessControlList** *(list) --*

          A list of grants that control access to the staged results.

          - *(dict) --*

            Contains information about a grant.

            - **Grantee** *(dict) --*

              The grantee.

              - **Type** *(string) --*

                Type of grantee

              - **DisplayName** *(string) --*

                Screen name of the grantee.

              - **URI** *(string) --*

                URI of the grantee group.

              - **ID** *(string) --*

                The canonical user ID of the grantee.

              - **EmailAddress** *(string) --*

                Email address of the grantee.

            - **Permission** *(string) --*

              Specifies the permission given to the grantee.

        - **Tagging** *(dict) --*

          The tag-set that is applied to the job results.

          - *(string) --*

            - *(string) --*

        - **UserMetadata** *(dict) --*

          A map of metadata to store with the job results in Amazon S3.

          - *(string) --*

            - *(string) --*

        - **StorageClass** *(string) --*

          The storage class used to store the job results.
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {"JobList": List[ListJobsPaginateResponseJobListTypeDef], "NextToken": str},
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    Type definition for `ListJobsPaginate` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **JobList** *(list) --*

      A list of job objects. Each job object contains metadata describing the job.

      - *(dict) --*

        Contains the description of an Amazon S3 Glacier job.

        - **JobId** *(string) --*

          An opaque string that identifies an Amazon S3 Glacier job.

        - **JobDescription** *(string) --*

          The job description provided when initiating the job.

        - **Action** *(string) --*

          The job type. This value is either ``ArchiveRetrieval`` , ``InventoryRetrieval`` , or
          ``Select`` .

        - **ArchiveId** *(string) --*

          The archive ID requested for a select job or archive retrieval. Otherwise, this field is
          null.

        - **VaultARN** *(string) --*

          The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

        - **CreationDate** *(string) --*

          The UTC date when the job was created. This value is a string representation of ISO 8601
          date format, for example ``"2012-03-20T17:03:43.221Z"`` .

        - **Completed** *(boolean) --*

          The job status. When a job is completed, you get the job's output using Get Job Output
          (GET output).

        - **StatusCode** *(string) --*

          The status code can be ``InProgress`` , ``Succeeded`` , or ``Failed`` , and indicates the
          status of the job.

        - **StatusMessage** *(string) --*

          A friendly message that describes the job status.

        - **ArchiveSizeInBytes** *(integer) --*

          For an archive retrieval job, this value is the size in bytes of the archive being
          requested for download. For an inventory retrieval or select job, this value is null.

        - **InventorySizeInBytes** *(integer) --*

          For an inventory retrieval job, this value is the size in bytes of the inventory
          requested for download. For an archive retrieval or select job, this value is null.

        - **SNSTopic** *(string) --*

          An Amazon SNS topic that receives notification.

        - **CompletionDate** *(string) --*

          The UTC time that the job request completed. While the job is in progress, the value is
          null.

        - **SHA256TreeHash** *(string) --*

          For an archive retrieval job, this value is the checksum of the archive. Otherwise, this
          value is null.

          The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob**
          request for an archive specified a tree-hash aligned range, then this field returns a
          value.

          If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash
          value.

          This field is null for the following:

          * Archive retrieval jobs that specify a range that is not tree-hash aligned

          * Archival jobs that specify a range that is equal to the whole archive, when the job
          status is ``InProgress``

          * Inventory jobs

          * Select jobs

        - **ArchiveSHA256TreeHash** *(string) --*

          The SHA256 tree hash of the entire archive for an archive retrieval. For inventory
          retrieval or select jobs, this field is null.

        - **RetrievalByteRange** *(string) --*

          The retrieved byte range for archive retrieval jobs in the form *StartByteValue*
          -*EndByteValue* . If no range was specified in the archive retrieval, then the whole
          archive is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals
          the size of the archive minus 1. For inventory retrieval or select jobs, this field is
          null.

        - **Tier** *(string) --*

          The tier to use for a select or an archive retrieval. Valid values are ``Expedited`` ,
          ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

        - **InventoryRetrievalParameters** *(dict) --*

          Parameters used for range inventory retrieval.

          - **Format** *(string) --*

            The output format for the vault inventory list, which is set by the **InitiateJob**
            request when initiating a job to retrieve a vault inventory. Valid values are ``CSV``
            and ``JSON`` .

          - **StartDate** *(string) --*

            The start of the date range in Universal Coordinated Time (UTC) for vault inventory
            retrieval that includes archives created on or after this date. This value should be a
            string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

          - **EndDate** *(string) --*

            The end of the date range in UTC for vault inventory retrieval that includes archives
            created before this date. This value should be a string in the ISO 8601 date format,
            for example ``2013-03-20T17:03:43Z`` .

          - **Limit** *(string) --*

            The maximum number of inventory items returned per vault inventory retrieval request.
            This limit is set when initiating the job with the a **InitiateJob** request.

          - **Marker** *(string) --*

            An opaque string that represents where to continue pagination of the vault inventory
            retrieval results. You use the marker in a new **InitiateJob** request to obtain
            additional inventory items. If there are no more inventory items, this value is
            ``null`` . For more information, see `Range Inventory Retrieval
            <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__
            .

        - **JobOutputPath** *(string) --*

          Contains the job output location.

        - **SelectParameters** *(dict) --*

          Contains the parameters used for a select.

          - **InputSerialization** *(dict) --*

            Describes the serialization format of the object.

            - **csv** *(dict) --*

              Describes the serialization of a CSV-encoded object.

              - **FileHeaderInfo** *(string) --*

                Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and
                ``Use`` .

              - **Comments** *(string) --*

                A single character used to indicate that a row should be ignored when the character
                is present at the start of that row.

              - **QuoteEscapeCharacter** *(string) --*

                A single character used for escaping the quotation-mark character inside an already
                escaped value.

              - **RecordDelimiter** *(string) --*

                A value used to separate individual records from each other.

              - **FieldDelimiter** *(string) --*

                A value used to separate individual fields from each other within a record.

              - **QuoteCharacter** *(string) --*

                A value used as an escape character where the field delimiter is part of the value.

          - **ExpressionType** *(string) --*

            The type of the provided expression, for example ``SQL`` .

          - **Expression** *(string) --*

            The expression that is used to select the object.

          - **OutputSerialization** *(dict) --*

            Describes how the results of the select job are serialized.

            - **csv** *(dict) --*

              Describes the serialization of CSV-encoded query results.

              - **QuoteFields** *(string) --*

                A value that indicates whether all output fields should be contained within
                quotation marks.

              - **QuoteEscapeCharacter** *(string) --*

                A single character used for escaping the quotation-mark character inside an already
                escaped value.

              - **RecordDelimiter** *(string) --*

                A value used to separate individual records from each other.

              - **FieldDelimiter** *(string) --*

                A value used to separate individual fields from each other within a record.

              - **QuoteCharacter** *(string) --*

                A value used as an escape character where the field delimiter is part of the value.

        - **OutputLocation** *(dict) --*

          Contains the location where the data from the select job is stored.

          - **S3** *(dict) --*

            Describes an S3 location that will receive the results of the job request.

            - **BucketName** *(string) --*

              The name of the Amazon S3 bucket where the job results are stored.

            - **Prefix** *(string) --*

              The prefix that is prepended to the results for this request.

            - **Encryption** *(dict) --*

              Contains information about the encryption used to store the job results in Amazon S3.

              - **EncryptionType** *(string) --*

                The server-side encryption algorithm used when storing job results in Amazon S3,
                for example ``AES256`` or ``aws:kms`` .

              - **KMSKeyId** *(string) --*

                The AWS KMS key ID to use for object encryption. All GET and PUT requests for an
                object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or
                Signature Version 4.

              - **KMSContext** *(string) --*

                Optional. If the encryption type is ``aws:kms`` , you can use this value to specify
                the encryption context for the job results.

            - **CannedACL** *(string) --*

              The canned access control list (ACL) to apply to the job results.

            - **AccessControlList** *(list) --*

              A list of grants that control access to the staged results.

              - *(dict) --*

                Contains information about a grant.

                - **Grantee** *(dict) --*

                  The grantee.

                  - **Type** *(string) --*

                    Type of grantee

                  - **DisplayName** *(string) --*

                    Screen name of the grantee.

                  - **URI** *(string) --*

                    URI of the grantee group.

                  - **ID** *(string) --*

                    The canonical user ID of the grantee.

                  - **EmailAddress** *(string) --*

                    Email address of the grantee.

                - **Permission** *(string) --*

                  Specifies the permission given to the grantee.

            - **Tagging** *(dict) --*

              The tag-set that is applied to the job results.

              - *(string) --*

                - *(string) --*

            - **UserMetadata** *(dict) --*

              A map of metadata to store with the job results in Amazon S3.

              - *(string) --*

                - *(string) --*

            - **StorageClass** *(string) --*

              The storage class used to store the job results.

    - **NextToken** *(string) --*

      A token to resume pagination.
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


_ListMultipartUploadsPaginateResponseUploadsListTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseUploadsListTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
    },
    total=False,
)


class ListMultipartUploadsPaginateResponseUploadsListTypeDef(
    _ListMultipartUploadsPaginateResponseUploadsListTypeDef
):
    """
    Type definition for `ListMultipartUploadsPaginateResponse` `UploadsList`

    A list of in-progress multipart uploads for a vault.

    - **MultipartUploadId** *(string) --*

      The ID of a multipart upload.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault that contains the archive.

    - **ArchiveDescription** *(string) --*

      The description of the archive that was specified in the Initiate Multipart Upload
      request.

    - **PartSizeInBytes** *(integer) --*

      The part size, in bytes, specified in the Initiate Multipart Upload request. This is the
      size of all the parts in the upload except the last part, which may be smaller than this
      size.

    - **CreationDate** *(string) --*

      The UTC time at which the multipart upload was initiated.
    """


_ListMultipartUploadsPaginateResponseTypeDef = TypedDict(
    "_ListMultipartUploadsPaginateResponseTypeDef",
    {
        "UploadsList": List[ListMultipartUploadsPaginateResponseUploadsListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListMultipartUploadsPaginateResponseTypeDef(
    _ListMultipartUploadsPaginateResponseTypeDef
):
    """
    Type definition for `ListMultipartUploadsPaginate` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **UploadsList** *(list) --*

      A list of in-progress multipart uploads.

      - *(dict) --*

        A list of in-progress multipart uploads for a vault.

        - **MultipartUploadId** *(string) --*

          The ID of a multipart upload.

        - **VaultARN** *(string) --*

          The Amazon Resource Name (ARN) of the vault that contains the archive.

        - **ArchiveDescription** *(string) --*

          The description of the archive that was specified in the Initiate Multipart Upload
          request.

        - **PartSizeInBytes** *(integer) --*

          The part size, in bytes, specified in the Initiate Multipart Upload request. This is the
          size of all the parts in the upload except the last part, which may be smaller than this
          size.

        - **CreationDate** *(string) --*

          The UTC time at which the multipart upload was initiated.

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


_ListPartsPaginateResponsePartsTypeDef = TypedDict(
    "_ListPartsPaginateResponsePartsTypeDef",
    {"RangeInBytes": str, "SHA256TreeHash": str},
    total=False,
)


class ListPartsPaginateResponsePartsTypeDef(_ListPartsPaginateResponsePartsTypeDef):
    """
    Type definition for `ListPartsPaginateResponse` `Parts`

    A list of the part sizes of the multipart upload.

    - **RangeInBytes** *(string) --*

      The byte range of a part, inclusive of the upper value of the range.

    - **SHA256TreeHash** *(string) --*

      The SHA256 tree hash value that Amazon S3 Glacier calculated for the part. This field is
      never ``null`` .
    """


_ListPartsPaginateResponseTypeDef = TypedDict(
    "_ListPartsPaginateResponseTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List[ListPartsPaginateResponsePartsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPartsPaginateResponseTypeDef(_ListPartsPaginateResponseTypeDef):
    """
    Type definition for `ListPartsPaginate` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **MultipartUploadId** *(string) --*

      The ID of the upload to which the parts are associated.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault to which the multipart upload was initiated.

    - **ArchiveDescription** *(string) --*

      The description of the archive that was specified in the Initiate Multipart Upload request.

    - **PartSizeInBytes** *(integer) --*

      The part size in bytes. This is the same value that you specified in the Initiate Multipart
      Upload request.

    - **CreationDate** *(string) --*

      The UTC time at which the multipart upload was initiated.

    - **Parts** *(list) --*

      A list of the part sizes of the multipart upload. Each object in the array contains a
      ``RangeBytes`` and ``sha256-tree-hash`` name/value pair.

      - *(dict) --*

        A list of the part sizes of the multipart upload.

        - **RangeInBytes** *(string) --*

          The byte range of a part, inclusive of the upper value of the range.

        - **SHA256TreeHash** *(string) --*

          The SHA256 tree hash value that Amazon S3 Glacier calculated for the part. This field is
          never ``null`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListVaultsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVaultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVaultsPaginatePaginationConfigTypeDef(
    _ListVaultsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListVaultsPaginate` `PaginationConfig`

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


_ListVaultsPaginateResponseVaultListTypeDef = TypedDict(
    "_ListVaultsPaginateResponseVaultListTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
    },
    total=False,
)


class ListVaultsPaginateResponseVaultListTypeDef(
    _ListVaultsPaginateResponseVaultListTypeDef
):
    """
    Type definition for `ListVaultsPaginateResponse` `VaultList`

    Contains the Amazon S3 Glacier response to your request.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault.

    - **VaultName** *(string) --*

      The name of the vault.

    - **CreationDate** *(string) --*

      The Universal Coordinated Time (UTC) date when the vault was created. This value should
      be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

    - **LastInventoryDate** *(string) --*

      The Universal Coordinated Time (UTC) date when Amazon S3 Glacier completed the last vault
      inventory. This value should be a string in the ISO 8601 date format, for example
      ``2012-03-20T17:03:43.221Z`` .

    - **NumberOfArchives** *(integer) --*

      The number of archives in the vault as of the last inventory date. This field will return
      ``null`` if an inventory has not yet run on the vault, for example if you just created
      the vault.

    - **SizeInBytes** *(integer) --*

      Total size, in bytes, of the archives in the vault as of the last inventory date. This
      field will return null if an inventory has not yet run on the vault, for example if you
      just created the vault.
    """


_ListVaultsPaginateResponseTypeDef = TypedDict(
    "_ListVaultsPaginateResponseTypeDef",
    {"VaultList": List[ListVaultsPaginateResponseVaultListTypeDef], "NextToken": str},
    total=False,
)


class ListVaultsPaginateResponseTypeDef(_ListVaultsPaginateResponseTypeDef):
    """
    Type definition for `ListVaultsPaginate` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **VaultList** *(list) --*

      List of vaults.

      - *(dict) --*

        Contains the Amazon S3 Glacier response to your request.

        - **VaultARN** *(string) --*

          The Amazon Resource Name (ARN) of the vault.

        - **VaultName** *(string) --*

          The name of the vault.

        - **CreationDate** *(string) --*

          The Universal Coordinated Time (UTC) date when the vault was created. This value should
          be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

        - **LastInventoryDate** *(string) --*

          The Universal Coordinated Time (UTC) date when Amazon S3 Glacier completed the last vault
          inventory. This value should be a string in the ISO 8601 date format, for example
          ``2012-03-20T17:03:43.221Z`` .

        - **NumberOfArchives** *(integer) --*

          The number of archives in the vault as of the last inventory date. This field will return
          ``null`` if an inventory has not yet run on the vault, for example if you just created
          the vault.

        - **SizeInBytes** *(integer) --*

          Total size, in bytes, of the archives in the vault as of the last inventory date. This
          field will return null if an inventory has not yet run on the vault, for example if you
          just created the vault.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_MultipartUploadCompleteResponseTypeDef = TypedDict(
    "_MultipartUploadCompleteResponseTypeDef",
    {"location": str, "checksum": str, "archiveId": str},
    total=False,
)


class MultipartUploadCompleteResponseTypeDef(_MultipartUploadCompleteResponseTypeDef):
    """
    Type definition for `MultipartUploadComplete` `Response`

    Contains the Amazon S3 Glacier response to your request.

    For information about the underlying REST API, see `Upload Archive
    <https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ . For
    conceptual information, see `Working with Archives in Amazon S3 Glacier
    <https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ .

    - **location** *(string) --*

      The relative URI path of the newly added archive resource.

    - **checksum** *(string) --*

      The checksum of the archive computed by Amazon S3 Glacier.

    - **archiveId** *(string) --*

      The ID of the archive. This value is also included as part of the location.
    """


_MultipartUploadPartsResponsePartsTypeDef = TypedDict(
    "_MultipartUploadPartsResponsePartsTypeDef",
    {"RangeInBytes": str, "SHA256TreeHash": str},
    total=False,
)


class MultipartUploadPartsResponsePartsTypeDef(
    _MultipartUploadPartsResponsePartsTypeDef
):
    """
    Type definition for `MultipartUploadPartsResponse` `Parts`

    A list of the part sizes of the multipart upload.

    - **RangeInBytes** *(string) --*

      The byte range of a part, inclusive of the upper value of the range.

    - **SHA256TreeHash** *(string) --*

      The SHA256 tree hash value that Amazon S3 Glacier calculated for the part. This field is
      never ``null`` .
    """


_MultipartUploadPartsResponseTypeDef = TypedDict(
    "_MultipartUploadPartsResponseTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List[MultipartUploadPartsResponsePartsTypeDef],
        "Marker": str,
    },
    total=False,
)


class MultipartUploadPartsResponseTypeDef(_MultipartUploadPartsResponseTypeDef):
    """
    Type definition for `MultipartUploadParts` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **MultipartUploadId** *(string) --*

      The ID of the upload to which the parts are associated.

    - **VaultARN** *(string) --*

      The Amazon Resource Name (ARN) of the vault to which the multipart upload was initiated.

    - **ArchiveDescription** *(string) --*

      The description of the archive that was specified in the Initiate Multipart Upload request.

    - **PartSizeInBytes** *(integer) --*

      The part size in bytes. This is the same value that you specified in the Initiate Multipart
      Upload request.

    - **CreationDate** *(string) --*

      The UTC time at which the multipart upload was initiated.

    - **Parts** *(list) --*

      A list of the part sizes of the multipart upload. Each object in the array contains a
      ``RangeBytes`` and ``sha256-tree-hash`` name/value pair.

      - *(dict) --*

        A list of the part sizes of the multipart upload.

        - **RangeInBytes** *(string) --*

          The byte range of a part, inclusive of the upper value of the range.

        - **SHA256TreeHash** *(string) --*

          The SHA256 tree hash value that Amazon S3 Glacier calculated for the part. This field is
          never ``null`` .

    - **Marker** *(string) --*

      An opaque string that represents where to continue pagination of the results. You use the
      marker in a new List Parts request to obtain more jobs in the list. If there are no more
      parts, this value is ``null`` .
    """


_MultipartUploadUploadPartResponseTypeDef = TypedDict(
    "_MultipartUploadUploadPartResponseTypeDef", {"checksum": str}, total=False
)


class MultipartUploadUploadPartResponseTypeDef(
    _MultipartUploadUploadPartResponseTypeDef
):
    """
    Type definition for `MultipartUploadUploadPart` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **checksum** *(string) --*

      The SHA256 tree hash that Amazon S3 Glacier computed for the uploaded part.
    """


_NotificationSetvaultNotificationConfigTypeDef = TypedDict(
    "_NotificationSetvaultNotificationConfigTypeDef",
    {"SNSTopic": str, "Events": List[str]},
    total=False,
)


class NotificationSetvaultNotificationConfigTypeDef(
    _NotificationSetvaultNotificationConfigTypeDef
):
    """
    Type definition for `NotificationSet` `vaultNotificationConfig`

    Provides options for specifying notification configuration.

    - **SNSTopic** *(string) --*

      The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).

    - **Events** *(list) --*

      A list of one or more events for which Amazon S3 Glacier will send a notification to the
      specified Amazon SNS topic.

      - *(string) --*
    """


_VaultCreateResponseTypeDef = TypedDict(
    "_VaultCreateResponseTypeDef", {"location": str}, total=False
)


class VaultCreateResponseTypeDef(_VaultCreateResponseTypeDef):
    """
    Type definition for `VaultCreate` `Response`

    Contains the Amazon S3 Glacier response to your request.

    - **location** *(string) --*

      The URI of the vault that was created.
    """


_VaultExistsWaitWaiterConfigTypeDef = TypedDict(
    "_VaultExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class VaultExistsWaitWaiterConfigTypeDef(_VaultExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `VaultExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 15
    """


_VaultNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "_VaultNotExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class VaultNotExistsWaitWaiterConfigTypeDef(_VaultNotExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `VaultNotExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 15
    """
