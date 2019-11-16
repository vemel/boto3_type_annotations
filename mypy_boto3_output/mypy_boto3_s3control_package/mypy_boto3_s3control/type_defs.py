"Main interface for s3control type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateJobManifestLocationTypeDef",
    "ClientCreateJobManifestSpecTypeDef",
    "ClientCreateJobManifestTypeDef",
    "ClientCreateJobOperationLambdaInvokeTypeDef",
    "ClientCreateJobOperationS3InitiateRestoreObjectTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    "ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    "ClientCreateJobOperationS3PutObjectAclTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    "ClientCreateJobOperationS3PutObjectCopyTypeDef",
    "ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef",
    "ClientCreateJobOperationS3PutObjectTaggingTypeDef",
    "ClientCreateJobOperationTypeDef",
    "ClientCreateJobReportTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientDescribeJobResponseJobFailureReasonsTypeDef",
    "ClientDescribeJobResponseJobManifestLocationTypeDef",
    "ClientDescribeJobResponseJobManifestSpecTypeDef",
    "ClientDescribeJobResponseJobManifestTypeDef",
    "ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef",
    "ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef",
    "ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef",
    "ClientDescribeJobResponseJobOperationTypeDef",
    "ClientDescribeJobResponseJobProgressSummaryTypeDef",
    "ClientDescribeJobResponseJobReportTypeDef",
    "ClientDescribeJobResponseJobTypeDef",
    "ClientDescribeJobResponseTypeDef",
    "ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    "ClientGetPublicAccessBlockResponseTypeDef",
    "ClientListJobsResponseJobsProgressSummaryTypeDef",
    "ClientListJobsResponseJobsTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    "ClientUpdateJobPriorityResponseTypeDef",
    "ClientUpdateJobStatusResponseTypeDef",
)


_RequiredClientCreateJobManifestLocationTypeDef = TypedDict(
    "_RequiredClientCreateJobManifestLocationTypeDef", {"ObjectArn": str, "ETag": str}
)
_OptionalClientCreateJobManifestLocationTypeDef = TypedDict(
    "_OptionalClientCreateJobManifestLocationTypeDef",
    {"ObjectVersionId": str},
    total=False,
)


class ClientCreateJobManifestLocationTypeDef(
    _RequiredClientCreateJobManifestLocationTypeDef,
    _OptionalClientCreateJobManifestLocationTypeDef,
):
    """
    Type definition for `ClientCreateJobManifest` `Location`

    Contains the information required to locate the specified job's manifest.

    - **ObjectArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) for a manifest object.

    - **ObjectVersionId** *(string) --*

      The optional version ID to identify a specific version of the manifest object.

    - **ETag** *(string) --* **[REQUIRED]**

      The ETag for the specified manifest object.
    """


_RequiredClientCreateJobManifestSpecTypeDef = TypedDict(
    "_RequiredClientCreateJobManifestSpecTypeDef", {"Format": str}
)
_OptionalClientCreateJobManifestSpecTypeDef = TypedDict(
    "_OptionalClientCreateJobManifestSpecTypeDef", {"Fields": List[str]}, total=False
)


class ClientCreateJobManifestSpecTypeDef(
    _RequiredClientCreateJobManifestSpecTypeDef,
    _OptionalClientCreateJobManifestSpecTypeDef,
):
    """
    Type definition for `ClientCreateJobManifest` `Spec`

    Describes the format of the specified job's manifest. If the manifest is in CSV format, also
    describes the columns contained within the manifest.

    - **Format** *(string) --* **[REQUIRED]**

      Indicates which of the available formats the specified manifest uses.

    - **Fields** *(list) --*

      If the specified manifest object is in the ``S3BatchOperations_CSV_20180820`` format, this
      element describes which columns contain the required data.

      - *(string) --*
    """


_ClientCreateJobManifestTypeDef = TypedDict(
    "_ClientCreateJobManifestTypeDef",
    {
        "Spec": ClientCreateJobManifestSpecTypeDef,
        "Location": ClientCreateJobManifestLocationTypeDef,
    },
)


class ClientCreateJobManifestTypeDef(_ClientCreateJobManifestTypeDef):
    """
    Type definition for `ClientCreateJob` `Manifest`

    Configuration parameters for the manifest.

    - **Spec** *(dict) --* **[REQUIRED]**

      Describes the format of the specified job's manifest. If the manifest is in CSV format, also
      describes the columns contained within the manifest.

      - **Format** *(string) --* **[REQUIRED]**

        Indicates which of the available formats the specified manifest uses.

      - **Fields** *(list) --*

        If the specified manifest object is in the ``S3BatchOperations_CSV_20180820`` format, this
        element describes which columns contain the required data.

        - *(string) --*

    - **Location** *(dict) --* **[REQUIRED]**

      Contains the information required to locate the specified job's manifest.

      - **ObjectArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) for a manifest object.

      - **ObjectVersionId** *(string) --*

        The optional version ID to identify a specific version of the manifest object.

      - **ETag** *(string) --* **[REQUIRED]**

        The ETag for the specified manifest object.
    """


_ClientCreateJobOperationLambdaInvokeTypeDef = TypedDict(
    "_ClientCreateJobOperationLambdaInvokeTypeDef", {"FunctionArn": str}, total=False
)


class ClientCreateJobOperationLambdaInvokeTypeDef(
    _ClientCreateJobOperationLambdaInvokeTypeDef
):
    """
    Type definition for `ClientCreateJobOperation` `LambdaInvoke`

    Directs the specified job to invoke an AWS Lambda function on each object in the manifest.

    - **FunctionArn** *(string) --*

      The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will invoke
      for each object in the manifest.
    """


_ClientCreateJobOperationS3InitiateRestoreObjectTypeDef = TypedDict(
    "_ClientCreateJobOperationS3InitiateRestoreObjectTypeDef",
    {"ExpirationInDays": int, "GlacierJobTier": str},
    total=False,
)


class ClientCreateJobOperationS3InitiateRestoreObjectTypeDef(
    _ClientCreateJobOperationS3InitiateRestoreObjectTypeDef
):
    """
    Type definition for `ClientCreateJobOperation` `S3InitiateRestoreObject`

    Directs the specified job to execute an Initiate Glacier Restore call on each object in the
    manifest.

    - **ExpirationInDays** *(integer) --*

    - **GlacierJobTier** *(string) --*
    """


_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    {"TypeIdentifier": str, "Identifier": str, "DisplayName": str},
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef(
    _ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef
):
    """
    Type definition for `ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrants` `Grantee`

    - **TypeIdentifier** *(string) --*

    - **Identifier** *(string) --*

    - **DisplayName** *(string) --*
    """


