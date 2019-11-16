"Main interface for ds type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef",
    "ClientAcceptSharedDirectoryResponseTypeDef",
    "ClientAddIpRoutesIpRoutesTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientConnectDirectoryConnectSettingsTypeDef",
    "ClientConnectDirectoryResponseTypeDef",
    "ClientConnectDirectoryTagsTypeDef",
    "ClientCreateAliasResponseTypeDef",
    "ClientCreateComputerComputerAttributesTypeDef",
    "ClientCreateComputerResponseComputerComputerAttributesTypeDef",
    "ClientCreateComputerResponseComputerTypeDef",
    "ClientCreateComputerResponseTypeDef",
    "ClientCreateDirectoryResponseTypeDef",
    "ClientCreateDirectoryTagsTypeDef",
    "ClientCreateDirectoryVpcSettingsTypeDef",
    "ClientCreateMicrosoftAdResponseTypeDef",
    "ClientCreateMicrosoftAdTagsTypeDef",
    "ClientCreateMicrosoftAdVpcSettingsTypeDef",
    "ClientCreateSnapshotResponseTypeDef",
    "ClientCreateTrustResponseTypeDef",
    "ClientDeleteDirectoryResponseTypeDef",
    "ClientDeleteSnapshotResponseTypeDef",
    "ClientDeleteTrustResponseTypeDef",
    "ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef",
    "ClientDescribeConditionalForwardersResponseTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef",
    "ClientDescribeDirectoriesResponseTypeDef",
    "ClientDescribeDomainControllersResponseDomainControllersTypeDef",
    "ClientDescribeDomainControllersResponseTypeDef",
    "ClientDescribeEventTopicsResponseEventTopicsTypeDef",
    "ClientDescribeEventTopicsResponseTypeDef",
    "ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef",
    "ClientDescribeSharedDirectoriesResponseTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    "ClientDescribeSnapshotsResponseTypeDef",
    "ClientDescribeTrustsResponseTrustsTypeDef",
    "ClientDescribeTrustsResponseTypeDef",
    "ClientEnableRadiusRadiusSettingsTypeDef",
    "ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef",
    "ClientGetDirectoryLimitsResponseTypeDef",
    "ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef",
    "ClientGetSnapshotLimitsResponseTypeDef",
    "ClientListIpRoutesResponseIpRoutesInfoTypeDef",
    "ClientListIpRoutesResponseTypeDef",
    "ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef",
    "ClientListLogSubscriptionsResponseTypeDef",
    "ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef",
    "ClientListSchemaExtensionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRejectSharedDirectoryResponseTypeDef",
    "ClientShareDirectoryResponseTypeDef",
    "ClientShareDirectoryShareTargetTypeDef",
    "ClientStartSchemaExtensionResponseTypeDef",
    "ClientUnshareDirectoryResponseTypeDef",
    "ClientUnshareDirectoryUnshareTargetTypeDef",
    "ClientUpdateRadiusRadiusSettingsTypeDef",
    "ClientUpdateTrustResponseTypeDef",
    "ClientVerifyTrustResponseTypeDef",
    "DescribeDirectoriesPaginatePaginationConfigTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef",
    "DescribeDirectoriesPaginateResponseTypeDef",
    "DescribeDomainControllersPaginatePaginationConfigTypeDef",
    "DescribeDomainControllersPaginateResponseDomainControllersTypeDef",
    "DescribeDomainControllersPaginateResponseTypeDef",
    "DescribeSharedDirectoriesPaginatePaginationConfigTypeDef",
    "DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef",
    "DescribeSharedDirectoriesPaginateResponseTypeDef",
    "DescribeSnapshotsPaginatePaginationConfigTypeDef",
    "DescribeSnapshotsPaginateResponseSnapshotsTypeDef",
    "DescribeSnapshotsPaginateResponseTypeDef",
    "DescribeTrustsPaginatePaginationConfigTypeDef",
    "DescribeTrustsPaginateResponseTrustsTypeDef",
    "DescribeTrustsPaginateResponseTypeDef",
    "ListIpRoutesPaginatePaginationConfigTypeDef",
    "ListIpRoutesPaginateResponseIpRoutesInfoTypeDef",
    "ListIpRoutesPaginateResponseTypeDef",
    "ListLogSubscriptionsPaginatePaginationConfigTypeDef",
    "ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef",
    "ListLogSubscriptionsPaginateResponseTypeDef",
    "ListSchemaExtensionsPaginatePaginationConfigTypeDef",
    "ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef",
    "ListSchemaExtensionsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
)


_ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef = TypedDict(
    "_ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": str,
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": str,
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef(
    _ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef
):
    """
    Type definition for `ClientAcceptSharedDirectoryResponse` `SharedDirectory`

    The shared directory in the directory consumer account.

    - **OwnerAccountId** *(string) --*

      Identifier of the directory owner account, which contains the directory that has been
      shared to the consumer account.

    - **OwnerDirectoryId** *(string) --*

      Identifier of the directory in the directory owner account.

    - **ShareMethod** *(string) --*

      The method used when sharing a directory to determine whether the directory should be
      shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by sending
      a shared directory request (``HANDSHAKE`` ).

    - **SharedAccountId** *(string) --*

      Identifier of the directory consumer account that has access to the shared directory
      (``OwnerDirectoryId`` ) in the directory owner account.

    - **SharedDirectoryId** *(string) --*

      Identifier of the shared directory in the directory consumer account. This identifier is
      different for each directory owner account.

    - **ShareStatus** *(string) --*

      Current directory status of the shared AWS Managed Microsoft AD directory.

    - **ShareNotes** *(string) --*

      A directory share request that is sent by the directory owner to the directory consumer.
      The request includes a typed message to help the directory consumer administrator determine
      whether to approve or reject the share invitation.

    - **CreatedDateTime** *(datetime) --*

      The date and time that the shared directory was created.

    - **LastUpdatedDateTime** *(datetime) --*

      The date and time that the shared directory was last updated.
    """


_ClientAcceptSharedDirectoryResponseTypeDef = TypedDict(
    "_ClientAcceptSharedDirectoryResponseTypeDef",
    {"SharedDirectory": ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef},
    total=False,
)


class ClientAcceptSharedDirectoryResponseTypeDef(
    _ClientAcceptSharedDirectoryResponseTypeDef
):
    """
    Type definition for `ClientAcceptSharedDirectory` `Response`

    - **SharedDirectory** *(dict) --*

      The shared directory in the directory consumer account.

      - **OwnerAccountId** *(string) --*

        Identifier of the directory owner account, which contains the directory that has been
        shared to the consumer account.

      - **OwnerDirectoryId** *(string) --*

        Identifier of the directory in the directory owner account.

      - **ShareMethod** *(string) --*

        The method used when sharing a directory to determine whether the directory should be
        shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by sending
        a shared directory request (``HANDSHAKE`` ).

      - **SharedAccountId** *(string) --*

        Identifier of the directory consumer account that has access to the shared directory
        (``OwnerDirectoryId`` ) in the directory owner account.

      - **SharedDirectoryId** *(string) --*

        Identifier of the shared directory in the directory consumer account. This identifier is
        different for each directory owner account.

      - **ShareStatus** *(string) --*

        Current directory status of the shared AWS Managed Microsoft AD directory.

      - **ShareNotes** *(string) --*

        A directory share request that is sent by the directory owner to the directory consumer.
        The request includes a typed message to help the directory consumer administrator determine
        whether to approve or reject the share invitation.

      - **CreatedDateTime** *(datetime) --*

        The date and time that the shared directory was created.

      - **LastUpdatedDateTime** *(datetime) --*

        The date and time that the shared directory was last updated.
    """


_ClientAddIpRoutesIpRoutesTypeDef = TypedDict(
    "_ClientAddIpRoutesIpRoutesTypeDef",
    {"CidrIp": str, "Description": str},
    total=False,
)


class ClientAddIpRoutesIpRoutesTypeDef(_ClientAddIpRoutesIpRoutesTypeDef):
    """
    Type definition for `ClientAddIpRoutes` `IpRoutes`

    IP address block. This is often the address block of the DNS server used for your on-premises
    domain.

    - **CidrIp** *(string) --*

      IP address block using CIDR format, for example 10.0.0.0/24. This is often the address block
      of the DNS server used for your on-premises domain. For a single IP address use a CIDR
      address block with /32. For example 10.0.0.0/32.

    - **Description** *(string) --*

      Description of the address block.
    """


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    Type definition for `ClientAddTagsToResource` `Tags`

    Metadata assigned to a directory consisting of a key-value pair.

    - **Key** *(string) --* **[REQUIRED]**

      Required name of the tag. The string value can be Unicode characters and cannot be prefixed
      with "aws:". The string can contain only the set of Unicode letters, digits, white-space,
      '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --* **[REQUIRED]**

      The optional value of the tag. The string value can be Unicode characters. The string can
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientConnectDirectoryConnectSettingsTypeDef = TypedDict(
    "_ClientConnectDirectoryConnectSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerDnsIps": List[str],
        "CustomerUserName": str,
    },
)


class ClientConnectDirectoryConnectSettingsTypeDef(
    _ClientConnectDirectoryConnectSettingsTypeDef
):
    """
    Type definition for `ClientConnectDirectory` `ConnectSettings`

    A  DirectoryConnectSettings object that contains additional information for the operation.

    - **VpcId** *(string) --* **[REQUIRED]**

      The identifier of the VPC in which the AD Connector is created.

    - **SubnetIds** *(list) --* **[REQUIRED]**

      A list of subnet identifiers in the VPC in which the AD Connector is created.

      - *(string) --*

    - **CustomerDnsIps** *(list) --* **[REQUIRED]**

      A list of one or more IP addresses of DNS servers or domain controllers in the on-premises
      directory.

      - *(string) --*

    - **CustomerUserName** *(string) --* **[REQUIRED]**

      The user name of an account in the on-premises directory that is used to connect to the
      directory. This account must have the following permissions:

      * Read users and groups

      * Create computer objects

      * Join computers to the domain
    """


_ClientConnectDirectoryResponseTypeDef = TypedDict(
    "_ClientConnectDirectoryResponseTypeDef", {"DirectoryId": str}, total=False
)


class ClientConnectDirectoryResponseTypeDef(_ClientConnectDirectoryResponseTypeDef):
    """
    Type definition for `ClientConnectDirectory` `Response`

    Contains the results of the  ConnectDirectory operation.

    - **DirectoryId** *(string) --*

      The identifier of the new directory.
    """


_ClientConnectDirectoryTagsTypeDef = TypedDict(
    "_ClientConnectDirectoryTagsTypeDef", {"Key": str, "Value": str}
)


class ClientConnectDirectoryTagsTypeDef(_ClientConnectDirectoryTagsTypeDef):
    """
    Type definition for `ClientConnectDirectory` `Tags`

    Metadata assigned to a directory consisting of a key-value pair.

    - **Key** *(string) --* **[REQUIRED]**

      Required name of the tag. The string value can be Unicode characters and cannot be prefixed
      with "aws:". The string can contain only the set of Unicode letters, digits, white-space,
      '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --* **[REQUIRED]**

      The optional value of the tag. The string value can be Unicode characters. The string can
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateAliasResponseTypeDef = TypedDict(
    "_ClientCreateAliasResponseTypeDef", {"DirectoryId": str, "Alias": str}, total=False
)


class ClientCreateAliasResponseTypeDef(_ClientCreateAliasResponseTypeDef):
    """
    Type definition for `ClientCreateAlias` `Response`

    Contains the results of the  CreateAlias operation.

    - **DirectoryId** *(string) --*

      The identifier of the directory.

    - **Alias** *(string) --*

      The alias for the directory.
    """


_ClientCreateComputerComputerAttributesTypeDef = TypedDict(
    "_ClientCreateComputerComputerAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateComputerComputerAttributesTypeDef(
    _ClientCreateComputerComputerAttributesTypeDef
):
    """
    Type definition for `ClientCreateComputer` `ComputerAttributes`

    Represents a named directory attribute.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientCreateComputerResponseComputerComputerAttributesTypeDef = TypedDict(
    "_ClientCreateComputerResponseComputerComputerAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateComputerResponseComputerComputerAttributesTypeDef(
    _ClientCreateComputerResponseComputerComputerAttributesTypeDef
):
    """
    Type definition for `ClientCreateComputerResponseComputer` `ComputerAttributes`

    Represents a named directory attribute.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientCreateComputerResponseComputerTypeDef = TypedDict(
    "_ClientCreateComputerResponseComputerTypeDef",
    {
        "ComputerId": str,
        "ComputerName": str,
        "ComputerAttributes": List[
            ClientCreateComputerResponseComputerComputerAttributesTypeDef
        ],
    },
    total=False,
)


class ClientCreateComputerResponseComputerTypeDef(
    _ClientCreateComputerResponseComputerTypeDef
):
    """
    Type definition for `ClientCreateComputerResponse` `Computer`

    A  Computer object that represents the computer account.

    - **ComputerId** *(string) --*

      The identifier of the computer.

    - **ComputerName** *(string) --*

      The computer name.

    - **ComputerAttributes** *(list) --*

      An array of  Attribute objects containing the LDAP attributes that belong to the computer
      account.

      - *(dict) --*

        Represents a named directory attribute.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.
    """


_ClientCreateComputerResponseTypeDef = TypedDict(
    "_ClientCreateComputerResponseTypeDef",
    {"Computer": ClientCreateComputerResponseComputerTypeDef},
    total=False,
)


class ClientCreateComputerResponseTypeDef(_ClientCreateComputerResponseTypeDef):
    """
    Type definition for `ClientCreateComputer` `Response`

    Contains the results for the  CreateComputer operation.

    - **Computer** *(dict) --*

      A  Computer object that represents the computer account.

      - **ComputerId** *(string) --*

        The identifier of the computer.

      - **ComputerName** *(string) --*

        The computer name.

      - **ComputerAttributes** *(list) --*

        An array of  Attribute objects containing the LDAP attributes that belong to the computer
        account.

        - *(dict) --*

          Represents a named directory attribute.

          - **Name** *(string) --*

            The name of the attribute.

          - **Value** *(string) --*

            The value of the attribute.
    """


_ClientCreateDirectoryResponseTypeDef = TypedDict(
    "_ClientCreateDirectoryResponseTypeDef", {"DirectoryId": str}, total=False
)


class ClientCreateDirectoryResponseTypeDef(_ClientCreateDirectoryResponseTypeDef):
    """
    Type definition for `ClientCreateDirectory` `Response`

    Contains the results of the  CreateDirectory operation.

    - **DirectoryId** *(string) --*

      The identifier of the directory that was created.
    """


_ClientCreateDirectoryTagsTypeDef = TypedDict(
    "_ClientCreateDirectoryTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateDirectoryTagsTypeDef(_ClientCreateDirectoryTagsTypeDef):
    """
    Type definition for `ClientCreateDirectory` `Tags`

    Metadata assigned to a directory consisting of a key-value pair.

    - **Key** *(string) --* **[REQUIRED]**

      Required name of the tag. The string value can be Unicode characters and cannot be prefixed
      with "aws:". The string can contain only the set of Unicode letters, digits, white-space,
      '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --* **[REQUIRED]**

      The optional value of the tag. The string value can be Unicode characters. The string can
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDirectoryVpcSettingsTypeDef = TypedDict(
    "_ClientCreateDirectoryVpcSettingsTypeDef", {"VpcId": str, "SubnetIds": List[str]}
)


