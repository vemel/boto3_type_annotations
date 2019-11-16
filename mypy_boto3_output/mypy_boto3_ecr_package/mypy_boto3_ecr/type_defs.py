"Main interface for ecr type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef",
    "ClientBatchCheckLayerAvailabilityResponselayersTypeDef",
    "ClientBatchCheckLayerAvailabilityResponseTypeDef",
    "ClientBatchDeleteImageResponsefailuresimageIdTypeDef",
    "ClientBatchDeleteImageResponsefailuresTypeDef",
    "ClientBatchDeleteImageResponseimageIdsTypeDef",
    "ClientBatchDeleteImageResponseTypeDef",
    "ClientBatchDeleteImageimageIdsTypeDef",
    "ClientBatchGetImageResponsefailuresimageIdTypeDef",
    "ClientBatchGetImageResponsefailuresTypeDef",
    "ClientBatchGetImageResponseimagesimageIdTypeDef",
    "ClientBatchGetImageResponseimagesTypeDef",
    "ClientBatchGetImageResponseTypeDef",
    "ClientBatchGetImageimageIdsTypeDef",
    "ClientCompleteLayerUploadResponseTypeDef",
    "ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    "ClientCreateRepositoryResponserepositoryTypeDef",
    "ClientCreateRepositoryResponseTypeDef",
    "ClientCreateRepositoryimageScanningConfigurationTypeDef",
    "ClientCreateRepositorytagsTypeDef",
    "ClientDeleteLifecyclePolicyResponseTypeDef",
    "ClientDeleteRepositoryPolicyResponseTypeDef",
    "ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    "ClientDeleteRepositoryResponserepositoryTypeDef",
    "ClientDeleteRepositoryResponseTypeDef",
    "ClientDescribeImageScanFindingsResponseimageIdTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef",
    "ClientDescribeImageScanFindingsResponseTypeDef",
    "ClientDescribeImageScanFindingsimageIdTypeDef",
    "ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef",
    "ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef",
    "ClientDescribeImagesResponseimageDetailsTypeDef",
    "ClientDescribeImagesResponseTypeDef",
    "ClientDescribeImagesfilterTypeDef",
    "ClientDescribeImagesimageIdsTypeDef",
    "ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef",
    "ClientDescribeRepositoriesResponserepositoriesTypeDef",
    "ClientDescribeRepositoriesResponseTypeDef",
    "ClientGetAuthorizationTokenResponseauthorizationDataTypeDef",
    "ClientGetAuthorizationTokenResponseTypeDef",
    "ClientGetDownloadUrlForLayerResponseTypeDef",
    "ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef",
    "ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef",
    "ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef",
    "ClientGetLifecyclePolicyPreviewResponseTypeDef",
    "ClientGetLifecyclePolicyPreviewfilterTypeDef",
    "ClientGetLifecyclePolicyPreviewimageIdsTypeDef",
    "ClientGetLifecyclePolicyResponseTypeDef",
    "ClientGetRepositoryPolicyResponseTypeDef",
    "ClientInitiateLayerUploadResponseTypeDef",
    "ClientListImagesResponseimageIdsTypeDef",
    "ClientListImagesResponseTypeDef",
    "ClientListImagesfilterTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutImageResponseimageimageIdTypeDef",
    "ClientPutImageResponseimageTypeDef",
    "ClientPutImageResponseTypeDef",
    "ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef",
    "ClientPutImageScanningConfigurationResponseTypeDef",
    "ClientPutImageScanningConfigurationimageScanningConfigurationTypeDef",
    "ClientPutImageTagMutabilityResponseTypeDef",
    "ClientPutLifecyclePolicyResponseTypeDef",
    "ClientSetRepositoryPolicyResponseTypeDef",
    "ClientStartImageScanResponseimageIdTypeDef",
    "ClientStartImageScanResponseimageScanStatusTypeDef",
    "ClientStartImageScanResponseTypeDef",
    "ClientStartImageScanimageIdTypeDef",
    "ClientStartLifecyclePolicyPreviewResponseTypeDef",
    "ClientTagResourcetagsTypeDef",
    "ClientUploadLayerPartResponseTypeDef",
    "DescribeImageScanFindingsPaginatePaginationConfigTypeDef",
    "DescribeImageScanFindingsPaginateResponseimageIdTypeDef",
    "DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef",
    "DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef",
    "DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef",
    "DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef",
    "DescribeImageScanFindingsPaginateResponseTypeDef",
    "DescribeImageScanFindingsPaginateimageIdTypeDef",
    "DescribeImagesPaginatePaginationConfigTypeDef",
    "DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef",
    "DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef",
    "DescribeImagesPaginateResponseimageDetailsTypeDef",
    "DescribeImagesPaginateResponseTypeDef",
    "DescribeImagesPaginatefilterTypeDef",
    "DescribeImagesPaginateimageIdsTypeDef",
    "DescribeRepositoriesPaginatePaginationConfigTypeDef",
    "DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef",
    "DescribeRepositoriesPaginateResponserepositoriesTypeDef",
    "DescribeRepositoriesPaginateResponseTypeDef",
    "GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef",
    "GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef",
    "GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef",
    "GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef",
    "GetLifecyclePolicyPreviewPaginateResponseTypeDef",
    "GetLifecyclePolicyPreviewPaginatefilterTypeDef",
    "GetLifecyclePolicyPreviewPaginateimageIdsTypeDef",
    "ListImagesPaginatePaginationConfigTypeDef",
    "ListImagesPaginateResponseimageIdsTypeDef",
    "ListImagesPaginateResponseTypeDef",
    "ListImagesPaginatefilterTypeDef",
)


_ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef = TypedDict(
    "_ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef",
    {"layerDigest": str, "failureCode": str, "failureReason": str},
    total=False,
)


class ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef(
    _ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef
):
    """
    Type definition for `ClientBatchCheckLayerAvailabilityResponse` `failures`

    An object representing an Amazon ECR image layer failure.

    - **layerDigest** *(string) --*

      The layer digest associated with the failure.

    - **failureCode** *(string) --*

      The failure code associated with the failure.

    - **failureReason** *(string) --*

      The reason for the failure.
    """


_ClientBatchCheckLayerAvailabilityResponselayersTypeDef = TypedDict(
    "_ClientBatchCheckLayerAvailabilityResponselayersTypeDef",
    {"layerDigest": str, "layerAvailability": str, "layerSize": int, "mediaType": str},
    total=False,
)


class ClientBatchCheckLayerAvailabilityResponselayersTypeDef(
    _ClientBatchCheckLayerAvailabilityResponselayersTypeDef
):
    """
    Type definition for `ClientBatchCheckLayerAvailabilityResponse` `layers`

    An object representing an Amazon ECR image layer.

    - **layerDigest** *(string) --*

      The ``sha256`` digest of the image layer.

    - **layerAvailability** *(string) --*

      The availability status of the image layer.

    - **layerSize** *(integer) --*

      The size, in bytes, of the image layer.

    - **mediaType** *(string) --*

      The media type of the layer, such as
      ``application/vnd.docker.image.rootfs.diff.tar.gzip`` or
      ``application/vnd.oci.image.layer.v1.tar+gzip`` .
    """


_ClientBatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "_ClientBatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List[ClientBatchCheckLayerAvailabilityResponselayersTypeDef],
        "failures": List[ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef],
    },
    total=False,
)


class ClientBatchCheckLayerAvailabilityResponseTypeDef(
    _ClientBatchCheckLayerAvailabilityResponseTypeDef
):
    """
    Type definition for `ClientBatchCheckLayerAvailability` `Response`

    - **layers** *(list) --*

      A list of image layer objects corresponding to the image layer references in the request.

      - *(dict) --*

        An object representing an Amazon ECR image layer.

        - **layerDigest** *(string) --*

          The ``sha256`` digest of the image layer.

        - **layerAvailability** *(string) --*

          The availability status of the image layer.

        - **layerSize** *(integer) --*

          The size, in bytes, of the image layer.

        - **mediaType** *(string) --*

          The media type of the layer, such as
          ``application/vnd.docker.image.rootfs.diff.tar.gzip`` or
          ``application/vnd.oci.image.layer.v1.tar+gzip`` .

    - **failures** *(list) --*

      Any failures associated with the call.

      - *(dict) --*

        An object representing an Amazon ECR image layer failure.

        - **layerDigest** *(string) --*

          The layer digest associated with the failure.

        - **failureCode** *(string) --*

          The failure code associated with the failure.

        - **failureReason** *(string) --*

          The reason for the failure.
    """


_ClientBatchDeleteImageResponsefailuresimageIdTypeDef = TypedDict(
    "_ClientBatchDeleteImageResponsefailuresimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientBatchDeleteImageResponsefailuresimageIdTypeDef(
    _ClientBatchDeleteImageResponsefailuresimageIdTypeDef
):
    """
    Type definition for `ClientBatchDeleteImageResponsefailures` `imageId`

    The image ID associated with the failure.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientBatchDeleteImageResponsefailuresTypeDef = TypedDict(
    "_ClientBatchDeleteImageResponsefailuresTypeDef",
    {
        "imageId": ClientBatchDeleteImageResponsefailuresimageIdTypeDef,
        "failureCode": str,
        "failureReason": str,
    },
    total=False,
)


class ClientBatchDeleteImageResponsefailuresTypeDef(
    _ClientBatchDeleteImageResponsefailuresTypeDef
):
    """
    Type definition for `ClientBatchDeleteImageResponse` `failures`

    An object representing an Amazon ECR image failure.

    - **imageId** *(dict) --*

      The image ID associated with the failure.

      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.

      - **imageTag** *(string) --*

        The tag used for the image.

    - **failureCode** *(string) --*

      The code associated with the failure.

    - **failureReason** *(string) --*

      The reason for the failure.
    """


_ClientBatchDeleteImageResponseimageIdsTypeDef = TypedDict(
    "_ClientBatchDeleteImageResponseimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientBatchDeleteImageResponseimageIdsTypeDef(
    _ClientBatchDeleteImageResponseimageIdsTypeDef
):
    """
    Type definition for `ClientBatchDeleteImageResponse` `imageIds`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientBatchDeleteImageResponseTypeDef = TypedDict(
    "_ClientBatchDeleteImageResponseTypeDef",
    {
        "imageIds": List[ClientBatchDeleteImageResponseimageIdsTypeDef],
        "failures": List[ClientBatchDeleteImageResponsefailuresTypeDef],
    },
    total=False,
)