_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    {
        "Grantee": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef(
    _ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef
):
    """
    Type definition for `ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlList` `Grants`

    - **Grantee** *(dict) --*

      - **TypeIdentifier** *(string) --*

      - **Identifier** *(string) --*

      - **DisplayName** *(string) --*

    - **Permission** *(string) --*
    """


_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef(
    _ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef
):
    """
    Type definition for `ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlList` `Owner`

    - **ID** *(string) --*

    - **DisplayName** *(string) --*
    """


_RequiredClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef = TypedDict(
    "_RequiredClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    {
        "Owner": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef
    },
)
_OptionalClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef = TypedDict(
    "_OptionalClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    {
        "Grants": List[
            ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef
        ]
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef(
    _RequiredClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef,
    _OptionalClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef,
):
    """
    Type definition for `ClientCreateJobOperationS3PutObjectAclAccessControlPolicy` `AccessControlList`

    - **Owner** *(dict) --* **[REQUIRED]**

      - **ID** *(string) --*

      - **DisplayName** *(string) --*

    - **Grants** *(list) --*

      - *(dict) --*

        - **Grantee** *(dict) --*

          - **TypeIdentifier** *(string) --*

          - **Identifier** *(string) --*

          - **DisplayName** *(string) --*

        - **Permission** *(string) --*
    """


_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    {
        "AccessControlList": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef,
        "CannedAccessControlList": str,
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef(
    _ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef
):
    """
    Type definition for `ClientCreateJobOperationS3PutObjectAcl` `AccessControlPolicy`

    - **AccessControlList** *(dict) --*

      - **Owner** *(dict) --* **[REQUIRED]**

        - **ID** *(string) --*

        - **DisplayName** *(string) --*

      - **Grants** *(list) --*

        - *(dict) --*

          - **Grantee** *(dict) --*

            - **TypeIdentifier** *(string) --*

            - **Identifier** *(string) --*

            - **DisplayName** *(string) --*

          - **Permission** *(string) --*

    - **CannedAccessControlList** *(string) --*
    """


_ClientCreateJobOperationS3PutObjectAclTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectAclTypeDef",
    {
        "AccessControlPolicy": ClientCreateJobOperationS3PutObjectAclAccessControlPolicyTypeDef
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectAclTypeDef(
    _ClientCreateJobOperationS3PutObjectAclTypeDef
):
    """
    Type definition for `ClientCreateJobOperation` `S3PutObjectAcl`

    Directs the specified job to execute a PUT Object acl call on each object in the manifest.

    - **AccessControlPolicy** *(dict) --*

      - **AccessControlList** *(dict) --*

        - **Owner** *(dict) --* **[REQUIRED]**

          - **ID** *(string) --*

          - **DisplayName** *(string) --*

        - **Grants** *(list) --*

          - *(dict) --*

            - **Grantee** *(dict) --*

              - **TypeIdentifier** *(string) --*

              - **Identifier** *(string) --*

              - **DisplayName** *(string) --*

            - **Permission** *(string) --*

      - **CannedAccessControlList** *(string) --*
    """


_ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    {"TypeIdentifier": str, "Identifier": str, "DisplayName": str},
    total=False,
)


class ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef(
    _ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef
):
    """
    Type definition for `ClientCreateJobOperationS3PutObjectCopyAccessControlGrants` `Grantee`

    - **TypeIdentifier** *(string) --*

    - **Identifier** *(string) --*

    - **DisplayName** *(string) --*
    """


_ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    {
        "Grantee": ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef(
    _ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef
):
    """
    Type definition for `ClientCreateJobOperationS3PutObjectCopy` `AccessControlGrants`

    - **Grantee** *(dict) --*

      - **TypeIdentifier** *(string) --*

      - **Identifier** *(string) --*

      - **DisplayName** *(string) --*

    - **Permission** *(string) --*
    """


_ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    {
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "UserMetadata": Dict[str, str],
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "HttpExpiresDate": datetime,
        "RequesterCharged": bool,
        "SSEAlgorithm": str,
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef(
    _ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef
):
    """
    Type definition for `ClientCreateJobOperationS3PutObjectCopy` `NewObjectMetadata`

    - **CacheControl** *(string) --*

    - **ContentDisposition** *(string) --*

    - **ContentEncoding** *(string) --*

    - **ContentLanguage** *(string) --*

    - **UserMetadata** *(dict) --*

      - *(string) --*

        - *(string) --*

    - **ContentLength** *(integer) --*

    - **ContentMD5** *(string) --*

    - **ContentType** *(string) --*

    - **HttpExpiresDate** *(datetime) --*

    - **RequesterCharged** *(boolean) --*

    - **SSEAlgorithm** *(string) --*
    """


_ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    {"Key": str, "Value": str},
)


class ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef(
    _ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef
):
    """
    Type definition for `ClientCreateJobOperationS3PutObjectCopy` `NewObjectTagging`

    - **Key** *(string) --* **[REQUIRED]**

    - **Value** *(string) --* **[REQUIRED]**
    """


_ClientCreateJobOperationS3PutObjectCopyTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectCopyTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": str,
        "AccessControlGrants": List[
            ClientCreateJobOperationS3PutObjectCopyAccessControlGrantsTypeDef
        ],
        "MetadataDirective": str,
        "ModifiedSinceConstraint": datetime,
        "NewObjectMetadata": ClientCreateJobOperationS3PutObjectCopyNewObjectMetadataTypeDef,
        "NewObjectTagging": List[
            ClientCreateJobOperationS3PutObjectCopyNewObjectTaggingTypeDef
        ],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": str,
        "UnModifiedSinceConstraint": datetime,
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": str,
        "ObjectLockMode": str,
        "ObjectLockRetainUntilDate": datetime,
    },
    total=False,
)


class ClientCreateJobOperationS3PutObjectCopyTypeDef(
    _ClientCreateJobOperationS3PutObjectCopyTypeDef
):
    """
    Type definition for `ClientCreateJobOperation` `S3PutObjectCopy`

    Directs the specified job to execute a PUT Copy object call on each object in the manifest.

    - **TargetResource** *(string) --*

    - **CannedAccessControlList** *(string) --*

    - **AccessControlGrants** *(list) --*

      - *(dict) --*

        - **Grantee** *(dict) --*

          - **TypeIdentifier** *(string) --*

          - **Identifier** *(string) --*

          - **DisplayName** *(string) --*

        - **Permission** *(string) --*

    - **MetadataDirective** *(string) --*

    - **ModifiedSinceConstraint** *(datetime) --*

    - **NewObjectMetadata** *(dict) --*

      - **CacheControl** *(string) --*

      - **ContentDisposition** *(string) --*

      - **ContentEncoding** *(string) --*

      - **ContentLanguage** *(string) --*

      - **UserMetadata** *(dict) --*

        - *(string) --*

          - *(string) --*

      - **ContentLength** *(integer) --*

      - **ContentMD5** *(string) --*

      - **ContentType** *(string) --*

      - **HttpExpiresDate** *(datetime) --*

      - **RequesterCharged** *(boolean) --*

      - **SSEAlgorithm** *(string) --*

    - **NewObjectTagging** *(list) --*

      - *(dict) --*

        - **Key** *(string) --* **[REQUIRED]**

        - **Value** *(string) --* **[REQUIRED]**

    - **RedirectLocation** *(string) --*

    - **RequesterPays** *(boolean) --*

    - **StorageClass** *(string) --*

    - **UnModifiedSinceConstraint** *(datetime) --*

    - **SSEAwsKmsKeyId** *(string) --*

    - **TargetKeyPrefix** *(string) --*

    - **ObjectLockLegalHoldStatus** *(string) --*

    - **ObjectLockMode** *(string) --*

    - **ObjectLockRetainUntilDate** *(datetime) --*
    """


_ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef",
    {"Key": str, "Value": str},
)


class ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef(
    _ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef
):
    """
    Type definition for `ClientCreateJobOperationS3PutObjectTagging` `TagSet`

    - **Key** *(string) --* **[REQUIRED]**

    - **Value** *(string) --* **[REQUIRED]**
    """