class ClientCreateDirectoryVpcSettingsTypeDef(_ClientCreateDirectoryVpcSettingsTypeDef):
    """
    Type definition for `ClientCreateDirectory` `VpcSettings`

    A  DirectoryVpcSettings object that contains additional information for the operation.

    - **VpcId** *(string) --* **[REQUIRED]**

      The identifier of the VPC in which to create the directory.

    - **SubnetIds** *(list) --* **[REQUIRED]**

      The identifiers of the subnets for the directory servers. The two subnets must be in different
      Availability Zones. AWS Directory Service creates a directory server and a DNS server in each
      of these subnets.

      - *(string) --*
    """


_ClientCreateMicrosoftAdResponseTypeDef = TypedDict(
    "_ClientCreateMicrosoftAdResponseTypeDef", {"DirectoryId": str}, total=False
)


class ClientCreateMicrosoftAdResponseTypeDef(_ClientCreateMicrosoftAdResponseTypeDef):
    """
    Type definition for `ClientCreateMicrosoftAd` `Response`

    Result of a CreateMicrosoftAD request.

    - **DirectoryId** *(string) --*

      The identifier of the directory that was created.
    """


_ClientCreateMicrosoftAdTagsTypeDef = TypedDict(
    "_ClientCreateMicrosoftAdTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateMicrosoftAdTagsTypeDef(_ClientCreateMicrosoftAdTagsTypeDef):
    """
    Type definition for `ClientCreateMicrosoftAd` `Tags`

    Metadata assigned to a directory consisting of a key-value pair.

    - **Key** *(string) --* **[REQUIRED]**

      Required name of the tag. The string value can be Unicode characters and cannot be prefixed
      with "aws:". The string can contain only the set of Unicode letters, digits, white-space,
      '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --* **[REQUIRED]**

      The optional value of the tag. The string value can be Unicode characters. The string can
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
      (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateMicrosoftAdVpcSettingsTypeDef = TypedDict(
    "_ClientCreateMicrosoftAdVpcSettingsTypeDef", {"VpcId": str, "SubnetIds": List[str]}
)


class ClientCreateMicrosoftAdVpcSettingsTypeDef(
    _ClientCreateMicrosoftAdVpcSettingsTypeDef
):
    """
    Type definition for `ClientCreateMicrosoftAd` `VpcSettings`

    Contains VPC information for the  CreateDirectory or  CreateMicrosoftAD operation.

    - **VpcId** *(string) --* **[REQUIRED]**

      The identifier of the VPC in which to create the directory.

    - **SubnetIds** *(list) --* **[REQUIRED]**

      The identifiers of the subnets for the directory servers. The two subnets must be in different
      Availability Zones. AWS Directory Service creates a directory server and a DNS server in each
      of these subnets.

      - *(string) --*
    """


_ClientCreateSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseTypeDef", {"SnapshotId": str}, total=False
)


class ClientCreateSnapshotResponseTypeDef(_ClientCreateSnapshotResponseTypeDef):
    """
    Type definition for `ClientCreateSnapshot` `Response`

    Contains the results of the  CreateSnapshot operation.

    - **SnapshotId** *(string) --*

      The identifier of the snapshot that was created.
    """


_ClientCreateTrustResponseTypeDef = TypedDict(
    "_ClientCreateTrustResponseTypeDef", {"TrustId": str}, total=False
)


class ClientCreateTrustResponseTypeDef(_ClientCreateTrustResponseTypeDef):
    """
    Type definition for `ClientCreateTrust` `Response`

    The result of a CreateTrust request.

    - **TrustId** *(string) --*

      A unique identifier for the trust relationship that was created.
    """


_ClientDeleteDirectoryResponseTypeDef = TypedDict(
    "_ClientDeleteDirectoryResponseTypeDef", {"DirectoryId": str}, total=False
)


class ClientDeleteDirectoryResponseTypeDef(_ClientDeleteDirectoryResponseTypeDef):
    """
    Type definition for `ClientDeleteDirectory` `Response`

    Contains the results of the  DeleteDirectory operation.

    - **DirectoryId** *(string) --*

      The directory identifier.
    """


_ClientDeleteSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteSnapshotResponseTypeDef", {"SnapshotId": str}, total=False
)


class ClientDeleteSnapshotResponseTypeDef(_ClientDeleteSnapshotResponseTypeDef):
    """
    Type definition for `ClientDeleteSnapshot` `Response`

    Contains the results of the  DeleteSnapshot operation.

    - **SnapshotId** *(string) --*

      The identifier of the directory snapshot that was deleted.
    """


_ClientDeleteTrustResponseTypeDef = TypedDict(
    "_ClientDeleteTrustResponseTypeDef", {"TrustId": str}, total=False
)


class ClientDeleteTrustResponseTypeDef(_ClientDeleteTrustResponseTypeDef):
    """
    Type definition for `ClientDeleteTrust` `Response`

    The result of a DeleteTrust request.

    - **TrustId** *(string) --*

      The Trust ID of the trust relationship that was deleted.
    """


_ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef = TypedDict(
    "_ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef",
    {"RemoteDomainName": str, "DnsIpAddrs": List[str], "ReplicationScope": str},
    total=False,
)


class ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef(
    _ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef
):
    """
    Type definition for `ClientDescribeConditionalForwardersResponse` `ConditionalForwarders`

    Points to a remote domain with which you are setting up a trust relationship. Conditional
    forwarders are required in order to set up a trust relationship with another domain.

    - **RemoteDomainName** *(string) --*

      The fully qualified domain name (FQDN) of the remote domains pointed to by the
      conditional forwarder.

    - **DnsIpAddrs** *(list) --*

      The IP addresses of the remote DNS server associated with RemoteDomainName. This is the
      IP address of the DNS server that your conditional forwarder points to.

      - *(string) --*

    - **ReplicationScope** *(string) --*

      The replication scope of the conditional forwarder. The only allowed value is ``Domain``
      , which will replicate the conditional forwarder to all of the domain controllers for
      your AWS directory.
    """


_ClientDescribeConditionalForwardersResponseTypeDef = TypedDict(
    "_ClientDescribeConditionalForwardersResponseTypeDef",
    {
        "ConditionalForwarders": List[
            ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConditionalForwardersResponseTypeDef(
    _ClientDescribeConditionalForwardersResponseTypeDef
):
    """
    Type definition for `ClientDescribeConditionalForwarders` `Response`

    The result of a DescribeConditionalForwarder request.

    - **ConditionalForwarders** *(list) --*

      The list of conditional forwarders that have been created.

      - *(dict) --*

        Points to a remote domain with which you are setting up a trust relationship. Conditional
        forwarders are required in order to set up a trust relationship with another domain.

        - **RemoteDomainName** *(string) --*

          The fully qualified domain name (FQDN) of the remote domains pointed to by the
          conditional forwarder.

        - **DnsIpAddrs** *(list) --*

          The IP addresses of the remote DNS server associated with RemoteDomainName. This is the
          IP address of the DNS server that your conditional forwarder points to.

          - *(string) --*

        - **ReplicationScope** *(string) --*

          The replication scope of the conditional forwarder. The only allowed value is ``Domain``
          , which will replicate the conditional forwarder to all of the domain controllers for
          your AWS directory.
    """


_ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerUserName": str,
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
        "ConnectIps": List[str],
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef
):
    """
    Type definition for `ClientDescribeDirectoriesResponseDirectoryDescriptions` `ConnectSettings`

    A  DirectoryConnectSettingsDescription object that contains additional information about
    an AD Connector directory. This member is only present if the directory is an AD
    Connector directory.

    - **VpcId** *(string) --*

      The identifier of the VPC that the AD Connector is in.

    - **SubnetIds** *(list) --*

      A list of subnet identifiers in the VPC that the AD connector is in.

      - *(string) --*

    - **CustomerUserName** *(string) --*

      The user name of the service account in the on-premises directory.

    - **SecurityGroupId** *(string) --*

      The security group identifier for the AD Connector directory.

    - **AvailabilityZones** *(list) --*

      A list of the Availability Zones that the directory is in.

      - *(string) --*

    - **ConnectIps** *(list) --*

      The IP addresses of the AD Connector servers.

      - *(string) --*
    """


_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": str,
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef
):
    """
    Type definition for `ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescription` `RadiusSettings`

    A  RadiusSettings object that contains information about the RADIUS server.

    - **RadiusServers** *(list) --*

      An array of strings that contains the IP addresses of the RADIUS server endpoints, or
      the IP addresses of your RADIUS server load balancer.

      - *(string) --*

    - **RadiusPort** *(integer) --*

      The port that your RADIUS server is using for communications. Your on-premises
      network must allow inbound traffic over this port from the AWS Directory Service
      servers.

    - **RadiusTimeout** *(integer) --*

      The amount of time, in seconds, to wait for the RADIUS server to respond.

    - **RadiusRetries** *(integer) --*

      The maximum number of times that communication with the RADIUS server is attempted.

    - **SharedSecret** *(string) --*

      Required for enabling RADIUS on the directory.

    - **AuthenticationProtocol** *(string) --*

      The protocol specified for your RADIUS endpoints.

    - **DisplayLabel** *(string) --*

      Not currently used.

    - **UseSameUsername** *(boolean) --*

      Not currently used.
    """


_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef
):
    """
    Type definition for `ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescription` `VpcSettings`

    Information about the VPC settings for the directory.

    - **VpcId** *(string) --*

      The identifier of the VPC that the directory is in.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets for the directory servers.

      - *(string) --*

    - **SecurityGroupId** *(string) --*

      The domain controller security group identifier for the directory.

    - **AvailabilityZones** *(list) --*

      The list of Availability Zones that the directory is in.

      - *(string) --*
    """


_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "AccountId": str,
        "DnsIpAddrs": List[str],
        "VpcSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef,
        "RadiusSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef,
        "RadiusStatus": str,
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDirectoriesResponseDirectoryDescriptions` `OwnerDirectoryDescription`

    Describes the AWS Managed Microsoft AD directory in the directory owner account.

    - **DirectoryId** *(string) --*

      Identifier of the AWS Managed Microsoft AD directory in the directory owner account.

    - **AccountId** *(string) --*

      Identifier of the directory owner account.

    - **DnsIpAddrs** *(list) --*

      IP address of the directory’s domain controllers.

      - *(string) --*

    - **VpcSettings** *(dict) --*

      Information about the VPC settings for the directory.

      - **VpcId** *(string) --*

        The identifier of the VPC that the directory is in.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets for the directory servers.

        - *(string) --*

      - **SecurityGroupId** *(string) --*

        The domain controller security group identifier for the directory.

      - **AvailabilityZones** *(list) --*

        The list of Availability Zones that the directory is in.

        - *(string) --*

    - **RadiusSettings** *(dict) --*

      A  RadiusSettings object that contains information about the RADIUS server.

      - **RadiusServers** *(list) --*

        An array of strings that contains the IP addresses of the RADIUS server endpoints, or
        the IP addresses of your RADIUS server load balancer.

        - *(string) --*

      - **RadiusPort** *(integer) --*

        The port that your RADIUS server is using for communications. Your on-premises
        network must allow inbound traffic over this port from the AWS Directory Service
        servers.

      - **RadiusTimeout** *(integer) --*

        The amount of time, in seconds, to wait for the RADIUS server to respond.

      - **RadiusRetries** *(integer) --*

        The maximum number of times that communication with the RADIUS server is attempted.

      - **SharedSecret** *(string) --*

        Required for enabling RADIUS on the directory.

      - **AuthenticationProtocol** *(string) --*

        The protocol specified for your RADIUS endpoints.

      - **DisplayLabel** *(string) --*

        Not currently used.

      - **UseSameUsername** *(boolean) --*

        Not currently used.

    - **RadiusStatus** *(string) --*

      Information about the status of the RADIUS server.
    """


_ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": str,
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef
):
    """
    Type definition for `ClientDescribeDirectoriesResponseDirectoryDescriptions` `RadiusSettings`

    A  RadiusSettings object that contains information about the RADIUS server configured for
    this directory.

    - **RadiusServers** *(list) --*

      An array of strings that contains the IP addresses of the RADIUS server endpoints, or
      the IP addresses of your RADIUS server load balancer.

      - *(string) --*

    - **RadiusPort** *(integer) --*

      The port that your RADIUS server is using for communications. Your on-premises network
      must allow inbound traffic over this port from the AWS Directory Service servers.

    - **RadiusTimeout** *(integer) --*

      The amount of time, in seconds, to wait for the RADIUS server to respond.

    - **RadiusRetries** *(integer) --*

      The maximum number of times that communication with the RADIUS server is attempted.

    - **SharedSecret** *(string) --*

      Required for enabling RADIUS on the directory.

    - **AuthenticationProtocol** *(string) --*

      The protocol specified for your RADIUS endpoints.

    - **DisplayLabel** *(string) --*

      Not currently used.

    - **UseSameUsername** *(boolean) --*

      Not currently used.
    """


_ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef
):
    """
    Type definition for `ClientDescribeDirectoriesResponseDirectoryDescriptions` `VpcSettings`

    A  DirectoryVpcSettingsDescription object that contains additional information about a
    directory. This member is only present if the directory is a Simple AD or Managed AD
    directory.

    - **VpcId** *(string) --*

      The identifier of the VPC that the directory is in.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets for the directory servers.

      - *(string) --*

    - **SecurityGroupId** *(string) --*

      The domain controller security group identifier for the directory.

    - **AvailabilityZones** *(list) --*

      The list of Availability Zones that the directory is in.

      - *(string) --*
    """


_ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef",
    {
        "DirectoryId": str,
        "Name": str,
        "ShortName": str,
        "Size": str,
        "Edition": str,
        "Alias": str,
        "AccessUrl": str,
        "Description": str,
        "DnsIpAddrs": List[str],
        "Stage": str,
        "ShareStatus": str,
        "ShareMethod": str,
        "ShareNotes": str,
        "LaunchTime": datetime,
        "StageLastUpdatedDateTime": datetime,
        "Type": str,
        "VpcSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef,
        "ConnectSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef,
        "RadiusSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef,
        "RadiusStatus": str,
        "StageReason": str,
        "SsoEnabled": bool,
        "DesiredNumberOfDomainControllers": int,
        "OwnerDirectoryDescription": ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef,
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeDirectoriesResponse` `DirectoryDescriptions`

    Contains information about an AWS Directory Service directory.

    - **DirectoryId** *(string) --*

      The directory identifier.

    - **Name** *(string) --*

      The fully qualified name of the directory.

    - **ShortName** *(string) --*

      The short name of the directory.

    - **Size** *(string) --*

      The directory size.

    - **Edition** *(string) --*

      The edition associated with this directory.

    - **Alias** *(string) --*

      The alias for the directory. If no alias has been created for the directory, the alias is
      the directory identifier, such as ``d-XXXXXXXXXX`` .

    - **AccessUrl** *(string) --*

      The access URL for the directory, such as ``http://<alias>.awsapps.com`` . If no alias
      has been created for the directory, ``<alias>`` is the directory identifier, such as
      ``d-XXXXXXXXXX`` .

    - **Description** *(string) --*

      The textual description for the directory.

    - **DnsIpAddrs** *(list) --*

      The IP addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD
      directory, these are the IP addresses of the Simple AD or Microsoft AD directory servers.
      For an AD Connector directory, these are the IP addresses of the DNS servers or domain
      controllers in the on-premises directory to which the AD Connector is connected.

      - *(string) --*

    - **Stage** *(string) --*

      The current stage of the directory.

    - **ShareStatus** *(string) --*

      Current directory status of the shared AWS Managed Microsoft AD directory.

    - **ShareMethod** *(string) --*

      The method used when sharing a directory to determine whether the directory should be
      shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by
      sending a shared directory request (``HANDSHAKE`` ).

    - **ShareNotes** *(string) --*

      A directory share request that is sent by the directory owner to the directory consumer.
      The request includes a typed message to help the directory consumer administrator
      determine whether to approve or reject the share invitation.

    - **LaunchTime** *(datetime) --*

      Specifies when the directory was created.

    - **StageLastUpdatedDateTime** *(datetime) --*

      The date and time that the stage was last updated.

    - **Type** *(string) --*

      The directory size.

    - **VpcSettings** *(dict) --*

      A  DirectoryVpcSettingsDescription object that contains additional information about a
      directory. This member is only present if the directory is a Simple AD or Managed AD
      directory.

      - **VpcId** *(string) --*

        The identifier of the VPC that the directory is in.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets for the directory servers.

        - *(string) --*

      - **SecurityGroupId** *(string) --*

        The domain controller security group identifier for the directory.

      - **AvailabilityZones** *(list) --*

        The list of Availability Zones that the directory is in.

        - *(string) --*

    - **ConnectSettings** *(dict) --*

      A  DirectoryConnectSettingsDescription object that contains additional information about
      an AD Connector directory. This member is only present if the directory is an AD
      Connector directory.

      - **VpcId** *(string) --*

        The identifier of the VPC that the AD Connector is in.

      - **SubnetIds** *(list) --*

        A list of subnet identifiers in the VPC that the AD connector is in.

        - *(string) --*

      - **CustomerUserName** *(string) --*

        The user name of the service account in the on-premises directory.

      - **SecurityGroupId** *(string) --*

        The security group identifier for the AD Connector directory.

      - **AvailabilityZones** *(list) --*

        A list of the Availability Zones that the directory is in.

        - *(string) --*

      - **ConnectIps** *(list) --*

        The IP addresses of the AD Connector servers.

        - *(string) --*

    - **RadiusSettings** *(dict) --*

      A  RadiusSettings object that contains information about the RADIUS server configured for
      this directory.

      - **RadiusServers** *(list) --*

        An array of strings that contains the IP addresses of the RADIUS server endpoints, or
        the IP addresses of your RADIUS server load balancer.

        - *(string) --*

      - **RadiusPort** *(integer) --*

        The port that your RADIUS server is using for communications. Your on-premises network
        must allow inbound traffic over this port from the AWS Directory Service servers.

      - **RadiusTimeout** *(integer) --*

        The amount of time, in seconds, to wait for the RADIUS server to respond.

      - **RadiusRetries** *(integer) --*

        The maximum number of times that communication with the RADIUS server is attempted.

      - **SharedSecret** *(string) --*

        Required for enabling RADIUS on the directory.

      - **AuthenticationProtocol** *(string) --*

        The protocol specified for your RADIUS endpoints.

      - **DisplayLabel** *(string) --*

        Not currently used.

      - **UseSameUsername** *(boolean) --*

        Not currently used.

    - **RadiusStatus** *(string) --*

      The status of the RADIUS MFA server connection.

    - **StageReason** *(string) --*

      Additional information about the directory stage.

    - **SsoEnabled** *(boolean) --*

      Indicates if single sign-on is enabled for the directory. For more information, see
      EnableSso and  DisableSso .

    - **DesiredNumberOfDomainControllers** *(integer) --*

      The desired number of domain controllers in the directory if the directory is Microsoft
      AD.

    - **OwnerDirectoryDescription** *(dict) --*

      Describes the AWS Managed Microsoft AD directory in the directory owner account.

      - **DirectoryId** *(string) --*

        Identifier of the AWS Managed Microsoft AD directory in the directory owner account.

      - **AccountId** *(string) --*

        Identifier of the directory owner account.

      - **DnsIpAddrs** *(list) --*

        IP address of the directory’s domain controllers.

        - *(string) --*

      - **VpcSettings** *(dict) --*

        Information about the VPC settings for the directory.

        - **VpcId** *(string) --*

          The identifier of the VPC that the directory is in.

        - **SubnetIds** *(list) --*

          The identifiers of the subnets for the directory servers.

          - *(string) --*

        - **SecurityGroupId** *(string) --*

          The domain controller security group identifier for the directory.

        - **AvailabilityZones** *(list) --*

          The list of Availability Zones that the directory is in.

          - *(string) --*

      - **RadiusSettings** *(dict) --*

        A  RadiusSettings object that contains information about the RADIUS server.

        - **RadiusServers** *(list) --*

          An array of strings that contains the IP addresses of the RADIUS server endpoints, or
          the IP addresses of your RADIUS server load balancer.

          - *(string) --*

        - **RadiusPort** *(integer) --*

          The port that your RADIUS server is using for communications. Your on-premises
          network must allow inbound traffic over this port from the AWS Directory Service
          servers.

        - **RadiusTimeout** *(integer) --*

          The amount of time, in seconds, to wait for the RADIUS server to respond.

        - **RadiusRetries** *(integer) --*

          The maximum number of times that communication with the RADIUS server is attempted.

        - **SharedSecret** *(string) --*

          Required for enabling RADIUS on the directory.

        - **AuthenticationProtocol** *(string) --*

          The protocol specified for your RADIUS endpoints.

        - **DisplayLabel** *(string) --*

          Not currently used.

        - **UseSameUsername** *(boolean) --*

          Not currently used.

      - **RadiusStatus** *(string) --*

        Information about the status of the RADIUS server.
    """


_ClientDescribeDirectoriesResponseTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseTypeDef",
    {
        "DirectoryDescriptions": List[
            ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeDirectoriesResponseTypeDef(
    _ClientDescribeDirectoriesResponseTypeDef
):
    """
    Type definition for `ClientDescribeDirectories` `Response`

    Contains the results of the  DescribeDirectories operation.

    - **DirectoryDescriptions** *(list) --*

      The list of  DirectoryDescription objects that were retrieved.

      It is possible that this list contains less than the number of items specified in the
      ``Limit`` member of the request. This occurs if there are less than the requested number of
      items left to retrieve, or if the limitations of the operation have been exceeded.

      - *(dict) --*

        Contains information about an AWS Directory Service directory.

        - **DirectoryId** *(string) --*

          The directory identifier.

        - **Name** *(string) --*

          The fully qualified name of the directory.

        - **ShortName** *(string) --*

          The short name of the directory.

        - **Size** *(string) --*

          The directory size.

        - **Edition** *(string) --*

          The edition associated with this directory.

        - **Alias** *(string) --*

          The alias for the directory. If no alias has been created for the directory, the alias is
          the directory identifier, such as ``d-XXXXXXXXXX`` .

        - **AccessUrl** *(string) --*

          The access URL for the directory, such as ``http://<alias>.awsapps.com`` . If no alias
          has been created for the directory, ``<alias>`` is the directory identifier, such as
          ``d-XXXXXXXXXX`` .

        - **Description** *(string) --*

          The textual description for the directory.

        - **DnsIpAddrs** *(list) --*

          The IP addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD
          directory, these are the IP addresses of the Simple AD or Microsoft AD directory servers.
          For an AD Connector directory, these are the IP addresses of the DNS servers or domain
          controllers in the on-premises directory to which the AD Connector is connected.

          - *(string) --*

        - **Stage** *(string) --*

          The current stage of the directory.

        - **ShareStatus** *(string) --*

          Current directory status of the shared AWS Managed Microsoft AD directory.

        - **ShareMethod** *(string) --*

          The method used when sharing a directory to determine whether the directory should be
          shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by
          sending a shared directory request (``HANDSHAKE`` ).

        - **ShareNotes** *(string) --*

          A directory share request that is sent by the directory owner to the directory consumer.
          The request includes a typed message to help the directory consumer administrator
          determine whether to approve or reject the share invitation.

        - **LaunchTime** *(datetime) --*

          Specifies when the directory was created.

        - **StageLastUpdatedDateTime** *(datetime) --*

          The date and time that the stage was last updated.

        - **Type** *(string) --*

          The directory size.

        - **VpcSettings** *(dict) --*

          A  DirectoryVpcSettingsDescription object that contains additional information about a
          directory. This member is only present if the directory is a Simple AD or Managed AD
          directory.

          - **VpcId** *(string) --*

            The identifier of the VPC that the directory is in.

          - **SubnetIds** *(list) --*

            The identifiers of the subnets for the directory servers.

            - *(string) --*

          - **SecurityGroupId** *(string) --*

            The domain controller security group identifier for the directory.

          - **AvailabilityZones** *(list) --*

            The list of Availability Zones that the directory is in.

            - *(string) --*

        - **ConnectSettings** *(dict) --*

          A  DirectoryConnectSettingsDescription object that contains additional information about
          an AD Connector directory. This member is only present if the directory is an AD
          Connector directory.

          - **VpcId** *(string) --*

            The identifier of the VPC that the AD Connector is in.

          - **SubnetIds** *(list) --*

            A list of subnet identifiers in the VPC that the AD connector is in.

            - *(string) --*

          - **CustomerUserName** *(string) --*

            The user name of the service account in the on-premises directory.

          - **SecurityGroupId** *(string) --*

            The security group identifier for the AD Connector directory.

          - **AvailabilityZones** *(list) --*

            A list of the Availability Zones that the directory is in.

            - *(string) --*

          - **ConnectIps** *(list) --*

            The IP addresses of the AD Connector servers.

            - *(string) --*

        - **RadiusSettings** *(dict) --*

          A  RadiusSettings object that contains information about the RADIUS server configured for
          this directory.

          - **RadiusServers** *(list) --*

            An array of strings that contains the IP addresses of the RADIUS server endpoints, or
            the IP addresses of your RADIUS server load balancer.

            - *(string) --*

          - **RadiusPort** *(integer) --*

            The port that your RADIUS server is using for communications. Your on-premises network
            must allow inbound traffic over this port from the AWS Directory Service servers.

          - **RadiusTimeout** *(integer) --*

            The amount of time, in seconds, to wait for the RADIUS server to respond.

          - **RadiusRetries** *(integer) --*

            The maximum number of times that communication with the RADIUS server is attempted.

          - **SharedSecret** *(string) --*

            Required for enabling RADIUS on the directory.

          - **AuthenticationProtocol** *(string) --*

            The protocol specified for your RADIUS endpoints.

          - **DisplayLabel** *(string) --*

            Not currently used.

          - **UseSameUsername** *(boolean) --*

            Not currently used.

        - **RadiusStatus** *(string) --*

          The status of the RADIUS MFA server connection.

        - **StageReason** *(string) --*

          Additional information about the directory stage.

        - **SsoEnabled** *(boolean) --*

          Indicates if single sign-on is enabled for the directory. For more information, see
          EnableSso and  DisableSso .

        - **DesiredNumberOfDomainControllers** *(integer) --*

          The desired number of domain controllers in the directory if the directory is Microsoft
          AD.

        - **OwnerDirectoryDescription** *(dict) --*

          Describes the AWS Managed Microsoft AD directory in the directory owner account.

          - **DirectoryId** *(string) --*

            Identifier of the AWS Managed Microsoft AD directory in the directory owner account.

          - **AccountId** *(string) --*

            Identifier of the directory owner account.

          - **DnsIpAddrs** *(list) --*

            IP address of the directory’s domain controllers.

            - *(string) --*

          - **VpcSettings** *(dict) --*

            Information about the VPC settings for the directory.

            - **VpcId** *(string) --*

              The identifier of the VPC that the directory is in.

            - **SubnetIds** *(list) --*

              The identifiers of the subnets for the directory servers.

              - *(string) --*

            - **SecurityGroupId** *(string) --*

              The domain controller security group identifier for the directory.

            - **AvailabilityZones** *(list) --*

              The list of Availability Zones that the directory is in.

              - *(string) --*

          - **RadiusSettings** *(dict) --*

            A  RadiusSettings object that contains information about the RADIUS server.

            - **RadiusServers** *(list) --*

              An array of strings that contains the IP addresses of the RADIUS server endpoints, or
              the IP addresses of your RADIUS server load balancer.

              - *(string) --*

            - **RadiusPort** *(integer) --*

              The port that your RADIUS server is using for communications. Your on-premises
              network must allow inbound traffic over this port from the AWS Directory Service
              servers.

            - **RadiusTimeout** *(integer) --*

              The amount of time, in seconds, to wait for the RADIUS server to respond.

            - **RadiusRetries** *(integer) --*

              The maximum number of times that communication with the RADIUS server is attempted.

            - **SharedSecret** *(string) --*

              Required for enabling RADIUS on the directory.

            - **AuthenticationProtocol** *(string) --*

              The protocol specified for your RADIUS endpoints.

            - **DisplayLabel** *(string) --*

              Not currently used.

            - **UseSameUsername** *(boolean) --*

              Not currently used.

          - **RadiusStatus** *(string) --*

            Information about the status of the RADIUS server.

    - **NextToken** *(string) --*

      If not null, more results are available. Pass this value for the ``NextToken`` parameter in a
      subsequent call to  DescribeDirectories to retrieve the next set of items.
    """


_ClientDescribeDomainControllersResponseDomainControllersTypeDef = TypedDict(
    "_ClientDescribeDomainControllersResponseDomainControllersTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerId": str,
        "DnsIpAddr": str,
        "VpcId": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "Status": str,
        "StatusReason": str,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeDomainControllersResponseDomainControllersTypeDef(
    _ClientDescribeDomainControllersResponseDomainControllersTypeDef
):
    """
    Type definition for `ClientDescribeDomainControllersResponse` `DomainControllers`

    Contains information about the domain controllers for a specified directory.

    - **DirectoryId** *(string) --*

      Identifier of the directory where the domain controller resides.

    - **DomainControllerId** *(string) --*

      Identifies a specific domain controller in the directory.

    - **DnsIpAddr** *(string) --*

      The IP address of the domain controller.

    - **VpcId** *(string) --*

      The identifier of the VPC that contains the domain controller.

    - **SubnetId** *(string) --*

      Identifier of the subnet in the VPC that contains the domain controller.

    - **AvailabilityZone** *(string) --*

      The Availability Zone where the domain controller is located.

    - **Status** *(string) --*

      The status of the domain controller.

    - **StatusReason** *(string) --*

      A description of the domain controller state.

    - **LaunchTime** *(datetime) --*

      Specifies when the domain controller was created.

    - **StatusLastUpdatedDateTime** *(datetime) --*

      The date and time that the status was last updated.
    """


_ClientDescribeDomainControllersResponseTypeDef = TypedDict(
    "_ClientDescribeDomainControllersResponseTypeDef",
    {
        "DomainControllers": List[
            ClientDescribeDomainControllersResponseDomainControllersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeDomainControllersResponseTypeDef(
    _ClientDescribeDomainControllersResponseTypeDef
):
    """
    Type definition for `ClientDescribeDomainControllers` `Response`

    - **DomainControllers** *(list) --*

      List of the  DomainController objects that were retrieved.

      - *(dict) --*

        Contains information about the domain controllers for a specified directory.

        - **DirectoryId** *(string) --*

          Identifier of the directory where the domain controller resides.

        - **DomainControllerId** *(string) --*

          Identifies a specific domain controller in the directory.

        - **DnsIpAddr** *(string) --*

          The IP address of the domain controller.

        - **VpcId** *(string) --*

          The identifier of the VPC that contains the domain controller.

        - **SubnetId** *(string) --*

          Identifier of the subnet in the VPC that contains the domain controller.

        - **AvailabilityZone** *(string) --*

          The Availability Zone where the domain controller is located.

        - **Status** *(string) --*

          The status of the domain controller.

        - **StatusReason** *(string) --*

          A description of the domain controller state.

        - **LaunchTime** *(datetime) --*

          Specifies when the domain controller was created.

        - **StatusLastUpdatedDateTime** *(datetime) --*

          The date and time that the status was last updated.

    - **NextToken** *(string) --*

      If not null, more results are available. Pass this value for the ``NextToken`` parameter in a
      subsequent call to  DescribeDomainControllers retrieve the next set of items.
    """


_ClientDescribeEventTopicsResponseEventTopicsTypeDef = TypedDict(
    "_ClientDescribeEventTopicsResponseEventTopicsTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
        "TopicArn": str,
        "CreatedDateTime": datetime,
        "Status": str,
    },
    total=False,
)


class ClientDescribeEventTopicsResponseEventTopicsTypeDef(
    _ClientDescribeEventTopicsResponseEventTopicsTypeDef
):
    """
    Type definition for `ClientDescribeEventTopicsResponse` `EventTopics`

    Information about SNS topic and AWS Directory Service directory associations.

    - **DirectoryId** *(string) --*

      The Directory ID of an AWS Directory Service directory that will publish status messages
      to an SNS topic.

    - **TopicName** *(string) --*

      The name of an AWS SNS topic the receives status messages from the directory.

    - **TopicArn** *(string) --*

      The SNS topic ARN (Amazon Resource Name).

    - **CreatedDateTime** *(datetime) --*

      The date and time of when you associated your directory with the SNS topic.

    - **Status** *(string) --*

      The topic registration status.
    """


_ClientDescribeEventTopicsResponseTypeDef = TypedDict(
    "_ClientDescribeEventTopicsResponseTypeDef",
    {"EventTopics": List[ClientDescribeEventTopicsResponseEventTopicsTypeDef]},
    total=False,
)


class ClientDescribeEventTopicsResponseTypeDef(
    _ClientDescribeEventTopicsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEventTopics` `Response`

    The result of a DescribeEventTopic request.

    - **EventTopics** *(list) --*

      A list of SNS topic names that receive status messages from the specified Directory ID.

      - *(dict) --*

        Information about SNS topic and AWS Directory Service directory associations.

        - **DirectoryId** *(string) --*

          The Directory ID of an AWS Directory Service directory that will publish status messages
          to an SNS topic.

        - **TopicName** *(string) --*

          The name of an AWS SNS topic the receives status messages from the directory.

        - **TopicArn** *(string) --*

          The SNS topic ARN (Amazon Resource Name).

        - **CreatedDateTime** *(datetime) --*

          The date and time of when you associated your directory with the SNS topic.

        - **Status** *(string) --*

          The topic registration status.
    """


_ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef = TypedDict(
    "_ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": str,
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": str,
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef(
    _ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef
):
    """
    Type definition for `ClientDescribeSharedDirectoriesResponse` `SharedDirectories`

    Details about the shared directory in the directory owner account for which the share
    request in the directory consumer account has been accepted.

    - **OwnerAccountId** *(string) --*

      Identifier of the directory owner account, which contains the directory that has been
      shared to the consumer account.

    - **OwnerDirectoryId** *(string) --*

      Identifier of the directory in the directory owner account.

    - **ShareMethod** *(string) --*

      The method used when sharing a directory to determine whether the directory should be
      shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by
      sending a shared directory request (``HANDSHAKE`` ).

    - **SharedAccountId** *(string) --*

      Identifier of the directory consumer account that has access to the shared directory
      (``OwnerDirectoryId`` ) in the directory owner account.

    - **SharedDirectoryId** *(string) --*

      Identifier of the shared directory in the directory consumer account. This identifier is
      different for each directory owner account.

    - **ShareStatus** *(string) --*

      Current directory status of the shared AWS Managed Microsoft AD directory.

    - **ShareNotes** *(string) --*

      A directory share request that is sent by the directory owner to the directory consumer.
      The request includes a typed message to help the directory consumer administrator
      determine whether to approve or reject the share invitation.

    - **CreatedDateTime** *(datetime) --*

      The date and time that the shared directory was created.

    - **LastUpdatedDateTime** *(datetime) --*

      The date and time that the shared directory was last updated.
    """


_ClientDescribeSharedDirectoriesResponseTypeDef = TypedDict(
    "_ClientDescribeSharedDirectoriesResponseTypeDef",
    {
        "SharedDirectories": List[
            ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeSharedDirectoriesResponseTypeDef(
    _ClientDescribeSharedDirectoriesResponseTypeDef
):
    """
    Type definition for `ClientDescribeSharedDirectories` `Response`

    - **SharedDirectories** *(list) --*

      A list of all shared directories in your account.

      - *(dict) --*

        Details about the shared directory in the directory owner account for which the share
        request in the directory consumer account has been accepted.

        - **OwnerAccountId** *(string) --*

          Identifier of the directory owner account, which contains the directory that has been
          shared to the consumer account.

        - **OwnerDirectoryId** *(string) --*

          Identifier of the directory in the directory owner account.

        - **ShareMethod** *(string) --*

          The method used when sharing a directory to determine whether the directory should be
          shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by
          sending a shared directory request (``HANDSHAKE`` ).

        - **SharedAccountId** *(string) --*

          Identifier of the directory consumer account that has access to the shared directory
          (``OwnerDirectoryId`` ) in the directory owner account.

        - **SharedDirectoryId** *(string) --*

          Identifier of the shared directory in the directory consumer account. This identifier is
          different for each directory owner account.

        - **ShareStatus** *(string) --*

          Current directory status of the shared AWS Managed Microsoft AD directory.

        - **ShareNotes** *(string) --*

          A directory share request that is sent by the directory owner to the directory consumer.
          The request includes a typed message to help the directory consumer administrator
          determine whether to approve or reject the share invitation.

        - **CreatedDateTime** *(datetime) --*

          The date and time that the shared directory was created.

        - **LastUpdatedDateTime** *(datetime) --*

          The date and time that the shared directory was last updated.

    - **NextToken** *(string) --*

      If not null, token that indicates that more results are available. Pass this value for the
      ``NextToken`` parameter in a subsequent call to  DescribeSharedDirectories to retrieve the
      next set of items.
    """


_ClientDescribeSnapshotsResponseSnapshotsTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    {
        "DirectoryId": str,
        "SnapshotId": str,
        "Type": str,
        "Name": str,
        "Status": str,
        "StartTime": datetime,
    },
    total=False,
)


class ClientDescribeSnapshotsResponseSnapshotsTypeDef(
    _ClientDescribeSnapshotsResponseSnapshotsTypeDef
):
    """
    Type definition for `ClientDescribeSnapshotsResponse` `Snapshots`

    Describes a directory snapshot.

    - **DirectoryId** *(string) --*

      The directory identifier.

    - **SnapshotId** *(string) --*

      The snapshot identifier.

    - **Type** *(string) --*

      The snapshot type.

    - **Name** *(string) --*

      The descriptive name of the snapshot.

    - **Status** *(string) --*

      The snapshot status.

    - **StartTime** *(datetime) --*

      The date and time that the snapshot was taken.
    """


_ClientDescribeSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseTypeDef",
    {
        "Snapshots": List[ClientDescribeSnapshotsResponseSnapshotsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeSnapshotsResponseTypeDef(_ClientDescribeSnapshotsResponseTypeDef):
    """
    Type definition for `ClientDescribeSnapshots` `Response`

    Contains the results of the  DescribeSnapshots operation.

    - **Snapshots** *(list) --*

      The list of  Snapshot objects that were retrieved.

      It is possible that this list contains less than the number of items specified in the *Limit*
      member of the request. This occurs if there are less than the requested number of items left
      to retrieve, or if the limitations of the operation have been exceeded.

      - *(dict) --*

        Describes a directory snapshot.

        - **DirectoryId** *(string) --*

          The directory identifier.

        - **SnapshotId** *(string) --*

          The snapshot identifier.

        - **Type** *(string) --*

          The snapshot type.

        - **Name** *(string) --*

          The descriptive name of the snapshot.

        - **Status** *(string) --*

          The snapshot status.

        - **StartTime** *(datetime) --*

          The date and time that the snapshot was taken.

    - **NextToken** *(string) --*

      If not null, more results are available. Pass this value in the *NextToken* member of a
      subsequent call to  DescribeSnapshots .
    """


_ClientDescribeTrustsResponseTrustsTypeDef = TypedDict(
    "_ClientDescribeTrustsResponseTrustsTypeDef",
    {
        "DirectoryId": str,
        "TrustId": str,
        "RemoteDomainName": str,
        "TrustType": str,
        "TrustDirection": str,
        "TrustState": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
        "StateLastUpdatedDateTime": datetime,
        "TrustStateReason": str,
        "SelectiveAuth": str,
    },
    total=False,
)


class ClientDescribeTrustsResponseTrustsTypeDef(
    _ClientDescribeTrustsResponseTrustsTypeDef
):
    """
    Type definition for `ClientDescribeTrustsResponse` `Trusts`

    Describes a trust relationship between an AWS Managed Microsoft AD directory and an
    external domain.

    - **DirectoryId** *(string) --*

      The Directory ID of the AWS directory involved in the trust relationship.

    - **TrustId** *(string) --*

      The unique ID of the trust relationship.

    - **RemoteDomainName** *(string) --*

      The Fully Qualified Domain Name (FQDN) of the external domain involved in the trust
      relationship.

    - **TrustType** *(string) --*

      The trust relationship type. ``Forest`` is the default.

    - **TrustDirection** *(string) --*

      The trust relationship direction.

    - **TrustState** *(string) --*

      The trust relationship state.

    - **CreatedDateTime** *(datetime) --*

      The date and time that the trust relationship was created.

    - **LastUpdatedDateTime** *(datetime) --*

      The date and time that the trust relationship was last updated.

    - **StateLastUpdatedDateTime** *(datetime) --*

      The date and time that the TrustState was last updated.

    - **TrustStateReason** *(string) --*

      The reason for the TrustState.

    - **SelectiveAuth** *(string) --*

      Current state of selective authentication for the trust.
    """


_ClientDescribeTrustsResponseTypeDef = TypedDict(
    "_ClientDescribeTrustsResponseTypeDef",
    {"Trusts": List[ClientDescribeTrustsResponseTrustsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeTrustsResponseTypeDef(_ClientDescribeTrustsResponseTypeDef):
    """
    Type definition for `ClientDescribeTrusts` `Response`

    The result of a DescribeTrust request.

    - **Trusts** *(list) --*

      The list of Trust objects that were retrieved.

      It is possible that this list contains less than the number of items specified in the *Limit*
      member of the request. This occurs if there are less than the requested number of items left
      to retrieve, or if the limitations of the operation have been exceeded.

      - *(dict) --*

        Describes a trust relationship between an AWS Managed Microsoft AD directory and an
        external domain.

        - **DirectoryId** *(string) --*

          The Directory ID of the AWS directory involved in the trust relationship.

        - **TrustId** *(string) --*

          The unique ID of the trust relationship.

        - **RemoteDomainName** *(string) --*

          The Fully Qualified Domain Name (FQDN) of the external domain involved in the trust
          relationship.

        - **TrustType** *(string) --*

          The trust relationship type. ``Forest`` is the default.

        - **TrustDirection** *(string) --*

          The trust relationship direction.

        - **TrustState** *(string) --*

          The trust relationship state.

        - **CreatedDateTime** *(datetime) --*

          The date and time that the trust relationship was created.

        - **LastUpdatedDateTime** *(datetime) --*

          The date and time that the trust relationship was last updated.

        - **StateLastUpdatedDateTime** *(datetime) --*

          The date and time that the TrustState was last updated.

        - **TrustStateReason** *(string) --*

          The reason for the TrustState.

        - **SelectiveAuth** *(string) --*

          Current state of selective authentication for the trust.

    - **NextToken** *(string) --*

      If not null, more results are available. Pass this value for the *NextToken* parameter in a
      subsequent call to  DescribeTrusts to retrieve the next set of items.
    """


_ClientEnableRadiusRadiusSettingsTypeDef = TypedDict(
    "_ClientEnableRadiusRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": str,
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class ClientEnableRadiusRadiusSettingsTypeDef(_ClientEnableRadiusRadiusSettingsTypeDef):
    """
    Type definition for `ClientEnableRadius` `RadiusSettings`

    A  RadiusSettings object that contains information about the RADIUS server.

    - **RadiusServers** *(list) --*

      An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP
      addresses of your RADIUS server load balancer.

      - *(string) --*

    - **RadiusPort** *(integer) --*

      The port that your RADIUS server is using for communications. Your on-premises network must
      allow inbound traffic over this port from the AWS Directory Service servers.

    - **RadiusTimeout** *(integer) --*

      The amount of time, in seconds, to wait for the RADIUS server to respond.

    - **RadiusRetries** *(integer) --*

      The maximum number of times that communication with the RADIUS server is attempted.

    - **SharedSecret** *(string) --*

      Required for enabling RADIUS on the directory.

    - **AuthenticationProtocol** *(string) --*

      The protocol specified for your RADIUS endpoints.

    - **DisplayLabel** *(string) --*

      Not currently used.

    - **UseSameUsername** *(boolean) --*

      Not currently used.
    """


_ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef = TypedDict(
    "_ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef",
    {
        "CloudOnlyDirectoriesLimit": int,
        "CloudOnlyDirectoriesCurrentCount": int,
        "CloudOnlyDirectoriesLimitReached": bool,
        "CloudOnlyMicrosoftADLimit": int,
        "CloudOnlyMicrosoftADCurrentCount": int,
        "CloudOnlyMicrosoftADLimitReached": bool,
        "ConnectedDirectoriesLimit": int,
        "ConnectedDirectoriesCurrentCount": int,
        "ConnectedDirectoriesLimitReached": bool,
    },
    total=False,
)


class ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef(
    _ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef
):
    """
    Type definition for `ClientGetDirectoryLimitsResponse` `DirectoryLimits`

    A  DirectoryLimits object that contains the directory limits for the current region.

    - **CloudOnlyDirectoriesLimit** *(integer) --*

      The maximum number of cloud directories allowed in the region.

    - **CloudOnlyDirectoriesCurrentCount** *(integer) --*

      The current number of cloud directories in the region.

    - **CloudOnlyDirectoriesLimitReached** *(boolean) --*

      Indicates if the cloud directory limit has been reached.

    - **CloudOnlyMicrosoftADLimit** *(integer) --*

      The maximum number of AWS Managed Microsoft AD directories allowed in the region.

    - **CloudOnlyMicrosoftADCurrentCount** *(integer) --*

      The current number of AWS Managed Microsoft AD directories in the region.

    - **CloudOnlyMicrosoftADLimitReached** *(boolean) --*

      Indicates if the AWS Managed Microsoft AD directory limit has been reached.

    - **ConnectedDirectoriesLimit** *(integer) --*

      The maximum number of connected directories allowed in the region.

    - **ConnectedDirectoriesCurrentCount** *(integer) --*

      The current number of connected directories in the region.

    - **ConnectedDirectoriesLimitReached** *(boolean) --*

      Indicates if the connected directory limit has been reached.
    """


_ClientGetDirectoryLimitsResponseTypeDef = TypedDict(
    "_ClientGetDirectoryLimitsResponseTypeDef",
    {"DirectoryLimits": ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef},
    total=False,
)


class ClientGetDirectoryLimitsResponseTypeDef(_ClientGetDirectoryLimitsResponseTypeDef):
    """
    Type definition for `ClientGetDirectoryLimits` `Response`

    Contains the results of the  GetDirectoryLimits operation.

    - **DirectoryLimits** *(dict) --*

      A  DirectoryLimits object that contains the directory limits for the current region.

      - **CloudOnlyDirectoriesLimit** *(integer) --*

        The maximum number of cloud directories allowed in the region.

      - **CloudOnlyDirectoriesCurrentCount** *(integer) --*

        The current number of cloud directories in the region.

      - **CloudOnlyDirectoriesLimitReached** *(boolean) --*

        Indicates if the cloud directory limit has been reached.

      - **CloudOnlyMicrosoftADLimit** *(integer) --*

        The maximum number of AWS Managed Microsoft AD directories allowed in the region.

      - **CloudOnlyMicrosoftADCurrentCount** *(integer) --*

        The current number of AWS Managed Microsoft AD directories in the region.

      - **CloudOnlyMicrosoftADLimitReached** *(boolean) --*

        Indicates if the AWS Managed Microsoft AD directory limit has been reached.

      - **ConnectedDirectoriesLimit** *(integer) --*

        The maximum number of connected directories allowed in the region.

      - **ConnectedDirectoriesCurrentCount** *(integer) --*

        The current number of connected directories in the region.

      - **ConnectedDirectoriesLimitReached** *(boolean) --*

        Indicates if the connected directory limit has been reached.
    """


_ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef = TypedDict(
    "_ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef",
    {
        "ManualSnapshotsLimit": int,
        "ManualSnapshotsCurrentCount": int,
        "ManualSnapshotsLimitReached": bool,
    },
    total=False,
)


class ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef(
    _ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef
):
    """
    Type definition for `ClientGetSnapshotLimitsResponse` `SnapshotLimits`

    A  SnapshotLimits object that contains the manual snapshot limits for the specified directory.

    - **ManualSnapshotsLimit** *(integer) --*

      The maximum number of manual snapshots allowed.

    - **ManualSnapshotsCurrentCount** *(integer) --*

      The current number of manual snapshots of the directory.

    - **ManualSnapshotsLimitReached** *(boolean) --*

      Indicates if the manual snapshot limit has been reached.
    """


_ClientGetSnapshotLimitsResponseTypeDef = TypedDict(
    "_ClientGetSnapshotLimitsResponseTypeDef",
    {"SnapshotLimits": ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef},
    total=False,
)


class ClientGetSnapshotLimitsResponseTypeDef(_ClientGetSnapshotLimitsResponseTypeDef):
    """
    Type definition for `ClientGetSnapshotLimits` `Response`

    Contains the results of the  GetSnapshotLimits operation.

    - **SnapshotLimits** *(dict) --*

      A  SnapshotLimits object that contains the manual snapshot limits for the specified directory.

      - **ManualSnapshotsLimit** *(integer) --*

        The maximum number of manual snapshots allowed.

      - **ManualSnapshotsCurrentCount** *(integer) --*

        The current number of manual snapshots of the directory.

      - **ManualSnapshotsLimitReached** *(boolean) --*

        Indicates if the manual snapshot limit has been reached.
    """


_ClientListIpRoutesResponseIpRoutesInfoTypeDef = TypedDict(
    "_ClientListIpRoutesResponseIpRoutesInfoTypeDef",
    {
        "DirectoryId": str,
        "CidrIp": str,
        "IpRouteStatusMsg": str,
        "AddedDateTime": datetime,
        "IpRouteStatusReason": str,
        "Description": str,
    },
    total=False,
)


class ClientListIpRoutesResponseIpRoutesInfoTypeDef(
    _ClientListIpRoutesResponseIpRoutesInfoTypeDef
):
    """
    Type definition for `ClientListIpRoutesResponse` `IpRoutesInfo`

    Information about one or more IP address blocks.

    - **DirectoryId** *(string) --*

      Identifier (ID) of the directory associated with the IP addresses.

    - **CidrIp** *(string) --*

      IP address block in the  IpRoute .

    - **IpRouteStatusMsg** *(string) --*

      The status of the IP address block.

    - **AddedDateTime** *(datetime) --*

      The date and time the address block was added to the directory.

    - **IpRouteStatusReason** *(string) --*

      The reason for the IpRouteStatusMsg.

    - **Description** *(string) --*

      Description of the  IpRouteInfo .
    """


_ClientListIpRoutesResponseTypeDef = TypedDict(
    "_ClientListIpRoutesResponseTypeDef",
    {
        "IpRoutesInfo": List[ClientListIpRoutesResponseIpRoutesInfoTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListIpRoutesResponseTypeDef(_ClientListIpRoutesResponseTypeDef):
    """
    Type definition for `ClientListIpRoutes` `Response`

    - **IpRoutesInfo** *(list) --*

      A list of  IpRoute s.

      - *(dict) --*

        Information about one or more IP address blocks.

        - **DirectoryId** *(string) --*

          Identifier (ID) of the directory associated with the IP addresses.

        - **CidrIp** *(string) --*

          IP address block in the  IpRoute .

        - **IpRouteStatusMsg** *(string) --*

          The status of the IP address block.

        - **AddedDateTime** *(datetime) --*

          The date and time the address block was added to the directory.

        - **IpRouteStatusReason** *(string) --*

          The reason for the IpRouteStatusMsg.

        - **Description** *(string) --*

          Description of the  IpRouteInfo .

    - **NextToken** *(string) --*

      If not null, more results are available. Pass this value for the *NextToken* parameter in a
      subsequent call to  ListIpRoutes to retrieve the next set of items.
    """


_ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef = TypedDict(
    "_ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef",
    {"DirectoryId": str, "LogGroupName": str, "SubscriptionCreatedDateTime": datetime},
    total=False,
)


class ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef(
    _ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef
):
    """
    Type definition for `ClientListLogSubscriptionsResponse` `LogSubscriptions`

    Represents a log subscription, which tracks real-time data from a chosen log group to a
    specified destination.

    - **DirectoryId** *(string) --*

      Identifier (ID) of the directory that you want to associate with the log subscription.

    - **LogGroupName** *(string) --*

      The name of the log group.

    - **SubscriptionCreatedDateTime** *(datetime) --*

      The date and time that the log subscription was created.
    """


_ClientListLogSubscriptionsResponseTypeDef = TypedDict(
    "_ClientListLogSubscriptionsResponseTypeDef",
    {
        "LogSubscriptions": List[
            ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListLogSubscriptionsResponseTypeDef(
    _ClientListLogSubscriptionsResponseTypeDef
):
    """
    Type definition for `ClientListLogSubscriptions` `Response`

    - **LogSubscriptions** *(list) --*

      A list of active  LogSubscription objects for calling the AWS account.

      - *(dict) --*

        Represents a log subscription, which tracks real-time data from a chosen log group to a
        specified destination.

        - **DirectoryId** *(string) --*

          Identifier (ID) of the directory that you want to associate with the log subscription.

        - **LogGroupName** *(string) --*

          The name of the log group.

        - **SubscriptionCreatedDateTime** *(datetime) --*

          The date and time that the log subscription was created.

    - **NextToken** *(string) --*

      The token for the next set of items to return.
    """


_ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef = TypedDict(
    "_ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
        "Description": str,
        "SchemaExtensionStatus": str,
        "SchemaExtensionStatusReason": str,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)


class ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef(
    _ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef
):
    """
    Type definition for `ClientListSchemaExtensionsResponse` `SchemaExtensionsInfo`

    Information about a schema extension.

    - **DirectoryId** *(string) --*

      The identifier of the directory to which the schema extension is applied.

    - **SchemaExtensionId** *(string) --*

      The identifier of the schema extension.

    - **Description** *(string) --*

      A description of the schema extension.

    - **SchemaExtensionStatus** *(string) --*

      The current status of the schema extension.

    - **SchemaExtensionStatusReason** *(string) --*

      The reason for the ``SchemaExtensionStatus`` .

    - **StartDateTime** *(datetime) --*

      The date and time that the schema extension started being applied to the directory.

    - **EndDateTime** *(datetime) --*

      The date and time that the schema extension was completed.
    """


_ClientListSchemaExtensionsResponseTypeDef = TypedDict(
    "_ClientListSchemaExtensionsResponseTypeDef",
    {
        "SchemaExtensionsInfo": List[
            ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSchemaExtensionsResponseTypeDef(
    _ClientListSchemaExtensionsResponseTypeDef
):
    """
    Type definition for `ClientListSchemaExtensions` `Response`

    - **SchemaExtensionsInfo** *(list) --*

      Information about the schema extensions applied to the directory.

      - *(dict) --*

        Information about a schema extension.

        - **DirectoryId** *(string) --*

          The identifier of the directory to which the schema extension is applied.

        - **SchemaExtensionId** *(string) --*

          The identifier of the schema extension.

        - **Description** *(string) --*

          A description of the schema extension.

        - **SchemaExtensionStatus** *(string) --*

          The current status of the schema extension.

        - **SchemaExtensionStatusReason** *(string) --*

          The reason for the ``SchemaExtensionStatus`` .

        - **StartDateTime** *(datetime) --*

          The date and time that the schema extension started being applied to the directory.

        - **EndDateTime** *(datetime) --*

          The date and time that the schema extension was completed.

    - **NextToken** *(string) --*

      If not null, more results are available. Pass this value for the ``NextToken`` parameter in a
      subsequent call to ``ListSchemaExtensions`` to retrieve the next set of items.
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

    Metadata assigned to a directory consisting of a key-value pair.

    - **Key** *(string) --*

      Required name of the tag. The string value can be Unicode characters and cannot be
      prefixed with "aws:". The string can contain only the set of Unicode letters, digits,
      white-space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be Unicode characters. The string can
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
      '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
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

    - **Tags** *(list) --*

      List of tags returned by the ListTagsForResource operation.

      - *(dict) --*

        Metadata assigned to a directory consisting of a key-value pair.

        - **Key** *(string) --*

          Required name of the tag. The string value can be Unicode characters and cannot be
          prefixed with "aws:". The string can contain only the set of Unicode letters, digits,
          white-space, '_', '.', '/', '=', '+', '-' (Java regex:
          "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        - **Value** *(string) --*

          The optional value of the tag. The string value can be Unicode characters. The string can
          contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
          '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **NextToken** *(string) --*

      Reserved for future use.
    """


_ClientRejectSharedDirectoryResponseTypeDef = TypedDict(
    "_ClientRejectSharedDirectoryResponseTypeDef",
    {"SharedDirectoryId": str},
    total=False,
)


class ClientRejectSharedDirectoryResponseTypeDef(
    _ClientRejectSharedDirectoryResponseTypeDef
):
    """
    Type definition for `ClientRejectSharedDirectory` `Response`

    - **SharedDirectoryId** *(string) --*

      Identifier of the shared directory in the directory consumer account.
    """


_ClientShareDirectoryResponseTypeDef = TypedDict(
    "_ClientShareDirectoryResponseTypeDef", {"SharedDirectoryId": str}, total=False
)


class ClientShareDirectoryResponseTypeDef(_ClientShareDirectoryResponseTypeDef):
    """
    Type definition for `ClientShareDirectory` `Response`

    - **SharedDirectoryId** *(string) --*

      Identifier of the directory that is stored in the directory consumer account that is shared
      from the specified directory (``DirectoryId`` ).
    """


_ClientShareDirectoryShareTargetTypeDef = TypedDict(
    "_ClientShareDirectoryShareTargetTypeDef", {"Id": str, "Type": str}
)


class ClientShareDirectoryShareTargetTypeDef(_ClientShareDirectoryShareTargetTypeDef):
    """
    Type definition for `ClientShareDirectory` `ShareTarget`

    Identifier for the directory consumer account with whom the directory is to be shared.

    - **Id** *(string) --* **[REQUIRED]**

      Identifier of the directory consumer account.

    - **Type** *(string) --* **[REQUIRED]**

      Type of identifier to be used in the ``Id`` field.
    """


_ClientStartSchemaExtensionResponseTypeDef = TypedDict(
    "_ClientStartSchemaExtensionResponseTypeDef",
    {"SchemaExtensionId": str},
    total=False,
)


class ClientStartSchemaExtensionResponseTypeDef(
    _ClientStartSchemaExtensionResponseTypeDef
):
    """
    Type definition for `ClientStartSchemaExtension` `Response`

    - **SchemaExtensionId** *(string) --*

      The identifier of the schema extension that will be applied.
    """


_ClientUnshareDirectoryResponseTypeDef = TypedDict(
    "_ClientUnshareDirectoryResponseTypeDef", {"SharedDirectoryId": str}, total=False
)


class ClientUnshareDirectoryResponseTypeDef(_ClientUnshareDirectoryResponseTypeDef):
    """
    Type definition for `ClientUnshareDirectory` `Response`

    - **SharedDirectoryId** *(string) --*

      Identifier of the directory stored in the directory consumer account that is to be unshared
      from the specified directory (``DirectoryId`` ).
    """


_ClientUnshareDirectoryUnshareTargetTypeDef = TypedDict(
    "_ClientUnshareDirectoryUnshareTargetTypeDef", {"Id": str, "Type": str}
)


class ClientUnshareDirectoryUnshareTargetTypeDef(
    _ClientUnshareDirectoryUnshareTargetTypeDef
):
    """
    Type definition for `ClientUnshareDirectory` `UnshareTarget`

    Identifier for the directory consumer account with whom the directory has to be unshared.

    - **Id** *(string) --* **[REQUIRED]**

      Identifier of the directory consumer account.

    - **Type** *(string) --* **[REQUIRED]**

      Type of identifier to be used in the *Id* field.
    """


_ClientUpdateRadiusRadiusSettingsTypeDef = TypedDict(
    "_ClientUpdateRadiusRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": str,
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class ClientUpdateRadiusRadiusSettingsTypeDef(_ClientUpdateRadiusRadiusSettingsTypeDef):
    """
    Type definition for `ClientUpdateRadius` `RadiusSettings`

    A  RadiusSettings object that contains information about the RADIUS server.

    - **RadiusServers** *(list) --*

      An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP
      addresses of your RADIUS server load balancer.

      - *(string) --*

    - **RadiusPort** *(integer) --*

      The port that your RADIUS server is using for communications. Your on-premises network must
      allow inbound traffic over this port from the AWS Directory Service servers.

    - **RadiusTimeout** *(integer) --*

      The amount of time, in seconds, to wait for the RADIUS server to respond.

    - **RadiusRetries** *(integer) --*

      The maximum number of times that communication with the RADIUS server is attempted.

    - **SharedSecret** *(string) --*

      Required for enabling RADIUS on the directory.

    - **AuthenticationProtocol** *(string) --*

      The protocol specified for your RADIUS endpoints.

    - **DisplayLabel** *(string) --*

      Not currently used.

    - **UseSameUsername** *(boolean) --*

      Not currently used.
    """


_ClientUpdateTrustResponseTypeDef = TypedDict(
    "_ClientUpdateTrustResponseTypeDef", {"RequestId": str, "TrustId": str}, total=False
)


class ClientUpdateTrustResponseTypeDef(_ClientUpdateTrustResponseTypeDef):
    """
    Type definition for `ClientUpdateTrust` `Response`

    - **RequestId** *(string) --*

      The AWS request identifier.

    - **TrustId** *(string) --*

      Identifier of the trust relationship.
    """


_ClientVerifyTrustResponseTypeDef = TypedDict(
    "_ClientVerifyTrustResponseTypeDef", {"TrustId": str}, total=False
)


class ClientVerifyTrustResponseTypeDef(_ClientVerifyTrustResponseTypeDef):
    """
    Type definition for `ClientVerifyTrust` `Response`

    Result of a VerifyTrust request.

    - **TrustId** *(string) --*

      The unique Trust ID of the trust relationship that was verified.
    """


_DescribeDirectoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDirectoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDirectoriesPaginatePaginationConfigTypeDef(
    _DescribeDirectoriesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDirectoriesPaginate` `PaginationConfig`

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


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerUserName": str,
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
        "ConnectIps": List[str],
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef
):
    """
    Type definition for `DescribeDirectoriesPaginateResponseDirectoryDescriptions` `ConnectSettings`

    A  DirectoryConnectSettingsDescription object that contains additional information about
    an AD Connector directory. This member is only present if the directory is an AD
    Connector directory.

    - **VpcId** *(string) --*

      The identifier of the VPC that the AD Connector is in.

    - **SubnetIds** *(list) --*

      A list of subnet identifiers in the VPC that the AD connector is in.

      - *(string) --*

    - **CustomerUserName** *(string) --*

      The user name of the service account in the on-premises directory.

    - **SecurityGroupId** *(string) --*

      The security group identifier for the AD Connector directory.

    - **AvailabilityZones** *(list) --*

      A list of the Availability Zones that the directory is in.

      - *(string) --*

    - **ConnectIps** *(list) --*

      The IP addresses of the AD Connector servers.

      - *(string) --*
    """


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": str,
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef
):
    """
    Type definition for `DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescription` `RadiusSettings`

    A  RadiusSettings object that contains information about the RADIUS server.

    - **RadiusServers** *(list) --*

      An array of strings that contains the IP addresses of the RADIUS server endpoints, or
      the IP addresses of your RADIUS server load balancer.

      - *(string) --*

    - **RadiusPort** *(integer) --*

      The port that your RADIUS server is using for communications. Your on-premises
      network must allow inbound traffic over this port from the AWS Directory Service
      servers.

    - **RadiusTimeout** *(integer) --*

      The amount of time, in seconds, to wait for the RADIUS server to respond.

    - **RadiusRetries** *(integer) --*

      The maximum number of times that communication with the RADIUS server is attempted.

    - **SharedSecret** *(string) --*

      Required for enabling RADIUS on the directory.

    - **AuthenticationProtocol** *(string) --*

      The protocol specified for your RADIUS endpoints.

    - **DisplayLabel** *(string) --*

      Not currently used.

    - **UseSameUsername** *(boolean) --*

      Not currently used.
    """


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef
):
    """
    Type definition for `DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescription` `VpcSettings`

    Information about the VPC settings for the directory.

    - **VpcId** *(string) --*

      The identifier of the VPC that the directory is in.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets for the directory servers.

      - *(string) --*

    - **SecurityGroupId** *(string) --*

      The domain controller security group identifier for the directory.

    - **AvailabilityZones** *(list) --*

      The list of Availability Zones that the directory is in.

      - *(string) --*
    """


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "AccountId": str,
        "DnsIpAddrs": List[str],
        "VpcSettings": DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef,
        "RadiusSettings": DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef,
        "RadiusStatus": str,
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef
):
    """
    Type definition for `DescribeDirectoriesPaginateResponseDirectoryDescriptions` `OwnerDirectoryDescription`

    Describes the AWS Managed Microsoft AD directory in the directory owner account.

    - **DirectoryId** *(string) --*

      Identifier of the AWS Managed Microsoft AD directory in the directory owner account.

    - **AccountId** *(string) --*

      Identifier of the directory owner account.

    - **DnsIpAddrs** *(list) --*

      IP address of the directory’s domain controllers.

      - *(string) --*

    - **VpcSettings** *(dict) --*

      Information about the VPC settings for the directory.

      - **VpcId** *(string) --*

        The identifier of the VPC that the directory is in.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets for the directory servers.

        - *(string) --*

      - **SecurityGroupId** *(string) --*

        The domain controller security group identifier for the directory.

      - **AvailabilityZones** *(list) --*

        The list of Availability Zones that the directory is in.

        - *(string) --*

    - **RadiusSettings** *(dict) --*

      A  RadiusSettings object that contains information about the RADIUS server.

      - **RadiusServers** *(list) --*

        An array of strings that contains the IP addresses of the RADIUS server endpoints, or
        the IP addresses of your RADIUS server load balancer.

        - *(string) --*

      - **RadiusPort** *(integer) --*

        The port that your RADIUS server is using for communications. Your on-premises
        network must allow inbound traffic over this port from the AWS Directory Service
        servers.

      - **RadiusTimeout** *(integer) --*

        The amount of time, in seconds, to wait for the RADIUS server to respond.

      - **RadiusRetries** *(integer) --*

        The maximum number of times that communication with the RADIUS server is attempted.

      - **SharedSecret** *(string) --*

        Required for enabling RADIUS on the directory.

      - **AuthenticationProtocol** *(string) --*

        The protocol specified for your RADIUS endpoints.

      - **DisplayLabel** *(string) --*

        Not currently used.

      - **UseSameUsername** *(boolean) --*

        Not currently used.

    - **RadiusStatus** *(string) --*

      Information about the status of the RADIUS server.
    """


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": str,
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef
):
    """
    Type definition for `DescribeDirectoriesPaginateResponseDirectoryDescriptions` `RadiusSettings`

    A  RadiusSettings object that contains information about the RADIUS server configured for
    this directory.

    - **RadiusServers** *(list) --*

      An array of strings that contains the IP addresses of the RADIUS server endpoints, or
      the IP addresses of your RADIUS server load balancer.

      - *(string) --*

    - **RadiusPort** *(integer) --*

      The port that your RADIUS server is using for communications. Your on-premises network
      must allow inbound traffic over this port from the AWS Directory Service servers.

    - **RadiusTimeout** *(integer) --*

      The amount of time, in seconds, to wait for the RADIUS server to respond.

    - **RadiusRetries** *(integer) --*

      The maximum number of times that communication with the RADIUS server is attempted.

    - **SharedSecret** *(string) --*

      Required for enabling RADIUS on the directory.

    - **AuthenticationProtocol** *(string) --*

      The protocol specified for your RADIUS endpoints.

    - **DisplayLabel** *(string) --*

      Not currently used.

    - **UseSameUsername** *(boolean) --*

      Not currently used.
    """


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef
):
    """
    Type definition for `DescribeDirectoriesPaginateResponseDirectoryDescriptions` `VpcSettings`

    A  DirectoryVpcSettingsDescription object that contains additional information about a
    directory. This member is only present if the directory is a Simple AD or Managed AD
    directory.

    - **VpcId** *(string) --*

      The identifier of the VPC that the directory is in.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets for the directory servers.

      - *(string) --*

    - **SecurityGroupId** *(string) --*

      The domain controller security group identifier for the directory.

    - **AvailabilityZones** *(list) --*

      The list of Availability Zones that the directory is in.

      - *(string) --*
    """


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef",
    {
        "DirectoryId": str,
        "Name": str,
        "ShortName": str,
        "Size": str,
        "Edition": str,
        "Alias": str,
        "AccessUrl": str,
        "Description": str,
        "DnsIpAddrs": List[str],
        "Stage": str,
        "ShareStatus": str,
        "ShareMethod": str,
        "ShareNotes": str,
        "LaunchTime": datetime,
        "StageLastUpdatedDateTime": datetime,
        "Type": str,
        "VpcSettings": DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef,
        "ConnectSettings": DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef,
        "RadiusSettings": DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef,
        "RadiusStatus": str,
        "StageReason": str,
        "SsoEnabled": bool,
        "DesiredNumberOfDomainControllers": int,
        "OwnerDirectoryDescription": DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef,
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef
):
    """
    Type definition for `DescribeDirectoriesPaginateResponse` `DirectoryDescriptions`

    Contains information about an AWS Directory Service directory.

    - **DirectoryId** *(string) --*

      The directory identifier.

    - **Name** *(string) --*

      The fully qualified name of the directory.

    - **ShortName** *(string) --*

      The short name of the directory.

    - **Size** *(string) --*

      The directory size.

    - **Edition** *(string) --*

      The edition associated with this directory.

    - **Alias** *(string) --*

      The alias for the directory. If no alias has been created for the directory, the alias is
      the directory identifier, such as ``d-XXXXXXXXXX`` .

    - **AccessUrl** *(string) --*

      The access URL for the directory, such as ``http://<alias>.awsapps.com`` . If no alias
      has been created for the directory, ``<alias>`` is the directory identifier, such as
      ``d-XXXXXXXXXX`` .

    - **Description** *(string) --*

      The textual description for the directory.

    - **DnsIpAddrs** *(list) --*

      The IP addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD
      directory, these are the IP addresses of the Simple AD or Microsoft AD directory servers.
      For an AD Connector directory, these are the IP addresses of the DNS servers or domain
      controllers in the on-premises directory to which the AD Connector is connected.

      - *(string) --*

    - **Stage** *(string) --*

      The current stage of the directory.

    - **ShareStatus** *(string) --*

      Current directory status of the shared AWS Managed Microsoft AD directory.

    - **ShareMethod** *(string) --*

      The method used when sharing a directory to determine whether the directory should be
      shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by
      sending a shared directory request (``HANDSHAKE`` ).

    - **ShareNotes** *(string) --*

      A directory share request that is sent by the directory owner to the directory consumer.
      The request includes a typed message to help the directory consumer administrator
      determine whether to approve or reject the share invitation.

    - **LaunchTime** *(datetime) --*

      Specifies when the directory was created.

    - **StageLastUpdatedDateTime** *(datetime) --*

      The date and time that the stage was last updated.

    - **Type** *(string) --*

      The directory size.

    - **VpcSettings** *(dict) --*

      A  DirectoryVpcSettingsDescription object that contains additional information about a
      directory. This member is only present if the directory is a Simple AD or Managed AD
      directory.

      - **VpcId** *(string) --*

        The identifier of the VPC that the directory is in.

      - **SubnetIds** *(list) --*

        The identifiers of the subnets for the directory servers.

        - *(string) --*

      - **SecurityGroupId** *(string) --*

        The domain controller security group identifier for the directory.

      - **AvailabilityZones** *(list) --*

        The list of Availability Zones that the directory is in.

        - *(string) --*

    - **ConnectSettings** *(dict) --*

      A  DirectoryConnectSettingsDescription object that contains additional information about
      an AD Connector directory. This member is only present if the directory is an AD
      Connector directory.

      - **VpcId** *(string) --*

        The identifier of the VPC that the AD Connector is in.

      - **SubnetIds** *(list) --*

        A list of subnet identifiers in the VPC that the AD connector is in.

        - *(string) --*

      - **CustomerUserName** *(string) --*

        The user name of the service account in the on-premises directory.

      - **SecurityGroupId** *(string) --*

        The security group identifier for the AD Connector directory.

      - **AvailabilityZones** *(list) --*

        A list of the Availability Zones that the directory is in.

        - *(string) --*

      - **ConnectIps** *(list) --*

        The IP addresses of the AD Connector servers.

        - *(string) --*

    - **RadiusSettings** *(dict) --*

      A  RadiusSettings object that contains information about the RADIUS server configured for
      this directory.

      - **RadiusServers** *(list) --*

        An array of strings that contains the IP addresses of the RADIUS server endpoints, or
        the IP addresses of your RADIUS server load balancer.

        - *(string) --*

      - **RadiusPort** *(integer) --*

        The port that your RADIUS server is using for communications. Your on-premises network
        must allow inbound traffic over this port from the AWS Directory Service servers.

      - **RadiusTimeout** *(integer) --*

        The amount of time, in seconds, to wait for the RADIUS server to respond.

      - **RadiusRetries** *(integer) --*

        The maximum number of times that communication with the RADIUS server is attempted.

      - **SharedSecret** *(string) --*

        Required for enabling RADIUS on the directory.

      - **AuthenticationProtocol** *(string) --*

        The protocol specified for your RADIUS endpoints.

      - **DisplayLabel** *(string) --*

        Not currently used.

      - **UseSameUsername** *(boolean) --*

        Not currently used.

    - **RadiusStatus** *(string) --*

      The status of the RADIUS MFA server connection.

    - **StageReason** *(string) --*

      Additional information about the directory stage.

    - **SsoEnabled** *(boolean) --*

      Indicates if single sign-on is enabled for the directory. For more information, see
      EnableSso and  DisableSso .

    - **DesiredNumberOfDomainControllers** *(integer) --*

      The desired number of domain controllers in the directory if the directory is Microsoft
      AD.

    - **OwnerDirectoryDescription** *(dict) --*

      Describes the AWS Managed Microsoft AD directory in the directory owner account.

      - **DirectoryId** *(string) --*

        Identifier of the AWS Managed Microsoft AD directory in the directory owner account.

      - **AccountId** *(string) --*

        Identifier of the directory owner account.

      - **DnsIpAddrs** *(list) --*

        IP address of the directory’s domain controllers.

        - *(string) --*

      - **VpcSettings** *(dict) --*

        Information about the VPC settings for the directory.

        - **VpcId** *(string) --*

          The identifier of the VPC that the directory is in.

        - **SubnetIds** *(list) --*

          The identifiers of the subnets for the directory servers.

          - *(string) --*

        - **SecurityGroupId** *(string) --*

          The domain controller security group identifier for the directory.

        - **AvailabilityZones** *(list) --*

          The list of Availability Zones that the directory is in.

          - *(string) --*

      - **RadiusSettings** *(dict) --*

        A  RadiusSettings object that contains information about the RADIUS server.

        - **RadiusServers** *(list) --*

          An array of strings that contains the IP addresses of the RADIUS server endpoints, or
          the IP addresses of your RADIUS server load balancer.

          - *(string) --*

        - **RadiusPort** *(integer) --*

          The port that your RADIUS server is using for communications. Your on-premises
          network must allow inbound traffic over this port from the AWS Directory Service
          servers.

        - **RadiusTimeout** *(integer) --*

          The amount of time, in seconds, to wait for the RADIUS server to respond.

        - **RadiusRetries** *(integer) --*

          The maximum number of times that communication with the RADIUS server is attempted.

        - **SharedSecret** *(string) --*

          Required for enabling RADIUS on the directory.

        - **AuthenticationProtocol** *(string) --*

          The protocol specified for your RADIUS endpoints.

        - **DisplayLabel** *(string) --*

          Not currently used.

        - **UseSameUsername** *(boolean) --*

          Not currently used.

      - **RadiusStatus** *(string) --*

        Information about the status of the RADIUS server.
    """


_DescribeDirectoriesPaginateResponseTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseTypeDef",
    {
        "DirectoryDescriptions": List[
            DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef
        ]
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseTypeDef(
    _DescribeDirectoriesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDirectoriesPaginate` `Response`

    Contains the results of the  DescribeDirectories operation.

    - **DirectoryDescriptions** *(list) --*

      The list of  DirectoryDescription objects that were retrieved.

      It is possible that this list contains less than the number of items specified in the
      ``Limit`` member of the request. This occurs if there are less than the requested number of
      items left to retrieve, or if the limitations of the operation have been exceeded.

      - *(dict) --*

        Contains information about an AWS Directory Service directory.

        - **DirectoryId** *(string) --*

          The directory identifier.

        - **Name** *(string) --*

          The fully qualified name of the directory.

        - **ShortName** *(string) --*

          The short name of the directory.

        - **Size** *(string) --*

          The directory size.

        - **Edition** *(string) --*

          The edition associated with this directory.

        - **Alias** *(string) --*

          The alias for the directory. If no alias has been created for the directory, the alias is
          the directory identifier, such as ``d-XXXXXXXXXX`` .

        - **AccessUrl** *(string) --*

          The access URL for the directory, such as ``http://<alias>.awsapps.com`` . If no alias
          has been created for the directory, ``<alias>`` is the directory identifier, such as
          ``d-XXXXXXXXXX`` .

        - **Description** *(string) --*

          The textual description for the directory.

        - **DnsIpAddrs** *(list) --*

          The IP addresses of the DNS servers for the directory. For a Simple AD or Microsoft AD
          directory, these are the IP addresses of the Simple AD or Microsoft AD directory servers.
          For an AD Connector directory, these are the IP addresses of the DNS servers or domain
          controllers in the on-premises directory to which the AD Connector is connected.

          - *(string) --*

        - **Stage** *(string) --*

          The current stage of the directory.

        - **ShareStatus** *(string) --*

          Current directory status of the shared AWS Managed Microsoft AD directory.

        - **ShareMethod** *(string) --*

          The method used when sharing a directory to determine whether the directory should be
          shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by
          sending a shared directory request (``HANDSHAKE`` ).

        - **ShareNotes** *(string) --*

          A directory share request that is sent by the directory owner to the directory consumer.
          The request includes a typed message to help the directory consumer administrator
          determine whether to approve or reject the share invitation.

        - **LaunchTime** *(datetime) --*

          Specifies when the directory was created.

        - **StageLastUpdatedDateTime** *(datetime) --*

          The date and time that the stage was last updated.

        - **Type** *(string) --*

          The directory size.

        - **VpcSettings** *(dict) --*

          A  DirectoryVpcSettingsDescription object that contains additional information about a
          directory. This member is only present if the directory is a Simple AD or Managed AD
          directory.

          - **VpcId** *(string) --*

            The identifier of the VPC that the directory is in.

          - **SubnetIds** *(list) --*

            The identifiers of the subnets for the directory servers.

            - *(string) --*

          - **SecurityGroupId** *(string) --*

            The domain controller security group identifier for the directory.

          - **AvailabilityZones** *(list) --*

            The list of Availability Zones that the directory is in.

            - *(string) --*

        - **ConnectSettings** *(dict) --*

          A  DirectoryConnectSettingsDescription object that contains additional information about
          an AD Connector directory. This member is only present if the directory is an AD
          Connector directory.

          - **VpcId** *(string) --*

            The identifier of the VPC that the AD Connector is in.

          - **SubnetIds** *(list) --*

            A list of subnet identifiers in the VPC that the AD connector is in.

            - *(string) --*

          - **CustomerUserName** *(string) --*

            The user name of the service account in the on-premises directory.

          - **SecurityGroupId** *(string) --*

            The security group identifier for the AD Connector directory.

          - **AvailabilityZones** *(list) --*

            A list of the Availability Zones that the directory is in.

            - *(string) --*

          - **ConnectIps** *(list) --*

            The IP addresses of the AD Connector servers.

            - *(string) --*

        - **RadiusSettings** *(dict) --*

          A  RadiusSettings object that contains information about the RADIUS server configured for
          this directory.

          - **RadiusServers** *(list) --*

            An array of strings that contains the IP addresses of the RADIUS server endpoints, or
            the IP addresses of your RADIUS server load balancer.

            - *(string) --*

          - **RadiusPort** *(integer) --*

            The port that your RADIUS server is using for communications. Your on-premises network
            must allow inbound traffic over this port from the AWS Directory Service servers.

          - **RadiusTimeout** *(integer) --*

            The amount of time, in seconds, to wait for the RADIUS server to respond.

          - **RadiusRetries** *(integer) --*

            The maximum number of times that communication with the RADIUS server is attempted.

          - **SharedSecret** *(string) --*

            Required for enabling RADIUS on the directory.

          - **AuthenticationProtocol** *(string) --*

            The protocol specified for your RADIUS endpoints.

          - **DisplayLabel** *(string) --*

            Not currently used.

          - **UseSameUsername** *(boolean) --*

            Not currently used.

        - **RadiusStatus** *(string) --*

          The status of the RADIUS MFA server connection.

        - **StageReason** *(string) --*

          Additional information about the directory stage.

        - **SsoEnabled** *(boolean) --*

          Indicates if single sign-on is enabled for the directory. For more information, see
          EnableSso and  DisableSso .

        - **DesiredNumberOfDomainControllers** *(integer) --*

          The desired number of domain controllers in the directory if the directory is Microsoft
          AD.

        - **OwnerDirectoryDescription** *(dict) --*

          Describes the AWS Managed Microsoft AD directory in the directory owner account.

          - **DirectoryId** *(string) --*

            Identifier of the AWS Managed Microsoft AD directory in the directory owner account.

          - **AccountId** *(string) --*

            Identifier of the directory owner account.

          - **DnsIpAddrs** *(list) --*

            IP address of the directory’s domain controllers.

            - *(string) --*

          - **VpcSettings** *(dict) --*

            Information about the VPC settings for the directory.

            - **VpcId** *(string) --*

              The identifier of the VPC that the directory is in.

            - **SubnetIds** *(list) --*

              The identifiers of the subnets for the directory servers.

              - *(string) --*

            - **SecurityGroupId** *(string) --*

              The domain controller security group identifier for the directory.

            - **AvailabilityZones** *(list) --*

              The list of Availability Zones that the directory is in.

              - *(string) --*

          - **RadiusSettings** *(dict) --*

            A  RadiusSettings object that contains information about the RADIUS server.

            - **RadiusServers** *(list) --*

              An array of strings that contains the IP addresses of the RADIUS server endpoints, or
              the IP addresses of your RADIUS server load balancer.

              - *(string) --*

            - **RadiusPort** *(integer) --*

              The port that your RADIUS server is using for communications. Your on-premises
              network must allow inbound traffic over this port from the AWS Directory Service
              servers.

            - **RadiusTimeout** *(integer) --*

              The amount of time, in seconds, to wait for the RADIUS server to respond.

            - **RadiusRetries** *(integer) --*

              The maximum number of times that communication with the RADIUS server is attempted.

            - **SharedSecret** *(string) --*

              Required for enabling RADIUS on the directory.

            - **AuthenticationProtocol** *(string) --*

              The protocol specified for your RADIUS endpoints.

            - **DisplayLabel** *(string) --*

              Not currently used.

            - **UseSameUsername** *(boolean) --*

              Not currently used.

          - **RadiusStatus** *(string) --*

            Information about the status of the RADIUS server.
    """


_DescribeDomainControllersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDomainControllersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDomainControllersPaginatePaginationConfigTypeDef(
    _DescribeDomainControllersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDomainControllersPaginate` `PaginationConfig`

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


_DescribeDomainControllersPaginateResponseDomainControllersTypeDef = TypedDict(
    "_DescribeDomainControllersPaginateResponseDomainControllersTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerId": str,
        "DnsIpAddr": str,
        "VpcId": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "Status": str,
        "StatusReason": str,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
    },
    total=False,
)


class DescribeDomainControllersPaginateResponseDomainControllersTypeDef(
    _DescribeDomainControllersPaginateResponseDomainControllersTypeDef
):
    """
    Type definition for `DescribeDomainControllersPaginateResponse` `DomainControllers`

    Contains information about the domain controllers for a specified directory.

    - **DirectoryId** *(string) --*

      Identifier of the directory where the domain controller resides.

    - **DomainControllerId** *(string) --*

      Identifies a specific domain controller in the directory.

    - **DnsIpAddr** *(string) --*

      The IP address of the domain controller.

    - **VpcId** *(string) --*

      The identifier of the VPC that contains the domain controller.

    - **SubnetId** *(string) --*

      Identifier of the subnet in the VPC that contains the domain controller.

    - **AvailabilityZone** *(string) --*

      The Availability Zone where the domain controller is located.

    - **Status** *(string) --*

      The status of the domain controller.

    - **StatusReason** *(string) --*

      A description of the domain controller state.

    - **LaunchTime** *(datetime) --*

      Specifies when the domain controller was created.

    - **StatusLastUpdatedDateTime** *(datetime) --*

      The date and time that the status was last updated.
    """


_DescribeDomainControllersPaginateResponseTypeDef = TypedDict(
    "_DescribeDomainControllersPaginateResponseTypeDef",
    {
        "DomainControllers": List[
            DescribeDomainControllersPaginateResponseDomainControllersTypeDef
        ]
    },
    total=False,
)


class DescribeDomainControllersPaginateResponseTypeDef(
    _DescribeDomainControllersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDomainControllersPaginate` `Response`

    - **DomainControllers** *(list) --*

      List of the  DomainController objects that were retrieved.

      - *(dict) --*

        Contains information about the domain controllers for a specified directory.

        - **DirectoryId** *(string) --*

          Identifier of the directory where the domain controller resides.

        - **DomainControllerId** *(string) --*

          Identifies a specific domain controller in the directory.

        - **DnsIpAddr** *(string) --*

          The IP address of the domain controller.

        - **VpcId** *(string) --*

          The identifier of the VPC that contains the domain controller.

        - **SubnetId** *(string) --*

          Identifier of the subnet in the VPC that contains the domain controller.

        - **AvailabilityZone** *(string) --*

          The Availability Zone where the domain controller is located.

        - **Status** *(string) --*

          The status of the domain controller.

        - **StatusReason** *(string) --*

          A description of the domain controller state.

        - **LaunchTime** *(datetime) --*

          Specifies when the domain controller was created.

        - **StatusLastUpdatedDateTime** *(datetime) --*

          The date and time that the status was last updated.
    """


_DescribeSharedDirectoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSharedDirectoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSharedDirectoriesPaginatePaginationConfigTypeDef(
    _DescribeSharedDirectoriesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeSharedDirectoriesPaginate` `PaginationConfig`

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


_DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef = TypedDict(
    "_DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": str,
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": str,
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)


class DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef(
    _DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef
):
    """
    Type definition for `DescribeSharedDirectoriesPaginateResponse` `SharedDirectories`

    Details about the shared directory in the directory owner account for which the share
    request in the directory consumer account has been accepted.

    - **OwnerAccountId** *(string) --*

      Identifier of the directory owner account, which contains the directory that has been
      shared to the consumer account.

    - **OwnerDirectoryId** *(string) --*

      Identifier of the directory in the directory owner account.

    - **ShareMethod** *(string) --*

      The method used when sharing a directory to determine whether the directory should be
      shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by
      sending a shared directory request (``HANDSHAKE`` ).

    - **SharedAccountId** *(string) --*

      Identifier of the directory consumer account that has access to the shared directory
      (``OwnerDirectoryId`` ) in the directory owner account.

    - **SharedDirectoryId** *(string) --*

      Identifier of the shared directory in the directory consumer account. This identifier is
      different for each directory owner account.

    - **ShareStatus** *(string) --*

      Current directory status of the shared AWS Managed Microsoft AD directory.

    - **ShareNotes** *(string) --*

      A directory share request that is sent by the directory owner to the directory consumer.
      The request includes a typed message to help the directory consumer administrator
      determine whether to approve or reject the share invitation.

    - **CreatedDateTime** *(datetime) --*

      The date and time that the shared directory was created.

    - **LastUpdatedDateTime** *(datetime) --*

      The date and time that the shared directory was last updated.
    """


_DescribeSharedDirectoriesPaginateResponseTypeDef = TypedDict(
    "_DescribeSharedDirectoriesPaginateResponseTypeDef",
    {
        "SharedDirectories": List[
            DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef
        ]
    },
    total=False,
)


class DescribeSharedDirectoriesPaginateResponseTypeDef(
    _DescribeSharedDirectoriesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeSharedDirectoriesPaginate` `Response`

    - **SharedDirectories** *(list) --*

      A list of all shared directories in your account.

      - *(dict) --*

        Details about the shared directory in the directory owner account for which the share
        request in the directory consumer account has been accepted.

        - **OwnerAccountId** *(string) --*

          Identifier of the directory owner account, which contains the directory that has been
          shared to the consumer account.

        - **OwnerDirectoryId** *(string) --*

          Identifier of the directory in the directory owner account.

        - **ShareMethod** *(string) --*

          The method used when sharing a directory to determine whether the directory should be
          shared within your AWS organization (``ORGANIZATIONS`` ) or with any AWS account by
          sending a shared directory request (``HANDSHAKE`` ).

        - **SharedAccountId** *(string) --*

          Identifier of the directory consumer account that has access to the shared directory
          (``OwnerDirectoryId`` ) in the directory owner account.

        - **SharedDirectoryId** *(string) --*

          Identifier of the shared directory in the directory consumer account. This identifier is
          different for each directory owner account.

        - **ShareStatus** *(string) --*

          Current directory status of the shared AWS Managed Microsoft AD directory.

        - **ShareNotes** *(string) --*

          A directory share request that is sent by the directory owner to the directory consumer.
          The request includes a typed message to help the directory consumer administrator
          determine whether to approve or reject the share invitation.

        - **CreatedDateTime** *(datetime) --*

          The date and time that the shared directory was created.

        - **LastUpdatedDateTime** *(datetime) --*

          The date and time that the shared directory was last updated.
    """


_DescribeSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSnapshotsPaginatePaginationConfigTypeDef(
    _DescribeSnapshotsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeSnapshotsPaginate` `PaginationConfig`

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


_DescribeSnapshotsPaginateResponseSnapshotsTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseSnapshotsTypeDef",
    {
        "DirectoryId": str,
        "SnapshotId": str,
        "Type": str,
        "Name": str,
        "Status": str,
        "StartTime": datetime,
    },
    total=False,
)


class DescribeSnapshotsPaginateResponseSnapshotsTypeDef(
    _DescribeSnapshotsPaginateResponseSnapshotsTypeDef
):
    """
    Type definition for `DescribeSnapshotsPaginateResponse` `Snapshots`

    Describes a directory snapshot.

    - **DirectoryId** *(string) --*

      The directory identifier.

    - **SnapshotId** *(string) --*

      The snapshot identifier.

    - **Type** *(string) --*

      The snapshot type.

    - **Name** *(string) --*

      The descriptive name of the snapshot.

    - **Status** *(string) --*

      The snapshot status.

    - **StartTime** *(datetime) --*

      The date and time that the snapshot was taken.
    """


_DescribeSnapshotsPaginateResponseTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseTypeDef",
    {"Snapshots": List[DescribeSnapshotsPaginateResponseSnapshotsTypeDef]},
    total=False,
)


class DescribeSnapshotsPaginateResponseTypeDef(
    _DescribeSnapshotsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeSnapshotsPaginate` `Response`

    Contains the results of the  DescribeSnapshots operation.

    - **Snapshots** *(list) --*

      The list of  Snapshot objects that were retrieved.

      It is possible that this list contains less than the number of items specified in the *Limit*
      member of the request. This occurs if there are less than the requested number of items left
      to retrieve, or if the limitations of the operation have been exceeded.

      - *(dict) --*

        Describes a directory snapshot.

        - **DirectoryId** *(string) --*

          The directory identifier.

        - **SnapshotId** *(string) --*

          The snapshot identifier.

        - **Type** *(string) --*

          The snapshot type.

        - **Name** *(string) --*

          The descriptive name of the snapshot.

        - **Status** *(string) --*

          The snapshot status.

        - **StartTime** *(datetime) --*

          The date and time that the snapshot was taken.
    """


_DescribeTrustsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTrustsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTrustsPaginatePaginationConfigTypeDef(
    _DescribeTrustsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeTrustsPaginate` `PaginationConfig`

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


_DescribeTrustsPaginateResponseTrustsTypeDef = TypedDict(
    "_DescribeTrustsPaginateResponseTrustsTypeDef",
    {
        "DirectoryId": str,
        "TrustId": str,
        "RemoteDomainName": str,
        "TrustType": str,
        "TrustDirection": str,
        "TrustState": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
        "StateLastUpdatedDateTime": datetime,
        "TrustStateReason": str,
        "SelectiveAuth": str,
    },
    total=False,
)


class DescribeTrustsPaginateResponseTrustsTypeDef(
    _DescribeTrustsPaginateResponseTrustsTypeDef
):
    """
    Type definition for `DescribeTrustsPaginateResponse` `Trusts`

    Describes a trust relationship between an AWS Managed Microsoft AD directory and an
    external domain.

    - **DirectoryId** *(string) --*

      The Directory ID of the AWS directory involved in the trust relationship.

    - **TrustId** *(string) --*

      The unique ID of the trust relationship.

    - **RemoteDomainName** *(string) --*

      The Fully Qualified Domain Name (FQDN) of the external domain involved in the trust
      relationship.

    - **TrustType** *(string) --*

      The trust relationship type. ``Forest`` is the default.

    - **TrustDirection** *(string) --*

      The trust relationship direction.

    - **TrustState** *(string) --*

      The trust relationship state.

    - **CreatedDateTime** *(datetime) --*

      The date and time that the trust relationship was created.

    - **LastUpdatedDateTime** *(datetime) --*

      The date and time that the trust relationship was last updated.

    - **StateLastUpdatedDateTime** *(datetime) --*

      The date and time that the TrustState was last updated.

    - **TrustStateReason** *(string) --*

      The reason for the TrustState.

    - **SelectiveAuth** *(string) --*

      Current state of selective authentication for the trust.
    """


_DescribeTrustsPaginateResponseTypeDef = TypedDict(
    "_DescribeTrustsPaginateResponseTypeDef",
    {"Trusts": List[DescribeTrustsPaginateResponseTrustsTypeDef]},
    total=False,
)


class DescribeTrustsPaginateResponseTypeDef(_DescribeTrustsPaginateResponseTypeDef):
    """
    Type definition for `DescribeTrustsPaginate` `Response`

    The result of a DescribeTrust request.

    - **Trusts** *(list) --*

      The list of Trust objects that were retrieved.

      It is possible that this list contains less than the number of items specified in the *Limit*
      member of the request. This occurs if there are less than the requested number of items left
      to retrieve, or if the limitations of the operation have been exceeded.

      - *(dict) --*

        Describes a trust relationship between an AWS Managed Microsoft AD directory and an
        external domain.

        - **DirectoryId** *(string) --*

          The Directory ID of the AWS directory involved in the trust relationship.

        - **TrustId** *(string) --*

          The unique ID of the trust relationship.

        - **RemoteDomainName** *(string) --*

          The Fully Qualified Domain Name (FQDN) of the external domain involved in the trust
          relationship.

        - **TrustType** *(string) --*

          The trust relationship type. ``Forest`` is the default.

        - **TrustDirection** *(string) --*

          The trust relationship direction.

        - **TrustState** *(string) --*

          The trust relationship state.

        - **CreatedDateTime** *(datetime) --*

          The date and time that the trust relationship was created.

        - **LastUpdatedDateTime** *(datetime) --*

          The date and time that the trust relationship was last updated.

        - **StateLastUpdatedDateTime** *(datetime) --*

          The date and time that the TrustState was last updated.

        - **TrustStateReason** *(string) --*

          The reason for the TrustState.

        - **SelectiveAuth** *(string) --*

          Current state of selective authentication for the trust.
    """


_ListIpRoutesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIpRoutesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIpRoutesPaginatePaginationConfigTypeDef(
    _ListIpRoutesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListIpRoutesPaginate` `PaginationConfig`

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


_ListIpRoutesPaginateResponseIpRoutesInfoTypeDef = TypedDict(
    "_ListIpRoutesPaginateResponseIpRoutesInfoTypeDef",
    {
        "DirectoryId": str,
        "CidrIp": str,
        "IpRouteStatusMsg": str,
        "AddedDateTime": datetime,
        "IpRouteStatusReason": str,
        "Description": str,
    },
    total=False,
)


class ListIpRoutesPaginateResponseIpRoutesInfoTypeDef(
    _ListIpRoutesPaginateResponseIpRoutesInfoTypeDef
):
    """
    Type definition for `ListIpRoutesPaginateResponse` `IpRoutesInfo`

    Information about one or more IP address blocks.

    - **DirectoryId** *(string) --*

      Identifier (ID) of the directory associated with the IP addresses.

    - **CidrIp** *(string) --*

      IP address block in the  IpRoute .

    - **IpRouteStatusMsg** *(string) --*

      The status of the IP address block.

    - **AddedDateTime** *(datetime) --*

      The date and time the address block was added to the directory.

    - **IpRouteStatusReason** *(string) --*

      The reason for the IpRouteStatusMsg.

    - **Description** *(string) --*

      Description of the  IpRouteInfo .
    """


_ListIpRoutesPaginateResponseTypeDef = TypedDict(
    "_ListIpRoutesPaginateResponseTypeDef",
    {"IpRoutesInfo": List[ListIpRoutesPaginateResponseIpRoutesInfoTypeDef]},
    total=False,
)


class ListIpRoutesPaginateResponseTypeDef(_ListIpRoutesPaginateResponseTypeDef):
    """
    Type definition for `ListIpRoutesPaginate` `Response`

    - **IpRoutesInfo** *(list) --*

      A list of  IpRoute s.

      - *(dict) --*

        Information about one or more IP address blocks.

        - **DirectoryId** *(string) --*

          Identifier (ID) of the directory associated with the IP addresses.

        - **CidrIp** *(string) --*

          IP address block in the  IpRoute .

        - **IpRouteStatusMsg** *(string) --*

          The status of the IP address block.

        - **AddedDateTime** *(datetime) --*

          The date and time the address block was added to the directory.

        - **IpRouteStatusReason** *(string) --*

          The reason for the IpRouteStatusMsg.

        - **Description** *(string) --*

          Description of the  IpRouteInfo .
    """


_ListLogSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLogSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLogSubscriptionsPaginatePaginationConfigTypeDef(
    _ListLogSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLogSubscriptionsPaginate` `PaginationConfig`

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


_ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef = TypedDict(
    "_ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef",
    {"DirectoryId": str, "LogGroupName": str, "SubscriptionCreatedDateTime": datetime},
    total=False,
)


class ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef(
    _ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef
):
    """
    Type definition for `ListLogSubscriptionsPaginateResponse` `LogSubscriptions`

    Represents a log subscription, which tracks real-time data from a chosen log group to a
    specified destination.

    - **DirectoryId** *(string) --*

      Identifier (ID) of the directory that you want to associate with the log subscription.

    - **LogGroupName** *(string) --*

      The name of the log group.

    - **SubscriptionCreatedDateTime** *(datetime) --*

      The date and time that the log subscription was created.
    """


_ListLogSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_ListLogSubscriptionsPaginateResponseTypeDef",
    {
        "LogSubscriptions": List[
            ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef
        ]
    },
    total=False,
)


class ListLogSubscriptionsPaginateResponseTypeDef(
    _ListLogSubscriptionsPaginateResponseTypeDef
):
    """
    Type definition for `ListLogSubscriptionsPaginate` `Response`

    - **LogSubscriptions** *(list) --*

      A list of active  LogSubscription objects for calling the AWS account.

      - *(dict) --*

        Represents a log subscription, which tracks real-time data from a chosen log group to a
        specified destination.

        - **DirectoryId** *(string) --*

          Identifier (ID) of the directory that you want to associate with the log subscription.

        - **LogGroupName** *(string) --*

          The name of the log group.

        - **SubscriptionCreatedDateTime** *(datetime) --*

          The date and time that the log subscription was created.
    """


_ListSchemaExtensionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSchemaExtensionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSchemaExtensionsPaginatePaginationConfigTypeDef(
    _ListSchemaExtensionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSchemaExtensionsPaginate` `PaginationConfig`

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


_ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef = TypedDict(
    "_ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
        "Description": str,
        "SchemaExtensionStatus": str,
        "SchemaExtensionStatusReason": str,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)


class ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef(
    _ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef
):
    """
    Type definition for `ListSchemaExtensionsPaginateResponse` `SchemaExtensionsInfo`

    Information about a schema extension.

    - **DirectoryId** *(string) --*

      The identifier of the directory to which the schema extension is applied.

    - **SchemaExtensionId** *(string) --*

      The identifier of the schema extension.

    - **Description** *(string) --*

      A description of the schema extension.

    - **SchemaExtensionStatus** *(string) --*

      The current status of the schema extension.

    - **SchemaExtensionStatusReason** *(string) --*

      The reason for the ``SchemaExtensionStatus`` .

    - **StartDateTime** *(datetime) --*

      The date and time that the schema extension started being applied to the directory.

    - **EndDateTime** *(datetime) --*

      The date and time that the schema extension was completed.
    """


_ListSchemaExtensionsPaginateResponseTypeDef = TypedDict(
    "_ListSchemaExtensionsPaginateResponseTypeDef",
    {
        "SchemaExtensionsInfo": List[
            ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef
        ]
    },
    total=False,
)


class ListSchemaExtensionsPaginateResponseTypeDef(
    _ListSchemaExtensionsPaginateResponseTypeDef
):
    """
    Type definition for `ListSchemaExtensionsPaginate` `Response`

    - **SchemaExtensionsInfo** *(list) --*

      Information about the schema extensions applied to the directory.

      - *(dict) --*

        Information about a schema extension.

        - **DirectoryId** *(string) --*

          The identifier of the directory to which the schema extension is applied.

        - **SchemaExtensionId** *(string) --*

          The identifier of the schema extension.

        - **Description** *(string) --*

          A description of the schema extension.

        - **SchemaExtensionStatus** *(string) --*

          The current status of the schema extension.

        - **SchemaExtensionStatusReason** *(string) --*

          The reason for the ``SchemaExtensionStatus`` .

        - **StartDateTime** *(datetime) --*

          The date and time that the schema extension started being applied to the directory.

        - **EndDateTime** *(datetime) --*

          The date and time that the schema extension was completed.
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

    Metadata assigned to a directory consisting of a key-value pair.

    - **Key** *(string) --*

      Required name of the tag. The string value can be Unicode characters and cannot be
      prefixed with "aws:". The string can contain only the set of Unicode letters, digits,
      white-space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be Unicode characters. The string can
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
      '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
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

    - **Tags** *(list) --*

      List of tags returned by the ListTagsForResource operation.

      - *(dict) --*

        Metadata assigned to a directory consisting of a key-value pair.

        - **Key** *(string) --*

          Required name of the tag. The string value can be Unicode characters and cannot be
          prefixed with "aws:". The string can contain only the set of Unicode letters, digits,
          white-space, '_', '.', '/', '=', '+', '-' (Java regex:
          "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        - **Value** *(string) --*

          The optional value of the tag. The string value can be Unicode characters. The string can
          contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
          '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """
