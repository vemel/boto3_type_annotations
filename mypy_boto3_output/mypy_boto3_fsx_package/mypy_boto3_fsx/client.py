"Main interface for fsx Client"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_fsx.client as client_scope

# pylint: disable=import-self
import mypy_boto3_fsx.paginator as paginator_scope
from mypy_boto3_fsx.type_defs import (
    ClientCreateBackupResponseTypeDef,
    ClientCreateBackupTagsTypeDef,
    ClientCreateFileSystemFromBackupResponseTypeDef,
    ClientCreateFileSystemFromBackupTagsTypeDef,
    ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef,
    ClientCreateFileSystemLustreConfigurationTypeDef,
    ClientCreateFileSystemResponseTypeDef,
    ClientCreateFileSystemTagsTypeDef,
    ClientCreateFileSystemWindowsConfigurationTypeDef,
    ClientDeleteBackupResponseTypeDef,
    ClientDeleteFileSystemResponseTypeDef,
    ClientDeleteFileSystemWindowsConfigurationTypeDef,
    ClientDescribeBackupsFiltersTypeDef,
    ClientDescribeBackupsResponseTypeDef,
    ClientDescribeFileSystemsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateFileSystemLustreConfigurationTypeDef,
    ClientUpdateFileSystemResponseTypeDef,
    ClientUpdateFileSystemWindowsConfigurationTypeDef,
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
    def create_backup(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        Tags: List[ClientCreateBackupTagsTypeDef] = None,
    ) -> ClientCreateBackupResponseTypeDef:
        """
        Creates a backup of an existing Amazon FSx for Windows File Server file system. Creating regular
        backups for your file system is a best practice that complements the replication that Amazon FSx
        for Windows File Server performs for your file system. It also enables you to restore from user
        modification of data.

        If a backup with the specified client request token exists, and the parameters match, this
        operation returns the description of the existing backup. If a backup specified client request
        token exists, and the parameters don't match, this operation returns ``IncompatibleParameterError``
        . If a backup with the specified client request token doesn't exist, ``CreateBackup`` does the
        following:

        * Creates a new Amazon FSx backup with an assigned ID, and an initial lifecycle state of
        ``CREATING`` .

        * Returns the description of the backup.

        By using the idempotent operation, you can retry a ``CreateBackup`` operation without the risk of
        creating an extra backup. This approach can be useful when an initial call fails in a way that
        makes it unclear whether a backup was created. If you use the same client request token and the
        initial call created a backup, the operation returns a successful result because all the parameters
        are the same.

        The ``CreateFileSystem`` operation returns while the backup's lifecycle state is still ``CREATING``
        . You can check the file system creation status by calling the  DescribeBackups operation, which
        returns the backup state along with other information.

        .. note::

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/CreateBackup>`_

        **Request Syntax**
        ::

          response = client.create_backup(
              FileSystemId='string',
              ClientRequestToken='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type FileSystemId: string
        :param FileSystemId: **[REQUIRED]**

          The ID of the file system to back up.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent
          creation. This string is automatically filled on your behalf when you use the AWS Command Line
          Interface (AWS CLI) or an AWS SDK.

          This field is autopopulated if not provided.

        :type Tags: list
        :param Tags:

          The tags to apply to the backup at backup creation. The key value of the ``Name`` tag appears in
          the console as the backup name.

          - *(dict) --*

            Specifies a key-value pair for a resource tag.

            - **Key** *(string) --*

              A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
              resource to which they are attached.

            - **Value** *(string) --*

              A value that specifies the ``TagValue`` , the value assigned to the corresponding tag key.
              Tag values can be null and don't have to be unique in a tag set. For example, you can have a
              key-value pair in a tag set of ``finances : April`` and also of ``payroll : April`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Backup': {
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
                    'DirectoryInformation': {
                        'DomainName': 'string',
                        'ActiveDirectoryId': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            The response object for the ``CreateBackup`` operation.

            - **Backup** *(dict) --*

              A description of the backup.

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
                    key. Tag values can be null and don't have to be unique in a tag set. For example, you
                    can have a key-value pair in a tag set of ``finances : April`` and also of ``payroll :
                    April`` .

              - **FileSystem** *(dict) --*

                Metadata of the file system associated with the backup. This metadata is persisted even if
                the file system is deleted.

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

              - **DirectoryInformation** *(dict) --*

                The configuration of the self-managed Microsoft Active Directory (AD) to which the Windows
                File Server instance is joined.

                - **DomainName** *(string) --*

                  The fully qualified domain name of the self-managed AD directory.

                - **ActiveDirectoryId** *(string) --*

                  The ID of the AWS Managed Microsoft Active Directory instance to which the file system is
                  joined.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_file_system(
        self,
        FileSystemType: str,
        StorageCapacity: int,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[str] = None,
        Tags: List[ClientCreateFileSystemTagsTypeDef] = None,
        KmsKeyId: str = None,
        WindowsConfiguration: ClientCreateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: ClientCreateFileSystemLustreConfigurationTypeDef = None,
    ) -> ClientCreateFileSystemResponseTypeDef:
        """
        Creates a new, empty Amazon FSx file system.

        If a file system with the specified client request token exists and the parameters match,
        ``CreateFileSystem`` returns the description of the existing file system. If a file system
        specified client request token exists and the parameters don't match, this call returns
        ``IncompatibleParameterError`` . If a file system with the specified client request token doesn't
        exist, ``CreateFileSystem`` does the following:

        * Creates a new, empty Amazon FSx file system with an assigned ID, and an initial lifecycle state
        of ``CREATING`` .

        * Returns the description of the file system.

        This operation requires a client request token in the request that Amazon FSx uses to ensure
        idempotent creation. This means that calling the operation multiple times with the same client
        request token has no effect. By using the idempotent operation, you can retry a
        ``CreateFileSystem`` operation without the risk of creating an extra file system. This approach can
        be useful when an initial call fails in a way that makes it unclear whether a file system was
        created. Examples are if a transport level timeout occurred, or your connection was reset. If you
        use the same client request token and the initial call created a file system, the client receives
        success as long as the parameters are the same.

        .. note::

          The ``CreateFileSystem`` call returns while the file system's lifecycle state is still
          ``CREATING`` . You can check the file-system creation status by calling the  DescribeFileSystems
          operation, which returns the file system state along with other information.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/CreateFileSystem>`_

        **Request Syntax**
        ::

          response = client.create_file_system(
              ClientRequestToken='string',
              FileSystemType='WINDOWS'|'LUSTRE',
              StorageCapacity=123,
              SubnetIds=[
                  'string',
              ],
              SecurityGroupIds=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              KmsKeyId='string',
              WindowsConfiguration={
                  'ActiveDirectoryId': 'string',
                  'SelfManagedActiveDirectoryConfiguration': {
                      'DomainName': 'string',
                      'OrganizationalUnitDistinguishedName': 'string',
                      'FileSystemAdministratorsGroup': 'string',
                      'UserName': 'string',
                      'Password': 'string',
                      'DnsIps': [
                          'string',
                      ]
                  },
                  'ThroughputCapacity': 123,
                  'WeeklyMaintenanceStartTime': 'string',
                  'DailyAutomaticBackupStartTime': 'string',
                  'AutomaticBackupRetentionDays': 123,
                  'CopyTagsToBackups': True|False
              },
              LustreConfiguration={
                  'WeeklyMaintenanceStartTime': 'string',
                  'ImportPath': 'string',
                  'ExportPath': 'string',
                  'ImportedFileChunkSize': 123
              }
          )
        :type ClientRequestToken: string
        :param ClientRequestToken:

          (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent
          creation. This string is automatically filled on your behalf when you use the AWS Command Line
          Interface (AWS CLI) or an AWS SDK.

          This field is autopopulated if not provided.

        :type FileSystemType: string
        :param FileSystemType: **[REQUIRED]**

          The type of Amazon FSx file system to create.

        :type StorageCapacity: integer
        :param StorageCapacity: **[REQUIRED]**

          The storage capacity of the file system being created.

          For Windows file systems, the storage capacity has a minimum of 300 GiB, and a maximum of 65,536
          GiB.

          For Lustre file systems, the storage capacity has a minimum of 3,600 GiB. Storage capacity is
          provisioned in increments of 3,600 GiB.

        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]**

          The IDs of the subnets that the file system will be accessible from. File systems support only
          one subnet. The file server is also launched in that subnet's Availability Zone.

          - *(string) --*

            The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC).
            For more information, see `VPC and Subnets
            <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html>`__ in the *Amazon VPC
            User Guide.*

        :type SecurityGroupIds: list
        :param SecurityGroupIds:

          A list of IDs specifying the security groups to apply to all network interfaces created for file
          system access. This list isn't returned in later requests to describe the file system.

          - *(string) --*

            The ID of your Amazon EC2 security group. This ID is used to control network access to the
            endpoint that Amazon FSx creates on your behalf in each subnet. For more information, see
            `Amazon EC2 Security Groups for Linux Instances
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`__ in the
            *Amazon EC2 User Guide* .

        :type Tags: list
        :param Tags:

          The tags to apply to the file system being created. The key value of the ``Name`` tag appears in
          the console as the file system name.

          - *(dict) --*

            Specifies a key-value pair for a resource tag.

            - **Key** *(string) --*

              A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
              resource to which they are attached.

            - **Value** *(string) --*

              A value that specifies the ``TagValue`` , the value assigned to the corresponding tag key.
              Tag values can be null and don't have to be unique in a tag set. For example, you can have a
              key-value pair in a tag set of ``finances : April`` and also of ``payroll : April`` .

        :type KmsKeyId: string
        :param KmsKeyId:

          The ID of your AWS Key Management Service (AWS KMS) key. This ID is used to encrypt the data in
          your file system at rest. For more information, see `Encrypt
          <https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html>`__ in the *AWS Key
          Management Service API Reference* .

        :type WindowsConfiguration: dict
        :param WindowsConfiguration:

          The Microsoft Windows configuration for the file system being created. This value is required if
          ``FileSystemType`` is set to ``WINDOWS`` .

          - **ActiveDirectoryId** *(string) --*

            The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file
            system should join when it's created.

          - **SelfManagedActiveDirectoryConfiguration** *(dict) --*

            The configuration that Amazon FSx uses to join the Windows File Server instance to your
            self-managed (including on-premises) Microsoft Active Directory (AD) directory.

            - **DomainName** *(string) --* **[REQUIRED]**

              The fully qualified domain name of the self-managed AD directory, such as
              ``corp.example.com`` .

            - **OrganizationalUnitDistinguishedName** *(string) --*

              (Optional) The fully qualified distinguished name of the organizational unit within your
              self-managed AD directory that the Windows File Server instance will join. Amazon FSx only
              accepts OU as the direct parent of the file system. An example is
              ``OU=FSx,DC=yourdomain,DC=corp,DC=com`` . To learn more, see `RFC 2253
              <https://tools.ietf.org/html/rfc2253>`__ . If none is provided, the FSx file system is
              created in the default location of your self-managed AD directory.

              .. warning::

                Only Organizational Unit (OU) objects can be the direct parent of the file system that
                you're creating.

            - **FileSystemAdministratorsGroup** *(string) --*

              (Optional) The name of the domain group whose members are granted administrative privileges
              for the file system. Administrative privileges include taking ownership of files and folders,
              and setting audit controls (audit ACLs) on files and folders. The group that you specify must
              already exist in your domain. If you don't provide one, your AD domain's Domain Admins group
              is used.

            - **UserName** *(string) --* **[REQUIRED]**

              The user name for the service account on your self-managed AD domain that Amazon FSx will use
              to join to your AD domain. This account must have the permission to join computers to the
              domain in the organizational unit provided in ``OrganizationalUnitDistinguishedName`` , or in
              the default location of your AD domain.

            - **Password** *(string) --* **[REQUIRED]**

              The password for the service account on your self-managed AD domain that Amazon FSx will use
              to join to your AD domain.

            - **DnsIps** *(list) --* **[REQUIRED]**

              A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD
              directory. The IP addresses need to be either in the same VPC CIDR range as the one in which
              your Amazon FSx file system is being created, or in the private IP version 4 (Iv4) address
              ranges, as specified in `RFC 1918 <http://www.faqs.org/rfcs/rfc1918.html>`__ :

              * 10.0.0.0 - 10.255.255.255 (10/8 prefix)

              * 172.16.0.0 - 172.31.255.255 (172.16/12 prefix)

              * 192.168.0.0 - 192.168.255.255 (192.168/16 prefix)

              - *(string) --*

          - **ThroughputCapacity** *(integer) --* **[REQUIRED]**

            The throughput of an Amazon FSx file system, measured in megabytes per second, in 2 to the *n*
            th increments, between 2^3 (8) and 2^11 (2048).

          - **WeeklyMaintenanceStartTime** *(string) --*

            The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone.

          - **DailyAutomaticBackupStartTime** *(string) --*

            The preferred time to take daily automatic backups, formatted HH:MM in the UTC time zone.

          - **AutomaticBackupRetentionDays** *(integer) --*

            The number of days to retain automatic backups. The default is to retain backups for 7 days.
            Setting this value to 0 disables the creation of automatic backups. The maximum retention
            period for backups is 35 days.

          - **CopyTagsToBackups** *(boolean) --*

            A boolean flag indicating whether tags for the file system should be copied to backups. This
            value defaults to false. If it's set to true, all tags for the file system are copied to all
            automatic and user-initiated backups where the user doesn't specify tags. If this value is
            true, and you specify one or more tags, only the specified tags are copied to backups.

        :type LustreConfiguration: dict
        :param LustreConfiguration:

          The Lustre configuration for the file system being created. This value is required if
          ``FileSystemType`` is set to ``LUSTRE`` .

          - **WeeklyMaintenanceStartTime** *(string) --*

            The preferred time to perform weekly maintenance, in the UTC time zone.

          - **ImportPath** *(string) --*

            (Optional) The path to the Amazon S3 bucket (including the optional prefix) that you're using
            as the data repository for your Amazon FSx for Lustre file system. The root of your FSx for
            Lustre file system will be mapped to the root of the Amazon S3 bucket you select. An example is
            ``s3://import-bucket/optional-prefix`` . If you specify a prefix after the Amazon S3 bucket
            name, only object keys with that prefix are loaded into the file system.

          - **ExportPath** *(string) --*

            (Optional) The path in Amazon S3 where the root of your Amazon FSx file system is exported. The
            path must use the same Amazon S3 bucket as specified in ImportPath. You can provide an optional
            prefix to which new and changed data is to be exported from your Amazon FSx for Lustre file
            system. If an ``ExportPath`` value is not provided, Amazon FSx sets a default export path,
            ``s3://import-bucket/FSxLustre[creation-timestamp]`` . The timestamp is in UTC format, for
            example ``s3://import-bucket/FSxLustre20181105T222312Z`` .

            The Amazon S3 export bucket must be the same as the import bucket specified by ``ImportPath`` .
            If you only specify a bucket name, such as ``s3://import-bucket`` , you get a 1:1 mapping of
            file system objects to S3 bucket objects. This mapping means that the input data in S3 is
            overwritten on export. If you provide a custom prefix in the export path, such as
            ``s3://import-bucket/[custom-optional-prefix]`` , Amazon FSx exports the contents of your file
            system to that export prefix in the Amazon S3 bucket.

          - **ImportedFileChunkSize** *(integer) --*

            (Optional) For files imported from a data repository, this value determines the stripe count
            and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum
            number of disks that a single file can be striped across is limited by the total number of
            disks that make up the file system.

            The chunk size default is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon
            S3 objects have a maximum size of 5 TB.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileSystem': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            The response object returned after the file system is created.

            - **FileSystem** *(dict) --*

              The configuration of the file system that was created.

              - **OwnerId** *(string) --*

                The AWS account that created the file system. If the file system was created by an AWS
                Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is
                the owner.

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

                * ``CREATING`` indicates that Amazon FSx is in the process of creating the new file system.

                * ``DELETING`` indicates that Amazon FSx is in the process of deleting the file system.

                * ``FAILED`` indicates that Amazon FSx was not able to create the file system.

                * ``MISCONFIGURED`` indicates that the file system is in a failed but recoverable state.

                * ``UPDATING`` indicates that the file system is undergoing a customer initiated update.

              - **FailureDetails** *(dict) --*

                A structure providing details of any failures that occur when creating the file system has
                failed.

                - **Message** *(string) --*

                  A message describing any failures that occurred during file system creation.

              - **StorageCapacity** *(integer) --*

                The storage capacity of the file system in gigabytes (GB).

              - **VpcId** *(string) --*

                The ID of the primary VPC for the file system.

              - **SubnetIds** *(list) --*

                The ID of the subnet to contain the endpoint for the file system. One and only one is
                supported. The file system is launched in the Availability Zone associated with this subnet.

                - *(string) --*

                  The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud
                  (VPC). For more information, see `VPC and Subnets
                  <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html>`__ in the
                  *Amazon VPC User Guide.*

              - **NetworkInterfaceIds** *(list) --*

                The IDs of the elastic network interface from which a specific file system is accessible.
                The elastic network interface is automatically created in the same VPC that the Amazon FSx
                file system was created in. For more information, see `Elastic Network Interfaces
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html>`__ in the *Amazon EC2
                User Guide.*

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

                The tags to associate with the file system. For more information, see `Tagging Your Amazon
                EC2 Resources <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in
                the *Amazon EC2 User Guide* .

                - *(dict) --*

                  Specifies a key-value pair for a resource tag.

                  - **Key** *(string) --*

                    A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
                    for the resource to which they are attached.

                  - **Value** *(string) --*

                    A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
                    key. Tag values can be null and don't have to be unique in a tag set. For example, you
                    can have a key-value pair in a tag set of ``finances : April`` and also of ``payroll :
                    April`` .

              - **WindowsConfiguration** *(dict) --*

                The configuration for this Microsoft Windows file system.

                - **ActiveDirectoryId** *(string) --*

                  The ID for an existing Microsoft Active Directory instance that the file system should
                  join when it's created.

                - **SelfManagedActiveDirectoryConfiguration** *(dict) --*

                  The configuration of the self-managed Microsoft Active Directory (AD) directory to which
                  the Windows File Server instance is joined.

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
                  This value defaults to false. If it's set to true, all tags on the file system are copied
                  to all automatic backups and any user-initiated backups where the user doesn't specify
                  any tags. If this value is true, and you specify one or more tags, only the specified
                  tags are copied to backups.

              - **LustreConfiguration** *(dict) --*

                The configuration for the Amazon FSx for Lustre file system.

                - **WeeklyMaintenanceStartTime** *(string) --*

                  The UTC time that you want to begin your weekly maintenance window.

                - **DataRepositoryConfiguration** *(dict) --*

                  The data repository configuration object for Lustre file systems returned in the response
                  of the ``CreateFileSystem`` operation.

                  - **ImportPath** *(string) --*

                    The import path to the Amazon S3 bucket (and optional prefix) that you're using as the
                    data repository for your FSx for Lustre file system, for example
                    ``s3://import-bucket/optional-prefix`` . If a prefix is specified after the Amazon S3
                    bucket name, only object keys with that prefix are loaded into the file system.

                  - **ExportPath** *(string) --*

                    The export path to the Amazon S3 bucket (and prefix) that you are using to store new
                    and changed Lustre file system files in S3.

                  - **ImportedFileChunkSize** *(integer) --*

                    For files imported from a data repository, this value determines the stripe count and
                    maximum amount of data per file (in MiB) stored on a single physical disk. The maximum
                    number of disks that a single file can be striped across is limited by the total number
                    of disks that make up the file system.

                    The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500
                    GiB). Amazon S3 objects have a maximum size of 5 TB.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_file_system_from_backup(
        self,
        BackupId: str,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[str] = None,
        Tags: List[ClientCreateFileSystemFromBackupTagsTypeDef] = None,
        WindowsConfiguration: ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef = None,
    ) -> ClientCreateFileSystemFromBackupResponseTypeDef:
        """
        Creates a new Amazon FSx file system from an existing Amazon FSx for Windows File Server backup.

        If a file system with the specified client request token exists and the parameters match, this
        operation returns the description of the file system. If a client request token specified by the
        file system exists and the parameters don't match, this call returns ``IncompatibleParameterError``
        . If a file system with the specified client request token doesn't exist, this operation does the
        following:

        * Creates a new Amazon FSx file system from backup with an assigned ID, and an initial lifecycle
        state of ``CREATING`` .

        * Returns the description of the file system.

        Parameters like Active Directory, default share name, automatic backup, and backup settings default
        to the parameters of the file system that was backed up, unless overridden. You can explicitly
        supply other settings.

        By using the idempotent operation, you can retry a ``CreateFileSystemFromBackup`` call without the
        risk of creating an extra file system. This approach can be useful when an initial call fails in a
        way that makes it unclear whether a file system was created. Examples are if a transport level
        timeout occurred, or your connection was reset. If you use the same client request token and the
        initial call created a file system, the client receives success as long as the parameters are the
        same.

        .. note::

          The ``CreateFileSystemFromBackup`` call returns while the file system's lifecycle state is still
          ``CREATING`` . You can check the file-system creation status by calling the  DescribeFileSystems
          operation, which returns the file system state along with other information.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/CreateFileSystemFromBackup>`_

        **Request Syntax**
        ::

          response = client.create_file_system_from_backup(
              BackupId='string',
              ClientRequestToken='string',
              SubnetIds=[
                  'string',
              ],
              SecurityGroupIds=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              WindowsConfiguration={
                  'ActiveDirectoryId': 'string',
                  'SelfManagedActiveDirectoryConfiguration': {
                      'DomainName': 'string',
                      'OrganizationalUnitDistinguishedName': 'string',
                      'FileSystemAdministratorsGroup': 'string',
                      'UserName': 'string',
                      'Password': 'string',
                      'DnsIps': [
                          'string',
                      ]
                  },
                  'ThroughputCapacity': 123,
                  'WeeklyMaintenanceStartTime': 'string',
                  'DailyAutomaticBackupStartTime': 'string',
                  'AutomaticBackupRetentionDays': 123,
                  'CopyTagsToBackups': True|False
              }
          )
        :type BackupId: string
        :param BackupId: **[REQUIRED]**

          The ID of the backup. Specifies the backup to use if you're creating a file system from an
          existing backup.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent
          creation. This string is automatically filled on your behalf when you use the AWS Command Line
          Interface (AWS CLI) or an AWS SDK.

          This field is autopopulated if not provided.

        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]**

          A list of IDs for the subnets that the file system will be accessible from. Currently, you can
          specify only one subnet. The file server is also launched in that subnet's Availability Zone.

          - *(string) --*

            The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC).
            For more information, see `VPC and Subnets
            <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html>`__ in the *Amazon VPC
            User Guide.*

        :type SecurityGroupIds: list
        :param SecurityGroupIds:

          A list of IDs for the security groups that apply to the specified network interfaces created for
          file system access. These security groups apply to all network interfaces. This value isn't
          returned in later describe requests.

          - *(string) --*

            The ID of your Amazon EC2 security group. This ID is used to control network access to the
            endpoint that Amazon FSx creates on your behalf in each subnet. For more information, see
            `Amazon EC2 Security Groups for Linux Instances
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`__ in the
            *Amazon EC2 User Guide* .

        :type Tags: list
        :param Tags:

          The tags to be applied to the file system at file system creation. The key value of the ``Name``
          tag appears in the console as the file system name.

          - *(dict) --*

            Specifies a key-value pair for a resource tag.

            - **Key** *(string) --*

              A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
              resource to which they are attached.

            - **Value** *(string) --*

              A value that specifies the ``TagValue`` , the value assigned to the corresponding tag key.
              Tag values can be null and don't have to be unique in a tag set. For example, you can have a
              key-value pair in a tag set of ``finances : April`` and also of ``payroll : April`` .

        :type WindowsConfiguration: dict
        :param WindowsConfiguration:

          The configuration for this Microsoft Windows file system.

          - **ActiveDirectoryId** *(string) --*

            The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file
            system should join when it's created.

          - **SelfManagedActiveDirectoryConfiguration** *(dict) --*

            The configuration that Amazon FSx uses to join the Windows File Server instance to your
            self-managed (including on-premises) Microsoft Active Directory (AD) directory.

            - **DomainName** *(string) --* **[REQUIRED]**

              The fully qualified domain name of the self-managed AD directory, such as
              ``corp.example.com`` .

            - **OrganizationalUnitDistinguishedName** *(string) --*

              (Optional) The fully qualified distinguished name of the organizational unit within your
              self-managed AD directory that the Windows File Server instance will join. Amazon FSx only
              accepts OU as the direct parent of the file system. An example is
              ``OU=FSx,DC=yourdomain,DC=corp,DC=com`` . To learn more, see `RFC 2253
              <https://tools.ietf.org/html/rfc2253>`__ . If none is provided, the FSx file system is
              created in the default location of your self-managed AD directory.

              .. warning::

                Only Organizational Unit (OU) objects can be the direct parent of the file system that
                you're creating.

            - **FileSystemAdministratorsGroup** *(string) --*

              (Optional) The name of the domain group whose members are granted administrative privileges
              for the file system. Administrative privileges include taking ownership of files and folders,
              and setting audit controls (audit ACLs) on files and folders. The group that you specify must
              already exist in your domain. If you don't provide one, your AD domain's Domain Admins group
              is used.

            - **UserName** *(string) --* **[REQUIRED]**

              The user name for the service account on your self-managed AD domain that Amazon FSx will use
              to join to your AD domain. This account must have the permission to join computers to the
              domain in the organizational unit provided in ``OrganizationalUnitDistinguishedName`` , or in
              the default location of your AD domain.

            - **Password** *(string) --* **[REQUIRED]**

              The password for the service account on your self-managed AD domain that Amazon FSx will use
              to join to your AD domain.

            - **DnsIps** *(list) --* **[REQUIRED]**

              A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD
              directory. The IP addresses need to be either in the same VPC CIDR range as the one in which
              your Amazon FSx file system is being created, or in the private IP version 4 (Iv4) address
              ranges, as specified in `RFC 1918 <http://www.faqs.org/rfcs/rfc1918.html>`__ :

              * 10.0.0.0 - 10.255.255.255 (10/8 prefix)

              * 172.16.0.0 - 172.31.255.255 (172.16/12 prefix)

              * 192.168.0.0 - 192.168.255.255 (192.168/16 prefix)

              - *(string) --*

          - **ThroughputCapacity** *(integer) --* **[REQUIRED]**

            The throughput of an Amazon FSx file system, measured in megabytes per second, in 2 to the *n*
            th increments, between 2^3 (8) and 2^11 (2048).

          - **WeeklyMaintenanceStartTime** *(string) --*

            The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone.

          - **DailyAutomaticBackupStartTime** *(string) --*

            The preferred time to take daily automatic backups, formatted HH:MM in the UTC time zone.

          - **AutomaticBackupRetentionDays** *(integer) --*

            The number of days to retain automatic backups. The default is to retain backups for 7 days.
            Setting this value to 0 disables the creation of automatic backups. The maximum retention
            period for backups is 35 days.

          - **CopyTagsToBackups** *(boolean) --*

            A boolean flag indicating whether tags for the file system should be copied to backups. This
            value defaults to false. If it's set to true, all tags for the file system are copied to all
            automatic and user-initiated backups where the user doesn't specify tags. If this value is
            true, and you specify one or more tags, only the specified tags are copied to backups.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileSystem': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            The response object for the ``CreateFileSystemFromBackup`` operation.

            - **FileSystem** *(dict) --*

              A description of the file system.

              - **OwnerId** *(string) --*

                The AWS account that created the file system. If the file system was created by an AWS
                Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is
                the owner.

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

                * ``CREATING`` indicates that Amazon FSx is in the process of creating the new file system.

                * ``DELETING`` indicates that Amazon FSx is in the process of deleting the file system.

                * ``FAILED`` indicates that Amazon FSx was not able to create the file system.

                * ``MISCONFIGURED`` indicates that the file system is in a failed but recoverable state.

                * ``UPDATING`` indicates that the file system is undergoing a customer initiated update.

              - **FailureDetails** *(dict) --*

                A structure providing details of any failures that occur when creating the file system has
                failed.

                - **Message** *(string) --*

                  A message describing any failures that occurred during file system creation.

              - **StorageCapacity** *(integer) --*

                The storage capacity of the file system in gigabytes (GB).

              - **VpcId** *(string) --*

                The ID of the primary VPC for the file system.

              - **SubnetIds** *(list) --*

                The ID of the subnet to contain the endpoint for the file system. One and only one is
                supported. The file system is launched in the Availability Zone associated with this subnet.

                - *(string) --*

                  The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud
                  (VPC). For more information, see `VPC and Subnets
                  <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html>`__ in the
                  *Amazon VPC User Guide.*

              - **NetworkInterfaceIds** *(list) --*

                The IDs of the elastic network interface from which a specific file system is accessible.
                The elastic network interface is automatically created in the same VPC that the Amazon FSx
                file system was created in. For more information, see `Elastic Network Interfaces
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html>`__ in the *Amazon EC2
                User Guide.*

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

                The tags to associate with the file system. For more information, see `Tagging Your Amazon
                EC2 Resources <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in
                the *Amazon EC2 User Guide* .

                - *(dict) --*

                  Specifies a key-value pair for a resource tag.

                  - **Key** *(string) --*

                    A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
                    for the resource to which they are attached.

                  - **Value** *(string) --*

                    A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
                    key. Tag values can be null and don't have to be unique in a tag set. For example, you
                    can have a key-value pair in a tag set of ``finances : April`` and also of ``payroll :
                    April`` .

              - **WindowsConfiguration** *(dict) --*

                The configuration for this Microsoft Windows file system.

                - **ActiveDirectoryId** *(string) --*

                  The ID for an existing Microsoft Active Directory instance that the file system should
                  join when it's created.

                - **SelfManagedActiveDirectoryConfiguration** *(dict) --*

                  The configuration of the self-managed Microsoft Active Directory (AD) directory to which
                  the Windows File Server instance is joined.

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
                  This value defaults to false. If it's set to true, all tags on the file system are copied
                  to all automatic backups and any user-initiated backups where the user doesn't specify
                  any tags. If this value is true, and you specify one or more tags, only the specified
                  tags are copied to backups.

              - **LustreConfiguration** *(dict) --*

                The configuration for the Amazon FSx for Lustre file system.

                - **WeeklyMaintenanceStartTime** *(string) --*

                  The UTC time that you want to begin your weekly maintenance window.

                - **DataRepositoryConfiguration** *(dict) --*

                  The data repository configuration object for Lustre file systems returned in the response
                  of the ``CreateFileSystem`` operation.

                  - **ImportPath** *(string) --*

                    The import path to the Amazon S3 bucket (and optional prefix) that you're using as the
                    data repository for your FSx for Lustre file system, for example
                    ``s3://import-bucket/optional-prefix`` . If a prefix is specified after the Amazon S3
                    bucket name, only object keys with that prefix are loaded into the file system.

                  - **ExportPath** *(string) --*

                    The export path to the Amazon S3 bucket (and prefix) that you are using to store new
                    and changed Lustre file system files in S3.

                  - **ImportedFileChunkSize** *(integer) --*

                    For files imported from a data repository, this value determines the stripe count and
                    maximum amount of data per file (in MiB) stored on a single physical disk. The maximum
                    number of disks that a single file can be striped across is limited by the total number
                    of disks that make up the file system.

                    The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500
                    GiB). Amazon S3 objects have a maximum size of 5 TB.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_backup(
        self, BackupId: str, ClientRequestToken: str = None
    ) -> ClientDeleteBackupResponseTypeDef:
        """
        Deletes an Amazon FSx for Windows File Server backup, deleting its contents. After deletion, the
        backup no longer exists, and its data is gone.

        The ``DeleteBackup`` call returns instantly. The backup will not show up in later
        ``DescribeBackups`` calls.

        .. warning::

          The data in a deleted backup is also deleted and can't be recovered by any means.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/DeleteBackup>`_

        **Request Syntax**
        ::

          response = client.delete_backup(
              BackupId='string',
              ClientRequestToken='string'
          )
        :type BackupId: string
        :param BackupId: **[REQUIRED]**

          The ID of the backup you want to delete.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent
          deletion. This is automatically filled on your behalf when using the AWS CLI or SDK.

          This field is autopopulated if not provided.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'BackupId': 'string',
                'Lifecycle': 'AVAILABLE'|'CREATING'|'DELETED'|'FAILED'
            }
          **Response Structure**

          - *(dict) --*

            The response object for ``DeleteBackup`` operation.

            - **BackupId** *(string) --*

              The ID of the backup deleted.

            - **Lifecycle** *(string) --*

              The lifecycle of the backup. Should be ``DELETED`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: ClientDeleteFileSystemWindowsConfigurationTypeDef = None,
    ) -> ClientDeleteFileSystemResponseTypeDef:
        """
        Deletes a file system, deleting its contents. After deletion, the file system no longer exists, and
        its data is gone. Any existing automatic backups will also be deleted.

        By default, when you delete an Amazon FSx for Windows File Server file system, a final backup is
        created upon deletion. This final backup is not subject to the file system's retention policy, and
        must be manually deleted.

        The ``DeleteFileSystem`` action returns while the file system has the ``DELETING`` status. You can
        check the file system deletion status by calling the  DescribeFileSystems action, which returns a
        list of file systems in your account. If you pass the file system ID for a deleted file system, the
         DescribeFileSystems returns a ``FileSystemNotFound`` error.

        .. warning::

          The data in a deleted file system is also deleted and can't be recovered by any means.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/DeleteFileSystem>`_

        **Request Syntax**
        ::

          response = client.delete_file_system(
              FileSystemId='string',
              ClientRequestToken='string',
              WindowsConfiguration={
                  'SkipFinalBackup': True|False,
                  'FinalBackupTags': [
                      {
                          'Key': 'string',
                          'Value': 'string'
                      },
                  ]
              }
          )
        :type FileSystemId: string
        :param FileSystemId: **[REQUIRED]**

          The ID of the file system you want to delete.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent
          deletion. This is automatically filled on your behalf when using the AWS CLI or SDK.

          This field is autopopulated if not provided.

        :type WindowsConfiguration: dict
        :param WindowsConfiguration:

          The configuration object for the Microsoft Windows file system used in the ``DeleteFileSystem``
          operation.

          - **SkipFinalBackup** *(boolean) --*

            By default, Amazon FSx for Windows takes a final backup on your behalf when the
            ``DeleteFileSystem`` operation is invoked. Doing this helps protect you from data loss, and we
            highly recommend taking the final backup. If you want to skip this backup, use this flag to do
            so.

          - **FinalBackupTags** *(list) --*

            A set of tags for your final backup.

            - *(dict) --*

              Specifies a key-value pair for a resource tag.

              - **Key** *(string) --*

                A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for
                the resource to which they are attached.

              - **Value** *(string) --*

                A value that specifies the ``TagValue`` , the value assigned to the corresponding tag key.
                Tag values can be null and don't have to be unique in a tag set. For example, you can have
                a key-value pair in a tag set of ``finances : April`` and also of ``payroll : April`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileSystemId': 'string',
                'Lifecycle': 'AVAILABLE'|'CREATING'|'FAILED'|'DELETING'|'MISCONFIGURED'|'UPDATING',
                'WindowsResponse': {
                    'FinalBackupId': 'string',
                    'FinalBackupTags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            The response object for the ``DeleteFileSystem`` operation.

            - **FileSystemId** *(string) --*

              The ID of the file system being deleted.

            - **Lifecycle** *(string) --*

              The file system lifecycle for the deletion request. Should be ``DELETING`` .

            - **WindowsResponse** *(dict) --*

              The response object for the Microsoft Windows file system used in the ``DeleteFileSystem``
              operation.

              - **FinalBackupId** *(string) --*

                The ID of the final backup for this file system.

              - **FinalBackupTags** *(list) --*

                The set of tags applied to the final backup.

                - *(dict) --*

                  Specifies a key-value pair for a resource tag.

                  - **Key** *(string) --*

                    A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
                    for the resource to which they are attached.

                  - **Value** *(string) --*

                    A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
                    key. Tag values can be null and don't have to be unique in a tag set. For example, you
                    can have a key-value pair in a tag set of ``finances : April`` and also of ``payroll :
                    April`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_backups(
        self,
        BackupIds: List[str] = None,
        Filters: List[ClientDescribeBackupsFiltersTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeBackupsResponseTypeDef:
        """
        Returns the description of specific Amazon FSx for Windows File Server backups, if a ``BackupIds``
        value is provided for that backup. Otherwise, it returns all backups owned by your AWS account in
        the AWS Region of the endpoint that you're calling.

        When retrieving all backups, you can optionally specify the ``MaxResults`` parameter to limit the
        number of backups in a response. If more backups remain, Amazon FSx returns a ``NextToken`` value
        in the response. In this case, send a later request with the ``NextToken`` request parameter set to
        the value of ``NextToken`` from the last response.

        This action is used in an iterative process to retrieve a list of your backups. ``DescribeBackups``
        is called first without a ``NextToken`` value. Then the action continues to be called with the
        ``NextToken`` parameter set to the value of the last ``NextToken`` value until a response has no
        ``NextToken`` .

        When using this action, keep the following in mind:

        * The implementation might return fewer than ``MaxResults`` file system descriptions while still
        including a ``NextToken`` value.

        * The order of backups returned in the response of one ``DescribeBackups`` call and the order of
        backups returned across the responses of a multi-call iteration is unspecified.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/DescribeBackups>`_

        **Request Syntax**
        ::

          response = client.describe_backups(
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
              MaxResults=123,
              NextToken='string'
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

        :type MaxResults: integer
        :param MaxResults:

          (Optional) Maximum number of backups to return in the response (integer). This parameter value
          must be greater than 0. The number of items that Amazon FSx returns is the minimum of the
          ``MaxResults`` parameter specified in the request and the service's internal maximum number of
          items per page.

        :type NextToken: string
        :param NextToken:

          (Optional) Opaque pagination token returned from a previous ``DescribeBackups`` operation
          (String). If a token present, the action continues the list from where the returning call left
          off.

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              This is present if there are more backups than returned in the response (String). You can use
              the ``NextToken`` value in the later request to fetch the backups.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_file_systems(
        self,
        FileSystemIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeFileSystemsResponseTypeDef:
        """
        Returns the description of specific Amazon FSx file systems, if a ``FileSystemIds`` value is
        provided for that file system. Otherwise, it returns descriptions of all file systems owned by your
        AWS account in the AWS Region of the endpoint that you're calling.

        When retrieving all file system descriptions, you can optionally specify the ``MaxResults``
        parameter to limit the number of descriptions in a response. If more file system descriptions
        remain, Amazon FSx returns a ``NextToken`` value in the response. In this case, send a later
        request with the ``NextToken`` request parameter set to the value of ``NextToken`` from the last
        response.

        This action is used in an iterative process to retrieve a list of your file system descriptions.
        ``DescribeFileSystems`` is called first without a ``NextToken`` value. Then the action continues to
        be called with the ``NextToken`` parameter set to the value of the last ``NextToken`` value until a
        response has no ``NextToken`` .

        When using this action, keep the following in mind:

        * The implementation might return fewer than ``MaxResults`` file system descriptions while still
        including a ``NextToken`` value.

        * The order of file systems returned in the response of one ``DescribeFileSystems`` call and the
        order of file systems returned across the responses of a multicall iteration is unspecified.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/DescribeFileSystems>`_

        **Request Syntax**
        ::

          response = client.describe_file_systems(
              FileSystemIds=[
                  'string',
              ],
              MaxResults=123,
              NextToken='string'
          )
        :type FileSystemIds: list
        :param FileSystemIds:

          (Optional) IDs of the file systems whose descriptions you want to retrieve (String).

          - *(string) --*

            The globally unique ID of the file system, assigned by Amazon FSx.

        :type MaxResults: integer
        :param MaxResults:

          (Optional) Maximum number of file systems to return in the response (integer). This parameter
          value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the
          ``MaxResults`` parameter specified in the request and the service's internal maximum number of
          items per page.

        :type NextToken: string
        :param NextToken:

          (Optional) Opaque pagination token returned from a previous ``DescribeFileSystems`` operation
          (String). If a token present, the action continues the list from where the returning call left
          off.

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              Present if there are more file systems than returned in the response (String). You can use
              the ``NextToken`` value in the later request to fetch the descriptions.

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
    def list_tags_for_resource(
        self, ResourceARN: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists tags for an Amazon FSx file systems and backups in the case of Amazon FSx for Windows File
        Server.

        When retrieving all tags, you can optionally specify the ``MaxResults`` parameter to limit the
        number of tags in a response. If more tags remain, Amazon FSx returns a ``NextToken`` value in the
        response. In this case, send a later request with the ``NextToken`` request parameter set to the
        value of ``NextToken`` from the last response.

        This action is used in an iterative process to retrieve a list of your tags.
        ``ListTagsForResource`` is called first without a ``NextToken`` value. Then the action continues to
        be called with the ``NextToken`` parameter set to the value of the last ``NextToken`` value until a
        response has no ``NextToken`` .

        When using this action, keep the following in mind:

        * The implementation might return fewer than ``MaxResults`` file system descriptions while still
        including a ``NextToken`` value.

        * The order of tags returned in the response of one ``ListTagsForResource`` call and the order of
        tags returned across the responses of a multi-call iteration is unspecified.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceARN='string',
              MaxResults=123,
              NextToken='string'
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The ARN of the Amazon FSx resource that will have its tags listed.

        :type MaxResults: integer
        :param MaxResults:

          (Optional) Maximum number of tags to return in the response (integer). This parameter value must
          be greater than 0. The number of items that Amazon FSx returns is the minimum of the
          ``MaxResults`` parameter specified in the request and the service's internal maximum number of
          items per page.

        :type NextToken: string
        :param NextToken:

          (Optional) Opaque pagination token returned from a previous ``ListTagsForResource`` operation
          (String). If a token present, the action continues the list from where the returning call left
          off.

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              This is present if there are more tags than returned in the response (String). You can use
              the ``NextToken`` value in the later request to fetch the tags.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict:
        """
        Tags an Amazon FSx resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceARN='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the Amazon FSx resource that you want to tag.

        :type Tags: list
        :param Tags: **[REQUIRED]**

          A list of tags for the resource. If a tag with a given key already exists, the value is replaced
          by the one specified in this parameter.

          - *(dict) --*

            Specifies a key-value pair for a resource tag.

            - **Key** *(string) --*

              A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
              resource to which they are attached.

            - **Value** *(string) --*

              A value that specifies the ``TagValue`` , the value assigned to the corresponding tag key.
              Tag values can be null and don't have to be unique in a tag set. For example, you can have a
              key-value pair in a tag set of ``finances : April`` and also of ``payroll : April`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            The response object for the ``TagResource`` operation.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict:
        """
        This action removes a tag from an Amazon FSx resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceARN='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The ARN of the Amazon FSx resource to untag.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          A list of keys of tags on the resource to untag. In case the tag key doesn't exist, the call will
          still succeed to be idempotent.

          - *(string) --*

            A string of 1 to 128 characters that specifies the key for a tag. Tag keys must be unique for
            the resource to which they are attached.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            The response object for ``UntagResource`` action.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: ClientUpdateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: ClientUpdateFileSystemLustreConfigurationTypeDef = None,
    ) -> ClientUpdateFileSystemResponseTypeDef:
        """
        Updates a file system configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/UpdateFileSystem>`_

        **Request Syntax**
        ::

          response = client.update_file_system(
              FileSystemId='string',
              ClientRequestToken='string',
              WindowsConfiguration={
                  'WeeklyMaintenanceStartTime': 'string',
                  'DailyAutomaticBackupStartTime': 'string',
                  'AutomaticBackupRetentionDays': 123,
                  'SelfManagedActiveDirectoryConfiguration': {
                      'UserName': 'string',
                      'Password': 'string',
                      'DnsIps': [
                          'string',
                      ]
                  }
              },
              LustreConfiguration={
                  'WeeklyMaintenanceStartTime': 'string'
              }
          )
        :type FileSystemId: string
        :param FileSystemId: **[REQUIRED]**

          The globally unique ID of the file system, assigned by Amazon FSx.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          (Optional) A string of up to 64 ASCII characters that Amazon FSx uses to ensure idempotent
          updates. This string is automatically filled on your behalf when you use the AWS Command Line
          Interface (AWS CLI) or an AWS SDK.

          This field is autopopulated if not provided.

        :type WindowsConfiguration: dict
        :param WindowsConfiguration:

          The configuration update for this Microsoft Windows file system. The only supported options are
          for backup and maintenance and for self-managed Active Directory configuration.

          - **WeeklyMaintenanceStartTime** *(string) --*

            The preferred time to perform weekly maintenance, in the UTC time zone.

          - **DailyAutomaticBackupStartTime** *(string) --*

            The preferred time to take daily automatic backups, in the UTC time zone.

          - **AutomaticBackupRetentionDays** *(integer) --*

            The number of days to retain automatic backups. Setting this to 0 disables automatic backups.
            You can retain automatic backups for a maximum of 35 days.

          - **SelfManagedActiveDirectoryConfiguration** *(dict) --*

            The configuration Amazon FSx uses to join the Windows File Server instance to the self-managed
            Microsoft AD directory.

            - **UserName** *(string) --*

              The user name for the service account on your self-managed AD domain that Amazon FSx will use
              to join to your AD domain. This account must have the permission to join computers to the
              domain in the organizational unit provided in ``OrganizationalUnitDistinguishedName`` .

            - **Password** *(string) --*

              The password for the service account on your self-managed AD domain that Amazon FSx will use
              to join to your AD domain.

            - **DnsIps** *(list) --*

              A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD
              directory.

              - *(string) --*

        :type LustreConfiguration: dict
        :param LustreConfiguration:

          The configuration object for Amazon FSx for Lustre file systems used in the ``UpdateFileSystem``
          operation.

          - **WeeklyMaintenanceStartTime** *(string) --*

            The preferred time to perform weekly maintenance, in the UTC time zone.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileSystem': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

            The response object for the ``UpdateFileSystem`` operation.

            - **FileSystem** *(dict) --*

              A description of the file system that was updated.

              - **OwnerId** *(string) --*

                The AWS account that created the file system. If the file system was created by an AWS
                Identity and Access Management (IAM) user, the AWS account to which the IAM user belongs is
                the owner.

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

                * ``CREATING`` indicates that Amazon FSx is in the process of creating the new file system.

                * ``DELETING`` indicates that Amazon FSx is in the process of deleting the file system.

                * ``FAILED`` indicates that Amazon FSx was not able to create the file system.

                * ``MISCONFIGURED`` indicates that the file system is in a failed but recoverable state.

                * ``UPDATING`` indicates that the file system is undergoing a customer initiated update.

              - **FailureDetails** *(dict) --*

                A structure providing details of any failures that occur when creating the file system has
                failed.

                - **Message** *(string) --*

                  A message describing any failures that occurred during file system creation.

              - **StorageCapacity** *(integer) --*

                The storage capacity of the file system in gigabytes (GB).

              - **VpcId** *(string) --*

                The ID of the primary VPC for the file system.

              - **SubnetIds** *(list) --*

                The ID of the subnet to contain the endpoint for the file system. One and only one is
                supported. The file system is launched in the Availability Zone associated with this subnet.

                - *(string) --*

                  The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud
                  (VPC). For more information, see `VPC and Subnets
                  <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html>`__ in the
                  *Amazon VPC User Guide.*

              - **NetworkInterfaceIds** *(list) --*

                The IDs of the elastic network interface from which a specific file system is accessible.
                The elastic network interface is automatically created in the same VPC that the Amazon FSx
                file system was created in. For more information, see `Elastic Network Interfaces
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html>`__ in the *Amazon EC2
                User Guide.*

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

                The tags to associate with the file system. For more information, see `Tagging Your Amazon
                EC2 Resources <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html>`__ in
                the *Amazon EC2 User Guide* .

                - *(dict) --*

                  Specifies a key-value pair for a resource tag.

                  - **Key** *(string) --*

                    A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
                    for the resource to which they are attached.

                  - **Value** *(string) --*

                    A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
                    key. Tag values can be null and don't have to be unique in a tag set. For example, you
                    can have a key-value pair in a tag set of ``finances : April`` and also of ``payroll :
                    April`` .

              - **WindowsConfiguration** *(dict) --*

                The configuration for this Microsoft Windows file system.

                - **ActiveDirectoryId** *(string) --*

                  The ID for an existing Microsoft Active Directory instance that the file system should
                  join when it's created.

                - **SelfManagedActiveDirectoryConfiguration** *(dict) --*

                  The configuration of the self-managed Microsoft Active Directory (AD) directory to which
                  the Windows File Server instance is joined.

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
                  This value defaults to false. If it's set to true, all tags on the file system are copied
                  to all automatic backups and any user-initiated backups where the user doesn't specify
                  any tags. If this value is true, and you specify one or more tags, only the specified
                  tags are copied to backups.

              - **LustreConfiguration** *(dict) --*

                The configuration for the Amazon FSx for Lustre file system.

                - **WeeklyMaintenanceStartTime** *(string) --*

                  The UTC time that you want to begin your weekly maintenance window.

                - **DataRepositoryConfiguration** *(dict) --*

                  The data repository configuration object for Lustre file systems returned in the response
                  of the ``CreateFileSystem`` operation.

                  - **ImportPath** *(string) --*

                    The import path to the Amazon S3 bucket (and optional prefix) that you're using as the
                    data repository for your FSx for Lustre file system, for example
                    ``s3://import-bucket/optional-prefix`` . If a prefix is specified after the Amazon S3
                    bucket name, only object keys with that prefix are loaded into the file system.

                  - **ExportPath** *(string) --*

                    The export path to the Amazon S3 bucket (and prefix) that you are using to store new
                    and changed Lustre file system files in S3.

                  - **ImportedFileChunkSize** *(integer) --*

                    For files imported from a data repository, this value determines the stripe count and
                    maximum amount of data per file (in MiB) stored on a single physical disk. The maximum
                    number of disks that a single file can be striped across is limited by the total number
                    of disks that make up the file system.

                    The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500
                    GiB). Amazon S3 objects have a maximum size of 5 TB.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> paginator_scope.DescribeBackupsPaginator:
        """
        Get Paginator for `describe_backups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> paginator_scope.DescribeFileSystemsPaginator:
        """
        Get Paginator for `describe_file_systems` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        Get Paginator for `list_tags_for_resource` operation.
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
    ActiveDirectoryError: Boto3ClientError
    BackupInProgress: Boto3ClientError
    BackupNotFound: Boto3ClientError
    BackupRestoring: Boto3ClientError
    BadRequest: Boto3ClientError
    ClientError: Boto3ClientError
    FileSystemNotFound: Boto3ClientError
    IncompatibleParameterError: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidExportPath: Boto3ClientError
    InvalidImportPath: Boto3ClientError
    InvalidNetworkSettings: Boto3ClientError
    MissingFileSystemConfiguration: Boto3ClientError
    NotServiceResourceError: Boto3ClientError
    ResourceDoesNotSupportTagging: Boto3ClientError
    ResourceNotFound: Boto3ClientError
    ServiceLimitExceeded: Boto3ClientError
    UnsupportedOperation: Boto3ClientError
