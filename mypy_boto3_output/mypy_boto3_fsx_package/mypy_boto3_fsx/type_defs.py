"Main interface for fsx type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateBackupResponseBackupDirectoryInformationTypeDef",
    "ClientCreateBackupResponseBackupFailureDetailsTypeDef",
    "ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef",
    "ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemTagsTypeDef",
    "ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemTypeDef",
    "ClientCreateBackupResponseBackupTagsTypeDef",
    "ClientCreateBackupResponseBackupTypeDef",
    "ClientCreateBackupResponseTypeDef",
    "ClientCreateBackupTagsTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemTypeDef",
    "ClientCreateFileSystemFromBackupResponseTypeDef",
    "ClientCreateFileSystemFromBackupTagsTypeDef",
    "ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef",
    "ClientCreateFileSystemLustreConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef",
    "ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemTagsTypeDef",
    "ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemTypeDef",
    "ClientCreateFileSystemResponseTypeDef",
    "ClientCreateFileSystemTagsTypeDef",
    "ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemWindowsConfigurationTypeDef",
    "ClientDeleteBackupResponseTypeDef",
    "ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef",
    "ClientDeleteFileSystemResponseWindowsResponseTypeDef",
    "ClientDeleteFileSystemResponseTypeDef",
    "ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef",
    "ClientDeleteFileSystemWindowsConfigurationTypeDef",
    "ClientDescribeBackupsFiltersTypeDef",
    "ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef",
    "ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemTypeDef",
    "ClientDescribeBackupsResponseBackupsTagsTypeDef",
    "ClientDescribeBackupsResponseBackupsTypeDef",
    "ClientDescribeBackupsResponseTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    "ClientDescribeFileSystemsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateFileSystemLustreConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef",
    "ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemTagsTypeDef",
    "ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemTypeDef",
    "ClientUpdateFileSystemResponseTypeDef",
    "ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientUpdateFileSystemWindowsConfigurationTypeDef",
    "DescribeBackupsPaginateFiltersTypeDef",
    "DescribeBackupsPaginatePaginationConfigTypeDef",
    "DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef",
    "DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef",
    "DescribeBackupsPaginateResponseBackupsFileSystemTypeDef",
    "DescribeBackupsPaginateResponseBackupsTagsTypeDef",
    "DescribeBackupsPaginateResponseBackupsTypeDef",
    "DescribeBackupsPaginateResponseTypeDef",
    "DescribeFileSystemsPaginatePaginationConfigTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef",
    "DescribeFileSystemsPaginateResponseFileSystemsTypeDef",
    "DescribeFileSystemsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
)


_ClientCreateBackupResponseBackupDirectoryInformationTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)


class ClientCreateBackupResponseBackupDirectoryInformationTypeDef(
    _ClientCreateBackupResponseBackupDirectoryInformationTypeDef
):
    """
    Type definition for `ClientCreateBackupResponseBackup` `DirectoryInformation`

    The configuration of the self-managed Microsoft Active Directory (AD) to which the Windows
    File Server instance is joined.

    - **DomainName** *(string) --*

      The fully qualified domain name of the self-managed AD directory.

    - **ActiveDirectoryId** *(string) --*

      The ID of the AWS Managed Microsoft Active Directory instance to which the file system is
      joined.
    """


_ClientCreateBackupResponseBackupFailureDetailsTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientCreateBackupResponseBackupFailureDetailsTypeDef(
    _ClientCreateBackupResponseBackupFailureDetailsTypeDef
):
    """
    Type definition for `ClientCreateBackupResponseBackup` `FailureDetails`

    Details explaining any failures that occur when creating a backup.

    - **Message** *(string) --*

      A message describing the backup creation failure.
    """


_ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef(
    _ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef
):
    """
    Type definition for `ClientCreateBackupResponseBackupFileSystem` `FailureDetails`

    A structure providing details of any failures that occur when creating the file system
    has failed.

    - **Message** *(string) --*

      A message describing any failures that occurred during file system creation.
    """


_ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    """
    Type definition for `ClientCreateBackupResponseBackupFileSystemLustreConfiguration` `DataRepositoryConfiguration`

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


_ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef(
    _ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef
):
    """
    Type definition for `ClientCreateBackupResponseBackupFileSystem` `LustreConfiguration`

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