_ClientCreateJobOperationS3PutObjectTaggingTypeDef = TypedDict(
    "_ClientCreateJobOperationS3PutObjectTaggingTypeDef",
    {"TagSet": List[ClientCreateJobOperationS3PutObjectTaggingTagSetTypeDef]},
    total=False,
)


class ClientCreateJobOperationS3PutObjectTaggingTypeDef(
    _ClientCreateJobOperationS3PutObjectTaggingTypeDef
):
    """
    Type definition for `ClientCreateJobOperation` `S3PutObjectTagging`

    Directs the specified job to execute a PUT Object tagging call on each object in the manifest.

    - **TagSet** *(list) --*

      - *(dict) --*

        - **Key** *(string) --* **[REQUIRED]**

        - **Value** *(string) --* **[REQUIRED]**
    """


_ClientCreateJobOperationTypeDef = TypedDict(
    "_ClientCreateJobOperationTypeDef",
    {
        "LambdaInvoke": ClientCreateJobOperationLambdaInvokeTypeDef,
        "S3PutObjectCopy": ClientCreateJobOperationS3PutObjectCopyTypeDef,
        "S3PutObjectAcl": ClientCreateJobOperationS3PutObjectAclTypeDef,
        "S3PutObjectTagging": ClientCreateJobOperationS3PutObjectTaggingTypeDef,
        "S3InitiateRestoreObject": ClientCreateJobOperationS3InitiateRestoreObjectTypeDef,
    },
    total=False,
)


class ClientCreateJobOperationTypeDef(_ClientCreateJobOperationTypeDef):
    """
    Type definition for `ClientCreateJob` `Operation`

    The operation that you want this job to perform on each object listed in the manifest. For more
    information about the available operations, see `Available Operations
    <https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html>`__ in the *Amazon
    Simple Storage Service Developer Guide* .

    - **LambdaInvoke** *(dict) --*

      Directs the specified job to invoke an AWS Lambda function on each object in the manifest.

      - **FunctionArn** *(string) --*

        The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will invoke
        for each object in the manifest.

    - **S3PutObjectCopy** *(dict) --*

      Directs the specified job to execute a PUT Copy object call on each object in the manifest.

      - **TargetResource** *(string) --*

      - **CannedAccessControlList** *(string) --*

      - **AccessControlGrants** *(list) --*

        - *(dict) --*

          - **Grantee** *(dict) --*

            - **TypeIdentifier** *(string) --*

            - **Identifier** *(string) --*

            - **DisplayName** *(string) --*

          - **Permission** *(string) --*

      - **MetadataDirective** *(string) --*

      - **ModifiedSinceConstraint** *(datetime) --*

      - **NewObjectMetadata** *(dict) --*

        - **CacheControl** *(string) --*

        - **ContentDisposition** *(string) --*

        - **ContentEncoding** *(string) --*

        - **ContentLanguage** *(string) --*

        - **UserMetadata** *(dict) --*

          - *(string) --*

            - *(string) --*

        - **ContentLength** *(integer) --*

        - **ContentMD5** *(string) --*

        - **ContentType** *(string) --*

        - **HttpExpiresDate** *(datetime) --*

        - **RequesterCharged** *(boolean) --*

        - **SSEAlgorithm** *(string) --*

      - **NewObjectTagging** *(list) --*

        - *(dict) --*

          - **Key** *(string) --* **[REQUIRED]**

          - **Value** *(string) --* **[REQUIRED]**

      - **RedirectLocation** *(string) --*

      - **RequesterPays** *(boolean) --*

      - **StorageClass** *(string) --*

      - **UnModifiedSinceConstraint** *(datetime) --*

      - **SSEAwsKmsKeyId** *(string) --*

      - **TargetKeyPrefix** *(string) --*

      - **ObjectLockLegalHoldStatus** *(string) --*

      - **ObjectLockMode** *(string) --*

      - **ObjectLockRetainUntilDate** *(datetime) --*

    - **S3PutObjectAcl** *(dict) --*

      Directs the specified job to execute a PUT Object acl call on each object in the manifest.

      - **AccessControlPolicy** *(dict) --*

        - **AccessControlList** *(dict) --*

          - **Owner** *(dict) --* **[REQUIRED]**

            - **ID** *(string) --*

            - **DisplayName** *(string) --*

          - **Grants** *(list) --*

            - *(dict) --*

              - **Grantee** *(dict) --*

                - **TypeIdentifier** *(string) --*

                - **Identifier** *(string) --*

                - **DisplayName** *(string) --*

              - **Permission** *(string) --*

        - **CannedAccessControlList** *(string) --*

    - **S3PutObjectTagging** *(dict) --*

      Directs the specified job to execute a PUT Object tagging call on each object in the manifest.

      - **TagSet** *(list) --*

        - *(dict) --*

          - **Key** *(string) --* **[REQUIRED]**

          - **Value** *(string) --* **[REQUIRED]**

    - **S3InitiateRestoreObject** *(dict) --*

      Directs the specified job to execute an Initiate Glacier Restore call on each object in the
      manifest.

      - **ExpirationInDays** *(integer) --*

      - **GlacierJobTier** *(string) --*
    """


_RequiredClientCreateJobReportTypeDef = TypedDict(
    "_RequiredClientCreateJobReportTypeDef", {"Enabled": bool}
)
_OptionalClientCreateJobReportTypeDef = TypedDict(
    "_OptionalClientCreateJobReportTypeDef",
    {"Bucket": str, "Format": str, "Prefix": str, "ReportScope": str},
    total=False,
)


class ClientCreateJobReportTypeDef(
    _RequiredClientCreateJobReportTypeDef, _OptionalClientCreateJobReportTypeDef
):
    """
    Type definition for `ClientCreateJob` `Report`

    Configuration parameters for the optional job-completion report.

    - **Bucket** *(string) --*

      The bucket where specified job-completion report will be stored.

    - **Format** *(string) --*

      The format of the specified job-completion report.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Indicates whether the specified job will generate a job-completion report.

    - **Prefix** *(string) --*

      An optional prefix to describe where in the specified bucket the job-completion report will be
      stored. Amazon S3 will store the job-completion report at <prefix>/job-<job-id>/report.json.

    - **ReportScope** *(string) --*

      Indicates whether the job-completion report will include details of all tasks or only failed
      tasks.
    """


_ClientCreateJobResponseTypeDef = TypedDict(
    "_ClientCreateJobResponseTypeDef", {"JobId": str}, total=False
)


class ClientCreateJobResponseTypeDef(_ClientCreateJobResponseTypeDef):
    """
    Type definition for `ClientCreateJob` `Response`

    - **JobId** *(string) --*

      The ID for this job. Amazon S3 generates this ID automatically and returns it after a
      successful ``Create Job`` request.
    """


_ClientDescribeJobResponseJobFailureReasonsTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobFailureReasonsTypeDef",
    {"FailureCode": str, "FailureReason": str},
    total=False,
)


