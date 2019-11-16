"Main interface for gamelift type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAliasResponseAliasRoutingStrategyTypeDef",
    "ClientCreateAliasResponseAliasTypeDef",
    "ClientCreateAliasResponseTypeDef",
    "ClientCreateAliasRoutingStrategyTypeDef",
    "ClientCreateBuildResponseBuildTypeDef",
    "ClientCreateBuildResponseStorageLocationTypeDef",
    "ClientCreateBuildResponseUploadCredentialsTypeDef",
    "ClientCreateBuildResponseTypeDef",
    "ClientCreateBuildStorageLocationTypeDef",
    "ClientCreateFleetCertificateConfigurationTypeDef",
    "ClientCreateFleetEC2InboundPermissionsTypeDef",
    "ClientCreateFleetResourceCreationLimitPolicyTypeDef",
    "ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef",
    "ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    "ClientCreateFleetResponseFleetAttributesTypeDef",
    "ClientCreateFleetResponseTypeDef",
    "ClientCreateFleetRuntimeConfigurationServerProcessesTypeDef",
    "ClientCreateFleetRuntimeConfigurationTypeDef",
    "ClientCreateGameSessionGamePropertiesTypeDef",
    "ClientCreateGameSessionQueueDestinationsTypeDef",
    "ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef",
    "ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef",
    "ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef",
    "ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef",
    "ClientCreateGameSessionQueueResponseTypeDef",
    "ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef",
    "ClientCreateGameSessionResponseGameSessionTypeDef",
    "ClientCreateGameSessionResponseTypeDef",
    "ClientCreateMatchmakingConfigurationGamePropertiesTypeDef",
    "ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef",
    "ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef",
    "ClientCreateMatchmakingConfigurationResponseTypeDef",
    "ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef",
    "ClientCreateMatchmakingRuleSetResponseTypeDef",
    "ClientCreatePlayerSessionResponsePlayerSessionTypeDef",
    "ClientCreatePlayerSessionResponseTypeDef",
    "ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef",
    "ClientCreatePlayerSessionsResponseTypeDef",
    "ClientCreateScriptResponseScriptStorageLocationTypeDef",
    "ClientCreateScriptResponseScriptTypeDef",
    "ClientCreateScriptResponseTypeDef",
    "ClientCreateScriptStorageLocationTypeDef",
    "ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef",
    "ClientCreateVpcPeeringAuthorizationResponseTypeDef",
    "ClientDescribeAliasResponseAliasRoutingStrategyTypeDef",
    "ClientDescribeAliasResponseAliasTypeDef",
    "ClientDescribeAliasResponseTypeDef",
    "ClientDescribeBuildResponseBuildTypeDef",
    "ClientDescribeBuildResponseTypeDef",
    "ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef",
    "ClientDescribeEc2InstanceLimitsResponseTypeDef",
    "ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef",
    "ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    "ClientDescribeFleetAttributesResponseFleetAttributesTypeDef",
    "ClientDescribeFleetAttributesResponseTypeDef",
    "ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef",
    "ClientDescribeFleetCapacityResponseFleetCapacityTypeDef",
    "ClientDescribeFleetCapacityResponseTypeDef",
    "ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef",
    "ClientDescribeFleetPortSettingsResponseTypeDef",
    "ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef",
    "ClientDescribeFleetUtilizationResponseTypeDef",
    "ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef",
    "ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef",
    "ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef",
    "ClientDescribeGameSessionDetailsResponseTypeDef",
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    "ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef",
    "ClientDescribeGameSessionPlacementResponseTypeDef",
    "ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef",
    "ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef",
    "ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef",
    "ClientDescribeGameSessionQueuesResponseTypeDef",
    "ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef",
    "ClientDescribeGameSessionsResponseGameSessionsTypeDef",
    "ClientDescribeGameSessionsResponseTypeDef",
    "ClientDescribeInstancesResponseInstancesTypeDef",
    "ClientDescribeInstancesResponseTypeDef",
    "ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef",
    "ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef",
    "ClientDescribeMatchmakingConfigurationsResponseTypeDef",
    "ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    "ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef",
    "ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef",
    "ClientDescribeMatchmakingResponseTicketListPlayersTypeDef",
    "ClientDescribeMatchmakingResponseTicketListTypeDef",
    "ClientDescribeMatchmakingResponseTypeDef",
    "ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef",
    "ClientDescribeMatchmakingRuleSetsResponseTypeDef",
    "ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef",
    "ClientDescribePlayerSessionsResponseTypeDef",
    "ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef",
    "ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef",
    "ClientDescribeRuntimeConfigurationResponseTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
    "ClientDescribeScalingPoliciesResponseTypeDef",
    "ClientDescribeScriptResponseScriptStorageLocationTypeDef",
    "ClientDescribeScriptResponseScriptTypeDef",
    "ClientDescribeScriptResponseTypeDef",
    "ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef",
    "ClientDescribeVpcPeeringAuthorizationsResponseTypeDef",
    "ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef",
    "ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef",
    "ClientDescribeVpcPeeringConnectionsResponseTypeDef",
    "ClientGetGameSessionLogUrlResponseTypeDef",
    "ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef",
    "ClientGetInstanceAccessResponseInstanceAccessTypeDef",
    "ClientGetInstanceAccessResponseTypeDef",
    "ClientListAliasesResponseAliasesRoutingStrategyTypeDef",
    "ClientListAliasesResponseAliasesTypeDef",
    "ClientListAliasesResponseTypeDef",
    "ClientListBuildsResponseBuildsTypeDef",
    "ClientListBuildsResponseTypeDef",
    "ClientListFleetsResponseTypeDef",
    "ClientListScriptsResponseScriptsStorageLocationTypeDef",
    "ClientListScriptsResponseScriptsTypeDef",
    "ClientListScriptsResponseTypeDef",
    "ClientPutScalingPolicyResponseTypeDef",
    "ClientPutScalingPolicyTargetConfigurationTypeDef",
    "ClientRequestUploadCredentialsResponseStorageLocationTypeDef",
    "ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef",
    "ClientRequestUploadCredentialsResponseTypeDef",
    "ClientResolveAliasResponseTypeDef",
    "ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef",
    "ClientSearchGameSessionsResponseGameSessionsTypeDef",
    "ClientSearchGameSessionsResponseTypeDef",
    "ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef",
    "ClientStartGameSessionPlacementGamePropertiesTypeDef",
    "ClientStartGameSessionPlacementPlayerLatenciesTypeDef",
    "ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    "ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    "ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    "ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef",
    "ClientStartGameSessionPlacementResponseTypeDef",
    "ClientStartMatchBackfillPlayersPlayerAttributesTypeDef",
    "ClientStartMatchBackfillPlayersTypeDef",
    "ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    "ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef",
    "ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef",
    "ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef",
    "ClientStartMatchBackfillResponseMatchmakingTicketTypeDef",
    "ClientStartMatchBackfillResponseTypeDef",
    "ClientStartMatchmakingPlayersPlayerAttributesTypeDef",
    "ClientStartMatchmakingPlayersTypeDef",
    "ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    "ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef",
    "ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef",
    "ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef",
    "ClientStartMatchmakingResponseMatchmakingTicketTypeDef",
    "ClientStartMatchmakingResponseTypeDef",
    "ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    "ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    "ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    "ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef",
    "ClientStopGameSessionPlacementResponseTypeDef",
    "ClientUpdateAliasResponseAliasRoutingStrategyTypeDef",
    "ClientUpdateAliasResponseAliasTypeDef",
    "ClientUpdateAliasResponseTypeDef",
    "ClientUpdateAliasRoutingStrategyTypeDef",
    "ClientUpdateBuildResponseBuildTypeDef",
    "ClientUpdateBuildResponseTypeDef",
    "ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef",
    "ClientUpdateFleetAttributesResponseTypeDef",
    "ClientUpdateFleetCapacityResponseTypeDef",
    "ClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef",
    "ClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef",
    "ClientUpdateFleetPortSettingsResponseTypeDef",
    "ClientUpdateGameSessionQueueDestinationsTypeDef",
    "ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef",
    "ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef",
    "ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef",
    "ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef",
    "ClientUpdateGameSessionQueueResponseTypeDef",
    "ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef",
    "ClientUpdateGameSessionResponseGameSessionTypeDef",
    "ClientUpdateGameSessionResponseTypeDef",
    "ClientUpdateMatchmakingConfigurationGamePropertiesTypeDef",
    "ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef",
    "ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef",
    "ClientUpdateMatchmakingConfigurationResponseTypeDef",
    "ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef",
    "ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef",
    "ClientUpdateRuntimeConfigurationResponseTypeDef",
    "ClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef",
    "ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef",
    "ClientUpdateScriptResponseScriptStorageLocationTypeDef",
    "ClientUpdateScriptResponseScriptTypeDef",
    "ClientUpdateScriptResponseTypeDef",
    "ClientUpdateScriptStorageLocationTypeDef",
    "ClientValidateMatchmakingRuleSetResponseTypeDef",
    "DescribeFleetAttributesPaginatePaginationConfigTypeDef",
    "DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef",
    "DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    "DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef",
    "DescribeFleetAttributesPaginateResponseTypeDef",
    "DescribeFleetCapacityPaginatePaginationConfigTypeDef",
    "DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef",
    "DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef",
    "DescribeFleetCapacityPaginateResponseTypeDef",
    "DescribeFleetEventsPaginatePaginationConfigTypeDef",
    "DescribeFleetUtilizationPaginatePaginationConfigTypeDef",
    "DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef",
    "DescribeFleetUtilizationPaginateResponseTypeDef",
    "DescribeGameSessionDetailsPaginatePaginationConfigTypeDef",
    "DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef",
    "DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef",
    "DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef",
    "DescribeGameSessionDetailsPaginateResponseTypeDef",
    "DescribeGameSessionQueuesPaginatePaginationConfigTypeDef",
    "DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef",
    "DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef",
    "DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef",
    "DescribeGameSessionQueuesPaginateResponseTypeDef",
    "DescribeGameSessionsPaginatePaginationConfigTypeDef",
    "DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef",
    "DescribeGameSessionsPaginateResponseGameSessionsTypeDef",
    "DescribeGameSessionsPaginateResponseTypeDef",
    "DescribeInstancesPaginatePaginationConfigTypeDef",
    "DescribeInstancesPaginateResponseInstancesTypeDef",
    "DescribeInstancesPaginateResponseTypeDef",
    "DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef",
    "DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef",
    "DescribeMatchmakingConfigurationsPaginateResponseTypeDef",
    "DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef",
    "DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef",
    "DescribeMatchmakingRuleSetsPaginateResponseTypeDef",
    "DescribePlayerSessionsPaginatePaginationConfigTypeDef",
    "DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef",
    "DescribePlayerSessionsPaginateResponseTypeDef",
    "DescribeScalingPoliciesPaginatePaginationConfigTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef",
    "DescribeScalingPoliciesPaginateResponseTypeDef",
    "ListAliasesPaginatePaginationConfigTypeDef",
    "ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef",
    "ListAliasesPaginateResponseAliasesTypeDef",
    "ListAliasesPaginateResponseTypeDef",
    "ListBuildsPaginatePaginationConfigTypeDef",
    "ListBuildsPaginateResponseBuildsTypeDef",
    "ListBuildsPaginateResponseTypeDef",
    "ListFleetsPaginatePaginationConfigTypeDef",
    "ListFleetsPaginateResponseTypeDef",
    "SearchGameSessionsPaginatePaginationConfigTypeDef",
    "SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef",
    "SearchGameSessionsPaginateResponseGameSessionsTypeDef",
    "SearchGameSessionsPaginateResponseTypeDef",
)


_ClientCreateAliasResponseAliasRoutingStrategyTypeDef = TypedDict(
    "_ClientCreateAliasResponseAliasRoutingStrategyTypeDef",
    {"Type": str, "FleetId": str, "Message": str},
    total=False,
)


class ClientCreateAliasResponseAliasRoutingStrategyTypeDef(
    _ClientCreateAliasResponseAliasRoutingStrategyTypeDef
):
    """
    Type definition for `ClientCreateAliasResponseAlias` `RoutingStrategy`

    Alias configuration for the alias, including routing type and settings.

    - **Type** *(string) --*

      Type of routing strategy.

      Possible routing types include the following:

      * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
      active fleets.

      * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
      display a message to the user. A terminal alias throws a TerminalRoutingStrategyException
      with the  RoutingStrategy message embedded.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the alias points to.

    - **Message** *(string) --*

      Message text to be used with a terminal routing strategy.
    """


_ClientCreateAliasResponseAliasTypeDef = TypedDict(
    "_ClientCreateAliasResponseAliasTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": ClientCreateAliasResponseAliasRoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientCreateAliasResponseAliasTypeDef(_ClientCreateAliasResponseAliasTypeDef):
    """
    Type definition for `ClientCreateAliasResponse` `Alias`

    Object that describes the newly created alias record.

    - **AliasId** *(string) --*

      Unique identifier for an alias; alias IDs are unique within a region.

    - **Name** *(string) --*

      Descriptive label that is associated with an alias. Alias names do not need to be unique.

    - **AliasArn** *(string) --*

      Unique identifier for an alias; alias ARNs are unique across all regions.

    - **Description** *(string) --*

      Human-readable description of an alias.

    - **RoutingStrategy** *(dict) --*

      Alias configuration for the alias, including routing type and settings.

      - **Type** *(string) --*

        Type of routing strategy.

        Possible routing types include the following:

        * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
        active fleets.

        * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
        display a message to the user. A terminal alias throws a TerminalRoutingStrategyException
        with the  RoutingStrategy message embedded.

      - **FleetId** *(string) --*

        Unique identifier for a fleet that the alias points to.

      - **Message** *(string) --*

        Message text to be used with a terminal routing strategy.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **LastUpdatedTime** *(datetime) --*

      Time stamp indicating when this data object was last modified. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientCreateAliasResponseTypeDef = TypedDict(
    "_ClientCreateAliasResponseTypeDef",
    {"Alias": ClientCreateAliasResponseAliasTypeDef},
    total=False,
)


class ClientCreateAliasResponseTypeDef(_ClientCreateAliasResponseTypeDef):
    """
    Type definition for `ClientCreateAlias` `Response`

    Represents the returned data in response to a request action.

    - **Alias** *(dict) --*

      Object that describes the newly created alias record.

      - **AliasId** *(string) --*

        Unique identifier for an alias; alias IDs are unique within a region.

      - **Name** *(string) --*

        Descriptive label that is associated with an alias. Alias names do not need to be unique.

      - **AliasArn** *(string) --*

        Unique identifier for an alias; alias ARNs are unique across all regions.

      - **Description** *(string) --*

        Human-readable description of an alias.

      - **RoutingStrategy** *(dict) --*

        Alias configuration for the alias, including routing type and settings.

        - **Type** *(string) --*

          Type of routing strategy.

          Possible routing types include the following:

          * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
          active fleets.

          * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
          display a message to the user. A terminal alias throws a TerminalRoutingStrategyException
          with the  RoutingStrategy message embedded.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the alias points to.

        - **Message** *(string) --*

          Message text to be used with a terminal routing strategy.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **LastUpdatedTime** *(datetime) --*

        Time stamp indicating when this data object was last modified. Format is a number expressed
        in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientCreateAliasRoutingStrategyTypeDef = TypedDict(
    "_ClientCreateAliasRoutingStrategyTypeDef",
    {"Type": str, "FleetId": str, "Message": str},
    total=False,
)


class ClientCreateAliasRoutingStrategyTypeDef(_ClientCreateAliasRoutingStrategyTypeDef):
    """
    Type definition for `ClientCreateAlias` `RoutingStrategy`

    Object that specifies the fleet and routing type to use for the alias.

    - **Type** *(string) --*

      Type of routing strategy.

      Possible routing types include the following:

      * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active
      fleets.

      * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a
      message to the user. A terminal alias throws a TerminalRoutingStrategyException with the
      RoutingStrategy message embedded.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the alias points to.

    - **Message** *(string) --*

      Message text to be used with a terminal routing strategy.
    """


_ClientCreateBuildResponseBuildTypeDef = TypedDict(
    "_ClientCreateBuildResponseBuildTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": str,
        "SizeOnDisk": int,
        "OperatingSystem": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientCreateBuildResponseBuildTypeDef(_ClientCreateBuildResponseBuildTypeDef):
    """
    Type definition for `ClientCreateBuildResponse` `Build`

    The newly created build record, including a unique build ID and status.

    - **BuildId** *(string) --*

      Unique identifier for a build.

    - **Name** *(string) --*

      Descriptive label that is associated with a build. Build names do not need to be unique. It
      can be set using  CreateBuild or  UpdateBuild .

    - **Version** *(string) --*

      Version that is associated with a build or script. Version strings do not need to be
      unique. This value can be set using  CreateBuild or  UpdateBuild .

    - **Status** *(string) --*

      Current status of the build.

      Possible build statuses include the following:

      * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You
      cannot create fleets for builds that are in this status. When a build is successfully
      created, the build status is set to this value.

      * **READY** -- The game build has been successfully uploaded. You can now create new fleets
      for this build.

      * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.

    - **SizeOnDisk** *(integer) --*

      File size of the uploaded game build, expressed in bytes. When the build status is
      ``INITIALIZED`` , this value is 0.

    - **OperatingSystem** *(string) --*

      Operating system that the game server binaries are built to run on. This value determines
      the type of fleet resources that you can use for this build.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").
    """


_ClientCreateBuildResponseStorageLocationTypeDef = TypedDict(
    "_ClientCreateBuildResponseStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientCreateBuildResponseStorageLocationTypeDef(
    _ClientCreateBuildResponseStorageLocationTypeDef
):
    """
    Type definition for `ClientCreateBuildResponse` `StorageLocation`

    Amazon S3 location for your game build file, including bucket name and key.

    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.

    - **Key** *(string) --*

      Name of the zip file containing the build files or script files.

    - **RoleArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
      that allows Amazon GameLift to access the S3 bucket.

    - **ObjectVersion** *(string) --*

      Version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses
      this information when retrieving files from an S3 bucket that you own. Use this parameter
      to specify a specific version of the file; if not set, the latest version of the file is
      retrieved.
    """


_ClientCreateBuildResponseUploadCredentialsTypeDef = TypedDict(
    "_ClientCreateBuildResponseUploadCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str},
    total=False,
)


class ClientCreateBuildResponseUploadCredentialsTypeDef(
    _ClientCreateBuildResponseUploadCredentialsTypeDef
):
    """
    Type definition for `ClientCreateBuildResponse` `UploadCredentials`

    This element is returned only when the operation is called without a storage location. It
    contains credentials to use when you are uploading a build file to an Amazon S3 bucket that
    is owned by Amazon GameLift. Credentials have a limited life span. To refresh these
    credentials, call  RequestUploadCredentials .

    - **AccessKeyId** *(string) --*

      Temporary key allowing access to the Amazon GameLift S3 account.

    - **SecretAccessKey** *(string) --*

      Temporary secret key allowing access to the Amazon GameLift S3 account.

    - **SessionToken** *(string) --*

      Token used to associate a specific build ID with the files uploaded using these credentials.
    """


_ClientCreateBuildResponseTypeDef = TypedDict(
    "_ClientCreateBuildResponseTypeDef",
    {
        "Build": ClientCreateBuildResponseBuildTypeDef,
        "UploadCredentials": ClientCreateBuildResponseUploadCredentialsTypeDef,
        "StorageLocation": ClientCreateBuildResponseStorageLocationTypeDef,
    },
    total=False,
)


class ClientCreateBuildResponseTypeDef(_ClientCreateBuildResponseTypeDef):
    """
    Type definition for `ClientCreateBuild` `Response`

    Represents the returned data in response to a request action.

    - **Build** *(dict) --*

      The newly created build record, including a unique build ID and status.

      - **BuildId** *(string) --*

        Unique identifier for a build.

      - **Name** *(string) --*

        Descriptive label that is associated with a build. Build names do not need to be unique. It
        can be set using  CreateBuild or  UpdateBuild .

      - **Version** *(string) --*

        Version that is associated with a build or script. Version strings do not need to be
        unique. This value can be set using  CreateBuild or  UpdateBuild .

      - **Status** *(string) --*

        Current status of the build.

        Possible build statuses include the following:

        * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You
        cannot create fleets for builds that are in this status. When a build is successfully
        created, the build status is set to this value.

        * **READY** -- The game build has been successfully uploaded. You can now create new fleets
        for this build.

        * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.

      - **SizeOnDisk** *(integer) --*

        File size of the uploaded game build, expressed in bytes. When the build status is
        ``INITIALIZED`` , this value is 0.

      - **OperatingSystem** *(string) --*

        Operating system that the game server binaries are built to run on. This value determines
        the type of fleet resources that you can use for this build.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

    - **UploadCredentials** *(dict) --*

      This element is returned only when the operation is called without a storage location. It
      contains credentials to use when you are uploading a build file to an Amazon S3 bucket that
      is owned by Amazon GameLift. Credentials have a limited life span. To refresh these
      credentials, call  RequestUploadCredentials .

      - **AccessKeyId** *(string) --*

        Temporary key allowing access to the Amazon GameLift S3 account.

      - **SecretAccessKey** *(string) --*

        Temporary secret key allowing access to the Amazon GameLift S3 account.

      - **SessionToken** *(string) --*

        Token used to associate a specific build ID with the files uploaded using these credentials.

    - **StorageLocation** *(dict) --*

      Amazon S3 location for your game build file, including bucket name and key.

      - **Bucket** *(string) --*

        Amazon S3 bucket identifier. This is the name of the S3 bucket.

      - **Key** *(string) --*

        Name of the zip file containing the build files or script files.

      - **RoleArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
        that allows Amazon GameLift to access the S3 bucket.

      - **ObjectVersion** *(string) --*

        Version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses
        this information when retrieving files from an S3 bucket that you own. Use this parameter
        to specify a specific version of the file; if not set, the latest version of the file is
        retrieved.
    """


_ClientCreateBuildStorageLocationTypeDef = TypedDict(
    "_ClientCreateBuildStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientCreateBuildStorageLocationTypeDef(_ClientCreateBuildStorageLocationTypeDef):
    """
    Type definition for `ClientCreateBuild` `StorageLocation`

    Information indicating where your game build files are stored. Use this parameter only when
    creating a build with files stored in an Amazon S3 bucket that you own. The storage location must
    specify an Amazon S3 bucket name and key, as well as a the ARN for a role that you set up to
    allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket must be in the same region
    that you want to create a new build in.

    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.

    - **Key** *(string) --*

      Name of the zip file containing the build files or script files.

    - **RoleArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role that
      allows Amazon GameLift to access the S3 bucket.

    - **ObjectVersion** *(string) --*

      Version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses
      this information when retrieving files from an S3 bucket that you own. Use this parameter to
      specify a specific version of the file; if not set, the latest version of the file is retrieved.
    """


_ClientCreateFleetCertificateConfigurationTypeDef = TypedDict(
    "_ClientCreateFleetCertificateConfigurationTypeDef", {"CertificateType": str}
)


class ClientCreateFleetCertificateConfigurationTypeDef(
    _ClientCreateFleetCertificateConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFleet` `CertificateConfiguration`

    - **CertificateType** *(string) --* **[REQUIRED]**
    """


_ClientCreateFleetEC2InboundPermissionsTypeDef = TypedDict(
    "_ClientCreateFleetEC2InboundPermissionsTypeDef",
    {"FromPort": int, "ToPort": int, "IpRange": str, "Protocol": str},
)


class ClientCreateFleetEC2InboundPermissionsTypeDef(
    _ClientCreateFleetEC2InboundPermissionsTypeDef
):
    """
    Type definition for `ClientCreateFleet` `EC2InboundPermissions`

    A range of IP addresses and port settings that allow inbound traffic to connect to server
    processes on an Amazon GameLift. New game sessions that are started on the fleet are assigned
    an IP address/port number combination, which must fall into the fleet's allowed ranges. For
    fleets created with a custom game server, the ranges reflect the server's game session
    assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges,
    one for TCP messaging and one for UDP for use by the Realtime servers.

    - **FromPort** *(integer) --* **[REQUIRED]**

      Starting value for a range of allowed port numbers.

    - **ToPort** *(integer) --* **[REQUIRED]**

      Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value
      must be higher than ``FromPort`` .

    - **IpRange** *(string) --* **[REQUIRED]**

      Range of allowed IP addresses. This value must be expressed in CIDR notation. Example:
      "``000.000.000.000/[subnet mask]`` " or optionally the shortened version "``0.0.0.0/[subnet
      mask]`` ".

    - **Protocol** *(string) --* **[REQUIRED]**

      Network communication protocol used by the fleet.
    """


_ClientCreateFleetResourceCreationLimitPolicyTypeDef = TypedDict(
    "_ClientCreateFleetResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)


class ClientCreateFleetResourceCreationLimitPolicyTypeDef(
    _ClientCreateFleetResourceCreationLimitPolicyTypeDef
):
    """
    Type definition for `ClientCreateFleet` `ResourceCreationLimitPolicy`

    Policy that limits the number of game sessions an individual player can create over a span of
    time for this fleet.

    - **NewGameSessionsPerCreator** *(integer) --*

      Maximum number of game sessions that an individual can create during the policy period.

    - **PolicyPeriodInMinutes** *(integer) --*

      Time span used in evaluating the resource creation limit policy.
    """


_ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef",
    {"CertificateType": str},
    total=False,
)


class ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef(
    _ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFleetResponseFleetAttributes` `CertificateConfiguration`

    - **CertificateType** *(string) --*
    """


_ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)


class ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef(
    _ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef
):
    """
    Type definition for `ClientCreateFleetResponseFleetAttributes` `ResourceCreationLimitPolicy`

    Fleet policy to limit the number of game sessions an individual player can create over a
    span of time.

    - **NewGameSessionsPerCreator** *(integer) --*

      Maximum number of game sessions that an individual can create during the policy period.

    - **PolicyPeriodInMinutes** *(integer) --*

      Time span used in evaluating the resource creation limit policy.
    """


_ClientCreateFleetResponseFleetAttributesTypeDef = TypedDict(
    "_ClientCreateFleetResponseFleetAttributesTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "FleetType": str,
        "InstanceType": str,
        "Description": str,
        "Name": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": str,
        "BuildId": str,
        "ScriptId": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "NewGameSessionProtectionPolicy": str,
        "OperatingSystem": str,
        "ResourceCreationLimitPolicy": ClientCreateFleetResponseFleetAttributesResourceCreationLimitPolicyTypeDef,
        "MetricGroups": List[str],
        "StoppedActions": List[str],
        "InstanceRoleArn": str,
        "CertificateConfiguration": ClientCreateFleetResponseFleetAttributesCertificateConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateFleetResponseFleetAttributesTypeDef(
    _ClientCreateFleetResponseFleetAttributesTypeDef
):
    """
    Type definition for `ClientCreateFleetResponse` `FleetAttributes`

    Properties for the newly created fleet.

    - **FleetId** *(string) --*

      Unique identifier for a fleet.

    - **FleetArn** *(string) --*

      Identifier for a fleet that is unique across all regions.

    - **FleetType** *(string) --*

      Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may be
      interrupted with a two-minute notification.

    - **InstanceType** *(string) --*

      EC2 instance type indicating the computing resources of each instance in the fleet,
      including CPU, memory, storage, and networking capacity. See `Amazon EC2 Instance Types
      <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.

    - **Description** *(string) --*

      Human-readable description of the fleet.

    - **Name** *(string) --*

      Descriptive label that is associated with a fleet. Fleet names do not need to be unique.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **Status** *(string) --*

      Current status of the fleet.

      Possible fleet statuses include the following:

      * **NEW** -- A new fleet has been defined and desired instances is set to 1.

      * **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** -- Amazon GameLift is setting up the new
      fleet, creating new instances with the game build or Realtime script and starting server
      processes.

      * **ACTIVE** -- Hosts can now accept game sessions.

      * **ERROR** -- An error occurred when downloading, validating, building, or activating the
      fleet.

      * **DELETING** -- Hosts are responding to a delete fleet request.

      * **TERMINATED** -- The fleet no longer exists.

    - **BuildId** *(string) --*

      Unique identifier for a build.

    - **ScriptId** *(string) --*

      Unique identifier for a Realtime script.

    - **ServerLaunchPath** *(string) --*

      Path to a game server executable in the fleet's build, specified for fleets created before
      2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after this date
      are specified in the fleet's  RuntimeConfiguration .

    - **ServerLaunchParameters** *(string) --*

      Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK v.
      0.12.16). Server launch parameters for fleets created after this date are specified in the
      fleet's  RuntimeConfiguration .

    - **LogPaths** *(list) --*

      Location of default log files. When a server process is shut down, Amazon GameLift captures
      and stores any log files in this location. These logs are in addition to game session logs;
      see more on game session logs in the `Amazon GameLift Developer Guide
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-api-server-code>`__
      . If no default log path for a fleet is specified, Amazon GameLift automatically uploads
      logs that are stored on each instance at ``C:\\game\\logs`` (for Windows) or
      ``/local/game/logs`` (for Linux). Use the Amazon GameLift console to access stored logs.

      - *(string) --*

    - **NewGameSessionProtectionPolicy** *(string) --*

      Type of game session protection to set for all new instances started in the fleet.

      * **NoProtection** -- The game session can be terminated during a scale-down event.

      * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be
      terminated during a scale-down event.

    - **OperatingSystem** *(string) --*

      Operating system of the fleet's computing resources. A fleet's operating system depends on
      the OS specified for the build that is deployed on this fleet.

    - **ResourceCreationLimitPolicy** *(dict) --*

      Fleet policy to limit the number of game sessions an individual player can create over a
      span of time.

      - **NewGameSessionsPerCreator** *(integer) --*

        Maximum number of game sessions that an individual can create during the policy period.

      - **PolicyPeriodInMinutes** *(integer) --*

        Time span used in evaluating the resource creation limit policy.

    - **MetricGroups** *(list) --*

      Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view
      metrics for an individual fleet or aggregated metrics for fleets that are in a fleet metric
      group. A fleet can be included in only one metric group at a time.

      - *(string) --*

    - **StoppedActions** *(list) --*

      List of fleet actions that have been suspended using  StopFleetActions . This includes
      auto-scaling.

      - *(string) --*

    - **InstanceRoleArn** *(string) --*

      Unique identifier for an AWS IAM role that manages access to your AWS services. With an
      instance role ARN set, any application that runs on an instance in this fleet can assume
      the role, including install scripts, server processes, daemons (background processes).
      Create a role or look up a role's ARN using the `IAM dashboard
      <https://console.aws.amazon.com/iam/>`__ in the AWS Management Console. Learn more about
      using on-box credentials for your game servers at `Access external resources from a game
      server
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`__
      .

    - **CertificateConfiguration** *(dict) --*

      - **CertificateType** *(string) --*
    """


_ClientCreateFleetResponseTypeDef = TypedDict(
    "_ClientCreateFleetResponseTypeDef",
    {"FleetAttributes": ClientCreateFleetResponseFleetAttributesTypeDef},
    total=False,
)


class ClientCreateFleetResponseTypeDef(_ClientCreateFleetResponseTypeDef):
    """
    Type definition for `ClientCreateFleet` `Response`

    Represents the returned data in response to a request action.

    - **FleetAttributes** *(dict) --*

      Properties for the newly created fleet.

      - **FleetId** *(string) --*

        Unique identifier for a fleet.

      - **FleetArn** *(string) --*

        Identifier for a fleet that is unique across all regions.

      - **FleetType** *(string) --*

        Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may be
        interrupted with a two-minute notification.

      - **InstanceType** *(string) --*

        EC2 instance type indicating the computing resources of each instance in the fleet,
        including CPU, memory, storage, and networking capacity. See `Amazon EC2 Instance Types
        <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.

      - **Description** *(string) --*

        Human-readable description of the fleet.

      - **Name** *(string) --*

        Descriptive label that is associated with a fleet. Fleet names do not need to be unique.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **TerminationTime** *(datetime) --*

        Time stamp indicating when this data object was terminated. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **Status** *(string) --*

        Current status of the fleet.

        Possible fleet statuses include the following:

        * **NEW** -- A new fleet has been defined and desired instances is set to 1.

        * **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** -- Amazon GameLift is setting up the new
        fleet, creating new instances with the game build or Realtime script and starting server
        processes.

        * **ACTIVE** -- Hosts can now accept game sessions.

        * **ERROR** -- An error occurred when downloading, validating, building, or activating the
        fleet.

        * **DELETING** -- Hosts are responding to a delete fleet request.

        * **TERMINATED** -- The fleet no longer exists.

      - **BuildId** *(string) --*

        Unique identifier for a build.

      - **ScriptId** *(string) --*

        Unique identifier for a Realtime script.

      - **ServerLaunchPath** *(string) --*

        Path to a game server executable in the fleet's build, specified for fleets created before
        2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after this date
        are specified in the fleet's  RuntimeConfiguration .

      - **ServerLaunchParameters** *(string) --*

        Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK v.
        0.12.16). Server launch parameters for fleets created after this date are specified in the
        fleet's  RuntimeConfiguration .

      - **LogPaths** *(list) --*

        Location of default log files. When a server process is shut down, Amazon GameLift captures
        and stores any log files in this location. These logs are in addition to game session logs;
        see more on game session logs in the `Amazon GameLift Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-api-server-code>`__
        . If no default log path for a fleet is specified, Amazon GameLift automatically uploads
        logs that are stored on each instance at ``C:\\game\\logs`` (for Windows) or
        ``/local/game/logs`` (for Linux). Use the Amazon GameLift console to access stored logs.

        - *(string) --*

      - **NewGameSessionProtectionPolicy** *(string) --*

        Type of game session protection to set for all new instances started in the fleet.

        * **NoProtection** -- The game session can be terminated during a scale-down event.

        * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be
        terminated during a scale-down event.

      - **OperatingSystem** *(string) --*

        Operating system of the fleet's computing resources. A fleet's operating system depends on
        the OS specified for the build that is deployed on this fleet.

      - **ResourceCreationLimitPolicy** *(dict) --*

        Fleet policy to limit the number of game sessions an individual player can create over a
        span of time.

        - **NewGameSessionsPerCreator** *(integer) --*

          Maximum number of game sessions that an individual can create during the policy period.

        - **PolicyPeriodInMinutes** *(integer) --*

          Time span used in evaluating the resource creation limit policy.

      - **MetricGroups** *(list) --*

        Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view
        metrics for an individual fleet or aggregated metrics for fleets that are in a fleet metric
        group. A fleet can be included in only one metric group at a time.

        - *(string) --*

      - **StoppedActions** *(list) --*

        List of fleet actions that have been suspended using  StopFleetActions . This includes
        auto-scaling.

        - *(string) --*

      - **InstanceRoleArn** *(string) --*

        Unique identifier for an AWS IAM role that manages access to your AWS services. With an
        instance role ARN set, any application that runs on an instance in this fleet can assume
        the role, including install scripts, server processes, daemons (background processes).
        Create a role or look up a role's ARN using the `IAM dashboard
        <https://console.aws.amazon.com/iam/>`__ in the AWS Management Console. Learn more about
        using on-box credentials for your game servers at `Access external resources from a game
        server
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`__
        .

      - **CertificateConfiguration** *(dict) --*

        - **CertificateType** *(string) --*
    """


_RequiredClientCreateFleetRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_RequiredClientCreateFleetRuntimeConfigurationServerProcessesTypeDef",
    {"LaunchPath": str, "ConcurrentExecutions": int},
)
_OptionalClientCreateFleetRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_OptionalClientCreateFleetRuntimeConfigurationServerProcessesTypeDef",
    {"Parameters": str},
    total=False,
)


class ClientCreateFleetRuntimeConfigurationServerProcessesTypeDef(
    _RequiredClientCreateFleetRuntimeConfigurationServerProcessesTypeDef,
    _OptionalClientCreateFleetRuntimeConfigurationServerProcessesTypeDef,
):
    """
    Type definition for `ClientCreateFleetRuntimeConfiguration` `ServerProcesses`

    A set of instructions for launching server processes on each instance in a fleet. Server
    processes run either a custom game build executable or a Realtime Servers script. Each
    instruction set identifies the location of the custom game build executable or Realtime
    launch script, optional launch parameters, and the number of server processes with this
    configuration to maintain concurrently on the instance. Server process configurations make up
    a fleet's ``  RuntimeConfiguration `` .

    - **LaunchPath** *(string) --* **[REQUIRED]**

      Location of the server executable in a custom game build or the name of the Realtime script
      file that contains the ``Init()`` function. Game builds and Realtime scripts are installed
      on instances at the root:

      * Windows (for custom game builds only): ``C:\\game`` . Example:
      "``C:\\game\\MyGame\\server.exe`` "

      * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
      "``/local/game/MyRealtimeScript.js`` "

    - **Parameters** *(string) --*

      Optional list of parameters to pass to the server executable or Realtime script on launch.

    - **ConcurrentExecutions** *(integer) --* **[REQUIRED]**

      Number of server processes using this configuration to run concurrently on an instance.
    """


_ClientCreateFleetRuntimeConfigurationTypeDef = TypedDict(
    "_ClientCreateFleetRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[
            ClientCreateFleetRuntimeConfigurationServerProcessesTypeDef
        ],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)


class ClientCreateFleetRuntimeConfigurationTypeDef(
    _ClientCreateFleetRuntimeConfigurationTypeDef
):
    """
    Type definition for `ClientCreateFleet` `RuntimeConfiguration`

    Instructions for launching server processes on each instance in the fleet. Server processes run
    either a custom game build executable or a Realtime Servers script. The run-time configuration
    lists the types of server processes to run on an instance and includes the following
    configuration settings: the server executable or launch script file, launch parameters, and the
    number of processes to run concurrently on each instance. A CreateFleet request must include a
    run-time configuration with at least one server process configuration.

    - **ServerProcesses** *(list) --*

      Collection of server process configurations that describe which server processes to run on each
      instance in a fleet.

      - *(dict) --*

        A set of instructions for launching server processes on each instance in a fleet. Server
        processes run either a custom game build executable or a Realtime Servers script. Each
        instruction set identifies the location of the custom game build executable or Realtime
        launch script, optional launch parameters, and the number of server processes with this
        configuration to maintain concurrently on the instance. Server process configurations make up
        a fleet's ``  RuntimeConfiguration `` .

        - **LaunchPath** *(string) --* **[REQUIRED]**

          Location of the server executable in a custom game build or the name of the Realtime script
          file that contains the ``Init()`` function. Game builds and Realtime scripts are installed
          on instances at the root:

          * Windows (for custom game builds only): ``C:\\game`` . Example:
          "``C:\\game\\MyGame\\server.exe`` "

          * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
          "``/local/game/MyRealtimeScript.js`` "

        - **Parameters** *(string) --*

          Optional list of parameters to pass to the server executable or Realtime script on launch.

        - **ConcurrentExecutions** *(integer) --* **[REQUIRED]**

          Number of server processes using this configuration to run concurrently on an instance.

    - **MaxConcurrentGameSessionActivations** *(integer) --*

      Maximum number of game sessions with status ``ACTIVATING`` to allow on an instance
      simultaneously. This setting limits the amount of instance resources that can be used for new
      game activations at any one time.

    - **GameSessionActivationTimeoutSeconds** *(integer) --*

      Maximum amount of time (in seconds) that a game session can remain in status ``ACTIVATING`` .
      If the game session is not active before the timeout, activation is terminated and the game
      session status is changed to ``TERMINATED`` .
    """


_ClientCreateGameSessionGamePropertiesTypeDef = TypedDict(
    "_ClientCreateGameSessionGamePropertiesTypeDef", {"Key": str, "Value": str}
)


class ClientCreateGameSessionGamePropertiesTypeDef(
    _ClientCreateGameSessionGamePropertiesTypeDef
):
    """
    Type definition for `ClientCreateGameSession` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a game
    session request, these properties communicate details to be used when setting up the new game
    session, such as to specify a game mode, level, or map. Game properties are passed to the game
    server process when initiating a new game session; the server process uses the properties as
    appropriate. For more information, see the `Amazon GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --* **[REQUIRED]**

      Game property identifier.

    - **Value** *(string) --* **[REQUIRED]**

      Game property value.
    """


_ClientCreateGameSessionQueueDestinationsTypeDef = TypedDict(
    "_ClientCreateGameSessionQueueDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)


class ClientCreateGameSessionQueueDestinationsTypeDef(
    _ClientCreateGameSessionQueueDestinationsTypeDef
):
    """
    Type definition for `ClientCreateGameSessionQueue` `Destinations`

    Fleet designated in a game session queue. Requests for new game sessions in the queue are
    fulfilled by starting a new game session on any destination configured for a queue.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **DestinationArn** *(string) --*

      Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID
      or alias ID and a region name, provide a unique identifier across all regions.
    """


_ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "_ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef(
    _ClientCreateGameSessionQueuePlayerLatencyPoliciesTypeDef
):
    """
    Type definition for `ClientCreateGameSessionQueue` `PlayerLatencyPolicies`

    Queue setting that determines the highest latency allowed for individual players when placing a
    game session. When a latency policy is in force, a game session cannot be placed at any
    destination in a region where a player is reporting latency higher than the cap. Latency
    policies are only enforced when the placement request contains player latency information.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

      The maximum latency value that is allowed for any player, in milliseconds. All policies must
      have a value set for this property.

    - **PolicyDurationSeconds** *(integer) --*

      The length of time, in seconds, that the policy is enforced while placing a new game session.
      A null value for this property means that the policy is enforced until the queue times out.
    """


_ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef = TypedDict(
    "_ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)


class ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef(
    _ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef
):
    """
    Type definition for `ClientCreateGameSessionQueueResponseGameSessionQueue` `Destinations`

    Fleet designated in a game session queue. Requests for new game sessions in the queue are
    fulfilled by starting a new game session on any destination configured for a queue.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **DestinationArn** *(string) --*

      Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
      fleet ID or alias ID and a region name, provide a unique identifier across all regions.
    """


_ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "_ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef(
    _ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef
):
    """
    Type definition for `ClientCreateGameSessionQueueResponseGameSessionQueue` `PlayerLatencyPolicies`

    Queue setting that determines the highest latency allowed for individual players when
    placing a game session. When a latency policy is in force, a game session cannot be
    placed at any destination in a region where a player is reporting latency higher than the
    cap. Latency policies are only enforced when the placement request contains player
    latency information.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

      The maximum latency value that is allowed for any player, in milliseconds. All policies
      must have a value set for this property.

    - **PolicyDurationSeconds** *(integer) --*

      The length of time, in seconds, that the policy is enforced while placing a new game
      session. A null value for this property means that the policy is enforced until the
      queue times out.
    """


_ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef = TypedDict(
    "_ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List[
            ClientCreateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef
        ],
        "Destinations": List[
            ClientCreateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef
        ],
    },
    total=False,
)


class ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef(
    _ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef
):
    """
    Type definition for `ClientCreateGameSessionQueueResponse` `GameSessionQueue`

    Object that describes the newly created game session queue.

    - **Name** *(string) --*

      Descriptive label that is associated with game session queue. Queue names must be unique
      within each region.

    - **GameSessionQueueArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned
      to a game session queue and uniquely identifies it. Format is
      ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` .

    - **TimeoutInSeconds** *(integer) --*

      Maximum time, in seconds, that a new game session placement request remains in the queue.
      When a request exceeds this time, the game session placement changes to a ``TIMED_OUT``
      status.

    - **PlayerLatencyPolicies** *(list) --*

      Collection of latency policies to apply when processing game sessions placement requests
      with player latency information. Multiple policies are evaluated in order of the maximum
      latency value, starting with the lowest latency values. With just one policy, it is
      enforced at the start of the game session placement for the duration period. With multiple
      policies, each policy is enforced consecutively for its duration period. For example, a
      queue might enforce a 60-second policy followed by a 120-second policy, and then no policy
      for the remainder of the placement.

      - *(dict) --*

        Queue setting that determines the highest latency allowed for individual players when
        placing a game session. When a latency policy is in force, a game session cannot be
        placed at any destination in a region where a player is reporting latency higher than the
        cap. Latency policies are only enforced when the placement request contains player
        latency information.

        *  CreateGameSessionQueue

        *  DescribeGameSessionQueues

        *  UpdateGameSessionQueue

        *  DeleteGameSessionQueue

        - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

          The maximum latency value that is allowed for any player, in milliseconds. All policies
          must have a value set for this property.

        - **PolicyDurationSeconds** *(integer) --*

          The length of time, in seconds, that the policy is enforced while placing a new game
          session. A null value for this property means that the policy is enforced until the
          queue times out.

    - **Destinations** *(list) --*

      List of fleets that can be used to fulfill game session placement requests in the queue.
      Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed
      in default preference order.

      - *(dict) --*

        Fleet designated in a game session queue. Requests for new game sessions in the queue are
        fulfilled by starting a new game session on any destination configured for a queue.

        *  CreateGameSessionQueue

        *  DescribeGameSessionQueues

        *  UpdateGameSessionQueue

        *  DeleteGameSessionQueue

        - **DestinationArn** *(string) --*

          Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
          fleet ID or alias ID and a region name, provide a unique identifier across all regions.
    """


_ClientCreateGameSessionQueueResponseTypeDef = TypedDict(
    "_ClientCreateGameSessionQueueResponseTypeDef",
    {"GameSessionQueue": ClientCreateGameSessionQueueResponseGameSessionQueueTypeDef},
    total=False,
)


class ClientCreateGameSessionQueueResponseTypeDef(
    _ClientCreateGameSessionQueueResponseTypeDef
):
    """
    Type definition for `ClientCreateGameSessionQueue` `Response`

    Represents the returned data in response to a request action.

    - **GameSessionQueue** *(dict) --*

      Object that describes the newly created game session queue.

      - **Name** *(string) --*

        Descriptive label that is associated with game session queue. Queue names must be unique
        within each region.

      - **GameSessionQueueArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned
        to a game session queue and uniquely identifies it. Format is
        ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` .

      - **TimeoutInSeconds** *(integer) --*

        Maximum time, in seconds, that a new game session placement request remains in the queue.
        When a request exceeds this time, the game session placement changes to a ``TIMED_OUT``
        status.

      - **PlayerLatencyPolicies** *(list) --*

        Collection of latency policies to apply when processing game sessions placement requests
        with player latency information. Multiple policies are evaluated in order of the maximum
        latency value, starting with the lowest latency values. With just one policy, it is
        enforced at the start of the game session placement for the duration period. With multiple
        policies, each policy is enforced consecutively for its duration period. For example, a
        queue might enforce a 60-second policy followed by a 120-second policy, and then no policy
        for the remainder of the placement.

        - *(dict) --*

          Queue setting that determines the highest latency allowed for individual players when
          placing a game session. When a latency policy is in force, a game session cannot be
          placed at any destination in a region where a player is reporting latency higher than the
          cap. Latency policies are only enforced when the placement request contains player
          latency information.

          *  CreateGameSessionQueue

          *  DescribeGameSessionQueues

          *  UpdateGameSessionQueue

          *  DeleteGameSessionQueue

          - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

            The maximum latency value that is allowed for any player, in milliseconds. All policies
            must have a value set for this property.

          - **PolicyDurationSeconds** *(integer) --*

            The length of time, in seconds, that the policy is enforced while placing a new game
            session. A null value for this property means that the policy is enforced until the
            queue times out.

      - **Destinations** *(list) --*

        List of fleets that can be used to fulfill game session placement requests in the queue.
        Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed
        in default preference order.

        - *(dict) --*

          Fleet designated in a game session queue. Requests for new game sessions in the queue are
          fulfilled by starting a new game session on any destination configured for a queue.

          *  CreateGameSessionQueue

          *  DescribeGameSessionQueues

          *  UpdateGameSessionQueue

          *  DeleteGameSessionQueue

          - **DestinationArn** *(string) --*

            Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
            fleet ID or alias ID and a region name, provide a unique identifier across all regions.
    """


_ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef = TypedDict(
    "_ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef(
    _ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef
):
    """
    Type definition for `ClientCreateGameSessionResponseGameSession` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a
    game session request, these properties communicate details to be used when setting up the
    new game session, such as to specify a game mode, level, or map. Game properties are
    passed to the game server process when initiating a new game session; the server process
    uses the properties as appropriate. For more information, see the `Amazon GameLift
    Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientCreateGameSessionResponseGameSessionTypeDef = TypedDict(
    "_ClientCreateGameSessionResponseGameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": str,
        "StatusReason": str,
        "GameProperties": List[
            ClientCreateGameSessionResponseGameSessionGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": str,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class ClientCreateGameSessionResponseGameSessionTypeDef(
    _ClientCreateGameSessionResponseGameSessionTypeDef
):
    """
    Type definition for `ClientCreateGameSessionResponse` `GameSession`

    Object that describes the newly created game session record.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. A game session ARN has the following format:
      ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
      token>`` .

    - **Name** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to be
      unique.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **CurrentPlayerSessionCount** *(integer) --*

      Number of players currently in the game session.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **Status** *(string) --*

      Current status of the game session. A game session must have an ``ACTIVE`` status to have
      player sessions.

    - **StatusReason** *(string) --*

      Provides additional information about game session status. ``INTERRUPTED`` indicates that
      the game session was hosted on a spot instance that was reclaimed, causing the active game
      session to be terminated.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These properties
      are passed to a game server process in the  GameSession object with a request to start a
      new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). You can search for active game sessions based on this custom data with
      SearchGameSessions .

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in a
        game session request, these properties communicate details to be used when setting up the
        new game session, such as to specify a game mode, level, or map. Game properties are
        passed to the game server process when initiating a new game session; the server process
        uses the properties as appropriate. For more information, see the `Amazon GameLift
        Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **PlayerSessionCreationPolicy** *(string) --*

      Indicates whether or not the game session is accepting new players.

    - **CreatorId** *(string) --*

      Unique identifier for a player. This ID is used to enforce a resource protection policy (if
      one exists), that limits the number of game sessions a player can create.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information about the matchmaking process that was used to create the game session. It is
      in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
      contains data on all players assigned to the match, including player attributes and team
      assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      . Matchmaker data is useful when requesting match backfills, and is updated whenever new
      players are added during a successful backfill (see  StartMatchBackfill ).
    """


_ClientCreateGameSessionResponseTypeDef = TypedDict(
    "_ClientCreateGameSessionResponseTypeDef",
    {"GameSession": ClientCreateGameSessionResponseGameSessionTypeDef},
    total=False,
)


class ClientCreateGameSessionResponseTypeDef(_ClientCreateGameSessionResponseTypeDef):
    """
    Type definition for `ClientCreateGameSession` `Response`

    Represents the returned data in response to a request action.

    - **GameSession** *(dict) --*

      Object that describes the newly created game session record.

      - **GameSessionId** *(string) --*

        Unique identifier for the game session. A game session ARN has the following format:
        ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
        token>`` .

      - **Name** *(string) --*

        Descriptive label that is associated with a game session. Session names do not need to be
        unique.

      - **FleetId** *(string) --*

        Unique identifier for a fleet that the game session is running on.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **TerminationTime** *(datetime) --*

        Time stamp indicating when this data object was terminated. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **CurrentPlayerSessionCount** *(integer) --*

        Number of players currently in the game session.

      - **MaximumPlayerSessionCount** *(integer) --*

        Maximum number of players that can be connected simultaneously to the game session.

      - **Status** *(string) --*

        Current status of the game session. A game session must have an ``ACTIVE`` status to have
        player sessions.

      - **StatusReason** *(string) --*

        Provides additional information about game session status. ``INTERRUPTED`` indicates that
        the game session was hosted on a spot instance that was reclaimed, causing the active game
        session to be terminated.

      - **GameProperties** *(list) --*

        Set of custom properties for a game session, formatted as key:value pairs. These properties
        are passed to a game server process in the  GameSession object with a request to start a
        new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ). You can search for active game sessions based on this custom data with
        SearchGameSessions .

        - *(dict) --*

          Set of key-value pairs that contain information about a game session. When included in a
          game session request, these properties communicate details to be used when setting up the
          new game session, such as to specify a game mode, level, or map. Game properties are
          passed to the game server process when initiating a new game session; the server process
          uses the properties as appropriate. For more information, see the `Amazon GameLift
          Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
          .

          - **Key** *(string) --*

            Game property identifier.

          - **Value** *(string) --*

            Game property value.

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number.

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number.

      - **PlayerSessionCreationPolicy** *(string) --*

        Indicates whether or not the game session is accepting new players.

      - **CreatorId** *(string) --*

        Unique identifier for a player. This ID is used to enforce a resource protection policy (if
        one exists), that limits the number of game sessions a player can create.

      - **GameSessionData** *(string) --*

        Set of custom game session properties, formatted as a single string value. This data is
        passed to a game server process in the  GameSession object with a request to start a new
        game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ).

      - **MatchmakerData** *(string) --*

        Information about the matchmaking process that was used to create the game session. It is
        in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
        contains data on all players assigned to the match, including player attributes and team
        assignments. For more details on matchmaker data, see `Match Data
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
        . Matchmaker data is useful when requesting match backfills, and is updated whenever new
        players are added during a successful backfill (see  StartMatchBackfill ).
    """


_ClientCreateMatchmakingConfigurationGamePropertiesTypeDef = TypedDict(
    "_ClientCreateMatchmakingConfigurationGamePropertiesTypeDef",
    {"Key": str, "Value": str},
)


class ClientCreateMatchmakingConfigurationGamePropertiesTypeDef(
    _ClientCreateMatchmakingConfigurationGamePropertiesTypeDef
):
    """
    Type definition for `ClientCreateMatchmakingConfiguration` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a game
    session request, these properties communicate details to be used when setting up the new game
    session, such as to specify a game mode, level, or map. Game properties are passed to the game
    server process when initiating a new game session; the server process uses the properties as
    appropriate. For more information, see the `Amazon GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --* **[REQUIRED]**

      Game property identifier.

    - **Value** *(string) --* **[REQUIRED]**

      Game property value.
    """


_ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef = TypedDict(
    "_ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef(
    _ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef
):
    """
    Type definition for `ClientCreateMatchmakingConfigurationResponseConfiguration` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a
    game session request, these properties communicate details to be used when setting up the
    new game session, such as to specify a game mode, level, or map. Game properties are
    passed to the game server process when initiating a new game session; the server process
    uses the properties as appropriate. For more information, see the `Amazon GameLift
    Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef = TypedDict(
    "_ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef",
    {
        "Name": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List[
            ClientCreateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef
        ],
        "GameSessionData": str,
        "BackfillMode": str,
    },
    total=False,
)


class ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef(
    _ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef
):
    """
    Type definition for `ClientCreateMatchmakingConfigurationResponse` `Configuration`

    Object that describes the newly created matchmaking configuration.

    - **Name** *(string) --*

      Unique identifier for a matchmaking configuration. This name is used to identify the
      configuration associated with a matchmaking request or ticket.

    - **Description** *(string) --*

      Descriptive label that is associated with matchmaking configuration.

    - **GameSessionQueueArns** *(list) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned
      to a game session queue and uniquely identifies it. Format is
      ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` . These queues
      are used when placing game sessions for matches that are created with this matchmaking
      configuration. Queues can be located in any region.

      - *(string) --*

    - **RequestTimeoutSeconds** *(integer) --*

      Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing
      out. Requests that fail due to timing out can be resubmitted as needed.

    - **AcceptanceTimeoutSeconds** *(integer) --*

      Length of time (in seconds) to wait for players to accept a proposed match. If any player
      rejects the match or fails to accept before the timeout, the ticket continues to look for
      an acceptable match.

    - **AcceptanceRequired** *(boolean) --*

      Flag that determines whether a match that was created with this configuration must be
      accepted by the matched players. To require acceptance, set to TRUE.

    - **RuleSetName** *(string) --*

      Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking
      configuration can only use rule sets that are defined in the same region.

    - **NotificationTarget** *(string) --*

      SNS topic ARN that is set up to receive matchmaking notifications.

    - **AdditionalPlayerCount** *(integer) --*

      Number of player slots in a match to keep open for future players. For example, if the
      configuration's rule set specifies a match for a single 12-person team, and the additional
      player count is set to 2, only 10 players are selected for the match.

    - **CustomEventData** *(string) --*

      Information to attach to all events related to the matchmaking configuration.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These properties
      are passed to a game server process in the  GameSession object with a request to start a
      new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). This information is added to the new  GameSession object that is created for a
      successful match.

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in a
        game session request, these properties communicate details to be used when setting up the
        new game session, such as to specify a game mode, level, or map. Game properties are
        passed to the game server process when initiating a new game session; the server process
        uses the properties as appropriate. For more information, see the `Amazon GameLift
        Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). This information is added to the new  GameSession object that is created for a
      successful match.

    - **BackfillMode** *(string) --*

      Method used to backfill game sessions created with this matchmaking configuration. MANUAL
      indicates that the game makes backfill requests or does not use the match backfill feature.
      AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever a game
      session has one or more open slots. Learn more about manual and automatic backfill in
      `Backfill Existing Games with FlexMatch
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-backfill.html>`__ .
    """


_ClientCreateMatchmakingConfigurationResponseTypeDef = TypedDict(
    "_ClientCreateMatchmakingConfigurationResponseTypeDef",
    {"Configuration": ClientCreateMatchmakingConfigurationResponseConfigurationTypeDef},
    total=False,
)


class ClientCreateMatchmakingConfigurationResponseTypeDef(
    _ClientCreateMatchmakingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientCreateMatchmakingConfiguration` `Response`

    Represents the returned data in response to a request action.

    - **Configuration** *(dict) --*

      Object that describes the newly created matchmaking configuration.

      - **Name** *(string) --*

        Unique identifier for a matchmaking configuration. This name is used to identify the
        configuration associated with a matchmaking request or ticket.

      - **Description** *(string) --*

        Descriptive label that is associated with matchmaking configuration.

      - **GameSessionQueueArns** *(list) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned
        to a game session queue and uniquely identifies it. Format is
        ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` . These queues
        are used when placing game sessions for matches that are created with this matchmaking
        configuration. Queues can be located in any region.

        - *(string) --*

      - **RequestTimeoutSeconds** *(integer) --*

        Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing
        out. Requests that fail due to timing out can be resubmitted as needed.

      - **AcceptanceTimeoutSeconds** *(integer) --*

        Length of time (in seconds) to wait for players to accept a proposed match. If any player
        rejects the match or fails to accept before the timeout, the ticket continues to look for
        an acceptable match.

      - **AcceptanceRequired** *(boolean) --*

        Flag that determines whether a match that was created with this configuration must be
        accepted by the matched players. To require acceptance, set to TRUE.

      - **RuleSetName** *(string) --*

        Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking
        configuration can only use rule sets that are defined in the same region.

      - **NotificationTarget** *(string) --*

        SNS topic ARN that is set up to receive matchmaking notifications.

      - **AdditionalPlayerCount** *(integer) --*

        Number of player slots in a match to keep open for future players. For example, if the
        configuration's rule set specifies a match for a single 12-person team, and the additional
        player count is set to 2, only 10 players are selected for the match.

      - **CustomEventData** *(string) --*

        Information to attach to all events related to the matchmaking configuration.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **GameProperties** *(list) --*

        Set of custom properties for a game session, formatted as key:value pairs. These properties
        are passed to a game server process in the  GameSession object with a request to start a
        new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ). This information is added to the new  GameSession object that is created for a
        successful match.

        - *(dict) --*

          Set of key-value pairs that contain information about a game session. When included in a
          game session request, these properties communicate details to be used when setting up the
          new game session, such as to specify a game mode, level, or map. Game properties are
          passed to the game server process when initiating a new game session; the server process
          uses the properties as appropriate. For more information, see the `Amazon GameLift
          Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
          .

          - **Key** *(string) --*

            Game property identifier.

          - **Value** *(string) --*

            Game property value.

      - **GameSessionData** *(string) --*

        Set of custom game session properties, formatted as a single string value. This data is
        passed to a game server process in the  GameSession object with a request to start a new
        game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ). This information is added to the new  GameSession object that is created for a
        successful match.

      - **BackfillMode** *(string) --*

        Method used to backfill game sessions created with this matchmaking configuration. MANUAL
        indicates that the game makes backfill requests or does not use the match backfill feature.
        AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever a game
        session has one or more open slots. Learn more about manual and automatic backfill in
        `Backfill Existing Games with FlexMatch
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-backfill.html>`__ .
    """


_ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef = TypedDict(
    "_ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef",
    {"RuleSetName": str, "RuleSetBody": str, "CreationTime": datetime},
    total=False,
)


class ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef(
    _ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef
):
    """
    Type definition for `ClientCreateMatchmakingRuleSetResponse` `RuleSet`

    Object that describes the newly created matchmaking rule set.

    - **RuleSetName** *(string) --*

      Unique identifier for a matchmaking rule set

    - **RuleSetBody** *(string) --*

      Collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in
      JSON, but most elements support a description field.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").
    """


_ClientCreateMatchmakingRuleSetResponseTypeDef = TypedDict(
    "_ClientCreateMatchmakingRuleSetResponseTypeDef",
    {"RuleSet": ClientCreateMatchmakingRuleSetResponseRuleSetTypeDef},
    total=False,
)


class ClientCreateMatchmakingRuleSetResponseTypeDef(
    _ClientCreateMatchmakingRuleSetResponseTypeDef
):
    """
    Type definition for `ClientCreateMatchmakingRuleSet` `Response`

    Represents the returned data in response to a request action.

    - **RuleSet** *(dict) --*

      Object that describes the newly created matchmaking rule set.

      - **RuleSetName** *(string) --*

        Unique identifier for a matchmaking rule set

      - **RuleSetBody** *(string) --*

        Collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in
        JSON, but most elements support a description field.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").
    """


_ClientCreatePlayerSessionResponsePlayerSessionTypeDef = TypedDict(
    "_ClientCreatePlayerSessionResponsePlayerSessionTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)


class ClientCreatePlayerSessionResponsePlayerSessionTypeDef(
    _ClientCreatePlayerSessionResponsePlayerSessionTypeDef
):
    """
    Type definition for `ClientCreatePlayerSessionResponse` `PlayerSession`

    Object that describes the newly created player session record.

    - **PlayerSessionId** *(string) --*

      Unique identifier for a player session.

    - **PlayerId** *(string) --*

      Unique identifier for a player that is associated with this player session.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session that the player session is connected to.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the player's game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **Status** *(string) --*

      Current status of the player session.

      Possible player session statuses include the following:

      * **RESERVED** -- The player session request has been received, but the player has not yet
      connected to the server process and/or been validated.

      * **ACTIVE** -- The player has been validated by the server process and is currently
      connected.

      * **COMPLETED** -- The player connection has been dropped.

      * **TIMEDOUT** -- A player session request was received, but the player did not connect
      and/or was not validated within the timeout limit (60 seconds).

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift server process, an app
      needs both the IP address and port number.

    - **PlayerData** *(string) --*

      Developer-defined information related to a player. Amazon GameLift does not use this data,
      so it can be formatted as needed for use in the game.
    """


_ClientCreatePlayerSessionResponseTypeDef = TypedDict(
    "_ClientCreatePlayerSessionResponseTypeDef",
    {"PlayerSession": ClientCreatePlayerSessionResponsePlayerSessionTypeDef},
    total=False,
)


class ClientCreatePlayerSessionResponseTypeDef(
    _ClientCreatePlayerSessionResponseTypeDef
):
    """
    Type definition for `ClientCreatePlayerSession` `Response`

    Represents the returned data in response to a request action.

    - **PlayerSession** *(dict) --*

      Object that describes the newly created player session record.

      - **PlayerSessionId** *(string) --*

        Unique identifier for a player session.

      - **PlayerId** *(string) --*

        Unique identifier for a player that is associated with this player session.

      - **GameSessionId** *(string) --*

        Unique identifier for the game session that the player session is connected to.

      - **FleetId** *(string) --*

        Unique identifier for a fleet that the player's game session is running on.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **TerminationTime** *(datetime) --*

        Time stamp indicating when this data object was terminated. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **Status** *(string) --*

        Current status of the player session.

        Possible player session statuses include the following:

        * **RESERVED** -- The player session request has been received, but the player has not yet
        connected to the server process and/or been validated.

        * **ACTIVE** -- The player has been validated by the server process and is currently
        connected.

        * **COMPLETED** -- The player connection has been dropped.

        * **TIMEDOUT** -- A player session request was received, but the player did not connect
        and/or was not validated within the timeout limit (60 seconds).

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number.

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift server process, an app
        needs both the IP address and port number.

      - **PlayerData** *(string) --*

        Developer-defined information related to a player. Amazon GameLift does not use this data,
        so it can be formatted as needed for use in the game.
    """


_ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef = TypedDict(
    "_ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)


class ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef(
    _ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef
):
    """
    Type definition for `ClientCreatePlayerSessionsResponse` `PlayerSessions`

    Properties describing a player session. Player session objects are created either by
    creating a player session for a specific game session, or as part of a game session
    placement. A player session represents either a player reservation for a game session
    (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A
    player session object (including player data) is automatically passed to a game session
    when the player connects to the game session and is validated.

    When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
    session ends, the player session object is retained for 30 days and then removed.

    *  CreatePlayerSession

    *  CreatePlayerSessions

    *  DescribePlayerSessions

    * Game session placements

      *  StartGameSessionPlacement

      *  DescribeGameSessionPlacement

      *  StopGameSessionPlacement

    - **PlayerSessionId** *(string) --*

      Unique identifier for a player session.

    - **PlayerId** *(string) --*

      Unique identifier for a player that is associated with this player session.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session that the player session is connected to.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the player's game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **Status** *(string) --*

      Current status of the player session.

      Possible player session statuses include the following:

      * **RESERVED** -- The player session request has been received, but the player has not
      yet connected to the server process and/or been validated.

      * **ACTIVE** -- The player has been validated by the server process and is currently
      connected.

      * **COMPLETED** -- The player connection has been dropped.

      * **TIMEDOUT** -- A player session request was received, but the player did not connect
      and/or was not validated within the timeout limit (60 seconds).

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift server process, an app
      needs both the IP address and port number.

    - **PlayerData** *(string) --*

      Developer-defined information related to a player. Amazon GameLift does not use this
      data, so it can be formatted as needed for use in the game.
    """


_ClientCreatePlayerSessionsResponseTypeDef = TypedDict(
    "_ClientCreatePlayerSessionsResponseTypeDef",
    {"PlayerSessions": List[ClientCreatePlayerSessionsResponsePlayerSessionsTypeDef]},
    total=False,
)


class ClientCreatePlayerSessionsResponseTypeDef(
    _ClientCreatePlayerSessionsResponseTypeDef
):
    """
    Type definition for `ClientCreatePlayerSessions` `Response`

    Represents the returned data in response to a request action.

    - **PlayerSessions** *(list) --*

      Collection of player session objects created for the added players.

      - *(dict) --*

        Properties describing a player session. Player session objects are created either by
        creating a player session for a specific game session, or as part of a game session
        placement. A player session represents either a player reservation for a game session
        (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A
        player session object (including player data) is automatically passed to a game session
        when the player connects to the game session and is validated.

        When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
        session ends, the player session object is retained for 30 days and then removed.

        *  CreatePlayerSession

        *  CreatePlayerSessions

        *  DescribePlayerSessions

        * Game session placements

          *  StartGameSessionPlacement

          *  DescribeGameSessionPlacement

          *  StopGameSessionPlacement

        - **PlayerSessionId** *(string) --*

          Unique identifier for a player session.

        - **PlayerId** *(string) --*

          Unique identifier for a player that is associated with this player session.

        - **GameSessionId** *(string) --*

          Unique identifier for the game session that the player session is connected to.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the player's game session is running on.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **TerminationTime** *(datetime) --*

          Time stamp indicating when this data object was terminated. Format is a number expressed
          in Unix time as milliseconds (for example "1469498468.057").

        - **Status** *(string) --*

          Current status of the player session.

          Possible player session statuses include the following:

          * **RESERVED** -- The player session request has been received, but the player has not
          yet connected to the server process and/or been validated.

          * **ACTIVE** -- The player has been validated by the server process and is currently
          connected.

          * **COMPLETED** -- The player connection has been dropped.

          * **TIMEDOUT** -- A player session request was received, but the player did not connect
          and/or was not validated within the timeout limit (60 seconds).

        - **IpAddress** *(string) --*

          IP address of the game session. To connect to a Amazon GameLift game server, an app needs
          both the IP address and port number.

        - **DnsName** *(string) --*

        - **Port** *(integer) --*

          Port number for the game session. To connect to a Amazon GameLift server process, an app
          needs both the IP address and port number.

        - **PlayerData** *(string) --*

          Developer-defined information related to a player. Amazon GameLift does not use this
          data, so it can be formatted as needed for use in the game.
    """


_ClientCreateScriptResponseScriptStorageLocationTypeDef = TypedDict(
    "_ClientCreateScriptResponseScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientCreateScriptResponseScriptStorageLocationTypeDef(
    _ClientCreateScriptResponseScriptStorageLocationTypeDef
):
    """
    Type definition for `ClientCreateScriptResponseScript` `StorageLocation`

    Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
    stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
    CreateScript , and  UpdateScript requests.

    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.

    - **Key** *(string) --*

      Name of the zip file containing the build files or script files.

    - **RoleArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
      that allows Amazon GameLift to access the S3 bucket.

    - **ObjectVersion** *(string) --*

      Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
      uses this information when retrieving files from an S3 bucket that you own. Use this
      parameter to specify a specific version of the file; if not set, the latest version of
      the file is retrieved.
    """


_ClientCreateScriptResponseScriptTypeDef = TypedDict(
    "_ClientCreateScriptResponseScriptTypeDef",
    {
        "ScriptId": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": ClientCreateScriptResponseScriptStorageLocationTypeDef,
    },
    total=False,
)


class ClientCreateScriptResponseScriptTypeDef(_ClientCreateScriptResponseScriptTypeDef):
    """
    Type definition for `ClientCreateScriptResponse` `Script`

    The newly created script record with a unique script ID. The new script's storage location
    reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your
    account, the storage location reflects the information that was provided in the
    *CreateScript* request; (2) If the script file was uploaded from a local zip file, the
    storage location reflects an S3 location controls by the Amazon GameLift service.

    - **ScriptId** *(string) --*

      Unique identifier for a Realtime script

    - **Name** *(string) --*

      Descriptive label that is associated with a script. Script names do not need to be unique.

    - **Version** *(string) --*

      Version that is associated with a build or script. Version strings do not need to be unique.

    - **SizeOnDisk** *(integer) --*

      File size of the uploaded Realtime script, expressed in bytes. When files are uploaded from
      an S3 location, this value remains at "0".

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **StorageLocation** *(dict) --*

      Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
      stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
      CreateScript , and  UpdateScript requests.

      - **Bucket** *(string) --*

        Amazon S3 bucket identifier. This is the name of the S3 bucket.

      - **Key** *(string) --*

        Name of the zip file containing the build files or script files.

      - **RoleArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
        that allows Amazon GameLift to access the S3 bucket.

      - **ObjectVersion** *(string) --*

        Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
        uses this information when retrieving files from an S3 bucket that you own. Use this
        parameter to specify a specific version of the file; if not set, the latest version of
        the file is retrieved.
    """


_ClientCreateScriptResponseTypeDef = TypedDict(
    "_ClientCreateScriptResponseTypeDef",
    {"Script": ClientCreateScriptResponseScriptTypeDef},
    total=False,
)


class ClientCreateScriptResponseTypeDef(_ClientCreateScriptResponseTypeDef):
    """
    Type definition for `ClientCreateScript` `Response`

    - **Script** *(dict) --*

      The newly created script record with a unique script ID. The new script's storage location
      reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your
      account, the storage location reflects the information that was provided in the
      *CreateScript* request; (2) If the script file was uploaded from a local zip file, the
      storage location reflects an S3 location controls by the Amazon GameLift service.

      - **ScriptId** *(string) --*

        Unique identifier for a Realtime script

      - **Name** *(string) --*

        Descriptive label that is associated with a script. Script names do not need to be unique.

      - **Version** *(string) --*

        Version that is associated with a build or script. Version strings do not need to be unique.

      - **SizeOnDisk** *(integer) --*

        File size of the uploaded Realtime script, expressed in bytes. When files are uploaded from
        an S3 location, this value remains at "0".

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **StorageLocation** *(dict) --*

        Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
        stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
        CreateScript , and  UpdateScript requests.

        - **Bucket** *(string) --*

          Amazon S3 bucket identifier. This is the name of the S3 bucket.

        - **Key** *(string) --*

          Name of the zip file containing the build files or script files.

        - **RoleArn** *(string) --*

          Amazon Resource Name (`ARN
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
          that allows Amazon GameLift to access the S3 bucket.

        - **ObjectVersion** *(string) --*

          Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
          uses this information when retrieving files from an S3 bucket that you own. Use this
          parameter to specify a specific version of the file; if not set, the latest version of
          the file is retrieved.
    """


_ClientCreateScriptStorageLocationTypeDef = TypedDict(
    "_ClientCreateScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientCreateScriptStorageLocationTypeDef(
    _ClientCreateScriptStorageLocationTypeDef
):
    """
    Type definition for `ClientCreateScript` `StorageLocation`

    Location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored.
    The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a
    role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must
    be in the same region where you want to create a new script. By default, Amazon GameLift uploads
    the latest version of the zip file; if you have S3 object versioning turned on, you can use the
    ``ObjectVersion`` parameter to specify an earlier version.

    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.

    - **Key** *(string) --*

      Name of the zip file containing the build files or script files.

    - **RoleArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role that
      allows Amazon GameLift to access the S3 bucket.

    - **ObjectVersion** *(string) --*

      Version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses
      this information when retrieving files from an S3 bucket that you own. Use this parameter to
      specify a specific version of the file; if not set, the latest version of the file is retrieved.
    """


_ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef = TypedDict(
    "_ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
    },
    total=False,
)


class ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef(
    _ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef
):
    """
    Type definition for `ClientCreateVpcPeeringAuthorizationResponse` `VpcPeeringAuthorization`

    Details on the requested VPC peering authorization, including expiration.

    - **GameLiftAwsAccountId** *(string) --*

      Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet.
      You can find your Account ID in the AWS Management Console under account settings.

    - **PeerVpcAwsAccountId** *(string) --*

    - **PeerVpcId** *(string) --*

      Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet.
      The VPC must be in the same region where your fleet is deployed. Look up a VPC ID using the
      `VPC Dashboard <https://console.aws.amazon.com/vpc/>`__ in the AWS Management Console.
      Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`__ .

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this authorization was issued. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **ExpirationTime** *(datetime) --*

      Time stamp indicating when this authorization expires (24 hours after issuance). Format is
      a number expressed in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientCreateVpcPeeringAuthorizationResponseTypeDef = TypedDict(
    "_ClientCreateVpcPeeringAuthorizationResponseTypeDef",
    {
        "VpcPeeringAuthorization": ClientCreateVpcPeeringAuthorizationResponseVpcPeeringAuthorizationTypeDef
    },
    total=False,
)


class ClientCreateVpcPeeringAuthorizationResponseTypeDef(
    _ClientCreateVpcPeeringAuthorizationResponseTypeDef
):
    """
    Type definition for `ClientCreateVpcPeeringAuthorization` `Response`

    Represents the returned data in response to a request action.

    - **VpcPeeringAuthorization** *(dict) --*

      Details on the requested VPC peering authorization, including expiration.

      - **GameLiftAwsAccountId** *(string) --*

        Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet.
        You can find your Account ID in the AWS Management Console under account settings.

      - **PeerVpcAwsAccountId** *(string) --*

      - **PeerVpcId** *(string) --*

        Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet.
        The VPC must be in the same region where your fleet is deployed. Look up a VPC ID using the
        `VPC Dashboard <https://console.aws.amazon.com/vpc/>`__ in the AWS Management Console.
        Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`__ .

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this authorization was issued. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **ExpirationTime** *(datetime) --*

        Time stamp indicating when this authorization expires (24 hours after issuance). Format is
        a number expressed in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientDescribeAliasResponseAliasRoutingStrategyTypeDef = TypedDict(
    "_ClientDescribeAliasResponseAliasRoutingStrategyTypeDef",
    {"Type": str, "FleetId": str, "Message": str},
    total=False,
)


class ClientDescribeAliasResponseAliasRoutingStrategyTypeDef(
    _ClientDescribeAliasResponseAliasRoutingStrategyTypeDef
):
    """
    Type definition for `ClientDescribeAliasResponseAlias` `RoutingStrategy`

    Alias configuration for the alias, including routing type and settings.

    - **Type** *(string) --*

      Type of routing strategy.

      Possible routing types include the following:

      * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
      active fleets.

      * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
      display a message to the user. A terminal alias throws a TerminalRoutingStrategyException
      with the  RoutingStrategy message embedded.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the alias points to.

    - **Message** *(string) --*

      Message text to be used with a terminal routing strategy.
    """


_ClientDescribeAliasResponseAliasTypeDef = TypedDict(
    "_ClientDescribeAliasResponseAliasTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": ClientDescribeAliasResponseAliasRoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeAliasResponseAliasTypeDef(_ClientDescribeAliasResponseAliasTypeDef):
    """
    Type definition for `ClientDescribeAliasResponse` `Alias`

    Object that contains the requested alias.

    - **AliasId** *(string) --*

      Unique identifier for an alias; alias IDs are unique within a region.

    - **Name** *(string) --*

      Descriptive label that is associated with an alias. Alias names do not need to be unique.

    - **AliasArn** *(string) --*

      Unique identifier for an alias; alias ARNs are unique across all regions.

    - **Description** *(string) --*

      Human-readable description of an alias.

    - **RoutingStrategy** *(dict) --*

      Alias configuration for the alias, including routing type and settings.

      - **Type** *(string) --*

        Type of routing strategy.

        Possible routing types include the following:

        * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
        active fleets.

        * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
        display a message to the user. A terminal alias throws a TerminalRoutingStrategyException
        with the  RoutingStrategy message embedded.

      - **FleetId** *(string) --*

        Unique identifier for a fleet that the alias points to.

      - **Message** *(string) --*

        Message text to be used with a terminal routing strategy.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **LastUpdatedTime** *(datetime) --*

      Time stamp indicating when this data object was last modified. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientDescribeAliasResponseTypeDef = TypedDict(
    "_ClientDescribeAliasResponseTypeDef",
    {"Alias": ClientDescribeAliasResponseAliasTypeDef},
    total=False,
)


class ClientDescribeAliasResponseTypeDef(_ClientDescribeAliasResponseTypeDef):
    """
    Type definition for `ClientDescribeAlias` `Response`

    Represents the returned data in response to a request action.

    - **Alias** *(dict) --*

      Object that contains the requested alias.

      - **AliasId** *(string) --*

        Unique identifier for an alias; alias IDs are unique within a region.

      - **Name** *(string) --*

        Descriptive label that is associated with an alias. Alias names do not need to be unique.

      - **AliasArn** *(string) --*

        Unique identifier for an alias; alias ARNs are unique across all regions.

      - **Description** *(string) --*

        Human-readable description of an alias.

      - **RoutingStrategy** *(dict) --*

        Alias configuration for the alias, including routing type and settings.

        - **Type** *(string) --*

          Type of routing strategy.

          Possible routing types include the following:

          * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
          active fleets.

          * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
          display a message to the user. A terminal alias throws a TerminalRoutingStrategyException
          with the  RoutingStrategy message embedded.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the alias points to.

        - **Message** *(string) --*

          Message text to be used with a terminal routing strategy.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **LastUpdatedTime** *(datetime) --*

        Time stamp indicating when this data object was last modified. Format is a number expressed
        in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientDescribeBuildResponseBuildTypeDef = TypedDict(
    "_ClientDescribeBuildResponseBuildTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": str,
        "SizeOnDisk": int,
        "OperatingSystem": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeBuildResponseBuildTypeDef(_ClientDescribeBuildResponseBuildTypeDef):
    """
    Type definition for `ClientDescribeBuildResponse` `Build`

    Set of properties describing the requested build.

    - **BuildId** *(string) --*

      Unique identifier for a build.

    - **Name** *(string) --*

      Descriptive label that is associated with a build. Build names do not need to be unique. It
      can be set using  CreateBuild or  UpdateBuild .

    - **Version** *(string) --*

      Version that is associated with a build or script. Version strings do not need to be
      unique. This value can be set using  CreateBuild or  UpdateBuild .

    - **Status** *(string) --*

      Current status of the build.

      Possible build statuses include the following:

      * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You
      cannot create fleets for builds that are in this status. When a build is successfully
      created, the build status is set to this value.

      * **READY** -- The game build has been successfully uploaded. You can now create new fleets
      for this build.

      * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.

    - **SizeOnDisk** *(integer) --*

      File size of the uploaded game build, expressed in bytes. When the build status is
      ``INITIALIZED`` , this value is 0.

    - **OperatingSystem** *(string) --*

      Operating system that the game server binaries are built to run on. This value determines
      the type of fleet resources that you can use for this build.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").
    """


_ClientDescribeBuildResponseTypeDef = TypedDict(
    "_ClientDescribeBuildResponseTypeDef",
    {"Build": ClientDescribeBuildResponseBuildTypeDef},
    total=False,
)


class ClientDescribeBuildResponseTypeDef(_ClientDescribeBuildResponseTypeDef):
    """
    Type definition for `ClientDescribeBuild` `Response`

    Represents the returned data in response to a request action.

    - **Build** *(dict) --*

      Set of properties describing the requested build.

      - **BuildId** *(string) --*

        Unique identifier for a build.

      - **Name** *(string) --*

        Descriptive label that is associated with a build. Build names do not need to be unique. It
        can be set using  CreateBuild or  UpdateBuild .

      - **Version** *(string) --*

        Version that is associated with a build or script. Version strings do not need to be
        unique. This value can be set using  CreateBuild or  UpdateBuild .

      - **Status** *(string) --*

        Current status of the build.

        Possible build statuses include the following:

        * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You
        cannot create fleets for builds that are in this status. When a build is successfully
        created, the build status is set to this value.

        * **READY** -- The game build has been successfully uploaded. You can now create new fleets
        for this build.

        * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.

      - **SizeOnDisk** *(integer) --*

        File size of the uploaded game build, expressed in bytes. When the build status is
        ``INITIALIZED`` , this value is 0.

      - **OperatingSystem** *(string) --*

        Operating system that the game server binaries are built to run on. This value determines
        the type of fleet resources that you can use for this build.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").
    """


_ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef = TypedDict(
    "_ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef",
    {"EC2InstanceType": str, "CurrentInstances": int, "InstanceLimit": int},
    total=False,
)


class ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef(
    _ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef
):
    """
    Type definition for `ClientDescribeEc2InstanceLimitsResponse` `EC2InstanceLimits`

    Maximum number of instances allowed based on the Amazon Elastic Compute Cloud (Amazon EC2)
    instance type. Instance limits can be retrieved by calling  DescribeEC2InstanceLimits .

    - **EC2InstanceType** *(string) --*

      Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type
      determines the computing resources of each instance in the fleet, including CPU, memory,
      storage, and networking capacity. Amazon GameLift supports the following EC2 instance
      types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for
      detailed descriptions.

    - **CurrentInstances** *(integer) --*

      Number of instances of the specified type that are currently in use by this AWS account.

    - **InstanceLimit** *(integer) --*

      Number of instances allowed.
    """


_ClientDescribeEc2InstanceLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeEc2InstanceLimitsResponseTypeDef",
    {
        "EC2InstanceLimits": List[
            ClientDescribeEc2InstanceLimitsResponseEC2InstanceLimitsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeEc2InstanceLimitsResponseTypeDef(
    _ClientDescribeEc2InstanceLimitsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEc2InstanceLimits` `Response`

    Represents the returned data in response to a request action.

    - **EC2InstanceLimits** *(list) --*

      Object that contains the maximum number of instances for the specified instance type.

      - *(dict) --*

        Maximum number of instances allowed based on the Amazon Elastic Compute Cloud (Amazon EC2)
        instance type. Instance limits can be retrieved by calling  DescribeEC2InstanceLimits .

        - **EC2InstanceType** *(string) --*

          Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type
          determines the computing resources of each instance in the fleet, including CPU, memory,
          storage, and networking capacity. Amazon GameLift supports the following EC2 instance
          types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for
          detailed descriptions.

        - **CurrentInstances** *(integer) --*

          Number of instances of the specified type that are currently in use by this AWS account.

        - **InstanceLimit** *(integer) --*

          Number of instances allowed.
    """


_ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef = TypedDict(
    "_ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef",
    {"CertificateType": str},
    total=False,
)


class ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef(
    _ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeFleetAttributesResponseFleetAttributes` `CertificateConfiguration`

    - **CertificateType** *(string) --*
    """


_ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "_ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)


class ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef(
    _ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef
):
    """
    Type definition for `ClientDescribeFleetAttributesResponseFleetAttributes` `ResourceCreationLimitPolicy`

    Fleet policy to limit the number of game sessions an individual player can create over a
    span of time.

    - **NewGameSessionsPerCreator** *(integer) --*

      Maximum number of game sessions that an individual can create during the policy period.

    - **PolicyPeriodInMinutes** *(integer) --*

      Time span used in evaluating the resource creation limit policy.
    """


_ClientDescribeFleetAttributesResponseFleetAttributesTypeDef = TypedDict(
    "_ClientDescribeFleetAttributesResponseFleetAttributesTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "FleetType": str,
        "InstanceType": str,
        "Description": str,
        "Name": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": str,
        "BuildId": str,
        "ScriptId": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "NewGameSessionProtectionPolicy": str,
        "OperatingSystem": str,
        "ResourceCreationLimitPolicy": ClientDescribeFleetAttributesResponseFleetAttributesResourceCreationLimitPolicyTypeDef,
        "MetricGroups": List[str],
        "StoppedActions": List[str],
        "InstanceRoleArn": str,
        "CertificateConfiguration": ClientDescribeFleetAttributesResponseFleetAttributesCertificateConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeFleetAttributesResponseFleetAttributesTypeDef(
    _ClientDescribeFleetAttributesResponseFleetAttributesTypeDef
):
    """
    Type definition for `ClientDescribeFleetAttributesResponse` `FleetAttributes`

    General properties describing a fleet.

    *  CreateFleet

    *  ListFleets

    *  DeleteFleet

    * Describe fleets:

      *  DescribeFleetAttributes

      *  DescribeFleetCapacity

      *  DescribeFleetPortSettings

      *  DescribeFleetUtilization

      *  DescribeRuntimeConfiguration

      *  DescribeEC2InstanceLimits

      *  DescribeFleetEvents

    * Update fleets:

      *  UpdateFleetAttributes

      *  UpdateFleetCapacity

      *  UpdateFleetPortSettings

      *  UpdateRuntimeConfiguration

    * Manage fleet actions:

      *  StartFleetActions

      *  StopFleetActions

    - **FleetId** *(string) --*

      Unique identifier for a fleet.

    - **FleetArn** *(string) --*

      Identifier for a fleet that is unique across all regions.

    - **FleetType** *(string) --*

      Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may
      be interrupted with a two-minute notification.

    - **InstanceType** *(string) --*

      EC2 instance type indicating the computing resources of each instance in the fleet,
      including CPU, memory, storage, and networking capacity. See `Amazon EC2 Instance Types
      <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.

    - **Description** *(string) --*

      Human-readable description of the fleet.

    - **Name** *(string) --*

      Descriptive label that is associated with a fleet. Fleet names do not need to be unique.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **Status** *(string) --*

      Current status of the fleet.

      Possible fleet statuses include the following:

      * **NEW** -- A new fleet has been defined and desired instances is set to 1.

      * **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** -- Amazon GameLift is setting up the new
      fleet, creating new instances with the game build or Realtime script and starting server
      processes.

      * **ACTIVE** -- Hosts can now accept game sessions.

      * **ERROR** -- An error occurred when downloading, validating, building, or activating
      the fleet.

      * **DELETING** -- Hosts are responding to a delete fleet request.

      * **TERMINATED** -- The fleet no longer exists.

    - **BuildId** *(string) --*

      Unique identifier for a build.

    - **ScriptId** *(string) --*

      Unique identifier for a Realtime script.

    - **ServerLaunchPath** *(string) --*

      Path to a game server executable in the fleet's build, specified for fleets created
      before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after
      this date are specified in the fleet's  RuntimeConfiguration .

    - **ServerLaunchParameters** *(string) --*

      Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK
      v. 0.12.16). Server launch parameters for fleets created after this date are specified in
      the fleet's  RuntimeConfiguration .

    - **LogPaths** *(list) --*

      Location of default log files. When a server process is shut down, Amazon GameLift
      captures and stores any log files in this location. These logs are in addition to game
      session logs; see more on game session logs in the `Amazon GameLift Developer Guide
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-api-server-code>`__
      . If no default log path for a fleet is specified, Amazon GameLift automatically uploads
      logs that are stored on each instance at ``C:\\game\\logs`` (for Windows) or
      ``/local/game/logs`` (for Linux). Use the Amazon GameLift console to access stored logs.

      - *(string) --*

    - **NewGameSessionProtectionPolicy** *(string) --*

      Type of game session protection to set for all new instances started in the fleet.

      * **NoProtection** -- The game session can be terminated during a scale-down event.

      * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be
      terminated during a scale-down event.

    - **OperatingSystem** *(string) --*

      Operating system of the fleet's computing resources. A fleet's operating system depends
      on the OS specified for the build that is deployed on this fleet.

    - **ResourceCreationLimitPolicy** *(dict) --*

      Fleet policy to limit the number of game sessions an individual player can create over a
      span of time.

      - **NewGameSessionsPerCreator** *(integer) --*

        Maximum number of game sessions that an individual can create during the policy period.

      - **PolicyPeriodInMinutes** *(integer) --*

        Time span used in evaluating the resource creation limit policy.

    - **MetricGroups** *(list) --*

      Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view
      metrics for an individual fleet or aggregated metrics for fleets that are in a fleet
      metric group. A fleet can be included in only one metric group at a time.

      - *(string) --*

    - **StoppedActions** *(list) --*

      List of fleet actions that have been suspended using  StopFleetActions . This includes
      auto-scaling.

      - *(string) --*

    - **InstanceRoleArn** *(string) --*

      Unique identifier for an AWS IAM role that manages access to your AWS services. With an
      instance role ARN set, any application that runs on an instance in this fleet can assume
      the role, including install scripts, server processes, daemons (background processes).
      Create a role or look up a role's ARN using the `IAM dashboard
      <https://console.aws.amazon.com/iam/>`__ in the AWS Management Console. Learn more about
      using on-box credentials for your game servers at `Access external resources from a game
      server
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`__
      .

    - **CertificateConfiguration** *(dict) --*

      - **CertificateType** *(string) --*
    """


_ClientDescribeFleetAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeFleetAttributesResponseTypeDef",
    {
        "FleetAttributes": List[
            ClientDescribeFleetAttributesResponseFleetAttributesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeFleetAttributesResponseTypeDef(
    _ClientDescribeFleetAttributesResponseTypeDef
):
    """
    Type definition for `ClientDescribeFleetAttributes` `Response`

    Represents the returned data in response to a request action.

    - **FleetAttributes** *(list) --*

      Collection of objects containing attribute metadata for each requested fleet ID.

      - *(dict) --*

        General properties describing a fleet.

        *  CreateFleet

        *  ListFleets

        *  DeleteFleet

        * Describe fleets:

          *  DescribeFleetAttributes

          *  DescribeFleetCapacity

          *  DescribeFleetPortSettings

          *  DescribeFleetUtilization

          *  DescribeRuntimeConfiguration

          *  DescribeEC2InstanceLimits

          *  DescribeFleetEvents

        * Update fleets:

          *  UpdateFleetAttributes

          *  UpdateFleetCapacity

          *  UpdateFleetPortSettings

          *  UpdateRuntimeConfiguration

        * Manage fleet actions:

          *  StartFleetActions

          *  StopFleetActions

        - **FleetId** *(string) --*

          Unique identifier for a fleet.

        - **FleetArn** *(string) --*

          Identifier for a fleet that is unique across all regions.

        - **FleetType** *(string) --*

          Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may
          be interrupted with a two-minute notification.

        - **InstanceType** *(string) --*

          EC2 instance type indicating the computing resources of each instance in the fleet,
          including CPU, memory, storage, and networking capacity. See `Amazon EC2 Instance Types
          <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.

        - **Description** *(string) --*

          Human-readable description of the fleet.

        - **Name** *(string) --*

          Descriptive label that is associated with a fleet. Fleet names do not need to be unique.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **TerminationTime** *(datetime) --*

          Time stamp indicating when this data object was terminated. Format is a number expressed
          in Unix time as milliseconds (for example "1469498468.057").

        - **Status** *(string) --*

          Current status of the fleet.

          Possible fleet statuses include the following:

          * **NEW** -- A new fleet has been defined and desired instances is set to 1.

          * **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** -- Amazon GameLift is setting up the new
          fleet, creating new instances with the game build or Realtime script and starting server
          processes.

          * **ACTIVE** -- Hosts can now accept game sessions.

          * **ERROR** -- An error occurred when downloading, validating, building, or activating
          the fleet.

          * **DELETING** -- Hosts are responding to a delete fleet request.

          * **TERMINATED** -- The fleet no longer exists.

        - **BuildId** *(string) --*

          Unique identifier for a build.

        - **ScriptId** *(string) --*

          Unique identifier for a Realtime script.

        - **ServerLaunchPath** *(string) --*

          Path to a game server executable in the fleet's build, specified for fleets created
          before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after
          this date are specified in the fleet's  RuntimeConfiguration .

        - **ServerLaunchParameters** *(string) --*

          Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK
          v. 0.12.16). Server launch parameters for fleets created after this date are specified in
          the fleet's  RuntimeConfiguration .

        - **LogPaths** *(list) --*

          Location of default log files. When a server process is shut down, Amazon GameLift
          captures and stores any log files in this location. These logs are in addition to game
          session logs; see more on game session logs in the `Amazon GameLift Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-api-server-code>`__
          . If no default log path for a fleet is specified, Amazon GameLift automatically uploads
          logs that are stored on each instance at ``C:\\game\\logs`` (for Windows) or
          ``/local/game/logs`` (for Linux). Use the Amazon GameLift console to access stored logs.

          - *(string) --*

        - **NewGameSessionProtectionPolicy** *(string) --*

          Type of game session protection to set for all new instances started in the fleet.

          * **NoProtection** -- The game session can be terminated during a scale-down event.

          * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be
          terminated during a scale-down event.

        - **OperatingSystem** *(string) --*

          Operating system of the fleet's computing resources. A fleet's operating system depends
          on the OS specified for the build that is deployed on this fleet.

        - **ResourceCreationLimitPolicy** *(dict) --*

          Fleet policy to limit the number of game sessions an individual player can create over a
          span of time.

          - **NewGameSessionsPerCreator** *(integer) --*

            Maximum number of game sessions that an individual can create during the policy period.

          - **PolicyPeriodInMinutes** *(integer) --*

            Time span used in evaluating the resource creation limit policy.

        - **MetricGroups** *(list) --*

          Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view
          metrics for an individual fleet or aggregated metrics for fleets that are in a fleet
          metric group. A fleet can be included in only one metric group at a time.

          - *(string) --*

        - **StoppedActions** *(list) --*

          List of fleet actions that have been suspended using  StopFleetActions . This includes
          auto-scaling.

          - *(string) --*

        - **InstanceRoleArn** *(string) --*

          Unique identifier for an AWS IAM role that manages access to your AWS services. With an
          instance role ARN set, any application that runs on an instance in this fleet can assume
          the role, including install scripts, server processes, daemons (background processes).
          Create a role or look up a role's ARN using the `IAM dashboard
          <https://console.aws.amazon.com/iam/>`__ in the AWS Management Console. Learn more about
          using on-box credentials for your game servers at `Access external resources from a game
          server
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`__
          .

        - **CertificateConfiguration** *(dict) --*

          - **CertificateType** *(string) --*

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef = TypedDict(
    "_ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef",
    {
        "DESIRED": int,
        "MINIMUM": int,
        "MAXIMUM": int,
        "PENDING": int,
        "ACTIVE": int,
        "IDLE": int,
        "TERMINATING": int,
    },
    total=False,
)


class ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef(
    _ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef
):
    """
    Type definition for `ClientDescribeFleetCapacityResponseFleetCapacity` `InstanceCounts`

    Current status of fleet capacity.

    - **DESIRED** *(integer) --*

      Ideal number of active instances in the fleet.

    - **MINIMUM** *(integer) --*

      Minimum value allowed for the fleet's instance count.

    - **MAXIMUM** *(integer) --*

      Maximum value allowed for the fleet's instance count.

    - **PENDING** *(integer) --*

      Number of instances in the fleet that are starting but not yet active.

    - **ACTIVE** *(integer) --*

      Actual number of active instances in the fleet.

    - **IDLE** *(integer) --*

      Number of active instances in the fleet that are not currently hosting a game session.

    - **TERMINATING** *(integer) --*

      Number of instances in the fleet that are no longer active but haven't yet been
      terminated.
    """


_ClientDescribeFleetCapacityResponseFleetCapacityTypeDef = TypedDict(
    "_ClientDescribeFleetCapacityResponseFleetCapacityTypeDef",
    {
        "FleetId": str,
        "InstanceType": str,
        "InstanceCounts": ClientDescribeFleetCapacityResponseFleetCapacityInstanceCountsTypeDef,
    },
    total=False,
)


class ClientDescribeFleetCapacityResponseFleetCapacityTypeDef(
    _ClientDescribeFleetCapacityResponseFleetCapacityTypeDef
):
    """
    Type definition for `ClientDescribeFleetCapacityResponse` `FleetCapacity`

    Information about the fleet's capacity. Fleet capacity is measured in EC2 instances. By
    default, new fleets have a capacity of one instance, but can be updated as needed. The
    maximum number of instances for a fleet is determined by the fleet's instance type.

    *  CreateFleet

    *  ListFleets

    *  DeleteFleet

    * Describe fleets:

      *  DescribeFleetAttributes

      *  DescribeFleetCapacity

      *  DescribeFleetPortSettings

      *  DescribeFleetUtilization

      *  DescribeRuntimeConfiguration

      *  DescribeEC2InstanceLimits

      *  DescribeFleetEvents

    * Update fleets:

      *  UpdateFleetAttributes

      *  UpdateFleetCapacity

      *  UpdateFleetPortSettings

      *  UpdateRuntimeConfiguration

    * Manage fleet actions:

      *  StartFleetActions

      *  StopFleetActions

    - **FleetId** *(string) --*

      Unique identifier for a fleet.

    - **InstanceType** *(string) --*

      Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type
      determines the computing resources of each instance in the fleet, including CPU, memory,
      storage, and networking capacity. Amazon GameLift supports the following EC2 instance
      types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for
      detailed descriptions.

    - **InstanceCounts** *(dict) --*

      Current status of fleet capacity.

      - **DESIRED** *(integer) --*

        Ideal number of active instances in the fleet.

      - **MINIMUM** *(integer) --*

        Minimum value allowed for the fleet's instance count.

      - **MAXIMUM** *(integer) --*

        Maximum value allowed for the fleet's instance count.

      - **PENDING** *(integer) --*

        Number of instances in the fleet that are starting but not yet active.

      - **ACTIVE** *(integer) --*

        Actual number of active instances in the fleet.

      - **IDLE** *(integer) --*

        Number of active instances in the fleet that are not currently hosting a game session.

      - **TERMINATING** *(integer) --*

        Number of instances in the fleet that are no longer active but haven't yet been
        terminated.
    """


_ClientDescribeFleetCapacityResponseTypeDef = TypedDict(
    "_ClientDescribeFleetCapacityResponseTypeDef",
    {
        "FleetCapacity": List[ClientDescribeFleetCapacityResponseFleetCapacityTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeFleetCapacityResponseTypeDef(
    _ClientDescribeFleetCapacityResponseTypeDef
):
    """
    Type definition for `ClientDescribeFleetCapacity` `Response`

    Represents the returned data in response to a request action.

    - **FleetCapacity** *(list) --*

      Collection of objects containing capacity information for each requested fleet ID. Leave this
      parameter empty to retrieve capacity information for all fleets.

      - *(dict) --*

        Information about the fleet's capacity. Fleet capacity is measured in EC2 instances. By
        default, new fleets have a capacity of one instance, but can be updated as needed. The
        maximum number of instances for a fleet is determined by the fleet's instance type.

        *  CreateFleet

        *  ListFleets

        *  DeleteFleet

        * Describe fleets:

          *  DescribeFleetAttributes

          *  DescribeFleetCapacity

          *  DescribeFleetPortSettings

          *  DescribeFleetUtilization

          *  DescribeRuntimeConfiguration

          *  DescribeEC2InstanceLimits

          *  DescribeFleetEvents

        * Update fleets:

          *  UpdateFleetAttributes

          *  UpdateFleetCapacity

          *  UpdateFleetPortSettings

          *  UpdateRuntimeConfiguration

        * Manage fleet actions:

          *  StartFleetActions

          *  StopFleetActions

        - **FleetId** *(string) --*

          Unique identifier for a fleet.

        - **InstanceType** *(string) --*

          Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type
          determines the computing resources of each instance in the fleet, including CPU, memory,
          storage, and networking capacity. Amazon GameLift supports the following EC2 instance
          types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for
          detailed descriptions.

        - **InstanceCounts** *(dict) --*

          Current status of fleet capacity.

          - **DESIRED** *(integer) --*

            Ideal number of active instances in the fleet.

          - **MINIMUM** *(integer) --*

            Minimum value allowed for the fleet's instance count.

          - **MAXIMUM** *(integer) --*

            Maximum value allowed for the fleet's instance count.

          - **PENDING** *(integer) --*

            Number of instances in the fleet that are starting but not yet active.

          - **ACTIVE** *(integer) --*

            Actual number of active instances in the fleet.

          - **IDLE** *(integer) --*

            Number of active instances in the fleet that are not currently hosting a game session.

          - **TERMINATING** *(integer) --*

            Number of instances in the fleet that are no longer active but haven't yet been
            terminated.

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef = TypedDict(
    "_ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef",
    {"FromPort": int, "ToPort": int, "IpRange": str, "Protocol": str},
    total=False,
)


class ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef(
    _ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef
):
    """
    Type definition for `ClientDescribeFleetPortSettingsResponse` `InboundPermissions`

    A range of IP addresses and port settings that allow inbound traffic to connect to server
    processes on an Amazon GameLift. New game sessions that are started on the fleet are
    assigned an IP address/port number combination, which must fall into the fleet's allowed
    ranges. For fleets created with a custom game server, the ranges reflect the server's game
    session assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two
    port ranges, one for TCP messaging and one for UDP for use by the Realtime servers.

    - **FromPort** *(integer) --*

      Starting value for a range of allowed port numbers.

    - **ToPort** *(integer) --*

      Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This
      value must be higher than ``FromPort`` .

    - **IpRange** *(string) --*

      Range of allowed IP addresses. This value must be expressed in CIDR notation. Example:
      "``000.000.000.000/[subnet mask]`` " or optionally the shortened version
      "``0.0.0.0/[subnet mask]`` ".

    - **Protocol** *(string) --*

      Network communication protocol used by the fleet.
    """


_ClientDescribeFleetPortSettingsResponseTypeDef = TypedDict(
    "_ClientDescribeFleetPortSettingsResponseTypeDef",
    {
        "InboundPermissions": List[
            ClientDescribeFleetPortSettingsResponseInboundPermissionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeFleetPortSettingsResponseTypeDef(
    _ClientDescribeFleetPortSettingsResponseTypeDef
):
    """
    Type definition for `ClientDescribeFleetPortSettings` `Response`

    Represents the returned data in response to a request action.

    - **InboundPermissions** *(list) --*

      Object that contains port settings for the requested fleet ID.

      - *(dict) --*

        A range of IP addresses and port settings that allow inbound traffic to connect to server
        processes on an Amazon GameLift. New game sessions that are started on the fleet are
        assigned an IP address/port number combination, which must fall into the fleet's allowed
        ranges. For fleets created with a custom game server, the ranges reflect the server's game
        session assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two
        port ranges, one for TCP messaging and one for UDP for use by the Realtime servers.

        - **FromPort** *(integer) --*

          Starting value for a range of allowed port numbers.

        - **ToPort** *(integer) --*

          Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This
          value must be higher than ``FromPort`` .

        - **IpRange** *(string) --*

          Range of allowed IP addresses. This value must be expressed in CIDR notation. Example:
          "``000.000.000.000/[subnet mask]`` " or optionally the shortened version
          "``0.0.0.0/[subnet mask]`` ".

        - **Protocol** *(string) --*

          Network communication protocol used by the fleet.
    """


_ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef = TypedDict(
    "_ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef",
    {
        "FleetId": str,
        "ActiveServerProcessCount": int,
        "ActiveGameSessionCount": int,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
    },
    total=False,
)


class ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef(
    _ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef
):
    """
    Type definition for `ClientDescribeFleetUtilizationResponse` `FleetUtilization`

    Current status of fleet utilization, including the number of game and player sessions being
    hosted.

    *  CreateFleet

    *  ListFleets

    *  DeleteFleet

    * Describe fleets:

      *  DescribeFleetAttributes

      *  DescribeFleetCapacity

      *  DescribeFleetPortSettings

      *  DescribeFleetUtilization

      *  DescribeRuntimeConfiguration

      *  DescribeEC2InstanceLimits

      *  DescribeFleetEvents

    * Update fleets:

      *  UpdateFleetAttributes

      *  UpdateFleetCapacity

      *  UpdateFleetPortSettings

      *  UpdateRuntimeConfiguration

    * Manage fleet actions:

      *  StartFleetActions

      *  StopFleetActions

    - **FleetId** *(string) --*

      Unique identifier for a fleet.

    - **ActiveServerProcessCount** *(integer) --*

      Number of server processes in an ``ACTIVE`` status currently running across all instances
      in the fleet

    - **ActiveGameSessionCount** *(integer) --*

      Number of active game sessions currently being hosted on all instances in the fleet.

    - **CurrentPlayerSessionCount** *(integer) --*

      Number of active player sessions currently being hosted on all instances in the fleet.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum players allowed across all game sessions currently being hosted on all instances
      in the fleet.
    """


_ClientDescribeFleetUtilizationResponseTypeDef = TypedDict(
    "_ClientDescribeFleetUtilizationResponseTypeDef",
    {
        "FleetUtilization": List[
            ClientDescribeFleetUtilizationResponseFleetUtilizationTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeFleetUtilizationResponseTypeDef(
    _ClientDescribeFleetUtilizationResponseTypeDef
):
    """
    Type definition for `ClientDescribeFleetUtilization` `Response`

    Represents the returned data in response to a request action.

    - **FleetUtilization** *(list) --*

      Collection of objects containing utilization information for each requested fleet ID.

      - *(dict) --*

        Current status of fleet utilization, including the number of game and player sessions being
        hosted.

        *  CreateFleet

        *  ListFleets

        *  DeleteFleet

        * Describe fleets:

          *  DescribeFleetAttributes

          *  DescribeFleetCapacity

          *  DescribeFleetPortSettings

          *  DescribeFleetUtilization

          *  DescribeRuntimeConfiguration

          *  DescribeEC2InstanceLimits

          *  DescribeFleetEvents

        * Update fleets:

          *  UpdateFleetAttributes

          *  UpdateFleetCapacity

          *  UpdateFleetPortSettings

          *  UpdateRuntimeConfiguration

        * Manage fleet actions:

          *  StartFleetActions

          *  StopFleetActions

        - **FleetId** *(string) --*

          Unique identifier for a fleet.

        - **ActiveServerProcessCount** *(integer) --*

          Number of server processes in an ``ACTIVE`` status currently running across all instances
          in the fleet

        - **ActiveGameSessionCount** *(integer) --*

          Number of active game sessions currently being hosted on all instances in the fleet.

        - **CurrentPlayerSessionCount** *(integer) --*

          Number of active player sessions currently being hosted on all instances in the fleet.

        - **MaximumPlayerSessionCount** *(integer) --*

          Maximum players allowed across all game sessions currently being hosted on all instances
          in the fleet.

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef = TypedDict(
    "_ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef(
    _ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSession` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included
    in a game session request, these properties communicate details to be used when
    setting up the new game session, such as to specify a game mode, level, or map. Game
    properties are passed to the game server process when initiating a new game session;
    the server process uses the properties as appropriate. For more information, see the
    `Amazon GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef = TypedDict(
    "_ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": str,
        "StatusReason": str,
        "GameProperties": List[
            ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": str,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef(
    _ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionDetailsResponseGameSessionDetails` `GameSession`

    Object that describes a game session.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. A game session ARN has the following format:
      ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
      token>`` .

    - **Name** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to
      be unique.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number
      expressed in Unix time as milliseconds (for example "1469498468.057").

    - **CurrentPlayerSessionCount** *(integer) --*

      Number of players currently in the game session.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **Status** *(string) --*

      Current status of the game session. A game session must have an ``ACTIVE`` status to
      have player sessions.

    - **StatusReason** *(string) --*

      Provides additional information about game session status. ``INTERRUPTED`` indicates
      that the game session was hosted on a spot instance that was reclaimed, causing the
      active game session to be terminated.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These
      properties are passed to a game server process in the  GameSession object with a
      request to start a new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). You can search for active game sessions based on this custom data with
      SearchGameSessions .

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included
        in a game session request, these properties communicate details to be used when
        setting up the new game session, such as to specify a game mode, level, or map. Game
        properties are passed to the game server process when initiating a new game session;
        the server process uses the properties as appropriate. For more information, see the
        `Amazon GameLift Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **PlayerSessionCreationPolicy** *(string) --*

      Indicates whether or not the game session is accepting new players.

    - **CreatorId** *(string) --*

      Unique identifier for a player. This ID is used to enforce a resource protection policy
      (if one exists), that limits the number of game sessions a player can create.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a
      new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information about the matchmaking process that was used to create the game session. It
      is in JSON syntax, formatted as a string. In addition the matchmaking configuration
      used, it contains data on all players assigned to the match, including player
      attributes and team assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      . Matchmaker data is useful when requesting match backfills, and is updated whenever
      new players are added during a successful backfill (see  StartMatchBackfill ).
    """


_ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef = TypedDict(
    "_ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef",
    {
        "GameSession": ClientDescribeGameSessionDetailsResponseGameSessionDetailsGameSessionTypeDef,
        "ProtectionPolicy": str,
    },
    total=False,
)


class ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef(
    _ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionDetailsResponse` `GameSessionDetails`

    A game session's properties plus the protection policy currently in force.

    - **GameSession** *(dict) --*

      Object that describes a game session.

      - **GameSessionId** *(string) --*

        Unique identifier for the game session. A game session ARN has the following format:
        ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
        token>`` .

      - **Name** *(string) --*

        Descriptive label that is associated with a game session. Session names do not need to
        be unique.

      - **FleetId** *(string) --*

        Unique identifier for a fleet that the game session is running on.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed
        in Unix time as milliseconds (for example "1469498468.057").

      - **TerminationTime** *(datetime) --*

        Time stamp indicating when this data object was terminated. Format is a number
        expressed in Unix time as milliseconds (for example "1469498468.057").

      - **CurrentPlayerSessionCount** *(integer) --*

        Number of players currently in the game session.

      - **MaximumPlayerSessionCount** *(integer) --*

        Maximum number of players that can be connected simultaneously to the game session.

      - **Status** *(string) --*

        Current status of the game session. A game session must have an ``ACTIVE`` status to
        have player sessions.

      - **StatusReason** *(string) --*

        Provides additional information about game session status. ``INTERRUPTED`` indicates
        that the game session was hosted on a spot instance that was reclaimed, causing the
        active game session to be terminated.

      - **GameProperties** *(list) --*

        Set of custom properties for a game session, formatted as key:value pairs. These
        properties are passed to a game server process in the  GameSession object with a
        request to start a new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ). You can search for active game sessions based on this custom data with
        SearchGameSessions .

        - *(dict) --*

          Set of key-value pairs that contain information about a game session. When included
          in a game session request, these properties communicate details to be used when
          setting up the new game session, such as to specify a game mode, level, or map. Game
          properties are passed to the game server process when initiating a new game session;
          the server process uses the properties as appropriate. For more information, see the
          `Amazon GameLift Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
          .

          - **Key** *(string) --*

            Game property identifier.

          - **Value** *(string) --*

            Game property value.

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app
        needs both the IP address and port number.

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift game server, an app
        needs both the IP address and port number.

      - **PlayerSessionCreationPolicy** *(string) --*

        Indicates whether or not the game session is accepting new players.

      - **CreatorId** *(string) --*

        Unique identifier for a player. This ID is used to enforce a resource protection policy
        (if one exists), that limits the number of game sessions a player can create.

      - **GameSessionData** *(string) --*

        Set of custom game session properties, formatted as a single string value. This data is
        passed to a game server process in the  GameSession object with a request to start a
        new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ).

      - **MatchmakerData** *(string) --*

        Information about the matchmaking process that was used to create the game session. It
        is in JSON syntax, formatted as a string. In addition the matchmaking configuration
        used, it contains data on all players assigned to the match, including player
        attributes and team assignments. For more details on matchmaker data, see `Match Data
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
        . Matchmaker data is useful when requesting match backfills, and is updated whenever
        new players are added during a successful backfill (see  StartMatchBackfill ).

    - **ProtectionPolicy** *(string) --*

      Current status of protection for the game session.

      * **NoProtection** -- The game session can be terminated during a scale-down event.

      * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be
      terminated during a scale-down event.
    """


_ClientDescribeGameSessionDetailsResponseTypeDef = TypedDict(
    "_ClientDescribeGameSessionDetailsResponseTypeDef",
    {
        "GameSessionDetails": List[
            ClientDescribeGameSessionDetailsResponseGameSessionDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeGameSessionDetailsResponseTypeDef(
    _ClientDescribeGameSessionDetailsResponseTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionDetails` `Response`

    Represents the returned data in response to a request action.

    - **GameSessionDetails** *(list) --*

      Collection of objects containing game session properties and the protection policy currently
      in force for each session matching the request.

      - *(dict) --*

        A game session's properties plus the protection policy currently in force.

        - **GameSession** *(dict) --*

          Object that describes a game session.

          - **GameSessionId** *(string) --*

            Unique identifier for the game session. A game session ARN has the following format:
            ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
            token>`` .

          - **Name** *(string) --*

            Descriptive label that is associated with a game session. Session names do not need to
            be unique.

          - **FleetId** *(string) --*

            Unique identifier for a fleet that the game session is running on.

          - **CreationTime** *(datetime) --*

            Time stamp indicating when this data object was created. Format is a number expressed
            in Unix time as milliseconds (for example "1469498468.057").

          - **TerminationTime** *(datetime) --*

            Time stamp indicating when this data object was terminated. Format is a number
            expressed in Unix time as milliseconds (for example "1469498468.057").

          - **CurrentPlayerSessionCount** *(integer) --*

            Number of players currently in the game session.

          - **MaximumPlayerSessionCount** *(integer) --*

            Maximum number of players that can be connected simultaneously to the game session.

          - **Status** *(string) --*

            Current status of the game session. A game session must have an ``ACTIVE`` status to
            have player sessions.

          - **StatusReason** *(string) --*

            Provides additional information about game session status. ``INTERRUPTED`` indicates
            that the game session was hosted on a spot instance that was reclaimed, causing the
            active game session to be terminated.

          - **GameProperties** *(list) --*

            Set of custom properties for a game session, formatted as key:value pairs. These
            properties are passed to a game server process in the  GameSession object with a
            request to start a new game session (see `Start a Game Session
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
            ). You can search for active game sessions based on this custom data with
            SearchGameSessions .

            - *(dict) --*

              Set of key-value pairs that contain information about a game session. When included
              in a game session request, these properties communicate details to be used when
              setting up the new game session, such as to specify a game mode, level, or map. Game
              properties are passed to the game server process when initiating a new game session;
              the server process uses the properties as appropriate. For more information, see the
              `Amazon GameLift Developer Guide
              <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
              .

              - **Key** *(string) --*

                Game property identifier.

              - **Value** *(string) --*

                Game property value.

          - **IpAddress** *(string) --*

            IP address of the game session. To connect to a Amazon GameLift game server, an app
            needs both the IP address and port number.

          - **DnsName** *(string) --*

          - **Port** *(integer) --*

            Port number for the game session. To connect to a Amazon GameLift game server, an app
            needs both the IP address and port number.

          - **PlayerSessionCreationPolicy** *(string) --*

            Indicates whether or not the game session is accepting new players.

          - **CreatorId** *(string) --*

            Unique identifier for a player. This ID is used to enforce a resource protection policy
            (if one exists), that limits the number of game sessions a player can create.

          - **GameSessionData** *(string) --*

            Set of custom game session properties, formatted as a single string value. This data is
            passed to a game server process in the  GameSession object with a request to start a
            new game session (see `Start a Game Session
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
            ).

          - **MatchmakerData** *(string) --*

            Information about the matchmaking process that was used to create the game session. It
            is in JSON syntax, formatted as a string. In addition the matchmaking configuration
            used, it contains data on all players assigned to the match, including player
            attributes and team assignments. For more details on matchmaker data, see `Match Data
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
            . Matchmaker data is useful when requesting match backfills, and is updated whenever
            new players are added during a successful backfill (see  StartMatchBackfill ).

        - **ProtectionPolicy** *(string) --*

          Current status of protection for the game session.

          * **NoProtection** -- The game session can be terminated during a scale-down event.

          * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be
          terminated during a scale-down event.

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "_ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef(
    _ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionPlacementResponseGameSessionPlacement` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a
    game session request, these properties communicate details to be used when setting up the
    new game session, such as to specify a game mode, level, or map. Game properties are
    passed to the game server process when initiating a new game session; the server process
    uses the properties as appropriate. For more information, see the `Amazon GameLift
    Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef = TypedDict(
    "_ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef(
    _ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionPlacementResponseGameSessionPlacement` `PlacedPlayerSessions`

    Information about a player session that was created as part of a
    StartGameSessionPlacement request. This object contains only the player ID and player
    session ID. To retrieve full details on a player session, call  DescribePlayerSessions
    with the player session ID.

    *  CreatePlayerSession

    *  CreatePlayerSessions

    *  DescribePlayerSessions

    * Game session placements

      *  StartGameSessionPlacement

      *  DescribeGameSessionPlacement

      *  StopGameSessionPlacement

    - **PlayerId** *(string) --*

      Unique identifier for a player that is associated with this player session.

    - **PlayerSessionId** *(string) --*

      Unique identifier for a player session.
    """


_ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "_ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": float},
    total=False,
)


class ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef(
    _ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionPlacementResponseGameSessionPlacement` `PlayerLatencies`

    Regional latency information for a player, used when requesting a new game session with
    StartGameSessionPlacement . This value indicates the amount of time lag that exists when
    the player is connected to a fleet in the specified region. The relative difference
    between a player's latency values for multiple regions are used to determine which fleets
    are best suited to place a new game session for the player.

    - **PlayerId** *(string) --*

      Unique identifier for a player associated with the latency data.

    - **RegionIdentifier** *(string) --*

      Name of the region that is associated with the latency value.

    - **LatencyInMilliseconds** *(float) --*

      Amount of time that represents the time lag experienced by the player when connected to
      the specified region.
    """


_ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef = TypedDict(
    "_ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "Status": str,
        "GameProperties": List[
            ClientDescribeGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
        ],
        "MaximumPlayerSessionCount": int,
        "GameSessionName": str,
        "GameSessionId": str,
        "GameSessionArn": str,
        "GameSessionRegion": str,
        "PlayerLatencies": List[
            ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlacedPlayerSessions": List[
            ClientDescribeGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
        ],
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef(
    _ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionPlacementResponse` `GameSessionPlacement`

    Object that describes the requested game session placement.

    - **PlacementId** *(string) --*

      Unique identifier for a game session placement.

    - **GameSessionQueueName** *(string) --*

      Descriptive label that is associated with game session queue. Queue names must be unique
      within each region.

    - **Status** *(string) --*

      Current status of the game session placement request.

      * **PENDING** -- The placement request is currently in the queue waiting to be processed.

      * **FULFILLED** -- A new game session and player sessions (if requested) have been
      successfully created. Values for *GameSessionArn* and *GameSessionRegion* are available.

      * **CANCELLED** -- The placement request was canceled with a call to
      StopGameSessionPlacement .

      * **TIMED_OUT** -- A new game session was not successfully created before the time limit
      expired. You can resubmit the placement request as needed.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These properties
      are passed to a game server process in the  GameSession object with a request to start a
      new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in a
        game session request, these properties communicate details to be used when setting up the
        new game session, such as to specify a game mode, level, or map. Game properties are
        passed to the game server process when initiating a new game session; the server process
        uses the properties as appropriate. For more information, see the `Amazon GameLift
        Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **GameSessionName** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to be
      unique.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. This value is set once the new game session is
      placed (placement status is ``FULFILLED`` ).

    - **GameSessionArn** *(string) --*

      Identifier for the game session created by this placement request. This value is set once
      the new game session is placed (placement status is ``FULFILLED`` ). This identifier is
      unique across all regions. You can use this value as a ``GameSessionId`` value as needed.

    - **GameSessionRegion** *(string) --*

      Name of the region where the game session created by this placement request is running.
      This value is set once the new game session is placed (placement status is ``FULFILLED`` ).

    - **PlayerLatencies** *(list) --*

      Set of values, expressed in milliseconds, indicating the amount of latency that a player
      experiences when connected to AWS regions.

      - *(dict) --*

        Regional latency information for a player, used when requesting a new game session with
        StartGameSessionPlacement . This value indicates the amount of time lag that exists when
        the player is connected to a fleet in the specified region. The relative difference
        between a player's latency values for multiple regions are used to determine which fleets
        are best suited to place a new game session for the player.

        - **PlayerId** *(string) --*

          Unique identifier for a player associated with the latency data.

        - **RegionIdentifier** *(string) --*

          Name of the region that is associated with the latency value.

        - **LatencyInMilliseconds** *(float) --*

          Amount of time that represents the time lag experienced by the player when connected to
          the specified region.

    - **StartTime** *(datetime) --*

      Time stamp indicating when this request was placed in the queue. Format is a number
      expressed in Unix time as milliseconds (for example "1469498468.057").

    - **EndTime** *(datetime) --*

      Time stamp indicating when this request was completed, canceled, or timed out.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number. This value is set once the new game session is placed
      (placement status is ``FULFILLED`` ).

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number. This value is set once the new game session is placed
      (placement status is ``FULFILLED`` ).

    - **PlacedPlayerSessions** *(list) --*

      Collection of information on player sessions created in response to the game session
      placement request. These player sessions are created only once a new game session is
      successfully placed (placement status is ``FULFILLED`` ). This information includes the
      player ID (as provided in the placement request) and the corresponding player session ID.
      Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.

      - *(dict) --*

        Information about a player session that was created as part of a
        StartGameSessionPlacement request. This object contains only the player ID and player
        session ID. To retrieve full details on a player session, call  DescribePlayerSessions
        with the player session ID.

        *  CreatePlayerSession

        *  CreatePlayerSessions

        *  DescribePlayerSessions

        * Game session placements

          *  StartGameSessionPlacement

          *  DescribeGameSessionPlacement

          *  StopGameSessionPlacement

        - **PlayerId** *(string) --*

          Unique identifier for a player that is associated with this player session.

        - **PlayerSessionId** *(string) --*

          Unique identifier for a player session.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information on the matchmaking process for this game. Data is in JSON syntax, formatted as
      a string. It identifies the matchmaking configuration used to create the match, and
      contains data on all players assigned to the match, including player attributes and team
      assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      .
    """


_ClientDescribeGameSessionPlacementResponseTypeDef = TypedDict(
    "_ClientDescribeGameSessionPlacementResponseTypeDef",
    {
        "GameSessionPlacement": ClientDescribeGameSessionPlacementResponseGameSessionPlacementTypeDef
    },
    total=False,
)


class ClientDescribeGameSessionPlacementResponseTypeDef(
    _ClientDescribeGameSessionPlacementResponseTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionPlacement` `Response`

    Represents the returned data in response to a request action.

    - **GameSessionPlacement** *(dict) --*

      Object that describes the requested game session placement.

      - **PlacementId** *(string) --*

        Unique identifier for a game session placement.

      - **GameSessionQueueName** *(string) --*

        Descriptive label that is associated with game session queue. Queue names must be unique
        within each region.

      - **Status** *(string) --*

        Current status of the game session placement request.

        * **PENDING** -- The placement request is currently in the queue waiting to be processed.

        * **FULFILLED** -- A new game session and player sessions (if requested) have been
        successfully created. Values for *GameSessionArn* and *GameSessionRegion* are available.

        * **CANCELLED** -- The placement request was canceled with a call to
        StopGameSessionPlacement .

        * **TIMED_OUT** -- A new game session was not successfully created before the time limit
        expired. You can resubmit the placement request as needed.

      - **GameProperties** *(list) --*

        Set of custom properties for a game session, formatted as key:value pairs. These properties
        are passed to a game server process in the  GameSession object with a request to start a
        new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ).

        - *(dict) --*

          Set of key-value pairs that contain information about a game session. When included in a
          game session request, these properties communicate details to be used when setting up the
          new game session, such as to specify a game mode, level, or map. Game properties are
          passed to the game server process when initiating a new game session; the server process
          uses the properties as appropriate. For more information, see the `Amazon GameLift
          Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
          .

          - **Key** *(string) --*

            Game property identifier.

          - **Value** *(string) --*

            Game property value.

      - **MaximumPlayerSessionCount** *(integer) --*

        Maximum number of players that can be connected simultaneously to the game session.

      - **GameSessionName** *(string) --*

        Descriptive label that is associated with a game session. Session names do not need to be
        unique.

      - **GameSessionId** *(string) --*

        Unique identifier for the game session. This value is set once the new game session is
        placed (placement status is ``FULFILLED`` ).

      - **GameSessionArn** *(string) --*

        Identifier for the game session created by this placement request. This value is set once
        the new game session is placed (placement status is ``FULFILLED`` ). This identifier is
        unique across all regions. You can use this value as a ``GameSessionId`` value as needed.

      - **GameSessionRegion** *(string) --*

        Name of the region where the game session created by this placement request is running.
        This value is set once the new game session is placed (placement status is ``FULFILLED`` ).

      - **PlayerLatencies** *(list) --*

        Set of values, expressed in milliseconds, indicating the amount of latency that a player
        experiences when connected to AWS regions.

        - *(dict) --*

          Regional latency information for a player, used when requesting a new game session with
          StartGameSessionPlacement . This value indicates the amount of time lag that exists when
          the player is connected to a fleet in the specified region. The relative difference
          between a player's latency values for multiple regions are used to determine which fleets
          are best suited to place a new game session for the player.

          - **PlayerId** *(string) --*

            Unique identifier for a player associated with the latency data.

          - **RegionIdentifier** *(string) --*

            Name of the region that is associated with the latency value.

          - **LatencyInMilliseconds** *(float) --*

            Amount of time that represents the time lag experienced by the player when connected to
            the specified region.

      - **StartTime** *(datetime) --*

        Time stamp indicating when this request was placed in the queue. Format is a number
        expressed in Unix time as milliseconds (for example "1469498468.057").

      - **EndTime** *(datetime) --*

        Time stamp indicating when this request was completed, canceled, or timed out.

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number. This value is set once the new game session is placed
        (placement status is ``FULFILLED`` ).

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number. This value is set once the new game session is placed
        (placement status is ``FULFILLED`` ).

      - **PlacedPlayerSessions** *(list) --*

        Collection of information on player sessions created in response to the game session
        placement request. These player sessions are created only once a new game session is
        successfully placed (placement status is ``FULFILLED`` ). This information includes the
        player ID (as provided in the placement request) and the corresponding player session ID.
        Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.

        - *(dict) --*

          Information about a player session that was created as part of a
          StartGameSessionPlacement request. This object contains only the player ID and player
          session ID. To retrieve full details on a player session, call  DescribePlayerSessions
          with the player session ID.

          *  CreatePlayerSession

          *  CreatePlayerSessions

          *  DescribePlayerSessions

          * Game session placements

            *  StartGameSessionPlacement

            *  DescribeGameSessionPlacement

            *  StopGameSessionPlacement

          - **PlayerId** *(string) --*

            Unique identifier for a player that is associated with this player session.

          - **PlayerSessionId** *(string) --*

            Unique identifier for a player session.

      - **GameSessionData** *(string) --*

        Set of custom game session properties, formatted as a single string value. This data is
        passed to a game server process in the  GameSession object with a request to start a new
        game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ).

      - **MatchmakerData** *(string) --*

        Information on the matchmaking process for this game. Data is in JSON syntax, formatted as
        a string. It identifies the matchmaking configuration used to create the match, and
        contains data on all players assigned to the match, including player attributes and team
        assignments. For more details on matchmaker data, see `Match Data
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
        .
    """


_ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef = TypedDict(
    "_ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)


class ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef(
    _ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionQueuesResponseGameSessionQueues` `Destinations`

    Fleet designated in a game session queue. Requests for new game sessions in the queue
    are fulfilled by starting a new game session on any destination configured for a queue.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **DestinationArn** *(string) --*

      Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
      fleet ID or alias ID and a region name, provide a unique identifier across all
      regions.
    """


_ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef = TypedDict(
    "_ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef(
    _ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionQueuesResponseGameSessionQueues` `PlayerLatencyPolicies`

    Queue setting that determines the highest latency allowed for individual players when
    placing a game session. When a latency policy is in force, a game session cannot be
    placed at any destination in a region where a player is reporting latency higher than
    the cap. Latency policies are only enforced when the placement request contains player
    latency information.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

      The maximum latency value that is allowed for any player, in milliseconds. All
      policies must have a value set for this property.

    - **PolicyDurationSeconds** *(integer) --*

      The length of time, in seconds, that the policy is enforced while placing a new game
      session. A null value for this property means that the policy is enforced until the
      queue times out.
    """


_ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef = TypedDict(
    "_ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List[
            ClientDescribeGameSessionQueuesResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef
        ],
        "Destinations": List[
            ClientDescribeGameSessionQueuesResponseGameSessionQueuesDestinationsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef(
    _ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionQueuesResponse` `GameSessionQueues`

    Configuration of a queue that is used to process game session placement requests. The queue
    configuration identifies several game features:

    * The destinations where a new game session can potentially be hosted. Amazon GameLift
    tries these destinations in an order based on either the queue's default order or player
    latency information, if provided in a placement request. With latency information, Amazon
    GameLift can place game sessions where the majority of players are reporting the lowest
    possible latency.

    * The length of time that placement requests can wait in the queue before timing out.

    * A set of optional latency policies that protect individual players from high latencies,
    preventing game sessions from being placed where any individual player is reporting latency
    higher than a policy's maximum.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **Name** *(string) --*

      Descriptive label that is associated with game session queue. Queue names must be unique
      within each region.

    - **GameSessionQueueArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
      assigned to a game session queue and uniquely identifies it. Format is
      ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` .

    - **TimeoutInSeconds** *(integer) --*

      Maximum time, in seconds, that a new game session placement request remains in the queue.
      When a request exceeds this time, the game session placement changes to a ``TIMED_OUT``
      status.

    - **PlayerLatencyPolicies** *(list) --*

      Collection of latency policies to apply when processing game sessions placement requests
      with player latency information. Multiple policies are evaluated in order of the maximum
      latency value, starting with the lowest latency values. With just one policy, it is
      enforced at the start of the game session placement for the duration period. With
      multiple policies, each policy is enforced consecutively for its duration period. For
      example, a queue might enforce a 60-second policy followed by a 120-second policy, and
      then no policy for the remainder of the placement.

      - *(dict) --*

        Queue setting that determines the highest latency allowed for individual players when
        placing a game session. When a latency policy is in force, a game session cannot be
        placed at any destination in a region where a player is reporting latency higher than
        the cap. Latency policies are only enforced when the placement request contains player
        latency information.

        *  CreateGameSessionQueue

        *  DescribeGameSessionQueues

        *  UpdateGameSessionQueue

        *  DeleteGameSessionQueue

        - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

          The maximum latency value that is allowed for any player, in milliseconds. All
          policies must have a value set for this property.

        - **PolicyDurationSeconds** *(integer) --*

          The length of time, in seconds, that the policy is enforced while placing a new game
          session. A null value for this property means that the policy is enforced until the
          queue times out.

    - **Destinations** *(list) --*

      List of fleets that can be used to fulfill game session placement requests in the queue.
      Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed
      in default preference order.

      - *(dict) --*

        Fleet designated in a game session queue. Requests for new game sessions in the queue
        are fulfilled by starting a new game session on any destination configured for a queue.

        *  CreateGameSessionQueue

        *  DescribeGameSessionQueues

        *  UpdateGameSessionQueue

        *  DeleteGameSessionQueue

        - **DestinationArn** *(string) --*

          Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
          fleet ID or alias ID and a region name, provide a unique identifier across all
          regions.
    """


_ClientDescribeGameSessionQueuesResponseTypeDef = TypedDict(
    "_ClientDescribeGameSessionQueuesResponseTypeDef",
    {
        "GameSessionQueues": List[
            ClientDescribeGameSessionQueuesResponseGameSessionQueuesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeGameSessionQueuesResponseTypeDef(
    _ClientDescribeGameSessionQueuesResponseTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionQueues` `Response`

    Represents the returned data in response to a request action.

    - **GameSessionQueues** *(list) --*

      Collection of objects that describes the requested game session queues.

      - *(dict) --*

        Configuration of a queue that is used to process game session placement requests. The queue
        configuration identifies several game features:

        * The destinations where a new game session can potentially be hosted. Amazon GameLift
        tries these destinations in an order based on either the queue's default order or player
        latency information, if provided in a placement request. With latency information, Amazon
        GameLift can place game sessions where the majority of players are reporting the lowest
        possible latency.

        * The length of time that placement requests can wait in the queue before timing out.

        * A set of optional latency policies that protect individual players from high latencies,
        preventing game sessions from being placed where any individual player is reporting latency
        higher than a policy's maximum.

        *  CreateGameSessionQueue

        *  DescribeGameSessionQueues

        *  UpdateGameSessionQueue

        *  DeleteGameSessionQueue

        - **Name** *(string) --*

          Descriptive label that is associated with game session queue. Queue names must be unique
          within each region.

        - **GameSessionQueueArn** *(string) --*

          Amazon Resource Name (`ARN
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
          assigned to a game session queue and uniquely identifies it. Format is
          ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` .

        - **TimeoutInSeconds** *(integer) --*

          Maximum time, in seconds, that a new game session placement request remains in the queue.
          When a request exceeds this time, the game session placement changes to a ``TIMED_OUT``
          status.

        - **PlayerLatencyPolicies** *(list) --*

          Collection of latency policies to apply when processing game sessions placement requests
          with player latency information. Multiple policies are evaluated in order of the maximum
          latency value, starting with the lowest latency values. With just one policy, it is
          enforced at the start of the game session placement for the duration period. With
          multiple policies, each policy is enforced consecutively for its duration period. For
          example, a queue might enforce a 60-second policy followed by a 120-second policy, and
          then no policy for the remainder of the placement.

          - *(dict) --*

            Queue setting that determines the highest latency allowed for individual players when
            placing a game session. When a latency policy is in force, a game session cannot be
            placed at any destination in a region where a player is reporting latency higher than
            the cap. Latency policies are only enforced when the placement request contains player
            latency information.

            *  CreateGameSessionQueue

            *  DescribeGameSessionQueues

            *  UpdateGameSessionQueue

            *  DeleteGameSessionQueue

            - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

              The maximum latency value that is allowed for any player, in milliseconds. All
              policies must have a value set for this property.

            - **PolicyDurationSeconds** *(integer) --*

              The length of time, in seconds, that the policy is enforced while placing a new game
              session. A null value for this property means that the policy is enforced until the
              queue times out.

        - **Destinations** *(list) --*

          List of fleets that can be used to fulfill game session placement requests in the queue.
          Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed
          in default preference order.

          - *(dict) --*

            Fleet designated in a game session queue. Requests for new game sessions in the queue
            are fulfilled by starting a new game session on any destination configured for a queue.

            *  CreateGameSessionQueue

            *  DescribeGameSessionQueues

            *  UpdateGameSessionQueue

            *  DeleteGameSessionQueue

            - **DestinationArn** *(string) --*

              Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
              fleet ID or alias ID and a region name, provide a unique identifier across all
              regions.

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "_ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef(
    _ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionsResponseGameSessions` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in
    a game session request, these properties communicate details to be used when setting up
    the new game session, such as to specify a game mode, level, or map. Game properties
    are passed to the game server process when initiating a new game session; the server
    process uses the properties as appropriate. For more information, see the `Amazon
    GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientDescribeGameSessionsResponseGameSessionsTypeDef = TypedDict(
    "_ClientDescribeGameSessionsResponseGameSessionsTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": str,
        "StatusReason": str,
        "GameProperties": List[
            ClientDescribeGameSessionsResponseGameSessionsGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": str,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class ClientDescribeGameSessionsResponseGameSessionsTypeDef(
    _ClientDescribeGameSessionsResponseGameSessionsTypeDef
):
    """
    Type definition for `ClientDescribeGameSessionsResponse` `GameSessions`

    Properties describing a game session.

    A game session in ACTIVE status can host players. When a game session ends, its status is
    set to ``TERMINATED`` .

    Once the session ends, the game session object is retained for 30 days. This means you can
    reuse idempotency token values after this time. Game session logs are retained for 14 days.

    *  CreateGameSession

    *  DescribeGameSessions

    *  DescribeGameSessionDetails

    *  SearchGameSessions

    *  UpdateGameSession

    *  GetGameSessionLogUrl

    * Game session placements

      *  StartGameSessionPlacement

      *  DescribeGameSessionPlacement

      *  StopGameSessionPlacement

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. A game session ARN has the following format:
      ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
      token>`` .

    - **Name** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to be
      unique.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **CurrentPlayerSessionCount** *(integer) --*

      Number of players currently in the game session.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **Status** *(string) --*

      Current status of the game session. A game session must have an ``ACTIVE`` status to have
      player sessions.

    - **StatusReason** *(string) --*

      Provides additional information about game session status. ``INTERRUPTED`` indicates that
      the game session was hosted on a spot instance that was reclaimed, causing the active
      game session to be terminated.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These
      properties are passed to a game server process in the  GameSession object with a request
      to start a new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). You can search for active game sessions based on this custom data with
      SearchGameSessions .

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in
        a game session request, these properties communicate details to be used when setting up
        the new game session, such as to specify a game mode, level, or map. Game properties
        are passed to the game server process when initiating a new game session; the server
        process uses the properties as appropriate. For more information, see the `Amazon
        GameLift Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **PlayerSessionCreationPolicy** *(string) --*

      Indicates whether or not the game session is accepting new players.

    - **CreatorId** *(string) --*

      Unique identifier for a player. This ID is used to enforce a resource protection policy
      (if one exists), that limits the number of game sessions a player can create.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information about the matchmaking process that was used to create the game session. It is
      in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
      contains data on all players assigned to the match, including player attributes and team
      assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      . Matchmaker data is useful when requesting match backfills, and is updated whenever new
      players are added during a successful backfill (see  StartMatchBackfill ).
    """


_ClientDescribeGameSessionsResponseTypeDef = TypedDict(
    "_ClientDescribeGameSessionsResponseTypeDef",
    {
        "GameSessions": List[ClientDescribeGameSessionsResponseGameSessionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeGameSessionsResponseTypeDef(
    _ClientDescribeGameSessionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeGameSessions` `Response`

    Represents the returned data in response to a request action.

    - **GameSessions** *(list) --*

      Collection of objects containing game session properties for each session matching the
      request.

      - *(dict) --*

        Properties describing a game session.

        A game session in ACTIVE status can host players. When a game session ends, its status is
        set to ``TERMINATED`` .

        Once the session ends, the game session object is retained for 30 days. This means you can
        reuse idempotency token values after this time. Game session logs are retained for 14 days.

        *  CreateGameSession

        *  DescribeGameSessions

        *  DescribeGameSessionDetails

        *  SearchGameSessions

        *  UpdateGameSession

        *  GetGameSessionLogUrl

        * Game session placements

          *  StartGameSessionPlacement

          *  DescribeGameSessionPlacement

          *  StopGameSessionPlacement

        - **GameSessionId** *(string) --*

          Unique identifier for the game session. A game session ARN has the following format:
          ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
          token>`` .

        - **Name** *(string) --*

          Descriptive label that is associated with a game session. Session names do not need to be
          unique.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the game session is running on.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **TerminationTime** *(datetime) --*

          Time stamp indicating when this data object was terminated. Format is a number expressed
          in Unix time as milliseconds (for example "1469498468.057").

        - **CurrentPlayerSessionCount** *(integer) --*

          Number of players currently in the game session.

        - **MaximumPlayerSessionCount** *(integer) --*

          Maximum number of players that can be connected simultaneously to the game session.

        - **Status** *(string) --*

          Current status of the game session. A game session must have an ``ACTIVE`` status to have
          player sessions.

        - **StatusReason** *(string) --*

          Provides additional information about game session status. ``INTERRUPTED`` indicates that
          the game session was hosted on a spot instance that was reclaimed, causing the active
          game session to be terminated.

        - **GameProperties** *(list) --*

          Set of custom properties for a game session, formatted as key:value pairs. These
          properties are passed to a game server process in the  GameSession object with a request
          to start a new game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ). You can search for active game sessions based on this custom data with
          SearchGameSessions .

          - *(dict) --*

            Set of key-value pairs that contain information about a game session. When included in
            a game session request, these properties communicate details to be used when setting up
            the new game session, such as to specify a game mode, level, or map. Game properties
            are passed to the game server process when initiating a new game session; the server
            process uses the properties as appropriate. For more information, see the `Amazon
            GameLift Developer Guide
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
            .

            - **Key** *(string) --*

              Game property identifier.

            - **Value** *(string) --*

              Game property value.

        - **IpAddress** *(string) --*

          IP address of the game session. To connect to a Amazon GameLift game server, an app needs
          both the IP address and port number.

        - **DnsName** *(string) --*

        - **Port** *(integer) --*

          Port number for the game session. To connect to a Amazon GameLift game server, an app
          needs both the IP address and port number.

        - **PlayerSessionCreationPolicy** *(string) --*

          Indicates whether or not the game session is accepting new players.

        - **CreatorId** *(string) --*

          Unique identifier for a player. This ID is used to enforce a resource protection policy
          (if one exists), that limits the number of game sessions a player can create.

        - **GameSessionData** *(string) --*

          Set of custom game session properties, formatted as a single string value. This data is
          passed to a game server process in the  GameSession object with a request to start a new
          game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ).

        - **MatchmakerData** *(string) --*

          Information about the matchmaking process that was used to create the game session. It is
          in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
          contains data on all players assigned to the match, including player attributes and team
          assignments. For more details on matchmaker data, see `Match Data
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
          . Matchmaker data is useful when requesting match backfills, and is updated whenever new
          players are added during a successful backfill (see  StartMatchBackfill ).

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribeInstancesResponseInstancesTypeDef = TypedDict(
    "_ClientDescribeInstancesResponseInstancesTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "DnsName": str,
        "OperatingSystem": str,
        "Type": str,
        "Status": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeInstancesResponseInstancesTypeDef(
    _ClientDescribeInstancesResponseInstancesTypeDef
):
    """
    Type definition for `ClientDescribeInstancesResponse` `Instances`

    Properties that describe an instance of a virtual computing resource that hosts one or more
    game servers. A fleet may contain zero or more instances.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the instance is in.

    - **InstanceId** *(string) --*

      Unique identifier for an instance.

    - **IpAddress** *(string) --*

      IP address assigned to the instance.

    - **DnsName** *(string) --*

    - **OperatingSystem** *(string) --*

      Operating system that is running on this instance.

    - **Type** *(string) --*

      EC2 instance type that defines the computing resources of this instance.

    - **Status** *(string) --*

      Current status of the instance. Possible statuses include the following:

      * **PENDING** -- The instance is in the process of being created and launching server
      processes as defined in the fleet's run-time configuration.

      * **ACTIVE** -- The instance has been successfully created and at least one server
      process has successfully launched and reported back to Amazon GameLift that it is ready
      to host a game session. The instance is now considered ready to host game sessions.

      * **TERMINATING** -- The instance is in the process of shutting down. This may happen to
      reduce capacity during a scaling down event or to recycle resources in the event of a
      problem.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").
    """


_ClientDescribeInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeInstancesResponseTypeDef",
    {
        "Instances": List[ClientDescribeInstancesResponseInstancesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeInstancesResponseTypeDef(_ClientDescribeInstancesResponseTypeDef):
    """
    Type definition for `ClientDescribeInstances` `Response`

    Represents the returned data in response to a request action.

    - **Instances** *(list) --*

      Collection of objects containing properties for each instance returned.

      - *(dict) --*

        Properties that describe an instance of a virtual computing resource that hosts one or more
        game servers. A fleet may contain zero or more instances.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the instance is in.

        - **InstanceId** *(string) --*

          Unique identifier for an instance.

        - **IpAddress** *(string) --*

          IP address assigned to the instance.

        - **DnsName** *(string) --*

        - **OperatingSystem** *(string) --*

          Operating system that is running on this instance.

        - **Type** *(string) --*

          EC2 instance type that defines the computing resources of this instance.

        - **Status** *(string) --*

          Current status of the instance. Possible statuses include the following:

          * **PENDING** -- The instance is in the process of being created and launching server
          processes as defined in the fleet's run-time configuration.

          * **ACTIVE** -- The instance has been successfully created and at least one server
          process has successfully launched and reported back to Amazon GameLift that it is ready
          to host a game session. The instance is now considered ready to host game sessions.

          * **TERMINATING** -- The instance is in the process of shutting down. This may happen to
          reduce capacity during a scaling down event or to recycle resources in the event of a
          problem.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef = TypedDict(
    "_ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef(
    _ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef
):
    """
    Type definition for `ClientDescribeMatchmakingConfigurationsResponseConfigurations` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in
    a game session request, these properties communicate details to be used when setting up
    the new game session, such as to specify a game mode, level, or map. Game properties
    are passed to the game server process when initiating a new game session; the server
    process uses the properties as appropriate. For more information, see the `Amazon
    GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef = TypedDict(
    "_ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef",
    {
        "Name": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List[
            ClientDescribeMatchmakingConfigurationsResponseConfigurationsGamePropertiesTypeDef
        ],
        "GameSessionData": str,
        "BackfillMode": str,
    },
    total=False,
)


class ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef(
    _ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeMatchmakingConfigurationsResponse` `Configurations`

    Guidelines for use with FlexMatch to match players into games. All matchmaking requests
    must specify a matchmaking configuration.

    - **Name** *(string) --*

      Unique identifier for a matchmaking configuration. This name is used to identify the
      configuration associated with a matchmaking request or ticket.

    - **Description** *(string) --*

      Descriptive label that is associated with matchmaking configuration.

    - **GameSessionQueueArns** *(list) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
      assigned to a game session queue and uniquely identifies it. Format is
      ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` . These queues
      are used when placing game sessions for matches that are created with this matchmaking
      configuration. Queues can be located in any region.

      - *(string) --*

    - **RequestTimeoutSeconds** *(integer) --*

      Maximum duration, in seconds, that a matchmaking ticket can remain in process before
      timing out. Requests that fail due to timing out can be resubmitted as needed.

    - **AcceptanceTimeoutSeconds** *(integer) --*

      Length of time (in seconds) to wait for players to accept a proposed match. If any player
      rejects the match or fails to accept before the timeout, the ticket continues to look for
      an acceptable match.

    - **AcceptanceRequired** *(boolean) --*

      Flag that determines whether a match that was created with this configuration must be
      accepted by the matched players. To require acceptance, set to TRUE.

    - **RuleSetName** *(string) --*

      Unique identifier for a matchmaking rule set to use with this configuration. A
      matchmaking configuration can only use rule sets that are defined in the same region.

    - **NotificationTarget** *(string) --*

      SNS topic ARN that is set up to receive matchmaking notifications.

    - **AdditionalPlayerCount** *(integer) --*

      Number of player slots in a match to keep open for future players. For example, if the
      configuration's rule set specifies a match for a single 12-person team, and the
      additional player count is set to 2, only 10 players are selected for the match.

    - **CustomEventData** *(string) --*

      Information to attach to all events related to the matchmaking configuration.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These
      properties are passed to a game server process in the  GameSession object with a request
      to start a new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). This information is added to the new  GameSession object that is created for a
      successful match.

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in
        a game session request, these properties communicate details to be used when setting up
        the new game session, such as to specify a game mode, level, or map. Game properties
        are passed to the game server process when initiating a new game session; the server
        process uses the properties as appropriate. For more information, see the `Amazon
        GameLift Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). This information is added to the new  GameSession object that is created for a
      successful match.

    - **BackfillMode** *(string) --*

      Method used to backfill game sessions created with this matchmaking configuration. MANUAL
      indicates that the game makes backfill requests or does not use the match backfill
      feature. AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever
      a game session has one or more open slots. Learn more about manual and automatic backfill
      in `Backfill Existing Games with FlexMatch
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-backfill.html>`__ .
    """


_ClientDescribeMatchmakingConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeMatchmakingConfigurationsResponseTypeDef",
    {
        "Configurations": List[
            ClientDescribeMatchmakingConfigurationsResponseConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeMatchmakingConfigurationsResponseTypeDef(
    _ClientDescribeMatchmakingConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeMatchmakingConfigurations` `Response`

    Represents the returned data in response to a request action.

    - **Configurations** *(list) --*

      Collection of requested matchmaking configuration objects.

      - *(dict) --*

        Guidelines for use with FlexMatch to match players into games. All matchmaking requests
        must specify a matchmaking configuration.

        - **Name** *(string) --*

          Unique identifier for a matchmaking configuration. This name is used to identify the
          configuration associated with a matchmaking request or ticket.

        - **Description** *(string) --*

          Descriptive label that is associated with matchmaking configuration.

        - **GameSessionQueueArns** *(list) --*

          Amazon Resource Name (`ARN
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
          assigned to a game session queue and uniquely identifies it. Format is
          ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` . These queues
          are used when placing game sessions for matches that are created with this matchmaking
          configuration. Queues can be located in any region.

          - *(string) --*

        - **RequestTimeoutSeconds** *(integer) --*

          Maximum duration, in seconds, that a matchmaking ticket can remain in process before
          timing out. Requests that fail due to timing out can be resubmitted as needed.

        - **AcceptanceTimeoutSeconds** *(integer) --*

          Length of time (in seconds) to wait for players to accept a proposed match. If any player
          rejects the match or fails to accept before the timeout, the ticket continues to look for
          an acceptable match.

        - **AcceptanceRequired** *(boolean) --*

          Flag that determines whether a match that was created with this configuration must be
          accepted by the matched players. To require acceptance, set to TRUE.

        - **RuleSetName** *(string) --*

          Unique identifier for a matchmaking rule set to use with this configuration. A
          matchmaking configuration can only use rule sets that are defined in the same region.

        - **NotificationTarget** *(string) --*

          SNS topic ARN that is set up to receive matchmaking notifications.

        - **AdditionalPlayerCount** *(integer) --*

          Number of player slots in a match to keep open for future players. For example, if the
          configuration's rule set specifies a match for a single 12-person team, and the
          additional player count is set to 2, only 10 players are selected for the match.

        - **CustomEventData** *(string) --*

          Information to attach to all events related to the matchmaking configuration.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **GameProperties** *(list) --*

          Set of custom properties for a game session, formatted as key:value pairs. These
          properties are passed to a game server process in the  GameSession object with a request
          to start a new game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ). This information is added to the new  GameSession object that is created for a
          successful match.

          - *(dict) --*

            Set of key-value pairs that contain information about a game session. When included in
            a game session request, these properties communicate details to be used when setting up
            the new game session, such as to specify a game mode, level, or map. Game properties
            are passed to the game server process when initiating a new game session; the server
            process uses the properties as appropriate. For more information, see the `Amazon
            GameLift Developer Guide
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
            .

            - **Key** *(string) --*

              Game property identifier.

            - **Value** *(string) --*

              Game property value.

        - **GameSessionData** *(string) --*

          Set of custom game session properties, formatted as a single string value. This data is
          passed to a game server process in the  GameSession object with a request to start a new
          game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ). This information is added to the new  GameSession object that is created for a
          successful match.

        - **BackfillMode** *(string) --*

          Method used to backfill game sessions created with this matchmaking configuration. MANUAL
          indicates that the game makes backfill requests or does not use the match backfill
          feature. AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever
          a game session has one or more open slots. Learn more about manual and automatic backfill
          in `Backfill Existing Games with FlexMatch
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-backfill.html>`__ .

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef(
    _ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
):
    """
    Type definition for `ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfo` `MatchedPlayerSessions`

    Represents a new player session that is created as a result of a successful FlexMatch
    match. A successful match automatically creates new player sessions for every player
    ID in the original matchmaking request.

    When players connect to the match's game session, they must include both player ID
    and player session ID in order to claim their assigned player slot.

    - **PlayerId** *(string) --*

      Unique identifier for a player

    - **PlayerSessionId** *(string) --*

      Unique identifier for a player session
    """


_ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "MatchedPlayerSessions": List[
            ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef(
    _ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef
):
    """
    Type definition for `ClientDescribeMatchmakingResponseTicketList` `GameSessionConnectionInfo`

    Identifier and connection information of the game session created for the match. This
    information is added to the ticket only after the matchmaking request has been
    successfully completed.

    - **GameSessionArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
      assigned to a game session and uniquely identifies it.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **MatchedPlayerSessions** *(list) --*

      Collection of player session IDs, one for each player ID that was included in the
      original matchmaking request.

      - *(dict) --*

        Represents a new player session that is created as a result of a successful FlexMatch
        match. A successful match automatically creates new player sessions for every player
        ID in the original matchmaking request.

        When players connect to the match's game session, they must include both player ID
        and player session ID in order to claim their assigned player slot.

        - **PlayerId** *(string) --*

          Unique identifier for a player

        - **PlayerSessionId** *(string) --*

          Unique identifier for a player session
    """


_ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)


class ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef(
    _ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef
):
    """
    Type definition for `ClientDescribeMatchmakingResponseTicketListPlayers` `PlayerAttributes`

    Values for use in  Player attribute key:value pairs. This object lets you specify
    an attribute value using any of the valid data types: string, number, string
    array, or data map. Each ``AttributeValue`` object can use only one of the
    available properties.

    - **S** *(string) --*

      For single string values. Maximum string length is 100 characters.

    - **N** *(float) --*

      For number values, expressed as double.

    - **SL** *(list) --*

      For a list of up to 10 strings. Maximum length for each string is 100
      characters. Duplicate values are not recognized; all occurrences of the
      repeated value after the first of a repeated value are ignored.

      - *(string) --*

    - **SDM** *(dict) --*

      For a map of up to 10 data type:value pairs. Maximum length for each string
      value is 100 characters.

      - *(string) --*

        - *(float) --*
    """


_ClientDescribeMatchmakingResponseTicketListPlayersTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTicketListPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[
            str,
            ClientDescribeMatchmakingResponseTicketListPlayersPlayerAttributesTypeDef,
        ],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)


class ClientDescribeMatchmakingResponseTicketListPlayersTypeDef(
    _ClientDescribeMatchmakingResponseTicketListPlayersTypeDef
):
    """
    Type definition for `ClientDescribeMatchmakingResponseTicketList` `Players`

    Represents a player in matchmaking. When starting a matchmaking request, a player has a
    player ID, attributes, and may have latency data. Team information is added after a
    match has been successfully completed.

    - **PlayerId** *(string) --*

      Unique identifier for a player

    - **PlayerAttributes** *(dict) --*

      Collection of key:value pairs containing player information for use in matchmaking.
      Player attribute keys must match the *playerAttributes* used in a matchmaking rule
      set. Example: ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S":
      "deathmatch"}}`` .

      - *(string) --*

        - *(dict) --*

          Values for use in  Player attribute key:value pairs. This object lets you specify
          an attribute value using any of the valid data types: string, number, string
          array, or data map. Each ``AttributeValue`` object can use only one of the
          available properties.

          - **S** *(string) --*

            For single string values. Maximum string length is 100 characters.

          - **N** *(float) --*

            For number values, expressed as double.

          - **SL** *(list) --*

            For a list of up to 10 strings. Maximum length for each string is 100
            characters. Duplicate values are not recognized; all occurrences of the
            repeated value after the first of a repeated value are ignored.

            - *(string) --*

          - **SDM** *(dict) --*

            For a map of up to 10 data type:value pairs. Maximum length for each string
            value is 100 characters.

            - *(string) --*

              - *(float) --*

    - **Team** *(string) --*

      Name of the team that the player is assigned to in a match. Team names are defined in
      a matchmaking rule set.

    - **LatencyInMs** *(dict) --*

      Set of values, expressed in milliseconds, indicating the amount of latency that a
      player experiences when connected to AWS regions. If this property is present,
      FlexMatch considers placing the match only in regions for which latency is reported.

      If a matchmaker has a rule that evaluates player latency, players must report latency
      in order to be matched. If no latency is reported in this scenario, FlexMatch assumes
      that no regions are available to the player and the ticket is not matchable.

      - *(string) --*

        - *(integer) --*
    """


_ClientDescribeMatchmakingResponseTicketListTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTicketListTypeDef",
    {
        "TicketId": str,
        "ConfigurationName": str,
        "Status": str,
        "StatusReason": str,
        "StatusMessage": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Players": List[ClientDescribeMatchmakingResponseTicketListPlayersTypeDef],
        "GameSessionConnectionInfo": ClientDescribeMatchmakingResponseTicketListGameSessionConnectionInfoTypeDef,
        "EstimatedWaitTime": int,
    },
    total=False,
)


class ClientDescribeMatchmakingResponseTicketListTypeDef(
    _ClientDescribeMatchmakingResponseTicketListTypeDef
):
    """
    Type definition for `ClientDescribeMatchmakingResponse` `TicketList`

    Ticket generated to track the progress of a matchmaking request. Each ticket is uniquely
    identified by a ticket ID, supplied by the requester, when creating a matchmaking request
    with  StartMatchmaking . Tickets can be retrieved by calling  DescribeMatchmaking with the
    ticket ID.

    - **TicketId** *(string) --*

      Unique identifier for a matchmaking ticket.

    - **ConfigurationName** *(string) --*

      Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking
      configurations determine how players are grouped into a match and how a new game session
      is created for the match.

    - **Status** *(string) --*

      Current status of the matchmaking request.

      * **QUEUED** -- The matchmaking request has been received and is currently waiting to be
      processed.

      * **SEARCHING** -- The matchmaking request is currently being processed.

      * **REQUIRES_ACCEPTANCE** -- A match has been proposed and the players must accept the
      match (see  AcceptMatch ). This status is used only with requests that use a matchmaking
      configuration with a player acceptance requirement.

      * **PLACING** -- The FlexMatch engine has matched players and is in the process of
      placing a new game session for the match.

      * **COMPLETED** -- Players have been matched and a game session is ready to host the
      players. A ticket in this state contains the necessary connection information for players.

      * **FAILED** -- The matchmaking request was not completed.

      * **CANCELLED** -- The matchmaking request was canceled. This may be the result of a call
      to  StopMatchmaking or a proposed match that one or more players failed to accept.

      * **TIMED_OUT** -- The matchmaking request was not successful within the duration
      specified in the matchmaking configuration.

      .. note::

        Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED,
        TIMED_OUT) can be resubmitted as new requests with new ticket IDs.

    - **StatusReason** *(string) --*

      Code to explain the current status. For example, a status reason may indicate when a
      ticket has returned to ``SEARCHING`` status after a proposed match fails to receive
      player acceptances.

    - **StatusMessage** *(string) --*

      Additional information about the current status.

    - **StartTime** *(datetime) --*

      Time stamp indicating when this matchmaking request was received. Format is a number
      expressed in Unix time as milliseconds (for example "1469498468.057").

    - **EndTime** *(datetime) --*

      Time stamp indicating when this matchmaking request stopped being processed due to
      success, failure, or cancellation. Format is a number expressed in Unix time as
      milliseconds (for example "1469498468.057").

    - **Players** *(list) --*

      A set of ``Player`` objects, each representing a player to find matches for. Players are
      identified by a unique player ID and may include latency data for use during matchmaking.
      If the ticket is in status ``COMPLETED`` , the ``Player`` objects include the team the
      players were assigned to in the resulting match.

      - *(dict) --*

        Represents a player in matchmaking. When starting a matchmaking request, a player has a
        player ID, attributes, and may have latency data. Team information is added after a
        match has been successfully completed.

        - **PlayerId** *(string) --*

          Unique identifier for a player

        - **PlayerAttributes** *(dict) --*

          Collection of key:value pairs containing player information for use in matchmaking.
          Player attribute keys must match the *playerAttributes* used in a matchmaking rule
          set. Example: ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S":
          "deathmatch"}}`` .

          - *(string) --*

            - *(dict) --*

              Values for use in  Player attribute key:value pairs. This object lets you specify
              an attribute value using any of the valid data types: string, number, string
              array, or data map. Each ``AttributeValue`` object can use only one of the
              available properties.

              - **S** *(string) --*

                For single string values. Maximum string length is 100 characters.

              - **N** *(float) --*

                For number values, expressed as double.

              - **SL** *(list) --*

                For a list of up to 10 strings. Maximum length for each string is 100
                characters. Duplicate values are not recognized; all occurrences of the
                repeated value after the first of a repeated value are ignored.

                - *(string) --*

              - **SDM** *(dict) --*

                For a map of up to 10 data type:value pairs. Maximum length for each string
                value is 100 characters.

                - *(string) --*

                  - *(float) --*

        - **Team** *(string) --*

          Name of the team that the player is assigned to in a match. Team names are defined in
          a matchmaking rule set.

        - **LatencyInMs** *(dict) --*

          Set of values, expressed in milliseconds, indicating the amount of latency that a
          player experiences when connected to AWS regions. If this property is present,
          FlexMatch considers placing the match only in regions for which latency is reported.

          If a matchmaker has a rule that evaluates player latency, players must report latency
          in order to be matched. If no latency is reported in this scenario, FlexMatch assumes
          that no regions are available to the player and the ticket is not matchable.

          - *(string) --*

            - *(integer) --*

    - **GameSessionConnectionInfo** *(dict) --*

      Identifier and connection information of the game session created for the match. This
      information is added to the ticket only after the matchmaking request has been
      successfully completed.

      - **GameSessionArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
        assigned to a game session and uniquely identifies it.

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app
        needs both the IP address and port number.

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift game server, an app
        needs both the IP address and port number.

      - **MatchedPlayerSessions** *(list) --*

        Collection of player session IDs, one for each player ID that was included in the
        original matchmaking request.

        - *(dict) --*

          Represents a new player session that is created as a result of a successful FlexMatch
          match. A successful match automatically creates new player sessions for every player
          ID in the original matchmaking request.

          When players connect to the match's game session, they must include both player ID
          and player session ID in order to claim their assigned player slot.

          - **PlayerId** *(string) --*

            Unique identifier for a player

          - **PlayerSessionId** *(string) --*

            Unique identifier for a player session

    - **EstimatedWaitTime** *(integer) --*

      Average amount of time (in seconds) that players are currently waiting for a match. If
      there is not enough recent data, this property may be empty.
    """


_ClientDescribeMatchmakingResponseTypeDef = TypedDict(
    "_ClientDescribeMatchmakingResponseTypeDef",
    {"TicketList": List[ClientDescribeMatchmakingResponseTicketListTypeDef]},
    total=False,
)


class ClientDescribeMatchmakingResponseTypeDef(
    _ClientDescribeMatchmakingResponseTypeDef
):
    """
    Type definition for `ClientDescribeMatchmaking` `Response`

    Represents the returned data in response to a request action.

    - **TicketList** *(list) --*

      Collection of existing matchmaking ticket objects matching the request.

      - *(dict) --*

        Ticket generated to track the progress of a matchmaking request. Each ticket is uniquely
        identified by a ticket ID, supplied by the requester, when creating a matchmaking request
        with  StartMatchmaking . Tickets can be retrieved by calling  DescribeMatchmaking with the
        ticket ID.

        - **TicketId** *(string) --*

          Unique identifier for a matchmaking ticket.

        - **ConfigurationName** *(string) --*

          Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking
          configurations determine how players are grouped into a match and how a new game session
          is created for the match.

        - **Status** *(string) --*

          Current status of the matchmaking request.

          * **QUEUED** -- The matchmaking request has been received and is currently waiting to be
          processed.

          * **SEARCHING** -- The matchmaking request is currently being processed.

          * **REQUIRES_ACCEPTANCE** -- A match has been proposed and the players must accept the
          match (see  AcceptMatch ). This status is used only with requests that use a matchmaking
          configuration with a player acceptance requirement.

          * **PLACING** -- The FlexMatch engine has matched players and is in the process of
          placing a new game session for the match.

          * **COMPLETED** -- Players have been matched and a game session is ready to host the
          players. A ticket in this state contains the necessary connection information for players.

          * **FAILED** -- The matchmaking request was not completed.

          * **CANCELLED** -- The matchmaking request was canceled. This may be the result of a call
          to  StopMatchmaking or a proposed match that one or more players failed to accept.

          * **TIMED_OUT** -- The matchmaking request was not successful within the duration
          specified in the matchmaking configuration.

          .. note::

            Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED,
            TIMED_OUT) can be resubmitted as new requests with new ticket IDs.

        - **StatusReason** *(string) --*

          Code to explain the current status. For example, a status reason may indicate when a
          ticket has returned to ``SEARCHING`` status after a proposed match fails to receive
          player acceptances.

        - **StatusMessage** *(string) --*

          Additional information about the current status.

        - **StartTime** *(datetime) --*

          Time stamp indicating when this matchmaking request was received. Format is a number
          expressed in Unix time as milliseconds (for example "1469498468.057").

        - **EndTime** *(datetime) --*

          Time stamp indicating when this matchmaking request stopped being processed due to
          success, failure, or cancellation. Format is a number expressed in Unix time as
          milliseconds (for example "1469498468.057").

        - **Players** *(list) --*

          A set of ``Player`` objects, each representing a player to find matches for. Players are
          identified by a unique player ID and may include latency data for use during matchmaking.
          If the ticket is in status ``COMPLETED`` , the ``Player`` objects include the team the
          players were assigned to in the resulting match.

          - *(dict) --*

            Represents a player in matchmaking. When starting a matchmaking request, a player has a
            player ID, attributes, and may have latency data. Team information is added after a
            match has been successfully completed.

            - **PlayerId** *(string) --*

              Unique identifier for a player

            - **PlayerAttributes** *(dict) --*

              Collection of key:value pairs containing player information for use in matchmaking.
              Player attribute keys must match the *playerAttributes* used in a matchmaking rule
              set. Example: ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S":
              "deathmatch"}}`` .

              - *(string) --*

                - *(dict) --*

                  Values for use in  Player attribute key:value pairs. This object lets you specify
                  an attribute value using any of the valid data types: string, number, string
                  array, or data map. Each ``AttributeValue`` object can use only one of the
                  available properties.

                  - **S** *(string) --*

                    For single string values. Maximum string length is 100 characters.

                  - **N** *(float) --*

                    For number values, expressed as double.

                  - **SL** *(list) --*

                    For a list of up to 10 strings. Maximum length for each string is 100
                    characters. Duplicate values are not recognized; all occurrences of the
                    repeated value after the first of a repeated value are ignored.

                    - *(string) --*

                  - **SDM** *(dict) --*

                    For a map of up to 10 data type:value pairs. Maximum length for each string
                    value is 100 characters.

                    - *(string) --*

                      - *(float) --*

            - **Team** *(string) --*

              Name of the team that the player is assigned to in a match. Team names are defined in
              a matchmaking rule set.

            - **LatencyInMs** *(dict) --*

              Set of values, expressed in milliseconds, indicating the amount of latency that a
              player experiences when connected to AWS regions. If this property is present,
              FlexMatch considers placing the match only in regions for which latency is reported.

              If a matchmaker has a rule that evaluates player latency, players must report latency
              in order to be matched. If no latency is reported in this scenario, FlexMatch assumes
              that no regions are available to the player and the ticket is not matchable.

              - *(string) --*

                - *(integer) --*

        - **GameSessionConnectionInfo** *(dict) --*

          Identifier and connection information of the game session created for the match. This
          information is added to the ticket only after the matchmaking request has been
          successfully completed.

          - **GameSessionArn** *(string) --*

            Amazon Resource Name (`ARN
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
            assigned to a game session and uniquely identifies it.

          - **IpAddress** *(string) --*

            IP address of the game session. To connect to a Amazon GameLift game server, an app
            needs both the IP address and port number.

          - **DnsName** *(string) --*

          - **Port** *(integer) --*

            Port number for the game session. To connect to a Amazon GameLift game server, an app
            needs both the IP address and port number.

          - **MatchedPlayerSessions** *(list) --*

            Collection of player session IDs, one for each player ID that was included in the
            original matchmaking request.

            - *(dict) --*

              Represents a new player session that is created as a result of a successful FlexMatch
              match. A successful match automatically creates new player sessions for every player
              ID in the original matchmaking request.

              When players connect to the match's game session, they must include both player ID
              and player session ID in order to claim their assigned player slot.

              - **PlayerId** *(string) --*

                Unique identifier for a player

              - **PlayerSessionId** *(string) --*

                Unique identifier for a player session

        - **EstimatedWaitTime** *(integer) --*

          Average amount of time (in seconds) that players are currently waiting for a match. If
          there is not enough recent data, this property may be empty.
    """


_ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef = TypedDict(
    "_ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef",
    {"RuleSetName": str, "RuleSetBody": str, "CreationTime": datetime},
    total=False,
)


class ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef(
    _ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef
):
    """
    Type definition for `ClientDescribeMatchmakingRuleSetsResponse` `RuleSets`

    Set of rule statements, used with FlexMatch, that determine how to build your player
    matches. Each rule set describes a type of group to be created and defines the parameters
    for acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.

    A rule set may define the following elements for a match. For detailed information and
    examples showing how to construct a rule set, see `Build a FlexMatch Rule Set
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-rulesets.html>`__ .

    * Teams -- Required. A rule set must define one or multiple teams for the match and set
    minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that
    requires all eight slots to be filled.

    * Player attributes -- Optional. These attributes specify a set of player characteristics
    to evaluate when looking for a match. Matchmaking requests that use a rule set with player
    attributes must provide the corresponding attribute values. For example, an attribute might
    specify a player's skill or level.

    * Rules -- Optional. Rules define how to evaluate potential players for a match based on
    player attributes. A rule might specify minimum requirements for individual players, teams,
    or entire matches. For example, a rule might require each player to meet a certain skill
    level, each team to have at least one player in a certain role, or the match to have a
    minimum average skill level. or may describe an entire group--such as all teams must be
    evenly matched or have at least one player in a certain role.

    * Expansions -- Optional. Expansions allow you to relax the rules after a period of time
    when no acceptable matches are found. This feature lets you balance getting players into
    games in a reasonable amount of time instead of making them wait indefinitely for the best
    possible match. For example, you might use an expansion to increase the maximum skill
    variance between players after 30 seconds.

    - **RuleSetName** *(string) --*

      Unique identifier for a matchmaking rule set

    - **RuleSetBody** *(string) --*

      Collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in
      JSON, but most elements support a description field.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").
    """


_ClientDescribeMatchmakingRuleSetsResponseTypeDef = TypedDict(
    "_ClientDescribeMatchmakingRuleSetsResponseTypeDef",
    {
        "RuleSets": List[ClientDescribeMatchmakingRuleSetsResponseRuleSetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeMatchmakingRuleSetsResponseTypeDef(
    _ClientDescribeMatchmakingRuleSetsResponseTypeDef
):
    """
    Type definition for `ClientDescribeMatchmakingRuleSets` `Response`

    Represents the returned data in response to a request action.

    - **RuleSets** *(list) --*

      Collection of requested matchmaking rule set objects.

      - *(dict) --*

        Set of rule statements, used with FlexMatch, that determine how to build your player
        matches. Each rule set describes a type of group to be created and defines the parameters
        for acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.

        A rule set may define the following elements for a match. For detailed information and
        examples showing how to construct a rule set, see `Build a FlexMatch Rule Set
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-rulesets.html>`__ .

        * Teams -- Required. A rule set must define one or multiple teams for the match and set
        minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that
        requires all eight slots to be filled.

        * Player attributes -- Optional. These attributes specify a set of player characteristics
        to evaluate when looking for a match. Matchmaking requests that use a rule set with player
        attributes must provide the corresponding attribute values. For example, an attribute might
        specify a player's skill or level.

        * Rules -- Optional. Rules define how to evaluate potential players for a match based on
        player attributes. A rule might specify minimum requirements for individual players, teams,
        or entire matches. For example, a rule might require each player to meet a certain skill
        level, each team to have at least one player in a certain role, or the match to have a
        minimum average skill level. or may describe an entire group--such as all teams must be
        evenly matched or have at least one player in a certain role.

        * Expansions -- Optional. Expansions allow you to relax the rules after a period of time
        when no acceptable matches are found. This feature lets you balance getting players into
        games in a reasonable amount of time instead of making them wait indefinitely for the best
        possible match. For example, you might use an expansion to increase the maximum skill
        variance between players after 30 seconds.

        - **RuleSetName** *(string) --*

          Unique identifier for a matchmaking rule set

        - **RuleSetBody** *(string) --*

          Collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in
          JSON, but most elements support a description field.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef = TypedDict(
    "_ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)


class ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef(
    _ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef
):
    """
    Type definition for `ClientDescribePlayerSessionsResponse` `PlayerSessions`

    Properties describing a player session. Player session objects are created either by
    creating a player session for a specific game session, or as part of a game session
    placement. A player session represents either a player reservation for a game session
    (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A
    player session object (including player data) is automatically passed to a game session
    when the player connects to the game session and is validated.

    When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
    session ends, the player session object is retained for 30 days and then removed.

    *  CreatePlayerSession

    *  CreatePlayerSessions

    *  DescribePlayerSessions

    * Game session placements

      *  StartGameSessionPlacement

      *  DescribeGameSessionPlacement

      *  StopGameSessionPlacement

    - **PlayerSessionId** *(string) --*

      Unique identifier for a player session.

    - **PlayerId** *(string) --*

      Unique identifier for a player that is associated with this player session.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session that the player session is connected to.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the player's game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **Status** *(string) --*

      Current status of the player session.

      Possible player session statuses include the following:

      * **RESERVED** -- The player session request has been received, but the player has not
      yet connected to the server process and/or been validated.

      * **ACTIVE** -- The player has been validated by the server process and is currently
      connected.

      * **COMPLETED** -- The player connection has been dropped.

      * **TIMEDOUT** -- A player session request was received, but the player did not connect
      and/or was not validated within the timeout limit (60 seconds).

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift server process, an app
      needs both the IP address and port number.

    - **PlayerData** *(string) --*

      Developer-defined information related to a player. Amazon GameLift does not use this
      data, so it can be formatted as needed for use in the game.
    """


_ClientDescribePlayerSessionsResponseTypeDef = TypedDict(
    "_ClientDescribePlayerSessionsResponseTypeDef",
    {
        "PlayerSessions": List[
            ClientDescribePlayerSessionsResponsePlayerSessionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribePlayerSessionsResponseTypeDef(
    _ClientDescribePlayerSessionsResponseTypeDef
):
    """
    Type definition for `ClientDescribePlayerSessions` `Response`

    Represents the returned data in response to a request action.

    - **PlayerSessions** *(list) --*

      Collection of objects containing properties for each player session that matches the request.

      - *(dict) --*

        Properties describing a player session. Player session objects are created either by
        creating a player session for a specific game session, or as part of a game session
        placement. A player session represents either a player reservation for a game session
        (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A
        player session object (including player data) is automatically passed to a game session
        when the player connects to the game session and is validated.

        When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
        session ends, the player session object is retained for 30 days and then removed.

        *  CreatePlayerSession

        *  CreatePlayerSessions

        *  DescribePlayerSessions

        * Game session placements

          *  StartGameSessionPlacement

          *  DescribeGameSessionPlacement

          *  StopGameSessionPlacement

        - **PlayerSessionId** *(string) --*

          Unique identifier for a player session.

        - **PlayerId** *(string) --*

          Unique identifier for a player that is associated with this player session.

        - **GameSessionId** *(string) --*

          Unique identifier for the game session that the player session is connected to.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the player's game session is running on.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **TerminationTime** *(datetime) --*

          Time stamp indicating when this data object was terminated. Format is a number expressed
          in Unix time as milliseconds (for example "1469498468.057").

        - **Status** *(string) --*

          Current status of the player session.

          Possible player session statuses include the following:

          * **RESERVED** -- The player session request has been received, but the player has not
          yet connected to the server process and/or been validated.

          * **ACTIVE** -- The player has been validated by the server process and is currently
          connected.

          * **COMPLETED** -- The player connection has been dropped.

          * **TIMEDOUT** -- A player session request was received, but the player did not connect
          and/or was not validated within the timeout limit (60 seconds).

        - **IpAddress** *(string) --*

          IP address of the game session. To connect to a Amazon GameLift game server, an app needs
          both the IP address and port number.

        - **DnsName** *(string) --*

        - **Port** *(integer) --*

          Port number for the game session. To connect to a Amazon GameLift server process, an app
          needs both the IP address and port number.

        - **PlayerData** *(string) --*

          Developer-defined information related to a player. Amazon GameLift does not use this
          data, so it can be formatted as needed for use in the game.

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef",
    {"LaunchPath": str, "Parameters": str, "ConcurrentExecutions": int},
    total=False,
)


class ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef(
    _ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef
):
    """
    Type definition for `ClientDescribeRuntimeConfigurationResponseRuntimeConfiguration` `ServerProcesses`

    A set of instructions for launching server processes on each instance in a fleet. Server
    processes run either a custom game build executable or a Realtime Servers script. Each
    instruction set identifies the location of the custom game build executable or Realtime
    launch script, optional launch parameters, and the number of server processes with this
    configuration to maintain concurrently on the instance. Server process configurations
    make up a fleet's ``  RuntimeConfiguration `` .

    - **LaunchPath** *(string) --*

      Location of the server executable in a custom game build or the name of the Realtime
      script file that contains the ``Init()`` function. Game builds and Realtime scripts are
      installed on instances at the root:

      * Windows (for custom game builds only): ``C:\\game`` . Example:
      "``C:\\game\\MyGame\\server.exe`` "

      * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
      "``/local/game/MyRealtimeScript.js`` "

    - **Parameters** *(string) --*

      Optional list of parameters to pass to the server executable or Realtime script on
      launch.

    - **ConcurrentExecutions** *(integer) --*

      Number of server processes using this configuration to run concurrently on an instance.
    """


_ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef = TypedDict(
    "_ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[
            ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef
        ],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)


class ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef(
    _ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeRuntimeConfigurationResponse` `RuntimeConfiguration`

    Instructions describing how server processes should be launched and maintained on each
    instance in the fleet.

    - **ServerProcesses** *(list) --*

      Collection of server process configurations that describe which server processes to run on
      each instance in a fleet.

      - *(dict) --*

        A set of instructions for launching server processes on each instance in a fleet. Server
        processes run either a custom game build executable or a Realtime Servers script. Each
        instruction set identifies the location of the custom game build executable or Realtime
        launch script, optional launch parameters, and the number of server processes with this
        configuration to maintain concurrently on the instance. Server process configurations
        make up a fleet's ``  RuntimeConfiguration `` .

        - **LaunchPath** *(string) --*

          Location of the server executable in a custom game build or the name of the Realtime
          script file that contains the ``Init()`` function. Game builds and Realtime scripts are
          installed on instances at the root:

          * Windows (for custom game builds only): ``C:\\game`` . Example:
          "``C:\\game\\MyGame\\server.exe`` "

          * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
          "``/local/game/MyRealtimeScript.js`` "

        - **Parameters** *(string) --*

          Optional list of parameters to pass to the server executable or Realtime script on
          launch.

        - **ConcurrentExecutions** *(integer) --*

          Number of server processes using this configuration to run concurrently on an instance.

    - **MaxConcurrentGameSessionActivations** *(integer) --*

      Maximum number of game sessions with status ``ACTIVATING`` to allow on an instance
      simultaneously. This setting limits the amount of instance resources that can be used for
      new game activations at any one time.

    - **GameSessionActivationTimeoutSeconds** *(integer) --*

      Maximum amount of time (in seconds) that a game session can remain in status ``ACTIVATING``
      . If the game session is not active before the timeout, activation is terminated and the
      game session status is changed to ``TERMINATED`` .
    """


_ClientDescribeRuntimeConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeRuntimeConfigurationResponseTypeDef",
    {
        "RuntimeConfiguration": ClientDescribeRuntimeConfigurationResponseRuntimeConfigurationTypeDef
    },
    total=False,
)


class ClientDescribeRuntimeConfigurationResponseTypeDef(
    _ClientDescribeRuntimeConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeRuntimeConfiguration` `Response`

    Represents the returned data in response to a request action.

    - **RuntimeConfiguration** *(dict) --*

      Instructions describing how server processes should be launched and maintained on each
      instance in the fleet.

      - **ServerProcesses** *(list) --*

        Collection of server process configurations that describe which server processes to run on
        each instance in a fleet.

        - *(dict) --*

          A set of instructions for launching server processes on each instance in a fleet. Server
          processes run either a custom game build executable or a Realtime Servers script. Each
          instruction set identifies the location of the custom game build executable or Realtime
          launch script, optional launch parameters, and the number of server processes with this
          configuration to maintain concurrently on the instance. Server process configurations
          make up a fleet's ``  RuntimeConfiguration `` .

          - **LaunchPath** *(string) --*

            Location of the server executable in a custom game build or the name of the Realtime
            script file that contains the ``Init()`` function. Game builds and Realtime scripts are
            installed on instances at the root:

            * Windows (for custom game builds only): ``C:\\game`` . Example:
            "``C:\\game\\MyGame\\server.exe`` "

            * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
            "``/local/game/MyRealtimeScript.js`` "

          - **Parameters** *(string) --*

            Optional list of parameters to pass to the server executable or Realtime script on
            launch.

          - **ConcurrentExecutions** *(integer) --*

            Number of server processes using this configuration to run concurrently on an instance.

      - **MaxConcurrentGameSessionActivations** *(integer) --*

        Maximum number of game sessions with status ``ACTIVATING`` to allow on an instance
        simultaneously. This setting limits the amount of instance resources that can be used for
        new game activations at any one time.

      - **GameSessionActivationTimeoutSeconds** *(integer) --*

        Maximum amount of time (in seconds) that a game session can remain in status ``ACTIVATING``
        . If the game session is not active before the timeout, activation is terminated and the
        game session status is changed to ``TERMINATED`` .
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef",
    {"TargetValue": float},
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPoliciesResponseScalingPolicies` `TargetConfiguration`

    Object that contains settings for a target-based scaling policy.

    - **TargetValue** *(float) --*

      Desired value to use with a target-based scaling policy. The value must be relevant for
      whatever metric the scaling policy is using. For example, in a policy using the metric
      PercentAvailableGameSessions, the target value should be the preferred size of the
      fleet's buffer (the percent of capacity that should be idle and ready for new game
      sessions).
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
    {
        "FleetId": str,
        "Name": str,
        "Status": str,
        "ScalingAdjustment": int,
        "ScalingAdjustmentType": str,
        "ComparisonOperator": str,
        "Threshold": float,
        "EvaluationPeriods": int,
        "MetricName": str,
        "PolicyType": str,
        "TargetConfiguration": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeScalingPoliciesResponse` `ScalingPolicies`

    Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the
    combination of name and fleet ID.

    *  DescribeFleetCapacity

    *  UpdateFleetCapacity

    *  DescribeEC2InstanceLimits

    * Manage scaling policies:

      *  PutScalingPolicy (auto-scaling)

      *  DescribeScalingPolicies (auto-scaling)

      *  DeleteScalingPolicy (auto-scaling)

    * Manage fleet actions:

      *  StartFleetActions

      *  StopFleetActions

    - **FleetId** *(string) --*

      Unique identifier for a fleet that is associated with this scaling policy.

    - **Name** *(string) --*

      Descriptive label that is associated with a scaling policy. Policy names do not need to
      be unique.

    - **Status** *(string) --*

      Current status of the scaling policy. The scaling policy can be in force only when in an
      ``ACTIVE`` status. Scaling policies can be suspended for individual fleets (see
      StopFleetActions ; if suspended for a fleet, the policy status does not change. View a
      fleet's stopped actions by calling  DescribeFleetCapacity .

      * **ACTIVE** -- The scaling policy can be used for auto-scaling a fleet.

      * **UPDATE_REQUESTED** -- A request to update the scaling policy has been received.

      * **UPDATING** -- A change is being made to the scaling policy.

      * **DELETE_REQUESTED** -- A request to delete the scaling policy has been received.

      * **DELETING** -- The scaling policy is being deleted.

      * **DELETED** -- The scaling policy has been deleted.

      * **ERROR** -- An error occurred in creating the policy. It should be removed and
      recreated.

    - **ScalingAdjustment** *(integer) --*

      Amount of adjustment to make, based on the scaling adjustment type.

    - **ScalingAdjustmentType** *(string) --*

      Type of adjustment to make to a fleet's instance count (see  FleetCapacity ):

      * **ChangeInCapacity** -- add (or subtract) the scaling adjustment value from the current
      instance count. Positive values scale up while negative values scale down.

      * **ExactCapacity** -- set the instance count to the scaling adjustment value.

      * **PercentChangeInCapacity** -- increase or reduce the current instance count by the
      scaling adjustment, read as a percentage. Positive values scale up while negative values
      scale down.

    - **ComparisonOperator** *(string) --*

      Comparison operator to use when measuring a metric against the threshold value.

    - **Threshold** *(float) --*

      Metric value used to trigger a scaling event.

    - **EvaluationPeriods** *(integer) --*

      Length of time (in minutes) the metric must be at or beyond the threshold before a
      scaling event is triggered.

    - **MetricName** *(string) --*

      Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment.
      For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift with Amazon
      CloudWatch
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`__
      .

      * **ActivatingGameSessions** -- Game sessions in the process of being created.

      * **ActiveGameSessions** -- Game sessions that are currently running.

      * **ActiveInstances** -- Fleet instances that are currently running at least one game
      session.

      * **AvailableGameSessions** -- Additional game sessions that fleet could host
      simultaneously, given current capacity.

      * **AvailablePlayerSessions** -- Empty player slots in currently active game sessions.
      This includes game sessions that are not currently accepting players. Reserved player
      slots are not included.

      * **CurrentPlayerSessions** -- Player slots in active game sessions that are being used
      by a player or are reserved for a player.

      * **IdleInstances** -- Active instances that are currently hosting zero game sessions.

      * **PercentAvailableGameSessions** -- Unused percentage of the total number of game
      sessions that a fleet could host simultaneously, given current capacity. Use this metric
      for a target-based scaling policy.

      * **PercentIdleInstances** -- Percentage of the total number of active instances that are
      hosting zero game sessions.

      * **QueueDepth** -- Pending game session placement requests, in any queue, where the
      current fleet is the top-priority destination.

      * **WaitTime** -- Current wait time for pending game session placement requests, in any
      queue, where the current fleet is the top-priority destination.

    - **PolicyType** *(string) --*

      Type of scaling policy to create. For a target-based policy, set the parameter
      *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For
      a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* ,
      *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .

    - **TargetConfiguration** *(dict) --*

      Object that contains settings for a target-based scaling policy.

      - **TargetValue** *(float) --*

        Desired value to use with a target-based scaling policy. The value must be relevant for
        whatever metric the scaling policy is using. For example, in a policy using the metric
        PercentAvailableGameSessions, the target value should be the preferred size of the
        fleet's buffer (the percent of capacity that should be idle and ready for new game
        sessions).
    """


_ClientDescribeScalingPoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[
            ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseTypeDef(
    _ClientDescribeScalingPoliciesResponseTypeDef
):
    """
    Type definition for `ClientDescribeScalingPolicies` `Response`

    Represents the returned data in response to a request action.

    - **ScalingPolicies** *(list) --*

      Collection of objects containing the scaling policies matching the request.

      - *(dict) --*

        Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the
        combination of name and fleet ID.

        *  DescribeFleetCapacity

        *  UpdateFleetCapacity

        *  DescribeEC2InstanceLimits

        * Manage scaling policies:

          *  PutScalingPolicy (auto-scaling)

          *  DescribeScalingPolicies (auto-scaling)

          *  DeleteScalingPolicy (auto-scaling)

        * Manage fleet actions:

          *  StartFleetActions

          *  StopFleetActions

        - **FleetId** *(string) --*

          Unique identifier for a fleet that is associated with this scaling policy.

        - **Name** *(string) --*

          Descriptive label that is associated with a scaling policy. Policy names do not need to
          be unique.

        - **Status** *(string) --*

          Current status of the scaling policy. The scaling policy can be in force only when in an
          ``ACTIVE`` status. Scaling policies can be suspended for individual fleets (see
          StopFleetActions ; if suspended for a fleet, the policy status does not change. View a
          fleet's stopped actions by calling  DescribeFleetCapacity .

          * **ACTIVE** -- The scaling policy can be used for auto-scaling a fleet.

          * **UPDATE_REQUESTED** -- A request to update the scaling policy has been received.

          * **UPDATING** -- A change is being made to the scaling policy.

          * **DELETE_REQUESTED** -- A request to delete the scaling policy has been received.

          * **DELETING** -- The scaling policy is being deleted.

          * **DELETED** -- The scaling policy has been deleted.

          * **ERROR** -- An error occurred in creating the policy. It should be removed and
          recreated.

        - **ScalingAdjustment** *(integer) --*

          Amount of adjustment to make, based on the scaling adjustment type.

        - **ScalingAdjustmentType** *(string) --*

          Type of adjustment to make to a fleet's instance count (see  FleetCapacity ):

          * **ChangeInCapacity** -- add (or subtract) the scaling adjustment value from the current
          instance count. Positive values scale up while negative values scale down.

          * **ExactCapacity** -- set the instance count to the scaling adjustment value.

          * **PercentChangeInCapacity** -- increase or reduce the current instance count by the
          scaling adjustment, read as a percentage. Positive values scale up while negative values
          scale down.

        - **ComparisonOperator** *(string) --*

          Comparison operator to use when measuring a metric against the threshold value.

        - **Threshold** *(float) --*

          Metric value used to trigger a scaling event.

        - **EvaluationPeriods** *(integer) --*

          Length of time (in minutes) the metric must be at or beyond the threshold before a
          scaling event is triggered.

        - **MetricName** *(string) --*

          Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment.
          For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift with Amazon
          CloudWatch
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`__
          .

          * **ActivatingGameSessions** -- Game sessions in the process of being created.

          * **ActiveGameSessions** -- Game sessions that are currently running.

          * **ActiveInstances** -- Fleet instances that are currently running at least one game
          session.

          * **AvailableGameSessions** -- Additional game sessions that fleet could host
          simultaneously, given current capacity.

          * **AvailablePlayerSessions** -- Empty player slots in currently active game sessions.
          This includes game sessions that are not currently accepting players. Reserved player
          slots are not included.

          * **CurrentPlayerSessions** -- Player slots in active game sessions that are being used
          by a player or are reserved for a player.

          * **IdleInstances** -- Active instances that are currently hosting zero game sessions.

          * **PercentAvailableGameSessions** -- Unused percentage of the total number of game
          sessions that a fleet could host simultaneously, given current capacity. Use this metric
          for a target-based scaling policy.

          * **PercentIdleInstances** -- Percentage of the total number of active instances that are
          hosting zero game sessions.

          * **QueueDepth** -- Pending game session placement requests, in any queue, where the
          current fleet is the top-priority destination.

          * **WaitTime** -- Current wait time for pending game session placement requests, in any
          queue, where the current fleet is the top-priority destination.

        - **PolicyType** *(string) --*

          Type of scaling policy to create. For a target-based policy, set the parameter
          *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For
          a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* ,
          *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .

        - **TargetConfiguration** *(dict) --*

          Object that contains settings for a target-based scaling policy.

          - **TargetValue** *(float) --*

            Desired value to use with a target-based scaling policy. The value must be relevant for
            whatever metric the scaling policy is using. For example, in a policy using the metric
            PercentAvailableGameSessions, the target value should be the preferred size of the
            fleet's buffer (the percent of capacity that should be idle and ready for new game
            sessions).

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientDescribeScriptResponseScriptStorageLocationTypeDef = TypedDict(
    "_ClientDescribeScriptResponseScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientDescribeScriptResponseScriptStorageLocationTypeDef(
    _ClientDescribeScriptResponseScriptStorageLocationTypeDef
):
    """
    Type definition for `ClientDescribeScriptResponseScript` `StorageLocation`

    Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
    stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
    CreateScript , and  UpdateScript requests.

    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.

    - **Key** *(string) --*

      Name of the zip file containing the build files or script files.

    - **RoleArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
      that allows Amazon GameLift to access the S3 bucket.

    - **ObjectVersion** *(string) --*

      Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
      uses this information when retrieving files from an S3 bucket that you own. Use this
      parameter to specify a specific version of the file; if not set, the latest version of
      the file is retrieved.
    """


_ClientDescribeScriptResponseScriptTypeDef = TypedDict(
    "_ClientDescribeScriptResponseScriptTypeDef",
    {
        "ScriptId": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": ClientDescribeScriptResponseScriptStorageLocationTypeDef,
    },
    total=False,
)


class ClientDescribeScriptResponseScriptTypeDef(
    _ClientDescribeScriptResponseScriptTypeDef
):
    """
    Type definition for `ClientDescribeScriptResponse` `Script`

    Set of properties describing the requested script.

    - **ScriptId** *(string) --*

      Unique identifier for a Realtime script

    - **Name** *(string) --*

      Descriptive label that is associated with a script. Script names do not need to be unique.

    - **Version** *(string) --*

      Version that is associated with a build or script. Version strings do not need to be unique.

    - **SizeOnDisk** *(integer) --*

      File size of the uploaded Realtime script, expressed in bytes. When files are uploaded from
      an S3 location, this value remains at "0".

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **StorageLocation** *(dict) --*

      Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
      stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
      CreateScript , and  UpdateScript requests.

      - **Bucket** *(string) --*

        Amazon S3 bucket identifier. This is the name of the S3 bucket.

      - **Key** *(string) --*

        Name of the zip file containing the build files or script files.

      - **RoleArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
        that allows Amazon GameLift to access the S3 bucket.

      - **ObjectVersion** *(string) --*

        Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
        uses this information when retrieving files from an S3 bucket that you own. Use this
        parameter to specify a specific version of the file; if not set, the latest version of
        the file is retrieved.
    """


_ClientDescribeScriptResponseTypeDef = TypedDict(
    "_ClientDescribeScriptResponseTypeDef",
    {"Script": ClientDescribeScriptResponseScriptTypeDef},
    total=False,
)


class ClientDescribeScriptResponseTypeDef(_ClientDescribeScriptResponseTypeDef):
    """
    Type definition for `ClientDescribeScript` `Response`

    - **Script** *(dict) --*

      Set of properties describing the requested script.

      - **ScriptId** *(string) --*

        Unique identifier for a Realtime script

      - **Name** *(string) --*

        Descriptive label that is associated with a script. Script names do not need to be unique.

      - **Version** *(string) --*

        Version that is associated with a build or script. Version strings do not need to be unique.

      - **SizeOnDisk** *(integer) --*

        File size of the uploaded Realtime script, expressed in bytes. When files are uploaded from
        an S3 location, this value remains at "0".

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **StorageLocation** *(dict) --*

        Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
        stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
        CreateScript , and  UpdateScript requests.

        - **Bucket** *(string) --*

          Amazon S3 bucket identifier. This is the name of the S3 bucket.

        - **Key** *(string) --*

          Name of the zip file containing the build files or script files.

        - **RoleArn** *(string) --*

          Amazon Resource Name (`ARN
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
          that allows Amazon GameLift to access the S3 bucket.

        - **ObjectVersion** *(string) --*

          Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
          uses this information when retrieving files from an S3 bucket that you own. Use this
          parameter to specify a specific version of the file; if not set, the latest version of
          the file is retrieved.
    """


_ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef = TypedDict(
    "_ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
    },
    total=False,
)


class ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef(
    _ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef
):
    """
    Type definition for `ClientDescribeVpcPeeringAuthorizationsResponse` `VpcPeeringAuthorizations`

    Represents an authorization for a VPC peering connection between the VPC for an Amazon
    GameLift fleet and another VPC on an account you have access to. This authorization must
    exist and be valid for the peering connection to be established. Authorizations are valid
    for 24 hours after they are issued.

    *  CreateVpcPeeringAuthorization

    *  DescribeVpcPeeringAuthorizations

    *  DeleteVpcPeeringAuthorization

    *  CreateVpcPeeringConnection

    *  DescribeVpcPeeringConnections

    *  DeleteVpcPeeringConnection

    - **GameLiftAwsAccountId** *(string) --*

      Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet.
      You can find your Account ID in the AWS Management Console under account settings.

    - **PeerVpcAwsAccountId** *(string) --*

    - **PeerVpcId** *(string) --*

      Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet.
      The VPC must be in the same region where your fleet is deployed. Look up a VPC ID using
      the `VPC Dashboard <https://console.aws.amazon.com/vpc/>`__ in the AWS Management
      Console. Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`__ .

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this authorization was issued. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **ExpirationTime** *(datetime) --*

      Time stamp indicating when this authorization expires (24 hours after issuance). Format
      is a number expressed in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientDescribeVpcPeeringAuthorizationsResponseTypeDef = TypedDict(
    "_ClientDescribeVpcPeeringAuthorizationsResponseTypeDef",
    {
        "VpcPeeringAuthorizations": List[
            ClientDescribeVpcPeeringAuthorizationsResponseVpcPeeringAuthorizationsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeVpcPeeringAuthorizationsResponseTypeDef(
    _ClientDescribeVpcPeeringAuthorizationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeVpcPeeringAuthorizations` `Response`

    - **VpcPeeringAuthorizations** *(list) --*

      Collection of objects that describe all valid VPC peering operations for the current AWS
      account.

      - *(dict) --*

        Represents an authorization for a VPC peering connection between the VPC for an Amazon
        GameLift fleet and another VPC on an account you have access to. This authorization must
        exist and be valid for the peering connection to be established. Authorizations are valid
        for 24 hours after they are issued.

        *  CreateVpcPeeringAuthorization

        *  DescribeVpcPeeringAuthorizations

        *  DeleteVpcPeeringAuthorization

        *  CreateVpcPeeringConnection

        *  DescribeVpcPeeringConnections

        *  DeleteVpcPeeringConnection

        - **GameLiftAwsAccountId** *(string) --*

          Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet.
          You can find your Account ID in the AWS Management Console under account settings.

        - **PeerVpcAwsAccountId** *(string) --*

        - **PeerVpcId** *(string) --*

          Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet.
          The VPC must be in the same region where your fleet is deployed. Look up a VPC ID using
          the `VPC Dashboard <https://console.aws.amazon.com/vpc/>`__ in the AWS Management
          Console. Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`__ .

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this authorization was issued. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **ExpirationTime** *(datetime) --*

          Time stamp indicating when this authorization expires (24 hours after issuance). Format
          is a number expressed in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef = TypedDict(
    "_ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef",
    {"Code": str, "Message": str},
    total=False,
)


class ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef(
    _ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef
):
    """
    Type definition for `ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnections` `Status`

    Object that contains status information about the connection. Status indicates if a
    connection is pending, successful, or failed.

    - **Code** *(string) --*

      Code indicating the status of a VPC peering connection.

    - **Message** *(string) --*

      Additional messaging associated with the connection status.
    """


_ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef = TypedDict(
    "_ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef",
    {
        "FleetId": str,
        "IpV4CidrBlock": str,
        "VpcPeeringConnectionId": str,
        "Status": ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsStatusTypeDef,
        "PeerVpcId": str,
        "GameLiftVpcId": str,
    },
    total=False,
)


class ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef(
    _ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef
):
    """
    Type definition for `ClientDescribeVpcPeeringConnectionsResponse` `VpcPeeringConnections`

    Represents a peering connection between a VPC on one of your AWS accounts and the VPC for
    your Amazon GameLift fleets. This record may be for an active peering connection or a
    pending connection that has not yet been established.

    *  CreateVpcPeeringAuthorization

    *  DescribeVpcPeeringAuthorizations

    *  DeleteVpcPeeringAuthorization

    *  CreateVpcPeeringConnection

    *  DescribeVpcPeeringConnections

    *  DeleteVpcPeeringConnection

    - **FleetId** *(string) --*

      Unique identifier for a fleet. This ID determines the ID of the Amazon GameLift VPC for
      your fleet.

    - **IpV4CidrBlock** *(string) --*

      CIDR block of IPv4 addresses assigned to the VPC peering connection for the GameLift VPC.
      The peered VPC also has an IPv4 CIDR block associated with it; these blocks cannot
      overlap or the peering connection cannot be created.

    - **VpcPeeringConnectionId** *(string) --*

      Unique identifier that is automatically assigned to the connection record. This ID is
      referenced in VPC peering connection events, and is used when deleting a connection with
      DeleteVpcPeeringConnection .

    - **Status** *(dict) --*

      Object that contains status information about the connection. Status indicates if a
      connection is pending, successful, or failed.

      - **Code** *(string) --*

        Code indicating the status of a VPC peering connection.

      - **Message** *(string) --*

        Additional messaging associated with the connection status.

    - **PeerVpcId** *(string) --*

      Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet.
      The VPC must be in the same region where your fleet is deployed. Look up a VPC ID using
      the `VPC Dashboard <https://console.aws.amazon.com/vpc/>`__ in the AWS Management
      Console. Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`__ .

    - **GameLiftVpcId** *(string) --*

      Unique identifier for the VPC that contains the Amazon GameLift fleet for this
      connection. This VPC is managed by Amazon GameLift and does not appear in your AWS
      account.
    """


_ClientDescribeVpcPeeringConnectionsResponseTypeDef = TypedDict(
    "_ClientDescribeVpcPeeringConnectionsResponseTypeDef",
    {
        "VpcPeeringConnections": List[
            ClientDescribeVpcPeeringConnectionsResponseVpcPeeringConnectionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeVpcPeeringConnectionsResponseTypeDef(
    _ClientDescribeVpcPeeringConnectionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeVpcPeeringConnections` `Response`

    Represents the returned data in response to a request action.

    - **VpcPeeringConnections** *(list) --*

      Collection of VPC peering connection records that match the request.

      - *(dict) --*

        Represents a peering connection between a VPC on one of your AWS accounts and the VPC for
        your Amazon GameLift fleets. This record may be for an active peering connection or a
        pending connection that has not yet been established.

        *  CreateVpcPeeringAuthorization

        *  DescribeVpcPeeringAuthorizations

        *  DeleteVpcPeeringAuthorization

        *  CreateVpcPeeringConnection

        *  DescribeVpcPeeringConnections

        *  DeleteVpcPeeringConnection

        - **FleetId** *(string) --*

          Unique identifier for a fleet. This ID determines the ID of the Amazon GameLift VPC for
          your fleet.

        - **IpV4CidrBlock** *(string) --*

          CIDR block of IPv4 addresses assigned to the VPC peering connection for the GameLift VPC.
          The peered VPC also has an IPv4 CIDR block associated with it; these blocks cannot
          overlap or the peering connection cannot be created.

        - **VpcPeeringConnectionId** *(string) --*

          Unique identifier that is automatically assigned to the connection record. This ID is
          referenced in VPC peering connection events, and is used when deleting a connection with
          DeleteVpcPeeringConnection .

        - **Status** *(dict) --*

          Object that contains status information about the connection. Status indicates if a
          connection is pending, successful, or failed.

          - **Code** *(string) --*

            Code indicating the status of a VPC peering connection.

          - **Message** *(string) --*

            Additional messaging associated with the connection status.

        - **PeerVpcId** *(string) --*

          Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet.
          The VPC must be in the same region where your fleet is deployed. Look up a VPC ID using
          the `VPC Dashboard <https://console.aws.amazon.com/vpc/>`__ in the AWS Management
          Console. Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`__ .

        - **GameLiftVpcId** *(string) --*

          Unique identifier for the VPC that contains the Amazon GameLift fleet for this
          connection. This VPC is managed by Amazon GameLift and does not appear in your AWS
          account.
    """


_ClientGetGameSessionLogUrlResponseTypeDef = TypedDict(
    "_ClientGetGameSessionLogUrlResponseTypeDef", {"PreSignedUrl": str}, total=False
)


class ClientGetGameSessionLogUrlResponseTypeDef(
    _ClientGetGameSessionLogUrlResponseTypeDef
):
    """
    Type definition for `ClientGetGameSessionLogUrl` `Response`

    Represents the returned data in response to a request action.

    - **PreSignedUrl** *(string) --*

      Location of the requested game session logs, available for download. This URL is valid for 15
      minutes, after which S3 will reject any download request using this URL. You can request a
      new URL any time within the 14-day period that the logs are retained.
    """


_ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef = TypedDict(
    "_ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef",
    {"UserName": str, "Secret": str},
    total=False,
)


class ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef(
    _ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef
):
    """
    Type definition for `ClientGetInstanceAccessResponseInstanceAccess` `Credentials`

    Credentials required to access the instance.

    - **UserName** *(string) --*

      User login string.

    - **Secret** *(string) --*

      Secret string. For Windows instances, the secret is a password for use with Windows
      Remote Desktop. For Linux instances, it is a private key (which must be saved as a
      ``.pem`` file) for use with SSH.
    """


_ClientGetInstanceAccessResponseInstanceAccessTypeDef = TypedDict(
    "_ClientGetInstanceAccessResponseInstanceAccessTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "OperatingSystem": str,
        "Credentials": ClientGetInstanceAccessResponseInstanceAccessCredentialsTypeDef,
    },
    total=False,
)


class ClientGetInstanceAccessResponseInstanceAccessTypeDef(
    _ClientGetInstanceAccessResponseInstanceAccessTypeDef
):
    """
    Type definition for `ClientGetInstanceAccessResponse` `InstanceAccess`

    Object that contains connection information for a fleet instance, including IP address and
    access credentials.

    - **FleetId** *(string) --*

      Unique identifier for a fleet containing the instance being accessed.

    - **InstanceId** *(string) --*

      Unique identifier for an instance being accessed.

    - **IpAddress** *(string) --*

      IP address assigned to the instance.

    - **OperatingSystem** *(string) --*

      Operating system that is running on the instance.

    - **Credentials** *(dict) --*

      Credentials required to access the instance.

      - **UserName** *(string) --*

        User login string.

      - **Secret** *(string) --*

        Secret string. For Windows instances, the secret is a password for use with Windows
        Remote Desktop. For Linux instances, it is a private key (which must be saved as a
        ``.pem`` file) for use with SSH.
    """


_ClientGetInstanceAccessResponseTypeDef = TypedDict(
    "_ClientGetInstanceAccessResponseTypeDef",
    {"InstanceAccess": ClientGetInstanceAccessResponseInstanceAccessTypeDef},
    total=False,
)


class ClientGetInstanceAccessResponseTypeDef(_ClientGetInstanceAccessResponseTypeDef):
    """
    Type definition for `ClientGetInstanceAccess` `Response`

    Represents the returned data in response to a request action.

    - **InstanceAccess** *(dict) --*

      Object that contains connection information for a fleet instance, including IP address and
      access credentials.

      - **FleetId** *(string) --*

        Unique identifier for a fleet containing the instance being accessed.

      - **InstanceId** *(string) --*

        Unique identifier for an instance being accessed.

      - **IpAddress** *(string) --*

        IP address assigned to the instance.

      - **OperatingSystem** *(string) --*

        Operating system that is running on the instance.

      - **Credentials** *(dict) --*

        Credentials required to access the instance.

        - **UserName** *(string) --*

          User login string.

        - **Secret** *(string) --*

          Secret string. For Windows instances, the secret is a password for use with Windows
          Remote Desktop. For Linux instances, it is a private key (which must be saved as a
          ``.pem`` file) for use with SSH.
    """


_ClientListAliasesResponseAliasesRoutingStrategyTypeDef = TypedDict(
    "_ClientListAliasesResponseAliasesRoutingStrategyTypeDef",
    {"Type": str, "FleetId": str, "Message": str},
    total=False,
)


class ClientListAliasesResponseAliasesRoutingStrategyTypeDef(
    _ClientListAliasesResponseAliasesRoutingStrategyTypeDef
):
    """
    Type definition for `ClientListAliasesResponseAliases` `RoutingStrategy`

    Alias configuration for the alias, including routing type and settings.

    - **Type** *(string) --*

      Type of routing strategy.

      Possible routing types include the following:

      * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
      active fleets.

      * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
      display a message to the user. A terminal alias throws a
      TerminalRoutingStrategyException with the  RoutingStrategy message embedded.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the alias points to.

    - **Message** *(string) --*

      Message text to be used with a terminal routing strategy.
    """


_ClientListAliasesResponseAliasesTypeDef = TypedDict(
    "_ClientListAliasesResponseAliasesTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": ClientListAliasesResponseAliasesRoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientListAliasesResponseAliasesTypeDef(_ClientListAliasesResponseAliasesTypeDef):
    """
    Type definition for `ClientListAliasesResponse` `Aliases`

    Properties describing a fleet alias.

    *  CreateAlias

    *  ListAliases

    *  DescribeAlias

    *  UpdateAlias

    *  DeleteAlias

    *  ResolveAlias

    - **AliasId** *(string) --*

      Unique identifier for an alias; alias IDs are unique within a region.

    - **Name** *(string) --*

      Descriptive label that is associated with an alias. Alias names do not need to be unique.

    - **AliasArn** *(string) --*

      Unique identifier for an alias; alias ARNs are unique across all regions.

    - **Description** *(string) --*

      Human-readable description of an alias.

    - **RoutingStrategy** *(dict) --*

      Alias configuration for the alias, including routing type and settings.

      - **Type** *(string) --*

        Type of routing strategy.

        Possible routing types include the following:

        * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
        active fleets.

        * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
        display a message to the user. A terminal alias throws a
        TerminalRoutingStrategyException with the  RoutingStrategy message embedded.

      - **FleetId** *(string) --*

        Unique identifier for a fleet that the alias points to.

      - **Message** *(string) --*

        Message text to be used with a terminal routing strategy.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **LastUpdatedTime** *(datetime) --*

      Time stamp indicating when this data object was last modified. Format is a number
      expressed in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientListAliasesResponseTypeDef = TypedDict(
    "_ClientListAliasesResponseTypeDef",
    {"Aliases": List[ClientListAliasesResponseAliasesTypeDef], "NextToken": str},
    total=False,
)


class ClientListAliasesResponseTypeDef(_ClientListAliasesResponseTypeDef):
    """
    Type definition for `ClientListAliases` `Response`

    Represents the returned data in response to a request action.

    - **Aliases** *(list) --*

      Collection of alias records that match the list request.

      - *(dict) --*

        Properties describing a fleet alias.

        *  CreateAlias

        *  ListAliases

        *  DescribeAlias

        *  UpdateAlias

        *  DeleteAlias

        *  ResolveAlias

        - **AliasId** *(string) --*

          Unique identifier for an alias; alias IDs are unique within a region.

        - **Name** *(string) --*

          Descriptive label that is associated with an alias. Alias names do not need to be unique.

        - **AliasArn** *(string) --*

          Unique identifier for an alias; alias ARNs are unique across all regions.

        - **Description** *(string) --*

          Human-readable description of an alias.

        - **RoutingStrategy** *(dict) --*

          Alias configuration for the alias, including routing type and settings.

          - **Type** *(string) --*

            Type of routing strategy.

            Possible routing types include the following:

            * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
            active fleets.

            * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
            display a message to the user. A terminal alias throws a
            TerminalRoutingStrategyException with the  RoutingStrategy message embedded.

          - **FleetId** *(string) --*

            Unique identifier for a fleet that the alias points to.

          - **Message** *(string) --*

            Message text to be used with a terminal routing strategy.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **LastUpdatedTime** *(datetime) --*

          Time stamp indicating when this data object was last modified. Format is a number
          expressed in Unix time as milliseconds (for example "1469498468.057").

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientListBuildsResponseBuildsTypeDef = TypedDict(
    "_ClientListBuildsResponseBuildsTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": str,
        "SizeOnDisk": int,
        "OperatingSystem": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientListBuildsResponseBuildsTypeDef(_ClientListBuildsResponseBuildsTypeDef):
    """
    Type definition for `ClientListBuildsResponse` `Builds`

    Properties describing a custom game build.

     **Related operations**

    *  CreateBuild

    *  ListBuilds

    *  DescribeBuild

    *  UpdateBuild

    *  DeleteBuild

    - **BuildId** *(string) --*

      Unique identifier for a build.

    - **Name** *(string) --*

      Descriptive label that is associated with a build. Build names do not need to be unique.
      It can be set using  CreateBuild or  UpdateBuild .

    - **Version** *(string) --*

      Version that is associated with a build or script. Version strings do not need to be
      unique. This value can be set using  CreateBuild or  UpdateBuild .

    - **Status** *(string) --*

      Current status of the build.

      Possible build statuses include the following:

      * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You
      cannot create fleets for builds that are in this status. When a build is successfully
      created, the build status is set to this value.

      * **READY** -- The game build has been successfully uploaded. You can now create new
      fleets for this build.

      * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.

    - **SizeOnDisk** *(integer) --*

      File size of the uploaded game build, expressed in bytes. When the build status is
      ``INITIALIZED`` , this value is 0.

    - **OperatingSystem** *(string) --*

      Operating system that the game server binaries are built to run on. This value determines
      the type of fleet resources that you can use for this build.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").
    """


_ClientListBuildsResponseTypeDef = TypedDict(
    "_ClientListBuildsResponseTypeDef",
    {"Builds": List[ClientListBuildsResponseBuildsTypeDef], "NextToken": str},
    total=False,
)


class ClientListBuildsResponseTypeDef(_ClientListBuildsResponseTypeDef):
    """
    Type definition for `ClientListBuilds` `Response`

    Represents the returned data in response to a request action.

    - **Builds** *(list) --*

      Collection of build records that match the request.

      - *(dict) --*

        Properties describing a custom game build.

         **Related operations**

        *  CreateBuild

        *  ListBuilds

        *  DescribeBuild

        *  UpdateBuild

        *  DeleteBuild

        - **BuildId** *(string) --*

          Unique identifier for a build.

        - **Name** *(string) --*

          Descriptive label that is associated with a build. Build names do not need to be unique.
          It can be set using  CreateBuild or  UpdateBuild .

        - **Version** *(string) --*

          Version that is associated with a build or script. Version strings do not need to be
          unique. This value can be set using  CreateBuild or  UpdateBuild .

        - **Status** *(string) --*

          Current status of the build.

          Possible build statuses include the following:

          * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You
          cannot create fleets for builds that are in this status. When a build is successfully
          created, the build status is set to this value.

          * **READY** -- The game build has been successfully uploaded. You can now create new
          fleets for this build.

          * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.

        - **SizeOnDisk** *(integer) --*

          File size of the uploaded game build, expressed in bytes. When the build status is
          ``INITIALIZED`` , this value is 0.

        - **OperatingSystem** *(string) --*

          Operating system that the game server binaries are built to run on. This value determines
          the type of fleet resources that you can use for this build.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientListFleetsResponseTypeDef = TypedDict(
    "_ClientListFleetsResponseTypeDef",
    {"FleetIds": List[str], "NextToken": str},
    total=False,
)


class ClientListFleetsResponseTypeDef(_ClientListFleetsResponseTypeDef):
    """
    Type definition for `ClientListFleets` `Response`

    Represents the returned data in response to a request action.

    - **FleetIds** *(list) --*

      Set of fleet IDs matching the list request. You can retrieve additional information about all
      returned fleets by passing this result set to a call to  DescribeFleetAttributes ,
      DescribeFleetCapacity , or  DescribeFleetUtilization .

      - *(string) --*

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientListScriptsResponseScriptsStorageLocationTypeDef = TypedDict(
    "_ClientListScriptsResponseScriptsStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientListScriptsResponseScriptsStorageLocationTypeDef(
    _ClientListScriptsResponseScriptsStorageLocationTypeDef
):
    """
    Type definition for `ClientListScriptsResponseScripts` `StorageLocation`

    Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
    stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
    CreateScript , and  UpdateScript requests.

    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.

    - **Key** *(string) --*

      Name of the zip file containing the build files or script files.

    - **RoleArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM
      role that allows Amazon GameLift to access the S3 bucket.

    - **ObjectVersion** *(string) --*

      Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
      uses this information when retrieving files from an S3 bucket that you own. Use this
      parameter to specify a specific version of the file; if not set, the latest version of
      the file is retrieved.
    """


_ClientListScriptsResponseScriptsTypeDef = TypedDict(
    "_ClientListScriptsResponseScriptsTypeDef",
    {
        "ScriptId": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": ClientListScriptsResponseScriptsStorageLocationTypeDef,
    },
    total=False,
)


class ClientListScriptsResponseScriptsTypeDef(_ClientListScriptsResponseScriptsTypeDef):
    """
    Type definition for `ClientListScriptsResponse` `Scripts`

    Properties describing a Realtime script.

     **Related operations**

    *  CreateScript

    *  ListScripts

    *  DescribeScript

    *  UpdateScript

    *  DeleteScript

    - **ScriptId** *(string) --*

      Unique identifier for a Realtime script

    - **Name** *(string) --*

      Descriptive label that is associated with a script. Script names do not need to be unique.

    - **Version** *(string) --*

      Version that is associated with a build or script. Version strings do not need to be
      unique.

    - **SizeOnDisk** *(integer) --*

      File size of the uploaded Realtime script, expressed in bytes. When files are uploaded
      from an S3 location, this value remains at "0".

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **StorageLocation** *(dict) --*

      Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
      stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
      CreateScript , and  UpdateScript requests.

      - **Bucket** *(string) --*

        Amazon S3 bucket identifier. This is the name of the S3 bucket.

      - **Key** *(string) --*

        Name of the zip file containing the build files or script files.

      - **RoleArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM
        role that allows Amazon GameLift to access the S3 bucket.

      - **ObjectVersion** *(string) --*

        Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
        uses this information when retrieving files from an S3 bucket that you own. Use this
        parameter to specify a specific version of the file; if not set, the latest version of
        the file is retrieved.
    """


_ClientListScriptsResponseTypeDef = TypedDict(
    "_ClientListScriptsResponseTypeDef",
    {"Scripts": List[ClientListScriptsResponseScriptsTypeDef], "NextToken": str},
    total=False,
)


class ClientListScriptsResponseTypeDef(_ClientListScriptsResponseTypeDef):
    """
    Type definition for `ClientListScripts` `Response`

    - **Scripts** *(list) --*

      Set of properties describing the requested script.

      - *(dict) --*

        Properties describing a Realtime script.

         **Related operations**

        *  CreateScript

        *  ListScripts

        *  DescribeScript

        *  UpdateScript

        *  DeleteScript

        - **ScriptId** *(string) --*

          Unique identifier for a Realtime script

        - **Name** *(string) --*

          Descriptive label that is associated with a script. Script names do not need to be unique.

        - **Version** *(string) --*

          Version that is associated with a build or script. Version strings do not need to be
          unique.

        - **SizeOnDisk** *(integer) --*

          File size of the uploaded Realtime script, expressed in bytes. When files are uploaded
          from an S3 location, this value remains at "0".

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **StorageLocation** *(dict) --*

          Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
          stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
          CreateScript , and  UpdateScript requests.

          - **Bucket** *(string) --*

            Amazon S3 bucket identifier. This is the name of the S3 bucket.

          - **Key** *(string) --*

            Name of the zip file containing the build files or script files.

          - **RoleArn** *(string) --*

            Amazon Resource Name (`ARN
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM
            role that allows Amazon GameLift to access the S3 bucket.

          - **ObjectVersion** *(string) --*

            Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
            uses this information when retrieving files from an S3 bucket that you own. Use this
            parameter to specify a specific version of the file; if not set, the latest version of
            the file is retrieved.

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientPutScalingPolicyResponseTypeDef = TypedDict(
    "_ClientPutScalingPolicyResponseTypeDef", {"Name": str}, total=False
)


class ClientPutScalingPolicyResponseTypeDef(_ClientPutScalingPolicyResponseTypeDef):
    """
    Type definition for `ClientPutScalingPolicy` `Response`

    Represents the returned data in response to a request action.

    - **Name** *(string) --*

      Descriptive label that is associated with a scaling policy. Policy names do not need to be
      unique.
    """


_ClientPutScalingPolicyTargetConfigurationTypeDef = TypedDict(
    "_ClientPutScalingPolicyTargetConfigurationTypeDef", {"TargetValue": float}
)


class ClientPutScalingPolicyTargetConfigurationTypeDef(
    _ClientPutScalingPolicyTargetConfigurationTypeDef
):
    """
    Type definition for `ClientPutScalingPolicy` `TargetConfiguration`

    Object that contains settings for a target-based scaling policy.

    - **TargetValue** *(float) --* **[REQUIRED]**

      Desired value to use with a target-based scaling policy. The value must be relevant for
      whatever metric the scaling policy is using. For example, in a policy using the metric
      PercentAvailableGameSessions, the target value should be the preferred size of the fleet's
      buffer (the percent of capacity that should be idle and ready for new game sessions).
    """


_ClientRequestUploadCredentialsResponseStorageLocationTypeDef = TypedDict(
    "_ClientRequestUploadCredentialsResponseStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientRequestUploadCredentialsResponseStorageLocationTypeDef(
    _ClientRequestUploadCredentialsResponseStorageLocationTypeDef
):
    """
    Type definition for `ClientRequestUploadCredentialsResponse` `StorageLocation`

    Amazon S3 path and key, identifying where the game build files are stored.

    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.

    - **Key** *(string) --*

      Name of the zip file containing the build files or script files.

    - **RoleArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
      that allows Amazon GameLift to access the S3 bucket.

    - **ObjectVersion** *(string) --*

      Version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses
      this information when retrieving files from an S3 bucket that you own. Use this parameter
      to specify a specific version of the file; if not set, the latest version of the file is
      retrieved.
    """


_ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef = TypedDict(
    "_ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str},
    total=False,
)


class ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef(
    _ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef
):
    """
    Type definition for `ClientRequestUploadCredentialsResponse` `UploadCredentials`

    AWS credentials required when uploading a game build to the storage location. These
    credentials have a limited lifespan and are valid only for the build they were issued for.

    - **AccessKeyId** *(string) --*

      Temporary key allowing access to the Amazon GameLift S3 account.

    - **SecretAccessKey** *(string) --*

      Temporary secret key allowing access to the Amazon GameLift S3 account.

    - **SessionToken** *(string) --*

      Token used to associate a specific build ID with the files uploaded using these credentials.
    """


_ClientRequestUploadCredentialsResponseTypeDef = TypedDict(
    "_ClientRequestUploadCredentialsResponseTypeDef",
    {
        "UploadCredentials": ClientRequestUploadCredentialsResponseUploadCredentialsTypeDef,
        "StorageLocation": ClientRequestUploadCredentialsResponseStorageLocationTypeDef,
    },
    total=False,
)


class ClientRequestUploadCredentialsResponseTypeDef(
    _ClientRequestUploadCredentialsResponseTypeDef
):
    """
    Type definition for `ClientRequestUploadCredentials` `Response`

    Represents the returned data in response to a request action.

    - **UploadCredentials** *(dict) --*

      AWS credentials required when uploading a game build to the storage location. These
      credentials have a limited lifespan and are valid only for the build they were issued for.

      - **AccessKeyId** *(string) --*

        Temporary key allowing access to the Amazon GameLift S3 account.

      - **SecretAccessKey** *(string) --*

        Temporary secret key allowing access to the Amazon GameLift S3 account.

      - **SessionToken** *(string) --*

        Token used to associate a specific build ID with the files uploaded using these credentials.

    - **StorageLocation** *(dict) --*

      Amazon S3 path and key, identifying where the game build files are stored.

      - **Bucket** *(string) --*

        Amazon S3 bucket identifier. This is the name of the S3 bucket.

      - **Key** *(string) --*

        Name of the zip file containing the build files or script files.

      - **RoleArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
        that allows Amazon GameLift to access the S3 bucket.

      - **ObjectVersion** *(string) --*

        Version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses
        this information when retrieving files from an S3 bucket that you own. Use this parameter
        to specify a specific version of the file; if not set, the latest version of the file is
        retrieved.
    """


_ClientResolveAliasResponseTypeDef = TypedDict(
    "_ClientResolveAliasResponseTypeDef", {"FleetId": str}, total=False
)


class ClientResolveAliasResponseTypeDef(_ClientResolveAliasResponseTypeDef):
    """
    Type definition for `ClientResolveAlias` `Response`

    Represents the returned data in response to a request action.

    - **FleetId** *(string) --*

      Fleet identifier that is associated with the requested alias.
    """


_ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "_ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef(
    _ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef
):
    """
    Type definition for `ClientSearchGameSessionsResponseGameSessions` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in
    a game session request, these properties communicate details to be used when setting up
    the new game session, such as to specify a game mode, level, or map. Game properties
    are passed to the game server process when initiating a new game session; the server
    process uses the properties as appropriate. For more information, see the `Amazon
    GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientSearchGameSessionsResponseGameSessionsTypeDef = TypedDict(
    "_ClientSearchGameSessionsResponseGameSessionsTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": str,
        "StatusReason": str,
        "GameProperties": List[
            ClientSearchGameSessionsResponseGameSessionsGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": str,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class ClientSearchGameSessionsResponseGameSessionsTypeDef(
    _ClientSearchGameSessionsResponseGameSessionsTypeDef
):
    """
    Type definition for `ClientSearchGameSessionsResponse` `GameSessions`

    Properties describing a game session.

    A game session in ACTIVE status can host players. When a game session ends, its status is
    set to ``TERMINATED`` .

    Once the session ends, the game session object is retained for 30 days. This means you can
    reuse idempotency token values after this time. Game session logs are retained for 14 days.

    *  CreateGameSession

    *  DescribeGameSessions

    *  DescribeGameSessionDetails

    *  SearchGameSessions

    *  UpdateGameSession

    *  GetGameSessionLogUrl

    * Game session placements

      *  StartGameSessionPlacement

      *  DescribeGameSessionPlacement

      *  StopGameSessionPlacement

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. A game session ARN has the following format:
      ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
      token>`` .

    - **Name** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to be
      unique.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **CurrentPlayerSessionCount** *(integer) --*

      Number of players currently in the game session.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **Status** *(string) --*

      Current status of the game session. A game session must have an ``ACTIVE`` status to have
      player sessions.

    - **StatusReason** *(string) --*

      Provides additional information about game session status. ``INTERRUPTED`` indicates that
      the game session was hosted on a spot instance that was reclaimed, causing the active
      game session to be terminated.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These
      properties are passed to a game server process in the  GameSession object with a request
      to start a new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). You can search for active game sessions based on this custom data with
      SearchGameSessions .

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in
        a game session request, these properties communicate details to be used when setting up
        the new game session, such as to specify a game mode, level, or map. Game properties
        are passed to the game server process when initiating a new game session; the server
        process uses the properties as appropriate. For more information, see the `Amazon
        GameLift Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **PlayerSessionCreationPolicy** *(string) --*

      Indicates whether or not the game session is accepting new players.

    - **CreatorId** *(string) --*

      Unique identifier for a player. This ID is used to enforce a resource protection policy
      (if one exists), that limits the number of game sessions a player can create.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information about the matchmaking process that was used to create the game session. It is
      in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
      contains data on all players assigned to the match, including player attributes and team
      assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      . Matchmaker data is useful when requesting match backfills, and is updated whenever new
      players are added during a successful backfill (see  StartMatchBackfill ).
    """


_ClientSearchGameSessionsResponseTypeDef = TypedDict(
    "_ClientSearchGameSessionsResponseTypeDef",
    {
        "GameSessions": List[ClientSearchGameSessionsResponseGameSessionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientSearchGameSessionsResponseTypeDef(_ClientSearchGameSessionsResponseTypeDef):
    """
    Type definition for `ClientSearchGameSessions` `Response`

    Represents the returned data in response to a request action.

    - **GameSessions** *(list) --*

      Collection of objects containing game session properties for each session matching the
      request.

      - *(dict) --*

        Properties describing a game session.

        A game session in ACTIVE status can host players. When a game session ends, its status is
        set to ``TERMINATED`` .

        Once the session ends, the game session object is retained for 30 days. This means you can
        reuse idempotency token values after this time. Game session logs are retained for 14 days.

        *  CreateGameSession

        *  DescribeGameSessions

        *  DescribeGameSessionDetails

        *  SearchGameSessions

        *  UpdateGameSession

        *  GetGameSessionLogUrl

        * Game session placements

          *  StartGameSessionPlacement

          *  DescribeGameSessionPlacement

          *  StopGameSessionPlacement

        - **GameSessionId** *(string) --*

          Unique identifier for the game session. A game session ARN has the following format:
          ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
          token>`` .

        - **Name** *(string) --*

          Descriptive label that is associated with a game session. Session names do not need to be
          unique.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the game session is running on.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **TerminationTime** *(datetime) --*

          Time stamp indicating when this data object was terminated. Format is a number expressed
          in Unix time as milliseconds (for example "1469498468.057").

        - **CurrentPlayerSessionCount** *(integer) --*

          Number of players currently in the game session.

        - **MaximumPlayerSessionCount** *(integer) --*

          Maximum number of players that can be connected simultaneously to the game session.

        - **Status** *(string) --*

          Current status of the game session. A game session must have an ``ACTIVE`` status to have
          player sessions.

        - **StatusReason** *(string) --*

          Provides additional information about game session status. ``INTERRUPTED`` indicates that
          the game session was hosted on a spot instance that was reclaimed, causing the active
          game session to be terminated.

        - **GameProperties** *(list) --*

          Set of custom properties for a game session, formatted as key:value pairs. These
          properties are passed to a game server process in the  GameSession object with a request
          to start a new game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ). You can search for active game sessions based on this custom data with
          SearchGameSessions .

          - *(dict) --*

            Set of key-value pairs that contain information about a game session. When included in
            a game session request, these properties communicate details to be used when setting up
            the new game session, such as to specify a game mode, level, or map. Game properties
            are passed to the game server process when initiating a new game session; the server
            process uses the properties as appropriate. For more information, see the `Amazon
            GameLift Developer Guide
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
            .

            - **Key** *(string) --*

              Game property identifier.

            - **Value** *(string) --*

              Game property value.

        - **IpAddress** *(string) --*

          IP address of the game session. To connect to a Amazon GameLift game server, an app needs
          both the IP address and port number.

        - **DnsName** *(string) --*

        - **Port** *(integer) --*

          Port number for the game session. To connect to a Amazon GameLift game server, an app
          needs both the IP address and port number.

        - **PlayerSessionCreationPolicy** *(string) --*

          Indicates whether or not the game session is accepting new players.

        - **CreatorId** *(string) --*

          Unique identifier for a player. This ID is used to enforce a resource protection policy
          (if one exists), that limits the number of game sessions a player can create.

        - **GameSessionData** *(string) --*

          Set of custom game session properties, formatted as a single string value. This data is
          passed to a game server process in the  GameSession object with a request to start a new
          game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ).

        - **MatchmakerData** *(string) --*

          Information about the matchmaking process that was used to create the game session. It is
          in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
          contains data on all players assigned to the match, including player attributes and team
          assignments. For more details on matchmaker data, see `Match Data
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
          . Matchmaker data is useful when requesting match backfills, and is updated whenever new
          players are added during a successful backfill (see  StartMatchBackfill ).

    - **NextToken** *(string) --*

      Token that indicates where to resume retrieving results on the next call to this action. If
      no token is returned, these results represent the end of the list.
    """


_ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerData": str},
    total=False,
)


class ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef(
    _ClientStartGameSessionPlacementDesiredPlayerSessionsTypeDef
):
    """
    Type definition for `ClientStartGameSessionPlacement` `DesiredPlayerSessions`

    Player information for use when creating player sessions using a game session placement request
    with  StartGameSessionPlacement .

    - **PlayerId** *(string) --*

      Unique identifier for a player to associate with the player session.

    - **PlayerData** *(string) --*

      Developer-defined information related to a player. Amazon GameLift does not use this data, so
      it can be formatted as needed for use in the game.
    """


_ClientStartGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementGamePropertiesTypeDef", {"Key": str, "Value": str}
)


class ClientStartGameSessionPlacementGamePropertiesTypeDef(
    _ClientStartGameSessionPlacementGamePropertiesTypeDef
):
    """
    Type definition for `ClientStartGameSessionPlacement` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a game
    session request, these properties communicate details to be used when setting up the new game
    session, such as to specify a game mode, level, or map. Game properties are passed to the game
    server process when initiating a new game session; the server process uses the properties as
    appropriate. For more information, see the `Amazon GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --* **[REQUIRED]**

      Game property identifier.

    - **Value** *(string) --* **[REQUIRED]**

      Game property value.
    """


_ClientStartGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": float},
    total=False,
)


class ClientStartGameSessionPlacementPlayerLatenciesTypeDef(
    _ClientStartGameSessionPlacementPlayerLatenciesTypeDef
):
    """
    Type definition for `ClientStartGameSessionPlacement` `PlayerLatencies`

    Regional latency information for a player, used when requesting a new game session with
    StartGameSessionPlacement . This value indicates the amount of time lag that exists when the
    player is connected to a fleet in the specified region. The relative difference between a
    player's latency values for multiple regions are used to determine which fleets are best suited
    to place a new game session for the player.

    - **PlayerId** *(string) --*

      Unique identifier for a player associated with the latency data.

    - **RegionIdentifier** *(string) --*

      Name of the region that is associated with the latency value.

    - **LatencyInMilliseconds** *(float) --*

      Amount of time that represents the time lag experienced by the player when connected to the
      specified region.
    """


_ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef(
    _ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
):
    """
    Type definition for `ClientStartGameSessionPlacementResponseGameSessionPlacement` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a
    game session request, these properties communicate details to be used when setting up the
    new game session, such as to specify a game mode, level, or map. Game properties are
    passed to the game server process when initiating a new game session; the server process
    uses the properties as appropriate. For more information, see the `Amazon GameLift
    Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef(
    _ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
):
    """
    Type definition for `ClientStartGameSessionPlacementResponseGameSessionPlacement` `PlacedPlayerSessions`

    Information about a player session that was created as part of a
    StartGameSessionPlacement request. This object contains only the player ID and player
    session ID. To retrieve full details on a player session, call  DescribePlayerSessions
    with the player session ID.

    *  CreatePlayerSession

    *  CreatePlayerSessions

    *  DescribePlayerSessions

    * Game session placements

      *  StartGameSessionPlacement

      *  DescribeGameSessionPlacement

      *  StopGameSessionPlacement

    - **PlayerId** *(string) --*

      Unique identifier for a player that is associated with this player session.

    - **PlayerSessionId** *(string) --*

      Unique identifier for a player session.
    """


_ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": float},
    total=False,
)


class ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef(
    _ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
):
    """
    Type definition for `ClientStartGameSessionPlacementResponseGameSessionPlacement` `PlayerLatencies`

    Regional latency information for a player, used when requesting a new game session with
    StartGameSessionPlacement . This value indicates the amount of time lag that exists when
    the player is connected to a fleet in the specified region. The relative difference
    between a player's latency values for multiple regions are used to determine which fleets
    are best suited to place a new game session for the player.

    - **PlayerId** *(string) --*

      Unique identifier for a player associated with the latency data.

    - **RegionIdentifier** *(string) --*

      Name of the region that is associated with the latency value.

    - **LatencyInMilliseconds** *(float) --*

      Amount of time that represents the time lag experienced by the player when connected to
      the specified region.
    """


_ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "Status": str,
        "GameProperties": List[
            ClientStartGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
        ],
        "MaximumPlayerSessionCount": int,
        "GameSessionName": str,
        "GameSessionId": str,
        "GameSessionArn": str,
        "GameSessionRegion": str,
        "PlayerLatencies": List[
            ClientStartGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlacedPlayerSessions": List[
            ClientStartGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
        ],
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef(
    _ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef
):
    """
    Type definition for `ClientStartGameSessionPlacementResponse` `GameSessionPlacement`

    Object that describes the newly created game session placement. This object includes all the
    information provided in the request, as well as start/end time stamps and placement status.

    - **PlacementId** *(string) --*

      Unique identifier for a game session placement.

    - **GameSessionQueueName** *(string) --*

      Descriptive label that is associated with game session queue. Queue names must be unique
      within each region.

    - **Status** *(string) --*

      Current status of the game session placement request.

      * **PENDING** -- The placement request is currently in the queue waiting to be processed.

      * **FULFILLED** -- A new game session and player sessions (if requested) have been
      successfully created. Values for *GameSessionArn* and *GameSessionRegion* are available.

      * **CANCELLED** -- The placement request was canceled with a call to
      StopGameSessionPlacement .

      * **TIMED_OUT** -- A new game session was not successfully created before the time limit
      expired. You can resubmit the placement request as needed.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These properties
      are passed to a game server process in the  GameSession object with a request to start a
      new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in a
        game session request, these properties communicate details to be used when setting up the
        new game session, such as to specify a game mode, level, or map. Game properties are
        passed to the game server process when initiating a new game session; the server process
        uses the properties as appropriate. For more information, see the `Amazon GameLift
        Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **GameSessionName** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to be
      unique.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. This value is set once the new game session is
      placed (placement status is ``FULFILLED`` ).

    - **GameSessionArn** *(string) --*

      Identifier for the game session created by this placement request. This value is set once
      the new game session is placed (placement status is ``FULFILLED`` ). This identifier is
      unique across all regions. You can use this value as a ``GameSessionId`` value as needed.

    - **GameSessionRegion** *(string) --*

      Name of the region where the game session created by this placement request is running.
      This value is set once the new game session is placed (placement status is ``FULFILLED`` ).

    - **PlayerLatencies** *(list) --*

      Set of values, expressed in milliseconds, indicating the amount of latency that a player
      experiences when connected to AWS regions.

      - *(dict) --*

        Regional latency information for a player, used when requesting a new game session with
        StartGameSessionPlacement . This value indicates the amount of time lag that exists when
        the player is connected to a fleet in the specified region. The relative difference
        between a player's latency values for multiple regions are used to determine which fleets
        are best suited to place a new game session for the player.

        - **PlayerId** *(string) --*

          Unique identifier for a player associated with the latency data.

        - **RegionIdentifier** *(string) --*

          Name of the region that is associated with the latency value.

        - **LatencyInMilliseconds** *(float) --*

          Amount of time that represents the time lag experienced by the player when connected to
          the specified region.

    - **StartTime** *(datetime) --*

      Time stamp indicating when this request was placed in the queue. Format is a number
      expressed in Unix time as milliseconds (for example "1469498468.057").

    - **EndTime** *(datetime) --*

      Time stamp indicating when this request was completed, canceled, or timed out.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number. This value is set once the new game session is placed
      (placement status is ``FULFILLED`` ).

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number. This value is set once the new game session is placed
      (placement status is ``FULFILLED`` ).

    - **PlacedPlayerSessions** *(list) --*

      Collection of information on player sessions created in response to the game session
      placement request. These player sessions are created only once a new game session is
      successfully placed (placement status is ``FULFILLED`` ). This information includes the
      player ID (as provided in the placement request) and the corresponding player session ID.
      Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.

      - *(dict) --*

        Information about a player session that was created as part of a
        StartGameSessionPlacement request. This object contains only the player ID and player
        session ID. To retrieve full details on a player session, call  DescribePlayerSessions
        with the player session ID.

        *  CreatePlayerSession

        *  CreatePlayerSessions

        *  DescribePlayerSessions

        * Game session placements

          *  StartGameSessionPlacement

          *  DescribeGameSessionPlacement

          *  StopGameSessionPlacement

        - **PlayerId** *(string) --*

          Unique identifier for a player that is associated with this player session.

        - **PlayerSessionId** *(string) --*

          Unique identifier for a player session.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information on the matchmaking process for this game. Data is in JSON syntax, formatted as
      a string. It identifies the matchmaking configuration used to create the match, and
      contains data on all players assigned to the match, including player attributes and team
      assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      .
    """


_ClientStartGameSessionPlacementResponseTypeDef = TypedDict(
    "_ClientStartGameSessionPlacementResponseTypeDef",
    {
        "GameSessionPlacement": ClientStartGameSessionPlacementResponseGameSessionPlacementTypeDef
    },
    total=False,
)


class ClientStartGameSessionPlacementResponseTypeDef(
    _ClientStartGameSessionPlacementResponseTypeDef
):
    """
    Type definition for `ClientStartGameSessionPlacement` `Response`

    Represents the returned data in response to a request action.

    - **GameSessionPlacement** *(dict) --*

      Object that describes the newly created game session placement. This object includes all the
      information provided in the request, as well as start/end time stamps and placement status.

      - **PlacementId** *(string) --*

        Unique identifier for a game session placement.

      - **GameSessionQueueName** *(string) --*

        Descriptive label that is associated with game session queue. Queue names must be unique
        within each region.

      - **Status** *(string) --*

        Current status of the game session placement request.

        * **PENDING** -- The placement request is currently in the queue waiting to be processed.

        * **FULFILLED** -- A new game session and player sessions (if requested) have been
        successfully created. Values for *GameSessionArn* and *GameSessionRegion* are available.

        * **CANCELLED** -- The placement request was canceled with a call to
        StopGameSessionPlacement .

        * **TIMED_OUT** -- A new game session was not successfully created before the time limit
        expired. You can resubmit the placement request as needed.

      - **GameProperties** *(list) --*

        Set of custom properties for a game session, formatted as key:value pairs. These properties
        are passed to a game server process in the  GameSession object with a request to start a
        new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ).

        - *(dict) --*

          Set of key-value pairs that contain information about a game session. When included in a
          game session request, these properties communicate details to be used when setting up the
          new game session, such as to specify a game mode, level, or map. Game properties are
          passed to the game server process when initiating a new game session; the server process
          uses the properties as appropriate. For more information, see the `Amazon GameLift
          Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
          .

          - **Key** *(string) --*

            Game property identifier.

          - **Value** *(string) --*

            Game property value.

      - **MaximumPlayerSessionCount** *(integer) --*

        Maximum number of players that can be connected simultaneously to the game session.

      - **GameSessionName** *(string) --*

        Descriptive label that is associated with a game session. Session names do not need to be
        unique.

      - **GameSessionId** *(string) --*

        Unique identifier for the game session. This value is set once the new game session is
        placed (placement status is ``FULFILLED`` ).

      - **GameSessionArn** *(string) --*

        Identifier for the game session created by this placement request. This value is set once
        the new game session is placed (placement status is ``FULFILLED`` ). This identifier is
        unique across all regions. You can use this value as a ``GameSessionId`` value as needed.

      - **GameSessionRegion** *(string) --*

        Name of the region where the game session created by this placement request is running.
        This value is set once the new game session is placed (placement status is ``FULFILLED`` ).

      - **PlayerLatencies** *(list) --*

        Set of values, expressed in milliseconds, indicating the amount of latency that a player
        experiences when connected to AWS regions.

        - *(dict) --*

          Regional latency information for a player, used when requesting a new game session with
          StartGameSessionPlacement . This value indicates the amount of time lag that exists when
          the player is connected to a fleet in the specified region. The relative difference
          between a player's latency values for multiple regions are used to determine which fleets
          are best suited to place a new game session for the player.

          - **PlayerId** *(string) --*

            Unique identifier for a player associated with the latency data.

          - **RegionIdentifier** *(string) --*

            Name of the region that is associated with the latency value.

          - **LatencyInMilliseconds** *(float) --*

            Amount of time that represents the time lag experienced by the player when connected to
            the specified region.

      - **StartTime** *(datetime) --*

        Time stamp indicating when this request was placed in the queue. Format is a number
        expressed in Unix time as milliseconds (for example "1469498468.057").

      - **EndTime** *(datetime) --*

        Time stamp indicating when this request was completed, canceled, or timed out.

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number. This value is set once the new game session is placed
        (placement status is ``FULFILLED`` ).

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number. This value is set once the new game session is placed
        (placement status is ``FULFILLED`` ).

      - **PlacedPlayerSessions** *(list) --*

        Collection of information on player sessions created in response to the game session
        placement request. These player sessions are created only once a new game session is
        successfully placed (placement status is ``FULFILLED`` ). This information includes the
        player ID (as provided in the placement request) and the corresponding player session ID.
        Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.

        - *(dict) --*

          Information about a player session that was created as part of a
          StartGameSessionPlacement request. This object contains only the player ID and player
          session ID. To retrieve full details on a player session, call  DescribePlayerSessions
          with the player session ID.

          *  CreatePlayerSession

          *  CreatePlayerSessions

          *  DescribePlayerSessions

          * Game session placements

            *  StartGameSessionPlacement

            *  DescribeGameSessionPlacement

            *  StopGameSessionPlacement

          - **PlayerId** *(string) --*

            Unique identifier for a player that is associated with this player session.

          - **PlayerSessionId** *(string) --*

            Unique identifier for a player session.

      - **GameSessionData** *(string) --*

        Set of custom game session properties, formatted as a single string value. This data is
        passed to a game server process in the  GameSession object with a request to start a new
        game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ).

      - **MatchmakerData** *(string) --*

        Information on the matchmaking process for this game. Data is in JSON syntax, formatted as
        a string. It identifies the matchmaking configuration used to create the match, and
        contains data on all players assigned to the match, including player attributes and team
        assignments. For more details on matchmaker data, see `Match Data
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
        .
    """


_ClientStartMatchBackfillPlayersPlayerAttributesTypeDef = TypedDict(
    "_ClientStartMatchBackfillPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)


class ClientStartMatchBackfillPlayersPlayerAttributesTypeDef(
    _ClientStartMatchBackfillPlayersPlayerAttributesTypeDef
):
    """
    Type definition for `ClientStartMatchBackfillPlayers` `PlayerAttributes`

    Values for use in  Player attribute key:value pairs. This object lets you specify an
    attribute value using any of the valid data types: string, number, string array, or data
    map. Each ``AttributeValue`` object can use only one of the available properties.

    - **S** *(string) --*

      For single string values. Maximum string length is 100 characters.

    - **N** *(float) --*

      For number values, expressed as double.

    - **SL** *(list) --*

      For a list of up to 10 strings. Maximum length for each string is 100 characters.
      Duplicate values are not recognized; all occurrences of the repeated value after the
      first of a repeated value are ignored.

      - *(string) --*

    - **SDM** *(dict) --*

      For a map of up to 10 data type:value pairs. Maximum length for each string value is
      100 characters.

      - *(string) --*

        - *(float) --*
    """


_ClientStartMatchBackfillPlayersTypeDef = TypedDict(
    "_ClientStartMatchBackfillPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[
            str, ClientStartMatchBackfillPlayersPlayerAttributesTypeDef
        ],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)


class ClientStartMatchBackfillPlayersTypeDef(_ClientStartMatchBackfillPlayersTypeDef):
    """
    Type definition for `ClientStartMatchBackfill` `Players`

    Represents a player in matchmaking. When starting a matchmaking request, a player has a player
    ID, attributes, and may have latency data. Team information is added after a match has been
    successfully completed.

    - **PlayerId** *(string) --*

      Unique identifier for a player

    - **PlayerAttributes** *(dict) --*

      Collection of key:value pairs containing player information for use in matchmaking. Player
      attribute keys must match the *playerAttributes* used in a matchmaking rule set. Example:
      ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}}`` .

      - *(string) --*

        - *(dict) --*

          Values for use in  Player attribute key:value pairs. This object lets you specify an
          attribute value using any of the valid data types: string, number, string array, or data
          map. Each ``AttributeValue`` object can use only one of the available properties.

          - **S** *(string) --*

            For single string values. Maximum string length is 100 characters.

          - **N** *(float) --*

            For number values, expressed as double.

          - **SL** *(list) --*

            For a list of up to 10 strings. Maximum length for each string is 100 characters.
            Duplicate values are not recognized; all occurrences of the repeated value after the
            first of a repeated value are ignored.

            - *(string) --*

          - **SDM** *(dict) --*

            For a map of up to 10 data type:value pairs. Maximum length for each string value is
            100 characters.

            - *(string) --*

              - *(float) --*

    - **Team** *(string) --*

      Name of the team that the player is assigned to in a match. Team names are defined in a
      matchmaking rule set.

    - **LatencyInMs** *(dict) --*

      Set of values, expressed in milliseconds, indicating the amount of latency that a player
      experiences when connected to AWS regions. If this property is present, FlexMatch considers
      placing the match only in regions for which latency is reported.

      If a matchmaker has a rule that evaluates player latency, players must report latency in
      order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no
      regions are available to the player and the ticket is not matchable.

      - *(string) --*

        - *(integer) --*
    """


_ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef(
    _ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
):
    """
    Type definition for `ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfo` `MatchedPlayerSessions`

    Represents a new player session that is created as a result of a successful FlexMatch
    match. A successful match automatically creates new player sessions for every player ID
    in the original matchmaking request.

    When players connect to the match's game session, they must include both player ID and
    player session ID in order to claim their assigned player slot.

    - **PlayerId** *(string) --*

      Unique identifier for a player

    - **PlayerSessionId** *(string) --*

      Unique identifier for a player session
    """


_ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "MatchedPlayerSessions": List[
            ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
        ],
    },
    total=False,
)


class ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef(
    _ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef
):
    """
    Type definition for `ClientStartMatchBackfillResponseMatchmakingTicket` `GameSessionConnectionInfo`

    Identifier and connection information of the game session created for the match. This
    information is added to the ticket only after the matchmaking request has been successfully
    completed.

    - **GameSessionArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
      assigned to a game session and uniquely identifies it.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **MatchedPlayerSessions** *(list) --*

      Collection of player session IDs, one for each player ID that was included in the
      original matchmaking request.

      - *(dict) --*

        Represents a new player session that is created as a result of a successful FlexMatch
        match. A successful match automatically creates new player sessions for every player ID
        in the original matchmaking request.

        When players connect to the match's game session, they must include both player ID and
        player session ID in order to claim their assigned player slot.

        - **PlayerId** *(string) --*

          Unique identifier for a player

        - **PlayerSessionId** *(string) --*

          Unique identifier for a player session
    """


_ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)


class ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef(
    _ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef
):
    """
    Type definition for `ClientStartMatchBackfillResponseMatchmakingTicketPlayers` `PlayerAttributes`

    Values for use in  Player attribute key:value pairs. This object lets you specify
    an attribute value using any of the valid data types: string, number, string array,
    or data map. Each ``AttributeValue`` object can use only one of the available
    properties.

    - **S** *(string) --*

      For single string values. Maximum string length is 100 characters.

    - **N** *(float) --*

      For number values, expressed as double.

    - **SL** *(list) --*

      For a list of up to 10 strings. Maximum length for each string is 100 characters.
      Duplicate values are not recognized; all occurrences of the repeated value after
      the first of a repeated value are ignored.

      - *(string) --*

    - **SDM** *(dict) --*

      For a map of up to 10 data type:value pairs. Maximum length for each string value
      is 100 characters.

      - *(string) --*

        - *(float) --*
    """


_ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[
            str,
            ClientStartMatchBackfillResponseMatchmakingTicketPlayersPlayerAttributesTypeDef,
        ],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)


class ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef(
    _ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef
):
    """
    Type definition for `ClientStartMatchBackfillResponseMatchmakingTicket` `Players`

    Represents a player in matchmaking. When starting a matchmaking request, a player has a
    player ID, attributes, and may have latency data. Team information is added after a match
    has been successfully completed.

    - **PlayerId** *(string) --*

      Unique identifier for a player

    - **PlayerAttributes** *(dict) --*

      Collection of key:value pairs containing player information for use in matchmaking.
      Player attribute keys must match the *playerAttributes* used in a matchmaking rule set.
      Example: ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S":
      "deathmatch"}}`` .

      - *(string) --*

        - *(dict) --*

          Values for use in  Player attribute key:value pairs. This object lets you specify
          an attribute value using any of the valid data types: string, number, string array,
          or data map. Each ``AttributeValue`` object can use only one of the available
          properties.

          - **S** *(string) --*

            For single string values. Maximum string length is 100 characters.

          - **N** *(float) --*

            For number values, expressed as double.

          - **SL** *(list) --*

            For a list of up to 10 strings. Maximum length for each string is 100 characters.
            Duplicate values are not recognized; all occurrences of the repeated value after
            the first of a repeated value are ignored.

            - *(string) --*

          - **SDM** *(dict) --*

            For a map of up to 10 data type:value pairs. Maximum length for each string value
            is 100 characters.

            - *(string) --*

              - *(float) --*

    - **Team** *(string) --*

      Name of the team that the player is assigned to in a match. Team names are defined in a
      matchmaking rule set.

    - **LatencyInMs** *(dict) --*

      Set of values, expressed in milliseconds, indicating the amount of latency that a
      player experiences when connected to AWS regions. If this property is present,
      FlexMatch considers placing the match only in regions for which latency is reported.

      If a matchmaker has a rule that evaluates player latency, players must report latency
      in order to be matched. If no latency is reported in this scenario, FlexMatch assumes
      that no regions are available to the player and the ticket is not matchable.

      - *(string) --*

        - *(integer) --*
    """


_ClientStartMatchBackfillResponseMatchmakingTicketTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseMatchmakingTicketTypeDef",
    {
        "TicketId": str,
        "ConfigurationName": str,
        "Status": str,
        "StatusReason": str,
        "StatusMessage": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Players": List[
            ClientStartMatchBackfillResponseMatchmakingTicketPlayersTypeDef
        ],
        "GameSessionConnectionInfo": ClientStartMatchBackfillResponseMatchmakingTicketGameSessionConnectionInfoTypeDef,
        "EstimatedWaitTime": int,
    },
    total=False,
)


class ClientStartMatchBackfillResponseMatchmakingTicketTypeDef(
    _ClientStartMatchBackfillResponseMatchmakingTicketTypeDef
):
    """
    Type definition for `ClientStartMatchBackfillResponse` `MatchmakingTicket`

    Ticket representing the backfill matchmaking request. This object includes the information in
    the request, ticket status, and match results as generated during the matchmaking process.

    - **TicketId** *(string) --*

      Unique identifier for a matchmaking ticket.

    - **ConfigurationName** *(string) --*

      Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking
      configurations determine how players are grouped into a match and how a new game session is
      created for the match.

    - **Status** *(string) --*

      Current status of the matchmaking request.

      * **QUEUED** -- The matchmaking request has been received and is currently waiting to be
      processed.

      * **SEARCHING** -- The matchmaking request is currently being processed.

      * **REQUIRES_ACCEPTANCE** -- A match has been proposed and the players must accept the
      match (see  AcceptMatch ). This status is used only with requests that use a matchmaking
      configuration with a player acceptance requirement.

      * **PLACING** -- The FlexMatch engine has matched players and is in the process of placing
      a new game session for the match.

      * **COMPLETED** -- Players have been matched and a game session is ready to host the
      players. A ticket in this state contains the necessary connection information for players.

      * **FAILED** -- The matchmaking request was not completed.

      * **CANCELLED** -- The matchmaking request was canceled. This may be the result of a call
      to  StopMatchmaking or a proposed match that one or more players failed to accept.

      * **TIMED_OUT** -- The matchmaking request was not successful within the duration specified
      in the matchmaking configuration.

      .. note::

        Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED,
        TIMED_OUT) can be resubmitted as new requests with new ticket IDs.

    - **StatusReason** *(string) --*

      Code to explain the current status. For example, a status reason may indicate when a ticket
      has returned to ``SEARCHING`` status after a proposed match fails to receive player
      acceptances.

    - **StatusMessage** *(string) --*

      Additional information about the current status.

    - **StartTime** *(datetime) --*

      Time stamp indicating when this matchmaking request was received. Format is a number
      expressed in Unix time as milliseconds (for example "1469498468.057").

    - **EndTime** *(datetime) --*

      Time stamp indicating when this matchmaking request stopped being processed due to success,
      failure, or cancellation. Format is a number expressed in Unix time as milliseconds (for
      example "1469498468.057").

    - **Players** *(list) --*

      A set of ``Player`` objects, each representing a player to find matches for. Players are
      identified by a unique player ID and may include latency data for use during matchmaking.
      If the ticket is in status ``COMPLETED`` , the ``Player`` objects include the team the
      players were assigned to in the resulting match.

      - *(dict) --*

        Represents a player in matchmaking. When starting a matchmaking request, a player has a
        player ID, attributes, and may have latency data. Team information is added after a match
        has been successfully completed.

        - **PlayerId** *(string) --*

          Unique identifier for a player

        - **PlayerAttributes** *(dict) --*

          Collection of key:value pairs containing player information for use in matchmaking.
          Player attribute keys must match the *playerAttributes* used in a matchmaking rule set.
          Example: ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S":
          "deathmatch"}}`` .

          - *(string) --*

            - *(dict) --*

              Values for use in  Player attribute key:value pairs. This object lets you specify
              an attribute value using any of the valid data types: string, number, string array,
              or data map. Each ``AttributeValue`` object can use only one of the available
              properties.

              - **S** *(string) --*

                For single string values. Maximum string length is 100 characters.

              - **N** *(float) --*

                For number values, expressed as double.

              - **SL** *(list) --*

                For a list of up to 10 strings. Maximum length for each string is 100 characters.
                Duplicate values are not recognized; all occurrences of the repeated value after
                the first of a repeated value are ignored.

                - *(string) --*

              - **SDM** *(dict) --*

                For a map of up to 10 data type:value pairs. Maximum length for each string value
                is 100 characters.

                - *(string) --*

                  - *(float) --*

        - **Team** *(string) --*

          Name of the team that the player is assigned to in a match. Team names are defined in a
          matchmaking rule set.

        - **LatencyInMs** *(dict) --*

          Set of values, expressed in milliseconds, indicating the amount of latency that a
          player experiences when connected to AWS regions. If this property is present,
          FlexMatch considers placing the match only in regions for which latency is reported.

          If a matchmaker has a rule that evaluates player latency, players must report latency
          in order to be matched. If no latency is reported in this scenario, FlexMatch assumes
          that no regions are available to the player and the ticket is not matchable.

          - *(string) --*

            - *(integer) --*

    - **GameSessionConnectionInfo** *(dict) --*

      Identifier and connection information of the game session created for the match. This
      information is added to the ticket only after the matchmaking request has been successfully
      completed.

      - **GameSessionArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
        assigned to a game session and uniquely identifies it.

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number.

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift game server, an app
        needs both the IP address and port number.

      - **MatchedPlayerSessions** *(list) --*

        Collection of player session IDs, one for each player ID that was included in the
        original matchmaking request.

        - *(dict) --*

          Represents a new player session that is created as a result of a successful FlexMatch
          match. A successful match automatically creates new player sessions for every player ID
          in the original matchmaking request.

          When players connect to the match's game session, they must include both player ID and
          player session ID in order to claim their assigned player slot.

          - **PlayerId** *(string) --*

            Unique identifier for a player

          - **PlayerSessionId** *(string) --*

            Unique identifier for a player session

    - **EstimatedWaitTime** *(integer) --*

      Average amount of time (in seconds) that players are currently waiting for a match. If
      there is not enough recent data, this property may be empty.
    """


_ClientStartMatchBackfillResponseTypeDef = TypedDict(
    "_ClientStartMatchBackfillResponseTypeDef",
    {"MatchmakingTicket": ClientStartMatchBackfillResponseMatchmakingTicketTypeDef},
    total=False,
)


class ClientStartMatchBackfillResponseTypeDef(_ClientStartMatchBackfillResponseTypeDef):
    """
    Type definition for `ClientStartMatchBackfill` `Response`

    Represents the returned data in response to a request action.

    - **MatchmakingTicket** *(dict) --*

      Ticket representing the backfill matchmaking request. This object includes the information in
      the request, ticket status, and match results as generated during the matchmaking process.

      - **TicketId** *(string) --*

        Unique identifier for a matchmaking ticket.

      - **ConfigurationName** *(string) --*

        Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking
        configurations determine how players are grouped into a match and how a new game session is
        created for the match.

      - **Status** *(string) --*

        Current status of the matchmaking request.

        * **QUEUED** -- The matchmaking request has been received and is currently waiting to be
        processed.

        * **SEARCHING** -- The matchmaking request is currently being processed.

        * **REQUIRES_ACCEPTANCE** -- A match has been proposed and the players must accept the
        match (see  AcceptMatch ). This status is used only with requests that use a matchmaking
        configuration with a player acceptance requirement.

        * **PLACING** -- The FlexMatch engine has matched players and is in the process of placing
        a new game session for the match.

        * **COMPLETED** -- Players have been matched and a game session is ready to host the
        players. A ticket in this state contains the necessary connection information for players.

        * **FAILED** -- The matchmaking request was not completed.

        * **CANCELLED** -- The matchmaking request was canceled. This may be the result of a call
        to  StopMatchmaking or a proposed match that one or more players failed to accept.

        * **TIMED_OUT** -- The matchmaking request was not successful within the duration specified
        in the matchmaking configuration.

        .. note::

          Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED,
          TIMED_OUT) can be resubmitted as new requests with new ticket IDs.

      - **StatusReason** *(string) --*

        Code to explain the current status. For example, a status reason may indicate when a ticket
        has returned to ``SEARCHING`` status after a proposed match fails to receive player
        acceptances.

      - **StatusMessage** *(string) --*

        Additional information about the current status.

      - **StartTime** *(datetime) --*

        Time stamp indicating when this matchmaking request was received. Format is a number
        expressed in Unix time as milliseconds (for example "1469498468.057").

      - **EndTime** *(datetime) --*

        Time stamp indicating when this matchmaking request stopped being processed due to success,
        failure, or cancellation. Format is a number expressed in Unix time as milliseconds (for
        example "1469498468.057").

      - **Players** *(list) --*

        A set of ``Player`` objects, each representing a player to find matches for. Players are
        identified by a unique player ID and may include latency data for use during matchmaking.
        If the ticket is in status ``COMPLETED`` , the ``Player`` objects include the team the
        players were assigned to in the resulting match.

        - *(dict) --*

          Represents a player in matchmaking. When starting a matchmaking request, a player has a
          player ID, attributes, and may have latency data. Team information is added after a match
          has been successfully completed.

          - **PlayerId** *(string) --*

            Unique identifier for a player

          - **PlayerAttributes** *(dict) --*

            Collection of key:value pairs containing player information for use in matchmaking.
            Player attribute keys must match the *playerAttributes* used in a matchmaking rule set.
            Example: ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S":
            "deathmatch"}}`` .

            - *(string) --*

              - *(dict) --*

                Values for use in  Player attribute key:value pairs. This object lets you specify
                an attribute value using any of the valid data types: string, number, string array,
                or data map. Each ``AttributeValue`` object can use only one of the available
                properties.

                - **S** *(string) --*

                  For single string values. Maximum string length is 100 characters.

                - **N** *(float) --*

                  For number values, expressed as double.

                - **SL** *(list) --*

                  For a list of up to 10 strings. Maximum length for each string is 100 characters.
                  Duplicate values are not recognized; all occurrences of the repeated value after
                  the first of a repeated value are ignored.

                  - *(string) --*

                - **SDM** *(dict) --*

                  For a map of up to 10 data type:value pairs. Maximum length for each string value
                  is 100 characters.

                  - *(string) --*

                    - *(float) --*

          - **Team** *(string) --*

            Name of the team that the player is assigned to in a match. Team names are defined in a
            matchmaking rule set.

          - **LatencyInMs** *(dict) --*

            Set of values, expressed in milliseconds, indicating the amount of latency that a
            player experiences when connected to AWS regions. If this property is present,
            FlexMatch considers placing the match only in regions for which latency is reported.

            If a matchmaker has a rule that evaluates player latency, players must report latency
            in order to be matched. If no latency is reported in this scenario, FlexMatch assumes
            that no regions are available to the player and the ticket is not matchable.

            - *(string) --*

              - *(integer) --*

      - **GameSessionConnectionInfo** *(dict) --*

        Identifier and connection information of the game session created for the match. This
        information is added to the ticket only after the matchmaking request has been successfully
        completed.

        - **GameSessionArn** *(string) --*

          Amazon Resource Name (`ARN
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
          assigned to a game session and uniquely identifies it.

        - **IpAddress** *(string) --*

          IP address of the game session. To connect to a Amazon GameLift game server, an app needs
          both the IP address and port number.

        - **DnsName** *(string) --*

        - **Port** *(integer) --*

          Port number for the game session. To connect to a Amazon GameLift game server, an app
          needs both the IP address and port number.

        - **MatchedPlayerSessions** *(list) --*

          Collection of player session IDs, one for each player ID that was included in the
          original matchmaking request.

          - *(dict) --*

            Represents a new player session that is created as a result of a successful FlexMatch
            match. A successful match automatically creates new player sessions for every player ID
            in the original matchmaking request.

            When players connect to the match's game session, they must include both player ID and
            player session ID in order to claim their assigned player slot.

            - **PlayerId** *(string) --*

              Unique identifier for a player

            - **PlayerSessionId** *(string) --*

              Unique identifier for a player session

      - **EstimatedWaitTime** *(integer) --*

        Average amount of time (in seconds) that players are currently waiting for a match. If
        there is not enough recent data, this property may be empty.
    """


_ClientStartMatchmakingPlayersPlayerAttributesTypeDef = TypedDict(
    "_ClientStartMatchmakingPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)


class ClientStartMatchmakingPlayersPlayerAttributesTypeDef(
    _ClientStartMatchmakingPlayersPlayerAttributesTypeDef
):
    """
    Type definition for `ClientStartMatchmakingPlayers` `PlayerAttributes`

    Values for use in  Player attribute key:value pairs. This object lets you specify an
    attribute value using any of the valid data types: string, number, string array, or data
    map. Each ``AttributeValue`` object can use only one of the available properties.

    - **S** *(string) --*

      For single string values. Maximum string length is 100 characters.

    - **N** *(float) --*

      For number values, expressed as double.

    - **SL** *(list) --*

      For a list of up to 10 strings. Maximum length for each string is 100 characters.
      Duplicate values are not recognized; all occurrences of the repeated value after the
      first of a repeated value are ignored.

      - *(string) --*

    - **SDM** *(dict) --*

      For a map of up to 10 data type:value pairs. Maximum length for each string value is
      100 characters.

      - *(string) --*

        - *(float) --*
    """


_ClientStartMatchmakingPlayersTypeDef = TypedDict(
    "_ClientStartMatchmakingPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[
            str, ClientStartMatchmakingPlayersPlayerAttributesTypeDef
        ],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)


class ClientStartMatchmakingPlayersTypeDef(_ClientStartMatchmakingPlayersTypeDef):
    """
    Type definition for `ClientStartMatchmaking` `Players`

    Represents a player in matchmaking. When starting a matchmaking request, a player has a player
    ID, attributes, and may have latency data. Team information is added after a match has been
    successfully completed.

    - **PlayerId** *(string) --*

      Unique identifier for a player

    - **PlayerAttributes** *(dict) --*

      Collection of key:value pairs containing player information for use in matchmaking. Player
      attribute keys must match the *playerAttributes* used in a matchmaking rule set. Example:
      ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}}`` .

      - *(string) --*

        - *(dict) --*

          Values for use in  Player attribute key:value pairs. This object lets you specify an
          attribute value using any of the valid data types: string, number, string array, or data
          map. Each ``AttributeValue`` object can use only one of the available properties.

          - **S** *(string) --*

            For single string values. Maximum string length is 100 characters.

          - **N** *(float) --*

            For number values, expressed as double.

          - **SL** *(list) --*

            For a list of up to 10 strings. Maximum length for each string is 100 characters.
            Duplicate values are not recognized; all occurrences of the repeated value after the
            first of a repeated value are ignored.

            - *(string) --*

          - **SDM** *(dict) --*

            For a map of up to 10 data type:value pairs. Maximum length for each string value is
            100 characters.

            - *(string) --*

              - *(float) --*

    - **Team** *(string) --*

      Name of the team that the player is assigned to in a match. Team names are defined in a
      matchmaking rule set.

    - **LatencyInMs** *(dict) --*

      Set of values, expressed in milliseconds, indicating the amount of latency that a player
      experiences when connected to AWS regions. If this property is present, FlexMatch considers
      placing the match only in regions for which latency is reported.

      If a matchmaker has a rule that evaluates player latency, players must report latency in
      order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no
      regions are available to the player and the ticket is not matchable.

      - *(string) --*

        - *(integer) --*
    """


_ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef(
    _ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
):
    """
    Type definition for `ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfo` `MatchedPlayerSessions`

    Represents a new player session that is created as a result of a successful FlexMatch
    match. A successful match automatically creates new player sessions for every player ID
    in the original matchmaking request.

    When players connect to the match's game session, they must include both player ID and
    player session ID in order to claim their assigned player slot.

    - **PlayerId** *(string) --*

      Unique identifier for a player

    - **PlayerSessionId** *(string) --*

      Unique identifier for a player session
    """


_ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "MatchedPlayerSessions": List[
            ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoMatchedPlayerSessionsTypeDef
        ],
    },
    total=False,
)


class ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef(
    _ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef
):
    """
    Type definition for `ClientStartMatchmakingResponseMatchmakingTicket` `GameSessionConnectionInfo`

    Identifier and connection information of the game session created for the match. This
    information is added to the ticket only after the matchmaking request has been successfully
    completed.

    - **GameSessionArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
      assigned to a game session and uniquely identifies it.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **MatchedPlayerSessions** *(list) --*

      Collection of player session IDs, one for each player ID that was included in the
      original matchmaking request.

      - *(dict) --*

        Represents a new player session that is created as a result of a successful FlexMatch
        match. A successful match automatically creates new player sessions for every player ID
        in the original matchmaking request.

        When players connect to the match's game session, they must include both player ID and
        player session ID in order to claim their assigned player slot.

        - **PlayerId** *(string) --*

          Unique identifier for a player

        - **PlayerSessionId** *(string) --*

          Unique identifier for a player session
    """


_ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)


class ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef(
    _ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef
):
    """
    Type definition for `ClientStartMatchmakingResponseMatchmakingTicketPlayers` `PlayerAttributes`

    Values for use in  Player attribute key:value pairs. This object lets you specify
    an attribute value using any of the valid data types: string, number, string array,
    or data map. Each ``AttributeValue`` object can use only one of the available
    properties.

    - **S** *(string) --*

      For single string values. Maximum string length is 100 characters.

    - **N** *(float) --*

      For number values, expressed as double.

    - **SL** *(list) --*

      For a list of up to 10 strings. Maximum length for each string is 100 characters.
      Duplicate values are not recognized; all occurrences of the repeated value after
      the first of a repeated value are ignored.

      - *(string) --*

    - **SDM** *(dict) --*

      For a map of up to 10 data type:value pairs. Maximum length for each string value
      is 100 characters.

      - *(string) --*

        - *(float) --*
    """


_ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[
            str,
            ClientStartMatchmakingResponseMatchmakingTicketPlayersPlayerAttributesTypeDef,
        ],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)


class ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef(
    _ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef
):
    """
    Type definition for `ClientStartMatchmakingResponseMatchmakingTicket` `Players`

    Represents a player in matchmaking. When starting a matchmaking request, a player has a
    player ID, attributes, and may have latency data. Team information is added after a match
    has been successfully completed.

    - **PlayerId** *(string) --*

      Unique identifier for a player

    - **PlayerAttributes** *(dict) --*

      Collection of key:value pairs containing player information for use in matchmaking.
      Player attribute keys must match the *playerAttributes* used in a matchmaking rule set.
      Example: ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S":
      "deathmatch"}}`` .

      - *(string) --*

        - *(dict) --*

          Values for use in  Player attribute key:value pairs. This object lets you specify
          an attribute value using any of the valid data types: string, number, string array,
          or data map. Each ``AttributeValue`` object can use only one of the available
          properties.

          - **S** *(string) --*

            For single string values. Maximum string length is 100 characters.

          - **N** *(float) --*

            For number values, expressed as double.

          - **SL** *(list) --*

            For a list of up to 10 strings. Maximum length for each string is 100 characters.
            Duplicate values are not recognized; all occurrences of the repeated value after
            the first of a repeated value are ignored.

            - *(string) --*

          - **SDM** *(dict) --*

            For a map of up to 10 data type:value pairs. Maximum length for each string value
            is 100 characters.

            - *(string) --*

              - *(float) --*

    - **Team** *(string) --*

      Name of the team that the player is assigned to in a match. Team names are defined in a
      matchmaking rule set.

    - **LatencyInMs** *(dict) --*

      Set of values, expressed in milliseconds, indicating the amount of latency that a
      player experiences when connected to AWS regions. If this property is present,
      FlexMatch considers placing the match only in regions for which latency is reported.

      If a matchmaker has a rule that evaluates player latency, players must report latency
      in order to be matched. If no latency is reported in this scenario, FlexMatch assumes
      that no regions are available to the player and the ticket is not matchable.

      - *(string) --*

        - *(integer) --*
    """


_ClientStartMatchmakingResponseMatchmakingTicketTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseMatchmakingTicketTypeDef",
    {
        "TicketId": str,
        "ConfigurationName": str,
        "Status": str,
        "StatusReason": str,
        "StatusMessage": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Players": List[ClientStartMatchmakingResponseMatchmakingTicketPlayersTypeDef],
        "GameSessionConnectionInfo": ClientStartMatchmakingResponseMatchmakingTicketGameSessionConnectionInfoTypeDef,
        "EstimatedWaitTime": int,
    },
    total=False,
)


class ClientStartMatchmakingResponseMatchmakingTicketTypeDef(
    _ClientStartMatchmakingResponseMatchmakingTicketTypeDef
):
    """
    Type definition for `ClientStartMatchmakingResponse` `MatchmakingTicket`

    Ticket representing the matchmaking request. This object include the information included in
    the request, ticket status, and match results as generated during the matchmaking process.

    - **TicketId** *(string) --*

      Unique identifier for a matchmaking ticket.

    - **ConfigurationName** *(string) --*

      Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking
      configurations determine how players are grouped into a match and how a new game session is
      created for the match.

    - **Status** *(string) --*

      Current status of the matchmaking request.

      * **QUEUED** -- The matchmaking request has been received and is currently waiting to be
      processed.

      * **SEARCHING** -- The matchmaking request is currently being processed.

      * **REQUIRES_ACCEPTANCE** -- A match has been proposed and the players must accept the
      match (see  AcceptMatch ). This status is used only with requests that use a matchmaking
      configuration with a player acceptance requirement.

      * **PLACING** -- The FlexMatch engine has matched players and is in the process of placing
      a new game session for the match.

      * **COMPLETED** -- Players have been matched and a game session is ready to host the
      players. A ticket in this state contains the necessary connection information for players.

      * **FAILED** -- The matchmaking request was not completed.

      * **CANCELLED** -- The matchmaking request was canceled. This may be the result of a call
      to  StopMatchmaking or a proposed match that one or more players failed to accept.

      * **TIMED_OUT** -- The matchmaking request was not successful within the duration specified
      in the matchmaking configuration.

      .. note::

        Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED,
        TIMED_OUT) can be resubmitted as new requests with new ticket IDs.

    - **StatusReason** *(string) --*

      Code to explain the current status. For example, a status reason may indicate when a ticket
      has returned to ``SEARCHING`` status after a proposed match fails to receive player
      acceptances.

    - **StatusMessage** *(string) --*

      Additional information about the current status.

    - **StartTime** *(datetime) --*

      Time stamp indicating when this matchmaking request was received. Format is a number
      expressed in Unix time as milliseconds (for example "1469498468.057").

    - **EndTime** *(datetime) --*

      Time stamp indicating when this matchmaking request stopped being processed due to success,
      failure, or cancellation. Format is a number expressed in Unix time as milliseconds (for
      example "1469498468.057").

    - **Players** *(list) --*

      A set of ``Player`` objects, each representing a player to find matches for. Players are
      identified by a unique player ID and may include latency data for use during matchmaking.
      If the ticket is in status ``COMPLETED`` , the ``Player`` objects include the team the
      players were assigned to in the resulting match.

      - *(dict) --*

        Represents a player in matchmaking. When starting a matchmaking request, a player has a
        player ID, attributes, and may have latency data. Team information is added after a match
        has been successfully completed.

        - **PlayerId** *(string) --*

          Unique identifier for a player

        - **PlayerAttributes** *(dict) --*

          Collection of key:value pairs containing player information for use in matchmaking.
          Player attribute keys must match the *playerAttributes* used in a matchmaking rule set.
          Example: ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S":
          "deathmatch"}}`` .

          - *(string) --*

            - *(dict) --*

              Values for use in  Player attribute key:value pairs. This object lets you specify
              an attribute value using any of the valid data types: string, number, string array,
              or data map. Each ``AttributeValue`` object can use only one of the available
              properties.

              - **S** *(string) --*

                For single string values. Maximum string length is 100 characters.

              - **N** *(float) --*

                For number values, expressed as double.

              - **SL** *(list) --*

                For a list of up to 10 strings. Maximum length for each string is 100 characters.
                Duplicate values are not recognized; all occurrences of the repeated value after
                the first of a repeated value are ignored.

                - *(string) --*

              - **SDM** *(dict) --*

                For a map of up to 10 data type:value pairs. Maximum length for each string value
                is 100 characters.

                - *(string) --*

                  - *(float) --*

        - **Team** *(string) --*

          Name of the team that the player is assigned to in a match. Team names are defined in a
          matchmaking rule set.

        - **LatencyInMs** *(dict) --*

          Set of values, expressed in milliseconds, indicating the amount of latency that a
          player experiences when connected to AWS regions. If this property is present,
          FlexMatch considers placing the match only in regions for which latency is reported.

          If a matchmaker has a rule that evaluates player latency, players must report latency
          in order to be matched. If no latency is reported in this scenario, FlexMatch assumes
          that no regions are available to the player and the ticket is not matchable.

          - *(string) --*

            - *(integer) --*

    - **GameSessionConnectionInfo** *(dict) --*

      Identifier and connection information of the game session created for the match. This
      information is added to the ticket only after the matchmaking request has been successfully
      completed.

      - **GameSessionArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
        assigned to a game session and uniquely identifies it.

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number.

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift game server, an app
        needs both the IP address and port number.

      - **MatchedPlayerSessions** *(list) --*

        Collection of player session IDs, one for each player ID that was included in the
        original matchmaking request.

        - *(dict) --*

          Represents a new player session that is created as a result of a successful FlexMatch
          match. A successful match automatically creates new player sessions for every player ID
          in the original matchmaking request.

          When players connect to the match's game session, they must include both player ID and
          player session ID in order to claim their assigned player slot.

          - **PlayerId** *(string) --*

            Unique identifier for a player

          - **PlayerSessionId** *(string) --*

            Unique identifier for a player session

    - **EstimatedWaitTime** *(integer) --*

      Average amount of time (in seconds) that players are currently waiting for a match. If
      there is not enough recent data, this property may be empty.
    """


_ClientStartMatchmakingResponseTypeDef = TypedDict(
    "_ClientStartMatchmakingResponseTypeDef",
    {"MatchmakingTicket": ClientStartMatchmakingResponseMatchmakingTicketTypeDef},
    total=False,
)


class ClientStartMatchmakingResponseTypeDef(_ClientStartMatchmakingResponseTypeDef):
    """
    Type definition for `ClientStartMatchmaking` `Response`

    Represents the returned data in response to a request action.

    - **MatchmakingTicket** *(dict) --*

      Ticket representing the matchmaking request. This object include the information included in
      the request, ticket status, and match results as generated during the matchmaking process.

      - **TicketId** *(string) --*

        Unique identifier for a matchmaking ticket.

      - **ConfigurationName** *(string) --*

        Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking
        configurations determine how players are grouped into a match and how a new game session is
        created for the match.

      - **Status** *(string) --*

        Current status of the matchmaking request.

        * **QUEUED** -- The matchmaking request has been received and is currently waiting to be
        processed.

        * **SEARCHING** -- The matchmaking request is currently being processed.

        * **REQUIRES_ACCEPTANCE** -- A match has been proposed and the players must accept the
        match (see  AcceptMatch ). This status is used only with requests that use a matchmaking
        configuration with a player acceptance requirement.

        * **PLACING** -- The FlexMatch engine has matched players and is in the process of placing
        a new game session for the match.

        * **COMPLETED** -- Players have been matched and a game session is ready to host the
        players. A ticket in this state contains the necessary connection information for players.

        * **FAILED** -- The matchmaking request was not completed.

        * **CANCELLED** -- The matchmaking request was canceled. This may be the result of a call
        to  StopMatchmaking or a proposed match that one or more players failed to accept.

        * **TIMED_OUT** -- The matchmaking request was not successful within the duration specified
        in the matchmaking configuration.

        .. note::

          Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED,
          TIMED_OUT) can be resubmitted as new requests with new ticket IDs.

      - **StatusReason** *(string) --*

        Code to explain the current status. For example, a status reason may indicate when a ticket
        has returned to ``SEARCHING`` status after a proposed match fails to receive player
        acceptances.

      - **StatusMessage** *(string) --*

        Additional information about the current status.

      - **StartTime** *(datetime) --*

        Time stamp indicating when this matchmaking request was received. Format is a number
        expressed in Unix time as milliseconds (for example "1469498468.057").

      - **EndTime** *(datetime) --*

        Time stamp indicating when this matchmaking request stopped being processed due to success,
        failure, or cancellation. Format is a number expressed in Unix time as milliseconds (for
        example "1469498468.057").

      - **Players** *(list) --*

        A set of ``Player`` objects, each representing a player to find matches for. Players are
        identified by a unique player ID and may include latency data for use during matchmaking.
        If the ticket is in status ``COMPLETED`` , the ``Player`` objects include the team the
        players were assigned to in the resulting match.

        - *(dict) --*

          Represents a player in matchmaking. When starting a matchmaking request, a player has a
          player ID, attributes, and may have latency data. Team information is added after a match
          has been successfully completed.

          - **PlayerId** *(string) --*

            Unique identifier for a player

          - **PlayerAttributes** *(dict) --*

            Collection of key:value pairs containing player information for use in matchmaking.
            Player attribute keys must match the *playerAttributes* used in a matchmaking rule set.
            Example: ``"PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S":
            "deathmatch"}}`` .

            - *(string) --*

              - *(dict) --*

                Values for use in  Player attribute key:value pairs. This object lets you specify
                an attribute value using any of the valid data types: string, number, string array,
                or data map. Each ``AttributeValue`` object can use only one of the available
                properties.

                - **S** *(string) --*

                  For single string values. Maximum string length is 100 characters.

                - **N** *(float) --*

                  For number values, expressed as double.

                - **SL** *(list) --*

                  For a list of up to 10 strings. Maximum length for each string is 100 characters.
                  Duplicate values are not recognized; all occurrences of the repeated value after
                  the first of a repeated value are ignored.

                  - *(string) --*

                - **SDM** *(dict) --*

                  For a map of up to 10 data type:value pairs. Maximum length for each string value
                  is 100 characters.

                  - *(string) --*

                    - *(float) --*

          - **Team** *(string) --*

            Name of the team that the player is assigned to in a match. Team names are defined in a
            matchmaking rule set.

          - **LatencyInMs** *(dict) --*

            Set of values, expressed in milliseconds, indicating the amount of latency that a
            player experiences when connected to AWS regions. If this property is present,
            FlexMatch considers placing the match only in regions for which latency is reported.

            If a matchmaker has a rule that evaluates player latency, players must report latency
            in order to be matched. If no latency is reported in this scenario, FlexMatch assumes
            that no regions are available to the player and the ticket is not matchable.

            - *(string) --*

              - *(integer) --*

      - **GameSessionConnectionInfo** *(dict) --*

        Identifier and connection information of the game session created for the match. This
        information is added to the ticket only after the matchmaking request has been successfully
        completed.

        - **GameSessionArn** *(string) --*

          Amazon Resource Name (`ARN
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
          assigned to a game session and uniquely identifies it.

        - **IpAddress** *(string) --*

          IP address of the game session. To connect to a Amazon GameLift game server, an app needs
          both the IP address and port number.

        - **DnsName** *(string) --*

        - **Port** *(integer) --*

          Port number for the game session. To connect to a Amazon GameLift game server, an app
          needs both the IP address and port number.

        - **MatchedPlayerSessions** *(list) --*

          Collection of player session IDs, one for each player ID that was included in the
          original matchmaking request.

          - *(dict) --*

            Represents a new player session that is created as a result of a successful FlexMatch
            match. A successful match automatically creates new player sessions for every player ID
            in the original matchmaking request.

            When players connect to the match's game session, they must include both player ID and
            player session ID in order to claim their assigned player slot.

            - **PlayerId** *(string) --*

              Unique identifier for a player

            - **PlayerSessionId** *(string) --*

              Unique identifier for a player session

      - **EstimatedWaitTime** *(integer) --*

        Average amount of time (in seconds) that players are currently waiting for a match. If
        there is not enough recent data, this property may be empty.
    """


_ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef = TypedDict(
    "_ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef(
    _ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
):
    """
    Type definition for `ClientStopGameSessionPlacementResponseGameSessionPlacement` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a
    game session request, these properties communicate details to be used when setting up the
    new game session, such as to specify a game mode, level, or map. Game properties are
    passed to the game server process when initiating a new game session; the server process
    uses the properties as appropriate. For more information, see the `Amazon GameLift
    Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef = TypedDict(
    "_ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef",
    {"PlayerId": str, "PlayerSessionId": str},
    total=False,
)


class ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef(
    _ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
):
    """
    Type definition for `ClientStopGameSessionPlacementResponseGameSessionPlacement` `PlacedPlayerSessions`

    Information about a player session that was created as part of a
    StartGameSessionPlacement request. This object contains only the player ID and player
    session ID. To retrieve full details on a player session, call  DescribePlayerSessions
    with the player session ID.

    *  CreatePlayerSession

    *  CreatePlayerSessions

    *  DescribePlayerSessions

    * Game session placements

      *  StartGameSessionPlacement

      *  DescribeGameSessionPlacement

      *  StopGameSessionPlacement

    - **PlayerId** *(string) --*

      Unique identifier for a player that is associated with this player session.

    - **PlayerSessionId** *(string) --*

      Unique identifier for a player session.
    """


_ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef = TypedDict(
    "_ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": float},
    total=False,
)


class ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef(
    _ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
):
    """
    Type definition for `ClientStopGameSessionPlacementResponseGameSessionPlacement` `PlayerLatencies`

    Regional latency information for a player, used when requesting a new game session with
    StartGameSessionPlacement . This value indicates the amount of time lag that exists when
    the player is connected to a fleet in the specified region. The relative difference
    between a player's latency values for multiple regions are used to determine which fleets
    are best suited to place a new game session for the player.

    - **PlayerId** *(string) --*

      Unique identifier for a player associated with the latency data.

    - **RegionIdentifier** *(string) --*

      Name of the region that is associated with the latency value.

    - **LatencyInMilliseconds** *(float) --*

      Amount of time that represents the time lag experienced by the player when connected to
      the specified region.
    """


_ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef = TypedDict(
    "_ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "Status": str,
        "GameProperties": List[
            ClientStopGameSessionPlacementResponseGameSessionPlacementGamePropertiesTypeDef
        ],
        "MaximumPlayerSessionCount": int,
        "GameSessionName": str,
        "GameSessionId": str,
        "GameSessionArn": str,
        "GameSessionRegion": str,
        "PlayerLatencies": List[
            ClientStopGameSessionPlacementResponseGameSessionPlacementPlayerLatenciesTypeDef
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlacedPlayerSessions": List[
            ClientStopGameSessionPlacementResponseGameSessionPlacementPlacedPlayerSessionsTypeDef
        ],
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef(
    _ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef
):
    """
    Type definition for `ClientStopGameSessionPlacementResponse` `GameSessionPlacement`

    Object that describes the canceled game session placement, with ``CANCELLED`` status and an
    end time stamp.

    - **PlacementId** *(string) --*

      Unique identifier for a game session placement.

    - **GameSessionQueueName** *(string) --*

      Descriptive label that is associated with game session queue. Queue names must be unique
      within each region.

    - **Status** *(string) --*

      Current status of the game session placement request.

      * **PENDING** -- The placement request is currently in the queue waiting to be processed.

      * **FULFILLED** -- A new game session and player sessions (if requested) have been
      successfully created. Values for *GameSessionArn* and *GameSessionRegion* are available.

      * **CANCELLED** -- The placement request was canceled with a call to
      StopGameSessionPlacement .

      * **TIMED_OUT** -- A new game session was not successfully created before the time limit
      expired. You can resubmit the placement request as needed.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These properties
      are passed to a game server process in the  GameSession object with a request to start a
      new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in a
        game session request, these properties communicate details to be used when setting up the
        new game session, such as to specify a game mode, level, or map. Game properties are
        passed to the game server process when initiating a new game session; the server process
        uses the properties as appropriate. For more information, see the `Amazon GameLift
        Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **GameSessionName** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to be
      unique.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. This value is set once the new game session is
      placed (placement status is ``FULFILLED`` ).

    - **GameSessionArn** *(string) --*

      Identifier for the game session created by this placement request. This value is set once
      the new game session is placed (placement status is ``FULFILLED`` ). This identifier is
      unique across all regions. You can use this value as a ``GameSessionId`` value as needed.

    - **GameSessionRegion** *(string) --*

      Name of the region where the game session created by this placement request is running.
      This value is set once the new game session is placed (placement status is ``FULFILLED`` ).

    - **PlayerLatencies** *(list) --*

      Set of values, expressed in milliseconds, indicating the amount of latency that a player
      experiences when connected to AWS regions.

      - *(dict) --*

        Regional latency information for a player, used when requesting a new game session with
        StartGameSessionPlacement . This value indicates the amount of time lag that exists when
        the player is connected to a fleet in the specified region. The relative difference
        between a player's latency values for multiple regions are used to determine which fleets
        are best suited to place a new game session for the player.

        - **PlayerId** *(string) --*

          Unique identifier for a player associated with the latency data.

        - **RegionIdentifier** *(string) --*

          Name of the region that is associated with the latency value.

        - **LatencyInMilliseconds** *(float) --*

          Amount of time that represents the time lag experienced by the player when connected to
          the specified region.

    - **StartTime** *(datetime) --*

      Time stamp indicating when this request was placed in the queue. Format is a number
      expressed in Unix time as milliseconds (for example "1469498468.057").

    - **EndTime** *(datetime) --*

      Time stamp indicating when this request was completed, canceled, or timed out.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number. This value is set once the new game session is placed
      (placement status is ``FULFILLED`` ).

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number. This value is set once the new game session is placed
      (placement status is ``FULFILLED`` ).

    - **PlacedPlayerSessions** *(list) --*

      Collection of information on player sessions created in response to the game session
      placement request. These player sessions are created only once a new game session is
      successfully placed (placement status is ``FULFILLED`` ). This information includes the
      player ID (as provided in the placement request) and the corresponding player session ID.
      Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.

      - *(dict) --*

        Information about a player session that was created as part of a
        StartGameSessionPlacement request. This object contains only the player ID and player
        session ID. To retrieve full details on a player session, call  DescribePlayerSessions
        with the player session ID.

        *  CreatePlayerSession

        *  CreatePlayerSessions

        *  DescribePlayerSessions

        * Game session placements

          *  StartGameSessionPlacement

          *  DescribeGameSessionPlacement

          *  StopGameSessionPlacement

        - **PlayerId** *(string) --*

          Unique identifier for a player that is associated with this player session.

        - **PlayerSessionId** *(string) --*

          Unique identifier for a player session.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information on the matchmaking process for this game. Data is in JSON syntax, formatted as
      a string. It identifies the matchmaking configuration used to create the match, and
      contains data on all players assigned to the match, including player attributes and team
      assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      .
    """


_ClientStopGameSessionPlacementResponseTypeDef = TypedDict(
    "_ClientStopGameSessionPlacementResponseTypeDef",
    {
        "GameSessionPlacement": ClientStopGameSessionPlacementResponseGameSessionPlacementTypeDef
    },
    total=False,
)


class ClientStopGameSessionPlacementResponseTypeDef(
    _ClientStopGameSessionPlacementResponseTypeDef
):
    """
    Type definition for `ClientStopGameSessionPlacement` `Response`

    Represents the returned data in response to a request action.

    - **GameSessionPlacement** *(dict) --*

      Object that describes the canceled game session placement, with ``CANCELLED`` status and an
      end time stamp.

      - **PlacementId** *(string) --*

        Unique identifier for a game session placement.

      - **GameSessionQueueName** *(string) --*

        Descriptive label that is associated with game session queue. Queue names must be unique
        within each region.

      - **Status** *(string) --*

        Current status of the game session placement request.

        * **PENDING** -- The placement request is currently in the queue waiting to be processed.

        * **FULFILLED** -- A new game session and player sessions (if requested) have been
        successfully created. Values for *GameSessionArn* and *GameSessionRegion* are available.

        * **CANCELLED** -- The placement request was canceled with a call to
        StopGameSessionPlacement .

        * **TIMED_OUT** -- A new game session was not successfully created before the time limit
        expired. You can resubmit the placement request as needed.

      - **GameProperties** *(list) --*

        Set of custom properties for a game session, formatted as key:value pairs. These properties
        are passed to a game server process in the  GameSession object with a request to start a
        new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ).

        - *(dict) --*

          Set of key-value pairs that contain information about a game session. When included in a
          game session request, these properties communicate details to be used when setting up the
          new game session, such as to specify a game mode, level, or map. Game properties are
          passed to the game server process when initiating a new game session; the server process
          uses the properties as appropriate. For more information, see the `Amazon GameLift
          Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
          .

          - **Key** *(string) --*

            Game property identifier.

          - **Value** *(string) --*

            Game property value.

      - **MaximumPlayerSessionCount** *(integer) --*

        Maximum number of players that can be connected simultaneously to the game session.

      - **GameSessionName** *(string) --*

        Descriptive label that is associated with a game session. Session names do not need to be
        unique.

      - **GameSessionId** *(string) --*

        Unique identifier for the game session. This value is set once the new game session is
        placed (placement status is ``FULFILLED`` ).

      - **GameSessionArn** *(string) --*

        Identifier for the game session created by this placement request. This value is set once
        the new game session is placed (placement status is ``FULFILLED`` ). This identifier is
        unique across all regions. You can use this value as a ``GameSessionId`` value as needed.

      - **GameSessionRegion** *(string) --*

        Name of the region where the game session created by this placement request is running.
        This value is set once the new game session is placed (placement status is ``FULFILLED`` ).

      - **PlayerLatencies** *(list) --*

        Set of values, expressed in milliseconds, indicating the amount of latency that a player
        experiences when connected to AWS regions.

        - *(dict) --*

          Regional latency information for a player, used when requesting a new game session with
          StartGameSessionPlacement . This value indicates the amount of time lag that exists when
          the player is connected to a fleet in the specified region. The relative difference
          between a player's latency values for multiple regions are used to determine which fleets
          are best suited to place a new game session for the player.

          - **PlayerId** *(string) --*

            Unique identifier for a player associated with the latency data.

          - **RegionIdentifier** *(string) --*

            Name of the region that is associated with the latency value.

          - **LatencyInMilliseconds** *(float) --*

            Amount of time that represents the time lag experienced by the player when connected to
            the specified region.

      - **StartTime** *(datetime) --*

        Time stamp indicating when this request was placed in the queue. Format is a number
        expressed in Unix time as milliseconds (for example "1469498468.057").

      - **EndTime** *(datetime) --*

        Time stamp indicating when this request was completed, canceled, or timed out.

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number. This value is set once the new game session is placed
        (placement status is ``FULFILLED`` ).

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number. This value is set once the new game session is placed
        (placement status is ``FULFILLED`` ).

      - **PlacedPlayerSessions** *(list) --*

        Collection of information on player sessions created in response to the game session
        placement request. These player sessions are created only once a new game session is
        successfully placed (placement status is ``FULFILLED`` ). This information includes the
        player ID (as provided in the placement request) and the corresponding player session ID.
        Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.

        - *(dict) --*

          Information about a player session that was created as part of a
          StartGameSessionPlacement request. This object contains only the player ID and player
          session ID. To retrieve full details on a player session, call  DescribePlayerSessions
          with the player session ID.

          *  CreatePlayerSession

          *  CreatePlayerSessions

          *  DescribePlayerSessions

          * Game session placements

            *  StartGameSessionPlacement

            *  DescribeGameSessionPlacement

            *  StopGameSessionPlacement

          - **PlayerId** *(string) --*

            Unique identifier for a player that is associated with this player session.

          - **PlayerSessionId** *(string) --*

            Unique identifier for a player session.

      - **GameSessionData** *(string) --*

        Set of custom game session properties, formatted as a single string value. This data is
        passed to a game server process in the  GameSession object with a request to start a new
        game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ).

      - **MatchmakerData** *(string) --*

        Information on the matchmaking process for this game. Data is in JSON syntax, formatted as
        a string. It identifies the matchmaking configuration used to create the match, and
        contains data on all players assigned to the match, including player attributes and team
        assignments. For more details on matchmaker data, see `Match Data
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
        .
    """


_ClientUpdateAliasResponseAliasRoutingStrategyTypeDef = TypedDict(
    "_ClientUpdateAliasResponseAliasRoutingStrategyTypeDef",
    {"Type": str, "FleetId": str, "Message": str},
    total=False,
)


class ClientUpdateAliasResponseAliasRoutingStrategyTypeDef(
    _ClientUpdateAliasResponseAliasRoutingStrategyTypeDef
):
    """
    Type definition for `ClientUpdateAliasResponseAlias` `RoutingStrategy`

    Alias configuration for the alias, including routing type and settings.

    - **Type** *(string) --*

      Type of routing strategy.

      Possible routing types include the following:

      * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
      active fleets.

      * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
      display a message to the user. A terminal alias throws a TerminalRoutingStrategyException
      with the  RoutingStrategy message embedded.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the alias points to.

    - **Message** *(string) --*

      Message text to be used with a terminal routing strategy.
    """


_ClientUpdateAliasResponseAliasTypeDef = TypedDict(
    "_ClientUpdateAliasResponseAliasTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": ClientUpdateAliasResponseAliasRoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientUpdateAliasResponseAliasTypeDef(_ClientUpdateAliasResponseAliasTypeDef):
    """
    Type definition for `ClientUpdateAliasResponse` `Alias`

    Object that contains the updated alias configuration.

    - **AliasId** *(string) --*

      Unique identifier for an alias; alias IDs are unique within a region.

    - **Name** *(string) --*

      Descriptive label that is associated with an alias. Alias names do not need to be unique.

    - **AliasArn** *(string) --*

      Unique identifier for an alias; alias ARNs are unique across all regions.

    - **Description** *(string) --*

      Human-readable description of an alias.

    - **RoutingStrategy** *(dict) --*

      Alias configuration for the alias, including routing type and settings.

      - **Type** *(string) --*

        Type of routing strategy.

        Possible routing types include the following:

        * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
        active fleets.

        * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
        display a message to the user. A terminal alias throws a TerminalRoutingStrategyException
        with the  RoutingStrategy message embedded.

      - **FleetId** *(string) --*

        Unique identifier for a fleet that the alias points to.

      - **Message** *(string) --*

        Message text to be used with a terminal routing strategy.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **LastUpdatedTime** *(datetime) --*

      Time stamp indicating when this data object was last modified. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientUpdateAliasResponseTypeDef = TypedDict(
    "_ClientUpdateAliasResponseTypeDef",
    {"Alias": ClientUpdateAliasResponseAliasTypeDef},
    total=False,
)


class ClientUpdateAliasResponseTypeDef(_ClientUpdateAliasResponseTypeDef):
    """
    Type definition for `ClientUpdateAlias` `Response`

    Represents the returned data in response to a request action.

    - **Alias** *(dict) --*

      Object that contains the updated alias configuration.

      - **AliasId** *(string) --*

        Unique identifier for an alias; alias IDs are unique within a region.

      - **Name** *(string) --*

        Descriptive label that is associated with an alias. Alias names do not need to be unique.

      - **AliasArn** *(string) --*

        Unique identifier for an alias; alias ARNs are unique across all regions.

      - **Description** *(string) --*

        Human-readable description of an alias.

      - **RoutingStrategy** *(dict) --*

        Alias configuration for the alias, including routing type and settings.

        - **Type** *(string) --*

          Type of routing strategy.

          Possible routing types include the following:

          * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
          active fleets.

          * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
          display a message to the user. A terminal alias throws a TerminalRoutingStrategyException
          with the  RoutingStrategy message embedded.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the alias points to.

        - **Message** *(string) --*

          Message text to be used with a terminal routing strategy.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **LastUpdatedTime** *(datetime) --*

        Time stamp indicating when this data object was last modified. Format is a number expressed
        in Unix time as milliseconds (for example "1469498468.057").
    """


_ClientUpdateAliasRoutingStrategyTypeDef = TypedDict(
    "_ClientUpdateAliasRoutingStrategyTypeDef",
    {"Type": str, "FleetId": str, "Message": str},
    total=False,
)


class ClientUpdateAliasRoutingStrategyTypeDef(_ClientUpdateAliasRoutingStrategyTypeDef):
    """
    Type definition for `ClientUpdateAlias` `RoutingStrategy`

    Object that specifies the fleet and routing type to use for the alias.

    - **Type** *(string) --*

      Type of routing strategy.

      Possible routing types include the following:

      * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to active
      fleets.

      * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to display a
      message to the user. A terminal alias throws a TerminalRoutingStrategyException with the
      RoutingStrategy message embedded.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the alias points to.

    - **Message** *(string) --*

      Message text to be used with a terminal routing strategy.
    """


_ClientUpdateBuildResponseBuildTypeDef = TypedDict(
    "_ClientUpdateBuildResponseBuildTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": str,
        "SizeOnDisk": int,
        "OperatingSystem": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientUpdateBuildResponseBuildTypeDef(_ClientUpdateBuildResponseBuildTypeDef):
    """
    Type definition for `ClientUpdateBuildResponse` `Build`

    Object that contains the updated build record.

    - **BuildId** *(string) --*

      Unique identifier for a build.

    - **Name** *(string) --*

      Descriptive label that is associated with a build. Build names do not need to be unique. It
      can be set using  CreateBuild or  UpdateBuild .

    - **Version** *(string) --*

      Version that is associated with a build or script. Version strings do not need to be
      unique. This value can be set using  CreateBuild or  UpdateBuild .

    - **Status** *(string) --*

      Current status of the build.

      Possible build statuses include the following:

      * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You
      cannot create fleets for builds that are in this status. When a build is successfully
      created, the build status is set to this value.

      * **READY** -- The game build has been successfully uploaded. You can now create new fleets
      for this build.

      * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.

    - **SizeOnDisk** *(integer) --*

      File size of the uploaded game build, expressed in bytes. When the build status is
      ``INITIALIZED`` , this value is 0.

    - **OperatingSystem** *(string) --*

      Operating system that the game server binaries are built to run on. This value determines
      the type of fleet resources that you can use for this build.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").
    """


_ClientUpdateBuildResponseTypeDef = TypedDict(
    "_ClientUpdateBuildResponseTypeDef",
    {"Build": ClientUpdateBuildResponseBuildTypeDef},
    total=False,
)


class ClientUpdateBuildResponseTypeDef(_ClientUpdateBuildResponseTypeDef):
    """
    Type definition for `ClientUpdateBuild` `Response`

    Represents the returned data in response to a request action.

    - **Build** *(dict) --*

      Object that contains the updated build record.

      - **BuildId** *(string) --*

        Unique identifier for a build.

      - **Name** *(string) --*

        Descriptive label that is associated with a build. Build names do not need to be unique. It
        can be set using  CreateBuild or  UpdateBuild .

      - **Version** *(string) --*

        Version that is associated with a build or script. Version strings do not need to be
        unique. This value can be set using  CreateBuild or  UpdateBuild .

      - **Status** *(string) --*

        Current status of the build.

        Possible build statuses include the following:

        * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You
        cannot create fleets for builds that are in this status. When a build is successfully
        created, the build status is set to this value.

        * **READY** -- The game build has been successfully uploaded. You can now create new fleets
        for this build.

        * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.

      - **SizeOnDisk** *(integer) --*

        File size of the uploaded game build, expressed in bytes. When the build status is
        ``INITIALIZED`` , this value is 0.

      - **OperatingSystem** *(string) --*

        Operating system that the game server binaries are built to run on. This value determines
        the type of fleet resources that you can use for this build.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").
    """


_ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "_ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)


class ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef(
    _ClientUpdateFleetAttributesResourceCreationLimitPolicyTypeDef
):
    """
    Type definition for `ClientUpdateFleetAttributes` `ResourceCreationLimitPolicy`

    Policy that limits the number of game sessions an individual player can create over a span of
    time.

    - **NewGameSessionsPerCreator** *(integer) --*

      Maximum number of game sessions that an individual can create during the policy period.

    - **PolicyPeriodInMinutes** *(integer) --*

      Time span used in evaluating the resource creation limit policy.
    """


_ClientUpdateFleetAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateFleetAttributesResponseTypeDef", {"FleetId": str}, total=False
)


class ClientUpdateFleetAttributesResponseTypeDef(
    _ClientUpdateFleetAttributesResponseTypeDef
):
    """
    Type definition for `ClientUpdateFleetAttributes` `Response`

    Represents the returned data in response to a request action.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that was updated.
    """


_ClientUpdateFleetCapacityResponseTypeDef = TypedDict(
    "_ClientUpdateFleetCapacityResponseTypeDef", {"FleetId": str}, total=False
)


class ClientUpdateFleetCapacityResponseTypeDef(
    _ClientUpdateFleetCapacityResponseTypeDef
):
    """
    Type definition for `ClientUpdateFleetCapacity` `Response`

    Represents the returned data in response to a request action.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that was updated.
    """


_ClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef = TypedDict(
    "_ClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef",
    {"FromPort": int, "ToPort": int, "IpRange": str, "Protocol": str},
)


class ClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef(
    _ClientUpdateFleetPortSettingsInboundPermissionAuthorizationsTypeDef
):
    """
    Type definition for `ClientUpdateFleetPortSettings` `InboundPermissionAuthorizations`

    A range of IP addresses and port settings that allow inbound traffic to connect to server
    processes on an Amazon GameLift. New game sessions that are started on the fleet are assigned
    an IP address/port number combination, which must fall into the fleet's allowed ranges. For
    fleets created with a custom game server, the ranges reflect the server's game session
    assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges,
    one for TCP messaging and one for UDP for use by the Realtime servers.

    - **FromPort** *(integer) --* **[REQUIRED]**

      Starting value for a range of allowed port numbers.

    - **ToPort** *(integer) --* **[REQUIRED]**

      Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value
      must be higher than ``FromPort`` .

    - **IpRange** *(string) --* **[REQUIRED]**

      Range of allowed IP addresses. This value must be expressed in CIDR notation. Example:
      "``000.000.000.000/[subnet mask]`` " or optionally the shortened version "``0.0.0.0/[subnet
      mask]`` ".

    - **Protocol** *(string) --* **[REQUIRED]**

      Network communication protocol used by the fleet.
    """


_ClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef = TypedDict(
    "_ClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef",
    {"FromPort": int, "ToPort": int, "IpRange": str, "Protocol": str},
)


class ClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef(
    _ClientUpdateFleetPortSettingsInboundPermissionRevocationsTypeDef
):
    """
    Type definition for `ClientUpdateFleetPortSettings` `InboundPermissionRevocations`

    A range of IP addresses and port settings that allow inbound traffic to connect to server
    processes on an Amazon GameLift. New game sessions that are started on the fleet are assigned
    an IP address/port number combination, which must fall into the fleet's allowed ranges. For
    fleets created with a custom game server, the ranges reflect the server's game session
    assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges,
    one for TCP messaging and one for UDP for use by the Realtime servers.

    - **FromPort** *(integer) --* **[REQUIRED]**

      Starting value for a range of allowed port numbers.

    - **ToPort** *(integer) --* **[REQUIRED]**

      Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value
      must be higher than ``FromPort`` .

    - **IpRange** *(string) --* **[REQUIRED]**

      Range of allowed IP addresses. This value must be expressed in CIDR notation. Example:
      "``000.000.000.000/[subnet mask]`` " or optionally the shortened version "``0.0.0.0/[subnet
      mask]`` ".

    - **Protocol** *(string) --* **[REQUIRED]**

      Network communication protocol used by the fleet.
    """


_ClientUpdateFleetPortSettingsResponseTypeDef = TypedDict(
    "_ClientUpdateFleetPortSettingsResponseTypeDef", {"FleetId": str}, total=False
)


class ClientUpdateFleetPortSettingsResponseTypeDef(
    _ClientUpdateFleetPortSettingsResponseTypeDef
):
    """
    Type definition for `ClientUpdateFleetPortSettings` `Response`

    Represents the returned data in response to a request action.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that was updated.
    """


_ClientUpdateGameSessionQueueDestinationsTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueueDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)


class ClientUpdateGameSessionQueueDestinationsTypeDef(
    _ClientUpdateGameSessionQueueDestinationsTypeDef
):
    """
    Type definition for `ClientUpdateGameSessionQueue` `Destinations`

    Fleet designated in a game session queue. Requests for new game sessions in the queue are
    fulfilled by starting a new game session on any destination configured for a queue.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **DestinationArn** *(string) --*

      Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID
      or alias ID and a region name, provide a unique identifier across all regions.
    """


_ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef(
    _ClientUpdateGameSessionQueuePlayerLatencyPoliciesTypeDef
):
    """
    Type definition for `ClientUpdateGameSessionQueue` `PlayerLatencyPolicies`

    Queue setting that determines the highest latency allowed for individual players when placing a
    game session. When a latency policy is in force, a game session cannot be placed at any
    destination in a region where a player is reporting latency higher than the cap. Latency
    policies are only enforced when the placement request contains player latency information.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

      The maximum latency value that is allowed for any player, in milliseconds. All policies must
      have a value set for this property.

    - **PolicyDurationSeconds** *(integer) --*

      The length of time, in seconds, that the policy is enforced while placing a new game session.
      A null value for this property means that the policy is enforced until the queue times out.
    """


_ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)


class ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef(
    _ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef
):
    """
    Type definition for `ClientUpdateGameSessionQueueResponseGameSessionQueue` `Destinations`

    Fleet designated in a game session queue. Requests for new game sessions in the queue are
    fulfilled by starting a new game session on any destination configured for a queue.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **DestinationArn** *(string) --*

      Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
      fleet ID or alias ID and a region name, provide a unique identifier across all regions.
    """


_ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef(
    _ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef
):
    """
    Type definition for `ClientUpdateGameSessionQueueResponseGameSessionQueue` `PlayerLatencyPolicies`

    Queue setting that determines the highest latency allowed for individual players when
    placing a game session. When a latency policy is in force, a game session cannot be
    placed at any destination in a region where a player is reporting latency higher than the
    cap. Latency policies are only enforced when the placement request contains player
    latency information.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

      The maximum latency value that is allowed for any player, in milliseconds. All policies
      must have a value set for this property.

    - **PolicyDurationSeconds** *(integer) --*

      The length of time, in seconds, that the policy is enforced while placing a new game
      session. A null value for this property means that the policy is enforced until the
      queue times out.
    """


_ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List[
            ClientUpdateGameSessionQueueResponseGameSessionQueuePlayerLatencyPoliciesTypeDef
        ],
        "Destinations": List[
            ClientUpdateGameSessionQueueResponseGameSessionQueueDestinationsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef(
    _ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef
):
    """
    Type definition for `ClientUpdateGameSessionQueueResponse` `GameSessionQueue`

    Object that describes the newly updated game session queue.

    - **Name** *(string) --*

      Descriptive label that is associated with game session queue. Queue names must be unique
      within each region.

    - **GameSessionQueueArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned
      to a game session queue and uniquely identifies it. Format is
      ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` .

    - **TimeoutInSeconds** *(integer) --*

      Maximum time, in seconds, that a new game session placement request remains in the queue.
      When a request exceeds this time, the game session placement changes to a ``TIMED_OUT``
      status.

    - **PlayerLatencyPolicies** *(list) --*

      Collection of latency policies to apply when processing game sessions placement requests
      with player latency information. Multiple policies are evaluated in order of the maximum
      latency value, starting with the lowest latency values. With just one policy, it is
      enforced at the start of the game session placement for the duration period. With multiple
      policies, each policy is enforced consecutively for its duration period. For example, a
      queue might enforce a 60-second policy followed by a 120-second policy, and then no policy
      for the remainder of the placement.

      - *(dict) --*

        Queue setting that determines the highest latency allowed for individual players when
        placing a game session. When a latency policy is in force, a game session cannot be
        placed at any destination in a region where a player is reporting latency higher than the
        cap. Latency policies are only enforced when the placement request contains player
        latency information.

        *  CreateGameSessionQueue

        *  DescribeGameSessionQueues

        *  UpdateGameSessionQueue

        *  DeleteGameSessionQueue

        - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

          The maximum latency value that is allowed for any player, in milliseconds. All policies
          must have a value set for this property.

        - **PolicyDurationSeconds** *(integer) --*

          The length of time, in seconds, that the policy is enforced while placing a new game
          session. A null value for this property means that the policy is enforced until the
          queue times out.

    - **Destinations** *(list) --*

      List of fleets that can be used to fulfill game session placement requests in the queue.
      Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed
      in default preference order.

      - *(dict) --*

        Fleet designated in a game session queue. Requests for new game sessions in the queue are
        fulfilled by starting a new game session on any destination configured for a queue.

        *  CreateGameSessionQueue

        *  DescribeGameSessionQueues

        *  UpdateGameSessionQueue

        *  DeleteGameSessionQueue

        - **DestinationArn** *(string) --*

          Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
          fleet ID or alias ID and a region name, provide a unique identifier across all regions.
    """


_ClientUpdateGameSessionQueueResponseTypeDef = TypedDict(
    "_ClientUpdateGameSessionQueueResponseTypeDef",
    {"GameSessionQueue": ClientUpdateGameSessionQueueResponseGameSessionQueueTypeDef},
    total=False,
)


class ClientUpdateGameSessionQueueResponseTypeDef(
    _ClientUpdateGameSessionQueueResponseTypeDef
):
    """
    Type definition for `ClientUpdateGameSessionQueue` `Response`

    Represents the returned data in response to a request action.

    - **GameSessionQueue** *(dict) --*

      Object that describes the newly updated game session queue.

      - **Name** *(string) --*

        Descriptive label that is associated with game session queue. Queue names must be unique
        within each region.

      - **GameSessionQueueArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned
        to a game session queue and uniquely identifies it. Format is
        ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` .

      - **TimeoutInSeconds** *(integer) --*

        Maximum time, in seconds, that a new game session placement request remains in the queue.
        When a request exceeds this time, the game session placement changes to a ``TIMED_OUT``
        status.

      - **PlayerLatencyPolicies** *(list) --*

        Collection of latency policies to apply when processing game sessions placement requests
        with player latency information. Multiple policies are evaluated in order of the maximum
        latency value, starting with the lowest latency values. With just one policy, it is
        enforced at the start of the game session placement for the duration period. With multiple
        policies, each policy is enforced consecutively for its duration period. For example, a
        queue might enforce a 60-second policy followed by a 120-second policy, and then no policy
        for the remainder of the placement.

        - *(dict) --*

          Queue setting that determines the highest latency allowed for individual players when
          placing a game session. When a latency policy is in force, a game session cannot be
          placed at any destination in a region where a player is reporting latency higher than the
          cap. Latency policies are only enforced when the placement request contains player
          latency information.

          *  CreateGameSessionQueue

          *  DescribeGameSessionQueues

          *  UpdateGameSessionQueue

          *  DeleteGameSessionQueue

          - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

            The maximum latency value that is allowed for any player, in milliseconds. All policies
            must have a value set for this property.

          - **PolicyDurationSeconds** *(integer) --*

            The length of time, in seconds, that the policy is enforced while placing a new game
            session. A null value for this property means that the policy is enforced until the
            queue times out.

      - **Destinations** *(list) --*

        List of fleets that can be used to fulfill game session placement requests in the queue.
        Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed
        in default preference order.

        - *(dict) --*

          Fleet designated in a game session queue. Requests for new game sessions in the queue are
          fulfilled by starting a new game session on any destination configured for a queue.

          *  CreateGameSessionQueue

          *  DescribeGameSessionQueues

          *  UpdateGameSessionQueue

          *  DeleteGameSessionQueue

          - **DestinationArn** *(string) --*

            Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
            fleet ID or alias ID and a region name, provide a unique identifier across all regions.
    """


_ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef = TypedDict(
    "_ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef(
    _ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef
):
    """
    Type definition for `ClientUpdateGameSessionResponseGameSession` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a
    game session request, these properties communicate details to be used when setting up the
    new game session, such as to specify a game mode, level, or map. Game properties are
    passed to the game server process when initiating a new game session; the server process
    uses the properties as appropriate. For more information, see the `Amazon GameLift
    Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientUpdateGameSessionResponseGameSessionTypeDef = TypedDict(
    "_ClientUpdateGameSessionResponseGameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": str,
        "StatusReason": str,
        "GameProperties": List[
            ClientUpdateGameSessionResponseGameSessionGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": str,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class ClientUpdateGameSessionResponseGameSessionTypeDef(
    _ClientUpdateGameSessionResponseGameSessionTypeDef
):
    """
    Type definition for `ClientUpdateGameSessionResponse` `GameSession`

    Object that contains the updated game session metadata.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. A game session ARN has the following format:
      ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
      token>`` .

    - **Name** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to be
      unique.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **CurrentPlayerSessionCount** *(integer) --*

      Number of players currently in the game session.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **Status** *(string) --*

      Current status of the game session. A game session must have an ``ACTIVE`` status to have
      player sessions.

    - **StatusReason** *(string) --*

      Provides additional information about game session status. ``INTERRUPTED`` indicates that
      the game session was hosted on a spot instance that was reclaimed, causing the active game
      session to be terminated.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These properties
      are passed to a game server process in the  GameSession object with a request to start a
      new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). You can search for active game sessions based on this custom data with
      SearchGameSessions .

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in a
        game session request, these properties communicate details to be used when setting up the
        new game session, such as to specify a game mode, level, or map. Game properties are
        passed to the game server process when initiating a new game session; the server process
        uses the properties as appropriate. For more information, see the `Amazon GameLift
        Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **PlayerSessionCreationPolicy** *(string) --*

      Indicates whether or not the game session is accepting new players.

    - **CreatorId** *(string) --*

      Unique identifier for a player. This ID is used to enforce a resource protection policy (if
      one exists), that limits the number of game sessions a player can create.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information about the matchmaking process that was used to create the game session. It is
      in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
      contains data on all players assigned to the match, including player attributes and team
      assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      . Matchmaker data is useful when requesting match backfills, and is updated whenever new
      players are added during a successful backfill (see  StartMatchBackfill ).
    """


_ClientUpdateGameSessionResponseTypeDef = TypedDict(
    "_ClientUpdateGameSessionResponseTypeDef",
    {"GameSession": ClientUpdateGameSessionResponseGameSessionTypeDef},
    total=False,
)


class ClientUpdateGameSessionResponseTypeDef(_ClientUpdateGameSessionResponseTypeDef):
    """
    Type definition for `ClientUpdateGameSession` `Response`

    Represents the returned data in response to a request action.

    - **GameSession** *(dict) --*

      Object that contains the updated game session metadata.

      - **GameSessionId** *(string) --*

        Unique identifier for the game session. A game session ARN has the following format:
        ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
        token>`` .

      - **Name** *(string) --*

        Descriptive label that is associated with a game session. Session names do not need to be
        unique.

      - **FleetId** *(string) --*

        Unique identifier for a fleet that the game session is running on.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **TerminationTime** *(datetime) --*

        Time stamp indicating when this data object was terminated. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **CurrentPlayerSessionCount** *(integer) --*

        Number of players currently in the game session.

      - **MaximumPlayerSessionCount** *(integer) --*

        Maximum number of players that can be connected simultaneously to the game session.

      - **Status** *(string) --*

        Current status of the game session. A game session must have an ``ACTIVE`` status to have
        player sessions.

      - **StatusReason** *(string) --*

        Provides additional information about game session status. ``INTERRUPTED`` indicates that
        the game session was hosted on a spot instance that was reclaimed, causing the active game
        session to be terminated.

      - **GameProperties** *(list) --*

        Set of custom properties for a game session, formatted as key:value pairs. These properties
        are passed to a game server process in the  GameSession object with a request to start a
        new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ). You can search for active game sessions based on this custom data with
        SearchGameSessions .

        - *(dict) --*

          Set of key-value pairs that contain information about a game session. When included in a
          game session request, these properties communicate details to be used when setting up the
          new game session, such as to specify a game mode, level, or map. Game properties are
          passed to the game server process when initiating a new game session; the server process
          uses the properties as appropriate. For more information, see the `Amazon GameLift
          Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
          .

          - **Key** *(string) --*

            Game property identifier.

          - **Value** *(string) --*

            Game property value.

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number.

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift game server, an app needs
        both the IP address and port number.

      - **PlayerSessionCreationPolicy** *(string) --*

        Indicates whether or not the game session is accepting new players.

      - **CreatorId** *(string) --*

        Unique identifier for a player. This ID is used to enforce a resource protection policy (if
        one exists), that limits the number of game sessions a player can create.

      - **GameSessionData** *(string) --*

        Set of custom game session properties, formatted as a single string value. This data is
        passed to a game server process in the  GameSession object with a request to start a new
        game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ).

      - **MatchmakerData** *(string) --*

        Information about the matchmaking process that was used to create the game session. It is
        in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
        contains data on all players assigned to the match, including player attributes and team
        assignments. For more details on matchmaker data, see `Match Data
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
        . Matchmaker data is useful when requesting match backfills, and is updated whenever new
        players are added during a successful backfill (see  StartMatchBackfill ).
    """


_ClientUpdateMatchmakingConfigurationGamePropertiesTypeDef = TypedDict(
    "_ClientUpdateMatchmakingConfigurationGamePropertiesTypeDef",
    {"Key": str, "Value": str},
)


class ClientUpdateMatchmakingConfigurationGamePropertiesTypeDef(
    _ClientUpdateMatchmakingConfigurationGamePropertiesTypeDef
):
    """
    Type definition for `ClientUpdateMatchmakingConfiguration` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a game
    session request, these properties communicate details to be used when setting up the new game
    session, such as to specify a game mode, level, or map. Game properties are passed to the game
    server process when initiating a new game session; the server process uses the properties as
    appropriate. For more information, see the `Amazon GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --* **[REQUIRED]**

      Game property identifier.

    - **Value** *(string) --* **[REQUIRED]**

      Game property value.
    """


_ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef = TypedDict(
    "_ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef(
    _ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef
):
    """
    Type definition for `ClientUpdateMatchmakingConfigurationResponseConfiguration` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in a
    game session request, these properties communicate details to be used when setting up the
    new game session, such as to specify a game mode, level, or map. Game properties are
    passed to the game server process when initiating a new game session; the server process
    uses the properties as appropriate. For more information, see the `Amazon GameLift
    Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef = TypedDict(
    "_ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef",
    {
        "Name": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List[
            ClientUpdateMatchmakingConfigurationResponseConfigurationGamePropertiesTypeDef
        ],
        "GameSessionData": str,
        "BackfillMode": str,
    },
    total=False,
)


class ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef(
    _ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateMatchmakingConfigurationResponse` `Configuration`

    Object that describes the updated matchmaking configuration.

    - **Name** *(string) --*

      Unique identifier for a matchmaking configuration. This name is used to identify the
      configuration associated with a matchmaking request or ticket.

    - **Description** *(string) --*

      Descriptive label that is associated with matchmaking configuration.

    - **GameSessionQueueArns** *(list) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned
      to a game session queue and uniquely identifies it. Format is
      ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` . These queues
      are used when placing game sessions for matches that are created with this matchmaking
      configuration. Queues can be located in any region.

      - *(string) --*

    - **RequestTimeoutSeconds** *(integer) --*

      Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing
      out. Requests that fail due to timing out can be resubmitted as needed.

    - **AcceptanceTimeoutSeconds** *(integer) --*

      Length of time (in seconds) to wait for players to accept a proposed match. If any player
      rejects the match or fails to accept before the timeout, the ticket continues to look for
      an acceptable match.

    - **AcceptanceRequired** *(boolean) --*

      Flag that determines whether a match that was created with this configuration must be
      accepted by the matched players. To require acceptance, set to TRUE.

    - **RuleSetName** *(string) --*

      Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking
      configuration can only use rule sets that are defined in the same region.

    - **NotificationTarget** *(string) --*

      SNS topic ARN that is set up to receive matchmaking notifications.

    - **AdditionalPlayerCount** *(integer) --*

      Number of player slots in a match to keep open for future players. For example, if the
      configuration's rule set specifies a match for a single 12-person team, and the additional
      player count is set to 2, only 10 players are selected for the match.

    - **CustomEventData** *(string) --*

      Information to attach to all events related to the matchmaking configuration.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These properties
      are passed to a game server process in the  GameSession object with a request to start a
      new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). This information is added to the new  GameSession object that is created for a
      successful match.

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in a
        game session request, these properties communicate details to be used when setting up the
        new game session, such as to specify a game mode, level, or map. Game properties are
        passed to the game server process when initiating a new game session; the server process
        uses the properties as appropriate. For more information, see the `Amazon GameLift
        Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). This information is added to the new  GameSession object that is created for a
      successful match.

    - **BackfillMode** *(string) --*

      Method used to backfill game sessions created with this matchmaking configuration. MANUAL
      indicates that the game makes backfill requests or does not use the match backfill feature.
      AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever a game
      session has one or more open slots. Learn more about manual and automatic backfill in
      `Backfill Existing Games with FlexMatch
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-backfill.html>`__ .
    """


_ClientUpdateMatchmakingConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateMatchmakingConfigurationResponseTypeDef",
    {"Configuration": ClientUpdateMatchmakingConfigurationResponseConfigurationTypeDef},
    total=False,
)


class ClientUpdateMatchmakingConfigurationResponseTypeDef(
    _ClientUpdateMatchmakingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientUpdateMatchmakingConfiguration` `Response`

    Represents the returned data in response to a request action.

    - **Configuration** *(dict) --*

      Object that describes the updated matchmaking configuration.

      - **Name** *(string) --*

        Unique identifier for a matchmaking configuration. This name is used to identify the
        configuration associated with a matchmaking request or ticket.

      - **Description** *(string) --*

        Descriptive label that is associated with matchmaking configuration.

      - **GameSessionQueueArns** *(list) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is assigned
        to a game session queue and uniquely identifies it. Format is
        ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` . These queues
        are used when placing game sessions for matches that are created with this matchmaking
        configuration. Queues can be located in any region.

        - *(string) --*

      - **RequestTimeoutSeconds** *(integer) --*

        Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing
        out. Requests that fail due to timing out can be resubmitted as needed.

      - **AcceptanceTimeoutSeconds** *(integer) --*

        Length of time (in seconds) to wait for players to accept a proposed match. If any player
        rejects the match or fails to accept before the timeout, the ticket continues to look for
        an acceptable match.

      - **AcceptanceRequired** *(boolean) --*

        Flag that determines whether a match that was created with this configuration must be
        accepted by the matched players. To require acceptance, set to TRUE.

      - **RuleSetName** *(string) --*

        Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking
        configuration can only use rule sets that are defined in the same region.

      - **NotificationTarget** *(string) --*

        SNS topic ARN that is set up to receive matchmaking notifications.

      - **AdditionalPlayerCount** *(integer) --*

        Number of player slots in a match to keep open for future players. For example, if the
        configuration's rule set specifies a match for a single 12-person team, and the additional
        player count is set to 2, only 10 players are selected for the match.

      - **CustomEventData** *(string) --*

        Information to attach to all events related to the matchmaking configuration.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **GameProperties** *(list) --*

        Set of custom properties for a game session, formatted as key:value pairs. These properties
        are passed to a game server process in the  GameSession object with a request to start a
        new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ). This information is added to the new  GameSession object that is created for a
        successful match.

        - *(dict) --*

          Set of key-value pairs that contain information about a game session. When included in a
          game session request, these properties communicate details to be used when setting up the
          new game session, such as to specify a game mode, level, or map. Game properties are
          passed to the game server process when initiating a new game session; the server process
          uses the properties as appropriate. For more information, see the `Amazon GameLift
          Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
          .

          - **Key** *(string) --*

            Game property identifier.

          - **Value** *(string) --*

            Game property value.

      - **GameSessionData** *(string) --*

        Set of custom game session properties, formatted as a single string value. This data is
        passed to a game server process in the  GameSession object with a request to start a new
        game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ). This information is added to the new  GameSession object that is created for a
        successful match.

      - **BackfillMode** *(string) --*

        Method used to backfill game sessions created with this matchmaking configuration. MANUAL
        indicates that the game makes backfill requests or does not use the match backfill feature.
        AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever a game
        session has one or more open slots. Learn more about manual and automatic backfill in
        `Backfill Existing Games with FlexMatch
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-backfill.html>`__ .
    """


_ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef",
    {"LaunchPath": str, "Parameters": str, "ConcurrentExecutions": int},
    total=False,
)


class ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef(
    _ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef
):
    """
    Type definition for `ClientUpdateRuntimeConfigurationResponseRuntimeConfiguration` `ServerProcesses`

    A set of instructions for launching server processes on each instance in a fleet. Server
    processes run either a custom game build executable or a Realtime Servers script. Each
    instruction set identifies the location of the custom game build executable or Realtime
    launch script, optional launch parameters, and the number of server processes with this
    configuration to maintain concurrently on the instance. Server process configurations
    make up a fleet's ``  RuntimeConfiguration `` .

    - **LaunchPath** *(string) --*

      Location of the server executable in a custom game build or the name of the Realtime
      script file that contains the ``Init()`` function. Game builds and Realtime scripts are
      installed on instances at the root:

      * Windows (for custom game builds only): ``C:\\game`` . Example:
      "``C:\\game\\MyGame\\server.exe`` "

      * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
      "``/local/game/MyRealtimeScript.js`` "

    - **Parameters** *(string) --*

      Optional list of parameters to pass to the server executable or Realtime script on
      launch.

    - **ConcurrentExecutions** *(integer) --*

      Number of server processes using this configuration to run concurrently on an instance.
    """


_ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef = TypedDict(
    "_ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[
            ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationServerProcessesTypeDef
        ],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)


class ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef(
    _ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateRuntimeConfigurationResponse` `RuntimeConfiguration`

    The run-time configuration currently in force. If the update was successful, this object
    matches the one in the request.

    - **ServerProcesses** *(list) --*

      Collection of server process configurations that describe which server processes to run on
      each instance in a fleet.

      - *(dict) --*

        A set of instructions for launching server processes on each instance in a fleet. Server
        processes run either a custom game build executable or a Realtime Servers script. Each
        instruction set identifies the location of the custom game build executable or Realtime
        launch script, optional launch parameters, and the number of server processes with this
        configuration to maintain concurrently on the instance. Server process configurations
        make up a fleet's ``  RuntimeConfiguration `` .

        - **LaunchPath** *(string) --*

          Location of the server executable in a custom game build or the name of the Realtime
          script file that contains the ``Init()`` function. Game builds and Realtime scripts are
          installed on instances at the root:

          * Windows (for custom game builds only): ``C:\\game`` . Example:
          "``C:\\game\\MyGame\\server.exe`` "

          * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
          "``/local/game/MyRealtimeScript.js`` "

        - **Parameters** *(string) --*

          Optional list of parameters to pass to the server executable or Realtime script on
          launch.

        - **ConcurrentExecutions** *(integer) --*

          Number of server processes using this configuration to run concurrently on an instance.

    - **MaxConcurrentGameSessionActivations** *(integer) --*

      Maximum number of game sessions with status ``ACTIVATING`` to allow on an instance
      simultaneously. This setting limits the amount of instance resources that can be used for
      new game activations at any one time.

    - **GameSessionActivationTimeoutSeconds** *(integer) --*

      Maximum amount of time (in seconds) that a game session can remain in status ``ACTIVATING``
      . If the game session is not active before the timeout, activation is terminated and the
      game session status is changed to ``TERMINATED`` .
    """


_ClientUpdateRuntimeConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateRuntimeConfigurationResponseTypeDef",
    {
        "RuntimeConfiguration": ClientUpdateRuntimeConfigurationResponseRuntimeConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateRuntimeConfigurationResponseTypeDef(
    _ClientUpdateRuntimeConfigurationResponseTypeDef
):
    """
    Type definition for `ClientUpdateRuntimeConfiguration` `Response`

    Represents the returned data in response to a request action.

    - **RuntimeConfiguration** *(dict) --*

      The run-time configuration currently in force. If the update was successful, this object
      matches the one in the request.

      - **ServerProcesses** *(list) --*

        Collection of server process configurations that describe which server processes to run on
        each instance in a fleet.

        - *(dict) --*

          A set of instructions for launching server processes on each instance in a fleet. Server
          processes run either a custom game build executable or a Realtime Servers script. Each
          instruction set identifies the location of the custom game build executable or Realtime
          launch script, optional launch parameters, and the number of server processes with this
          configuration to maintain concurrently on the instance. Server process configurations
          make up a fleet's ``  RuntimeConfiguration `` .

          - **LaunchPath** *(string) --*

            Location of the server executable in a custom game build or the name of the Realtime
            script file that contains the ``Init()`` function. Game builds and Realtime scripts are
            installed on instances at the root:

            * Windows (for custom game builds only): ``C:\\game`` . Example:
            "``C:\\game\\MyGame\\server.exe`` "

            * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
            "``/local/game/MyRealtimeScript.js`` "

          - **Parameters** *(string) --*

            Optional list of parameters to pass to the server executable or Realtime script on
            launch.

          - **ConcurrentExecutions** *(integer) --*

            Number of server processes using this configuration to run concurrently on an instance.

      - **MaxConcurrentGameSessionActivations** *(integer) --*

        Maximum number of game sessions with status ``ACTIVATING`` to allow on an instance
        simultaneously. This setting limits the amount of instance resources that can be used for
        new game activations at any one time.

      - **GameSessionActivationTimeoutSeconds** *(integer) --*

        Maximum amount of time (in seconds) that a game session can remain in status ``ACTIVATING``
        . If the game session is not active before the timeout, activation is terminated and the
        game session status is changed to ``TERMINATED`` .
    """


_RequiredClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_RequiredClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef",
    {"LaunchPath": str, "ConcurrentExecutions": int},
)
_OptionalClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef = TypedDict(
    "_OptionalClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef",
    {"Parameters": str},
    total=False,
)


class ClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef(
    _RequiredClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef,
    _OptionalClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef,
):
    """
    Type definition for `ClientUpdateRuntimeConfigurationRuntimeConfiguration` `ServerProcesses`

    A set of instructions for launching server processes on each instance in a fleet. Server
    processes run either a custom game build executable or a Realtime Servers script. Each
    instruction set identifies the location of the custom game build executable or Realtime
    launch script, optional launch parameters, and the number of server processes with this
    configuration to maintain concurrently on the instance. Server process configurations make up
    a fleet's ``  RuntimeConfiguration `` .

    - **LaunchPath** *(string) --* **[REQUIRED]**

      Location of the server executable in a custom game build or the name of the Realtime script
      file that contains the ``Init()`` function. Game builds and Realtime scripts are installed
      on instances at the root:

      * Windows (for custom game builds only): ``C:\\game`` . Example:
      "``C:\\game\\MyGame\\server.exe`` "

      * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
      "``/local/game/MyRealtimeScript.js`` "

    - **Parameters** *(string) --*

      Optional list of parameters to pass to the server executable or Realtime script on launch.

    - **ConcurrentExecutions** *(integer) --* **[REQUIRED]**

      Number of server processes using this configuration to run concurrently on an instance.
    """


_ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef = TypedDict(
    "_ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[
            ClientUpdateRuntimeConfigurationRuntimeConfigurationServerProcessesTypeDef
        ],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)


class ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef(
    _ClientUpdateRuntimeConfigurationRuntimeConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateRuntimeConfiguration` `RuntimeConfiguration`

    Instructions for launching server processes on each instance in the fleet. Server processes run
    either a custom game build executable or a Realtime Servers script. The run-time configuration
    lists the types of server processes to run on an instance and includes the following
    configuration settings: the server executable or launch script file, launch parameters, and the
    number of processes to run concurrently on each instance. A CreateFleet request must include a
    run-time configuration with at least one server process configuration.

    - **ServerProcesses** *(list) --*

      Collection of server process configurations that describe which server processes to run on each
      instance in a fleet.

      - *(dict) --*

        A set of instructions for launching server processes on each instance in a fleet. Server
        processes run either a custom game build executable or a Realtime Servers script. Each
        instruction set identifies the location of the custom game build executable or Realtime
        launch script, optional launch parameters, and the number of server processes with this
        configuration to maintain concurrently on the instance. Server process configurations make up
        a fleet's ``  RuntimeConfiguration `` .

        - **LaunchPath** *(string) --* **[REQUIRED]**

          Location of the server executable in a custom game build or the name of the Realtime script
          file that contains the ``Init()`` function. Game builds and Realtime scripts are installed
          on instances at the root:

          * Windows (for custom game builds only): ``C:\\game`` . Example:
          "``C:\\game\\MyGame\\server.exe`` "

          * Linux: ``/local/game`` . Examples: "``/local/game/MyGame/server.exe`` " or
          "``/local/game/MyRealtimeScript.js`` "

        - **Parameters** *(string) --*

          Optional list of parameters to pass to the server executable or Realtime script on launch.

        - **ConcurrentExecutions** *(integer) --* **[REQUIRED]**

          Number of server processes using this configuration to run concurrently on an instance.

    - **MaxConcurrentGameSessionActivations** *(integer) --*

      Maximum number of game sessions with status ``ACTIVATING`` to allow on an instance
      simultaneously. This setting limits the amount of instance resources that can be used for new
      game activations at any one time.

    - **GameSessionActivationTimeoutSeconds** *(integer) --*

      Maximum amount of time (in seconds) that a game session can remain in status ``ACTIVATING`` .
      If the game session is not active before the timeout, activation is terminated and the game
      session status is changed to ``TERMINATED`` .
    """


_ClientUpdateScriptResponseScriptStorageLocationTypeDef = TypedDict(
    "_ClientUpdateScriptResponseScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientUpdateScriptResponseScriptStorageLocationTypeDef(
    _ClientUpdateScriptResponseScriptStorageLocationTypeDef
):
    """
    Type definition for `ClientUpdateScriptResponseScript` `StorageLocation`

    Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
    stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
    CreateScript , and  UpdateScript requests.

    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.

    - **Key** *(string) --*

      Name of the zip file containing the build files or script files.

    - **RoleArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
      that allows Amazon GameLift to access the S3 bucket.

    - **ObjectVersion** *(string) --*

      Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
      uses this information when retrieving files from an S3 bucket that you own. Use this
      parameter to specify a specific version of the file; if not set, the latest version of
      the file is retrieved.
    """


_ClientUpdateScriptResponseScriptTypeDef = TypedDict(
    "_ClientUpdateScriptResponseScriptTypeDef",
    {
        "ScriptId": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": ClientUpdateScriptResponseScriptStorageLocationTypeDef,
    },
    total=False,
)


class ClientUpdateScriptResponseScriptTypeDef(_ClientUpdateScriptResponseScriptTypeDef):
    """
    Type definition for `ClientUpdateScriptResponse` `Script`

    The newly created script record with a unique script ID. The new script's storage location
    reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your
    account, the storage location reflects the information that was provided in the
    *CreateScript* request; (2) If the script file was uploaded from a local zip file, the
    storage location reflects an S3 location controls by the Amazon GameLift service.

    - **ScriptId** *(string) --*

      Unique identifier for a Realtime script

    - **Name** *(string) --*

      Descriptive label that is associated with a script. Script names do not need to be unique.

    - **Version** *(string) --*

      Version that is associated with a build or script. Version strings do not need to be unique.

    - **SizeOnDisk** *(integer) --*

      File size of the uploaded Realtime script, expressed in bytes. When files are uploaded from
      an S3 location, this value remains at "0".

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **StorageLocation** *(dict) --*

      Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
      stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
      CreateScript , and  UpdateScript requests.

      - **Bucket** *(string) --*

        Amazon S3 bucket identifier. This is the name of the S3 bucket.

      - **Key** *(string) --*

        Name of the zip file containing the build files or script files.

      - **RoleArn** *(string) --*

        Amazon Resource Name (`ARN
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
        that allows Amazon GameLift to access the S3 bucket.

      - **ObjectVersion** *(string) --*

        Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
        uses this information when retrieving files from an S3 bucket that you own. Use this
        parameter to specify a specific version of the file; if not set, the latest version of
        the file is retrieved.
    """


_ClientUpdateScriptResponseTypeDef = TypedDict(
    "_ClientUpdateScriptResponseTypeDef",
    {"Script": ClientUpdateScriptResponseScriptTypeDef},
    total=False,
)


class ClientUpdateScriptResponseTypeDef(_ClientUpdateScriptResponseTypeDef):
    """
    Type definition for `ClientUpdateScript` `Response`

    - **Script** *(dict) --*

      The newly created script record with a unique script ID. The new script's storage location
      reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your
      account, the storage location reflects the information that was provided in the
      *CreateScript* request; (2) If the script file was uploaded from a local zip file, the
      storage location reflects an S3 location controls by the Amazon GameLift service.

      - **ScriptId** *(string) --*

        Unique identifier for a Realtime script

      - **Name** *(string) --*

        Descriptive label that is associated with a script. Script names do not need to be unique.

      - **Version** *(string) --*

        Version that is associated with a build or script. Version strings do not need to be unique.

      - **SizeOnDisk** *(integer) --*

        File size of the uploaded Realtime script, expressed in bytes. When files are uploaded from
        an S3 location, this value remains at "0".

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed in
        Unix time as milliseconds (for example "1469498468.057").

      - **StorageLocation** *(dict) --*

        Location in Amazon Simple Storage Service (Amazon S3) where build or script files are
        stored for access by Amazon GameLift. This location is specified in  CreateBuild ,
        CreateScript , and  UpdateScript requests.

        - **Bucket** *(string) --*

          Amazon S3 bucket identifier. This is the name of the S3 bucket.

        - **Key** *(string) --*

          Name of the zip file containing the build files or script files.

        - **RoleArn** *(string) --*

          Amazon Resource Name (`ARN
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role
          that allows Amazon GameLift to access the S3 bucket.

        - **ObjectVersion** *(string) --*

          Version of the file, if object versioning is turned on for the bucket. Amazon GameLift
          uses this information when retrieving files from an S3 bucket that you own. Use this
          parameter to specify a specific version of the file; if not set, the latest version of
          the file is retrieved.
    """


_ClientUpdateScriptStorageLocationTypeDef = TypedDict(
    "_ClientUpdateScriptStorageLocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)


class ClientUpdateScriptStorageLocationTypeDef(
    _ClientUpdateScriptStorageLocationTypeDef
):
    """
    Type definition for `ClientUpdateScript` `StorageLocation`

    Location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored.
    The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a
    role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must
    be in the same region where you want to create a new script. By default, Amazon GameLift uploads
    the latest version of the zip file; if you have S3 object versioning turned on, you can use the
    ``ObjectVersion`` parameter to specify an earlier version.

    - **Bucket** *(string) --*

      Amazon S3 bucket identifier. This is the name of the S3 bucket.

    - **Key** *(string) --*

      Name of the zip file containing the build files or script files.

    - **RoleArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) for an IAM role that
      allows Amazon GameLift to access the S3 bucket.

    - **ObjectVersion** *(string) --*

      Version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses
      this information when retrieving files from an S3 bucket that you own. Use this parameter to
      specify a specific version of the file; if not set, the latest version of the file is retrieved.
    """


_ClientValidateMatchmakingRuleSetResponseTypeDef = TypedDict(
    "_ClientValidateMatchmakingRuleSetResponseTypeDef", {"Valid": bool}, total=False
)


class ClientValidateMatchmakingRuleSetResponseTypeDef(
    _ClientValidateMatchmakingRuleSetResponseTypeDef
):
    """
    Type definition for `ClientValidateMatchmakingRuleSet` `Response`

    Represents the returned data in response to a request action.

    - **Valid** *(boolean) --*

      Response indicating whether the rule set is valid.
    """


_DescribeFleetAttributesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFleetAttributesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFleetAttributesPaginatePaginationConfigTypeDef(
    _DescribeFleetAttributesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeFleetAttributesPaginate` `PaginationConfig`

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


_DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef = TypedDict(
    "_DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef",
    {"CertificateType": str},
    total=False,
)


class DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef(
    _DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef
):
    """
    Type definition for `DescribeFleetAttributesPaginateResponseFleetAttributes` `CertificateConfiguration`

    - **CertificateType** *(string) --*
    """


_DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef = TypedDict(
    "_DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)


class DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef(
    _DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef
):
    """
    Type definition for `DescribeFleetAttributesPaginateResponseFleetAttributes` `ResourceCreationLimitPolicy`

    Fleet policy to limit the number of game sessions an individual player can create over a
    span of time.

    - **NewGameSessionsPerCreator** *(integer) --*

      Maximum number of game sessions that an individual can create during the policy period.

    - **PolicyPeriodInMinutes** *(integer) --*

      Time span used in evaluating the resource creation limit policy.
    """


_DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef = TypedDict(
    "_DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "FleetType": str,
        "InstanceType": str,
        "Description": str,
        "Name": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": str,
        "BuildId": str,
        "ScriptId": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "NewGameSessionProtectionPolicy": str,
        "OperatingSystem": str,
        "ResourceCreationLimitPolicy": DescribeFleetAttributesPaginateResponseFleetAttributesResourceCreationLimitPolicyTypeDef,
        "MetricGroups": List[str],
        "StoppedActions": List[str],
        "InstanceRoleArn": str,
        "CertificateConfiguration": DescribeFleetAttributesPaginateResponseFleetAttributesCertificateConfigurationTypeDef,
    },
    total=False,
)


class DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef(
    _DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef
):
    """
    Type definition for `DescribeFleetAttributesPaginateResponse` `FleetAttributes`

    General properties describing a fleet.

    *  CreateFleet

    *  ListFleets

    *  DeleteFleet

    * Describe fleets:

      *  DescribeFleetAttributes

      *  DescribeFleetCapacity

      *  DescribeFleetPortSettings

      *  DescribeFleetUtilization

      *  DescribeRuntimeConfiguration

      *  DescribeEC2InstanceLimits

      *  DescribeFleetEvents

    * Update fleets:

      *  UpdateFleetAttributes

      *  UpdateFleetCapacity

      *  UpdateFleetPortSettings

      *  UpdateRuntimeConfiguration

    * Manage fleet actions:

      *  StartFleetActions

      *  StopFleetActions

    - **FleetId** *(string) --*

      Unique identifier for a fleet.

    - **FleetArn** *(string) --*

      Identifier for a fleet that is unique across all regions.

    - **FleetType** *(string) --*

      Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may
      be interrupted with a two-minute notification.

    - **InstanceType** *(string) --*

      EC2 instance type indicating the computing resources of each instance in the fleet,
      including CPU, memory, storage, and networking capacity. See `Amazon EC2 Instance Types
      <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.

    - **Description** *(string) --*

      Human-readable description of the fleet.

    - **Name** *(string) --*

      Descriptive label that is associated with a fleet. Fleet names do not need to be unique.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **Status** *(string) --*

      Current status of the fleet.

      Possible fleet statuses include the following:

      * **NEW** -- A new fleet has been defined and desired instances is set to 1.

      * **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** -- Amazon GameLift is setting up the new
      fleet, creating new instances with the game build or Realtime script and starting server
      processes.

      * **ACTIVE** -- Hosts can now accept game sessions.

      * **ERROR** -- An error occurred when downloading, validating, building, or activating
      the fleet.

      * **DELETING** -- Hosts are responding to a delete fleet request.

      * **TERMINATED** -- The fleet no longer exists.

    - **BuildId** *(string) --*

      Unique identifier for a build.

    - **ScriptId** *(string) --*

      Unique identifier for a Realtime script.

    - **ServerLaunchPath** *(string) --*

      Path to a game server executable in the fleet's build, specified for fleets created
      before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after
      this date are specified in the fleet's  RuntimeConfiguration .

    - **ServerLaunchParameters** *(string) --*

      Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK
      v. 0.12.16). Server launch parameters for fleets created after this date are specified in
      the fleet's  RuntimeConfiguration .

    - **LogPaths** *(list) --*

      Location of default log files. When a server process is shut down, Amazon GameLift
      captures and stores any log files in this location. These logs are in addition to game
      session logs; see more on game session logs in the `Amazon GameLift Developer Guide
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-api-server-code>`__
      . If no default log path for a fleet is specified, Amazon GameLift automatically uploads
      logs that are stored on each instance at ``C:\\game\\logs`` (for Windows) or
      ``/local/game/logs`` (for Linux). Use the Amazon GameLift console to access stored logs.

      - *(string) --*

    - **NewGameSessionProtectionPolicy** *(string) --*

      Type of game session protection to set for all new instances started in the fleet.

      * **NoProtection** -- The game session can be terminated during a scale-down event.

      * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be
      terminated during a scale-down event.

    - **OperatingSystem** *(string) --*

      Operating system of the fleet's computing resources. A fleet's operating system depends
      on the OS specified for the build that is deployed on this fleet.

    - **ResourceCreationLimitPolicy** *(dict) --*

      Fleet policy to limit the number of game sessions an individual player can create over a
      span of time.

      - **NewGameSessionsPerCreator** *(integer) --*

        Maximum number of game sessions that an individual can create during the policy period.

      - **PolicyPeriodInMinutes** *(integer) --*

        Time span used in evaluating the resource creation limit policy.

    - **MetricGroups** *(list) --*

      Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view
      metrics for an individual fleet or aggregated metrics for fleets that are in a fleet
      metric group. A fleet can be included in only one metric group at a time.

      - *(string) --*

    - **StoppedActions** *(list) --*

      List of fleet actions that have been suspended using  StopFleetActions . This includes
      auto-scaling.

      - *(string) --*

    - **InstanceRoleArn** *(string) --*

      Unique identifier for an AWS IAM role that manages access to your AWS services. With an
      instance role ARN set, any application that runs on an instance in this fleet can assume
      the role, including install scripts, server processes, daemons (background processes).
      Create a role or look up a role's ARN using the `IAM dashboard
      <https://console.aws.amazon.com/iam/>`__ in the AWS Management Console. Learn more about
      using on-box credentials for your game servers at `Access external resources from a game
      server
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`__
      .

    - **CertificateConfiguration** *(dict) --*

      - **CertificateType** *(string) --*
    """


_DescribeFleetAttributesPaginateResponseTypeDef = TypedDict(
    "_DescribeFleetAttributesPaginateResponseTypeDef",
    {
        "FleetAttributes": List[
            DescribeFleetAttributesPaginateResponseFleetAttributesTypeDef
        ]
    },
    total=False,
)


class DescribeFleetAttributesPaginateResponseTypeDef(
    _DescribeFleetAttributesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeFleetAttributesPaginate` `Response`

    Represents the returned data in response to a request action.

    - **FleetAttributes** *(list) --*

      Collection of objects containing attribute metadata for each requested fleet ID.

      - *(dict) --*

        General properties describing a fleet.

        *  CreateFleet

        *  ListFleets

        *  DeleteFleet

        * Describe fleets:

          *  DescribeFleetAttributes

          *  DescribeFleetCapacity

          *  DescribeFleetPortSettings

          *  DescribeFleetUtilization

          *  DescribeRuntimeConfiguration

          *  DescribeEC2InstanceLimits

          *  DescribeFleetEvents

        * Update fleets:

          *  UpdateFleetAttributes

          *  UpdateFleetCapacity

          *  UpdateFleetPortSettings

          *  UpdateRuntimeConfiguration

        * Manage fleet actions:

          *  StartFleetActions

          *  StopFleetActions

        - **FleetId** *(string) --*

          Unique identifier for a fleet.

        - **FleetArn** *(string) --*

          Identifier for a fleet that is unique across all regions.

        - **FleetType** *(string) --*

          Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may
          be interrupted with a two-minute notification.

        - **InstanceType** *(string) --*

          EC2 instance type indicating the computing resources of each instance in the fleet,
          including CPU, memory, storage, and networking capacity. See `Amazon EC2 Instance Types
          <http://aws.amazon.com/ec2/instance-types/>`__ for detailed descriptions.

        - **Description** *(string) --*

          Human-readable description of the fleet.

        - **Name** *(string) --*

          Descriptive label that is associated with a fleet. Fleet names do not need to be unique.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **TerminationTime** *(datetime) --*

          Time stamp indicating when this data object was terminated. Format is a number expressed
          in Unix time as milliseconds (for example "1469498468.057").

        - **Status** *(string) --*

          Current status of the fleet.

          Possible fleet statuses include the following:

          * **NEW** -- A new fleet has been defined and desired instances is set to 1.

          * **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** -- Amazon GameLift is setting up the new
          fleet, creating new instances with the game build or Realtime script and starting server
          processes.

          * **ACTIVE** -- Hosts can now accept game sessions.

          * **ERROR** -- An error occurred when downloading, validating, building, or activating
          the fleet.

          * **DELETING** -- Hosts are responding to a delete fleet request.

          * **TERMINATED** -- The fleet no longer exists.

        - **BuildId** *(string) --*

          Unique identifier for a build.

        - **ScriptId** *(string) --*

          Unique identifier for a Realtime script.

        - **ServerLaunchPath** *(string) --*

          Path to a game server executable in the fleet's build, specified for fleets created
          before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after
          this date are specified in the fleet's  RuntimeConfiguration .

        - **ServerLaunchParameters** *(string) --*

          Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK
          v. 0.12.16). Server launch parameters for fleets created after this date are specified in
          the fleet's  RuntimeConfiguration .

        - **LogPaths** *(list) --*

          Location of default log files. When a server process is shut down, Amazon GameLift
          captures and stores any log files in this location. These logs are in addition to game
          session logs; see more on game session logs in the `Amazon GameLift Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-api-server-code>`__
          . If no default log path for a fleet is specified, Amazon GameLift automatically uploads
          logs that are stored on each instance at ``C:\\game\\logs`` (for Windows) or
          ``/local/game/logs`` (for Linux). Use the Amazon GameLift console to access stored logs.

          - *(string) --*

        - **NewGameSessionProtectionPolicy** *(string) --*

          Type of game session protection to set for all new instances started in the fleet.

          * **NoProtection** -- The game session can be terminated during a scale-down event.

          * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be
          terminated during a scale-down event.

        - **OperatingSystem** *(string) --*

          Operating system of the fleet's computing resources. A fleet's operating system depends
          on the OS specified for the build that is deployed on this fleet.

        - **ResourceCreationLimitPolicy** *(dict) --*

          Fleet policy to limit the number of game sessions an individual player can create over a
          span of time.

          - **NewGameSessionsPerCreator** *(integer) --*

            Maximum number of game sessions that an individual can create during the policy period.

          - **PolicyPeriodInMinutes** *(integer) --*

            Time span used in evaluating the resource creation limit policy.

        - **MetricGroups** *(list) --*

          Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view
          metrics for an individual fleet or aggregated metrics for fleets that are in a fleet
          metric group. A fleet can be included in only one metric group at a time.

          - *(string) --*

        - **StoppedActions** *(list) --*

          List of fleet actions that have been suspended using  StopFleetActions . This includes
          auto-scaling.

          - *(string) --*

        - **InstanceRoleArn** *(string) --*

          Unique identifier for an AWS IAM role that manages access to your AWS services. With an
          instance role ARN set, any application that runs on an instance in this fleet can assume
          the role, including install scripts, server processes, daemons (background processes).
          Create a role or look up a role's ARN using the `IAM dashboard
          <https://console.aws.amazon.com/iam/>`__ in the AWS Management Console. Learn more about
          using on-box credentials for your game servers at `Access external resources from a game
          server
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`__
          .

        - **CertificateConfiguration** *(dict) --*

          - **CertificateType** *(string) --*
    """


_DescribeFleetCapacityPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFleetCapacityPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFleetCapacityPaginatePaginationConfigTypeDef(
    _DescribeFleetCapacityPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeFleetCapacityPaginate` `PaginationConfig`

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


_DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef = TypedDict(
    "_DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef",
    {
        "DESIRED": int,
        "MINIMUM": int,
        "MAXIMUM": int,
        "PENDING": int,
        "ACTIVE": int,
        "IDLE": int,
        "TERMINATING": int,
    },
    total=False,
)


class DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef(
    _DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef
):
    """
    Type definition for `DescribeFleetCapacityPaginateResponseFleetCapacity` `InstanceCounts`

    Current status of fleet capacity.

    - **DESIRED** *(integer) --*

      Ideal number of active instances in the fleet.

    - **MINIMUM** *(integer) --*

      Minimum value allowed for the fleet's instance count.

    - **MAXIMUM** *(integer) --*

      Maximum value allowed for the fleet's instance count.

    - **PENDING** *(integer) --*

      Number of instances in the fleet that are starting but not yet active.

    - **ACTIVE** *(integer) --*

      Actual number of active instances in the fleet.

    - **IDLE** *(integer) --*

      Number of active instances in the fleet that are not currently hosting a game session.

    - **TERMINATING** *(integer) --*

      Number of instances in the fleet that are no longer active but haven't yet been
      terminated.
    """


_DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef = TypedDict(
    "_DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef",
    {
        "FleetId": str,
        "InstanceType": str,
        "InstanceCounts": DescribeFleetCapacityPaginateResponseFleetCapacityInstanceCountsTypeDef,
    },
    total=False,
)


class DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef(
    _DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef
):
    """
    Type definition for `DescribeFleetCapacityPaginateResponse` `FleetCapacity`

    Information about the fleet's capacity. Fleet capacity is measured in EC2 instances. By
    default, new fleets have a capacity of one instance, but can be updated as needed. The
    maximum number of instances for a fleet is determined by the fleet's instance type.

    *  CreateFleet

    *  ListFleets

    *  DeleteFleet

    * Describe fleets:

      *  DescribeFleetAttributes

      *  DescribeFleetCapacity

      *  DescribeFleetPortSettings

      *  DescribeFleetUtilization

      *  DescribeRuntimeConfiguration

      *  DescribeEC2InstanceLimits

      *  DescribeFleetEvents

    * Update fleets:

      *  UpdateFleetAttributes

      *  UpdateFleetCapacity

      *  UpdateFleetPortSettings

      *  UpdateRuntimeConfiguration

    * Manage fleet actions:

      *  StartFleetActions

      *  StopFleetActions

    - **FleetId** *(string) --*

      Unique identifier for a fleet.

    - **InstanceType** *(string) --*

      Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type
      determines the computing resources of each instance in the fleet, including CPU, memory,
      storage, and networking capacity. Amazon GameLift supports the following EC2 instance
      types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for
      detailed descriptions.

    - **InstanceCounts** *(dict) --*

      Current status of fleet capacity.

      - **DESIRED** *(integer) --*

        Ideal number of active instances in the fleet.

      - **MINIMUM** *(integer) --*

        Minimum value allowed for the fleet's instance count.

      - **MAXIMUM** *(integer) --*

        Maximum value allowed for the fleet's instance count.

      - **PENDING** *(integer) --*

        Number of instances in the fleet that are starting but not yet active.

      - **ACTIVE** *(integer) --*

        Actual number of active instances in the fleet.

      - **IDLE** *(integer) --*

        Number of active instances in the fleet that are not currently hosting a game session.

      - **TERMINATING** *(integer) --*

        Number of instances in the fleet that are no longer active but haven't yet been
        terminated.
    """


_DescribeFleetCapacityPaginateResponseTypeDef = TypedDict(
    "_DescribeFleetCapacityPaginateResponseTypeDef",
    {"FleetCapacity": List[DescribeFleetCapacityPaginateResponseFleetCapacityTypeDef]},
    total=False,
)


class DescribeFleetCapacityPaginateResponseTypeDef(
    _DescribeFleetCapacityPaginateResponseTypeDef
):
    """
    Type definition for `DescribeFleetCapacityPaginate` `Response`

    Represents the returned data in response to a request action.

    - **FleetCapacity** *(list) --*

      Collection of objects containing capacity information for each requested fleet ID. Leave this
      parameter empty to retrieve capacity information for all fleets.

      - *(dict) --*

        Information about the fleet's capacity. Fleet capacity is measured in EC2 instances. By
        default, new fleets have a capacity of one instance, but can be updated as needed. The
        maximum number of instances for a fleet is determined by the fleet's instance type.

        *  CreateFleet

        *  ListFleets

        *  DeleteFleet

        * Describe fleets:

          *  DescribeFleetAttributes

          *  DescribeFleetCapacity

          *  DescribeFleetPortSettings

          *  DescribeFleetUtilization

          *  DescribeRuntimeConfiguration

          *  DescribeEC2InstanceLimits

          *  DescribeFleetEvents

        * Update fleets:

          *  UpdateFleetAttributes

          *  UpdateFleetCapacity

          *  UpdateFleetPortSettings

          *  UpdateRuntimeConfiguration

        * Manage fleet actions:

          *  StartFleetActions

          *  StopFleetActions

        - **FleetId** *(string) --*

          Unique identifier for a fleet.

        - **InstanceType** *(string) --*

          Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type
          determines the computing resources of each instance in the fleet, including CPU, memory,
          storage, and networking capacity. Amazon GameLift supports the following EC2 instance
          types. See `Amazon EC2 Instance Types <http://aws.amazon.com/ec2/instance-types/>`__ for
          detailed descriptions.

        - **InstanceCounts** *(dict) --*

          Current status of fleet capacity.

          - **DESIRED** *(integer) --*

            Ideal number of active instances in the fleet.

          - **MINIMUM** *(integer) --*

            Minimum value allowed for the fleet's instance count.

          - **MAXIMUM** *(integer) --*

            Maximum value allowed for the fleet's instance count.

          - **PENDING** *(integer) --*

            Number of instances in the fleet that are starting but not yet active.

          - **ACTIVE** *(integer) --*

            Actual number of active instances in the fleet.

          - **IDLE** *(integer) --*

            Number of active instances in the fleet that are not currently hosting a game session.

          - **TERMINATING** *(integer) --*

            Number of instances in the fleet that are no longer active but haven't yet been
            terminated.
    """


_DescribeFleetEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFleetEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFleetEventsPaginatePaginationConfigTypeDef(
    _DescribeFleetEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeFleetEventsPaginate` `PaginationConfig`

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


_DescribeFleetUtilizationPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeFleetUtilizationPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeFleetUtilizationPaginatePaginationConfigTypeDef(
    _DescribeFleetUtilizationPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeFleetUtilizationPaginate` `PaginationConfig`

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


_DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef = TypedDict(
    "_DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef",
    {
        "FleetId": str,
        "ActiveServerProcessCount": int,
        "ActiveGameSessionCount": int,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
    },
    total=False,
)


class DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef(
    _DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef
):
    """
    Type definition for `DescribeFleetUtilizationPaginateResponse` `FleetUtilization`

    Current status of fleet utilization, including the number of game and player sessions being
    hosted.

    *  CreateFleet

    *  ListFleets

    *  DeleteFleet

    * Describe fleets:

      *  DescribeFleetAttributes

      *  DescribeFleetCapacity

      *  DescribeFleetPortSettings

      *  DescribeFleetUtilization

      *  DescribeRuntimeConfiguration

      *  DescribeEC2InstanceLimits

      *  DescribeFleetEvents

    * Update fleets:

      *  UpdateFleetAttributes

      *  UpdateFleetCapacity

      *  UpdateFleetPortSettings

      *  UpdateRuntimeConfiguration

    * Manage fleet actions:

      *  StartFleetActions

      *  StopFleetActions

    - **FleetId** *(string) --*

      Unique identifier for a fleet.

    - **ActiveServerProcessCount** *(integer) --*

      Number of server processes in an ``ACTIVE`` status currently running across all instances
      in the fleet

    - **ActiveGameSessionCount** *(integer) --*

      Number of active game sessions currently being hosted on all instances in the fleet.

    - **CurrentPlayerSessionCount** *(integer) --*

      Number of active player sessions currently being hosted on all instances in the fleet.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum players allowed across all game sessions currently being hosted on all instances
      in the fleet.
    """


_DescribeFleetUtilizationPaginateResponseTypeDef = TypedDict(
    "_DescribeFleetUtilizationPaginateResponseTypeDef",
    {
        "FleetUtilization": List[
            DescribeFleetUtilizationPaginateResponseFleetUtilizationTypeDef
        ]
    },
    total=False,
)


class DescribeFleetUtilizationPaginateResponseTypeDef(
    _DescribeFleetUtilizationPaginateResponseTypeDef
):
    """
    Type definition for `DescribeFleetUtilizationPaginate` `Response`

    Represents the returned data in response to a request action.

    - **FleetUtilization** *(list) --*

      Collection of objects containing utilization information for each requested fleet ID.

      - *(dict) --*

        Current status of fleet utilization, including the number of game and player sessions being
        hosted.

        *  CreateFleet

        *  ListFleets

        *  DeleteFleet

        * Describe fleets:

          *  DescribeFleetAttributes

          *  DescribeFleetCapacity

          *  DescribeFleetPortSettings

          *  DescribeFleetUtilization

          *  DescribeRuntimeConfiguration

          *  DescribeEC2InstanceLimits

          *  DescribeFleetEvents

        * Update fleets:

          *  UpdateFleetAttributes

          *  UpdateFleetCapacity

          *  UpdateFleetPortSettings

          *  UpdateRuntimeConfiguration

        * Manage fleet actions:

          *  StartFleetActions

          *  StopFleetActions

        - **FleetId** *(string) --*

          Unique identifier for a fleet.

        - **ActiveServerProcessCount** *(integer) --*

          Number of server processes in an ``ACTIVE`` status currently running across all instances
          in the fleet

        - **ActiveGameSessionCount** *(integer) --*

          Number of active game sessions currently being hosted on all instances in the fleet.

        - **CurrentPlayerSessionCount** *(integer) --*

          Number of active player sessions currently being hosted on all instances in the fleet.

        - **MaximumPlayerSessionCount** *(integer) --*

          Maximum players allowed across all game sessions currently being hosted on all instances
          in the fleet.
    """


_DescribeGameSessionDetailsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeGameSessionDetailsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeGameSessionDetailsPaginatePaginationConfigTypeDef(
    _DescribeGameSessionDetailsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeGameSessionDetailsPaginate` `PaginationConfig`

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


_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef = TypedDict(
    "_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef(
    _DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef
):
    """
    Type definition for `DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSession` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included
    in a game session request, these properties communicate details to be used when
    setting up the new game session, such as to specify a game mode, level, or map. Game
    properties are passed to the game server process when initiating a new game session;
    the server process uses the properties as appropriate. For more information, see the
    `Amazon GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef = TypedDict(
    "_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": str,
        "StatusReason": str,
        "GameProperties": List[
            DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": str,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef(
    _DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef
):
    """
    Type definition for `DescribeGameSessionDetailsPaginateResponseGameSessionDetails` `GameSession`

    Object that describes a game session.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. A game session ARN has the following format:
      ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
      token>`` .

    - **Name** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to
      be unique.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number
      expressed in Unix time as milliseconds (for example "1469498468.057").

    - **CurrentPlayerSessionCount** *(integer) --*

      Number of players currently in the game session.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **Status** *(string) --*

      Current status of the game session. A game session must have an ``ACTIVE`` status to
      have player sessions.

    - **StatusReason** *(string) --*

      Provides additional information about game session status. ``INTERRUPTED`` indicates
      that the game session was hosted on a spot instance that was reclaimed, causing the
      active game session to be terminated.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These
      properties are passed to a game server process in the  GameSession object with a
      request to start a new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). You can search for active game sessions based on this custom data with
      SearchGameSessions .

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included
        in a game session request, these properties communicate details to be used when
        setting up the new game session, such as to specify a game mode, level, or map. Game
        properties are passed to the game server process when initiating a new game session;
        the server process uses the properties as appropriate. For more information, see the
        `Amazon GameLift Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **PlayerSessionCreationPolicy** *(string) --*

      Indicates whether or not the game session is accepting new players.

    - **CreatorId** *(string) --*

      Unique identifier for a player. This ID is used to enforce a resource protection policy
      (if one exists), that limits the number of game sessions a player can create.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a
      new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information about the matchmaking process that was used to create the game session. It
      is in JSON syntax, formatted as a string. In addition the matchmaking configuration
      used, it contains data on all players assigned to the match, including player
      attributes and team assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      . Matchmaker data is useful when requesting match backfills, and is updated whenever
      new players are added during a successful backfill (see  StartMatchBackfill ).
    """


_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef = TypedDict(
    "_DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef",
    {
        "GameSession": DescribeGameSessionDetailsPaginateResponseGameSessionDetailsGameSessionTypeDef,
        "ProtectionPolicy": str,
    },
    total=False,
)


class DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef(
    _DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef
):
    """
    Type definition for `DescribeGameSessionDetailsPaginateResponse` `GameSessionDetails`

    A game session's properties plus the protection policy currently in force.

    - **GameSession** *(dict) --*

      Object that describes a game session.

      - **GameSessionId** *(string) --*

        Unique identifier for the game session. A game session ARN has the following format:
        ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
        token>`` .

      - **Name** *(string) --*

        Descriptive label that is associated with a game session. Session names do not need to
        be unique.

      - **FleetId** *(string) --*

        Unique identifier for a fleet that the game session is running on.

      - **CreationTime** *(datetime) --*

        Time stamp indicating when this data object was created. Format is a number expressed
        in Unix time as milliseconds (for example "1469498468.057").

      - **TerminationTime** *(datetime) --*

        Time stamp indicating when this data object was terminated. Format is a number
        expressed in Unix time as milliseconds (for example "1469498468.057").

      - **CurrentPlayerSessionCount** *(integer) --*

        Number of players currently in the game session.

      - **MaximumPlayerSessionCount** *(integer) --*

        Maximum number of players that can be connected simultaneously to the game session.

      - **Status** *(string) --*

        Current status of the game session. A game session must have an ``ACTIVE`` status to
        have player sessions.

      - **StatusReason** *(string) --*

        Provides additional information about game session status. ``INTERRUPTED`` indicates
        that the game session was hosted on a spot instance that was reclaimed, causing the
        active game session to be terminated.

      - **GameProperties** *(list) --*

        Set of custom properties for a game session, formatted as key:value pairs. These
        properties are passed to a game server process in the  GameSession object with a
        request to start a new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ). You can search for active game sessions based on this custom data with
        SearchGameSessions .

        - *(dict) --*

          Set of key-value pairs that contain information about a game session. When included
          in a game session request, these properties communicate details to be used when
          setting up the new game session, such as to specify a game mode, level, or map. Game
          properties are passed to the game server process when initiating a new game session;
          the server process uses the properties as appropriate. For more information, see the
          `Amazon GameLift Developer Guide
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
          .

          - **Key** *(string) --*

            Game property identifier.

          - **Value** *(string) --*

            Game property value.

      - **IpAddress** *(string) --*

        IP address of the game session. To connect to a Amazon GameLift game server, an app
        needs both the IP address and port number.

      - **DnsName** *(string) --*

      - **Port** *(integer) --*

        Port number for the game session. To connect to a Amazon GameLift game server, an app
        needs both the IP address and port number.

      - **PlayerSessionCreationPolicy** *(string) --*

        Indicates whether or not the game session is accepting new players.

      - **CreatorId** *(string) --*

        Unique identifier for a player. This ID is used to enforce a resource protection policy
        (if one exists), that limits the number of game sessions a player can create.

      - **GameSessionData** *(string) --*

        Set of custom game session properties, formatted as a single string value. This data is
        passed to a game server process in the  GameSession object with a request to start a
        new game session (see `Start a Game Session
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
        ).

      - **MatchmakerData** *(string) --*

        Information about the matchmaking process that was used to create the game session. It
        is in JSON syntax, formatted as a string. In addition the matchmaking configuration
        used, it contains data on all players assigned to the match, including player
        attributes and team assignments. For more details on matchmaker data, see `Match Data
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
        . Matchmaker data is useful when requesting match backfills, and is updated whenever
        new players are added during a successful backfill (see  StartMatchBackfill ).

    - **ProtectionPolicy** *(string) --*

      Current status of protection for the game session.

      * **NoProtection** -- The game session can be terminated during a scale-down event.

      * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be
      terminated during a scale-down event.
    """


_DescribeGameSessionDetailsPaginateResponseTypeDef = TypedDict(
    "_DescribeGameSessionDetailsPaginateResponseTypeDef",
    {
        "GameSessionDetails": List[
            DescribeGameSessionDetailsPaginateResponseGameSessionDetailsTypeDef
        ]
    },
    total=False,
)


class DescribeGameSessionDetailsPaginateResponseTypeDef(
    _DescribeGameSessionDetailsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeGameSessionDetailsPaginate` `Response`

    Represents the returned data in response to a request action.

    - **GameSessionDetails** *(list) --*

      Collection of objects containing game session properties and the protection policy currently
      in force for each session matching the request.

      - *(dict) --*

        A game session's properties plus the protection policy currently in force.

        - **GameSession** *(dict) --*

          Object that describes a game session.

          - **GameSessionId** *(string) --*

            Unique identifier for the game session. A game session ARN has the following format:
            ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
            token>`` .

          - **Name** *(string) --*

            Descriptive label that is associated with a game session. Session names do not need to
            be unique.

          - **FleetId** *(string) --*

            Unique identifier for a fleet that the game session is running on.

          - **CreationTime** *(datetime) --*

            Time stamp indicating when this data object was created. Format is a number expressed
            in Unix time as milliseconds (for example "1469498468.057").

          - **TerminationTime** *(datetime) --*

            Time stamp indicating when this data object was terminated. Format is a number
            expressed in Unix time as milliseconds (for example "1469498468.057").

          - **CurrentPlayerSessionCount** *(integer) --*

            Number of players currently in the game session.

          - **MaximumPlayerSessionCount** *(integer) --*

            Maximum number of players that can be connected simultaneously to the game session.

          - **Status** *(string) --*

            Current status of the game session. A game session must have an ``ACTIVE`` status to
            have player sessions.

          - **StatusReason** *(string) --*

            Provides additional information about game session status. ``INTERRUPTED`` indicates
            that the game session was hosted on a spot instance that was reclaimed, causing the
            active game session to be terminated.

          - **GameProperties** *(list) --*

            Set of custom properties for a game session, formatted as key:value pairs. These
            properties are passed to a game server process in the  GameSession object with a
            request to start a new game session (see `Start a Game Session
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
            ). You can search for active game sessions based on this custom data with
            SearchGameSessions .

            - *(dict) --*

              Set of key-value pairs that contain information about a game session. When included
              in a game session request, these properties communicate details to be used when
              setting up the new game session, such as to specify a game mode, level, or map. Game
              properties are passed to the game server process when initiating a new game session;
              the server process uses the properties as appropriate. For more information, see the
              `Amazon GameLift Developer Guide
              <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
              .

              - **Key** *(string) --*

                Game property identifier.

              - **Value** *(string) --*

                Game property value.

          - **IpAddress** *(string) --*

            IP address of the game session. To connect to a Amazon GameLift game server, an app
            needs both the IP address and port number.

          - **DnsName** *(string) --*

          - **Port** *(integer) --*

            Port number for the game session. To connect to a Amazon GameLift game server, an app
            needs both the IP address and port number.

          - **PlayerSessionCreationPolicy** *(string) --*

            Indicates whether or not the game session is accepting new players.

          - **CreatorId** *(string) --*

            Unique identifier for a player. This ID is used to enforce a resource protection policy
            (if one exists), that limits the number of game sessions a player can create.

          - **GameSessionData** *(string) --*

            Set of custom game session properties, formatted as a single string value. This data is
            passed to a game server process in the  GameSession object with a request to start a
            new game session (see `Start a Game Session
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
            ).

          - **MatchmakerData** *(string) --*

            Information about the matchmaking process that was used to create the game session. It
            is in JSON syntax, formatted as a string. In addition the matchmaking configuration
            used, it contains data on all players assigned to the match, including player
            attributes and team assignments. For more details on matchmaker data, see `Match Data
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
            . Matchmaker data is useful when requesting match backfills, and is updated whenever
            new players are added during a successful backfill (see  StartMatchBackfill ).

        - **ProtectionPolicy** *(string) --*

          Current status of protection for the game session.

          * **NoProtection** -- The game session can be terminated during a scale-down event.

          * **FullProtection** -- If the game session is in an ``ACTIVE`` status, it cannot be
          terminated during a scale-down event.
    """


_DescribeGameSessionQueuesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeGameSessionQueuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeGameSessionQueuesPaginatePaginationConfigTypeDef(
    _DescribeGameSessionQueuesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeGameSessionQueuesPaginate` `PaginationConfig`

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


_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef = TypedDict(
    "_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef",
    {"DestinationArn": str},
    total=False,
)


class DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef(
    _DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef
):
    """
    Type definition for `DescribeGameSessionQueuesPaginateResponseGameSessionQueues` `Destinations`

    Fleet designated in a game session queue. Requests for new game sessions in the queue
    are fulfilled by starting a new game session on any destination configured for a queue.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **DestinationArn** *(string) --*

      Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
      fleet ID or alias ID and a region name, provide a unique identifier across all
      regions.
    """


_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef = TypedDict(
    "_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)


class DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef(
    _DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef
):
    """
    Type definition for `DescribeGameSessionQueuesPaginateResponseGameSessionQueues` `PlayerLatencyPolicies`

    Queue setting that determines the highest latency allowed for individual players when
    placing a game session. When a latency policy is in force, a game session cannot be
    placed at any destination in a region where a player is reporting latency higher than
    the cap. Latency policies are only enforced when the placement request contains player
    latency information.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

      The maximum latency value that is allowed for any player, in milliseconds. All
      policies must have a value set for this property.

    - **PolicyDurationSeconds** *(integer) --*

      The length of time, in seconds, that the policy is enforced while placing a new game
      session. A null value for this property means that the policy is enforced until the
      queue times out.
    """


_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef = TypedDict(
    "_DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List[
            DescribeGameSessionQueuesPaginateResponseGameSessionQueuesPlayerLatencyPoliciesTypeDef
        ],
        "Destinations": List[
            DescribeGameSessionQueuesPaginateResponseGameSessionQueuesDestinationsTypeDef
        ],
    },
    total=False,
)


class DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef(
    _DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef
):
    """
    Type definition for `DescribeGameSessionQueuesPaginateResponse` `GameSessionQueues`

    Configuration of a queue that is used to process game session placement requests. The queue
    configuration identifies several game features:

    * The destinations where a new game session can potentially be hosted. Amazon GameLift
    tries these destinations in an order based on either the queue's default order or player
    latency information, if provided in a placement request. With latency information, Amazon
    GameLift can place game sessions where the majority of players are reporting the lowest
    possible latency.

    * The length of time that placement requests can wait in the queue before timing out.

    * A set of optional latency policies that protect individual players from high latencies,
    preventing game sessions from being placed where any individual player is reporting latency
    higher than a policy's maximum.

    *  CreateGameSessionQueue

    *  DescribeGameSessionQueues

    *  UpdateGameSessionQueue

    *  DeleteGameSessionQueue

    - **Name** *(string) --*

      Descriptive label that is associated with game session queue. Queue names must be unique
      within each region.

    - **GameSessionQueueArn** *(string) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
      assigned to a game session queue and uniquely identifies it. Format is
      ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` .

    - **TimeoutInSeconds** *(integer) --*

      Maximum time, in seconds, that a new game session placement request remains in the queue.
      When a request exceeds this time, the game session placement changes to a ``TIMED_OUT``
      status.

    - **PlayerLatencyPolicies** *(list) --*

      Collection of latency policies to apply when processing game sessions placement requests
      with player latency information. Multiple policies are evaluated in order of the maximum
      latency value, starting with the lowest latency values. With just one policy, it is
      enforced at the start of the game session placement for the duration period. With
      multiple policies, each policy is enforced consecutively for its duration period. For
      example, a queue might enforce a 60-second policy followed by a 120-second policy, and
      then no policy for the remainder of the placement.

      - *(dict) --*

        Queue setting that determines the highest latency allowed for individual players when
        placing a game session. When a latency policy is in force, a game session cannot be
        placed at any destination in a region where a player is reporting latency higher than
        the cap. Latency policies are only enforced when the placement request contains player
        latency information.

        *  CreateGameSessionQueue

        *  DescribeGameSessionQueues

        *  UpdateGameSessionQueue

        *  DeleteGameSessionQueue

        - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

          The maximum latency value that is allowed for any player, in milliseconds. All
          policies must have a value set for this property.

        - **PolicyDurationSeconds** *(integer) --*

          The length of time, in seconds, that the policy is enforced while placing a new game
          session. A null value for this property means that the policy is enforced until the
          queue times out.

    - **Destinations** *(list) --*

      List of fleets that can be used to fulfill game session placement requests in the queue.
      Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed
      in default preference order.

      - *(dict) --*

        Fleet designated in a game session queue. Requests for new game sessions in the queue
        are fulfilled by starting a new game session on any destination configured for a queue.

        *  CreateGameSessionQueue

        *  DescribeGameSessionQueues

        *  UpdateGameSessionQueue

        *  DeleteGameSessionQueue

        - **DestinationArn** *(string) --*

          Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
          fleet ID or alias ID and a region name, provide a unique identifier across all
          regions.
    """


_DescribeGameSessionQueuesPaginateResponseTypeDef = TypedDict(
    "_DescribeGameSessionQueuesPaginateResponseTypeDef",
    {
        "GameSessionQueues": List[
            DescribeGameSessionQueuesPaginateResponseGameSessionQueuesTypeDef
        ]
    },
    total=False,
)


class DescribeGameSessionQueuesPaginateResponseTypeDef(
    _DescribeGameSessionQueuesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeGameSessionQueuesPaginate` `Response`

    Represents the returned data in response to a request action.

    - **GameSessionQueues** *(list) --*

      Collection of objects that describes the requested game session queues.

      - *(dict) --*

        Configuration of a queue that is used to process game session placement requests. The queue
        configuration identifies several game features:

        * The destinations where a new game session can potentially be hosted. Amazon GameLift
        tries these destinations in an order based on either the queue's default order or player
        latency information, if provided in a placement request. With latency information, Amazon
        GameLift can place game sessions where the majority of players are reporting the lowest
        possible latency.

        * The length of time that placement requests can wait in the queue before timing out.

        * A set of optional latency policies that protect individual players from high latencies,
        preventing game sessions from being placed where any individual player is reporting latency
        higher than a policy's maximum.

        *  CreateGameSessionQueue

        *  DescribeGameSessionQueues

        *  UpdateGameSessionQueue

        *  DeleteGameSessionQueue

        - **Name** *(string) --*

          Descriptive label that is associated with game session queue. Queue names must be unique
          within each region.

        - **GameSessionQueueArn** *(string) --*

          Amazon Resource Name (`ARN
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
          assigned to a game session queue and uniquely identifies it. Format is
          ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` .

        - **TimeoutInSeconds** *(integer) --*

          Maximum time, in seconds, that a new game session placement request remains in the queue.
          When a request exceeds this time, the game session placement changes to a ``TIMED_OUT``
          status.

        - **PlayerLatencyPolicies** *(list) --*

          Collection of latency policies to apply when processing game sessions placement requests
          with player latency information. Multiple policies are evaluated in order of the maximum
          latency value, starting with the lowest latency values. With just one policy, it is
          enforced at the start of the game session placement for the duration period. With
          multiple policies, each policy is enforced consecutively for its duration period. For
          example, a queue might enforce a 60-second policy followed by a 120-second policy, and
          then no policy for the remainder of the placement.

          - *(dict) --*

            Queue setting that determines the highest latency allowed for individual players when
            placing a game session. When a latency policy is in force, a game session cannot be
            placed at any destination in a region where a player is reporting latency higher than
            the cap. Latency policies are only enforced when the placement request contains player
            latency information.

            *  CreateGameSessionQueue

            *  DescribeGameSessionQueues

            *  UpdateGameSessionQueue

            *  DeleteGameSessionQueue

            - **MaximumIndividualPlayerLatencyMilliseconds** *(integer) --*

              The maximum latency value that is allowed for any player, in milliseconds. All
              policies must have a value set for this property.

            - **PolicyDurationSeconds** *(integer) --*

              The length of time, in seconds, that the policy is enforced while placing a new game
              session. A null value for this property means that the policy is enforced until the
              queue times out.

        - **Destinations** *(list) --*

          List of fleets that can be used to fulfill game session placement requests in the queue.
          Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed
          in default preference order.

          - *(dict) --*

            Fleet designated in a game session queue. Requests for new game sessions in the queue
            are fulfilled by starting a new game session on any destination configured for a queue.

            *  CreateGameSessionQueue

            *  DescribeGameSessionQueues

            *  UpdateGameSessionQueue

            *  DeleteGameSessionQueue

            - **DestinationArn** *(string) --*

              Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a
              fleet ID or alias ID and a region name, provide a unique identifier across all
              regions.
    """


_DescribeGameSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeGameSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeGameSessionsPaginatePaginationConfigTypeDef(
    _DescribeGameSessionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeGameSessionsPaginate` `PaginationConfig`

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


_DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "_DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef(
    _DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef
):
    """
    Type definition for `DescribeGameSessionsPaginateResponseGameSessions` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in
    a game session request, these properties communicate details to be used when setting up
    the new game session, such as to specify a game mode, level, or map. Game properties
    are passed to the game server process when initiating a new game session; the server
    process uses the properties as appropriate. For more information, see the `Amazon
    GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_DescribeGameSessionsPaginateResponseGameSessionsTypeDef = TypedDict(
    "_DescribeGameSessionsPaginateResponseGameSessionsTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": str,
        "StatusReason": str,
        "GameProperties": List[
            DescribeGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": str,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class DescribeGameSessionsPaginateResponseGameSessionsTypeDef(
    _DescribeGameSessionsPaginateResponseGameSessionsTypeDef
):
    """
    Type definition for `DescribeGameSessionsPaginateResponse` `GameSessions`

    Properties describing a game session.

    A game session in ACTIVE status can host players. When a game session ends, its status is
    set to ``TERMINATED`` .

    Once the session ends, the game session object is retained for 30 days. This means you can
    reuse idempotency token values after this time. Game session logs are retained for 14 days.

    *  CreateGameSession

    *  DescribeGameSessions

    *  DescribeGameSessionDetails

    *  SearchGameSessions

    *  UpdateGameSession

    *  GetGameSessionLogUrl

    * Game session placements

      *  StartGameSessionPlacement

      *  DescribeGameSessionPlacement

      *  StopGameSessionPlacement

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. A game session ARN has the following format:
      ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
      token>`` .

    - **Name** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to be
      unique.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **CurrentPlayerSessionCount** *(integer) --*

      Number of players currently in the game session.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **Status** *(string) --*

      Current status of the game session. A game session must have an ``ACTIVE`` status to have
      player sessions.

    - **StatusReason** *(string) --*

      Provides additional information about game session status. ``INTERRUPTED`` indicates that
      the game session was hosted on a spot instance that was reclaimed, causing the active
      game session to be terminated.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These
      properties are passed to a game server process in the  GameSession object with a request
      to start a new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). You can search for active game sessions based on this custom data with
      SearchGameSessions .

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in
        a game session request, these properties communicate details to be used when setting up
        the new game session, such as to specify a game mode, level, or map. Game properties
        are passed to the game server process when initiating a new game session; the server
        process uses the properties as appropriate. For more information, see the `Amazon
        GameLift Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **PlayerSessionCreationPolicy** *(string) --*

      Indicates whether or not the game session is accepting new players.

    - **CreatorId** *(string) --*

      Unique identifier for a player. This ID is used to enforce a resource protection policy
      (if one exists), that limits the number of game sessions a player can create.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information about the matchmaking process that was used to create the game session. It is
      in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
      contains data on all players assigned to the match, including player attributes and team
      assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      . Matchmaker data is useful when requesting match backfills, and is updated whenever new
      players are added during a successful backfill (see  StartMatchBackfill ).
    """


_DescribeGameSessionsPaginateResponseTypeDef = TypedDict(
    "_DescribeGameSessionsPaginateResponseTypeDef",
    {"GameSessions": List[DescribeGameSessionsPaginateResponseGameSessionsTypeDef]},
    total=False,
)


class DescribeGameSessionsPaginateResponseTypeDef(
    _DescribeGameSessionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeGameSessionsPaginate` `Response`

    Represents the returned data in response to a request action.

    - **GameSessions** *(list) --*

      Collection of objects containing game session properties for each session matching the
      request.

      - *(dict) --*

        Properties describing a game session.

        A game session in ACTIVE status can host players. When a game session ends, its status is
        set to ``TERMINATED`` .

        Once the session ends, the game session object is retained for 30 days. This means you can
        reuse idempotency token values after this time. Game session logs are retained for 14 days.

        *  CreateGameSession

        *  DescribeGameSessions

        *  DescribeGameSessionDetails

        *  SearchGameSessions

        *  UpdateGameSession

        *  GetGameSessionLogUrl

        * Game session placements

          *  StartGameSessionPlacement

          *  DescribeGameSessionPlacement

          *  StopGameSessionPlacement

        - **GameSessionId** *(string) --*

          Unique identifier for the game session. A game session ARN has the following format:
          ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
          token>`` .

        - **Name** *(string) --*

          Descriptive label that is associated with a game session. Session names do not need to be
          unique.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the game session is running on.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **TerminationTime** *(datetime) --*

          Time stamp indicating when this data object was terminated. Format is a number expressed
          in Unix time as milliseconds (for example "1469498468.057").

        - **CurrentPlayerSessionCount** *(integer) --*

          Number of players currently in the game session.

        - **MaximumPlayerSessionCount** *(integer) --*

          Maximum number of players that can be connected simultaneously to the game session.

        - **Status** *(string) --*

          Current status of the game session. A game session must have an ``ACTIVE`` status to have
          player sessions.

        - **StatusReason** *(string) --*

          Provides additional information about game session status. ``INTERRUPTED`` indicates that
          the game session was hosted on a spot instance that was reclaimed, causing the active
          game session to be terminated.

        - **GameProperties** *(list) --*

          Set of custom properties for a game session, formatted as key:value pairs. These
          properties are passed to a game server process in the  GameSession object with a request
          to start a new game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ). You can search for active game sessions based on this custom data with
          SearchGameSessions .

          - *(dict) --*

            Set of key-value pairs that contain information about a game session. When included in
            a game session request, these properties communicate details to be used when setting up
            the new game session, such as to specify a game mode, level, or map. Game properties
            are passed to the game server process when initiating a new game session; the server
            process uses the properties as appropriate. For more information, see the `Amazon
            GameLift Developer Guide
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
            .

            - **Key** *(string) --*

              Game property identifier.

            - **Value** *(string) --*

              Game property value.

        - **IpAddress** *(string) --*

          IP address of the game session. To connect to a Amazon GameLift game server, an app needs
          both the IP address and port number.

        - **DnsName** *(string) --*

        - **Port** *(integer) --*

          Port number for the game session. To connect to a Amazon GameLift game server, an app
          needs both the IP address and port number.

        - **PlayerSessionCreationPolicy** *(string) --*

          Indicates whether or not the game session is accepting new players.

        - **CreatorId** *(string) --*

          Unique identifier for a player. This ID is used to enforce a resource protection policy
          (if one exists), that limits the number of game sessions a player can create.

        - **GameSessionData** *(string) --*

          Set of custom game session properties, formatted as a single string value. This data is
          passed to a game server process in the  GameSession object with a request to start a new
          game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ).

        - **MatchmakerData** *(string) --*

          Information about the matchmaking process that was used to create the game session. It is
          in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
          contains data on all players assigned to the match, including player attributes and team
          assignments. For more details on matchmaker data, see `Match Data
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
          . Matchmaker data is useful when requesting match backfills, and is updated whenever new
          players are added during a successful backfill (see  StartMatchBackfill ).
    """


_DescribeInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeInstancesPaginatePaginationConfigTypeDef(
    _DescribeInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeInstancesPaginate` `PaginationConfig`

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


_DescribeInstancesPaginateResponseInstancesTypeDef = TypedDict(
    "_DescribeInstancesPaginateResponseInstancesTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "DnsName": str,
        "OperatingSystem": str,
        "Type": str,
        "Status": str,
        "CreationTime": datetime,
    },
    total=False,
)


class DescribeInstancesPaginateResponseInstancesTypeDef(
    _DescribeInstancesPaginateResponseInstancesTypeDef
):
    """
    Type definition for `DescribeInstancesPaginateResponse` `Instances`

    Properties that describe an instance of a virtual computing resource that hosts one or more
    game servers. A fleet may contain zero or more instances.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the instance is in.

    - **InstanceId** *(string) --*

      Unique identifier for an instance.

    - **IpAddress** *(string) --*

      IP address assigned to the instance.

    - **DnsName** *(string) --*

    - **OperatingSystem** *(string) --*

      Operating system that is running on this instance.

    - **Type** *(string) --*

      EC2 instance type that defines the computing resources of this instance.

    - **Status** *(string) --*

      Current status of the instance. Possible statuses include the following:

      * **PENDING** -- The instance is in the process of being created and launching server
      processes as defined in the fleet's run-time configuration.

      * **ACTIVE** -- The instance has been successfully created and at least one server
      process has successfully launched and reported back to Amazon GameLift that it is ready
      to host a game session. The instance is now considered ready to host game sessions.

      * **TERMINATING** -- The instance is in the process of shutting down. This may happen to
      reduce capacity during a scaling down event or to recycle resources in the event of a
      problem.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").
    """


_DescribeInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeInstancesPaginateResponseTypeDef",
    {"Instances": List[DescribeInstancesPaginateResponseInstancesTypeDef]},
    total=False,
)


class DescribeInstancesPaginateResponseTypeDef(
    _DescribeInstancesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeInstancesPaginate` `Response`

    Represents the returned data in response to a request action.

    - **Instances** *(list) --*

      Collection of objects containing properties for each instance returned.

      - *(dict) --*

        Properties that describe an instance of a virtual computing resource that hosts one or more
        game servers. A fleet may contain zero or more instances.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the instance is in.

        - **InstanceId** *(string) --*

          Unique identifier for an instance.

        - **IpAddress** *(string) --*

          IP address assigned to the instance.

        - **DnsName** *(string) --*

        - **OperatingSystem** *(string) --*

          Operating system that is running on this instance.

        - **Type** *(string) --*

          EC2 instance type that defines the computing resources of this instance.

        - **Status** *(string) --*

          Current status of the instance. Possible statuses include the following:

          * **PENDING** -- The instance is in the process of being created and launching server
          processes as defined in the fleet's run-time configuration.

          * **ACTIVE** -- The instance has been successfully created and at least one server
          process has successfully launched and reported back to Amazon GameLift that it is ready
          to host a game session. The instance is now considered ready to host game sessions.

          * **TERMINATING** -- The instance is in the process of shutting down. This may happen to
          reduce capacity during a scaling down event or to recycle resources in the event of a
          problem.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").
    """


_DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeMatchmakingConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeMatchmakingConfigurationsPaginate` `PaginationConfig`

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


_DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef = TypedDict(
    "_DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef(
    _DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef
):
    """
    Type definition for `DescribeMatchmakingConfigurationsPaginateResponseConfigurations` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in
    a game session request, these properties communicate details to be used when setting up
    the new game session, such as to specify a game mode, level, or map. Game properties
    are passed to the game server process when initiating a new game session; the server
    process uses the properties as appropriate. For more information, see the `Amazon
    GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef = TypedDict(
    "_DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef",
    {
        "Name": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List[
            DescribeMatchmakingConfigurationsPaginateResponseConfigurationsGamePropertiesTypeDef
        ],
        "GameSessionData": str,
        "BackfillMode": str,
    },
    total=False,
)


class DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef(
    _DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef
):
    """
    Type definition for `DescribeMatchmakingConfigurationsPaginateResponse` `Configurations`

    Guidelines for use with FlexMatch to match players into games. All matchmaking requests
    must specify a matchmaking configuration.

    - **Name** *(string) --*

      Unique identifier for a matchmaking configuration. This name is used to identify the
      configuration associated with a matchmaking request or ticket.

    - **Description** *(string) --*

      Descriptive label that is associated with matchmaking configuration.

    - **GameSessionQueueArns** *(list) --*

      Amazon Resource Name (`ARN
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
      assigned to a game session queue and uniquely identifies it. Format is
      ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` . These queues
      are used when placing game sessions for matches that are created with this matchmaking
      configuration. Queues can be located in any region.

      - *(string) --*

    - **RequestTimeoutSeconds** *(integer) --*

      Maximum duration, in seconds, that a matchmaking ticket can remain in process before
      timing out. Requests that fail due to timing out can be resubmitted as needed.

    - **AcceptanceTimeoutSeconds** *(integer) --*

      Length of time (in seconds) to wait for players to accept a proposed match. If any player
      rejects the match or fails to accept before the timeout, the ticket continues to look for
      an acceptable match.

    - **AcceptanceRequired** *(boolean) --*

      Flag that determines whether a match that was created with this configuration must be
      accepted by the matched players. To require acceptance, set to TRUE.

    - **RuleSetName** *(string) --*

      Unique identifier for a matchmaking rule set to use with this configuration. A
      matchmaking configuration can only use rule sets that are defined in the same region.

    - **NotificationTarget** *(string) --*

      SNS topic ARN that is set up to receive matchmaking notifications.

    - **AdditionalPlayerCount** *(integer) --*

      Number of player slots in a match to keep open for future players. For example, if the
      configuration's rule set specifies a match for a single 12-person team, and the
      additional player count is set to 2, only 10 players are selected for the match.

    - **CustomEventData** *(string) --*

      Information to attach to all events related to the matchmaking configuration.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These
      properties are passed to a game server process in the  GameSession object with a request
      to start a new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). This information is added to the new  GameSession object that is created for a
      successful match.

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in
        a game session request, these properties communicate details to be used when setting up
        the new game session, such as to specify a game mode, level, or map. Game properties
        are passed to the game server process when initiating a new game session; the server
        process uses the properties as appropriate. For more information, see the `Amazon
        GameLift Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). This information is added to the new  GameSession object that is created for a
      successful match.

    - **BackfillMode** *(string) --*

      Method used to backfill game sessions created with this matchmaking configuration. MANUAL
      indicates that the game makes backfill requests or does not use the match backfill
      feature. AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever
      a game session has one or more open slots. Learn more about manual and automatic backfill
      in `Backfill Existing Games with FlexMatch
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-backfill.html>`__ .
    """


_DescribeMatchmakingConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeMatchmakingConfigurationsPaginateResponseTypeDef",
    {
        "Configurations": List[
            DescribeMatchmakingConfigurationsPaginateResponseConfigurationsTypeDef
        ]
    },
    total=False,
)


class DescribeMatchmakingConfigurationsPaginateResponseTypeDef(
    _DescribeMatchmakingConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeMatchmakingConfigurationsPaginate` `Response`

    Represents the returned data in response to a request action.

    - **Configurations** *(list) --*

      Collection of requested matchmaking configuration objects.

      - *(dict) --*

        Guidelines for use with FlexMatch to match players into games. All matchmaking requests
        must specify a matchmaking configuration.

        - **Name** *(string) --*

          Unique identifier for a matchmaking configuration. This name is used to identify the
          configuration associated with a matchmaking request or ticket.

        - **Description** *(string) --*

          Descriptive label that is associated with matchmaking configuration.

        - **GameSessionQueueArns** *(list) --*

          Amazon Resource Name (`ARN
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`__ ) that is
          assigned to a game session queue and uniquely identifies it. Format is
          ``arn:aws:gamelift:<region>:<aws account>:gamesessionqueue/<queue name>`` . These queues
          are used when placing game sessions for matches that are created with this matchmaking
          configuration. Queues can be located in any region.

          - *(string) --*

        - **RequestTimeoutSeconds** *(integer) --*

          Maximum duration, in seconds, that a matchmaking ticket can remain in process before
          timing out. Requests that fail due to timing out can be resubmitted as needed.

        - **AcceptanceTimeoutSeconds** *(integer) --*

          Length of time (in seconds) to wait for players to accept a proposed match. If any player
          rejects the match or fails to accept before the timeout, the ticket continues to look for
          an acceptable match.

        - **AcceptanceRequired** *(boolean) --*

          Flag that determines whether a match that was created with this configuration must be
          accepted by the matched players. To require acceptance, set to TRUE.

        - **RuleSetName** *(string) --*

          Unique identifier for a matchmaking rule set to use with this configuration. A
          matchmaking configuration can only use rule sets that are defined in the same region.

        - **NotificationTarget** *(string) --*

          SNS topic ARN that is set up to receive matchmaking notifications.

        - **AdditionalPlayerCount** *(integer) --*

          Number of player slots in a match to keep open for future players. For example, if the
          configuration's rule set specifies a match for a single 12-person team, and the
          additional player count is set to 2, only 10 players are selected for the match.

        - **CustomEventData** *(string) --*

          Information to attach to all events related to the matchmaking configuration.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **GameProperties** *(list) --*

          Set of custom properties for a game session, formatted as key:value pairs. These
          properties are passed to a game server process in the  GameSession object with a request
          to start a new game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ). This information is added to the new  GameSession object that is created for a
          successful match.

          - *(dict) --*

            Set of key-value pairs that contain information about a game session. When included in
            a game session request, these properties communicate details to be used when setting up
            the new game session, such as to specify a game mode, level, or map. Game properties
            are passed to the game server process when initiating a new game session; the server
            process uses the properties as appropriate. For more information, see the `Amazon
            GameLift Developer Guide
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
            .

            - **Key** *(string) --*

              Game property identifier.

            - **Value** *(string) --*

              Game property value.

        - **GameSessionData** *(string) --*

          Set of custom game session properties, formatted as a single string value. This data is
          passed to a game server process in the  GameSession object with a request to start a new
          game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ). This information is added to the new  GameSession object that is created for a
          successful match.

        - **BackfillMode** *(string) --*

          Method used to backfill game sessions created with this matchmaking configuration. MANUAL
          indicates that the game makes backfill requests or does not use the match backfill
          feature. AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever
          a game session has one or more open slots. Learn more about manual and automatic backfill
          in `Backfill Existing Games with FlexMatch
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-backfill.html>`__ .
    """


_DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef(
    _DescribeMatchmakingRuleSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeMatchmakingRuleSetsPaginate` `PaginationConfig`

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


_DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef = TypedDict(
    "_DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef",
    {"RuleSetName": str, "RuleSetBody": str, "CreationTime": datetime},
    total=False,
)


class DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef(
    _DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef
):
    """
    Type definition for `DescribeMatchmakingRuleSetsPaginateResponse` `RuleSets`

    Set of rule statements, used with FlexMatch, that determine how to build your player
    matches. Each rule set describes a type of group to be created and defines the parameters
    for acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.

    A rule set may define the following elements for a match. For detailed information and
    examples showing how to construct a rule set, see `Build a FlexMatch Rule Set
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-rulesets.html>`__ .

    * Teams -- Required. A rule set must define one or multiple teams for the match and set
    minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that
    requires all eight slots to be filled.

    * Player attributes -- Optional. These attributes specify a set of player characteristics
    to evaluate when looking for a match. Matchmaking requests that use a rule set with player
    attributes must provide the corresponding attribute values. For example, an attribute might
    specify a player's skill or level.

    * Rules -- Optional. Rules define how to evaluate potential players for a match based on
    player attributes. A rule might specify minimum requirements for individual players, teams,
    or entire matches. For example, a rule might require each player to meet a certain skill
    level, each team to have at least one player in a certain role, or the match to have a
    minimum average skill level. or may describe an entire group--such as all teams must be
    evenly matched or have at least one player in a certain role.

    * Expansions -- Optional. Expansions allow you to relax the rules after a period of time
    when no acceptable matches are found. This feature lets you balance getting players into
    games in a reasonable amount of time instead of making them wait indefinitely for the best
    possible match. For example, you might use an expansion to increase the maximum skill
    variance between players after 30 seconds.

    - **RuleSetName** *(string) --*

      Unique identifier for a matchmaking rule set

    - **RuleSetBody** *(string) --*

      Collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in
      JSON, but most elements support a description field.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").
    """


_DescribeMatchmakingRuleSetsPaginateResponseTypeDef = TypedDict(
    "_DescribeMatchmakingRuleSetsPaginateResponseTypeDef",
    {"RuleSets": List[DescribeMatchmakingRuleSetsPaginateResponseRuleSetsTypeDef]},
    total=False,
)


class DescribeMatchmakingRuleSetsPaginateResponseTypeDef(
    _DescribeMatchmakingRuleSetsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeMatchmakingRuleSetsPaginate` `Response`

    Represents the returned data in response to a request action.

    - **RuleSets** *(list) --*

      Collection of requested matchmaking rule set objects.

      - *(dict) --*

        Set of rule statements, used with FlexMatch, that determine how to build your player
        matches. Each rule set describes a type of group to be created and defines the parameters
        for acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.

        A rule set may define the following elements for a match. For detailed information and
        examples showing how to construct a rule set, see `Build a FlexMatch Rule Set
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-rulesets.html>`__ .

        * Teams -- Required. A rule set must define one or multiple teams for the match and set
        minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that
        requires all eight slots to be filled.

        * Player attributes -- Optional. These attributes specify a set of player characteristics
        to evaluate when looking for a match. Matchmaking requests that use a rule set with player
        attributes must provide the corresponding attribute values. For example, an attribute might
        specify a player's skill or level.

        * Rules -- Optional. Rules define how to evaluate potential players for a match based on
        player attributes. A rule might specify minimum requirements for individual players, teams,
        or entire matches. For example, a rule might require each player to meet a certain skill
        level, each team to have at least one player in a certain role, or the match to have a
        minimum average skill level. or may describe an entire group--such as all teams must be
        evenly matched or have at least one player in a certain role.

        * Expansions -- Optional. Expansions allow you to relax the rules after a period of time
        when no acceptable matches are found. This feature lets you balance getting players into
        games in a reasonable amount of time instead of making them wait indefinitely for the best
        possible match. For example, you might use an expansion to increase the maximum skill
        variance between players after 30 seconds.

        - **RuleSetName** *(string) --*

          Unique identifier for a matchmaking rule set

        - **RuleSetBody** *(string) --*

          Collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in
          JSON, but most elements support a description field.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").
    """


_DescribePlayerSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePlayerSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePlayerSessionsPaginatePaginationConfigTypeDef(
    _DescribePlayerSessionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribePlayerSessionsPaginate` `PaginationConfig`

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


_DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef = TypedDict(
    "_DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)


class DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef(
    _DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef
):
    """
    Type definition for `DescribePlayerSessionsPaginateResponse` `PlayerSessions`

    Properties describing a player session. Player session objects are created either by
    creating a player session for a specific game session, or as part of a game session
    placement. A player session represents either a player reservation for a game session
    (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A
    player session object (including player data) is automatically passed to a game session
    when the player connects to the game session and is validated.

    When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
    session ends, the player session object is retained for 30 days and then removed.

    *  CreatePlayerSession

    *  CreatePlayerSessions

    *  DescribePlayerSessions

    * Game session placements

      *  StartGameSessionPlacement

      *  DescribeGameSessionPlacement

      *  StopGameSessionPlacement

    - **PlayerSessionId** *(string) --*

      Unique identifier for a player session.

    - **PlayerId** *(string) --*

      Unique identifier for a player that is associated with this player session.

    - **GameSessionId** *(string) --*

      Unique identifier for the game session that the player session is connected to.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the player's game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **Status** *(string) --*

      Current status of the player session.

      Possible player session statuses include the following:

      * **RESERVED** -- The player session request has been received, but the player has not
      yet connected to the server process and/or been validated.

      * **ACTIVE** -- The player has been validated by the server process and is currently
      connected.

      * **COMPLETED** -- The player connection has been dropped.

      * **TIMEDOUT** -- A player session request was received, but the player did not connect
      and/or was not validated within the timeout limit (60 seconds).

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift server process, an app
      needs both the IP address and port number.

    - **PlayerData** *(string) --*

      Developer-defined information related to a player. Amazon GameLift does not use this
      data, so it can be formatted as needed for use in the game.
    """


_DescribePlayerSessionsPaginateResponseTypeDef = TypedDict(
    "_DescribePlayerSessionsPaginateResponseTypeDef",
    {
        "PlayerSessions": List[
            DescribePlayerSessionsPaginateResponsePlayerSessionsTypeDef
        ]
    },
    total=False,
)


class DescribePlayerSessionsPaginateResponseTypeDef(
    _DescribePlayerSessionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribePlayerSessionsPaginate` `Response`

    Represents the returned data in response to a request action.

    - **PlayerSessions** *(list) --*

      Collection of objects containing properties for each player session that matches the request.

      - *(dict) --*

        Properties describing a player session. Player session objects are created either by
        creating a player session for a specific game session, or as part of a game session
        placement. A player session represents either a player reservation for a game session
        (status ``RESERVED`` ) or actual player activity in a game session (status ``ACTIVE`` ). A
        player session object (including player data) is automatically passed to a game session
        when the player connects to the game session and is validated.

        When a player disconnects, the player session status changes to ``COMPLETED`` . Once the
        session ends, the player session object is retained for 30 days and then removed.

        *  CreatePlayerSession

        *  CreatePlayerSessions

        *  DescribePlayerSessions

        * Game session placements

          *  StartGameSessionPlacement

          *  DescribeGameSessionPlacement

          *  StopGameSessionPlacement

        - **PlayerSessionId** *(string) --*

          Unique identifier for a player session.

        - **PlayerId** *(string) --*

          Unique identifier for a player that is associated with this player session.

        - **GameSessionId** *(string) --*

          Unique identifier for the game session that the player session is connected to.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the player's game session is running on.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **TerminationTime** *(datetime) --*

          Time stamp indicating when this data object was terminated. Format is a number expressed
          in Unix time as milliseconds (for example "1469498468.057").

        - **Status** *(string) --*

          Current status of the player session.

          Possible player session statuses include the following:

          * **RESERVED** -- The player session request has been received, but the player has not
          yet connected to the server process and/or been validated.

          * **ACTIVE** -- The player has been validated by the server process and is currently
          connected.

          * **COMPLETED** -- The player connection has been dropped.

          * **TIMEDOUT** -- A player session request was received, but the player did not connect
          and/or was not validated within the timeout limit (60 seconds).

        - **IpAddress** *(string) --*

          IP address of the game session. To connect to a Amazon GameLift game server, an app needs
          both the IP address and port number.

        - **DnsName** *(string) --*

        - **Port** *(integer) --*

          Port number for the game session. To connect to a Amazon GameLift server process, an app
          needs both the IP address and port number.

        - **PlayerData** *(string) --*

          Developer-defined information related to a player. Amazon GameLift does not use this
          data, so it can be formatted as needed for use in the game.
    """


_DescribeScalingPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalingPoliciesPaginatePaginationConfigTypeDef(
    _DescribeScalingPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginate` `PaginationConfig`

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


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef",
    {"TargetValue": float},
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginateResponseScalingPolicies` `TargetConfiguration`

    Object that contains settings for a target-based scaling policy.

    - **TargetValue** *(float) --*

      Desired value to use with a target-based scaling policy. The value must be relevant for
      whatever metric the scaling policy is using. For example, in a policy using the metric
      PercentAvailableGameSessions, the target value should be the preferred size of the
      fleet's buffer (the percent of capacity that should be idle and ready for new game
      sessions).
    """


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef",
    {
        "FleetId": str,
        "Name": str,
        "Status": str,
        "ScalingAdjustment": int,
        "ScalingAdjustmentType": str,
        "ComparisonOperator": str,
        "Threshold": float,
        "EvaluationPeriods": int,
        "MetricName": str,
        "PolicyType": str,
        "TargetConfiguration": DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetConfigurationTypeDef,
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginateResponse` `ScalingPolicies`

    Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the
    combination of name and fleet ID.

    *  DescribeFleetCapacity

    *  UpdateFleetCapacity

    *  DescribeEC2InstanceLimits

    * Manage scaling policies:

      *  PutScalingPolicy (auto-scaling)

      *  DescribeScalingPolicies (auto-scaling)

      *  DeleteScalingPolicy (auto-scaling)

    * Manage fleet actions:

      *  StartFleetActions

      *  StopFleetActions

    - **FleetId** *(string) --*

      Unique identifier for a fleet that is associated with this scaling policy.

    - **Name** *(string) --*

      Descriptive label that is associated with a scaling policy. Policy names do not need to
      be unique.

    - **Status** *(string) --*

      Current status of the scaling policy. The scaling policy can be in force only when in an
      ``ACTIVE`` status. Scaling policies can be suspended for individual fleets (see
      StopFleetActions ; if suspended for a fleet, the policy status does not change. View a
      fleet's stopped actions by calling  DescribeFleetCapacity .

      * **ACTIVE** -- The scaling policy can be used for auto-scaling a fleet.

      * **UPDATE_REQUESTED** -- A request to update the scaling policy has been received.

      * **UPDATING** -- A change is being made to the scaling policy.

      * **DELETE_REQUESTED** -- A request to delete the scaling policy has been received.

      * **DELETING** -- The scaling policy is being deleted.

      * **DELETED** -- The scaling policy has been deleted.

      * **ERROR** -- An error occurred in creating the policy. It should be removed and
      recreated.

    - **ScalingAdjustment** *(integer) --*

      Amount of adjustment to make, based on the scaling adjustment type.

    - **ScalingAdjustmentType** *(string) --*

      Type of adjustment to make to a fleet's instance count (see  FleetCapacity ):

      * **ChangeInCapacity** -- add (or subtract) the scaling adjustment value from the current
      instance count. Positive values scale up while negative values scale down.

      * **ExactCapacity** -- set the instance count to the scaling adjustment value.

      * **PercentChangeInCapacity** -- increase or reduce the current instance count by the
      scaling adjustment, read as a percentage. Positive values scale up while negative values
      scale down.

    - **ComparisonOperator** *(string) --*

      Comparison operator to use when measuring a metric against the threshold value.

    - **Threshold** *(float) --*

      Metric value used to trigger a scaling event.

    - **EvaluationPeriods** *(integer) --*

      Length of time (in minutes) the metric must be at or beyond the threshold before a
      scaling event is triggered.

    - **MetricName** *(string) --*

      Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment.
      For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift with Amazon
      CloudWatch
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`__
      .

      * **ActivatingGameSessions** -- Game sessions in the process of being created.

      * **ActiveGameSessions** -- Game sessions that are currently running.

      * **ActiveInstances** -- Fleet instances that are currently running at least one game
      session.

      * **AvailableGameSessions** -- Additional game sessions that fleet could host
      simultaneously, given current capacity.

      * **AvailablePlayerSessions** -- Empty player slots in currently active game sessions.
      This includes game sessions that are not currently accepting players. Reserved player
      slots are not included.

      * **CurrentPlayerSessions** -- Player slots in active game sessions that are being used
      by a player or are reserved for a player.

      * **IdleInstances** -- Active instances that are currently hosting zero game sessions.

      * **PercentAvailableGameSessions** -- Unused percentage of the total number of game
      sessions that a fleet could host simultaneously, given current capacity. Use this metric
      for a target-based scaling policy.

      * **PercentIdleInstances** -- Percentage of the total number of active instances that are
      hosting zero game sessions.

      * **QueueDepth** -- Pending game session placement requests, in any queue, where the
      current fleet is the top-priority destination.

      * **WaitTime** -- Current wait time for pending game session placement requests, in any
      queue, where the current fleet is the top-priority destination.

    - **PolicyType** *(string) --*

      Type of scaling policy to create. For a target-based policy, set the parameter
      *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For
      a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* ,
      *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .

    - **TargetConfiguration** *(dict) --*

      Object that contains settings for a target-based scaling policy.

      - **TargetValue** *(float) --*

        Desired value to use with a target-based scaling policy. The value must be relevant for
        whatever metric the scaling policy is using. For example, in a policy using the metric
        PercentAvailableGameSessions, the target value should be the preferred size of the
        fleet's buffer (the percent of capacity that should be idle and ready for new game
        sessions).
    """


_DescribeScalingPoliciesPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseTypeDef",
    {
        "ScalingPolicies": List[
            DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef
        ]
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseTypeDef(
    _DescribeScalingPoliciesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginate` `Response`

    Represents the returned data in response to a request action.

    - **ScalingPolicies** *(list) --*

      Collection of objects containing the scaling policies matching the request.

      - *(dict) --*

        Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the
        combination of name and fleet ID.

        *  DescribeFleetCapacity

        *  UpdateFleetCapacity

        *  DescribeEC2InstanceLimits

        * Manage scaling policies:

          *  PutScalingPolicy (auto-scaling)

          *  DescribeScalingPolicies (auto-scaling)

          *  DeleteScalingPolicy (auto-scaling)

        * Manage fleet actions:

          *  StartFleetActions

          *  StopFleetActions

        - **FleetId** *(string) --*

          Unique identifier for a fleet that is associated with this scaling policy.

        - **Name** *(string) --*

          Descriptive label that is associated with a scaling policy. Policy names do not need to
          be unique.

        - **Status** *(string) --*

          Current status of the scaling policy. The scaling policy can be in force only when in an
          ``ACTIVE`` status. Scaling policies can be suspended for individual fleets (see
          StopFleetActions ; if suspended for a fleet, the policy status does not change. View a
          fleet's stopped actions by calling  DescribeFleetCapacity .

          * **ACTIVE** -- The scaling policy can be used for auto-scaling a fleet.

          * **UPDATE_REQUESTED** -- A request to update the scaling policy has been received.

          * **UPDATING** -- A change is being made to the scaling policy.

          * **DELETE_REQUESTED** -- A request to delete the scaling policy has been received.

          * **DELETING** -- The scaling policy is being deleted.

          * **DELETED** -- The scaling policy has been deleted.

          * **ERROR** -- An error occurred in creating the policy. It should be removed and
          recreated.

        - **ScalingAdjustment** *(integer) --*

          Amount of adjustment to make, based on the scaling adjustment type.

        - **ScalingAdjustmentType** *(string) --*

          Type of adjustment to make to a fleet's instance count (see  FleetCapacity ):

          * **ChangeInCapacity** -- add (or subtract) the scaling adjustment value from the current
          instance count. Positive values scale up while negative values scale down.

          * **ExactCapacity** -- set the instance count to the scaling adjustment value.

          * **PercentChangeInCapacity** -- increase or reduce the current instance count by the
          scaling adjustment, read as a percentage. Positive values scale up while negative values
          scale down.

        - **ComparisonOperator** *(string) --*

          Comparison operator to use when measuring a metric against the threshold value.

        - **Threshold** *(float) --*

          Metric value used to trigger a scaling event.

        - **EvaluationPeriods** *(integer) --*

          Length of time (in minutes) the metric must be at or beyond the threshold before a
          scaling event is triggered.

        - **MetricName** *(string) --*

          Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment.
          For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift with Amazon
          CloudWatch
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`__
          .

          * **ActivatingGameSessions** -- Game sessions in the process of being created.

          * **ActiveGameSessions** -- Game sessions that are currently running.

          * **ActiveInstances** -- Fleet instances that are currently running at least one game
          session.

          * **AvailableGameSessions** -- Additional game sessions that fleet could host
          simultaneously, given current capacity.

          * **AvailablePlayerSessions** -- Empty player slots in currently active game sessions.
          This includes game sessions that are not currently accepting players. Reserved player
          slots are not included.

          * **CurrentPlayerSessions** -- Player slots in active game sessions that are being used
          by a player or are reserved for a player.

          * **IdleInstances** -- Active instances that are currently hosting zero game sessions.

          * **PercentAvailableGameSessions** -- Unused percentage of the total number of game
          sessions that a fleet could host simultaneously, given current capacity. Use this metric
          for a target-based scaling policy.

          * **PercentIdleInstances** -- Percentage of the total number of active instances that are
          hosting zero game sessions.

          * **QueueDepth** -- Pending game session placement requests, in any queue, where the
          current fleet is the top-priority destination.

          * **WaitTime** -- Current wait time for pending game session placement requests, in any
          queue, where the current fleet is the top-priority destination.

        - **PolicyType** *(string) --*

          Type of scaling policy to create. For a target-based policy, set the parameter
          *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For
          a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* ,
          *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .

        - **TargetConfiguration** *(dict) --*

          Object that contains settings for a target-based scaling policy.

          - **TargetValue** *(float) --*

            Desired value to use with a target-based scaling policy. The value must be relevant for
            whatever metric the scaling policy is using. For example, in a policy using the metric
            PercentAvailableGameSessions, the target value should be the preferred size of the
            fleet's buffer (the percent of capacity that should be idle and ready for new game
            sessions).
    """


_ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAliasesPaginatePaginationConfigTypeDef(
    _ListAliasesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAliasesPaginate` `PaginationConfig`

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


_ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef = TypedDict(
    "_ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef",
    {"Type": str, "FleetId": str, "Message": str},
    total=False,
)


class ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef(
    _ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef
):
    """
    Type definition for `ListAliasesPaginateResponseAliases` `RoutingStrategy`

    Alias configuration for the alias, including routing type and settings.

    - **Type** *(string) --*

      Type of routing strategy.

      Possible routing types include the following:

      * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
      active fleets.

      * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
      display a message to the user. A terminal alias throws a
      TerminalRoutingStrategyException with the  RoutingStrategy message embedded.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the alias points to.

    - **Message** *(string) --*

      Message text to be used with a terminal routing strategy.
    """


_ListAliasesPaginateResponseAliasesTypeDef = TypedDict(
    "_ListAliasesPaginateResponseAliasesTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": ListAliasesPaginateResponseAliasesRoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ListAliasesPaginateResponseAliasesTypeDef(
    _ListAliasesPaginateResponseAliasesTypeDef
):
    """
    Type definition for `ListAliasesPaginateResponse` `Aliases`

    Properties describing a fleet alias.

    *  CreateAlias

    *  ListAliases

    *  DescribeAlias

    *  UpdateAlias

    *  DeleteAlias

    *  ResolveAlias

    - **AliasId** *(string) --*

      Unique identifier for an alias; alias IDs are unique within a region.

    - **Name** *(string) --*

      Descriptive label that is associated with an alias. Alias names do not need to be unique.

    - **AliasArn** *(string) --*

      Unique identifier for an alias; alias ARNs are unique across all regions.

    - **Description** *(string) --*

      Human-readable description of an alias.

    - **RoutingStrategy** *(dict) --*

      Alias configuration for the alias, including routing type and settings.

      - **Type** *(string) --*

        Type of routing strategy.

        Possible routing types include the following:

        * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
        active fleets.

        * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
        display a message to the user. A terminal alias throws a
        TerminalRoutingStrategyException with the  RoutingStrategy message embedded.

      - **FleetId** *(string) --*

        Unique identifier for a fleet that the alias points to.

      - **Message** *(string) --*

        Message text to be used with a terminal routing strategy.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **LastUpdatedTime** *(datetime) --*

      Time stamp indicating when this data object was last modified. Format is a number
      expressed in Unix time as milliseconds (for example "1469498468.057").
    """


_ListAliasesPaginateResponseTypeDef = TypedDict(
    "_ListAliasesPaginateResponseTypeDef",
    {"Aliases": List[ListAliasesPaginateResponseAliasesTypeDef]},
    total=False,
)


class ListAliasesPaginateResponseTypeDef(_ListAliasesPaginateResponseTypeDef):
    """
    Type definition for `ListAliasesPaginate` `Response`

    Represents the returned data in response to a request action.

    - **Aliases** *(list) --*

      Collection of alias records that match the list request.

      - *(dict) --*

        Properties describing a fleet alias.

        *  CreateAlias

        *  ListAliases

        *  DescribeAlias

        *  UpdateAlias

        *  DeleteAlias

        *  ResolveAlias

        - **AliasId** *(string) --*

          Unique identifier for an alias; alias IDs are unique within a region.

        - **Name** *(string) --*

          Descriptive label that is associated with an alias. Alias names do not need to be unique.

        - **AliasArn** *(string) --*

          Unique identifier for an alias; alias ARNs are unique across all regions.

        - **Description** *(string) --*

          Human-readable description of an alias.

        - **RoutingStrategy** *(dict) --*

          Alias configuration for the alias, including routing type and settings.

          - **Type** *(string) --*

            Type of routing strategy.

            Possible routing types include the following:

            * **SIMPLE** -- The alias resolves to one specific fleet. Use this type when routing to
            active fleets.

            * **TERMINAL** -- The alias does not resolve to a fleet but instead can be used to
            display a message to the user. A terminal alias throws a
            TerminalRoutingStrategyException with the  RoutingStrategy message embedded.

          - **FleetId** *(string) --*

            Unique identifier for a fleet that the alias points to.

          - **Message** *(string) --*

            Message text to be used with a terminal routing strategy.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **LastUpdatedTime** *(datetime) --*

          Time stamp indicating when this data object was last modified. Format is a number
          expressed in Unix time as milliseconds (for example "1469498468.057").
    """


_ListBuildsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBuildsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBuildsPaginatePaginationConfigTypeDef(
    _ListBuildsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBuildsPaginate` `PaginationConfig`

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


_ListBuildsPaginateResponseBuildsTypeDef = TypedDict(
    "_ListBuildsPaginateResponseBuildsTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": str,
        "SizeOnDisk": int,
        "OperatingSystem": str,
        "CreationTime": datetime,
    },
    total=False,
)


class ListBuildsPaginateResponseBuildsTypeDef(_ListBuildsPaginateResponseBuildsTypeDef):
    """
    Type definition for `ListBuildsPaginateResponse` `Builds`

    Properties describing a custom game build.

     **Related operations**

    *  CreateBuild

    *  ListBuilds

    *  DescribeBuild

    *  UpdateBuild

    *  DeleteBuild

    - **BuildId** *(string) --*

      Unique identifier for a build.

    - **Name** *(string) --*

      Descriptive label that is associated with a build. Build names do not need to be unique.
      It can be set using  CreateBuild or  UpdateBuild .

    - **Version** *(string) --*

      Version that is associated with a build or script. Version strings do not need to be
      unique. This value can be set using  CreateBuild or  UpdateBuild .

    - **Status** *(string) --*

      Current status of the build.

      Possible build statuses include the following:

      * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You
      cannot create fleets for builds that are in this status. When a build is successfully
      created, the build status is set to this value.

      * **READY** -- The game build has been successfully uploaded. You can now create new
      fleets for this build.

      * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.

    - **SizeOnDisk** *(integer) --*

      File size of the uploaded game build, expressed in bytes. When the build status is
      ``INITIALIZED`` , this value is 0.

    - **OperatingSystem** *(string) --*

      Operating system that the game server binaries are built to run on. This value determines
      the type of fleet resources that you can use for this build.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").
    """


_ListBuildsPaginateResponseTypeDef = TypedDict(
    "_ListBuildsPaginateResponseTypeDef",
    {"Builds": List[ListBuildsPaginateResponseBuildsTypeDef]},
    total=False,
)


class ListBuildsPaginateResponseTypeDef(_ListBuildsPaginateResponseTypeDef):
    """
    Type definition for `ListBuildsPaginate` `Response`

    Represents the returned data in response to a request action.

    - **Builds** *(list) --*

      Collection of build records that match the request.

      - *(dict) --*

        Properties describing a custom game build.

         **Related operations**

        *  CreateBuild

        *  ListBuilds

        *  DescribeBuild

        *  UpdateBuild

        *  DeleteBuild

        - **BuildId** *(string) --*

          Unique identifier for a build.

        - **Name** *(string) --*

          Descriptive label that is associated with a build. Build names do not need to be unique.
          It can be set using  CreateBuild or  UpdateBuild .

        - **Version** *(string) --*

          Version that is associated with a build or script. Version strings do not need to be
          unique. This value can be set using  CreateBuild or  UpdateBuild .

        - **Status** *(string) --*

          Current status of the build.

          Possible build statuses include the following:

          * **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You
          cannot create fleets for builds that are in this status. When a build is successfully
          created, the build status is set to this value.

          * **READY** -- The game build has been successfully uploaded. You can now create new
          fleets for this build.

          * **FAILED** -- The game build upload failed. You cannot create new fleets for this build.

        - **SizeOnDisk** *(integer) --*

          File size of the uploaded game build, expressed in bytes. When the build status is
          ``INITIALIZED`` , this value is 0.

        - **OperatingSystem** *(string) --*

          Operating system that the game server binaries are built to run on. This value determines
          the type of fleet resources that you can use for this build.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").
    """


_ListFleetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFleetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFleetsPaginatePaginationConfigTypeDef(
    _ListFleetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFleetsPaginate` `PaginationConfig`

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


_ListFleetsPaginateResponseTypeDef = TypedDict(
    "_ListFleetsPaginateResponseTypeDef", {"FleetIds": List[str]}, total=False
)


class ListFleetsPaginateResponseTypeDef(_ListFleetsPaginateResponseTypeDef):
    """
    Type definition for `ListFleetsPaginate` `Response`

    Represents the returned data in response to a request action.

    - **FleetIds** *(list) --*

      Set of fleet IDs matching the list request. You can retrieve additional information about all
      returned fleets by passing this result set to a call to  DescribeFleetAttributes ,
      DescribeFleetCapacity , or  DescribeFleetUtilization .

      - *(string) --*
    """


_SearchGameSessionsPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchGameSessionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchGameSessionsPaginatePaginationConfigTypeDef(
    _SearchGameSessionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchGameSessionsPaginate` `PaginationConfig`

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


_SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef = TypedDict(
    "_SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef(
    _SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef
):
    """
    Type definition for `SearchGameSessionsPaginateResponseGameSessions` `GameProperties`

    Set of key-value pairs that contain information about a game session. When included in
    a game session request, these properties communicate details to be used when setting up
    the new game session, such as to specify a game mode, level, or map. Game properties
    are passed to the game server process when initiating a new game session; the server
    process uses the properties as appropriate. For more information, see the `Amazon
    GameLift Developer Guide
    <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
    .

    - **Key** *(string) --*

      Game property identifier.

    - **Value** *(string) --*

      Game property value.
    """


_SearchGameSessionsPaginateResponseGameSessionsTypeDef = TypedDict(
    "_SearchGameSessionsPaginateResponseGameSessionsTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": str,
        "StatusReason": str,
        "GameProperties": List[
            SearchGameSessionsPaginateResponseGameSessionsGamePropertiesTypeDef
        ],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": str,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)


class SearchGameSessionsPaginateResponseGameSessionsTypeDef(
    _SearchGameSessionsPaginateResponseGameSessionsTypeDef
):
    """
    Type definition for `SearchGameSessionsPaginateResponse` `GameSessions`

    Properties describing a game session.

    A game session in ACTIVE status can host players. When a game session ends, its status is
    set to ``TERMINATED`` .

    Once the session ends, the game session object is retained for 30 days. This means you can
    reuse idempotency token values after this time. Game session logs are retained for 14 days.

    *  CreateGameSession

    *  DescribeGameSessions

    *  DescribeGameSessionDetails

    *  SearchGameSessions

    *  UpdateGameSession

    *  GetGameSessionLogUrl

    * Game session placements

      *  StartGameSessionPlacement

      *  DescribeGameSessionPlacement

      *  StopGameSessionPlacement

    - **GameSessionId** *(string) --*

      Unique identifier for the game session. A game session ARN has the following format:
      ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
      token>`` .

    - **Name** *(string) --*

      Descriptive label that is associated with a game session. Session names do not need to be
      unique.

    - **FleetId** *(string) --*

      Unique identifier for a fleet that the game session is running on.

    - **CreationTime** *(datetime) --*

      Time stamp indicating when this data object was created. Format is a number expressed in
      Unix time as milliseconds (for example "1469498468.057").

    - **TerminationTime** *(datetime) --*

      Time stamp indicating when this data object was terminated. Format is a number expressed
      in Unix time as milliseconds (for example "1469498468.057").

    - **CurrentPlayerSessionCount** *(integer) --*

      Number of players currently in the game session.

    - **MaximumPlayerSessionCount** *(integer) --*

      Maximum number of players that can be connected simultaneously to the game session.

    - **Status** *(string) --*

      Current status of the game session. A game session must have an ``ACTIVE`` status to have
      player sessions.

    - **StatusReason** *(string) --*

      Provides additional information about game session status. ``INTERRUPTED`` indicates that
      the game session was hosted on a spot instance that was reclaimed, causing the active
      game session to be terminated.

    - **GameProperties** *(list) --*

      Set of custom properties for a game session, formatted as key:value pairs. These
      properties are passed to a game server process in the  GameSession object with a request
      to start a new game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ). You can search for active game sessions based on this custom data with
      SearchGameSessions .

      - *(dict) --*

        Set of key-value pairs that contain information about a game session. When included in
        a game session request, these properties communicate details to be used when setting up
        the new game session, such as to specify a game mode, level, or map. Game properties
        are passed to the game server process when initiating a new game session; the server
        process uses the properties as appropriate. For more information, see the `Amazon
        GameLift Developer Guide
        <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
        .

        - **Key** *(string) --*

          Game property identifier.

        - **Value** *(string) --*

          Game property value.

    - **IpAddress** *(string) --*

      IP address of the game session. To connect to a Amazon GameLift game server, an app needs
      both the IP address and port number.

    - **DnsName** *(string) --*

    - **Port** *(integer) --*

      Port number for the game session. To connect to a Amazon GameLift game server, an app
      needs both the IP address and port number.

    - **PlayerSessionCreationPolicy** *(string) --*

      Indicates whether or not the game session is accepting new players.

    - **CreatorId** *(string) --*

      Unique identifier for a player. This ID is used to enforce a resource protection policy
      (if one exists), that limits the number of game sessions a player can create.

    - **GameSessionData** *(string) --*

      Set of custom game session properties, formatted as a single string value. This data is
      passed to a game server process in the  GameSession object with a request to start a new
      game session (see `Start a Game Session
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
      ).

    - **MatchmakerData** *(string) --*

      Information about the matchmaking process that was used to create the game session. It is
      in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
      contains data on all players assigned to the match, including player attributes and team
      assignments. For more details on matchmaker data, see `Match Data
      <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
      . Matchmaker data is useful when requesting match backfills, and is updated whenever new
      players are added during a successful backfill (see  StartMatchBackfill ).
    """


_SearchGameSessionsPaginateResponseTypeDef = TypedDict(
    "_SearchGameSessionsPaginateResponseTypeDef",
    {"GameSessions": List[SearchGameSessionsPaginateResponseGameSessionsTypeDef]},
    total=False,
)


class SearchGameSessionsPaginateResponseTypeDef(
    _SearchGameSessionsPaginateResponseTypeDef
):
    """
    Type definition for `SearchGameSessionsPaginate` `Response`

    Represents the returned data in response to a request action.

    - **GameSessions** *(list) --*

      Collection of objects containing game session properties for each session matching the
      request.

      - *(dict) --*

        Properties describing a game session.

        A game session in ACTIVE status can host players. When a game session ends, its status is
        set to ``TERMINATED`` .

        Once the session ends, the game session object is retained for 30 days. This means you can
        reuse idempotency token values after this time. Game session logs are retained for 14 days.

        *  CreateGameSession

        *  DescribeGameSessions

        *  DescribeGameSessionDetails

        *  SearchGameSessions

        *  UpdateGameSession

        *  GetGameSessionLogUrl

        * Game session placements

          *  StartGameSessionPlacement

          *  DescribeGameSessionPlacement

          *  StopGameSessionPlacement

        - **GameSessionId** *(string) --*

          Unique identifier for the game session. A game session ARN has the following format:
          ``arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency
          token>`` .

        - **Name** *(string) --*

          Descriptive label that is associated with a game session. Session names do not need to be
          unique.

        - **FleetId** *(string) --*

          Unique identifier for a fleet that the game session is running on.

        - **CreationTime** *(datetime) --*

          Time stamp indicating when this data object was created. Format is a number expressed in
          Unix time as milliseconds (for example "1469498468.057").

        - **TerminationTime** *(datetime) --*

          Time stamp indicating when this data object was terminated. Format is a number expressed
          in Unix time as milliseconds (for example "1469498468.057").

        - **CurrentPlayerSessionCount** *(integer) --*

          Number of players currently in the game session.

        - **MaximumPlayerSessionCount** *(integer) --*

          Maximum number of players that can be connected simultaneously to the game session.

        - **Status** *(string) --*

          Current status of the game session. A game session must have an ``ACTIVE`` status to have
          player sessions.

        - **StatusReason** *(string) --*

          Provides additional information about game session status. ``INTERRUPTED`` indicates that
          the game session was hosted on a spot instance that was reclaimed, causing the active
          game session to be terminated.

        - **GameProperties** *(list) --*

          Set of custom properties for a game session, formatted as key:value pairs. These
          properties are passed to a game server process in the  GameSession object with a request
          to start a new game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ). You can search for active game sessions based on this custom data with
          SearchGameSessions .

          - *(dict) --*

            Set of key-value pairs that contain information about a game session. When included in
            a game session request, these properties communicate details to be used when setting up
            the new game session, such as to specify a game mode, level, or map. Game properties
            are passed to the game server process when initiating a new game session; the server
            process uses the properties as appropriate. For more information, see the `Amazon
            GameLift Developer Guide
            <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`__
            .

            - **Key** *(string) --*

              Game property identifier.

            - **Value** *(string) --*

              Game property value.

        - **IpAddress** *(string) --*

          IP address of the game session. To connect to a Amazon GameLift game server, an app needs
          both the IP address and port number.

        - **DnsName** *(string) --*

        - **Port** *(integer) --*

          Port number for the game session. To connect to a Amazon GameLift game server, an app
          needs both the IP address and port number.

        - **PlayerSessionCreationPolicy** *(string) --*

          Indicates whether or not the game session is accepting new players.

        - **CreatorId** *(string) --*

          Unique identifier for a player. This ID is used to enforce a resource protection policy
          (if one exists), that limits the number of game sessions a player can create.

        - **GameSessionData** *(string) --*

          Set of custom game session properties, formatted as a single string value. This data is
          passed to a game server process in the  GameSession object with a request to start a new
          game session (see `Start a Game Session
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`__
          ).

        - **MatchmakerData** *(string) --*

          Information about the matchmaking process that was used to create the game session. It is
          in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it
          contains data on all players assigned to the match, including player attributes and team
          assignments. For more details on matchmaker data, see `Match Data
          <https://docs.aws.amazon.com/gamelift/latest/developerguide/match-server.html#match-server-data>`__
          . Matchmaker data is useful when requesting match backfills, and is updated whenever new
          players are added during a successful backfill (see  StartMatchBackfill ).
    """
