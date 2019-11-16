"Main interface for opsworkscm type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAssociateNodeEngineAttributesTypeDef",
    "ClientAssociateNodeResponseTypeDef",
    "ClientCreateBackupResponseBackupTypeDef",
    "ClientCreateBackupResponseTypeDef",
    "ClientCreateServerEngineAttributesTypeDef",
    "ClientCreateServerResponseServerEngineAttributesTypeDef",
    "ClientCreateServerResponseServerTypeDef",
    "ClientCreateServerResponseTypeDef",
    "ClientDescribeAccountAttributesResponseAttributesTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeBackupsResponseBackupsTypeDef",
    "ClientDescribeBackupsResponseTypeDef",
    "ClientDescribeEventsResponseServerEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef",
    "ClientDescribeNodeAssociationStatusResponseTypeDef",
    "ClientDescribeServersResponseServersEngineAttributesTypeDef",
    "ClientDescribeServersResponseServersTypeDef",
    "ClientDescribeServersResponseTypeDef",
    "ClientDisassociateNodeEngineAttributesTypeDef",
    "ClientDisassociateNodeResponseTypeDef",
    "ClientExportServerEngineAttributeInputAttributesTypeDef",
    "ClientExportServerEngineAttributeResponseEngineAttributeTypeDef",
    "ClientExportServerEngineAttributeResponseTypeDef",
    "ClientStartMaintenanceEngineAttributesTypeDef",
    "ClientStartMaintenanceResponseServerEngineAttributesTypeDef",
    "ClientStartMaintenanceResponseServerTypeDef",
    "ClientStartMaintenanceResponseTypeDef",
    "ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef",
    "ClientUpdateServerEngineAttributesResponseServerTypeDef",
    "ClientUpdateServerEngineAttributesResponseTypeDef",
    "ClientUpdateServerResponseServerEngineAttributesTypeDef",
    "ClientUpdateServerResponseServerTypeDef",
    "ClientUpdateServerResponseTypeDef",
    "DescribeBackupsPaginatePaginationConfigTypeDef",
    "DescribeBackupsPaginateResponseBackupsTypeDef",
    "DescribeBackupsPaginateResponseTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseServerEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeServersPaginatePaginationConfigTypeDef",
    "DescribeServersPaginateResponseServersEngineAttributesTypeDef",
    "DescribeServersPaginateResponseServersTypeDef",
    "DescribeServersPaginateResponseTypeDef",
    "NodeAssociatedWaitWaiterConfigTypeDef",
)


