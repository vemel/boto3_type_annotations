"Main interface for ecr Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ecr.type_defs import (
    DescribeImageScanFindingsPaginatePaginationConfigTypeDef,
    DescribeImageScanFindingsPaginateResponseTypeDef,
    DescribeImageScanFindingsPaginateimageIdTypeDef,
    DescribeImagesPaginatePaginationConfigTypeDef,
    DescribeImagesPaginateResponseTypeDef,
    DescribeImagesPaginatefilterTypeDef,
    DescribeImagesPaginateimageIdsTypeDef,
    DescribeRepositoriesPaginatePaginationConfigTypeDef,
    DescribeRepositoriesPaginateResponseTypeDef,
    GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef,
    GetLifecyclePolicyPreviewPaginateResponseTypeDef,
    GetLifecyclePolicyPreviewPaginatefilterTypeDef,
    GetLifecyclePolicyPreviewPaginateimageIdsTypeDef,
    ListImagesPaginatePaginationConfigTypeDef,
    ListImagesPaginateResponseTypeDef,
    ListImagesPaginatefilterTypeDef,
)


__all__ = (
    "DescribeImageScanFindingsPaginator",
    "DescribeImagesPaginator",
    "DescribeRepositoriesPaginator",
    "GetLifecyclePolicyPreviewPaginator",
    "ListImagesPaginator",
)