class ClientBatchDeleteImageResponseTypeDef(_ClientBatchDeleteImageResponseTypeDef):
    """
    Type definition for `ClientBatchDeleteImage` `Response`

    - **imageIds** *(list) --*

      The image IDs of the deleted images.

      - *(dict) --*

        An object with identifying information for an Amazon ECR image.

        - **imageDigest** *(string) --*

          The ``sha256`` digest of the image manifest.

        - **imageTag** *(string) --*

          The tag used for the image.

    - **failures** *(list) --*

      Any failures associated with the call.

      - *(dict) --*

        An object representing an Amazon ECR image failure.

        - **imageId** *(dict) --*

          The image ID associated with the failure.

          - **imageDigest** *(string) --*

            The ``sha256`` digest of the image manifest.

          - **imageTag** *(string) --*

            The tag used for the image.

        - **failureCode** *(string) --*

          The code associated with the failure.

        - **failureReason** *(string) --*

          The reason for the failure.
    """


_ClientBatchDeleteImageimageIdsTypeDef = TypedDict(
    "_ClientBatchDeleteImageimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientBatchDeleteImageimageIdsTypeDef(_ClientBatchDeleteImageimageIdsTypeDef):
    """
    Type definition for `ClientBatchDeleteImage` `imageIds`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientBatchGetImageResponsefailuresimageIdTypeDef = TypedDict(
    "_ClientBatchGetImageResponsefailuresimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientBatchGetImageResponsefailuresimageIdTypeDef(
    _ClientBatchGetImageResponsefailuresimageIdTypeDef
):
    """
    Type definition for `ClientBatchGetImageResponsefailures` `imageId`

    The image ID associated with the failure.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientBatchGetImageResponsefailuresTypeDef = TypedDict(
    "_ClientBatchGetImageResponsefailuresTypeDef",
    {
        "imageId": ClientBatchGetImageResponsefailuresimageIdTypeDef,
        "failureCode": str,
        "failureReason": str,
    },
    total=False,
)


class ClientBatchGetImageResponsefailuresTypeDef(
    _ClientBatchGetImageResponsefailuresTypeDef
):
    """
    Type definition for `ClientBatchGetImageResponse` `failures`

    An object representing an Amazon ECR image failure.

    - **imageId** *(dict) --*

      The image ID associated with the failure.

      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.

      - **imageTag** *(string) --*

        The tag used for the image.

    - **failureCode** *(string) --*

      The code associated with the failure.

    - **failureReason** *(string) --*

      The reason for the failure.
    """


_ClientBatchGetImageResponseimagesimageIdTypeDef = TypedDict(
    "_ClientBatchGetImageResponseimagesimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientBatchGetImageResponseimagesimageIdTypeDef(
    _ClientBatchGetImageResponseimagesimageIdTypeDef
):
    """
    Type definition for `ClientBatchGetImageResponseimages` `imageId`

    An object containing the image tag and image digest associated with an image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientBatchGetImageResponseimagesTypeDef = TypedDict(
    "_ClientBatchGetImageResponseimagesTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientBatchGetImageResponseimagesimageIdTypeDef,
        "imageManifest": str,
    },
    total=False,
)


class ClientBatchGetImageResponseimagesTypeDef(
    _ClientBatchGetImageResponseimagesTypeDef
):
    """
    Type definition for `ClientBatchGetImageResponse` `images`

    An object representing an Amazon ECR image.

    - **registryId** *(string) --*

      The AWS account ID associated with the registry containing the image.

    - **repositoryName** *(string) --*

      The name of the repository associated with the image.

    - **imageId** *(dict) --*

      An object containing the image tag and image digest associated with an image.

      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.

      - **imageTag** *(string) --*

        The tag used for the image.

    - **imageManifest** *(string) --*

      The image manifest associated with the image.
    """


_ClientBatchGetImageResponseTypeDef = TypedDict(
    "_ClientBatchGetImageResponseTypeDef",
    {
        "images": List[ClientBatchGetImageResponseimagesTypeDef],
        "failures": List[ClientBatchGetImageResponsefailuresTypeDef],
    },
    total=False,
)


class ClientBatchGetImageResponseTypeDef(_ClientBatchGetImageResponseTypeDef):
    """
    Type definition for `ClientBatchGetImage` `Response`

    - **images** *(list) --*

      A list of image objects corresponding to the image references in the request.

      - *(dict) --*

        An object representing an Amazon ECR image.

        - **registryId** *(string) --*

          The AWS account ID associated with the registry containing the image.

        - **repositoryName** *(string) --*

          The name of the repository associated with the image.

        - **imageId** *(dict) --*

          An object containing the image tag and image digest associated with an image.

          - **imageDigest** *(string) --*

            The ``sha256`` digest of the image manifest.

          - **imageTag** *(string) --*

            The tag used for the image.

        - **imageManifest** *(string) --*

          The image manifest associated with the image.

    - **failures** *(list) --*

      Any failures associated with the call.

      - *(dict) --*

        An object representing an Amazon ECR image failure.

        - **imageId** *(dict) --*

          The image ID associated with the failure.

          - **imageDigest** *(string) --*

            The ``sha256`` digest of the image manifest.

          - **imageTag** *(string) --*

            The tag used for the image.

        - **failureCode** *(string) --*

          The code associated with the failure.

        - **failureReason** *(string) --*

          The reason for the failure.
    """


_ClientBatchGetImageimageIdsTypeDef = TypedDict(
    "_ClientBatchGetImageimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientBatchGetImageimageIdsTypeDef(_ClientBatchGetImageimageIdsTypeDef):
    """
    Type definition for `ClientBatchGetImage` `imageIds`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientCompleteLayerUploadResponseTypeDef = TypedDict(
    "_ClientCompleteLayerUploadResponseTypeDef",
    {"registryId": str, "repositoryName": str, "uploadId": str, "layerDigest": str},
    total=False,
)


class ClientCompleteLayerUploadResponseTypeDef(
    _ClientCompleteLayerUploadResponseTypeDef
):
    """
    Type definition for `ClientCompleteLayerUpload` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **uploadId** *(string) --*

      The upload ID associated with the layer.

    - **layerDigest** *(string) --*

      The ``sha256`` digest of the image layer.
    """


_ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef = TypedDict(
    "_ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef(
    _ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef
):
    """
    Type definition for `ClientCreateRepositoryResponserepository` `imageScanningConfiguration`

    The image scanning configuration for a repository.

    - **scanOnPush** *(boolean) --*

      The setting that determines whether images are scanned after being pushed to a
      repository. If set to ``true`` , images will be scanned after being pushed. If this
      parameter is not specified, it will default to ``false`` and images will not be scanned
      unless a scan is manually started with the  StartImageScan API.
    """


_ClientCreateRepositoryResponserepositoryTypeDef = TypedDict(
    "_ClientCreateRepositoryResponserepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": str,
        "imageScanningConfiguration": ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateRepositoryResponserepositoryTypeDef(
    _ClientCreateRepositoryResponserepositoryTypeDef
):
    """
    Type definition for `ClientCreateRepositoryResponse` `repository`

    The repository that was created.

    - **repositoryArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
      ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the
      repository owner, repository namespace, and repository name. For example,
      ``arn:aws:ecr:region:012345678910:repository/test`` .

    - **registryId** *(string) --*

      The AWS account ID associated with the registry that contains the repository.

    - **repositoryName** *(string) --*

      The name of the repository.

    - **repositoryUri** *(string) --*

      The URI for the repository. You can use this URI for Docker ``push`` or ``pull`` operations.

    - **createdAt** *(datetime) --*

      The date and time, in JavaScript date format, when the repository was created.

    - **imageTagMutability** *(string) --*

      The tag mutability setting for the repository.

    - **imageScanningConfiguration** *(dict) --*

      The image scanning configuration for a repository.

      - **scanOnPush** *(boolean) --*

        The setting that determines whether images are scanned after being pushed to a
        repository. If set to ``true`` , images will be scanned after being pushed. If this
        parameter is not specified, it will default to ``false`` and images will not be scanned
        unless a scan is manually started with the  StartImageScan API.
    """


_ClientCreateRepositoryResponseTypeDef = TypedDict(
    "_ClientCreateRepositoryResponseTypeDef",
    {"repository": ClientCreateRepositoryResponserepositoryTypeDef},
    total=False,
)


class ClientCreateRepositoryResponseTypeDef(_ClientCreateRepositoryResponseTypeDef):
    """
    Type definition for `ClientCreateRepository` `Response`

    - **repository** *(dict) --*

      The repository that was created.

      - **repositoryArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
        ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the
        repository owner, repository namespace, and repository name. For example,
        ``arn:aws:ecr:region:012345678910:repository/test`` .

      - **registryId** *(string) --*

        The AWS account ID associated with the registry that contains the repository.

      - **repositoryName** *(string) --*

        The name of the repository.

      - **repositoryUri** *(string) --*

        The URI for the repository. You can use this URI for Docker ``push`` or ``pull`` operations.

      - **createdAt** *(datetime) --*

        The date and time, in JavaScript date format, when the repository was created.

      - **imageTagMutability** *(string) --*

        The tag mutability setting for the repository.

      - **imageScanningConfiguration** *(dict) --*

        The image scanning configuration for a repository.

        - **scanOnPush** *(boolean) --*

          The setting that determines whether images are scanned after being pushed to a
          repository. If set to ``true`` , images will be scanned after being pushed. If this
          parameter is not specified, it will default to ``false`` and images will not be scanned
          unless a scan is manually started with the  StartImageScan API.
    """


_ClientCreateRepositoryimageScanningConfigurationTypeDef = TypedDict(
    "_ClientCreateRepositoryimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientCreateRepositoryimageScanningConfigurationTypeDef(
    _ClientCreateRepositoryimageScanningConfigurationTypeDef
):
    """
    Type definition for `ClientCreateRepository` `imageScanningConfiguration`

    The image scanning configuration for the repository. This setting determines whether images are
    scanned for known vulnerabilities after being pushed to the repository.

    - **scanOnPush** *(boolean) --*

      The setting that determines whether images are scanned after being pushed to a repository. If
      set to ``true`` , images will be scanned after being pushed. If this parameter is not
      specified, it will default to ``false`` and images will not be scanned unless a scan is
      manually started with the  StartImageScan API.
    """


_ClientCreateRepositorytagsTypeDef = TypedDict(
    "_ClientCreateRepositorytagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRepositorytagsTypeDef(_ClientCreateRepositorytagsTypeDef):
    """
    Type definition for `ClientCreateRepository` `tags`

    The metadata that you apply to a resource to help you categorize and organize them. Each tag
    consists of a key and an optional value, both of which you define. Tag keys can have a maximum
    character length of 128 characters, and tag values can have a maximum length of 256 characters.

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
      a category for more specific tag values.

    - **Value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
      within a tag category (key).
    """


_ClientDeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientDeleteLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
    },
    total=False,
)


class ClientDeleteLifecyclePolicyResponseTypeDef(
    _ClientDeleteLifecyclePolicyResponseTypeDef
):
    """
    Type definition for `ClientDeleteLifecyclePolicy` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **lifecyclePolicyText** *(string) --*

      The JSON lifecycle policy text.

    - **lastEvaluatedAt** *(datetime) --*

      The time stamp of the last time that the lifecycle policy was run.
    """


_ClientDeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "_ClientDeleteRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)


class ClientDeleteRepositoryPolicyResponseTypeDef(
    _ClientDeleteRepositoryPolicyResponseTypeDef
):
    """
    Type definition for `ClientDeleteRepositoryPolicy` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **policyText** *(string) --*

      The JSON repository policy that was deleted from the repository.
    """


_ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef = TypedDict(
    "_ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef(
    _ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef
):
    """
    Type definition for `ClientDeleteRepositoryResponserepository` `imageScanningConfiguration`

    The image scanning configuration for a repository.

    - **scanOnPush** *(boolean) --*

      The setting that determines whether images are scanned after being pushed to a
      repository. If set to ``true`` , images will be scanned after being pushed. If this
      parameter is not specified, it will default to ``false`` and images will not be scanned
      unless a scan is manually started with the  StartImageScan API.
    """


_ClientDeleteRepositoryResponserepositoryTypeDef = TypedDict(
    "_ClientDeleteRepositoryResponserepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": str,
        "imageScanningConfiguration": ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef,
    },
    total=False,
)


