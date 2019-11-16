"Main interface for greengrass type defs"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAssociateRoleToGroupResponseTypeDef",
    "ClientAssociateServiceRoleToAccountResponseTypeDef",
    "ClientCreateConnectorDefinitionInitialVersionTypeDef",
    "ClientCreateConnectorDefinitionResponseTypeDef",
    "ClientCreateConnectorDefinitionVersionResponseTypeDef",
    "ClientCreateCoreDefinitionInitialVersionCoresTypeDef",
    "ClientCreateCoreDefinitionInitialVersionTypeDef",
    "ClientCreateCoreDefinitionResponseTypeDef",
    "ClientCreateCoreDefinitionVersionCoresTypeDef",
    "ClientCreateCoreDefinitionVersionResponseTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDeviceDefinitionInitialVersionDevicesTypeDef",
    "ClientCreateDeviceDefinitionInitialVersionTypeDef",
    "ClientCreateDeviceDefinitionResponseTypeDef",
    "ClientCreateDeviceDefinitionVersionDevicesTypeDef",
    "ClientCreateDeviceDefinitionVersionResponseTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionTypeDef",
    "ClientCreateFunctionDefinitionResponseTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsTypeDef",
    "ClientCreateFunctionDefinitionVersionResponseTypeDef",
    "ClientCreateGroupCertificateAuthorityResponseTypeDef",
    "ClientCreateGroupInitialVersionTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateGroupVersionResponseTypeDef",
    "ClientCreateLoggerDefinitionInitialVersionLoggersTypeDef",
    "ClientCreateLoggerDefinitionInitialVersionTypeDef",
    "ClientCreateLoggerDefinitionResponseTypeDef",
    "ClientCreateLoggerDefinitionVersionLoggersTypeDef",
    "ClientCreateLoggerDefinitionVersionResponseTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesTypeDef",
    "ClientCreateResourceDefinitionInitialVersionTypeDef",
    "ClientCreateResourceDefinitionResponseTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesTypeDef",
    "ClientCreateResourceDefinitionVersionResponseTypeDef",
    "ClientCreateSoftwareUpdateJobResponseTypeDef",
    "ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef",
    "ClientCreateSubscriptionDefinitionInitialVersionTypeDef",
    "ClientCreateSubscriptionDefinitionResponseTypeDef",
    "ClientCreateSubscriptionDefinitionVersionResponseTypeDef",
    "ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef",
    "ClientDisassociateRoleFromGroupResponseTypeDef",
    "ClientDisassociateServiceRoleFromAccountResponseTypeDef",
    "ClientGetAssociatedRoleResponseTypeDef",
    "ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef",
    "ClientGetBulkDeploymentStatusResponseTypeDef",
    "ClientGetConnectivityInfoResponseConnectivityInfoTypeDef",
    "ClientGetConnectivityInfoResponseTypeDef",
    "ClientGetConnectorDefinitionResponseTypeDef",
    "ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetConnectorDefinitionVersionResponseTypeDef",
    "ClientGetCoreDefinitionResponseTypeDef",
    "ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef",
    "ClientGetCoreDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetCoreDefinitionVersionResponseTypeDef",
    "ClientGetDeploymentStatusResponseErrorDetailsTypeDef",
    "ClientGetDeploymentStatusResponseTypeDef",
    "ClientGetDeviceDefinitionResponseTypeDef",
    "ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef",
    "ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetDeviceDefinitionVersionResponseTypeDef",
    "ClientGetFunctionDefinitionResponseTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetFunctionDefinitionVersionResponseTypeDef",
    "ClientGetGroupCertificateAuthorityResponseTypeDef",
    "ClientGetGroupCertificateConfigurationResponseTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetGroupVersionResponseDefinitionTypeDef",
    "ClientGetGroupVersionResponseTypeDef",
    "ClientGetLoggerDefinitionResponseTypeDef",
    "ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef",
    "ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetLoggerDefinitionVersionResponseTypeDef",
    "ClientGetResourceDefinitionResponseTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetResourceDefinitionVersionResponseTypeDef",
    "ClientGetServiceRoleForAccountResponseTypeDef",
    "ClientGetSubscriptionDefinitionResponseTypeDef",
    "ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef",
    "ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetSubscriptionDefinitionVersionResponseTypeDef",
    "ClientListBulkDeploymentDetailedReportsResponseTypeDef",
    "ClientListBulkDeploymentsResponseTypeDef",
    "ClientListConnectorDefinitionVersionsResponseVersionsTypeDef",
    "ClientListConnectorDefinitionVersionsResponseTypeDef",
    "ClientListConnectorDefinitionsResponseDefinitionsTypeDef",
    "ClientListConnectorDefinitionsResponseTypeDef",
    "ClientListCoreDefinitionVersionsResponseVersionsTypeDef",
    "ClientListCoreDefinitionVersionsResponseTypeDef",
    "ClientListCoreDefinitionsResponseDefinitionsTypeDef",
    "ClientListCoreDefinitionsResponseTypeDef",
    "ClientListDeploymentsResponseDeploymentsTypeDef",
    "ClientListDeploymentsResponseTypeDef",
    "ClientListDeviceDefinitionVersionsResponseVersionsTypeDef",
    "ClientListDeviceDefinitionVersionsResponseTypeDef",
    "ClientListDeviceDefinitionsResponseDefinitionsTypeDef",
    "ClientListDeviceDefinitionsResponseTypeDef",
    "ClientListFunctionDefinitionVersionsResponseVersionsTypeDef",
    "ClientListFunctionDefinitionVersionsResponseTypeDef",
    "ClientListGroupCertificateAuthoritiesResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListLoggerDefinitionVersionsResponseVersionsTypeDef",
    "ClientListLoggerDefinitionVersionsResponseTypeDef",
    "ClientListLoggerDefinitionsResponseDefinitionsTypeDef",
    "ClientListLoggerDefinitionsResponseTypeDef",
    "ClientListResourceDefinitionVersionsResponseVersionsTypeDef",
    "ClientListResourceDefinitionVersionsResponseTypeDef",
    "ClientListResourceDefinitionsResponseDefinitionsTypeDef",
    "ClientListResourceDefinitionsResponseTypeDef",
    "ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef",
    "ClientListSubscriptionDefinitionVersionsResponseTypeDef",
    "ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef",
    "ClientListSubscriptionDefinitionsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientResetDeploymentsResponseTypeDef",
    "ClientStartBulkDeploymentResponseTypeDef",
    "ClientUpdateConnectivityInfoConnectivityInfoTypeDef",
    "ClientUpdateConnectivityInfoResponseTypeDef",
    "ClientUpdateGroupCertificateConfigurationResponseTypeDef",
    "ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef",
    "ListBulkDeploymentDetailedReportsPaginateResponseTypeDef",
    "ListBulkDeploymentsPaginatePaginationConfigTypeDef",
    "ListBulkDeploymentsPaginateResponseTypeDef",
    "ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListConnectorDefinitionVersionsPaginateResponseTypeDef",
    "ListConnectorDefinitionsPaginatePaginationConfigTypeDef",
    "ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListConnectorDefinitionsPaginateResponseTypeDef",
    "ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListCoreDefinitionVersionsPaginateResponseTypeDef",
    "ListCoreDefinitionsPaginatePaginationConfigTypeDef",
    "ListCoreDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListCoreDefinitionsPaginateResponseTypeDef",
    "ListDeploymentsPaginatePaginationConfigTypeDef",
    "ListDeploymentsPaginateResponseDeploymentsTypeDef",
    "ListDeploymentsPaginateResponseTypeDef",
    "ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListDeviceDefinitionVersionsPaginateResponseTypeDef",
    "ListDeviceDefinitionsPaginatePaginationConfigTypeDef",
    "ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListDeviceDefinitionsPaginateResponseTypeDef",
    "ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListFunctionDefinitionVersionsPaginateResponseTypeDef",
    "ListFunctionDefinitionsPaginatePaginationConfigTypeDef",
    "ListGroupVersionsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginateResponseGroupsTypeDef",
    "ListGroupsPaginateResponseTypeDef",
    "ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListLoggerDefinitionVersionsPaginateResponseTypeDef",
    "ListLoggerDefinitionsPaginatePaginationConfigTypeDef",
    "ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListLoggerDefinitionsPaginateResponseTypeDef",
    "ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListResourceDefinitionVersionsPaginateResponseTypeDef",
    "ListResourceDefinitionsPaginatePaginationConfigTypeDef",
    "ListResourceDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListResourceDefinitionsPaginateResponseTypeDef",
    "ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListSubscriptionDefinitionVersionsPaginateResponseTypeDef",
    "ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef",
    "ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListSubscriptionDefinitionsPaginateResponseTypeDef",
)


_ClientAssociateRoleToGroupResponseTypeDef = TypedDict(
    "_ClientAssociateRoleToGroupResponseTypeDef", {"AssociatedAt": str}, total=False
)


class ClientAssociateRoleToGroupResponseTypeDef(
    _ClientAssociateRoleToGroupResponseTypeDef
):
    """
    Type definition for `ClientAssociateRoleToGroup` `Response`

    - **AssociatedAt** *(string) --* The time, in milliseconds since the epoch, when the role ARN
    was associated with the group.
    """


_ClientAssociateServiceRoleToAccountResponseTypeDef = TypedDict(
    "_ClientAssociateServiceRoleToAccountResponseTypeDef",
    {"AssociatedAt": str},
    total=False,
)


class ClientAssociateServiceRoleToAccountResponseTypeDef(
    _ClientAssociateServiceRoleToAccountResponseTypeDef
):
    """
    Type definition for `ClientAssociateServiceRoleToAccount` `Response`

    - **AssociatedAt** *(string) --* The time when the service role was associated with the account.
    """


_ClientCreateConnectorDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateConnectorDefinitionInitialVersionTypeDef",
    {"Connectors": List[Any]},
    total=False,
)


class ClientCreateConnectorDefinitionInitialVersionTypeDef(
    _ClientCreateConnectorDefinitionInitialVersionTypeDef
):
    """
    Type definition for `ClientCreateConnectorDefinition` `InitialVersion`

    - **Connectors** *(list) --* A list of references to connectors in this version, with their
    corresponding configuration settings.

      - *(dict) --* Information about a connector. Connectors run on the Greengrass core and contain
      built-in integration with local infrastructure, device protocols, AWS, and other cloud services.

        - **ConnectorArn** *(string) --* **[REQUIRED]** The ARN of the connector.

        - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the connector. This
        value must be unique within the connector definition version. Max length is 128 characters
        with pattern [a-zA-Z0-9:_-]+.

        - **Parameters** *(dict) --* The parameters or configuration that the connector uses.

          - *(string) --*

            - *(string) --*
    """


_ClientCreateConnectorDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateConnectorDefinitionResponseTypeDef(
    _ClientCreateConnectorDefinitionResponseTypeDef
):
    """
    Type definition for `ClientCreateConnectorDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.
    """


_ClientCreateConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateConnectorDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateConnectorDefinitionVersionResponseTypeDef(
    _ClientCreateConnectorDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateConnectorDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the version.

    - **Version** *(string) --* The unique ID of the version.
    """


_RequiredClientCreateCoreDefinitionInitialVersionCoresTypeDef = TypedDict(
    "_RequiredClientCreateCoreDefinitionInitialVersionCoresTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateCoreDefinitionInitialVersionCoresTypeDef = TypedDict(
    "_OptionalClientCreateCoreDefinitionInitialVersionCoresTypeDef",
    {"SyncShadow": bool},
    total=False,
)


class ClientCreateCoreDefinitionInitialVersionCoresTypeDef(
    _RequiredClientCreateCoreDefinitionInitialVersionCoresTypeDef,
    _OptionalClientCreateCoreDefinitionInitialVersionCoresTypeDef,
):
    """
    Type definition for `ClientCreateCoreDefinitionInitialVersion` `Cores`

    - **CertificateArn** *(string) --* **[REQUIRED]** The ARN of the certificate associated with
    the core.

    - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the core. This value
    must be unique within the core definition version. Max length is 128 characters with pattern
    ''[a-zA-Z0-9:_-]+''.

    - **SyncShadow** *(boolean) --* If true, the core's local shadow is automatically synced with
    the cloud.

    - **ThingArn** *(string) --* **[REQUIRED]** The ARN of the thing which is the core.
    """


_ClientCreateCoreDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateCoreDefinitionInitialVersionTypeDef",
    {"Cores": List[ClientCreateCoreDefinitionInitialVersionCoresTypeDef]},
    total=False,
)


class ClientCreateCoreDefinitionInitialVersionTypeDef(
    _ClientCreateCoreDefinitionInitialVersionTypeDef
):
    """
    Type definition for `ClientCreateCoreDefinition` `InitialVersion`

    - **Cores** *(list) --* A list of cores in the core definition version.

      - *(dict) --* Information about a core.

        - **CertificateArn** *(string) --* **[REQUIRED]** The ARN of the certificate associated with
        the core.

        - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the core. This value
        must be unique within the core definition version. Max length is 128 characters with pattern
        ''[a-zA-Z0-9:_-]+''.

        - **SyncShadow** *(boolean) --* If true, the core's local shadow is automatically synced with
        the cloud.

        - **ThingArn** *(string) --* **[REQUIRED]** The ARN of the thing which is the core.
    """


_ClientCreateCoreDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateCoreDefinitionResponseTypeDef(
    _ClientCreateCoreDefinitionResponseTypeDef
):
    """
    Type definition for `ClientCreateCoreDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.
    """


_RequiredClientCreateCoreDefinitionVersionCoresTypeDef = TypedDict(
    "_RequiredClientCreateCoreDefinitionVersionCoresTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateCoreDefinitionVersionCoresTypeDef = TypedDict(
    "_OptionalClientCreateCoreDefinitionVersionCoresTypeDef",
    {"SyncShadow": bool},
    total=False,
)


class ClientCreateCoreDefinitionVersionCoresTypeDef(
    _RequiredClientCreateCoreDefinitionVersionCoresTypeDef,
    _OptionalClientCreateCoreDefinitionVersionCoresTypeDef,
):
    """
    Type definition for `ClientCreateCoreDefinitionVersion` `Cores`

    - **CertificateArn** *(string) --* **[REQUIRED]** The ARN of the certificate associated with
    the core.

    - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the core. This value
    must be unique within the core definition version. Max length is 128 characters with pattern
    ''[a-zA-Z0-9:_-]+''.

    - **SyncShadow** *(boolean) --* If true, the core's local shadow is automatically synced with
    the cloud.

    - **ThingArn** *(string) --* **[REQUIRED]** The ARN of the thing which is the core.
    """


_ClientCreateCoreDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateCoreDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateCoreDefinitionVersionResponseTypeDef(
    _ClientCreateCoreDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateCoreDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the version.

    - **Version** *(string) --* The unique ID of the version.
    """


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef",
    {"DeploymentArn": str, "DeploymentId": str},
    total=False,
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    Type definition for `ClientCreateDeployment` `Response`

    - **DeploymentArn** *(string) --* The ARN of the deployment.

    - **DeploymentId** *(string) --* The ID of the deployment.
    """


_RequiredClientCreateDeviceDefinitionInitialVersionDevicesTypeDef = TypedDict(
    "_RequiredClientCreateDeviceDefinitionInitialVersionDevicesTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateDeviceDefinitionInitialVersionDevicesTypeDef = TypedDict(
    "_OptionalClientCreateDeviceDefinitionInitialVersionDevicesTypeDef",
    {"SyncShadow": bool},
    total=False,
)


class ClientCreateDeviceDefinitionInitialVersionDevicesTypeDef(
    _RequiredClientCreateDeviceDefinitionInitialVersionDevicesTypeDef,
    _OptionalClientCreateDeviceDefinitionInitialVersionDevicesTypeDef,
):
    """
    Type definition for `ClientCreateDeviceDefinitionInitialVersion` `Devices`

    - **CertificateArn** *(string) --* **[REQUIRED]** The ARN of the certificate associated with
    the device.

    - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the device. This
    value must be unique within the device definition version. Max length is 128 characters with
    pattern ''[a-zA-Z0-9:_-]+''.

    - **SyncShadow** *(boolean) --* If true, the device's local shadow will be automatically
    synced with the cloud.

    - **ThingArn** *(string) --* **[REQUIRED]** The thing ARN of the device.
    """


_ClientCreateDeviceDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateDeviceDefinitionInitialVersionTypeDef",
    {"Devices": List[ClientCreateDeviceDefinitionInitialVersionDevicesTypeDef]},
    total=False,
)


class ClientCreateDeviceDefinitionInitialVersionTypeDef(
    _ClientCreateDeviceDefinitionInitialVersionTypeDef
):
    """
    Type definition for `ClientCreateDeviceDefinition` `InitialVersion`

    - **Devices** *(list) --* A list of devices in the definition version.

      - *(dict) --* Information about a device.

        - **CertificateArn** *(string) --* **[REQUIRED]** The ARN of the certificate associated with
        the device.

        - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the device. This
        value must be unique within the device definition version. Max length is 128 characters with
        pattern ''[a-zA-Z0-9:_-]+''.

        - **SyncShadow** *(boolean) --* If true, the device's local shadow will be automatically
        synced with the cloud.

        - **ThingArn** *(string) --* **[REQUIRED]** The thing ARN of the device.
    """


_ClientCreateDeviceDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateDeviceDefinitionResponseTypeDef(
    _ClientCreateDeviceDefinitionResponseTypeDef
):
    """
    Type definition for `ClientCreateDeviceDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.
    """


_RequiredClientCreateDeviceDefinitionVersionDevicesTypeDef = TypedDict(
    "_RequiredClientCreateDeviceDefinitionVersionDevicesTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateDeviceDefinitionVersionDevicesTypeDef = TypedDict(
    "_OptionalClientCreateDeviceDefinitionVersionDevicesTypeDef",
    {"SyncShadow": bool},
    total=False,
)


class ClientCreateDeviceDefinitionVersionDevicesTypeDef(
    _RequiredClientCreateDeviceDefinitionVersionDevicesTypeDef,
    _OptionalClientCreateDeviceDefinitionVersionDevicesTypeDef,
):
    """
    Type definition for `ClientCreateDeviceDefinitionVersion` `Devices`

    - **CertificateArn** *(string) --* **[REQUIRED]** The ARN of the certificate associated with
    the device.

    - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the device. This value
    must be unique within the device definition version. Max length is 128 characters with pattern
    ''[a-zA-Z0-9:_-]+''.

    - **SyncShadow** *(boolean) --* If true, the device's local shadow will be automatically synced
    with the cloud.

    - **ThingArn** *(string) --* **[REQUIRED]** The thing ARN of the device.
    """


_ClientCreateDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateDeviceDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateDeviceDefinitionVersionResponseTypeDef(
    _ClientCreateDeviceDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateDeviceDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the version.

    - **Version** *(string) --* The unique ID of the version.
    """


_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {"IsolationMode": str, "RunAs": Dict[str, Any]},
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef
):
    """
    Type definition for `ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironment` `Execution`

    - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
    Greengrass container (default) or without containerization. Unless your scenario
    requires that you run without containerization, we recommend that you run in a
    Greengrass container. Omit this value to run the Lambda function with the default
    containerization for the group.

    - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
    running the Lambda function. You can specify one or both values to override the default
    values. We recommend that you avoid running as root unless absolutely necessary to
    minimize the risk of unintended changes or malicious attacks. To run as root, you must
    set ''IsolationMode'' to ''NoContainer'' and update config.json in
    ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

      - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
      function.

      - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
      function.
    """