class DescribeImageScanFindingsPaginator(Boto3Paginator):
    """
    Paginator for `describe_image_scan_findings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        imageId: DescribeImageScanFindingsPaginateimageIdTypeDef,
        registryId: str = None,
        PaginationConfig: DescribeImageScanFindingsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeImageScanFindingsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ECR.Client.describe_image_scan_findings`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DescribeImageScanFindings>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              registryId='string',
              repositoryName='string',
              imageId={
                  'imageDigest': 'string',
                  'imageTag': 'string'
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type registryId: string
        :param registryId:

          The AWS account ID associated with the registry that contains the repository in which to describe
          the image scan findings for. If you do not specify a registry, the default registry is assumed.

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The repository for the image for which to describe the scan findings.

        :type imageId: dict
        :param imageId: **[REQUIRED]**

          An object with identifying information for an Amazon ECR image.

          - **imageDigest** *(string) --*

            The ``sha256`` digest of the image manifest.

          - **imageTag** *(string) --*

            The tag used for the image.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'registryId': 'string',
                'repositoryName': 'string',
                'imageId': {
                    'imageDigest': 'string',
                    'imageTag': 'string'
                },
                'imageScanStatus': {
                    'status': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
                    'description': 'string'
                },
                'imageScanFindings': {
                    'imageScanCompletedAt': datetime(2015, 1, 1),
                    'vulnerabilitySourceUpdatedAt': datetime(2015, 1, 1),
                    'findings': [
                        {
                            'name': 'string',
                            'description': 'string',
                            'uri': 'string',
                            'severity': 'INFORMATIONAL'|'LOW'|'MEDIUM'|'HIGH'|'CRITICAL'|'UNDEFINED',
                            'attributes': [
                                {
                                    'key': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ],
                    'findingSeverityCounts': {
                        'string': 123
                    }
                },
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class DescribeImagesPaginator(Boto3Paginator):
    """
    Paginator for `describe_images`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[DescribeImagesPaginateimageIdsTypeDef] = None,
        filter: DescribeImagesPaginatefilterTypeDef = None,
        PaginationConfig: DescribeImagesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeImagesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ECR.Client.describe_images`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DescribeImages>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              registryId='string',
              repositoryName='string',
              imageIds=[
                  {
                      'imageDigest': 'string',
                      'imageTag': 'string'
                  },
              ],
              filter={
                  'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type registryId: string
        :param registryId:

          The AWS account ID associated with the registry that contains the repository in which to describe
          images. If you do not specify a registry, the default registry is assumed.

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The repository that contains the images to describe.

        :type imageIds: list
        :param imageIds:

          The list of image IDs for the requested repository.

          - *(dict) --*

            An object with identifying information for an Amazon ECR image.

            - **imageDigest** *(string) --*

              The ``sha256`` digest of the image manifest.

            - **imageTag** *(string) --*

              The tag used for the image.

        :type filter: dict
        :param filter:

          The filter key and value with which to filter your ``DescribeImages`` results.

          - **tagStatus** *(string) --*

            The tag status with which to filter your  DescribeImages results. You can filter results based
            on whether they are ``TAGGED`` or ``UNTAGGED`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'imageDetails': [
                    {
                        'registryId': 'string',
                        'repositoryName': 'string',
                        'imageDigest': 'string',
                        'imageTags': [
                            'string',
                        ],
                        'imageSizeInBytes': 123,
                        'imagePushedAt': datetime(2015, 1, 1),
                        'imageScanStatus': {
                            'status': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
                            'description': 'string'
                        },
                        'imageScanFindingsSummary': {
                            'imageScanCompletedAt': datetime(2015, 1, 1),
                            'vulnerabilitySourceUpdatedAt': datetime(2015, 1, 1),
                            'findingSeverityCounts': {
                                'string': 123
                            }
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class DescribeRepositoriesPaginator(Boto3Paginator):
    """
    Paginator for `describe_repositories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        registryId: str = None,
        repositoryNames: List[str] = None,
        PaginationConfig: DescribeRepositoriesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeRepositoriesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ECR.Client.describe_repositories`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/DescribeRepositories>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              registryId='string',
              repositoryNames=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type registryId: string
        :param registryId:

          The AWS account ID associated with the registry that contains the repositories to be described.
          If you do not specify a registry, the default registry is assumed.

        :type repositoryNames: list
        :param repositoryNames:

          A list of repositories to describe. If this parameter is omitted, then all repositories in a
          registry are described.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'repositories': [
                    {
                        'repositoryArn': 'string',
                        'registryId': 'string',
                        'repositoryName': 'string',
                        'repositoryUri': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'imageTagMutability': 'MUTABLE'|'IMMUTABLE',
                        'imageScanningConfiguration': {
                            'scanOnPush': True|False
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class GetLifecyclePolicyPreviewPaginator(Boto3Paginator):
    """
    Paginator for `get_lifecycle_policy_preview`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[GetLifecyclePolicyPreviewPaginateimageIdsTypeDef] = None,
        filter: GetLifecyclePolicyPreviewPaginatefilterTypeDef = None,
        PaginationConfig: GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef = None,
    ) -> GetLifecyclePolicyPreviewPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ECR.Client.get_lifecycle_policy_preview`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/GetLifecyclePolicyPreview>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              registryId='string',
              repositoryName='string',
              imageIds=[
                  {
                      'imageDigest': 'string',
                      'imageTag': 'string'
                  },
              ],
              filter={
                  'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type registryId: string
        :param registryId:

          The AWS account ID associated with the registry that contains the repository. If you do not
          specify a registry, the default registry is assumed.

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository.

        :type imageIds: list
        :param imageIds:

          The list of imageIDs to be included.

          - *(dict) --*

            An object with identifying information for an Amazon ECR image.

            - **imageDigest** *(string) --*

              The ``sha256`` digest of the image manifest.

            - **imageTag** *(string) --*

              The tag used for the image.

        :type filter: dict
        :param filter:

          An optional parameter that filters results based on image tag status and all tags, if tagged.

          - **tagStatus** *(string) --*

            The tag status of the image.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'registryId': 'string',
                'repositoryName': 'string',
                'lifecyclePolicyText': 'string',
                'status': 'IN_PROGRESS'|'COMPLETE'|'EXPIRED'|'FAILED',
                'previewResults': [
                    {
                        'imageTags': [
                            'string',
                        ],
                        'imageDigest': 'string',
                        'imagePushedAt': datetime(2015, 1, 1),
                        'action': {
                            'type': 'EXPIRE'
                        },
                        'appliedRulePriority': 123
                    },
                ],
                'summary': {
                    'expiringImageTotalCount': 123
                },
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListImagesPaginator(Boto3Paginator):
    """
    Paginator for `list_images`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        filter: ListImagesPaginatefilterTypeDef = None,
        PaginationConfig: ListImagesPaginatePaginationConfigTypeDef = None,
    ) -> ListImagesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ECR.Client.list_images`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ecr-2015-09-21/ListImages>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              registryId='string',
              repositoryName='string',
              filter={
                  'tagStatus': 'TAGGED'|'UNTAGGED'|'ANY'
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type registryId: string
        :param registryId:

          The AWS account ID associated with the registry that contains the repository in which to list
          images. If you do not specify a registry, the default registry is assumed.

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The repository with image IDs to be listed.

        :type filter: dict
        :param filter:

          The filter key and value with which to filter your ``ListImages`` results.

          - **tagStatus** *(string) --*

            The tag status with which to filter your  ListImages results. You can filter results based on
            whether they are ``TAGGED`` or ``UNTAGGED`` .

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'imageIds': [
                    {
                        'imageDigest': 'string',
                        'imageTag': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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