class ClientDeleteRepositoryResponserepositoryTypeDef(
    _ClientDeleteRepositoryResponserepositoryTypeDef
):
    """
    Type definition for `ClientDeleteRepositoryResponse` `repository`

    The repository that was deleted.

    - **repositoryArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
      ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the
      repository owner, repository namespace, and repository name. For example,
      ``arn:aws:ecr:region:012345678910:repository/test`` .

    - **registryId** *(string) --*

      The AWS account ID associated with the registry that contains the repository.

    - **repositoryName** *(string) --*

      The name of the repository.

    - **repositoryUri** *(string) --*

      The URI for the repository. You can use this URI for Docker ``push`` or ``pull`` operations.

    - **createdAt** *(datetime) --*

      The date and time, in JavaScript date format, when the repository was created.

    - **imageTagMutability** *(string) --*

      The tag mutability setting for the repository.

    - **imageScanningConfiguration** *(dict) --*

      The image scanning configuration for a repository.

      - **scanOnPush** *(boolean) --*

        The setting that determines whether images are scanned after being pushed to a
        repository. If set to ``true`` , images will be scanned after being pushed. If this
        parameter is not specified, it will default to ``false`` and images will not be scanned
        unless a scan is manually started with the  StartImageScan API.
    """


_ClientDeleteRepositoryResponseTypeDef = TypedDict(
    "_ClientDeleteRepositoryResponseTypeDef",
    {"repository": ClientDeleteRepositoryResponserepositoryTypeDef},
    total=False,
)


class ClientDeleteRepositoryResponseTypeDef(_ClientDeleteRepositoryResponseTypeDef):
    """
    Type definition for `ClientDeleteRepository` `Response`

    - **repository** *(dict) --*

      The repository that was deleted.

      - **repositoryArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
        ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the
        repository owner, repository namespace, and repository name. For example,
        ``arn:aws:ecr:region:012345678910:repository/test`` .

      - **registryId** *(string) --*

        The AWS account ID associated with the registry that contains the repository.

      - **repositoryName** *(string) --*

        The name of the repository.

      - **repositoryUri** *(string) --*

        The URI for the repository. You can use this URI for Docker ``push`` or ``pull`` operations.

      - **createdAt** *(datetime) --*

        The date and time, in JavaScript date format, when the repository was created.

      - **imageTagMutability** *(string) --*

        The tag mutability setting for the repository.

      - **imageScanningConfiguration** *(dict) --*

        The image scanning configuration for a repository.

        - **scanOnPush** *(boolean) --*

          The setting that determines whether images are scanned after being pushed to a
          repository. If set to ``true`` , images will be scanned after being pushed. If this
          parameter is not specified, it will default to ``false`` and images will not be scanned
          unless a scan is manually started with the  StartImageScan API.
    """


_ClientDescribeImageScanFindingsResponseimageIdTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientDescribeImageScanFindingsResponseimageIdTypeDef(
    _ClientDescribeImageScanFindingsResponseimageIdTypeDef
):
    """
    Type definition for `ClientDescribeImageScanFindingsResponse` `imageId`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef(
    _ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef
):
    """
    Type definition for `ClientDescribeImageScanFindingsResponseimageScanFindingsfindings` `attributes`

    This data type is used in the  ImageScanFinding data type.

    - **key** *(string) --*

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef",
    {
        "name": str,
        "description": str,
        "uri": str,
        "severity": str,
        "attributes": List[
            ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef(
    _ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef
):
    """
    Type definition for `ClientDescribeImageScanFindingsResponseimageScanFindings` `findings`

    Contains information about an image scan finding.

    - **name** *(string) --*

      The name associated with the finding, usually a CVE number.

    - **description** *(string) --*

      The description of the finding.

    - **uri** *(string) --*

      A link containing additional details about the security vulnerability.

    - **severity** *(string) --*

      The finding severity.

    - **attributes** *(list) --*

      A collection of attributes of the host from which the finding is generated.

      - *(dict) --*

        This data type is used in the  ImageScanFinding data type.

        - **key** *(string) --*

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.
    """


_ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findings": List[
            ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef
        ],
        "findingSeverityCounts": Dict[str, int],
    },
    total=False,
)


class ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef(
    _ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef
):
    """
    Type definition for `ClientDescribeImageScanFindingsResponse` `imageScanFindings`

    The information contained in the image scan findings.

    - **imageScanCompletedAt** *(datetime) --*

      The time of the last completed image scan.

    - **vulnerabilitySourceUpdatedAt** *(datetime) --*

      The time when the vulnerability data was last scanned.

    - **findings** *(list) --*

      The findings from the image scan.

      - *(dict) --*

        Contains information about an image scan finding.

        - **name** *(string) --*

          The name associated with the finding, usually a CVE number.

        - **description** *(string) --*

          The description of the finding.

        - **uri** *(string) --*

          A link containing additional details about the security vulnerability.

        - **severity** *(string) --*

          The finding severity.

        - **attributes** *(list) --*

          A collection of attributes of the host from which the finding is generated.

          - *(dict) --*

            This data type is used in the  ImageScanFinding data type.

            - **key** *(string) --*

              The attribute key.

            - **value** *(string) --*

              The value assigned to the attribute key.

    - **findingSeverityCounts** *(dict) --*

      The image vulnerability counts, sorted by severity.

      - *(string) --*

        - *(integer) --*
    """


_ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef",
    {"status": str, "description": str},
    total=False,
)


class ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef(
    _ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef
):
    """
    Type definition for `ClientDescribeImageScanFindingsResponse` `imageScanStatus`

    The current state of the scan.

    - **status** *(string) --*

      The current state of an image scan.

    - **description** *(string) --*

      The description of the image scan status.
    """


_ClientDescribeImageScanFindingsResponseTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientDescribeImageScanFindingsResponseimageIdTypeDef,
        "imageScanStatus": ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef,
        "imageScanFindings": ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef,
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeImageScanFindingsResponseTypeDef(
    _ClientDescribeImageScanFindingsResponseTypeDef
):
    """
    Type definition for `ClientDescribeImageScanFindings` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **imageId** *(dict) --*

      An object with identifying information for an Amazon ECR image.

      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.

      - **imageTag** *(string) --*

        The tag used for the image.

    - **imageScanStatus** *(dict) --*

      The current state of the scan.

      - **status** *(string) --*

        The current state of an image scan.

      - **description** *(string) --*

        The description of the image scan status.

    - **imageScanFindings** *(dict) --*

      The information contained in the image scan findings.

      - **imageScanCompletedAt** *(datetime) --*

        The time of the last completed image scan.

      - **vulnerabilitySourceUpdatedAt** *(datetime) --*

        The time when the vulnerability data was last scanned.

      - **findings** *(list) --*

        The findings from the image scan.

        - *(dict) --*

          Contains information about an image scan finding.

          - **name** *(string) --*

            The name associated with the finding, usually a CVE number.

          - **description** *(string) --*

            The description of the finding.

          - **uri** *(string) --*

            A link containing additional details about the security vulnerability.

          - **severity** *(string) --*

            The finding severity.

          - **attributes** *(list) --*

            A collection of attributes of the host from which the finding is generated.

            - *(dict) --*

              This data type is used in the  ImageScanFinding data type.

              - **key** *(string) --*

                The attribute key.

              - **value** *(string) --*

                The value assigned to the attribute key.

      - **findingSeverityCounts** *(dict) --*

        The image vulnerability counts, sorted by severity.

        - *(string) --*

          - *(integer) --*

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``DescribeImageScanFindings`` request. When
      the results of a ``DescribeImageScanFindings`` request exceed ``maxResults`` , this value can
      be used to retrieve the next page of results. This value is null when there are no more
      results to return.
    """


_ClientDescribeImageScanFindingsimageIdTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientDescribeImageScanFindingsimageIdTypeDef(
    _ClientDescribeImageScanFindingsimageIdTypeDef
):
    """
    Type definition for `ClientDescribeImageScanFindings` `imageId`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef = TypedDict(
    "_ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[str, int],
    },
    total=False,
)


class ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef(
    _ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef
):
    """
    Type definition for `ClientDescribeImagesResponseimageDetails` `imageScanFindingsSummary`

    A summary of the last completed image scan.

    - **imageScanCompletedAt** *(datetime) --*

      The time of the last completed image scan.

    - **vulnerabilitySourceUpdatedAt** *(datetime) --*

      The time when the vulnerability data was last scanned.

    - **findingSeverityCounts** *(dict) --*

      The image vulnerability counts, sorted by severity.

      - *(string) --*

        - *(integer) --*
    """


_ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef = TypedDict(
    "_ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef",
    {"status": str, "description": str},
    total=False,
)


class ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef(
    _ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef
):
    """
    Type definition for `ClientDescribeImagesResponseimageDetails` `imageScanStatus`

    The current state of the scan.

    - **status** *(string) --*

      The current state of an image scan.

    - **description** *(string) --*

      The description of the image scan status.
    """


_ClientDescribeImagesResponseimageDetailsTypeDef = TypedDict(
    "_ClientDescribeImagesResponseimageDetailsTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageDigest": str,
        "imageTags": List[str],
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageScanStatus": ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef,
        "imageScanFindingsSummary": ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef,
    },
    total=False,
)


class ClientDescribeImagesResponseimageDetailsTypeDef(
    _ClientDescribeImagesResponseimageDetailsTypeDef
):
    """
    Type definition for `ClientDescribeImagesResponse` `imageDetails`

    An object that describes an image returned by a  DescribeImages operation.

    - **registryId** *(string) --*

      The AWS account ID associated with the registry to which this image belongs.

    - **repositoryName** *(string) --*

      The name of the repository to which this image belongs.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTags** *(list) --*

      The list of tags associated with this image.

      - *(string) --*

    - **imageSizeInBytes** *(integer) --*

      The size, in bytes, of the image in the repository.

      .. note::

        Beginning with Docker version 1.9, the Docker client compresses image layers before
        pushing them to a V2 Docker registry. The output of the ``docker images`` command shows
        the uncompressed image size, so it may return a larger image size than the image sizes
        returned by  DescribeImages .

    - **imagePushedAt** *(datetime) --*

      The date and time, expressed in standard JavaScript date format, at which the current
      image was pushed to the repository.

    - **imageScanStatus** *(dict) --*

      The current state of the scan.

      - **status** *(string) --*

        The current state of an image scan.

      - **description** *(string) --*

        The description of the image scan status.

    - **imageScanFindingsSummary** *(dict) --*

      A summary of the last completed image scan.

      - **imageScanCompletedAt** *(datetime) --*

        The time of the last completed image scan.

      - **vulnerabilitySourceUpdatedAt** *(datetime) --*

        The time when the vulnerability data was last scanned.

      - **findingSeverityCounts** *(dict) --*

        The image vulnerability counts, sorted by severity.

        - *(string) --*

          - *(integer) --*
    """


_ClientDescribeImagesResponseTypeDef = TypedDict(
    "_ClientDescribeImagesResponseTypeDef",
    {
        "imageDetails": List[ClientDescribeImagesResponseimageDetailsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeImagesResponseTypeDef(_ClientDescribeImagesResponseTypeDef):
    """
    Type definition for `ClientDescribeImages` `Response`

    - **imageDetails** *(list) --*

      A list of  ImageDetail objects that contain data about the image.

      - *(dict) --*

        An object that describes an image returned by a  DescribeImages operation.

        - **registryId** *(string) --*

          The AWS account ID associated with the registry to which this image belongs.

        - **repositoryName** *(string) --*

          The name of the repository to which this image belongs.

        - **imageDigest** *(string) --*

          The ``sha256`` digest of the image manifest.

        - **imageTags** *(list) --*

          The list of tags associated with this image.

          - *(string) --*

        - **imageSizeInBytes** *(integer) --*

          The size, in bytes, of the image in the repository.

          .. note::

            Beginning with Docker version 1.9, the Docker client compresses image layers before
            pushing them to a V2 Docker registry. The output of the ``docker images`` command shows
            the uncompressed image size, so it may return a larger image size than the image sizes
            returned by  DescribeImages .

        - **imagePushedAt** *(datetime) --*

          The date and time, expressed in standard JavaScript date format, at which the current
          image was pushed to the repository.

        - **imageScanStatus** *(dict) --*

          The current state of the scan.

          - **status** *(string) --*

            The current state of an image scan.

          - **description** *(string) --*

            The description of the image scan status.

        - **imageScanFindingsSummary** *(dict) --*

          A summary of the last completed image scan.

          - **imageScanCompletedAt** *(datetime) --*

            The time of the last completed image scan.

          - **vulnerabilitySourceUpdatedAt** *(datetime) --*

            The time when the vulnerability data was last scanned.

          - **findingSeverityCounts** *(dict) --*

            The image vulnerability counts, sorted by severity.

            - *(string) --*

              - *(integer) --*

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``DescribeImages`` request. When the results
      of a ``DescribeImages`` request exceed ``maxResults`` , this value can be used to retrieve
      the next page of results. This value is ``null`` when there are no more results to return.
    """


_ClientDescribeImagesfilterTypeDef = TypedDict(
    "_ClientDescribeImagesfilterTypeDef", {"tagStatus": str}, total=False
)


class ClientDescribeImagesfilterTypeDef(_ClientDescribeImagesfilterTypeDef):
    """
    Type definition for `ClientDescribeImages` `filter`

    The filter key and value with which to filter your ``DescribeImages`` results.

    - **tagStatus** *(string) --*

      The tag status with which to filter your  DescribeImages results. You can filter results based
      on whether they are ``TAGGED`` or ``UNTAGGED`` .
    """


_ClientDescribeImagesimageIdsTypeDef = TypedDict(
    "_ClientDescribeImagesimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientDescribeImagesimageIdsTypeDef(_ClientDescribeImagesimageIdsTypeDef):
    """
    Type definition for `ClientDescribeImages` `imageIds`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef = TypedDict(
    "_ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef(
    _ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeRepositoriesResponserepositories` `imageScanningConfiguration`

    The image scanning configuration for a repository.

    - **scanOnPush** *(boolean) --*

      The setting that determines whether images are scanned after being pushed to a
      repository. If set to ``true`` , images will be scanned after being pushed. If this
      parameter is not specified, it will default to ``false`` and images will not be scanned
      unless a scan is manually started with the  StartImageScan API.
    """


_ClientDescribeRepositoriesResponserepositoriesTypeDef = TypedDict(
    "_ClientDescribeRepositoriesResponserepositoriesTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": str,
        "imageScanningConfiguration": ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeRepositoriesResponserepositoriesTypeDef(
    _ClientDescribeRepositoriesResponserepositoriesTypeDef
):
    """
    Type definition for `ClientDescribeRepositoriesResponse` `repositories`

    An object representing a repository.

    - **repositoryArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
      ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of
      the repository owner, repository namespace, and repository name. For example,
      ``arn:aws:ecr:region:012345678910:repository/test`` .

    - **registryId** *(string) --*

      The AWS account ID associated with the registry that contains the repository.

    - **repositoryName** *(string) --*

      The name of the repository.

    - **repositoryUri** *(string) --*

      The URI for the repository. You can use this URI for Docker ``push`` or ``pull``
      operations.

    - **createdAt** *(datetime) --*

      The date and time, in JavaScript date format, when the repository was created.

    - **imageTagMutability** *(string) --*

      The tag mutability setting for the repository.

    - **imageScanningConfiguration** *(dict) --*

      The image scanning configuration for a repository.

      - **scanOnPush** *(boolean) --*

        The setting that determines whether images are scanned after being pushed to a
        repository. If set to ``true`` , images will be scanned after being pushed. If this
        parameter is not specified, it will default to ``false`` and images will not be scanned
        unless a scan is manually started with the  StartImageScan API.
    """


_ClientDescribeRepositoriesResponseTypeDef = TypedDict(
    "_ClientDescribeRepositoriesResponseTypeDef",
    {
        "repositories": List[ClientDescribeRepositoriesResponserepositoriesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeRepositoriesResponseTypeDef(
    _ClientDescribeRepositoriesResponseTypeDef
):
    """
    Type definition for `ClientDescribeRepositories` `Response`

    - **repositories** *(list) --*

      A list of repository objects corresponding to valid repositories.

      - *(dict) --*

        An object representing a repository.

        - **repositoryArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
          ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of
          the repository owner, repository namespace, and repository name. For example,
          ``arn:aws:ecr:region:012345678910:repository/test`` .

        - **registryId** *(string) --*

          The AWS account ID associated with the registry that contains the repository.

        - **repositoryName** *(string) --*

          The name of the repository.

        - **repositoryUri** *(string) --*

          The URI for the repository. You can use this URI for Docker ``push`` or ``pull``
          operations.

        - **createdAt** *(datetime) --*

          The date and time, in JavaScript date format, when the repository was created.

        - **imageTagMutability** *(string) --*

          The tag mutability setting for the repository.

        - **imageScanningConfiguration** *(dict) --*

          The image scanning configuration for a repository.

          - **scanOnPush** *(boolean) --*

            The setting that determines whether images are scanned after being pushed to a
            repository. If set to ``true`` , images will be scanned after being pushed. If this
            parameter is not specified, it will default to ``false`` and images will not be scanned
            unless a scan is manually started with the  StartImageScan API.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``DescribeRepositories`` request. When the
      results of a ``DescribeRepositories`` request exceed ``maxResults`` , this value can be used
      to retrieve the next page of results. This value is ``null`` when there are no more results
      to return.
    """


_ClientGetAuthorizationTokenResponseauthorizationDataTypeDef = TypedDict(
    "_ClientGetAuthorizationTokenResponseauthorizationDataTypeDef",
    {"authorizationToken": str, "expiresAt": datetime, "proxyEndpoint": str},
    total=False,
)


class ClientGetAuthorizationTokenResponseauthorizationDataTypeDef(
    _ClientGetAuthorizationTokenResponseauthorizationDataTypeDef
):
    """
    Type definition for `ClientGetAuthorizationTokenResponse` `authorizationData`

    An object representing authorization data for an Amazon ECR registry.

    - **authorizationToken** *(string) --*

      A base64-encoded string that contains authorization data for the specified Amazon ECR
      registry. When the string is decoded, it is presented in the format ``user:password`` for
      private registry authentication using ``docker login`` .

    - **expiresAt** *(datetime) --*

      The Unix time in seconds and milliseconds when the authorization token expires.
      Authorization tokens are valid for 12 hours.

    - **proxyEndpoint** *(string) --*

      The registry URL to use for this authorization token in a ``docker login`` command. The
      Amazon ECR registry URL format is ``https://aws_account_id.dkr.ecr.region.amazonaws.com``
      . For example, ``https://012345678910.dkr.ecr.us-east-1.amazonaws.com`` ..
    """


_ClientGetAuthorizationTokenResponseTypeDef = TypedDict(
    "_ClientGetAuthorizationTokenResponseTypeDef",
    {
        "authorizationData": List[
            ClientGetAuthorizationTokenResponseauthorizationDataTypeDef
        ]
    },
    total=False,
)


class ClientGetAuthorizationTokenResponseTypeDef(
    _ClientGetAuthorizationTokenResponseTypeDef
):
    """
    Type definition for `ClientGetAuthorizationToken` `Response`

    - **authorizationData** *(list) --*

      A list of authorization token data objects that correspond to the ``registryIds`` values in
      the request.

      - *(dict) --*

        An object representing authorization data for an Amazon ECR registry.

        - **authorizationToken** *(string) --*

          A base64-encoded string that contains authorization data for the specified Amazon ECR
          registry. When the string is decoded, it is presented in the format ``user:password`` for
          private registry authentication using ``docker login`` .

        - **expiresAt** *(datetime) --*

          The Unix time in seconds and milliseconds when the authorization token expires.
          Authorization tokens are valid for 12 hours.

        - **proxyEndpoint** *(string) --*

          The registry URL to use for this authorization token in a ``docker login`` command. The
          Amazon ECR registry URL format is ``https://aws_account_id.dkr.ecr.region.amazonaws.com``
          . For example, ``https://012345678910.dkr.ecr.us-east-1.amazonaws.com`` ..
    """


_ClientGetDownloadUrlForLayerResponseTypeDef = TypedDict(
    "_ClientGetDownloadUrlForLayerResponseTypeDef",
    {"downloadUrl": str, "layerDigest": str},
    total=False,
)


class ClientGetDownloadUrlForLayerResponseTypeDef(
    _ClientGetDownloadUrlForLayerResponseTypeDef
):
    """
    Type definition for `ClientGetDownloadUrlForLayer` `Response`

    - **downloadUrl** *(string) --*

      The pre-signed Amazon S3 download URL for the requested layer.

    - **layerDigest** *(string) --*

      The digest of the image layer to download.
    """


_ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef",
    {"type": str},
    total=False,
)


class ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef(
    _ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyPreviewResponsepreviewResults` `action`

    The type of action to be taken.

    - **type** *(string) --*

      The type of action to be taken.
    """


_ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef",
    {
        "imageTags": List[str],
        "imageDigest": str,
        "imagePushedAt": datetime,
        "action": ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef,
        "appliedRulePriority": int,
    },
    total=False,
)


class ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef(
    _ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyPreviewResponse` `previewResults`

    The result of the lifecycle policy preview.

    - **imageTags** *(list) --*

      The list of tags associated with this image.

      - *(string) --*

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imagePushedAt** *(datetime) --*

      The date and time, expressed in standard JavaScript date format, at which the current
      image was pushed to the repository.

    - **action** *(dict) --*

      The type of action to be taken.

      - **type** *(string) --*

        The type of action to be taken.

    - **appliedRulePriority** *(integer) --*

      The priority of the applied rule.
    """


_ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef",
    {"expiringImageTotalCount": int},
    total=False,
)


class ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef(
    _ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyPreviewResponse` `summary`

    The list of images that is returned as a result of the action.

    - **expiringImageTotalCount** *(integer) --*

      The number of expiring images.
    """


_ClientGetLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": str,
        "nextToken": str,
        "previewResults": List[
            ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef
        ],
        "summary": ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef,
    },
    total=False,
)


class ClientGetLifecyclePolicyPreviewResponseTypeDef(
    _ClientGetLifecyclePolicyPreviewResponseTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyPreview` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **lifecyclePolicyText** *(string) --*

      The JSON lifecycle policy text.

    - **status** *(string) --*

      The status of the lifecycle policy preview request.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``GetLifecyclePolicyPreview`` request. When
      the results of a ``GetLifecyclePolicyPreview`` request exceed ``maxResults`` , this value can
      be used to retrieve the next page of results. This value is ``null`` when there are no more
      results to return.

    - **previewResults** *(list) --*

      The results of the lifecycle policy preview request.

      - *(dict) --*

        The result of the lifecycle policy preview.

        - **imageTags** *(list) --*

          The list of tags associated with this image.

          - *(string) --*

        - **imageDigest** *(string) --*

          The ``sha256`` digest of the image manifest.

        - **imagePushedAt** *(datetime) --*

          The date and time, expressed in standard JavaScript date format, at which the current
          image was pushed to the repository.

        - **action** *(dict) --*

          The type of action to be taken.

          - **type** *(string) --*

            The type of action to be taken.

        - **appliedRulePriority** *(integer) --*

          The priority of the applied rule.

    - **summary** *(dict) --*

      The list of images that is returned as a result of the action.

      - **expiringImageTotalCount** *(integer) --*

        The number of expiring images.
    """


_ClientGetLifecyclePolicyPreviewfilterTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewfilterTypeDef", {"tagStatus": str}, total=False
)


class ClientGetLifecyclePolicyPreviewfilterTypeDef(
    _ClientGetLifecyclePolicyPreviewfilterTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyPreview` `filter`

    An optional parameter that filters results based on image tag status and all tags, if tagged.

    - **tagStatus** *(string) --*

      The tag status of the image.
    """


_ClientGetLifecyclePolicyPreviewimageIdsTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientGetLifecyclePolicyPreviewimageIdsTypeDef(
    _ClientGetLifecyclePolicyPreviewimageIdsTypeDef
):
    """
    Type definition for `ClientGetLifecyclePolicyPreview` `imageIds`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientGetLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
    },
    total=False,
)


class ClientGetLifecyclePolicyResponseTypeDef(_ClientGetLifecyclePolicyResponseTypeDef):
    """
    Type definition for `ClientGetLifecyclePolicy` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **lifecyclePolicyText** *(string) --*

      The JSON lifecycle policy text.

    - **lastEvaluatedAt** *(datetime) --*

      The time stamp of the last time that the lifecycle policy was run.
    """


_ClientGetRepositoryPolicyResponseTypeDef = TypedDict(
    "_ClientGetRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)


class ClientGetRepositoryPolicyResponseTypeDef(
    _ClientGetRepositoryPolicyResponseTypeDef
):
    """
    Type definition for `ClientGetRepositoryPolicy` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **policyText** *(string) --*

      The JSON repository policy text associated with the repository.
    """


_ClientInitiateLayerUploadResponseTypeDef = TypedDict(
    "_ClientInitiateLayerUploadResponseTypeDef",
    {"uploadId": str, "partSize": int},
    total=False,
)


class ClientInitiateLayerUploadResponseTypeDef(
    _ClientInitiateLayerUploadResponseTypeDef
):
    """
    Type definition for `ClientInitiateLayerUpload` `Response`

    - **uploadId** *(string) --*

      The upload ID for the layer upload. This parameter is passed to further  UploadLayerPart and
      CompleteLayerUpload operations.

    - **partSize** *(integer) --*

      The size, in bytes, that Amazon ECR expects future layer part uploads to be.
    """


_ClientListImagesResponseimageIdsTypeDef = TypedDict(
    "_ClientListImagesResponseimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientListImagesResponseimageIdsTypeDef(_ClientListImagesResponseimageIdsTypeDef):
    """
    Type definition for `ClientListImagesResponse` `imageIds`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientListImagesResponseTypeDef = TypedDict(
    "_ClientListImagesResponseTypeDef",
    {"imageIds": List[ClientListImagesResponseimageIdsTypeDef], "nextToken": str},
    total=False,
)


class ClientListImagesResponseTypeDef(_ClientListImagesResponseTypeDef):
    """
    Type definition for `ClientListImages` `Response`

    - **imageIds** *(list) --*

      The list of image IDs for the requested repository.

      - *(dict) --*

        An object with identifying information for an Amazon ECR image.

        - **imageDigest** *(string) --*

          The ``sha256`` digest of the image manifest.

        - **imageTag** *(string) --*

          The tag used for the image.

    - **nextToken** *(string) --*

      The ``nextToken`` value to include in a future ``ListImages`` request. When the results of a
      ``ListImages`` request exceed ``maxResults`` , this value can be used to retrieve the next
      page of results. This value is ``null`` when there are no more results to return.
    """


_ClientListImagesfilterTypeDef = TypedDict(
    "_ClientListImagesfilterTypeDef", {"tagStatus": str}, total=False
)


class ClientListImagesfilterTypeDef(_ClientListImagesfilterTypeDef):
    """
    Type definition for `ClientListImages` `filter`

    The filter key and value with which to filter your ``ListImages`` results.

    - **tagStatus** *(string) --*

      The tag status with which to filter your  ListImages results. You can filter results based on
      whether they are ``TAGGED`` or ``UNTAGGED`` .
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponsetagsTypeDef(
    _ClientListTagsForResourceResponsetagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `tags`

    The metadata that you apply to a resource to help you categorize and organize them. Each
    tag consists of a key and an optional value, both of which you define. Tag keys can have a
    maximum character length of 128 characters, and tag values can have a maximum length of 256
    characters.

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
      like a category for more specific tag values.

    - **Value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a
      descriptor within a tag category (key).
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(list) --*

      The tags for the resource.

      - *(dict) --*

        The metadata that you apply to a resource to help you categorize and organize them. Each
        tag consists of a key and an optional value, both of which you define. Tag keys can have a
        maximum character length of 128 characters, and tag values can have a maximum length of 256
        characters.

        - **Key** *(string) --*

          One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
          like a category for more specific tag values.

        - **Value** *(string) --*

          The optional part of a key-value pair that make up a tag. A ``value`` acts as a
          descriptor within a tag category (key).
    """


_ClientPutImageResponseimageimageIdTypeDef = TypedDict(
    "_ClientPutImageResponseimageimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientPutImageResponseimageimageIdTypeDef(
    _ClientPutImageResponseimageimageIdTypeDef
):
    """
    Type definition for `ClientPutImageResponseimage` `imageId`

    An object containing the image tag and image digest associated with an image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientPutImageResponseimageTypeDef = TypedDict(
    "_ClientPutImageResponseimageTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientPutImageResponseimageimageIdTypeDef,
        "imageManifest": str,
    },
    total=False,
)


class ClientPutImageResponseimageTypeDef(_ClientPutImageResponseimageTypeDef):
    """
    Type definition for `ClientPutImageResponse` `image`

    Details of the image uploaded.

    - **registryId** *(string) --*

      The AWS account ID associated with the registry containing the image.

    - **repositoryName** *(string) --*

      The name of the repository associated with the image.

    - **imageId** *(dict) --*

      An object containing the image tag and image digest associated with an image.

      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.

      - **imageTag** *(string) --*

        The tag used for the image.

    - **imageManifest** *(string) --*

      The image manifest associated with the image.
    """


_ClientPutImageResponseTypeDef = TypedDict(
    "_ClientPutImageResponseTypeDef",
    {"image": ClientPutImageResponseimageTypeDef},
    total=False,
)


class ClientPutImageResponseTypeDef(_ClientPutImageResponseTypeDef):
    """
    Type definition for `ClientPutImage` `Response`

    - **image** *(dict) --*

      Details of the image uploaded.

      - **registryId** *(string) --*

        The AWS account ID associated with the registry containing the image.

      - **repositoryName** *(string) --*

        The name of the repository associated with the image.

      - **imageId** *(dict) --*

        An object containing the image tag and image digest associated with an image.

        - **imageDigest** *(string) --*

          The ``sha256`` digest of the image manifest.

        - **imageTag** *(string) --*

          The tag used for the image.

      - **imageManifest** *(string) --*

        The image manifest associated with the image.
    """


_ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef = TypedDict(
    "_ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef(
    _ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef
):
    """
    Type definition for `ClientPutImageScanningConfigurationResponse` `imageScanningConfiguration`

    The image scanning configuration setting for the repository.

    - **scanOnPush** *(boolean) --*

      The setting that determines whether images are scanned after being pushed to a repository.
      If set to ``true`` , images will be scanned after being pushed. If this parameter is not
      specified, it will default to ``false`` and images will not be scanned unless a scan is
      manually started with the  StartImageScan API.
    """


_ClientPutImageScanningConfigurationResponseTypeDef = TypedDict(
    "_ClientPutImageScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageScanningConfiguration": ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef,
    },
    total=False,
)


class ClientPutImageScanningConfigurationResponseTypeDef(
    _ClientPutImageScanningConfigurationResponseTypeDef
):
    """
    Type definition for `ClientPutImageScanningConfiguration` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **imageScanningConfiguration** *(dict) --*

      The image scanning configuration setting for the repository.

      - **scanOnPush** *(boolean) --*

        The setting that determines whether images are scanned after being pushed to a repository.
        If set to ``true`` , images will be scanned after being pushed. If this parameter is not
        specified, it will default to ``false`` and images will not be scanned unless a scan is
        manually started with the  StartImageScan API.
    """


_ClientPutImageScanningConfigurationimageScanningConfigurationTypeDef = TypedDict(
    "_ClientPutImageScanningConfigurationimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientPutImageScanningConfigurationimageScanningConfigurationTypeDef(
    _ClientPutImageScanningConfigurationimageScanningConfigurationTypeDef
):
    """
    Type definition for `ClientPutImageScanningConfiguration` `imageScanningConfiguration`

    The image scanning configuration for the repository. This setting determines whether images are
    scanned for known vulnerabilities after being pushed to the repository.

    - **scanOnPush** *(boolean) --*

      The setting that determines whether images are scanned after being pushed to a repository. If
      set to ``true`` , images will be scanned after being pushed. If this parameter is not
      specified, it will default to ``false`` and images will not be scanned unless a scan is
      manually started with the  StartImageScan API.
    """


_ClientPutImageTagMutabilityResponseTypeDef = TypedDict(
    "_ClientPutImageTagMutabilityResponseTypeDef",
    {"registryId": str, "repositoryName": str, "imageTagMutability": str},
    total=False,
)


class ClientPutImageTagMutabilityResponseTypeDef(
    _ClientPutImageTagMutabilityResponseTypeDef
):
    """
    Type definition for `ClientPutImageTagMutability` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **imageTagMutability** *(string) --*

      The image tag mutability setting for the repository.
    """


_ClientPutLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientPutLifecyclePolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "lifecyclePolicyText": str},
    total=False,
)


class ClientPutLifecyclePolicyResponseTypeDef(_ClientPutLifecyclePolicyResponseTypeDef):
    """
    Type definition for `ClientPutLifecyclePolicy` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **lifecyclePolicyText** *(string) --*

      The JSON repository policy text.
    """


_ClientSetRepositoryPolicyResponseTypeDef = TypedDict(
    "_ClientSetRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)


class ClientSetRepositoryPolicyResponseTypeDef(
    _ClientSetRepositoryPolicyResponseTypeDef
):
    """
    Type definition for `ClientSetRepositoryPolicy` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **policyText** *(string) --*

      The JSON repository policy text applied to the repository.
    """


_ClientStartImageScanResponseimageIdTypeDef = TypedDict(
    "_ClientStartImageScanResponseimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientStartImageScanResponseimageIdTypeDef(
    _ClientStartImageScanResponseimageIdTypeDef
):
    """
    Type definition for `ClientStartImageScanResponse` `imageId`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientStartImageScanResponseimageScanStatusTypeDef = TypedDict(
    "_ClientStartImageScanResponseimageScanStatusTypeDef",
    {"status": str, "description": str},
    total=False,
)


class ClientStartImageScanResponseimageScanStatusTypeDef(
    _ClientStartImageScanResponseimageScanStatusTypeDef
):
    """
    Type definition for `ClientStartImageScanResponse` `imageScanStatus`

    The current state of the scan.

    - **status** *(string) --*

      The current state of an image scan.

    - **description** *(string) --*

      The description of the image scan status.
    """


_ClientStartImageScanResponseTypeDef = TypedDict(
    "_ClientStartImageScanResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientStartImageScanResponseimageIdTypeDef,
        "imageScanStatus": ClientStartImageScanResponseimageScanStatusTypeDef,
    },
    total=False,
)


