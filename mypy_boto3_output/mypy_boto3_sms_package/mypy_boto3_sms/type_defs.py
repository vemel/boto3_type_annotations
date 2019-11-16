"Main interface for sms type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAppResponseappSummarylaunchDetailsTypeDef",
    "ClientCreateAppResponseappSummaryTypeDef",
    "ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    "ClientCreateAppResponseserverGroupsserverListvmServerTypeDef",
    "ClientCreateAppResponseserverGroupsserverListTypeDef",
    "ClientCreateAppResponseserverGroupsTypeDef",
    "ClientCreateAppResponsetagsTypeDef",
    "ClientCreateAppResponseTypeDef",
    "ClientCreateAppserverGroupsserverListvmServervmServerAddressTypeDef",
    "ClientCreateAppserverGroupsserverListvmServerTypeDef",
    "ClientCreateAppserverGroupsserverListTypeDef",
    "ClientCreateAppserverGroupsTypeDef",
    "ClientCreateApptagsTypeDef",
    "ClientCreateReplicationJobResponseTypeDef",
    "ClientGenerateChangeSetResponses3LocationTypeDef",
    "ClientGenerateChangeSetResponseTypeDef",
    "ClientGenerateTemplateResponses3LocationTypeDef",
    "ClientGenerateTemplateResponseTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef",
    "ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef",
    "ClientGetAppLaunchConfigurationResponseTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef",
    "ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef",
    "ClientGetAppReplicationConfigurationResponseTypeDef",
    "ClientGetAppResponseappSummarylaunchDetailsTypeDef",
    "ClientGetAppResponseappSummaryTypeDef",
    "ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    "ClientGetAppResponseserverGroupsserverListvmServerTypeDef",
    "ClientGetAppResponseserverGroupsserverListTypeDef",
    "ClientGetAppResponseserverGroupsTypeDef",
    "ClientGetAppResponsetagsTypeDef",
    "ClientGetAppResponseTypeDef",
    "ClientGetConnectorsResponseconnectorListTypeDef",
    "ClientGetConnectorsResponseTypeDef",
    "ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef",
    "ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef",
    "ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef",
    "ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef",
    "ClientGetReplicationJobsResponsereplicationJobListTypeDef",
    "ClientGetReplicationJobsResponseTypeDef",
    "ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef",
    "ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef",
    "ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef",
    "ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef",
    "ClientGetReplicationRunsResponsereplicationJobTypeDef",
    "ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef",
    "ClientGetReplicationRunsResponsereplicationRunListTypeDef",
    "ClientGetReplicationRunsResponseTypeDef",
    "ClientGetServersResponseserverListvmServervmServerAddressTypeDef",
    "ClientGetServersResponseserverListvmServerTypeDef",
    "ClientGetServersResponseserverListTypeDef",
    "ClientGetServersResponseTypeDef",
    "ClientGetServersvmServerAddressListTypeDef",
    "ClientListAppsResponseappslaunchDetailsTypeDef",
    "ClientListAppsResponseappsTypeDef",
    "ClientListAppsResponseTypeDef",
    "ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef",
    "ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef",
    "ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef",
    "ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef",
    "ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef",
    "ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef",
    "ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsTypeDef",
    "ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef",
    "ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef",
    "ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef",
    "ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef",
    "ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef",
    "ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsTypeDef",
    "ClientStartOnDemandReplicationRunResponseTypeDef",
    "ClientUpdateAppResponseappSummarylaunchDetailsTypeDef",
    "ClientUpdateAppResponseappSummaryTypeDef",
    "ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    "ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef",
    "ClientUpdateAppResponseserverGroupsserverListTypeDef",
    "ClientUpdateAppResponseserverGroupsTypeDef",
    "ClientUpdateAppResponsetagsTypeDef",
    "ClientUpdateAppResponseTypeDef",
    "ClientUpdateAppserverGroupsserverListvmServervmServerAddressTypeDef",
    "ClientUpdateAppserverGroupsserverListvmServerTypeDef",
    "ClientUpdateAppserverGroupsserverListTypeDef",
    "ClientUpdateAppserverGroupsTypeDef",
    "ClientUpdateApptagsTypeDef",
    "GetConnectorsPaginatePaginationConfigTypeDef",
    "GetConnectorsPaginateResponseconnectorListTypeDef",
    "GetConnectorsPaginateResponseTypeDef",
    "GetReplicationJobsPaginatePaginationConfigTypeDef",
    "GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef",
    "GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef",
    "GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef",
    "GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef",
    "GetReplicationJobsPaginateResponsereplicationJobListTypeDef",
    "GetReplicationJobsPaginateResponseTypeDef",
    "GetReplicationRunsPaginatePaginationConfigTypeDef",
    "GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef",
    "GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef",
    "GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef",
    "GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef",
    "GetReplicationRunsPaginateResponsereplicationJobTypeDef",
    "GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef",
    "GetReplicationRunsPaginateResponsereplicationRunListTypeDef",
    "GetReplicationRunsPaginateResponseTypeDef",
    "GetServersPaginatePaginationConfigTypeDef",
    "GetServersPaginateResponseserverListvmServervmServerAddressTypeDef",
    "GetServersPaginateResponseserverListvmServerTypeDef",
    "GetServersPaginateResponseserverListTypeDef",
    "GetServersPaginateResponseTypeDef",
    "GetServersPaginatevmServerAddressListTypeDef",
    "ListAppsPaginatePaginationConfigTypeDef",
    "ListAppsPaginateResponseappslaunchDetailsTypeDef",
    "ListAppsPaginateResponseappsTypeDef",
    "ListAppsPaginateResponseTypeDef",
)