_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef,
        "ResourceAccessPolicies": List[Any],
        "Variables": Dict[str, str],
    },
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef
):
    """
    Type definition for `ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfiguration` `Environment`

    - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the
    host's /sys folder. Use this when the Lambda function needs to read device information
    from /sys. This setting applies only when you run the Lambda function in a Greengrass
    container.

    - **Execution** *(dict) --* Configuration related to executing the Lambda function

      - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
      Greengrass container (default) or without containerization. Unless your scenario
      requires that you run without containerization, we recommend that you run in a
      Greengrass container. Omit this value to run the Lambda function with the default
      containerization for the group.

      - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
      running the Lambda function. You can specify one or both values to override the default
      values. We recommend that you avoid running as root unless absolutely necessary to
      minimize the risk of unintended changes or malicious attacks. To run as root, you must
      set ''IsolationMode'' to ''NoContainer'' and update config.json in
      ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

        - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
        function.

        - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
        function.

    - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions,
    to which the Lambda function will be granted access. A Lambda function can have at most
    10 resources. ResourceAccessPolicies apply only when you run the Lambda function in a
    Greengrass container.

      - *(dict) --* A policy used by the function to access a resource.

        - **Permission** *(string) --* The permissions that the Lambda function has to the
        resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

        - **ResourceId** *(string) --* **[REQUIRED]** The ID of the resource. (This ID is
        assigned to the resource when you create the resource definiton.)

    - **Variables** *(dict) --* Environment variables for the Lambda function's configuration.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef",
    {
        "EncodingType": str,
        "Environment": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef,
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFunctionDefinitionInitialVersionFunctions` `FunctionConfiguration`

    - **EncodingType** *(string) --* The expected encoding type of the input payload for the
    function. The default is ''json''.

    - **Environment** *(dict) --* The environment configuration of the function.

      - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the
      host's /sys folder. Use this when the Lambda function needs to read device information
      from /sys. This setting applies only when you run the Lambda function in a Greengrass
      container.

      - **Execution** *(dict) --* Configuration related to executing the Lambda function

        - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
        Greengrass container (default) or without containerization. Unless your scenario
        requires that you run without containerization, we recommend that you run in a
        Greengrass container. Omit this value to run the Lambda function with the default
        containerization for the group.

        - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
        running the Lambda function. You can specify one or both values to override the default
        values. We recommend that you avoid running as root unless absolutely necessary to
        minimize the risk of unintended changes or malicious attacks. To run as root, you must
        set ''IsolationMode'' to ''NoContainer'' and update config.json in
        ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

          - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
          function.

          - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
          function.

      - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions,
      to which the Lambda function will be granted access. A Lambda function can have at most
      10 resources. ResourceAccessPolicies apply only when you run the Lambda function in a
      Greengrass container.

        - *(dict) --* A policy used by the function to access a resource.

          - **Permission** *(string) --* The permissions that the Lambda function has to the
          resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

          - **ResourceId** *(string) --* **[REQUIRED]** The ID of the resource. (This ID is
          assigned to the resource when you create the resource definiton.)

      - **Variables** *(dict) --* Environment variables for the Lambda function's configuration.

        - *(string) --*

          - *(string) --*

    - **ExecArgs** *(string) --* The execution arguments.

    - **Executable** *(string) --* The name of the function executable.

    - **MemorySize** *(integer) --* The memory size, in KB, which the function requires. This
    setting is not applicable and should be cleared when you run the Lambda function without
    containerization.

    - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function is
    long-lived and starts when the core starts.

    - **Timeout** *(integer) --* The allowed function execution time, after which Lambda should
    terminate the function. This timeout still applies to pinned Lambda functions for each
    request.
    """


_RequiredClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef = TypedDict(
    "_RequiredClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef", {"Id": str}
)
_OptionalClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef = TypedDict(
    "_OptionalClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef(
    _RequiredClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef,
    _OptionalClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef,
):
    """
    Type definition for `ClientCreateFunctionDefinitionInitialVersion` `Functions`

    - **FunctionArn** *(string) --* The ARN of the Lambda function.

    - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.

      - **EncodingType** *(string) --* The expected encoding type of the input payload for the
      function. The default is ''json''.

      - **Environment** *(dict) --* The environment configuration of the function.

        - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the
        host's /sys folder. Use this when the Lambda function needs to read device information
        from /sys. This setting applies only when you run the Lambda function in a Greengrass
        container.

        - **Execution** *(dict) --* Configuration related to executing the Lambda function

          - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
          Greengrass container (default) or without containerization. Unless your scenario
          requires that you run without containerization, we recommend that you run in a
          Greengrass container. Omit this value to run the Lambda function with the default
          containerization for the group.

          - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
          running the Lambda function. You can specify one or both values to override the default
          values. We recommend that you avoid running as root unless absolutely necessary to
          minimize the risk of unintended changes or malicious attacks. To run as root, you must
          set ''IsolationMode'' to ''NoContainer'' and update config.json in
          ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

            - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
            function.

            - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
            function.

        - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions,
        to which the Lambda function will be granted access. A Lambda function can have at most
        10 resources. ResourceAccessPolicies apply only when you run the Lambda function in a
        Greengrass container.

          - *(dict) --* A policy used by the function to access a resource.

            - **Permission** *(string) --* The permissions that the Lambda function has to the
            resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

            - **ResourceId** *(string) --* **[REQUIRED]** The ID of the resource. (This ID is
            assigned to the resource when you create the resource definiton.)

        - **Variables** *(dict) --* Environment variables for the Lambda function's configuration.

          - *(string) --*

            - *(string) --*

      - **ExecArgs** *(string) --* The execution arguments.

      - **Executable** *(string) --* The name of the function executable.

      - **MemorySize** *(integer) --* The memory size, in KB, which the function requires. This
      setting is not applicable and should be cleared when you run the Lambda function without
      containerization.

      - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function is
      long-lived and starts when the core starts.

      - **Timeout** *(integer) --* The allowed function execution time, after which Lambda should
      terminate the function. This timeout still applies to pinned Lambda functions for each
      request.

    - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the function. This
    value must be unique within the function definition version. Max length is 128 characters
    with pattern ''[a-zA-Z0-9:_-]+''.
    """


_ClientCreateFunctionDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionTypeDef",
    {
        "DefaultConfig": Dict[str, Any],
        "Functions": List[ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef],
    },
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionTypeDef
):
    """
    Type definition for `ClientCreateFunctionDefinition` `InitialVersion`

    - **DefaultConfig** *(dict) --* The default configuration that applies to all Lambda functions in
    this function definition version. Individual Lambda functions can override these settings.

      - **Execution** *(dict) --* Configuration information that specifies how a Lambda function runs.

        - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a Greengrass
        container (default) or without containerization. Unless your scenario requires that you run
        without containerization, we recommend that you run in a Greengrass container. Omit this
        value to run the Lambda function with the default containerization for the group.

        - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when running
        the Lambda function. You can specify one or both values to override the default values. We
        recommend that you avoid running as root unless absolutely necessary to minimize the risk of
        unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
        ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
        ''allowFunctionsToRunAsRoot'' to ''yes''.

          - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda function.

          - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda function.

    - **Functions** *(list) --* A list of Lambda functions in this function definition version.

      - *(dict) --* Information about a Lambda function.

        - **FunctionArn** *(string) --* The ARN of the Lambda function.

        - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.

          - **EncodingType** *(string) --* The expected encoding type of the input payload for the
          function. The default is ''json''.

          - **Environment** *(dict) --* The environment configuration of the function.

            - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the
            host's /sys folder. Use this when the Lambda function needs to read device information
            from /sys. This setting applies only when you run the Lambda function in a Greengrass
            container.

            - **Execution** *(dict) --* Configuration related to executing the Lambda function

              - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
              Greengrass container (default) or without containerization. Unless your scenario
              requires that you run without containerization, we recommend that you run in a
              Greengrass container. Omit this value to run the Lambda function with the default
              containerization for the group.

              - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
              running the Lambda function. You can specify one or both values to override the default
              values. We recommend that you avoid running as root unless absolutely necessary to
              minimize the risk of unintended changes or malicious attacks. To run as root, you must
              set ''IsolationMode'' to ''NoContainer'' and update config.json in
              ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

                - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
                function.

                - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
                function.

            - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions,
            to which the Lambda function will be granted access. A Lambda function can have at most
            10 resources. ResourceAccessPolicies apply only when you run the Lambda function in a
            Greengrass container.

              - *(dict) --* A policy used by the function to access a resource.

                - **Permission** *(string) --* The permissions that the Lambda function has to the
                resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

                - **ResourceId** *(string) --* **[REQUIRED]** The ID of the resource. (This ID is
                assigned to the resource when you create the resource definiton.)

            - **Variables** *(dict) --* Environment variables for the Lambda function's configuration.

              - *(string) --*

                - *(string) --*

          - **ExecArgs** *(string) --* The execution arguments.

          - **Executable** *(string) --* The name of the function executable.

          - **MemorySize** *(integer) --* The memory size, in KB, which the function requires. This
          setting is not applicable and should be cleared when you run the Lambda function without
          containerization.

          - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function is
          long-lived and starts when the core starts.

          - **Timeout** *(integer) --* The allowed function execution time, after which Lambda should
          terminate the function. This timeout still applies to pinned Lambda functions for each
          request.

        - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the function. This
        value must be unique within the function definition version. Max length is 128 characters
        with pattern ''[a-zA-Z0-9:_-]+''.
    """


_ClientCreateFunctionDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateFunctionDefinitionResponseTypeDef(
    _ClientCreateFunctionDefinitionResponseTypeDef
):
    """
    Type definition for `ClientCreateFunctionDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.
    """


_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {"IsolationMode": str, "RunAs": Dict[str, Any]},
    total=False,
)


class ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef(
    _ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef
):
    """
    Type definition for `ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironment` `Execution`

    - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
    Greengrass container (default) or without containerization. Unless your scenario requires
    that you run without containerization, we recommend that you run in a Greengrass
    container. Omit this value to run the Lambda function with the default containerization
    for the group.

    - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
    running the Lambda function. You can specify one or both values to override the default
    values. We recommend that you avoid running as root unless absolutely necessary to
    minimize the risk of unintended changes or malicious attacks. To run as root, you must
    set ''IsolationMode'' to ''NoContainer'' and update config.json in
    ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

      - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
      function.

      - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
      function.
    """


_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef,
        "ResourceAccessPolicies": List[Any],
        "Variables": Dict[str, str],
    },
    total=False,
)


class ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef(
    _ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef
):
    """
    Type definition for `ClientCreateFunctionDefinitionVersionFunctionsFunctionConfiguration` `Environment`

    - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the
    host's /sys folder. Use this when the Lambda function needs to read device information from
    /sys. This setting applies only when you run the Lambda function in a Greengrass container.

    - **Execution** *(dict) --* Configuration related to executing the Lambda function

      - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
      Greengrass container (default) or without containerization. Unless your scenario requires
      that you run without containerization, we recommend that you run in a Greengrass
      container. Omit this value to run the Lambda function with the default containerization
      for the group.

      - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
      running the Lambda function. You can specify one or both values to override the default
      values. We recommend that you avoid running as root unless absolutely necessary to
      minimize the risk of unintended changes or malicious attacks. To run as root, you must
      set ''IsolationMode'' to ''NoContainer'' and update config.json in
      ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

        - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
        function.

        - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
        function.

    - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions,
    to which the Lambda function will be granted access. A Lambda function can have at most 10
    resources. ResourceAccessPolicies apply only when you run the Lambda function in a
    Greengrass container.

      - *(dict) --* A policy used by the function to access a resource.

        - **Permission** *(string) --* The permissions that the Lambda function has to the
        resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

        - **ResourceId** *(string) --* **[REQUIRED]** The ID of the resource. (This ID is
        assigned to the resource when you create the resource definiton.)

    - **Variables** *(dict) --* Environment variables for the Lambda function's configuration.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef",
    {
        "EncodingType": str,
        "Environment": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef,
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)


class ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef(
    _ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFunctionDefinitionVersionFunctions` `FunctionConfiguration`

    - **EncodingType** *(string) --* The expected encoding type of the input payload for the
    function. The default is ''json''.

    - **Environment** *(dict) --* The environment configuration of the function.

      - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the
      host's /sys folder. Use this when the Lambda function needs to read device information from
      /sys. This setting applies only when you run the Lambda function in a Greengrass container.

      - **Execution** *(dict) --* Configuration related to executing the Lambda function

        - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
        Greengrass container (default) or without containerization. Unless your scenario requires
        that you run without containerization, we recommend that you run in a Greengrass
        container. Omit this value to run the Lambda function with the default containerization
        for the group.

        - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
        running the Lambda function. You can specify one or both values to override the default
        values. We recommend that you avoid running as root unless absolutely necessary to
        minimize the risk of unintended changes or malicious attacks. To run as root, you must
        set ''IsolationMode'' to ''NoContainer'' and update config.json in
        ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

          - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
          function.

          - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
          function.

      - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions,
      to which the Lambda function will be granted access. A Lambda function can have at most 10
      resources. ResourceAccessPolicies apply only when you run the Lambda function in a
      Greengrass container.

        - *(dict) --* A policy used by the function to access a resource.

          - **Permission** *(string) --* The permissions that the Lambda function has to the
          resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

          - **ResourceId** *(string) --* **[REQUIRED]** The ID of the resource. (This ID is
          assigned to the resource when you create the resource definiton.)

      - **Variables** *(dict) --* Environment variables for the Lambda function's configuration.

        - *(string) --*

          - *(string) --*

    - **ExecArgs** *(string) --* The execution arguments.

    - **Executable** *(string) --* The name of the function executable.

    - **MemorySize** *(integer) --* The memory size, in KB, which the function requires. This
    setting is not applicable and should be cleared when you run the Lambda function without
    containerization.

    - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function is
    long-lived and starts when the core starts.

    - **Timeout** *(integer) --* The allowed function execution time, after which Lambda should
    terminate the function. This timeout still applies to pinned Lambda functions for each
    request.
    """


