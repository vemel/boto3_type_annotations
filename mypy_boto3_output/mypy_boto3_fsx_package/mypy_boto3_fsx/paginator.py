"Main interface for fsx Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_fsx.type_defs import (
    DescribeBackupsPaginateFiltersTypeDef,
    DescribeBackupsPaginatePaginationConfigTypeDef,
    DescribeBackupsPaginateResponseTypeDef,
    DescribeFileSystemsPaginatePaginationConfigTypeDef,
    DescribeFileSystemsPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
)


__all__ = (
    "DescribeBackupsPaginator",
    "DescribeFileSystemsPaginator",
    "ListTagsForResourcePaginator",
)


class DescribeBackupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_backups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BackupIds: List[str] = None,
        Filters: List[DescribeBackupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeBackupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeBackupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`FSx.Client.describe_backups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/DescribeBackups>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              BackupIds=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'file-system-id'|'backup-type',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type BackupIds: list
        :param BackupIds:

          (Optional) IDs of the backups you want to retrieve (String). This overrides any filters. If any
          IDs are not found, BackupNotFound will be thrown.

          - *(string) --*

            The ID of the backup. Specifies the backup to use if you're creating a file system from an
            existing backup.

        :type Filters: list
        :param Filters:

          (Optional) Filters structure. Supported names are file-system-id and backup-type.

          - *(dict) --*

            A filter used to restrict the results of describe calls. You can use multiple filters to return
            results that meet all applied filter requirements.

            - **Name** *(string) --*

              The name for this filter.

            - **Values** *(list) --*

              The values of the filter. These are all the values for any of the applied filters.

              - *(string) --*

                The value for a filter.

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
                'Backups': [
                    {
                        'BackupId': 'string',
                        'Lifecycle': 'AVAILABLE'|'CREATING'|'DELETED'|'FAILED',
                        'FailureDetails': {
                            'Message': 'string'
                        },
                        'Type': 'AUTOMATIC'|'USER_INITIATED',
                        'ProgressPercent': 123,
                        'CreationTime': datetime(2015, 1, 1),
                        'KmsKeyId': 'string',
                        'ResourceARN': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'FileSystem': {
                            'OwnerId': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'FileSystemId': 'string',
                            'FileSystemType': 'WINDOWS'|'LUSTRE',
                            'Lifecycle':
                            'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
                            'FailureDetails': {
                                'Message': 'string'
                            },
                            'StorageCapacity': 123,
                            'VpcId': 'string',
                            'SubnetIds': [
                                'string',
                            ],
                            'NetworkInterfaceIds': [
                                'string',
                            ],
                            'DNSName': 'string',
                            'KmsKeyId': 'string',
                            'ResourceARN': 'string',
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'WindowsConfiguration': {
                                'ActiveDirectoryId': 'string',
                                'SelfManagedActiveDirectoryConfiguration': {
                                    'DomainName': 'string',
                                    'OrganizationalUnitDistinguishedName': 'string',
                                    'FileSystemAdministratorsGroup': 'string',
                                    'UserName': 'string',
                                    'DnsIps': [
                                        'string',
                                    ]
                                },
                                'ThroughputCapacity': 123,
                                'MaintenanceOperationsInProgress': [
                                    'PATCHING'|'BACKING_UP',
                                ],
                                'WeeklyMaintenanceStartTime': 'string',
                                'DailyAutomaticBackupStartTime': 'string',
                                'AutomaticBackupRetentionDays': 123,
                                'CopyTagsToBackups': True|False
                            },
                            'LustreConfiguration': {
                                'WeeklyMaintenanceStartTime': 'string',
                                'DataRepositoryConfiguration': {
                                    'ImportPath': 'string',
                                    'ExportPath': 'string',
                                    'ImportedFileChunkSize': 123
                                }
                            }
                        },
                        'DirectoryInformation': {
                            'DomainName': 'string',
                            'ActiveDirectoryId': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Response object for ``DescribeBackups`` operation.

            - **Backups** *(list) --*

              Any array of backups.

              - *(dict) --*

                A backup of an Amazon FSx for Windows File Server file system. You can create a new file
                system from a backup to protect against data loss.

                - **BackupId** *(string) --*

                  The ID of the backup.

                - **Lifecycle** *(string) --*

                  The lifecycle status of the backup.

                - **FailureDetails** *(dict) --*

                  Details explaining any failures that occur when creating a backup.

                  - **Message** *(string) --*

                    A message describing the backup creation failure.

                - **Type** *(string) --*

                  The type of the backup.

                - **ProgressPercent** *(integer) --*

                  The current percent of progress of an asynchronous task.

                - **CreationTime** *(datetime) --*

                  The time when a particular backup was created.

                - **KmsKeyId** *(string) --*

                  The ID of the AWS Key Management Service (AWS KMS) key used to encrypt this backup's data.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) for the backup resource.

                - **Tags** *(list) --*

                  Tags associated with a particular file system.

                  - *(dict) --*

                    Specifies a key-value pair for a resource tag.

                    - **Key** *(string) --*

                      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
                      for the resource to which they are attached.

                    - **Value** *(string) --*

                      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
                      key. Tag values can be null and don't have to be unique in a tag set. For example,
                      you can have a key-value pair in a tag set of ``finances : April`` and also of
                      ``payroll : April`` .

                - **FileSystem** *(dict) --*

                  Metadata of the file system associated with the backup. This metadata is persisted even
                  if the file system is deleted.

                  - **OwnerId** *(string) --*

                    The AWS account that created the file system. If the file system was created by an AWS
                    Identity and Access Management (IAM) user, the AWS account to which the IAM user
                    belongs is the owner.

                  - **CreationTime** *(datetime) --*

                    The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z),
                    also known as Unix time.

                  - **FileSystemId** *(string) --*

                    The system-generated, unique 17-digit ID of the file system.

                  - **FileSystemType** *(string) --*

                    The type of Amazon FSx file system, either ``LUSTRE`` or ``WINDOWS`` .

                  - **Lifecycle** *(string) --*

                    The lifecycle status of the file system:

                    * ``AVAILABLE`` indicates that the file system is reachable and available for use.

                    * ``CREATING`` indicates that Amazon FSx is in the process of creating the new file
                    system.

                    * ``DELETING`` indicates that Amazon FSx is in the process of deleting the file system.

                    * ``FAILED`` indicates that Amazon FSx was not able to create the file system.

                    * ``MISCONFIGURED`` indicates that the file system is in a failed but recoverable state.

                    * ``UPDATING`` indicates that the file system is undergoing a customer initiated update.

                  - **FailureDetails** *(dict) --*

                    A structure providing details of any failures that occur when creating the file system
                    has failed.

                    - **Message** *(string) --*

                      A message describing any failures that occurred during file system creation.

                  - **StorageCapacity** *(integer) --*

                    The storage capacity of the file system in gigabytes (GB).

                  - **VpcId** *(string) --*

                    The ID of the primary VPC for the file system.

                  - **SubnetIds** *(list) --*

                    The ID of the subnet to contain the endpoint for the file system. One and only one is
                    supported. The file system is launched in the Availability Zone associated with this
                    subnet.

                    - *(string) --*

                      The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private
                      cloud (VPC). For more information, see `VPC and Subnets
                      <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html>`__ in the
                      *Amazon VPC User Guide.*

                  - **NetworkInterfaceIds** *(list) --*

                    The IDs of the elastic network interface from which a specific file system is
                    accessible. The elastic network interface is automatically created in the same VPC that
                    the Amazon FSx file system was created in. For more information, see `Elastic Network
                    Interfaces <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html>`__ in
                    the *Amazon EC2 User Guide.*

                    For an Amazon FSx for Windows File Server file system, you can have one network
                    interface ID. For an Amazon FSx for Lustre file system, you can have more than one.

                    - *(string) --*

                      An elastic network interface ID. An elastic network interface is a logical networking
                      component in a virtual private cloud (VPC) that represents a virtual network card.
                      For more information, see `Elastic Network Interfaces
                      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html>`__ in the
                      *Amazon EC2 User Guide for Linux Instances* .

                  - **DNSName** *(string) --*

                    The DNS name for the file system.

                  - **KmsKeyId** *(string) --*

                    The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the file
                    system's data for an Amazon FSx for Windows File Server file system.

                  - **ResourceARN** *(string) --*

                    The Amazon Resource Name (ARN) for the file system resource.

                  - **Tags** *(list) --*

                    The tags to associate with the file system. For more information, see `Tagging Your
                    Amazon EC2 Resources
                    <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon
                    EC2 User Guide* .

                    - *(dict) --*

                      Specifies a key-value pair for a resource tag.

                      - **Key** *(string) --*

                        A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be
                        unique for the resource to which they are attached.

                      - **Value** *(string) --*

                        A value that specifies the ``TagValue`` , the value assigned to the corresponding
                        tag key. Tag values can be null and don't have to be unique in a tag set. For
                        example, you can have a key-value pair in a tag set of ``finances : April`` and
                        also of ``payroll : April`` .

                  - **WindowsConfiguration** *(dict) --*

                    The configuration for this Microsoft Windows file system.

                    - **ActiveDirectoryId** *(string) --*

                      The ID for an existing Microsoft Active Directory instance that the file system
                      should join when it's created.

                    - **SelfManagedActiveDirectoryConfiguration** *(dict) --*

                      The configuration of the self-managed Microsoft Active Directory (AD) directory to
                      which the Windows File Server instance is joined.

                      - **DomainName** *(string) --*

                        The fully qualified domain name of the self-managed AD directory.

                      - **OrganizationalUnitDistinguishedName** *(string) --*

                        The fully qualified distinguished name of the organizational unit within the
                        self-managed AD directory to which the Windows File Server instance is joined.

                      - **FileSystemAdministratorsGroup** *(string) --*

                        The name of the domain group whose members have administrative privileges for the
                        FSx file system.

                      - **UserName** *(string) --*

                        The user name for the service account on your self-managed AD domain that FSx uses
                        to join to your AD domain.

                      - **DnsIps** *(list) --*

                        A list of up to two IP addresses of DNS servers or domain controllers in the
                        self-managed AD directory.

                        - *(string) --*

                    - **ThroughputCapacity** *(integer) --*

                      The throughput of an Amazon FSx file system, measured in megabytes per second.

                    - **MaintenanceOperationsInProgress** *(list) --*

                      The list of maintenance operations in progress for this file system.

                      - *(string) --*

                        An enumeration specifying the currently ongoing maintenance operation.

                    - **WeeklyMaintenanceStartTime** *(string) --*

                      The preferred time to perform weekly maintenance, in the UTC time zone.

                    - **DailyAutomaticBackupStartTime** *(string) --*

                      The preferred time to take daily automatic backups, in the UTC time zone.

                    - **AutomaticBackupRetentionDays** *(integer) --*

                      The number of days to retain automatic backups. Setting this to 0 disables automatic
                      backups. You can retain automatic backups for a maximum of 35 days.

                    - **CopyTagsToBackups** *(boolean) --*

                      A boolean flag indicating whether tags on the file system should be copied to
                      backups. This value defaults to false. If it's set to true, all tags on the file
                      system are copied to all automatic backups and any user-initiated backups where the
                      user doesn't specify any tags. If this value is true, and you specify one or more
                      tags, only the specified tags are copied to backups.

                  - **LustreConfiguration** *(dict) --*

                    The configuration for the Amazon FSx for Lustre file system.

                    - **WeeklyMaintenanceStartTime** *(string) --*

                      The UTC time that you want to begin your weekly maintenance window.

                    - **DataRepositoryConfiguration** *(dict) --*

                      The data repository configuration object for Lustre file systems returned in the
                      response of the ``CreateFileSystem`` operation.

                      - **ImportPath** *(string) --*

                        The import path to the Amazon S3 bucket (and optional prefix) that you're using as
                        the data repository for your FSx for Lustre file system, for example
                        ``s3://import-bucket/optional-prefix`` . If a prefix is specified after the Amazon
                        S3 bucket name, only object keys with that prefix are loaded into the file system.

                      - **ExportPath** *(string) --*

                        The export path to the Amazon S3 bucket (and prefix) that you are using to store
                        new and changed Lustre file system files in S3.

                      - **ImportedFileChunkSize** *(integer) --*

                        For files imported from a data repository, this value determines the stripe count
                        and maximum amount of data per file (in MiB) stored on a single physical disk. The
                        maximum number of disks that a single file can be striped across is limited by the
                        total number of disks that make up the file system.

                        The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500
                        GiB). Amazon S3 objects have a maximum size of 5 TB.

                - **DirectoryInformation** *(dict) --*

                  The configuration of the self-managed Microsoft Active Directory (AD) to which the
                  Windows File Server instance is joined.

                  - **DomainName** *(string) --*

                    The fully qualified domain name of the self-managed AD directory.

                  - **ActiveDirectoryId** *(string) --*

                    The ID of the AWS Managed Microsoft Active Directory instance to which the file system
                    is joined.

        """


class DescribeFileSystemsPaginator(Boto3Paginator):
    """
    Paginator for `describe_file_systems`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FileSystemIds: List[str] = None,
        PaginationConfig: DescribeFileSystemsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeFileSystemsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`FSx.Client.describe_file_systems`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/DescribeFileSystems>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              FileSystemIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type FileSystemIds: list
        :param FileSystemIds:

          (Optional) IDs of the file systems whose descriptions you want to retrieve (String).

          - *(string) --*

            The globally unique ID of the file system, assigned by Amazon FSx.

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
                'FileSystems': [
                    {
                        'OwnerId': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'FileSystemId': 'string',
                        'FileSystemType': 'WINDOWS'|'LUSTRE',
                        'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
                        'FailureDetails': {
                            'Message': 'string'
                        },
                        'StorageCapacity': 123,
                        'VpcId': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'NetworkInterfaceIds': [
                            'string',
                        ],
                        'DNSName': 'string',
                        'KmsKeyId': 'string',
                        'ResourceARN': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'WindowsConfiguration': {
                            'ActiveDirectoryId': 'string',
                            'SelfManagedActiveDirectoryConfiguration': {
                                'DomainName': 'string',
                                'OrganizationalUnitDistinguishedName': 'string',
                                'FileSystemAdministratorsGroup': 'string',
                                'UserName': 'string',
                                'DnsIps': [
                                    'string',
                                ]
                            },
                            'ThroughputCapacity': 123,
                            'MaintenanceOperationsInProgress': [
                                'PATCHING'|'BACKING_UP',
                            ],
                            'WeeklyMaintenanceStartTime': 'string',
                            'DailyAutomaticBackupStartTime': 'string',
                            'AutomaticBackupRetentionDays': 123,
                            'CopyTagsToBackups': True|False
                        },
                        'LustreConfiguration': {
                            'WeeklyMaintenanceStartTime': 'string',
                            'DataRepositoryConfiguration': {
                                'ImportPath': 'string',
                                'ExportPath': 'string',
                                'ImportedFileChunkSize': 123
                            }
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            The response object for ``DescribeFileSystems`` operation.

            - **FileSystems** *(list) --*

              An array of file system descriptions.

              - *(dict) --*

                A description of a specific Amazon FSx file system.

                - **OwnerId** *(string) --*

                  The AWS account that created the file system. If the file system was created by an AWS
                  Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs
                  is the owner.

                - **CreationTime** *(datetime) --*

                  The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also
                  known as Unix time.

                - **FileSystemId** *(string) --*

                  The system-generated, unique 17-digit ID of the file system.

                - **FileSystemType** *(string) --*

                  The type of Amazon FSx file system, either ``LUSTRE`` or ``WINDOWS`` .

                - **Lifecycle** *(string) --*

                  The lifecycle status of the file system:

                  * ``AVAILABLE`` indicates that the file system is reachable and available for use.

                  * ``CREATING`` indicates that Amazon FSx is in the process of creating the new file
                  system.

                  * ``DELETING`` indicates that Amazon FSx is in the process of deleting the file system.

                  * ``FAILED`` indicates that Amazon FSx was not able to create the file system.

                  * ``MISCONFIGURED`` indicates that the file system is in a failed but recoverable state.

                  * ``UPDATING`` indicates that the file system is undergoing a customer initiated update.

                - **FailureDetails** *(dict) --*

                  A structure providing details of any failures that occur when creating the file system
                  has failed.

                  - **Message** *(string) --*

                    A message describing any failures that occurred during file system creation.

                - **StorageCapacity** *(integer) --*

                  The storage capacity of the file system in gigabytes (GB).

                - **VpcId** *(string) --*

                  The ID of the primary VPC for the file system.

                - **SubnetIds** *(list) --*

                  The ID of the subnet to contain the endpoint for the file system. One and only one is
                  supported. The file system is launched in the Availability Zone associated with this
                  subnet.

                  - *(string) --*

                    The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private
                    cloud (VPC). For more information, see `VPC and Subnets
                    <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html>`__ in the
                    *Amazon VPC User Guide.*

                - **NetworkInterfaceIds** *(list) --*

                  The IDs of the elastic network interface from which a specific file system is accessible.
                  The elastic network interface is automatically created in the same VPC that the Amazon
                  FSx file system was created in. For more information, see `Elastic Network Interfaces
                  <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html>`__ in the *Amazon
                  EC2 User Guide.*

                  For an Amazon FSx for Windows File Server file system, you can have one network interface
                  ID. For an Amazon FSx for Lustre file system, you can have more than one.

                  - *(string) --*

                    An elastic network interface ID. An elastic network interface is a logical networking
                    component in a virtual private cloud (VPC) that represents a virtual network card. For
                    more information, see `Elastic Network Interfaces
                    <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html>`__ in the *Amazon
                    EC2 User Guide for Linux Instances* .

                - **DNSName** *(string) --*

                  The DNS name for the file system.

                - **KmsKeyId** *(string) --*

                  The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the file system's
                  data for an Amazon FSx for Windows File Server file system.

                - **ResourceARN** *(string) --*

                  The Amazon Resource Name (ARN) for the file system resource.

                - **Tags** *(list) --*

                  The tags to associate with the file system. For more information, see `Tagging Your
                  Amazon EC2 Resources
                  <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in the *Amazon
                  EC2 User Guide* .

                  - *(dict) --*

                    Specifies a key-value pair for a resource tag.

                    - **Key** *(string) --*

                      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
                      for the resource to which they are attached.

                    - **Value** *(string) --*

                      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
                      key. Tag values can be null and don't have to be unique in a tag set. For example,
                      you can have a key-value pair in a tag set of ``finances : April`` and also of
                      ``payroll : April`` .

                - **WindowsConfiguration** *(dict) --*

                  The configuration for this Microsoft Windows file system.

                  - **ActiveDirectoryId** *(string) --*

                    The ID for an existing Microsoft Active Directory instance that the file system should
                    join when it's created.

                  - **SelfManagedActiveDirectoryConfiguration** *(dict) --*

                    The configuration of the self-managed Microsoft Active Directory (AD) directory to
                    which the Windows File Server instance is joined.

                    - **DomainName** *(string) --*

                      The fully qualified domain name of the self-managed AD directory.

                    - **OrganizationalUnitDistinguishedName** *(string) --*

                      The fully qualified distinguished name of the organizational unit within the
                      self-managed AD directory to which the Windows File Server instance is joined.

                    - **FileSystemAdministratorsGroup** *(string) --*

                      The name of the domain group whose members have administrative privileges for the FSx
                      file system.

                    - **UserName** *(string) --*

                      The user name for the service account on your self-managed AD domain that FSx uses to
                      join to your AD domain.

                    - **DnsIps** *(list) --*

                      A list of up to two IP addresses of DNS servers or domain controllers in the
                      self-managed AD directory.

                      - *(string) --*

                  - **ThroughputCapacity** *(integer) --*

                    The throughput of an Amazon FSx file system, measured in megabytes per second.

                  - **MaintenanceOperationsInProgress** *(list) --*

                    The list of maintenance operations in progress for this file system.

                    - *(string) --*

                      An enumeration specifying the currently ongoing maintenance operation.

                  - **WeeklyMaintenanceStartTime** *(string) --*

                    The preferred time to perform weekly maintenance, in the UTC time zone.

                  - **DailyAutomaticBackupStartTime** *(string) --*

                    The preferred time to take daily automatic backups, in the UTC time zone.

                  - **AutomaticBackupRetentionDays** *(integer) --*

                    The number of days to retain automatic backups. Setting this to 0 disables automatic
                    backups. You can retain automatic backups for a maximum of 35 days.

                  - **CopyTagsToBackups** *(boolean) --*

                    A boolean flag indicating whether tags on the file system should be copied to backups.
                    This value defaults to false. If it's set to true, all tags on the file system are
                    copied to all automatic backups and any user-initiated backups where the user doesn't
                    specify any tags. If this value is true, and you specify one or more tags, only the
                    specified tags are copied to backups.

                - **LustreConfiguration** *(dict) --*

                  The configuration for the Amazon FSx for Lustre file system.

                  - **WeeklyMaintenanceStartTime** *(string) --*

                    The UTC time that you want to begin your weekly maintenance window.

                  - **DataRepositoryConfiguration** *(dict) --*

                    The data repository configuration object for Lustre file systems returned in the
                    response of the ``CreateFileSystem`` operation.

                    - **ImportPath** *(string) --*

                      The import path to the Amazon S3 bucket (and optional prefix) that you're using as
                      the data repository for your FSx for Lustre file system, for example
                      ``s3://import-bucket/optional-prefix`` . If a prefix is specified after the Amazon S3
                      bucket name, only object keys with that prefix are loaded into the file system.

                    - **ExportPath** *(string) --*

                      The export path to the Amazon S3 bucket (and prefix) that you are using to store new
                      and changed Lustre file system files in S3.

                    - **ImportedFileChunkSize** *(integer) --*

                      For files imported from a data repository, this value determines the stripe count and
                      maximum amount of data per file (in MiB) stored on a single physical disk. The
                      maximum number of disks that a single file can be striped across is limited by the
                      total number of disks that make up the file system.

                      The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500
                      GiB). Amazon S3 objects have a maximum size of 5 TB.

        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceARN: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`FSx.Client.list_tags_for_resource`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/ListTagsForResource>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ResourceARN='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The ARN of the Amazon FSx resource that will have its tags listed.

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
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            The response object for ``ListTagsForResource`` operation.

            - **Tags** *(list) --*

              A list of tags on the resource.

              - *(dict) --*

                Specifies a key-value pair for a resource tag.

                - **Key** *(string) --*

                  A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for
                  the resource to which they are attached.

                - **Value** *(string) --*

                  A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
                  key. Tag values can be null and don't have to be unique in a tag set. For example, you
                  can have a key-value pair in a tag set of ``finances : April`` and also of ``payroll :
                  April`` .

        """