_ClientAssociateNodeEngineAttributesTypeDef = TypedDict(
    "_ClientAssociateNodeEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientAssociateNodeEngineAttributesTypeDef(
    _ClientAssociateNodeEngineAttributesTypeDef
):
    """
    Type definition for `ClientAssociateNode` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientAssociateNodeResponseTypeDef = TypedDict(
    "_ClientAssociateNodeResponseTypeDef",
    {"NodeAssociationStatusToken": str},
    total=False,
)


class ClientAssociateNodeResponseTypeDef(_ClientAssociateNodeResponseTypeDef):
    """
    Type definition for `ClientAssociateNode` `Response`

    - **NodeAssociationStatusToken** *(string) --*

      Contains a token which can be passed to the ``DescribeNodeAssociationStatus`` API call to get
      the status of the association request.
    """


_ClientCreateBackupResponseBackupTypeDef = TypedDict(
    "_ClientCreateBackupResponseBackupTypeDef",
    {
        "BackupArn": str,
        "BackupId": str,
        "BackupType": str,
        "CreatedAt": datetime,
        "Description": str,
        "Engine": str,
        "EngineModel": str,
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "S3DataSize": int,
        "S3DataUrl": str,
        "S3LogUrl": str,
        "SecurityGroupIds": List[str],
        "ServerName": str,
        "ServiceRoleArn": str,
        "Status": str,
        "StatusDescription": str,
        "SubnetIds": List[str],
        "ToolsVersion": str,
        "UserArn": str,
    },
    total=False,
)


class ClientCreateBackupResponseBackupTypeDef(_ClientCreateBackupResponseBackupTypeDef):
    """
    Type definition for `ClientCreateBackupResponse` `Backup`

    Backup created by request.

    - **BackupArn** *(string) --*

      The ARN of the backup.

    - **BackupId** *(string) --*

      The generated ID of the backup. Example: ``myServerName-yyyyMMddHHmmssSSS``

    - **BackupType** *(string) --*

      The backup type. Valid values are ``automated`` or ``manual`` .

    - **CreatedAt** *(datetime) --*

      The time stamp when the backup was created in the database. Example:
      ``2016-07-29T13:38:47.520Z``

    - **Description** *(string) --*

      A user-provided description for a manual backup. This field is empty for automated backups.

    - **Engine** *(string) --*

      The engine type that is obtained from the server when the backup is created.

    - **EngineModel** *(string) --*

      The engine model that is obtained from the server when the backup is created.

    - **EngineVersion** *(string) --*

      The engine version that is obtained from the server when the backup is created.

    - **InstanceProfileArn** *(string) --*

      The EC2 instance profile ARN that is obtained from the server when the backup is created.
      Because this value is stored, you are not required to provide the InstanceProfileArn again
      if you restore a backup.

    - **InstanceType** *(string) --*

      The instance type that is obtained from the server when the backup is created.

    - **KeyPair** *(string) --*

      The key pair that is obtained from the server when the backup is created.

    - **PreferredBackupWindow** *(string) --*

      The preferred backup period that is obtained from the server when the backup is created.

    - **PreferredMaintenanceWindow** *(string) --*

      The preferred maintenance period that is obtained from the server when the backup is
      created.

    - **S3DataSize** *(integer) --*

      This field is deprecated and is no longer used.

    - **S3DataUrl** *(string) --*

      This field is deprecated and is no longer used.

    - **S3LogUrl** *(string) --*

      The Amazon S3 URL of the backup's log file.

    - **SecurityGroupIds** *(list) --*

      The security group IDs that are obtained from the server when the backup is created.

      - *(string) --*

    - **ServerName** *(string) --*

      The name of the server from which the backup was made.

    - **ServiceRoleArn** *(string) --*

      The service role ARN that is obtained from the server when the backup is created.

    - **Status** *(string) --*

      The status of a backup while in progress.

    - **StatusDescription** *(string) --*

      An informational message about backup status.

    - **SubnetIds** *(list) --*

      The subnet IDs that are obtained from the server when the backup is created.

      - *(string) --*

    - **ToolsVersion** *(string) --*

      The version of AWS OpsWorks CM-specific tools that is obtained from the server when the
      backup is created.

    - **UserArn** *(string) --*

      The IAM user ARN of the requester for manual backups. This field is empty for automated
      backups.
    """


_ClientCreateBackupResponseTypeDef = TypedDict(
    "_ClientCreateBackupResponseTypeDef",
    {"Backup": ClientCreateBackupResponseBackupTypeDef},
    total=False,
)


class ClientCreateBackupResponseTypeDef(_ClientCreateBackupResponseTypeDef):
    """
    Type definition for `ClientCreateBackup` `Response`

    - **Backup** *(dict) --*

      Backup created by request.

      - **BackupArn** *(string) --*

        The ARN of the backup.

      - **BackupId** *(string) --*

        The generated ID of the backup. Example: ``myServerName-yyyyMMddHHmmssSSS``

      - **BackupType** *(string) --*

        The backup type. Valid values are ``automated`` or ``manual`` .

      - **CreatedAt** *(datetime) --*

        The time stamp when the backup was created in the database. Example:
        ``2016-07-29T13:38:47.520Z``

      - **Description** *(string) --*

        A user-provided description for a manual backup. This field is empty for automated backups.

      - **Engine** *(string) --*

        The engine type that is obtained from the server when the backup is created.

      - **EngineModel** *(string) --*

        The engine model that is obtained from the server when the backup is created.

      - **EngineVersion** *(string) --*

        The engine version that is obtained from the server when the backup is created.

      - **InstanceProfileArn** *(string) --*

        The EC2 instance profile ARN that is obtained from the server when the backup is created.
        Because this value is stored, you are not required to provide the InstanceProfileArn again
        if you restore a backup.

      - **InstanceType** *(string) --*

        The instance type that is obtained from the server when the backup is created.

      - **KeyPair** *(string) --*

        The key pair that is obtained from the server when the backup is created.

      - **PreferredBackupWindow** *(string) --*

        The preferred backup period that is obtained from the server when the backup is created.

      - **PreferredMaintenanceWindow** *(string) --*

        The preferred maintenance period that is obtained from the server when the backup is
        created.

      - **S3DataSize** *(integer) --*

        This field is deprecated and is no longer used.

      - **S3DataUrl** *(string) --*

        This field is deprecated and is no longer used.

      - **S3LogUrl** *(string) --*

        The Amazon S3 URL of the backup's log file.

      - **SecurityGroupIds** *(list) --*

        The security group IDs that are obtained from the server when the backup is created.

        - *(string) --*

      - **ServerName** *(string) --*

        The name of the server from which the backup was made.

      - **ServiceRoleArn** *(string) --*

        The service role ARN that is obtained from the server when the backup is created.

      - **Status** *(string) --*

        The status of a backup while in progress.

      - **StatusDescription** *(string) --*

        An informational message about backup status.

      - **SubnetIds** *(list) --*

        The subnet IDs that are obtained from the server when the backup is created.

        - *(string) --*

      - **ToolsVersion** *(string) --*

        The version of AWS OpsWorks CM-specific tools that is obtained from the server when the
        backup is created.

      - **UserArn** *(string) --*

        The IAM user ARN of the requester for manual backups. This field is empty for automated
        backups.
    """


_ClientCreateServerEngineAttributesTypeDef = TypedDict(
    "_ClientCreateServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateServerEngineAttributesTypeDef(
    _ClientCreateServerEngineAttributesTypeDef
):
    """
    Type definition for `ClientCreateServer` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientCreateServerResponseServerEngineAttributesTypeDef = TypedDict(
    "_ClientCreateServerResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateServerResponseServerEngineAttributesTypeDef(
    _ClientCreateServerResponseServerEngineAttributesTypeDef
):
    """
    Type definition for `ClientCreateServerResponseServer` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientCreateServerResponseServerTypeDef = TypedDict(
    "_ClientCreateServerResponseServerTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[
            ClientCreateServerResponseServerEngineAttributesTypeDef
        ],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": str,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": str,
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)


class ClientCreateServerResponseServerTypeDef(_ClientCreateServerResponseServerTypeDef):
    """
    Type definition for `ClientCreateServerResponse` `Server`

    The server that is created by the request.

    - **AssociatePublicIpAddress** *(boolean) --*

      Associate a public IP address with a server that you are launching.

    - **BackupRetentionCount** *(integer) --*

      The number of automated backups to keep.

    - **ServerName** *(string) --*

      The name of the server.

    - **CreatedAt** *(datetime) --*

      Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

    - **CloudFormationStackArn** *(string) --*

      The ARN of the CloudFormation stack that was used to create the server.

    - **CustomDomain** *(string) --*

      An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
      cannot access the server by using the ``Endpoint`` value if the server has a
      ``CustomDomain`` specified.

    - **DisableAutomatedBackup** *(boolean) --*

      Disables automated backups. The number of stored backups is dependent on the value of
      PreferredBackupCount.

    - **Endpoint** *(string) --*

      A DNS name that can be used to access the engine. Example:
      ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
      ``Endpoint`` value if the server has a ``CustomDomain`` specified.

    - **Engine** *(string) --*

      The engine type of the server. Valid values in this release include ``ChefAutomate`` and
      ``Puppet`` .

    - **EngineModel** *(string) --*

      The engine model of the server. Valid values in this release include ``Monolithic`` for
      Puppet and ``Single`` for Chef.

    - **EngineAttributes** *(list) --*

      The response of a createServer() request returns the master credential to access the server
      in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned
      only as part of the result of createServer().

       **Attributes returned in a createServer response for Chef**

      * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS
      OpsWorks for Chef Automate. This private key is required to access the Chef API.

      * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
      kit, which includes a README, a configuration file, and the required RSA private key. Save
      this file, unzip it, and then change to the directory where you've unzipped the file
      contents. From this directory, you can run Knife commands.

       **Attributes returned in a createServer response for Puppet**

      * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
      starter kit, including a README and a required private key. Save this file, unzip it, and
      then change to the directory where you've unzipped the file contents.

      * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the
      Puppet Enterprise console after the server is online.

      - *(dict) --*

        A name and value pair that is specific to the engine of the server.

        - **Name** *(string) --*

          The name of the engine attribute.

        - **Value** *(string) --*

          The value of the engine attribute.

    - **EngineVersion** *(string) --*

      The engine version of the server. For a Chef server, the valid value for EngineVersion is
      currently ``12`` . For a Puppet server, the valid value is ``2017`` .

    - **InstanceProfileArn** *(string) --*

      The instance profile ARN of the server.

    - **InstanceType** *(string) --*

      The instance type for the server, as specified in the CloudFormation stack. This might not
      be the same instance type that is shown in the EC2 console.

    - **KeyPair** *(string) --*

      The key pair associated with the server.

    - **MaintenanceStatus** *(string) --*

      The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

    - **PreferredMaintenanceWindow** *(string) --*

      The preferred maintenance period specified for the server.

    - **PreferredBackupWindow** *(string) --*

      The preferred backup period specified for the server.

    - **SecurityGroupIds** *(list) --*

      The security group IDs for the server, as specified in the CloudFormation stack. These
      might not be the same security groups that are shown in the EC2 console.

      - *(string) --*

    - **ServiceRoleArn** *(string) --*

      The service role ARN used to create the server.

    - **Status** *(string) --*

      The server's status. This field displays the states of actions in progress, such as
      creating, running, or backing up the server, as well as the server's health state.

    - **StatusReason** *(string) --*

      Depending on the server status, this field has either a human-readable message (such as a
      create or backup error), or an escaped block of JSON (used for health check results).

    - **SubnetIds** *(list) --*

      The subnet IDs specified in a CreateServer request.

      - *(string) --*

    - **ServerArn** *(string) --*

      The ARN of the server.
    """


_ClientCreateServerResponseTypeDef = TypedDict(
    "_ClientCreateServerResponseTypeDef",
    {"Server": ClientCreateServerResponseServerTypeDef},
    total=False,
)


class ClientCreateServerResponseTypeDef(_ClientCreateServerResponseTypeDef):
    """
    Type definition for `ClientCreateServer` `Response`

    - **Server** *(dict) --*

      The server that is created by the request.

      - **AssociatePublicIpAddress** *(boolean) --*

        Associate a public IP address with a server that you are launching.

      - **BackupRetentionCount** *(integer) --*

        The number of automated backups to keep.

      - **ServerName** *(string) --*

        The name of the server.

      - **CreatedAt** *(datetime) --*

        Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

      - **CloudFormationStackArn** *(string) --*

        The ARN of the CloudFormation stack that was used to create the server.

      - **CustomDomain** *(string) --*

        An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
        cannot access the server by using the ``Endpoint`` value if the server has a
        ``CustomDomain`` specified.

      - **DisableAutomatedBackup** *(boolean) --*

        Disables automated backups. The number of stored backups is dependent on the value of
        PreferredBackupCount.

      - **Endpoint** *(string) --*

        A DNS name that can be used to access the engine. Example:
        ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
        ``Endpoint`` value if the server has a ``CustomDomain`` specified.

      - **Engine** *(string) --*

        The engine type of the server. Valid values in this release include ``ChefAutomate`` and
        ``Puppet`` .

      - **EngineModel** *(string) --*

        The engine model of the server. Valid values in this release include ``Monolithic`` for
        Puppet and ``Single`` for Chef.

      - **EngineAttributes** *(list) --*

        The response of a createServer() request returns the master credential to access the server
        in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned
        only as part of the result of createServer().

         **Attributes returned in a createServer response for Chef**

        * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS
        OpsWorks for Chef Automate. This private key is required to access the Chef API.

        * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
        kit, which includes a README, a configuration file, and the required RSA private key. Save
        this file, unzip it, and then change to the directory where you've unzipped the file
        contents. From this directory, you can run Knife commands.

         **Attributes returned in a createServer response for Puppet**

        * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
        starter kit, including a README and a required private key. Save this file, unzip it, and
        then change to the directory where you've unzipped the file contents.

        * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the
        Puppet Enterprise console after the server is online.

        - *(dict) --*

          A name and value pair that is specific to the engine of the server.

          - **Name** *(string) --*

            The name of the engine attribute.

          - **Value** *(string) --*

            The value of the engine attribute.

      - **EngineVersion** *(string) --*

        The engine version of the server. For a Chef server, the valid value for EngineVersion is
        currently ``12`` . For a Puppet server, the valid value is ``2017`` .

      - **InstanceProfileArn** *(string) --*

        The instance profile ARN of the server.

      - **InstanceType** *(string) --*

        The instance type for the server, as specified in the CloudFormation stack. This might not
        be the same instance type that is shown in the EC2 console.

      - **KeyPair** *(string) --*

        The key pair associated with the server.

      - **MaintenanceStatus** *(string) --*

        The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

      - **PreferredMaintenanceWindow** *(string) --*

        The preferred maintenance period specified for the server.

      - **PreferredBackupWindow** *(string) --*

        The preferred backup period specified for the server.

      - **SecurityGroupIds** *(list) --*

        The security group IDs for the server, as specified in the CloudFormation stack. These
        might not be the same security groups that are shown in the EC2 console.

        - *(string) --*

      - **ServiceRoleArn** *(string) --*

        The service role ARN used to create the server.

      - **Status** *(string) --*

        The server's status. This field displays the states of actions in progress, such as
        creating, running, or backing up the server, as well as the server's health state.

      - **StatusReason** *(string) --*

        Depending on the server status, this field has either a human-readable message (such as a
        create or backup error), or an escaped block of JSON (used for health check results).

      - **SubnetIds** *(list) --*

        The subnet IDs specified in a CreateServer request.

        - *(string) --*

      - **ServerArn** *(string) --*

        The ARN of the server.
    """


_ClientDescribeAccountAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseAttributesTypeDef",
    {"Name": str, "Maximum": int, "Used": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseAttributesTypeDef(
    _ClientDescribeAccountAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributesResponse` `Attributes`

    Stores account attributes.

    - **Name** *(string) --*

      The attribute name. The following are supported attribute names.

      * *ServerLimit:* The number of current servers/maximum number of servers allowed. By
      default, you can have a maximum of 10 servers.

      * *ManualBackupLimit:* The number of current manual backups/maximum number of backups
      allowed. By default, you can have a maximum of 50 manual backups saved.

    - **Maximum** *(integer) --*

      The maximum allowed value.

    - **Used** *(integer) --*

      The current usage, such as the current number of servers that are associated with the
      account.
    """


_ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseTypeDef",
    {"Attributes": List[ClientDescribeAccountAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientDescribeAccountAttributesResponseTypeDef(
    _ClientDescribeAccountAttributesResponseTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributes` `Response`

    - **Attributes** *(list) --*

      The attributes that are currently set for the account.

      - *(dict) --*

        Stores account attributes.

        - **Name** *(string) --*

          The attribute name. The following are supported attribute names.

          * *ServerLimit:* The number of current servers/maximum number of servers allowed. By
          default, you can have a maximum of 10 servers.

          * *ManualBackupLimit:* The number of current manual backups/maximum number of backups
          allowed. By default, you can have a maximum of 50 manual backups saved.

        - **Maximum** *(integer) --*

          The maximum allowed value.

        - **Used** *(integer) --*

          The current usage, such as the current number of servers that are associated with the
          account.
    """


_ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseBackupsTypeDef",
    {
        "BackupArn": str,
        "BackupId": str,
        "BackupType": str,
        "CreatedAt": datetime,
        "Description": str,
        "Engine": str,
        "EngineModel": str,
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "S3DataSize": int,
        "S3DataUrl": str,
        "S3LogUrl": str,
        "SecurityGroupIds": List[str],
        "ServerName": str,
        "ServiceRoleArn": str,
        "Status": str,
        "StatusDescription": str,
        "SubnetIds": List[str],
        "ToolsVersion": str,
        "UserArn": str,
    },
    total=False,
)


class ClientDescribeBackupsResponseBackupsTypeDef(
    _ClientDescribeBackupsResponseBackupsTypeDef
):
    """
    Type definition for `ClientDescribeBackupsResponse` `Backups`

    Describes a single backup.

    - **BackupArn** *(string) --*

      The ARN of the backup.

    - **BackupId** *(string) --*

      The generated ID of the backup. Example: ``myServerName-yyyyMMddHHmmssSSS``

    - **BackupType** *(string) --*

      The backup type. Valid values are ``automated`` or ``manual`` .

    - **CreatedAt** *(datetime) --*

      The time stamp when the backup was created in the database. Example:
      ``2016-07-29T13:38:47.520Z``

    - **Description** *(string) --*

      A user-provided description for a manual backup. This field is empty for automated
      backups.

    - **Engine** *(string) --*

      The engine type that is obtained from the server when the backup is created.

    - **EngineModel** *(string) --*

      The engine model that is obtained from the server when the backup is created.

    - **EngineVersion** *(string) --*

      The engine version that is obtained from the server when the backup is created.

    - **InstanceProfileArn** *(string) --*

      The EC2 instance profile ARN that is obtained from the server when the backup is created.
      Because this value is stored, you are not required to provide the InstanceProfileArn
      again if you restore a backup.

    - **InstanceType** *(string) --*

      The instance type that is obtained from the server when the backup is created.

    - **KeyPair** *(string) --*

      The key pair that is obtained from the server when the backup is created.

    - **PreferredBackupWindow** *(string) --*

      The preferred backup period that is obtained from the server when the backup is created.

    - **PreferredMaintenanceWindow** *(string) --*

      The preferred maintenance period that is obtained from the server when the backup is
      created.

    - **S3DataSize** *(integer) --*

      This field is deprecated and is no longer used.

    - **S3DataUrl** *(string) --*

      This field is deprecated and is no longer used.

    - **S3LogUrl** *(string) --*

      The Amazon S3 URL of the backup's log file.

    - **SecurityGroupIds** *(list) --*

      The security group IDs that are obtained from the server when the backup is created.

      - *(string) --*

    - **ServerName** *(string) --*

      The name of the server from which the backup was made.

    - **ServiceRoleArn** *(string) --*

      The service role ARN that is obtained from the server when the backup is created.

    - **Status** *(string) --*

      The status of a backup while in progress.

    - **StatusDescription** *(string) --*

      An informational message about backup status.

    - **SubnetIds** *(list) --*

      The subnet IDs that are obtained from the server when the backup is created.

      - *(string) --*

    - **ToolsVersion** *(string) --*

      The version of AWS OpsWorks CM-specific tools that is obtained from the server when the
      backup is created.

    - **UserArn** *(string) --*

      The IAM user ARN of the requester for manual backups. This field is empty for automated
      backups.
    """


_ClientDescribeBackupsResponseTypeDef = TypedDict(
    "_ClientDescribeBackupsResponseTypeDef",
    {"Backups": List[ClientDescribeBackupsResponseBackupsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeBackupsResponseTypeDef(_ClientDescribeBackupsResponseTypeDef):
    """
    Type definition for `ClientDescribeBackups` `Response`

    - **Backups** *(list) --*

      Contains the response to a ``DescribeBackups`` request.

      - *(dict) --*

        Describes a single backup.

        - **BackupArn** *(string) --*

          The ARN of the backup.

        - **BackupId** *(string) --*

          The generated ID of the backup. Example: ``myServerName-yyyyMMddHHmmssSSS``

        - **BackupType** *(string) --*

          The backup type. Valid values are ``automated`` or ``manual`` .

        - **CreatedAt** *(datetime) --*

          The time stamp when the backup was created in the database. Example:
          ``2016-07-29T13:38:47.520Z``

        - **Description** *(string) --*

          A user-provided description for a manual backup. This field is empty for automated
          backups.

        - **Engine** *(string) --*

          The engine type that is obtained from the server when the backup is created.

        - **EngineModel** *(string) --*

          The engine model that is obtained from the server when the backup is created.

        - **EngineVersion** *(string) --*

          The engine version that is obtained from the server when the backup is created.

        - **InstanceProfileArn** *(string) --*

          The EC2 instance profile ARN that is obtained from the server when the backup is created.
          Because this value is stored, you are not required to provide the InstanceProfileArn
          again if you restore a backup.

        - **InstanceType** *(string) --*

          The instance type that is obtained from the server when the backup is created.

        - **KeyPair** *(string) --*

          The key pair that is obtained from the server when the backup is created.

        - **PreferredBackupWindow** *(string) --*

          The preferred backup period that is obtained from the server when the backup is created.

        - **PreferredMaintenanceWindow** *(string) --*

          The preferred maintenance period that is obtained from the server when the backup is
          created.

        - **S3DataSize** *(integer) --*

          This field is deprecated and is no longer used.

        - **S3DataUrl** *(string) --*

          This field is deprecated and is no longer used.

        - **S3LogUrl** *(string) --*

          The Amazon S3 URL of the backup's log file.

        - **SecurityGroupIds** *(list) --*

          The security group IDs that are obtained from the server when the backup is created.

          - *(string) --*

        - **ServerName** *(string) --*

          The name of the server from which the backup was made.

        - **ServiceRoleArn** *(string) --*

          The service role ARN that is obtained from the server when the backup is created.

        - **Status** *(string) --*

          The status of a backup while in progress.

        - **StatusDescription** *(string) --*

          An informational message about backup status.

        - **SubnetIds** *(list) --*

          The subnet IDs that are obtained from the server when the backup is created.

          - *(string) --*

        - **ToolsVersion** *(string) --*

          The version of AWS OpsWorks CM-specific tools that is obtained from the server when the
          backup is created.

        - **UserArn** *(string) --*

          The IAM user ARN of the requester for manual backups. This field is empty for automated
          backups.

    - **NextToken** *(string) --*

      This is not currently implemented for ``DescribeBackups`` requests.
    """


_ClientDescribeEventsResponseServerEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseServerEventsTypeDef",
    {"CreatedAt": datetime, "ServerName": str, "Message": str, "LogUrl": str},
    total=False,
)


class ClientDescribeEventsResponseServerEventsTypeDef(
    _ClientDescribeEventsResponseServerEventsTypeDef
):
    """
    Type definition for `ClientDescribeEventsResponse` `ServerEvents`

    An event that is related to the server, such as the start of maintenance or backup.

    - **CreatedAt** *(datetime) --*

      The time when the event occurred.

    - **ServerName** *(string) --*

      The name of the server on or for which the event occurred.

    - **Message** *(string) --*

      A human-readable informational or status message.

    - **LogUrl** *(string) --*

      The Amazon S3 URL of the event's log file.
    """


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {
        "ServerEvents": List[ClientDescribeEventsResponseServerEventsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    Type definition for `ClientDescribeEvents` `Response`

    - **ServerEvents** *(list) --*

      Contains the response to a ``DescribeEvents`` request.

      - *(dict) --*

        An event that is related to the server, such as the start of maintenance or backup.

        - **CreatedAt** *(datetime) --*

          The time when the event occurred.

        - **ServerName** *(string) --*

          The name of the server on or for which the event occurred.

        - **Message** *(string) --*

          A human-readable informational or status message.

        - **LogUrl** *(string) --*

          The Amazon S3 URL of the event's log file.

    - **NextToken** *(string) --*

      NextToken is a string that is returned in some command responses. It indicates that not all
      entries have been returned, and that you must run at least one more request to get remaining
      items. To get remaining results, call ``DescribeEvents`` again, and assign the token from the
      previous results as the value of the ``nextToken`` parameter. If there are no more results,
      the response object's ``nextToken`` parameter value is ``null`` . Setting a ``nextToken``
      value that was not returned in your previous results causes an ``InvalidNextTokenException``
      to occur.
    """


_ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef = TypedDict(
    "_ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef(
    _ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef
):
    """
    Type definition for `ClientDescribeNodeAssociationStatusResponse` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientDescribeNodeAssociationStatusResponseTypeDef = TypedDict(
    "_ClientDescribeNodeAssociationStatusResponseTypeDef",
    {
        "NodeAssociationStatus": str,
        "EngineAttributes": List[
            ClientDescribeNodeAssociationStatusResponseEngineAttributesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeNodeAssociationStatusResponseTypeDef(
    _ClientDescribeNodeAssociationStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeNodeAssociationStatus` `Response`

    - **NodeAssociationStatus** *(string) --*

      The status of the association or disassociation request.

       **Possible values:**

      * ``SUCCESS`` : The association or disassociation succeeded.

      * ``FAILED`` : The association or disassociation failed.

      * ``IN_PROGRESS`` : The association or disassociation is still in progress.

    - **EngineAttributes** *(list) --*

      Attributes specific to the node association. In Puppet, the attibute PUPPET_NODE_CERT
      contains the signed certificate (the result of the CSR).

      - *(dict) --*

        A name and value pair that is specific to the engine of the server.

        - **Name** *(string) --*

          The name of the engine attribute.

        - **Value** *(string) --*

          The value of the engine attribute.
    """


_ClientDescribeServersResponseServersEngineAttributesTypeDef = TypedDict(
    "_ClientDescribeServersResponseServersEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeServersResponseServersEngineAttributesTypeDef(
    _ClientDescribeServersResponseServersEngineAttributesTypeDef
):
    """
    Type definition for `ClientDescribeServersResponseServers` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientDescribeServersResponseServersTypeDef = TypedDict(
    "_ClientDescribeServersResponseServersTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[
            ClientDescribeServersResponseServersEngineAttributesTypeDef
        ],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": str,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": str,
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)


class ClientDescribeServersResponseServersTypeDef(
    _ClientDescribeServersResponseServersTypeDef
):
    """
    Type definition for `ClientDescribeServersResponse` `Servers`

    Describes a configuration management server.

    - **AssociatePublicIpAddress** *(boolean) --*

      Associate a public IP address with a server that you are launching.

    - **BackupRetentionCount** *(integer) --*

      The number of automated backups to keep.

    - **ServerName** *(string) --*

      The name of the server.

    - **CreatedAt** *(datetime) --*

      Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

    - **CloudFormationStackArn** *(string) --*

      The ARN of the CloudFormation stack that was used to create the server.

    - **CustomDomain** *(string) --*

      An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
      cannot access the server by using the ``Endpoint`` value if the server has a
      ``CustomDomain`` specified.

    - **DisableAutomatedBackup** *(boolean) --*

      Disables automated backups. The number of stored backups is dependent on the value of
      PreferredBackupCount.

    - **Endpoint** *(string) --*

      A DNS name that can be used to access the engine. Example:
      ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
      ``Endpoint`` value if the server has a ``CustomDomain`` specified.

    - **Engine** *(string) --*

      The engine type of the server. Valid values in this release include ``ChefAutomate`` and
      ``Puppet`` .

    - **EngineModel** *(string) --*

      The engine model of the server. Valid values in this release include ``Monolithic`` for
      Puppet and ``Single`` for Chef.

    - **EngineAttributes** *(list) --*

      The response of a createServer() request returns the master credential to access the
      server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are
      returned only as part of the result of createServer().

       **Attributes returned in a createServer response for Chef**

      * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by
      AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.

      * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
      kit, which includes a README, a configuration file, and the required RSA private key.
      Save this file, unzip it, and then change to the directory where you've unzipped the file
      contents. From this directory, you can run Knife commands.

       **Attributes returned in a createServer response for Puppet**

      * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
      starter kit, including a README and a required private key. Save this file, unzip it, and
      then change to the directory where you've unzipped the file contents.

      * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to
      the Puppet Enterprise console after the server is online.

      - *(dict) --*

        A name and value pair that is specific to the engine of the server.

        - **Name** *(string) --*

          The name of the engine attribute.

        - **Value** *(string) --*

          The value of the engine attribute.

    - **EngineVersion** *(string) --*

      The engine version of the server. For a Chef server, the valid value for EngineVersion is
      currently ``12`` . For a Puppet server, the valid value is ``2017`` .

    - **InstanceProfileArn** *(string) --*

      The instance profile ARN of the server.

    - **InstanceType** *(string) --*

      The instance type for the server, as specified in the CloudFormation stack. This might
      not be the same instance type that is shown in the EC2 console.

    - **KeyPair** *(string) --*

      The key pair associated with the server.

    - **MaintenanceStatus** *(string) --*

      The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

    - **PreferredMaintenanceWindow** *(string) --*

      The preferred maintenance period specified for the server.

    - **PreferredBackupWindow** *(string) --*

      The preferred backup period specified for the server.

    - **SecurityGroupIds** *(list) --*

      The security group IDs for the server, as specified in the CloudFormation stack. These
      might not be the same security groups that are shown in the EC2 console.

      - *(string) --*

    - **ServiceRoleArn** *(string) --*

      The service role ARN used to create the server.

    - **Status** *(string) --*

      The server's status. This field displays the states of actions in progress, such as
      creating, running, or backing up the server, as well as the server's health state.

    - **StatusReason** *(string) --*

      Depending on the server status, this field has either a human-readable message (such as a
      create or backup error), or an escaped block of JSON (used for health check results).

    - **SubnetIds** *(list) --*

      The subnet IDs specified in a CreateServer request.

      - *(string) --*

    - **ServerArn** *(string) --*

      The ARN of the server.
    """


_ClientDescribeServersResponseTypeDef = TypedDict(
    "_ClientDescribeServersResponseTypeDef",
    {"Servers": List[ClientDescribeServersResponseServersTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeServersResponseTypeDef(_ClientDescribeServersResponseTypeDef):
    """
    Type definition for `ClientDescribeServers` `Response`

    - **Servers** *(list) --*

      Contains the response to a ``DescribeServers`` request.

       *For Puppet Server:*  ``DescribeServersResponse$Servers$EngineAttributes`` contains
       PUPPET_API_CA_CERT. This is the PEM-encoded CA certificate that is used by the Puppet API
       over TCP port number 8140. The CA certificate is also used to sign node certificates.

      - *(dict) --*

        Describes a configuration management server.

        - **AssociatePublicIpAddress** *(boolean) --*

          Associate a public IP address with a server that you are launching.

        - **BackupRetentionCount** *(integer) --*

          The number of automated backups to keep.

        - **ServerName** *(string) --*

          The name of the server.

        - **CreatedAt** *(datetime) --*

          Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

        - **CloudFormationStackArn** *(string) --*

          The ARN of the CloudFormation stack that was used to create the server.

        - **CustomDomain** *(string) --*

          An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
          cannot access the server by using the ``Endpoint`` value if the server has a
          ``CustomDomain`` specified.

        - **DisableAutomatedBackup** *(boolean) --*

          Disables automated backups. The number of stored backups is dependent on the value of
          PreferredBackupCount.

        - **Endpoint** *(string) --*

          A DNS name that can be used to access the engine. Example:
          ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
          ``Endpoint`` value if the server has a ``CustomDomain`` specified.

        - **Engine** *(string) --*

          The engine type of the server. Valid values in this release include ``ChefAutomate`` and
          ``Puppet`` .

        - **EngineModel** *(string) --*

          The engine model of the server. Valid values in this release include ``Monolithic`` for
          Puppet and ``Single`` for Chef.

        - **EngineAttributes** *(list) --*

          The response of a createServer() request returns the master credential to access the
          server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are
          returned only as part of the result of createServer().

           **Attributes returned in a createServer response for Chef**

          * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by
          AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.

          * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
          kit, which includes a README, a configuration file, and the required RSA private key.
          Save this file, unzip it, and then change to the directory where you've unzipped the file
          contents. From this directory, you can run Knife commands.

           **Attributes returned in a createServer response for Puppet**

          * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
          starter kit, including a README and a required private key. Save this file, unzip it, and
          then change to the directory where you've unzipped the file contents.

          * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to
          the Puppet Enterprise console after the server is online.

          - *(dict) --*

            A name and value pair that is specific to the engine of the server.

            - **Name** *(string) --*

              The name of the engine attribute.

            - **Value** *(string) --*

              The value of the engine attribute.

        - **EngineVersion** *(string) --*

          The engine version of the server. For a Chef server, the valid value for EngineVersion is
          currently ``12`` . For a Puppet server, the valid value is ``2017`` .

        - **InstanceProfileArn** *(string) --*

          The instance profile ARN of the server.

        - **InstanceType** *(string) --*

          The instance type for the server, as specified in the CloudFormation stack. This might
          not be the same instance type that is shown in the EC2 console.

        - **KeyPair** *(string) --*

          The key pair associated with the server.

        - **MaintenanceStatus** *(string) --*

          The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

        - **PreferredMaintenanceWindow** *(string) --*

          The preferred maintenance period specified for the server.

        - **PreferredBackupWindow** *(string) --*

          The preferred backup period specified for the server.

        - **SecurityGroupIds** *(list) --*

          The security group IDs for the server, as specified in the CloudFormation stack. These
          might not be the same security groups that are shown in the EC2 console.

          - *(string) --*

        - **ServiceRoleArn** *(string) --*

          The service role ARN used to create the server.

        - **Status** *(string) --*

          The server's status. This field displays the states of actions in progress, such as
          creating, running, or backing up the server, as well as the server's health state.

        - **StatusReason** *(string) --*

          Depending on the server status, this field has either a human-readable message (such as a
          create or backup error), or an escaped block of JSON (used for health check results).

        - **SubnetIds** *(list) --*

          The subnet IDs specified in a CreateServer request.

          - *(string) --*

        - **ServerArn** *(string) --*

          The ARN of the server.

    - **NextToken** *(string) --*

      This is not currently implemented for ``DescribeServers`` requests.
    """


_ClientDisassociateNodeEngineAttributesTypeDef = TypedDict(
    "_ClientDisassociateNodeEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDisassociateNodeEngineAttributesTypeDef(
    _ClientDisassociateNodeEngineAttributesTypeDef
):
    """
    Type definition for `ClientDisassociateNode` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientDisassociateNodeResponseTypeDef = TypedDict(
    "_ClientDisassociateNodeResponseTypeDef",
    {"NodeAssociationStatusToken": str},
    total=False,
)


class ClientDisassociateNodeResponseTypeDef(_ClientDisassociateNodeResponseTypeDef):
    """
    Type definition for `ClientDisassociateNode` `Response`

    - **NodeAssociationStatusToken** *(string) --*

      Contains a token which can be passed to the ``DescribeNodeAssociationStatus`` API call to get
      the status of the disassociation request.
    """


_ClientExportServerEngineAttributeInputAttributesTypeDef = TypedDict(
    "_ClientExportServerEngineAttributeInputAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientExportServerEngineAttributeInputAttributesTypeDef(
    _ClientExportServerEngineAttributeInputAttributesTypeDef
):
    """
    Type definition for `ClientExportServerEngineAttribute` `InputAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientExportServerEngineAttributeResponseEngineAttributeTypeDef = TypedDict(
    "_ClientExportServerEngineAttributeResponseEngineAttributeTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientExportServerEngineAttributeResponseEngineAttributeTypeDef(
    _ClientExportServerEngineAttributeResponseEngineAttributeTypeDef
):
    """
    Type definition for `ClientExportServerEngineAttributeResponse` `EngineAttribute`

    The requested engine attribute pair with attribute name and value.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientExportServerEngineAttributeResponseTypeDef = TypedDict(
    "_ClientExportServerEngineAttributeResponseTypeDef",
    {
        "EngineAttribute": ClientExportServerEngineAttributeResponseEngineAttributeTypeDef,
        "ServerName": str,
    },
    total=False,
)


class ClientExportServerEngineAttributeResponseTypeDef(
    _ClientExportServerEngineAttributeResponseTypeDef
):
    """
    Type definition for `ClientExportServerEngineAttribute` `Response`

    - **EngineAttribute** *(dict) --*

      The requested engine attribute pair with attribute name and value.

      - **Name** *(string) --*

        The name of the engine attribute.

      - **Value** *(string) --*

        The value of the engine attribute.

    - **ServerName** *(string) --*

      The server name used in the request.
    """


_ClientStartMaintenanceEngineAttributesTypeDef = TypedDict(
    "_ClientStartMaintenanceEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientStartMaintenanceEngineAttributesTypeDef(
    _ClientStartMaintenanceEngineAttributesTypeDef
):
    """
    Type definition for `ClientStartMaintenance` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientStartMaintenanceResponseServerEngineAttributesTypeDef = TypedDict(
    "_ClientStartMaintenanceResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientStartMaintenanceResponseServerEngineAttributesTypeDef(
    _ClientStartMaintenanceResponseServerEngineAttributesTypeDef
):
    """
    Type definition for `ClientStartMaintenanceResponseServer` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientStartMaintenanceResponseServerTypeDef = TypedDict(
    "_ClientStartMaintenanceResponseServerTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[
            ClientStartMaintenanceResponseServerEngineAttributesTypeDef
        ],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": str,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": str,
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)


class ClientStartMaintenanceResponseServerTypeDef(
    _ClientStartMaintenanceResponseServerTypeDef
):
    """
    Type definition for `ClientStartMaintenanceResponse` `Server`

    Contains the response to a ``StartMaintenance`` request.

    - **AssociatePublicIpAddress** *(boolean) --*

      Associate a public IP address with a server that you are launching.

    - **BackupRetentionCount** *(integer) --*

      The number of automated backups to keep.

    - **ServerName** *(string) --*

      The name of the server.

    - **CreatedAt** *(datetime) --*

      Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

    - **CloudFormationStackArn** *(string) --*

      The ARN of the CloudFormation stack that was used to create the server.

    - **CustomDomain** *(string) --*

      An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
      cannot access the server by using the ``Endpoint`` value if the server has a
      ``CustomDomain`` specified.

    - **DisableAutomatedBackup** *(boolean) --*

      Disables automated backups. The number of stored backups is dependent on the value of
      PreferredBackupCount.

    - **Endpoint** *(string) --*

      A DNS name that can be used to access the engine. Example:
      ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
      ``Endpoint`` value if the server has a ``CustomDomain`` specified.

    - **Engine** *(string) --*

      The engine type of the server. Valid values in this release include ``ChefAutomate`` and
      ``Puppet`` .

    - **EngineModel** *(string) --*

      The engine model of the server. Valid values in this release include ``Monolithic`` for
      Puppet and ``Single`` for Chef.

    - **EngineAttributes** *(list) --*

      The response of a createServer() request returns the master credential to access the server
      in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned
      only as part of the result of createServer().

       **Attributes returned in a createServer response for Chef**

      * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS
      OpsWorks for Chef Automate. This private key is required to access the Chef API.

      * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
      kit, which includes a README, a configuration file, and the required RSA private key. Save
      this file, unzip it, and then change to the directory where you've unzipped the file
      contents. From this directory, you can run Knife commands.

       **Attributes returned in a createServer response for Puppet**

      * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
      starter kit, including a README and a required private key. Save this file, unzip it, and
      then change to the directory where you've unzipped the file contents.

      * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the
      Puppet Enterprise console after the server is online.

      - *(dict) --*

        A name and value pair that is specific to the engine of the server.

        - **Name** *(string) --*

          The name of the engine attribute.

        - **Value** *(string) --*

          The value of the engine attribute.

    - **EngineVersion** *(string) --*

      The engine version of the server. For a Chef server, the valid value for EngineVersion is
      currently ``12`` . For a Puppet server, the valid value is ``2017`` .

    - **InstanceProfileArn** *(string) --*

      The instance profile ARN of the server.

    - **InstanceType** *(string) --*

      The instance type for the server, as specified in the CloudFormation stack. This might not
      be the same instance type that is shown in the EC2 console.

    - **KeyPair** *(string) --*

      The key pair associated with the server.

    - **MaintenanceStatus** *(string) --*

      The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

    - **PreferredMaintenanceWindow** *(string) --*

      The preferred maintenance period specified for the server.

    - **PreferredBackupWindow** *(string) --*

      The preferred backup period specified for the server.

    - **SecurityGroupIds** *(list) --*

      The security group IDs for the server, as specified in the CloudFormation stack. These
      might not be the same security groups that are shown in the EC2 console.

      - *(string) --*

    - **ServiceRoleArn** *(string) --*

      The service role ARN used to create the server.

    - **Status** *(string) --*

      The server's status. This field displays the states of actions in progress, such as
      creating, running, or backing up the server, as well as the server's health state.

    - **StatusReason** *(string) --*

      Depending on the server status, this field has either a human-readable message (such as a
      create or backup error), or an escaped block of JSON (used for health check results).

    - **SubnetIds** *(list) --*

      The subnet IDs specified in a CreateServer request.

      - *(string) --*

    - **ServerArn** *(string) --*

      The ARN of the server.
    """


_ClientStartMaintenanceResponseTypeDef = TypedDict(
    "_ClientStartMaintenanceResponseTypeDef",
    {"Server": ClientStartMaintenanceResponseServerTypeDef},
    total=False,
)


class ClientStartMaintenanceResponseTypeDef(_ClientStartMaintenanceResponseTypeDef):
    """
    Type definition for `ClientStartMaintenance` `Response`

    - **Server** *(dict) --*

      Contains the response to a ``StartMaintenance`` request.

      - **AssociatePublicIpAddress** *(boolean) --*

        Associate a public IP address with a server that you are launching.

      - **BackupRetentionCount** *(integer) --*

        The number of automated backups to keep.

      - **ServerName** *(string) --*

        The name of the server.

      - **CreatedAt** *(datetime) --*

        Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

      - **CloudFormationStackArn** *(string) --*

        The ARN of the CloudFormation stack that was used to create the server.

      - **CustomDomain** *(string) --*

        An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
        cannot access the server by using the ``Endpoint`` value if the server has a
        ``CustomDomain`` specified.

      - **DisableAutomatedBackup** *(boolean) --*

        Disables automated backups. The number of stored backups is dependent on the value of
        PreferredBackupCount.

      - **Endpoint** *(string) --*

        A DNS name that can be used to access the engine. Example:
        ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
        ``Endpoint`` value if the server has a ``CustomDomain`` specified.

      - **Engine** *(string) --*

        The engine type of the server. Valid values in this release include ``ChefAutomate`` and
        ``Puppet`` .

      - **EngineModel** *(string) --*

        The engine model of the server. Valid values in this release include ``Monolithic`` for
        Puppet and ``Single`` for Chef.

      - **EngineAttributes** *(list) --*

        The response of a createServer() request returns the master credential to access the server
        in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned
        only as part of the result of createServer().

         **Attributes returned in a createServer response for Chef**

        * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS
        OpsWorks for Chef Automate. This private key is required to access the Chef API.

        * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
        kit, which includes a README, a configuration file, and the required RSA private key. Save
        this file, unzip it, and then change to the directory where you've unzipped the file
        contents. From this directory, you can run Knife commands.

         **Attributes returned in a createServer response for Puppet**

        * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
        starter kit, including a README and a required private key. Save this file, unzip it, and
        then change to the directory where you've unzipped the file contents.

        * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the
        Puppet Enterprise console after the server is online.

        - *(dict) --*

          A name and value pair that is specific to the engine of the server.

          - **Name** *(string) --*

            The name of the engine attribute.

          - **Value** *(string) --*

            The value of the engine attribute.

      - **EngineVersion** *(string) --*

        The engine version of the server. For a Chef server, the valid value for EngineVersion is
        currently ``12`` . For a Puppet server, the valid value is ``2017`` .

      - **InstanceProfileArn** *(string) --*

        The instance profile ARN of the server.

      - **InstanceType** *(string) --*

        The instance type for the server, as specified in the CloudFormation stack. This might not
        be the same instance type that is shown in the EC2 console.

      - **KeyPair** *(string) --*

        The key pair associated with the server.

      - **MaintenanceStatus** *(string) --*

        The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

      - **PreferredMaintenanceWindow** *(string) --*

        The preferred maintenance period specified for the server.

      - **PreferredBackupWindow** *(string) --*

        The preferred backup period specified for the server.

      - **SecurityGroupIds** *(list) --*

        The security group IDs for the server, as specified in the CloudFormation stack. These
        might not be the same security groups that are shown in the EC2 console.

        - *(string) --*

      - **ServiceRoleArn** *(string) --*

        The service role ARN used to create the server.

      - **Status** *(string) --*

        The server's status. This field displays the states of actions in progress, such as
        creating, running, or backing up the server, as well as the server's health state.

      - **StatusReason** *(string) --*

        Depending on the server status, this field has either a human-readable message (such as a
        create or backup error), or an escaped block of JSON (used for health check results).

      - **SubnetIds** *(list) --*

        The subnet IDs specified in a CreateServer request.

        - *(string) --*

      - **ServerArn** *(string) --*

        The ARN of the server.
    """


_ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef = TypedDict(
    "_ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef(
    _ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef
):
    """
    Type definition for `ClientUpdateServerEngineAttributesResponseServer` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientUpdateServerEngineAttributesResponseServerTypeDef = TypedDict(
    "_ClientUpdateServerEngineAttributesResponseServerTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[
            ClientUpdateServerEngineAttributesResponseServerEngineAttributesTypeDef
        ],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": str,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": str,
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)


class ClientUpdateServerEngineAttributesResponseServerTypeDef(
    _ClientUpdateServerEngineAttributesResponseServerTypeDef
):
    """
    Type definition for `ClientUpdateServerEngineAttributesResponse` `Server`

    Contains the response to an ``UpdateServerEngineAttributes`` request.

    - **AssociatePublicIpAddress** *(boolean) --*

      Associate a public IP address with a server that you are launching.

    - **BackupRetentionCount** *(integer) --*

      The number of automated backups to keep.

    - **ServerName** *(string) --*

      The name of the server.

    - **CreatedAt** *(datetime) --*

      Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

    - **CloudFormationStackArn** *(string) --*

      The ARN of the CloudFormation stack that was used to create the server.

    - **CustomDomain** *(string) --*

      An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
      cannot access the server by using the ``Endpoint`` value if the server has a
      ``CustomDomain`` specified.

    - **DisableAutomatedBackup** *(boolean) --*

      Disables automated backups. The number of stored backups is dependent on the value of
      PreferredBackupCount.

    - **Endpoint** *(string) --*

      A DNS name that can be used to access the engine. Example:
      ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
      ``Endpoint`` value if the server has a ``CustomDomain`` specified.

    - **Engine** *(string) --*

      The engine type of the server. Valid values in this release include ``ChefAutomate`` and
      ``Puppet`` .

    - **EngineModel** *(string) --*

      The engine model of the server. Valid values in this release include ``Monolithic`` for
      Puppet and ``Single`` for Chef.

    - **EngineAttributes** *(list) --*

      The response of a createServer() request returns the master credential to access the server
      in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned
      only as part of the result of createServer().

       **Attributes returned in a createServer response for Chef**

      * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS
      OpsWorks for Chef Automate. This private key is required to access the Chef API.

      * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
      kit, which includes a README, a configuration file, and the required RSA private key. Save
      this file, unzip it, and then change to the directory where you've unzipped the file
      contents. From this directory, you can run Knife commands.

       **Attributes returned in a createServer response for Puppet**

      * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
      starter kit, including a README and a required private key. Save this file, unzip it, and
      then change to the directory where you've unzipped the file contents.

      * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the
      Puppet Enterprise console after the server is online.

      - *(dict) --*

        A name and value pair that is specific to the engine of the server.

        - **Name** *(string) --*

          The name of the engine attribute.

        - **Value** *(string) --*

          The value of the engine attribute.

    - **EngineVersion** *(string) --*

      The engine version of the server. For a Chef server, the valid value for EngineVersion is
      currently ``12`` . For a Puppet server, the valid value is ``2017`` .

    - **InstanceProfileArn** *(string) --*

      The instance profile ARN of the server.

    - **InstanceType** *(string) --*

      The instance type for the server, as specified in the CloudFormation stack. This might not
      be the same instance type that is shown in the EC2 console.

    - **KeyPair** *(string) --*

      The key pair associated with the server.

    - **MaintenanceStatus** *(string) --*

      The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

    - **PreferredMaintenanceWindow** *(string) --*

      The preferred maintenance period specified for the server.

    - **PreferredBackupWindow** *(string) --*

      The preferred backup period specified for the server.

    - **SecurityGroupIds** *(list) --*

      The security group IDs for the server, as specified in the CloudFormation stack. These
      might not be the same security groups that are shown in the EC2 console.

      - *(string) --*

    - **ServiceRoleArn** *(string) --*

      The service role ARN used to create the server.

    - **Status** *(string) --*

      The server's status. This field displays the states of actions in progress, such as
      creating, running, or backing up the server, as well as the server's health state.

    - **StatusReason** *(string) --*

      Depending on the server status, this field has either a human-readable message (such as a
      create or backup error), or an escaped block of JSON (used for health check results).

    - **SubnetIds** *(list) --*

      The subnet IDs specified in a CreateServer request.

      - *(string) --*

    - **ServerArn** *(string) --*

      The ARN of the server.
    """


_ClientUpdateServerEngineAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateServerEngineAttributesResponseTypeDef",
    {"Server": ClientUpdateServerEngineAttributesResponseServerTypeDef},
    total=False,
)


class ClientUpdateServerEngineAttributesResponseTypeDef(
    _ClientUpdateServerEngineAttributesResponseTypeDef
):
    """
    Type definition for `ClientUpdateServerEngineAttributes` `Response`

    - **Server** *(dict) --*

      Contains the response to an ``UpdateServerEngineAttributes`` request.

      - **AssociatePublicIpAddress** *(boolean) --*

        Associate a public IP address with a server that you are launching.

      - **BackupRetentionCount** *(integer) --*

        The number of automated backups to keep.

      - **ServerName** *(string) --*

        The name of the server.

      - **CreatedAt** *(datetime) --*

        Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

      - **CloudFormationStackArn** *(string) --*

        The ARN of the CloudFormation stack that was used to create the server.

      - **CustomDomain** *(string) --*

        An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
        cannot access the server by using the ``Endpoint`` value if the server has a
        ``CustomDomain`` specified.

      - **DisableAutomatedBackup** *(boolean) --*

        Disables automated backups. The number of stored backups is dependent on the value of
        PreferredBackupCount.

      - **Endpoint** *(string) --*

        A DNS name that can be used to access the engine. Example:
        ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
        ``Endpoint`` value if the server has a ``CustomDomain`` specified.

      - **Engine** *(string) --*

        The engine type of the server. Valid values in this release include ``ChefAutomate`` and
        ``Puppet`` .

      - **EngineModel** *(string) --*

        The engine model of the server. Valid values in this release include ``Monolithic`` for
        Puppet and ``Single`` for Chef.

      - **EngineAttributes** *(list) --*

        The response of a createServer() request returns the master credential to access the server
        in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned
        only as part of the result of createServer().

         **Attributes returned in a createServer response for Chef**

        * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS
        OpsWorks for Chef Automate. This private key is required to access the Chef API.

        * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
        kit, which includes a README, a configuration file, and the required RSA private key. Save
        this file, unzip it, and then change to the directory where you've unzipped the file
        contents. From this directory, you can run Knife commands.

         **Attributes returned in a createServer response for Puppet**

        * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
        starter kit, including a README and a required private key. Save this file, unzip it, and
        then change to the directory where you've unzipped the file contents.

        * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the
        Puppet Enterprise console after the server is online.

        - *(dict) --*

          A name and value pair that is specific to the engine of the server.

          - **Name** *(string) --*

            The name of the engine attribute.

          - **Value** *(string) --*

            The value of the engine attribute.

      - **EngineVersion** *(string) --*

        The engine version of the server. For a Chef server, the valid value for EngineVersion is
        currently ``12`` . For a Puppet server, the valid value is ``2017`` .

      - **InstanceProfileArn** *(string) --*

        The instance profile ARN of the server.

      - **InstanceType** *(string) --*

        The instance type for the server, as specified in the CloudFormation stack. This might not
        be the same instance type that is shown in the EC2 console.

      - **KeyPair** *(string) --*

        The key pair associated with the server.

      - **MaintenanceStatus** *(string) --*

        The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

      - **PreferredMaintenanceWindow** *(string) --*

        The preferred maintenance period specified for the server.

      - **PreferredBackupWindow** *(string) --*

        The preferred backup period specified for the server.

      - **SecurityGroupIds** *(list) --*

        The security group IDs for the server, as specified in the CloudFormation stack. These
        might not be the same security groups that are shown in the EC2 console.

        - *(string) --*

      - **ServiceRoleArn** *(string) --*

        The service role ARN used to create the server.

      - **Status** *(string) --*

        The server's status. This field displays the states of actions in progress, such as
        creating, running, or backing up the server, as well as the server's health state.

      - **StatusReason** *(string) --*

        Depending on the server status, this field has either a human-readable message (such as a
        create or backup error), or an escaped block of JSON (used for health check results).

      - **SubnetIds** *(list) --*

        The subnet IDs specified in a CreateServer request.

        - *(string) --*

      - **ServerArn** *(string) --*

        The ARN of the server.
    """


_ClientUpdateServerResponseServerEngineAttributesTypeDef = TypedDict(
    "_ClientUpdateServerResponseServerEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientUpdateServerResponseServerEngineAttributesTypeDef(
    _ClientUpdateServerResponseServerEngineAttributesTypeDef
):
    """
    Type definition for `ClientUpdateServerResponseServer` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_ClientUpdateServerResponseServerTypeDef = TypedDict(
    "_ClientUpdateServerResponseServerTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[
            ClientUpdateServerResponseServerEngineAttributesTypeDef
        ],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": str,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": str,
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)


class ClientUpdateServerResponseServerTypeDef(_ClientUpdateServerResponseServerTypeDef):
    """
    Type definition for `ClientUpdateServerResponse` `Server`

    Contains the response to a ``UpdateServer`` request.

    - **AssociatePublicIpAddress** *(boolean) --*

      Associate a public IP address with a server that you are launching.

    - **BackupRetentionCount** *(integer) --*

      The number of automated backups to keep.

    - **ServerName** *(string) --*

      The name of the server.

    - **CreatedAt** *(datetime) --*

      Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

    - **CloudFormationStackArn** *(string) --*

      The ARN of the CloudFormation stack that was used to create the server.

    - **CustomDomain** *(string) --*

      An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
      cannot access the server by using the ``Endpoint`` value if the server has a
      ``CustomDomain`` specified.

    - **DisableAutomatedBackup** *(boolean) --*

      Disables automated backups. The number of stored backups is dependent on the value of
      PreferredBackupCount.

    - **Endpoint** *(string) --*

      A DNS name that can be used to access the engine. Example:
      ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
      ``Endpoint`` value if the server has a ``CustomDomain`` specified.

    - **Engine** *(string) --*

      The engine type of the server. Valid values in this release include ``ChefAutomate`` and
      ``Puppet`` .

    - **EngineModel** *(string) --*

      The engine model of the server. Valid values in this release include ``Monolithic`` for
      Puppet and ``Single`` for Chef.

    - **EngineAttributes** *(list) --*

      The response of a createServer() request returns the master credential to access the server
      in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned
      only as part of the result of createServer().

       **Attributes returned in a createServer response for Chef**

      * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS
      OpsWorks for Chef Automate. This private key is required to access the Chef API.

      * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
      kit, which includes a README, a configuration file, and the required RSA private key. Save
      this file, unzip it, and then change to the directory where you've unzipped the file
      contents. From this directory, you can run Knife commands.

       **Attributes returned in a createServer response for Puppet**

      * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
      starter kit, including a README and a required private key. Save this file, unzip it, and
      then change to the directory where you've unzipped the file contents.

      * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the
      Puppet Enterprise console after the server is online.

      - *(dict) --*

        A name and value pair that is specific to the engine of the server.

        - **Name** *(string) --*

          The name of the engine attribute.

        - **Value** *(string) --*

          The value of the engine attribute.

    - **EngineVersion** *(string) --*

      The engine version of the server. For a Chef server, the valid value for EngineVersion is
      currently ``12`` . For a Puppet server, the valid value is ``2017`` .

    - **InstanceProfileArn** *(string) --*

      The instance profile ARN of the server.

    - **InstanceType** *(string) --*

      The instance type for the server, as specified in the CloudFormation stack. This might not
      be the same instance type that is shown in the EC2 console.

    - **KeyPair** *(string) --*

      The key pair associated with the server.

    - **MaintenanceStatus** *(string) --*

      The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

    - **PreferredMaintenanceWindow** *(string) --*

      The preferred maintenance period specified for the server.

    - **PreferredBackupWindow** *(string) --*

      The preferred backup period specified for the server.

    - **SecurityGroupIds** *(list) --*

      The security group IDs for the server, as specified in the CloudFormation stack. These
      might not be the same security groups that are shown in the EC2 console.

      - *(string) --*

    - **ServiceRoleArn** *(string) --*

      The service role ARN used to create the server.

    - **Status** *(string) --*

      The server's status. This field displays the states of actions in progress, such as
      creating, running, or backing up the server, as well as the server's health state.

    - **StatusReason** *(string) --*

      Depending on the server status, this field has either a human-readable message (such as a
      create or backup error), or an escaped block of JSON (used for health check results).

    - **SubnetIds** *(list) --*

      The subnet IDs specified in a CreateServer request.

      - *(string) --*

    - **ServerArn** *(string) --*

      The ARN of the server.
    """


_ClientUpdateServerResponseTypeDef = TypedDict(
    "_ClientUpdateServerResponseTypeDef",
    {"Server": ClientUpdateServerResponseServerTypeDef},
    total=False,
)


class ClientUpdateServerResponseTypeDef(_ClientUpdateServerResponseTypeDef):
    """
    Type definition for `ClientUpdateServer` `Response`

    - **Server** *(dict) --*

      Contains the response to a ``UpdateServer`` request.

      - **AssociatePublicIpAddress** *(boolean) --*

        Associate a public IP address with a server that you are launching.

      - **BackupRetentionCount** *(integer) --*

        The number of automated backups to keep.

      - **ServerName** *(string) --*

        The name of the server.

      - **CreatedAt** *(datetime) --*

        Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

      - **CloudFormationStackArn** *(string) --*

        The ARN of the CloudFormation stack that was used to create the server.

      - **CustomDomain** *(string) --*

        An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
        cannot access the server by using the ``Endpoint`` value if the server has a
        ``CustomDomain`` specified.

      - **DisableAutomatedBackup** *(boolean) --*

        Disables automated backups. The number of stored backups is dependent on the value of
        PreferredBackupCount.

      - **Endpoint** *(string) --*

        A DNS name that can be used to access the engine. Example:
        ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
        ``Endpoint`` value if the server has a ``CustomDomain`` specified.

      - **Engine** *(string) --*

        The engine type of the server. Valid values in this release include ``ChefAutomate`` and
        ``Puppet`` .

      - **EngineModel** *(string) --*

        The engine model of the server. Valid values in this release include ``Monolithic`` for
        Puppet and ``Single`` for Chef.

      - **EngineAttributes** *(list) --*

        The response of a createServer() request returns the master credential to access the server
        in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned
        only as part of the result of createServer().

         **Attributes returned in a createServer response for Chef**

        * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS
        OpsWorks for Chef Automate. This private key is required to access the Chef API.

        * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
        kit, which includes a README, a configuration file, and the required RSA private key. Save
        this file, unzip it, and then change to the directory where you've unzipped the file
        contents. From this directory, you can run Knife commands.

         **Attributes returned in a createServer response for Puppet**

        * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
        starter kit, including a README and a required private key. Save this file, unzip it, and
        then change to the directory where you've unzipped the file contents.

        * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the
        Puppet Enterprise console after the server is online.

        - *(dict) --*

          A name and value pair that is specific to the engine of the server.

          - **Name** *(string) --*

            The name of the engine attribute.

          - **Value** *(string) --*

            The value of the engine attribute.

      - **EngineVersion** *(string) --*

        The engine version of the server. For a Chef server, the valid value for EngineVersion is
        currently ``12`` . For a Puppet server, the valid value is ``2017`` .

      - **InstanceProfileArn** *(string) --*

        The instance profile ARN of the server.

      - **InstanceType** *(string) --*

        The instance type for the server, as specified in the CloudFormation stack. This might not
        be the same instance type that is shown in the EC2 console.

      - **KeyPair** *(string) --*

        The key pair associated with the server.

      - **MaintenanceStatus** *(string) --*

        The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

      - **PreferredMaintenanceWindow** *(string) --*

        The preferred maintenance period specified for the server.

      - **PreferredBackupWindow** *(string) --*

        The preferred backup period specified for the server.

      - **SecurityGroupIds** *(list) --*

        The security group IDs for the server, as specified in the CloudFormation stack. These
        might not be the same security groups that are shown in the EC2 console.

        - *(string) --*

      - **ServiceRoleArn** *(string) --*

        The service role ARN used to create the server.

      - **Status** *(string) --*

        The server's status. This field displays the states of actions in progress, such as
        creating, running, or backing up the server, as well as the server's health state.

      - **StatusReason** *(string) --*

        Depending on the server status, this field has either a human-readable message (such as a
        create or backup error), or an escaped block of JSON (used for health check results).

      - **SubnetIds** *(list) --*

        The subnet IDs specified in a CreateServer request.

        - *(string) --*

      - **ServerArn** *(string) --*

        The ARN of the server.
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


_DescribeBackupsPaginateResponseBackupsTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseBackupsTypeDef",
    {
        "BackupArn": str,
        "BackupId": str,
        "BackupType": str,
        "CreatedAt": datetime,
        "Description": str,
        "Engine": str,
        "EngineModel": str,
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "S3DataSize": int,
        "S3DataUrl": str,
        "S3LogUrl": str,
        "SecurityGroupIds": List[str],
        "ServerName": str,
        "ServiceRoleArn": str,
        "Status": str,
        "StatusDescription": str,
        "SubnetIds": List[str],
        "ToolsVersion": str,
        "UserArn": str,
    },
    total=False,
)


class DescribeBackupsPaginateResponseBackupsTypeDef(
    _DescribeBackupsPaginateResponseBackupsTypeDef
):
    """
    Type definition for `DescribeBackupsPaginateResponse` `Backups`

    Describes a single backup.

    - **BackupArn** *(string) --*

      The ARN of the backup.

    - **BackupId** *(string) --*

      The generated ID of the backup. Example: ``myServerName-yyyyMMddHHmmssSSS``

    - **BackupType** *(string) --*

      The backup type. Valid values are ``automated`` or ``manual`` .

    - **CreatedAt** *(datetime) --*

      The time stamp when the backup was created in the database. Example:
      ``2016-07-29T13:38:47.520Z``

    - **Description** *(string) --*

      A user-provided description for a manual backup. This field is empty for automated
      backups.

    - **Engine** *(string) --*

      The engine type that is obtained from the server when the backup is created.

    - **EngineModel** *(string) --*

      The engine model that is obtained from the server when the backup is created.

    - **EngineVersion** *(string) --*

      The engine version that is obtained from the server when the backup is created.

    - **InstanceProfileArn** *(string) --*

      The EC2 instance profile ARN that is obtained from the server when the backup is created.
      Because this value is stored, you are not required to provide the InstanceProfileArn
      again if you restore a backup.

    - **InstanceType** *(string) --*

      The instance type that is obtained from the server when the backup is created.

    - **KeyPair** *(string) --*

      The key pair that is obtained from the server when the backup is created.

    - **PreferredBackupWindow** *(string) --*

      The preferred backup period that is obtained from the server when the backup is created.

    - **PreferredMaintenanceWindow** *(string) --*

      The preferred maintenance period that is obtained from the server when the backup is
      created.

    - **S3DataSize** *(integer) --*

      This field is deprecated and is no longer used.

    - **S3DataUrl** *(string) --*

      This field is deprecated and is no longer used.

    - **S3LogUrl** *(string) --*

      The Amazon S3 URL of the backup's log file.

    - **SecurityGroupIds** *(list) --*

      The security group IDs that are obtained from the server when the backup is created.

      - *(string) --*

    - **ServerName** *(string) --*

      The name of the server from which the backup was made.

    - **ServiceRoleArn** *(string) --*

      The service role ARN that is obtained from the server when the backup is created.

    - **Status** *(string) --*

      The status of a backup while in progress.

    - **StatusDescription** *(string) --*

      An informational message about backup status.

    - **SubnetIds** *(list) --*

      The subnet IDs that are obtained from the server when the backup is created.

      - *(string) --*

    - **ToolsVersion** *(string) --*

      The version of AWS OpsWorks CM-specific tools that is obtained from the server when the
      backup is created.

    - **UserArn** *(string) --*

      The IAM user ARN of the requester for manual backups. This field is empty for automated
      backups.
    """


_DescribeBackupsPaginateResponseTypeDef = TypedDict(
    "_DescribeBackupsPaginateResponseTypeDef",
    {"Backups": List[DescribeBackupsPaginateResponseBackupsTypeDef]},
    total=False,
)


class DescribeBackupsPaginateResponseTypeDef(_DescribeBackupsPaginateResponseTypeDef):
    """
    Type definition for `DescribeBackupsPaginate` `Response`

    - **Backups** *(list) --*

      Contains the response to a ``DescribeBackups`` request.

      - *(dict) --*

        Describes a single backup.

        - **BackupArn** *(string) --*

          The ARN of the backup.

        - **BackupId** *(string) --*

          The generated ID of the backup. Example: ``myServerName-yyyyMMddHHmmssSSS``

        - **BackupType** *(string) --*

          The backup type. Valid values are ``automated`` or ``manual`` .

        - **CreatedAt** *(datetime) --*

          The time stamp when the backup was created in the database. Example:
          ``2016-07-29T13:38:47.520Z``

        - **Description** *(string) --*

          A user-provided description for a manual backup. This field is empty for automated
          backups.

        - **Engine** *(string) --*

          The engine type that is obtained from the server when the backup is created.

        - **EngineModel** *(string) --*

          The engine model that is obtained from the server when the backup is created.

        - **EngineVersion** *(string) --*

          The engine version that is obtained from the server when the backup is created.

        - **InstanceProfileArn** *(string) --*

          The EC2 instance profile ARN that is obtained from the server when the backup is created.
          Because this value is stored, you are not required to provide the InstanceProfileArn
          again if you restore a backup.

        - **InstanceType** *(string) --*

          The instance type that is obtained from the server when the backup is created.

        - **KeyPair** *(string) --*

          The key pair that is obtained from the server when the backup is created.

        - **PreferredBackupWindow** *(string) --*

          The preferred backup period that is obtained from the server when the backup is created.

        - **PreferredMaintenanceWindow** *(string) --*

          The preferred maintenance period that is obtained from the server when the backup is
          created.

        - **S3DataSize** *(integer) --*

          This field is deprecated and is no longer used.

        - **S3DataUrl** *(string) --*

          This field is deprecated and is no longer used.

        - **S3LogUrl** *(string) --*

          The Amazon S3 URL of the backup's log file.

        - **SecurityGroupIds** *(list) --*

          The security group IDs that are obtained from the server when the backup is created.

          - *(string) --*

        - **ServerName** *(string) --*

          The name of the server from which the backup was made.

        - **ServiceRoleArn** *(string) --*

          The service role ARN that is obtained from the server when the backup is created.

        - **Status** *(string) --*

          The status of a backup while in progress.

        - **StatusDescription** *(string) --*

          An informational message about backup status.

        - **SubnetIds** *(list) --*

          The subnet IDs that are obtained from the server when the backup is created.

          - *(string) --*

        - **ToolsVersion** *(string) --*

          The version of AWS OpsWorks CM-specific tools that is obtained from the server when the
          backup is created.

        - **UserArn** *(string) --*

          The IAM user ARN of the requester for manual backups. This field is empty for automated
          backups.
    """


_DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventsPaginatePaginationConfigTypeDef(
    _DescribeEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEventsPaginate` `PaginationConfig`

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


_DescribeEventsPaginateResponseServerEventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseServerEventsTypeDef",
    {"CreatedAt": datetime, "ServerName": str, "Message": str, "LogUrl": str},
    total=False,
)


class DescribeEventsPaginateResponseServerEventsTypeDef(
    _DescribeEventsPaginateResponseServerEventsTypeDef
):
    """
    Type definition for `DescribeEventsPaginateResponse` `ServerEvents`

    An event that is related to the server, such as the start of maintenance or backup.

    - **CreatedAt** *(datetime) --*

      The time when the event occurred.

    - **ServerName** *(string) --*

      The name of the server on or for which the event occurred.

    - **Message** *(string) --*

      A human-readable informational or status message.

    - **LogUrl** *(string) --*

      The Amazon S3 URL of the event's log file.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"ServerEvents": List[DescribeEventsPaginateResponseServerEventsTypeDef]},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `Response`

    - **ServerEvents** *(list) --*

      Contains the response to a ``DescribeEvents`` request.

      - *(dict) --*

        An event that is related to the server, such as the start of maintenance or backup.

        - **CreatedAt** *(datetime) --*

          The time when the event occurred.

        - **ServerName** *(string) --*

          The name of the server on or for which the event occurred.

        - **Message** *(string) --*

          A human-readable informational or status message.

        - **LogUrl** *(string) --*

          The Amazon S3 URL of the event's log file.
    """


_DescribeServersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeServersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeServersPaginatePaginationConfigTypeDef(
    _DescribeServersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeServersPaginate` `PaginationConfig`

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


_DescribeServersPaginateResponseServersEngineAttributesTypeDef = TypedDict(
    "_DescribeServersPaginateResponseServersEngineAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeServersPaginateResponseServersEngineAttributesTypeDef(
    _DescribeServersPaginateResponseServersEngineAttributesTypeDef
):
    """
    Type definition for `DescribeServersPaginateResponseServers` `EngineAttributes`

    A name and value pair that is specific to the engine of the server.

    - **Name** *(string) --*

      The name of the engine attribute.

    - **Value** *(string) --*

      The value of the engine attribute.
    """


_DescribeServersPaginateResponseServersTypeDef = TypedDict(
    "_DescribeServersPaginateResponseServersTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List[
            DescribeServersPaginateResponseServersEngineAttributesTypeDef
        ],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": str,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": str,
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)


class DescribeServersPaginateResponseServersTypeDef(
    _DescribeServersPaginateResponseServersTypeDef
):
    """
    Type definition for `DescribeServersPaginateResponse` `Servers`

    Describes a configuration management server.

    - **AssociatePublicIpAddress** *(boolean) --*

      Associate a public IP address with a server that you are launching.

    - **BackupRetentionCount** *(integer) --*

      The number of automated backups to keep.

    - **ServerName** *(string) --*

      The name of the server.

    - **CreatedAt** *(datetime) --*

      Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

    - **CloudFormationStackArn** *(string) --*

      The ARN of the CloudFormation stack that was used to create the server.

    - **CustomDomain** *(string) --*

      An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
      cannot access the server by using the ``Endpoint`` value if the server has a
      ``CustomDomain`` specified.

    - **DisableAutomatedBackup** *(boolean) --*

      Disables automated backups. The number of stored backups is dependent on the value of
      PreferredBackupCount.

    - **Endpoint** *(string) --*

      A DNS name that can be used to access the engine. Example:
      ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
      ``Endpoint`` value if the server has a ``CustomDomain`` specified.

    - **Engine** *(string) --*

      The engine type of the server. Valid values in this release include ``ChefAutomate`` and
      ``Puppet`` .

    - **EngineModel** *(string) --*

      The engine model of the server. Valid values in this release include ``Monolithic`` for
      Puppet and ``Single`` for Chef.

    - **EngineAttributes** *(list) --*

      The response of a createServer() request returns the master credential to access the
      server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are
      returned only as part of the result of createServer().

       **Attributes returned in a createServer response for Chef**

      * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by
      AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.

      * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
      kit, which includes a README, a configuration file, and the required RSA private key.
      Save this file, unzip it, and then change to the directory where you've unzipped the file
      contents. From this directory, you can run Knife commands.

       **Attributes returned in a createServer response for Puppet**

      * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
      starter kit, including a README and a required private key. Save this file, unzip it, and
      then change to the directory where you've unzipped the file contents.

      * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to
      the Puppet Enterprise console after the server is online.

      - *(dict) --*

        A name and value pair that is specific to the engine of the server.

        - **Name** *(string) --*

          The name of the engine attribute.

        - **Value** *(string) --*

          The value of the engine attribute.

    - **EngineVersion** *(string) --*

      The engine version of the server. For a Chef server, the valid value for EngineVersion is
      currently ``12`` . For a Puppet server, the valid value is ``2017`` .

    - **InstanceProfileArn** *(string) --*

      The instance profile ARN of the server.

    - **InstanceType** *(string) --*

      The instance type for the server, as specified in the CloudFormation stack. This might
      not be the same instance type that is shown in the EC2 console.

    - **KeyPair** *(string) --*

      The key pair associated with the server.

    - **MaintenanceStatus** *(string) --*

      The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

    - **PreferredMaintenanceWindow** *(string) --*

      The preferred maintenance period specified for the server.

    - **PreferredBackupWindow** *(string) --*

      The preferred backup period specified for the server.

    - **SecurityGroupIds** *(list) --*

      The security group IDs for the server, as specified in the CloudFormation stack. These
      might not be the same security groups that are shown in the EC2 console.

      - *(string) --*

    - **ServiceRoleArn** *(string) --*

      The service role ARN used to create the server.

    - **Status** *(string) --*

      The server's status. This field displays the states of actions in progress, such as
      creating, running, or backing up the server, as well as the server's health state.

    - **StatusReason** *(string) --*

      Depending on the server status, this field has either a human-readable message (such as a
      create or backup error), or an escaped block of JSON (used for health check results).

    - **SubnetIds** *(list) --*

      The subnet IDs specified in a CreateServer request.

      - *(string) --*

    - **ServerArn** *(string) --*

      The ARN of the server.
    """


_DescribeServersPaginateResponseTypeDef = TypedDict(
    "_DescribeServersPaginateResponseTypeDef",
    {"Servers": List[DescribeServersPaginateResponseServersTypeDef]},
    total=False,
)


class DescribeServersPaginateResponseTypeDef(_DescribeServersPaginateResponseTypeDef):
    """
    Type definition for `DescribeServersPaginate` `Response`

    - **Servers** *(list) --*

      Contains the response to a ``DescribeServers`` request.

       *For Puppet Server:*  ``DescribeServersResponse$Servers$EngineAttributes`` contains
       PUPPET_API_CA_CERT. This is the PEM-encoded CA certificate that is used by the Puppet API
       over TCP port number 8140. The CA certificate is also used to sign node certificates.

      - *(dict) --*

        Describes a configuration management server.

        - **AssociatePublicIpAddress** *(boolean) --*

          Associate a public IP address with a server that you are launching.

        - **BackupRetentionCount** *(integer) --*

          The number of automated backups to keep.

        - **ServerName** *(string) --*

          The name of the server.

        - **CreatedAt** *(datetime) --*

          Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``

        - **CloudFormationStackArn** *(string) --*

          The ARN of the CloudFormation stack that was used to create the server.

        - **CustomDomain** *(string) --*

          An optional public endpoint of a server, such as ``https://aws.my-company.com`` . You
          cannot access the server by using the ``Endpoint`` value if the server has a
          ``CustomDomain`` specified.

        - **DisableAutomatedBackup** *(boolean) --*

          Disables automated backups. The number of stored backups is dependent on the value of
          PreferredBackupCount.

        - **Endpoint** *(string) --*

          A DNS name that can be used to access the engine. Example:
          ``myserver-asdfghjkl.us-east-1.opsworks.io`` . You cannot access the server by using the
          ``Endpoint`` value if the server has a ``CustomDomain`` specified.

        - **Engine** *(string) --*

          The engine type of the server. Valid values in this release include ``ChefAutomate`` and
          ``Puppet`` .

        - **EngineModel** *(string) --*

          The engine model of the server. Valid values in this release include ``Monolithic`` for
          Puppet and ``Single`` for Chef.

        - **EngineAttributes** *(list) --*

          The response of a createServer() request returns the master credential to access the
          server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are
          returned only as part of the result of createServer().

           **Attributes returned in a createServer response for Chef**

          * ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by
          AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.

          * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter
          kit, which includes a README, a configuration file, and the required RSA private key.
          Save this file, unzip it, and then change to the directory where you've unzipped the file
          contents. From this directory, you can run Knife commands.

           **Attributes returned in a createServer response for Puppet**

          * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet
          starter kit, including a README and a required private key. Save this file, unzip it, and
          then change to the directory where you've unzipped the file contents.

          * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to
          the Puppet Enterprise console after the server is online.

          - *(dict) --*

            A name and value pair that is specific to the engine of the server.

            - **Name** *(string) --*

              The name of the engine attribute.

            - **Value** *(string) --*

              The value of the engine attribute.

        - **EngineVersion** *(string) --*

          The engine version of the server. For a Chef server, the valid value for EngineVersion is
          currently ``12`` . For a Puppet server, the valid value is ``2017`` .

        - **InstanceProfileArn** *(string) --*

          The instance profile ARN of the server.

        - **InstanceType** *(string) --*

          The instance type for the server, as specified in the CloudFormation stack. This might
          not be the same instance type that is shown in the EC2 console.

        - **KeyPair** *(string) --*

          The key pair associated with the server.

        - **MaintenanceStatus** *(string) --*

          The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` .

        - **PreferredMaintenanceWindow** *(string) --*

          The preferred maintenance period specified for the server.

        - **PreferredBackupWindow** *(string) --*

          The preferred backup period specified for the server.

        - **SecurityGroupIds** *(list) --*

          The security group IDs for the server, as specified in the CloudFormation stack. These
          might not be the same security groups that are shown in the EC2 console.

          - *(string) --*

        - **ServiceRoleArn** *(string) --*

          The service role ARN used to create the server.

        - **Status** *(string) --*

          The server's status. This field displays the states of actions in progress, such as
          creating, running, or backing up the server, as well as the server's health state.

        - **StatusReason** *(string) --*

          Depending on the server status, this field has either a human-readable message (such as a
          create or backup error), or an escaped block of JSON (used for health check results).

        - **SubnetIds** *(list) --*

          The subnet IDs specified in a CreateServer request.

          - *(string) --*

        - **ServerArn** *(string) --*

          The ARN of the server.
    """


_NodeAssociatedWaitWaiterConfigTypeDef = TypedDict(
    "_NodeAssociatedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class NodeAssociatedWaitWaiterConfigTypeDef(_NodeAssociatedWaitWaiterConfigTypeDef):
    """
    Type definition for `NodeAssociatedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 15
    """