_RequiredClientCreateFunctionDefinitionVersionFunctionsTypeDef = TypedDict(
    "_RequiredClientCreateFunctionDefinitionVersionFunctionsTypeDef", {"Id": str}
)
_OptionalClientCreateFunctionDefinitionVersionFunctionsTypeDef = TypedDict(
    "_OptionalClientCreateFunctionDefinitionVersionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFunctionDefinitionVersionFunctionsTypeDef(
    _RequiredClientCreateFunctionDefinitionVersionFunctionsTypeDef,
    _OptionalClientCreateFunctionDefinitionVersionFunctionsTypeDef,
):
    """
    Type definition for `ClientCreateFunctionDefinitionVersion` `Functions`

    - **FunctionArn** *(string) --* The ARN of the Lambda function.

    - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.

      - **EncodingType** *(string) --* The expected encoding type of the input payload for the
      function. The default is ''json''.

      - **Environment** *(dict) --* The environment configuration of the function.

        - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the
        host's /sys folder. Use this when the Lambda function needs to read device information from
        /sys. This setting applies only when you run the Lambda function in a Greengrass container.

        - **Execution** *(dict) --* Configuration related to executing the Lambda function

          - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
          Greengrass container (default) or without containerization. Unless your scenario requires
          that you run without containerization, we recommend that you run in a Greengrass
          container. Omit this value to run the Lambda function with the default containerization
          for the group.

          - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
          running the Lambda function. You can specify one or both values to override the default
          values. We recommend that you avoid running as root unless absolutely necessary to
          minimize the risk of unintended changes or malicious attacks. To run as root, you must
          set ''IsolationMode'' to ''NoContainer'' and update config.json in
          ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

            - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
            function.

            - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
            function.

        - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions,
        to which the Lambda function will be granted access. A Lambda function can have at most 10
        resources. ResourceAccessPolicies apply only when you run the Lambda function in a
        Greengrass container.

          - *(dict) --* A policy used by the function to access a resource.

            - **Permission** *(string) --* The permissions that the Lambda function has to the
            resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

            - **ResourceId** *(string) --* **[REQUIRED]** The ID of the resource. (This ID is
            assigned to the resource when you create the resource definiton.)

        - **Variables** *(dict) --* Environment variables for the Lambda function's configuration.

          - *(string) --*

            - *(string) --*

      - **ExecArgs** *(string) --* The execution arguments.

      - **Executable** *(string) --* The name of the function executable.

      - **MemorySize** *(integer) --* The memory size, in KB, which the function requires. This
      setting is not applicable and should be cleared when you run the Lambda function without
      containerization.

      - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function is
      long-lived and starts when the core starts.

      - **Timeout** *(integer) --* The allowed function execution time, after which Lambda should
      terminate the function. This timeout still applies to pinned Lambda functions for each
      request.

    - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the function. This
    value must be unique within the function definition version. Max length is 128 characters with
    pattern ''[a-zA-Z0-9:_-]+''.
    """


_ClientCreateFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateFunctionDefinitionVersionResponseTypeDef(
    _ClientCreateFunctionDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateFunctionDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the version.

    - **Version** *(string) --* The unique ID of the version.
    """


_ClientCreateGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientCreateGroupCertificateAuthorityResponseTypeDef",
    {"GroupCertificateAuthorityArn": str},
    total=False,
)


class ClientCreateGroupCertificateAuthorityResponseTypeDef(
    _ClientCreateGroupCertificateAuthorityResponseTypeDef
):
    """
    Type definition for `ClientCreateGroupCertificateAuthority` `Response`

    - **GroupCertificateAuthorityArn** *(string) --* The ARN of the group certificate authority.
    """


_ClientCreateGroupInitialVersionTypeDef = TypedDict(
    "_ClientCreateGroupInitialVersionTypeDef",
    {
        "ConnectorDefinitionVersionArn": str,
        "CoreDefinitionVersionArn": str,
        "DeviceDefinitionVersionArn": str,
        "FunctionDefinitionVersionArn": str,
        "LoggerDefinitionVersionArn": str,
        "ResourceDefinitionVersionArn": str,
        "SubscriptionDefinitionVersionArn": str,
    },
    total=False,
)


class ClientCreateGroupInitialVersionTypeDef(_ClientCreateGroupInitialVersionTypeDef):
    """
    Type definition for `ClientCreateGroup` `InitialVersion`

    - **ConnectorDefinitionVersionArn** *(string) --* The ARN of the connector definition version for
    this group.

    - **CoreDefinitionVersionArn** *(string) --* The ARN of the core definition version for this
    group.

    - **DeviceDefinitionVersionArn** *(string) --* The ARN of the device definition version for this
    group.

    - **FunctionDefinitionVersionArn** *(string) --* The ARN of the function definition version for
    this group.

    - **LoggerDefinitionVersionArn** *(string) --* The ARN of the logger definition version for this
    group.

    - **ResourceDefinitionVersionArn** *(string) --* The ARN of the resource definition version for
    this group.

    - **SubscriptionDefinitionVersionArn** *(string) --* The ARN of the subscription definition
    version for this group.
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    Type definition for `ClientCreateGroup` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.
    """


_ClientCreateGroupVersionResponseTypeDef = TypedDict(
    "_ClientCreateGroupVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateGroupVersionResponseTypeDef(_ClientCreateGroupVersionResponseTypeDef):
    """
    Type definition for `ClientCreateGroupVersion` `Response`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the version.

    - **Version** *(string) --* The unique ID of the version.
    """


_RequiredClientCreateLoggerDefinitionInitialVersionLoggersTypeDef = TypedDict(
    "_RequiredClientCreateLoggerDefinitionInitialVersionLoggersTypeDef",
    {"Component": str, "Id": str, "Level": str, "Type": str},
)
_OptionalClientCreateLoggerDefinitionInitialVersionLoggersTypeDef = TypedDict(
    "_OptionalClientCreateLoggerDefinitionInitialVersionLoggersTypeDef",
    {"Space": int},
    total=False,
)


class ClientCreateLoggerDefinitionInitialVersionLoggersTypeDef(
    _RequiredClientCreateLoggerDefinitionInitialVersionLoggersTypeDef,
    _OptionalClientCreateLoggerDefinitionInitialVersionLoggersTypeDef,
):
    """
    Type definition for `ClientCreateLoggerDefinitionInitialVersion` `Loggers`

    - **Component** *(string) --* **[REQUIRED]** The component that will be subject to logging.

    - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the logger. This
    value must be unique within the logger definition version. Max length is 128 characters with
    pattern ''[a-zA-Z0-9:_-]+''.

    - **Level** *(string) --* **[REQUIRED]** The level of the logs.

    - **Space** *(integer) --* The amount of file space, in KB, to use if the local file system
    is used for logging purposes.

    - **Type** *(string) --* **[REQUIRED]** The type of log output which will be used.
    """


_ClientCreateLoggerDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateLoggerDefinitionInitialVersionTypeDef",
    {"Loggers": List[ClientCreateLoggerDefinitionInitialVersionLoggersTypeDef]},
    total=False,
)


class ClientCreateLoggerDefinitionInitialVersionTypeDef(
    _ClientCreateLoggerDefinitionInitialVersionTypeDef
):
    """
    Type definition for `ClientCreateLoggerDefinition` `InitialVersion`

    - **Loggers** *(list) --* A list of loggers.

      - *(dict) --* Information about a logger

        - **Component** *(string) --* **[REQUIRED]** The component that will be subject to logging.

        - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the logger. This
        value must be unique within the logger definition version. Max length is 128 characters with
        pattern ''[a-zA-Z0-9:_-]+''.

        - **Level** *(string) --* **[REQUIRED]** The level of the logs.

        - **Space** *(integer) --* The amount of file space, in KB, to use if the local file system
        is used for logging purposes.

        - **Type** *(string) --* **[REQUIRED]** The type of log output which will be used.
    """


_ClientCreateLoggerDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateLoggerDefinitionResponseTypeDef(
    _ClientCreateLoggerDefinitionResponseTypeDef
):
    """
    Type definition for `ClientCreateLoggerDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.
    """


_RequiredClientCreateLoggerDefinitionVersionLoggersTypeDef = TypedDict(
    "_RequiredClientCreateLoggerDefinitionVersionLoggersTypeDef",
    {"Component": str, "Id": str, "Level": str, "Type": str},
)
_OptionalClientCreateLoggerDefinitionVersionLoggersTypeDef = TypedDict(
    "_OptionalClientCreateLoggerDefinitionVersionLoggersTypeDef",
    {"Space": int},
    total=False,
)


class ClientCreateLoggerDefinitionVersionLoggersTypeDef(
    _RequiredClientCreateLoggerDefinitionVersionLoggersTypeDef,
    _OptionalClientCreateLoggerDefinitionVersionLoggersTypeDef,
):
    """
    Type definition for `ClientCreateLoggerDefinitionVersion` `Loggers`

    - **Component** *(string) --* **[REQUIRED]** The component that will be subject to logging.

    - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the logger. This value
    must be unique within the logger definition version. Max length is 128 characters with pattern
    ''[a-zA-Z0-9:_-]+''.

    - **Level** *(string) --* **[REQUIRED]** The level of the logs.

    - **Space** *(integer) --* The amount of file space, in KB, to use if the local file system is
    used for logging purposes.

    - **Type** *(string) --* **[REQUIRED]** The type of log output which will be used.
    """


_ClientCreateLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateLoggerDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateLoggerDefinitionVersionResponseTypeDef(
    _ClientCreateLoggerDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateLoggerDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the version.

    - **Version** *(string) --* The unique ID of the version.
    """


_ClientCreateResourceDefinitionInitialVersionResourcesTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesTypeDef",
    {"Id": str, "Name": str, "ResourceDataContainer": Dict[str, Any]},
)


class ClientCreateResourceDefinitionInitialVersionResourcesTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesTypeDef
):
    """
    Type definition for `ClientCreateResourceDefinitionInitialVersion` `Resources`

    - **Id** *(string) --* **[REQUIRED]** The resource ID, used to refer to a resource in the
    Lambda function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
    This must be unique within a Greengrass group.

    - **Name** *(string) --* **[REQUIRED]** The descriptive resource name, which is displayed on
    the AWS IoT Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
    This must be unique within a Greengrass group.

    - **ResourceDataContainer** *(dict) --* **[REQUIRED]** A container of data for all resource
    types.

      - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device resource.

        - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.

          - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically adds
          the specified Linux OS group owner of the resource to the Lambda process privileges.
          Thus the Lambda process will have the file access permissions of the added Linux group.

          - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be
          added to the Lambda process. This field is optional.

        - **SourcePath** *(string) --* The local absolute path of the device resource. The source
        path for a device resource can refer only to a character device or block device under
        ''/dev''.

      - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume resource.

        - **DestinationPath** *(string) --* The absolute local path of the resource inside the
        Lambda environment.

        - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group privileges
        for the Lambda process. This field is optional.

          - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically adds
          the specified Linux OS group owner of the resource to the Lambda process privileges.
          Thus the Lambda process will have the file access permissions of the added Linux group.

          - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be
          added to the Lambda process. This field is optional.

        - **SourcePath** *(string) --* The local absolute path of the volume resource on the
        host. The source path for a volume resource type cannot start with ''/sys''.

      - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon S3
      machine learning resource.

        - **DestinationPath** *(string) --* The absolute local path of the resource inside the
        Lambda environment.

        - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model package
        must be in tar.gz or .zip format.

      - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an
      Amazon SageMaker machine learning resource.

        - **DestinationPath** *(string) --* The absolute local path of the resource inside the
        Lambda environment.

        - **SageMakerJobArn** *(string) --* The ARN of the Amazon SageMaker training job that
        represents the source model.

      - **SecretsManagerSecretResourceData** *(dict) --* Attributes that define a secret
      resource, which references a secret from AWS Secrets Manager.

        - **ARN** *(string) --* The ARN of the Secrets Manager secret to make available on the
        core. The value of the secret's latest version (represented by the ''AWSCURRENT'' staging
        label) is included by default.

        - **AdditionalStagingLabelsToDownload** *(list) --* Optional. The staging labels whose
        values you want to make available on the core, in addition to ''AWSCURRENT''.

          - *(string) --*
    """


_ClientCreateResourceDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionTypeDef",
    {"Resources": List[ClientCreateResourceDefinitionInitialVersionResourcesTypeDef]},
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionTypeDef(
    _ClientCreateResourceDefinitionInitialVersionTypeDef
):
    """
    Type definition for `ClientCreateResourceDefinition` `InitialVersion`

    - **Resources** *(list) --* A list of resources.

      - *(dict) --* Information about a resource.

        - **Id** *(string) --* **[REQUIRED]** The resource ID, used to refer to a resource in the
        Lambda function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
        This must be unique within a Greengrass group.

        - **Name** *(string) --* **[REQUIRED]** The descriptive resource name, which is displayed on
        the AWS IoT Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
        This must be unique within a Greengrass group.

        - **ResourceDataContainer** *(dict) --* **[REQUIRED]** A container of data for all resource
        types.

          - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device resource.

            - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.

              - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically adds
              the specified Linux OS group owner of the resource to the Lambda process privileges.
              Thus the Lambda process will have the file access permissions of the added Linux group.

              - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be
              added to the Lambda process. This field is optional.

            - **SourcePath** *(string) --* The local absolute path of the device resource. The source
            path for a device resource can refer only to a character device or block device under
            ''/dev''.

          - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume resource.

            - **DestinationPath** *(string) --* The absolute local path of the resource inside the
            Lambda environment.

            - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group privileges
            for the Lambda process. This field is optional.

              - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically adds
              the specified Linux OS group owner of the resource to the Lambda process privileges.
              Thus the Lambda process will have the file access permissions of the added Linux group.

              - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be
              added to the Lambda process. This field is optional.

            - **SourcePath** *(string) --* The local absolute path of the volume resource on the
            host. The source path for a volume resource type cannot start with ''/sys''.

          - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon S3
          machine learning resource.

            - **DestinationPath** *(string) --* The absolute local path of the resource inside the
            Lambda environment.

            - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model package
            must be in tar.gz or .zip format.

          - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an
          Amazon SageMaker machine learning resource.

            - **DestinationPath** *(string) --* The absolute local path of the resource inside the
            Lambda environment.

            - **SageMakerJobArn** *(string) --* The ARN of the Amazon SageMaker training job that
            represents the source model.

          - **SecretsManagerSecretResourceData** *(dict) --* Attributes that define a secret
          resource, which references a secret from AWS Secrets Manager.

            - **ARN** *(string) --* The ARN of the Secrets Manager secret to make available on the
            core. The value of the secret's latest version (represented by the ''AWSCURRENT'' staging
            label) is included by default.

            - **AdditionalStagingLabelsToDownload** *(list) --* Optional. The staging labels whose
            values you want to make available on the core, in addition to ''AWSCURRENT''.

              - *(string) --*
    """


_ClientCreateResourceDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateResourceDefinitionResponseTypeDef(
    _ClientCreateResourceDefinitionResponseTypeDef
):
    """
    Type definition for `ClientCreateResourceDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.
    """


_ClientCreateResourceDefinitionVersionResourcesTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesTypeDef",
    {"Id": str, "Name": str, "ResourceDataContainer": Dict[str, Any]},
)


class ClientCreateResourceDefinitionVersionResourcesTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesTypeDef
):
    """
    Type definition for `ClientCreateResourceDefinitionVersion` `Resources`

    - **Id** *(string) --* **[REQUIRED]** The resource ID, used to refer to a resource in the
    Lambda function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
    This must be unique within a Greengrass group.

    - **Name** *(string) --* **[REQUIRED]** The descriptive resource name, which is displayed on
    the AWS IoT Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
    This must be unique within a Greengrass group.

    - **ResourceDataContainer** *(dict) --* **[REQUIRED]** A container of data for all resource
    types.

      - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device resource.

        - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.

          - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically adds the
          specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
          Lambda process will have the file access permissions of the added Linux group.

          - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be
          added to the Lambda process. This field is optional.

        - **SourcePath** *(string) --* The local absolute path of the device resource. The source
        path for a device resource can refer only to a character device or block device under
        ''/dev''.

      - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume resource.

        - **DestinationPath** *(string) --* The absolute local path of the resource inside the
        Lambda environment.

        - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group privileges for
        the Lambda process. This field is optional.

          - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically adds the
          specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
          Lambda process will have the file access permissions of the added Linux group.

          - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be
          added to the Lambda process. This field is optional.

        - **SourcePath** *(string) --* The local absolute path of the volume resource on the host.
        The source path for a volume resource type cannot start with ''/sys''.

      - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon S3
      machine learning resource.

        - **DestinationPath** *(string) --* The absolute local path of the resource inside the
        Lambda environment.

        - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model package
        must be in tar.gz or .zip format.

      - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon
      SageMaker machine learning resource.

        - **DestinationPath** *(string) --* The absolute local path of the resource inside the
        Lambda environment.

        - **SageMakerJobArn** *(string) --* The ARN of the Amazon SageMaker training job that
        represents the source model.

      - **SecretsManagerSecretResourceData** *(dict) --* Attributes that define a secret resource,
      which references a secret from AWS Secrets Manager.

        - **ARN** *(string) --* The ARN of the Secrets Manager secret to make available on the
        core. The value of the secret's latest version (represented by the ''AWSCURRENT'' staging
        label) is included by default.

        - **AdditionalStagingLabelsToDownload** *(list) --* Optional. The staging labels whose
        values you want to make available on the core, in addition to ''AWSCURRENT''.

          - *(string) --*
    """


_ClientCreateResourceDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateResourceDefinitionVersionResponseTypeDef(
    _ClientCreateResourceDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateResourceDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the version.

    - **Version** *(string) --* The unique ID of the version.
    """


