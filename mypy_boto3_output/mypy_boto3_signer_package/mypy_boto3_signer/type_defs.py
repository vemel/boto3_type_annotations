"Main interface for signer type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef",
    "ClientDescribeSigningJobResponseoverridesTypeDef",
    "ClientDescribeSigningJobResponsesignedObjects3TypeDef",
    "ClientDescribeSigningJobResponsesignedObjectTypeDef",
    "ClientDescribeSigningJobResponsesigningMaterialTypeDef",
    "ClientDescribeSigningJobResponsesources3TypeDef",
    "ClientDescribeSigningJobResponsesourceTypeDef",
    "ClientDescribeSigningJobResponseTypeDef",
    "ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef",
    "ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef",
    "ClientGetSigningPlatformResponsesigningConfigurationTypeDef",
    "ClientGetSigningPlatformResponsesigningImageFormatTypeDef",
    "ClientGetSigningPlatformResponseTypeDef",
    "ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef",
    "ClientGetSigningProfileResponseoverridesTypeDef",
    "ClientGetSigningProfileResponsesigningMaterialTypeDef",
    "ClientGetSigningProfileResponseTypeDef",
    "ClientListSigningJobsResponsejobssignedObjects3TypeDef",
    "ClientListSigningJobsResponsejobssignedObjectTypeDef",
    "ClientListSigningJobsResponsejobssigningMaterialTypeDef",
    "ClientListSigningJobsResponsejobssources3TypeDef",
    "ClientListSigningJobsResponsejobssourceTypeDef",
    "ClientListSigningJobsResponsejobsTypeDef",
    "ClientListSigningJobsResponseTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef",
    "ClientListSigningPlatformsResponseplatformsTypeDef",
    "ClientListSigningPlatformsResponseTypeDef",
    "ClientListSigningProfilesResponseprofilessigningMaterialTypeDef",
    "ClientListSigningProfilesResponseprofilesTypeDef",
    "ClientListSigningProfilesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutSigningProfileResponseTypeDef",
    "ClientPutSigningProfileoverridessigningConfigurationTypeDef",
    "ClientPutSigningProfileoverridesTypeDef",
    "ClientPutSigningProfilesigningMaterialTypeDef",
    "ClientStartSigningJobResponseTypeDef",
    "ClientStartSigningJobdestinations3TypeDef",
    "ClientStartSigningJobdestinationTypeDef",
    "ClientStartSigningJobsources3TypeDef",
    "ClientStartSigningJobsourceTypeDef",
    "ListSigningJobsPaginatePaginationConfigTypeDef",
    "ListSigningJobsPaginateResponsejobssignedObjects3TypeDef",
    "ListSigningJobsPaginateResponsejobssignedObjectTypeDef",
    "ListSigningJobsPaginateResponsejobssigningMaterialTypeDef",
    "ListSigningJobsPaginateResponsejobssources3TypeDef",
    "ListSigningJobsPaginateResponsejobssourceTypeDef",
    "ListSigningJobsPaginateResponsejobsTypeDef",
    "ListSigningJobsPaginateResponseTypeDef",
    "ListSigningPlatformsPaginatePaginationConfigTypeDef",
    "ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    "ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    "ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef",
    "ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef",
    "ListSigningPlatformsPaginateResponseplatformsTypeDef",
    "ListSigningPlatformsPaginateResponseTypeDef",
    "ListSigningProfilesPaginatePaginationConfigTypeDef",
    "ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef",
    "ListSigningProfilesPaginateResponseprofilesTypeDef",
    "ListSigningProfilesPaginateResponseTypeDef",
    "SuccessfulSigningJobWaitWaiterConfigTypeDef",
)


_ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": str, "hashAlgorithm": str},
    total=False,
)


class ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef(
    _ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeSigningJobResponseoverrides` `signingConfiguration`

    A signing configuration that overrides the default encryption or hash algorithm of a
    signing job.

    - **encryptionAlgorithm** *(string) --*

      A specified override of the default encryption algorithm that is used in a code signing
      job.

    - **hashAlgorithm** *(string) --*

      A specified override of the default hash algorithm that is used in a code signing job.
    """


_ClientDescribeSigningJobResponseoverridesTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponseoverridesTypeDef",
    {
        "signingConfiguration": ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef
    },
    total=False,
)


class ClientDescribeSigningJobResponseoverridesTypeDef(
    _ClientDescribeSigningJobResponseoverridesTypeDef
):
    """
    Type definition for `ClientDescribeSigningJobResponse` `overrides`

    A list of any overrides that were applied to the signing operation.

    - **signingConfiguration** *(dict) --*

      A signing configuration that overrides the default encryption or hash algorithm of a
      signing job.

      - **encryptionAlgorithm** *(string) --*

        A specified override of the default encryption algorithm that is used in a code signing
        job.

      - **hashAlgorithm** *(string) --*

        A specified override of the default hash algorithm that is used in a code signing job.
    """


_ClientDescribeSigningJobResponsesignedObjects3TypeDef = TypedDict(
    "_ClientDescribeSigningJobResponsesignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)


class ClientDescribeSigningJobResponsesignedObjects3TypeDef(
    _ClientDescribeSigningJobResponsesignedObjects3TypeDef
):
    """
    Type definition for `ClientDescribeSigningJobResponsesignedObject` `s3`

    The ``S3SignedObject`` .

    - **bucketName** *(string) --*

      Name of the S3 bucket.

    - **key** *(string) --*

      Key name that uniquely identifies a signed code image in your bucket.
    """


_ClientDescribeSigningJobResponsesignedObjectTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponsesignedObjectTypeDef",
    {"s3": ClientDescribeSigningJobResponsesignedObjects3TypeDef},
    total=False,
)


class ClientDescribeSigningJobResponsesignedObjectTypeDef(
    _ClientDescribeSigningJobResponsesignedObjectTypeDef
):
    """
    Type definition for `ClientDescribeSigningJobResponse` `signedObject`

    Name of the S3 bucket where the signed code image is saved by code signing.

    - **s3** *(dict) --*

      The ``S3SignedObject`` .

      - **bucketName** *(string) --*

        Name of the S3 bucket.

      - **key** *(string) --*

        Key name that uniquely identifies a signed code image in your bucket.
    """


_ClientDescribeSigningJobResponsesigningMaterialTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponsesigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)


class ClientDescribeSigningJobResponsesigningMaterialTypeDef(
    _ClientDescribeSigningJobResponsesigningMaterialTypeDef
):
    """
    Type definition for `ClientDescribeSigningJobResponse` `signingMaterial`

    Amazon Resource Name (ARN) of your code signing certificate.

    - **certificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificates that is used to sign your code.
    """


_ClientDescribeSigningJobResponsesources3TypeDef = TypedDict(
    "_ClientDescribeSigningJobResponsesources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)


class ClientDescribeSigningJobResponsesources3TypeDef(
    _ClientDescribeSigningJobResponsesources3TypeDef
):
    """
    Type definition for `ClientDescribeSigningJobResponsesource` `s3`

    The ``S3Source`` object.

    - **bucketName** *(string) --*

      Name of the S3 bucket.

    - **key** *(string) --*

      Key name of the bucket object that contains your unsigned code.

    - **version** *(string) --*

      Version of your source image in your version enabled S3 bucket.
    """


_ClientDescribeSigningJobResponsesourceTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponsesourceTypeDef",
    {"s3": ClientDescribeSigningJobResponsesources3TypeDef},
    total=False,
)


class ClientDescribeSigningJobResponsesourceTypeDef(
    _ClientDescribeSigningJobResponsesourceTypeDef
):
    """
    Type definition for `ClientDescribeSigningJobResponse` `source`

    The object that contains the name of your S3 bucket or your raw code.

    - **s3** *(dict) --*

      The ``S3Source`` object.

      - **bucketName** *(string) --*

        Name of the S3 bucket.

      - **key** *(string) --*

        Key name of the bucket object that contains your unsigned code.

      - **version** *(string) --*

        Version of your source image in your version enabled S3 bucket.
    """


_ClientDescribeSigningJobResponseTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponseTypeDef",
    {
        "jobId": str,
        "source": ClientDescribeSigningJobResponsesourceTypeDef,
        "signingMaterial": ClientDescribeSigningJobResponsesigningMaterialTypeDef,
        "platformId": str,
        "profileName": str,
        "overrides": ClientDescribeSigningJobResponseoverridesTypeDef,
        "signingParameters": Dict[str, str],
        "createdAt": datetime,
        "completedAt": datetime,
        "requestedBy": str,
        "status": str,
        "statusReason": str,
        "signedObject": ClientDescribeSigningJobResponsesignedObjectTypeDef,
    },
    total=False,
)


class ClientDescribeSigningJobResponseTypeDef(_ClientDescribeSigningJobResponseTypeDef):
    """
    Type definition for `ClientDescribeSigningJob` `Response`

    - **jobId** *(string) --*

      The ID of the signing job on output.

    - **source** *(dict) --*

      The object that contains the name of your S3 bucket or your raw code.

      - **s3** *(dict) --*

        The ``S3Source`` object.

        - **bucketName** *(string) --*

          Name of the S3 bucket.

        - **key** *(string) --*

          Key name of the bucket object that contains your unsigned code.

        - **version** *(string) --*

          Version of your source image in your version enabled S3 bucket.

    - **signingMaterial** *(dict) --*

      Amazon Resource Name (ARN) of your code signing certificate.

      - **certificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

    - **platformId** *(string) --*

      The microcontroller platform to which your signed code image will be distributed.

    - **profileName** *(string) --*

      The name of the profile that initiated the signing operation.

    - **overrides** *(dict) --*

      A list of any overrides that were applied to the signing operation.

      - **signingConfiguration** *(dict) --*

        A signing configuration that overrides the default encryption or hash algorithm of a
        signing job.

        - **encryptionAlgorithm** *(string) --*

          A specified override of the default encryption algorithm that is used in a code signing
          job.

        - **hashAlgorithm** *(string) --*

          A specified override of the default hash algorithm that is used in a code signing job.

    - **signingParameters** *(dict) --*

      Map of user-assigned key-value pairs used during signing. These values contain any
      information that you specified for use in your signing job.

      - *(string) --*

        - *(string) --*

    - **createdAt** *(datetime) --*

      Date and time that the signing job was created.

    - **completedAt** *(datetime) --*

      Date and time that the signing job was completed.

    - **requestedBy** *(string) --*

      The IAM principal that requested the signing job.

    - **status** *(string) --*

      Status of the signing job.

    - **statusReason** *(string) --*

      String value that contains the status reason.

    - **signedObject** *(dict) --*

      Name of the S3 bucket where the signed code image is saved by code signing.

      - **s3** *(dict) --*

        The ``S3SignedObject`` .

        - **bucketName** *(string) --*

          Name of the S3 bucket.

        - **key** *(string) --*

          Key name that uniquely identifies a signed code image in your bucket.
    """


_ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "_ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[str], "defaultValue": str},
    total=False,
)


class ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef(
    _ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef
):
    """
    Type definition for `ClientGetSigningPlatformResponsesigningConfiguration` `encryptionAlgorithmOptions`

    The encryption algorithm options that are available for a code signing job.

    - **allowedValues** *(list) --*

      The set of accepted encryption algorithms that are allowed in a code signing job.

      - *(string) --*

    - **defaultValue** *(string) --*

      The default encryption algorithm that is used by a code signing job.
    """


_ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "_ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[str], "defaultValue": str},
    total=False,
)


class ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef(
    _ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef
):
    """
    Type definition for `ClientGetSigningPlatformResponsesigningConfiguration` `hashAlgorithmOptions`

    The hash algorithm options that are available for a a code signing job.

    - **allowedValues** *(list) --*

      The set of accepted hash algorithms allowed in a code signing job.

      - *(string) --*

    - **defaultValue** *(string) --*

      The default hash algorithm that is used in a code signing job.
    """


_ClientGetSigningPlatformResponsesigningConfigurationTypeDef = TypedDict(
    "_ClientGetSigningPlatformResponsesigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)


class ClientGetSigningPlatformResponsesigningConfigurationTypeDef(
    _ClientGetSigningPlatformResponsesigningConfigurationTypeDef
):
    """
    Type definition for `ClientGetSigningPlatformResponse` `signingConfiguration`

    A list of configurations applied to the target platform at signing.

    - **encryptionAlgorithmOptions** *(dict) --*

      The encryption algorithm options that are available for a code signing job.

      - **allowedValues** *(list) --*

        The set of accepted encryption algorithms that are allowed in a code signing job.

        - *(string) --*

      - **defaultValue** *(string) --*

        The default encryption algorithm that is used by a code signing job.

    - **hashAlgorithmOptions** *(dict) --*

      The hash algorithm options that are available for a a code signing job.

      - **allowedValues** *(list) --*

        The set of accepted hash algorithms allowed in a code signing job.

        - *(string) --*

      - **defaultValue** *(string) --*

        The default hash algorithm that is used in a code signing job.
    """


_ClientGetSigningPlatformResponsesigningImageFormatTypeDef = TypedDict(
    "_ClientGetSigningPlatformResponsesigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)


class ClientGetSigningPlatformResponsesigningImageFormatTypeDef(
    _ClientGetSigningPlatformResponsesigningImageFormatTypeDef
):
    """
    Type definition for `ClientGetSigningPlatformResponse` `signingImageFormat`

    The format of the target platform's signing image.

    - **supportedFormats** *(list) --*

      The supported formats of a code signing signing image.

      - *(string) --*

    - **defaultFormat** *(string) --*

      The default format of a code signing signing image.
    """


_ClientGetSigningPlatformResponseTypeDef = TypedDict(
    "_ClientGetSigningPlatformResponseTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": str,
        "signingConfiguration": ClientGetSigningPlatformResponsesigningConfigurationTypeDef,
        "signingImageFormat": ClientGetSigningPlatformResponsesigningImageFormatTypeDef,
        "maxSizeInMB": int,
    },
    total=False,
)


class ClientGetSigningPlatformResponseTypeDef(_ClientGetSigningPlatformResponseTypeDef):
    """
    Type definition for `ClientGetSigningPlatform` `Response`

    - **platformId** *(string) --*

      The ID of the target signing platform.

    - **displayName** *(string) --*

      The display name of the target signing platform.

    - **partner** *(string) --*

      A list of partner entities that use the target signing platform.

    - **target** *(string) --*

      The validation template that is used by the target signing platform.

    - **category** *(string) --*

      The category type of the target signing platform.

    - **signingConfiguration** *(dict) --*

      A list of configurations applied to the target platform at signing.

      - **encryptionAlgorithmOptions** *(dict) --*

        The encryption algorithm options that are available for a code signing job.

        - **allowedValues** *(list) --*

          The set of accepted encryption algorithms that are allowed in a code signing job.

          - *(string) --*

        - **defaultValue** *(string) --*

          The default encryption algorithm that is used by a code signing job.

      - **hashAlgorithmOptions** *(dict) --*

        The hash algorithm options that are available for a a code signing job.

        - **allowedValues** *(list) --*

          The set of accepted hash algorithms allowed in a code signing job.

          - *(string) --*

        - **defaultValue** *(string) --*

          The default hash algorithm that is used in a code signing job.

    - **signingImageFormat** *(dict) --*

      The format of the target platform's signing image.

      - **supportedFormats** *(list) --*

        The supported formats of a code signing signing image.

        - *(string) --*

      - **defaultFormat** *(string) --*

        The default format of a code signing signing image.

    - **maxSizeInMB** *(integer) --*

      The maximum size (in MB) of the payload that can be signed by the target platform.
    """


_ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef = TypedDict(
    "_ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": str, "hashAlgorithm": str},
    total=False,
)


class ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef(
    _ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef
):
    """
    Type definition for `ClientGetSigningProfileResponseoverrides` `signingConfiguration`

    A signing configuration that overrides the default encryption or hash algorithm of a
    signing job.

    - **encryptionAlgorithm** *(string) --*

      A specified override of the default encryption algorithm that is used in a code signing
      job.

    - **hashAlgorithm** *(string) --*

      A specified override of the default hash algorithm that is used in a code signing job.
    """


_ClientGetSigningProfileResponseoverridesTypeDef = TypedDict(
    "_ClientGetSigningProfileResponseoverridesTypeDef",
    {
        "signingConfiguration": ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef
    },
    total=False,
)


class ClientGetSigningProfileResponseoverridesTypeDef(
    _ClientGetSigningProfileResponseoverridesTypeDef
):
    """
    Type definition for `ClientGetSigningProfileResponse` `overrides`

    A list of overrides applied by the target signing profile for signing operations.

    - **signingConfiguration** *(dict) --*

      A signing configuration that overrides the default encryption or hash algorithm of a
      signing job.

      - **encryptionAlgorithm** *(string) --*

        A specified override of the default encryption algorithm that is used in a code signing
        job.

      - **hashAlgorithm** *(string) --*

        A specified override of the default hash algorithm that is used in a code signing job.
    """


_ClientGetSigningProfileResponsesigningMaterialTypeDef = TypedDict(
    "_ClientGetSigningProfileResponsesigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)


class ClientGetSigningProfileResponsesigningMaterialTypeDef(
    _ClientGetSigningProfileResponsesigningMaterialTypeDef
):
    """
    Type definition for `ClientGetSigningProfileResponse` `signingMaterial`

    The ARN of the certificate that the target profile uses for signing operations.

    - **certificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificates that is used to sign your code.
    """


_ClientGetSigningProfileResponseTypeDef = TypedDict(
    "_ClientGetSigningProfileResponseTypeDef",
    {
        "profileName": str,
        "signingMaterial": ClientGetSigningProfileResponsesigningMaterialTypeDef,
        "platformId": str,
        "overrides": ClientGetSigningProfileResponseoverridesTypeDef,
        "signingParameters": Dict[str, str],
        "status": str,
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetSigningProfileResponseTypeDef(_ClientGetSigningProfileResponseTypeDef):
    """
    Type definition for `ClientGetSigningProfile` `Response`

    - **profileName** *(string) --*

      The name of the target signing profile.

    - **signingMaterial** *(dict) --*

      The ARN of the certificate that the target profile uses for signing operations.

      - **certificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

    - **platformId** *(string) --*

      The ID of the platform that is used by the target signing profile.

    - **overrides** *(dict) --*

      A list of overrides applied by the target signing profile for signing operations.

      - **signingConfiguration** *(dict) --*

        A signing configuration that overrides the default encryption or hash algorithm of a
        signing job.

        - **encryptionAlgorithm** *(string) --*

          A specified override of the default encryption algorithm that is used in a code signing
          job.

        - **hashAlgorithm** *(string) --*

          A specified override of the default hash algorithm that is used in a code signing job.

    - **signingParameters** *(dict) --*

      A map of key-value pairs for signing operations that is attached to the target signing
      profile.

      - *(string) --*

        - *(string) --*

    - **status** *(string) --*

      The status of the target signing profile.

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) for the signing profile.

    - **tags** *(dict) --*

      A list of tags associated with the signing profile.

      - *(string) --*

        - *(string) --*
    """


_ClientListSigningJobsResponsejobssignedObjects3TypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobssignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)


class ClientListSigningJobsResponsejobssignedObjects3TypeDef(
    _ClientListSigningJobsResponsejobssignedObjects3TypeDef
):
    """
    Type definition for `ClientListSigningJobsResponsejobssignedObject` `s3`

    The ``S3SignedObject`` .

    - **bucketName** *(string) --*

      Name of the S3 bucket.

    - **key** *(string) --*

      Key name that uniquely identifies a signed code image in your bucket.
    """


_ClientListSigningJobsResponsejobssignedObjectTypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobssignedObjectTypeDef",
    {"s3": ClientListSigningJobsResponsejobssignedObjects3TypeDef},
    total=False,
)


class ClientListSigningJobsResponsejobssignedObjectTypeDef(
    _ClientListSigningJobsResponsejobssignedObjectTypeDef
):
    """
    Type definition for `ClientListSigningJobsResponsejobs` `signedObject`

    A ``SignedObject`` structure that contains information about a signing job's signed code
    image.

    - **s3** *(dict) --*

      The ``S3SignedObject`` .

      - **bucketName** *(string) --*

        Name of the S3 bucket.

      - **key** *(string) --*

        Key name that uniquely identifies a signed code image in your bucket.
    """


_ClientListSigningJobsResponsejobssigningMaterialTypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobssigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)


class ClientListSigningJobsResponsejobssigningMaterialTypeDef(
    _ClientListSigningJobsResponsejobssigningMaterialTypeDef
):
    """
    Type definition for `ClientListSigningJobsResponsejobs` `signingMaterial`

    A ``SigningMaterial`` object that contains the Amazon Resource Name (ARN) of the
    certificate used for the signing job.

    - **certificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificates that is used to sign your code.
    """


_ClientListSigningJobsResponsejobssources3TypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobssources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)


class ClientListSigningJobsResponsejobssources3TypeDef(
    _ClientListSigningJobsResponsejobssources3TypeDef
):
    """
    Type definition for `ClientListSigningJobsResponsejobssource` `s3`

    The ``S3Source`` object.

    - **bucketName** *(string) --*

      Name of the S3 bucket.

    - **key** *(string) --*

      Key name of the bucket object that contains your unsigned code.

    - **version** *(string) --*

      Version of your source image in your version enabled S3 bucket.
    """


_ClientListSigningJobsResponsejobssourceTypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobssourceTypeDef",
    {"s3": ClientListSigningJobsResponsejobssources3TypeDef},
    total=False,
)


class ClientListSigningJobsResponsejobssourceTypeDef(
    _ClientListSigningJobsResponsejobssourceTypeDef
):
    """
    Type definition for `ClientListSigningJobsResponsejobs` `source`

    A ``Source`` that contains information about a signing job's code image source.

    - **s3** *(dict) --*

      The ``S3Source`` object.

      - **bucketName** *(string) --*

        Name of the S3 bucket.

      - **key** *(string) --*

        Key name of the bucket object that contains your unsigned code.

      - **version** *(string) --*

        Version of your source image in your version enabled S3 bucket.
    """


_ClientListSigningJobsResponsejobsTypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobsTypeDef",
    {
        "jobId": str,
        "source": ClientListSigningJobsResponsejobssourceTypeDef,
        "signedObject": ClientListSigningJobsResponsejobssignedObjectTypeDef,
        "signingMaterial": ClientListSigningJobsResponsejobssigningMaterialTypeDef,
        "createdAt": datetime,
        "status": str,
    },
    total=False,
)


class ClientListSigningJobsResponsejobsTypeDef(
    _ClientListSigningJobsResponsejobsTypeDef
):
    """
    Type definition for `ClientListSigningJobsResponse` `jobs`

    Contains information about a signing job.

    - **jobId** *(string) --*

      The ID of the signing job.

    - **source** *(dict) --*

      A ``Source`` that contains information about a signing job's code image source.

      - **s3** *(dict) --*

        The ``S3Source`` object.

        - **bucketName** *(string) --*

          Name of the S3 bucket.

        - **key** *(string) --*

          Key name of the bucket object that contains your unsigned code.

        - **version** *(string) --*

          Version of your source image in your version enabled S3 bucket.

    - **signedObject** *(dict) --*

      A ``SignedObject`` structure that contains information about a signing job's signed code
      image.

      - **s3** *(dict) --*

        The ``S3SignedObject`` .

        - **bucketName** *(string) --*

          Name of the S3 bucket.

        - **key** *(string) --*

          Key name that uniquely identifies a signed code image in your bucket.

    - **signingMaterial** *(dict) --*

      A ``SigningMaterial`` object that contains the Amazon Resource Name (ARN) of the
      certificate used for the signing job.

      - **certificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

    - **createdAt** *(datetime) --*

      The date and time that the signing job was created.

    - **status** *(string) --*

      The status of the signing job.
    """


_ClientListSigningJobsResponseTypeDef = TypedDict(
    "_ClientListSigningJobsResponseTypeDef",
    {"jobs": List[ClientListSigningJobsResponsejobsTypeDef], "nextToken": str},
    total=False,
)


class ClientListSigningJobsResponseTypeDef(_ClientListSigningJobsResponseTypeDef):
    """
    Type definition for `ClientListSigningJobs` `Response`

    - **jobs** *(list) --*

      A list of your signing jobs.

      - *(dict) --*

        Contains information about a signing job.

        - **jobId** *(string) --*

          The ID of the signing job.

        - **source** *(dict) --*

          A ``Source`` that contains information about a signing job's code image source.

          - **s3** *(dict) --*

            The ``S3Source`` object.

            - **bucketName** *(string) --*

              Name of the S3 bucket.

            - **key** *(string) --*

              Key name of the bucket object that contains your unsigned code.

            - **version** *(string) --*

              Version of your source image in your version enabled S3 bucket.

        - **signedObject** *(dict) --*

          A ``SignedObject`` structure that contains information about a signing job's signed code
          image.

          - **s3** *(dict) --*

            The ``S3SignedObject`` .

            - **bucketName** *(string) --*

              Name of the S3 bucket.

            - **key** *(string) --*

              Key name that uniquely identifies a signed code image in your bucket.

        - **signingMaterial** *(dict) --*

          A ``SigningMaterial`` object that contains the Amazon Resource Name (ARN) of the
          certificate used for the signing job.

          - **certificateArn** *(string) --*

            The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

        - **createdAt** *(datetime) --*

          The date and time that the signing job was created.

        - **status** *(string) --*

          The status of the signing job.

    - **nextToken** *(string) --*

      String for specifying the next set of paginated results.
    """


_ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[str], "defaultValue": str},
    total=False,
)


class ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef(
    _ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef
):
    """
    Type definition for `ClientListSigningPlatformsResponseplatformssigningConfiguration` `encryptionAlgorithmOptions`

    The encryption algorithm options that are available for a code signing job.

    - **allowedValues** *(list) --*

      The set of accepted encryption algorithms that are allowed in a code signing job.

      - *(string) --*

    - **defaultValue** *(string) --*

      The default encryption algorithm that is used by a code signing job.
    """


_ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[str], "defaultValue": str},
    total=False,
)


class ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef(
    _ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef
):
    """
    Type definition for `ClientListSigningPlatformsResponseplatformssigningConfiguration` `hashAlgorithmOptions`

    The hash algorithm options that are available for a a code signing job.

    - **allowedValues** *(list) --*

      The set of accepted hash algorithms allowed in a code signing job.

      - *(string) --*

    - **defaultValue** *(string) --*

      The default hash algorithm that is used in a code signing job.
    """


_ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)


class ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef(
    _ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef
):
    """
    Type definition for `ClientListSigningPlatformsResponseplatforms` `signingConfiguration`

    The configuration of a code signing platform. This includes the designated hash algorithm
    and encryption algorithm of a signing platform.

    - **encryptionAlgorithmOptions** *(dict) --*

      The encryption algorithm options that are available for a code signing job.

      - **allowedValues** *(list) --*

        The set of accepted encryption algorithms that are allowed in a code signing job.

        - *(string) --*

      - **defaultValue** *(string) --*

        The default encryption algorithm that is used by a code signing job.

    - **hashAlgorithmOptions** *(dict) --*

      The hash algorithm options that are available for a a code signing job.

      - **allowedValues** *(list) --*

        The set of accepted hash algorithms allowed in a code signing job.

        - *(string) --*

      - **defaultValue** *(string) --*

        The default hash algorithm that is used in a code signing job.
    """


_ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)


class ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef(
    _ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef
):
    """
    Type definition for `ClientListSigningPlatformsResponseplatforms` `signingImageFormat`

    The image format of a code signing platform or profile.

    - **supportedFormats** *(list) --*

      The supported formats of a code signing signing image.

      - *(string) --*

    - **defaultFormat** *(string) --*

      The default format of a code signing signing image.
    """


_ClientListSigningPlatformsResponseplatformsTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseplatformsTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": str,
        "signingConfiguration": ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef,
        "signingImageFormat": ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef,
        "maxSizeInMB": int,
    },
    total=False,
)


class ClientListSigningPlatformsResponseplatformsTypeDef(
    _ClientListSigningPlatformsResponseplatformsTypeDef
):
    """
    Type definition for `ClientListSigningPlatformsResponse` `platforms`

    Contains information about the signing configurations and parameters that is used to
    perform a code signing job.

    - **platformId** *(string) --*

      The ID of a code signing; platform.

    - **displayName** *(string) --*

      The display name of a code signing platform.

    - **partner** *(string) --*

      Any partner entities linked to a code signing platform.

    - **target** *(string) --*

      The types of targets that can be signed by a code signing platform.

    - **category** *(string) --*

      The category of a code signing platform.

    - **signingConfiguration** *(dict) --*

      The configuration of a code signing platform. This includes the designated hash algorithm
      and encryption algorithm of a signing platform.

      - **encryptionAlgorithmOptions** *(dict) --*

        The encryption algorithm options that are available for a code signing job.

        - **allowedValues** *(list) --*

          The set of accepted encryption algorithms that are allowed in a code signing job.

          - *(string) --*

        - **defaultValue** *(string) --*

          The default encryption algorithm that is used by a code signing job.

      - **hashAlgorithmOptions** *(dict) --*

        The hash algorithm options that are available for a a code signing job.

        - **allowedValues** *(list) --*

          The set of accepted hash algorithms allowed in a code signing job.

          - *(string) --*

        - **defaultValue** *(string) --*

          The default hash algorithm that is used in a code signing job.

    - **signingImageFormat** *(dict) --*

      The image format of a code signing platform or profile.

      - **supportedFormats** *(list) --*

        The supported formats of a code signing signing image.

        - *(string) --*

      - **defaultFormat** *(string) --*

        The default format of a code signing signing image.

    - **maxSizeInMB** *(integer) --*

      The maximum size (in MB) of code that can be signed by a code signing platform.
    """


_ClientListSigningPlatformsResponseTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseTypeDef",
    {
        "platforms": List[ClientListSigningPlatformsResponseplatformsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListSigningPlatformsResponseTypeDef(
    _ClientListSigningPlatformsResponseTypeDef
):
    """
    Type definition for `ClientListSigningPlatforms` `Response`

    - **platforms** *(list) --*

      A list of all platforms that match the request parameters.

      - *(dict) --*

        Contains information about the signing configurations and parameters that is used to
        perform a code signing job.

        - **platformId** *(string) --*

          The ID of a code signing; platform.

        - **displayName** *(string) --*

          The display name of a code signing platform.

        - **partner** *(string) --*

          Any partner entities linked to a code signing platform.

        - **target** *(string) --*

          The types of targets that can be signed by a code signing platform.

        - **category** *(string) --*

          The category of a code signing platform.

        - **signingConfiguration** *(dict) --*

          The configuration of a code signing platform. This includes the designated hash algorithm
          and encryption algorithm of a signing platform.

          - **encryptionAlgorithmOptions** *(dict) --*

            The encryption algorithm options that are available for a code signing job.

            - **allowedValues** *(list) --*

              The set of accepted encryption algorithms that are allowed in a code signing job.

              - *(string) --*

            - **defaultValue** *(string) --*

              The default encryption algorithm that is used by a code signing job.

          - **hashAlgorithmOptions** *(dict) --*

            The hash algorithm options that are available for a a code signing job.

            - **allowedValues** *(list) --*

              The set of accepted hash algorithms allowed in a code signing job.

              - *(string) --*

            - **defaultValue** *(string) --*

              The default hash algorithm that is used in a code signing job.

        - **signingImageFormat** *(dict) --*

          The image format of a code signing platform or profile.

          - **supportedFormats** *(list) --*

            The supported formats of a code signing signing image.

            - *(string) --*

          - **defaultFormat** *(string) --*

            The default format of a code signing signing image.

        - **maxSizeInMB** *(integer) --*

          The maximum size (in MB) of code that can be signed by a code signing platform.

    - **nextToken** *(string) --*

      Value for specifying the next set of paginated results to return.
    """


_ClientListSigningProfilesResponseprofilessigningMaterialTypeDef = TypedDict(
    "_ClientListSigningProfilesResponseprofilessigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)


class ClientListSigningProfilesResponseprofilessigningMaterialTypeDef(
    _ClientListSigningProfilesResponseprofilessigningMaterialTypeDef
):
    """
    Type definition for `ClientListSigningProfilesResponseprofiles` `signingMaterial`

    The ACM certificate that is available for use by a signing profile.

    - **certificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificates that is used to sign your code.
    """


_ClientListSigningProfilesResponseprofilesTypeDef = TypedDict(
    "_ClientListSigningProfilesResponseprofilesTypeDef",
    {
        "profileName": str,
        "signingMaterial": ClientListSigningProfilesResponseprofilessigningMaterialTypeDef,
        "platformId": str,
        "signingParameters": Dict[str, str],
        "status": str,
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientListSigningProfilesResponseprofilesTypeDef(
    _ClientListSigningProfilesResponseprofilesTypeDef
):
    """
    Type definition for `ClientListSigningProfilesResponse` `profiles`

    Contains information about the ACM certificates and code signing configuration parameters
    that can be used by a given code signing user.

    - **profileName** *(string) --*

      The name of the signing profile.

    - **signingMaterial** *(dict) --*

      The ACM certificate that is available for use by a signing profile.

      - **certificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

    - **platformId** *(string) --*

      The ID of a platform that is available for use by a signing profile.

    - **signingParameters** *(dict) --*

      The parameters that are available for use by a code signing user.

      - *(string) --*

        - *(string) --*

    - **status** *(string) --*

      The status of a code signing profile.

    - **arn** *(string) --*

      Amazon Resource Name (ARN) for the signing profile.

    - **tags** *(dict) --*

      A list of tags associated with the signing profile.

      - *(string) --*

        - *(string) --*
    """


_ClientListSigningProfilesResponseTypeDef = TypedDict(
    "_ClientListSigningProfilesResponseTypeDef",
    {
        "profiles": List[ClientListSigningProfilesResponseprofilesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListSigningProfilesResponseTypeDef(
    _ClientListSigningProfilesResponseTypeDef
):
    """
    Type definition for `ClientListSigningProfiles` `Response`

    - **profiles** *(list) --*

      A list of profiles that are available in the AWS account. This includes profiles with the
      status of ``CANCELED`` if the ``includeCanceled`` parameter is set to ``true`` .

      - *(dict) --*

        Contains information about the ACM certificates and code signing configuration parameters
        that can be used by a given code signing user.

        - **profileName** *(string) --*

          The name of the signing profile.

        - **signingMaterial** *(dict) --*

          The ACM certificate that is available for use by a signing profile.

          - **certificateArn** *(string) --*

            The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

        - **platformId** *(string) --*

          The ID of a platform that is available for use by a signing profile.

        - **signingParameters** *(dict) --*

          The parameters that are available for use by a code signing user.

          - *(string) --*

            - *(string) --*

        - **status** *(string) --*

          The status of a code signing profile.

        - **arn** *(string) --*

          Amazon Resource Name (ARN) for the signing profile.

        - **tags** *(dict) --*

          A list of tags associated with the signing profile.

          - *(string) --*

            - *(string) --*

    - **nextToken** *(string) --*

      Value for specifying the next set of paginated results to return.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(dict) --*

      A list of tags associated with the signing profile.

      - *(string) --*

        - *(string) --*
    """


_ClientPutSigningProfileResponseTypeDef = TypedDict(
    "_ClientPutSigningProfileResponseTypeDef", {"arn": str}, total=False
)


class ClientPutSigningProfileResponseTypeDef(_ClientPutSigningProfileResponseTypeDef):
    """
    Type definition for `ClientPutSigningProfile` `Response`

    - **arn** *(string) --*

      The Amazon Resource Name (ARN) of the signing profile created.
    """


_ClientPutSigningProfileoverridessigningConfigurationTypeDef = TypedDict(
    "_ClientPutSigningProfileoverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": str, "hashAlgorithm": str},
    total=False,
)


class ClientPutSigningProfileoverridessigningConfigurationTypeDef(
    _ClientPutSigningProfileoverridessigningConfigurationTypeDef
):
    """
    Type definition for `ClientPutSigningProfileoverrides` `signingConfiguration`

    A signing configuration that overrides the default encryption or hash algorithm of a signing
    job.

    - **encryptionAlgorithm** *(string) --*

      A specified override of the default encryption algorithm that is used in a code signing job.

    - **hashAlgorithm** *(string) --*

      A specified override of the default hash algorithm that is used in a code signing job.
    """


_ClientPutSigningProfileoverridesTypeDef = TypedDict(
    "_ClientPutSigningProfileoverridesTypeDef",
    {
        "signingConfiguration": ClientPutSigningProfileoverridessigningConfigurationTypeDef
    },
    total=False,
)


class ClientPutSigningProfileoverridesTypeDef(_ClientPutSigningProfileoverridesTypeDef):
    """
    Type definition for `ClientPutSigningProfile` `overrides`

    A subfield of ``platform`` . This specifies any different configuration options that you want to
    apply to the chosen platform (such as a different ``hash-algorithm`` or ``signing-algorithm`` ).

    - **signingConfiguration** *(dict) --*

      A signing configuration that overrides the default encryption or hash algorithm of a signing
      job.

      - **encryptionAlgorithm** *(string) --*

        A specified override of the default encryption algorithm that is used in a code signing job.

      - **hashAlgorithm** *(string) --*

        A specified override of the default hash algorithm that is used in a code signing job.
    """


_ClientPutSigningProfilesigningMaterialTypeDef = TypedDict(
    "_ClientPutSigningProfilesigningMaterialTypeDef", {"certificateArn": str}
)


class ClientPutSigningProfilesigningMaterialTypeDef(
    _ClientPutSigningProfilesigningMaterialTypeDef
):
    """
    Type definition for `ClientPutSigningProfile` `signingMaterial`

    The AWS Certificate Manager certificate that will be used to sign code with the new signing
    profile.

    - **certificateArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the certificates that is used to sign your code.
    """


_ClientStartSigningJobResponseTypeDef = TypedDict(
    "_ClientStartSigningJobResponseTypeDef", {"jobId": str}, total=False
)


class ClientStartSigningJobResponseTypeDef(_ClientStartSigningJobResponseTypeDef):
    """
    Type definition for `ClientStartSigningJob` `Response`

    - **jobId** *(string) --*

      The ID of your signing job.
    """


_ClientStartSigningJobdestinations3TypeDef = TypedDict(
    "_ClientStartSigningJobdestinations3TypeDef",
    {"bucketName": str, "prefix": str},
    total=False,
)


class ClientStartSigningJobdestinations3TypeDef(
    _ClientStartSigningJobdestinations3TypeDef
):
    """
    Type definition for `ClientStartSigningJobdestination` `s3`

    The ``S3Destination`` object.

    - **bucketName** *(string) --*

      Name of the S3 bucket.

    - **prefix** *(string) --*

      An Amazon S3 prefix that you can use to limit responses to those that begin with the
      specified prefix.
    """


_ClientStartSigningJobdestinationTypeDef = TypedDict(
    "_ClientStartSigningJobdestinationTypeDef",
    {"s3": ClientStartSigningJobdestinations3TypeDef},
    total=False,
)


class ClientStartSigningJobdestinationTypeDef(_ClientStartSigningJobdestinationTypeDef):
    """
    Type definition for `ClientStartSigningJob` `destination`

    The S3 bucket in which to save your signed object. The destination contains the name of your
    bucket and an optional prefix.

    - **s3** *(dict) --*

      The ``S3Destination`` object.

      - **bucketName** *(string) --*

        Name of the S3 bucket.

      - **prefix** *(string) --*

        An Amazon S3 prefix that you can use to limit responses to those that begin with the
        specified prefix.
    """


_ClientStartSigningJobsources3TypeDef = TypedDict(
    "_ClientStartSigningJobsources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
)


class ClientStartSigningJobsources3TypeDef(_ClientStartSigningJobsources3TypeDef):
    """
    Type definition for `ClientStartSigningJobsource` `s3`

    The ``S3Source`` object.

    - **bucketName** *(string) --* **[REQUIRED]**

      Name of the S3 bucket.

    - **key** *(string) --* **[REQUIRED]**

      Key name of the bucket object that contains your unsigned code.

    - **version** *(string) --* **[REQUIRED]**

      Version of your source image in your version enabled S3 bucket.
    """


_ClientStartSigningJobsourceTypeDef = TypedDict(
    "_ClientStartSigningJobsourceTypeDef",
    {"s3": ClientStartSigningJobsources3TypeDef},
    total=False,
)


class ClientStartSigningJobsourceTypeDef(_ClientStartSigningJobsourceTypeDef):
    """
    Type definition for `ClientStartSigningJob` `source`

    The S3 bucket that contains the object to sign or a BLOB that contains your raw code.

    - **s3** *(dict) --*

      The ``S3Source`` object.

      - **bucketName** *(string) --* **[REQUIRED]**

        Name of the S3 bucket.

      - **key** *(string) --* **[REQUIRED]**

        Key name of the bucket object that contains your unsigned code.

      - **version** *(string) --* **[REQUIRED]**

        Version of your source image in your version enabled S3 bucket.
    """


_ListSigningJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSigningJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSigningJobsPaginatePaginationConfigTypeDef(
    _ListSigningJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSigningJobsPaginate` `PaginationConfig`

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


_ListSigningJobsPaginateResponsejobssignedObjects3TypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobssignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)