_ClientCreateBackupResponseBackupFileSystemTagsTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemTagsTypeDef(
    _ClientCreateBackupResponseBackupFileSystemTagsTypeDef
):
    """
    Type definition for `ClientCreateBackupResponseBackupFileSystem` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
      for the resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
      key. Tag values can be null and don't have to be unique in a tag set. For example,
      you can have a key-value pair in a tag set of ``finances : April`` and also of
      ``payroll : April`` .
    """


_ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    """
    Type definition for `ClientCreateBackupResponseBackupFileSystemWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[str],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef(
    _ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef
):
    """
    Type definition for `ClientCreateBackupResponseBackupFileSystem` `WindowsConfiguration`

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
    """


_ClientCreateBackupResponseBackupFileSystemTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": str,
        "Lifecycle": str,
        "FailureDetails": ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateBackupResponseBackupFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateBackupResponseBackupFileSystemTypeDef(
    _ClientCreateBackupResponseBackupFileSystemTypeDef
):
    """
    Type definition for `ClientCreateBackupResponseBackup` `FileSystem`

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
    """


_ClientCreateBackupResponseBackupTagsTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateBackupResponseBackupTagsTypeDef(
    _ClientCreateBackupResponseBackupTagsTypeDef
):
    """
    Type definition for `ClientCreateBackupResponseBackup` `Tags`

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


_ClientCreateBackupResponseBackupTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": str,
        "FailureDetails": ClientCreateBackupResponseBackupFailureDetailsTypeDef,
        "Type": str,
        "ProgressPercent": int,
        "CreationTime": datetime,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateBackupResponseBackupTagsTypeDef],
        "FileSystem": ClientCreateBackupResponseBackupFileSystemTypeDef,
        "DirectoryInformation": ClientCreateBackupResponseBackupDirectoryInformationTypeDef,
    },
    total=False,
)


class ClientCreateBackupResponseBackupTypeDef(_ClientCreateBackupResponseBackupTypeDef):
    """
    Type definition for `ClientCreateBackupResponse` `Backup`

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


_ClientCreateBackupResponseTypeDef = TypedDict(
    "_ClientCreateBackupResponseTypeDef",
    {"Backup": ClientCreateBackupResponseBackupTypeDef},
    total=False,
)


class ClientCreateBackupResponseTypeDef(_ClientCreateBackupResponseTypeDef):
    """
    Type definition for `ClientCreateBackup` `Response`

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


_ClientCreateBackupTagsTypeDef = TypedDict(
    "_ClientCreateBackupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateBackupTagsTypeDef(_ClientCreateBackupTagsTypeDef):
    """
    Type definition for `ClientCreateBackup` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
      resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag key.
      Tag values can be null and don't have to be unique in a tag set. For example, you can have a
      key-value pair in a tag set of ``finances : April`` and also of ``payroll : April`` .
    """


_ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef
):
    """
    Type definition for `ClientCreateFileSystemFromBackupResponseFileSystem` `FailureDetails`

    A structure providing details of any failures that occur when creating the file system has
    failed.

    - **Message** *(string) --*

      A message describing any failures that occurred during file system creation.
    """


_ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFileSystemFromBackupResponseFileSystemLustreConfiguration` `DataRepositoryConfiguration`

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


_ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFileSystemFromBackupResponseFileSystem` `LustreConfiguration`

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


_ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef
):
    """
    Type definition for `ClientCreateFileSystemFromBackupResponseFileSystem` `Tags`

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


_ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[str],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFileSystemFromBackupResponseFileSystem` `WindowsConfiguration`

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
    """


_ClientCreateFileSystemFromBackupResponseFileSystemTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": str,
        "Lifecycle": str,
        "FailureDetails": ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFileSystemFromBackupResponseFileSystemTypeDef(
    _ClientCreateFileSystemFromBackupResponseFileSystemTypeDef
):
    """
    Type definition for `ClientCreateFileSystemFromBackupResponse` `FileSystem`

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


_ClientCreateFileSystemFromBackupResponseTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupResponseTypeDef",
    {"FileSystem": ClientCreateFileSystemFromBackupResponseFileSystemTypeDef},
    total=False,
)


class ClientCreateFileSystemFromBackupResponseTypeDef(
    _ClientCreateFileSystemFromBackupResponseTypeDef
):
    """
    Type definition for `ClientCreateFileSystemFromBackup` `Response`

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


_ClientCreateFileSystemFromBackupTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemFromBackupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateFileSystemFromBackupTagsTypeDef(
    _ClientCreateFileSystemFromBackupTagsTypeDef
):
    """
    Type definition for `ClientCreateFileSystemFromBackup` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
      resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag key.
      Tag values can be null and don't have to be unique in a tag set. For example, you can have a
      key-value pair in a tag set of ``finances : April`` and also of ``payroll : April`` .
    """


_RequiredClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {"DomainName": str, "UserName": str, "Password": str, "DnsIps": List[str]},
)
_OptionalClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {"OrganizationalUnitDistinguishedName": str, "FileSystemAdministratorsGroup": str},
    total=False,
)


class ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _RequiredClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
    _OptionalClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateFileSystemFromBackupWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_RequiredClientCreateFileSystemFromBackupWindowsConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateFileSystemFromBackupWindowsConfigurationTypeDef",
    {"ThroughputCapacity": int},
)
_OptionalClientCreateFileSystemFromBackupWindowsConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateFileSystemFromBackupWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef(
    _RequiredClientCreateFileSystemFromBackupWindowsConfigurationTypeDef,
    _OptionalClientCreateFileSystemFromBackupWindowsConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateFileSystemFromBackup` `WindowsConfiguration`

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
    """


_ClientCreateFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
    },
    total=False,
)


class ClientCreateFileSystemLustreConfigurationTypeDef(
    _ClientCreateFileSystemLustreConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFileSystem` `LustreConfiguration`

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
    """


_ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef(
    _ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef
):
    """
    Type definition for `ClientCreateFileSystemResponseFileSystem` `FailureDetails`

    A structure providing details of any failures that occur when creating the file system has
    failed.

    - **Message** *(string) --*

      A message describing any failures that occurred during file system creation.
    """


_ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFileSystemResponseFileSystemLustreConfiguration` `DataRepositoryConfiguration`

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


_ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef(
    _ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFileSystemResponseFileSystem` `LustreConfiguration`

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


_ClientCreateFileSystemResponseFileSystemTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateFileSystemResponseFileSystemTagsTypeDef(
    _ClientCreateFileSystemResponseFileSystemTagsTypeDef
):
    """
    Type definition for `ClientCreateFileSystemResponseFileSystem` `Tags`

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


_ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFileSystemResponseFileSystemWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[str],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef(
    _ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFileSystemResponseFileSystem` `WindowsConfiguration`

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
    """


_ClientCreateFileSystemResponseFileSystemTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": str,
        "Lifecycle": str,
        "FailureDetails": ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateFileSystemResponseFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFileSystemResponseFileSystemTypeDef(
    _ClientCreateFileSystemResponseFileSystemTypeDef
):
    """
    Type definition for `ClientCreateFileSystemResponse` `FileSystem`

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


_ClientCreateFileSystemResponseTypeDef = TypedDict(
    "_ClientCreateFileSystemResponseTypeDef",
    {"FileSystem": ClientCreateFileSystemResponseFileSystemTypeDef},
    total=False,
)


class ClientCreateFileSystemResponseTypeDef(_ClientCreateFileSystemResponseTypeDef):
    """
    Type definition for `ClientCreateFileSystem` `Response`

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


_ClientCreateFileSystemTagsTypeDef = TypedDict(
    "_ClientCreateFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateFileSystemTagsTypeDef(_ClientCreateFileSystemTagsTypeDef):
    """
    Type definition for `ClientCreateFileSystem` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
      resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag key.
      Tag values can be null and don't have to be unique in a tag set. For example, you can have a
      key-value pair in a tag set of ``finances : April`` and also of ``payroll : April`` .
    """


_RequiredClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {"DomainName": str, "UserName": str, "Password": str, "DnsIps": List[str]},
)
_OptionalClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {"OrganizationalUnitDistinguishedName": str, "FileSystemAdministratorsGroup": str},
    total=False,
)


class ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _RequiredClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
    _OptionalClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateFileSystemWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_RequiredClientCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateFileSystemWindowsConfigurationTypeDef",
    {"ThroughputCapacity": int},
)
_OptionalClientCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientCreateFileSystemWindowsConfigurationTypeDef(
    _RequiredClientCreateFileSystemWindowsConfigurationTypeDef,
    _OptionalClientCreateFileSystemWindowsConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateFileSystem` `WindowsConfiguration`

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
    """


_ClientDeleteBackupResponseTypeDef = TypedDict(
    "_ClientDeleteBackupResponseTypeDef",
    {"BackupId": str, "Lifecycle": str},
    total=False,
)


class ClientDeleteBackupResponseTypeDef(_ClientDeleteBackupResponseTypeDef):
    """
    Type definition for `ClientDeleteBackup` `Response`

    The response object for ``DeleteBackup`` operation.

    - **BackupId** *(string) --*

      The ID of the backup deleted.

    - **Lifecycle** *(string) --*

      The lifecycle of the backup. Should be ``DELETED`` .
    """


_ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef = TypedDict(
    "_ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef(
    _ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef
):
    """
    Type definition for `ClientDeleteFileSystemResponseWindowsResponse` `FinalBackupTags`

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


_ClientDeleteFileSystemResponseWindowsResponseTypeDef = TypedDict(
    "_ClientDeleteFileSystemResponseWindowsResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List[
            ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef
        ],
    },
    total=False,
)