_ClientCreateSoftwareUpdateJobResponseTypeDef = TypedDict(
    "_ClientCreateSoftwareUpdateJobResponseTypeDef",
    {"IotJobArn": str, "IotJobId": str, "PlatformSoftwareVersion": str},
    total=False,
)


class ClientCreateSoftwareUpdateJobResponseTypeDef(
    _ClientCreateSoftwareUpdateJobResponseTypeDef
):
    """
    Type definition for `ClientCreateSoftwareUpdateJob` `Response`

    - **IotJobArn** *(string) --* The IoT Job ARN corresponding to this update.

    - **IotJobId** *(string) --* The IoT Job Id corresponding to this update.

    - **PlatformSoftwareVersion** *(string) --* The software version installed on the device or
    devices after the update.
    """


_ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef = TypedDict(
    "_ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
)


class ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef(
    _ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef
):
    """
    Type definition for `ClientCreateSubscriptionDefinitionInitialVersion` `Subscriptions`

    - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the subscription.
    This value must be unique within the subscription definition version. Max length is 128
    characters with pattern ''[a-zA-Z0-9:_-]+''.

    - **Source** *(string) --* **[REQUIRED]** The source of the subscription. Can be a thing ARN,
    a Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
    'GGShadowService'.

    - **Subject** *(string) --* **[REQUIRED]** The MQTT topic used to route the message.

    - **Target** *(string) --* **[REQUIRED]** Where the message is sent to. Can be a thing ARN, a
    Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
    'GGShadowService'.
    """


_ClientCreateSubscriptionDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateSubscriptionDefinitionInitialVersionTypeDef",
    {
        "Subscriptions": List[
            ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef
        ]
    },
    total=False,
)


class ClientCreateSubscriptionDefinitionInitialVersionTypeDef(
    _ClientCreateSubscriptionDefinitionInitialVersionTypeDef
):
    """
    Type definition for `ClientCreateSubscriptionDefinition` `InitialVersion`

    - **Subscriptions** *(list) --* A list of subscriptions.

      - *(dict) --* Information about a subscription.

        - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the subscription.
        This value must be unique within the subscription definition version. Max length is 128
        characters with pattern ''[a-zA-Z0-9:_-]+''.

        - **Source** *(string) --* **[REQUIRED]** The source of the subscription. Can be a thing ARN,
        a Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
        'GGShadowService'.

        - **Subject** *(string) --* **[REQUIRED]** The MQTT topic used to route the message.

        - **Target** *(string) --* **[REQUIRED]** Where the message is sent to. Can be a thing ARN, a
        Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
        'GGShadowService'.
    """


_ClientCreateSubscriptionDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateSubscriptionDefinitionResponseTypeDef(
    _ClientCreateSubscriptionDefinitionResponseTypeDef
):
    """
    Type definition for `ClientCreateSubscriptionDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.
    """


_ClientCreateSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateSubscriptionDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateSubscriptionDefinitionVersionResponseTypeDef(
    _ClientCreateSubscriptionDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateSubscriptionDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the version.

    - **Version** *(string) --* The unique ID of the version.
    """


_ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef = TypedDict(
    "_ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
)


class ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef(
    _ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef
):
    """
    Type definition for `ClientCreateSubscriptionDefinitionVersion` `Subscriptions`

    - **Id** *(string) --* **[REQUIRED]** A descriptive or arbitrary ID for the subscription. This
    value must be unique within the subscription definition version. Max length is 128 characters
    with pattern ''[a-zA-Z0-9:_-]+''.

    - **Source** *(string) --* **[REQUIRED]** The source of the subscription. Can be a thing ARN, a
    Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
    'GGShadowService'.

    - **Subject** *(string) --* **[REQUIRED]** The MQTT topic used to route the message.

    - **Target** *(string) --* **[REQUIRED]** Where the message is sent to. Can be a thing ARN, a
    Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
    'GGShadowService'.
    """


_ClientDisassociateRoleFromGroupResponseTypeDef = TypedDict(
    "_ClientDisassociateRoleFromGroupResponseTypeDef",
    {"DisassociatedAt": str},
    total=False,
)


class ClientDisassociateRoleFromGroupResponseTypeDef(
    _ClientDisassociateRoleFromGroupResponseTypeDef
):
    """
    Type definition for `ClientDisassociateRoleFromGroup` `Response`

    - **DisassociatedAt** *(string) --* The time, in milliseconds since the epoch, when the role
    was disassociated from the group.
    """


_ClientDisassociateServiceRoleFromAccountResponseTypeDef = TypedDict(
    "_ClientDisassociateServiceRoleFromAccountResponseTypeDef",
    {"DisassociatedAt": str},
    total=False,
)


class ClientDisassociateServiceRoleFromAccountResponseTypeDef(
    _ClientDisassociateServiceRoleFromAccountResponseTypeDef
):
    """
    Type definition for `ClientDisassociateServiceRoleFromAccount` `Response`

    - **DisassociatedAt** *(string) --* The time when the service role was disassociated from the
    account.
    """


_ClientGetAssociatedRoleResponseTypeDef = TypedDict(
    "_ClientGetAssociatedRoleResponseTypeDef",
    {"AssociatedAt": str, "RoleArn": str},
    total=False,
)


class ClientGetAssociatedRoleResponseTypeDef(_ClientGetAssociatedRoleResponseTypeDef):
    """
    Type definition for `ClientGetAssociatedRole` `Response`

    - **AssociatedAt** *(string) --* The time when the role was associated with the group.

    - **RoleArn** *(string) --* The ARN of the role that is associated with the group.
    """


_ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef = TypedDict(
    "_ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)


class ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef(
    _ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef
):
    """
    Type definition for `ClientGetBulkDeploymentStatusResponse` `ErrorDetails`

    - **DetailedErrorCode** *(string) --* A detailed error code.

    - **DetailedErrorMessage** *(string) --* A detailed error message.
    """


_ClientGetBulkDeploymentStatusResponseTypeDef = TypedDict(
    "_ClientGetBulkDeploymentStatusResponseTypeDef",
    {
        "BulkDeploymentMetrics": Dict[str, Any],
        "BulkDeploymentStatus": str,
        "CreatedAt": str,
        "ErrorDetails": List[ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef],
        "ErrorMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetBulkDeploymentStatusResponseTypeDef(
    _ClientGetBulkDeploymentStatusResponseTypeDef
):
    """
    Type definition for `ClientGetBulkDeploymentStatus` `Response`

    - **BulkDeploymentMetrics** *(dict) --* Relevant metrics on input records processed during bulk
    deployment.

      - **InvalidInputRecords** *(integer) --* The total number of records that returned a
      non-retryable error. For example, this can occur if a group record from the input file uses
      an invalid format or specifies a nonexistent group version, or if the execution role doesn't
      grant permission to deploy a group or group version.

      - **RecordsProcessed** *(integer) --* The total number of group records from the input file
      that have been processed so far, or attempted.

      - **RetryAttempts** *(integer) --* The total number of deployment attempts that returned a
      retryable error. For example, a retry is triggered if the attempt to deploy a group returns a
      throttling error. ''StartBulkDeployment'' retries a group deployment up to five times.

    - **BulkDeploymentStatus** *(string) --* The status of the bulk deployment.

    - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.

    - **ErrorDetails** *(list) --* Error details

      - *(dict) --* Details about the error.

        - **DetailedErrorCode** *(string) --* A detailed error code.

        - **DetailedErrorMessage** *(string) --* A detailed error message.

    - **ErrorMessage** *(string) --* Error message

    - **tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientGetConnectivityInfoResponseConnectivityInfoTypeDef = TypedDict(
    "_ClientGetConnectivityInfoResponseConnectivityInfoTypeDef",
    {"HostAddress": str, "Id": str, "Metadata": str, "PortNumber": int},
    total=False,
)


class ClientGetConnectivityInfoResponseConnectivityInfoTypeDef(
    _ClientGetConnectivityInfoResponseConnectivityInfoTypeDef
):
    """
    Type definition for `ClientGetConnectivityInfoResponse` `ConnectivityInfo`

    - **HostAddress** *(string) --* The endpoint for the Greengrass core. Can be an IP address
    or DNS.

    - **Id** *(string) --* The ID of the connectivity information.

    - **Metadata** *(string) --* Metadata for this endpoint.

    - **PortNumber** *(integer) --* The port of the Greengrass core. Usually 8883.
    """


_ClientGetConnectivityInfoResponseTypeDef = TypedDict(
    "_ClientGetConnectivityInfoResponseTypeDef",
    {
        "ConnectivityInfo": List[
            ClientGetConnectivityInfoResponseConnectivityInfoTypeDef
        ],
        "Message": str,
    },
    total=False,
)


class ClientGetConnectivityInfoResponseTypeDef(
    _ClientGetConnectivityInfoResponseTypeDef
):
    """
    Type definition for `ClientGetConnectivityInfo` `Response`

    - **ConnectivityInfo** *(list) --* Connectivity info list.

      - *(dict) --* Information about a Greengrass core's connectivity.

        - **HostAddress** *(string) --* The endpoint for the Greengrass core. Can be an IP address
        or DNS.

        - **Id** *(string) --* The ID of the connectivity information.

        - **Metadata** *(string) --* Metadata for this endpoint.

        - **PortNumber** *(integer) --* The port of the Greengrass core. Usually 8883.

    - **Message** *(string) --* A message about the connectivity info request.
    """


_ClientGetConnectorDefinitionResponseTypeDef = TypedDict(
    "_ClientGetConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetConnectorDefinitionResponseTypeDef(
    _ClientGetConnectorDefinitionResponseTypeDef
):
    """
    Type definition for `ClientGetConnectorDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef",
    {"Connectors": List[Any]},
    total=False,
)


class ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef
):
    """
    Type definition for `ClientGetConnectorDefinitionVersionResponse` `Definition`

    - **Connectors** *(list) --* A list of references to connectors in this version, with their
    corresponding configuration settings.

      - *(dict) --* Information about a connector. Connectors run on the Greengrass core and
      contain built-in integration with local infrastructure, device protocols, AWS, and other
      cloud services.

        - **ConnectorArn** *(string) --* The ARN of the connector.

        - **Id** *(string) --* A descriptive or arbitrary ID for the connector. This value must
        be unique within the connector definition version. Max length is 128 characters with
        pattern [a-zA-Z0-9:_-]+.

        - **Parameters** *(dict) --* The parameters or configuration that the connector uses.

          - *(string) --*

            - *(string) --*
    """


_ClientGetConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetConnectorDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)


class ClientGetConnectorDefinitionVersionResponseTypeDef(
    _ClientGetConnectorDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientGetConnectorDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the connector definition version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    connector definition version was created.

    - **Definition** *(dict) --* Information about the connector definition version.

      - **Connectors** *(list) --* A list of references to connectors in this version, with their
      corresponding configuration settings.

        - *(dict) --* Information about a connector. Connectors run on the Greengrass core and
        contain built-in integration with local infrastructure, device protocols, AWS, and other
        cloud services.

          - **ConnectorArn** *(string) --* The ARN of the connector.

          - **Id** *(string) --* A descriptive or arbitrary ID for the connector. This value must
          be unique within the connector definition version. Max length is 128 characters with
          pattern [a-zA-Z0-9:_-]+.

          - **Parameters** *(dict) --* The parameters or configuration that the connector uses.

            - *(string) --*

              - *(string) --*

    - **Id** *(string) --* The ID of the connector definition version.

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Version** *(string) --* The version of the connector definition version.
    """


_ClientGetCoreDefinitionResponseTypeDef = TypedDict(
    "_ClientGetCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetCoreDefinitionResponseTypeDef(_ClientGetCoreDefinitionResponseTypeDef):
    """
    Type definition for `ClientGetCoreDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef = TypedDict(
    "_ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef",
    {"CertificateArn": str, "Id": str, "SyncShadow": bool, "ThingArn": str},
    total=False,
)


class ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef(
    _ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef
):
    """
    Type definition for `ClientGetCoreDefinitionVersionResponseDefinition` `Cores`

    - **CertificateArn** *(string) --* The ARN of the certificate associated with the core.

    - **Id** *(string) --* A descriptive or arbitrary ID for the core. This value must be
    unique within the core definition version. Max length is 128 characters with pattern
    ''[a-zA-Z0-9:_-]+''.

    - **SyncShadow** *(boolean) --* If true, the core's local shadow is automatically synced
    with the cloud.

    - **ThingArn** *(string) --* The ARN of the thing which is the core.
    """


_ClientGetCoreDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetCoreDefinitionVersionResponseDefinitionTypeDef",
    {"Cores": List[ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef]},
    total=False,
)


class ClientGetCoreDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetCoreDefinitionVersionResponseDefinitionTypeDef
):
    """
    Type definition for `ClientGetCoreDefinitionVersionResponse` `Definition`

    - **Cores** *(list) --* A list of cores in the core definition version.

      - *(dict) --* Information about a core.

        - **CertificateArn** *(string) --* The ARN of the certificate associated with the core.

        - **Id** *(string) --* A descriptive or arbitrary ID for the core. This value must be
        unique within the core definition version. Max length is 128 characters with pattern
        ''[a-zA-Z0-9:_-]+''.

        - **SyncShadow** *(boolean) --* If true, the core's local shadow is automatically synced
        with the cloud.

        - **ThingArn** *(string) --* The ARN of the thing which is the core.
    """


_ClientGetCoreDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetCoreDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetCoreDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)


class ClientGetCoreDefinitionVersionResponseTypeDef(
    _ClientGetCoreDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientGetCoreDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the core definition version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the core
    definition version was created.

    - **Definition** *(dict) --* Information about the core definition version.

      - **Cores** *(list) --* A list of cores in the core definition version.

        - *(dict) --* Information about a core.

          - **CertificateArn** *(string) --* The ARN of the certificate associated with the core.

          - **Id** *(string) --* A descriptive or arbitrary ID for the core. This value must be
          unique within the core definition version. Max length is 128 characters with pattern
          ''[a-zA-Z0-9:_-]+''.

          - **SyncShadow** *(boolean) --* If true, the core's local shadow is automatically synced
          with the cloud.

          - **ThingArn** *(string) --* The ARN of the thing which is the core.

    - **Id** *(string) --* The ID of the core definition version.

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Version** *(string) --* The version of the core definition version.
    """


_ClientGetDeploymentStatusResponseErrorDetailsTypeDef = TypedDict(
    "_ClientGetDeploymentStatusResponseErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)


class ClientGetDeploymentStatusResponseErrorDetailsTypeDef(
    _ClientGetDeploymentStatusResponseErrorDetailsTypeDef
):
    """
    Type definition for `ClientGetDeploymentStatusResponse` `ErrorDetails`

    - **DetailedErrorCode** *(string) --* A detailed error code.

    - **DetailedErrorMessage** *(string) --* A detailed error message.
    """


_ClientGetDeploymentStatusResponseTypeDef = TypedDict(
    "_ClientGetDeploymentStatusResponseTypeDef",
    {
        "DeploymentStatus": str,
        "DeploymentType": str,
        "ErrorDetails": List[ClientGetDeploymentStatusResponseErrorDetailsTypeDef],
        "ErrorMessage": str,
        "UpdatedAt": str,
    },
    total=False,
)


class ClientGetDeploymentStatusResponseTypeDef(
    _ClientGetDeploymentStatusResponseTypeDef
):
    """
    Type definition for `ClientGetDeploymentStatus` `Response`

    - **DeploymentStatus** *(string) --* The status of the deployment: ''InProgress'',
    ''Building'', ''Success'', or ''Failure''.

    - **DeploymentType** *(string) --* The type of the deployment.

    - **ErrorDetails** *(list) --* Error details

      - *(dict) --* Details about the error.

        - **DetailedErrorCode** *(string) --* A detailed error code.

        - **DetailedErrorMessage** *(string) --* A detailed error message.

    - **ErrorMessage** *(string) --* Error message

    - **UpdatedAt** *(string) --* The time, in milliseconds since the epoch, when the deployment
    status was updated.
    """


_ClientGetDeviceDefinitionResponseTypeDef = TypedDict(
    "_ClientGetDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDeviceDefinitionResponseTypeDef(
    _ClientGetDeviceDefinitionResponseTypeDef
):
    """
    Type definition for `ClientGetDeviceDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef = TypedDict(
    "_ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef",
    {"CertificateArn": str, "Id": str, "SyncShadow": bool, "ThingArn": str},
    total=False,
)


class ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef(
    _ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef
):
    """
    Type definition for `ClientGetDeviceDefinitionVersionResponseDefinition` `Devices`

    - **CertificateArn** *(string) --* The ARN of the certificate associated with the device.

    - **Id** *(string) --* A descriptive or arbitrary ID for the device. This value must be
    unique within the device definition version. Max length is 128 characters with pattern
    ''[a-zA-Z0-9:_-]+''.

    - **SyncShadow** *(boolean) --* If true, the device's local shadow will be automatically
    synced with the cloud.

    - **ThingArn** *(string) --* The thing ARN of the device.
    """


_ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef",
    {"Devices": List[ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef]},
    total=False,
)


class ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef
):
    """
    Type definition for `ClientGetDeviceDefinitionVersionResponse` `Definition`

    - **Devices** *(list) --* A list of devices in the definition version.

      - *(dict) --* Information about a device.

        - **CertificateArn** *(string) --* The ARN of the certificate associated with the device.

        - **Id** *(string) --* A descriptive or arbitrary ID for the device. This value must be
        unique within the device definition version. Max length is 128 characters with pattern
        ''[a-zA-Z0-9:_-]+''.

        - **SyncShadow** *(boolean) --* If true, the device's local shadow will be automatically
        synced with the cloud.

        - **ThingArn** *(string) --* The thing ARN of the device.
    """


_ClientGetDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetDeviceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)


class ClientGetDeviceDefinitionVersionResponseTypeDef(
    _ClientGetDeviceDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientGetDeviceDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the device definition version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    device definition version was created.

    - **Definition** *(dict) --* Information about the device definition version.

      - **Devices** *(list) --* A list of devices in the definition version.

        - *(dict) --* Information about a device.

          - **CertificateArn** *(string) --* The ARN of the certificate associated with the device.

          - **Id** *(string) --* A descriptive or arbitrary ID for the device. This value must be
          unique within the device definition version. Max length is 128 characters with pattern
          ''[a-zA-Z0-9:_-]+''.

          - **SyncShadow** *(boolean) --* If true, the device's local shadow will be automatically
          synced with the cloud.

          - **ThingArn** *(string) --* The thing ARN of the device.

    - **Id** *(string) --* The ID of the device definition version.

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Version** *(string) --* The version of the device definition version.
    """


_ClientGetFunctionDefinitionResponseTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetFunctionDefinitionResponseTypeDef(
    _ClientGetFunctionDefinitionResponseTypeDef
):
    """
    Type definition for `ClientGetFunctionDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {"IsolationMode": str, "RunAs": Dict[str, Any]},
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef
):
    """
    Type definition for `ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironment` `Execution`

    - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
    Greengrass container (default) or without containerization. Unless your scenario
    requires that you run without containerization, we recommend that you run in a
    Greengrass container. Omit this value to run the Lambda function with the default
    containerization for the group.

    - **RunAs** *(dict) --* Specifies the user and group whose permissions are used
    when running the Lambda function. You can specify one or both values to override
    the default values. We recommend that you avoid running as root unless absolutely
    necessary to minimize the risk of unintended changes or malicious attacks. To run
    as root, you must set ''IsolationMode'' to ''NoContainer'' and update config.json
    in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

      - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
      function.

      - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
      function.
    """


_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef,
        "ResourceAccessPolicies": List[Any],
        "Variables": Dict[str, Any],
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef
):
    """
    Type definition for `ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfiguration` `Environment`

    - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access
    the host's /sys folder. Use this when the Lambda function needs to read device
    information from /sys. This setting applies only when you run the Lambda function in
    a Greengrass container.

    - **Execution** *(dict) --* Configuration related to executing the Lambda function

      - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
      Greengrass container (default) or without containerization. Unless your scenario
      requires that you run without containerization, we recommend that you run in a
      Greengrass container. Omit this value to run the Lambda function with the default
      containerization for the group.

      - **RunAs** *(dict) --* Specifies the user and group whose permissions are used
      when running the Lambda function. You can specify one or both values to override
      the default values. We recommend that you avoid running as root unless absolutely
      necessary to minimize the risk of unintended changes or malicious attacks. To run
      as root, you must set ''IsolationMode'' to ''NoContainer'' and update config.json
      in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

        - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
        function.

        - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
        function.

    - **ResourceAccessPolicies** *(list) --* A list of the resources, with their
    permissions, to which the Lambda function will be granted access. A Lambda function
    can have at most 10 resources. ResourceAccessPolicies apply only when you run the
    Lambda function in a Greengrass container.

      - *(dict) --* A policy used by the function to access a resource.

        - **Permission** *(string) --* The permissions that the Lambda function has to
        the resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

        - **ResourceId** *(string) --* The ID of the resource. (This ID is assigned to
        the resource when you create the resource definiton.)

    - **Variables** *(dict) --* Environment variables for the Lambda function's
    configuration.

      - *(string) --*

        - *(string) --*
    """


_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef",
    {
        "EncodingType": str,
        "Environment": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef,
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef
):
    """
    Type definition for `ClientGetFunctionDefinitionVersionResponseDefinitionFunctions` `FunctionConfiguration`

    - **EncodingType** *(string) --* The expected encoding type of the input payload for
    the function. The default is ''json''.

    - **Environment** *(dict) --* The environment configuration of the function.

      - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access
      the host's /sys folder. Use this when the Lambda function needs to read device
      information from /sys. This setting applies only when you run the Lambda function in
      a Greengrass container.

      - **Execution** *(dict) --* Configuration related to executing the Lambda function

        - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
        Greengrass container (default) or without containerization. Unless your scenario
        requires that you run without containerization, we recommend that you run in a
        Greengrass container. Omit this value to run the Lambda function with the default
        containerization for the group.

        - **RunAs** *(dict) --* Specifies the user and group whose permissions are used
        when running the Lambda function. You can specify one or both values to override
        the default values. We recommend that you avoid running as root unless absolutely
        necessary to minimize the risk of unintended changes or malicious attacks. To run
        as root, you must set ''IsolationMode'' to ''NoContainer'' and update config.json
        in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

          - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
          function.

          - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
          function.

      - **ResourceAccessPolicies** *(list) --* A list of the resources, with their
      permissions, to which the Lambda function will be granted access. A Lambda function
      can have at most 10 resources. ResourceAccessPolicies apply only when you run the
      Lambda function in a Greengrass container.

        - *(dict) --* A policy used by the function to access a resource.

          - **Permission** *(string) --* The permissions that the Lambda function has to
          the resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

          - **ResourceId** *(string) --* The ID of the resource. (This ID is assigned to
          the resource when you create the resource definiton.)

      - **Variables** *(dict) --* Environment variables for the Lambda function's
      configuration.

        - *(string) --*

          - *(string) --*

    - **ExecArgs** *(string) --* The execution arguments.

    - **Executable** *(string) --* The name of the function executable.

    - **MemorySize** *(integer) --* The memory size, in KB, which the function requires.
    This setting is not applicable and should be cleared when you run the Lambda function
    without containerization.

    - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function
    is long-lived and starts when the core starts.

    - **Timeout** *(integer) --* The allowed function execution time, after which Lambda
    should terminate the function. This timeout still applies to pinned Lambda functions
    for each request.
    """


_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef,
        "Id": str,
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef
):
    """
    Type definition for `ClientGetFunctionDefinitionVersionResponseDefinition` `Functions`

    - **FunctionArn** *(string) --* The ARN of the Lambda function.

    - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.

      - **EncodingType** *(string) --* The expected encoding type of the input payload for
      the function. The default is ''json''.

      - **Environment** *(dict) --* The environment configuration of the function.

        - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access
        the host's /sys folder. Use this when the Lambda function needs to read device
        information from /sys. This setting applies only when you run the Lambda function in
        a Greengrass container.

        - **Execution** *(dict) --* Configuration related to executing the Lambda function

          - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
          Greengrass container (default) or without containerization. Unless your scenario
          requires that you run without containerization, we recommend that you run in a
          Greengrass container. Omit this value to run the Lambda function with the default
          containerization for the group.

          - **RunAs** *(dict) --* Specifies the user and group whose permissions are used
          when running the Lambda function. You can specify one or both values to override
          the default values. We recommend that you avoid running as root unless absolutely
          necessary to minimize the risk of unintended changes or malicious attacks. To run
          as root, you must set ''IsolationMode'' to ''NoContainer'' and update config.json
          in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

            - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
            function.

            - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
            function.

        - **ResourceAccessPolicies** *(list) --* A list of the resources, with their
        permissions, to which the Lambda function will be granted access. A Lambda function
        can have at most 10 resources. ResourceAccessPolicies apply only when you run the
        Lambda function in a Greengrass container.

          - *(dict) --* A policy used by the function to access a resource.

            - **Permission** *(string) --* The permissions that the Lambda function has to
            the resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

            - **ResourceId** *(string) --* The ID of the resource. (This ID is assigned to
            the resource when you create the resource definiton.)

        - **Variables** *(dict) --* Environment variables for the Lambda function's
        configuration.

          - *(string) --*

            - *(string) --*

      - **ExecArgs** *(string) --* The execution arguments.

      - **Executable** *(string) --* The name of the function executable.

      - **MemorySize** *(integer) --* The memory size, in KB, which the function requires.
      This setting is not applicable and should be cleared when you run the Lambda function
      without containerization.

      - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function
      is long-lived and starts when the core starts.

      - **Timeout** *(integer) --* The allowed function execution time, after which Lambda
      should terminate the function. This timeout still applies to pinned Lambda functions
      for each request.

    - **Id** *(string) --* A descriptive or arbitrary ID for the function. This value must be
    unique within the function definition version. Max length is 128 characters with pattern
    ''[a-zA-Z0-9:_-]+''.
    """


_ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef",
    {
        "DefaultConfig": Dict[str, Any],
        "Functions": List[
            ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef
        ],
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef
):
    """
    Type definition for `ClientGetFunctionDefinitionVersionResponse` `Definition`

    - **DefaultConfig** *(dict) --* The default configuration that applies to all Lambda
    functions in this function definition version. Individual Lambda functions can override these
    settings.

      - **Execution** *(dict) --* Configuration information that specifies how a Lambda function
      runs.

        - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
        Greengrass container (default) or without containerization. Unless your scenario requires
        that you run without containerization, we recommend that you run in a Greengrass
        container. Omit this value to run the Lambda function with the default containerization
        for the group.

        - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
        running the Lambda function. You can specify one or both values to override the default
        values. We recommend that you avoid running as root unless absolutely necessary to
        minimize the risk of unintended changes or malicious attacks. To run as root, you must
        set ''IsolationMode'' to ''NoContainer'' and update config.json in
        ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

          - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
          function.

          - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
          function.

    - **Functions** *(list) --* A list of Lambda functions in this function definition version.

      - *(dict) --* Information about a Lambda function.

        - **FunctionArn** *(string) --* The ARN of the Lambda function.

        - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.

          - **EncodingType** *(string) --* The expected encoding type of the input payload for
          the function. The default is ''json''.

          - **Environment** *(dict) --* The environment configuration of the function.

            - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access
            the host's /sys folder. Use this when the Lambda function needs to read device
            information from /sys. This setting applies only when you run the Lambda function in
            a Greengrass container.

            - **Execution** *(dict) --* Configuration related to executing the Lambda function

              - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
              Greengrass container (default) or without containerization. Unless your scenario
              requires that you run without containerization, we recommend that you run in a
              Greengrass container. Omit this value to run the Lambda function with the default
              containerization for the group.

              - **RunAs** *(dict) --* Specifies the user and group whose permissions are used
              when running the Lambda function. You can specify one or both values to override
              the default values. We recommend that you avoid running as root unless absolutely
              necessary to minimize the risk of unintended changes or malicious attacks. To run
              as root, you must set ''IsolationMode'' to ''NoContainer'' and update config.json
              in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

                - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
                function.

                - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
                function.

            - **ResourceAccessPolicies** *(list) --* A list of the resources, with their
            permissions, to which the Lambda function will be granted access. A Lambda function
            can have at most 10 resources. ResourceAccessPolicies apply only when you run the
            Lambda function in a Greengrass container.

              - *(dict) --* A policy used by the function to access a resource.

                - **Permission** *(string) --* The permissions that the Lambda function has to
                the resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

                - **ResourceId** *(string) --* The ID of the resource. (This ID is assigned to
                the resource when you create the resource definiton.)

            - **Variables** *(dict) --* Environment variables for the Lambda function's
            configuration.

              - *(string) --*

                - *(string) --*

          - **ExecArgs** *(string) --* The execution arguments.

          - **Executable** *(string) --* The name of the function executable.

          - **MemorySize** *(integer) --* The memory size, in KB, which the function requires.
          This setting is not applicable and should be cleared when you run the Lambda function
          without containerization.

          - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function
          is long-lived and starts when the core starts.

          - **Timeout** *(integer) --* The allowed function execution time, after which Lambda
          should terminate the function. This timeout still applies to pinned Lambda functions
          for each request.

        - **Id** *(string) --* A descriptive or arbitrary ID for the function. This value must be
        unique within the function definition version. Max length is 128 characters with pattern
        ''[a-zA-Z0-9:_-]+''.
    """


_ClientGetFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseTypeDef(
    _ClientGetFunctionDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientGetFunctionDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the function definition version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    function definition version was created.

    - **Definition** *(dict) --* Information on the definition.

      - **DefaultConfig** *(dict) --* The default configuration that applies to all Lambda
      functions in this function definition version. Individual Lambda functions can override these
      settings.

        - **Execution** *(dict) --* Configuration information that specifies how a Lambda function
        runs.

          - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
          Greengrass container (default) or without containerization. Unless your scenario requires
          that you run without containerization, we recommend that you run in a Greengrass
          container. Omit this value to run the Lambda function with the default containerization
          for the group.

          - **RunAs** *(dict) --* Specifies the user and group whose permissions are used when
          running the Lambda function. You can specify one or both values to override the default
          values. We recommend that you avoid running as root unless absolutely necessary to
          minimize the risk of unintended changes or malicious attacks. To run as root, you must
          set ''IsolationMode'' to ''NoContainer'' and update config.json in
          ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

            - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
            function.

            - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
            function.

      - **Functions** *(list) --* A list of Lambda functions in this function definition version.

        - *(dict) --* Information about a Lambda function.

          - **FunctionArn** *(string) --* The ARN of the Lambda function.

          - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.

            - **EncodingType** *(string) --* The expected encoding type of the input payload for
            the function. The default is ''json''.

            - **Environment** *(dict) --* The environment configuration of the function.

              - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access
              the host's /sys folder. Use this when the Lambda function needs to read device
              information from /sys. This setting applies only when you run the Lambda function in
              a Greengrass container.

              - **Execution** *(dict) --* Configuration related to executing the Lambda function

                - **IsolationMode** *(string) --* Specifies whether the Lambda function runs in a
                Greengrass container (default) or without containerization. Unless your scenario
                requires that you run without containerization, we recommend that you run in a
                Greengrass container. Omit this value to run the Lambda function with the default
                containerization for the group.

                - **RunAs** *(dict) --* Specifies the user and group whose permissions are used
                when running the Lambda function. You can specify one or both values to override
                the default values. We recommend that you avoid running as root unless absolutely
                necessary to minimize the risk of unintended changes or malicious attacks. To run
                as root, you must set ''IsolationMode'' to ''NoContainer'' and update config.json
                in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

                  - **Gid** *(integer) --* The group ID whose permissions are used to run a Lambda
                  function.

                  - **Uid** *(integer) --* The user ID whose permissions are used to run a Lambda
                  function.

              - **ResourceAccessPolicies** *(list) --* A list of the resources, with their
              permissions, to which the Lambda function will be granted access. A Lambda function
              can have at most 10 resources. ResourceAccessPolicies apply only when you run the
              Lambda function in a Greengrass container.

                - *(dict) --* A policy used by the function to access a resource.

                  - **Permission** *(string) --* The permissions that the Lambda function has to
                  the resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only).

                  - **ResourceId** *(string) --* The ID of the resource. (This ID is assigned to
                  the resource when you create the resource definiton.)

              - **Variables** *(dict) --* Environment variables for the Lambda function's
              configuration.

                - *(string) --*

                  - *(string) --*

            - **ExecArgs** *(string) --* The execution arguments.

            - **Executable** *(string) --* The name of the function executable.

            - **MemorySize** *(integer) --* The memory size, in KB, which the function requires.
            This setting is not applicable and should be cleared when you run the Lambda function
            without containerization.

            - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function
            is long-lived and starts when the core starts.

            - **Timeout** *(integer) --* The allowed function execution time, after which Lambda
            should terminate the function. This timeout still applies to pinned Lambda functions
            for each request.

          - **Id** *(string) --* A descriptive or arbitrary ID for the function. This value must be
          unique within the function definition version. Max length is 128 characters with pattern
          ''[a-zA-Z0-9:_-]+''.

    - **Id** *(string) --* The ID of the function definition version.

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Version** *(string) --* The version of the function definition version.
    """


_ClientGetGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientGetGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
        "PemEncodedCertificate": str,
    },
    total=False,
)


class ClientGetGroupCertificateAuthorityResponseTypeDef(
    _ClientGetGroupCertificateAuthorityResponseTypeDef
):
    """
    Type definition for `ClientGetGroupCertificateAuthority` `Response`

    - **GroupCertificateAuthorityArn** *(string) --* The ARN of the certificate authority for the
    group.

    - **GroupCertificateAuthorityId** *(string) --* The ID of the certificate authority for the
    group.

    - **PemEncodedCertificate** *(string) --* The PEM encoded certificate for the group.
    """


_ClientGetGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "_ClientGetGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
    },
    total=False,
)


