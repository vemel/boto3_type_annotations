"Main interface for mq type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateBrokerConfigurationTypeDef",
    "ClientCreateBrokerEncryptionOptionsTypeDef",
    "ClientCreateBrokerLogsTypeDef",
    "ClientCreateBrokerMaintenanceWindowStartTimeTypeDef",
    "ClientCreateBrokerResponseTypeDef",
    "ClientCreateConfigurationResponseLatestRevisionTypeDef",
    "ClientCreateConfigurationResponseTypeDef",
    "ClientDeleteBrokerResponseTypeDef",
    "ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef",
    "ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef",
    "ClientDescribeBrokerEngineTypesResponseTypeDef",
    "ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef",
    "ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef",
    "ClientDescribeBrokerInstanceOptionsResponseTypeDef",
    "ClientDescribeBrokerResponseBrokerInstancesTypeDef",
    "ClientDescribeBrokerResponseConfigurationsCurrentTypeDef",
    "ClientDescribeBrokerResponseConfigurationsHistoryTypeDef",
    "ClientDescribeBrokerResponseConfigurationsPendingTypeDef",
    "ClientDescribeBrokerResponseConfigurationsTypeDef",
    "ClientDescribeBrokerResponseEncryptionOptionsTypeDef",
    "ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef",
    "ClientDescribeBrokerResponseUsersTypeDef",
    "ClientDescribeBrokerResponseTypeDef",
    "ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    "ClientDescribeConfigurationResponseTypeDef",
    "ClientDescribeConfigurationRevisionResponseTypeDef",
    "ClientDescribeUserResponsePendingTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientListBrokersResponseBrokerSummariesTypeDef",
    "ClientListBrokersResponseTypeDef",
    "ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    "ClientListConfigurationRevisionsResponseTypeDef",
    "ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    "ClientListConfigurationsResponseConfigurationsTypeDef",
    "ClientListConfigurationsResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientUpdateBrokerConfigurationTypeDef",
    "ClientUpdateBrokerLogsTypeDef",
    "ClientUpdateBrokerResponseConfigurationTypeDef",
    "ClientUpdateBrokerResponseTypeDef",
    "ClientUpdateConfigurationResponseLatestRevisionTypeDef",
    "ClientUpdateConfigurationResponseTypeDef",
    "ListBrokersPaginatePaginationConfigTypeDef",
    "ListBrokersPaginateResponseBrokerSummariesTypeDef",
    "ListBrokersPaginateResponseTypeDef",
)


_ClientCreateBrokerConfigurationTypeDef = TypedDict(
    "_ClientCreateBrokerConfigurationTypeDef", {"Id": str, "Revision": int}, total=False
)


class ClientCreateBrokerConfigurationTypeDef(_ClientCreateBrokerConfigurationTypeDef):
    """
    Type definition for `ClientCreateBroker` `Configuration`

    - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.

    - **Revision** *(integer) --* The revision number of the configuration.
    """


_RequiredClientCreateBrokerEncryptionOptionsTypeDef = TypedDict(
    "_RequiredClientCreateBrokerEncryptionOptionsTypeDef", {"UseAwsOwnedKey": bool}
)
_OptionalClientCreateBrokerEncryptionOptionsTypeDef = TypedDict(
    "_OptionalClientCreateBrokerEncryptionOptionsTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientCreateBrokerEncryptionOptionsTypeDef(
    _RequiredClientCreateBrokerEncryptionOptionsTypeDef,
    _OptionalClientCreateBrokerEncryptionOptionsTypeDef,
):
    """
    Type definition for `ClientCreateBroker` `EncryptionOptions`

    - **KmsKeyId** *(string) --* The customer master key (CMK) to use for the AWS Key Management
    Service (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will use
    a default CMK to encrypt your data.

    - **UseAwsOwnedKey** *(boolean) --* **[REQUIRED]** Enables the use of an AWS owned CMK using AWS
    Key Management Service (KMS).
    """


_ClientCreateBrokerLogsTypeDef = TypedDict(
    "_ClientCreateBrokerLogsTypeDef", {"Audit": bool, "General": bool}, total=False
)


class ClientCreateBrokerLogsTypeDef(_ClientCreateBrokerLogsTypeDef):
    """
    Type definition for `ClientCreateBroker` `Logs`

    - **Audit** *(boolean) --* Enables audit logging. Every user management action made using JMX or
    the ActiveMQ Web Console is logged.

    - **General** *(boolean) --* Enables general logging.
    """


_ClientCreateBrokerMaintenanceWindowStartTimeTypeDef = TypedDict(
    "_ClientCreateBrokerMaintenanceWindowStartTimeTypeDef",
    {"DayOfWeek": str, "TimeOfDay": str, "TimeZone": str},
    total=False,
)


class ClientCreateBrokerMaintenanceWindowStartTimeTypeDef(
    _ClientCreateBrokerMaintenanceWindowStartTimeTypeDef
):
    """
    Type definition for `ClientCreateBroker` `MaintenanceWindowStartTime`

    - **DayOfWeek** *(string) --* Required. The day of the week.

    - **TimeOfDay** *(string) --* Required. The time, in 24-hour format.

    - **TimeZone** *(string) --* The time zone, UTC by default, in either the Country/City format, or
    the UTC offset format.
    """


_ClientCreateBrokerResponseTypeDef = TypedDict(
    "_ClientCreateBrokerResponseTypeDef",
    {"BrokerArn": str, "BrokerId": str},
    total=False,
)


class ClientCreateBrokerResponseTypeDef(_ClientCreateBrokerResponseTypeDef):
    """
    Type definition for `ClientCreateBroker` `Response`

    - **BrokerArn** *(string) --* The Amazon Resource Name (ARN) of the broker.

    - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.
    """


_ClientCreateConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "_ClientCreateConfigurationResponseLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientCreateConfigurationResponseLatestRevisionTypeDef(
    _ClientCreateConfigurationResponseLatestRevisionTypeDef
):
    """
    Type definition for `ClientCreateConfigurationResponse` `LatestRevision`

    - **Created** *(datetime) --* Required. The date and time of the configuration revision.

    - **Description** *(string) --* The description of the configuration revision.

    - **Revision** *(integer) --* Required. The revision number of the configuration.
    """


_ClientCreateConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": ClientCreateConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)


class ClientCreateConfigurationResponseTypeDef(
    _ClientCreateConfigurationResponseTypeDef
):
    """
    Type definition for `ClientCreateConfiguration` `Response`

    - **Arn** *(string) --* Required. The Amazon Resource Name (ARN) of the configuration.

    - **Created** *(datetime) --* Required. The date and time of the configuration.

    - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.

    - **LatestRevision** *(dict) --* The latest revision of the configuration.

      - **Created** *(datetime) --* Required. The date and time of the configuration revision.

      - **Description** *(string) --* The description of the configuration revision.

      - **Revision** *(integer) --* Required. The revision number of the configuration.

    - **Name** *(string) --* Required. The name of the configuration. This value can contain only
    alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be
    1-150 characters long.
    """


_ClientDeleteBrokerResponseTypeDef = TypedDict(
    "_ClientDeleteBrokerResponseTypeDef", {"BrokerId": str}, total=False
)


class ClientDeleteBrokerResponseTypeDef(_ClientDeleteBrokerResponseTypeDef):
    """
    Type definition for `ClientDeleteBroker` `Response`

    - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.
    """


_ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef = TypedDict(
    "_ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef(
    _ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef
):
    """
    Type definition for `ClientDescribeBrokerEngineTypesResponseBrokerEngineTypes` `EngineVersions`

    - **Name** *(string) --* Id for the version.
    """


_ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef = TypedDict(
    "_ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef",
    {
        "EngineType": str,
        "EngineVersions": List[
            ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesEngineVersionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef(
    _ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef
):
    """
    Type definition for `ClientDescribeBrokerEngineTypesResponse` `BrokerEngineTypes`

    - **EngineType** *(string) --* The type of broker engine.

    - **EngineVersions** *(list) --* The list of engine versions.

      - *(dict) --* Id of the engine version.

        - **Name** *(string) --* Id for the version.
    """


_ClientDescribeBrokerEngineTypesResponseTypeDef = TypedDict(
    "_ClientDescribeBrokerEngineTypesResponseTypeDef",
    {
        "BrokerEngineTypes": List[
            ClientDescribeBrokerEngineTypesResponseBrokerEngineTypesTypeDef
        ],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeBrokerEngineTypesResponseTypeDef(
    _ClientDescribeBrokerEngineTypesResponseTypeDef
):
    """
    Type definition for `ClientDescribeBrokerEngineTypes` `Response`

    - **BrokerEngineTypes** *(list) --* List of available engine types and versions.

      - *(dict) --* Types of broker engines.

        - **EngineType** *(string) --* The type of broker engine.

        - **EngineVersions** *(list) --* The list of engine versions.

          - *(dict) --* Id of the engine version.

            - **Name** *(string) --* Id for the version.

    - **MaxResults** *(integer) --* Required. The maximum number of engine types that can be
    returned per page (20 by default). This value must be an integer from 5 to 100.

    - **NextToken** *(string) --* The token that specifies the next page of results Amazon MQ
    should return. To request the first page, leave nextToken empty.
    """


_ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "_ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef(
    _ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef
):
    """
    Type definition for `ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptions` `AvailabilityZones`

    - **Name** *(string) --* Id for the availability zone.
    """


_ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef = TypedDict(
    "_ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef",
    {
        "AvailabilityZones": List[
            ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsAvailabilityZonesTypeDef
        ],
        "EngineType": str,
        "HostInstanceType": str,
        "SupportedEngineVersions": List[str],
    },
    total=False,
)


class ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef(
    _ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef
):
    """
    Type definition for `ClientDescribeBrokerInstanceOptionsResponse` `BrokerInstanceOptions`

    - **AvailabilityZones** *(list) --* The list of available az.

      - *(dict) --* Name of the availability zone.

        - **Name** *(string) --* Id for the availability zone.

    - **EngineType** *(string) --* The type of broker engine.

    - **HostInstanceType** *(string) --* The type of broker instance.

    - **SupportedEngineVersions** *(list) --* The list of supported engine versions.

      - *(string) --*
    """


_ClientDescribeBrokerInstanceOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeBrokerInstanceOptionsResponseTypeDef",
    {
        "BrokerInstanceOptions": List[
            ClientDescribeBrokerInstanceOptionsResponseBrokerInstanceOptionsTypeDef
        ],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeBrokerInstanceOptionsResponseTypeDef(
    _ClientDescribeBrokerInstanceOptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeBrokerInstanceOptions` `Response`

    - **BrokerInstanceOptions** *(list) --* List of available broker instance options.

      - *(dict) --* Option for host instance type.

        - **AvailabilityZones** *(list) --* The list of available az.

          - *(dict) --* Name of the availability zone.

            - **Name** *(string) --* Id for the availability zone.

        - **EngineType** *(string) --* The type of broker engine.

        - **HostInstanceType** *(string) --* The type of broker instance.

        - **SupportedEngineVersions** *(list) --* The list of supported engine versions.

          - *(string) --*

    - **MaxResults** *(integer) --* Required. The maximum number of instance options that can be
    returned per page (20 by default). This value must be an integer from 5 to 100.

    - **NextToken** *(string) --* The token that specifies the next page of results Amazon MQ
    should return. To request the first page, leave nextToken empty.
    """


_ClientDescribeBrokerResponseBrokerInstancesTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseBrokerInstancesTypeDef",
    {"ConsoleURL": str, "Endpoints": List[str], "IpAddress": str},
    total=False,
)


class ClientDescribeBrokerResponseBrokerInstancesTypeDef(
    _ClientDescribeBrokerResponseBrokerInstancesTypeDef
):
    """
    Type definition for `ClientDescribeBrokerResponse` `BrokerInstances`

    - **ConsoleURL** *(string) --* The URL of the broker's ActiveMQ Web Console.

    - **Endpoints** *(list) --* The broker's wire-level protocol endpoints.

      - *(string) --*

    - **IpAddress** *(string) --* The IP address of the Elastic Network Interface (ENI)
    attached to the broker.
    """


_ClientDescribeBrokerResponseConfigurationsCurrentTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseConfigurationsCurrentTypeDef",
    {"Id": str, "Revision": int},
    total=False,
)


class ClientDescribeBrokerResponseConfigurationsCurrentTypeDef(
    _ClientDescribeBrokerResponseConfigurationsCurrentTypeDef
):
    """
    Type definition for `ClientDescribeBrokerResponseConfigurations` `Current`

    - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
    configuration.

    - **Revision** *(integer) --* The revision number of the configuration.
    """


_ClientDescribeBrokerResponseConfigurationsHistoryTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseConfigurationsHistoryTypeDef",
    {"Id": str, "Revision": int},
    total=False,
)


class ClientDescribeBrokerResponseConfigurationsHistoryTypeDef(
    _ClientDescribeBrokerResponseConfigurationsHistoryTypeDef
):
    """
    Type definition for `ClientDescribeBrokerResponseConfigurations` `History`

    - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
    configuration.

    - **Revision** *(integer) --* The revision number of the configuration.
    """


_ClientDescribeBrokerResponseConfigurationsPendingTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseConfigurationsPendingTypeDef",
    {"Id": str, "Revision": int},
    total=False,
)


class ClientDescribeBrokerResponseConfigurationsPendingTypeDef(
    _ClientDescribeBrokerResponseConfigurationsPendingTypeDef
):
    """
    Type definition for `ClientDescribeBrokerResponseConfigurations` `Pending`

    - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
    configuration.

    - **Revision** *(integer) --* The revision number of the configuration.
    """


_ClientDescribeBrokerResponseConfigurationsTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseConfigurationsTypeDef",
    {
        "Current": ClientDescribeBrokerResponseConfigurationsCurrentTypeDef,
        "History": List[ClientDescribeBrokerResponseConfigurationsHistoryTypeDef],
        "Pending": ClientDescribeBrokerResponseConfigurationsPendingTypeDef,
    },
    total=False,
)


class ClientDescribeBrokerResponseConfigurationsTypeDef(
    _ClientDescribeBrokerResponseConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeBrokerResponse` `Configurations`

    - **Current** *(dict) --* The current configuration of the broker.

      - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
      configuration.

      - **Revision** *(integer) --* The revision number of the configuration.

    - **History** *(list) --* The history of configurations applied to the broker.

      - *(dict) --* A list of information about the configuration.

        - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
        configuration.

        - **Revision** *(integer) --* The revision number of the configuration.

    - **Pending** *(dict) --* The pending configuration of the broker.

      - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
      configuration.

      - **Revision** *(integer) --* The revision number of the configuration.
    """


_ClientDescribeBrokerResponseEncryptionOptionsTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseEncryptionOptionsTypeDef",
    {"KmsKeyId": str, "UseAwsOwnedKey": bool},
    total=False,
)


class ClientDescribeBrokerResponseEncryptionOptionsTypeDef(
    _ClientDescribeBrokerResponseEncryptionOptionsTypeDef
):
    """
    Type definition for `ClientDescribeBrokerResponse` `EncryptionOptions`

    - **KmsKeyId** *(string) --* The customer master key (CMK) to use for the AWS Key Management
    Service (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will
    use a default CMK to encrypt your data.

    - **UseAwsOwnedKey** *(boolean) --* Enables the use of an AWS owned CMK using AWS Key
    Management Service (KMS).
    """


_ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef",
    {"DayOfWeek": str, "TimeOfDay": str, "TimeZone": str},
    total=False,
)


class ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef(
    _ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef
):
    """
    Type definition for `ClientDescribeBrokerResponse` `MaintenanceWindowStartTime`

    - **DayOfWeek** *(string) --* Required. The day of the week.

    - **TimeOfDay** *(string) --* Required. The time, in 24-hour format.

    - **TimeZone** *(string) --* The time zone, UTC by default, in either the Country/City
    format, or the UTC offset format.
    """


_ClientDescribeBrokerResponseUsersTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseUsersTypeDef",
    {"PendingChange": str, "Username": str},
    total=False,
)


class ClientDescribeBrokerResponseUsersTypeDef(
    _ClientDescribeBrokerResponseUsersTypeDef
):
    """
    Type definition for `ClientDescribeBrokerResponse` `Users`

    - **PendingChange** *(string) --* The type of change pending for the ActiveMQ user.

    - **Username** *(string) --* Required. The username of the ActiveMQ user. This value can
    contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~).
    This value must be 2-100 characters long.
    """


_ClientDescribeBrokerResponseTypeDef = TypedDict(
    "_ClientDescribeBrokerResponseTypeDef",
    {
        "AutoMinorVersionUpgrade": bool,
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerInstances": List[ClientDescribeBrokerResponseBrokerInstancesTypeDef],
        "BrokerName": str,
        "BrokerState": str,
        "Configurations": ClientDescribeBrokerResponseConfigurationsTypeDef,
        "Created": datetime,
        "DeploymentMode": str,
        "EncryptionOptions": ClientDescribeBrokerResponseEncryptionOptionsTypeDef,
        "EngineType": str,
        "EngineVersion": str,
        "HostInstanceType": str,
        "Logs": Dict[str, Any],
        "MaintenanceWindowStartTime": ClientDescribeBrokerResponseMaintenanceWindowStartTimeTypeDef,
        "PendingEngineVersion": str,
        "PendingSecurityGroups": List[Any],
        "PendingHostInstanceType": str,
        "PubliclyAccessible": bool,
        "SecurityGroups": List[Any],
        "SubnetIds": List[Any],
        "Tags": Dict[str, str],
        "Users": List[ClientDescribeBrokerResponseUsersTypeDef],
    },
    total=False,
)


class ClientDescribeBrokerResponseTypeDef(_ClientDescribeBrokerResponseTypeDef):
    """
    Type definition for `ClientDescribeBroker` `Response`

    - **AutoMinorVersionUpgrade** *(boolean) --* Required. Enables automatic upgrades to new minor
    versions for brokers, as Apache releases the versions. The automatic upgrades occur during the
    maintenance window of the broker or after a manual broker reboot.

    - **BrokerArn** *(string) --* The Amazon Resource Name (ARN) of the broker.

    - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.

    - **BrokerInstances** *(list) --* A list of information about allocated brokers.

      - *(dict) --* Returns information about all brokers.

        - **ConsoleURL** *(string) --* The URL of the broker's ActiveMQ Web Console.

        - **Endpoints** *(list) --* The broker's wire-level protocol endpoints.

          - *(string) --*

        - **IpAddress** *(string) --* The IP address of the Elastic Network Interface (ENI)
        attached to the broker.

    - **BrokerName** *(string) --* The name of the broker. This value must be unique in your AWS
    account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and
    must not contain whitespaces, brackets, wildcard characters, or special characters.

    - **BrokerState** *(string) --* The status of the broker.

    - **Configurations** *(dict) --* The list of all revisions for the specified configuration.

      - **Current** *(dict) --* The current configuration of the broker.

        - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
        configuration.

        - **Revision** *(integer) --* The revision number of the configuration.

      - **History** *(list) --* The history of configurations applied to the broker.

        - *(dict) --* A list of information about the configuration.

          - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
          configuration.

          - **Revision** *(integer) --* The revision number of the configuration.

      - **Pending** *(dict) --* The pending configuration of the broker.

        - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
        configuration.

        - **Revision** *(integer) --* The revision number of the configuration.

    - **Created** *(datetime) --* The time when the broker was created.

    - **DeploymentMode** *(string) --* Required. The deployment mode of the broker.

    - **EncryptionOptions** *(dict) --* Encryption options for the broker.

      - **KmsKeyId** *(string) --* The customer master key (CMK) to use for the AWS Key Management
      Service (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will
      use a default CMK to encrypt your data.

      - **UseAwsOwnedKey** *(boolean) --* Enables the use of an AWS owned CMK using AWS Key
      Management Service (KMS).

    - **EngineType** *(string) --* Required. The type of broker engine. Note: Currently, Amazon MQ
    supports only ACTIVEMQ.

    - **EngineVersion** *(string) --* The version of the broker engine. For a list of supported
    engine versions, see
    https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html

    - **HostInstanceType** *(string) --* The broker's instance type.

    - **Logs** *(dict) --* The list of information about logs currently enabled and pending to be
    deployed for the specified broker.

      - **Audit** *(boolean) --* Enables audit logging. Every user management action made using JMX
      or the ActiveMQ Web Console is logged.

      - **AuditLogGroup** *(string) --* The location of the CloudWatch Logs log group where audit
      logs are sent.

      - **General** *(boolean) --* Enables general logging.

      - **GeneralLogGroup** *(string) --* The location of the CloudWatch Logs log group where
      general logs are sent.

      - **Pending** *(dict) --* The list of information about logs pending to be deployed for the
      specified broker.

        - **Audit** *(boolean) --* Enables audit logging. Every user management action made using
        JMX or the ActiveMQ Web Console is logged.

        - **General** *(boolean) --* Enables general logging.

    - **MaintenanceWindowStartTime** *(dict) --* The parameters that determine the WeeklyStartTime.

      - **DayOfWeek** *(string) --* Required. The day of the week.

      - **TimeOfDay** *(string) --* Required. The time, in 24-hour format.

      - **TimeZone** *(string) --* The time zone, UTC by default, in either the Country/City
      format, or the UTC offset format.

    - **PendingEngineVersion** *(string) --* The version of the broker engine to upgrade to. For a
    list of supported engine versions, see
    https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html

    - **PendingSecurityGroups** *(list) --* The list of pending security groups to authorize
    connections to brokers.

      - *(string) --*

    - **PendingHostInstanceType** *(string) --* The host instance type of the broker to upgrade to.
    For a list of supported instance types, see
    https://docs.aws.amazon.com/amazon-mq/latest/developer-guide//broker.html#broker-instance-types

    - **PubliclyAccessible** *(boolean) --* Required. Enables connections from applications outside
    of the VPC that hosts the broker's subnets.

    - **SecurityGroups** *(list) --* The list of security groups (1 minimum, 5 maximum) that
    authorize connections to brokers.

      - *(string) --*

    - **SubnetIds** *(list) --* The list of groups (2 maximum) that define which subnets and IP
    ranges the broker can use from different Availability Zones. A SINGLE_INSTANCE deployment
    requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ deployment
    requires two subnets.

      - *(string) --*

    - **Tags** *(dict) --* The list of all tags associated with this broker.

      - *(string) --*

        - *(string) --*

    - **Users** *(list) --* The list of all ActiveMQ usernames for the specified broker.

      - *(dict) --* Returns a list of all ActiveMQ users.

        - **PendingChange** *(string) --* The type of change pending for the ActiveMQ user.

        - **Username** *(string) --* Required. The username of the ActiveMQ user. This value can
        contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~).
        This value must be 2-100 characters long.
    """


_ClientDescribeConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "_ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientDescribeConfigurationResponseLatestRevisionTypeDef(
    _ClientDescribeConfigurationResponseLatestRevisionTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationResponse` `LatestRevision`

    - **Created** *(datetime) --* Required. The date and time of the configuration revision.

    - **Description** *(string) --* The description of the configuration revision.

    - **Revision** *(integer) --* Required. The revision number of the configuration.
    """


_ClientDescribeConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Description": str,
        "EngineType": str,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": ClientDescribeConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeConfigurationResponseTypeDef(
    _ClientDescribeConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfiguration` `Response`

    - **Arn** *(string) --* Required. The ARN of the configuration.

    - **Created** *(datetime) --* Required. The date and time of the configuration revision.

    - **Description** *(string) --* Required. The description of the configuration.

    - **EngineType** *(string) --* Required. The type of broker engine. Note: Currently, Amazon MQ
    supports only ACTIVEMQ.

    - **EngineVersion** *(string) --* Required. The version of the broker engine. For a list of
    supported engine versions, see
    https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html

    - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.

    - **LatestRevision** *(dict) --* Required. The latest revision of the configuration.

      - **Created** *(datetime) --* Required. The date and time of the configuration revision.

      - **Description** *(string) --* The description of the configuration revision.

      - **Revision** *(integer) --* Required. The revision number of the configuration.

    - **Name** *(string) --* Required. The name of the configuration. This value can contain only
    alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be
    1-150 characters long.

    - **Tags** *(dict) --* The list of all tags associated with this configuration.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationRevisionResponseTypeDef",
    {"ConfigurationId": str, "Created": datetime, "Data": str, "Description": str},
    total=False,
)


class ClientDescribeConfigurationRevisionResponseTypeDef(
    _ClientDescribeConfigurationRevisionResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationRevision` `Response`

    - **ConfigurationId** *(string) --* Required. The unique ID that Amazon MQ generates for the
    configuration.

    - **Created** *(datetime) --* Required. The date and time of the configuration.

    - **Data** *(string) --* Required. The base64-encoded XML configuration.

    - **Description** *(string) --* The description of the configuration.
    """


_ClientDescribeUserResponsePendingTypeDef = TypedDict(
    "_ClientDescribeUserResponsePendingTypeDef",
    {"ConsoleAccess": bool, "Groups": List[Any], "PendingChange": str},
    total=False,
)


class ClientDescribeUserResponsePendingTypeDef(
    _ClientDescribeUserResponsePendingTypeDef
):
    """
    Type definition for `ClientDescribeUserResponse` `Pending`

    - **ConsoleAccess** *(boolean) --* Enables access to the the ActiveMQ Web Console for the
    ActiveMQ user.

    - **Groups** *(list) --* The list of groups (20 maximum) to which the ActiveMQ user belongs.
    This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes
    (- . _ ~). This value must be 2-100 characters long.

      - *(string) --*

    - **PendingChange** *(string) --* Required. The type of change pending for the ActiveMQ user.
    """


_ClientDescribeUserResponseTypeDef = TypedDict(
    "_ClientDescribeUserResponseTypeDef",
    {
        "BrokerId": str,
        "ConsoleAccess": bool,
        "Groups": List[Any],
        "Pending": ClientDescribeUserResponsePendingTypeDef,
        "Username": str,
    },
    total=False,
)


class ClientDescribeUserResponseTypeDef(_ClientDescribeUserResponseTypeDef):
    """
    Type definition for `ClientDescribeUser` `Response`

    - **BrokerId** *(string) --* Required. The unique ID that Amazon MQ generates for the broker.

    - **ConsoleAccess** *(boolean) --* Enables access to the the ActiveMQ Web Console for the
    ActiveMQ user.

    - **Groups** *(list) --* The list of groups (20 maximum) to which the ActiveMQ user belongs.
    This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes
    (- . _ ~). This value must be 2-100 characters long.

      - *(string) --*

    - **Pending** *(dict) --* The status of the changes pending for the ActiveMQ user.

      - **ConsoleAccess** *(boolean) --* Enables access to the the ActiveMQ Web Console for the
      ActiveMQ user.

      - **Groups** *(list) --* The list of groups (20 maximum) to which the ActiveMQ user belongs.
      This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes
      (- . _ ~). This value must be 2-100 characters long.

        - *(string) --*

      - **PendingChange** *(string) --* Required. The type of change pending for the ActiveMQ user.

    - **Username** *(string) --* Required. The username of the ActiveMQ user. This value can
    contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This
    value must be 2-100 characters long.
    """


_ClientListBrokersResponseBrokerSummariesTypeDef = TypedDict(
    "_ClientListBrokersResponseBrokerSummariesTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerName": str,
        "BrokerState": str,
        "Created": datetime,
        "DeploymentMode": str,
        "HostInstanceType": str,
    },
    total=False,
)


class ClientListBrokersResponseBrokerSummariesTypeDef(
    _ClientListBrokersResponseBrokerSummariesTypeDef
):
    """
    Type definition for `ClientListBrokersResponse` `BrokerSummaries`

    - **BrokerArn** *(string) --* The Amazon Resource Name (ARN) of the broker.

    - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.

    - **BrokerName** *(string) --* The name of the broker. This value must be unique in your
    AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and
    underscores, and must not contain whitespaces, brackets, wildcard characters, or special
    characters.

    - **BrokerState** *(string) --* The status of the broker.

    - **Created** *(datetime) --* The time when the broker was created.

    - **DeploymentMode** *(string) --* Required. The deployment mode of the broker.

    - **HostInstanceType** *(string) --* The broker's instance type.
    """


_ClientListBrokersResponseTypeDef = TypedDict(
    "_ClientListBrokersResponseTypeDef",
    {
        "BrokerSummaries": List[ClientListBrokersResponseBrokerSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListBrokersResponseTypeDef(_ClientListBrokersResponseTypeDef):
    """
    Type definition for `ClientListBrokers` `Response`

    - **BrokerSummaries** *(list) --* A list of information about all brokers.

      - *(dict) --* The Amazon Resource Name (ARN) of the broker.

        - **BrokerArn** *(string) --* The Amazon Resource Name (ARN) of the broker.

        - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.

        - **BrokerName** *(string) --* The name of the broker. This value must be unique in your
        AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and
        underscores, and must not contain whitespaces, brackets, wildcard characters, or special
        characters.

        - **BrokerState** *(string) --* The status of the broker.

        - **Created** *(datetime) --* The time when the broker was created.

        - **DeploymentMode** *(string) --* Required. The deployment mode of the broker.

        - **HostInstanceType** *(string) --* The broker's instance type.

    - **NextToken** *(string) --* The token that specifies the next page of results Amazon MQ
    should return. To request the first page, leave nextToken empty.
    """


_ClientListConfigurationRevisionsResponseRevisionsTypeDef = TypedDict(
    "_ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientListConfigurationRevisionsResponseRevisionsTypeDef(
    _ClientListConfigurationRevisionsResponseRevisionsTypeDef
):
    """
    Type definition for `ClientListConfigurationRevisionsResponse` `Revisions`

    - **Created** *(datetime) --* Required. The date and time of the configuration revision.

    - **Description** *(string) --* The description of the configuration revision.

    - **Revision** *(integer) --* Required. The revision number of the configuration.
    """


_ClientListConfigurationRevisionsResponseTypeDef = TypedDict(
    "_ClientListConfigurationRevisionsResponseTypeDef",
    {
        "ConfigurationId": str,
        "MaxResults": int,
        "NextToken": str,
        "Revisions": List[ClientListConfigurationRevisionsResponseRevisionsTypeDef],
    },
    total=False,
)


class ClientListConfigurationRevisionsResponseTypeDef(
    _ClientListConfigurationRevisionsResponseTypeDef
):
    """
    Type definition for `ClientListConfigurationRevisions` `Response`

    - **ConfigurationId** *(string) --* The unique ID that Amazon MQ generates for the
    configuration.

    - **MaxResults** *(integer) --* The maximum number of configuration revisions that can be
    returned per page (20 by default). This value must be an integer from 5 to 100.

    - **NextToken** *(string) --* The token that specifies the next page of results Amazon MQ
    should return. To request the first page, leave nextToken empty.

    - **Revisions** *(list) --* The list of all revisions for the specified configuration.

      - *(dict) --* Returns information about the specified configuration revision.

        - **Created** *(datetime) --* Required. The date and time of the configuration revision.

        - **Description** *(string) --* The description of the configuration revision.

        - **Revision** *(integer) --* Required. The revision number of the configuration.
    """


_ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef = TypedDict(
    "_ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef(
    _ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef
):
    """
    Type definition for `ClientListConfigurationsResponseConfigurations` `LatestRevision`

    - **Created** *(datetime) --* Required. The date and time of the configuration revision.

    - **Description** *(string) --* The description of the configuration revision.

    - **Revision** *(integer) --* Required. The revision number of the configuration.
    """


_ClientListConfigurationsResponseConfigurationsTypeDef = TypedDict(
    "_ClientListConfigurationsResponseConfigurationsTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Description": str,
        "EngineType": str,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListConfigurationsResponseConfigurationsTypeDef(
    _ClientListConfigurationsResponseConfigurationsTypeDef
):
    """
    Type definition for `ClientListConfigurationsResponse` `Configurations`

    - **Arn** *(string) --* Required. The ARN of the configuration.

    - **Created** *(datetime) --* Required. The date and time of the configuration revision.

    - **Description** *(string) --* Required. The description of the configuration.

    - **EngineType** *(string) --* Required. The type of broker engine. Note: Currently, Amazon
    MQ supports only ACTIVEMQ.

    - **EngineVersion** *(string) --* Required. The version of the broker engine. For a list of
    supported engine versions, see
    https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html

    - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
    configuration.

    - **LatestRevision** *(dict) --* Required. The latest revision of the configuration.

      - **Created** *(datetime) --* Required. The date and time of the configuration revision.

      - **Description** *(string) --* The description of the configuration revision.

      - **Revision** *(integer) --* Required. The revision number of the configuration.

    - **Name** *(string) --* Required. The name of the configuration. This value can contain
    only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This
    value must be 1-150 characters long.

    - **Tags** *(dict) --* The list of all tags associated with this configuration.

      - *(string) --*

        - *(string) --*
    """


_ClientListConfigurationsResponseTypeDef = TypedDict(
    "_ClientListConfigurationsResponseTypeDef",
    {
        "Configurations": List[ClientListConfigurationsResponseConfigurationsTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ClientListConfigurationsResponseTypeDef(_ClientListConfigurationsResponseTypeDef):
    """
    Type definition for `ClientListConfigurations` `Response`

    - **Configurations** *(list) --* The list of all revisions for the specified configuration.

      - *(dict) --* Returns information about all configurations.

        - **Arn** *(string) --* Required. The ARN of the configuration.

        - **Created** *(datetime) --* Required. The date and time of the configuration revision.

        - **Description** *(string) --* Required. The description of the configuration.

        - **EngineType** *(string) --* Required. The type of broker engine. Note: Currently, Amazon
        MQ supports only ACTIVEMQ.

        - **EngineVersion** *(string) --* Required. The version of the broker engine. For a list of
        supported engine versions, see
        https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html

        - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the
        configuration.

        - **LatestRevision** *(dict) --* Required. The latest revision of the configuration.

          - **Created** *(datetime) --* Required. The date and time of the configuration revision.

          - **Description** *(string) --* The description of the configuration revision.

          - **Revision** *(integer) --* Required. The revision number of the configuration.

        - **Name** *(string) --* Required. The name of the configuration. This value can contain
        only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This
        value must be 1-150 characters long.

        - **Tags** *(dict) --* The list of all tags associated with this configuration.

          - *(string) --*

            - *(string) --*

    - **MaxResults** *(integer) --* The maximum number of configurations that Amazon MQ can return
    per page (20 by default). This value must be an integer from 5 to 100.

    - **NextToken** *(string) --* The token that specifies the next page of results Amazon MQ
    should return. To request the first page, leave nextToken empty.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    Type definition for `ClientListTags` `Response`

    - **Tags** *(dict) --* The key-value pair for the resource tag.

      - *(string) --*

        - *(string) --*
    """


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {"PendingChange": str, "Username": str},
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    Type definition for `ClientListUsersResponse` `Users`

    - **PendingChange** *(string) --* The type of change pending for the ActiveMQ user.

    - **Username** *(string) --* Required. The username of the ActiveMQ user. This value can
    contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~).
    This value must be 2-100 characters long.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {
        "BrokerId": str,
        "MaxResults": int,
        "NextToken": str,
        "Users": List[ClientListUsersResponseUsersTypeDef],
    },
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    Type definition for `ClientListUsers` `Response`

    - **BrokerId** *(string) --* Required. The unique ID that Amazon MQ generates for the broker.

    - **MaxResults** *(integer) --* Required. The maximum number of ActiveMQ users that can be
    returned per page (20 by default). This value must be an integer from 5 to 100.

    - **NextToken** *(string) --* The token that specifies the next page of results Amazon MQ
    should return. To request the first page, leave nextToken empty.

    - **Users** *(list) --* Required. The list of all ActiveMQ usernames for the specified broker.

      - *(dict) --* Returns a list of all ActiveMQ users.

        - **PendingChange** *(string) --* The type of change pending for the ActiveMQ user.

        - **Username** *(string) --* Required. The username of the ActiveMQ user. This value can
        contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~).
        This value must be 2-100 characters long.
    """


_ClientUpdateBrokerConfigurationTypeDef = TypedDict(
    "_ClientUpdateBrokerConfigurationTypeDef", {"Id": str, "Revision": int}, total=False
)


class ClientUpdateBrokerConfigurationTypeDef(_ClientUpdateBrokerConfigurationTypeDef):
    """
    Type definition for `ClientUpdateBroker` `Configuration`

    - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.

    - **Revision** *(integer) --* The revision number of the configuration.
    """


_ClientUpdateBrokerLogsTypeDef = TypedDict(
    "_ClientUpdateBrokerLogsTypeDef", {"Audit": bool, "General": bool}, total=False
)


class ClientUpdateBrokerLogsTypeDef(_ClientUpdateBrokerLogsTypeDef):
    """
    Type definition for `ClientUpdateBroker` `Logs`

    - **Audit** *(boolean) --* Enables audit logging. Every user management action made using JMX or
    the ActiveMQ Web Console is logged.

    - **General** *(boolean) --* Enables general logging.
    """


_ClientUpdateBrokerResponseConfigurationTypeDef = TypedDict(
    "_ClientUpdateBrokerResponseConfigurationTypeDef",
    {"Id": str, "Revision": int},
    total=False,
)


class ClientUpdateBrokerResponseConfigurationTypeDef(
    _ClientUpdateBrokerResponseConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateBrokerResponse` `Configuration`

    - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.

    - **Revision** *(integer) --* The revision number of the configuration.
    """


_ClientUpdateBrokerResponseTypeDef = TypedDict(
    "_ClientUpdateBrokerResponseTypeDef",
    {
        "AutoMinorVersionUpgrade": bool,
        "BrokerId": str,
        "Configuration": ClientUpdateBrokerResponseConfigurationTypeDef,
        "EngineVersion": str,
        "HostInstanceType": str,
        "Logs": Dict[str, Any],
        "SecurityGroups": List[Any],
    },
    total=False,
)


class ClientUpdateBrokerResponseTypeDef(_ClientUpdateBrokerResponseTypeDef):
    """
    Type definition for `ClientUpdateBroker` `Response`

    - **AutoMinorVersionUpgrade** *(boolean) --* The new value of automatic upgrades to new minor
    version for brokers.

    - **BrokerId** *(string) --* Required. The unique ID that Amazon MQ generates for the broker.

    - **Configuration** *(dict) --* The ID of the updated configuration.

      - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.

      - **Revision** *(integer) --* The revision number of the configuration.

    - **EngineVersion** *(string) --* The version of the broker engine to upgrade to. For a list of
    supported engine versions, see
    https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html

    - **HostInstanceType** *(string) --* The host instance type of the broker to upgrade to. For a
    list of supported instance types, see
    https://docs.aws.amazon.com/amazon-mq/latest/developer-guide//broker.html#broker-instance-types

    - **Logs** *(dict) --* The list of information about logs to be enabled for the specified
    broker.

      - **Audit** *(boolean) --* Enables audit logging. Every user management action made using JMX
      or the ActiveMQ Web Console is logged.

      - **General** *(boolean) --* Enables general logging.

    - **SecurityGroups** *(list) --* The list of security groups (1 minimum, 5 maximum) that
    authorize connections to brokers.

      - *(string) --*
    """


_ClientUpdateConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "_ClientUpdateConfigurationResponseLatestRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)


class ClientUpdateConfigurationResponseLatestRevisionTypeDef(
    _ClientUpdateConfigurationResponseLatestRevisionTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationResponse` `LatestRevision`

    - **Created** *(datetime) --* Required. The date and time of the configuration revision.

    - **Description** *(string) --* The description of the configuration revision.

    - **Revision** *(integer) --* Required. The revision number of the configuration.
    """


_ClientUpdateConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": ClientUpdateConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
        "Warnings": List[Any],
    },
    total=False,
)


class ClientUpdateConfigurationResponseTypeDef(
    _ClientUpdateConfigurationResponseTypeDef
):
    """
    Type definition for `ClientUpdateConfiguration` `Response`

    - **Arn** *(string) --* Required. The Amazon Resource Name (ARN) of the configuration.

    - **Created** *(datetime) --* Required. The date and time of the configuration.

    - **Id** *(string) --* Required. The unique ID that Amazon MQ generates for the configuration.

    - **LatestRevision** *(dict) --* The latest revision of the configuration.

      - **Created** *(datetime) --* Required. The date and time of the configuration revision.

      - **Description** *(string) --* The description of the configuration revision.

      - **Revision** *(integer) --* Required. The revision number of the configuration.

    - **Name** *(string) --* Required. The name of the configuration. This value can contain only
    alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be
    1-150 characters long.

    - **Warnings** *(list) --* The list of the first 20 warnings about the configuration XML
    elements or attributes that were sanitized.

      - *(dict) --* Returns information about the XML element or attribute that was sanitized in
      the configuration.

        - **AttributeName** *(string) --* The name of the XML attribute that has been sanitized.

        - **ElementName** *(string) --* The name of the XML element that has been sanitized.

        - **Reason** *(string) --* Required. The reason for which the XML elements or attributes
        were sanitized.
    """


_ListBrokersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBrokersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBrokersPaginatePaginationConfigTypeDef(
    _ListBrokersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBrokersPaginate` `PaginationConfig`

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


_ListBrokersPaginateResponseBrokerSummariesTypeDef = TypedDict(
    "_ListBrokersPaginateResponseBrokerSummariesTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerName": str,
        "BrokerState": str,
        "Created": datetime,
        "DeploymentMode": str,
        "HostInstanceType": str,
    },
    total=False,
)


class ListBrokersPaginateResponseBrokerSummariesTypeDef(
    _ListBrokersPaginateResponseBrokerSummariesTypeDef
):
    """
    Type definition for `ListBrokersPaginateResponse` `BrokerSummaries`

    - **BrokerArn** *(string) --* The Amazon Resource Name (ARN) of the broker.

    - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.

    - **BrokerName** *(string) --* The name of the broker. This value must be unique in your
    AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and
    underscores, and must not contain whitespaces, brackets, wildcard characters, or special
    characters.

    - **BrokerState** *(string) --* The status of the broker.

    - **Created** *(datetime) --* The time when the broker was created.

    - **DeploymentMode** *(string) --* Required. The deployment mode of the broker.

    - **HostInstanceType** *(string) --* The broker's instance type.
    """


_ListBrokersPaginateResponseTypeDef = TypedDict(
    "_ListBrokersPaginateResponseTypeDef",
    {"BrokerSummaries": List[ListBrokersPaginateResponseBrokerSummariesTypeDef]},
    total=False,
)


class ListBrokersPaginateResponseTypeDef(_ListBrokersPaginateResponseTypeDef):
    """
    Type definition for `ListBrokersPaginate` `Response`

    - **BrokerSummaries** *(list) --* A list of information about all brokers.

      - *(dict) --* The Amazon Resource Name (ARN) of the broker.

        - **BrokerArn** *(string) --* The Amazon Resource Name (ARN) of the broker.

        - **BrokerId** *(string) --* The unique ID that Amazon MQ generates for the broker.

        - **BrokerName** *(string) --* The name of the broker. This value must be unique in your
        AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and
        underscores, and must not contain whitespaces, brackets, wildcard characters, or special
        characters.

        - **BrokerState** *(string) --* The status of the broker.

        - **Created** *(datetime) --* The time when the broker was created.

        - **DeploymentMode** *(string) --* Required. The deployment mode of the broker.

        - **HostInstanceType** *(string) --* The broker's instance type.
    """
