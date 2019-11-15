"Main interface for workspaces Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_workspaces.type_defs import (
    DescribeAccountModificationsPaginatePaginationConfigTypeDef,
    DescribeAccountModificationsPaginateResponseTypeDef,
    DescribeIpGroupsPaginatePaginationConfigTypeDef,
    DescribeIpGroupsPaginateResponseTypeDef,
    DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef,
    DescribeWorkspaceBundlesPaginateResponseTypeDef,
    DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef,
    DescribeWorkspaceDirectoriesPaginateResponseTypeDef,
    DescribeWorkspaceImagesPaginatePaginationConfigTypeDef,
    DescribeWorkspaceImagesPaginateResponseTypeDef,
    DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef,
    DescribeWorkspacesConnectionStatusPaginateResponseTypeDef,
    DescribeWorkspacesPaginatePaginationConfigTypeDef,
    DescribeWorkspacesPaginateResponseTypeDef,
    ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef,
    ListAvailableManagementCidrRangesPaginateResponseTypeDef,
)


class DescribeAccountModifications(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        PaginationConfig: DescribeAccountModificationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAccountModificationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`WorkSpaces.Client.describe_account_modifications`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeAccountModifications>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AccountModifications': [
                    {
                        'ModificationState': 'PENDING'|'COMPLETED'|'FAILED',
                        'DedicatedTenancySupport': 'ENABLED'|'DISABLED',
                        'DedicatedTenancyManagementCidrRange': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **AccountModifications** *(list) --*

              The list of modifications to the configuration of BYOL.

              - *(dict) --*

                Describes a modification to the configuration of bring your own license (BYOL) for the
                specified account.

                - **ModificationState** *(string) --*

                  The state of the modification to the configuration of BYOL.

                - **DedicatedTenancySupport** *(string) --*

                  The status of BYOL (whether BYOL is being enabled or disabled).

                - **DedicatedTenancyManagementCidrRange** *(string) --*

                  The IP address range, specified as an IPv4 CIDR block, for the management network
                  interface used for the account.

                - **StartTime** *(datetime) --*

                  The timestamp when the modification of the BYOL configuration was started.

                - **ErrorCode** *(string) --*

                  The error code that is returned if the configuration of BYOL cannot be modified.

                - **ErrorMessage** *(string) --*

                  The text of the error message that is returned if the configuration of BYOL cannot be
                  modified.

        """


class DescribeIpGroups(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        GroupIds: List[str] = None,
        PaginationConfig: DescribeIpGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeIpGroupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`WorkSpaces.Client.describe_ip_groups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeIpGroups>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              GroupIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type GroupIds: list
        :param GroupIds:

          The identifiers of one or more IP access control groups.

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
                'Result': [
                    {
                        'groupId': 'string',
                        'groupName': 'string',
                        'groupDesc': 'string',
                        'userRules': [
                            {
                                'ipRule': 'string',
                                'ruleDesc': 'string'
                            },
                        ]
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Result** *(list) --*

              Information about the IP access control groups.

              - *(dict) --*

                Describes an IP access control group.

                - **groupId** *(string) --*

                  The identifier of the group.

                - **groupName** *(string) --*

                  The name of the group.

                - **groupDesc** *(string) --*

                  The description of the group.

                - **userRules** *(list) --*

                  The rules.

                  - *(dict) --*

                    Describes a rule for an IP access control group.

                    - **ipRule** *(string) --*

                      The IP address range, in CIDR notation.

                    - **ruleDesc** *(string) --*

                      The description.

        """


class DescribeWorkspaceBundles(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        BundleIds: List[str] = None,
        Owner: str = None,
        PaginationConfig: DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeWorkspaceBundlesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`WorkSpaces.Client.describe_workspace_bundles`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceBundles>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              BundleIds=[
                  'string',
              ],
              Owner='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type BundleIds: list
        :param BundleIds:

          The identifiers of the bundles. You cannot combine this parameter with any other filter.

          - *(string) --*

        :type Owner: string
        :param Owner:

          The owner of the bundles. You cannot combine this parameter with any other filter.

          Specify ``AMAZON`` to describe the bundles provided by AWS or null to describe the bundles that
          belong to your account.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Bundles': [
                    {
                        'BundleId': 'string',
                        'Name': 'string',
                        'Owner': 'string',
                        'Description': 'string',
                        'RootStorage': {
                            'Capacity': 'string'
                        },
                        'UserStorage': {
                            'Capacity': 'string'
                        },
                        'ComputeType': {
                            'Name':
                            'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Bundles** *(list) --*

              Information about the bundles.

              - *(dict) --*

                Describes a WorkSpace bundle.

                - **BundleId** *(string) --*

                  The bundle identifier.

                - **Name** *(string) --*

                  The name of the bundle.

                - **Owner** *(string) --*

                  The owner of the bundle. This is the account identifier of the owner, or ``AMAZON`` if
                  the bundle is provided by AWS.

                - **Description** *(string) --*

                  A description.

                - **RootStorage** *(dict) --*

                  The size of the root volume.

                  - **Capacity** *(string) --*

                    The size of the root volume.

                - **UserStorage** *(dict) --*

                  The size of the user storage.

                  - **Capacity** *(string) --*

                    The size of the user storage.

                - **ComputeType** *(dict) --*

                  The compute type. For more information, see `Amazon WorkSpaces Bundles
                  <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

                  - **Name** *(string) --*

                    The compute type.

        """


class DescribeWorkspaceDirectories(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryIds: List[str] = None,
        PaginationConfig: DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeWorkspaceDirectoriesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`WorkSpaces.Client.describe_workspace_directories`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceDirectories>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              DirectoryIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type DirectoryIds: list
        :param DirectoryIds:

          The identifiers of the directories. If the value is null, all directories are retrieved.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Directories': [
                    {
                        'DirectoryId': 'string',
                        'Alias': 'string',
                        'DirectoryName': 'string',
                        'RegistrationCode': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'DnsIpAddresses': [
                            'string',
                        ],
                        'CustomerUserName': 'string',
                        'IamRoleId': 'string',
                        'DirectoryType': 'SIMPLE_AD'|'AD_CONNECTOR',
                        'WorkspaceSecurityGroupId': 'string',
                        'State': 'REGISTERING'|'REGISTERED'|'DEREGISTERING'|'DEREGISTERED'|'ERROR',
                        'WorkspaceCreationProperties': {
                            'EnableWorkDocs': True|False,
                            'EnableInternetAccess': True|False,
                            'DefaultOu': 'string',
                            'CustomSecurityGroupId': 'string',
                            'UserEnabledAsLocalAdministrator': True|False
                        },
                        'ipGroupIds': [
                            'string',
                        ]
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Directories** *(list) --*

              Information about the directories.

              - *(dict) --*

                Describes an AWS Directory Service directory that is used with Amazon WorkSpaces.

                - **DirectoryId** *(string) --*

                  The directory identifier.

                - **Alias** *(string) --*

                  The directory alias.

                - **DirectoryName** *(string) --*

                  The name of the directory.

                - **RegistrationCode** *(string) --*

                  The registration code for the directory. This is the code that users enter in their
                  Amazon WorkSpaces client application to connect to the directory.

                - **SubnetIds** *(list) --*

                  The identifiers of the subnets used with the directory.

                  - *(string) --*

                - **DnsIpAddresses** *(list) --*

                  The IP addresses of the DNS servers for the directory.

                  - *(string) --*

                - **CustomerUserName** *(string) --*

                  The user name for the service account.

                - **IamRoleId** *(string) --*

                  The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make
                  calls to other services, such as Amazon EC2, on your behalf.

                - **DirectoryType** *(string) --*

                  The directory type.

                - **WorkspaceSecurityGroupId** *(string) --*

                  The identifier of the security group that is assigned to new WorkSpaces.

                - **State** *(string) --*

                  The state of the directory's registration with Amazon WorkSpaces

                - **WorkspaceCreationProperties** *(dict) --*

                  The default creation properties for all WorkSpaces in the directory.

                  - **EnableWorkDocs** *(boolean) --*

                    Specifies whether the directory is enabled for Amazon WorkDocs.

                  - **EnableInternetAccess** *(boolean) --*

                    Specifies whether to automatically assign a public IP address to WorkSpaces in this
                    directory by default. If enabled, the public IP address allows outbound internet access
                    from your WorkSpaces when you’re using an internet gateway in the Amazon VPC in which
                    your WorkSpaces are located. If you're using a Network Address Translation (NAT)
                    gateway for outbound internet access from your VPC, or if your WorkSpaces are in public
                    subnets and you manually assign them Elastic IP addresses, you should disable this
                    setting. This setting applies to new WorkSpaces that you launch or to existing
                    WorkSpaces that you rebuild. For more information, see `Configure a VPC for Amazon
                    WorkSpaces
                    <https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html>`__
                    .

                  - **DefaultOu** *(string) --*

                    The organizational unit (OU) in the directory for the WorkSpace machine accounts.

                  - **CustomSecurityGroupId** *(string) --*

                    The identifier of any security groups to apply to WorkSpaces when they are created.

                  - **UserEnabledAsLocalAdministrator** *(boolean) --*

                    Specifies whether the WorkSpace user is an administrator on the WorkSpace.

                - **ipGroupIds** *(list) --*

                  The identifiers of the IP access control groups associated with the directory.

                  - *(string) --*

        """


class DescribeWorkspaceImages(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        ImageIds: List[str] = None,
        PaginationConfig: DescribeWorkspaceImagesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeWorkspaceImagesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`WorkSpaces.Client.describe_workspace_images`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceImages>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ImageIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ImageIds: list
        :param ImageIds:

          The identifier of the image.

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
                'Images': [
                    {
                        'ImageId': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'OperatingSystem': {
                            'Type': 'WINDOWS'|'LINUX'
                        },
                        'State': 'AVAILABLE'|'PENDING'|'ERROR',
                        'RequiredTenancy': 'DEFAULT'|'DEDICATED',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Images** *(list) --*

              Information about the images.

              - *(dict) --*

                Describes a WorkSpace image.

                - **ImageId** *(string) --*

                  The identifier of the image.

                - **Name** *(string) --*

                  The name of the image.

                - **Description** *(string) --*

                  The description of the image.

                - **OperatingSystem** *(dict) --*

                  The operating system that the image is running.

                  - **Type** *(string) --*

                    The operating system.

                - **State** *(string) --*

                  The status of the image.

                - **RequiredTenancy** *(string) --*

                  Specifies whether the image is running on dedicated hardware. When bring your own license
                  (BYOL) is enabled, this value is set to DEDICATED.

                - **ErrorCode** *(string) --*

                  The error code that is returned for the image.

                - **ErrorMessage** *(string) --*

                  The text of the error message that is returned for the image.

        """


class DescribeWorkspaces(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        PaginationConfig: DescribeWorkspacesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeWorkspacesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`WorkSpaces.Client.describe_workspaces`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaces>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              WorkspaceIds=[
                  'string',
              ],
              DirectoryId='string',
              UserName='string',
              BundleId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type WorkspaceIds: list
        :param WorkspaceIds:

          The identifiers of the WorkSpaces. You cannot combine this parameter with any other filter.

          Because the  CreateWorkspaces operation is asynchronous, the identifier it returns is not
          immediately available. If you immediately call  DescribeWorkspaces with this identifier, no
          information is returned.

          - *(string) --*

        :type DirectoryId: string
        :param DirectoryId:

          The identifier of the directory. In addition, you can optionally specify a specific directory
          user (see ``UserName`` ). You cannot combine this parameter with any other filter.

        :type UserName: string
        :param UserName:

          The name of the directory user. You must specify this parameter with ``DirectoryId`` .

        :type BundleId: string
        :param BundleId:

          The identifier of the bundle. All WorkSpaces that are created from this bundle are retrieved. You
          cannot combine this parameter with any other filter.

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
                'Workspaces': [
                    {
                        'WorkspaceId': 'string',
                        'DirectoryId': 'string',
                        'UserName': 'string',
                        'IpAddress': 'string',
                        'State':
                        'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'
                        |'RESTORING'|'MAINTENANCE'|'ADMIN_MAINTENANCE'|'TERMINATING'|'TERMINATED'
                        |'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
                        'BundleId': 'string',
                        'SubnetId': 'string',
                        'ErrorMessage': 'string',
                        'ErrorCode': 'string',
                        'ComputerName': 'string',
                        'VolumeEncryptionKey': 'string',
                        'UserVolumeEncryptionEnabled': True|False,
                        'RootVolumeEncryptionEnabled': True|False,
                        'WorkspaceProperties': {
                            'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                            'RunningModeAutoStopTimeoutInMinutes': 123,
                            'RootVolumeSizeGib': 123,
                            'UserVolumeSizeGib': 123,
                            'ComputeTypeName':
                            'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                        },
                        'ModificationStates': [
                            {
                                'Resource': 'ROOT_VOLUME'|'USER_VOLUME'|'COMPUTE_TYPE',
                                'State': 'UPDATE_INITIATED'|'UPDATE_IN_PROGRESS'
                            },
                        ]
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Workspaces** *(list) --*

              Information about the WorkSpaces.

              Because  CreateWorkspaces is an asynchronous operation, some of the returned information
              could be incomplete.

              - *(dict) --*

                Describes a WorkSpace.

                - **WorkspaceId** *(string) --*

                  The identifier of the WorkSpace.

                - **DirectoryId** *(string) --*

                  The identifier of the AWS Directory Service directory for the WorkSpace.

                - **UserName** *(string) --*

                  The user for the WorkSpace.

                - **IpAddress** *(string) --*

                  The IP address of the WorkSpace.

                - **State** *(string) --*

                  The operational state of the WorkSpace.

                - **BundleId** *(string) --*

                  The identifier of the bundle used to create the WorkSpace.

                - **SubnetId** *(string) --*

                  The identifier of the subnet for the WorkSpace.

                - **ErrorMessage** *(string) --*

                  The text of the error message that is returned if the WorkSpace cannot be created.

                - **ErrorCode** *(string) --*

                  The error code that is returned if the WorkSpace cannot be created.

                - **ComputerName** *(string) --*

                  The name of the WorkSpace, as seen by the operating system.

                - **VolumeEncryptionKey** *(string) --*

                  The KMS key used to encrypt data stored on your WorkSpace.

                - **UserVolumeEncryptionEnabled** *(boolean) --*

                  Indicates whether the data stored on the user volume is encrypted.

                - **RootVolumeEncryptionEnabled** *(boolean) --*

                  Indicates whether the data stored on the root volume is encrypted.

                - **WorkspaceProperties** *(dict) --*

                  The properties of the WorkSpace.

                  - **RunningMode** *(string) --*

                    The running mode. For more information, see `Manage the WorkSpace Running Mode
                    <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

                  - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

                    The time after a user logs off when WorkSpaces are automatically stopped. Configured in
                    60-minute intervals.

                  - **RootVolumeSizeGib** *(integer) --*

                    The size of the root volume.

                  - **UserVolumeSizeGib** *(integer) --*

                    The size of the user storage.

                  - **ComputeTypeName** *(string) --*

                    The compute type. For more information, see `Amazon WorkSpaces Bundles
                    <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

                - **ModificationStates** *(list) --*

                  The modification states of the WorkSpace.

                  - *(dict) --*

                    Describes a WorkSpace modification.

                    - **Resource** *(string) --*

                      The resource.

                    - **State** *(string) --*

                      The modification state.

        """


class DescribeWorkspacesConnectionStatus(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        WorkspaceIds: List[str] = None,
        PaginationConfig: DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeWorkspacesConnectionStatusPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`WorkSpaces.Client.describe_workspaces_connection_status`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              WorkspaceIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type WorkspaceIds: list
        :param WorkspaceIds:

          The identifiers of the WorkSpaces. You can specify up to 25 WorkSpaces.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than the
            value specified in max-items then a ``NextToken`` will be provided in the output that you can
            use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'WorkspacesConnectionStatus': [
                    {
                        'WorkspaceId': 'string',
                        'ConnectionState': 'CONNECTED'|'DISCONNECTED'|'UNKNOWN',
                        'ConnectionStateCheckTimestamp': datetime(2015, 1, 1),
                        'LastKnownUserConnectionTimestamp': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **WorkspacesConnectionStatus** *(list) --*

              Information about the connection status of the WorkSpace.

              - *(dict) --*

                Describes the connection status of a WorkSpace.

                - **WorkspaceId** *(string) --*

                  The identifier of the WorkSpace.

                - **ConnectionState** *(string) --*

                  The connection state of the WorkSpace. The connection state is unknown if the WorkSpace
                  is stopped.

                - **ConnectionStateCheckTimestamp** *(datetime) --*

                  The timestamp of the connection status check.

                - **LastKnownUserConnectionTimestamp** *(datetime) --*

                  The timestamp of the last known user connection.

        """


class ListAvailableManagementCidrRanges(Boto3Paginator):
    # pylint: disable=arguments-differ
    def paginate(
        self,
        ManagementCidrRangeConstraint: str,
        PaginationConfig: ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef = None,
    ) -> ListAvailableManagementCidrRangesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`WorkSpaces.Client.list_available_management_cidr_ranges`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ListAvailableManagementCidrRanges>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ManagementCidrRangeConstraint='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ManagementCidrRangeConstraint: string
        :param ManagementCidrRangeConstraint: **[REQUIRED]**

          The IP address range to search. Specify an IP address range that is compatible with your network
          and in CIDR notation (that is, specify the range as an IPv4 CIDR block).

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
                'ManagementCidrRanges': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ManagementCidrRanges** *(list) --*

              The list of available IP address ranges, specified as IPv4 CIDR blocks.

              - *(string) --*

        """