class ListSigningJobsPaginateResponsejobssignedObjects3TypeDef(
    _ListSigningJobsPaginateResponsejobssignedObjects3TypeDef
):
    """
    Type definition for `ListSigningJobsPaginateResponsejobssignedObject` `s3`

    The ``S3SignedObject`` .

    - **bucketName** *(string) --*

      Name of the S3 bucket.

    - **key** *(string) --*

      Key name that uniquely identifies a signed code image in your bucket.
    """


_ListSigningJobsPaginateResponsejobssignedObjectTypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobssignedObjectTypeDef",
    {"s3": ListSigningJobsPaginateResponsejobssignedObjects3TypeDef},
    total=False,
)


class ListSigningJobsPaginateResponsejobssignedObjectTypeDef(
    _ListSigningJobsPaginateResponsejobssignedObjectTypeDef
):
    """
    Type definition for `ListSigningJobsPaginateResponsejobs` `signedObject`

    A ``SignedObject`` structure that contains information about a signing job's signed code
    image.

    - **s3** *(dict) --*

      The ``S3SignedObject`` .

      - **bucketName** *(string) --*

        Name of the S3 bucket.

      - **key** *(string) --*

        Key name that uniquely identifies a signed code image in your bucket.
    """


_ListSigningJobsPaginateResponsejobssigningMaterialTypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobssigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)