class ClientDescribeJobResponseJobFailureReasonsTypeDef(
    _ClientDescribeJobResponseJobFailureReasonsTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJob` `FailureReasons`

    If this job failed, this element indicates why the job failed.

    - **FailureCode** *(string) --*

      The failure code, if any, for the specified job.

    - **FailureReason** *(string) --*

      The failure reason, if any, for the specified job.
    """


_ClientDescribeJobResponseJobManifestLocationTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobManifestLocationTypeDef",
    {"ObjectArn": str, "ObjectVersionId": str, "ETag": str},
    total=False,
)


class ClientDescribeJobResponseJobManifestLocationTypeDef(
    _ClientDescribeJobResponseJobManifestLocationTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobManifest` `Location`

    Contains the information required to locate the specified job's manifest.

    - **ObjectArn** *(string) --*

      The Amazon Resource Name (ARN) for a manifest object.

    - **ObjectVersionId** *(string) --*

      The optional version ID to identify a specific version of the manifest object.

    - **ETag** *(string) --*

      The ETag for the specified manifest object.
    """


_ClientDescribeJobResponseJobManifestSpecTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobManifestSpecTypeDef",
    {"Format": str, "Fields": List[str]},
    total=False,
)


class ClientDescribeJobResponseJobManifestSpecTypeDef(
    _ClientDescribeJobResponseJobManifestSpecTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobManifest` `Spec`

    Describes the format of the specified job's manifest. If the manifest is in CSV format,
    also describes the columns contained within the manifest.

    - **Format** *(string) --*

      Indicates which of the available formats the specified manifest uses.

    - **Fields** *(list) --*

      If the specified manifest object is in the ``S3BatchOperations_CSV_20180820`` format,
      this element describes which columns contain the required data.

      - *(string) --*
    """


_ClientDescribeJobResponseJobManifestTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobManifestTypeDef",
    {
        "Spec": ClientDescribeJobResponseJobManifestSpecTypeDef,
        "Location": ClientDescribeJobResponseJobManifestLocationTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseJobManifestTypeDef(
    _ClientDescribeJobResponseJobManifestTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJob` `Manifest`

    The configuration information for the specified job's manifest object.

    - **Spec** *(dict) --*

      Describes the format of the specified job's manifest. If the manifest is in CSV format,
      also describes the columns contained within the manifest.

      - **Format** *(string) --*

        Indicates which of the available formats the specified manifest uses.

      - **Fields** *(list) --*

        If the specified manifest object is in the ``S3BatchOperations_CSV_20180820`` format,
        this element describes which columns contain the required data.

        - *(string) --*

    - **Location** *(dict) --*

      Contains the information required to locate the specified job's manifest.

      - **ObjectArn** *(string) --*

        The Amazon Resource Name (ARN) for a manifest object.

      - **ObjectVersionId** *(string) --*

        The optional version ID to identify a specific version of the manifest object.

      - **ETag** *(string) --*

        The ETag for the specified manifest object.
    """


_ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef",
    {"FunctionArn": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef(
    _ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperation` `LambdaInvoke`

    Directs the specified job to invoke an AWS Lambda function on each object in the manifest.

    - **FunctionArn** *(string) --*

      The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will
      invoke for each object in the manifest.
    """


_ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef",
    {"ExpirationInDays": int, "GlacierJobTier": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef(
    _ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperation` `S3InitiateRestoreObject`

    Directs the specified job to execute an Initiate Glacier Restore call on each object in
    the manifest.

    - **ExpirationInDays** *(integer) --*

    - **GlacierJobTier** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef",
    {"TypeIdentifier": str, "Identifier": str, "DisplayName": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrants` `Grantee`

    - **TypeIdentifier** *(string) --*

    - **Identifier** *(string) --*

    - **DisplayName** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef",
    {
        "Grantee": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlList` `Grants`

    - **Grantee** *(dict) --*

      - **TypeIdentifier** *(string) --*

      - **Identifier** *(string) --*

      - **DisplayName** *(string) --*

    - **Permission** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlList` `Owner`

    - **ID** *(string) --*

    - **DisplayName** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef",
    {
        "Owner": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListOwnerTypeDef,
        "Grants": List[
            ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListGrantsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicy` `AccessControlList`

    - **Owner** *(dict) --*

      - **ID** *(string) --*

      - **DisplayName** *(string) --*

    - **Grants** *(list) --*

      - *(dict) --*

        - **Grantee** *(dict) --*

          - **TypeIdentifier** *(string) --*

          - **Identifier** *(string) --*

          - **DisplayName** *(string) --*

        - **Permission** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef",
    {
        "AccessControlList": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyAccessControlListTypeDef,
        "CannedAccessControlList": str,
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperationS3PutObjectAcl` `AccessControlPolicy`

    - **AccessControlList** *(dict) --*

      - **Owner** *(dict) --*

        - **ID** *(string) --*

        - **DisplayName** *(string) --*

      - **Grants** *(list) --*

        - *(dict) --*

          - **Grantee** *(dict) --*

            - **TypeIdentifier** *(string) --*

            - **Identifier** *(string) --*

            - **DisplayName** *(string) --*

          - **Permission** *(string) --*

    - **CannedAccessControlList** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef",
    {
        "AccessControlPolicy": ClientDescribeJobResponseJobOperationS3PutObjectAclAccessControlPolicyTypeDef
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperation` `S3PutObjectAcl`

    Directs the specified job to execute a PUT Object acl call on each object in the manifest.

    - **AccessControlPolicy** *(dict) --*

      - **AccessControlList** *(dict) --*

        - **Owner** *(dict) --*

          - **ID** *(string) --*

          - **DisplayName** *(string) --*

        - **Grants** *(list) --*

          - *(dict) --*

            - **Grantee** *(dict) --*

              - **TypeIdentifier** *(string) --*

              - **Identifier** *(string) --*

              - **DisplayName** *(string) --*

            - **Permission** *(string) --*

      - **CannedAccessControlList** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef",
    {"TypeIdentifier": str, "Identifier": str, "DisplayName": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrants` `Grantee`

    - **TypeIdentifier** *(string) --*

    - **Identifier** *(string) --*

    - **DisplayName** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef",
    {
        "Grantee": ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsGranteeTypeDef,
        "Permission": str,
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperationS3PutObjectCopy` `AccessControlGrants`

    - **Grantee** *(dict) --*

      - **TypeIdentifier** *(string) --*

      - **Identifier** *(string) --*

      - **DisplayName** *(string) --*

    - **Permission** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef",
    {
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "UserMetadata": Dict[str, str],
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "HttpExpiresDate": datetime,
        "RequesterCharged": bool,
        "SSEAlgorithm": str,
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperationS3PutObjectCopy` `NewObjectMetadata`

    - **CacheControl** *(string) --*

    - **ContentDisposition** *(string) --*

    - **ContentEncoding** *(string) --*

    - **ContentLanguage** *(string) --*

    - **UserMetadata** *(dict) --*

      - *(string) --*

        - *(string) --*

    - **ContentLength** *(integer) --*

    - **ContentMD5** *(string) --*

    - **ContentType** *(string) --*

    - **HttpExpiresDate** *(datetime) --*

    - **RequesterCharged** *(boolean) --*

    - **SSEAlgorithm** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperationS3PutObjectCopy` `NewObjectTagging`

    - **Key** *(string) --*

    - **Value** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": str,
        "AccessControlGrants": List[
            ClientDescribeJobResponseJobOperationS3PutObjectCopyAccessControlGrantsTypeDef
        ],
        "MetadataDirective": str,
        "ModifiedSinceConstraint": datetime,
        "NewObjectMetadata": ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectMetadataTypeDef,
        "NewObjectTagging": List[
            ClientDescribeJobResponseJobOperationS3PutObjectCopyNewObjectTaggingTypeDef
        ],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": str,
        "UnModifiedSinceConstraint": datetime,
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": str,
        "ObjectLockMode": str,
        "ObjectLockRetainUntilDate": datetime,
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperation` `S3PutObjectCopy`

    Directs the specified job to execute a PUT Copy object call on each object in the
    manifest.

    - **TargetResource** *(string) --*

    - **CannedAccessControlList** *(string) --*

    - **AccessControlGrants** *(list) --*

      - *(dict) --*

        - **Grantee** *(dict) --*

          - **TypeIdentifier** *(string) --*

          - **Identifier** *(string) --*

          - **DisplayName** *(string) --*

        - **Permission** *(string) --*

    - **MetadataDirective** *(string) --*

    - **ModifiedSinceConstraint** *(datetime) --*

    - **NewObjectMetadata** *(dict) --*

      - **CacheControl** *(string) --*

      - **ContentDisposition** *(string) --*

      - **ContentEncoding** *(string) --*

      - **ContentLanguage** *(string) --*

      - **UserMetadata** *(dict) --*

        - *(string) --*

          - *(string) --*

      - **ContentLength** *(integer) --*

      - **ContentMD5** *(string) --*

      - **ContentType** *(string) --*

      - **HttpExpiresDate** *(datetime) --*

      - **RequesterCharged** *(boolean) --*

      - **SSEAlgorithm** *(string) --*

    - **NewObjectTagging** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **Value** *(string) --*

    - **RedirectLocation** *(string) --*

    - **RequesterPays** *(boolean) --*

    - **StorageClass** *(string) --*

    - **UnModifiedSinceConstraint** *(datetime) --*

    - **SSEAwsKmsKeyId** *(string) --*

    - **TargetKeyPrefix** *(string) --*

    - **ObjectLockLegalHoldStatus** *(string) --*

    - **ObjectLockMode** *(string) --*

    - **ObjectLockRetainUntilDate** *(datetime) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperationS3PutObjectTagging` `TagSet`

    - **Key** *(string) --*

    - **Value** *(string) --*
    """


_ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef",
    {
        "TagSet": List[
            ClientDescribeJobResponseJobOperationS3PutObjectTaggingTagSetTypeDef
        ]
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef(
    _ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJobOperation` `S3PutObjectTagging`

    Directs the specified job to execute a PUT Object tagging call on each object in the
    manifest.

    - **TagSet** *(list) --*

      - *(dict) --*

        - **Key** *(string) --*

        - **Value** *(string) --*
    """


_ClientDescribeJobResponseJobOperationTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobOperationTypeDef",
    {
        "LambdaInvoke": ClientDescribeJobResponseJobOperationLambdaInvokeTypeDef,
        "S3PutObjectCopy": ClientDescribeJobResponseJobOperationS3PutObjectCopyTypeDef,
        "S3PutObjectAcl": ClientDescribeJobResponseJobOperationS3PutObjectAclTypeDef,
        "S3PutObjectTagging": ClientDescribeJobResponseJobOperationS3PutObjectTaggingTypeDef,
        "S3InitiateRestoreObject": ClientDescribeJobResponseJobOperationS3InitiateRestoreObjectTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseJobOperationTypeDef(
    _ClientDescribeJobResponseJobOperationTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJob` `Operation`

    The operation that the specified job is configured to execute on the objects listed in the
    manifest.

    - **LambdaInvoke** *(dict) --*

      Directs the specified job to invoke an AWS Lambda function on each object in the manifest.

      - **FunctionArn** *(string) --*

        The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will
        invoke for each object in the manifest.

    - **S3PutObjectCopy** *(dict) --*

      Directs the specified job to execute a PUT Copy object call on each object in the
      manifest.

      - **TargetResource** *(string) --*

      - **CannedAccessControlList** *(string) --*

      - **AccessControlGrants** *(list) --*

        - *(dict) --*

          - **Grantee** *(dict) --*

            - **TypeIdentifier** *(string) --*

            - **Identifier** *(string) --*

            - **DisplayName** *(string) --*

          - **Permission** *(string) --*

      - **MetadataDirective** *(string) --*

      - **ModifiedSinceConstraint** *(datetime) --*

      - **NewObjectMetadata** *(dict) --*

        - **CacheControl** *(string) --*

        - **ContentDisposition** *(string) --*

        - **ContentEncoding** *(string) --*

        - **ContentLanguage** *(string) --*

        - **UserMetadata** *(dict) --*

          - *(string) --*

            - *(string) --*

        - **ContentLength** *(integer) --*

        - **ContentMD5** *(string) --*

        - **ContentType** *(string) --*

        - **HttpExpiresDate** *(datetime) --*

        - **RequesterCharged** *(boolean) --*

        - **SSEAlgorithm** *(string) --*

      - **NewObjectTagging** *(list) --*

        - *(dict) --*

          - **Key** *(string) --*

          - **Value** *(string) --*

      - **RedirectLocation** *(string) --*

      - **RequesterPays** *(boolean) --*

      - **StorageClass** *(string) --*

      - **UnModifiedSinceConstraint** *(datetime) --*

      - **SSEAwsKmsKeyId** *(string) --*

      - **TargetKeyPrefix** *(string) --*

      - **ObjectLockLegalHoldStatus** *(string) --*

      - **ObjectLockMode** *(string) --*

      - **ObjectLockRetainUntilDate** *(datetime) --*

    - **S3PutObjectAcl** *(dict) --*

      Directs the specified job to execute a PUT Object acl call on each object in the manifest.

      - **AccessControlPolicy** *(dict) --*

        - **AccessControlList** *(dict) --*

          - **Owner** *(dict) --*

            - **ID** *(string) --*

            - **DisplayName** *(string) --*

          - **Grants** *(list) --*

            - *(dict) --*

              - **Grantee** *(dict) --*

                - **TypeIdentifier** *(string) --*

                - **Identifier** *(string) --*

                - **DisplayName** *(string) --*

              - **Permission** *(string) --*

        - **CannedAccessControlList** *(string) --*

    - **S3PutObjectTagging** *(dict) --*

      Directs the specified job to execute a PUT Object tagging call on each object in the
      manifest.

      - **TagSet** *(list) --*

        - *(dict) --*

          - **Key** *(string) --*

          - **Value** *(string) --*

    - **S3InitiateRestoreObject** *(dict) --*

      Directs the specified job to execute an Initiate Glacier Restore call on each object in
      the manifest.

      - **ExpirationInDays** *(integer) --*

      - **GlacierJobTier** *(string) --*
    """


_ClientDescribeJobResponseJobProgressSummaryTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobProgressSummaryTypeDef",
    {
        "TotalNumberOfTasks": int,
        "NumberOfTasksSucceeded": int,
        "NumberOfTasksFailed": int,
    },
    total=False,
)


class ClientDescribeJobResponseJobProgressSummaryTypeDef(
    _ClientDescribeJobResponseJobProgressSummaryTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJob` `ProgressSummary`

    Describes the total number of tasks that the specified job has executed, the number of
    tasks that succeeded, and the number of tasks that failed.

    - **TotalNumberOfTasks** *(integer) --*

    - **NumberOfTasksSucceeded** *(integer) --*

    - **NumberOfTasksFailed** *(integer) --*
    """


_ClientDescribeJobResponseJobReportTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobReportTypeDef",
    {"Bucket": str, "Format": str, "Enabled": bool, "Prefix": str, "ReportScope": str},
    total=False,
)


class ClientDescribeJobResponseJobReportTypeDef(
    _ClientDescribeJobResponseJobReportTypeDef
):
    """
    Type definition for `ClientDescribeJobResponseJob` `Report`

    Contains the configuration information for the job-completion report if you requested one
    in the ``Create Job`` request.

    - **Bucket** *(string) --*

      The bucket where specified job-completion report will be stored.

    - **Format** *(string) --*

      The format of the specified job-completion report.

    - **Enabled** *(boolean) --*

      Indicates whether the specified job will generate a job-completion report.

    - **Prefix** *(string) --*

      An optional prefix to describe where in the specified bucket the job-completion report
      will be stored. Amazon S3 will store the job-completion report at
      <prefix>/job-<job-id>/report.json.

    - **ReportScope** *(string) --*

      Indicates whether the job-completion report will include details of all tasks or only
      failed tasks.
    """


_ClientDescribeJobResponseJobTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobTypeDef",
    {
        "JobId": str,
        "ConfirmationRequired": bool,
        "Description": str,
        "JobArn": str,
        "Status": str,
        "Manifest": ClientDescribeJobResponseJobManifestTypeDef,
        "Operation": ClientDescribeJobResponseJobOperationTypeDef,
        "Priority": int,
        "ProgressSummary": ClientDescribeJobResponseJobProgressSummaryTypeDef,
        "StatusUpdateReason": str,
        "FailureReasons": List[ClientDescribeJobResponseJobFailureReasonsTypeDef],
        "Report": ClientDescribeJobResponseJobReportTypeDef,
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "RoleArn": str,
        "SuspendedDate": datetime,
        "SuspendedCause": str,
    },
    total=False,
)


class ClientDescribeJobResponseJobTypeDef(_ClientDescribeJobResponseJobTypeDef):
    """
    Type definition for `ClientDescribeJobResponse` `Job`

    Contains the configuration parameters and status for the job specified in the ``Describe
    Job`` request.

    - **JobId** *(string) --*

      The ID for the specified job.

    - **ConfirmationRequired** *(boolean) --*

      Indicates whether confirmation is required before Amazon S3 begins running the specified
      job. Confirmation is required only for jobs created through the Amazon S3 console.

    - **Description** *(string) --*

      The description for this job, if one was provided in this job's ``Create Job`` request.

    - **JobArn** *(string) --*

      The Amazon Resource Name (ARN) for this job.

    - **Status** *(string) --*

      The current status of the specified job.

    - **Manifest** *(dict) --*

      The configuration information for the specified job's manifest object.

      - **Spec** *(dict) --*

        Describes the format of the specified job's manifest. If the manifest is in CSV format,
        also describes the columns contained within the manifest.

        - **Format** *(string) --*

          Indicates which of the available formats the specified manifest uses.

        - **Fields** *(list) --*

          If the specified manifest object is in the ``S3BatchOperations_CSV_20180820`` format,
          this element describes which columns contain the required data.

          - *(string) --*

      - **Location** *(dict) --*

        Contains the information required to locate the specified job's manifest.

        - **ObjectArn** *(string) --*

          The Amazon Resource Name (ARN) for a manifest object.

        - **ObjectVersionId** *(string) --*

          The optional version ID to identify a specific version of the manifest object.

        - **ETag** *(string) --*

          The ETag for the specified manifest object.

    - **Operation** *(dict) --*

      The operation that the specified job is configured to execute on the objects listed in the
      manifest.

      - **LambdaInvoke** *(dict) --*

        Directs the specified job to invoke an AWS Lambda function on each object in the manifest.

        - **FunctionArn** *(string) --*

          The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will
          invoke for each object in the manifest.

      - **S3PutObjectCopy** *(dict) --*

        Directs the specified job to execute a PUT Copy object call on each object in the
        manifest.

        - **TargetResource** *(string) --*

        - **CannedAccessControlList** *(string) --*

        - **AccessControlGrants** *(list) --*

          - *(dict) --*

            - **Grantee** *(dict) --*

              - **TypeIdentifier** *(string) --*

              - **Identifier** *(string) --*

              - **DisplayName** *(string) --*

            - **Permission** *(string) --*

        - **MetadataDirective** *(string) --*

        - **ModifiedSinceConstraint** *(datetime) --*

        - **NewObjectMetadata** *(dict) --*

          - **CacheControl** *(string) --*

          - **ContentDisposition** *(string) --*

          - **ContentEncoding** *(string) --*

          - **ContentLanguage** *(string) --*

          - **UserMetadata** *(dict) --*

            - *(string) --*

              - *(string) --*

          - **ContentLength** *(integer) --*

          - **ContentMD5** *(string) --*

          - **ContentType** *(string) --*

          - **HttpExpiresDate** *(datetime) --*

          - **RequesterCharged** *(boolean) --*

          - **SSEAlgorithm** *(string) --*

        - **NewObjectTagging** *(list) --*

          - *(dict) --*

            - **Key** *(string) --*

            - **Value** *(string) --*

        - **RedirectLocation** *(string) --*

        - **RequesterPays** *(boolean) --*

        - **StorageClass** *(string) --*

        - **UnModifiedSinceConstraint** *(datetime) --*

        - **SSEAwsKmsKeyId** *(string) --*

        - **TargetKeyPrefix** *(string) --*

        - **ObjectLockLegalHoldStatus** *(string) --*

        - **ObjectLockMode** *(string) --*

        - **ObjectLockRetainUntilDate** *(datetime) --*

      - **S3PutObjectAcl** *(dict) --*

        Directs the specified job to execute a PUT Object acl call on each object in the manifest.

        - **AccessControlPolicy** *(dict) --*

          - **AccessControlList** *(dict) --*

            - **Owner** *(dict) --*

              - **ID** *(string) --*

              - **DisplayName** *(string) --*

            - **Grants** *(list) --*

              - *(dict) --*

                - **Grantee** *(dict) --*

                  - **TypeIdentifier** *(string) --*

                  - **Identifier** *(string) --*

                  - **DisplayName** *(string) --*

                - **Permission** *(string) --*

          - **CannedAccessControlList** *(string) --*

      - **S3PutObjectTagging** *(dict) --*

        Directs the specified job to execute a PUT Object tagging call on each object in the
        manifest.

        - **TagSet** *(list) --*

          - *(dict) --*

            - **Key** *(string) --*

            - **Value** *(string) --*

      - **S3InitiateRestoreObject** *(dict) --*

        Directs the specified job to execute an Initiate Glacier Restore call on each object in
        the manifest.

        - **ExpirationInDays** *(integer) --*

        - **GlacierJobTier** *(string) --*

    - **Priority** *(integer) --*

      The priority of the specified job.

    - **ProgressSummary** *(dict) --*

      Describes the total number of tasks that the specified job has executed, the number of
      tasks that succeeded, and the number of tasks that failed.

      - **TotalNumberOfTasks** *(integer) --*

      - **NumberOfTasksSucceeded** *(integer) --*

      - **NumberOfTasksFailed** *(integer) --*

    - **StatusUpdateReason** *(string) --*

    - **FailureReasons** *(list) --*

      If the specified job failed, this field contains information describing the failure.

      - *(dict) --*

        If this job failed, this element indicates why the job failed.

        - **FailureCode** *(string) --*

          The failure code, if any, for the specified job.

        - **FailureReason** *(string) --*

          The failure reason, if any, for the specified job.

    - **Report** *(dict) --*

      Contains the configuration information for the job-completion report if you requested one
      in the ``Create Job`` request.

      - **Bucket** *(string) --*

        The bucket where specified job-completion report will be stored.

      - **Format** *(string) --*

        The format of the specified job-completion report.

      - **Enabled** *(boolean) --*

        Indicates whether the specified job will generate a job-completion report.

      - **Prefix** *(string) --*

        An optional prefix to describe where in the specified bucket the job-completion report
        will be stored. Amazon S3 will store the job-completion report at
        <prefix>/job-<job-id>/report.json.

      - **ReportScope** *(string) --*

        Indicates whether the job-completion report will include details of all tasks or only
        failed tasks.

    - **CreationTime** *(datetime) --*

      A timestamp indicating when this job was created.

    - **TerminationDate** *(datetime) --*

      A timestamp indicating when this job terminated. A job's termination date is the date and
      time when it succeeded, failed, or was canceled.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) Role assigned
      to execute the tasks for this job.

    - **SuspendedDate** *(datetime) --*

      The timestamp when this job was suspended, if it has been suspended.

    - **SuspendedCause** *(string) --*

      The reason why the specified job was suspended. A job is only suspended if you create it
      through the Amazon S3 console. When you create the job, it enters the ``Suspended`` state
      to await confirmation before running. After you confirm the job, it automatically exits the
      ``Suspended`` state.
    """


_ClientDescribeJobResponseTypeDef = TypedDict(
    "_ClientDescribeJobResponseTypeDef",
    {"Job": ClientDescribeJobResponseJobTypeDef},
    total=False,
)


class ClientDescribeJobResponseTypeDef(_ClientDescribeJobResponseTypeDef):
    """
    Type definition for `ClientDescribeJob` `Response`

    - **Job** *(dict) --*

      Contains the configuration parameters and status for the job specified in the ``Describe
      Job`` request.

      - **JobId** *(string) --*

        The ID for the specified job.

      - **ConfirmationRequired** *(boolean) --*

        Indicates whether confirmation is required before Amazon S3 begins running the specified
        job. Confirmation is required only for jobs created through the Amazon S3 console.

      - **Description** *(string) --*

        The description for this job, if one was provided in this job's ``Create Job`` request.

      - **JobArn** *(string) --*

        The Amazon Resource Name (ARN) for this job.

      - **Status** *(string) --*

        The current status of the specified job.

      - **Manifest** *(dict) --*

        The configuration information for the specified job's manifest object.

        - **Spec** *(dict) --*

          Describes the format of the specified job's manifest. If the manifest is in CSV format,
          also describes the columns contained within the manifest.

          - **Format** *(string) --*

            Indicates which of the available formats the specified manifest uses.

          - **Fields** *(list) --*

            If the specified manifest object is in the ``S3BatchOperations_CSV_20180820`` format,
            this element describes which columns contain the required data.

            - *(string) --*

        - **Location** *(dict) --*

          Contains the information required to locate the specified job's manifest.

          - **ObjectArn** *(string) --*

            The Amazon Resource Name (ARN) for a manifest object.

          - **ObjectVersionId** *(string) --*

            The optional version ID to identify a specific version of the manifest object.

          - **ETag** *(string) --*

            The ETag for the specified manifest object.

      - **Operation** *(dict) --*

        The operation that the specified job is configured to execute on the objects listed in the
        manifest.

        - **LambdaInvoke** *(dict) --*

          Directs the specified job to invoke an AWS Lambda function on each object in the manifest.

          - **FunctionArn** *(string) --*

            The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will
            invoke for each object in the manifest.

        - **S3PutObjectCopy** *(dict) --*

          Directs the specified job to execute a PUT Copy object call on each object in the
          manifest.

          - **TargetResource** *(string) --*

          - **CannedAccessControlList** *(string) --*

          - **AccessControlGrants** *(list) --*

            - *(dict) --*

              - **Grantee** *(dict) --*

                - **TypeIdentifier** *(string) --*

                - **Identifier** *(string) --*

                - **DisplayName** *(string) --*

              - **Permission** *(string) --*

          - **MetadataDirective** *(string) --*

          - **ModifiedSinceConstraint** *(datetime) --*

          - **NewObjectMetadata** *(dict) --*

            - **CacheControl** *(string) --*

            - **ContentDisposition** *(string) --*

            - **ContentEncoding** *(string) --*

            - **ContentLanguage** *(string) --*

            - **UserMetadata** *(dict) --*

              - *(string) --*

                - *(string) --*

            - **ContentLength** *(integer) --*

            - **ContentMD5** *(string) --*

            - **ContentType** *(string) --*

            - **HttpExpiresDate** *(datetime) --*

            - **RequesterCharged** *(boolean) --*

            - **SSEAlgorithm** *(string) --*

          - **NewObjectTagging** *(list) --*

            - *(dict) --*

              - **Key** *(string) --*

              - **Value** *(string) --*

          - **RedirectLocation** *(string) --*

          - **RequesterPays** *(boolean) --*

          - **StorageClass** *(string) --*

          - **UnModifiedSinceConstraint** *(datetime) --*

          - **SSEAwsKmsKeyId** *(string) --*

          - **TargetKeyPrefix** *(string) --*

          - **ObjectLockLegalHoldStatus** *(string) --*

          - **ObjectLockMode** *(string) --*

          - **ObjectLockRetainUntilDate** *(datetime) --*

        - **S3PutObjectAcl** *(dict) --*

          Directs the specified job to execute a PUT Object acl call on each object in the manifest.

          - **AccessControlPolicy** *(dict) --*

            - **AccessControlList** *(dict) --*

              - **Owner** *(dict) --*

                - **ID** *(string) --*

                - **DisplayName** *(string) --*

              - **Grants** *(list) --*

                - *(dict) --*

                  - **Grantee** *(dict) --*

                    - **TypeIdentifier** *(string) --*

                    - **Identifier** *(string) --*

                    - **DisplayName** *(string) --*

                  - **Permission** *(string) --*

            - **CannedAccessControlList** *(string) --*

        - **S3PutObjectTagging** *(dict) --*

          Directs the specified job to execute a PUT Object tagging call on each object in the
          manifest.

          - **TagSet** *(list) --*

            - *(dict) --*

              - **Key** *(string) --*

              - **Value** *(string) --*

        - **S3InitiateRestoreObject** *(dict) --*

          Directs the specified job to execute an Initiate Glacier Restore call on each object in
          the manifest.

          - **ExpirationInDays** *(integer) --*

          - **GlacierJobTier** *(string) --*

      - **Priority** *(integer) --*

        The priority of the specified job.

      - **ProgressSummary** *(dict) --*

        Describes the total number of tasks that the specified job has executed, the number of
        tasks that succeeded, and the number of tasks that failed.

        - **TotalNumberOfTasks** *(integer) --*

        - **NumberOfTasksSucceeded** *(integer) --*

        - **NumberOfTasksFailed** *(integer) --*

      - **StatusUpdateReason** *(string) --*

      - **FailureReasons** *(list) --*

        If the specified job failed, this field contains information describing the failure.

        - *(dict) --*

          If this job failed, this element indicates why the job failed.

          - **FailureCode** *(string) --*

            The failure code, if any, for the specified job.

          - **FailureReason** *(string) --*

            The failure reason, if any, for the specified job.

      - **Report** *(dict) --*

        Contains the configuration information for the job-completion report if you requested one
        in the ``Create Job`` request.

        - **Bucket** *(string) --*

          The bucket where specified job-completion report will be stored.

        - **Format** *(string) --*

          The format of the specified job-completion report.

        - **Enabled** *(boolean) --*

          Indicates whether the specified job will generate a job-completion report.

        - **Prefix** *(string) --*

          An optional prefix to describe where in the specified bucket the job-completion report
          will be stored. Amazon S3 will store the job-completion report at
          <prefix>/job-<job-id>/report.json.

        - **ReportScope** *(string) --*

          Indicates whether the job-completion report will include details of all tasks or only
          failed tasks.

      - **CreationTime** *(datetime) --*

        A timestamp indicating when this job was created.

      - **TerminationDate** *(datetime) --*

        A timestamp indicating when this job terminated. A job's termination date is the date and
        time when it succeeded, failed, or was canceled.

      - **RoleArn** *(string) --*

        The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) Role assigned
        to execute the tasks for this job.

      - **SuspendedDate** *(datetime) --*

        The timestamp when this job was suspended, if it has been suspended.

      - **SuspendedCause** *(string) --*

        The reason why the specified job was suspended. A job is only suspended if you create it
        through the Amazon S3 console. When you create the job, it enters the ``Suspended`` state
        to await confirmation before running. After you confirm the job, it automatically exits the
        ``Suspended`` state.
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

    - **BlockPublicAcls** *(boolean) --*

    - **IgnorePublicAcls** *(boolean) --*

    - **BlockPublicPolicy** *(boolean) --*

    - **RestrictPublicBuckets** *(boolean) --*
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

      - **BlockPublicAcls** *(boolean) --*

      - **IgnorePublicAcls** *(boolean) --*

      - **BlockPublicPolicy** *(boolean) --*

      - **RestrictPublicBuckets** *(boolean) --*
    """


_ClientListJobsResponseJobsProgressSummaryTypeDef = TypedDict(
    "_ClientListJobsResponseJobsProgressSummaryTypeDef",
    {
        "TotalNumberOfTasks": int,
        "NumberOfTasksSucceeded": int,
        "NumberOfTasksFailed": int,
    },
    total=False,
)


class ClientListJobsResponseJobsProgressSummaryTypeDef(
    _ClientListJobsResponseJobsProgressSummaryTypeDef
):
    """
    Type definition for `ClientListJobsResponseJobs` `ProgressSummary`

    Describes the total number of tasks that the specified job has executed, the number of
    tasks that succeeded, and the number of tasks that failed.

    - **TotalNumberOfTasks** *(integer) --*

    - **NumberOfTasksSucceeded** *(integer) --*

    - **NumberOfTasksFailed** *(integer) --*
    """


_ClientListJobsResponseJobsTypeDef = TypedDict(
    "_ClientListJobsResponseJobsTypeDef",
    {
        "JobId": str,
        "Description": str,
        "Operation": str,
        "Priority": int,
        "Status": str,
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "ProgressSummary": ClientListJobsResponseJobsProgressSummaryTypeDef,
    },
    total=False,
)


class ClientListJobsResponseJobsTypeDef(_ClientListJobsResponseJobsTypeDef):
    """
    Type definition for `ClientListJobsResponse` `Jobs`

    Contains the configuration and status information for a single job retrieved as part of a
    job list.

    - **JobId** *(string) --*

      The ID for the specified job.

    - **Description** *(string) --*

      The user-specified description that was included in the specified job's ``Create Job``
      request.

    - **Operation** *(string) --*

      The operation that the specified job is configured to run on each object listed in the
      manifest.

    - **Priority** *(integer) --*

      The current priority for the specified job.

    - **Status** *(string) --*

      The specified job's current status.

    - **CreationTime** *(datetime) --*

      A timestamp indicating when the specified job was created.

    - **TerminationDate** *(datetime) --*

      A timestamp indicating when the specified job terminated. A job's termination date is the
      date and time when it succeeded, failed, or was canceled.

    - **ProgressSummary** *(dict) --*

      Describes the total number of tasks that the specified job has executed, the number of
      tasks that succeeded, and the number of tasks that failed.

      - **TotalNumberOfTasks** *(integer) --*

      - **NumberOfTasksSucceeded** *(integer) --*

      - **NumberOfTasksFailed** *(integer) --*
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"NextToken": str, "Jobs": List[ClientListJobsResponseJobsTypeDef]},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    Type definition for `ClientListJobs` `Response`

    - **NextToken** *(string) --*

      If the ``List Jobs`` request produced more than the maximum number of results, you can pass
      this value into a subsequent ``List Jobs`` request in order to retrieve the next page of
      results.

    - **Jobs** *(list) --*

      The list of current jobs and jobs that have ended within the last 30 days.

      - *(dict) --*

        Contains the configuration and status information for a single job retrieved as part of a
        job list.

        - **JobId** *(string) --*

          The ID for the specified job.

        - **Description** *(string) --*

          The user-specified description that was included in the specified job's ``Create Job``
          request.

        - **Operation** *(string) --*

          The operation that the specified job is configured to run on each object listed in the
          manifest.

        - **Priority** *(integer) --*

          The current priority for the specified job.

        - **Status** *(string) --*

          The specified job's current status.

        - **CreationTime** *(datetime) --*

          A timestamp indicating when the specified job was created.

        - **TerminationDate** *(datetime) --*

          A timestamp indicating when the specified job terminated. A job's termination date is the
          date and time when it succeeded, failed, or was canceled.

        - **ProgressSummary** *(dict) --*

          Describes the total number of tasks that the specified job has executed, the number of
          tasks that succeeded, and the number of tasks that failed.

          - **TotalNumberOfTasks** *(integer) --*

          - **NumberOfTasksSucceeded** *(integer) --*

          - **NumberOfTasksFailed** *(integer) --*
    """


_ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef = TypedDict(
    "_ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)


class ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef(
    _ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef
):
    """
    Type definition for `ClientPutPublicAccessBlock` `PublicAccessBlockConfiguration`

    - **BlockPublicAcls** *(boolean) --*

    - **IgnorePublicAcls** *(boolean) --*

    - **BlockPublicPolicy** *(boolean) --*

    - **RestrictPublicBuckets** *(boolean) --*
    """


_ClientUpdateJobPriorityResponseTypeDef = TypedDict(
    "_ClientUpdateJobPriorityResponseTypeDef",
    {"JobId": str, "Priority": int},
    total=False,
)


class ClientUpdateJobPriorityResponseTypeDef(_ClientUpdateJobPriorityResponseTypeDef):
    """
    Type definition for `ClientUpdateJobPriority` `Response`

    - **JobId** *(string) --*

      The ID for the job whose priority Amazon S3 updated.

    - **Priority** *(integer) --*

      The new priority assigned to the specified job.
    """


_ClientUpdateJobStatusResponseTypeDef = TypedDict(
    "_ClientUpdateJobStatusResponseTypeDef",
    {"JobId": str, "Status": str, "StatusUpdateReason": str},
    total=False,
)


class ClientUpdateJobStatusResponseTypeDef(_ClientUpdateJobStatusResponseTypeDef):
    """
    Type definition for `ClientUpdateJobStatus` `Response`

    - **JobId** *(string) --*

      The ID for the job whose status was updated.

    - **Status** *(string) --*

      The current status for the specified job.

    - **StatusUpdateReason** *(string) --*

      The reason that the specified job's status was updated.
    """