class ClientStartImageScanResponseTypeDef(_ClientStartImageScanResponseTypeDef):
    """
    Type definition for `ClientStartImageScan` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **imageId** *(dict) --*

      An object with identifying information for an Amazon ECR image.

      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.

      - **imageTag** *(string) --*

        The tag used for the image.

    - **imageScanStatus** *(dict) --*

      The current state of the scan.

      - **status** *(string) --*

        The current state of an image scan.

      - **description** *(string) --*

        The description of the image scan status.
    """


_ClientStartImageScanimageIdTypeDef = TypedDict(
    "_ClientStartImageScanimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientStartImageScanimageIdTypeDef(_ClientStartImageScanimageIdTypeDef):
    """
    Type definition for `ClientStartImageScan` `imageId`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ClientStartLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "_ClientStartLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": str,
    },
    total=False,
)


class ClientStartLifecyclePolicyPreviewResponseTypeDef(
    _ClientStartLifecyclePolicyPreviewResponseTypeDef
):
    """
    Type definition for `ClientStartLifecyclePolicyPreview` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **lifecyclePolicyText** *(string) --*

      The JSON repository policy text.

    - **status** *(string) --*

      The status of the lifecycle policy preview request.
    """


_ClientTagResourcetagsTypeDef = TypedDict(
    "_ClientTagResourcetagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourcetagsTypeDef(_ClientTagResourcetagsTypeDef):
    """
    Type definition for `ClientTagResource` `tags`

    The metadata that you apply to a resource to help you categorize and organize them. Each tag
    consists of a key and an optional value, both of which you define. Tag keys can have a maximum
    character length of 128 characters, and tag values can have a maximum length of 256 characters.

    - **Key** *(string) --*

      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
      a category for more specific tag values.

    - **Value** *(string) --*

      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
      within a tag category (key).
    """


_ClientUploadLayerPartResponseTypeDef = TypedDict(
    "_ClientUploadLayerPartResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "lastByteReceived": int,
    },
    total=False,
)


class ClientUploadLayerPartResponseTypeDef(_ClientUploadLayerPartResponseTypeDef):
    """
    Type definition for `ClientUploadLayerPart` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **uploadId** *(string) --*

      The upload ID associated with the request.

    - **lastByteReceived** *(integer) --*

      The integer value of the last byte received in the request.
    """


_DescribeImageScanFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeImageScanFindingsPaginatePaginationConfigTypeDef(
    _DescribeImageScanFindingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeImageScanFindingsPaginate` `PaginationConfig`

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


_DescribeImageScanFindingsPaginateResponseimageIdTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class DescribeImageScanFindingsPaginateResponseimageIdTypeDef(
    _DescribeImageScanFindingsPaginateResponseimageIdTypeDef
):
    """
    Type definition for `DescribeImageScanFindingsPaginateResponse` `imageId`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef(
    _DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef
):
    """
    Type definition for `DescribeImageScanFindingsPaginateResponseimageScanFindingsfindings` `attributes`

    This data type is used in the  ImageScanFinding data type.

    - **key** *(string) --*

      The attribute key.

    - **value** *(string) --*

      The value assigned to the attribute key.
    """


_DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef",
    {
        "name": str,
        "description": str,
        "uri": str,
        "severity": str,
        "attributes": List[
            DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef
        ],
    },
    total=False,
)


class DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef(
    _DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef
):
    """
    Type definition for `DescribeImageScanFindingsPaginateResponseimageScanFindings` `findings`

    Contains information about an image scan finding.

    - **name** *(string) --*

      The name associated with the finding, usually a CVE number.

    - **description** *(string) --*

      The description of the finding.

    - **uri** *(string) --*

      A link containing additional details about the security vulnerability.

    - **severity** *(string) --*

      The finding severity.

    - **attributes** *(list) --*

      A collection of attributes of the host from which the finding is generated.

      - *(dict) --*

        This data type is used in the  ImageScanFinding data type.

        - **key** *(string) --*

          The attribute key.

        - **value** *(string) --*

          The value assigned to the attribute key.
    """


_DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findings": List[
            DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef
        ],
        "findingSeverityCounts": Dict[str, int],
    },
    total=False,
)


class DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef(
    _DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef
):
    """
    Type definition for `DescribeImageScanFindingsPaginateResponse` `imageScanFindings`

    The information contained in the image scan findings.

    - **imageScanCompletedAt** *(datetime) --*

      The time of the last completed image scan.

    - **vulnerabilitySourceUpdatedAt** *(datetime) --*

      The time when the vulnerability data was last scanned.

    - **findings** *(list) --*

      The findings from the image scan.

      - *(dict) --*

        Contains information about an image scan finding.

        - **name** *(string) --*

          The name associated with the finding, usually a CVE number.

        - **description** *(string) --*

          The description of the finding.

        - **uri** *(string) --*

          A link containing additional details about the security vulnerability.

        - **severity** *(string) --*

          The finding severity.

        - **attributes** *(list) --*

          A collection of attributes of the host from which the finding is generated.

          - *(dict) --*

            This data type is used in the  ImageScanFinding data type.

            - **key** *(string) --*

              The attribute key.

            - **value** *(string) --*

              The value assigned to the attribute key.

    - **findingSeverityCounts** *(dict) --*

      The image vulnerability counts, sorted by severity.

      - *(string) --*

        - *(integer) --*
    """


_DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef",
    {"status": str, "description": str},
    total=False,
)


class DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef(
    _DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef
):
    """
    Type definition for `DescribeImageScanFindingsPaginateResponse` `imageScanStatus`

    The current state of the scan.

    - **status** *(string) --*

      The current state of an image scan.

    - **description** *(string) --*

      The description of the image scan status.
    """


_DescribeImageScanFindingsPaginateResponseTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": DescribeImageScanFindingsPaginateResponseimageIdTypeDef,
        "imageScanStatus": DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef,
        "imageScanFindings": DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef,
        "NextToken": str,
    },
    total=False,
)


class DescribeImageScanFindingsPaginateResponseTypeDef(
    _DescribeImageScanFindingsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeImageScanFindingsPaginate` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **imageId** *(dict) --*

      An object with identifying information for an Amazon ECR image.

      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.

      - **imageTag** *(string) --*

        The tag used for the image.

    - **imageScanStatus** *(dict) --*

      The current state of the scan.

      - **status** *(string) --*

        The current state of an image scan.

      - **description** *(string) --*

        The description of the image scan status.

    - **imageScanFindings** *(dict) --*

      The information contained in the image scan findings.

      - **imageScanCompletedAt** *(datetime) --*

        The time of the last completed image scan.

      - **vulnerabilitySourceUpdatedAt** *(datetime) --*

        The time when the vulnerability data was last scanned.

      - **findings** *(list) --*

        The findings from the image scan.

        - *(dict) --*

          Contains information about an image scan finding.

          - **name** *(string) --*

            The name associated with the finding, usually a CVE number.

          - **description** *(string) --*

            The description of the finding.

          - **uri** *(string) --*

            A link containing additional details about the security vulnerability.

          - **severity** *(string) --*

            The finding severity.

          - **attributes** *(list) --*

            A collection of attributes of the host from which the finding is generated.

            - *(dict) --*

              This data type is used in the  ImageScanFinding data type.

              - **key** *(string) --*

                The attribute key.

              - **value** *(string) --*

                The value assigned to the attribute key.

      - **findingSeverityCounts** *(dict) --*

        The image vulnerability counts, sorted by severity.

        - *(string) --*

          - *(integer) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeImageScanFindingsPaginateimageIdTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class DescribeImageScanFindingsPaginateimageIdTypeDef(
    _DescribeImageScanFindingsPaginateimageIdTypeDef
):
    """
    Type definition for `DescribeImageScanFindingsPaginate` `imageId`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_DescribeImagesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeImagesPaginatePaginationConfigTypeDef(
    _DescribeImagesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeImagesPaginate` `PaginationConfig`

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


_DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[str, int],
    },
    total=False,
)


class DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef(
    _DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef
):
    """
    Type definition for `DescribeImagesPaginateResponseimageDetails` `imageScanFindingsSummary`

    A summary of the last completed image scan.

    - **imageScanCompletedAt** *(datetime) --*

      The time of the last completed image scan.

    - **vulnerabilitySourceUpdatedAt** *(datetime) --*

      The time when the vulnerability data was last scanned.

    - **findingSeverityCounts** *(dict) --*

      The image vulnerability counts, sorted by severity.

      - *(string) --*

        - *(integer) --*
    """


_DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef",
    {"status": str, "description": str},
    total=False,
)


class DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef(
    _DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef
):
    """
    Type definition for `DescribeImagesPaginateResponseimageDetails` `imageScanStatus`

    The current state of the scan.

    - **status** *(string) --*

      The current state of an image scan.

    - **description** *(string) --*

      The description of the image scan status.
    """


_DescribeImagesPaginateResponseimageDetailsTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseimageDetailsTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageDigest": str,
        "imageTags": List[str],
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageScanStatus": DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef,
        "imageScanFindingsSummary": DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef,
    },
    total=False,
)


class DescribeImagesPaginateResponseimageDetailsTypeDef(
    _DescribeImagesPaginateResponseimageDetailsTypeDef
):
    """
    Type definition for `DescribeImagesPaginateResponse` `imageDetails`

    An object that describes an image returned by a  DescribeImages operation.

    - **registryId** *(string) --*

      The AWS account ID associated with the registry to which this image belongs.

    - **repositoryName** *(string) --*

      The name of the repository to which this image belongs.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTags** *(list) --*

      The list of tags associated with this image.

      - *(string) --*

    - **imageSizeInBytes** *(integer) --*

      The size, in bytes, of the image in the repository.

      .. note::

        Beginning with Docker version 1.9, the Docker client compresses image layers before
        pushing them to a V2 Docker registry. The output of the ``docker images`` command shows
        the uncompressed image size, so it may return a larger image size than the image sizes
        returned by  DescribeImages .

    - **imagePushedAt** *(datetime) --*

      The date and time, expressed in standard JavaScript date format, at which the current
      image was pushed to the repository.

    - **imageScanStatus** *(dict) --*

      The current state of the scan.

      - **status** *(string) --*

        The current state of an image scan.

      - **description** *(string) --*

        The description of the image scan status.

    - **imageScanFindingsSummary** *(dict) --*

      A summary of the last completed image scan.

      - **imageScanCompletedAt** *(datetime) --*

        The time of the last completed image scan.

      - **vulnerabilitySourceUpdatedAt** *(datetime) --*

        The time when the vulnerability data was last scanned.

      - **findingSeverityCounts** *(dict) --*

        The image vulnerability counts, sorted by severity.

        - *(string) --*

          - *(integer) --*
    """


_DescribeImagesPaginateResponseTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseTypeDef",
    {
        "imageDetails": List[DescribeImagesPaginateResponseimageDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeImagesPaginateResponseTypeDef(_DescribeImagesPaginateResponseTypeDef):
    """
    Type definition for `DescribeImagesPaginate` `Response`

    - **imageDetails** *(list) --*

      A list of  ImageDetail objects that contain data about the image.

      - *(dict) --*

        An object that describes an image returned by a  DescribeImages operation.

        - **registryId** *(string) --*

          The AWS account ID associated with the registry to which this image belongs.

        - **repositoryName** *(string) --*

          The name of the repository to which this image belongs.

        - **imageDigest** *(string) --*

          The ``sha256`` digest of the image manifest.

        - **imageTags** *(list) --*

          The list of tags associated with this image.

          - *(string) --*

        - **imageSizeInBytes** *(integer) --*

          The size, in bytes, of the image in the repository.

          .. note::

            Beginning with Docker version 1.9, the Docker client compresses image layers before
            pushing them to a V2 Docker registry. The output of the ``docker images`` command shows
            the uncompressed image size, so it may return a larger image size than the image sizes
            returned by  DescribeImages .

        - **imagePushedAt** *(datetime) --*

          The date and time, expressed in standard JavaScript date format, at which the current
          image was pushed to the repository.

        - **imageScanStatus** *(dict) --*

          The current state of the scan.

          - **status** *(string) --*

            The current state of an image scan.

          - **description** *(string) --*

            The description of the image scan status.

        - **imageScanFindingsSummary** *(dict) --*

          A summary of the last completed image scan.

          - **imageScanCompletedAt** *(datetime) --*

            The time of the last completed image scan.

          - **vulnerabilitySourceUpdatedAt** *(datetime) --*

            The time when the vulnerability data was last scanned.

          - **findingSeverityCounts** *(dict) --*

            The image vulnerability counts, sorted by severity.

            - *(string) --*

              - *(integer) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeImagesPaginatefilterTypeDef = TypedDict(
    "_DescribeImagesPaginatefilterTypeDef", {"tagStatus": str}, total=False
)


class DescribeImagesPaginatefilterTypeDef(_DescribeImagesPaginatefilterTypeDef):
    """
    Type definition for `DescribeImagesPaginate` `filter`

    The filter key and value with which to filter your ``DescribeImages`` results.

    - **tagStatus** *(string) --*

      The tag status with which to filter your  DescribeImages results. You can filter results based
      on whether they are ``TAGGED`` or ``UNTAGGED`` .
    """


_DescribeImagesPaginateimageIdsTypeDef = TypedDict(
    "_DescribeImagesPaginateimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class DescribeImagesPaginateimageIdsTypeDef(_DescribeImagesPaginateimageIdsTypeDef):
    """
    Type definition for `DescribeImagesPaginate` `imageIds`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_DescribeRepositoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeRepositoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeRepositoriesPaginatePaginationConfigTypeDef(
    _DescribeRepositoriesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeRepositoriesPaginate` `PaginationConfig`

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


_DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef = TypedDict(
    "_DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef(
    _DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef
):
    """
    Type definition for `DescribeRepositoriesPaginateResponserepositories` `imageScanningConfiguration`

    The image scanning configuration for a repository.

    - **scanOnPush** *(boolean) --*

      The setting that determines whether images are scanned after being pushed to a
      repository. If set to ``true`` , images will be scanned after being pushed. If this
      parameter is not specified, it will default to ``false`` and images will not be scanned
      unless a scan is manually started with the  StartImageScan API.
    """


_DescribeRepositoriesPaginateResponserepositoriesTypeDef = TypedDict(
    "_DescribeRepositoriesPaginateResponserepositoriesTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": str,
        "imageScanningConfiguration": DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef,
    },
    total=False,
)


class DescribeRepositoriesPaginateResponserepositoriesTypeDef(
    _DescribeRepositoriesPaginateResponserepositoriesTypeDef
):
    """
    Type definition for `DescribeRepositoriesPaginateResponse` `repositories`

    An object representing a repository.

    - **repositoryArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
      ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of
      the repository owner, repository namespace, and repository name. For example,
      ``arn:aws:ecr:region:012345678910:repository/test`` .

    - **registryId** *(string) --*

      The AWS account ID associated with the registry that contains the repository.

    - **repositoryName** *(string) --*

      The name of the repository.

    - **repositoryUri** *(string) --*

      The URI for the repository. You can use this URI for Docker ``push`` or ``pull``
      operations.

    - **createdAt** *(datetime) --*

      The date and time, in JavaScript date format, when the repository was created.

    - **imageTagMutability** *(string) --*

      The tag mutability setting for the repository.

    - **imageScanningConfiguration** *(dict) --*

      The image scanning configuration for a repository.

      - **scanOnPush** *(boolean) --*

        The setting that determines whether images are scanned after being pushed to a
        repository. If set to ``true`` , images will be scanned after being pushed. If this
        parameter is not specified, it will default to ``false`` and images will not be scanned
        unless a scan is manually started with the  StartImageScan API.
    """


_DescribeRepositoriesPaginateResponseTypeDef = TypedDict(
    "_DescribeRepositoriesPaginateResponseTypeDef",
    {
        "repositories": List[DescribeRepositoriesPaginateResponserepositoriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeRepositoriesPaginateResponseTypeDef(
    _DescribeRepositoriesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeRepositoriesPaginate` `Response`

    - **repositories** *(list) --*

      A list of repository objects corresponding to valid repositories.

      - *(dict) --*

        An object representing a repository.

        - **repositoryArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
          ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of
          the repository owner, repository namespace, and repository name. For example,
          ``arn:aws:ecr:region:012345678910:repository/test`` .

        - **registryId** *(string) --*

          The AWS account ID associated with the registry that contains the repository.

        - **repositoryName** *(string) --*

          The name of the repository.

        - **repositoryUri** *(string) --*

          The URI for the repository. You can use this URI for Docker ``push`` or ``pull``
          operations.

        - **createdAt** *(datetime) --*

          The date and time, in JavaScript date format, when the repository was created.

        - **imageTagMutability** *(string) --*

          The tag mutability setting for the repository.

        - **imageScanningConfiguration** *(dict) --*

          The image scanning configuration for a repository.

          - **scanOnPush** *(boolean) --*

            The setting that determines whether images are scanned after being pushed to a
            repository. If set to ``true`` , images will be scanned after being pushed. If this
            parameter is not specified, it will default to ``false`` and images will not be scanned
            unless a scan is manually started with the  StartImageScan API.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef(
    _GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetLifecyclePolicyPreviewPaginate` `PaginationConfig`

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


_GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef",
    {"type": str},
    total=False,
)


class GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef(
    _GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef
):
    """
    Type definition for `GetLifecyclePolicyPreviewPaginateResponsepreviewResults` `action`

    The type of action to be taken.

    - **type** *(string) --*

      The type of action to be taken.
    """


_GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef",
    {
        "imageTags": List[str],
        "imageDigest": str,
        "imagePushedAt": datetime,
        "action": GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef,
        "appliedRulePriority": int,
    },
    total=False,
)


class GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef(
    _GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef
):
    """
    Type definition for `GetLifecyclePolicyPreviewPaginateResponse` `previewResults`

    The result of the lifecycle policy preview.

    - **imageTags** *(list) --*

      The list of tags associated with this image.

      - *(string) --*

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imagePushedAt** *(datetime) --*

      The date and time, expressed in standard JavaScript date format, at which the current
      image was pushed to the repository.

    - **action** *(dict) --*

      The type of action to be taken.

      - **type** *(string) --*

        The type of action to be taken.

    - **appliedRulePriority** *(integer) --*

      The priority of the applied rule.
    """


_GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef",
    {"expiringImageTotalCount": int},
    total=False,
)


class GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef(
    _GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef
):
    """
    Type definition for `GetLifecyclePolicyPreviewPaginateResponse` `summary`

    The list of images that is returned as a result of the action.

    - **expiringImageTotalCount** *(integer) --*

      The number of expiring images.
    """


_GetLifecyclePolicyPreviewPaginateResponseTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": str,
        "previewResults": List[
            GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef
        ],
        "summary": GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef,
        "NextToken": str,
    },
    total=False,
)


class GetLifecyclePolicyPreviewPaginateResponseTypeDef(
    _GetLifecyclePolicyPreviewPaginateResponseTypeDef
):
    """
    Type definition for `GetLifecyclePolicyPreviewPaginate` `Response`

    - **registryId** *(string) --*

      The registry ID associated with the request.

    - **repositoryName** *(string) --*

      The repository name associated with the request.

    - **lifecyclePolicyText** *(string) --*

      The JSON lifecycle policy text.

    - **status** *(string) --*

      The status of the lifecycle policy preview request.

    - **previewResults** *(list) --*

      The results of the lifecycle policy preview request.

      - *(dict) --*

        The result of the lifecycle policy preview.

        - **imageTags** *(list) --*

          The list of tags associated with this image.

          - *(string) --*

        - **imageDigest** *(string) --*

          The ``sha256`` digest of the image manifest.

        - **imagePushedAt** *(datetime) --*

          The date and time, expressed in standard JavaScript date format, at which the current
          image was pushed to the repository.

        - **action** *(dict) --*

          The type of action to be taken.

          - **type** *(string) --*

            The type of action to be taken.

        - **appliedRulePriority** *(integer) --*

          The priority of the applied rule.

    - **summary** *(dict) --*

      The list of images that is returned as a result of the action.

      - **expiringImageTotalCount** *(integer) --*

        The number of expiring images.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetLifecyclePolicyPreviewPaginatefilterTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginatefilterTypeDef", {"tagStatus": str}, total=False
)


class GetLifecyclePolicyPreviewPaginatefilterTypeDef(
    _GetLifecyclePolicyPreviewPaginatefilterTypeDef
):
    """
    Type definition for `GetLifecyclePolicyPreviewPaginate` `filter`

    An optional parameter that filters results based on image tag status and all tags, if tagged.

    - **tagStatus** *(string) --*

      The tag status of the image.
    """


_GetLifecyclePolicyPreviewPaginateimageIdsTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class GetLifecyclePolicyPreviewPaginateimageIdsTypeDef(
    _GetLifecyclePolicyPreviewPaginateimageIdsTypeDef
):
    """
    Type definition for `GetLifecyclePolicyPreviewPaginate` `imageIds`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ListImagesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListImagesPaginatePaginationConfigTypeDef(
    _ListImagesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListImagesPaginate` `PaginationConfig`

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


_ListImagesPaginateResponseimageIdsTypeDef = TypedDict(
    "_ListImagesPaginateResponseimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ListImagesPaginateResponseimageIdsTypeDef(
    _ListImagesPaginateResponseimageIdsTypeDef
):
    """
    Type definition for `ListImagesPaginateResponse` `imageIds`

    An object with identifying information for an Amazon ECR image.

    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.

    - **imageTag** *(string) --*

      The tag used for the image.
    """


_ListImagesPaginateResponseTypeDef = TypedDict(
    "_ListImagesPaginateResponseTypeDef",
    {"imageIds": List[ListImagesPaginateResponseimageIdsTypeDef], "NextToken": str},
    total=False,
)


class ListImagesPaginateResponseTypeDef(_ListImagesPaginateResponseTypeDef):
    """
    Type definition for `ListImagesPaginate` `Response`

    - **imageIds** *(list) --*

      The list of image IDs for the requested repository.

      - *(dict) --*

        An object with identifying information for an Amazon ECR image.

        - **imageDigest** *(string) --*

          The ``sha256`` digest of the image manifest.

        - **imageTag** *(string) --*

          The tag used for the image.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListImagesPaginatefilterTypeDef = TypedDict(
    "_ListImagesPaginatefilterTypeDef", {"tagStatus": str}, total=False
)


class ListImagesPaginatefilterTypeDef(_ListImagesPaginatefilterTypeDef):
    """
    Type definition for `ListImagesPaginate` `filter`

    The filter key and value with which to filter your ``ListImages`` results.

    - **tagStatus** *(string) --*

      The tag status with which to filter your  ListImages results. You can filter results based on
      whether they are ``TAGGED`` or ``UNTAGGED`` .
    """