class ListSigningJobsPaginateResponsejobssigningMaterialTypeDef(
    _ListSigningJobsPaginateResponsejobssigningMaterialTypeDef
):
    """
    Type definition for `ListSigningJobsPaginateResponsejobs` `signingMaterial`

    A ``SigningMaterial`` object that contains the Amazon Resource Name (ARN) of the
    certificate used for the signing job.

    - **certificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificates that is used to sign your code.
    """


_ListSigningJobsPaginateResponsejobssources3TypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobssources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)


class ListSigningJobsPaginateResponsejobssources3TypeDef(
    _ListSigningJobsPaginateResponsejobssources3TypeDef
):
    """
    Type definition for `ListSigningJobsPaginateResponsejobssource` `s3`

    The ``S3Source`` object.

    - **bucketName** *(string) --*

      Name of the S3 bucket.

    - **key** *(string) --*

      Key name of the bucket object that contains your unsigned code.

    - **version** *(string) --*

      Version of your source image in your version enabled S3 bucket.
    """


_ListSigningJobsPaginateResponsejobssourceTypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobssourceTypeDef",
    {"s3": ListSigningJobsPaginateResponsejobssources3TypeDef},
    total=False,
)


class ListSigningJobsPaginateResponsejobssourceTypeDef(
    _ListSigningJobsPaginateResponsejobssourceTypeDef
):
    """
    Type definition for `ListSigningJobsPaginateResponsejobs` `source`

    A ``Source`` that contains information about a signing job's code image source.

    - **s3** *(dict) --*

      The ``S3Source`` object.

      - **bucketName** *(string) --*

        Name of the S3 bucket.

      - **key** *(string) --*

        Key name of the bucket object that contains your unsigned code.

      - **version** *(string) --*

        Version of your source image in your version enabled S3 bucket.
    """


_ListSigningJobsPaginateResponsejobsTypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobsTypeDef",
    {
        "jobId": str,
        "source": ListSigningJobsPaginateResponsejobssourceTypeDef,
        "signedObject": ListSigningJobsPaginateResponsejobssignedObjectTypeDef,
        "signingMaterial": ListSigningJobsPaginateResponsejobssigningMaterialTypeDef,
        "createdAt": datetime,
        "status": str,
    },
    total=False,
)


class ListSigningJobsPaginateResponsejobsTypeDef(
    _ListSigningJobsPaginateResponsejobsTypeDef
):
    """
    Type definition for `ListSigningJobsPaginateResponse` `jobs`

    Contains information about a signing job.

    - **jobId** *(string) --*

      The ID of the signing job.

    - **source** *(dict) --*

      A ``Source`` that contains information about a signing job's code image source.

      - **s3** *(dict) --*

        The ``S3Source`` object.

        - **bucketName** *(string) --*

          Name of the S3 bucket.

        - **key** *(string) --*

          Key name of the bucket object that contains your unsigned code.

        - **version** *(string) --*

          Version of your source image in your version enabled S3 bucket.

    - **signedObject** *(dict) --*

      A ``SignedObject`` structure that contains information about a signing job's signed code
      image.

      - **s3** *(dict) --*

        The ``S3SignedObject`` .

        - **bucketName** *(string) --*

          Name of the S3 bucket.

        - **key** *(string) --*

          Key name that uniquely identifies a signed code image in your bucket.

    - **signingMaterial** *(dict) --*

      A ``SigningMaterial`` object that contains the Amazon Resource Name (ARN) of the
      certificate used for the signing job.

      - **certificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

    - **createdAt** *(datetime) --*

      The date and time that the signing job was created.

    - **status** *(string) --*

      The status of the signing job.
    """