class ClientDeleteFileSystemResponseWindowsResponseTypeDef(
    _ClientDeleteFileSystemResponseWindowsResponseTypeDef
):
    """
    Type definition for `ClientDeleteFileSystemResponse` `WindowsResponse`

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


_ClientDeleteFileSystemResponseTypeDef = TypedDict(
    "_ClientDeleteFileSystemResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": str,
        "WindowsResponse": ClientDeleteFileSystemResponseWindowsResponseTypeDef,
    },
    total=False,
)


class ClientDeleteFileSystemResponseTypeDef(_ClientDeleteFileSystemResponseTypeDef):
    """
    Type definition for `ClientDeleteFileSystem` `Response`

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


_ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef = TypedDict(
    "_ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef(
    _ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef
):
    """
    Type definition for `ClientDeleteFileSystemWindowsConfiguration` `FinalBackupTags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for
      the resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag key.
      Tag values can be null and don't have to be unique in a tag set. For example, you can have
      a key-value pair in a tag set of ``finances : April`` and also of ``payroll : April`` .
    """


_ClientDeleteFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientDeleteFileSystemWindowsConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": List[
            ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef
        ],
    },
    total=False,
)


class ClientDeleteFileSystemWindowsConfigurationTypeDef(
    _ClientDeleteFileSystemWindowsConfigurationTypeDef
):
    """
    Type definition for `ClientDeleteFileSystem` `WindowsConfiguration`

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
    """


_ClientDescribeBackupsFiltersTypeDef = TypedDict(
    "_ClientDescribeBackupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientDescribeBackupsFiltersTypeDef(_ClientDescribeBackupsFiltersTypeDef):
    """
    Type definition for `ClientDescribeBackups` `Filters`

    A filter used to restrict the results of describe calls. You can use multiple filters to return
    results that meet all applied filter requirements.

    - **Name** *(string) --*

      The name for this filter.

    - **Values** *(list) --*

      The values of the filter. These are all the values for any of the applied filters.

      - *(string) --*

        The value for a filter.
    """


_ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)


class ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef(
    _ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponseBackups` `DirectoryInformation`

    The configuration of the self-managed Microsoft Active Directory (AD) to which the
    Windows File Server instance is joined.

    - **DomainName** *(string) --*

      The fully qualified domain name of the self-managed AD directory.

    - **ActiveDirectoryId** *(string) --*

      The ID of the AWS Managed Microsoft Active Directory instance to which the file system
      is joined.
    """


_ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef(
    _ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponseBackups` `FailureDetails`

    Details explaining any failures that occur when creating a backup.

    - **Message** *(string) --*

      A message describing the backup creation failure.
    """


_ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponseBackupsFileSystem` `FailureDetails`

    A structure providing details of any failures that occur when creating the file system
    has failed.

    - **Message** *(string) --*

      A message describing any failures that occurred during file system creation.
    """


_ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponseBackupsFileSystemLustreConfiguration` `DataRepositoryConfiguration`

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
    """


_ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponseBackupsFileSystem` `LustreConfiguration`

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
    """


_ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponseBackupsFileSystem` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be
      unique for the resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding
      tag key. Tag values can be null and don't have to be unique in a tag set. For
      example, you can have a key-value pair in a tag set of ``finances : April`` and
      also of ``payroll : April`` .
    """


_ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponseBackupsFileSystemWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[str],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponseBackupsFileSystem` `WindowsConfiguration`

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
    """


_ClientDescribeBackupsResponseBackupsFileSystemTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": str,
        "Lifecycle": str,
        "FailureDetails": ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsFileSystemTypeDef(
    _ClientDescribeBackupsResponseBackupsFileSystemTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponseBackups` `FileSystem`

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
    """


_ClientDescribeBackupsResponseBackupsTagsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeBackupsResponseBackupsTagsTypeDef(
    _ClientDescribeBackupsResponseBackupsTagsTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponseBackups` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
      for the resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
      key. Tag values can be null and don't have to be unique in a tag set. For example,
      you can have a key-value pair in a tag set of ``finances : April`` and also of
      ``payroll : April`` .
    """


_ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsTypeDef",
    {
        "BackupId": str,
        "Lifecycle": str,
        "FailureDetails": ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef,
        "Type": str,
        "ProgressPercent": int,
        "CreationTime": datetime,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientDescribeBackupsResponseBackupsTagsTypeDef],
        "FileSystem": ClientDescribeBackupsResponseBackupsFileSystemTypeDef,
        "DirectoryInformation": ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef,
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsTypeDef(
    _ClientDescribeBackupsResponseBackupsTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponse` `Backups`

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


_ClientDescribeBackupsResponseTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseTypeDef",
    {"Backups": List[ClientDescribeBackupsResponseBackupsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeBackupsResponseTypeDef(_ClientDescribeBackupsResponseTypeDef):
    """
    Type definition for `ClientDescribeBackups` `Response`

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


_ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef
):
    """
    Type definition for `ClientDescribeFileSystemsResponseFileSystems` `FailureDetails`

    A structure providing details of any failures that occur when creating the file system
    has failed.

    - **Message** *(string) --*

      A message describing any failures that occurred during file system creation.
    """


_ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeFileSystemsResponseFileSystemsLustreConfiguration` `DataRepositoryConfiguration`

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


_ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeFileSystemsResponseFileSystems` `LustreConfiguration`

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


_ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef
):
    """
    Type definition for `ClientDescribeFileSystemsResponseFileSystems` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
      for the resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
      key. Tag values can be null and don't have to be unique in a tag set. For example,
      you can have a key-value pair in a tag set of ``finances : April`` and also of
      ``payroll : April`` .
    """


_ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeFileSystemsResponseFileSystemsWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[str],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeFileSystemsResponseFileSystems` `WindowsConfiguration`

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
    """


_ClientDescribeFileSystemsResponseFileSystemsTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": str,
        "Lifecycle": str,
        "FailureDetails": ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef],
        "WindowsConfiguration": ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeFileSystemsResponseFileSystemsTypeDef(
    _ClientDescribeFileSystemsResponseFileSystemsTypeDef
):
    """
    Type definition for `ClientDescribeFileSystemsResponse` `FileSystems`

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


_ClientDescribeFileSystemsResponseTypeDef = TypedDict(
    "_ClientDescribeFileSystemsResponseTypeDef",
    {
        "FileSystems": List[ClientDescribeFileSystemsResponseFileSystemsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeFileSystemsResponseTypeDef(
    _ClientDescribeFileSystemsResponseTypeDef
):
    """
    Type definition for `ClientDescribeFileSystems` `Response`

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


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

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


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

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


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
      resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag key.
      Tag values can be null and don't have to be unique in a tag set. For example, you can have a
      key-value pair in a tag set of ``finances : April`` and also of ``payroll : April`` .
    """


_ClientUpdateFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemLustreConfigurationTypeDef",
    {"WeeklyMaintenanceStartTime": str},
    total=False,
)


class ClientUpdateFileSystemLustreConfigurationTypeDef(
    _ClientUpdateFileSystemLustreConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateFileSystem` `LustreConfiguration`

    The configuration object for Amazon FSx for Lustre file systems used in the ``UpdateFileSystem``
    operation.

    - **WeeklyMaintenanceStartTime** *(string) --*

      The preferred time to perform weekly maintenance, in the UTC time zone.
    """


_ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef(
    _ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef
):
    """
    Type definition for `ClientUpdateFileSystemResponseFileSystem` `FailureDetails`

    A structure providing details of any failures that occur when creating the file system has
    failed.

    - **Message** *(string) --*

      A message describing any failures that occurred during file system creation.
    """


_ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateFileSystemResponseFileSystemLustreConfiguration` `DataRepositoryConfiguration`

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


_ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef(
    _ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateFileSystemResponseFileSystem` `LustreConfiguration`

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


_ClientUpdateFileSystemResponseFileSystemTagsTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemTagsTypeDef(
    _ClientUpdateFileSystemResponseFileSystemTagsTypeDef
):
    """
    Type definition for `ClientUpdateFileSystemResponseFileSystem` `Tags`

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


_ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateFileSystemResponseFileSystemWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[str],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef(
    _ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateFileSystemResponseFileSystem` `WindowsConfiguration`

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
    """


_ClientUpdateFileSystemResponseFileSystemTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": str,
        "Lifecycle": str,
        "FailureDetails": ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientUpdateFileSystemResponseFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateFileSystemResponseFileSystemTypeDef(
    _ClientUpdateFileSystemResponseFileSystemTypeDef
):
    """
    Type definition for `ClientUpdateFileSystemResponse` `FileSystem`

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


_ClientUpdateFileSystemResponseTypeDef = TypedDict(
    "_ClientUpdateFileSystemResponseTypeDef",
    {"FileSystem": ClientUpdateFileSystemResponseFileSystemTypeDef},
    total=False,
)


class ClientUpdateFileSystemResponseTypeDef(_ClientUpdateFileSystemResponseTypeDef):
    """
    Type definition for `ClientUpdateFileSystem` `Response`

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


_ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {"UserName": str, "Password": str, "DnsIps": List[str]},
    total=False,
)


class ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateFileSystemWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_ClientUpdateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_ClientUpdateFileSystemWindowsConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "SelfManagedActiveDirectoryConfiguration": ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateFileSystemWindowsConfigurationTypeDef(
    _ClientUpdateFileSystemWindowsConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateFileSystem` `WindowsConfiguration`

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
    """


_DescribeBackupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeBackupsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeBackupsPaginateFiltersTypeDef(_DescribeBackupsPaginateFiltersTypeDef):
    """
    Type definition for `DescribeBackupsPaginate` `Filters`

    A filter used to restrict the results of describe calls. You can use multiple filters to return
    results that meet all applied filter requirements.

    - **Name** *(string) --*

      The name for this filter.

    - **Values** *(list) --*

      The values of the filter. These are all the values for any of the applied filters.

      - *(string) --*

        The value for a filter.
    """


_DescribeBackupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeBackupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeBackupsPaginatePaginationConfigTypeDef(
    _DescribeBackupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeBackupsPaginate` `PaginationConfig`

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


_DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)


class DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef(
    _DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponseBackups` `DirectoryInformation`

    The configuration of the self-managed Microsoft Active Directory (AD) to which the
    Windows File Server instance is joined.

    - **DomainName** *(string) --*

      The fully qualified domain name of the self-managed AD directory.

    - **ActiveDirectoryId** *(string) --*

      The ID of the AWS Managed Microsoft Active Directory instance to which the file system
      is joined.
    """


_DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef(
    _DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponseBackups` `FailureDetails`

    Details explaining any failures that occur when creating a backup.

    - **Message** *(string) --*

      A message describing the backup creation failure.
    """


_DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponseBackupsFileSystem` `FailureDetails`

    A structure providing details of any failures that occur when creating the file system
    has failed.

    - **Message** *(string) --*

      A message describing any failures that occurred during file system creation.
    """


_DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponseBackupsFileSystemLustreConfiguration` `DataRepositoryConfiguration`

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
    """


_DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponseBackupsFileSystem` `LustreConfiguration`

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
    """


_DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponseBackupsFileSystem` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be
      unique for the resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding
      tag key. Tag values can be null and don't have to be unique in a tag set. For
      example, you can have a key-value pair in a tag set of ``finances : April`` and
      also of ``payroll : April`` .
    """


_DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[str],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponseBackupsFileSystem` `WindowsConfiguration`

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
    """


_DescribeBackupsPaginateResponseBackupsFileSystemTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": str,
        "Lifecycle": str,
        "FailureDetails": DescribeBackupsPaginateResponseBackupsFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[DescribeBackupsPaginateResponseBackupsFileSystemTagsTypeDef],
        "WindowsConfiguration": DescribeBackupsPaginateResponseBackupsFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": DescribeBackupsPaginateResponseBackupsFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsFileSystemTypeDef(
    _DescribeBackupsPaginateResponseBackupsFileSystemTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponseBackups` `FileSystem`

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
    """


_DescribeBackupsPaginateResponseBackupsTagsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeBackupsPaginateResponseBackupsTagsTypeDef(
    _DescribeBackupsPaginateResponseBackupsTagsTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponseBackups` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
      for the resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
      key. Tag values can be null and don't have to be unique in a tag set. For example,
      you can have a key-value pair in a tag set of ``finances : April`` and also of
      ``payroll : April`` .
    """


_DescribeBackupsPaginateResponseBackupsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsTypeDef",
    {
        "BackupId": str,
        "Lifecycle": str,
        "FailureDetails": DescribeBackupsPaginateResponseBackupsFailureDetailsTypeDef,
        "Type": str,
        "ProgressPercent": int,
        "CreationTime": datetime,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[DescribeBackupsPaginateResponseBackupsTagsTypeDef],
        "FileSystem": DescribeBackupsPaginateResponseBackupsFileSystemTypeDef,
        "DirectoryInformation": DescribeBackupsPaginateResponseBackupsDirectoryInformationTypeDef,
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsTypeDef(
    _DescribeBackupsPaginateResponseBackupsTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponse` `Backups`

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


_DescribeBackupsPaginateResponseTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseTypeDef",
    {"Backups": List[DescribeBackupsPaginateResponseBackupsTypeDef]},
    total=False,
)


class DescribeBackupsPaginateResponseTypeDef(_DescribeBackupsPaginateResponseTypeDef):
    """
    Type definition for `DescribeBackupsPaginate` `Response`

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


_DescribeFileSystemsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFileSystemsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFileSystemsPaginatePaginationConfigTypeDef(
    _DescribeFileSystemsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginate` `PaginationConfig`

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


_DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginateResponseFileSystems` `FailureDetails`

    A structure providing details of any failures that occur when creating the file system
    has failed.

    - **Message** *(string) --*

      A message describing any failures that occurred during file system creation.
    """


_DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginateResponseFileSystemsLustreConfiguration` `DataRepositoryConfiguration`

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


_DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginateResponseFileSystems` `LustreConfiguration`

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


_DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginateResponseFileSystems` `Tags`

    Specifies a key-value pair for a resource tag.

    - **Key** *(string) --*

      A value that specifies the ``TagKey`` , the name of the tag. Tag keys must be unique
      for the resource to which they are attached.

    - **Value** *(string) --*

      A value that specifies the ``TagValue`` , the value assigned to the corresponding tag
      key. Tag values can be null and don't have to be unique in a tag set. For example,
      you can have a key-value pair in a tag set of ``finances : April`` and also of
      ``payroll : April`` .
    """


_DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginateResponseFileSystemsWindowsConfiguration` `SelfManagedActiveDirectoryConfiguration`

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
    """


_DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[str],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginateResponseFileSystems` `WindowsConfiguration`

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
    """


_DescribeFileSystemsPaginateResponseFileSystemsTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseFileSystemsTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": str,
        "Lifecycle": str,
        "FailureDetails": DescribeFileSystemsPaginateResponseFileSystemsFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[DescribeFileSystemsPaginateResponseFileSystemsTagsTypeDef],
        "WindowsConfiguration": DescribeFileSystemsPaginateResponseFileSystemsWindowsConfigurationTypeDef,
        "LustreConfiguration": DescribeFileSystemsPaginateResponseFileSystemsLustreConfigurationTypeDef,
    },
    total=False,
)


class DescribeFileSystemsPaginateResponseFileSystemsTypeDef(
    _DescribeFileSystemsPaginateResponseFileSystemsTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginateResponse` `FileSystems`

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


_DescribeFileSystemsPaginateResponseTypeDef = TypedDict(
    "_DescribeFileSystemsPaginateResponseTypeDef",
    {"FileSystems": List[DescribeFileSystemsPaginateResponseFileSystemsTypeDef]},
    total=False,
)


class DescribeFileSystemsPaginateResponseTypeDef(
    _DescribeFileSystemsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeFileSystemsPaginate` `Response`

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


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `PaginationConfig`

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


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginateResponse` `Tags`

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


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(
    _ListTagsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `Response`

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
