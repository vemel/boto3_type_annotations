"Main interface for mobile Client"
from __future__ import annotations

from typing import Dict, IO, Union
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_mobile.client as client_scope

# pylint: disable=import-self
import mypy_boto3_mobile.paginator as paginator_scope
from mypy_boto3_mobile.type_defs import (
    ClientCreateProjectResponseTypeDef,
    ClientDeleteProjectResponseTypeDef,
    ClientDescribeBundleResponseTypeDef,
    ClientDescribeProjectResponseTypeDef,
    ClientExportBundleResponseTypeDef,
    ClientExportProjectResponseTypeDef,
    ClientListBundlesResponseTypeDef,
    ClientListProjectsResponseTypeDef,
    ClientUpdateProjectResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

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
    def create_project(
        self,
        name: str = None,
        region: str = None,
        contents: Union[bytes, IO] = None,
        snapshotId: str = None,
    ) -> ClientCreateProjectResponseTypeDef:
        """
        Creates an AWS Mobile Hub project.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/CreateProject>`_

        **Request Syntax**
        ::

          response = client.create_project(
              name='string',
              region='string',
              contents=b'bytes'|file,
              snapshotId='string'
          )
        :type name: string
        :param name:

          Name of the project.

        :type region: string
        :param region:

          Default region where project resources should be created.

        :type contents: bytes or seekable file-like object
        :param contents:

          ZIP or YAML file which contains configuration settings to be used when creating the project. This
          may be the contents of the file downloaded from the URL provided in an export project operation.

        :type snapshotId: string
        :param snapshotId:

          Unique identifier for an exported snapshot of project configuration. This snapshot identifier is
          included in the share URL when a project is exported.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'details': {
                    'name': 'string',
                    'projectId': 'string',
                    'region': 'string',
                    'state': 'NORMAL'|'SYNCING'|'IMPORTING',
                    'createdDate': datetime(2015, 1, 1),
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'consoleUrl': 'string',
                    'resources': [
                        {
                            'type': 'string',
                            'name': 'string',
                            'arn': 'string',
                            'feature': 'string',
                            'attributes': {
                                'string': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure used in response to a request to create a project.

            - **details** *(dict) --*

              Detailed information about the created AWS Mobile Hub project.

              - **name** *(string) --*

                Name of the project.

              - **projectId** *(string) --*

                Unique project identifier.

              - **region** *(string) --*

                Default region to use for AWS resource creation in the AWS Mobile Hub project.

              - **state** *(string) --*

                Synchronization state for a project.

              - **createdDate** *(datetime) --*

                Date the project was created.

              - **lastUpdatedDate** *(datetime) --*

                Date of the last modification of the project.

              - **consoleUrl** *(string) --*

                Website URL for this project in the AWS Mobile Hub console.

              - **resources** *(list) --*

                List of AWS resources associated with a project.

                - *(dict) --*

                  Information about an instance of an AWS resource associated with a project.

                  - **type** *(string) --*

                    Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

                  - **name** *(string) --*

                    Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

                  - **arn** *(string) --*

                    AWS resource name which uniquely identifies the resource in AWS systems.

                  - **feature** *(string) --*

                    Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

                  - **attributes** *(dict) --*

                    Key-value attribute pairs.

                    - *(string) --*

                      Key part of key-value attribute pairs.

                      - *(string) --*

                        Value part of key-value attribute pairs.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_project(self, projectId: str) -> ClientDeleteProjectResponseTypeDef:
        """
        Delets a project in AWS Mobile Hub.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/DeleteProject>`_

        **Request Syntax**
        ::

          response = client.delete_project(
              projectId='string'
          )
        :type projectId: string
        :param projectId: **[REQUIRED]**

          Unique project identifier.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deletedResources': [
                    {
                        'type': 'string',
                        'name': 'string',
                        'arn': 'string',
                        'feature': 'string',
                        'attributes': {
                            'string': 'string'
                        }
                    },
                ],
                'orphanedResources': [
                    {
                        'type': 'string',
                        'name': 'string',
                        'arn': 'string',
                        'feature': 'string',
                        'attributes': {
                            'string': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Result structure used in response to request to delete a project.

            - **deletedResources** *(list) --*

              Resources which were deleted.

              - *(dict) --*

                Information about an instance of an AWS resource associated with a project.

                - **type** *(string) --*

                  Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

                - **name** *(string) --*

                  Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

                - **arn** *(string) --*

                  AWS resource name which uniquely identifies the resource in AWS systems.

                - **feature** *(string) --*

                  Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

                - **attributes** *(dict) --*

                  Key-value attribute pairs.

                  - *(string) --*

                    Key part of key-value attribute pairs.

                    - *(string) --*

                      Value part of key-value attribute pairs.

            - **orphanedResources** *(list) --*

              Resources which were not deleted, due to a risk of losing potentially important data or files.

              - *(dict) --*

                Information about an instance of an AWS resource associated with a project.

                - **type** *(string) --*

                  Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

                - **name** *(string) --*

                  Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

                - **arn** *(string) --*

                  AWS resource name which uniquely identifies the resource in AWS systems.

                - **feature** *(string) --*

                  Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

                - **attributes** *(dict) --*

                  Key-value attribute pairs.

                  - *(string) --*

                    Key part of key-value attribute pairs.

                    - *(string) --*

                      Value part of key-value attribute pairs.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_bundle(self, bundleId: str) -> ClientDescribeBundleResponseTypeDef:
        """
        Get the bundle details for the requested bundle id.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/DescribeBundle>`_

        **Request Syntax**
        ::

          response = client.describe_bundle(
              bundleId='string'
          )
        :type bundleId: string
        :param bundleId: **[REQUIRED]**

          Unique bundle identifier.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'details': {
                    'bundleId': 'string',
                    'title': 'string',
                    'version': 'string',
                    'description': 'string',
                    'iconUrl': 'string',
                    'availablePlatforms': [
                        'OSX'|'WINDOWS'|'LINUX'|'OBJC'|'SWIFT'|'ANDROID'|'JAVASCRIPT',
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure contains the details of the bundle.

            - **details** *(dict) --*

              The details of the bundle.

              - **bundleId** *(string) --*

                Unique bundle identifier.

              - **title** *(string) --*

                Title of the download bundle.

              - **version** *(string) --*

                Version of the download bundle.

              - **description** *(string) --*

                Description of the download bundle.

              - **iconUrl** *(string) --*

                Icon for the download bundle.

              - **availablePlatforms** *(list) --*

                Developer desktop or mobile app or website platforms.

                - *(string) --*

                  Developer desktop or target mobile app or website platform.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_project(
        self, projectId: str, syncFromResources: bool = None
    ) -> ClientDescribeProjectResponseTypeDef:
        """
        Gets details about a project in AWS Mobile Hub.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/DescribeProject>`_

        **Request Syntax**
        ::

          response = client.describe_project(
              projectId='string',
              syncFromResources=True|False
          )
        :type projectId: string
        :param projectId: **[REQUIRED]**

          Unique project identifier.

        :type syncFromResources: boolean
        :param syncFromResources:

          If set to true, causes AWS Mobile Hub to synchronize information from other services, e.g.,
          update state of AWS CloudFormation stacks in the AWS Mobile Hub project.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'details': {
                    'name': 'string',
                    'projectId': 'string',
                    'region': 'string',
                    'state': 'NORMAL'|'SYNCING'|'IMPORTING',
                    'createdDate': datetime(2015, 1, 1),
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'consoleUrl': 'string',
                    'resources': [
                        {
                            'type': 'string',
                            'name': 'string',
                            'arn': 'string',
                            'feature': 'string',
                            'attributes': {
                                'string': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure used for requests of project details.

            - **details** *(dict) --*

              Detailed information about an AWS Mobile Hub project.

              - **name** *(string) --*

                Name of the project.

              - **projectId** *(string) --*

                Unique project identifier.

              - **region** *(string) --*

                Default region to use for AWS resource creation in the AWS Mobile Hub project.

              - **state** *(string) --*

                Synchronization state for a project.

              - **createdDate** *(datetime) --*

                Date the project was created.

              - **lastUpdatedDate** *(datetime) --*

                Date of the last modification of the project.

              - **consoleUrl** *(string) --*

                Website URL for this project in the AWS Mobile Hub console.

              - **resources** *(list) --*

                List of AWS resources associated with a project.

                - *(dict) --*

                  Information about an instance of an AWS resource associated with a project.

                  - **type** *(string) --*

                    Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

                  - **name** *(string) --*

                    Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

                  - **arn** *(string) --*

                    AWS resource name which uniquely identifies the resource in AWS systems.

                  - **feature** *(string) --*

                    Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

                  - **attributes** *(dict) --*

                    Key-value attribute pairs.

                    - *(string) --*

                      Key part of key-value attribute pairs.

                      - *(string) --*

                        Value part of key-value attribute pairs.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_bundle(
        self, bundleId: str, projectId: str = None, platform: str = None
    ) -> ClientExportBundleResponseTypeDef:
        """
        Generates customized software development kit (SDK) and or tool packages used to integrate mobile
        web or mobile app clients with backend AWS resources.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/ExportBundle>`_

        **Request Syntax**
        ::

          response = client.export_bundle(
              bundleId='string',
              projectId='string',
              platform='OSX'|'WINDOWS'|'LINUX'|'OBJC'|'SWIFT'|'ANDROID'|'JAVASCRIPT'
          )
        :type bundleId: string
        :param bundleId: **[REQUIRED]**

          Unique bundle identifier.

        :type projectId: string
        :param projectId:

          Unique project identifier.

        :type platform: string
        :param platform:

          Developer desktop or target application platform.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'downloadUrl': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure which contains link to download custom-generated SDK and tool packages used to
            integrate mobile web or app clients with backed AWS resources.

            - **downloadUrl** *(string) --*

              URL which contains the custom-generated SDK and tool packages used to integrate the client
              mobile app or web app with the AWS resources created by the AWS Mobile Hub project.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_project(self, projectId: str) -> ClientExportProjectResponseTypeDef:
        """
        Exports project configuration to a snapshot which can be downloaded and shared. Note that mobile
        app push credentials are encrypted in exported projects, so they can only be shared successfully
        within the same AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/ExportProject>`_

        **Request Syntax**
        ::

          response = client.export_project(
              projectId='string'
          )
        :type projectId: string
        :param projectId: **[REQUIRED]**

          Unique project identifier.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'downloadUrl': 'string',
                'shareUrl': 'string',
                'snapshotId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure used for requests to export project configuration details.

            - **downloadUrl** *(string) --*

              URL which can be used to download the exported project configuation file(s).

            - **shareUrl** *(string) --*

              URL which can be shared to allow other AWS users to create their own project in AWS Mobile
              Hub with the same configuration as the specified project. This URL pertains to a snapshot in
              time of the project configuration that is created when this API is called. If you want to
              share additional changes to your project configuration, then you will need to create and
              share a new snapshot by calling this method again.

            - **snapshotId** *(string) --*

              Unique identifier for the exported snapshot of the project configuration. This snapshot
              identifier is included in the share URL.

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
    def list_bundles(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListBundlesResponseTypeDef:
        """
        List all available bundles.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/ListBundles>`_

        **Request Syntax**
        ::

          response = client.list_bundles(
              maxResults=123,
              nextToken='string'
          )
        :type maxResults: integer
        :param maxResults:

          Maximum number of records to list in a single response.

        :type nextToken: string
        :param nextToken:

          Pagination token. Set to null to start listing bundles from start. If non-null pagination token
          is returned in a result, then pass its value in here in another request to list more bundles.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'bundleList': [
                    {
                        'bundleId': 'string',
                        'title': 'string',
                        'version': 'string',
                        'description': 'string',
                        'iconUrl': 'string',
                        'availablePlatforms': [
                            'OSX'|'WINDOWS'|'LINUX'|'OBJC'|'SWIFT'|'ANDROID'|'JAVASCRIPT',
                        ]
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure contains a list of all available bundles with details.

            - **bundleList** *(list) --*

              A list of bundles.

              - *(dict) --*

                The details of the bundle.

                - **bundleId** *(string) --*

                  Unique bundle identifier.

                - **title** *(string) --*

                  Title of the download bundle.

                - **version** *(string) --*

                  Version of the download bundle.

                - **description** *(string) --*

                  Description of the download bundle.

                - **iconUrl** *(string) --*

                  Icon for the download bundle.

                - **availablePlatforms** *(list) --*

                  Developer desktop or mobile app or website platforms.

                  - *(string) --*

                    Developer desktop or target mobile app or website platform.

            - **nextToken** *(string) --*

              Pagination token. If non-null pagination token is returned in a result, then pass its value
              in another request to fetch more entries.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_projects(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListProjectsResponseTypeDef:
        """
        Lists projects in AWS Mobile Hub.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/ListProjects>`_

        **Request Syntax**
        ::

          response = client.list_projects(
              maxResults=123,
              nextToken='string'
          )
        :type maxResults: integer
        :param maxResults:

          Maximum number of records to list in a single response.

        :type nextToken: string
        :param nextToken:

          Pagination token. Set to null to start listing projects from start. If non-null pagination token
          is returned in a result, then pass its value in here in another request to list more projects.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'projects': [
                    {
                        'name': 'string',
                        'projectId': 'string'
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Result structure used for requests to list projects in AWS Mobile Hub.

            - **projects** *(list) --*

              List of projects.

              - *(dict) --*

                Summary information about an AWS Mobile Hub project.

                - **name** *(string) --*

                  Name of the project.

                - **projectId** *(string) --*

                  Unique project identifier.

            - **nextToken** *(string) --*

              Pagination token. Set to null to start listing records from start. If non-null pagination
              token is returned in a result, then pass its value in here in another request to list more
              entries.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_project(
        self, projectId: str, contents: Union[bytes, IO] = None
    ) -> ClientUpdateProjectResponseTypeDef:
        """
        Update an existing project.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mobile-2017-07-01/UpdateProject>`_

        **Request Syntax**
        ::

          response = client.update_project(
              contents=b'bytes'|file,
              projectId='string'
          )
        :type contents: bytes or seekable file-like object
        :param contents:

          ZIP or YAML file which contains project configuration to be updated. This should be the contents
          of the file downloaded from the URL provided in an export project operation.

        :type projectId: string
        :param projectId: **[REQUIRED]**

          Unique project identifier.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'details': {
                    'name': 'string',
                    'projectId': 'string',
                    'region': 'string',
                    'state': 'NORMAL'|'SYNCING'|'IMPORTING',
                    'createdDate': datetime(2015, 1, 1),
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'consoleUrl': 'string',
                    'resources': [
                        {
                            'type': 'string',
                            'name': 'string',
                            'arn': 'string',
                            'feature': 'string',
                            'attributes': {
                                'string': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            Result structure used for requests to updated project configuration.

            - **details** *(dict) --*

              Detailed information about the updated AWS Mobile Hub project.

              - **name** *(string) --*

                Name of the project.

              - **projectId** *(string) --*

                Unique project identifier.

              - **region** *(string) --*

                Default region to use for AWS resource creation in the AWS Mobile Hub project.

              - **state** *(string) --*

                Synchronization state for a project.

              - **createdDate** *(datetime) --*

                Date the project was created.

              - **lastUpdatedDate** *(datetime) --*

                Date of the last modification of the project.

              - **consoleUrl** *(string) --*

                Website URL for this project in the AWS Mobile Hub console.

              - **resources** *(list) --*

                List of AWS resources associated with a project.

                - *(dict) --*

                  Information about an instance of an AWS resource associated with a project.

                  - **type** *(string) --*

                    Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).

                  - **name** *(string) --*

                    Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).

                  - **arn** *(string) --*

                    AWS resource name which uniquely identifies the resource in AWS systems.

                  - **feature** *(string) --*

                    Identifies which feature in AWS Mobile Hub is associated with this AWS resource.

                  - **attributes** *(dict) --*

                    Key-value attribute pairs.

                    - *(string) --*

                      Key part of key-value attribute pairs.

                      - *(string) --*

                        Value part of key-value attribute pairs.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_bundles"]
    ) -> paginator_scope.ListBundlesPaginator:
        """
        Get Paginator for `list_bundles` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> paginator_scope.ListProjectsPaginator:
        """
        Get Paginator for `list_projects` operation.
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


class Exceptions:
    AccountActionRequiredException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