_ListSigningJobsPaginateResponseTypeDef = TypedDict(
    "_ListSigningJobsPaginateResponseTypeDef",
    {"jobs": List[ListSigningJobsPaginateResponsejobsTypeDef], "NextToken": str},
    total=False,
)


class ListSigningJobsPaginateResponseTypeDef(_ListSigningJobsPaginateResponseTypeDef):
    """
    Type definition for `ListSigningJobsPaginate` `Response`

    - **jobs** *(list) --*

      A list of your signing jobs.

      - *(dict) --*

        Contains information about a signing job.

        - **jobId** *(string) --*

          The ID of the signing job.

        - **source** *(dict) --*

          A ``Source`` that contains information about a signing job's code image source.

          - **s3** *(dict) --*

            The ``S3Source`` object.

            - **bucketName** *(string) --*

              Name of the S3 bucket.

            - **key** *(string) --*

              Key name of the bucket object that contains your unsigned code.

            - **version** *(string) --*

              Version of your source image in your version enabled S3 bucket.

        - **signedObject** *(dict) --*

          A ``SignedObject`` structure that contains information about a signing job's signed code
          image.

          - **s3** *(dict) --*

            The ``S3SignedObject`` .

            - **bucketName** *(string) --*

              Name of the S3 bucket.

            - **key** *(string) --*

              Key name that uniquely identifies a signed code image in your bucket.

        - **signingMaterial** *(dict) --*

          A ``SigningMaterial`` object that contains the Amazon Resource Name (ARN) of the
          certificate used for the signing job.

          - **certificateArn** *(string) --*

            The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

        - **createdAt** *(datetime) --*

          The date and time that the signing job was created.

        - **status** *(string) --*

          The status of the signing job.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSigningPlatformsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSigningPlatformsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSigningPlatformsPaginatePaginationConfigTypeDef(
    _ListSigningPlatformsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSigningPlatformsPaginate` `PaginationConfig`

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


_ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[str], "defaultValue": str},
    total=False,
)


class ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef(
    _ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef
):
    """
    Type definition for `ListSigningPlatformsPaginateResponseplatformssigningConfiguration` `encryptionAlgorithmOptions`

    The encryption algorithm options that are available for a code signing job.

    - **allowedValues** *(list) --*

      The set of accepted encryption algorithms that are allowed in a code signing job.

      - *(string) --*

    - **defaultValue** *(string) --*

      The default encryption algorithm that is used by a code signing job.
    """


_ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[str], "defaultValue": str},
    total=False,
)


class ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef(
    _ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef
):
    """
    Type definition for `ListSigningPlatformsPaginateResponseplatformssigningConfiguration` `hashAlgorithmOptions`

    The hash algorithm options that are available for a a code signing job.

    - **allowedValues** *(list) --*

      The set of accepted hash algorithms allowed in a code signing job.

      - *(string) --*

    - **defaultValue** *(string) --*

      The default hash algorithm that is used in a code signing job.
    """


_ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)


class ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef(
    _ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef
):
    """
    Type definition for `ListSigningPlatformsPaginateResponseplatforms` `signingConfiguration`

    The configuration of a code signing platform. This includes the designated hash algorithm
    and encryption algorithm of a signing platform.

    - **encryptionAlgorithmOptions** *(dict) --*

      The encryption algorithm options that are available for a code signing job.

      - **allowedValues** *(list) --*

        The set of accepted encryption algorithms that are allowed in a code signing job.

        - *(string) --*

      - **defaultValue** *(string) --*

        The default encryption algorithm that is used by a code signing job.

    - **hashAlgorithmOptions** *(dict) --*

      The hash algorithm options that are available for a a code signing job.

      - **allowedValues** *(list) --*

        The set of accepted hash algorithms allowed in a code signing job.

        - *(string) --*

      - **defaultValue** *(string) --*

        The default hash algorithm that is used in a code signing job.
    """


_ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)


class ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef(
    _ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef
):
    """
    Type definition for `ListSigningPlatformsPaginateResponseplatforms` `signingImageFormat`

    The image format of a code signing platform or profile.

    - **supportedFormats** *(list) --*

      The supported formats of a code signing signing image.

      - *(string) --*

    - **defaultFormat** *(string) --*

      The default format of a code signing signing image.
    """


_ListSigningPlatformsPaginateResponseplatformsTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseplatformsTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": str,
        "signingConfiguration": ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef,
        "signingImageFormat": ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef,
        "maxSizeInMB": int,
    },
    total=False,
)


class ListSigningPlatformsPaginateResponseplatformsTypeDef(
    _ListSigningPlatformsPaginateResponseplatformsTypeDef
):
    """
    Type definition for `ListSigningPlatformsPaginateResponse` `platforms`

    Contains information about the signing configurations and parameters that is used to
    perform a code signing job.

    - **platformId** *(string) --*

      The ID of a code signing; platform.

    - **displayName** *(string) --*

      The display name of a code signing platform.

    - **partner** *(string) --*

      Any partner entities linked to a code signing platform.

    - **target** *(string) --*

      The types of targets that can be signed by a code signing platform.

    - **category** *(string) --*

      The category of a code signing platform.

    - **signingConfiguration** *(dict) --*

      The configuration of a code signing platform. This includes the designated hash algorithm
      and encryption algorithm of a signing platform.

      - **encryptionAlgorithmOptions** *(dict) --*

        The encryption algorithm options that are available for a code signing job.

        - **allowedValues** *(list) --*

          The set of accepted encryption algorithms that are allowed in a code signing job.

          - *(string) --*

        - **defaultValue** *(string) --*

          The default encryption algorithm that is used by a code signing job.

      - **hashAlgorithmOptions** *(dict) --*

        The hash algorithm options that are available for a a code signing job.

        - **allowedValues** *(list) --*

          The set of accepted hash algorithms allowed in a code signing job.

          - *(string) --*

        - **defaultValue** *(string) --*

          The default hash algorithm that is used in a code signing job.

    - **signingImageFormat** *(dict) --*

      The image format of a code signing platform or profile.

      - **supportedFormats** *(list) --*

        The supported formats of a code signing signing image.

        - *(string) --*

      - **defaultFormat** *(string) --*

        The default format of a code signing signing image.

    - **maxSizeInMB** *(integer) --*

      The maximum size (in MB) of code that can be signed by a code signing platform.
    """


_ListSigningPlatformsPaginateResponseTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseTypeDef",
    {
        "platforms": List[ListSigningPlatformsPaginateResponseplatformsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListSigningPlatformsPaginateResponseTypeDef(
    _ListSigningPlatformsPaginateResponseTypeDef
):
    """
    Type definition for `ListSigningPlatformsPaginate` `Response`

    - **platforms** *(list) --*

      A list of all platforms that match the request parameters.

      - *(dict) --*

        Contains information about the signing configurations and parameters that is used to
        perform a code signing job.

        - **platformId** *(string) --*

          The ID of a code signing; platform.

        - **displayName** *(string) --*

          The display name of a code signing platform.

        - **partner** *(string) --*

          Any partner entities linked to a code signing platform.

        - **target** *(string) --*

          The types of targets that can be signed by a code signing platform.

        - **category** *(string) --*

          The category of a code signing platform.

        - **signingConfiguration** *(dict) --*

          The configuration of a code signing platform. This includes the designated hash algorithm
          and encryption algorithm of a signing platform.

          - **encryptionAlgorithmOptions** *(dict) --*

            The encryption algorithm options that are available for a code signing job.

            - **allowedValues** *(list) --*

              The set of accepted encryption algorithms that are allowed in a code signing job.

              - *(string) --*

            - **defaultValue** *(string) --*

              The default encryption algorithm that is used by a code signing job.

          - **hashAlgorithmOptions** *(dict) --*

            The hash algorithm options that are available for a a code signing job.

            - **allowedValues** *(list) --*

              The set of accepted hash algorithms allowed in a code signing job.

              - *(string) --*

            - **defaultValue** *(string) --*

              The default hash algorithm that is used in a code signing job.

        - **signingImageFormat** *(dict) --*

          The image format of a code signing platform or profile.

          - **supportedFormats** *(list) --*

            The supported formats of a code signing signing image.

            - *(string) --*

          - **defaultFormat** *(string) --*

            The default format of a code signing signing image.

        - **maxSizeInMB** *(integer) --*

          The maximum size (in MB) of code that can be signed by a code signing platform.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSigningProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSigningProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSigningProfilesPaginatePaginationConfigTypeDef(
    _ListSigningProfilesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSigningProfilesPaginate` `PaginationConfig`

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


_ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef = TypedDict(
    "_ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)


class ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef(
    _ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef
):
    """
    Type definition for `ListSigningProfilesPaginateResponseprofiles` `signingMaterial`

    The ACM certificate that is available for use by a signing profile.

    - **certificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificates that is used to sign your code.
    """


_ListSigningProfilesPaginateResponseprofilesTypeDef = TypedDict(
    "_ListSigningProfilesPaginateResponseprofilesTypeDef",
    {
        "profileName": str,
        "signingMaterial": ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef,
        "platformId": str,
        "signingParameters": Dict[str, str],
        "status": str,
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ListSigningProfilesPaginateResponseprofilesTypeDef(
    _ListSigningProfilesPaginateResponseprofilesTypeDef
):
    """
    Type definition for `ListSigningProfilesPaginateResponse` `profiles`

    Contains information about the ACM certificates and code signing configuration parameters
    that can be used by a given code signing user.

    - **profileName** *(string) --*

      The name of the signing profile.

    - **signingMaterial** *(dict) --*

      The ACM certificate that is available for use by a signing profile.

      - **certificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

    - **platformId** *(string) --*

      The ID of a platform that is available for use by a signing profile.

    - **signingParameters** *(dict) --*

      The parameters that are available for use by a code signing user.

      - *(string) --*

        - *(string) --*

    - **status** *(string) --*

      The status of a code signing profile.

    - **arn** *(string) --*

      Amazon Resource Name (ARN) for the signing profile.

    - **tags** *(dict) --*

      A list of tags associated with the signing profile.

      - *(string) --*

        - *(string) --*
    """


_ListSigningProfilesPaginateResponseTypeDef = TypedDict(
    "_ListSigningProfilesPaginateResponseTypeDef",
    {
        "profiles": List[ListSigningProfilesPaginateResponseprofilesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListSigningProfilesPaginateResponseTypeDef(
    _ListSigningProfilesPaginateResponseTypeDef
):
    """
    Type definition for `ListSigningProfilesPaginate` `Response`

    - **profiles** *(list) --*

      A list of profiles that are available in the AWS account. This includes profiles with the
      status of ``CANCELED`` if the ``includeCanceled`` parameter is set to ``true`` .

      - *(dict) --*

        Contains information about the ACM certificates and code signing configuration parameters
        that can be used by a given code signing user.

        - **profileName** *(string) --*

          The name of the signing profile.

        - **signingMaterial** *(dict) --*

          The ACM certificate that is available for use by a signing profile.

          - **certificateArn** *(string) --*

            The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

        - **platformId** *(string) --*

          The ID of a platform that is available for use by a signing profile.

        - **signingParameters** *(dict) --*

          The parameters that are available for use by a code signing user.

          - *(string) --*

            - *(string) --*

        - **status** *(string) --*

          The status of a code signing profile.

        - **arn** *(string) --*

          Amazon Resource Name (ARN) for the signing profile.

        - **tags** *(dict) --*

          A list of tags associated with the signing profile.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_SuccessfulSigningJobWaitWaiterConfigTypeDef = TypedDict(
    "_SuccessfulSigningJobWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class SuccessfulSigningJobWaitWaiterConfigTypeDef(
    _SuccessfulSigningJobWaitWaiterConfigTypeDef
):
    """
    Type definition for `SuccessfulSigningJobWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 20

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 25
    """