class ClientGetGroupCertificateConfigurationResponseTypeDef(
    _ClientGetGroupCertificateConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetGroupCertificateConfiguration` `Response`

    - **CertificateAuthorityExpiryInMilliseconds** *(string) --* The amount of time remaining
    before the certificate authority expires, in milliseconds.

    - **CertificateExpiryInMilliseconds** *(string) --* The amount of time remaining before the
    certificate expires, in milliseconds.

    - **GroupId** *(string) --* The ID of the group certificate configuration.
    """


_ClientGetGroupResponseTypeDef = TypedDict(
    "_ClientGetGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetGroupResponseTypeDef(_ClientGetGroupResponseTypeDef):
    """
    Type definition for `ClientGetGroup` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientGetGroupVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetGroupVersionResponseDefinitionTypeDef",
    {
        "ConnectorDefinitionVersionArn": str,
        "CoreDefinitionVersionArn": str,
        "DeviceDefinitionVersionArn": str,
        "FunctionDefinitionVersionArn": str,
        "LoggerDefinitionVersionArn": str,
        "ResourceDefinitionVersionArn": str,
        "SubscriptionDefinitionVersionArn": str,
    },
    total=False,
)


class ClientGetGroupVersionResponseDefinitionTypeDef(
    _ClientGetGroupVersionResponseDefinitionTypeDef
):
    """
    Type definition for `ClientGetGroupVersionResponse` `Definition`

    - **ConnectorDefinitionVersionArn** *(string) --* The ARN of the connector definition version
    for this group.

    - **CoreDefinitionVersionArn** *(string) --* The ARN of the core definition version for this
    group.

    - **DeviceDefinitionVersionArn** *(string) --* The ARN of the device definition version for
    this group.

    - **FunctionDefinitionVersionArn** *(string) --* The ARN of the function definition version
    for this group.

    - **LoggerDefinitionVersionArn** *(string) --* The ARN of the logger definition version for
    this group.

    - **ResourceDefinitionVersionArn** *(string) --* The ARN of the resource definition version
    for this group.

    - **SubscriptionDefinitionVersionArn** *(string) --* The ARN of the subscription definition
    version for this group.
    """


_ClientGetGroupVersionResponseTypeDef = TypedDict(
    "_ClientGetGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetGroupVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)


class ClientGetGroupVersionResponseTypeDef(_ClientGetGroupVersionResponseTypeDef):
    """
    Type definition for `ClientGetGroupVersion` `Response`

    - **Arn** *(string) --* The ARN of the group version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the group
    version was created.

    - **Definition** *(dict) --* Information about the group version definition.

      - **ConnectorDefinitionVersionArn** *(string) --* The ARN of the connector definition version
      for this group.

      - **CoreDefinitionVersionArn** *(string) --* The ARN of the core definition version for this
      group.

      - **DeviceDefinitionVersionArn** *(string) --* The ARN of the device definition version for
      this group.

      - **FunctionDefinitionVersionArn** *(string) --* The ARN of the function definition version
      for this group.

      - **LoggerDefinitionVersionArn** *(string) --* The ARN of the logger definition version for
      this group.

      - **ResourceDefinitionVersionArn** *(string) --* The ARN of the resource definition version
      for this group.

      - **SubscriptionDefinitionVersionArn** *(string) --* The ARN of the subscription definition
      version for this group.

    - **Id** *(string) --* The ID of the group that the version is associated with.

    - **Version** *(string) --* The ID of the group version.
    """


_ClientGetLoggerDefinitionResponseTypeDef = TypedDict(
    "_ClientGetLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetLoggerDefinitionResponseTypeDef(
    _ClientGetLoggerDefinitionResponseTypeDef
):
    """
    Type definition for `ClientGetLoggerDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef = TypedDict(
    "_ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef",
    {"Component": str, "Id": str, "Level": str, "Space": int, "Type": str},
    total=False,
)


class ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef(
    _ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef
):
    """
    Type definition for `ClientGetLoggerDefinitionVersionResponseDefinition` `Loggers`

    - **Component** *(string) --* The component that will be subject to logging.

    - **Id** *(string) --* A descriptive or arbitrary ID for the logger. This value must be
    unique within the logger definition version. Max length is 128 characters with pattern
    ''[a-zA-Z0-9:_-]+''.

    - **Level** *(string) --* The level of the logs.

    - **Space** *(integer) --* The amount of file space, in KB, to use if the local file
    system is used for logging purposes.

    - **Type** *(string) --* The type of log output which will be used.
    """


_ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef",
    {"Loggers": List[ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef]},
    total=False,
)


class ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef
):
    """
    Type definition for `ClientGetLoggerDefinitionVersionResponse` `Definition`

    - **Loggers** *(list) --* A list of loggers.

      - *(dict) --* Information about a logger

        - **Component** *(string) --* The component that will be subject to logging.

        - **Id** *(string) --* A descriptive or arbitrary ID for the logger. This value must be
        unique within the logger definition version. Max length is 128 characters with pattern
        ''[a-zA-Z0-9:_-]+''.

        - **Level** *(string) --* The level of the logs.

        - **Space** *(integer) --* The amount of file space, in KB, to use if the local file
        system is used for logging purposes.

        - **Type** *(string) --* The type of log output which will be used.
    """


_ClientGetLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)


class ClientGetLoggerDefinitionVersionResponseTypeDef(
    _ClientGetLoggerDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientGetLoggerDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the logger definition version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    logger definition version was created.

    - **Definition** *(dict) --* Information about the logger definition version.

      - **Loggers** *(list) --* A list of loggers.

        - *(dict) --* Information about a logger

          - **Component** *(string) --* The component that will be subject to logging.

          - **Id** *(string) --* A descriptive or arbitrary ID for the logger. This value must be
          unique within the logger definition version. Max length is 128 characters with pattern
          ''[a-zA-Z0-9:_-]+''.

          - **Level** *(string) --* The level of the logs.

          - **Space** *(integer) --* The amount of file space, in KB, to use if the local file
          system is used for logging purposes.

          - **Type** *(string) --* The type of log output which will be used.

    - **Id** *(string) --* The ID of the logger definition version.

    - **Version** *(string) --* The version of the logger definition version.
    """


_ClientGetResourceDefinitionResponseTypeDef = TypedDict(
    "_ClientGetResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetResourceDefinitionResponseTypeDef(
    _ClientGetResourceDefinitionResponseTypeDef
):
    """
    Type definition for `ClientGetResourceDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": Dict[str, Any],
        "LocalVolumeResourceData": Dict[str, Any],
        "S3MachineLearningModelResourceData": Dict[str, Any],
        "SageMakerMachineLearningModelResourceData": Dict[str, Any],
        "SecretsManagerSecretResourceData": Dict[str, Any],
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef
):
    """
    Type definition for `ClientGetResourceDefinitionVersionResponseDefinitionResources` `ResourceDataContainer`

    - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device
    resource.

      - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.

        - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically
        adds the specified Linux OS group owner of the resource to the Lambda process
        privileges. Thus the Lambda process will have the file access permissions of the
        added Linux group.

        - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will
        be added to the Lambda process. This field is optional.

      - **SourcePath** *(string) --* The local absolute path of the device resource. The
      source path for a device resource can refer only to a character device or block
      device under ''/dev''.

    - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume
    resource.

      - **DestinationPath** *(string) --* The absolute local path of the resource inside
      the Lambda environment.

      - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group
      privileges for the Lambda process. This field is optional.

        - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically
        adds the specified Linux OS group owner of the resource to the Lambda process
        privileges. Thus the Lambda process will have the file access permissions of the
        added Linux group.

        - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will
        be added to the Lambda process. This field is optional.

      - **SourcePath** *(string) --* The local absolute path of the volume resource on the
      host. The source path for a volume resource type cannot start with ''/sys''.

    - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon
    S3 machine learning resource.

      - **DestinationPath** *(string) --* The absolute local path of the resource inside
      the Lambda environment.

      - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model
      package must be in tar.gz or .zip format.

    - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an
    Amazon SageMaker machine learning resource.

      - **DestinationPath** *(string) --* The absolute local path of the resource inside
      the Lambda environment.

      - **SageMakerJobArn** *(string) --* The ARN of the Amazon SageMaker training job that
      represents the source model.

    - **SecretsManagerSecretResourceData** *(dict) --* Attributes that define a secret
    resource, which references a secret from AWS Secrets Manager.

      - **ARN** *(string) --* The ARN of the Secrets Manager secret to make available on
      the core. The value of the secret's latest version (represented by the ''AWSCURRENT''
      staging label) is included by default.

      - **AdditionalStagingLabelsToDownload** *(list) --* Optional. The staging labels
      whose values you want to make available on the core, in addition to ''AWSCURRENT''.

        - *(string) --*
    """


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef,
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef
):
    """
    Type definition for `ClientGetResourceDefinitionVersionResponseDefinition` `Resources`

    - **Id** *(string) --* The resource ID, used to refer to a resource in the Lambda
    function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
    This must be unique within a Greengrass group.

    - **Name** *(string) --* The descriptive resource name, which is displayed on the AWS IoT
    Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This must
    be unique within a Greengrass group.

    - **ResourceDataContainer** *(dict) --* A container of data for all resource types.

      - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device
      resource.

        - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.

          - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically
          adds the specified Linux OS group owner of the resource to the Lambda process
          privileges. Thus the Lambda process will have the file access permissions of the
          added Linux group.

          - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will
          be added to the Lambda process. This field is optional.

        - **SourcePath** *(string) --* The local absolute path of the device resource. The
        source path for a device resource can refer only to a character device or block
        device under ''/dev''.

      - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume
      resource.

        - **DestinationPath** *(string) --* The absolute local path of the resource inside
        the Lambda environment.

        - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group
        privileges for the Lambda process. This field is optional.

          - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically
          adds the specified Linux OS group owner of the resource to the Lambda process
          privileges. Thus the Lambda process will have the file access permissions of the
          added Linux group.

          - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will
          be added to the Lambda process. This field is optional.

        - **SourcePath** *(string) --* The local absolute path of the volume resource on the
        host. The source path for a volume resource type cannot start with ''/sys''.

      - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon
      S3 machine learning resource.

        - **DestinationPath** *(string) --* The absolute local path of the resource inside
        the Lambda environment.

        - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model
        package must be in tar.gz or .zip format.

      - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an
      Amazon SageMaker machine learning resource.

        - **DestinationPath** *(string) --* The absolute local path of the resource inside
        the Lambda environment.

        - **SageMakerJobArn** *(string) --* The ARN of the Amazon SageMaker training job that
        represents the source model.

      - **SecretsManagerSecretResourceData** *(dict) --* Attributes that define a secret
      resource, which references a secret from AWS Secrets Manager.

        - **ARN** *(string) --* The ARN of the Secrets Manager secret to make available on
        the core. The value of the secret's latest version (represented by the ''AWSCURRENT''
        staging label) is included by default.

        - **AdditionalStagingLabelsToDownload** *(list) --* Optional. The staging labels
        whose values you want to make available on the core, in addition to ''AWSCURRENT''.

          - *(string) --*
    """


_ClientGetResourceDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionTypeDef",
    {
        "Resources": List[
            ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef
        ]
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionTypeDef
):
    """
    Type definition for `ClientGetResourceDefinitionVersionResponse` `Definition`

    - **Resources** *(list) --* A list of resources.

      - *(dict) --* Information about a resource.

        - **Id** *(string) --* The resource ID, used to refer to a resource in the Lambda
        function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
        This must be unique within a Greengrass group.

        - **Name** *(string) --* The descriptive resource name, which is displayed on the AWS IoT
        Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This must
        be unique within a Greengrass group.

        - **ResourceDataContainer** *(dict) --* A container of data for all resource types.

          - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device
          resource.

            - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.

              - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically
              adds the specified Linux OS group owner of the resource to the Lambda process
              privileges. Thus the Lambda process will have the file access permissions of the
              added Linux group.

              - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will
              be added to the Lambda process. This field is optional.

            - **SourcePath** *(string) --* The local absolute path of the device resource. The
            source path for a device resource can refer only to a character device or block
            device under ''/dev''.

          - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume
          resource.

            - **DestinationPath** *(string) --* The absolute local path of the resource inside
            the Lambda environment.

            - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group
            privileges for the Lambda process. This field is optional.

              - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically
              adds the specified Linux OS group owner of the resource to the Lambda process
              privileges. Thus the Lambda process will have the file access permissions of the
              added Linux group.

              - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will
              be added to the Lambda process. This field is optional.

            - **SourcePath** *(string) --* The local absolute path of the volume resource on the
            host. The source path for a volume resource type cannot start with ''/sys''.

          - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon
          S3 machine learning resource.

            - **DestinationPath** *(string) --* The absolute local path of the resource inside
            the Lambda environment.

            - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model
            package must be in tar.gz or .zip format.

          - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an
          Amazon SageMaker machine learning resource.

            - **DestinationPath** *(string) --* The absolute local path of the resource inside
            the Lambda environment.

            - **SageMakerJobArn** *(string) --* The ARN of the Amazon SageMaker training job that
            represents the source model.

          - **SecretsManagerSecretResourceData** *(dict) --* Attributes that define a secret
          resource, which references a secret from AWS Secrets Manager.

            - **ARN** *(string) --* The ARN of the Secrets Manager secret to make available on
            the core. The value of the secret's latest version (represented by the ''AWSCURRENT''
            staging label) is included by default.

            - **AdditionalStagingLabelsToDownload** *(list) --* Optional. The staging labels
            whose values you want to make available on the core, in addition to ''AWSCURRENT''.

              - *(string) --*
    """


_ClientGetResourceDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetResourceDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseTypeDef(
    _ClientGetResourceDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientGetResourceDefinitionVersion` `Response`

    - **Arn** *(string) --* Arn of the resource definition version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    resource definition version was created.

    - **Definition** *(dict) --* Information about the definition.

      - **Resources** *(list) --* A list of resources.

        - *(dict) --* Information about a resource.

          - **Id** *(string) --* The resource ID, used to refer to a resource in the Lambda
          function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
          This must be unique within a Greengrass group.

          - **Name** *(string) --* The descriptive resource name, which is displayed on the AWS IoT
          Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This must
          be unique within a Greengrass group.

          - **ResourceDataContainer** *(dict) --* A container of data for all resource types.

            - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device
            resource.

              - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.

                - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically
                adds the specified Linux OS group owner of the resource to the Lambda process
                privileges. Thus the Lambda process will have the file access permissions of the
                added Linux group.

                - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will
                be added to the Lambda process. This field is optional.

              - **SourcePath** *(string) --* The local absolute path of the device resource. The
              source path for a device resource can refer only to a character device or block
              device under ''/dev''.

            - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume
            resource.

              - **DestinationPath** *(string) --* The absolute local path of the resource inside
              the Lambda environment.

              - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group
              privileges for the Lambda process. This field is optional.

                - **AutoAddGroupOwner** *(boolean) --* If true, AWS IoT Greengrass automatically
                adds the specified Linux OS group owner of the resource to the Lambda process
                privileges. Thus the Lambda process will have the file access permissions of the
                added Linux group.

                - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will
                be added to the Lambda process. This field is optional.

              - **SourcePath** *(string) --* The local absolute path of the volume resource on the
              host. The source path for a volume resource type cannot start with ''/sys''.

            - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an Amazon
            S3 machine learning resource.

              - **DestinationPath** *(string) --* The absolute local path of the resource inside
              the Lambda environment.

              - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model
              package must be in tar.gz or .zip format.

            - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an
            Amazon SageMaker machine learning resource.

              - **DestinationPath** *(string) --* The absolute local path of the resource inside
              the Lambda environment.

              - **SageMakerJobArn** *(string) --* The ARN of the Amazon SageMaker training job that
              represents the source model.

            - **SecretsManagerSecretResourceData** *(dict) --* Attributes that define a secret
            resource, which references a secret from AWS Secrets Manager.

              - **ARN** *(string) --* The ARN of the Secrets Manager secret to make available on
              the core. The value of the secret's latest version (represented by the ''AWSCURRENT''
              staging label) is included by default.

              - **AdditionalStagingLabelsToDownload** *(list) --* Optional. The staging labels
              whose values you want to make available on the core, in addition to ''AWSCURRENT''.

                - *(string) --*

    - **Id** *(string) --* The ID of the resource definition version.

    - **Version** *(string) --* The version of the resource definition version.
    """


_ClientGetServiceRoleForAccountResponseTypeDef = TypedDict(
    "_ClientGetServiceRoleForAccountResponseTypeDef",
    {"AssociatedAt": str, "RoleArn": str},
    total=False,
)


class ClientGetServiceRoleForAccountResponseTypeDef(
    _ClientGetServiceRoleForAccountResponseTypeDef
):
    """
    Type definition for `ClientGetServiceRoleForAccount` `Response`

    - **AssociatedAt** *(string) --* The time when the service role was associated with the account.

    - **RoleArn** *(string) --* The ARN of the role which is associated with the account.
    """


_ClientGetSubscriptionDefinitionResponseTypeDef = TypedDict(
    "_ClientGetSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetSubscriptionDefinitionResponseTypeDef(
    _ClientGetSubscriptionDefinitionResponseTypeDef
):
    """
    Type definition for `ClientGetSubscriptionDefinition` `Response`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef = TypedDict(
    "_ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
    total=False,
)


class ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef(
    _ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef
):
    """
    Type definition for `ClientGetSubscriptionDefinitionVersionResponseDefinition` `Subscriptions`

    - **Id** *(string) --* A descriptive or arbitrary ID for the subscription. This value
    must be unique within the subscription definition version. Max length is 128 characters
    with pattern ''[a-zA-Z0-9:_-]+''.

    - **Source** *(string) --* The source of the subscription. Can be a thing ARN, a Lambda
    function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
    'GGShadowService'.

    - **Subject** *(string) --* The MQTT topic used to route the message.

    - **Target** *(string) --* Where the message is sent to. Can be a thing ARN, a Lambda
    function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
    'GGShadowService'.
    """


_ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef",
    {
        "Subscriptions": List[
            ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef
        ]
    },
    total=False,
)


class ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef
):
    """
    Type definition for `ClientGetSubscriptionDefinitionVersionResponse` `Definition`

    - **Subscriptions** *(list) --* A list of subscriptions.

      - *(dict) --* Information about a subscription.

        - **Id** *(string) --* A descriptive or arbitrary ID for the subscription. This value
        must be unique within the subscription definition version. Max length is 128 characters
        with pattern ''[a-zA-Z0-9:_-]+''.

        - **Source** *(string) --* The source of the subscription. Can be a thing ARN, a Lambda
        function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
        'GGShadowService'.

        - **Subject** *(string) --* The MQTT topic used to route the message.

        - **Target** *(string) --* Where the message is sent to. Can be a thing ARN, a Lambda
        function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
        'GGShadowService'.
    """


_ClientGetSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetSubscriptionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)


class ClientGetSubscriptionDefinitionVersionResponseTypeDef(
    _ClientGetSubscriptionDefinitionVersionResponseTypeDef
):
    """
    Type definition for `ClientGetSubscriptionDefinitionVersion` `Response`

    - **Arn** *(string) --* The ARN of the subscription definition version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    subscription definition version was created.

    - **Definition** *(dict) --* Information about the subscription definition version.

      - **Subscriptions** *(list) --* A list of subscriptions.

        - *(dict) --* Information about a subscription.

          - **Id** *(string) --* A descriptive or arbitrary ID for the subscription. This value
          must be unique within the subscription definition version. Max length is 128 characters
          with pattern ''[a-zA-Z0-9:_-]+''.

          - **Source** *(string) --* The source of the subscription. Can be a thing ARN, a Lambda
          function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
          'GGShadowService'.

          - **Subject** *(string) --* The MQTT topic used to route the message.

          - **Target** *(string) --* Where the message is sent to. Can be a thing ARN, a Lambda
          function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
          'GGShadowService'.

    - **Id** *(string) --* The ID of the subscription definition version.

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Version** *(string) --* The version of the subscription definition version.
    """


_ClientListBulkDeploymentDetailedReportsResponseTypeDef = TypedDict(
    "_ClientListBulkDeploymentDetailedReportsResponseTypeDef",
    {"Deployments": List[Any], "NextToken": str},
    total=False,
)


class ClientListBulkDeploymentDetailedReportsResponseTypeDef(
    _ClientListBulkDeploymentDetailedReportsResponseTypeDef
):
    """
    Type definition for `ClientListBulkDeploymentDetailedReports` `Response`

    - **Deployments** *(list) --* A list of the individual group deployments in the bulk deployment
    operation.

      - *(dict) --* Information about an individual group deployment in a bulk deployment operation.

        - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.

        - **DeploymentArn** *(string) --* The ARN of the group deployment.

        - **DeploymentId** *(string) --* The ID of the group deployment.

        - **DeploymentStatus** *(string) --* The current status of the group deployment:
        ''InProgress'', ''Building'', ''Success'', or ''Failure''.

        - **DeploymentType** *(string) --* The type of the deployment.

        - **ErrorDetails** *(list) --* Details about the error.

          - *(dict) --* Details about the error.

            - **DetailedErrorCode** *(string) --* A detailed error code.

            - **DetailedErrorMessage** *(string) --* A detailed error message.

        - **ErrorMessage** *(string) --* The error message for a failed deployment

        - **GroupArn** *(string) --* The ARN of the Greengrass group.

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.
    """


_ClientListBulkDeploymentsResponseTypeDef = TypedDict(
    "_ClientListBulkDeploymentsResponseTypeDef",
    {"BulkDeployments": List[Dict], "NextToken": str},
    total=False,
)


class ClientListBulkDeploymentsResponseTypeDef(
    _ClientListBulkDeploymentsResponseTypeDef
):
    """
    Type definition for `ClientListBulkDeployments` `Response`

    - **BulkDeployments** *(list) --* A list of bulk deployments.

      - *(dict) --* Information about a bulk deployment. You cannot start a new bulk deployment
      while another one is still running or in a non-terminal state.

        - **BulkDeploymentArn** *(string) --* The ARN of the bulk deployment.

        - **BulkDeploymentId** *(string) --* The ID of the bulk deployment.

        - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.
    """


_ClientListConnectorDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListConnectorDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListConnectorDefinitionVersionsResponseVersionsTypeDef(
    _ClientListConnectorDefinitionVersionsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListConnectorDefinitionVersionsResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ClientListConnectorDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListConnectorDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListConnectorDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListConnectorDefinitionVersionsResponseTypeDef(
    _ClientListConnectorDefinitionVersionsResponseTypeDef
):
    """
    Type definition for `ClientListConnectorDefinitionVersions` `Response`

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ClientListConnectorDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListConnectorDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListConnectorDefinitionsResponseDefinitionsTypeDef(
    _ClientListConnectorDefinitionsResponseDefinitionsTypeDef
):
    """
    Type definition for `ClientListConnectorDefinitionsResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientListConnectorDefinitionsResponseTypeDef = TypedDict(
    "_ClientListConnectorDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListConnectorDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListConnectorDefinitionsResponseTypeDef(
    _ClientListConnectorDefinitionsResponseTypeDef
):
    """
    Type definition for `ClientListConnectorDefinitions` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.
    """


_ClientListCoreDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListCoreDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListCoreDefinitionVersionsResponseVersionsTypeDef(
    _ClientListCoreDefinitionVersionsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListCoreDefinitionVersionsResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ClientListCoreDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListCoreDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListCoreDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListCoreDefinitionVersionsResponseTypeDef(
    _ClientListCoreDefinitionVersionsResponseTypeDef
):
    """
    Type definition for `ClientListCoreDefinitionVersions` `Response`

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ClientListCoreDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListCoreDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListCoreDefinitionsResponseDefinitionsTypeDef(
    _ClientListCoreDefinitionsResponseDefinitionsTypeDef
):
    """
    Type definition for `ClientListCoreDefinitionsResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientListCoreDefinitionsResponseTypeDef = TypedDict(
    "_ClientListCoreDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListCoreDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListCoreDefinitionsResponseTypeDef(
    _ClientListCoreDefinitionsResponseTypeDef
):
    """
    Type definition for `ClientListCoreDefinitions` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.
    """


_ClientListDeploymentsResponseDeploymentsTypeDef = TypedDict(
    "_ClientListDeploymentsResponseDeploymentsTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentType": str,
        "GroupArn": str,
    },
    total=False,
)


class ClientListDeploymentsResponseDeploymentsTypeDef(
    _ClientListDeploymentsResponseDeploymentsTypeDef
):
    """
    Type definition for `ClientListDeploymentsResponse` `Deployments`

    - **CreatedAt** *(string) --* The time, in milliseconds since the epoch, when the
    deployment was created.

    - **DeploymentArn** *(string) --* The ARN of the deployment.

    - **DeploymentId** *(string) --* The ID of the deployment.

    - **DeploymentType** *(string) --* The type of the deployment.

    - **GroupArn** *(string) --* The ARN of the group for this deployment.
    """


_ClientListDeploymentsResponseTypeDef = TypedDict(
    "_ClientListDeploymentsResponseTypeDef",
    {
        "Deployments": List[ClientListDeploymentsResponseDeploymentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListDeploymentsResponseTypeDef(_ClientListDeploymentsResponseTypeDef):
    """
    Type definition for `ClientListDeployments` `Response`

    - **Deployments** *(list) --* A list of deployments for the requested groups.

      - *(dict) --* Information about a deployment.

        - **CreatedAt** *(string) --* The time, in milliseconds since the epoch, when the
        deployment was created.

        - **DeploymentArn** *(string) --* The ARN of the deployment.

        - **DeploymentId** *(string) --* The ID of the deployment.

        - **DeploymentType** *(string) --* The type of the deployment.

        - **GroupArn** *(string) --* The ARN of the group for this deployment.

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.
    """


_ClientListDeviceDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListDeviceDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListDeviceDefinitionVersionsResponseVersionsTypeDef(
    _ClientListDeviceDefinitionVersionsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListDeviceDefinitionVersionsResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ClientListDeviceDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListDeviceDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListDeviceDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListDeviceDefinitionVersionsResponseTypeDef(
    _ClientListDeviceDefinitionVersionsResponseTypeDef
):
    """
    Type definition for `ClientListDeviceDefinitionVersions` `Response`

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ClientListDeviceDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListDeviceDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListDeviceDefinitionsResponseDefinitionsTypeDef(
    _ClientListDeviceDefinitionsResponseDefinitionsTypeDef
):
    """
    Type definition for `ClientListDeviceDefinitionsResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientListDeviceDefinitionsResponseTypeDef = TypedDict(
    "_ClientListDeviceDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListDeviceDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListDeviceDefinitionsResponseTypeDef(
    _ClientListDeviceDefinitionsResponseTypeDef
):
    """
    Type definition for `ClientListDeviceDefinitions` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.
    """


_ClientListFunctionDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListFunctionDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListFunctionDefinitionVersionsResponseVersionsTypeDef(
    _ClientListFunctionDefinitionVersionsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListFunctionDefinitionVersionsResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ClientListFunctionDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListFunctionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListFunctionDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListFunctionDefinitionVersionsResponseTypeDef(
    _ClientListFunctionDefinitionVersionsResponseTypeDef
):
    """
    Type definition for `ClientListFunctionDefinitionVersions` `Response`

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ClientListGroupCertificateAuthoritiesResponseTypeDef = TypedDict(
    "_ClientListGroupCertificateAuthoritiesResponseTypeDef",
    {"GroupCertificateAuthorities": List[Any]},
    total=False,
)


class ClientListGroupCertificateAuthoritiesResponseTypeDef(
    _ClientListGroupCertificateAuthoritiesResponseTypeDef
):
    """
    Type definition for `ClientListGroupCertificateAuthorities` `Response`

    - **GroupCertificateAuthorities** *(list) --* A list of certificate authorities associated with
    the group.

      - *(dict) --* Information about a certificate authority for a group.

        - **GroupCertificateAuthorityArn** *(string) --* The ARN of the certificate authority for
        the group.

        - **GroupCertificateAuthorityId** *(string) --* The ID of the certificate authority for the
        group.
    """


_ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientListGroupsResponseGroupsTypeDef(_ClientListGroupsResponseGroupsTypeDef):
    """
    Type definition for `ClientListGroupsResponse` `Groups`

    - **Arn** *(string) --* The ARN of the group.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    group was created.

    - **Id** *(string) --* The ID of the group.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the group was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the group.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    group.

    - **Name** *(string) --* The name of the group.
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    Type definition for `ClientListGroups` `Response`

    - **Groups** *(list) --* Information about a group.

      - *(dict) --* Information about a group.

        - **Arn** *(string) --* The ARN of the group.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        group was created.

        - **Id** *(string) --* The ID of the group.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the group was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the group.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        group.

        - **Name** *(string) --* The name of the group.

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.
    """


_ClientListLoggerDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListLoggerDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListLoggerDefinitionVersionsResponseVersionsTypeDef(
    _ClientListLoggerDefinitionVersionsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListLoggerDefinitionVersionsResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ClientListLoggerDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListLoggerDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListLoggerDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListLoggerDefinitionVersionsResponseTypeDef(
    _ClientListLoggerDefinitionVersionsResponseTypeDef
):
    """
    Type definition for `ClientListLoggerDefinitionVersions` `Response`

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ClientListLoggerDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListLoggerDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListLoggerDefinitionsResponseDefinitionsTypeDef(
    _ClientListLoggerDefinitionsResponseDefinitionsTypeDef
):
    """
    Type definition for `ClientListLoggerDefinitionsResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientListLoggerDefinitionsResponseTypeDef = TypedDict(
    "_ClientListLoggerDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListLoggerDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListLoggerDefinitionsResponseTypeDef(
    _ClientListLoggerDefinitionsResponseTypeDef
):
    """
    Type definition for `ClientListLoggerDefinitions` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.
    """


_ClientListResourceDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListResourceDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListResourceDefinitionVersionsResponseVersionsTypeDef(
    _ClientListResourceDefinitionVersionsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListResourceDefinitionVersionsResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ClientListResourceDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListResourceDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListResourceDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListResourceDefinitionVersionsResponseTypeDef(
    _ClientListResourceDefinitionVersionsResponseTypeDef
):
    """
    Type definition for `ClientListResourceDefinitionVersions` `Response`

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ClientListResourceDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListResourceDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListResourceDefinitionsResponseDefinitionsTypeDef(
    _ClientListResourceDefinitionsResponseDefinitionsTypeDef
):
    """
    Type definition for `ClientListResourceDefinitionsResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientListResourceDefinitionsResponseTypeDef = TypedDict(
    "_ClientListResourceDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListResourceDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourceDefinitionsResponseTypeDef(
    _ClientListResourceDefinitionsResponseTypeDef
):
    """
    Type definition for `ClientListResourceDefinitions` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.
    """


_ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef(
    _ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListSubscriptionDefinitionVersionsResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ClientListSubscriptionDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListSubscriptionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[
            ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef
        ],
    },
    total=False,
)


class ClientListSubscriptionDefinitionVersionsResponseTypeDef(
    _ClientListSubscriptionDefinitionVersionsResponseTypeDef
):
    """
    Type definition for `ClientListSubscriptionDefinitionVersions` `Response`

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef(
    _ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef
):
    """
    Type definition for `ClientListSubscriptionDefinitionsResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ClientListSubscriptionDefinitionsResponseTypeDef = TypedDict(
    "_ClientListSubscriptionDefinitionsResponseTypeDef",
    {
        "Definitions": List[
            ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSubscriptionDefinitionsResponseTypeDef(
    _ClientListSubscriptionDefinitionsResponseTypeDef
):
    """
    Type definition for `ClientListSubscriptionDefinitions` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --* The token for the next set of results, or ''null'' if there are
    no additional results.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(dict) --* The key-value pair for the resource tag.

      - *(string) --*

        - *(string) --*
    """


_ClientResetDeploymentsResponseTypeDef = TypedDict(
    "_ClientResetDeploymentsResponseTypeDef",
    {"DeploymentArn": str, "DeploymentId": str},
    total=False,
)


class ClientResetDeploymentsResponseTypeDef(_ClientResetDeploymentsResponseTypeDef):
    """
    Type definition for `ClientResetDeployments` `Response`

    - **DeploymentArn** *(string) --* The ARN of the deployment.

    - **DeploymentId** *(string) --* The ID of the deployment.
    """


_ClientStartBulkDeploymentResponseTypeDef = TypedDict(
    "_ClientStartBulkDeploymentResponseTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str},
    total=False,
)


class ClientStartBulkDeploymentResponseTypeDef(
    _ClientStartBulkDeploymentResponseTypeDef
):
    """
    Type definition for `ClientStartBulkDeployment` `Response`

    - **BulkDeploymentArn** *(string) --* The ARN of the bulk deployment.

    - **BulkDeploymentId** *(string) --* The ID of the bulk deployment.
    """


_ClientUpdateConnectivityInfoConnectivityInfoTypeDef = TypedDict(
    "_ClientUpdateConnectivityInfoConnectivityInfoTypeDef",
    {"HostAddress": str, "Id": str, "Metadata": str, "PortNumber": int},
    total=False,
)


class ClientUpdateConnectivityInfoConnectivityInfoTypeDef(
    _ClientUpdateConnectivityInfoConnectivityInfoTypeDef
):
    """
    Type definition for `ClientUpdateConnectivityInfo` `ConnectivityInfo`

    - **HostAddress** *(string) --* The endpoint for the Greengrass core. Can be an IP address or
    DNS.

    - **Id** *(string) --* The ID of the connectivity information.

    - **Metadata** *(string) --* Metadata for this endpoint.

    - **PortNumber** *(integer) --* The port of the Greengrass core. Usually 8883.
    """


_ClientUpdateConnectivityInfoResponseTypeDef = TypedDict(
    "_ClientUpdateConnectivityInfoResponseTypeDef",
    {"Message": str, "Version": str},
    total=False,
)


class ClientUpdateConnectivityInfoResponseTypeDef(
    _ClientUpdateConnectivityInfoResponseTypeDef
):
    """
    Type definition for `ClientUpdateConnectivityInfo` `Response`

    - **Message** *(string) --* A message about the connectivity info update request.

    - **Version** *(string) --* The new version of the connectivity info.
    """


_ClientUpdateGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
    },
    total=False,
)


class ClientUpdateGroupCertificateConfigurationResponseTypeDef(
    _ClientUpdateGroupCertificateConfigurationResponseTypeDef
):
    """
    Type definition for `ClientUpdateGroupCertificateConfiguration` `Response`

    - **CertificateAuthorityExpiryInMilliseconds** *(string) --* The amount of time remaining
    before the certificate authority expires, in milliseconds.

    - **CertificateExpiryInMilliseconds** *(string) --* The amount of time remaining before the
    certificate expires, in milliseconds.

    - **GroupId** *(string) --* The ID of the group certificate configuration.
    """


_ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef(
    _ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBulkDeploymentDetailedReportsPaginate` `PaginationConfig`

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


_ListBulkDeploymentDetailedReportsPaginateResponseTypeDef = TypedDict(
    "_ListBulkDeploymentDetailedReportsPaginateResponseTypeDef",
    {"Deployments": List[Any]},
    total=False,
)


class ListBulkDeploymentDetailedReportsPaginateResponseTypeDef(
    _ListBulkDeploymentDetailedReportsPaginateResponseTypeDef
):
    """
    Type definition for `ListBulkDeploymentDetailedReportsPaginate` `Response`

    - **Deployments** *(list) --* A list of the individual group deployments in the bulk deployment
    operation.

      - *(dict) --* Information about an individual group deployment in a bulk deployment operation.

        - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.

        - **DeploymentArn** *(string) --* The ARN of the group deployment.

        - **DeploymentId** *(string) --* The ID of the group deployment.

        - **DeploymentStatus** *(string) --* The current status of the group deployment:
        ''InProgress'', ''Building'', ''Success'', or ''Failure''.

        - **DeploymentType** *(string) --* The type of the deployment.

        - **ErrorDetails** *(list) --* Details about the error.

          - *(dict) --* Details about the error.

            - **DetailedErrorCode** *(string) --* A detailed error code.

            - **DetailedErrorMessage** *(string) --* A detailed error message.

        - **ErrorMessage** *(string) --* The error message for a failed deployment

        - **GroupArn** *(string) --* The ARN of the Greengrass group.
    """


_ListBulkDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBulkDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBulkDeploymentsPaginatePaginationConfigTypeDef(
    _ListBulkDeploymentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBulkDeploymentsPaginate` `PaginationConfig`

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


_ListBulkDeploymentsPaginateResponseTypeDef = TypedDict(
    "_ListBulkDeploymentsPaginateResponseTypeDef",
    {"BulkDeployments": List[Dict]},
    total=False,
)


class ListBulkDeploymentsPaginateResponseTypeDef(
    _ListBulkDeploymentsPaginateResponseTypeDef
):
    """
    Type definition for `ListBulkDeploymentsPaginate` `Response`

    - **BulkDeployments** *(list) --* A list of bulk deployments.

      - *(dict) --* Information about a bulk deployment. You cannot start a new bulk deployment
      while another one is still running or in a non-terminal state.

        - **BulkDeploymentArn** *(string) --* The ARN of the bulk deployment.

        - **BulkDeploymentId** *(string) --* The ID of the bulk deployment.

        - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.
    """


_ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListConnectorDefinitionVersionsPaginate` `PaginationConfig`

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


_ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListConnectorDefinitionVersionsPaginateResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ListConnectorDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListConnectorDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListConnectorDefinitionVersionsPaginateResponseTypeDef(
    _ListConnectorDefinitionVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListConnectorDefinitionVersionsPaginate` `Response`

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ListConnectorDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConnectorDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConnectorDefinitionsPaginatePaginationConfigTypeDef(
    _ListConnectorDefinitionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListConnectorDefinitionsPaginate` `PaginationConfig`

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


_ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    Type definition for `ListConnectorDefinitionsPaginateResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ListConnectorDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListConnectorDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListConnectorDefinitionsPaginateResponseTypeDef(
    _ListConnectorDefinitionsPaginateResponseTypeDef
):
    """
    Type definition for `ListConnectorDefinitionsPaginate` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*
    """


_ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCoreDefinitionVersionsPaginate` `PaginationConfig`

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


_ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListCoreDefinitionVersionsPaginateResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ListCoreDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListCoreDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListCoreDefinitionVersionsPaginateResponseTypeDef(
    _ListCoreDefinitionVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListCoreDefinitionVersionsPaginate` `Response`

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ListCoreDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCoreDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCoreDefinitionsPaginatePaginationConfigTypeDef(
    _ListCoreDefinitionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCoreDefinitionsPaginate` `PaginationConfig`

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


_ListCoreDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListCoreDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListCoreDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListCoreDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    Type definition for `ListCoreDefinitionsPaginateResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ListCoreDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListCoreDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListCoreDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListCoreDefinitionsPaginateResponseTypeDef(
    _ListCoreDefinitionsPaginateResponseTypeDef
):
    """
    Type definition for `ListCoreDefinitionsPaginate` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*
    """


_ListDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeploymentsPaginatePaginationConfigTypeDef(
    _ListDeploymentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeploymentsPaginate` `PaginationConfig`

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


_ListDeploymentsPaginateResponseDeploymentsTypeDef = TypedDict(
    "_ListDeploymentsPaginateResponseDeploymentsTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentType": str,
        "GroupArn": str,
    },
    total=False,
)


class ListDeploymentsPaginateResponseDeploymentsTypeDef(
    _ListDeploymentsPaginateResponseDeploymentsTypeDef
):
    """
    Type definition for `ListDeploymentsPaginateResponse` `Deployments`

    - **CreatedAt** *(string) --* The time, in milliseconds since the epoch, when the
    deployment was created.

    - **DeploymentArn** *(string) --* The ARN of the deployment.

    - **DeploymentId** *(string) --* The ID of the deployment.

    - **DeploymentType** *(string) --* The type of the deployment.

    - **GroupArn** *(string) --* The ARN of the group for this deployment.
    """


_ListDeploymentsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentsPaginateResponseTypeDef",
    {"Deployments": List[ListDeploymentsPaginateResponseDeploymentsTypeDef]},
    total=False,
)


class ListDeploymentsPaginateResponseTypeDef(_ListDeploymentsPaginateResponseTypeDef):
    """
    Type definition for `ListDeploymentsPaginate` `Response`

    - **Deployments** *(list) --* A list of deployments for the requested groups.

      - *(dict) --* Information about a deployment.

        - **CreatedAt** *(string) --* The time, in milliseconds since the epoch, when the
        deployment was created.

        - **DeploymentArn** *(string) --* The ARN of the deployment.

        - **DeploymentId** *(string) --* The ID of the deployment.

        - **DeploymentType** *(string) --* The type of the deployment.

        - **GroupArn** *(string) --* The ARN of the group for this deployment.
    """


_ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeviceDefinitionVersionsPaginate` `PaginationConfig`

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


_ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListDeviceDefinitionVersionsPaginateResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ListDeviceDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListDeviceDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListDeviceDefinitionVersionsPaginateResponseTypeDef(
    _ListDeviceDefinitionVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListDeviceDefinitionVersionsPaginate` `Response`

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ListDeviceDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeviceDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeviceDefinitionsPaginatePaginationConfigTypeDef(
    _ListDeviceDefinitionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeviceDefinitionsPaginate` `PaginationConfig`

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


_ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    Type definition for `ListDeviceDefinitionsPaginateResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ListDeviceDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListDeviceDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListDeviceDefinitionsPaginateResponseTypeDef(
    _ListDeviceDefinitionsPaginateResponseTypeDef
):
    """
    Type definition for `ListDeviceDefinitionsPaginate` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*
    """


_ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFunctionDefinitionVersionsPaginate` `PaginationConfig`

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


_ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListFunctionDefinitionVersionsPaginateResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ListFunctionDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListFunctionDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListFunctionDefinitionVersionsPaginateResponseTypeDef(
    _ListFunctionDefinitionVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListFunctionDefinitionVersionsPaginate` `Response`

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ListFunctionDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFunctionDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFunctionDefinitionsPaginatePaginationConfigTypeDef(
    _ListFunctionDefinitionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFunctionDefinitionsPaginate` `PaginationConfig`

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


_ListGroupVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupVersionsPaginatePaginationConfigTypeDef(
    _ListGroupVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGroupVersionsPaginate` `PaginationConfig`

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


_ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsPaginatePaginationConfigTypeDef(
    _ListGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGroupsPaginate` `PaginationConfig`

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


_ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ListGroupsPaginateResponseGroupsTypeDef(_ListGroupsPaginateResponseGroupsTypeDef):
    """
    Type definition for `ListGroupsPaginateResponse` `Groups`

    - **Arn** *(string) --* The ARN of the group.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    group was created.

    - **Id** *(string) --* The ID of the group.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the group was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the group.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    group.

    - **Name** *(string) --* The name of the group.
    """


_ListGroupsPaginateResponseTypeDef = TypedDict(
    "_ListGroupsPaginateResponseTypeDef",
    {"Groups": List[ListGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)


class ListGroupsPaginateResponseTypeDef(_ListGroupsPaginateResponseTypeDef):
    """
    Type definition for `ListGroupsPaginate` `Response`

    - **Groups** *(list) --* Information about a group.

      - *(dict) --* Information about a group.

        - **Arn** *(string) --* The ARN of the group.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        group was created.

        - **Id** *(string) --* The ID of the group.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the group was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the group.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        group.

        - **Name** *(string) --* The name of the group.
    """


_ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLoggerDefinitionVersionsPaginate` `PaginationConfig`

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


_ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListLoggerDefinitionVersionsPaginateResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ListLoggerDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListLoggerDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListLoggerDefinitionVersionsPaginateResponseTypeDef(
    _ListLoggerDefinitionVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListLoggerDefinitionVersionsPaginate` `Response`

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ListLoggerDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLoggerDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLoggerDefinitionsPaginatePaginationConfigTypeDef(
    _ListLoggerDefinitionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLoggerDefinitionsPaginate` `PaginationConfig`

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


_ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    Type definition for `ListLoggerDefinitionsPaginateResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ListLoggerDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListLoggerDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListLoggerDefinitionsPaginateResponseTypeDef(
    _ListLoggerDefinitionsPaginateResponseTypeDef
):
    """
    Type definition for `ListLoggerDefinitionsPaginate` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*
    """


_ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListResourceDefinitionVersionsPaginate` `PaginationConfig`

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


_ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListResourceDefinitionVersionsPaginateResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ListResourceDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListResourceDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListResourceDefinitionVersionsPaginateResponseTypeDef(
    _ListResourceDefinitionVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListResourceDefinitionVersionsPaginate` `Response`

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ListResourceDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceDefinitionsPaginatePaginationConfigTypeDef(
    _ListResourceDefinitionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListResourceDefinitionsPaginate` `PaginationConfig`

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


_ListResourceDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListResourceDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListResourceDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListResourceDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    Type definition for `ListResourceDefinitionsPaginateResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ListResourceDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListResourceDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListResourceDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListResourceDefinitionsPaginateResponseTypeDef(
    _ListResourceDefinitionsPaginateResponseTypeDef
):
    """
    Type definition for `ListResourceDefinitionsPaginate` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*
    """


_ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSubscriptionDefinitionVersionsPaginate` `PaginationConfig`

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


_ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListSubscriptionDefinitionVersionsPaginateResponse` `Versions`

    - **Arn** *(string) --* The ARN of the version.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    version was created.

    - **Id** *(string) --* The ID of the parent definition that the version is associated with.

    - **Version** *(string) --* The ID of the version.
    """


_ListSubscriptionDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListSubscriptionDefinitionVersionsPaginateResponseTypeDef",
    {
        "Versions": List[
            ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef
        ]
    },
    total=False,
)


class ListSubscriptionDefinitionVersionsPaginateResponseTypeDef(
    _ListSubscriptionDefinitionVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListSubscriptionDefinitionVersionsPaginate` `Response`

    - **Versions** *(list) --* Information about a version.

      - *(dict) --* Information about a version.

        - **Arn** *(string) --* The ARN of the version.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        version was created.

        - **Id** *(string) --* The ID of the parent definition that the version is associated with.

        - **Version** *(string) --* The ID of the version.
    """


_ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef(
    _ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSubscriptionDefinitionsPaginate` `PaginationConfig`

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


_ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    Type definition for `ListSubscriptionDefinitionsPaginateResponse` `Definitions`

    - **Arn** *(string) --* The ARN of the definition.

    - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
    definition was created.

    - **Id** *(string) --* The ID of the definition.

    - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
    the definition was last updated.

    - **LatestVersion** *(string) --* The ID of the latest version associated with the
    definition.

    - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
    definition.

    - **Name** *(string) --* The name of the definition.

    - **Tags** *(dict) --* Tag(s) attached to the resource arn.

      - *(string) --*

        - *(string) --*
    """


_ListSubscriptionDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListSubscriptionDefinitionsPaginateResponseTypeDef",
    {
        "Definitions": List[
            ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef
        ]
    },
    total=False,
)


class ListSubscriptionDefinitionsPaginateResponseTypeDef(
    _ListSubscriptionDefinitionsPaginateResponseTypeDef
):
    """
    Type definition for `ListSubscriptionDefinitionsPaginate` `Response`

    - **Definitions** *(list) --* Information about a definition.

      - *(dict) --* Information about a definition.

        - **Arn** *(string) --* The ARN of the definition.

        - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the
        definition was created.

        - **Id** *(string) --* The ID of the definition.

        - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when
        the definition was last updated.

        - **LatestVersion** *(string) --* The ID of the latest version associated with the
        definition.

        - **LatestVersionArn** *(string) --* The ARN of the latest version associated with the
        definition.

        - **Name** *(string) --* The name of the definition.

        - **Tags** *(dict) --* Tag(s) attached to the resource arn.

          - *(string) --*

            - *(string) --*
    """