_ClientCreateAppResponseappSummarylaunchDetailsTypeDef = TypedDict(
    "_ClientCreateAppResponseappSummarylaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)


class ClientCreateAppResponseappSummarylaunchDetailsTypeDef(
    _ClientCreateAppResponseappSummarylaunchDetailsTypeDef
):
    """
    Type definition for `ClientCreateAppResponseappSummary` `launchDetails`

    Details about the latest launch of the application.

    - **latestLaunchTime** *(datetime) --*

      Latest time this application was launched successfully.

    - **stackName** *(string) --*

      Name of the latest stack launched for this application.

    - **stackId** *(string) --*

      Identifier of the latest stack launched for this application.
    """


_ClientCreateAppResponseappSummaryTypeDef = TypedDict(
    "_ClientCreateAppResponseappSummaryTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "status": str,
        "statusMessage": str,
        "replicationStatus": str,
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchStatus": str,
        "launchStatusMessage": str,
        "launchDetails": ClientCreateAppResponseappSummarylaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)


class ClientCreateAppResponseappSummaryTypeDef(
    _ClientCreateAppResponseappSummaryTypeDef
):
    """
    Type definition for `ClientCreateAppResponse` `appSummary`

    Summary description of the application.

    - **appId** *(string) --*

      Unique ID of the application.

    - **name** *(string) --*

      Name of the application.

    - **description** *(string) --*

      Description of the application.

    - **status** *(string) --*

      Status of the application.

    - **statusMessage** *(string) --*

      A message related to the status of the application

    - **replicationStatus** *(string) --*

      Replication status of the application.

    - **replicationStatusMessage** *(string) --*

      A message related to the replication status of the application.

    - **latestReplicationTime** *(datetime) --*

      Timestamp of the application's most recent successful replication.

    - **launchStatus** *(string) --*

      Launch status of the application.

    - **launchStatusMessage** *(string) --*

      A message related to the launch status of the application.

    - **launchDetails** *(dict) --*

      Details about the latest launch of the application.

      - **latestLaunchTime** *(datetime) --*

        Latest time this application was launched successfully.

      - **stackName** *(string) --*

        Name of the latest stack launched for this application.

      - **stackId** *(string) --*

        Identifier of the latest stack launched for this application.

    - **creationTime** *(datetime) --*

      Time of creation of this application.

    - **lastModified** *(datetime) --*

      Timestamp of the application's creation.

    - **roleName** *(string) --*

      Name of the service role in the customer's account used by AWS SMS.

    - **totalServerGroups** *(integer) --*

      Number of server groups present in the application.

    - **totalServers** *(integer) --*

      Number of servers present in the application.
    """


_ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef(
    _ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientCreateAppResponseserverGroupsserverListvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientCreateAppResponseserverGroupsserverListvmServerTypeDef = TypedDict(
    "_ClientCreateAppResponseserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientCreateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientCreateAppResponseserverGroupsserverListvmServerTypeDef(
    _ClientCreateAppResponseserverGroupsserverListvmServerTypeDef
):
    """
    Type definition for `ClientCreateAppResponseserverGroupsserverList` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientCreateAppResponseserverGroupsserverListTypeDef = TypedDict(
    "_ClientCreateAppResponseserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientCreateAppResponseserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientCreateAppResponseserverGroupsserverListTypeDef(
    _ClientCreateAppResponseserverGroupsserverListTypeDef
):
    """
    Type definition for `ClientCreateAppResponseserverGroups` `serverList`

    Represents a server.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_ClientCreateAppResponseserverGroupsTypeDef = TypedDict(
    "_ClientCreateAppResponseserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientCreateAppResponseserverGroupsserverListTypeDef],
    },
    total=False,
)


class ClientCreateAppResponseserverGroupsTypeDef(
    _ClientCreateAppResponseserverGroupsTypeDef
):
    """
    Type definition for `ClientCreateAppResponse` `serverGroups`

    A logical grouping of servers.

    - **serverGroupId** *(string) --*

      Identifier of a server group.

    - **name** *(string) --*

      Name of a server group.

    - **serverList** *(list) --*

      List of servers belonging to a server group.

      - *(dict) --*

        Represents a server.

        - **serverId** *(string) --*

          The identifier of the server.

        - **serverType** *(string) --*

          The type of server.

        - **vmServer** *(dict) --*

          Information about the VM server.

          - **vmServerAddress** *(dict) --*

            Information about the VM server location.

            - **vmManagerId** *(string) --*

              The identifier of the VM manager.

            - **vmId** *(string) --*

              The identifier of the VM.

          - **vmName** *(string) --*

            The name of the VM.

          - **vmManagerName** *(string) --*

            The name of the VM manager.

          - **vmManagerType** *(string) --*

            The type of VM management product.

          - **vmPath** *(string) --*

            The VM folder path in the vCenter Server virtual machine inventory tree.

        - **replicationJobId** *(string) --*

          The identifier of the replication job.

        - **replicationJobTerminated** *(boolean) --*

          Indicates whether the replication job is deleted or failed.
    """


_ClientCreateAppResponsetagsTypeDef = TypedDict(
    "_ClientCreateAppResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateAppResponsetagsTypeDef(_ClientCreateAppResponsetagsTypeDef):
    """
    Type definition for `ClientCreateAppResponse` `tags`

    A label that can be assigned to an application.

    - **key** *(string) --*

      Tag key.

    - **value** *(string) --*

      Tag value.
    """


_ClientCreateAppResponseTypeDef = TypedDict(
    "_ClientCreateAppResponseTypeDef",
    {
        "appSummary": ClientCreateAppResponseappSummaryTypeDef,
        "serverGroups": List[ClientCreateAppResponseserverGroupsTypeDef],
        "tags": List[ClientCreateAppResponsetagsTypeDef],
    },
    total=False,
)


class ClientCreateAppResponseTypeDef(_ClientCreateAppResponseTypeDef):
    """
    Type definition for `ClientCreateApp` `Response`

    - **appSummary** *(dict) --*

      Summary description of the application.

      - **appId** *(string) --*

        Unique ID of the application.

      - **name** *(string) --*

        Name of the application.

      - **description** *(string) --*

        Description of the application.

      - **status** *(string) --*

        Status of the application.

      - **statusMessage** *(string) --*

        A message related to the status of the application

      - **replicationStatus** *(string) --*

        Replication status of the application.

      - **replicationStatusMessage** *(string) --*

        A message related to the replication status of the application.

      - **latestReplicationTime** *(datetime) --*

        Timestamp of the application's most recent successful replication.

      - **launchStatus** *(string) --*

        Launch status of the application.

      - **launchStatusMessage** *(string) --*

        A message related to the launch status of the application.

      - **launchDetails** *(dict) --*

        Details about the latest launch of the application.

        - **latestLaunchTime** *(datetime) --*

          Latest time this application was launched successfully.

        - **stackName** *(string) --*

          Name of the latest stack launched for this application.

        - **stackId** *(string) --*

          Identifier of the latest stack launched for this application.

      - **creationTime** *(datetime) --*

        Time of creation of this application.

      - **lastModified** *(datetime) --*

        Timestamp of the application's creation.

      - **roleName** *(string) --*

        Name of the service role in the customer's account used by AWS SMS.

      - **totalServerGroups** *(integer) --*

        Number of server groups present in the application.

      - **totalServers** *(integer) --*

        Number of servers present in the application.

    - **serverGroups** *(list) --*

      List of server groups included in the application.

      - *(dict) --*

        A logical grouping of servers.

        - **serverGroupId** *(string) --*

          Identifier of a server group.

        - **name** *(string) --*

          Name of a server group.

        - **serverList** *(list) --*

          List of servers belonging to a server group.

          - *(dict) --*

            Represents a server.

            - **serverId** *(string) --*

              The identifier of the server.

            - **serverType** *(string) --*

              The type of server.

            - **vmServer** *(dict) --*

              Information about the VM server.

              - **vmServerAddress** *(dict) --*

                Information about the VM server location.

                - **vmManagerId** *(string) --*

                  The identifier of the VM manager.

                - **vmId** *(string) --*

                  The identifier of the VM.

              - **vmName** *(string) --*

                The name of the VM.

              - **vmManagerName** *(string) --*

                The name of the VM manager.

              - **vmManagerType** *(string) --*

                The type of VM management product.

              - **vmPath** *(string) --*

                The VM folder path in the vCenter Server virtual machine inventory tree.

            - **replicationJobId** *(string) --*

              The identifier of the replication job.

            - **replicationJobTerminated** *(boolean) --*

              Indicates whether the replication job is deleted or failed.

    - **tags** *(list) --*

      List of taags associated with the application.

      - *(dict) --*

        A label that can be assigned to an application.

        - **key** *(string) --*

          Tag key.

        - **value** *(string) --*

          Tag value.
    """


_ClientCreateAppserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientCreateAppserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientCreateAppserverGroupsserverListvmServervmServerAddressTypeDef(
    _ClientCreateAppserverGroupsserverListvmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientCreateAppserverGroupsserverListvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientCreateAppserverGroupsserverListvmServerTypeDef = TypedDict(
    "_ClientCreateAppserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientCreateAppserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientCreateAppserverGroupsserverListvmServerTypeDef(
    _ClientCreateAppserverGroupsserverListvmServerTypeDef
):
    """
    Type definition for `ClientCreateAppserverGroupsserverList` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientCreateAppserverGroupsserverListTypeDef = TypedDict(
    "_ClientCreateAppserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientCreateAppserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientCreateAppserverGroupsserverListTypeDef(
    _ClientCreateAppserverGroupsserverListTypeDef
):
    """
    Type definition for `ClientCreateAppserverGroups` `serverList`

    Represents a server.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_ClientCreateAppserverGroupsTypeDef = TypedDict(
    "_ClientCreateAppserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientCreateAppserverGroupsserverListTypeDef],
    },
    total=False,
)


class ClientCreateAppserverGroupsTypeDef(_ClientCreateAppserverGroupsTypeDef):
    """
    Type definition for `ClientCreateApp` `serverGroups`

    A logical grouping of servers.

    - **serverGroupId** *(string) --*

      Identifier of a server group.

    - **name** *(string) --*

      Name of a server group.

    - **serverList** *(list) --*

      List of servers belonging to a server group.

      - *(dict) --*

        Represents a server.

        - **serverId** *(string) --*

          The identifier of the server.

        - **serverType** *(string) --*

          The type of server.

        - **vmServer** *(dict) --*

          Information about the VM server.

          - **vmServerAddress** *(dict) --*

            Information about the VM server location.

            - **vmManagerId** *(string) --*

              The identifier of the VM manager.

            - **vmId** *(string) --*

              The identifier of the VM.

          - **vmName** *(string) --*

            The name of the VM.

          - **vmManagerName** *(string) --*

            The name of the VM manager.

          - **vmManagerType** *(string) --*

            The type of VM management product.

          - **vmPath** *(string) --*

            The VM folder path in the vCenter Server virtual machine inventory tree.

        - **replicationJobId** *(string) --*

          The identifier of the replication job.

        - **replicationJobTerminated** *(boolean) --*

          Indicates whether the replication job is deleted or failed.
    """


_ClientCreateApptagsTypeDef = TypedDict(
    "_ClientCreateApptagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateApptagsTypeDef(_ClientCreateApptagsTypeDef):
    """
    Type definition for `ClientCreateApp` `tags`

    A label that can be assigned to an application.

    - **key** *(string) --*

      Tag key.

    - **value** *(string) --*

      Tag value.
    """


_ClientCreateReplicationJobResponseTypeDef = TypedDict(
    "_ClientCreateReplicationJobResponseTypeDef", {"replicationJobId": str}, total=False
)


class ClientCreateReplicationJobResponseTypeDef(
    _ClientCreateReplicationJobResponseTypeDef
):
    """
    Type definition for `ClientCreateReplicationJob` `Response`

    - **replicationJobId** *(string) --*

      The unique identifier of the replication job.
    """


_ClientGenerateChangeSetResponses3LocationTypeDef = TypedDict(
    "_ClientGenerateChangeSetResponses3LocationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ClientGenerateChangeSetResponses3LocationTypeDef(
    _ClientGenerateChangeSetResponses3LocationTypeDef
):
    """
    Type definition for `ClientGenerateChangeSetResponse` `s3Location`

    Location of the Amazon S3 object.

    - **bucket** *(string) --*

      Amazon S3 bucket name.

    - **key** *(string) --*

      Amazon S3 bucket key.
    """


_ClientGenerateChangeSetResponseTypeDef = TypedDict(
    "_ClientGenerateChangeSetResponseTypeDef",
    {"s3Location": ClientGenerateChangeSetResponses3LocationTypeDef},
    total=False,
)


class ClientGenerateChangeSetResponseTypeDef(_ClientGenerateChangeSetResponseTypeDef):
    """
    Type definition for `ClientGenerateChangeSet` `Response`

    - **s3Location** *(dict) --*

      Location of the Amazon S3 object.

      - **bucket** *(string) --*

        Amazon S3 bucket name.

      - **key** *(string) --*

        Amazon S3 bucket key.
    """


_ClientGenerateTemplateResponses3LocationTypeDef = TypedDict(
    "_ClientGenerateTemplateResponses3LocationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ClientGenerateTemplateResponses3LocationTypeDef(
    _ClientGenerateTemplateResponses3LocationTypeDef
):
    """
    Type definition for `ClientGenerateTemplateResponse` `s3Location`

    Location of the Amazon S3 object.

    - **bucket** *(string) --*

      Amazon S3 bucket name.

    - **key** *(string) --*

      Amazon S3 bucket key.
    """


_ClientGenerateTemplateResponseTypeDef = TypedDict(
    "_ClientGenerateTemplateResponseTypeDef",
    {"s3Location": ClientGenerateTemplateResponses3LocationTypeDef},
    total=False,
)


class ClientGenerateTemplateResponseTypeDef(_ClientGenerateTemplateResponseTypeDef):
    """
    Type definition for `ClientGenerateTemplate` `Response`

    - **s3Location** *(dict) --*

      Location of the Amazon S3 object.

      - **bucket** *(string) --*

        Amazon S3 bucket name.

      - **key** *(string) --*

        Amazon S3 bucket key.
    """


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef
):
    """
    Type definition for `ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserver` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef
):
    """
    Type definition for `ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurations` `server`

    Identifier of the server the launch configuration is associated with.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef
):
    """
    Type definition for `ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserData` `s3Location`

    Amazon S3 location of the user-data script.

    - **bucket** *(string) --*

      Amazon S3 bucket name.

    - **key** *(string) --*

      Amazon S3 bucket key.
    """


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef",
    {
        "s3Location": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef
):
    """
    Type definition for `ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurations` `userData`

    Location of the user-data script to be executed when launching the server.

    - **s3Location** *(dict) --*

      Amazon S3 location of the user-data script.

      - **bucket** *(string) --*

        Amazon S3 bucket name.

      - **key** *(string) --*

        Amazon S3 bucket key.
    """


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef",
    {
        "server": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef,
        "logicalId": str,
        "vpc": str,
        "subnet": str,
        "securityGroup": str,
        "ec2KeyName": str,
        "userData": ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef,
        "instanceType": str,
        "associatePublicIpAddress": bool,
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef
):
    """
    Type definition for `ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurations` `serverLaunchConfigurations`

    Launch configuration for a server.

    - **server** *(dict) --*

      Identifier of the server the launch configuration is associated with.

      - **serverId** *(string) --*

        The identifier of the server.

      - **serverType** *(string) --*

        The type of server.

      - **vmServer** *(dict) --*

        Information about the VM server.

        - **vmServerAddress** *(dict) --*

          Information about the VM server location.

          - **vmManagerId** *(string) --*

            The identifier of the VM manager.

          - **vmId** *(string) --*

            The identifier of the VM.

        - **vmName** *(string) --*

          The name of the VM.

        - **vmManagerName** *(string) --*

          The name of the VM manager.

        - **vmManagerType** *(string) --*

          The type of VM management product.

        - **vmPath** *(string) --*

          The VM folder path in the vCenter Server virtual machine inventory tree.

      - **replicationJobId** *(string) --*

        The identifier of the replication job.

      - **replicationJobTerminated** *(boolean) --*

        Indicates whether the replication job is deleted or failed.

    - **logicalId** *(string) --*

      Logical ID of the server in the Amazon CloudFormation template.

    - **vpc** *(string) --*

      Identifier of the VPC the server should be launched into.

    - **subnet** *(string) --*

      Identifier of the subnet the server should be launched into.

    - **securityGroup** *(string) --*

      Identifier of the security group that applies to the launched server.

    - **ec2KeyName** *(string) --*

      Name of the EC2 SSH Key to be used for connecting to the launched server.

    - **userData** *(dict) --*

      Location of the user-data script to be executed when launching the server.

      - **s3Location** *(dict) --*

        Amazon S3 location of the user-data script.

        - **bucket** *(string) --*

          Amazon S3 bucket name.

        - **key** *(string) --*

          Amazon S3 bucket key.

    - **instanceType** *(string) --*

      Instance type to be used for launching the server.

    - **associatePublicIpAddress** *(boolean) --*

      If true, a publicly accessible IP address is created when launching the server.
    """


_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": List[
            ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef(
    _ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef
):
    """
    Type definition for `ClientGetAppLaunchConfigurationResponse` `serverGroupLaunchConfigurations`

    Launch configuration for a server group.

    - **serverGroupId** *(string) --*

      Identifier of the server group the launch configuration is associated with.

    - **launchOrder** *(integer) --*

      Launch order of servers in the server group.

    - **serverLaunchConfigurations** *(list) --*

      Launch configuration for servers in the server group.

      - *(dict) --*

        Launch configuration for a server.

        - **server** *(dict) --*

          Identifier of the server the launch configuration is associated with.

          - **serverId** *(string) --*

            The identifier of the server.

          - **serverType** *(string) --*

            The type of server.

          - **vmServer** *(dict) --*

            Information about the VM server.

            - **vmServerAddress** *(dict) --*

              Information about the VM server location.

              - **vmManagerId** *(string) --*

                The identifier of the VM manager.

              - **vmId** *(string) --*

                The identifier of the VM.

            - **vmName** *(string) --*

              The name of the VM.

            - **vmManagerName** *(string) --*

              The name of the VM manager.

            - **vmManagerType** *(string) --*

              The type of VM management product.

            - **vmPath** *(string) --*

              The VM folder path in the vCenter Server virtual machine inventory tree.

          - **replicationJobId** *(string) --*

            The identifier of the replication job.

          - **replicationJobTerminated** *(boolean) --*

            Indicates whether the replication job is deleted or failed.

        - **logicalId** *(string) --*

          Logical ID of the server in the Amazon CloudFormation template.

        - **vpc** *(string) --*

          Identifier of the VPC the server should be launched into.

        - **subnet** *(string) --*

          Identifier of the subnet the server should be launched into.

        - **securityGroup** *(string) --*

          Identifier of the security group that applies to the launched server.

        - **ec2KeyName** *(string) --*

          Name of the EC2 SSH Key to be used for connecting to the launched server.

        - **userData** *(dict) --*

          Location of the user-data script to be executed when launching the server.

          - **s3Location** *(dict) --*

            Amazon S3 location of the user-data script.

            - **bucket** *(string) --*

              Amazon S3 bucket name.

            - **key** *(string) --*

              Amazon S3 bucket key.

        - **instanceType** *(string) --*

          Instance type to be used for launching the server.

        - **associatePublicIpAddress** *(boolean) --*

          If true, a publicly accessible IP address is created when launching the server.
    """


_ClientGetAppLaunchConfigurationResponseTypeDef = TypedDict(
    "_ClientGetAppLaunchConfigurationResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "serverGroupLaunchConfigurations": List[
            ClientGetAppLaunchConfigurationResponseserverGroupLaunchConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientGetAppLaunchConfigurationResponseTypeDef(
    _ClientGetAppLaunchConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetAppLaunchConfiguration` `Response`

    - **appId** *(string) --*

      ID of the application associated with the launch configuration.

    - **roleName** *(string) --*

      Name of the service role in the customer's account that Amazon CloudFormation uses to launch
      the application.

    - **serverGroupLaunchConfigurations** *(list) --*

      List of launch configurations for server groups in this application.

      - *(dict) --*

        Launch configuration for a server group.

        - **serverGroupId** *(string) --*

          Identifier of the server group the launch configuration is associated with.

        - **launchOrder** *(integer) --*

          Launch order of servers in the server group.

        - **serverLaunchConfigurations** *(list) --*

          Launch configuration for servers in the server group.

          - *(dict) --*

            Launch configuration for a server.

            - **server** *(dict) --*

              Identifier of the server the launch configuration is associated with.

              - **serverId** *(string) --*

                The identifier of the server.

              - **serverType** *(string) --*

                The type of server.

              - **vmServer** *(dict) --*

                Information about the VM server.

                - **vmServerAddress** *(dict) --*

                  Information about the VM server location.

                  - **vmManagerId** *(string) --*

                    The identifier of the VM manager.

                  - **vmId** *(string) --*

                    The identifier of the VM.

                - **vmName** *(string) --*

                  The name of the VM.

                - **vmManagerName** *(string) --*

                  The name of the VM manager.

                - **vmManagerType** *(string) --*

                  The type of VM management product.

                - **vmPath** *(string) --*

                  The VM folder path in the vCenter Server virtual machine inventory tree.

              - **replicationJobId** *(string) --*

                The identifier of the replication job.

              - **replicationJobTerminated** *(boolean) --*

                Indicates whether the replication job is deleted or failed.

            - **logicalId** *(string) --*

              Logical ID of the server in the Amazon CloudFormation template.

            - **vpc** *(string) --*

              Identifier of the VPC the server should be launched into.

            - **subnet** *(string) --*

              Identifier of the subnet the server should be launched into.

            - **securityGroup** *(string) --*

              Identifier of the security group that applies to the launched server.

            - **ec2KeyName** *(string) --*

              Name of the EC2 SSH Key to be used for connecting to the launched server.

            - **userData** *(dict) --*

              Location of the user-data script to be executed when launching the server.

              - **s3Location** *(dict) --*

                Amazon S3 location of the user-data script.

                - **bucket** *(string) --*

                  Amazon S3 bucket name.

                - **key** *(string) --*

                  Amazon S3 bucket key.

            - **instanceType** *(string) --*

              Instance type to be used for launching the server.

            - **associatePublicIpAddress** *(boolean) --*

              If true, a publicly accessible IP address is created when launching the server.
    """


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef",
    {
        "seedTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "licenseType": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef
):
    """
    Type definition for `ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurations` `serverReplicationParameters`

    Parameters for replicating the server.

    - **seedTime** *(datetime) --*

      Seed time for creating a replication job for the server.

    - **frequency** *(integer) --*

      Frequency of creating replication jobs for the server.

    - **runOnce** *(boolean) --*

    - **licenseType** *(string) --*

      License type for creating a replication job for the server.

    - **numberOfRecentAmisToKeep** *(integer) --*

      Number of recent AMIs to keep when creating a replication job for this server.

    - **encrypted** *(boolean) --*

      When true, the replication job produces encrypted AMIs. See also ``KmsKeyId`` below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
      following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default
      KMS key for EBS is used.
    """


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef
):
    """
    Type definition for `ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserver` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef
):
    """
    Type definition for `ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurations` `server`

    Identifier of the server this replication configuration is associated with.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef",
    {
        "server": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef,
        "serverReplicationParameters": ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef,
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef
):
    """
    Type definition for `ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurations` `serverReplicationConfigurations`

    Replication configuration of a server.

    - **server** *(dict) --*

      Identifier of the server this replication configuration is associated with.

      - **serverId** *(string) --*

        The identifier of the server.

      - **serverType** *(string) --*

        The type of server.

      - **vmServer** *(dict) --*

        Information about the VM server.

        - **vmServerAddress** *(dict) --*

          Information about the VM server location.

          - **vmManagerId** *(string) --*

            The identifier of the VM manager.

          - **vmId** *(string) --*

            The identifier of the VM.

        - **vmName** *(string) --*

          The name of the VM.

        - **vmManagerName** *(string) --*

          The name of the VM manager.

        - **vmManagerType** *(string) --*

          The type of VM management product.

        - **vmPath** *(string) --*

          The VM folder path in the vCenter Server virtual machine inventory tree.

      - **replicationJobId** *(string) --*

        The identifier of the replication job.

      - **replicationJobTerminated** *(boolean) --*

        Indicates whether the replication job is deleted or failed.

    - **serverReplicationParameters** *(dict) --*

      Parameters for replicating the server.

      - **seedTime** *(datetime) --*

        Seed time for creating a replication job for the server.

      - **frequency** *(integer) --*

        Frequency of creating replication jobs for the server.

      - **runOnce** *(boolean) --*

      - **licenseType** *(string) --*

        License type for creating a replication job for the server.

      - **numberOfRecentAmisToKeep** *(integer) --*

        Number of recent AMIs to keep when creating a replication job for this server.

      - **encrypted** *(boolean) --*

        When true, the replication job produces encrypted AMIs. See also ``KmsKeyId`` below.

      - **kmsKeyId** *(string) --*

        KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
        following:

        * KMS key ID

        * KMS key alias

        * ARN referring to KMS key ID

        * ARN referring to KMS key alias

        If encrypted is *true* but a KMS key id is not specified, the customer's default
        KMS key for EBS is used.
    """


_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": List[
            ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef(
    _ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef
):
    """
    Type definition for `ClientGetAppReplicationConfigurationResponse` `serverGroupReplicationConfigurations`

    Replication configuration for a server group.

    - **serverGroupId** *(string) --*

      Identifier of the server group this replication configuration is associated with.

    - **serverReplicationConfigurations** *(list) --*

      Replication configuration for servers in the server group.

      - *(dict) --*

        Replication configuration of a server.

        - **server** *(dict) --*

          Identifier of the server this replication configuration is associated with.

          - **serverId** *(string) --*

            The identifier of the server.

          - **serverType** *(string) --*

            The type of server.

          - **vmServer** *(dict) --*

            Information about the VM server.

            - **vmServerAddress** *(dict) --*

              Information about the VM server location.

              - **vmManagerId** *(string) --*

                The identifier of the VM manager.

              - **vmId** *(string) --*

                The identifier of the VM.

            - **vmName** *(string) --*

              The name of the VM.

            - **vmManagerName** *(string) --*

              The name of the VM manager.

            - **vmManagerType** *(string) --*

              The type of VM management product.

            - **vmPath** *(string) --*

              The VM folder path in the vCenter Server virtual machine inventory tree.

          - **replicationJobId** *(string) --*

            The identifier of the replication job.

          - **replicationJobTerminated** *(boolean) --*

            Indicates whether the replication job is deleted or failed.

        - **serverReplicationParameters** *(dict) --*

          Parameters for replicating the server.

          - **seedTime** *(datetime) --*

            Seed time for creating a replication job for the server.

          - **frequency** *(integer) --*

            Frequency of creating replication jobs for the server.

          - **runOnce** *(boolean) --*

          - **licenseType** *(string) --*

            License type for creating a replication job for the server.

          - **numberOfRecentAmisToKeep** *(integer) --*

            Number of recent AMIs to keep when creating a replication job for this server.

          - **encrypted** *(boolean) --*

            When true, the replication job produces encrypted AMIs. See also ``KmsKeyId`` below.

          - **kmsKeyId** *(string) --*

            KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
            following:

            * KMS key ID

            * KMS key alias

            * ARN referring to KMS key ID

            * ARN referring to KMS key alias

            If encrypted is *true* but a KMS key id is not specified, the customer's default
            KMS key for EBS is used.
    """


_ClientGetAppReplicationConfigurationResponseTypeDef = TypedDict(
    "_ClientGetAppReplicationConfigurationResponseTypeDef",
    {
        "serverGroupReplicationConfigurations": List[
            ClientGetAppReplicationConfigurationResponseserverGroupReplicationConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientGetAppReplicationConfigurationResponseTypeDef(
    _ClientGetAppReplicationConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetAppReplicationConfiguration` `Response`

    - **serverGroupReplicationConfigurations** *(list) --*

      Replication configurations associated with server groups in this application.

      - *(dict) --*

        Replication configuration for a server group.

        - **serverGroupId** *(string) --*

          Identifier of the server group this replication configuration is associated with.

        - **serverReplicationConfigurations** *(list) --*

          Replication configuration for servers in the server group.

          - *(dict) --*

            Replication configuration of a server.

            - **server** *(dict) --*

              Identifier of the server this replication configuration is associated with.

              - **serverId** *(string) --*

                The identifier of the server.

              - **serverType** *(string) --*

                The type of server.

              - **vmServer** *(dict) --*

                Information about the VM server.

                - **vmServerAddress** *(dict) --*

                  Information about the VM server location.

                  - **vmManagerId** *(string) --*

                    The identifier of the VM manager.

                  - **vmId** *(string) --*

                    The identifier of the VM.

                - **vmName** *(string) --*

                  The name of the VM.

                - **vmManagerName** *(string) --*

                  The name of the VM manager.

                - **vmManagerType** *(string) --*

                  The type of VM management product.

                - **vmPath** *(string) --*

                  The VM folder path in the vCenter Server virtual machine inventory tree.

              - **replicationJobId** *(string) --*

                The identifier of the replication job.

              - **replicationJobTerminated** *(boolean) --*

                Indicates whether the replication job is deleted or failed.

            - **serverReplicationParameters** *(dict) --*

              Parameters for replicating the server.

              - **seedTime** *(datetime) --*

                Seed time for creating a replication job for the server.

              - **frequency** *(integer) --*

                Frequency of creating replication jobs for the server.

              - **runOnce** *(boolean) --*

              - **licenseType** *(string) --*

                License type for creating a replication job for the server.

              - **numberOfRecentAmisToKeep** *(integer) --*

                Number of recent AMIs to keep when creating a replication job for this server.

              - **encrypted** *(boolean) --*

                When true, the replication job produces encrypted AMIs. See also ``KmsKeyId`` below.

              - **kmsKeyId** *(string) --*

                KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
                following:

                * KMS key ID

                * KMS key alias

                * ARN referring to KMS key ID

                * ARN referring to KMS key alias

                If encrypted is *true* but a KMS key id is not specified, the customer's default
                KMS key for EBS is used.
    """


_ClientGetAppResponseappSummarylaunchDetailsTypeDef = TypedDict(
    "_ClientGetAppResponseappSummarylaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)


class ClientGetAppResponseappSummarylaunchDetailsTypeDef(
    _ClientGetAppResponseappSummarylaunchDetailsTypeDef
):
    """
    Type definition for `ClientGetAppResponseappSummary` `launchDetails`

    Details about the latest launch of the application.

    - **latestLaunchTime** *(datetime) --*

      Latest time this application was launched successfully.

    - **stackName** *(string) --*

      Name of the latest stack launched for this application.

    - **stackId** *(string) --*

      Identifier of the latest stack launched for this application.
    """


_ClientGetAppResponseappSummaryTypeDef = TypedDict(
    "_ClientGetAppResponseappSummaryTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "status": str,
        "statusMessage": str,
        "replicationStatus": str,
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchStatus": str,
        "launchStatusMessage": str,
        "launchDetails": ClientGetAppResponseappSummarylaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)


class ClientGetAppResponseappSummaryTypeDef(_ClientGetAppResponseappSummaryTypeDef):
    """
    Type definition for `ClientGetAppResponse` `appSummary`

    Information about the application.

    - **appId** *(string) --*

      Unique ID of the application.

    - **name** *(string) --*

      Name of the application.

    - **description** *(string) --*

      Description of the application.

    - **status** *(string) --*

      Status of the application.

    - **statusMessage** *(string) --*

      A message related to the status of the application

    - **replicationStatus** *(string) --*

      Replication status of the application.

    - **replicationStatusMessage** *(string) --*

      A message related to the replication status of the application.

    - **latestReplicationTime** *(datetime) --*

      Timestamp of the application's most recent successful replication.

    - **launchStatus** *(string) --*

      Launch status of the application.

    - **launchStatusMessage** *(string) --*

      A message related to the launch status of the application.

    - **launchDetails** *(dict) --*

      Details about the latest launch of the application.

      - **latestLaunchTime** *(datetime) --*

        Latest time this application was launched successfully.

      - **stackName** *(string) --*

        Name of the latest stack launched for this application.

      - **stackId** *(string) --*

        Identifier of the latest stack launched for this application.

    - **creationTime** *(datetime) --*

      Time of creation of this application.

    - **lastModified** *(datetime) --*

      Timestamp of the application's creation.

    - **roleName** *(string) --*

      Name of the service role in the customer's account used by AWS SMS.

    - **totalServerGroups** *(integer) --*

      Number of server groups present in the application.

    - **totalServers** *(integer) --*

      Number of servers present in the application.
    """


_ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef(
    _ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientGetAppResponseserverGroupsserverListvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientGetAppResponseserverGroupsserverListvmServerTypeDef = TypedDict(
    "_ClientGetAppResponseserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientGetAppResponseserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientGetAppResponseserverGroupsserverListvmServerTypeDef(
    _ClientGetAppResponseserverGroupsserverListvmServerTypeDef
):
    """
    Type definition for `ClientGetAppResponseserverGroupsserverList` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientGetAppResponseserverGroupsserverListTypeDef = TypedDict(
    "_ClientGetAppResponseserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetAppResponseserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientGetAppResponseserverGroupsserverListTypeDef(
    _ClientGetAppResponseserverGroupsserverListTypeDef
):
    """
    Type definition for `ClientGetAppResponseserverGroups` `serverList`

    Represents a server.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_ClientGetAppResponseserverGroupsTypeDef = TypedDict(
    "_ClientGetAppResponseserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientGetAppResponseserverGroupsserverListTypeDef],
    },
    total=False,
)


class ClientGetAppResponseserverGroupsTypeDef(_ClientGetAppResponseserverGroupsTypeDef):
    """
    Type definition for `ClientGetAppResponse` `serverGroups`

    A logical grouping of servers.

    - **serverGroupId** *(string) --*

      Identifier of a server group.

    - **name** *(string) --*

      Name of a server group.

    - **serverList** *(list) --*

      List of servers belonging to a server group.

      - *(dict) --*

        Represents a server.

        - **serverId** *(string) --*

          The identifier of the server.

        - **serverType** *(string) --*

          The type of server.

        - **vmServer** *(dict) --*

          Information about the VM server.

          - **vmServerAddress** *(dict) --*

            Information about the VM server location.

            - **vmManagerId** *(string) --*

              The identifier of the VM manager.

            - **vmId** *(string) --*

              The identifier of the VM.

          - **vmName** *(string) --*

            The name of the VM.

          - **vmManagerName** *(string) --*

            The name of the VM manager.

          - **vmManagerType** *(string) --*

            The type of VM management product.

          - **vmPath** *(string) --*

            The VM folder path in the vCenter Server virtual machine inventory tree.

        - **replicationJobId** *(string) --*

          The identifier of the replication job.

        - **replicationJobTerminated** *(boolean) --*

          Indicates whether the replication job is deleted or failed.
    """


_ClientGetAppResponsetagsTypeDef = TypedDict(
    "_ClientGetAppResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientGetAppResponsetagsTypeDef(_ClientGetAppResponsetagsTypeDef):
    """
    Type definition for `ClientGetAppResponse` `tags`

    A label that can be assigned to an application.

    - **key** *(string) --*

      Tag key.

    - **value** *(string) --*

      Tag value.
    """


_ClientGetAppResponseTypeDef = TypedDict(
    "_ClientGetAppResponseTypeDef",
    {
        "appSummary": ClientGetAppResponseappSummaryTypeDef,
        "serverGroups": List[ClientGetAppResponseserverGroupsTypeDef],
        "tags": List[ClientGetAppResponsetagsTypeDef],
    },
    total=False,
)


class ClientGetAppResponseTypeDef(_ClientGetAppResponseTypeDef):
    """
    Type definition for `ClientGetApp` `Response`

    - **appSummary** *(dict) --*

      Information about the application.

      - **appId** *(string) --*

        Unique ID of the application.

      - **name** *(string) --*

        Name of the application.

      - **description** *(string) --*

        Description of the application.

      - **status** *(string) --*

        Status of the application.

      - **statusMessage** *(string) --*

        A message related to the status of the application

      - **replicationStatus** *(string) --*

        Replication status of the application.

      - **replicationStatusMessage** *(string) --*

        A message related to the replication status of the application.

      - **latestReplicationTime** *(datetime) --*

        Timestamp of the application's most recent successful replication.

      - **launchStatus** *(string) --*

        Launch status of the application.

      - **launchStatusMessage** *(string) --*

        A message related to the launch status of the application.

      - **launchDetails** *(dict) --*

        Details about the latest launch of the application.

        - **latestLaunchTime** *(datetime) --*

          Latest time this application was launched successfully.

        - **stackName** *(string) --*

          Name of the latest stack launched for this application.

        - **stackId** *(string) --*

          Identifier of the latest stack launched for this application.

      - **creationTime** *(datetime) --*

        Time of creation of this application.

      - **lastModified** *(datetime) --*

        Timestamp of the application's creation.

      - **roleName** *(string) --*

        Name of the service role in the customer's account used by AWS SMS.

      - **totalServerGroups** *(integer) --*

        Number of server groups present in the application.

      - **totalServers** *(integer) --*

        Number of servers present in the application.

    - **serverGroups** *(list) --*

      List of server groups belonging to the application.

      - *(dict) --*

        A logical grouping of servers.

        - **serverGroupId** *(string) --*

          Identifier of a server group.

        - **name** *(string) --*

          Name of a server group.

        - **serverList** *(list) --*

          List of servers belonging to a server group.

          - *(dict) --*

            Represents a server.

            - **serverId** *(string) --*

              The identifier of the server.

            - **serverType** *(string) --*

              The type of server.

            - **vmServer** *(dict) --*

              Information about the VM server.

              - **vmServerAddress** *(dict) --*

                Information about the VM server location.

                - **vmManagerId** *(string) --*

                  The identifier of the VM manager.

                - **vmId** *(string) --*

                  The identifier of the VM.

              - **vmName** *(string) --*

                The name of the VM.

              - **vmManagerName** *(string) --*

                The name of the VM manager.

              - **vmManagerType** *(string) --*

                The type of VM management product.

              - **vmPath** *(string) --*

                The VM folder path in the vCenter Server virtual machine inventory tree.

            - **replicationJobId** *(string) --*

              The identifier of the replication job.

            - **replicationJobTerminated** *(boolean) --*

              Indicates whether the replication job is deleted or failed.

    - **tags** *(list) --*

      List of tags associated with the application.

      - *(dict) --*

        A label that can be assigned to an application.

        - **key** *(string) --*

          Tag key.

        - **value** *(string) --*

          Tag value.
    """


_ClientGetConnectorsResponseconnectorListTypeDef = TypedDict(
    "_ClientGetConnectorsResponseconnectorListTypeDef",
    {
        "connectorId": str,
        "version": str,
        "status": str,
        "capabilityList": List[str],
        "vmManagerName": str,
        "vmManagerType": str,
        "vmManagerId": str,
        "ipAddress": str,
        "macAddress": str,
        "associatedOn": datetime,
    },
    total=False,
)


class ClientGetConnectorsResponseconnectorListTypeDef(
    _ClientGetConnectorsResponseconnectorListTypeDef
):
    """
    Type definition for `ClientGetConnectorsResponse` `connectorList`

    Represents a connector.

    - **connectorId** *(string) --*

      The identifier of the connector.

    - **version** *(string) --*

      The connector version.

    - **status** *(string) --*

      The status of the connector.

    - **capabilityList** *(list) --*

      The capabilities of the connector.

      - *(string) --*

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The VM management product.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **ipAddress** *(string) --*

      The IP address of the connector.

    - **macAddress** *(string) --*

      The MAC address of the connector.

    - **associatedOn** *(datetime) --*

      The time the connector was associated.
    """


_ClientGetConnectorsResponseTypeDef = TypedDict(
    "_ClientGetConnectorsResponseTypeDef",
    {
        "connectorList": List[ClientGetConnectorsResponseconnectorListTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetConnectorsResponseTypeDef(_ClientGetConnectorsResponseTypeDef):
    """
    Type definition for `ClientGetConnectors` `Response`

    - **connectorList** *(list) --*

      Information about the registered connectors.

      - *(dict) --*

        Represents a connector.

        - **connectorId** *(string) --*

          The identifier of the connector.

        - **version** *(string) --*

          The connector version.

        - **status** *(string) --*

          The status of the connector.

        - **capabilityList** *(list) --*

          The capabilities of the connector.

          - *(string) --*

        - **vmManagerName** *(string) --*

          The name of the VM manager.

        - **vmManagerType** *(string) --*

          The VM management product.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **ipAddress** *(string) --*

          The IP address of the connector.

        - **macAddress** *(string) --*

          The MAC address of the connector.

        - **associatedOn** *(datetime) --*

          The time the connector was associated.

    - **nextToken** *(string) --*

      The token required to retrieve the next set of results. This value is null when there are no
      more results to return.
    """


_ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef(
    _ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef
):
    """
    Type definition for `ClientGetReplicationJobsResponsereplicationJobListreplicationRunList` `stageDetails`

    Details of the current stage of the replication run.

    - **stage** *(string) --*

      String describing the current stage of a replication run.

    - **stageProgress** *(string) --*

      String describing the progress of the current stage of a replication run.
    """


_ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": str,
        "type": str,
        "stageDetails": ClientGetReplicationJobsResponsereplicationJobListreplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef(
    _ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef
):
    """
    Type definition for `ClientGetReplicationJobsResponsereplicationJobList` `replicationRunList`

    Represents a replication run.

    - **replicationRunId** *(string) --*

      The identifier of the replication run.

    - **state** *(string) --*

      The state of the replication run.

    - **type** *(string) --*

      The type of replication run.

    - **stageDetails** *(dict) --*

      Details of the current stage of the replication run.

      - **stage** *(string) --*

        String describing the current stage of a replication run.

      - **stageProgress** *(string) --*

        String describing the progress of the current stage of a replication run.

    - **statusMessage** *(string) --*

      The description of the current status of the replication job.

    - **amiId** *(string) --*

      The identifier of the Amazon Machine Image (AMI) from the replication run.

    - **scheduledStartTime** *(datetime) --*

      The start time of the next replication run.

    - **completedTime** *(datetime) --*

      The completion time of the last replication run.

    - **description** *(string) --*

      The description of the replication run.

    - **encrypted** *(boolean) --*

      Whether the replication run should produce encrypted AMI or not. See also
      ``KmsKeyId`` below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
      following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
      key for EBS is used.
    """


_ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef(
    _ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientGetReplicationJobsResponsereplicationJobListvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef",
    {
        "vmServerAddress": ClientGetReplicationJobsResponsereplicationJobListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef(
    _ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef
):
    """
    Type definition for `ClientGetReplicationJobsResponsereplicationJobList` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientGetReplicationJobsResponsereplicationJobListTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponsereplicationJobListTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetReplicationJobsResponsereplicationJobListvmServerTypeDef,
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": str,
        "roleName": str,
        "latestAmiId": str,
        "state": str,
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List[
            ClientGetReplicationJobsResponsereplicationJobListreplicationRunListTypeDef
        ],
    },
    total=False,
)


class ClientGetReplicationJobsResponsereplicationJobListTypeDef(
    _ClientGetReplicationJobsResponsereplicationJobListTypeDef
):
    """
    Type definition for `ClientGetReplicationJobsResponse` `replicationJobList`

    Represents a replication job.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **seedReplicationTime** *(datetime) --*

      The seed replication time.

    - **frequency** *(integer) --*

      The time between consecutive replication runs, in hours.

    - **runOnce** *(boolean) --*

    - **nextReplicationRunStartTime** *(datetime) --*

      The start time of the next replication run.

    - **licenseType** *(string) --*

      The license type to be used for the AMI created by a successful replication run.

    - **roleName** *(string) --*

      The name of the IAM role to be used by the Server Migration Service.

    - **latestAmiId** *(string) --*

      The ID of the latest Amazon Machine Image (AMI).

    - **state** *(string) --*

      The state of the replication job.

    - **statusMessage** *(string) --*

      The description of the current status of the replication job.

    - **description** *(string) --*

      The description of the replication job.

    - **numberOfRecentAmisToKeep** *(integer) --*

      Number of recent AMIs to keep in the customer's account for a replication job. By default
      the value is set to zero, meaning that all AMIs are kept.

    - **encrypted** *(boolean) --*

      Whether the replication job should produce encrypted AMIs or not. See also ``KmsKeyId``
      below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
      for EBS is used.

    - **replicationRunList** *(list) --*

      Information about the replication runs.

      - *(dict) --*

        Represents a replication run.

        - **replicationRunId** *(string) --*

          The identifier of the replication run.

        - **state** *(string) --*

          The state of the replication run.

        - **type** *(string) --*

          The type of replication run.

        - **stageDetails** *(dict) --*

          Details of the current stage of the replication run.

          - **stage** *(string) --*

            String describing the current stage of a replication run.

          - **stageProgress** *(string) --*

            String describing the progress of the current stage of a replication run.

        - **statusMessage** *(string) --*

          The description of the current status of the replication job.

        - **amiId** *(string) --*

          The identifier of the Amazon Machine Image (AMI) from the replication run.

        - **scheduledStartTime** *(datetime) --*

          The start time of the next replication run.

        - **completedTime** *(datetime) --*

          The completion time of the last replication run.

        - **description** *(string) --*

          The description of the replication run.

        - **encrypted** *(boolean) --*

          Whether the replication run should produce encrypted AMI or not. See also
          ``KmsKeyId`` below.

        - **kmsKeyId** *(string) --*

          KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
          following:

          * KMS key ID

          * KMS key alias

          * ARN referring to KMS key ID

          * ARN referring to KMS key alias

          If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
          key for EBS is used.
    """


_ClientGetReplicationJobsResponseTypeDef = TypedDict(
    "_ClientGetReplicationJobsResponseTypeDef",
    {
        "replicationJobList": List[
            ClientGetReplicationJobsResponsereplicationJobListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetReplicationJobsResponseTypeDef(_ClientGetReplicationJobsResponseTypeDef):
    """
    Type definition for `ClientGetReplicationJobs` `Response`

    - **replicationJobList** *(list) --*

      Information about the replication jobs.

      - *(dict) --*

        Represents a replication job.

        - **replicationJobId** *(string) --*

          The identifier of the replication job.

        - **serverId** *(string) --*

          The identifier of the server.

        - **serverType** *(string) --*

          The type of server.

        - **vmServer** *(dict) --*

          Information about the VM server.

          - **vmServerAddress** *(dict) --*

            Information about the VM server location.

            - **vmManagerId** *(string) --*

              The identifier of the VM manager.

            - **vmId** *(string) --*

              The identifier of the VM.

          - **vmName** *(string) --*

            The name of the VM.

          - **vmManagerName** *(string) --*

            The name of the VM manager.

          - **vmManagerType** *(string) --*

            The type of VM management product.

          - **vmPath** *(string) --*

            The VM folder path in the vCenter Server virtual machine inventory tree.

        - **seedReplicationTime** *(datetime) --*

          The seed replication time.

        - **frequency** *(integer) --*

          The time between consecutive replication runs, in hours.

        - **runOnce** *(boolean) --*

        - **nextReplicationRunStartTime** *(datetime) --*

          The start time of the next replication run.

        - **licenseType** *(string) --*

          The license type to be used for the AMI created by a successful replication run.

        - **roleName** *(string) --*

          The name of the IAM role to be used by the Server Migration Service.

        - **latestAmiId** *(string) --*

          The ID of the latest Amazon Machine Image (AMI).

        - **state** *(string) --*

          The state of the replication job.

        - **statusMessage** *(string) --*

          The description of the current status of the replication job.

        - **description** *(string) --*

          The description of the replication job.

        - **numberOfRecentAmisToKeep** *(integer) --*

          Number of recent AMIs to keep in the customer's account for a replication job. By default
          the value is set to zero, meaning that all AMIs are kept.

        - **encrypted** *(boolean) --*

          Whether the replication job should produce encrypted AMIs or not. See also ``KmsKeyId``
          below.

        - **kmsKeyId** *(string) --*

          KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

          * KMS key ID

          * KMS key alias

          * ARN referring to KMS key ID

          * ARN referring to KMS key alias

          If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
          for EBS is used.

        - **replicationRunList** *(list) --*

          Information about the replication runs.

          - *(dict) --*

            Represents a replication run.

            - **replicationRunId** *(string) --*

              The identifier of the replication run.

            - **state** *(string) --*

              The state of the replication run.

            - **type** *(string) --*

              The type of replication run.

            - **stageDetails** *(dict) --*

              Details of the current stage of the replication run.

              - **stage** *(string) --*

                String describing the current stage of a replication run.

              - **stageProgress** *(string) --*

                String describing the progress of the current stage of a replication run.

            - **statusMessage** *(string) --*

              The description of the current status of the replication job.

            - **amiId** *(string) --*

              The identifier of the Amazon Machine Image (AMI) from the replication run.

            - **scheduledStartTime** *(datetime) --*

              The start time of the next replication run.

            - **completedTime** *(datetime) --*

              The completion time of the last replication run.

            - **description** *(string) --*

              The description of the replication run.

            - **encrypted** *(boolean) --*

              Whether the replication run should produce encrypted AMI or not. See also
              ``KmsKeyId`` below.

            - **kmsKeyId** *(string) --*

              KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
              following:

              * KMS key ID

              * KMS key alias

              * ARN referring to KMS key ID

              * ARN referring to KMS key alias

              If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
              key for EBS is used.

    - **nextToken** *(string) --*

      The token required to retrieve the next set of results. This value is null when there are no
      more results to return.
    """


_ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef(
    _ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef
):
    """
    Type definition for `ClientGetReplicationRunsResponsereplicationJobreplicationRunList` `stageDetails`

    Details of the current stage of the replication run.

    - **stage** *(string) --*

      String describing the current stage of a replication run.

    - **stageProgress** *(string) --*

      String describing the progress of the current stage of a replication run.
    """


_ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": str,
        "type": str,
        "stageDetails": ClientGetReplicationRunsResponsereplicationJobreplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef(
    _ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef
):
    """
    Type definition for `ClientGetReplicationRunsResponsereplicationJob` `replicationRunList`

    Represents a replication run.

    - **replicationRunId** *(string) --*

      The identifier of the replication run.

    - **state** *(string) --*

      The state of the replication run.

    - **type** *(string) --*

      The type of replication run.

    - **stageDetails** *(dict) --*

      Details of the current stage of the replication run.

      - **stage** *(string) --*

        String describing the current stage of a replication run.

      - **stageProgress** *(string) --*

        String describing the progress of the current stage of a replication run.

    - **statusMessage** *(string) --*

      The description of the current status of the replication job.

    - **amiId** *(string) --*

      The identifier of the Amazon Machine Image (AMI) from the replication run.

    - **scheduledStartTime** *(datetime) --*

      The start time of the next replication run.

    - **completedTime** *(datetime) --*

      The completion time of the last replication run.

    - **description** *(string) --*

      The description of the replication run.

    - **encrypted** *(boolean) --*

      Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId``
      below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
      following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
      key for EBS is used.
    """


_ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef(
    _ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientGetReplicationRunsResponsereplicationJobvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef",
    {
        "vmServerAddress": ClientGetReplicationRunsResponsereplicationJobvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef(
    _ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef
):
    """
    Type definition for `ClientGetReplicationRunsResponsereplicationJob` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientGetReplicationRunsResponsereplicationJobTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationJobTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetReplicationRunsResponsereplicationJobvmServerTypeDef,
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": str,
        "roleName": str,
        "latestAmiId": str,
        "state": str,
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List[
            ClientGetReplicationRunsResponsereplicationJobreplicationRunListTypeDef
        ],
    },
    total=False,
)


class ClientGetReplicationRunsResponsereplicationJobTypeDef(
    _ClientGetReplicationRunsResponsereplicationJobTypeDef
):
    """
    Type definition for `ClientGetReplicationRunsResponse` `replicationJob`

    Information about the replication job.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **seedReplicationTime** *(datetime) --*

      The seed replication time.

    - **frequency** *(integer) --*

      The time between consecutive replication runs, in hours.

    - **runOnce** *(boolean) --*

    - **nextReplicationRunStartTime** *(datetime) --*

      The start time of the next replication run.

    - **licenseType** *(string) --*

      The license type to be used for the AMI created by a successful replication run.

    - **roleName** *(string) --*

      The name of the IAM role to be used by the Server Migration Service.

    - **latestAmiId** *(string) --*

      The ID of the latest Amazon Machine Image (AMI).

    - **state** *(string) --*

      The state of the replication job.

    - **statusMessage** *(string) --*

      The description of the current status of the replication job.

    - **description** *(string) --*

      The description of the replication job.

    - **numberOfRecentAmisToKeep** *(integer) --*

      Number of recent AMIs to keep in the customer's account for a replication job. By default
      the value is set to zero, meaning that all AMIs are kept.

    - **encrypted** *(boolean) --*

      Whether the replication job should produce encrypted AMIs or not. See also ``KmsKeyId``
      below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
      for EBS is used.

    - **replicationRunList** *(list) --*

      Information about the replication runs.

      - *(dict) --*

        Represents a replication run.

        - **replicationRunId** *(string) --*

          The identifier of the replication run.

        - **state** *(string) --*

          The state of the replication run.

        - **type** *(string) --*

          The type of replication run.

        - **stageDetails** *(dict) --*

          Details of the current stage of the replication run.

          - **stage** *(string) --*

            String describing the current stage of a replication run.

          - **stageProgress** *(string) --*

            String describing the progress of the current stage of a replication run.

        - **statusMessage** *(string) --*

          The description of the current status of the replication job.

        - **amiId** *(string) --*

          The identifier of the Amazon Machine Image (AMI) from the replication run.

        - **scheduledStartTime** *(datetime) --*

          The start time of the next replication run.

        - **completedTime** *(datetime) --*

          The completion time of the last replication run.

        - **description** *(string) --*

          The description of the replication run.

        - **encrypted** *(boolean) --*

          Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId``
          below.

        - **kmsKeyId** *(string) --*

          KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
          following:

          * KMS key ID

          * KMS key alias

          * ARN referring to KMS key ID

          * ARN referring to KMS key alias

          If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
          key for EBS is used.
    """


_ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef(
    _ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef
):
    """
    Type definition for `ClientGetReplicationRunsResponsereplicationRunList` `stageDetails`

    Details of the current stage of the replication run.

    - **stage** *(string) --*

      String describing the current stage of a replication run.

    - **stageProgress** *(string) --*

      String describing the progress of the current stage of a replication run.
    """


_ClientGetReplicationRunsResponsereplicationRunListTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponsereplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": str,
        "type": str,
        "stageDetails": ClientGetReplicationRunsResponsereplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientGetReplicationRunsResponsereplicationRunListTypeDef(
    _ClientGetReplicationRunsResponsereplicationRunListTypeDef
):
    """
    Type definition for `ClientGetReplicationRunsResponse` `replicationRunList`

    Represents a replication run.

    - **replicationRunId** *(string) --*

      The identifier of the replication run.

    - **state** *(string) --*

      The state of the replication run.

    - **type** *(string) --*

      The type of replication run.

    - **stageDetails** *(dict) --*

      Details of the current stage of the replication run.

      - **stage** *(string) --*

        String describing the current stage of a replication run.

      - **stageProgress** *(string) --*

        String describing the progress of the current stage of a replication run.

    - **statusMessage** *(string) --*

      The description of the current status of the replication job.

    - **amiId** *(string) --*

      The identifier of the Amazon Machine Image (AMI) from the replication run.

    - **scheduledStartTime** *(datetime) --*

      The start time of the next replication run.

    - **completedTime** *(datetime) --*

      The completion time of the last replication run.

    - **description** *(string) --*

      The description of the replication run.

    - **encrypted** *(boolean) --*

      Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId``
      below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
      for EBS is used.
    """


_ClientGetReplicationRunsResponseTypeDef = TypedDict(
    "_ClientGetReplicationRunsResponseTypeDef",
    {
        "replicationJob": ClientGetReplicationRunsResponsereplicationJobTypeDef,
        "replicationRunList": List[
            ClientGetReplicationRunsResponsereplicationRunListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetReplicationRunsResponseTypeDef(_ClientGetReplicationRunsResponseTypeDef):
    """
    Type definition for `ClientGetReplicationRuns` `Response`

    - **replicationJob** *(dict) --*

      Information about the replication job.

      - **replicationJobId** *(string) --*

        The identifier of the replication job.

      - **serverId** *(string) --*

        The identifier of the server.

      - **serverType** *(string) --*

        The type of server.

      - **vmServer** *(dict) --*

        Information about the VM server.

        - **vmServerAddress** *(dict) --*

          Information about the VM server location.

          - **vmManagerId** *(string) --*

            The identifier of the VM manager.

          - **vmId** *(string) --*

            The identifier of the VM.

        - **vmName** *(string) --*

          The name of the VM.

        - **vmManagerName** *(string) --*

          The name of the VM manager.

        - **vmManagerType** *(string) --*

          The type of VM management product.

        - **vmPath** *(string) --*

          The VM folder path in the vCenter Server virtual machine inventory tree.

      - **seedReplicationTime** *(datetime) --*

        The seed replication time.

      - **frequency** *(integer) --*

        The time between consecutive replication runs, in hours.

      - **runOnce** *(boolean) --*

      - **nextReplicationRunStartTime** *(datetime) --*

        The start time of the next replication run.

      - **licenseType** *(string) --*

        The license type to be used for the AMI created by a successful replication run.

      - **roleName** *(string) --*

        The name of the IAM role to be used by the Server Migration Service.

      - **latestAmiId** *(string) --*

        The ID of the latest Amazon Machine Image (AMI).

      - **state** *(string) --*

        The state of the replication job.

      - **statusMessage** *(string) --*

        The description of the current status of the replication job.

      - **description** *(string) --*

        The description of the replication job.

      - **numberOfRecentAmisToKeep** *(integer) --*

        Number of recent AMIs to keep in the customer's account for a replication job. By default
        the value is set to zero, meaning that all AMIs are kept.

      - **encrypted** *(boolean) --*

        Whether the replication job should produce encrypted AMIs or not. See also ``KmsKeyId``
        below.

      - **kmsKeyId** *(string) --*

        KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

        * KMS key ID

        * KMS key alias

        * ARN referring to KMS key ID

        * ARN referring to KMS key alias

        If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
        for EBS is used.

      - **replicationRunList** *(list) --*

        Information about the replication runs.

        - *(dict) --*

          Represents a replication run.

          - **replicationRunId** *(string) --*

            The identifier of the replication run.

          - **state** *(string) --*

            The state of the replication run.

          - **type** *(string) --*

            The type of replication run.

          - **stageDetails** *(dict) --*

            Details of the current stage of the replication run.

            - **stage** *(string) --*

              String describing the current stage of a replication run.

            - **stageProgress** *(string) --*

              String describing the progress of the current stage of a replication run.

          - **statusMessage** *(string) --*

            The description of the current status of the replication job.

          - **amiId** *(string) --*

            The identifier of the Amazon Machine Image (AMI) from the replication run.

          - **scheduledStartTime** *(datetime) --*

            The start time of the next replication run.

          - **completedTime** *(datetime) --*

            The completion time of the last replication run.

          - **description** *(string) --*

            The description of the replication run.

          - **encrypted** *(boolean) --*

            Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId``
            below.

          - **kmsKeyId** *(string) --*

            KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
            following:

            * KMS key ID

            * KMS key alias

            * ARN referring to KMS key ID

            * ARN referring to KMS key alias

            If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
            key for EBS is used.

    - **replicationRunList** *(list) --*

      Information about the replication runs.

      - *(dict) --*

        Represents a replication run.

        - **replicationRunId** *(string) --*

          The identifier of the replication run.

        - **state** *(string) --*

          The state of the replication run.

        - **type** *(string) --*

          The type of replication run.

        - **stageDetails** *(dict) --*

          Details of the current stage of the replication run.

          - **stage** *(string) --*

            String describing the current stage of a replication run.

          - **stageProgress** *(string) --*

            String describing the progress of the current stage of a replication run.

        - **statusMessage** *(string) --*

          The description of the current status of the replication job.

        - **amiId** *(string) --*

          The identifier of the Amazon Machine Image (AMI) from the replication run.

        - **scheduledStartTime** *(datetime) --*

          The start time of the next replication run.

        - **completedTime** *(datetime) --*

          The completion time of the last replication run.

        - **description** *(string) --*

          The description of the replication run.

        - **encrypted** *(boolean) --*

          Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId``
          below.

        - **kmsKeyId** *(string) --*

          KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

          * KMS key ID

          * KMS key alias

          * ARN referring to KMS key ID

          * ARN referring to KMS key alias

          If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
          for EBS is used.

    - **nextToken** *(string) --*

      The token required to retrieve the next set of results. This value is null when there are no
      more results to return.
    """


_ClientGetServersResponseserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientGetServersResponseserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetServersResponseserverListvmServervmServerAddressTypeDef(
    _ClientGetServersResponseserverListvmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientGetServersResponseserverListvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientGetServersResponseserverListvmServerTypeDef = TypedDict(
    "_ClientGetServersResponseserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientGetServersResponseserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientGetServersResponseserverListvmServerTypeDef(
    _ClientGetServersResponseserverListvmServerTypeDef
):
    """
    Type definition for `ClientGetServersResponseserverList` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientGetServersResponseserverListTypeDef = TypedDict(
    "_ClientGetServersResponseserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientGetServersResponseserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientGetServersResponseserverListTypeDef(
    _ClientGetServersResponseserverListTypeDef
):
    """
    Type definition for `ClientGetServersResponse` `serverList`

    Represents a server.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_ClientGetServersResponseTypeDef = TypedDict(
    "_ClientGetServersResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": str,
        "serverList": List[ClientGetServersResponseserverListTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetServersResponseTypeDef(_ClientGetServersResponseTypeDef):
    """
    Type definition for `ClientGetServers` `Response`

    - **lastModifiedOn** *(datetime) --*

      The time when the server was last modified.

    - **serverCatalogStatus** *(string) --*

      The status of the server catalog.

    - **serverList** *(list) --*

      Information about the servers.

      - *(dict) --*

        Represents a server.

        - **serverId** *(string) --*

          The identifier of the server.

        - **serverType** *(string) --*

          The type of server.

        - **vmServer** *(dict) --*

          Information about the VM server.

          - **vmServerAddress** *(dict) --*

            Information about the VM server location.

            - **vmManagerId** *(string) --*

              The identifier of the VM manager.

            - **vmId** *(string) --*

              The identifier of the VM.

          - **vmName** *(string) --*

            The name of the VM.

          - **vmManagerName** *(string) --*

            The name of the VM manager.

          - **vmManagerType** *(string) --*

            The type of VM management product.

          - **vmPath** *(string) --*

            The VM folder path in the vCenter Server virtual machine inventory tree.

        - **replicationJobId** *(string) --*

          The identifier of the replication job.

        - **replicationJobTerminated** *(boolean) --*

          Indicates whether the replication job is deleted or failed.

    - **nextToken** *(string) --*

      The token required to retrieve the next set of results. This value is null when there are no
      more results to return.
    """


_ClientGetServersvmServerAddressListTypeDef = TypedDict(
    "_ClientGetServersvmServerAddressListTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientGetServersvmServerAddressListTypeDef(
    _ClientGetServersvmServerAddressListTypeDef
):
    """
    Type definition for `ClientGetServers` `vmServerAddressList`

    Represents a VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientListAppsResponseappslaunchDetailsTypeDef = TypedDict(
    "_ClientListAppsResponseappslaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)


class ClientListAppsResponseappslaunchDetailsTypeDef(
    _ClientListAppsResponseappslaunchDetailsTypeDef
):
    """
    Type definition for `ClientListAppsResponseapps` `launchDetails`

    Details about the latest launch of the application.

    - **latestLaunchTime** *(datetime) --*

      Latest time this application was launched successfully.

    - **stackName** *(string) --*

      Name of the latest stack launched for this application.

    - **stackId** *(string) --*

      Identifier of the latest stack launched for this application.
    """


_ClientListAppsResponseappsTypeDef = TypedDict(
    "_ClientListAppsResponseappsTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "status": str,
        "statusMessage": str,
        "replicationStatus": str,
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchStatus": str,
        "launchStatusMessage": str,
        "launchDetails": ClientListAppsResponseappslaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)


class ClientListAppsResponseappsTypeDef(_ClientListAppsResponseappsTypeDef):
    """
    Type definition for `ClientListAppsResponse` `apps`

    Information about the application.

    - **appId** *(string) --*

      Unique ID of the application.

    - **name** *(string) --*

      Name of the application.

    - **description** *(string) --*

      Description of the application.

    - **status** *(string) --*

      Status of the application.

    - **statusMessage** *(string) --*

      A message related to the status of the application

    - **replicationStatus** *(string) --*

      Replication status of the application.

    - **replicationStatusMessage** *(string) --*

      A message related to the replication status of the application.

    - **latestReplicationTime** *(datetime) --*

      Timestamp of the application's most recent successful replication.

    - **launchStatus** *(string) --*

      Launch status of the application.

    - **launchStatusMessage** *(string) --*

      A message related to the launch status of the application.

    - **launchDetails** *(dict) --*

      Details about the latest launch of the application.

      - **latestLaunchTime** *(datetime) --*

        Latest time this application was launched successfully.

      - **stackName** *(string) --*

        Name of the latest stack launched for this application.

      - **stackId** *(string) --*

        Identifier of the latest stack launched for this application.

    - **creationTime** *(datetime) --*

      Time of creation of this application.

    - **lastModified** *(datetime) --*

      Timestamp of the application's creation.

    - **roleName** *(string) --*

      Name of the service role in the customer's account used by AWS SMS.

    - **totalServerGroups** *(integer) --*

      Number of server groups present in the application.

    - **totalServers** *(integer) --*

      Number of servers present in the application.
    """


_ClientListAppsResponseTypeDef = TypedDict(
    "_ClientListAppsResponseTypeDef",
    {"apps": List[ClientListAppsResponseappsTypeDef], "nextToken": str},
    total=False,
)


class ClientListAppsResponseTypeDef(_ClientListAppsResponseTypeDef):
    """
    Type definition for `ClientListApps` `Response`

    - **apps** *(list) --*

      A list of application summaries.

      - *(dict) --*

        Information about the application.

        - **appId** *(string) --*

          Unique ID of the application.

        - **name** *(string) --*

          Name of the application.

        - **description** *(string) --*

          Description of the application.

        - **status** *(string) --*

          Status of the application.

        - **statusMessage** *(string) --*

          A message related to the status of the application

        - **replicationStatus** *(string) --*

          Replication status of the application.

        - **replicationStatusMessage** *(string) --*

          A message related to the replication status of the application.

        - **latestReplicationTime** *(datetime) --*

          Timestamp of the application's most recent successful replication.

        - **launchStatus** *(string) --*

          Launch status of the application.

        - **launchStatusMessage** *(string) --*

          A message related to the launch status of the application.

        - **launchDetails** *(dict) --*

          Details about the latest launch of the application.

          - **latestLaunchTime** *(datetime) --*

            Latest time this application was launched successfully.

          - **stackName** *(string) --*

            Name of the latest stack launched for this application.

          - **stackId** *(string) --*

            Identifier of the latest stack launched for this application.

        - **creationTime** *(datetime) --*

          Time of creation of this application.

        - **lastModified** *(datetime) --*

          Timestamp of the application's creation.

        - **roleName** *(string) --*

          Name of the service role in the customer's account used by AWS SMS.

        - **totalServerGroups** *(integer) --*

          Number of server groups present in the application.

        - **totalServers** *(integer) --*

          Number of servers present in the application.

    - **nextToken** *(string) --*

      The token required to retrieve the next set of results. This value is null when there are no
      more results to return.
    """


_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef(
    _ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef(
    _ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef
):
    """
    Type definition for `ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsserver` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef(
    _ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef
):
    """
    Type definition for `ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurations` `server`

    Identifier of the server the launch configuration is associated with.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef",
    {"bucket": str, "key": str},
    total=False,
)


class ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef(
    _ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef
):
    """
    Type definition for `ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserData` `s3Location`

    Amazon S3 location of the user-data script.

    - **bucket** *(string) --*

      Amazon S3 bucket name.

    - **key** *(string) --*

      Amazon S3 bucket key.
    """


_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef",
    {
        "s3Location": ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDatas3LocationTypeDef
    },
    total=False,
)


class ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef(
    _ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef
):
    """
    Type definition for `ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurations` `userData`

    Location of the user-data script to be executed when launching the server.

    - **s3Location** *(dict) --*

      Amazon S3 location of the user-data script.

      - **bucket** *(string) --*

        Amazon S3 bucket name.

      - **key** *(string) --*

        Amazon S3 bucket key.
    """


_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef",
    {
        "server": ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsserverTypeDef,
        "logicalId": str,
        "vpc": str,
        "subnet": str,
        "securityGroup": str,
        "ec2KeyName": str,
        "userData": ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsuserDataTypeDef,
        "instanceType": str,
        "associatePublicIpAddress": bool,
    },
    total=False,
)


class ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef(
    _ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef
):
    """
    Type definition for `ClientPutAppLaunchConfigurationserverGroupLaunchConfigurations` `serverLaunchConfigurations`

    Launch configuration for a server.

    - **server** *(dict) --*

      Identifier of the server the launch configuration is associated with.

      - **serverId** *(string) --*

        The identifier of the server.

      - **serverType** *(string) --*

        The type of server.

      - **vmServer** *(dict) --*

        Information about the VM server.

        - **vmServerAddress** *(dict) --*

          Information about the VM server location.

          - **vmManagerId** *(string) --*

            The identifier of the VM manager.

          - **vmId** *(string) --*

            The identifier of the VM.

        - **vmName** *(string) --*

          The name of the VM.

        - **vmManagerName** *(string) --*

          The name of the VM manager.

        - **vmManagerType** *(string) --*

          The type of VM management product.

        - **vmPath** *(string) --*

          The VM folder path in the vCenter Server virtual machine inventory tree.

      - **replicationJobId** *(string) --*

        The identifier of the replication job.

      - **replicationJobTerminated** *(boolean) --*

        Indicates whether the replication job is deleted or failed.

    - **logicalId** *(string) --*

      Logical ID of the server in the Amazon CloudFormation template.

    - **vpc** *(string) --*

      Identifier of the VPC the server should be launched into.

    - **subnet** *(string) --*

      Identifier of the subnet the server should be launched into.

    - **securityGroup** *(string) --*

      Identifier of the security group that applies to the launched server.

    - **ec2KeyName** *(string) --*

      Name of the EC2 SSH Key to be used for connecting to the launched server.

    - **userData** *(dict) --*

      Location of the user-data script to be executed when launching the server.

      - **s3Location** *(dict) --*

        Amazon S3 location of the user-data script.

        - **bucket** *(string) --*

          Amazon S3 bucket name.

        - **key** *(string) --*

          Amazon S3 bucket key.

    - **instanceType** *(string) --*

      Instance type to be used for launching the server.

    - **associatePublicIpAddress** *(boolean) --*

      If true, a publicly accessible IP address is created when launching the server.
    """


_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsTypeDef = TypedDict(
    "_ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": List[
            ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsserverLaunchConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsTypeDef(
    _ClientPutAppLaunchConfigurationserverGroupLaunchConfigurationsTypeDef
):
    """
    Type definition for `ClientPutAppLaunchConfiguration` `serverGroupLaunchConfigurations`

    Launch configuration for a server group.

    - **serverGroupId** *(string) --*

      Identifier of the server group the launch configuration is associated with.

    - **launchOrder** *(integer) --*

      Launch order of servers in the server group.

    - **serverLaunchConfigurations** *(list) --*

      Launch configuration for servers in the server group.

      - *(dict) --*

        Launch configuration for a server.

        - **server** *(dict) --*

          Identifier of the server the launch configuration is associated with.

          - **serverId** *(string) --*

            The identifier of the server.

          - **serverType** *(string) --*

            The type of server.

          - **vmServer** *(dict) --*

            Information about the VM server.

            - **vmServerAddress** *(dict) --*

              Information about the VM server location.

              - **vmManagerId** *(string) --*

                The identifier of the VM manager.

              - **vmId** *(string) --*

                The identifier of the VM.

            - **vmName** *(string) --*

              The name of the VM.

            - **vmManagerName** *(string) --*

              The name of the VM manager.

            - **vmManagerType** *(string) --*

              The type of VM management product.

            - **vmPath** *(string) --*

              The VM folder path in the vCenter Server virtual machine inventory tree.

          - **replicationJobId** *(string) --*

            The identifier of the replication job.

          - **replicationJobTerminated** *(boolean) --*

            Indicates whether the replication job is deleted or failed.

        - **logicalId** *(string) --*

          Logical ID of the server in the Amazon CloudFormation template.

        - **vpc** *(string) --*

          Identifier of the VPC the server should be launched into.

        - **subnet** *(string) --*

          Identifier of the subnet the server should be launched into.

        - **securityGroup** *(string) --*

          Identifier of the security group that applies to the launched server.

        - **ec2KeyName** *(string) --*

          Name of the EC2 SSH Key to be used for connecting to the launched server.

        - **userData** *(dict) --*

          Location of the user-data script to be executed when launching the server.

          - **s3Location** *(dict) --*

            Amazon S3 location of the user-data script.

            - **bucket** *(string) --*

              Amazon S3 bucket name.

            - **key** *(string) --*

              Amazon S3 bucket key.

        - **instanceType** *(string) --*

          Instance type to be used for launching the server.

        - **associatePublicIpAddress** *(boolean) --*

          If true, a publicly accessible IP address is created when launching the server.
    """


_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef",
    {
        "seedTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "licenseType": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef(
    _ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef
):
    """
    Type definition for `ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurations` `serverReplicationParameters`

    Parameters for replicating the server.

    - **seedTime** *(datetime) --*

      Seed time for creating a replication job for the server.

    - **frequency** *(integer) --*

      Frequency of creating replication jobs for the server.

    - **runOnce** *(boolean) --*

    - **licenseType** *(string) --*

      License type for creating a replication job for the server.

    - **numberOfRecentAmisToKeep** *(integer) --*

      Number of recent AMIs to keep when creating a replication job for this server.

    - **encrypted** *(boolean) --*

      When true, the replication job produces encrypted AMIs. See also ``KmsKeyId`` below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
      following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
      key for EBS is used.
    """


_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef(
    _ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef",
    {
        "vmServerAddress": ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef(
    _ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef
):
    """
    Type definition for `ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserver` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsservervmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef(
    _ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef
):
    """
    Type definition for `ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurations` `server`

    Identifier of the server this replication configuration is associated with.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef",
    {
        "server": ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverTypeDef,
        "serverReplicationParameters": ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsserverReplicationParametersTypeDef,
    },
    total=False,
)


class ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef(
    _ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef
):
    """
    Type definition for `ClientPutAppReplicationConfigurationserverGroupReplicationConfigurations` `serverReplicationConfigurations`

    Replication configuration of a server.

    - **server** *(dict) --*

      Identifier of the server this replication configuration is associated with.

      - **serverId** *(string) --*

        The identifier of the server.

      - **serverType** *(string) --*

        The type of server.

      - **vmServer** *(dict) --*

        Information about the VM server.

        - **vmServerAddress** *(dict) --*

          Information about the VM server location.

          - **vmManagerId** *(string) --*

            The identifier of the VM manager.

          - **vmId** *(string) --*

            The identifier of the VM.

        - **vmName** *(string) --*

          The name of the VM.

        - **vmManagerName** *(string) --*

          The name of the VM manager.

        - **vmManagerType** *(string) --*

          The type of VM management product.

        - **vmPath** *(string) --*

          The VM folder path in the vCenter Server virtual machine inventory tree.

      - **replicationJobId** *(string) --*

        The identifier of the replication job.

      - **replicationJobTerminated** *(boolean) --*

        Indicates whether the replication job is deleted or failed.

    - **serverReplicationParameters** *(dict) --*

      Parameters for replicating the server.

      - **seedTime** *(datetime) --*

        Seed time for creating a replication job for the server.

      - **frequency** *(integer) --*

        Frequency of creating replication jobs for the server.

      - **runOnce** *(boolean) --*

      - **licenseType** *(string) --*

        License type for creating a replication job for the server.

      - **numberOfRecentAmisToKeep** *(integer) --*

        Number of recent AMIs to keep when creating a replication job for this server.

      - **encrypted** *(boolean) --*

        When true, the replication job produces encrypted AMIs. See also ``KmsKeyId`` below.

      - **kmsKeyId** *(string) --*

        KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
        following:

        * KMS key ID

        * KMS key alias

        * ARN referring to KMS key ID

        * ARN referring to KMS key alias

        If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
        key for EBS is used.
    """


_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsTypeDef = TypedDict(
    "_ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": List[
            ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsserverReplicationConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsTypeDef(
    _ClientPutAppReplicationConfigurationserverGroupReplicationConfigurationsTypeDef
):
    """
    Type definition for `ClientPutAppReplicationConfiguration` `serverGroupReplicationConfigurations`

    Replication configuration for a server group.

    - **serverGroupId** *(string) --*

      Identifier of the server group this replication configuration is associated with.

    - **serverReplicationConfigurations** *(list) --*

      Replication configuration for servers in the server group.

      - *(dict) --*

        Replication configuration of a server.

        - **server** *(dict) --*

          Identifier of the server this replication configuration is associated with.

          - **serverId** *(string) --*

            The identifier of the server.

          - **serverType** *(string) --*

            The type of server.

          - **vmServer** *(dict) --*

            Information about the VM server.

            - **vmServerAddress** *(dict) --*

              Information about the VM server location.

              - **vmManagerId** *(string) --*

                The identifier of the VM manager.

              - **vmId** *(string) --*

                The identifier of the VM.

            - **vmName** *(string) --*

              The name of the VM.

            - **vmManagerName** *(string) --*

              The name of the VM manager.

            - **vmManagerType** *(string) --*

              The type of VM management product.

            - **vmPath** *(string) --*

              The VM folder path in the vCenter Server virtual machine inventory tree.

          - **replicationJobId** *(string) --*

            The identifier of the replication job.

          - **replicationJobTerminated** *(boolean) --*

            Indicates whether the replication job is deleted or failed.

        - **serverReplicationParameters** *(dict) --*

          Parameters for replicating the server.

          - **seedTime** *(datetime) --*

            Seed time for creating a replication job for the server.

          - **frequency** *(integer) --*

            Frequency of creating replication jobs for the server.

          - **runOnce** *(boolean) --*

          - **licenseType** *(string) --*

            License type for creating a replication job for the server.

          - **numberOfRecentAmisToKeep** *(integer) --*

            Number of recent AMIs to keep when creating a replication job for this server.

          - **encrypted** *(boolean) --*

            When true, the replication job produces encrypted AMIs. See also ``KmsKeyId`` below.

          - **kmsKeyId** *(string) --*

            KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
            following:

            * KMS key ID

            * KMS key alias

            * ARN referring to KMS key ID

            * ARN referring to KMS key alias

            If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
            key for EBS is used.
    """


_ClientStartOnDemandReplicationRunResponseTypeDef = TypedDict(
    "_ClientStartOnDemandReplicationRunResponseTypeDef",
    {"replicationRunId": str},
    total=False,
)


class ClientStartOnDemandReplicationRunResponseTypeDef(
    _ClientStartOnDemandReplicationRunResponseTypeDef
):
    """
    Type definition for `ClientStartOnDemandReplicationRun` `Response`

    - **replicationRunId** *(string) --*

      The identifier of the replication run.
    """


_ClientUpdateAppResponseappSummarylaunchDetailsTypeDef = TypedDict(
    "_ClientUpdateAppResponseappSummarylaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)


class ClientUpdateAppResponseappSummarylaunchDetailsTypeDef(
    _ClientUpdateAppResponseappSummarylaunchDetailsTypeDef
):
    """
    Type definition for `ClientUpdateAppResponseappSummary` `launchDetails`

    Details about the latest launch of the application.

    - **latestLaunchTime** *(datetime) --*

      Latest time this application was launched successfully.

    - **stackName** *(string) --*

      Name of the latest stack launched for this application.

    - **stackId** *(string) --*

      Identifier of the latest stack launched for this application.
    """


_ClientUpdateAppResponseappSummaryTypeDef = TypedDict(
    "_ClientUpdateAppResponseappSummaryTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "status": str,
        "statusMessage": str,
        "replicationStatus": str,
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchStatus": str,
        "launchStatusMessage": str,
        "launchDetails": ClientUpdateAppResponseappSummarylaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)


class ClientUpdateAppResponseappSummaryTypeDef(
    _ClientUpdateAppResponseappSummaryTypeDef
):
    """
    Type definition for `ClientUpdateAppResponse` `appSummary`

    Summary description of the application.

    - **appId** *(string) --*

      Unique ID of the application.

    - **name** *(string) --*

      Name of the application.

    - **description** *(string) --*

      Description of the application.

    - **status** *(string) --*

      Status of the application.

    - **statusMessage** *(string) --*

      A message related to the status of the application

    - **replicationStatus** *(string) --*

      Replication status of the application.

    - **replicationStatusMessage** *(string) --*

      A message related to the replication status of the application.

    - **latestReplicationTime** *(datetime) --*

      Timestamp of the application's most recent successful replication.

    - **launchStatus** *(string) --*

      Launch status of the application.

    - **launchStatusMessage** *(string) --*

      A message related to the launch status of the application.

    - **launchDetails** *(dict) --*

      Details about the latest launch of the application.

      - **latestLaunchTime** *(datetime) --*

        Latest time this application was launched successfully.

      - **stackName** *(string) --*

        Name of the latest stack launched for this application.

      - **stackId** *(string) --*

        Identifier of the latest stack launched for this application.

    - **creationTime** *(datetime) --*

      Time of creation of this application.

    - **lastModified** *(datetime) --*

      Timestamp of the application's creation.

    - **roleName** *(string) --*

      Name of the service role in the customer's account used by AWS SMS.

    - **totalServerGroups** *(integer) --*

      Number of server groups present in the application.

    - **totalServers** *(integer) --*

      Number of servers present in the application.
    """


_ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef(
    _ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientUpdateAppResponseserverGroupsserverListvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef = TypedDict(
    "_ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientUpdateAppResponseserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef(
    _ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef
):
    """
    Type definition for `ClientUpdateAppResponseserverGroupsserverList` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientUpdateAppResponseserverGroupsserverListTypeDef = TypedDict(
    "_ClientUpdateAppResponseserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientUpdateAppResponseserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientUpdateAppResponseserverGroupsserverListTypeDef(
    _ClientUpdateAppResponseserverGroupsserverListTypeDef
):
    """
    Type definition for `ClientUpdateAppResponseserverGroups` `serverList`

    Represents a server.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_ClientUpdateAppResponseserverGroupsTypeDef = TypedDict(
    "_ClientUpdateAppResponseserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientUpdateAppResponseserverGroupsserverListTypeDef],
    },
    total=False,
)


class ClientUpdateAppResponseserverGroupsTypeDef(
    _ClientUpdateAppResponseserverGroupsTypeDef
):
    """
    Type definition for `ClientUpdateAppResponse` `serverGroups`

    A logical grouping of servers.

    - **serverGroupId** *(string) --*

      Identifier of a server group.

    - **name** *(string) --*

      Name of a server group.

    - **serverList** *(list) --*

      List of servers belonging to a server group.

      - *(dict) --*

        Represents a server.

        - **serverId** *(string) --*

          The identifier of the server.

        - **serverType** *(string) --*

          The type of server.

        - **vmServer** *(dict) --*

          Information about the VM server.

          - **vmServerAddress** *(dict) --*

            Information about the VM server location.

            - **vmManagerId** *(string) --*

              The identifier of the VM manager.

            - **vmId** *(string) --*

              The identifier of the VM.

          - **vmName** *(string) --*

            The name of the VM.

          - **vmManagerName** *(string) --*

            The name of the VM manager.

          - **vmManagerType** *(string) --*

            The type of VM management product.

          - **vmPath** *(string) --*

            The VM folder path in the vCenter Server virtual machine inventory tree.

        - **replicationJobId** *(string) --*

          The identifier of the replication job.

        - **replicationJobTerminated** *(boolean) --*

          Indicates whether the replication job is deleted or failed.
    """


_ClientUpdateAppResponsetagsTypeDef = TypedDict(
    "_ClientUpdateAppResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateAppResponsetagsTypeDef(_ClientUpdateAppResponsetagsTypeDef):
    """
    Type definition for `ClientUpdateAppResponse` `tags`

    A label that can be assigned to an application.

    - **key** *(string) --*

      Tag key.

    - **value** *(string) --*

      Tag value.
    """


_ClientUpdateAppResponseTypeDef = TypedDict(
    "_ClientUpdateAppResponseTypeDef",
    {
        "appSummary": ClientUpdateAppResponseappSummaryTypeDef,
        "serverGroups": List[ClientUpdateAppResponseserverGroupsTypeDef],
        "tags": List[ClientUpdateAppResponsetagsTypeDef],
    },
    total=False,
)


class ClientUpdateAppResponseTypeDef(_ClientUpdateAppResponseTypeDef):
    """
    Type definition for `ClientUpdateApp` `Response`

    - **appSummary** *(dict) --*

      Summary description of the application.

      - **appId** *(string) --*

        Unique ID of the application.

      - **name** *(string) --*

        Name of the application.

      - **description** *(string) --*

        Description of the application.

      - **status** *(string) --*

        Status of the application.

      - **statusMessage** *(string) --*

        A message related to the status of the application

      - **replicationStatus** *(string) --*

        Replication status of the application.

      - **replicationStatusMessage** *(string) --*

        A message related to the replication status of the application.

      - **latestReplicationTime** *(datetime) --*

        Timestamp of the application's most recent successful replication.

      - **launchStatus** *(string) --*

        Launch status of the application.

      - **launchStatusMessage** *(string) --*

        A message related to the launch status of the application.

      - **launchDetails** *(dict) --*

        Details about the latest launch of the application.

        - **latestLaunchTime** *(datetime) --*

          Latest time this application was launched successfully.

        - **stackName** *(string) --*

          Name of the latest stack launched for this application.

        - **stackId** *(string) --*

          Identifier of the latest stack launched for this application.

      - **creationTime** *(datetime) --*

        Time of creation of this application.

      - **lastModified** *(datetime) --*

        Timestamp of the application's creation.

      - **roleName** *(string) --*

        Name of the service role in the customer's account used by AWS SMS.

      - **totalServerGroups** *(integer) --*

        Number of server groups present in the application.

      - **totalServers** *(integer) --*

        Number of servers present in the application.

    - **serverGroups** *(list) --*

      List of updated server groups in the application.

      - *(dict) --*

        A logical grouping of servers.

        - **serverGroupId** *(string) --*

          Identifier of a server group.

        - **name** *(string) --*

          Name of a server group.

        - **serverList** *(list) --*

          List of servers belonging to a server group.

          - *(dict) --*

            Represents a server.

            - **serverId** *(string) --*

              The identifier of the server.

            - **serverType** *(string) --*

              The type of server.

            - **vmServer** *(dict) --*

              Information about the VM server.

              - **vmServerAddress** *(dict) --*

                Information about the VM server location.

                - **vmManagerId** *(string) --*

                  The identifier of the VM manager.

                - **vmId** *(string) --*

                  The identifier of the VM.

              - **vmName** *(string) --*

                The name of the VM.

              - **vmManagerName** *(string) --*

                The name of the VM manager.

              - **vmManagerType** *(string) --*

                The type of VM management product.

              - **vmPath** *(string) --*

                The VM folder path in the vCenter Server virtual machine inventory tree.

            - **replicationJobId** *(string) --*

              The identifier of the replication job.

            - **replicationJobTerminated** *(boolean) --*

              Indicates whether the replication job is deleted or failed.

    - **tags** *(list) --*

      List of tags associated with the application.

      - *(dict) --*

        A label that can be assigned to an application.

        - **key** *(string) --*

          Tag key.

        - **value** *(string) --*

          Tag value.
    """


_ClientUpdateAppserverGroupsserverListvmServervmServerAddressTypeDef = TypedDict(
    "_ClientUpdateAppserverGroupsserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class ClientUpdateAppserverGroupsserverListvmServervmServerAddressTypeDef(
    _ClientUpdateAppserverGroupsserverListvmServervmServerAddressTypeDef
):
    """
    Type definition for `ClientUpdateAppserverGroupsserverListvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ClientUpdateAppserverGroupsserverListvmServerTypeDef = TypedDict(
    "_ClientUpdateAppserverGroupsserverListvmServerTypeDef",
    {
        "vmServerAddress": ClientUpdateAppserverGroupsserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class ClientUpdateAppserverGroupsserverListvmServerTypeDef(
    _ClientUpdateAppserverGroupsserverListvmServerTypeDef
):
    """
    Type definition for `ClientUpdateAppserverGroupsserverList` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_ClientUpdateAppserverGroupsserverListTypeDef = TypedDict(
    "_ClientUpdateAppserverGroupsserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": ClientUpdateAppserverGroupsserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class ClientUpdateAppserverGroupsserverListTypeDef(
    _ClientUpdateAppserverGroupsserverListTypeDef
):
    """
    Type definition for `ClientUpdateAppserverGroups` `serverList`

    Represents a server.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_ClientUpdateAppserverGroupsTypeDef = TypedDict(
    "_ClientUpdateAppserverGroupsTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List[ClientUpdateAppserverGroupsserverListTypeDef],
    },
    total=False,
)


class ClientUpdateAppserverGroupsTypeDef(_ClientUpdateAppserverGroupsTypeDef):
    """
    Type definition for `ClientUpdateApp` `serverGroups`

    A logical grouping of servers.

    - **serverGroupId** *(string) --*

      Identifier of a server group.

    - **name** *(string) --*

      Name of a server group.

    - **serverList** *(list) --*

      List of servers belonging to a server group.

      - *(dict) --*

        Represents a server.

        - **serverId** *(string) --*

          The identifier of the server.

        - **serverType** *(string) --*

          The type of server.

        - **vmServer** *(dict) --*

          Information about the VM server.

          - **vmServerAddress** *(dict) --*

            Information about the VM server location.

            - **vmManagerId** *(string) --*

              The identifier of the VM manager.

            - **vmId** *(string) --*

              The identifier of the VM.

          - **vmName** *(string) --*

            The name of the VM.

          - **vmManagerName** *(string) --*

            The name of the VM manager.

          - **vmManagerType** *(string) --*

            The type of VM management product.

          - **vmPath** *(string) --*

            The VM folder path in the vCenter Server virtual machine inventory tree.

        - **replicationJobId** *(string) --*

          The identifier of the replication job.

        - **replicationJobTerminated** *(boolean) --*

          Indicates whether the replication job is deleted or failed.
    """


_ClientUpdateApptagsTypeDef = TypedDict(
    "_ClientUpdateApptagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateApptagsTypeDef(_ClientUpdateApptagsTypeDef):
    """
    Type definition for `ClientUpdateApp` `tags`

    A label that can be assigned to an application.

    - **key** *(string) --*

      Tag key.

    - **value** *(string) --*

      Tag value.
    """


_GetConnectorsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetConnectorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetConnectorsPaginatePaginationConfigTypeDef(
    _GetConnectorsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetConnectorsPaginate` `PaginationConfig`

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


_GetConnectorsPaginateResponseconnectorListTypeDef = TypedDict(
    "_GetConnectorsPaginateResponseconnectorListTypeDef",
    {
        "connectorId": str,
        "version": str,
        "status": str,
        "capabilityList": List[str],
        "vmManagerName": str,
        "vmManagerType": str,
        "vmManagerId": str,
        "ipAddress": str,
        "macAddress": str,
        "associatedOn": datetime,
    },
    total=False,
)


class GetConnectorsPaginateResponseconnectorListTypeDef(
    _GetConnectorsPaginateResponseconnectorListTypeDef
):
    """
    Type definition for `GetConnectorsPaginateResponse` `connectorList`

    Represents a connector.

    - **connectorId** *(string) --*

      The identifier of the connector.

    - **version** *(string) --*

      The connector version.

    - **status** *(string) --*

      The status of the connector.

    - **capabilityList** *(list) --*

      The capabilities of the connector.

      - *(string) --*

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The VM management product.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **ipAddress** *(string) --*

      The IP address of the connector.

    - **macAddress** *(string) --*

      The MAC address of the connector.

    - **associatedOn** *(datetime) --*

      The time the connector was associated.
    """


_GetConnectorsPaginateResponseTypeDef = TypedDict(
    "_GetConnectorsPaginateResponseTypeDef",
    {
        "connectorList": List[GetConnectorsPaginateResponseconnectorListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetConnectorsPaginateResponseTypeDef(_GetConnectorsPaginateResponseTypeDef):
    """
    Type definition for `GetConnectorsPaginate` `Response`

    - **connectorList** *(list) --*

      Information about the registered connectors.

      - *(dict) --*

        Represents a connector.

        - **connectorId** *(string) --*

          The identifier of the connector.

        - **version** *(string) --*

          The connector version.

        - **status** *(string) --*

          The status of the connector.

        - **capabilityList** *(list) --*

          The capabilities of the connector.

          - *(string) --*

        - **vmManagerName** *(string) --*

          The name of the VM manager.

        - **vmManagerType** *(string) --*

          The VM management product.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **ipAddress** *(string) --*

          The IP address of the connector.

        - **macAddress** *(string) --*

          The MAC address of the connector.

        - **associatedOn** *(datetime) --*

          The time the connector was associated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetReplicationJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetReplicationJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetReplicationJobsPaginatePaginationConfigTypeDef(
    _GetReplicationJobsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetReplicationJobsPaginate` `PaginationConfig`

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


_GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef(
    _GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef
):
    """
    Type definition for `GetReplicationJobsPaginateResponsereplicationJobListreplicationRunList` `stageDetails`

    Details of the current stage of the replication run.

    - **stage** *(string) --*

      String describing the current stage of a replication run.

    - **stageProgress** *(string) --*

      String describing the progress of the current stage of a replication run.
    """


_GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": str,
        "type": str,
        "stageDetails": GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef(
    _GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef
):
    """
    Type definition for `GetReplicationJobsPaginateResponsereplicationJobList` `replicationRunList`

    Represents a replication run.

    - **replicationRunId** *(string) --*

      The identifier of the replication run.

    - **state** *(string) --*

      The state of the replication run.

    - **type** *(string) --*

      The type of replication run.

    - **stageDetails** *(dict) --*

      Details of the current stage of the replication run.

      - **stage** *(string) --*

        String describing the current stage of a replication run.

      - **stageProgress** *(string) --*

        String describing the progress of the current stage of a replication run.

    - **statusMessage** *(string) --*

      The description of the current status of the replication job.

    - **amiId** *(string) --*

      The identifier of the Amazon Machine Image (AMI) from the replication run.

    - **scheduledStartTime** *(datetime) --*

      The start time of the next replication run.

    - **completedTime** *(datetime) --*

      The completion time of the last replication run.

    - **description** *(string) --*

      The description of the replication run.

    - **encrypted** *(boolean) --*

      Whether the replication run should produce encrypted AMI or not. See also
      ``KmsKeyId`` below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
      following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
      key for EBS is used.
    """


_GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef(
    _GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef
):
    """
    Type definition for `GetReplicationJobsPaginateResponsereplicationJobListvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef",
    {
        "vmServerAddress": GetReplicationJobsPaginateResponsereplicationJobListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef(
    _GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef
):
    """
    Type definition for `GetReplicationJobsPaginateResponsereplicationJobList` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_GetReplicationJobsPaginateResponsereplicationJobListTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponsereplicationJobListTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": str,
        "vmServer": GetReplicationJobsPaginateResponsereplicationJobListvmServerTypeDef,
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": str,
        "roleName": str,
        "latestAmiId": str,
        "state": str,
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List[
            GetReplicationJobsPaginateResponsereplicationJobListreplicationRunListTypeDef
        ],
    },
    total=False,
)


class GetReplicationJobsPaginateResponsereplicationJobListTypeDef(
    _GetReplicationJobsPaginateResponsereplicationJobListTypeDef
):
    """
    Type definition for `GetReplicationJobsPaginateResponse` `replicationJobList`

    Represents a replication job.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **seedReplicationTime** *(datetime) --*

      The seed replication time.

    - **frequency** *(integer) --*

      The time between consecutive replication runs, in hours.

    - **runOnce** *(boolean) --*

    - **nextReplicationRunStartTime** *(datetime) --*

      The start time of the next replication run.

    - **licenseType** *(string) --*

      The license type to be used for the AMI created by a successful replication run.

    - **roleName** *(string) --*

      The name of the IAM role to be used by the Server Migration Service.

    - **latestAmiId** *(string) --*

      The ID of the latest Amazon Machine Image (AMI).

    - **state** *(string) --*

      The state of the replication job.

    - **statusMessage** *(string) --*

      The description of the current status of the replication job.

    - **description** *(string) --*

      The description of the replication job.

    - **numberOfRecentAmisToKeep** *(integer) --*

      Number of recent AMIs to keep in the customer's account for a replication job. By default
      the value is set to zero, meaning that all AMIs are kept.

    - **encrypted** *(boolean) --*

      Whether the replication job should produce encrypted AMIs or not. See also ``KmsKeyId``
      below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
      for EBS is used.

    - **replicationRunList** *(list) --*

      Information about the replication runs.

      - *(dict) --*

        Represents a replication run.

        - **replicationRunId** *(string) --*

          The identifier of the replication run.

        - **state** *(string) --*

          The state of the replication run.

        - **type** *(string) --*

          The type of replication run.

        - **stageDetails** *(dict) --*

          Details of the current stage of the replication run.

          - **stage** *(string) --*

            String describing the current stage of a replication run.

          - **stageProgress** *(string) --*

            String describing the progress of the current stage of a replication run.

        - **statusMessage** *(string) --*

          The description of the current status of the replication job.

        - **amiId** *(string) --*

          The identifier of the Amazon Machine Image (AMI) from the replication run.

        - **scheduledStartTime** *(datetime) --*

          The start time of the next replication run.

        - **completedTime** *(datetime) --*

          The completion time of the last replication run.

        - **description** *(string) --*

          The description of the replication run.

        - **encrypted** *(boolean) --*

          Whether the replication run should produce encrypted AMI or not. See also
          ``KmsKeyId`` below.

        - **kmsKeyId** *(string) --*

          KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
          following:

          * KMS key ID

          * KMS key alias

          * ARN referring to KMS key ID

          * ARN referring to KMS key alias

          If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
          key for EBS is used.
    """


_GetReplicationJobsPaginateResponseTypeDef = TypedDict(
    "_GetReplicationJobsPaginateResponseTypeDef",
    {
        "replicationJobList": List[
            GetReplicationJobsPaginateResponsereplicationJobListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetReplicationJobsPaginateResponseTypeDef(
    _GetReplicationJobsPaginateResponseTypeDef
):
    """
    Type definition for `GetReplicationJobsPaginate` `Response`

    - **replicationJobList** *(list) --*

      Information about the replication jobs.

      - *(dict) --*

        Represents a replication job.

        - **replicationJobId** *(string) --*

          The identifier of the replication job.

        - **serverId** *(string) --*

          The identifier of the server.

        - **serverType** *(string) --*

          The type of server.

        - **vmServer** *(dict) --*

          Information about the VM server.

          - **vmServerAddress** *(dict) --*

            Information about the VM server location.

            - **vmManagerId** *(string) --*

              The identifier of the VM manager.

            - **vmId** *(string) --*

              The identifier of the VM.

          - **vmName** *(string) --*

            The name of the VM.

          - **vmManagerName** *(string) --*

            The name of the VM manager.

          - **vmManagerType** *(string) --*

            The type of VM management product.

          - **vmPath** *(string) --*

            The VM folder path in the vCenter Server virtual machine inventory tree.

        - **seedReplicationTime** *(datetime) --*

          The seed replication time.

        - **frequency** *(integer) --*

          The time between consecutive replication runs, in hours.

        - **runOnce** *(boolean) --*

        - **nextReplicationRunStartTime** *(datetime) --*

          The start time of the next replication run.

        - **licenseType** *(string) --*

          The license type to be used for the AMI created by a successful replication run.

        - **roleName** *(string) --*

          The name of the IAM role to be used by the Server Migration Service.

        - **latestAmiId** *(string) --*

          The ID of the latest Amazon Machine Image (AMI).

        - **state** *(string) --*

          The state of the replication job.

        - **statusMessage** *(string) --*

          The description of the current status of the replication job.

        - **description** *(string) --*

          The description of the replication job.

        - **numberOfRecentAmisToKeep** *(integer) --*

          Number of recent AMIs to keep in the customer's account for a replication job. By default
          the value is set to zero, meaning that all AMIs are kept.

        - **encrypted** *(boolean) --*

          Whether the replication job should produce encrypted AMIs or not. See also ``KmsKeyId``
          below.

        - **kmsKeyId** *(string) --*

          KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

          * KMS key ID

          * KMS key alias

          * ARN referring to KMS key ID

          * ARN referring to KMS key alias

          If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
          for EBS is used.

        - **replicationRunList** *(list) --*

          Information about the replication runs.

          - *(dict) --*

            Represents a replication run.

            - **replicationRunId** *(string) --*

              The identifier of the replication run.

            - **state** *(string) --*

              The state of the replication run.

            - **type** *(string) --*

              The type of replication run.

            - **stageDetails** *(dict) --*

              Details of the current stage of the replication run.

              - **stage** *(string) --*

                String describing the current stage of a replication run.

              - **stageProgress** *(string) --*

                String describing the progress of the current stage of a replication run.

            - **statusMessage** *(string) --*

              The description of the current status of the replication job.

            - **amiId** *(string) --*

              The identifier of the Amazon Machine Image (AMI) from the replication run.

            - **scheduledStartTime** *(datetime) --*

              The start time of the next replication run.

            - **completedTime** *(datetime) --*

              The completion time of the last replication run.

            - **description** *(string) --*

              The description of the replication run.

            - **encrypted** *(boolean) --*

              Whether the replication run should produce encrypted AMI or not. See also
              ``KmsKeyId`` below.

            - **kmsKeyId** *(string) --*

              KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
              following:

              * KMS key ID

              * KMS key alias

              * ARN referring to KMS key ID

              * ARN referring to KMS key alias

              If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
              key for EBS is used.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetReplicationRunsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetReplicationRunsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetReplicationRunsPaginatePaginationConfigTypeDef(
    _GetReplicationRunsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetReplicationRunsPaginate` `PaginationConfig`

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


_GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef(
    _GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef
):
    """
    Type definition for `GetReplicationRunsPaginateResponsereplicationJobreplicationRunList` `stageDetails`

    Details of the current stage of the replication run.

    - **stage** *(string) --*

      String describing the current stage of a replication run.

    - **stageProgress** *(string) --*

      String describing the progress of the current stage of a replication run.
    """


_GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": str,
        "type": str,
        "stageDetails": GetReplicationRunsPaginateResponsereplicationJobreplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef(
    _GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef
):
    """
    Type definition for `GetReplicationRunsPaginateResponsereplicationJob` `replicationRunList`

    Represents a replication run.

    - **replicationRunId** *(string) --*

      The identifier of the replication run.

    - **state** *(string) --*

      The state of the replication run.

    - **type** *(string) --*

      The type of replication run.

    - **stageDetails** *(dict) --*

      Details of the current stage of the replication run.

      - **stage** *(string) --*

        String describing the current stage of a replication run.

      - **stageProgress** *(string) --*

        String describing the progress of the current stage of a replication run.

    - **statusMessage** *(string) --*

      The description of the current status of the replication job.

    - **amiId** *(string) --*

      The identifier of the Amazon Machine Image (AMI) from the replication run.

    - **scheduledStartTime** *(datetime) --*

      The start time of the next replication run.

    - **completedTime** *(datetime) --*

      The completion time of the last replication run.

    - **description** *(string) --*

      The description of the replication run.

    - **encrypted** *(boolean) --*

      Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId``
      below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
      following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
      key for EBS is used.
    """


_GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef(
    _GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef
):
    """
    Type definition for `GetReplicationRunsPaginateResponsereplicationJobvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef",
    {
        "vmServerAddress": GetReplicationRunsPaginateResponsereplicationJobvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef(
    _GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef
):
    """
    Type definition for `GetReplicationRunsPaginateResponsereplicationJob` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_GetReplicationRunsPaginateResponsereplicationJobTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationJobTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": str,
        "vmServer": GetReplicationRunsPaginateResponsereplicationJobvmServerTypeDef,
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": str,
        "roleName": str,
        "latestAmiId": str,
        "state": str,
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List[
            GetReplicationRunsPaginateResponsereplicationJobreplicationRunListTypeDef
        ],
    },
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationJobTypeDef(
    _GetReplicationRunsPaginateResponsereplicationJobTypeDef
):
    """
    Type definition for `GetReplicationRunsPaginateResponse` `replicationJob`

    Information about the replication job.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **seedReplicationTime** *(datetime) --*

      The seed replication time.

    - **frequency** *(integer) --*

      The time between consecutive replication runs, in hours.

    - **runOnce** *(boolean) --*

    - **nextReplicationRunStartTime** *(datetime) --*

      The start time of the next replication run.

    - **licenseType** *(string) --*

      The license type to be used for the AMI created by a successful replication run.

    - **roleName** *(string) --*

      The name of the IAM role to be used by the Server Migration Service.

    - **latestAmiId** *(string) --*

      The ID of the latest Amazon Machine Image (AMI).

    - **state** *(string) --*

      The state of the replication job.

    - **statusMessage** *(string) --*

      The description of the current status of the replication job.

    - **description** *(string) --*

      The description of the replication job.

    - **numberOfRecentAmisToKeep** *(integer) --*

      Number of recent AMIs to keep in the customer's account for a replication job. By default
      the value is set to zero, meaning that all AMIs are kept.

    - **encrypted** *(boolean) --*

      Whether the replication job should produce encrypted AMIs or not. See also ``KmsKeyId``
      below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
      for EBS is used.

    - **replicationRunList** *(list) --*

      Information about the replication runs.

      - *(dict) --*

        Represents a replication run.

        - **replicationRunId** *(string) --*

          The identifier of the replication run.

        - **state** *(string) --*

          The state of the replication run.

        - **type** *(string) --*

          The type of replication run.

        - **stageDetails** *(dict) --*

          Details of the current stage of the replication run.

          - **stage** *(string) --*

            String describing the current stage of a replication run.

          - **stageProgress** *(string) --*

            String describing the progress of the current stage of a replication run.

        - **statusMessage** *(string) --*

          The description of the current status of the replication job.

        - **amiId** *(string) --*

          The identifier of the Amazon Machine Image (AMI) from the replication run.

        - **scheduledStartTime** *(datetime) --*

          The start time of the next replication run.

        - **completedTime** *(datetime) --*

          The completion time of the last replication run.

        - **description** *(string) --*

          The description of the replication run.

        - **encrypted** *(boolean) --*

          Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId``
          below.

        - **kmsKeyId** *(string) --*

          KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
          following:

          * KMS key ID

          * KMS key alias

          * ARN referring to KMS key ID

          * ARN referring to KMS key alias

          If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
          key for EBS is used.
    """


_GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef",
    {"stage": str, "stageProgress": str},
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef(
    _GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef
):
    """
    Type definition for `GetReplicationRunsPaginateResponsereplicationRunList` `stageDetails`

    Details of the current stage of the replication run.

    - **stage** *(string) --*

      String describing the current stage of a replication run.

    - **stageProgress** *(string) --*

      String describing the progress of the current stage of a replication run.
    """


_GetReplicationRunsPaginateResponsereplicationRunListTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponsereplicationRunListTypeDef",
    {
        "replicationRunId": str,
        "state": str,
        "type": str,
        "stageDetails": GetReplicationRunsPaginateResponsereplicationRunListstageDetailsTypeDef,
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class GetReplicationRunsPaginateResponsereplicationRunListTypeDef(
    _GetReplicationRunsPaginateResponsereplicationRunListTypeDef
):
    """
    Type definition for `GetReplicationRunsPaginateResponse` `replicationRunList`

    Represents a replication run.

    - **replicationRunId** *(string) --*

      The identifier of the replication run.

    - **state** *(string) --*

      The state of the replication run.

    - **type** *(string) --*

      The type of replication run.

    - **stageDetails** *(dict) --*

      Details of the current stage of the replication run.

      - **stage** *(string) --*

        String describing the current stage of a replication run.

      - **stageProgress** *(string) --*

        String describing the progress of the current stage of a replication run.

    - **statusMessage** *(string) --*

      The description of the current status of the replication job.

    - **amiId** *(string) --*

      The identifier of the Amazon Machine Image (AMI) from the replication run.

    - **scheduledStartTime** *(datetime) --*

      The start time of the next replication run.

    - **completedTime** *(datetime) --*

      The completion time of the last replication run.

    - **description** *(string) --*

      The description of the replication run.

    - **encrypted** *(boolean) --*

      Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId``
      below.

    - **kmsKeyId** *(string) --*

      KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

      * KMS key ID

      * KMS key alias

      * ARN referring to KMS key ID

      * ARN referring to KMS key alias

      If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
      for EBS is used.
    """


_GetReplicationRunsPaginateResponseTypeDef = TypedDict(
    "_GetReplicationRunsPaginateResponseTypeDef",
    {
        "replicationJob": GetReplicationRunsPaginateResponsereplicationJobTypeDef,
        "replicationRunList": List[
            GetReplicationRunsPaginateResponsereplicationRunListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetReplicationRunsPaginateResponseTypeDef(
    _GetReplicationRunsPaginateResponseTypeDef
):
    """
    Type definition for `GetReplicationRunsPaginate` `Response`

    - **replicationJob** *(dict) --*

      Information about the replication job.

      - **replicationJobId** *(string) --*

        The identifier of the replication job.

      - **serverId** *(string) --*

        The identifier of the server.

      - **serverType** *(string) --*

        The type of server.

      - **vmServer** *(dict) --*

        Information about the VM server.

        - **vmServerAddress** *(dict) --*

          Information about the VM server location.

          - **vmManagerId** *(string) --*

            The identifier of the VM manager.

          - **vmId** *(string) --*

            The identifier of the VM.

        - **vmName** *(string) --*

          The name of the VM.

        - **vmManagerName** *(string) --*

          The name of the VM manager.

        - **vmManagerType** *(string) --*

          The type of VM management product.

        - **vmPath** *(string) --*

          The VM folder path in the vCenter Server virtual machine inventory tree.

      - **seedReplicationTime** *(datetime) --*

        The seed replication time.

      - **frequency** *(integer) --*

        The time between consecutive replication runs, in hours.

      - **runOnce** *(boolean) --*

      - **nextReplicationRunStartTime** *(datetime) --*

        The start time of the next replication run.

      - **licenseType** *(string) --*

        The license type to be used for the AMI created by a successful replication run.

      - **roleName** *(string) --*

        The name of the IAM role to be used by the Server Migration Service.

      - **latestAmiId** *(string) --*

        The ID of the latest Amazon Machine Image (AMI).

      - **state** *(string) --*

        The state of the replication job.

      - **statusMessage** *(string) --*

        The description of the current status of the replication job.

      - **description** *(string) --*

        The description of the replication job.

      - **numberOfRecentAmisToKeep** *(integer) --*

        Number of recent AMIs to keep in the customer's account for a replication job. By default
        the value is set to zero, meaning that all AMIs are kept.

      - **encrypted** *(boolean) --*

        Whether the replication job should produce encrypted AMIs or not. See also ``KmsKeyId``
        below.

      - **kmsKeyId** *(string) --*

        KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

        * KMS key ID

        * KMS key alias

        * ARN referring to KMS key ID

        * ARN referring to KMS key alias

        If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
        for EBS is used.

      - **replicationRunList** *(list) --*

        Information about the replication runs.

        - *(dict) --*

          Represents a replication run.

          - **replicationRunId** *(string) --*

            The identifier of the replication run.

          - **state** *(string) --*

            The state of the replication run.

          - **type** *(string) --*

            The type of replication run.

          - **stageDetails** *(dict) --*

            Details of the current stage of the replication run.

            - **stage** *(string) --*

              String describing the current stage of a replication run.

            - **stageProgress** *(string) --*

              String describing the progress of the current stage of a replication run.

          - **statusMessage** *(string) --*

            The description of the current status of the replication job.

          - **amiId** *(string) --*

            The identifier of the Amazon Machine Image (AMI) from the replication run.

          - **scheduledStartTime** *(datetime) --*

            The start time of the next replication run.

          - **completedTime** *(datetime) --*

            The completion time of the last replication run.

          - **description** *(string) --*

            The description of the replication run.

          - **encrypted** *(boolean) --*

            Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId``
            below.

          - **kmsKeyId** *(string) --*

            KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the
            following:

            * KMS key ID

            * KMS key alias

            * ARN referring to KMS key ID

            * ARN referring to KMS key alias

            If encrypted is *true* but a KMS key id is not specified, the customer's default KMS
            key for EBS is used.

    - **replicationRunList** *(list) --*

      Information about the replication runs.

      - *(dict) --*

        Represents a replication run.

        - **replicationRunId** *(string) --*

          The identifier of the replication run.

        - **state** *(string) --*

          The state of the replication run.

        - **type** *(string) --*

          The type of replication run.

        - **stageDetails** *(dict) --*

          Details of the current stage of the replication run.

          - **stage** *(string) --*

            String describing the current stage of a replication run.

          - **stageProgress** *(string) --*

            String describing the progress of the current stage of a replication run.

        - **statusMessage** *(string) --*

          The description of the current status of the replication job.

        - **amiId** *(string) --*

          The identifier of the Amazon Machine Image (AMI) from the replication run.

        - **scheduledStartTime** *(datetime) --*

          The start time of the next replication run.

        - **completedTime** *(datetime) --*

          The completion time of the last replication run.

        - **description** *(string) --*

          The description of the replication run.

        - **encrypted** *(boolean) --*

          Whether the replication run should produce encrypted AMI or not. See also ``KmsKeyId``
          below.

        - **kmsKeyId** *(string) --*

          KMS key ID for replication jobs that produce encrypted AMIs. Can be any of the following:

          * KMS key ID

          * KMS key alias

          * ARN referring to KMS key ID

          * ARN referring to KMS key alias

          If encrypted is *true* but a KMS key id is not specified, the customer's default KMS key
          for EBS is used.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetServersPaginatePaginationConfigTypeDef = TypedDict(
    "_GetServersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetServersPaginatePaginationConfigTypeDef(
    _GetServersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetServersPaginate` `PaginationConfig`

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


_GetServersPaginateResponseserverListvmServervmServerAddressTypeDef = TypedDict(
    "_GetServersPaginateResponseserverListvmServervmServerAddressTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class GetServersPaginateResponseserverListvmServervmServerAddressTypeDef(
    _GetServersPaginateResponseserverListvmServervmServerAddressTypeDef
):
    """
    Type definition for `GetServersPaginateResponseserverListvmServer` `vmServerAddress`

    Information about the VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_GetServersPaginateResponseserverListvmServerTypeDef = TypedDict(
    "_GetServersPaginateResponseserverListvmServerTypeDef",
    {
        "vmServerAddress": GetServersPaginateResponseserverListvmServervmServerAddressTypeDef,
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": str,
        "vmPath": str,
    },
    total=False,
)


class GetServersPaginateResponseserverListvmServerTypeDef(
    _GetServersPaginateResponseserverListvmServerTypeDef
):
    """
    Type definition for `GetServersPaginateResponseserverList` `vmServer`

    Information about the VM server.

    - **vmServerAddress** *(dict) --*

      Information about the VM server location.

      - **vmManagerId** *(string) --*

        The identifier of the VM manager.

      - **vmId** *(string) --*

        The identifier of the VM.

    - **vmName** *(string) --*

      The name of the VM.

    - **vmManagerName** *(string) --*

      The name of the VM manager.

    - **vmManagerType** *(string) --*

      The type of VM management product.

    - **vmPath** *(string) --*

      The VM folder path in the vCenter Server virtual machine inventory tree.
    """


_GetServersPaginateResponseserverListTypeDef = TypedDict(
    "_GetServersPaginateResponseserverListTypeDef",
    {
        "serverId": str,
        "serverType": str,
        "vmServer": GetServersPaginateResponseserverListvmServerTypeDef,
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)


class GetServersPaginateResponseserverListTypeDef(
    _GetServersPaginateResponseserverListTypeDef
):
    """
    Type definition for `GetServersPaginateResponse` `serverList`

    Represents a server.

    - **serverId** *(string) --*

      The identifier of the server.

    - **serverType** *(string) --*

      The type of server.

    - **vmServer** *(dict) --*

      Information about the VM server.

      - **vmServerAddress** *(dict) --*

        Information about the VM server location.

        - **vmManagerId** *(string) --*

          The identifier of the VM manager.

        - **vmId** *(string) --*

          The identifier of the VM.

      - **vmName** *(string) --*

        The name of the VM.

      - **vmManagerName** *(string) --*

        The name of the VM manager.

      - **vmManagerType** *(string) --*

        The type of VM management product.

      - **vmPath** *(string) --*

        The VM folder path in the vCenter Server virtual machine inventory tree.

    - **replicationJobId** *(string) --*

      The identifier of the replication job.

    - **replicationJobTerminated** *(boolean) --*

      Indicates whether the replication job is deleted or failed.
    """


_GetServersPaginateResponseTypeDef = TypedDict(
    "_GetServersPaginateResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": str,
        "serverList": List[GetServersPaginateResponseserverListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetServersPaginateResponseTypeDef(_GetServersPaginateResponseTypeDef):
    """
    Type definition for `GetServersPaginate` `Response`

    - **lastModifiedOn** *(datetime) --*

      The time when the server was last modified.

    - **serverCatalogStatus** *(string) --*

      The status of the server catalog.

    - **serverList** *(list) --*

      Information about the servers.

      - *(dict) --*

        Represents a server.

        - **serverId** *(string) --*

          The identifier of the server.

        - **serverType** *(string) --*

          The type of server.

        - **vmServer** *(dict) --*

          Information about the VM server.

          - **vmServerAddress** *(dict) --*

            Information about the VM server location.

            - **vmManagerId** *(string) --*

              The identifier of the VM manager.

            - **vmId** *(string) --*

              The identifier of the VM.

          - **vmName** *(string) --*

            The name of the VM.

          - **vmManagerName** *(string) --*

            The name of the VM manager.

          - **vmManagerType** *(string) --*

            The type of VM management product.

          - **vmPath** *(string) --*

            The VM folder path in the vCenter Server virtual machine inventory tree.

        - **replicationJobId** *(string) --*

          The identifier of the replication job.

        - **replicationJobTerminated** *(boolean) --*

          Indicates whether the replication job is deleted or failed.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetServersPaginatevmServerAddressListTypeDef = TypedDict(
    "_GetServersPaginatevmServerAddressListTypeDef",
    {"vmManagerId": str, "vmId": str},
    total=False,
)


class GetServersPaginatevmServerAddressListTypeDef(
    _GetServersPaginatevmServerAddressListTypeDef
):
    """
    Type definition for `GetServersPaginate` `vmServerAddressList`

    Represents a VM server location.

    - **vmManagerId** *(string) --*

      The identifier of the VM manager.

    - **vmId** *(string) --*

      The identifier of the VM.
    """


_ListAppsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAppsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAppsPaginatePaginationConfigTypeDef(_ListAppsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListAppsPaginate` `PaginationConfig`

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


_ListAppsPaginateResponseappslaunchDetailsTypeDef = TypedDict(
    "_ListAppsPaginateResponseappslaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)


class ListAppsPaginateResponseappslaunchDetailsTypeDef(
    _ListAppsPaginateResponseappslaunchDetailsTypeDef
):
    """
    Type definition for `ListAppsPaginateResponseapps` `launchDetails`

    Details about the latest launch of the application.

    - **latestLaunchTime** *(datetime) --*

      Latest time this application was launched successfully.

    - **stackName** *(string) --*

      Name of the latest stack launched for this application.

    - **stackId** *(string) --*

      Identifier of the latest stack launched for this application.
    """


_ListAppsPaginateResponseappsTypeDef = TypedDict(
    "_ListAppsPaginateResponseappsTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "status": str,
        "statusMessage": str,
        "replicationStatus": str,
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchStatus": str,
        "launchStatusMessage": str,
        "launchDetails": ListAppsPaginateResponseappslaunchDetailsTypeDef,
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)


class ListAppsPaginateResponseappsTypeDef(_ListAppsPaginateResponseappsTypeDef):
    """
    Type definition for `ListAppsPaginateResponse` `apps`

    Information about the application.

    - **appId** *(string) --*

      Unique ID of the application.

    - **name** *(string) --*

      Name of the application.

    - **description** *(string) --*

      Description of the application.

    - **status** *(string) --*

      Status of the application.

    - **statusMessage** *(string) --*

      A message related to the status of the application

    - **replicationStatus** *(string) --*

      Replication status of the application.

    - **replicationStatusMessage** *(string) --*

      A message related to the replication status of the application.

    - **latestReplicationTime** *(datetime) --*

      Timestamp of the application's most recent successful replication.

    - **launchStatus** *(string) --*

      Launch status of the application.

    - **launchStatusMessage** *(string) --*

      A message related to the launch status of the application.

    - **launchDetails** *(dict) --*

      Details about the latest launch of the application.

      - **latestLaunchTime** *(datetime) --*

        Latest time this application was launched successfully.

      - **stackName** *(string) --*

        Name of the latest stack launched for this application.

      - **stackId** *(string) --*

        Identifier of the latest stack launched for this application.

    - **creationTime** *(datetime) --*

      Time of creation of this application.

    - **lastModified** *(datetime) --*

      Timestamp of the application's creation.

    - **roleName** *(string) --*

      Name of the service role in the customer's account used by AWS SMS.

    - **totalServerGroups** *(integer) --*

      Number of server groups present in the application.

    - **totalServers** *(integer) --*

      Number of servers present in the application.
    """


_ListAppsPaginateResponseTypeDef = TypedDict(
    "_ListAppsPaginateResponseTypeDef",
    {"apps": List[ListAppsPaginateResponseappsTypeDef], "NextToken": str},
    total=False,
)


class ListAppsPaginateResponseTypeDef(_ListAppsPaginateResponseTypeDef):
    """
    Type definition for `ListAppsPaginate` `Response`

    - **apps** *(list) --*

      A list of application summaries.

      - *(dict) --*

        Information about the application.

        - **appId** *(string) --*

          Unique ID of the application.

        - **name** *(string) --*

          Name of the application.

        - **description** *(string) --*

          Description of the application.

        - **status** *(string) --*

          Status of the application.

        - **statusMessage** *(string) --*

          A message related to the status of the application

        - **replicationStatus** *(string) --*

          Replication status of the application.

        - **replicationStatusMessage** *(string) --*

          A message related to the replication status of the application.

        - **latestReplicationTime** *(datetime) --*

          Timestamp of the application's most recent successful replication.

        - **launchStatus** *(string) --*

          Launch status of the application.

        - **launchStatusMessage** *(string) --*

          A message related to the launch status of the application.

        - **launchDetails** *(dict) --*

          Details about the latest launch of the application.

          - **latestLaunchTime** *(datetime) --*

            Latest time this application was launched successfully.

          - **stackName** *(string) --*

            Name of the latest stack launched for this application.

          - **stackId** *(string) --*

            Identifier of the latest stack launched for this application.

        - **creationTime** *(datetime) --*

          Time of creation of this application.

        - **lastModified** *(datetime) --*

          Timestamp of the application's creation.

        - **roleName** *(string) --*

          Name of the service role in the customer's account used by AWS SMS.

        - **totalServerGroups** *(integer) --*

          Number of server groups present in the application.

        - **totalServers** *(integer) --*

          Number of servers present in the application.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
