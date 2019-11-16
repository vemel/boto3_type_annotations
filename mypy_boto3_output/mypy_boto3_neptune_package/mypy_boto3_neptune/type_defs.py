"Main interface for neptune type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef",
    "ClientAddSourceIdentifierToSubscriptionResponseTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    "ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCopyDbClusterParameterGroupResponseTypeDef",
    "ClientCopyDbClusterParameterGroupTagsTypeDef",
    "ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCopyDbClusterSnapshotResponseTypeDef",
    "ClientCopyDbClusterSnapshotTagsTypeDef",
    "ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef",
    "ClientCopyDbParameterGroupResponseTypeDef",
    "ClientCopyDbParameterGroupTagsTypeDef",
    "ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCreateDbClusterParameterGroupResponseTypeDef",
    "ClientCreateDbClusterParameterGroupTagsTypeDef",
    "ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientCreateDbClusterResponseDBClusterTypeDef",
    "ClientCreateDbClusterResponseTypeDef",
    "ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCreateDbClusterSnapshotResponseTypeDef",
    "ClientCreateDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterTagsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceTypeDef",
    "ClientCreateDbInstanceResponseTypeDef",
    "ClientCreateDbInstanceTagsTypeDef",
    "ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef",
    "ClientCreateDbParameterGroupResponseTypeDef",
    "ClientCreateDbParameterGroupTagsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientCreateDbSubnetGroupResponseTypeDef",
    "ClientCreateDbSubnetGroupTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientCreateEventSubscriptionResponseTypeDef",
    "ClientCreateEventSubscriptionTagsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterTypeDef",
    "ClientDeleteDbClusterResponseTypeDef",
    "ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientDeleteDbClusterSnapshotResponseTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    "ClientDeleteDbInstanceResponseTypeDef",
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientDeleteEventSubscriptionResponseTypeDef",
    "ClientDescribeDbClusterParameterGroupsFiltersTypeDef",
    "ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef",
    "ClientDescribeDbClusterParameterGroupsResponseTypeDef",
    "ClientDescribeDbClusterParametersFiltersTypeDef",
    "ClientDescribeDbClusterParametersResponseParametersTypeDef",
    "ClientDescribeDbClusterParametersResponseTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseTypeDef",
    "ClientDescribeDbClusterSnapshotsFiltersTypeDef",
    "ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef",
    "ClientDescribeDbClusterSnapshotsResponseTypeDef",
    "ClientDescribeDbClustersFiltersTypeDef",
    "ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef",
    "ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef",
    "ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef",
    "ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef",
    "ClientDescribeDbClustersResponseDBClustersTypeDef",
    "ClientDescribeDbClustersResponseTypeDef",
    "ClientDescribeDbEngineVersionsFiltersTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef",
    "ClientDescribeDbEngineVersionsResponseTypeDef",
    "ClientDescribeDbInstancesFiltersTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    "ClientDescribeDbInstancesResponseTypeDef",
    "ClientDescribeDbParameterGroupsFiltersTypeDef",
    "ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef",
    "ClientDescribeDbParameterGroupsResponseTypeDef",
    "ClientDescribeDbParametersFiltersTypeDef",
    "ClientDescribeDbParametersResponseParametersTypeDef",
    "ClientDescribeDbParametersResponseTypeDef",
    "ClientDescribeDbSubnetGroupsFiltersTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseTypeDef",
    "ClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseTypeDef",
    "ClientDescribeEngineDefaultParametersFiltersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultParametersResponseTypeDef",
    "ClientDescribeEventCategoriesFiltersTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventSubscriptionsFiltersTypeDef",
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    "ClientDescribeEventSubscriptionsResponseTypeDef",
    "ClientDescribeEventsFiltersTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseTypeDef",
    "ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef",
    "ClientDescribeValidDbInstanceModificationsResponseTypeDef",
    "ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientFailoverDbClusterResponseDBClusterTypeDef",
    "ClientFailoverDbClusterResponseTypeDef",
    "ClientListTagsForResourceFiltersTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbClusterParameterGroupParametersTypeDef",
    "ClientModifyDbClusterParameterGroupResponseTypeDef",
    "ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientModifyDbClusterResponseDBClusterTypeDef",
    "ClientModifyDbClusterResponseTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    "ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceTypeDef",
    "ClientModifyDbInstanceResponseTypeDef",
    "ClientModifyDbParameterGroupParametersTypeDef",
    "ClientModifyDbParameterGroupResponseTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientModifyDbSubnetGroupResponseTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientModifyEventSubscriptionResponseTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef",
    "ClientPromoteReadReplicaDbClusterResponseTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceTypeDef",
    "ClientRebootDbInstanceResponseTypeDef",
    "ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef",
    "ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef",
    "ClientResetDbClusterParameterGroupParametersTypeDef",
    "ClientResetDbClusterParameterGroupResponseTypeDef",
    "ClientResetDbParameterGroupParametersTypeDef",
    "ClientResetDbParameterGroupResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotTagsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    "ClientRestoreDbClusterToPointInTimeTagsTypeDef",
    "DbInstanceAvailableWaitFiltersTypeDef",
    "DbInstanceAvailableWaitWaiterConfigTypeDef",
    "DbInstanceDeletedWaitFiltersTypeDef",
    "DbInstanceDeletedWaitWaiterConfigTypeDef",
    "DescribeDBClusterParameterGroupsPaginateFiltersTypeDef",
    "DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef",
    "DescribeDBClusterParameterGroupsPaginateResponseTypeDef",
    "DescribeDBClusterParametersPaginateFiltersTypeDef",
    "DescribeDBClusterParametersPaginatePaginationConfigTypeDef",
    "DescribeDBClusterParametersPaginateResponseParametersTypeDef",
    "DescribeDBClusterParametersPaginateResponseTypeDef",
    "DescribeDBClusterSnapshotsPaginateFiltersTypeDef",
    "DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef",
    "DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef",
    "DescribeDBClusterSnapshotsPaginateResponseTypeDef",
    "DescribeDBClustersPaginateFiltersTypeDef",
    "DescribeDBClustersPaginatePaginationConfigTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersTypeDef",
    "DescribeDBClustersPaginateResponseTypeDef",
    "DescribeDBEngineVersionsPaginateFiltersTypeDef",
    "DescribeDBEngineVersionsPaginatePaginationConfigTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef",
    "DescribeDBEngineVersionsPaginateResponseTypeDef",
    "DescribeDBInstancesPaginateFiltersTypeDef",
    "DescribeDBInstancesPaginatePaginationConfigTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesTypeDef",
    "DescribeDBInstancesPaginateResponseTypeDef",
    "DescribeDBParameterGroupsPaginateFiltersTypeDef",
    "DescribeDBParameterGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef",
    "DescribeDBParameterGroupsPaginateResponseTypeDef",
    "DescribeDBParametersPaginateFiltersTypeDef",
    "DescribeDBParametersPaginatePaginationConfigTypeDef",
    "DescribeDBParametersPaginateResponseParametersTypeDef",
    "DescribeDBParametersPaginateResponseTypeDef",
    "DescribeDBSubnetGroupsPaginateFiltersTypeDef",
    "DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseTypeDef",
    "DescribeEngineDefaultParametersPaginateFiltersTypeDef",
    "DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseTypeDef",
    "DescribeEventSubscriptionsPaginateFiltersTypeDef",
    "DescribeEventSubscriptionsPaginatePaginationConfigTypeDef",
    "DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
    "DescribeEventSubscriptionsPaginateResponseTypeDef",
    "DescribeEventsPaginateFiltersTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef",
    "DescribePendingMaintenanceActionsPaginateFiltersTypeDef",
    "DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef",
    "DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef",
    "DescribePendingMaintenanceActionsPaginateResponseTypeDef",
)


_ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef(
    _ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef
):
    """
    Type definition for `ClientAddSourceIdentifierToSubscriptionResponse` `EventSubscription`

    Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the event notification subscription.

    - **Status** *(string) --*

      The status of the event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that Neptune no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the event notification subscription was created.

    - **SourceType** *(string) --*

      The source type for the event notification subscription.

    - **SourceIdsList** *(list) --*

      A list of source IDs for the event notification subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A list of event categories for the event notification subscription.

      - *(string) --*

    - **Enabled** *(boolean) --*

      A Boolean value indicating if the subscription is enabled. True indicates the subscription
      is enabled.

    - **EventSubscriptionArn** *(string) --*

      The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientAddSourceIdentifierToSubscriptionResponseTypeDef = TypedDict(
    "_ClientAddSourceIdentifierToSubscriptionResponseTypeDef",
    {
        "EventSubscription": ClientAddSourceIdentifierToSubscriptionResponseEventSubscriptionTypeDef
    },
    total=False,
)


class ClientAddSourceIdentifierToSubscriptionResponseTypeDef(
    _ClientAddSourceIdentifierToSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientAddSourceIdentifierToSubscription` `Response`

    - **EventSubscription** *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.

      - **CustSubscriptionId** *(string) --*

        The event notification subscription Id.

      - **SnsTopicArn** *(string) --*

        The topic ARN of the event notification subscription.

      - **Status** *(string) --*

        The status of the event notification subscription.

        Constraints:

        Can be one of the following: creating | modifying | deleting | active | no-permission |
        topic-not-exist

        The status "no-permission" indicates that Neptune no longer has permission to post to the
        SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
        subscription was created.

      - **SubscriptionCreationTime** *(string) --*

        The time the event notification subscription was created.

      - **SourceType** *(string) --*

        The source type for the event notification subscription.

      - **SourceIdsList** *(list) --*

        A list of source IDs for the event notification subscription.

        - *(string) --*

      - **EventCategoriesList** *(list) --*

        A list of event categories for the event notification subscription.

        - *(string) --*

      - **Enabled** *(boolean) --*

        A Boolean value indicating if the subscription is enabled. True indicates the subscription
        is enabled.

      - **EventSubscriptionArn** *(string) --*

        The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    Type definition for `ClientAddTagsToResource` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    """
    Type definition for `ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActions` `PendingMaintenanceActionDetails`

    Provides information about a pending maintenance action for a resource.

    - **Action** *(string) --*

      The type of pending maintenance action that is available for the resource.

    - **AutoAppliedAfterDate** *(datetime) --*

      The date of the maintenance window when the action is applied. The maintenance action
      is applied to the resource during its first maintenance window after this date. If this
      date is specified, any ``next-maintenance`` opt-in requests are ignored.

    - **ForcedApplyDate** *(datetime) --*

      The date when the maintenance action is automatically applied. The maintenance action
      is applied to the resource on this date regardless of the maintenance window for the
      resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

    - **OptInStatus** *(string) --*

      Indicates the type of opt-in request that has been received for the resource.

    - **CurrentApplyDate** *(datetime) --*

      The effective date when the pending maintenance action is applied to the resource. This
      date takes into account opt-in requests received from the
      ApplyPendingMaintenanceAction API, the ``AutoAppliedAfterDate`` , and the
      ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
      and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

    - **Description** *(string) --*

      A description providing more detail about the maintenance action.
    """


_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef(
    _ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
):
    """
    Type definition for `ClientApplyPendingMaintenanceActionResponse` `ResourcePendingMaintenanceActions`

    Describes the pending maintenance actions for a resource.

    - **ResourceIdentifier** *(string) --*

      The ARN of the resource that has pending maintenance actions.

    - **PendingMaintenanceActionDetails** *(list) --*

      A list that provides details about the pending maintenance actions for the resource.

      - *(dict) --*

        Provides information about a pending maintenance action for a resource.

        - **Action** *(string) --*

          The type of pending maintenance action that is available for the resource.

        - **AutoAppliedAfterDate** *(datetime) --*

          The date of the maintenance window when the action is applied. The maintenance action
          is applied to the resource during its first maintenance window after this date. If this
          date is specified, any ``next-maintenance`` opt-in requests are ignored.

        - **ForcedApplyDate** *(datetime) --*

          The date when the maintenance action is automatically applied. The maintenance action
          is applied to the resource on this date regardless of the maintenance window for the
          resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

        - **OptInStatus** *(string) --*

          Indicates the type of opt-in request that has been received for the resource.

        - **CurrentApplyDate** *(datetime) --*

          The effective date when the pending maintenance action is applied to the resource. This
          date takes into account opt-in requests received from the
          ApplyPendingMaintenanceAction API, the ``AutoAppliedAfterDate`` , and the
          ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
          and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

        - **Description** *(string) --*

          A description providing more detail about the maintenance action.
    """


_ClientApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseTypeDef(
    _ClientApplyPendingMaintenanceActionResponseTypeDef
):
    """
    Type definition for `ClientApplyPendingMaintenanceAction` `Response`

    - **ResourcePendingMaintenanceActions** *(dict) --*

      Describes the pending maintenance actions for a resource.

      - **ResourceIdentifier** *(string) --*

        The ARN of the resource that has pending maintenance actions.

      - **PendingMaintenanceActionDetails** *(list) --*

        A list that provides details about the pending maintenance actions for the resource.

        - *(dict) --*

          Provides information about a pending maintenance action for a resource.

          - **Action** *(string) --*

            The type of pending maintenance action that is available for the resource.

          - **AutoAppliedAfterDate** *(datetime) --*

            The date of the maintenance window when the action is applied. The maintenance action
            is applied to the resource during its first maintenance window after this date. If this
            date is specified, any ``next-maintenance`` opt-in requests are ignored.

          - **ForcedApplyDate** *(datetime) --*

            The date when the maintenance action is automatically applied. The maintenance action
            is applied to the resource on this date regardless of the maintenance window for the
            resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

          - **OptInStatus** *(string) --*

            Indicates the type of opt-in request that has been received for the resource.

          - **CurrentApplyDate** *(datetime) --*

            The effective date when the pending maintenance action is applied to the resource. This
            date takes into account opt-in requests received from the
            ApplyPendingMaintenanceAction API, the ``AutoAppliedAfterDate`` , and the
            ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
            and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

          - **Description** *(string) --*

            A description providing more detail about the maintenance action.
    """


_ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef = TypedDict(
    "_ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef(
    _ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
):
    """
    Type definition for `ClientCopyDbClusterParameterGroupResponse` `DBClusterParameterGroup`

    Contains the details of an Amazon Neptune DB cluster parameter group.

    This data type is used as a response element in the  DescribeDBClusterParameterGroups action.

    - **DBClusterParameterGroupName** *(string) --*

      Provides the name of the DB cluster parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB cluster parameter group is
      compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB cluster parameter group.

    - **DBClusterParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientCopyDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientCopyDbClusterParameterGroupResponseTypeDef",
    {
        "DBClusterParameterGroup": ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
    },
    total=False,
)


class ClientCopyDbClusterParameterGroupResponseTypeDef(
    _ClientCopyDbClusterParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientCopyDbClusterParameterGroup` `Response`

    - **DBClusterParameterGroup** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster parameter group.

      This data type is used as a response element in the  DescribeDBClusterParameterGroups action.

      - **DBClusterParameterGroupName** *(string) --*

        Provides the name of the DB cluster parameter group.

      - **DBParameterGroupFamily** *(string) --*

        Provides the name of the DB parameter group family that this DB cluster parameter group is
        compatible with.

      - **Description** *(string) --*

        Provides the customer-specified description for this DB cluster parameter group.

      - **DBClusterParameterGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientCopyDbClusterParameterGroupTagsTypeDef = TypedDict(
    "_ClientCopyDbClusterParameterGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCopyDbClusterParameterGroupTagsTypeDef(
    _ClientCopyDbClusterParameterGroupTagsTypeDef
):
    """
    Type definition for `ClientCopyDbClusterParameterGroup` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    Type definition for `ClientCopyDbClusterSnapshotResponse` `DBClusterSnapshot`

    Contains the details for an Amazon Neptune DB cluster snapshot

    This data type is used as a response element in the  DescribeDBClusterSnapshots action.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
      be restored in.

      - *(string) --*

    - **DBClusterSnapshotIdentifier** *(string) --*

      Specifies the identifier for the DB cluster snapshot.

    - **DBClusterIdentifier** *(string) --*

      Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
      created from.

    - **SnapshotCreateTime** *(datetime) --*

      Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

    - **Engine** *(string) --*

      Specifies the name of the database engine.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size in gibibytes (GiB).

    - **Status** *(string) --*

      Specifies the status of this DB cluster snapshot.

    - **Port** *(integer) --*

      Specifies the port that the DB cluster was listening on at the time of the snapshot.

    - **VpcId** *(string) --*

      Provides the VPC ID associated with the DB cluster snapshot.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **MasterUsername** *(string) --*

      Provides the master username for the DB cluster snapshot.

    - **EngineVersion** *(string) --*

      Provides the version of the database engine for this DB cluster snapshot.

    - **LicenseModel** *(string) --*

      Provides the license model information for this DB cluster snapshot.

    - **SnapshotType** *(string) --*

      Provides the type of the DB cluster snapshot.

    - **PercentProgress** *(integer) --*

      Specifies the percentage of the estimated data that has been transferred.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster snapshot is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster
      snapshot.

    - **DBClusterSnapshotArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster snapshot.

    - **SourceDBClusterSnapshotArn** *(string) --*

      If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon
      Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.
    """


_ClientCopyDbClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotResponseTypeDef",
    {"DBClusterSnapshot": ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef},
    total=False,
)


class ClientCopyDbClusterSnapshotResponseTypeDef(
    _ClientCopyDbClusterSnapshotResponseTypeDef
):
    """
    Type definition for `ClientCopyDbClusterSnapshot` `Response`

    - **DBClusterSnapshot** *(dict) --*

      Contains the details for an Amazon Neptune DB cluster snapshot

      This data type is used as a response element in the  DescribeDBClusterSnapshots action.

      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
        be restored in.

        - *(string) --*

      - **DBClusterSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB cluster snapshot.

      - **DBClusterIdentifier** *(string) --*

        Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
        created from.

      - **SnapshotCreateTime** *(datetime) --*

        Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

      - **Engine** *(string) --*

        Specifies the name of the database engine.

      - **AllocatedStorage** *(integer) --*

        Specifies the allocated storage size in gibibytes (GiB).

      - **Status** *(string) --*

        Specifies the status of this DB cluster snapshot.

      - **Port** *(integer) --*

        Specifies the port that the DB cluster was listening on at the time of the snapshot.

      - **VpcId** *(string) --*

        Provides the VPC ID associated with the DB cluster snapshot.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **MasterUsername** *(string) --*

        Provides the master username for the DB cluster snapshot.

      - **EngineVersion** *(string) --*

        Provides the version of the database engine for this DB cluster snapshot.

      - **LicenseModel** *(string) --*

        Provides the license model information for this DB cluster snapshot.

      - **SnapshotType** *(string) --*

        Provides the type of the DB cluster snapshot.

      - **PercentProgress** *(integer) --*

        Specifies the percentage of the estimated data that has been transferred.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster snapshot is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster
        snapshot.

      - **DBClusterSnapshotArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster snapshot.

      - **SourceDBClusterSnapshotArn** *(string) --*

        If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon
        Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
        is enabled, and otherwise false.
    """


_ClientCopyDbClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbClusterSnapshotTagsTypeDef(_ClientCopyDbClusterSnapshotTagsTypeDef):
    """
    Type definition for `ClientCopyDbClusterSnapshot` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef = TypedDict(
    "_ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)


class ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef(
    _ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef
):
    """
    Type definition for `ClientCopyDbParameterGroupResponse` `DBParameterGroup`

    Contains the details of an Amazon Neptune DB parameter group.

    This data type is used as a response element in the  DescribeDBParameterGroups action.

    - **DBParameterGroupName** *(string) --*

      Provides the name of the DB parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB parameter group is
      compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB parameter group.

    - **DBParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB parameter group.
    """


_ClientCopyDbParameterGroupResponseTypeDef = TypedDict(
    "_ClientCopyDbParameterGroupResponseTypeDef",
    {"DBParameterGroup": ClientCopyDbParameterGroupResponseDBParameterGroupTypeDef},
    total=False,
)


class ClientCopyDbParameterGroupResponseTypeDef(
    _ClientCopyDbParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientCopyDbParameterGroup` `Response`

    - **DBParameterGroup** *(dict) --*

      Contains the details of an Amazon Neptune DB parameter group.

      This data type is used as a response element in the  DescribeDBParameterGroups action.

      - **DBParameterGroupName** *(string) --*

        Provides the name of the DB parameter group.

      - **DBParameterGroupFamily** *(string) --*

        Provides the name of the DB parameter group family that this DB parameter group is
        compatible with.

      - **Description** *(string) --*

        Provides the customer-specified description for this DB parameter group.

      - **DBParameterGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB parameter group.
    """


_ClientCopyDbParameterGroupTagsTypeDef = TypedDict(
    "_ClientCopyDbParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbParameterGroupTagsTypeDef(_ClientCopyDbParameterGroupTagsTypeDef):
    """
    Type definition for `ClientCopyDbParameterGroup` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef = TypedDict(
    "_ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef(
    _ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
):
    """
    Type definition for `ClientCreateDbClusterParameterGroupResponse` `DBClusterParameterGroup`

    Contains the details of an Amazon Neptune DB cluster parameter group.

    This data type is used as a response element in the  DescribeDBClusterParameterGroups action.

    - **DBClusterParameterGroupName** *(string) --*

      Provides the name of the DB cluster parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB cluster parameter group is
      compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB cluster parameter group.

    - **DBClusterParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientCreateDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientCreateDbClusterParameterGroupResponseTypeDef",
    {
        "DBClusterParameterGroup": ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
    },
    total=False,
)


class ClientCreateDbClusterParameterGroupResponseTypeDef(
    _ClientCreateDbClusterParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateDbClusterParameterGroup` `Response`

    - **DBClusterParameterGroup** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster parameter group.

      This data type is used as a response element in the  DescribeDBClusterParameterGroups action.

      - **DBClusterParameterGroupName** *(string) --*

        Provides the name of the DB cluster parameter group.

      - **DBParameterGroupFamily** *(string) --*

        Provides the name of the DB parameter group family that this DB cluster parameter group is
        compatible with.

      - **Description** *(string) --*

        Provides the customer-specified description for this DB cluster parameter group.

      - **DBClusterParameterGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientCreateDbClusterParameterGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterParameterGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateDbClusterParameterGroupTagsTypeDef(
    _ClientCreateDbClusterParameterGroupTagsTypeDef
):
    """
    Type definition for `ClientCreateDbClusterParameterGroup` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientCreateDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The Status
      property returns one of the following values:

      * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
      is unable to assume the IAM role in order to access other AWS services on your behalf.
    """


_ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientCreateDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      Value that is ``true`` if the cluster member is the primary instance for the DB cluster
      and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.
    """


_ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientCreateDbClusterResponseDBCluster` `DBClusterOptionGroupMemberships`

    Contains status information for a DB cluster option group.

    - **DBClusterOptionGroupName** *(string) --*

      Specifies the name of the DB cluster option group.

    - **Status** *(string) --*

      Specifies the status of the DB cluster option group.
    """


_ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientCreateDbClusterResponseDBCluster` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientCreateDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientCreateDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientCreateDbClusterResponseDBClusterTypeDef(
    _ClientCreateDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientCreateDbClusterResponse` `DBCluster`

    Contains the details of an Amazon Neptune DB cluster.

    This data type is used as a response element in the  DescribeDBClusters action.

    - **AllocatedStorage** *(integer) --*

       ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
       fixed, but instead automatically adjusts as needed.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
      in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this cluster is associated with.

    - **DatabaseName** *(string) --*

      Contains the name of the initial database of this DB cluster that was provided at create
      time, if one was specified when the DB cluster was created. This same name is returned for
      the life of the DB cluster.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group associated with the DB cluster, including the
      name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      Specifies the earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
      connections across the Read Replicas that are available in a DB cluster. As clients request
      new connections to the reader endpoint, Neptune distributes the connection requests among
      the Read Replicas in the DB cluster. This functionality can help balance your read workload
      across multiple Read Replicas in your DB cluster.

      If a failover occurs, and the Read Replica that you are connected to is promoted to be the
      primary instance, your connection is dropped. To continue sending your read workload to
      other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB cluster.

    - **DBClusterOptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB cluster.

      - *(dict) --*

        Contains status information for a DB cluster option group.

        - **DBClusterOptionGroupName** *(string) --*

          Specifies the name of the DB cluster option group.

        - **Status** *(string) --*

          Specifies the status of the DB cluster option group.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **ReplicationSourceIdentifier** *(string) --*

      Not supported by Neptune.

    - **ReadReplicaIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB cluster.

      - *(string) --*

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          Value that is ``true`` if the cluster member is the primary instance for the DB cluster
          and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security groups that the DB cluster belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The Status
          property returns one of the following values:

          * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
          is unable to assume the IAM role in order to access other AWS services on your behalf.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.

    - **CloneGroupId** *(string) --*

      Identifies the clone group to which the DB cluster is associated.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientCreateDbClusterResponseTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseTypeDef",
    {"DBCluster": ClientCreateDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientCreateDbClusterResponseTypeDef(_ClientCreateDbClusterResponseTypeDef):
    """
    Type definition for `ClientCreateDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.

      This data type is used as a response element in the  DescribeDBClusters action.

      - **AllocatedStorage** *(integer) --*

         ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
         fixed, but instead automatically adjusts as needed.

      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
        in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this cluster is associated with.

      - **DatabaseName** *(string) --*

        Contains the name of the initial database of this DB cluster that was provided at create
        time, if one was specified when the DB cluster was created. This same name is returned for
        the life of the DB cluster.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group associated with the DB cluster, including the
        name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        Specifies the earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
        connections across the Read Replicas that are available in a DB cluster. As clients request
        new connections to the reader endpoint, Neptune distributes the connection requests among
        the Read Replicas in the DB cluster. This functionality can help balance your read workload
        across multiple Read Replicas in your DB cluster.

        If a failover occurs, and the Read Replica that you are connected to is promoted to be the
        primary instance, your connection is dropped. To continue sending your read workload to
        other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB cluster.

      - **DBClusterOptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB cluster.

        - *(dict) --*

          Contains status information for a DB cluster option group.

          - **DBClusterOptionGroupName** *(string) --*

            Specifies the name of the DB cluster option group.

          - **Status** *(string) --*

            Specifies the status of the DB cluster option group.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **ReplicationSourceIdentifier** *(string) --*

        Not supported by Neptune.

      - **ReadReplicaIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB cluster.

        - *(string) --*

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            Value that is ``true`` if the cluster member is the primary instance for the DB cluster
            and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which a Read Replica is promoted to the primary
            instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security groups that the DB cluster belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The Status
            property returns one of the following values:

            * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
            is unable to assume the IAM role in order to access other AWS services on your behalf.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
        is enabled, and otherwise false.

      - **CloneGroupId** *(string) --*

        Identifies the clone group to which the DB cluster is associated.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    Type definition for `ClientCreateDbClusterSnapshotResponse` `DBClusterSnapshot`

    Contains the details for an Amazon Neptune DB cluster snapshot

    This data type is used as a response element in the  DescribeDBClusterSnapshots action.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
      be restored in.

      - *(string) --*

    - **DBClusterSnapshotIdentifier** *(string) --*

      Specifies the identifier for the DB cluster snapshot.

    - **DBClusterIdentifier** *(string) --*

      Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
      created from.

    - **SnapshotCreateTime** *(datetime) --*

      Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

    - **Engine** *(string) --*

      Specifies the name of the database engine.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size in gibibytes (GiB).

    - **Status** *(string) --*

      Specifies the status of this DB cluster snapshot.

    - **Port** *(integer) --*

      Specifies the port that the DB cluster was listening on at the time of the snapshot.

    - **VpcId** *(string) --*

      Provides the VPC ID associated with the DB cluster snapshot.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **MasterUsername** *(string) --*

      Provides the master username for the DB cluster snapshot.

    - **EngineVersion** *(string) --*

      Provides the version of the database engine for this DB cluster snapshot.

    - **LicenseModel** *(string) --*

      Provides the license model information for this DB cluster snapshot.

    - **SnapshotType** *(string) --*

      Provides the type of the DB cluster snapshot.

    - **PercentProgress** *(integer) --*

      Specifies the percentage of the estimated data that has been transferred.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster snapshot is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster
      snapshot.

    - **DBClusterSnapshotArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster snapshot.

    - **SourceDBClusterSnapshotArn** *(string) --*

      If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon
      Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.
    """


_ClientCreateDbClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotResponseTypeDef",
    {
        "DBClusterSnapshot": ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef
    },
    total=False,
)


class ClientCreateDbClusterSnapshotResponseTypeDef(
    _ClientCreateDbClusterSnapshotResponseTypeDef
):
    """
    Type definition for `ClientCreateDbClusterSnapshot` `Response`

    - **DBClusterSnapshot** *(dict) --*

      Contains the details for an Amazon Neptune DB cluster snapshot

      This data type is used as a response element in the  DescribeDBClusterSnapshots action.

      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
        be restored in.

        - *(string) --*

      - **DBClusterSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB cluster snapshot.

      - **DBClusterIdentifier** *(string) --*

        Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
        created from.

      - **SnapshotCreateTime** *(datetime) --*

        Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

      - **Engine** *(string) --*

        Specifies the name of the database engine.

      - **AllocatedStorage** *(integer) --*

        Specifies the allocated storage size in gibibytes (GiB).

      - **Status** *(string) --*

        Specifies the status of this DB cluster snapshot.

      - **Port** *(integer) --*

        Specifies the port that the DB cluster was listening on at the time of the snapshot.

      - **VpcId** *(string) --*

        Provides the VPC ID associated with the DB cluster snapshot.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **MasterUsername** *(string) --*

        Provides the master username for the DB cluster snapshot.

      - **EngineVersion** *(string) --*

        Provides the version of the database engine for this DB cluster snapshot.

      - **LicenseModel** *(string) --*

        Provides the license model information for this DB cluster snapshot.

      - **SnapshotType** *(string) --*

        Provides the type of the DB cluster snapshot.

      - **PercentProgress** *(integer) --*

        Specifies the percentage of the estimated data that has been transferred.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster snapshot is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster
        snapshot.

      - **DBClusterSnapshotArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster snapshot.

      - **SourceDBClusterSnapshotArn** *(string) --*

        If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon
        Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
        is enabled, and otherwise false.
    """


_ClientCreateDbClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterSnapshotTagsTypeDef(
    _ClientCreateDbClusterSnapshotTagsTypeDef
):
    """
    Type definition for `ClientCreateDbClusterSnapshot` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterTagsTypeDef(_ClientCreateDbClusterTagsTypeDef):
    """
    Type definition for `ClientCreateDbCluster` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `DBParameterGroups`

    The status of the DB parameter group.

    This data type is used as a response element in the following actions:

    *  CreateDBInstance

    *  DeleteDBInstance

    *  ModifyDBInstance

    *  RebootDBInstance

    - **DBParameterGroupName** *(string) --*

      The name of the DP parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.
    """


_ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `DBSecurityGroups`

    Specifies membership in a designated DB security group.

    - **DBSecurityGroupName** *(string) --*

      The name of the DB security group.

    - **Status** *(string) --*

      The status of the DB security group.
    """


_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the EC2 Availability Zone that the subnet is in.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstanceDBSubnetGroup` `Subnets`

    Specifies a subnet.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the EC2 Availability Zone that the subnet is in.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `DBSubnetGroup`

    Specifies information on the subnet group associated with the DB instance, including the
    name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the VpcId of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Contains a list of  Subnet elements.

      - *(dict) --*

        Specifies a subnet.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the EC2 Availability Zone that the subnet is in.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `DomainMemberships`

    An Active Directory Domain membership record associated with a DB instance.

    - **Domain** *(string) --*

      The identifier of the Active Directory Domain.

    - **Status** *(string) --*

      The status of the DB instance's Active Directory Domain membership, such as joined,
      pending-join, failed etc).

    - **FQDN** *(string) --*

      The fully qualified domain name of the Active Directory Domain.

    - **IAMRoleName** *(string) --*

      The name of the IAM role to be used when making API calls to the Directory Service.
    """


_ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `OptionGroupMemberships`

    Provides information on the option groups the DB instance is a member of.

    - **OptionGroupName** *(string) --*

      The name of the option group that the instance belongs to.

    - **Status** *(string) --*

      The status of the DB instance's option group membership. Valid values are: ``in-sync``
      , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
      ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .
    """


_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstancePendingModifiedValues` `PendingCloudwatchLogsExports`

    Specifies the CloudWatch logs to be exported.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to CloudWatch Logs.

      - *(string) --*
    """


_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is only included when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
      currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently-in-progress change of the master credentials for the DB
      instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` | ``bring-your-own-license`` |
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
      currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the CA certificate for the DB instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      Specifies the CloudWatch logs to be exported.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to CloudWatch Logs.

        - *(string) --*
    """


_ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "read replication."

    - **Normal** *(boolean) --*

      Boolean value that is true if the instance is operating normally, or false if the
      instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a StatusType of read replica, the values can be
      replicating, error, stopped, or terminated.

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientCreateDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientCreateDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientCreateDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientCreateDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientCreateDbInstanceResponseDBInstanceDomainMembershipsTypeDef
        ],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponse` `DBInstance`

    Contains the details of an Amazon Neptune DB instance.

    This data type is used as a response element in the  DescribeDBInstances action.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-supplied database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB instance.

    - **DBName** *(string) --*

      The database name.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size specified in gibibytes.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBSecurityGroups** *(list) --*

      Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
      ``DBSecurityGroup.Status`` subelements.

      - *(dict) --*

        Specifies membership in a designated DB security group.

        - **DBSecurityGroupName** *(string) --*

          The name of the DB security group.

        - **Status** *(string) --*

          The status of the DB security group.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **DBParameterGroups** *(list) --*

      Provides the list of DB parameter groups applied to this DB instance.

      - *(dict) --*

        The status of the DB parameter group.

        This data type is used as a response element in the following actions:

        *  CreateDBInstance

        *  DeleteDBInstance

        *  ModifyDBInstance

        *  RebootDBInstance

        - **DBParameterGroupName** *(string) --*

          The name of the DP parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group associated with the DB instance, including the
      name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the VpcId of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Contains a list of  Subnet elements.

        - *(dict) --*

          Specifies a subnet.

          This data type is used as a response element in the  DescribeDBSubnetGroups action.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the EC2 Availability Zone that the subnet is in.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is only included when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
        currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently-in-progress change of the master credentials for the DB
        instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` | ``bring-your-own-license`` |
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
        currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the CA certificate for the DB instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        Specifies the CloudWatch logs to be exported.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **MultiAZ** *(boolean) --*

      Specifies if the DB instance is a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

      Contains the identifier of the source DB instance if this DB instance is a Read Replica.

    - **ReadReplicaDBInstanceIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB instance.

      - *(string) --*

    - **ReadReplicaDBClusterIdentifiers** *(list) --*

      Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

      - *(string) --*

    - **LicenseModel** *(string) --*

      License model information for this DB instance.

    - **Iops** *(integer) --*

      Specifies the Provisioned IOPS (I/O operations per second) value.

    - **OptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB instance.

      - *(dict) --*

        Provides information on the option groups the DB instance is a member of.

        - **OptionGroupName** *(string) --*

          The name of the option group that the instance belongs to.

        - **Status** *(string) --*

          The status of the DB instance's option group membership. Valid values are: ``in-sync``
          , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
          ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this instance is associated with.

    - **SecondaryAvailabilityZone** *(string) --*

      If present, specifies the name of the secondary Availability Zone for a DB instance with
      multi-AZ support.

    - **PubliclyAccessible** *(boolean) --*

      This flag should no longer be used.

    - **StatusInfos** *(list) --*

      The status of a Read Replica. If the instance is not a Read Replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "read replication."

        - **Normal** *(boolean) --*

          Boolean value that is true if the instance is operating normally, or false if the
          instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a StatusType of read replica, the values can be
          replicating, error, stopped, or terminated.

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **StorageType** *(string) --*

      Specifies the storage type associated with DB instance.

    - **TdeCredentialArn** *(string) --*

      The ARN from the key store with which the instance is associated for TDE encryption.

    - **DbInstancePort** *(integer) --*

      Specifies the port that the DB instance listens on. If the DB instance is part of a DB
      cluster, this can be a different port than the DB cluster port.

    - **DBClusterIdentifier** *(string) --*

      If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
      the DB instance is a member of.

    - **StorageEncrypted** *(boolean) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **KmsKeyId** *(string) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **DomainMemberships** *(list) --*

      Not supported

      - *(dict) --*

        An Active Directory Domain membership record associated with a DB instance.

        - **Domain** *(string) --*

          The identifier of the Active Directory Domain.

        - **Status** *(string) --*

          The status of the DB instance's Active Directory Domain membership, such as joined,
          pending-join, failed etc).

        - **FQDN** *(string) --*

          The fully qualified domain name of the Active Directory Domain.

        - **IAMRoleName** *(string) --*

          The name of the IAM role to be used when making API calls to the Directory Service.

    - **CopyTagsToSnapshot** *(boolean) --*

      Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

    - **MonitoringInterval** *(integer) --*

      The interval, in seconds, between points when Enhanced Monitoring metrics are collected for
      the DB instance.

    - **EnhancedMonitoringResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
      Enhanced Monitoring metrics data for the DB instance.

    - **MonitoringRoleArn** *(string) --*

      The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon
      CloudWatch Logs.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **Timezone** *(string) --*

      Not supported.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
      false.

    - **PerformanceInsightsEnabled** *(boolean) --*

      True if Performance Insights is enabled for the DB instance, and otherwise false.

    - **PerformanceInsightsKMSKeyId** *(string) --*

      The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
      the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
      encryption key.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientCreateDbInstanceResponseTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseTypeDef",
    {"DBInstance": ClientCreateDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientCreateDbInstanceResponseTypeDef(_ClientCreateDbInstanceResponseTypeDef):
    """
    Type definition for `ClientCreateDbInstance` `Response`

    - **DBInstance** *(dict) --*

      Contains the details of an Amazon Neptune DB instance.

      This data type is used as a response element in the  DescribeDBInstances action.

      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.

      - **DBInstanceClass** *(string) --*

        Contains the name of the compute and memory capacity class of the DB instance.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB instance.

      - **DBInstanceStatus** *(string) --*

        Specifies the current state of this database.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB instance.

      - **DBName** *(string) --*

        The database name.

      - **Endpoint** *(dict) --*

        Specifies the connection endpoint.

        - **Address** *(string) --*

          Specifies the DNS address of the DB instance.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **AllocatedStorage** *(integer) --*

        Specifies the allocated storage size specified in gibibytes.

      - **InstanceCreateTime** *(datetime) --*

        Provides the date and time the DB instance was created.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBSecurityGroups** *(list) --*

        Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
        ``DBSecurityGroup.Status`` subelements.

        - *(dict) --*

          Specifies membership in a designated DB security group.

          - **DBSecurityGroupName** *(string) --*

            The name of the DB security group.

          - **Status** *(string) --*

            The status of the DB security group.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security group elements that the DB instance belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **DBParameterGroups** *(list) --*

        Provides the list of DB parameter groups applied to this DB instance.

        - *(dict) --*

          The status of the DB parameter group.

          This data type is used as a response element in the following actions:

          *  CreateDBInstance

          *  DeleteDBInstance

          *  ModifyDBInstance

          *  RebootDBInstance

          - **DBParameterGroupName** *(string) --*

            The name of the DP parameter group.

          - **ParameterApplyStatus** *(string) --*

            The status of parameter updates.

      - **AvailabilityZone** *(string) --*

        Specifies the name of the Availability Zone the DB instance is located in.

      - **DBSubnetGroup** *(dict) --*

        Specifies information on the subnet group associated with the DB instance, including the
        name, description, and subnets in the subnet group.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the VpcId of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Contains a list of  Subnet elements.

          - *(dict) --*

            Specifies a subnet.

            This data type is used as a response element in the  DescribeDBSubnetGroups action.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the EC2 Availability Zone that the subnet is in.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **PendingModifiedValues** *(dict) --*

        Specifies that changes to the DB instance are pending. This element is only included when
        changes are pending. Specific changes are identified by subelements.

        - **DBInstanceClass** *(string) --*

          Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
          currently being applied.

        - **AllocatedStorage** *(integer) --*

          Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
          currently being applied.

        - **MasterUserPassword** *(string) --*

          Contains the pending or currently-in-progress change of the master credentials for the DB
          instance.

        - **Port** *(integer) --*

          Specifies the pending port for the DB instance.

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the pending number of days for which automated backups are retained.

        - **MultiAZ** *(boolean) --*

          Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LicenseModel** *(string) --*

          The license model for the DB instance.

          Valid values: ``license-included`` | ``bring-your-own-license`` |
          ``general-public-license``

        - **Iops** *(integer) --*

          Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
          currently being applied.

        - **DBInstanceIdentifier** *(string) --*

          Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
          currently being applied.

        - **StorageType** *(string) --*

          Specifies the storage type to be associated with the DB instance.

        - **CACertificateIdentifier** *(string) --*

          Specifies the identifier of the CA certificate for the DB instance.

        - **DBSubnetGroupName** *(string) --*

          The new DB subnet group for the DB instance.

        - **PendingCloudwatchLogsExports** *(dict) --*

          Specifies the CloudWatch logs to be exported.

          - **LogTypesToEnable** *(list) --*

            Log types that are in the process of being deactivated. After they are deactivated,
            these log types aren't exported to CloudWatch Logs.

            - *(string) --*

          - **LogTypesToDisable** *(list) --*

            Log types that are in the process of being enabled. After they are enabled, these log
            types are exported to CloudWatch Logs.

            - *(string) --*

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **MultiAZ** *(boolean) --*

        Specifies if the DB instance is a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Indicates that minor version patches are applied automatically.

      - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

        Contains the identifier of the source DB instance if this DB instance is a Read Replica.

      - **ReadReplicaDBInstanceIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB instance.

        - *(string) --*

      - **ReadReplicaDBClusterIdentifiers** *(list) --*

        Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

        - *(string) --*

      - **LicenseModel** *(string) --*

        License model information for this DB instance.

      - **Iops** *(integer) --*

        Specifies the Provisioned IOPS (I/O operations per second) value.

      - **OptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB instance.

        - *(dict) --*

          Provides information on the option groups the DB instance is a member of.

          - **OptionGroupName** *(string) --*

            The name of the option group that the instance belongs to.

          - **Status** *(string) --*

            The status of the DB instance's option group membership. Valid values are: ``in-sync``
            , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
            ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this instance is associated with.

      - **SecondaryAvailabilityZone** *(string) --*

        If present, specifies the name of the secondary Availability Zone for a DB instance with
        multi-AZ support.

      - **PubliclyAccessible** *(boolean) --*

        This flag should no longer be used.

      - **StatusInfos** *(list) --*

        The status of a Read Replica. If the instance is not a Read Replica, this is blank.

        - *(dict) --*

          Provides a list of status information for a DB instance.

          - **StatusType** *(string) --*

            This value is currently "read replication."

          - **Normal** *(boolean) --*

            Boolean value that is true if the instance is operating normally, or false if the
            instance is in an error state.

          - **Status** *(string) --*

            Status of the DB instance. For a StatusType of read replica, the values can be
            replicating, error, stopped, or terminated.

          - **Message** *(string) --*

            Details of the error if there is an error for the instance. If the instance is not in
            an error state, this value is blank.

      - **StorageType** *(string) --*

        Specifies the storage type associated with DB instance.

      - **TdeCredentialArn** *(string) --*

        The ARN from the key store with which the instance is associated for TDE encryption.

      - **DbInstancePort** *(integer) --*

        Specifies the port that the DB instance listens on. If the DB instance is part of a DB
        cluster, this can be a different port than the DB cluster port.

      - **DBClusterIdentifier** *(string) --*

        If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
        the DB instance is a member of.

      - **StorageEncrypted** *(boolean) --*

        Not supported: The encryption for DB instances is managed by the DB cluster.

      - **KmsKeyId** *(string) --*

        Not supported: The encryption for DB instances is managed by the DB cluster.

      - **DbiResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
        in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

      - **CACertificateIdentifier** *(string) --*

        The identifier of the CA certificate for this DB instance.

      - **DomainMemberships** *(list) --*

        Not supported

        - *(dict) --*

          An Active Directory Domain membership record associated with a DB instance.

          - **Domain** *(string) --*

            The identifier of the Active Directory Domain.

          - **Status** *(string) --*

            The status of the DB instance's Active Directory Domain membership, such as joined,
            pending-join, failed etc).

          - **FQDN** *(string) --*

            The fully qualified domain name of the Active Directory Domain.

          - **IAMRoleName** *(string) --*

            The name of the IAM role to be used when making API calls to the Directory Service.

      - **CopyTagsToSnapshot** *(boolean) --*

        Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

      - **MonitoringInterval** *(integer) --*

        The interval, in seconds, between points when Enhanced Monitoring metrics are collected for
        the DB instance.

      - **EnhancedMonitoringResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
        Enhanced Monitoring metrics data for the DB instance.

      - **MonitoringRoleArn** *(string) --*

        The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon
        CloudWatch Logs.

      - **PromotionTier** *(integer) --*

        A value that specifies the order in which a Read Replica is promoted to the primary
        instance after a failure of the existing primary instance.

      - **DBInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB instance.

      - **Timezone** *(string) --*

        Not supported.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
        false.

      - **PerformanceInsightsEnabled** *(boolean) --*

        True if Performance Insights is enabled for the DB instance, and otherwise false.

      - **PerformanceInsightsKMSKeyId** *(string) --*

        The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
        the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
        encryption key.

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB instance is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientCreateDbInstanceTagsTypeDef = TypedDict(
    "_ClientCreateDbInstanceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbInstanceTagsTypeDef(_ClientCreateDbInstanceTagsTypeDef):
    """
    Type definition for `ClientCreateDbInstance` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef = TypedDict(
    "_ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)


class ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef(
    _ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef
):
    """
    Type definition for `ClientCreateDbParameterGroupResponse` `DBParameterGroup`

    Contains the details of an Amazon Neptune DB parameter group.

    This data type is used as a response element in the  DescribeDBParameterGroups action.

    - **DBParameterGroupName** *(string) --*

      Provides the name of the DB parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB parameter group is
      compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB parameter group.

    - **DBParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB parameter group.
    """


_ClientCreateDbParameterGroupResponseTypeDef = TypedDict(
    "_ClientCreateDbParameterGroupResponseTypeDef",
    {"DBParameterGroup": ClientCreateDbParameterGroupResponseDBParameterGroupTypeDef},
    total=False,
)


class ClientCreateDbParameterGroupResponseTypeDef(
    _ClientCreateDbParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateDbParameterGroup` `Response`

    - **DBParameterGroup** *(dict) --*

      Contains the details of an Amazon Neptune DB parameter group.

      This data type is used as a response element in the  DescribeDBParameterGroups action.

      - **DBParameterGroupName** *(string) --*

        Provides the name of the DB parameter group.

      - **DBParameterGroupFamily** *(string) --*

        Provides the name of the DB parameter group family that this DB parameter group is
        compatible with.

      - **Description** *(string) --*

        Provides the customer-specified description for this DB parameter group.

      - **DBParameterGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB parameter group.
    """


_ClientCreateDbParameterGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbParameterGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbParameterGroupTagsTypeDef(_ClientCreateDbParameterGroupTagsTypeDef):
    """
    Type definition for `ClientCreateDbParameterGroup` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the EC2 Availability Zone that the subnet is in.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef(
    _ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientCreateDbSubnetGroupResponseDBSubnetGroup` `Subnets`

    Specifies a subnet.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the EC2 Availability Zone that the subnet is in.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef(
    _ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientCreateDbSubnetGroupResponse` `DBSubnetGroup`

    Contains the details of an Amazon Neptune DB subnet group.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the VpcId of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Contains a list of  Subnet elements.

      - *(dict) --*

        Specifies a subnet.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the EC2 Availability Zone that the subnet is in.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientCreateDbSubnetGroupResponseTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseTypeDef",
    {"DBSubnetGroup": ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef},
    total=False,
)


class ClientCreateDbSubnetGroupResponseTypeDef(
    _ClientCreateDbSubnetGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateDbSubnetGroup` `Response`

    - **DBSubnetGroup** *(dict) --*

      Contains the details of an Amazon Neptune DB subnet group.

      This data type is used as a response element in the  DescribeDBSubnetGroups action.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the VpcId of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Contains a list of  Subnet elements.

        - *(dict) --*

          Specifies a subnet.

          This data type is used as a response element in the  DescribeDBSubnetGroups action.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the EC2 Availability Zone that the subnet is in.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientCreateDbSubnetGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbSubnetGroupTagsTypeDef(_ClientCreateDbSubnetGroupTagsTypeDef):
    """
    Type definition for `ClientCreateDbSubnetGroup` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    Type definition for `ClientCreateEventSubscriptionResponse` `EventSubscription`

    Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the event notification subscription.

    - **Status** *(string) --*

      The status of the event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that Neptune no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the event notification subscription was created.

    - **SourceType** *(string) --*

      The source type for the event notification subscription.

    - **SourceIdsList** *(list) --*

      A list of source IDs for the event notification subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A list of event categories for the event notification subscription.

      - *(string) --*

    - **Enabled** *(boolean) --*

      A Boolean value indicating if the subscription is enabled. True indicates the subscription
      is enabled.

    - **EventSubscriptionArn** *(string) --*

      The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientCreateEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef
    },
    total=False,
)


class ClientCreateEventSubscriptionResponseTypeDef(
    _ClientCreateEventSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientCreateEventSubscription` `Response`

    - **EventSubscription** *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.

      - **CustSubscriptionId** *(string) --*

        The event notification subscription Id.

      - **SnsTopicArn** *(string) --*

        The topic ARN of the event notification subscription.

      - **Status** *(string) --*

        The status of the event notification subscription.

        Constraints:

        Can be one of the following: creating | modifying | deleting | active | no-permission |
        topic-not-exist

        The status "no-permission" indicates that Neptune no longer has permission to post to the
        SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
        subscription was created.

      - **SubscriptionCreationTime** *(string) --*

        The time the event notification subscription was created.

      - **SourceType** *(string) --*

        The source type for the event notification subscription.

      - **SourceIdsList** *(list) --*

        A list of source IDs for the event notification subscription.

        - *(string) --*

      - **EventCategoriesList** *(list) --*

        A list of event categories for the event notification subscription.

        - *(string) --*

      - **Enabled** *(boolean) --*

        A Boolean value indicating if the subscription is enabled. True indicates the subscription
        is enabled.

      - **EventSubscriptionArn** *(string) --*

        The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientCreateEventSubscriptionTagsTypeDef = TypedDict(
    "_ClientCreateEventSubscriptionTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateEventSubscriptionTagsTypeDef(
    _ClientCreateEventSubscriptionTagsTypeDef
):
    """
    Type definition for `ClientCreateEventSubscription` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The Status
      property returns one of the following values:

      * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
      is unable to assume the IAM role in order to access other AWS services on your behalf.
    """


_ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      Value that is ``true`` if the cluster member is the primary instance for the DB cluster
      and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.
    """


_ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterResponseDBCluster` `DBClusterOptionGroupMemberships`

    Contains status information for a DB cluster option group.

    - **DBClusterOptionGroupName** *(string) --*

      Specifies the name of the DB cluster option group.

    - **Status** *(string) --*

      Specifies the status of the DB cluster option group.
    """


_ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterResponseDBCluster` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientDeleteDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientDeleteDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterTypeDef(
    _ClientDeleteDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterResponse` `DBCluster`

    Contains the details of an Amazon Neptune DB cluster.

    This data type is used as a response element in the  DescribeDBClusters action.

    - **AllocatedStorage** *(integer) --*

       ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
       fixed, but instead automatically adjusts as needed.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
      in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this cluster is associated with.

    - **DatabaseName** *(string) --*

      Contains the name of the initial database of this DB cluster that was provided at create
      time, if one was specified when the DB cluster was created. This same name is returned for
      the life of the DB cluster.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group associated with the DB cluster, including the
      name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      Specifies the earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
      connections across the Read Replicas that are available in a DB cluster. As clients request
      new connections to the reader endpoint, Neptune distributes the connection requests among
      the Read Replicas in the DB cluster. This functionality can help balance your read workload
      across multiple Read Replicas in your DB cluster.

      If a failover occurs, and the Read Replica that you are connected to is promoted to be the
      primary instance, your connection is dropped. To continue sending your read workload to
      other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB cluster.

    - **DBClusterOptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB cluster.

      - *(dict) --*

        Contains status information for a DB cluster option group.

        - **DBClusterOptionGroupName** *(string) --*

          Specifies the name of the DB cluster option group.

        - **Status** *(string) --*

          Specifies the status of the DB cluster option group.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **ReplicationSourceIdentifier** *(string) --*

      Not supported by Neptune.

    - **ReadReplicaIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB cluster.

      - *(string) --*

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          Value that is ``true`` if the cluster member is the primary instance for the DB cluster
          and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security groups that the DB cluster belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The Status
          property returns one of the following values:

          * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
          is unable to assume the IAM role in order to access other AWS services on your behalf.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.

    - **CloneGroupId** *(string) --*

      Identifies the clone group to which the DB cluster is associated.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientDeleteDbClusterResponseTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseTypeDef",
    {"DBCluster": ClientDeleteDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientDeleteDbClusterResponseTypeDef(_ClientDeleteDbClusterResponseTypeDef):
    """
    Type definition for `ClientDeleteDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.

      This data type is used as a response element in the  DescribeDBClusters action.

      - **AllocatedStorage** *(integer) --*

         ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
         fixed, but instead automatically adjusts as needed.

      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
        in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this cluster is associated with.

      - **DatabaseName** *(string) --*

        Contains the name of the initial database of this DB cluster that was provided at create
        time, if one was specified when the DB cluster was created. This same name is returned for
        the life of the DB cluster.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group associated with the DB cluster, including the
        name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        Specifies the earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
        connections across the Read Replicas that are available in a DB cluster. As clients request
        new connections to the reader endpoint, Neptune distributes the connection requests among
        the Read Replicas in the DB cluster. This functionality can help balance your read workload
        across multiple Read Replicas in your DB cluster.

        If a failover occurs, and the Read Replica that you are connected to is promoted to be the
        primary instance, your connection is dropped. To continue sending your read workload to
        other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB cluster.

      - **DBClusterOptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB cluster.

        - *(dict) --*

          Contains status information for a DB cluster option group.

          - **DBClusterOptionGroupName** *(string) --*

            Specifies the name of the DB cluster option group.

          - **Status** *(string) --*

            Specifies the status of the DB cluster option group.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **ReplicationSourceIdentifier** *(string) --*

        Not supported by Neptune.

      - **ReadReplicaIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB cluster.

        - *(string) --*

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            Value that is ``true`` if the cluster member is the primary instance for the DB cluster
            and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which a Read Replica is promoted to the primary
            instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security groups that the DB cluster belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The Status
            property returns one of the following values:

            * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
            is unable to assume the IAM role in order to access other AWS services on your behalf.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
        is enabled, and otherwise false.

      - **CloneGroupId** *(string) --*

        Identifies the clone group to which the DB cluster is associated.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterSnapshotResponse` `DBClusterSnapshot`

    Contains the details for an Amazon Neptune DB cluster snapshot

    This data type is used as a response element in the  DescribeDBClusterSnapshots action.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
      be restored in.

      - *(string) --*

    - **DBClusterSnapshotIdentifier** *(string) --*

      Specifies the identifier for the DB cluster snapshot.

    - **DBClusterIdentifier** *(string) --*

      Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
      created from.

    - **SnapshotCreateTime** *(datetime) --*

      Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

    - **Engine** *(string) --*

      Specifies the name of the database engine.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size in gibibytes (GiB).

    - **Status** *(string) --*

      Specifies the status of this DB cluster snapshot.

    - **Port** *(integer) --*

      Specifies the port that the DB cluster was listening on at the time of the snapshot.

    - **VpcId** *(string) --*

      Provides the VPC ID associated with the DB cluster snapshot.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **MasterUsername** *(string) --*

      Provides the master username for the DB cluster snapshot.

    - **EngineVersion** *(string) --*

      Provides the version of the database engine for this DB cluster snapshot.

    - **LicenseModel** *(string) --*

      Provides the license model information for this DB cluster snapshot.

    - **SnapshotType** *(string) --*

      Provides the type of the DB cluster snapshot.

    - **PercentProgress** *(integer) --*

      Specifies the percentage of the estimated data that has been transferred.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster snapshot is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster
      snapshot.

    - **DBClusterSnapshotArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster snapshot.

    - **SourceDBClusterSnapshotArn** *(string) --*

      If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon
      Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.
    """


_ClientDeleteDbClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteDbClusterSnapshotResponseTypeDef",
    {
        "DBClusterSnapshot": ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef
    },
    total=False,
)


class ClientDeleteDbClusterSnapshotResponseTypeDef(
    _ClientDeleteDbClusterSnapshotResponseTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterSnapshot` `Response`

    - **DBClusterSnapshot** *(dict) --*

      Contains the details for an Amazon Neptune DB cluster snapshot

      This data type is used as a response element in the  DescribeDBClusterSnapshots action.

      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
        be restored in.

        - *(string) --*

      - **DBClusterSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB cluster snapshot.

      - **DBClusterIdentifier** *(string) --*

        Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
        created from.

      - **SnapshotCreateTime** *(datetime) --*

        Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

      - **Engine** *(string) --*

        Specifies the name of the database engine.

      - **AllocatedStorage** *(integer) --*

        Specifies the allocated storage size in gibibytes (GiB).

      - **Status** *(string) --*

        Specifies the status of this DB cluster snapshot.

      - **Port** *(integer) --*

        Specifies the port that the DB cluster was listening on at the time of the snapshot.

      - **VpcId** *(string) --*

        Provides the VPC ID associated with the DB cluster snapshot.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **MasterUsername** *(string) --*

        Provides the master username for the DB cluster snapshot.

      - **EngineVersion** *(string) --*

        Provides the version of the database engine for this DB cluster snapshot.

      - **LicenseModel** *(string) --*

        Provides the license model information for this DB cluster snapshot.

      - **SnapshotType** *(string) --*

        Provides the type of the DB cluster snapshot.

      - **PercentProgress** *(integer) --*

        Specifies the percentage of the estimated data that has been transferred.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster snapshot is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster
        snapshot.

      - **DBClusterSnapshotArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster snapshot.

      - **SourceDBClusterSnapshotArn** *(string) --*

        If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon
        Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
        is enabled, and otherwise false.
    """


_ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `DBParameterGroups`

    The status of the DB parameter group.

    This data type is used as a response element in the following actions:

    *  CreateDBInstance

    *  DeleteDBInstance

    *  ModifyDBInstance

    *  RebootDBInstance

    - **DBParameterGroupName** *(string) --*

      The name of the DP parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.
    """


_ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `DBSecurityGroups`

    Specifies membership in a designated DB security group.

    - **DBSecurityGroupName** *(string) --*

      The name of the DB security group.

    - **Status** *(string) --*

      The status of the DB security group.
    """


_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the EC2 Availability Zone that the subnet is in.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroup` `Subnets`

    Specifies a subnet.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the EC2 Availability Zone that the subnet is in.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `DBSubnetGroup`

    Specifies information on the subnet group associated with the DB instance, including the
    name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the VpcId of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Contains a list of  Subnet elements.

      - *(dict) --*

        Specifies a subnet.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the EC2 Availability Zone that the subnet is in.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `DomainMemberships`

    An Active Directory Domain membership record associated with a DB instance.

    - **Domain** *(string) --*

      The identifier of the Active Directory Domain.

    - **Status** *(string) --*

      The status of the DB instance's Active Directory Domain membership, such as joined,
      pending-join, failed etc).

    - **FQDN** *(string) --*

      The fully qualified domain name of the Active Directory Domain.

    - **IAMRoleName** *(string) --*

      The name of the IAM role to be used when making API calls to the Directory Service.
    """


_ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `OptionGroupMemberships`

    Provides information on the option groups the DB instance is a member of.

    - **OptionGroupName** *(string) --*

      The name of the option group that the instance belongs to.

    - **Status** *(string) --*

      The status of the DB instance's option group membership. Valid values are: ``in-sync``
      , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
      ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .
    """


_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstancePendingModifiedValues` `PendingCloudwatchLogsExports`

    Specifies the CloudWatch logs to be exported.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to CloudWatch Logs.

      - *(string) --*
    """


_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is only included when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
      currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently-in-progress change of the master credentials for the DB
      instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` | ``bring-your-own-license`` |
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
      currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the CA certificate for the DB instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      Specifies the CloudWatch logs to be exported.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to CloudWatch Logs.

        - *(string) --*
    """


_ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "read replication."

    - **Normal** *(boolean) --*

      Boolean value that is true if the instance is operating normally, or false if the
      instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a StatusType of read replica, the values can be
      replicating, error, stopped, or terminated.

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientDeleteDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientDeleteDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientDeleteDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientDeleteDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientDeleteDbInstanceResponseDBInstanceDomainMembershipsTypeDef
        ],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponse` `DBInstance`

    Contains the details of an Amazon Neptune DB instance.

    This data type is used as a response element in the  DescribeDBInstances action.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-supplied database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB instance.

    - **DBName** *(string) --*

      The database name.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size specified in gibibytes.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBSecurityGroups** *(list) --*

      Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
      ``DBSecurityGroup.Status`` subelements.

      - *(dict) --*

        Specifies membership in a designated DB security group.

        - **DBSecurityGroupName** *(string) --*

          The name of the DB security group.

        - **Status** *(string) --*

          The status of the DB security group.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **DBParameterGroups** *(list) --*

      Provides the list of DB parameter groups applied to this DB instance.

      - *(dict) --*

        The status of the DB parameter group.

        This data type is used as a response element in the following actions:

        *  CreateDBInstance

        *  DeleteDBInstance

        *  ModifyDBInstance

        *  RebootDBInstance

        - **DBParameterGroupName** *(string) --*

          The name of the DP parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group associated with the DB instance, including the
      name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the VpcId of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Contains a list of  Subnet elements.

        - *(dict) --*

          Specifies a subnet.

          This data type is used as a response element in the  DescribeDBSubnetGroups action.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the EC2 Availability Zone that the subnet is in.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is only included when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
        currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently-in-progress change of the master credentials for the DB
        instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` | ``bring-your-own-license`` |
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
        currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the CA certificate for the DB instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        Specifies the CloudWatch logs to be exported.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **MultiAZ** *(boolean) --*

      Specifies if the DB instance is a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

      Contains the identifier of the source DB instance if this DB instance is a Read Replica.

    - **ReadReplicaDBInstanceIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB instance.

      - *(string) --*

    - **ReadReplicaDBClusterIdentifiers** *(list) --*

      Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

      - *(string) --*

    - **LicenseModel** *(string) --*

      License model information for this DB instance.

    - **Iops** *(integer) --*

      Specifies the Provisioned IOPS (I/O operations per second) value.

    - **OptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB instance.

      - *(dict) --*

        Provides information on the option groups the DB instance is a member of.

        - **OptionGroupName** *(string) --*

          The name of the option group that the instance belongs to.

        - **Status** *(string) --*

          The status of the DB instance's option group membership. Valid values are: ``in-sync``
          , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
          ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this instance is associated with.

    - **SecondaryAvailabilityZone** *(string) --*

      If present, specifies the name of the secondary Availability Zone for a DB instance with
      multi-AZ support.

    - **PubliclyAccessible** *(boolean) --*

      This flag should no longer be used.

    - **StatusInfos** *(list) --*

      The status of a Read Replica. If the instance is not a Read Replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "read replication."

        - **Normal** *(boolean) --*

          Boolean value that is true if the instance is operating normally, or false if the
          instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a StatusType of read replica, the values can be
          replicating, error, stopped, or terminated.

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **StorageType** *(string) --*

      Specifies the storage type associated with DB instance.

    - **TdeCredentialArn** *(string) --*

      The ARN from the key store with which the instance is associated for TDE encryption.

    - **DbInstancePort** *(integer) --*

      Specifies the port that the DB instance listens on. If the DB instance is part of a DB
      cluster, this can be a different port than the DB cluster port.

    - **DBClusterIdentifier** *(string) --*

      If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
      the DB instance is a member of.

    - **StorageEncrypted** *(boolean) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **KmsKeyId** *(string) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **DomainMemberships** *(list) --*

      Not supported

      - *(dict) --*

        An Active Directory Domain membership record associated with a DB instance.

        - **Domain** *(string) --*

          The identifier of the Active Directory Domain.

        - **Status** *(string) --*

          The status of the DB instance's Active Directory Domain membership, such as joined,
          pending-join, failed etc).

        - **FQDN** *(string) --*

          The fully qualified domain name of the Active Directory Domain.

        - **IAMRoleName** *(string) --*

          The name of the IAM role to be used when making API calls to the Directory Service.

    - **CopyTagsToSnapshot** *(boolean) --*

      Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

    - **MonitoringInterval** *(integer) --*

      The interval, in seconds, between points when Enhanced Monitoring metrics are collected for
      the DB instance.

    - **EnhancedMonitoringResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
      Enhanced Monitoring metrics data for the DB instance.

    - **MonitoringRoleArn** *(string) --*

      The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon
      CloudWatch Logs.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **Timezone** *(string) --*

      Not supported.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
      false.

    - **PerformanceInsightsEnabled** *(boolean) --*

      True if Performance Insights is enabled for the DB instance, and otherwise false.

    - **PerformanceInsightsKMSKeyId** *(string) --*

      The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
      the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
      encryption key.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientDeleteDbInstanceResponseTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseTypeDef",
    {"DBInstance": ClientDeleteDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientDeleteDbInstanceResponseTypeDef(_ClientDeleteDbInstanceResponseTypeDef):
    """
    Type definition for `ClientDeleteDbInstance` `Response`

    - **DBInstance** *(dict) --*

      Contains the details of an Amazon Neptune DB instance.

      This data type is used as a response element in the  DescribeDBInstances action.

      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.

      - **DBInstanceClass** *(string) --*

        Contains the name of the compute and memory capacity class of the DB instance.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB instance.

      - **DBInstanceStatus** *(string) --*

        Specifies the current state of this database.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB instance.

      - **DBName** *(string) --*

        The database name.

      - **Endpoint** *(dict) --*

        Specifies the connection endpoint.

        - **Address** *(string) --*

          Specifies the DNS address of the DB instance.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **AllocatedStorage** *(integer) --*

        Specifies the allocated storage size specified in gibibytes.

      - **InstanceCreateTime** *(datetime) --*

        Provides the date and time the DB instance was created.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBSecurityGroups** *(list) --*

        Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
        ``DBSecurityGroup.Status`` subelements.

        - *(dict) --*

          Specifies membership in a designated DB security group.

          - **DBSecurityGroupName** *(string) --*

            The name of the DB security group.

          - **Status** *(string) --*

            The status of the DB security group.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security group elements that the DB instance belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **DBParameterGroups** *(list) --*

        Provides the list of DB parameter groups applied to this DB instance.

        - *(dict) --*

          The status of the DB parameter group.

          This data type is used as a response element in the following actions:

          *  CreateDBInstance

          *  DeleteDBInstance

          *  ModifyDBInstance

          *  RebootDBInstance

          - **DBParameterGroupName** *(string) --*

            The name of the DP parameter group.

          - **ParameterApplyStatus** *(string) --*

            The status of parameter updates.

      - **AvailabilityZone** *(string) --*

        Specifies the name of the Availability Zone the DB instance is located in.

      - **DBSubnetGroup** *(dict) --*

        Specifies information on the subnet group associated with the DB instance, including the
        name, description, and subnets in the subnet group.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the VpcId of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Contains a list of  Subnet elements.

          - *(dict) --*

            Specifies a subnet.

            This data type is used as a response element in the  DescribeDBSubnetGroups action.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the EC2 Availability Zone that the subnet is in.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **PendingModifiedValues** *(dict) --*

        Specifies that changes to the DB instance are pending. This element is only included when
        changes are pending. Specific changes are identified by subelements.

        - **DBInstanceClass** *(string) --*

          Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
          currently being applied.

        - **AllocatedStorage** *(integer) --*

          Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
          currently being applied.

        - **MasterUserPassword** *(string) --*

          Contains the pending or currently-in-progress change of the master credentials for the DB
          instance.

        - **Port** *(integer) --*

          Specifies the pending port for the DB instance.

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the pending number of days for which automated backups are retained.

        - **MultiAZ** *(boolean) --*

          Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LicenseModel** *(string) --*

          The license model for the DB instance.

          Valid values: ``license-included`` | ``bring-your-own-license`` |
          ``general-public-license``

        - **Iops** *(integer) --*

          Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
          currently being applied.

        - **DBInstanceIdentifier** *(string) --*

          Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
          currently being applied.

        - **StorageType** *(string) --*

          Specifies the storage type to be associated with the DB instance.

        - **CACertificateIdentifier** *(string) --*

          Specifies the identifier of the CA certificate for the DB instance.

        - **DBSubnetGroupName** *(string) --*

          The new DB subnet group for the DB instance.

        - **PendingCloudwatchLogsExports** *(dict) --*

          Specifies the CloudWatch logs to be exported.

          - **LogTypesToEnable** *(list) --*

            Log types that are in the process of being deactivated. After they are deactivated,
            these log types aren't exported to CloudWatch Logs.

            - *(string) --*

          - **LogTypesToDisable** *(list) --*

            Log types that are in the process of being enabled. After they are enabled, these log
            types are exported to CloudWatch Logs.

            - *(string) --*

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **MultiAZ** *(boolean) --*

        Specifies if the DB instance is a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Indicates that minor version patches are applied automatically.

      - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

        Contains the identifier of the source DB instance if this DB instance is a Read Replica.

      - **ReadReplicaDBInstanceIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB instance.

        - *(string) --*

      - **ReadReplicaDBClusterIdentifiers** *(list) --*

        Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

        - *(string) --*

      - **LicenseModel** *(string) --*

        License model information for this DB instance.

      - **Iops** *(integer) --*

        Specifies the Provisioned IOPS (I/O operations per second) value.

      - **OptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB instance.

        - *(dict) --*

          Provides information on the option groups the DB instance is a member of.

          - **OptionGroupName** *(string) --*

            The name of the option group that the instance belongs to.

          - **Status** *(string) --*

            The status of the DB instance's option group membership. Valid values are: ``in-sync``
            , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
            ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this instance is associated with.

      - **SecondaryAvailabilityZone** *(string) --*

        If present, specifies the name of the secondary Availability Zone for a DB instance with
        multi-AZ support.

      - **PubliclyAccessible** *(boolean) --*

        This flag should no longer be used.

      - **StatusInfos** *(list) --*

        The status of a Read Replica. If the instance is not a Read Replica, this is blank.

        - *(dict) --*

          Provides a list of status information for a DB instance.

          - **StatusType** *(string) --*

            This value is currently "read replication."

          - **Normal** *(boolean) --*

            Boolean value that is true if the instance is operating normally, or false if the
            instance is in an error state.

          - **Status** *(string) --*

            Status of the DB instance. For a StatusType of read replica, the values can be
            replicating, error, stopped, or terminated.

          - **Message** *(string) --*

            Details of the error if there is an error for the instance. If the instance is not in
            an error state, this value is blank.

      - **StorageType** *(string) --*

        Specifies the storage type associated with DB instance.

      - **TdeCredentialArn** *(string) --*

        The ARN from the key store with which the instance is associated for TDE encryption.

      - **DbInstancePort** *(integer) --*

        Specifies the port that the DB instance listens on. If the DB instance is part of a DB
        cluster, this can be a different port than the DB cluster port.

      - **DBClusterIdentifier** *(string) --*

        If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
        the DB instance is a member of.

      - **StorageEncrypted** *(boolean) --*

        Not supported: The encryption for DB instances is managed by the DB cluster.

      - **KmsKeyId** *(string) --*

        Not supported: The encryption for DB instances is managed by the DB cluster.

      - **DbiResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
        in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

      - **CACertificateIdentifier** *(string) --*

        The identifier of the CA certificate for this DB instance.

      - **DomainMemberships** *(list) --*

        Not supported

        - *(dict) --*

          An Active Directory Domain membership record associated with a DB instance.

          - **Domain** *(string) --*

            The identifier of the Active Directory Domain.

          - **Status** *(string) --*

            The status of the DB instance's Active Directory Domain membership, such as joined,
            pending-join, failed etc).

          - **FQDN** *(string) --*

            The fully qualified domain name of the Active Directory Domain.

          - **IAMRoleName** *(string) --*

            The name of the IAM role to be used when making API calls to the Directory Service.

      - **CopyTagsToSnapshot** *(boolean) --*

        Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

      - **MonitoringInterval** *(integer) --*

        The interval, in seconds, between points when Enhanced Monitoring metrics are collected for
        the DB instance.

      - **EnhancedMonitoringResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
        Enhanced Monitoring metrics data for the DB instance.

      - **MonitoringRoleArn** *(string) --*

        The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon
        CloudWatch Logs.

      - **PromotionTier** *(integer) --*

        A value that specifies the order in which a Read Replica is promoted to the primary
        instance after a failure of the existing primary instance.

      - **DBInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB instance.

      - **Timezone** *(string) --*

        Not supported.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
        false.

      - **PerformanceInsightsEnabled** *(boolean) --*

        True if Performance Insights is enabled for the DB instance, and otherwise false.

      - **PerformanceInsightsKMSKeyId** *(string) --*

        The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
        the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
        encryption key.

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB instance is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    Type definition for `ClientDeleteEventSubscriptionResponse` `EventSubscription`

    Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the event notification subscription.

    - **Status** *(string) --*

      The status of the event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that Neptune no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the event notification subscription was created.

    - **SourceType** *(string) --*

      The source type for the event notification subscription.

    - **SourceIdsList** *(list) --*

      A list of source IDs for the event notification subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A list of event categories for the event notification subscription.

      - *(string) --*

    - **Enabled** *(boolean) --*

      A Boolean value indicating if the subscription is enabled. True indicates the subscription
      is enabled.

    - **EventSubscriptionArn** *(string) --*

      The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientDeleteEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientDeleteEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef
    },
    total=False,
)


class ClientDeleteEventSubscriptionResponseTypeDef(
    _ClientDeleteEventSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientDeleteEventSubscription` `Response`

    - **EventSubscription** *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.

      - **CustSubscriptionId** *(string) --*

        The event notification subscription Id.

      - **SnsTopicArn** *(string) --*

        The topic ARN of the event notification subscription.

      - **Status** *(string) --*

        The status of the event notification subscription.

        Constraints:

        Can be one of the following: creating | modifying | deleting | active | no-permission |
        topic-not-exist

        The status "no-permission" indicates that Neptune no longer has permission to post to the
        SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
        subscription was created.

      - **SubscriptionCreationTime** *(string) --*

        The time the event notification subscription was created.

      - **SourceType** *(string) --*

        The source type for the event notification subscription.

      - **SourceIdsList** *(list) --*

        A list of source IDs for the event notification subscription.

        - *(string) --*

      - **EventCategoriesList** *(list) --*

        A list of event categories for the event notification subscription.

        - *(string) --*

      - **Enabled** *(boolean) --*

        A Boolean value indicating if the subscription is enabled. True indicates the subscription
        is enabled.

      - **EventSubscriptionArn** *(string) --*

        The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientDescribeDbClusterParameterGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterParameterGroupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeDbClusterParameterGroupsFiltersTypeDef(
    _ClientDescribeDbClusterParameterGroupsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParameterGroups` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef(
    _ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParameterGroupsResponse` `DBClusterParameterGroups`

    Contains the details of an Amazon Neptune DB cluster parameter group.

    This data type is used as a response element in the  DescribeDBClusterParameterGroups
    action.

    - **DBClusterParameterGroupName** *(string) --*

      Provides the name of the DB cluster parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB cluster parameter group
      is compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB cluster parameter group.

    - **DBClusterParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientDescribeDbClusterParameterGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List[
            ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterParameterGroupsResponseTypeDef(
    _ClientDescribeDbClusterParameterGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParameterGroups` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous ``DescribeDBClusterParameterGroups``
      request. If this parameter is specified, the response includes only records beyond the
      marker, up to the value specified by ``MaxRecords`` .

    - **DBClusterParameterGroups** *(list) --*

      A list of DB cluster parameter groups.

      - *(dict) --*

        Contains the details of an Amazon Neptune DB cluster parameter group.

        This data type is used as a response element in the  DescribeDBClusterParameterGroups
        action.

        - **DBClusterParameterGroupName** *(string) --*

          Provides the name of the DB cluster parameter group.

        - **DBParameterGroupFamily** *(string) --*

          Provides the name of the DB parameter group family that this DB cluster parameter group
          is compatible with.

        - **Description** *(string) --*

          Provides the customer-specified description for this DB cluster parameter group.

        - **DBClusterParameterGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientDescribeDbClusterParametersFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeDbClusterParametersFiltersTypeDef(
    _ClientDescribeDbClusterParametersFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParameters` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeDbClusterParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeDbClusterParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientDescribeDbClusterParametersResponseParametersTypeDef(
    _ClientDescribeDbClusterParametersResponseParametersTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParametersResponse` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientDescribeDbClusterParametersResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterParametersResponseTypeDef",
    {
        "Parameters": List[ClientDescribeDbClusterParametersResponseParametersTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeDbClusterParametersResponseTypeDef(
    _ClientDescribeDbClusterParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParameters` `Response`

    - **Parameters** *(list) --*

      Provides a list of parameters for the DB cluster parameter group.

      - *(dict) --*

        Specifies a parameter.

        - **ParameterName** *(string) --*

          Specifies the name of the parameter.

        - **ParameterValue** *(string) --*

          Specifies the value of the parameter.

        - **Description** *(string) --*

          Provides a description of the parameter.

        - **Source** *(string) --*

          Indicates the source of the parameter value.

        - **ApplyType** *(string) --*

          Specifies the engine specific parameters type.

        - **DataType** *(string) --*

          Specifies the valid data type for the parameter.

        - **AllowedValues** *(string) --*

          Specifies the valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest engine version to which the parameter can apply.

        - **ApplyMethod** *(string) --*

          Indicates when to apply parameter updates.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous DescribeDBClusterParameters request. If
      this parameter is specified, the response includes only records beyond the marker, up to the
      value specified by ``MaxRecords`` .
    """


_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)


class ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef(
    _ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResult` `DBClusterSnapshotAttributes`

    Contains the name and values of a manual DB cluster snapshot attribute.

    Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
    a manual DB cluster snapshot. For more information, see the
    ModifyDBClusterSnapshotAttribute API action.

    - **AttributeName** *(string) --*

      The name of the manual DB cluster snapshot attribute.

      The attribute named ``restore`` refers to the list of AWS accounts that have permission
      to copy or restore the manual DB cluster snapshot. For more information, see the
      ModifyDBClusterSnapshotAttribute API action.

    - **AttributeValues** *(list) --*

      The value(s) for the manual DB cluster snapshot attribute.

      If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
      of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
      snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
      public and available for any AWS account to copy or restore.

      - *(string) --*
    """


_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List[
            ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef(
    _ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshotAttributesResponse` `DBClusterSnapshotAttributesResult`

    Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API
    action.

    Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
    restore a manual DB cluster snapshot. For more information, see the
    ModifyDBClusterSnapshotAttribute API action.

    - **DBClusterSnapshotIdentifier** *(string) --*

      The identifier of the manual DB cluster snapshot that the attributes apply to.

    - **DBClusterSnapshotAttributes** *(list) --*

      The list of attributes and values for the manual DB cluster snapshot.

      - *(dict) --*

        Contains the name and values of a manual DB cluster snapshot attribute.

        Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
        a manual DB cluster snapshot. For more information, see the
        ModifyDBClusterSnapshotAttribute API action.

        - **AttributeName** *(string) --*

          The name of the manual DB cluster snapshot attribute.

          The attribute named ``restore`` refers to the list of AWS accounts that have permission
          to copy or restore the manual DB cluster snapshot. For more information, see the
          ModifyDBClusterSnapshotAttribute API action.

        - **AttributeValues** *(list) --*

          The value(s) for the manual DB cluster snapshot attribute.

          If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
          of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
          snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
          public and available for any AWS account to copy or restore.

          - *(string) --*
    """


_ClientDescribeDbClusterSnapshotAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotAttributesResponseTypeDef",
    {
        "DBClusterSnapshotAttributesResult": ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotAttributesResponseTypeDef(
    _ClientDescribeDbClusterSnapshotAttributesResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshotAttributes` `Response`

    - **DBClusterSnapshotAttributesResult** *(dict) --*

      Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API
      action.

      Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
      restore a manual DB cluster snapshot. For more information, see the
      ModifyDBClusterSnapshotAttribute API action.

      - **DBClusterSnapshotIdentifier** *(string) --*

        The identifier of the manual DB cluster snapshot that the attributes apply to.

      - **DBClusterSnapshotAttributes** *(list) --*

        The list of attributes and values for the manual DB cluster snapshot.

        - *(dict) --*

          Contains the name and values of a manual DB cluster snapshot attribute.

          Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
          a manual DB cluster snapshot. For more information, see the
          ModifyDBClusterSnapshotAttribute API action.

          - **AttributeName** *(string) --*

            The name of the manual DB cluster snapshot attribute.

            The attribute named ``restore`` refers to the list of AWS accounts that have permission
            to copy or restore the manual DB cluster snapshot. For more information, see the
            ModifyDBClusterSnapshotAttribute API action.

          - **AttributeValues** *(list) --*

            The value(s) for the manual DB cluster snapshot attribute.

            If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
            of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
            snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
            public and available for any AWS account to copy or restore.

            - *(string) --*
    """


_ClientDescribeDbClusterSnapshotsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeDbClusterSnapshotsFiltersTypeDef(
    _ClientDescribeDbClusterSnapshotsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshots` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef(
    _ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshotsResponse` `DBClusterSnapshots`

    Contains the details for an Amazon Neptune DB cluster snapshot

    This data type is used as a response element in the  DescribeDBClusterSnapshots action.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
      be restored in.

      - *(string) --*

    - **DBClusterSnapshotIdentifier** *(string) --*

      Specifies the identifier for the DB cluster snapshot.

    - **DBClusterIdentifier** *(string) --*

      Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
      created from.

    - **SnapshotCreateTime** *(datetime) --*

      Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

    - **Engine** *(string) --*

      Specifies the name of the database engine.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size in gibibytes (GiB).

    - **Status** *(string) --*

      Specifies the status of this DB cluster snapshot.

    - **Port** *(integer) --*

      Specifies the port that the DB cluster was listening on at the time of the snapshot.

    - **VpcId** *(string) --*

      Provides the VPC ID associated with the DB cluster snapshot.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **MasterUsername** *(string) --*

      Provides the master username for the DB cluster snapshot.

    - **EngineVersion** *(string) --*

      Provides the version of the database engine for this DB cluster snapshot.

    - **LicenseModel** *(string) --*

      Provides the license model information for this DB cluster snapshot.

    - **SnapshotType** *(string) --*

      Provides the type of the DB cluster snapshot.

    - **PercentProgress** *(integer) --*

      Specifies the percentage of the estimated data that has been transferred.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster snapshot is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster
      snapshot.

    - **DBClusterSnapshotArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster snapshot.

    - **SourceDBClusterSnapshotArn** *(string) --*

      If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon
      Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.
    """


_ClientDescribeDbClusterSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotsResponseTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List[
            ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotsResponseTypeDef(
    _ClientDescribeDbClusterSnapshotsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshots` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous  DescribeDBClusterSnapshots request. If
      this parameter is specified, the response includes only records beyond the marker, up to the
      value specified by ``MaxRecords`` .

    - **DBClusterSnapshots** *(list) --*

      Provides a list of DB cluster snapshots for the user.

      - *(dict) --*

        Contains the details for an Amazon Neptune DB cluster snapshot

        This data type is used as a response element in the  DescribeDBClusterSnapshots action.

        - **AvailabilityZones** *(list) --*

          Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
          be restored in.

          - *(string) --*

        - **DBClusterSnapshotIdentifier** *(string) --*

          Specifies the identifier for the DB cluster snapshot.

        - **DBClusterIdentifier** *(string) --*

          Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
          created from.

        - **SnapshotCreateTime** *(datetime) --*

          Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

        - **Engine** *(string) --*

          Specifies the name of the database engine.

        - **AllocatedStorage** *(integer) --*

          Specifies the allocated storage size in gibibytes (GiB).

        - **Status** *(string) --*

          Specifies the status of this DB cluster snapshot.

        - **Port** *(integer) --*

          Specifies the port that the DB cluster was listening on at the time of the snapshot.

        - **VpcId** *(string) --*

          Provides the VPC ID associated with the DB cluster snapshot.

        - **ClusterCreateTime** *(datetime) --*

          Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

        - **MasterUsername** *(string) --*

          Provides the master username for the DB cluster snapshot.

        - **EngineVersion** *(string) --*

          Provides the version of the database engine for this DB cluster snapshot.

        - **LicenseModel** *(string) --*

          Provides the license model information for this DB cluster snapshot.

        - **SnapshotType** *(string) --*

          Provides the type of the DB cluster snapshot.

        - **PercentProgress** *(integer) --*

          Specifies the percentage of the estimated data that has been transferred.

        - **StorageEncrypted** *(boolean) --*

          Specifies whether the DB cluster snapshot is encrypted.

        - **KmsKeyId** *(string) --*

          If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster
          snapshot.

        - **DBClusterSnapshotArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB cluster snapshot.

        - **SourceDBClusterSnapshotArn** *(string) --*

          If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon
          Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

        - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

          True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
          is enabled, and otherwise false.
    """


_ClientDescribeDbClustersFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClustersFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeDbClustersFiltersTypeDef(_ClientDescribeDbClustersFiltersTypeDef):
    """
    Type definition for `ClientDescribeDbClusters` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef(
    _ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef
):
    """
    Type definition for `ClientDescribeDbClustersResponseDBClusters` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      Status property returns one of the following values:

      * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB
      cluster is unable to assume the IAM role in order to access other AWS services on
      your behalf.
    """


_ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef(
    _ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef
):
    """
    Type definition for `ClientDescribeDbClustersResponseDBClusters` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      Value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.
    """


_ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef(
    _ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientDescribeDbClustersResponseDBClusters` `DBClusterOptionGroupMemberships`

    Contains status information for a DB cluster option group.

    - **DBClusterOptionGroupName** *(string) --*

      Specifies the name of the DB cluster option group.

    - **Status** *(string) --*

      Specifies the status of the DB cluster option group.
    """


_ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef(
    _ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbClustersResponseDBClusters` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientDescribeDbClustersResponseDBClustersTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientDescribeDbClustersResponseDBClustersDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersTypeDef(
    _ClientDescribeDbClustersResponseDBClustersTypeDef
):
    """
    Type definition for `ClientDescribeDbClustersResponse` `DBClusters`

    Contains the details of an Amazon Neptune DB cluster.

    This data type is used as a response element in the  DescribeDBClusters action.

    - **AllocatedStorage** *(integer) --*

       ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
       fixed, but instead automatically adjusts as needed.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster can be
      created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this cluster is associated with.

    - **DatabaseName** *(string) --*

      Contains the name of the initial database of this DB cluster that was provided at create
      time, if one was specified when the DB cluster was created. This same name is returned
      for the life of the DB cluster.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group associated with the DB cluster, including the
      name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      Specifies the earliest time to which a database can be restored with point-in-time
      restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
      load-balances connections across the Read Replicas that are available in a DB cluster. As
      clients request new connections to the reader endpoint, Neptune distributes the
      connection requests among the Read Replicas in the DB cluster. This functionality can
      help balance your read workload across multiple Read Replicas in your DB cluster.

      If a failover occurs, and the Read Replica that you are connected to is promoted to be
      the primary instance, your connection is dropped. To continue sending your read workload
      to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB cluster.

    - **DBClusterOptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB cluster.

      - *(dict) --*

        Contains status information for a DB cluster option group.

        - **DBClusterOptionGroupName** *(string) --*

          Specifies the name of the DB cluster option group.

        - **Status** *(string) --*

          Specifies the status of the DB cluster option group.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **ReplicationSourceIdentifier** *(string) --*

      Not supported by Neptune.

    - **ReadReplicaIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB cluster.

      - *(string) --*

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          Value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security groups that the DB cluster belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          Status property returns one of the following values:

          * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB
          cluster is unable to assume the IAM role in order to access other AWS services on
          your behalf.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.

    - **CloneGroupId** *(string) --*

      Identifies the clone group to which the DB cluster is associated.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientDescribeDbClustersResponseTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseTypeDef",
    {
        "Marker": str,
        "DBClusters": List[ClientDescribeDbClustersResponseDBClustersTypeDef],
    },
    total=False,
)


class ClientDescribeDbClustersResponseTypeDef(_ClientDescribeDbClustersResponseTypeDef):
    """
    Type definition for `ClientDescribeDbClusters` `Response`

    - **Marker** *(string) --*

      A pagination token that can be used in a subsequent DescribeDBClusters request.

    - **DBClusters** *(list) --*

      Contains a list of DB clusters for the user.

      - *(dict) --*

        Contains the details of an Amazon Neptune DB cluster.

        This data type is used as a response element in the  DescribeDBClusters action.

        - **AllocatedStorage** *(integer) --*

           ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
           fixed, but instead automatically adjusts as needed.

        - **AvailabilityZones** *(list) --*

          Provides the list of EC2 Availability Zones that instances in the DB cluster can be
          created in.

          - *(string) --*

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the number of days for which automatic DB snapshots are retained.

        - **CharacterSetName** *(string) --*

          If present, specifies the name of the character set that this cluster is associated with.

        - **DatabaseName** *(string) --*

          Contains the name of the initial database of this DB cluster that was provided at create
          time, if one was specified when the DB cluster was created. This same name is returned
          for the life of the DB cluster.

        - **DBClusterIdentifier** *(string) --*

          Contains a user-supplied DB cluster identifier. This identifier is the unique key that
          identifies a DB cluster.

        - **DBClusterParameterGroup** *(string) --*

          Specifies the name of the DB cluster parameter group for the DB cluster.

        - **DBSubnetGroup** *(string) --*

          Specifies information on the subnet group associated with the DB cluster, including the
          name, description, and subnets in the subnet group.

        - **Status** *(string) --*

          Specifies the current state of this DB cluster.

        - **PercentProgress** *(string) --*

          Specifies the progress of the operation as a percentage.

        - **EarliestRestorableTime** *(datetime) --*

          Specifies the earliest time to which a database can be restored with point-in-time
          restore.

        - **Endpoint** *(string) --*

          Specifies the connection endpoint for the primary instance of the DB cluster.

        - **ReaderEndpoint** *(string) --*

          The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
          load-balances connections across the Read Replicas that are available in a DB cluster. As
          clients request new connections to the reader endpoint, Neptune distributes the
          connection requests among the Read Replicas in the DB cluster. This functionality can
          help balance your read workload across multiple Read Replicas in your DB cluster.

          If a failover occurs, and the Read Replica that you are connected to is promoted to be
          the primary instance, your connection is dropped. To continue sending your read workload
          to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

        - **MultiAZ** *(boolean) --*

          Specifies whether the DB cluster has instances in multiple Availability Zones.

        - **Engine** *(string) --*

          Provides the name of the database engine to be used for this DB cluster.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LatestRestorableTime** *(datetime) --*

          Specifies the latest time to which a database can be restored with point-in-time restore.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **MasterUsername** *(string) --*

          Contains the master username for the DB cluster.

        - **DBClusterOptionGroupMemberships** *(list) --*

          Provides the list of option group memberships for this DB cluster.

          - *(dict) --*

            Contains status information for a DB cluster option group.

            - **DBClusterOptionGroupName** *(string) --*

              Specifies the name of the DB cluster option group.

            - **Status** *(string) --*

              Specifies the status of the DB cluster option group.

        - **PreferredBackupWindow** *(string) --*

          Specifies the daily time range during which automated backups are created if automated
          backups are enabled, as determined by the ``BackupRetentionPeriod`` .

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which system maintenance can occur, in Universal
          Coordinated Time (UTC).

        - **ReplicationSourceIdentifier** *(string) --*

          Not supported by Neptune.

        - **ReadReplicaIdentifiers** *(list) --*

          Contains one or more identifiers of the Read Replicas associated with this DB cluster.

          - *(string) --*

        - **DBClusterMembers** *(list) --*

          Provides the list of instances that make up the DB cluster.

          - *(dict) --*

            Contains information about an instance that is part of a DB cluster.

            - **DBInstanceIdentifier** *(string) --*

              Specifies the instance identifier for this member of the DB cluster.

            - **IsClusterWriter** *(boolean) --*

              Value that is ``true`` if the cluster member is the primary instance for the DB
              cluster and ``false`` otherwise.

            - **DBClusterParameterGroupStatus** *(string) --*

              Specifies the status of the DB cluster parameter group for this member of the DB
              cluster.

            - **PromotionTier** *(integer) --*

              A value that specifies the order in which a Read Replica is promoted to the primary
              instance after a failure of the existing primary instance.

        - **VpcSecurityGroups** *(list) --*

          Provides a list of VPC security groups that the DB cluster belongs to.

          - *(dict) --*

            This data type is used as a response element for queries on VPC security group
            membership.

            - **VpcSecurityGroupId** *(string) --*

              The name of the VPC security group.

            - **Status** *(string) --*

              The status of the VPC security group.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

        - **StorageEncrypted** *(boolean) --*

          Specifies whether the DB cluster is encrypted.

        - **KmsKeyId** *(string) --*

          If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

        - **DbClusterResourceId** *(string) --*

          The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found
          in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

        - **DBClusterArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB cluster.

        - **AssociatedRoles** *(list) --*

          Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
          with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
          the DB cluster to access other AWS services on your behalf.

          - *(dict) --*

            Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
            cluster.

            - **RoleArn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

            - **Status** *(string) --*

              Describes the state of association between the IAM role and the DB cluster. The
              Status property returns one of the following values:

              * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
              access other AWS services on your behalf.

              * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

              * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB
              cluster is unable to assume the IAM role in order to access other AWS services on
              your behalf.

        - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

          True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
          is enabled, and otherwise false.

        - **CloneGroupId** *(string) --*

          Identifies the clone group to which the DB cluster is associated.

        - **ClusterCreateTime** *(datetime) --*

          Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

        - **EnabledCloudwatchLogsExports** *(list) --*

          A list of log types that this DB cluster is configured to export to CloudWatch Logs.

          - *(string) --*
    """


_ClientDescribeDbEngineVersionsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeDbEngineVersionsFiltersTypeDef(
    _ClientDescribeDbEngineVersionsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersions` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef",
    {"CharacterSetName": str, "CharacterSetDescription": str},
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersionsResponseDBEngineVersions` `DefaultCharacterSet`

    The default character set for new instances of this engine version, if the
    ``CharacterSetName`` parameter of the CreateDBInstance API is not specified.

    - **CharacterSetName** *(string) --*

      The name of the character set.

    - **CharacterSetDescription** *(string) --*

      The description of the character set.
    """


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef",
    {"CharacterSetName": str, "CharacterSetDescription": str},
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersionsResponseDBEngineVersions` `SupportedCharacterSets`

    Specifies a character set.

    - **CharacterSetName** *(string) --*

      The name of the character set.

    - **CharacterSetDescription** *(string) --*

      The description of the character set.
    """


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef",
    {"TimezoneName": str},
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersionsResponseDBEngineVersions` `SupportedTimezones`

    A time zone associated with a  DBInstance .

    - **TimezoneName** *(string) --*

      The name of the time zone.
    """


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
    },
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersionsResponseDBEngineVersions` `ValidUpgradeTarget`

    The version of the database engine that a DB instance can be upgraded to.

    - **Engine** *(string) --*

      The name of the upgrade target database engine.

    - **EngineVersion** *(string) --*

      The version number of the upgrade target database engine.

    - **Description** *(string) --*

      The version of the database engine that a DB instance can be upgraded to.

    - **AutoUpgrade** *(boolean) --*

      A value that indicates whether the target version is applied to any source DB
      instances that have AutoMinorVersionUpgrade set to true.

    - **IsMajorVersionUpgrade** *(boolean) --*

      A value that indicates whether a database engine is upgraded to a major version.
    """


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "DefaultCharacterSet": ClientDescribeDbEngineVersionsResponseDBEngineVersionsDefaultCharacterSetTypeDef,
        "SupportedCharacterSets": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedCharacterSetsTypeDef
        ],
        "ValidUpgradeTarget": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef
        ],
        "SupportedTimezones": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsSupportedTimezonesTypeDef
        ],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
    },
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersionsResponse` `DBEngineVersions`

    This data type is used as a response element in the action  DescribeDBEngineVersions .

    - **Engine** *(string) --*

      The name of the database engine.

    - **EngineVersion** *(string) --*

      The version number of the database engine.

    - **DBParameterGroupFamily** *(string) --*

      The name of the DB parameter group family for the database engine.

    - **DBEngineDescription** *(string) --*

      The description of the database engine.

    - **DBEngineVersionDescription** *(string) --*

      The description of the database engine version.

    - **DefaultCharacterSet** *(dict) --*

      The default character set for new instances of this engine version, if the
      ``CharacterSetName`` parameter of the CreateDBInstance API is not specified.

      - **CharacterSetName** *(string) --*

        The name of the character set.

      - **CharacterSetDescription** *(string) --*

        The description of the character set.

    - **SupportedCharacterSets** *(list) --*

      A list of the character sets supported by this engine for the ``CharacterSetName``
      parameter of the ``CreateDBInstance`` action.

      - *(dict) --*

        Specifies a character set.

        - **CharacterSetName** *(string) --*

          The name of the character set.

        - **CharacterSetDescription** *(string) --*

          The description of the character set.

    - **ValidUpgradeTarget** *(list) --*

      A list of engine versions that this database engine version can be upgraded to.

      - *(dict) --*

        The version of the database engine that a DB instance can be upgraded to.

        - **Engine** *(string) --*

          The name of the upgrade target database engine.

        - **EngineVersion** *(string) --*

          The version number of the upgrade target database engine.

        - **Description** *(string) --*

          The version of the database engine that a DB instance can be upgraded to.

        - **AutoUpgrade** *(boolean) --*

          A value that indicates whether the target version is applied to any source DB
          instances that have AutoMinorVersionUpgrade set to true.

        - **IsMajorVersionUpgrade** *(boolean) --*

          A value that indicates whether a database engine is upgraded to a major version.

    - **SupportedTimezones** *(list) --*

      A list of the time zones supported by this engine for the ``Timezone`` parameter of the
      ``CreateDBInstance`` action.

      - *(dict) --*

        A time zone associated with a  DBInstance .

        - **TimezoneName** *(string) --*

          The name of the time zone.

    - **ExportableLogTypes** *(list) --*

      The types of logs that the database engine has available for export to CloudWatch Logs.

      - *(string) --*

    - **SupportsLogExportsToCloudwatchLogs** *(boolean) --*

      A value that indicates whether the engine version supports exporting the log types
      specified by ExportableLogTypes to CloudWatch Logs.

    - **SupportsReadReplica** *(boolean) --*

      Indicates whether the database engine version supports read replicas.
    """


_ClientDescribeDbEngineVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbEngineVersionsResponseTypeDef(
    _ClientDescribeDbEngineVersionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersions` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **DBEngineVersions** *(list) --*

      A list of ``DBEngineVersion`` elements.

      - *(dict) --*

        This data type is used as a response element in the action  DescribeDBEngineVersions .

        - **Engine** *(string) --*

          The name of the database engine.

        - **EngineVersion** *(string) --*

          The version number of the database engine.

        - **DBParameterGroupFamily** *(string) --*

          The name of the DB parameter group family for the database engine.

        - **DBEngineDescription** *(string) --*

          The description of the database engine.

        - **DBEngineVersionDescription** *(string) --*

          The description of the database engine version.

        - **DefaultCharacterSet** *(dict) --*

          The default character set for new instances of this engine version, if the
          ``CharacterSetName`` parameter of the CreateDBInstance API is not specified.

          - **CharacterSetName** *(string) --*

            The name of the character set.

          - **CharacterSetDescription** *(string) --*

            The description of the character set.

        - **SupportedCharacterSets** *(list) --*

          A list of the character sets supported by this engine for the ``CharacterSetName``
          parameter of the ``CreateDBInstance`` action.

          - *(dict) --*

            Specifies a character set.

            - **CharacterSetName** *(string) --*

              The name of the character set.

            - **CharacterSetDescription** *(string) --*

              The description of the character set.

        - **ValidUpgradeTarget** *(list) --*

          A list of engine versions that this database engine version can be upgraded to.

          - *(dict) --*

            The version of the database engine that a DB instance can be upgraded to.

            - **Engine** *(string) --*

              The name of the upgrade target database engine.

            - **EngineVersion** *(string) --*

              The version number of the upgrade target database engine.

            - **Description** *(string) --*

              The version of the database engine that a DB instance can be upgraded to.

            - **AutoUpgrade** *(boolean) --*

              A value that indicates whether the target version is applied to any source DB
              instances that have AutoMinorVersionUpgrade set to true.

            - **IsMajorVersionUpgrade** *(boolean) --*

              A value that indicates whether a database engine is upgraded to a major version.

        - **SupportedTimezones** *(list) --*

          A list of the time zones supported by this engine for the ``Timezone`` parameter of the
          ``CreateDBInstance`` action.

          - *(dict) --*

            A time zone associated with a  DBInstance .

            - **TimezoneName** *(string) --*

              The name of the time zone.

        - **ExportableLogTypes** *(list) --*

          The types of logs that the database engine has available for export to CloudWatch Logs.

          - *(string) --*

        - **SupportsLogExportsToCloudwatchLogs** *(boolean) --*

          A value that indicates whether the engine version supports exporting the log types
          specified by ExportableLogTypes to CloudWatch Logs.

        - **SupportsReadReplica** *(boolean) --*

          Indicates whether the database engine version supports read replicas.
    """


_ClientDescribeDbInstancesFiltersTypeDef = TypedDict(
    "_ClientDescribeDbInstancesFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeDbInstancesFiltersTypeDef(_ClientDescribeDbInstancesFiltersTypeDef):
    """
    Type definition for `ClientDescribeDbInstances` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `DBParameterGroups`

    The status of the DB parameter group.

    This data type is used as a response element in the following actions:

    *  CreateDBInstance

    *  DeleteDBInstance

    *  ModifyDBInstance

    *  RebootDBInstance

    - **DBParameterGroupName** *(string) --*

      The name of the DP parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.
    """


_ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `DBSecurityGroups`

    Specifies membership in a designated DB security group.

    - **DBSecurityGroupName** *(string) --*

      The name of the DB security group.

    - **Status** *(string) --*

      The status of the DB security group.
    """


_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the EC2 Availability Zone that the subnet is in.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroup` `Subnets`

    Specifies a subnet.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the EC2 Availability Zone that the subnet is in.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `DBSubnetGroup`

    Specifies information on the subnet group associated with the DB instance, including the
    name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the VpcId of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Contains a list of  Subnet elements.

      - *(dict) --*

        Specifies a subnet.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the EC2 Availability Zone that the subnet is in.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `DomainMemberships`

    An Active Directory Domain membership record associated with a DB instance.

    - **Domain** *(string) --*

      The identifier of the Active Directory Domain.

    - **Status** *(string) --*

      The status of the DB instance's Active Directory Domain membership, such as joined,
      pending-join, failed etc).

    - **FQDN** *(string) --*

      The fully qualified domain name of the Active Directory Domain.

    - **IAMRoleName** *(string) --*

      The name of the IAM role to be used when making API calls to the Directory Service.
    """


_ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `OptionGroupMemberships`

    Provides information on the option groups the DB instance is a member of.

    - **OptionGroupName** *(string) --*

      The name of the option group that the instance belongs to.

    - **Status** *(string) --*

      The status of the DB instance's option group membership. Valid values are:
      ``in-sync`` , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply``
      , ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .
    """


_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValues` `PendingCloudwatchLogsExports`

    Specifies the CloudWatch logs to be exported.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to CloudWatch Logs.

      - *(string) --*
    """


_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is only included when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
      is currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently-in-progress change of the master credentials for the
      DB instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` | ``bring-your-own-license`` |
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
      is currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the CA certificate for the DB instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      Specifies the CloudWatch logs to be exported.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to CloudWatch Logs.

        - *(string) --*
    """


_ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "read replication."

    - **Normal** *(boolean) --*

      Boolean value that is true if the instance is operating normally, or false if the
      instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a StatusType of read replica, the values can be
      replicating, error, stopped, or terminated.

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientDescribeDbInstancesResponseDBInstancesTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientDescribeDbInstancesResponseDBInstancesOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[
            ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef
        ],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientDescribeDbInstancesResponseDBInstancesDomainMembershipsTypeDef
        ],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponse` `DBInstances`

    Contains the details of an Amazon Neptune DB instance.

    This data type is used as a response element in the  DescribeDBInstances action.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-supplied database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB instance.

    - **DBName** *(string) --*

      The database name.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size specified in gibibytes.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBSecurityGroups** *(list) --*

      Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
      ``DBSecurityGroup.Status`` subelements.

      - *(dict) --*

        Specifies membership in a designated DB security group.

        - **DBSecurityGroupName** *(string) --*

          The name of the DB security group.

        - **Status** *(string) --*

          The status of the DB security group.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **DBParameterGroups** *(list) --*

      Provides the list of DB parameter groups applied to this DB instance.

      - *(dict) --*

        The status of the DB parameter group.

        This data type is used as a response element in the following actions:

        *  CreateDBInstance

        *  DeleteDBInstance

        *  ModifyDBInstance

        *  RebootDBInstance

        - **DBParameterGroupName** *(string) --*

          The name of the DP parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group associated with the DB instance, including the
      name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the VpcId of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Contains a list of  Subnet elements.

        - *(dict) --*

          Specifies a subnet.

          This data type is used as a response element in the  DescribeDBSubnetGroups action.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the EC2 Availability Zone that the subnet is in.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is only included when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
        is currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently-in-progress change of the master credentials for the
        DB instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` | ``bring-your-own-license`` |
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
        is currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the CA certificate for the DB instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        Specifies the CloudWatch logs to be exported.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **MultiAZ** *(boolean) --*

      Specifies if the DB instance is a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

      Contains the identifier of the source DB instance if this DB instance is a Read Replica.

    - **ReadReplicaDBInstanceIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB instance.

      - *(string) --*

    - **ReadReplicaDBClusterIdentifiers** *(list) --*

      Contains one or more identifiers of DB clusters that are Read Replicas of this DB
      instance.

      - *(string) --*

    - **LicenseModel** *(string) --*

      License model information for this DB instance.

    - **Iops** *(integer) --*

      Specifies the Provisioned IOPS (I/O operations per second) value.

    - **OptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB instance.

      - *(dict) --*

        Provides information on the option groups the DB instance is a member of.

        - **OptionGroupName** *(string) --*

          The name of the option group that the instance belongs to.

        - **Status** *(string) --*

          The status of the DB instance's option group membership. Valid values are:
          ``in-sync`` , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply``
          , ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this instance is associated with.

    - **SecondaryAvailabilityZone** *(string) --*

      If present, specifies the name of the secondary Availability Zone for a DB instance with
      multi-AZ support.

    - **PubliclyAccessible** *(boolean) --*

      This flag should no longer be used.

    - **StatusInfos** *(list) --*

      The status of a Read Replica. If the instance is not a Read Replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "read replication."

        - **Normal** *(boolean) --*

          Boolean value that is true if the instance is operating normally, or false if the
          instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a StatusType of read replica, the values can be
          replicating, error, stopped, or terminated.

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **StorageType** *(string) --*

      Specifies the storage type associated with DB instance.

    - **TdeCredentialArn** *(string) --*

      The ARN from the key store with which the instance is associated for TDE encryption.

    - **DbInstancePort** *(integer) --*

      Specifies the port that the DB instance listens on. If the DB instance is part of a DB
      cluster, this can be a different port than the DB cluster port.

    - **DBClusterIdentifier** *(string) --*

      If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
      the DB instance is a member of.

    - **StorageEncrypted** *(boolean) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **KmsKeyId** *(string) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **DomainMemberships** *(list) --*

      Not supported

      - *(dict) --*

        An Active Directory Domain membership record associated with a DB instance.

        - **Domain** *(string) --*

          The identifier of the Active Directory Domain.

        - **Status** *(string) --*

          The status of the DB instance's Active Directory Domain membership, such as joined,
          pending-join, failed etc).

        - **FQDN** *(string) --*

          The fully qualified domain name of the Active Directory Domain.

        - **IAMRoleName** *(string) --*

          The name of the IAM role to be used when making API calls to the Directory Service.

    - **CopyTagsToSnapshot** *(boolean) --*

      Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

    - **MonitoringInterval** *(integer) --*

      The interval, in seconds, between points when Enhanced Monitoring metrics are collected
      for the DB instance.

    - **EnhancedMonitoringResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
      Enhanced Monitoring metrics data for the DB instance.

    - **MonitoringRoleArn** *(string) --*

      The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to
      Amazon CloudWatch Logs.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **Timezone** *(string) --*

      Not supported.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
      false.

    - **PerformanceInsightsEnabled** *(boolean) --*

      True if Performance Insights is enabled for the DB instance, and otherwise false.

    - **PerformanceInsightsKMSKeyId** *(string) --*

      The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
      the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
      encryption key.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientDescribeDbInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseTypeDef",
    {
        "Marker": str,
        "DBInstances": List[ClientDescribeDbInstancesResponseDBInstancesTypeDef],
    },
    total=False,
)


class ClientDescribeDbInstancesResponseTypeDef(
    _ClientDescribeDbInstancesResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbInstances` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **DBInstances** *(list) --*

      A list of  DBInstance instances.

      - *(dict) --*

        Contains the details of an Amazon Neptune DB instance.

        This data type is used as a response element in the  DescribeDBInstances action.

        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.

        - **DBInstanceClass** *(string) --*

          Contains the name of the compute and memory capacity class of the DB instance.

        - **Engine** *(string) --*

          Provides the name of the database engine to be used for this DB instance.

        - **DBInstanceStatus** *(string) --*

          Specifies the current state of this database.

        - **MasterUsername** *(string) --*

          Contains the master username for the DB instance.

        - **DBName** *(string) --*

          The database name.

        - **Endpoint** *(dict) --*

          Specifies the connection endpoint.

          - **Address** *(string) --*

            Specifies the DNS address of the DB instance.

          - **Port** *(integer) --*

            Specifies the port that the database engine is listening on.

          - **HostedZoneId** *(string) --*

            Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

        - **AllocatedStorage** *(integer) --*

          Specifies the allocated storage size specified in gibibytes.

        - **InstanceCreateTime** *(datetime) --*

          Provides the date and time the DB instance was created.

        - **PreferredBackupWindow** *(string) --*

          Specifies the daily time range during which automated backups are created if automated
          backups are enabled, as determined by the ``BackupRetentionPeriod`` .

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the number of days for which automatic DB snapshots are retained.

        - **DBSecurityGroups** *(list) --*

          Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
          ``DBSecurityGroup.Status`` subelements.

          - *(dict) --*

            Specifies membership in a designated DB security group.

            - **DBSecurityGroupName** *(string) --*

              The name of the DB security group.

            - **Status** *(string) --*

              The status of the DB security group.

        - **VpcSecurityGroups** *(list) --*

          Provides a list of VPC security group elements that the DB instance belongs to.

          - *(dict) --*

            This data type is used as a response element for queries on VPC security group
            membership.

            - **VpcSecurityGroupId** *(string) --*

              The name of the VPC security group.

            - **Status** *(string) --*

              The status of the VPC security group.

        - **DBParameterGroups** *(list) --*

          Provides the list of DB parameter groups applied to this DB instance.

          - *(dict) --*

            The status of the DB parameter group.

            This data type is used as a response element in the following actions:

            *  CreateDBInstance

            *  DeleteDBInstance

            *  ModifyDBInstance

            *  RebootDBInstance

            - **DBParameterGroupName** *(string) --*

              The name of the DP parameter group.

            - **ParameterApplyStatus** *(string) --*

              The status of parameter updates.

        - **AvailabilityZone** *(string) --*

          Specifies the name of the Availability Zone the DB instance is located in.

        - **DBSubnetGroup** *(dict) --*

          Specifies information on the subnet group associated with the DB instance, including the
          name, description, and subnets in the subnet group.

          - **DBSubnetGroupName** *(string) --*

            The name of the DB subnet group.

          - **DBSubnetGroupDescription** *(string) --*

            Provides the description of the DB subnet group.

          - **VpcId** *(string) --*

            Provides the VpcId of the DB subnet group.

          - **SubnetGroupStatus** *(string) --*

            Provides the status of the DB subnet group.

          - **Subnets** *(list) --*

            Contains a list of  Subnet elements.

            - *(dict) --*

              Specifies a subnet.

              This data type is used as a response element in the  DescribeDBSubnetGroups action.

              - **SubnetIdentifier** *(string) --*

                Specifies the identifier of the subnet.

              - **SubnetAvailabilityZone** *(dict) --*

                Specifies the EC2 Availability Zone that the subnet is in.

                - **Name** *(string) --*

                  The name of the availability zone.

              - **SubnetStatus** *(string) --*

                Specifies the status of the subnet.

          - **DBSubnetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) for the DB subnet group.

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which system maintenance can occur, in Universal
          Coordinated Time (UTC).

        - **PendingModifiedValues** *(dict) --*

          Specifies that changes to the DB instance are pending. This element is only included when
          changes are pending. Specific changes are identified by subelements.

          - **DBInstanceClass** *(string) --*

            Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
            currently being applied.

          - **AllocatedStorage** *(integer) --*

            Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
            is currently being applied.

          - **MasterUserPassword** *(string) --*

            Contains the pending or currently-in-progress change of the master credentials for the
            DB instance.

          - **Port** *(integer) --*

            Specifies the pending port for the DB instance.

          - **BackupRetentionPeriod** *(integer) --*

            Specifies the pending number of days for which automated backups are retained.

          - **MultiAZ** *(boolean) --*

            Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

          - **EngineVersion** *(string) --*

            Indicates the database engine version.

          - **LicenseModel** *(string) --*

            The license model for the DB instance.

            Valid values: ``license-included`` | ``bring-your-own-license`` |
            ``general-public-license``

          - **Iops** *(integer) --*

            Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
            currently being applied.

          - **DBInstanceIdentifier** *(string) --*

            Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
            is currently being applied.

          - **StorageType** *(string) --*

            Specifies the storage type to be associated with the DB instance.

          - **CACertificateIdentifier** *(string) --*

            Specifies the identifier of the CA certificate for the DB instance.

          - **DBSubnetGroupName** *(string) --*

            The new DB subnet group for the DB instance.

          - **PendingCloudwatchLogsExports** *(dict) --*

            Specifies the CloudWatch logs to be exported.

            - **LogTypesToEnable** *(list) --*

              Log types that are in the process of being deactivated. After they are deactivated,
              these log types aren't exported to CloudWatch Logs.

              - *(string) --*

            - **LogTypesToDisable** *(list) --*

              Log types that are in the process of being enabled. After they are enabled, these log
              types are exported to CloudWatch Logs.

              - *(string) --*

        - **LatestRestorableTime** *(datetime) --*

          Specifies the latest time to which a database can be restored with point-in-time restore.

        - **MultiAZ** *(boolean) --*

          Specifies if the DB instance is a Multi-AZ deployment.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **AutoMinorVersionUpgrade** *(boolean) --*

          Indicates that minor version patches are applied automatically.

        - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

          Contains the identifier of the source DB instance if this DB instance is a Read Replica.

        - **ReadReplicaDBInstanceIdentifiers** *(list) --*

          Contains one or more identifiers of the Read Replicas associated with this DB instance.

          - *(string) --*

        - **ReadReplicaDBClusterIdentifiers** *(list) --*

          Contains one or more identifiers of DB clusters that are Read Replicas of this DB
          instance.

          - *(string) --*

        - **LicenseModel** *(string) --*

          License model information for this DB instance.

        - **Iops** *(integer) --*

          Specifies the Provisioned IOPS (I/O operations per second) value.

        - **OptionGroupMemberships** *(list) --*

          Provides the list of option group memberships for this DB instance.

          - *(dict) --*

            Provides information on the option groups the DB instance is a member of.

            - **OptionGroupName** *(string) --*

              The name of the option group that the instance belongs to.

            - **Status** *(string) --*

              The status of the DB instance's option group membership. Valid values are:
              ``in-sync`` , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply``
              , ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

        - **CharacterSetName** *(string) --*

          If present, specifies the name of the character set that this instance is associated with.

        - **SecondaryAvailabilityZone** *(string) --*

          If present, specifies the name of the secondary Availability Zone for a DB instance with
          multi-AZ support.

        - **PubliclyAccessible** *(boolean) --*

          This flag should no longer be used.

        - **StatusInfos** *(list) --*

          The status of a Read Replica. If the instance is not a Read Replica, this is blank.

          - *(dict) --*

            Provides a list of status information for a DB instance.

            - **StatusType** *(string) --*

              This value is currently "read replication."

            - **Normal** *(boolean) --*

              Boolean value that is true if the instance is operating normally, or false if the
              instance is in an error state.

            - **Status** *(string) --*

              Status of the DB instance. For a StatusType of read replica, the values can be
              replicating, error, stopped, or terminated.

            - **Message** *(string) --*

              Details of the error if there is an error for the instance. If the instance is not in
              an error state, this value is blank.

        - **StorageType** *(string) --*

          Specifies the storage type associated with DB instance.

        - **TdeCredentialArn** *(string) --*

          The ARN from the key store with which the instance is associated for TDE encryption.

        - **DbInstancePort** *(integer) --*

          Specifies the port that the DB instance listens on. If the DB instance is part of a DB
          cluster, this can be a different port than the DB cluster port.

        - **DBClusterIdentifier** *(string) --*

          If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
          the DB instance is a member of.

        - **StorageEncrypted** *(boolean) --*

          Not supported: The encryption for DB instances is managed by the DB cluster.

        - **KmsKeyId** *(string) --*

          Not supported: The encryption for DB instances is managed by the DB cluster.

        - **DbiResourceId** *(string) --*

          The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
          in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

        - **CACertificateIdentifier** *(string) --*

          The identifier of the CA certificate for this DB instance.

        - **DomainMemberships** *(list) --*

          Not supported

          - *(dict) --*

            An Active Directory Domain membership record associated with a DB instance.

            - **Domain** *(string) --*

              The identifier of the Active Directory Domain.

            - **Status** *(string) --*

              The status of the DB instance's Active Directory Domain membership, such as joined,
              pending-join, failed etc).

            - **FQDN** *(string) --*

              The fully qualified domain name of the Active Directory Domain.

            - **IAMRoleName** *(string) --*

              The name of the IAM role to be used when making API calls to the Directory Service.

        - **CopyTagsToSnapshot** *(boolean) --*

          Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

        - **MonitoringInterval** *(integer) --*

          The interval, in seconds, between points when Enhanced Monitoring metrics are collected
          for the DB instance.

        - **EnhancedMonitoringResourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
          Enhanced Monitoring metrics data for the DB instance.

        - **MonitoringRoleArn** *(string) --*

          The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to
          Amazon CloudWatch Logs.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

        - **DBInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB instance.

        - **Timezone** *(string) --*

          Not supported.

        - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

          True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
          false.

        - **PerformanceInsightsEnabled** *(boolean) --*

          True if Performance Insights is enabled for the DB instance, and otherwise false.

        - **PerformanceInsightsKMSKeyId** *(string) --*

          The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
          the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
          encryption key.

        - **EnabledCloudwatchLogsExports** *(list) --*

          A list of log types that this DB instance is configured to export to CloudWatch Logs.

          - *(string) --*
    """


_ClientDescribeDbParameterGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbParameterGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeDbParameterGroupsFiltersTypeDef(
    _ClientDescribeDbParameterGroupsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbParameterGroups` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef(
    _ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbParameterGroupsResponse` `DBParameterGroups`

    Contains the details of an Amazon Neptune DB parameter group.

    This data type is used as a response element in the  DescribeDBParameterGroups action.

    - **DBParameterGroupName** *(string) --*

      Provides the name of the DB parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB parameter group is
      compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB parameter group.

    - **DBParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB parameter group.
    """


_ClientDescribeDbParameterGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBParameterGroups": List[
            ClientDescribeDbParameterGroupsResponseDBParameterGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbParameterGroupsResponseTypeDef(
    _ClientDescribeDbParameterGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbParameterGroups` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **DBParameterGroups** *(list) --*

      A list of  DBParameterGroup instances.

      - *(dict) --*

        Contains the details of an Amazon Neptune DB parameter group.

        This data type is used as a response element in the  DescribeDBParameterGroups action.

        - **DBParameterGroupName** *(string) --*

          Provides the name of the DB parameter group.

        - **DBParameterGroupFamily** *(string) --*

          Provides the name of the DB parameter group family that this DB parameter group is
          compatible with.

        - **Description** *(string) --*

          Provides the customer-specified description for this DB parameter group.

        - **DBParameterGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB parameter group.
    """


_ClientDescribeDbParametersFiltersTypeDef = TypedDict(
    "_ClientDescribeDbParametersFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeDbParametersFiltersTypeDef(
    _ClientDescribeDbParametersFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbParameters` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeDbParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeDbParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientDescribeDbParametersResponseParametersTypeDef(
    _ClientDescribeDbParametersResponseParametersTypeDef
):
    """
    Type definition for `ClientDescribeDbParametersResponse` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientDescribeDbParametersResponseTypeDef = TypedDict(
    "_ClientDescribeDbParametersResponseTypeDef",
    {
        "Parameters": List[ClientDescribeDbParametersResponseParametersTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeDbParametersResponseTypeDef(
    _ClientDescribeDbParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbParameters` `Response`

    - **Parameters** *(list) --*

      A list of  Parameter values.

      - *(dict) --*

        Specifies a parameter.

        - **ParameterName** *(string) --*

          Specifies the name of the parameter.

        - **ParameterValue** *(string) --*

          Specifies the value of the parameter.

        - **Description** *(string) --*

          Provides a description of the parameter.

        - **Source** *(string) --*

          Indicates the source of the parameter value.

        - **ApplyType** *(string) --*

          Specifies the engine specific parameters type.

        - **DataType** *(string) --*

          Specifies the valid data type for the parameter.

        - **AllowedValues** *(string) --*

          Specifies the valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest engine version to which the parameter can apply.

        - **ApplyMethod** *(string) --*

          Indicates when to apply parameter updates.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .
    """


_ClientDescribeDbSubnetGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeDbSubnetGroupsFiltersTypeDef(
    _ClientDescribeDbSubnetGroupsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbSubnetGroups` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnets` `SubnetAvailabilityZone`

    Specifies the EC2 Availability Zone that the subnet is in.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef(
    _ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef
):
    """
    Type definition for `ClientDescribeDbSubnetGroupsResponseDBSubnetGroups` `Subnets`

    Specifies a subnet.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the EC2 Availability Zone that the subnet is in.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef(
    _ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbSubnetGroupsResponse` `DBSubnetGroups`

    Contains the details of an Amazon Neptune DB subnet group.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the VpcId of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Contains a list of  Subnet elements.

      - *(dict) --*

        Specifies a subnet.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the EC2 Availability Zone that the subnet is in.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientDescribeDbSubnetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List[
            ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseTypeDef(
    _ClientDescribeDbSubnetGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbSubnetGroups` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **DBSubnetGroups** *(list) --*

      A list of  DBSubnetGroup instances.

      - *(dict) --*

        Contains the details of an Amazon Neptune DB subnet group.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the VpcId of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Contains a list of  Subnet elements.

          - *(dict) --*

            Specifies a subnet.

            This data type is used as a response element in the  DescribeDBSubnetGroups action.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the EC2 Availability Zone that the subnet is in.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientDescribeEngineDefaultClusterParametersFiltersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeEngineDefaultClusterParametersFiltersTypeDef(
    _ClientDescribeEngineDefaultClusterParametersFiltersTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultClusterParameters` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef(
    _ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultClusterParametersResponseEngineDefaults` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being
      changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef(
    _ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultClusterParametersResponse` `EngineDefaults`

    Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.

    - **DBParameterGroupFamily** *(string) --*

      Specifies the name of the DB parameter group family that the engine default parameters
      apply to.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous EngineDefaults request. If this
      parameter is specified, the response includes only records beyond the marker, up to the
      value specified by ``MaxRecords`` .

    - **Parameters** *(list) --*

      Contains a list of engine default parameters.

      - *(dict) --*

        Specifies a parameter.

        - **ParameterName** *(string) --*

          Specifies the name of the parameter.

        - **ParameterValue** *(string) --*

          Specifies the value of the parameter.

        - **Description** *(string) --*

          Provides a description of the parameter.

        - **Source** *(string) --*

          Indicates the source of the parameter value.

        - **ApplyType** *(string) --*

          Specifies the engine specific parameters type.

        - **DataType** *(string) --*

          Specifies the valid data type for the parameter.

        - **AllowedValues** *(string) --*

          Specifies the valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being
          changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest engine version to which the parameter can apply.

        - **ApplyMethod** *(string) --*

          Indicates when to apply parameter updates.
    """


_ClientDescribeEngineDefaultClusterParametersResponseTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersResponseTypeDef",
    {
        "EngineDefaults": ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef
    },
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersResponseTypeDef(
    _ClientDescribeEngineDefaultClusterParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultClusterParameters` `Response`

    - **EngineDefaults** *(dict) --*

      Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.

      - **DBParameterGroupFamily** *(string) --*

        Specifies the name of the DB parameter group family that the engine default parameters
        apply to.

      - **Marker** *(string) --*

        An optional pagination token provided by a previous EngineDefaults request. If this
        parameter is specified, the response includes only records beyond the marker, up to the
        value specified by ``MaxRecords`` .

      - **Parameters** *(list) --*

        Contains a list of engine default parameters.

        - *(dict) --*

          Specifies a parameter.

          - **ParameterName** *(string) --*

            Specifies the name of the parameter.

          - **ParameterValue** *(string) --*

            Specifies the value of the parameter.

          - **Description** *(string) --*

            Provides a description of the parameter.

          - **Source** *(string) --*

            Indicates the source of the parameter value.

          - **ApplyType** *(string) --*

            Specifies the engine specific parameters type.

          - **DataType** *(string) --*

            Specifies the valid data type for the parameter.

          - **AllowedValues** *(string) --*

            Specifies the valid range of values for the parameter.

          - **IsModifiable** *(boolean) --*

            Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
            parameters have security or operational implications that prevent them from being
            changed.

          - **MinimumEngineVersion** *(string) --*

            The earliest engine version to which the parameter can apply.

          - **ApplyMethod** *(string) --*

            Indicates when to apply parameter updates.
    """


_ClientDescribeEngineDefaultParametersFiltersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeEngineDefaultParametersFiltersTypeDef(
    _ClientDescribeEngineDefaultParametersFiltersTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultParameters` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultParametersResponseEngineDefaults` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being
      changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultParametersResponse` `EngineDefaults`

    Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.

    - **DBParameterGroupFamily** *(string) --*

      Specifies the name of the DB parameter group family that the engine default parameters
      apply to.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous EngineDefaults request. If this
      parameter is specified, the response includes only records beyond the marker, up to the
      value specified by ``MaxRecords`` .

    - **Parameters** *(list) --*

      Contains a list of engine default parameters.

      - *(dict) --*

        Specifies a parameter.

        - **ParameterName** *(string) --*

          Specifies the name of the parameter.

        - **ParameterValue** *(string) --*

          Specifies the value of the parameter.

        - **Description** *(string) --*

          Provides a description of the parameter.

        - **Source** *(string) --*

          Indicates the source of the parameter value.

        - **ApplyType** *(string) --*

          Specifies the engine specific parameters type.

        - **DataType** *(string) --*

          Specifies the valid data type for the parameter.

        - **AllowedValues** *(string) --*

          Specifies the valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being
          changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest engine version to which the parameter can apply.

        - **ApplyMethod** *(string) --*

          Indicates when to apply parameter updates.
    """


_ClientDescribeEngineDefaultParametersResponseTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseTypeDef",
    {
        "EngineDefaults": ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef
    },
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseTypeDef(
    _ClientDescribeEngineDefaultParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultParameters` `Response`

    - **EngineDefaults** *(dict) --*

      Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.

      - **DBParameterGroupFamily** *(string) --*

        Specifies the name of the DB parameter group family that the engine default parameters
        apply to.

      - **Marker** *(string) --*

        An optional pagination token provided by a previous EngineDefaults request. If this
        parameter is specified, the response includes only records beyond the marker, up to the
        value specified by ``MaxRecords`` .

      - **Parameters** *(list) --*

        Contains a list of engine default parameters.

        - *(dict) --*

          Specifies a parameter.

          - **ParameterName** *(string) --*

            Specifies the name of the parameter.

          - **ParameterValue** *(string) --*

            Specifies the value of the parameter.

          - **Description** *(string) --*

            Provides a description of the parameter.

          - **Source** *(string) --*

            Indicates the source of the parameter value.

          - **ApplyType** *(string) --*

            Specifies the engine specific parameters type.

          - **DataType** *(string) --*

            Specifies the valid data type for the parameter.

          - **AllowedValues** *(string) --*

            Specifies the valid range of values for the parameter.

          - **IsModifiable** *(boolean) --*

            Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
            parameters have security or operational implications that prevent them from being
            changed.

          - **MinimumEngineVersion** *(string) --*

            The earliest engine version to which the parameter can apply.

          - **ApplyMethod** *(string) --*

            Indicates when to apply parameter updates.
    """


_ClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeEventCategoriesFiltersTypeDef(
    _ClientDescribeEventCategoriesFiltersTypeDef
):
    """
    Type definition for `ClientDescribeEventCategories` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    {"SourceType": str, "EventCategories": List[str]},
    total=False,
)


class ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef(
    _ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef
):
    """
    Type definition for `ClientDescribeEventCategoriesResponse` `EventCategoriesMapList`

    Contains the results of a successful invocation of the  DescribeEventCategories action.

    - **SourceType** *(string) --*

      The source type that the returned categories belong to

    - **EventCategories** *(list) --*

      The event categories for the specified source type

      - *(string) --*
    """


_ClientDescribeEventCategoriesResponseTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoriesMapList": List[
            ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeEventCategoriesResponseTypeDef(
    _ClientDescribeEventCategoriesResponseTypeDef
):
    """
    Type definition for `ClientDescribeEventCategories` `Response`

    - **EventCategoriesMapList** *(list) --*

      A list of EventCategoriesMap data types.

      - *(dict) --*

        Contains the results of a successful invocation of the  DescribeEventCategories action.

        - **SourceType** *(string) --*

          The source type that the returned categories belong to

        - **EventCategories** *(list) --*

          The event categories for the specified source type

          - *(string) --*
    """


_ClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeEventSubscriptionsFiltersTypeDef(
    _ClientDescribeEventSubscriptionsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeEventSubscriptions` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef(
    _ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
):
    """
    Type definition for `ClientDescribeEventSubscriptionsResponse` `EventSubscriptionsList`

    Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the event notification subscription.

    - **Status** *(string) --*

      The status of the event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that Neptune no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the event notification subscription was created.

    - **SourceType** *(string) --*

      The source type for the event notification subscription.

    - **SourceIdsList** *(list) --*

      A list of source IDs for the event notification subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A list of event categories for the event notification subscription.

      - *(string) --*

    - **Enabled** *(boolean) --*

      A Boolean value indicating if the subscription is enabled. True indicates the
      subscription is enabled.

    - **EventSubscriptionArn** *(string) --*

      The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientDescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "_ClientDescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List[
            ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEventSubscriptionsResponseTypeDef(
    _ClientDescribeEventSubscriptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEventSubscriptions` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions
      request. If this parameter is specified, the response includes only records beyond the
      marker, up to the value specified by ``MaxRecords`` .

    - **EventSubscriptionsList** *(list) --*

      A list of EventSubscriptions data types.

      - *(dict) --*

        Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the event notification subscription.

        - **CustSubscriptionId** *(string) --*

          The event notification subscription Id.

        - **SnsTopicArn** *(string) --*

          The topic ARN of the event notification subscription.

        - **Status** *(string) --*

          The status of the event notification subscription.

          Constraints:

          Can be one of the following: creating | modifying | deleting | active | no-permission |
          topic-not-exist

          The status "no-permission" indicates that Neptune no longer has permission to post to the
          SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
          subscription was created.

        - **SubscriptionCreationTime** *(string) --*

          The time the event notification subscription was created.

        - **SourceType** *(string) --*

          The source type for the event notification subscription.

        - **SourceIdsList** *(list) --*

          A list of source IDs for the event notification subscription.

          - *(string) --*

        - **EventCategoriesList** *(list) --*

          A list of event categories for the event notification subscription.

          - *(string) --*

        - **Enabled** *(boolean) --*

          A Boolean value indicating if the subscription is enabled. True indicates the
          subscription is enabled.

        - **EventSubscriptionArn** *(string) --*

          The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientDescribeEventsFiltersTypeDef = TypedDict(
    "_ClientDescribeEventsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeEventsFiltersTypeDef(_ClientDescribeEventsFiltersTypeDef):
    """
    Type definition for `ClientDescribeEvents` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)


class ClientDescribeEventsResponseEventsTypeDef(
    _ClientDescribeEventsResponseEventsTypeDef
):
    """
    Type definition for `ClientDescribeEventsResponse` `Events`

    This data type is used as a response element in the  DescribeEvents action.

    - **SourceIdentifier** *(string) --*

      Provides the identifier for the source of the event.

    - **SourceType** *(string) --*

      Specifies the source type for this event.

    - **Message** *(string) --*

      Provides the text of this event.

    - **EventCategories** *(list) --*

      Specifies the category for the event.

      - *(string) --*

    - **Date** *(datetime) --*

      Specifies the date and time of the event.

    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) for the event.
    """


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    Type definition for `ClientDescribeEvents` `Response`

    - **Marker** *(string) --*

      An optional pagination token provided by a previous Events request. If this parameter is
      specified, the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **Events** *(list) --*

      A list of  Event instances.

      - *(dict) --*

        This data type is used as a response element in the  DescribeEvents action.

        - **SourceIdentifier** *(string) --*

          Provides the identifier for the source of the event.

        - **SourceType** *(string) --*

          Specifies the source type for this event.

        - **Message** *(string) --*

          Provides the text of this event.

        - **EventCategories** *(list) --*

          Specifies the category for the event.

          - *(string) --*

        - **Date** *(datetime) --*

          Specifies the date and time of the event.

        - **SourceArn** *(string) --*

          The Amazon Resource Name (ARN) for the event.
    """


_ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeOrderableDbInstanceOptions` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
):
    """
    Type definition for `ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptions` `AvailabilityZones`

    Specifies an Availability Zone.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List[
            ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
        ],
        "MultiAZCapable": bool,
        "ReadReplicaCapable": bool,
        "Vpc": bool,
        "SupportsStorageEncryption": bool,
        "StorageType": str,
        "SupportsIops": bool,
        "SupportsEnhancedMonitoring": bool,
        "SupportsIAMDatabaseAuthentication": bool,
        "SupportsPerformanceInsights": bool,
        "MinStorageSize": int,
        "MaxStorageSize": int,
        "MinIopsPerDbInstance": int,
        "MaxIopsPerDbInstance": int,
        "MinIopsPerGib": float,
        "MaxIopsPerGib": float,
    },
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef
):
    """
    Type definition for `ClientDescribeOrderableDbInstanceOptionsResponse` `OrderableDBInstanceOptions`

    Contains a list of available options for a DB instance.

    This data type is used as a response element in the  DescribeOrderableDBInstanceOptions
    action.

    - **Engine** *(string) --*

      The engine type of a DB instance.

    - **EngineVersion** *(string) --*

      The engine version of a DB instance.

    - **DBInstanceClass** *(string) --*

      The DB instance class for a DB instance.

    - **LicenseModel** *(string) --*

      The license model for a DB instance.

    - **AvailabilityZones** *(list) --*

      A list of Availability Zones for a DB instance.

      - *(dict) --*

        Specifies an Availability Zone.

        - **Name** *(string) --*

          The name of the availability zone.

    - **MultiAZCapable** *(boolean) --*

      Indicates whether a DB instance is Multi-AZ capable.

    - **ReadReplicaCapable** *(boolean) --*

      Indicates whether a DB instance can have a Read Replica.

    - **Vpc** *(boolean) --*

      Indicates whether a DB instance is in a VPC.

    - **SupportsStorageEncryption** *(boolean) --*

      Indicates whether a DB instance supports encrypted storage.

    - **StorageType** *(string) --*

      Indicates the storage type for a DB instance.

    - **SupportsIops** *(boolean) --*

      Indicates whether a DB instance supports provisioned IOPS.

    - **SupportsEnhancedMonitoring** *(boolean) --*

      Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60
      seconds.

    - **SupportsIAMDatabaseAuthentication** *(boolean) --*

      Indicates whether a DB instance supports IAM database authentication.

    - **SupportsPerformanceInsights** *(boolean) --*

      True if a DB instance supports Performance Insights, otherwise false.

    - **MinStorageSize** *(integer) --*

      Minimum storage size for a DB instance.

    - **MaxStorageSize** *(integer) --*

      Maximum storage size for a DB instance.

    - **MinIopsPerDbInstance** *(integer) --*

      Minimum total provisioned IOPS for a DB instance.

    - **MaxIopsPerDbInstance** *(integer) --*

      Maximum total provisioned IOPS for a DB instance.

    - **MinIopsPerGib** *(float) --*

      Minimum provisioned IOPS per GiB for a DB instance.

    - **MaxIopsPerGib** *(float) --*

      Maximum provisioned IOPS per GiB for a DB instance.
    """


_ClientDescribeOrderableDbInstanceOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsResponseTypeDef",
    {
        "OrderableDBInstanceOptions": List[
            ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeOrderableDbInstanceOptions` `Response`

    - **OrderableDBInstanceOptions** *(list) --*

      An  OrderableDBInstanceOption structure containing information about orderable options for
      the DB instance.

      - *(dict) --*

        Contains a list of available options for a DB instance.

        This data type is used as a response element in the  DescribeOrderableDBInstanceOptions
        action.

        - **Engine** *(string) --*

          The engine type of a DB instance.

        - **EngineVersion** *(string) --*

          The engine version of a DB instance.

        - **DBInstanceClass** *(string) --*

          The DB instance class for a DB instance.

        - **LicenseModel** *(string) --*

          The license model for a DB instance.

        - **AvailabilityZones** *(list) --*

          A list of Availability Zones for a DB instance.

          - *(dict) --*

            Specifies an Availability Zone.

            - **Name** *(string) --*

              The name of the availability zone.

        - **MultiAZCapable** *(boolean) --*

          Indicates whether a DB instance is Multi-AZ capable.

        - **ReadReplicaCapable** *(boolean) --*

          Indicates whether a DB instance can have a Read Replica.

        - **Vpc** *(boolean) --*

          Indicates whether a DB instance is in a VPC.

        - **SupportsStorageEncryption** *(boolean) --*

          Indicates whether a DB instance supports encrypted storage.

        - **StorageType** *(string) --*

          Indicates the storage type for a DB instance.

        - **SupportsIops** *(boolean) --*

          Indicates whether a DB instance supports provisioned IOPS.

        - **SupportsEnhancedMonitoring** *(boolean) --*

          Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60
          seconds.

        - **SupportsIAMDatabaseAuthentication** *(boolean) --*

          Indicates whether a DB instance supports IAM database authentication.

        - **SupportsPerformanceInsights** *(boolean) --*

          True if a DB instance supports Performance Insights, otherwise false.

        - **MinStorageSize** *(integer) --*

          Minimum storage size for a DB instance.

        - **MaxStorageSize** *(integer) --*

          Maximum storage size for a DB instance.

        - **MinIopsPerDbInstance** *(integer) --*

          Minimum total provisioned IOPS for a DB instance.

        - **MaxIopsPerDbInstance** *(integer) --*

          Maximum total provisioned IOPS for a DB instance.

        - **MinIopsPerGib** *(float) --*

          Minimum provisioned IOPS per GiB for a DB instance.

        - **MaxIopsPerGib** *(float) --*

          Maximum provisioned IOPS per GiB for a DB instance.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous OrderableDBInstanceOptions request. If
      this parameter is specified, the response includes only records beyond the marker, up to the
      value specified by ``MaxRecords`` .
    """


_ClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribePendingMaintenanceActionsFiltersTypeDef(
    _ClientDescribePendingMaintenanceActionsFiltersTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActions` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActions` `PendingMaintenanceActionDetails`

    Provides information about a pending maintenance action for a resource.

    - **Action** *(string) --*

      The type of pending maintenance action that is available for the resource.

    - **AutoAppliedAfterDate** *(datetime) --*

      The date of the maintenance window when the action is applied. The maintenance action
      is applied to the resource during its first maintenance window after this date. If
      this date is specified, any ``next-maintenance`` opt-in requests are ignored.

    - **ForcedApplyDate** *(datetime) --*

      The date when the maintenance action is automatically applied. The maintenance action
      is applied to the resource on this date regardless of the maintenance window for the
      resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

    - **OptInStatus** *(string) --*

      Indicates the type of opt-in request that has been received for the resource.

    - **CurrentApplyDate** *(datetime) --*

      The effective date when the pending maintenance action is applied to the resource.
      This date takes into account opt-in requests received from the
      ApplyPendingMaintenanceAction API, the ``AutoAppliedAfterDate`` , and the
      ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
      and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

    - **Description** *(string) --*

      A description providing more detail about the maintenance action.
    """


_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef(
    _ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActionsResponse` `PendingMaintenanceActions`

    Describes the pending maintenance actions for a resource.

    - **ResourceIdentifier** *(string) --*

      The ARN of the resource that has pending maintenance actions.

    - **PendingMaintenanceActionDetails** *(list) --*

      A list that provides details about the pending maintenance actions for the resource.

      - *(dict) --*

        Provides information about a pending maintenance action for a resource.

        - **Action** *(string) --*

          The type of pending maintenance action that is available for the resource.

        - **AutoAppliedAfterDate** *(datetime) --*

          The date of the maintenance window when the action is applied. The maintenance action
          is applied to the resource during its first maintenance window after this date. If
          this date is specified, any ``next-maintenance`` opt-in requests are ignored.

        - **ForcedApplyDate** *(datetime) --*

          The date when the maintenance action is automatically applied. The maintenance action
          is applied to the resource on this date regardless of the maintenance window for the
          resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

        - **OptInStatus** *(string) --*

          Indicates the type of opt-in request that has been received for the resource.

        - **CurrentApplyDate** *(datetime) --*

          The effective date when the pending maintenance action is applied to the resource.
          This date takes into account opt-in requests received from the
          ApplyPendingMaintenanceAction API, the ``AutoAppliedAfterDate`` , and the
          ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
          and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

        - **Description** *(string) --*

          A description providing more detail about the maintenance action.
    """


_ClientDescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponseTypeDef(
    _ClientDescribePendingMaintenanceActionsResponseTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActions` `Response`

    - **PendingMaintenanceActions** *(list) --*

      A list of the pending maintenance actions for the resource.

      - *(dict) --*

        Describes the pending maintenance actions for a resource.

        - **ResourceIdentifier** *(string) --*

          The ARN of the resource that has pending maintenance actions.

        - **PendingMaintenanceActionDetails** *(list) --*

          A list that provides details about the pending maintenance actions for the resource.

          - *(dict) --*

            Provides information about a pending maintenance action for a resource.

            - **Action** *(string) --*

              The type of pending maintenance action that is available for the resource.

            - **AutoAppliedAfterDate** *(datetime) --*

              The date of the maintenance window when the action is applied. The maintenance action
              is applied to the resource during its first maintenance window after this date. If
              this date is specified, any ``next-maintenance`` opt-in requests are ignored.

            - **ForcedApplyDate** *(datetime) --*

              The date when the maintenance action is automatically applied. The maintenance action
              is applied to the resource on this date regardless of the maintenance window for the
              resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

            - **OptInStatus** *(string) --*

              Indicates the type of opt-in request that has been received for the resource.

            - **CurrentApplyDate** *(datetime) --*

              The effective date when the pending maintenance action is applied to the resource.
              This date takes into account opt-in requests received from the
              ApplyPendingMaintenanceAction API, the ``AutoAppliedAfterDate`` , and the
              ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
              and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

            - **Description** *(string) --*

              A description providing more detail about the maintenance action.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous ``DescribePendingMaintenanceActions``
      request. If this parameter is specified, the response includes only records beyond the
      marker, up to a number of records specified by ``MaxRecords`` .
    """


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef",
    {"From": float, "To": float},
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef
):
    """
    Type definition for `ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorage` `IopsToStorageRatio`

    A range of double values.

    - **From** *(float) --*

      The minimum value in the range.

    - **To** *(float) --*

      The maximum value in the range.
    """


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef",
    {"From": int, "To": int, "Step": int},
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef
):
    """
    Type definition for `ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorage` `ProvisionedIops`

    A range of integer values.

    - **From** *(integer) --*

      The minimum value in the range.

    - **To** *(integer) --*

      The maximum value in the range.

    - **Step** *(integer) --*

      The step value for the range. For example, if you have a range of 5,000 to 10,000,
      with a step value of 1,000, the valid values start at 5,000 and step up by 1,000.
      Even though 7,500 is within the range, it isn't a valid value for the range. The
      valid values are 5,000, 6,000, 7,000, 8,000...
    """


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef",
    {"From": int, "To": int, "Step": int},
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef
):
    """
    Type definition for `ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorage` `StorageSize`

    A range of integer values.

    - **From** *(integer) --*

      The minimum value in the range.

    - **To** *(integer) --*

      The maximum value in the range.

    - **Step** *(integer) --*

      The step value for the range. For example, if you have a range of 5,000 to 10,000,
      with a step value of 1,000, the valid values start at 5,000 and step up by 1,000.
      Even though 7,500 is within the range, it isn't a valid value for the range. The
      valid values are 5,000, 6,000, 7,000, 8,000...
    """


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef",
    {
        "StorageType": str,
        "StorageSize": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageStorageSizeTypeDef
        ],
        "ProvisionedIops": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageProvisionedIopsTypeDef
        ],
        "IopsToStorageRatio": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageIopsToStorageRatioTypeDef
        ],
    },
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef
):
    """
    Type definition for `ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessage` `Storage`

    Information about valid modifications that you can make to your DB instance.

    Contains the result of a successful call to the  DescribeValidDBInstanceModifications
    action.

    - **StorageType** *(string) --*

      The valid storage types for your DB instance. For example, gp2, io1.

    - **StorageSize** *(list) --*

      The valid range of storage in gibibytes. For example, 100 to 16384.

      - *(dict) --*

        A range of integer values.

        - **From** *(integer) --*

          The minimum value in the range.

        - **To** *(integer) --*

          The maximum value in the range.

        - **Step** *(integer) --*

          The step value for the range. For example, if you have a range of 5,000 to 10,000,
          with a step value of 1,000, the valid values start at 5,000 and step up by 1,000.
          Even though 7,500 is within the range, it isn't a valid value for the range. The
          valid values are 5,000, 6,000, 7,000, 8,000...

    - **ProvisionedIops** *(list) --*

      The valid range of provisioned IOPS. For example, 1000-20000.

      - *(dict) --*

        A range of integer values.

        - **From** *(integer) --*

          The minimum value in the range.

        - **To** *(integer) --*

          The maximum value in the range.

        - **Step** *(integer) --*

          The step value for the range. For example, if you have a range of 5,000 to 10,000,
          with a step value of 1,000, the valid values start at 5,000 and step up by 1,000.
          Even though 7,500 is within the range, it isn't a valid value for the range. The
          valid values are 5,000, 6,000, 7,000, 8,000...

    - **IopsToStorageRatio** *(list) --*

      The valid range of Provisioned IOPS to gibibytes of storage multiplier. For example,
      3-10, which means that provisioned IOPS can be between 3 and 10 times storage.

      - *(dict) --*

        A range of double values.

        - **From** *(float) --*

          The minimum value in the range.

        - **To** *(float) --*

          The maximum value in the range.
    """


_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": List[
            ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageStorageTypeDef
        ]
    },
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef
):
    """
    Type definition for `ClientDescribeValidDbInstanceModificationsResponse` `ValidDBInstanceModificationsMessage`

    Information about valid modifications that you can make to your DB instance. Contains the
    result of a successful call to the  DescribeValidDBInstanceModifications action. You can use
    this information when you call  ModifyDBInstance .

    - **Storage** *(list) --*

      Valid storage options for your DB instance.

      - *(dict) --*

        Information about valid modifications that you can make to your DB instance.

        Contains the result of a successful call to the  DescribeValidDBInstanceModifications
        action.

        - **StorageType** *(string) --*

          The valid storage types for your DB instance. For example, gp2, io1.

        - **StorageSize** *(list) --*

          The valid range of storage in gibibytes. For example, 100 to 16384.

          - *(dict) --*

            A range of integer values.

            - **From** *(integer) --*

              The minimum value in the range.

            - **To** *(integer) --*

              The maximum value in the range.

            - **Step** *(integer) --*

              The step value for the range. For example, if you have a range of 5,000 to 10,000,
              with a step value of 1,000, the valid values start at 5,000 and step up by 1,000.
              Even though 7,500 is within the range, it isn't a valid value for the range. The
              valid values are 5,000, 6,000, 7,000, 8,000...

        - **ProvisionedIops** *(list) --*

          The valid range of provisioned IOPS. For example, 1000-20000.

          - *(dict) --*

            A range of integer values.

            - **From** *(integer) --*

              The minimum value in the range.

            - **To** *(integer) --*

              The maximum value in the range.

            - **Step** *(integer) --*

              The step value for the range. For example, if you have a range of 5,000 to 10,000,
              with a step value of 1,000, the valid values start at 5,000 and step up by 1,000.
              Even though 7,500 is within the range, it isn't a valid value for the range. The
              valid values are 5,000, 6,000, 7,000, 8,000...

        - **IopsToStorageRatio** *(list) --*

          The valid range of Provisioned IOPS to gibibytes of storage multiplier. For example,
          3-10, which means that provisioned IOPS can be between 3 and 10 times storage.

          - *(dict) --*

            A range of double values.

            - **From** *(float) --*

              The minimum value in the range.

            - **To** *(float) --*

              The maximum value in the range.
    """


_ClientDescribeValidDbInstanceModificationsResponseTypeDef = TypedDict(
    "_ClientDescribeValidDbInstanceModificationsResponseTypeDef",
    {
        "ValidDBInstanceModificationsMessage": ClientDescribeValidDbInstanceModificationsResponseValidDBInstanceModificationsMessageTypeDef
    },
    total=False,
)


class ClientDescribeValidDbInstanceModificationsResponseTypeDef(
    _ClientDescribeValidDbInstanceModificationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeValidDbInstanceModifications` `Response`

    - **ValidDBInstanceModificationsMessage** *(dict) --*

      Information about valid modifications that you can make to your DB instance. Contains the
      result of a successful call to the  DescribeValidDBInstanceModifications action. You can use
      this information when you call  ModifyDBInstance .

      - **Storage** *(list) --*

        Valid storage options for your DB instance.

        - *(dict) --*

          Information about valid modifications that you can make to your DB instance.

          Contains the result of a successful call to the  DescribeValidDBInstanceModifications
          action.

          - **StorageType** *(string) --*

            The valid storage types for your DB instance. For example, gp2, io1.

          - **StorageSize** *(list) --*

            The valid range of storage in gibibytes. For example, 100 to 16384.

            - *(dict) --*

              A range of integer values.

              - **From** *(integer) --*

                The minimum value in the range.

              - **To** *(integer) --*

                The maximum value in the range.

              - **Step** *(integer) --*

                The step value for the range. For example, if you have a range of 5,000 to 10,000,
                with a step value of 1,000, the valid values start at 5,000 and step up by 1,000.
                Even though 7,500 is within the range, it isn't a valid value for the range. The
                valid values are 5,000, 6,000, 7,000, 8,000...

          - **ProvisionedIops** *(list) --*

            The valid range of provisioned IOPS. For example, 1000-20000.

            - *(dict) --*

              A range of integer values.

              - **From** *(integer) --*

                The minimum value in the range.

              - **To** *(integer) --*

                The maximum value in the range.

              - **Step** *(integer) --*

                The step value for the range. For example, if you have a range of 5,000 to 10,000,
                with a step value of 1,000, the valid values start at 5,000 and step up by 1,000.
                Even though 7,500 is within the range, it isn't a valid value for the range. The
                valid values are 5,000, 6,000, 7,000, 8,000...

          - **IopsToStorageRatio** *(list) --*

            The valid range of Provisioned IOPS to gibibytes of storage multiplier. For example,
            3-10, which means that provisioned IOPS can be between 3 and 10 times storage.

            - *(dict) --*

              A range of double values.

              - **From** *(float) --*

                The minimum value in the range.

              - **To** *(float) --*

                The maximum value in the range.
    """


_ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientFailoverDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The Status
      property returns one of the following values:

      * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
      is unable to assume the IAM role in order to access other AWS services on your behalf.
    """


_ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientFailoverDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      Value that is ``true`` if the cluster member is the primary instance for the DB cluster
      and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.
    """


_ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientFailoverDbClusterResponseDBCluster` `DBClusterOptionGroupMemberships`

    Contains status information for a DB cluster option group.

    - **DBClusterOptionGroupName** *(string) --*

      Specifies the name of the DB cluster option group.

    - **Status** *(string) --*

      Specifies the status of the DB cluster option group.
    """


_ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientFailoverDbClusterResponseDBCluster` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientFailoverDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientFailoverDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterTypeDef(
    _ClientFailoverDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientFailoverDbClusterResponse` `DBCluster`

    Contains the details of an Amazon Neptune DB cluster.

    This data type is used as a response element in the  DescribeDBClusters action.

    - **AllocatedStorage** *(integer) --*

       ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
       fixed, but instead automatically adjusts as needed.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
      in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this cluster is associated with.

    - **DatabaseName** *(string) --*

      Contains the name of the initial database of this DB cluster that was provided at create
      time, if one was specified when the DB cluster was created. This same name is returned for
      the life of the DB cluster.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group associated with the DB cluster, including the
      name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      Specifies the earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
      connections across the Read Replicas that are available in a DB cluster. As clients request
      new connections to the reader endpoint, Neptune distributes the connection requests among
      the Read Replicas in the DB cluster. This functionality can help balance your read workload
      across multiple Read Replicas in your DB cluster.

      If a failover occurs, and the Read Replica that you are connected to is promoted to be the
      primary instance, your connection is dropped. To continue sending your read workload to
      other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB cluster.

    - **DBClusterOptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB cluster.

      - *(dict) --*

        Contains status information for a DB cluster option group.

        - **DBClusterOptionGroupName** *(string) --*

          Specifies the name of the DB cluster option group.

        - **Status** *(string) --*

          Specifies the status of the DB cluster option group.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **ReplicationSourceIdentifier** *(string) --*

      Not supported by Neptune.

    - **ReadReplicaIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB cluster.

      - *(string) --*

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          Value that is ``true`` if the cluster member is the primary instance for the DB cluster
          and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security groups that the DB cluster belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The Status
          property returns one of the following values:

          * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
          is unable to assume the IAM role in order to access other AWS services on your behalf.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.

    - **CloneGroupId** *(string) --*

      Identifies the clone group to which the DB cluster is associated.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientFailoverDbClusterResponseTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseTypeDef",
    {"DBCluster": ClientFailoverDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientFailoverDbClusterResponseTypeDef(_ClientFailoverDbClusterResponseTypeDef):
    """
    Type definition for `ClientFailoverDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.

      This data type is used as a response element in the  DescribeDBClusters action.

      - **AllocatedStorage** *(integer) --*

         ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
         fixed, but instead automatically adjusts as needed.

      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
        in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this cluster is associated with.

      - **DatabaseName** *(string) --*

        Contains the name of the initial database of this DB cluster that was provided at create
        time, if one was specified when the DB cluster was created. This same name is returned for
        the life of the DB cluster.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group associated with the DB cluster, including the
        name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        Specifies the earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
        connections across the Read Replicas that are available in a DB cluster. As clients request
        new connections to the reader endpoint, Neptune distributes the connection requests among
        the Read Replicas in the DB cluster. This functionality can help balance your read workload
        across multiple Read Replicas in your DB cluster.

        If a failover occurs, and the Read Replica that you are connected to is promoted to be the
        primary instance, your connection is dropped. To continue sending your read workload to
        other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB cluster.

      - **DBClusterOptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB cluster.

        - *(dict) --*

          Contains status information for a DB cluster option group.

          - **DBClusterOptionGroupName** *(string) --*

            Specifies the name of the DB cluster option group.

          - **Status** *(string) --*

            Specifies the status of the DB cluster option group.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **ReplicationSourceIdentifier** *(string) --*

        Not supported by Neptune.

      - **ReadReplicaIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB cluster.

        - *(string) --*

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            Value that is ``true`` if the cluster member is the primary instance for the DB cluster
            and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which a Read Replica is promoted to the primary
            instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security groups that the DB cluster belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The Status
            property returns one of the following values:

            * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
            is unable to assume the IAM role in order to access other AWS services on your behalf.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
        is enabled, and otherwise false.

      - **CloneGroupId** *(string) --*

        Identifies the clone group to which the DB cluster is associated.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientListTagsForResourceFiltersTypeDef = TypedDict(
    "_ClientListTagsForResourceFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientListTagsForResourceFiltersTypeDef(_ClientListTagsForResourceFiltersTypeDef):
    """
    Type definition for `ClientListTagsForResource` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagListTypeDef(
    _ClientListTagsForResourceResponseTagListTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `TagList`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
      '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only
      contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
      '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **TagList** *(list) --*

      List of tags returned by the ListTagsForResource operation.

      - *(dict) --*

        Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

        - **Key** *(string) --*

          A key is the required name of the tag. The string value can be from 1 to 128 Unicode
          characters in length and can't be prefixed with "aws:" or "rds:". The string can only
          contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
          '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        - **Value** *(string) --*

          A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
          characters in length and can't be prefixed with "aws:" or "rds:". The string can only
          contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
          '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "_ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    {"EnableLogTypes": List[str], "DisableLogTypes": List[str]},
    total=False,
)


class ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef(
    _ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef
):
    """
    Type definition for `ClientModifyDbCluster` `CloudwatchLogsExportConfiguration`

    The configuration setting for the log types to be enabled for export to CloudWatch Logs for a
    specific DB cluster.

    - **EnableLogTypes** *(list) --*

      The list of log types to enable.

      - *(string) --*

    - **DisableLogTypes** *(list) --*

      The list of log types to disable.

      - *(string) --*
    """


_ClientModifyDbClusterParameterGroupParametersTypeDef = TypedDict(
    "_ClientModifyDbClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientModifyDbClusterParameterGroupParametersTypeDef(
    _ClientModifyDbClusterParameterGroupParametersTypeDef
):
    """
    Type definition for `ClientModifyDbClusterParameterGroup` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientModifyDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientModifyDbClusterParameterGroupResponseTypeDef",
    {"DBClusterParameterGroupName": str},
    total=False,
)


class ClientModifyDbClusterParameterGroupResponseTypeDef(
    _ClientModifyDbClusterParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientModifyDbClusterParameterGroup` `Response`

    - **DBClusterParameterGroupName** *(string) --*

      The name of the DB cluster parameter group.

      Constraints:

      * Must be 1 to 255 letters or numbers.

      * First character must be a letter

      * Cannot end with a hyphen or contain two consecutive hyphens

      .. note::

        This value is stored as a lowercase string.
    """


_ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientModifyDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The Status
      property returns one of the following values:

      * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
      is unable to assume the IAM role in order to access other AWS services on your behalf.
    """


_ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientModifyDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      Value that is ``true`` if the cluster member is the primary instance for the DB cluster
      and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.
    """


_ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientModifyDbClusterResponseDBCluster` `DBClusterOptionGroupMemberships`

    Contains status information for a DB cluster option group.

    - **DBClusterOptionGroupName** *(string) --*

      Specifies the name of the DB cluster option group.

    - **Status** *(string) --*

      Specifies the status of the DB cluster option group.
    """


_ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientModifyDbClusterResponseDBCluster` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientModifyDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientModifyDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientModifyDbClusterResponseDBClusterTypeDef(
    _ClientModifyDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientModifyDbClusterResponse` `DBCluster`

    Contains the details of an Amazon Neptune DB cluster.

    This data type is used as a response element in the  DescribeDBClusters action.

    - **AllocatedStorage** *(integer) --*

       ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
       fixed, but instead automatically adjusts as needed.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
      in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this cluster is associated with.

    - **DatabaseName** *(string) --*

      Contains the name of the initial database of this DB cluster that was provided at create
      time, if one was specified when the DB cluster was created. This same name is returned for
      the life of the DB cluster.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group associated with the DB cluster, including the
      name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      Specifies the earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
      connections across the Read Replicas that are available in a DB cluster. As clients request
      new connections to the reader endpoint, Neptune distributes the connection requests among
      the Read Replicas in the DB cluster. This functionality can help balance your read workload
      across multiple Read Replicas in your DB cluster.

      If a failover occurs, and the Read Replica that you are connected to is promoted to be the
      primary instance, your connection is dropped. To continue sending your read workload to
      other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB cluster.

    - **DBClusterOptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB cluster.

      - *(dict) --*

        Contains status information for a DB cluster option group.

        - **DBClusterOptionGroupName** *(string) --*

          Specifies the name of the DB cluster option group.

        - **Status** *(string) --*

          Specifies the status of the DB cluster option group.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **ReplicationSourceIdentifier** *(string) --*

      Not supported by Neptune.

    - **ReadReplicaIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB cluster.

      - *(string) --*

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          Value that is ``true`` if the cluster member is the primary instance for the DB cluster
          and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security groups that the DB cluster belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The Status
          property returns one of the following values:

          * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
          is unable to assume the IAM role in order to access other AWS services on your behalf.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.

    - **CloneGroupId** *(string) --*

      Identifies the clone group to which the DB cluster is associated.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientModifyDbClusterResponseTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseTypeDef",
    {"DBCluster": ClientModifyDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientModifyDbClusterResponseTypeDef(_ClientModifyDbClusterResponseTypeDef):
    """
    Type definition for `ClientModifyDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.

      This data type is used as a response element in the  DescribeDBClusters action.

      - **AllocatedStorage** *(integer) --*

         ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
         fixed, but instead automatically adjusts as needed.

      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
        in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this cluster is associated with.

      - **DatabaseName** *(string) --*

        Contains the name of the initial database of this DB cluster that was provided at create
        time, if one was specified when the DB cluster was created. This same name is returned for
        the life of the DB cluster.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group associated with the DB cluster, including the
        name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        Specifies the earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
        connections across the Read Replicas that are available in a DB cluster. As clients request
        new connections to the reader endpoint, Neptune distributes the connection requests among
        the Read Replicas in the DB cluster. This functionality can help balance your read workload
        across multiple Read Replicas in your DB cluster.

        If a failover occurs, and the Read Replica that you are connected to is promoted to be the
        primary instance, your connection is dropped. To continue sending your read workload to
        other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB cluster.

      - **DBClusterOptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB cluster.

        - *(dict) --*

          Contains status information for a DB cluster option group.

          - **DBClusterOptionGroupName** *(string) --*

            Specifies the name of the DB cluster option group.

          - **Status** *(string) --*

            Specifies the status of the DB cluster option group.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **ReplicationSourceIdentifier** *(string) --*

        Not supported by Neptune.

      - **ReadReplicaIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB cluster.

        - *(string) --*

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            Value that is ``true`` if the cluster member is the primary instance for the DB cluster
            and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which a Read Replica is promoted to the primary
            instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security groups that the DB cluster belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The Status
            property returns one of the following values:

            * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
            is unable to assume the IAM role in order to access other AWS services on your behalf.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
        is enabled, and otherwise false.

      - **CloneGroupId** *(string) --*

        Identifies the clone group to which the DB cluster is associated.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef = TypedDict(
    "_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)


class ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef(
    _ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
):
    """
    Type definition for `ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResult` `DBClusterSnapshotAttributes`

    Contains the name and values of a manual DB cluster snapshot attribute.

    Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
    a manual DB cluster snapshot. For more information, see the
    ModifyDBClusterSnapshotAttribute API action.

    - **AttributeName** *(string) --*

      The name of the manual DB cluster snapshot attribute.

      The attribute named ``restore`` refers to the list of AWS accounts that have permission
      to copy or restore the manual DB cluster snapshot. For more information, see the
      ModifyDBClusterSnapshotAttribute API action.

    - **AttributeValues** *(list) --*

      The value(s) for the manual DB cluster snapshot attribute.

      If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
      of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
      snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
      public and available for any AWS account to copy or restore.

      - *(string) --*
    """


_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List[
            ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
        ],
    },
    total=False,
)


class ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef(
    _ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef
):
    """
    Type definition for `ClientModifyDbClusterSnapshotAttributeResponse` `DBClusterSnapshotAttributesResult`

    Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API
    action.

    Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
    restore a manual DB cluster snapshot. For more information, see the
    ModifyDBClusterSnapshotAttribute API action.

    - **DBClusterSnapshotIdentifier** *(string) --*

      The identifier of the manual DB cluster snapshot that the attributes apply to.

    - **DBClusterSnapshotAttributes** *(list) --*

      The list of attributes and values for the manual DB cluster snapshot.

      - *(dict) --*

        Contains the name and values of a manual DB cluster snapshot attribute.

        Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
        a manual DB cluster snapshot. For more information, see the
        ModifyDBClusterSnapshotAttribute API action.

        - **AttributeName** *(string) --*

          The name of the manual DB cluster snapshot attribute.

          The attribute named ``restore`` refers to the list of AWS accounts that have permission
          to copy or restore the manual DB cluster snapshot. For more information, see the
          ModifyDBClusterSnapshotAttribute API action.

        - **AttributeValues** *(list) --*

          The value(s) for the manual DB cluster snapshot attribute.

          If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
          of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
          snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
          public and available for any AWS account to copy or restore.

          - *(string) --*
    """


_ClientModifyDbClusterSnapshotAttributeResponseTypeDef = TypedDict(
    "_ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    {
        "DBClusterSnapshotAttributesResult": ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef
    },
    total=False,
)


class ClientModifyDbClusterSnapshotAttributeResponseTypeDef(
    _ClientModifyDbClusterSnapshotAttributeResponseTypeDef
):
    """
    Type definition for `ClientModifyDbClusterSnapshotAttribute` `Response`

    - **DBClusterSnapshotAttributesResult** *(dict) --*

      Contains the results of a successful call to the  DescribeDBClusterSnapshotAttributes API
      action.

      Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or
      restore a manual DB cluster snapshot. For more information, see the
      ModifyDBClusterSnapshotAttribute API action.

      - **DBClusterSnapshotIdentifier** *(string) --*

        The identifier of the manual DB cluster snapshot that the attributes apply to.

      - **DBClusterSnapshotAttributes** *(list) --*

        The list of attributes and values for the manual DB cluster snapshot.

        - *(dict) --*

          Contains the name and values of a manual DB cluster snapshot attribute.

          Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
          a manual DB cluster snapshot. For more information, see the
          ModifyDBClusterSnapshotAttribute API action.

          - **AttributeName** *(string) --*

            The name of the manual DB cluster snapshot attribute.

            The attribute named ``restore`` refers to the list of AWS accounts that have permission
            to copy or restore the manual DB cluster snapshot. For more information, see the
            ModifyDBClusterSnapshotAttribute API action.

          - **AttributeValues** *(list) --*

            The value(s) for the manual DB cluster snapshot attribute.

            If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
            of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
            snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
            public and available for any AWS account to copy or restore.

            - *(string) --*
    """


_ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "_ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef",
    {"EnableLogTypes": List[str], "DisableLogTypes": List[str]},
    total=False,
)


class ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef(
    _ClientModifyDbInstanceCloudwatchLogsExportConfigurationTypeDef
):
    """
    Type definition for `ClientModifyDbInstance` `CloudwatchLogsExportConfiguration`

    The configuration setting for the log types to be enabled for export to CloudWatch Logs for a
    specific DB instance or DB cluster.

    - **EnableLogTypes** *(list) --*

      The list of log types to enable.

      - *(string) --*

    - **DisableLogTypes** *(list) --*

      The list of log types to disable.

      - *(string) --*
    """


_ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `DBParameterGroups`

    The status of the DB parameter group.

    This data type is used as a response element in the following actions:

    *  CreateDBInstance

    *  DeleteDBInstance

    *  ModifyDBInstance

    *  RebootDBInstance

    - **DBParameterGroupName** *(string) --*

      The name of the DP parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.
    """


_ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `DBSecurityGroups`

    Specifies membership in a designated DB security group.

    - **DBSecurityGroupName** *(string) --*

      The name of the DB security group.

    - **Status** *(string) --*

      The status of the DB security group.
    """


_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the EC2 Availability Zone that the subnet is in.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstanceDBSubnetGroup` `Subnets`

    Specifies a subnet.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the EC2 Availability Zone that the subnet is in.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `DBSubnetGroup`

    Specifies information on the subnet group associated with the DB instance, including the
    name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the VpcId of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Contains a list of  Subnet elements.

      - *(dict) --*

        Specifies a subnet.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the EC2 Availability Zone that the subnet is in.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `DomainMemberships`

    An Active Directory Domain membership record associated with a DB instance.

    - **Domain** *(string) --*

      The identifier of the Active Directory Domain.

    - **Status** *(string) --*

      The status of the DB instance's Active Directory Domain membership, such as joined,
      pending-join, failed etc).

    - **FQDN** *(string) --*

      The fully qualified domain name of the Active Directory Domain.

    - **IAMRoleName** *(string) --*

      The name of the IAM role to be used when making API calls to the Directory Service.
    """


_ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `OptionGroupMemberships`

    Provides information on the option groups the DB instance is a member of.

    - **OptionGroupName** *(string) --*

      The name of the option group that the instance belongs to.

    - **Status** *(string) --*

      The status of the DB instance's option group membership. Valid values are: ``in-sync``
      , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
      ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .
    """


_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstancePendingModifiedValues` `PendingCloudwatchLogsExports`

    Specifies the CloudWatch logs to be exported.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to CloudWatch Logs.

      - *(string) --*
    """


_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is only included when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
      currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently-in-progress change of the master credentials for the DB
      instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` | ``bring-your-own-license`` |
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
      currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the CA certificate for the DB instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      Specifies the CloudWatch logs to be exported.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to CloudWatch Logs.

        - *(string) --*
    """


_ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "read replication."

    - **Normal** *(boolean) --*

      Boolean value that is true if the instance is operating normally, or false if the
      instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a StatusType of read replica, the values can be
      replicating, error, stopped, or terminated.

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientModifyDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientModifyDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientModifyDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientModifyDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientModifyDbInstanceResponseDBInstanceDomainMembershipsTypeDef
        ],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponse` `DBInstance`

    Contains the details of an Amazon Neptune DB instance.

    This data type is used as a response element in the  DescribeDBInstances action.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-supplied database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB instance.

    - **DBName** *(string) --*

      The database name.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size specified in gibibytes.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBSecurityGroups** *(list) --*

      Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
      ``DBSecurityGroup.Status`` subelements.

      - *(dict) --*

        Specifies membership in a designated DB security group.

        - **DBSecurityGroupName** *(string) --*

          The name of the DB security group.

        - **Status** *(string) --*

          The status of the DB security group.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **DBParameterGroups** *(list) --*

      Provides the list of DB parameter groups applied to this DB instance.

      - *(dict) --*

        The status of the DB parameter group.

        This data type is used as a response element in the following actions:

        *  CreateDBInstance

        *  DeleteDBInstance

        *  ModifyDBInstance

        *  RebootDBInstance

        - **DBParameterGroupName** *(string) --*

          The name of the DP parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group associated with the DB instance, including the
      name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the VpcId of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Contains a list of  Subnet elements.

        - *(dict) --*

          Specifies a subnet.

          This data type is used as a response element in the  DescribeDBSubnetGroups action.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the EC2 Availability Zone that the subnet is in.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is only included when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
        currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently-in-progress change of the master credentials for the DB
        instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` | ``bring-your-own-license`` |
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
        currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the CA certificate for the DB instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        Specifies the CloudWatch logs to be exported.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **MultiAZ** *(boolean) --*

      Specifies if the DB instance is a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

      Contains the identifier of the source DB instance if this DB instance is a Read Replica.

    - **ReadReplicaDBInstanceIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB instance.

      - *(string) --*

    - **ReadReplicaDBClusterIdentifiers** *(list) --*

      Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

      - *(string) --*

    - **LicenseModel** *(string) --*

      License model information for this DB instance.

    - **Iops** *(integer) --*

      Specifies the Provisioned IOPS (I/O operations per second) value.

    - **OptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB instance.

      - *(dict) --*

        Provides information on the option groups the DB instance is a member of.

        - **OptionGroupName** *(string) --*

          The name of the option group that the instance belongs to.

        - **Status** *(string) --*

          The status of the DB instance's option group membership. Valid values are: ``in-sync``
          , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
          ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this instance is associated with.

    - **SecondaryAvailabilityZone** *(string) --*

      If present, specifies the name of the secondary Availability Zone for a DB instance with
      multi-AZ support.

    - **PubliclyAccessible** *(boolean) --*

      This flag should no longer be used.

    - **StatusInfos** *(list) --*

      The status of a Read Replica. If the instance is not a Read Replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "read replication."

        - **Normal** *(boolean) --*

          Boolean value that is true if the instance is operating normally, or false if the
          instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a StatusType of read replica, the values can be
          replicating, error, stopped, or terminated.

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **StorageType** *(string) --*

      Specifies the storage type associated with DB instance.

    - **TdeCredentialArn** *(string) --*

      The ARN from the key store with which the instance is associated for TDE encryption.

    - **DbInstancePort** *(integer) --*

      Specifies the port that the DB instance listens on. If the DB instance is part of a DB
      cluster, this can be a different port than the DB cluster port.

    - **DBClusterIdentifier** *(string) --*

      If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
      the DB instance is a member of.

    - **StorageEncrypted** *(boolean) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **KmsKeyId** *(string) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **DomainMemberships** *(list) --*

      Not supported

      - *(dict) --*

        An Active Directory Domain membership record associated with a DB instance.

        - **Domain** *(string) --*

          The identifier of the Active Directory Domain.

        - **Status** *(string) --*

          The status of the DB instance's Active Directory Domain membership, such as joined,
          pending-join, failed etc).

        - **FQDN** *(string) --*

          The fully qualified domain name of the Active Directory Domain.

        - **IAMRoleName** *(string) --*

          The name of the IAM role to be used when making API calls to the Directory Service.

    - **CopyTagsToSnapshot** *(boolean) --*

      Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

    - **MonitoringInterval** *(integer) --*

      The interval, in seconds, between points when Enhanced Monitoring metrics are collected for
      the DB instance.

    - **EnhancedMonitoringResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
      Enhanced Monitoring metrics data for the DB instance.

    - **MonitoringRoleArn** *(string) --*

      The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon
      CloudWatch Logs.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **Timezone** *(string) --*

      Not supported.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
      false.

    - **PerformanceInsightsEnabled** *(boolean) --*

      True if Performance Insights is enabled for the DB instance, and otherwise false.

    - **PerformanceInsightsKMSKeyId** *(string) --*

      The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
      the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
      encryption key.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientModifyDbInstanceResponseTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseTypeDef",
    {"DBInstance": ClientModifyDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientModifyDbInstanceResponseTypeDef(_ClientModifyDbInstanceResponseTypeDef):
    """
    Type definition for `ClientModifyDbInstance` `Response`

    - **DBInstance** *(dict) --*

      Contains the details of an Amazon Neptune DB instance.

      This data type is used as a response element in the  DescribeDBInstances action.

      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.

      - **DBInstanceClass** *(string) --*

        Contains the name of the compute and memory capacity class of the DB instance.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB instance.

      - **DBInstanceStatus** *(string) --*

        Specifies the current state of this database.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB instance.

      - **DBName** *(string) --*

        The database name.

      - **Endpoint** *(dict) --*

        Specifies the connection endpoint.

        - **Address** *(string) --*

          Specifies the DNS address of the DB instance.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **AllocatedStorage** *(integer) --*

        Specifies the allocated storage size specified in gibibytes.

      - **InstanceCreateTime** *(datetime) --*

        Provides the date and time the DB instance was created.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBSecurityGroups** *(list) --*

        Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
        ``DBSecurityGroup.Status`` subelements.

        - *(dict) --*

          Specifies membership in a designated DB security group.

          - **DBSecurityGroupName** *(string) --*

            The name of the DB security group.

          - **Status** *(string) --*

            The status of the DB security group.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security group elements that the DB instance belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **DBParameterGroups** *(list) --*

        Provides the list of DB parameter groups applied to this DB instance.

        - *(dict) --*

          The status of the DB parameter group.

          This data type is used as a response element in the following actions:

          *  CreateDBInstance

          *  DeleteDBInstance

          *  ModifyDBInstance

          *  RebootDBInstance

          - **DBParameterGroupName** *(string) --*

            The name of the DP parameter group.

          - **ParameterApplyStatus** *(string) --*

            The status of parameter updates.

      - **AvailabilityZone** *(string) --*

        Specifies the name of the Availability Zone the DB instance is located in.

      - **DBSubnetGroup** *(dict) --*

        Specifies information on the subnet group associated with the DB instance, including the
        name, description, and subnets in the subnet group.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the VpcId of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Contains a list of  Subnet elements.

          - *(dict) --*

            Specifies a subnet.

            This data type is used as a response element in the  DescribeDBSubnetGroups action.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the EC2 Availability Zone that the subnet is in.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **PendingModifiedValues** *(dict) --*

        Specifies that changes to the DB instance are pending. This element is only included when
        changes are pending. Specific changes are identified by subelements.

        - **DBInstanceClass** *(string) --*

          Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
          currently being applied.

        - **AllocatedStorage** *(integer) --*

          Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
          currently being applied.

        - **MasterUserPassword** *(string) --*

          Contains the pending or currently-in-progress change of the master credentials for the DB
          instance.

        - **Port** *(integer) --*

          Specifies the pending port for the DB instance.

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the pending number of days for which automated backups are retained.

        - **MultiAZ** *(boolean) --*

          Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LicenseModel** *(string) --*

          The license model for the DB instance.

          Valid values: ``license-included`` | ``bring-your-own-license`` |
          ``general-public-license``

        - **Iops** *(integer) --*

          Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
          currently being applied.

        - **DBInstanceIdentifier** *(string) --*

          Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
          currently being applied.

        - **StorageType** *(string) --*

          Specifies the storage type to be associated with the DB instance.

        - **CACertificateIdentifier** *(string) --*

          Specifies the identifier of the CA certificate for the DB instance.

        - **DBSubnetGroupName** *(string) --*

          The new DB subnet group for the DB instance.

        - **PendingCloudwatchLogsExports** *(dict) --*

          Specifies the CloudWatch logs to be exported.

          - **LogTypesToEnable** *(list) --*

            Log types that are in the process of being deactivated. After they are deactivated,
            these log types aren't exported to CloudWatch Logs.

            - *(string) --*

          - **LogTypesToDisable** *(list) --*

            Log types that are in the process of being enabled. After they are enabled, these log
            types are exported to CloudWatch Logs.

            - *(string) --*

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **MultiAZ** *(boolean) --*

        Specifies if the DB instance is a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Indicates that minor version patches are applied automatically.

      - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

        Contains the identifier of the source DB instance if this DB instance is a Read Replica.

      - **ReadReplicaDBInstanceIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB instance.

        - *(string) --*

      - **ReadReplicaDBClusterIdentifiers** *(list) --*

        Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

        - *(string) --*

      - **LicenseModel** *(string) --*

        License model information for this DB instance.

      - **Iops** *(integer) --*

        Specifies the Provisioned IOPS (I/O operations per second) value.

      - **OptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB instance.

        - *(dict) --*

          Provides information on the option groups the DB instance is a member of.

          - **OptionGroupName** *(string) --*

            The name of the option group that the instance belongs to.

          - **Status** *(string) --*

            The status of the DB instance's option group membership. Valid values are: ``in-sync``
            , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
            ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this instance is associated with.

      - **SecondaryAvailabilityZone** *(string) --*

        If present, specifies the name of the secondary Availability Zone for a DB instance with
        multi-AZ support.

      - **PubliclyAccessible** *(boolean) --*

        This flag should no longer be used.

      - **StatusInfos** *(list) --*

        The status of a Read Replica. If the instance is not a Read Replica, this is blank.

        - *(dict) --*

          Provides a list of status information for a DB instance.

          - **StatusType** *(string) --*

            This value is currently "read replication."

          - **Normal** *(boolean) --*

            Boolean value that is true if the instance is operating normally, or false if the
            instance is in an error state.

          - **Status** *(string) --*

            Status of the DB instance. For a StatusType of read replica, the values can be
            replicating, error, stopped, or terminated.

          - **Message** *(string) --*

            Details of the error if there is an error for the instance. If the instance is not in
            an error state, this value is blank.

      - **StorageType** *(string) --*

        Specifies the storage type associated with DB instance.

      - **TdeCredentialArn** *(string) --*

        The ARN from the key store with which the instance is associated for TDE encryption.

      - **DbInstancePort** *(integer) --*

        Specifies the port that the DB instance listens on. If the DB instance is part of a DB
        cluster, this can be a different port than the DB cluster port.

      - **DBClusterIdentifier** *(string) --*

        If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
        the DB instance is a member of.

      - **StorageEncrypted** *(boolean) --*

        Not supported: The encryption for DB instances is managed by the DB cluster.

      - **KmsKeyId** *(string) --*

        Not supported: The encryption for DB instances is managed by the DB cluster.

      - **DbiResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
        in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

      - **CACertificateIdentifier** *(string) --*

        The identifier of the CA certificate for this DB instance.

      - **DomainMemberships** *(list) --*

        Not supported

        - *(dict) --*

          An Active Directory Domain membership record associated with a DB instance.

          - **Domain** *(string) --*

            The identifier of the Active Directory Domain.

          - **Status** *(string) --*

            The status of the DB instance's Active Directory Domain membership, such as joined,
            pending-join, failed etc).

          - **FQDN** *(string) --*

            The fully qualified domain name of the Active Directory Domain.

          - **IAMRoleName** *(string) --*

            The name of the IAM role to be used when making API calls to the Directory Service.

      - **CopyTagsToSnapshot** *(boolean) --*

        Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

      - **MonitoringInterval** *(integer) --*

        The interval, in seconds, between points when Enhanced Monitoring metrics are collected for
        the DB instance.

      - **EnhancedMonitoringResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
        Enhanced Monitoring metrics data for the DB instance.

      - **MonitoringRoleArn** *(string) --*

        The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon
        CloudWatch Logs.

      - **PromotionTier** *(integer) --*

        A value that specifies the order in which a Read Replica is promoted to the primary
        instance after a failure of the existing primary instance.

      - **DBInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB instance.

      - **Timezone** *(string) --*

        Not supported.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
        false.

      - **PerformanceInsightsEnabled** *(boolean) --*

        True if Performance Insights is enabled for the DB instance, and otherwise false.

      - **PerformanceInsightsKMSKeyId** *(string) --*

        The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
        the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
        encryption key.

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB instance is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientModifyDbParameterGroupParametersTypeDef = TypedDict(
    "_ClientModifyDbParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientModifyDbParameterGroupParametersTypeDef(
    _ClientModifyDbParameterGroupParametersTypeDef
):
    """
    Type definition for `ClientModifyDbParameterGroup` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientModifyDbParameterGroupResponseTypeDef = TypedDict(
    "_ClientModifyDbParameterGroupResponseTypeDef",
    {"DBParameterGroupName": str},
    total=False,
)


class ClientModifyDbParameterGroupResponseTypeDef(
    _ClientModifyDbParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientModifyDbParameterGroup` `Response`

    - **DBParameterGroupName** *(string) --*

      Provides the name of the DB parameter group.
    """


_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the EC2 Availability Zone that the subnet is in.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef(
    _ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientModifyDbSubnetGroupResponseDBSubnetGroup` `Subnets`

    Specifies a subnet.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the EC2 Availability Zone that the subnet is in.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef(
    _ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientModifyDbSubnetGroupResponse` `DBSubnetGroup`

    Contains the details of an Amazon Neptune DB subnet group.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the VpcId of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Contains a list of  Subnet elements.

      - *(dict) --*

        Specifies a subnet.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the EC2 Availability Zone that the subnet is in.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientModifyDbSubnetGroupResponseTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseTypeDef",
    {"DBSubnetGroup": ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef},
    total=False,
)


class ClientModifyDbSubnetGroupResponseTypeDef(
    _ClientModifyDbSubnetGroupResponseTypeDef
):
    """
    Type definition for `ClientModifyDbSubnetGroup` `Response`

    - **DBSubnetGroup** *(dict) --*

      Contains the details of an Amazon Neptune DB subnet group.

      This data type is used as a response element in the  DescribeDBSubnetGroups action.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the VpcId of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Contains a list of  Subnet elements.

        - *(dict) --*

          Specifies a subnet.

          This data type is used as a response element in the  DescribeDBSubnetGroups action.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the EC2 Availability Zone that the subnet is in.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef(
    _ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef
):
    """
    Type definition for `ClientModifyEventSubscriptionResponse` `EventSubscription`

    Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the event notification subscription.

    - **Status** *(string) --*

      The status of the event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that Neptune no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the event notification subscription was created.

    - **SourceType** *(string) --*

      The source type for the event notification subscription.

    - **SourceIdsList** *(list) --*

      A list of source IDs for the event notification subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A list of event categories for the event notification subscription.

      - *(string) --*

    - **Enabled** *(boolean) --*

      A Boolean value indicating if the subscription is enabled. True indicates the subscription
      is enabled.

    - **EventSubscriptionArn** *(string) --*

      The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientModifyEventSubscriptionResponseTypeDef = TypedDict(
    "_ClientModifyEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef
    },
    total=False,
)


class ClientModifyEventSubscriptionResponseTypeDef(
    _ClientModifyEventSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientModifyEventSubscription` `Response`

    - **EventSubscription** *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.

      - **CustSubscriptionId** *(string) --*

        The event notification subscription Id.

      - **SnsTopicArn** *(string) --*

        The topic ARN of the event notification subscription.

      - **Status** *(string) --*

        The status of the event notification subscription.

        Constraints:

        Can be one of the following: creating | modifying | deleting | active | no-permission |
        topic-not-exist

        The status "no-permission" indicates that Neptune no longer has permission to post to the
        SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
        subscription was created.

      - **SubscriptionCreationTime** *(string) --*

        The time the event notification subscription was created.

      - **SourceType** *(string) --*

        The source type for the event notification subscription.

      - **SourceIdsList** *(list) --*

        A list of source IDs for the event notification subscription.

        - *(string) --*

      - **EventCategoriesList** *(list) --*

        A list of event categories for the event notification subscription.

        - *(string) --*

      - **Enabled** *(boolean) --*

        A Boolean value indicating if the subscription is enabled. True indicates the subscription
        is enabled.

      - **EventSubscriptionArn** *(string) --*

        The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientPromoteReadReplicaDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The Status
      property returns one of the following values:

      * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
      is unable to assume the IAM role in order to access other AWS services on your behalf.
    """


_ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientPromoteReadReplicaDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      Value that is ``true`` if the cluster member is the primary instance for the DB cluster
      and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.
    """


_ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientPromoteReadReplicaDbClusterResponseDBCluster` `DBClusterOptionGroupMemberships`

    Contains status information for a DB cluster option group.

    - **DBClusterOptionGroupName** *(string) --*

      Specifies the name of the DB cluster option group.

    - **Status** *(string) --*

      Specifies the status of the DB cluster option group.
    """


_ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientPromoteReadReplicaDbClusterResponseDBCluster` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientPromoteReadReplicaDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientPromoteReadReplicaDbClusterResponse` `DBCluster`

    Contains the details of an Amazon Neptune DB cluster.

    This data type is used as a response element in the  DescribeDBClusters action.

    - **AllocatedStorage** *(integer) --*

       ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
       fixed, but instead automatically adjusts as needed.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
      in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this cluster is associated with.

    - **DatabaseName** *(string) --*

      Contains the name of the initial database of this DB cluster that was provided at create
      time, if one was specified when the DB cluster was created. This same name is returned for
      the life of the DB cluster.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group associated with the DB cluster, including the
      name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      Specifies the earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
      connections across the Read Replicas that are available in a DB cluster. As clients request
      new connections to the reader endpoint, Neptune distributes the connection requests among
      the Read Replicas in the DB cluster. This functionality can help balance your read workload
      across multiple Read Replicas in your DB cluster.

      If a failover occurs, and the Read Replica that you are connected to is promoted to be the
      primary instance, your connection is dropped. To continue sending your read workload to
      other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB cluster.

    - **DBClusterOptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB cluster.

      - *(dict) --*

        Contains status information for a DB cluster option group.

        - **DBClusterOptionGroupName** *(string) --*

          Specifies the name of the DB cluster option group.

        - **Status** *(string) --*

          Specifies the status of the DB cluster option group.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **ReplicationSourceIdentifier** *(string) --*

      Not supported by Neptune.

    - **ReadReplicaIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB cluster.

      - *(string) --*

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          Value that is ``true`` if the cluster member is the primary instance for the DB cluster
          and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security groups that the DB cluster belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The Status
          property returns one of the following values:

          * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
          is unable to assume the IAM role in order to access other AWS services on your behalf.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.

    - **CloneGroupId** *(string) --*

      Identifies the clone group to which the DB cluster is associated.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientPromoteReadReplicaDbClusterResponseTypeDef = TypedDict(
    "_ClientPromoteReadReplicaDbClusterResponseTypeDef",
    {"DBCluster": ClientPromoteReadReplicaDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientPromoteReadReplicaDbClusterResponseTypeDef(
    _ClientPromoteReadReplicaDbClusterResponseTypeDef
):
    """
    Type definition for `ClientPromoteReadReplicaDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.

      This data type is used as a response element in the  DescribeDBClusters action.

      - **AllocatedStorage** *(integer) --*

         ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
         fixed, but instead automatically adjusts as needed.

      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
        in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this cluster is associated with.

      - **DatabaseName** *(string) --*

        Contains the name of the initial database of this DB cluster that was provided at create
        time, if one was specified when the DB cluster was created. This same name is returned for
        the life of the DB cluster.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group associated with the DB cluster, including the
        name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        Specifies the earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
        connections across the Read Replicas that are available in a DB cluster. As clients request
        new connections to the reader endpoint, Neptune distributes the connection requests among
        the Read Replicas in the DB cluster. This functionality can help balance your read workload
        across multiple Read Replicas in your DB cluster.

        If a failover occurs, and the Read Replica that you are connected to is promoted to be the
        primary instance, your connection is dropped. To continue sending your read workload to
        other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB cluster.

      - **DBClusterOptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB cluster.

        - *(dict) --*

          Contains status information for a DB cluster option group.

          - **DBClusterOptionGroupName** *(string) --*

            Specifies the name of the DB cluster option group.

          - **Status** *(string) --*

            Specifies the status of the DB cluster option group.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **ReplicationSourceIdentifier** *(string) --*

        Not supported by Neptune.

      - **ReadReplicaIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB cluster.

        - *(string) --*

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            Value that is ``true`` if the cluster member is the primary instance for the DB cluster
            and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which a Read Replica is promoted to the primary
            instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security groups that the DB cluster belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The Status
            property returns one of the following values:

            * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
            is unable to assume the IAM role in order to access other AWS services on your behalf.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
        is enabled, and otherwise false.

      - **CloneGroupId** *(string) --*

        Identifies the clone group to which the DB cluster is associated.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `DBParameterGroups`

    The status of the DB parameter group.

    This data type is used as a response element in the following actions:

    *  CreateDBInstance

    *  DeleteDBInstance

    *  ModifyDBInstance

    *  RebootDBInstance

    - **DBParameterGroupName** *(string) --*

      The name of the DP parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.
    """


_ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `DBSecurityGroups`

    Specifies membership in a designated DB security group.

    - **DBSecurityGroupName** *(string) --*

      The name of the DB security group.

    - **Status** *(string) --*

      The status of the DB security group.
    """


_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the EC2 Availability Zone that the subnet is in.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstanceDBSubnetGroup` `Subnets`

    Specifies a subnet.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the EC2 Availability Zone that the subnet is in.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `DBSubnetGroup`

    Specifies information on the subnet group associated with the DB instance, including the
    name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the VpcId of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Contains a list of  Subnet elements.

      - *(dict) --*

        Specifies a subnet.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the EC2 Availability Zone that the subnet is in.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `DomainMemberships`

    An Active Directory Domain membership record associated with a DB instance.

    - **Domain** *(string) --*

      The identifier of the Active Directory Domain.

    - **Status** *(string) --*

      The status of the DB instance's Active Directory Domain membership, such as joined,
      pending-join, failed etc).

    - **FQDN** *(string) --*

      The fully qualified domain name of the Active Directory Domain.

    - **IAMRoleName** *(string) --*

      The name of the IAM role to be used when making API calls to the Directory Service.
    """


_ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `OptionGroupMemberships`

    Provides information on the option groups the DB instance is a member of.

    - **OptionGroupName** *(string) --*

      The name of the option group that the instance belongs to.

    - **Status** *(string) --*

      The status of the DB instance's option group membership. Valid values are: ``in-sync``
      , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
      ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .
    """


_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstancePendingModifiedValues` `PendingCloudwatchLogsExports`

    Specifies the CloudWatch logs to be exported.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to CloudWatch Logs.

      - *(string) --*
    """


_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is only included when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
      currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently-in-progress change of the master credentials for the DB
      instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` | ``bring-your-own-license`` |
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
      currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the CA certificate for the DB instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      Specifies the CloudWatch logs to be exported.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to CloudWatch Logs.

        - *(string) --*
    """


_ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "read replication."

    - **Normal** *(boolean) --*

      Boolean value that is true if the instance is operating normally, or false if the
      instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a StatusType of read replica, the values can be
      replicating, error, stopped, or terminated.

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientRebootDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            ClientRebootDbInstanceResponseDBInstanceDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            ClientRebootDbInstanceResponseDBInstanceDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            ClientRebootDbInstanceResponseDBInstanceOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            ClientRebootDbInstanceResponseDBInstanceDomainMembershipsTypeDef
        ],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponse` `DBInstance`

    Contains the details of an Amazon Neptune DB instance.

    This data type is used as a response element in the  DescribeDBInstances action.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-supplied database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB instance.

    - **DBName** *(string) --*

      The database name.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size specified in gibibytes.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBSecurityGroups** *(list) --*

      Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
      ``DBSecurityGroup.Status`` subelements.

      - *(dict) --*

        Specifies membership in a designated DB security group.

        - **DBSecurityGroupName** *(string) --*

          The name of the DB security group.

        - **Status** *(string) --*

          The status of the DB security group.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **DBParameterGroups** *(list) --*

      Provides the list of DB parameter groups applied to this DB instance.

      - *(dict) --*

        The status of the DB parameter group.

        This data type is used as a response element in the following actions:

        *  CreateDBInstance

        *  DeleteDBInstance

        *  ModifyDBInstance

        *  RebootDBInstance

        - **DBParameterGroupName** *(string) --*

          The name of the DP parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group associated with the DB instance, including the
      name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the VpcId of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Contains a list of  Subnet elements.

        - *(dict) --*

          Specifies a subnet.

          This data type is used as a response element in the  DescribeDBSubnetGroups action.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the EC2 Availability Zone that the subnet is in.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is only included when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
        currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently-in-progress change of the master credentials for the DB
        instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` | ``bring-your-own-license`` |
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
        currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the CA certificate for the DB instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        Specifies the CloudWatch logs to be exported.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **MultiAZ** *(boolean) --*

      Specifies if the DB instance is a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

      Contains the identifier of the source DB instance if this DB instance is a Read Replica.

    - **ReadReplicaDBInstanceIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB instance.

      - *(string) --*

    - **ReadReplicaDBClusterIdentifiers** *(list) --*

      Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

      - *(string) --*

    - **LicenseModel** *(string) --*

      License model information for this DB instance.

    - **Iops** *(integer) --*

      Specifies the Provisioned IOPS (I/O operations per second) value.

    - **OptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB instance.

      - *(dict) --*

        Provides information on the option groups the DB instance is a member of.

        - **OptionGroupName** *(string) --*

          The name of the option group that the instance belongs to.

        - **Status** *(string) --*

          The status of the DB instance's option group membership. Valid values are: ``in-sync``
          , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
          ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this instance is associated with.

    - **SecondaryAvailabilityZone** *(string) --*

      If present, specifies the name of the secondary Availability Zone for a DB instance with
      multi-AZ support.

    - **PubliclyAccessible** *(boolean) --*

      This flag should no longer be used.

    - **StatusInfos** *(list) --*

      The status of a Read Replica. If the instance is not a Read Replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "read replication."

        - **Normal** *(boolean) --*

          Boolean value that is true if the instance is operating normally, or false if the
          instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a StatusType of read replica, the values can be
          replicating, error, stopped, or terminated.

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **StorageType** *(string) --*

      Specifies the storage type associated with DB instance.

    - **TdeCredentialArn** *(string) --*

      The ARN from the key store with which the instance is associated for TDE encryption.

    - **DbInstancePort** *(integer) --*

      Specifies the port that the DB instance listens on. If the DB instance is part of a DB
      cluster, this can be a different port than the DB cluster port.

    - **DBClusterIdentifier** *(string) --*

      If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
      the DB instance is a member of.

    - **StorageEncrypted** *(boolean) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **KmsKeyId** *(string) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **DomainMemberships** *(list) --*

      Not supported

      - *(dict) --*

        An Active Directory Domain membership record associated with a DB instance.

        - **Domain** *(string) --*

          The identifier of the Active Directory Domain.

        - **Status** *(string) --*

          The status of the DB instance's Active Directory Domain membership, such as joined,
          pending-join, failed etc).

        - **FQDN** *(string) --*

          The fully qualified domain name of the Active Directory Domain.

        - **IAMRoleName** *(string) --*

          The name of the IAM role to be used when making API calls to the Directory Service.

    - **CopyTagsToSnapshot** *(boolean) --*

      Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

    - **MonitoringInterval** *(integer) --*

      The interval, in seconds, between points when Enhanced Monitoring metrics are collected for
      the DB instance.

    - **EnhancedMonitoringResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
      Enhanced Monitoring metrics data for the DB instance.

    - **MonitoringRoleArn** *(string) --*

      The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon
      CloudWatch Logs.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **Timezone** *(string) --*

      Not supported.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
      false.

    - **PerformanceInsightsEnabled** *(boolean) --*

      True if Performance Insights is enabled for the DB instance, and otherwise false.

    - **PerformanceInsightsKMSKeyId** *(string) --*

      The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
      the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
      encryption key.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientRebootDbInstanceResponseTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseTypeDef",
    {"DBInstance": ClientRebootDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientRebootDbInstanceResponseTypeDef(_ClientRebootDbInstanceResponseTypeDef):
    """
    Type definition for `ClientRebootDbInstance` `Response`

    - **DBInstance** *(dict) --*

      Contains the details of an Amazon Neptune DB instance.

      This data type is used as a response element in the  DescribeDBInstances action.

      - **DBInstanceIdentifier** *(string) --*

        Contains a user-supplied database identifier. This identifier is the unique key that
        identifies a DB instance.

      - **DBInstanceClass** *(string) --*

        Contains the name of the compute and memory capacity class of the DB instance.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB instance.

      - **DBInstanceStatus** *(string) --*

        Specifies the current state of this database.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB instance.

      - **DBName** *(string) --*

        The database name.

      - **Endpoint** *(dict) --*

        Specifies the connection endpoint.

        - **Address** *(string) --*

          Specifies the DNS address of the DB instance.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **AllocatedStorage** *(integer) --*

        Specifies the allocated storage size specified in gibibytes.

      - **InstanceCreateTime** *(datetime) --*

        Provides the date and time the DB instance was created.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBSecurityGroups** *(list) --*

        Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
        ``DBSecurityGroup.Status`` subelements.

        - *(dict) --*

          Specifies membership in a designated DB security group.

          - **DBSecurityGroupName** *(string) --*

            The name of the DB security group.

          - **Status** *(string) --*

            The status of the DB security group.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security group elements that the DB instance belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **DBParameterGroups** *(list) --*

        Provides the list of DB parameter groups applied to this DB instance.

        - *(dict) --*

          The status of the DB parameter group.

          This data type is used as a response element in the following actions:

          *  CreateDBInstance

          *  DeleteDBInstance

          *  ModifyDBInstance

          *  RebootDBInstance

          - **DBParameterGroupName** *(string) --*

            The name of the DP parameter group.

          - **ParameterApplyStatus** *(string) --*

            The status of parameter updates.

      - **AvailabilityZone** *(string) --*

        Specifies the name of the Availability Zone the DB instance is located in.

      - **DBSubnetGroup** *(dict) --*

        Specifies information on the subnet group associated with the DB instance, including the
        name, description, and subnets in the subnet group.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the VpcId of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Contains a list of  Subnet elements.

          - *(dict) --*

            Specifies a subnet.

            This data type is used as a response element in the  DescribeDBSubnetGroups action.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the EC2 Availability Zone that the subnet is in.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **PendingModifiedValues** *(dict) --*

        Specifies that changes to the DB instance are pending. This element is only included when
        changes are pending. Specific changes are identified by subelements.

        - **DBInstanceClass** *(string) --*

          Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
          currently being applied.

        - **AllocatedStorage** *(integer) --*

          Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
          currently being applied.

        - **MasterUserPassword** *(string) --*

          Contains the pending or currently-in-progress change of the master credentials for the DB
          instance.

        - **Port** *(integer) --*

          Specifies the pending port for the DB instance.

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the pending number of days for which automated backups are retained.

        - **MultiAZ** *(boolean) --*

          Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LicenseModel** *(string) --*

          The license model for the DB instance.

          Valid values: ``license-included`` | ``bring-your-own-license`` |
          ``general-public-license``

        - **Iops** *(integer) --*

          Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
          currently being applied.

        - **DBInstanceIdentifier** *(string) --*

          Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
          currently being applied.

        - **StorageType** *(string) --*

          Specifies the storage type to be associated with the DB instance.

        - **CACertificateIdentifier** *(string) --*

          Specifies the identifier of the CA certificate for the DB instance.

        - **DBSubnetGroupName** *(string) --*

          The new DB subnet group for the DB instance.

        - **PendingCloudwatchLogsExports** *(dict) --*

          Specifies the CloudWatch logs to be exported.

          - **LogTypesToEnable** *(list) --*

            Log types that are in the process of being deactivated. After they are deactivated,
            these log types aren't exported to CloudWatch Logs.

            - *(string) --*

          - **LogTypesToDisable** *(list) --*

            Log types that are in the process of being enabled. After they are enabled, these log
            types are exported to CloudWatch Logs.

            - *(string) --*

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **MultiAZ** *(boolean) --*

        Specifies if the DB instance is a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Indicates that minor version patches are applied automatically.

      - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

        Contains the identifier of the source DB instance if this DB instance is a Read Replica.

      - **ReadReplicaDBInstanceIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB instance.

        - *(string) --*

      - **ReadReplicaDBClusterIdentifiers** *(list) --*

        Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.

        - *(string) --*

      - **LicenseModel** *(string) --*

        License model information for this DB instance.

      - **Iops** *(integer) --*

        Specifies the Provisioned IOPS (I/O operations per second) value.

      - **OptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB instance.

        - *(dict) --*

          Provides information on the option groups the DB instance is a member of.

          - **OptionGroupName** *(string) --*

            The name of the option group that the instance belongs to.

          - **Status** *(string) --*

            The status of the DB instance's option group membership. Valid values are: ``in-sync``
            , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply`` ,
            ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this instance is associated with.

      - **SecondaryAvailabilityZone** *(string) --*

        If present, specifies the name of the secondary Availability Zone for a DB instance with
        multi-AZ support.

      - **PubliclyAccessible** *(boolean) --*

        This flag should no longer be used.

      - **StatusInfos** *(list) --*

        The status of a Read Replica. If the instance is not a Read Replica, this is blank.

        - *(dict) --*

          Provides a list of status information for a DB instance.

          - **StatusType** *(string) --*

            This value is currently "read replication."

          - **Normal** *(boolean) --*

            Boolean value that is true if the instance is operating normally, or false if the
            instance is in an error state.

          - **Status** *(string) --*

            Status of the DB instance. For a StatusType of read replica, the values can be
            replicating, error, stopped, or terminated.

          - **Message** *(string) --*

            Details of the error if there is an error for the instance. If the instance is not in
            an error state, this value is blank.

      - **StorageType** *(string) --*

        Specifies the storage type associated with DB instance.

      - **TdeCredentialArn** *(string) --*

        The ARN from the key store with which the instance is associated for TDE encryption.

      - **DbInstancePort** *(integer) --*

        Specifies the port that the DB instance listens on. If the DB instance is part of a DB
        cluster, this can be a different port than the DB cluster port.

      - **DBClusterIdentifier** *(string) --*

        If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
        the DB instance is a member of.

      - **StorageEncrypted** *(boolean) --*

        Not supported: The encryption for DB instances is managed by the DB cluster.

      - **KmsKeyId** *(string) --*

        Not supported: The encryption for DB instances is managed by the DB cluster.

      - **DbiResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
        in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

      - **CACertificateIdentifier** *(string) --*

        The identifier of the CA certificate for this DB instance.

      - **DomainMemberships** *(list) --*

        Not supported

        - *(dict) --*

          An Active Directory Domain membership record associated with a DB instance.

          - **Domain** *(string) --*

            The identifier of the Active Directory Domain.

          - **Status** *(string) --*

            The status of the DB instance's Active Directory Domain membership, such as joined,
            pending-join, failed etc).

          - **FQDN** *(string) --*

            The fully qualified domain name of the Active Directory Domain.

          - **IAMRoleName** *(string) --*

            The name of the IAM role to be used when making API calls to the Directory Service.

      - **CopyTagsToSnapshot** *(boolean) --*

        Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

      - **MonitoringInterval** *(integer) --*

        The interval, in seconds, between points when Enhanced Monitoring metrics are collected for
        the DB instance.

      - **EnhancedMonitoringResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
        Enhanced Monitoring metrics data for the DB instance.

      - **MonitoringRoleArn** *(string) --*

        The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon
        CloudWatch Logs.

      - **PromotionTier** *(integer) --*

        A value that specifies the order in which a Read Replica is promoted to the primary
        instance after a failure of the existing primary instance.

      - **DBInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB instance.

      - **Timezone** *(string) --*

        Not supported.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
        false.

      - **PerformanceInsightsEnabled** *(boolean) --*

        True if Performance Insights is enabled for the DB instance, and otherwise false.

      - **PerformanceInsightsKMSKeyId** *(string) --*

        The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
        the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
        encryption key.

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB instance is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "_ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef(
    _ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef
):
    """
    Type definition for `ClientRemoveSourceIdentifierFromSubscriptionResponse` `EventSubscription`

    Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the event notification subscription.

    - **Status** *(string) --*

      The status of the event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that Neptune no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the event notification subscription was created.

    - **SourceType** *(string) --*

      The source type for the event notification subscription.

    - **SourceIdsList** *(list) --*

      A list of source IDs for the event notification subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A list of event categories for the event notification subscription.

      - *(string) --*

    - **Enabled** *(boolean) --*

      A Boolean value indicating if the subscription is enabled. True indicates the subscription
      is enabled.

    - **EventSubscriptionArn** *(string) --*

      The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef = TypedDict(
    "_ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef",
    {
        "EventSubscription": ClientRemoveSourceIdentifierFromSubscriptionResponseEventSubscriptionTypeDef
    },
    total=False,
)


class ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef(
    _ClientRemoveSourceIdentifierFromSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientRemoveSourceIdentifierFromSubscription` `Response`

    - **EventSubscription** *(dict) --*

      Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

      - **CustomerAwsId** *(string) --*

        The AWS customer account associated with the event notification subscription.

      - **CustSubscriptionId** *(string) --*

        The event notification subscription Id.

      - **SnsTopicArn** *(string) --*

        The topic ARN of the event notification subscription.

      - **Status** *(string) --*

        The status of the event notification subscription.

        Constraints:

        Can be one of the following: creating | modifying | deleting | active | no-permission |
        topic-not-exist

        The status "no-permission" indicates that Neptune no longer has permission to post to the
        SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
        subscription was created.

      - **SubscriptionCreationTime** *(string) --*

        The time the event notification subscription was created.

      - **SourceType** *(string) --*

        The source type for the event notification subscription.

      - **SourceIdsList** *(list) --*

        A list of source IDs for the event notification subscription.

        - *(string) --*

      - **EventCategoriesList** *(list) --*

        A list of event categories for the event notification subscription.

        - *(string) --*

      - **Enabled** *(boolean) --*

        A Boolean value indicating if the subscription is enabled. True indicates the subscription
        is enabled.

      - **EventSubscriptionArn** *(string) --*

        The Amazon Resource Name (ARN) for the event subscription.
    """


_ClientResetDbClusterParameterGroupParametersTypeDef = TypedDict(
    "_ClientResetDbClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientResetDbClusterParameterGroupParametersTypeDef(
    _ClientResetDbClusterParameterGroupParametersTypeDef
):
    """
    Type definition for `ClientResetDbClusterParameterGroup` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientResetDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientResetDbClusterParameterGroupResponseTypeDef",
    {"DBClusterParameterGroupName": str},
    total=False,
)


class ClientResetDbClusterParameterGroupResponseTypeDef(
    _ClientResetDbClusterParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientResetDbClusterParameterGroup` `Response`

    - **DBClusterParameterGroupName** *(string) --*

      The name of the DB cluster parameter group.

      Constraints:

      * Must be 1 to 255 letters or numbers.

      * First character must be a letter

      * Cannot end with a hyphen or contain two consecutive hyphens

      .. note::

        This value is stored as a lowercase string.
    """


_ClientResetDbParameterGroupParametersTypeDef = TypedDict(
    "_ClientResetDbParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientResetDbParameterGroupParametersTypeDef(
    _ClientResetDbParameterGroupParametersTypeDef
):
    """
    Type definition for `ClientResetDbParameterGroup` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientResetDbParameterGroupResponseTypeDef = TypedDict(
    "_ClientResetDbParameterGroupResponseTypeDef",
    {"DBParameterGroupName": str},
    total=False,
)


class ClientResetDbParameterGroupResponseTypeDef(
    _ClientResetDbParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientResetDbParameterGroup` `Response`

    - **DBParameterGroupName** *(string) --*

      Provides the name of the DB parameter group.
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshotResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The Status
      property returns one of the following values:

      * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
      is unable to assume the IAM role in order to access other AWS services on your behalf.
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshotResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      Value that is ``true`` if the cluster member is the primary instance for the DB cluster
      and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshotResponseDBCluster` `DBClusterOptionGroupMemberships`

    Contains status information for a DB cluster option group.

    - **DBClusterOptionGroupName** *(string) --*

      Specifies the name of the DB cluster option group.

    - **Status** *(string) --*

      Specifies the status of the DB cluster option group.
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshotResponseDBCluster` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshotResponse` `DBCluster`

    Contains the details of an Amazon Neptune DB cluster.

    This data type is used as a response element in the  DescribeDBClusters action.

    - **AllocatedStorage** *(integer) --*

       ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
       fixed, but instead automatically adjusts as needed.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
      in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this cluster is associated with.

    - **DatabaseName** *(string) --*

      Contains the name of the initial database of this DB cluster that was provided at create
      time, if one was specified when the DB cluster was created. This same name is returned for
      the life of the DB cluster.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group associated with the DB cluster, including the
      name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      Specifies the earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
      connections across the Read Replicas that are available in a DB cluster. As clients request
      new connections to the reader endpoint, Neptune distributes the connection requests among
      the Read Replicas in the DB cluster. This functionality can help balance your read workload
      across multiple Read Replicas in your DB cluster.

      If a failover occurs, and the Read Replica that you are connected to is promoted to be the
      primary instance, your connection is dropped. To continue sending your read workload to
      other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB cluster.

    - **DBClusterOptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB cluster.

      - *(dict) --*

        Contains status information for a DB cluster option group.

        - **DBClusterOptionGroupName** *(string) --*

          Specifies the name of the DB cluster option group.

        - **Status** *(string) --*

          Specifies the status of the DB cluster option group.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **ReplicationSourceIdentifier** *(string) --*

      Not supported by Neptune.

    - **ReadReplicaIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB cluster.

      - *(string) --*

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          Value that is ``true`` if the cluster member is the primary instance for the DB cluster
          and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security groups that the DB cluster belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The Status
          property returns one of the following values:

          * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
          is unable to assume the IAM role in order to access other AWS services on your behalf.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.

    - **CloneGroupId** *(string) --*

      Identifies the clone group to which the DB cluster is associated.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientRestoreDbClusterFromSnapshotResponseTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshot` `Response`

    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.

      This data type is used as a response element in the  DescribeDBClusters action.

      - **AllocatedStorage** *(integer) --*

         ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
         fixed, but instead automatically adjusts as needed.

      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
        in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this cluster is associated with.

      - **DatabaseName** *(string) --*

        Contains the name of the initial database of this DB cluster that was provided at create
        time, if one was specified when the DB cluster was created. This same name is returned for
        the life of the DB cluster.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group associated with the DB cluster, including the
        name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        Specifies the earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
        connections across the Read Replicas that are available in a DB cluster. As clients request
        new connections to the reader endpoint, Neptune distributes the connection requests among
        the Read Replicas in the DB cluster. This functionality can help balance your read workload
        across multiple Read Replicas in your DB cluster.

        If a failover occurs, and the Read Replica that you are connected to is promoted to be the
        primary instance, your connection is dropped. To continue sending your read workload to
        other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB cluster.

      - **DBClusterOptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB cluster.

        - *(dict) --*

          Contains status information for a DB cluster option group.

          - **DBClusterOptionGroupName** *(string) --*

            Specifies the name of the DB cluster option group.

          - **Status** *(string) --*

            Specifies the status of the DB cluster option group.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **ReplicationSourceIdentifier** *(string) --*

        Not supported by Neptune.

      - **ReadReplicaIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB cluster.

        - *(string) --*

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            Value that is ``true`` if the cluster member is the primary instance for the DB cluster
            and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which a Read Replica is promoted to the primary
            instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security groups that the DB cluster belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The Status
            property returns one of the following values:

            * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
            is unable to assume the IAM role in order to access other AWS services on your behalf.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
        is enabled, and otherwise false.

      - **CloneGroupId** *(string) --*

        Identifies the clone group to which the DB cluster is associated.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientRestoreDbClusterFromSnapshotTagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotTagsTypeDef(
    _ClientRestoreDbClusterFromSnapshotTagsTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshot` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTimeResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The Status
      property returns one of the following values:

      * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
      is unable to assume the IAM role in order to access other AWS services on your behalf.
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTimeResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      Value that is ``true`` if the cluster member is the primary instance for the DB cluster
      and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTimeResponseDBCluster` `DBClusterOptionGroupMemberships`

    Contains status information for a DB cluster option group.

    - **DBClusterOptionGroupName** *(string) --*

      Specifies the name of the DB cluster option group.

    - **Status** *(string) --*

      Specifies the status of the DB cluster option group.
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTimeResponseDBCluster` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTimeResponse` `DBCluster`

    Contains the details of an Amazon Neptune DB cluster.

    This data type is used as a response element in the  DescribeDBClusters action.

    - **AllocatedStorage** *(integer) --*

       ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
       fixed, but instead automatically adjusts as needed.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
      in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this cluster is associated with.

    - **DatabaseName** *(string) --*

      Contains the name of the initial database of this DB cluster that was provided at create
      time, if one was specified when the DB cluster was created. This same name is returned for
      the life of the DB cluster.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group associated with the DB cluster, including the
      name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      Specifies the earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
      connections across the Read Replicas that are available in a DB cluster. As clients request
      new connections to the reader endpoint, Neptune distributes the connection requests among
      the Read Replicas in the DB cluster. This functionality can help balance your read workload
      across multiple Read Replicas in your DB cluster.

      If a failover occurs, and the Read Replica that you are connected to is promoted to be the
      primary instance, your connection is dropped. To continue sending your read workload to
      other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB cluster.

    - **DBClusterOptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB cluster.

      - *(dict) --*

        Contains status information for a DB cluster option group.

        - **DBClusterOptionGroupName** *(string) --*

          Specifies the name of the DB cluster option group.

        - **Status** *(string) --*

          Specifies the status of the DB cluster option group.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **ReplicationSourceIdentifier** *(string) --*

      Not supported by Neptune.

    - **ReadReplicaIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB cluster.

      - *(string) --*

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          Value that is ``true`` if the cluster member is the primary instance for the DB cluster
          and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security groups that the DB cluster belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The Status
          property returns one of the following values:

          * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
          is unable to assume the IAM role in order to access other AWS services on your behalf.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.

    - **CloneGroupId** *(string) --*

      Identifies the clone group to which the DB cluster is associated.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_ClientRestoreDbClusterToPointInTimeResponseTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTime` `Response`

    - **DBCluster** *(dict) --*

      Contains the details of an Amazon Neptune DB cluster.

      This data type is used as a response element in the  DescribeDBClusters action.

      - **AllocatedStorage** *(integer) --*

         ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
         fixed, but instead automatically adjusts as needed.

      - **AvailabilityZones** *(list) --*

        Provides the list of EC2 Availability Zones that instances in the DB cluster can be created
        in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **CharacterSetName** *(string) --*

        If present, specifies the name of the character set that this cluster is associated with.

      - **DatabaseName** *(string) --*

        Contains the name of the initial database of this DB cluster that was provided at create
        time, if one was specified when the DB cluster was created. This same name is returned for
        the life of the DB cluster.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group associated with the DB cluster, including the
        name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        Specifies the earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances
        connections across the Read Replicas that are available in a DB cluster. As clients request
        new connections to the reader endpoint, Neptune distributes the connection requests among
        the Read Replicas in the DB cluster. This functionality can help balance your read workload
        across multiple Read Replicas in your DB cluster.

        If a failover occurs, and the Read Replica that you are connected to is promoted to be the
        primary instance, your connection is dropped. To continue sending your read workload to
        other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master username for the DB cluster.

      - **DBClusterOptionGroupMemberships** *(list) --*

        Provides the list of option group memberships for this DB cluster.

        - *(dict) --*

          Contains status information for a DB cluster option group.

          - **DBClusterOptionGroupName** *(string) --*

            Specifies the name of the DB cluster option group.

          - **Status** *(string) --*

            Specifies the status of the DB cluster option group.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **ReplicationSourceIdentifier** *(string) --*

        Not supported by Neptune.

      - **ReadReplicaIdentifiers** *(list) --*

        Contains one or more identifiers of the Read Replicas associated with this DB cluster.

        - *(string) --*

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            Value that is ``true`` if the cluster member is the primary instance for the DB cluster
            and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which a Read Replica is promoted to the primary
            instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security groups that the DB cluster belongs to.

        - *(dict) --*

          This data type is used as a response element for queries on VPC security group membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The Status
            property returns one of the following values:

            * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB cluster
            is unable to assume the IAM role in order to access other AWS services on your behalf.

      - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

        True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
        is enabled, and otherwise false.

      - **CloneGroupId** *(string) --*

        Identifies the clone group to which the DB cluster is associated.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to CloudWatch Logs.

        - *(string) --*
    """


_ClientRestoreDbClusterToPointInTimeTagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeTagsTypeDef(
    _ClientRestoreDbClusterToPointInTimeTagsTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTime` `Tags`

    Metadata assigned to an Amazon Neptune resource consisting of a key-value pair.

    - **Key** *(string) --*

      A key is the required name of the tag. The string value can be from 1 to 128 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
      characters in length and can't be prefixed with "aws:" or "rds:". The string can only contain
      only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java
      regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_DbInstanceAvailableWaitFiltersTypeDef = TypedDict(
    "_DbInstanceAvailableWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DbInstanceAvailableWaitFiltersTypeDef(_DbInstanceAvailableWaitFiltersTypeDef):
    """
    Type definition for `DbInstanceAvailableWait` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DbInstanceAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_DbInstanceAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class DbInstanceAvailableWaitWaiterConfigTypeDef(
    _DbInstanceAvailableWaitWaiterConfigTypeDef
):
    """
    Type definition for `DbInstanceAvailableWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_DbInstanceDeletedWaitFiltersTypeDef = TypedDict(
    "_DbInstanceDeletedWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DbInstanceDeletedWaitFiltersTypeDef(_DbInstanceDeletedWaitFiltersTypeDef):
    """
    Type definition for `DbInstanceDeletedWait` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DbInstanceDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_DbInstanceDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class DbInstanceDeletedWaitWaiterConfigTypeDef(
    _DbInstanceDeletedWaitWaiterConfigTypeDef
):
    """
    Type definition for `DbInstanceDeletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_DescribeDBClusterParameterGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClusterParameterGroupsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeDBClusterParameterGroupsPaginateFiltersTypeDef(
    _DescribeDBClusterParameterGroupsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBClusterParameterGroupsPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef(
    _DescribeDBClusterParameterGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBClusterParameterGroupsPaginate` `PaginationConfig`

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


_DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef = TypedDict(
    "_DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef(
    _DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef
):
    """
    Type definition for `DescribeDBClusterParameterGroupsPaginateResponse` `DBClusterParameterGroups`

    Contains the details of an Amazon Neptune DB cluster parameter group.

    This data type is used as a response element in the  DescribeDBClusterParameterGroups
    action.

    - **DBClusterParameterGroupName** *(string) --*

      Provides the name of the DB cluster parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB cluster parameter group
      is compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB cluster parameter group.

    - **DBClusterParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_DescribeDBClusterParameterGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClusterParameterGroupsPaginateResponseTypeDef",
    {
        "DBClusterParameterGroups": List[
            DescribeDBClusterParameterGroupsPaginateResponseDBClusterParameterGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBClusterParameterGroupsPaginateResponseTypeDef(
    _DescribeDBClusterParameterGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBClusterParameterGroupsPaginate` `Response`

    - **DBClusterParameterGroups** *(list) --*

      A list of DB cluster parameter groups.

      - *(dict) --*

        Contains the details of an Amazon Neptune DB cluster parameter group.

        This data type is used as a response element in the  DescribeDBClusterParameterGroups
        action.

        - **DBClusterParameterGroupName** *(string) --*

          Provides the name of the DB cluster parameter group.

        - **DBParameterGroupFamily** *(string) --*

          Provides the name of the DB parameter group family that this DB cluster parameter group
          is compatible with.

        - **Description** *(string) --*

          Provides the customer-specified description for this DB cluster parameter group.

        - **DBClusterParameterGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB cluster parameter group.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBClusterParametersPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClusterParametersPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeDBClusterParametersPaginateFiltersTypeDef(
    _DescribeDBClusterParametersPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBClusterParametersPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeDBClusterParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClusterParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClusterParametersPaginatePaginationConfigTypeDef(
    _DescribeDBClusterParametersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBClusterParametersPaginate` `PaginationConfig`

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


_DescribeDBClusterParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeDBClusterParametersPaginateResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class DescribeDBClusterParametersPaginateResponseParametersTypeDef(
    _DescribeDBClusterParametersPaginateResponseParametersTypeDef
):
    """
    Type definition for `DescribeDBClusterParametersPaginateResponse` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_DescribeDBClusterParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClusterParametersPaginateResponseTypeDef",
    {
        "Parameters": List[
            DescribeDBClusterParametersPaginateResponseParametersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBClusterParametersPaginateResponseTypeDef(
    _DescribeDBClusterParametersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBClusterParametersPaginate` `Response`

    - **Parameters** *(list) --*

      Provides a list of parameters for the DB cluster parameter group.

      - *(dict) --*

        Specifies a parameter.

        - **ParameterName** *(string) --*

          Specifies the name of the parameter.

        - **ParameterValue** *(string) --*

          Specifies the value of the parameter.

        - **Description** *(string) --*

          Provides a description of the parameter.

        - **Source** *(string) --*

          Indicates the source of the parameter value.

        - **ApplyType** *(string) --*

          Specifies the engine specific parameters type.

        - **DataType** *(string) --*

          Specifies the valid data type for the parameter.

        - **AllowedValues** *(string) --*

          Specifies the valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest engine version to which the parameter can apply.

        - **ApplyMethod** *(string) --*

          Indicates when to apply parameter updates.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBClusterSnapshotsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClusterSnapshotsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeDBClusterSnapshotsPaginateFiltersTypeDef(
    _DescribeDBClusterSnapshotsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBClusterSnapshotsPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef(
    _DescribeDBClusterSnapshotsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBClusterSnapshotsPaginate` `PaginationConfig`

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


_DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef = TypedDict(
    "_DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)


class DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef(
    _DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef
):
    """
    Type definition for `DescribeDBClusterSnapshotsPaginateResponse` `DBClusterSnapshots`

    Contains the details for an Amazon Neptune DB cluster snapshot

    This data type is used as a response element in the  DescribeDBClusterSnapshots action.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
      be restored in.

      - *(string) --*

    - **DBClusterSnapshotIdentifier** *(string) --*

      Specifies the identifier for the DB cluster snapshot.

    - **DBClusterIdentifier** *(string) --*

      Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
      created from.

    - **SnapshotCreateTime** *(datetime) --*

      Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

    - **Engine** *(string) --*

      Specifies the name of the database engine.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size in gibibytes (GiB).

    - **Status** *(string) --*

      Specifies the status of this DB cluster snapshot.

    - **Port** *(integer) --*

      Specifies the port that the DB cluster was listening on at the time of the snapshot.

    - **VpcId** *(string) --*

      Provides the VPC ID associated with the DB cluster snapshot.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **MasterUsername** *(string) --*

      Provides the master username for the DB cluster snapshot.

    - **EngineVersion** *(string) --*

      Provides the version of the database engine for this DB cluster snapshot.

    - **LicenseModel** *(string) --*

      Provides the license model information for this DB cluster snapshot.

    - **SnapshotType** *(string) --*

      Provides the type of the DB cluster snapshot.

    - **PercentProgress** *(integer) --*

      Specifies the percentage of the estimated data that has been transferred.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster snapshot is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster
      snapshot.

    - **DBClusterSnapshotArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster snapshot.

    - **SourceDBClusterSnapshotArn** *(string) --*

      If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon
      Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.
    """


_DescribeDBClusterSnapshotsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClusterSnapshotsPaginateResponseTypeDef",
    {
        "DBClusterSnapshots": List[
            DescribeDBClusterSnapshotsPaginateResponseDBClusterSnapshotsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBClusterSnapshotsPaginateResponseTypeDef(
    _DescribeDBClusterSnapshotsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBClusterSnapshotsPaginate` `Response`

    - **DBClusterSnapshots** *(list) --*

      Provides a list of DB cluster snapshots for the user.

      - *(dict) --*

        Contains the details for an Amazon Neptune DB cluster snapshot

        This data type is used as a response element in the  DescribeDBClusterSnapshots action.

        - **AvailabilityZones** *(list) --*

          Provides the list of EC2 Availability Zones that instances in the DB cluster snapshot can
          be restored in.

          - *(string) --*

        - **DBClusterSnapshotIdentifier** *(string) --*

          Specifies the identifier for the DB cluster snapshot.

        - **DBClusterIdentifier** *(string) --*

          Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
          created from.

        - **SnapshotCreateTime** *(datetime) --*

          Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).

        - **Engine** *(string) --*

          Specifies the name of the database engine.

        - **AllocatedStorage** *(integer) --*

          Specifies the allocated storage size in gibibytes (GiB).

        - **Status** *(string) --*

          Specifies the status of this DB cluster snapshot.

        - **Port** *(integer) --*

          Specifies the port that the DB cluster was listening on at the time of the snapshot.

        - **VpcId** *(string) --*

          Provides the VPC ID associated with the DB cluster snapshot.

        - **ClusterCreateTime** *(datetime) --*

          Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

        - **MasterUsername** *(string) --*

          Provides the master username for the DB cluster snapshot.

        - **EngineVersion** *(string) --*

          Provides the version of the database engine for this DB cluster snapshot.

        - **LicenseModel** *(string) --*

          Provides the license model information for this DB cluster snapshot.

        - **SnapshotType** *(string) --*

          Provides the type of the DB cluster snapshot.

        - **PercentProgress** *(integer) --*

          Specifies the percentage of the estimated data that has been transferred.

        - **StorageEncrypted** *(boolean) --*

          Specifies whether the DB cluster snapshot is encrypted.

        - **KmsKeyId** *(string) --*

          If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster
          snapshot.

        - **DBClusterSnapshotArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB cluster snapshot.

        - **SourceDBClusterSnapshotArn** *(string) --*

          If the DB cluster snapshot was copied from a source DB cluster snapshot, the Amazon
          Resource Name (ARN) for the source DB cluster snapshot, otherwise, a null value.

        - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

          True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
          is enabled, and otherwise false.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBClustersPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClustersPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeDBClustersPaginateFiltersTypeDef(
    _DescribeDBClustersPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeDBClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClustersPaginatePaginationConfigTypeDef(
    _DescribeDBClustersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginate` `PaginationConfig`

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


_DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginateResponseDBClusters` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      Status property returns one of the following values:

      * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB
      cluster is unable to assume the IAM role in order to access other AWS services on
      your behalf.
    """


_DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginateResponseDBClusters` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      Value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.
    """


_DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef",
    {"DBClusterOptionGroupName": str, "Status": str},
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginateResponseDBClusters` `DBClusterOptionGroupMemberships`

    Contains status information for a DB cluster option group.

    - **DBClusterOptionGroupName** *(string) --*

      Specifies the name of the DB cluster option group.

    - **Status** *(string) --*

      Specifies the status of the DB cluster option group.
    """


_DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginateResponseDBClusters` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_DescribeDBClustersPaginateResponseDBClustersTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List[
            DescribeDBClustersPaginateResponseDBClustersDBClusterOptionGroupMembershipsTypeDef
        ],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List[
            DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef
        ],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginateResponse` `DBClusters`

    Contains the details of an Amazon Neptune DB cluster.

    This data type is used as a response element in the  DescribeDBClusters action.

    - **AllocatedStorage** *(integer) --*

       ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
       fixed, but instead automatically adjusts as needed.

    - **AvailabilityZones** *(list) --*

      Provides the list of EC2 Availability Zones that instances in the DB cluster can be
      created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this cluster is associated with.

    - **DatabaseName** *(string) --*

      Contains the name of the initial database of this DB cluster that was provided at create
      time, if one was specified when the DB cluster was created. This same name is returned
      for the life of the DB cluster.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group associated with the DB cluster, including the
      name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      Specifies the earliest time to which a database can be restored with point-in-time
      restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
      load-balances connections across the Read Replicas that are available in a DB cluster. As
      clients request new connections to the reader endpoint, Neptune distributes the
      connection requests among the Read Replicas in the DB cluster. This functionality can
      help balance your read workload across multiple Read Replicas in your DB cluster.

      If a failover occurs, and the Read Replica that you are connected to is promoted to be
      the primary instance, your connection is dropped. To continue sending your read workload
      to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB cluster.

    - **DBClusterOptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB cluster.

      - *(dict) --*

        Contains status information for a DB cluster option group.

        - **DBClusterOptionGroupName** *(string) --*

          Specifies the name of the DB cluster option group.

        - **Status** *(string) --*

          Specifies the status of the DB cluster option group.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **ReplicationSourceIdentifier** *(string) --*

      Not supported by Neptune.

    - **ReadReplicaIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB cluster.

      - *(string) --*

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          Value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security groups that the DB cluster belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          Status property returns one of the following values:

          * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB
          cluster is unable to assume the IAM role in order to access other AWS services on
          your behalf.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
      is enabled, and otherwise false.

    - **CloneGroupId** *(string) --*

      Identifies the clone group to which the DB cluster is associated.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_DescribeDBClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseTypeDef",
    {
        "DBClusters": List[DescribeDBClustersPaginateResponseDBClustersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBClustersPaginateResponseTypeDef(
    _DescribeDBClustersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginate` `Response`

    - **DBClusters** *(list) --*

      Contains a list of DB clusters for the user.

      - *(dict) --*

        Contains the details of an Amazon Neptune DB cluster.

        This data type is used as a response element in the  DescribeDBClusters action.

        - **AllocatedStorage** *(integer) --*

           ``AllocatedStorage`` always returns 1, because Neptune DB cluster storage size is not
           fixed, but instead automatically adjusts as needed.

        - **AvailabilityZones** *(list) --*

          Provides the list of EC2 Availability Zones that instances in the DB cluster can be
          created in.

          - *(string) --*

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the number of days for which automatic DB snapshots are retained.

        - **CharacterSetName** *(string) --*

          If present, specifies the name of the character set that this cluster is associated with.

        - **DatabaseName** *(string) --*

          Contains the name of the initial database of this DB cluster that was provided at create
          time, if one was specified when the DB cluster was created. This same name is returned
          for the life of the DB cluster.

        - **DBClusterIdentifier** *(string) --*

          Contains a user-supplied DB cluster identifier. This identifier is the unique key that
          identifies a DB cluster.

        - **DBClusterParameterGroup** *(string) --*

          Specifies the name of the DB cluster parameter group for the DB cluster.

        - **DBSubnetGroup** *(string) --*

          Specifies information on the subnet group associated with the DB cluster, including the
          name, description, and subnets in the subnet group.

        - **Status** *(string) --*

          Specifies the current state of this DB cluster.

        - **PercentProgress** *(string) --*

          Specifies the progress of the operation as a percentage.

        - **EarliestRestorableTime** *(datetime) --*

          Specifies the earliest time to which a database can be restored with point-in-time
          restore.

        - **Endpoint** *(string) --*

          Specifies the connection endpoint for the primary instance of the DB cluster.

        - **ReaderEndpoint** *(string) --*

          The reader endpoint for the DB cluster. The reader endpoint for a DB cluster
          load-balances connections across the Read Replicas that are available in a DB cluster. As
          clients request new connections to the reader endpoint, Neptune distributes the
          connection requests among the Read Replicas in the DB cluster. This functionality can
          help balance your read workload across multiple Read Replicas in your DB cluster.

          If a failover occurs, and the Read Replica that you are connected to is promoted to be
          the primary instance, your connection is dropped. To continue sending your read workload
          to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.

        - **MultiAZ** *(boolean) --*

          Specifies whether the DB cluster has instances in multiple Availability Zones.

        - **Engine** *(string) --*

          Provides the name of the database engine to be used for this DB cluster.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LatestRestorableTime** *(datetime) --*

          Specifies the latest time to which a database can be restored with point-in-time restore.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **MasterUsername** *(string) --*

          Contains the master username for the DB cluster.

        - **DBClusterOptionGroupMemberships** *(list) --*

          Provides the list of option group memberships for this DB cluster.

          - *(dict) --*

            Contains status information for a DB cluster option group.

            - **DBClusterOptionGroupName** *(string) --*

              Specifies the name of the DB cluster option group.

            - **Status** *(string) --*

              Specifies the status of the DB cluster option group.

        - **PreferredBackupWindow** *(string) --*

          Specifies the daily time range during which automated backups are created if automated
          backups are enabled, as determined by the ``BackupRetentionPeriod`` .

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which system maintenance can occur, in Universal
          Coordinated Time (UTC).

        - **ReplicationSourceIdentifier** *(string) --*

          Not supported by Neptune.

        - **ReadReplicaIdentifiers** *(list) --*

          Contains one or more identifiers of the Read Replicas associated with this DB cluster.

          - *(string) --*

        - **DBClusterMembers** *(list) --*

          Provides the list of instances that make up the DB cluster.

          - *(dict) --*

            Contains information about an instance that is part of a DB cluster.

            - **DBInstanceIdentifier** *(string) --*

              Specifies the instance identifier for this member of the DB cluster.

            - **IsClusterWriter** *(boolean) --*

              Value that is ``true`` if the cluster member is the primary instance for the DB
              cluster and ``false`` otherwise.

            - **DBClusterParameterGroupStatus** *(string) --*

              Specifies the status of the DB cluster parameter group for this member of the DB
              cluster.

            - **PromotionTier** *(integer) --*

              A value that specifies the order in which a Read Replica is promoted to the primary
              instance after a failure of the existing primary instance.

        - **VpcSecurityGroups** *(list) --*

          Provides a list of VPC security groups that the DB cluster belongs to.

          - *(dict) --*

            This data type is used as a response element for queries on VPC security group
            membership.

            - **VpcSecurityGroupId** *(string) --*

              The name of the VPC security group.

            - **Status** *(string) --*

              The status of the VPC security group.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

        - **StorageEncrypted** *(boolean) --*

          Specifies whether the DB cluster is encrypted.

        - **KmsKeyId** *(string) --*

          If ``StorageEncrypted`` is true, the AWS KMS key identifier for the encrypted DB cluster.

        - **DbClusterResourceId** *(string) --*

          The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found
          in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

        - **DBClusterArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB cluster.

        - **AssociatedRoles** *(list) --*

          Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
          with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
          the DB cluster to access other AWS services on your behalf.

          - *(dict) --*

            Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
            cluster.

            - **RoleArn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

            - **Status** *(string) --*

              Describes the state of association between the IAM role and the DB cluster. The
              Status property returns one of the following values:

              * ``ACTIVE`` - the IAM role ARN is associated with the DB cluster and can be used to
              access other AWS services on your behalf.

              * ``PENDING`` - the IAM role ARN is being associated with the DB cluster.

              * ``INVALID`` - the IAM role ARN is associated with the DB cluster, but the DB
              cluster is unable to assume the IAM role in order to access other AWS services on
              your behalf.

        - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

          True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts
          is enabled, and otherwise false.

        - **CloneGroupId** *(string) --*

          Identifies the clone group to which the DB cluster is associated.

        - **ClusterCreateTime** *(datetime) --*

          Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

        - **EnabledCloudwatchLogsExports** *(list) --*

          A list of log types that this DB cluster is configured to export to CloudWatch Logs.

          - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBEngineVersionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeDBEngineVersionsPaginateFiltersTypeDef(
    _DescribeDBEngineVersionsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeDBEngineVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBEngineVersionsPaginatePaginationConfigTypeDef(
    _DescribeDBEngineVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginate` `PaginationConfig`

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


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef",
    {"CharacterSetName": str, "CharacterSetDescription": str},
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginateResponseDBEngineVersions` `DefaultCharacterSet`

    The default character set for new instances of this engine version, if the
    ``CharacterSetName`` parameter of the CreateDBInstance API is not specified.

    - **CharacterSetName** *(string) --*

      The name of the character set.

    - **CharacterSetDescription** *(string) --*

      The description of the character set.
    """


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef",
    {"CharacterSetName": str, "CharacterSetDescription": str},
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginateResponseDBEngineVersions` `SupportedCharacterSets`

    Specifies a character set.

    - **CharacterSetName** *(string) --*

      The name of the character set.

    - **CharacterSetDescription** *(string) --*

      The description of the character set.
    """


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef",
    {"TimezoneName": str},
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginateResponseDBEngineVersions` `SupportedTimezones`

    A time zone associated with a  DBInstance .

    - **TimezoneName** *(string) --*

      The name of the time zone.
    """


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginateResponseDBEngineVersions` `ValidUpgradeTarget`

    The version of the database engine that a DB instance can be upgraded to.

    - **Engine** *(string) --*

      The name of the upgrade target database engine.

    - **EngineVersion** *(string) --*

      The version number of the upgrade target database engine.

    - **Description** *(string) --*

      The version of the database engine that a DB instance can be upgraded to.

    - **AutoUpgrade** *(boolean) --*

      A value that indicates whether the target version is applied to any source DB
      instances that have AutoMinorVersionUpgrade set to true.

    - **IsMajorVersionUpgrade** *(boolean) --*

      A value that indicates whether a database engine is upgraded to a major version.
    """


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "DefaultCharacterSet": DescribeDBEngineVersionsPaginateResponseDBEngineVersionsDefaultCharacterSetTypeDef,
        "SupportedCharacterSets": List[
            DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedCharacterSetsTypeDef
        ],
        "ValidUpgradeTarget": List[
            DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef
        ],
        "SupportedTimezones": List[
            DescribeDBEngineVersionsPaginateResponseDBEngineVersionsSupportedTimezonesTypeDef
        ],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginateResponse` `DBEngineVersions`

    This data type is used as a response element in the action  DescribeDBEngineVersions .

    - **Engine** *(string) --*

      The name of the database engine.

    - **EngineVersion** *(string) --*

      The version number of the database engine.

    - **DBParameterGroupFamily** *(string) --*

      The name of the DB parameter group family for the database engine.

    - **DBEngineDescription** *(string) --*

      The description of the database engine.

    - **DBEngineVersionDescription** *(string) --*

      The description of the database engine version.

    - **DefaultCharacterSet** *(dict) --*

      The default character set for new instances of this engine version, if the
      ``CharacterSetName`` parameter of the CreateDBInstance API is not specified.

      - **CharacterSetName** *(string) --*

        The name of the character set.

      - **CharacterSetDescription** *(string) --*

        The description of the character set.

    - **SupportedCharacterSets** *(list) --*

      A list of the character sets supported by this engine for the ``CharacterSetName``
      parameter of the ``CreateDBInstance`` action.

      - *(dict) --*

        Specifies a character set.

        - **CharacterSetName** *(string) --*

          The name of the character set.

        - **CharacterSetDescription** *(string) --*

          The description of the character set.

    - **ValidUpgradeTarget** *(list) --*

      A list of engine versions that this database engine version can be upgraded to.

      - *(dict) --*

        The version of the database engine that a DB instance can be upgraded to.

        - **Engine** *(string) --*

          The name of the upgrade target database engine.

        - **EngineVersion** *(string) --*

          The version number of the upgrade target database engine.

        - **Description** *(string) --*

          The version of the database engine that a DB instance can be upgraded to.

        - **AutoUpgrade** *(boolean) --*

          A value that indicates whether the target version is applied to any source DB
          instances that have AutoMinorVersionUpgrade set to true.

        - **IsMajorVersionUpgrade** *(boolean) --*

          A value that indicates whether a database engine is upgraded to a major version.

    - **SupportedTimezones** *(list) --*

      A list of the time zones supported by this engine for the ``Timezone`` parameter of the
      ``CreateDBInstance`` action.

      - *(dict) --*

        A time zone associated with a  DBInstance .

        - **TimezoneName** *(string) --*

          The name of the time zone.

    - **ExportableLogTypes** *(list) --*

      The types of logs that the database engine has available for export to CloudWatch Logs.

      - *(string) --*

    - **SupportsLogExportsToCloudwatchLogs** *(boolean) --*

      A value that indicates whether the engine version supports exporting the log types
      specified by ExportableLogTypes to CloudWatch Logs.

    - **SupportsReadReplica** *(boolean) --*

      Indicates whether the database engine version supports read replicas.
    """


_DescribeDBEngineVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseTypeDef",
    {
        "DBEngineVersions": List[
            DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseTypeDef(
    _DescribeDBEngineVersionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginate` `Response`

    - **DBEngineVersions** *(list) --*

      A list of ``DBEngineVersion`` elements.

      - *(dict) --*

        This data type is used as a response element in the action  DescribeDBEngineVersions .

        - **Engine** *(string) --*

          The name of the database engine.

        - **EngineVersion** *(string) --*

          The version number of the database engine.

        - **DBParameterGroupFamily** *(string) --*

          The name of the DB parameter group family for the database engine.

        - **DBEngineDescription** *(string) --*

          The description of the database engine.

        - **DBEngineVersionDescription** *(string) --*

          The description of the database engine version.

        - **DefaultCharacterSet** *(dict) --*

          The default character set for new instances of this engine version, if the
          ``CharacterSetName`` parameter of the CreateDBInstance API is not specified.

          - **CharacterSetName** *(string) --*

            The name of the character set.

          - **CharacterSetDescription** *(string) --*

            The description of the character set.

        - **SupportedCharacterSets** *(list) --*

          A list of the character sets supported by this engine for the ``CharacterSetName``
          parameter of the ``CreateDBInstance`` action.

          - *(dict) --*

            Specifies a character set.

            - **CharacterSetName** *(string) --*

              The name of the character set.

            - **CharacterSetDescription** *(string) --*

              The description of the character set.

        - **ValidUpgradeTarget** *(list) --*

          A list of engine versions that this database engine version can be upgraded to.

          - *(dict) --*

            The version of the database engine that a DB instance can be upgraded to.

            - **Engine** *(string) --*

              The name of the upgrade target database engine.

            - **EngineVersion** *(string) --*

              The version number of the upgrade target database engine.

            - **Description** *(string) --*

              The version of the database engine that a DB instance can be upgraded to.

            - **AutoUpgrade** *(boolean) --*

              A value that indicates whether the target version is applied to any source DB
              instances that have AutoMinorVersionUpgrade set to true.

            - **IsMajorVersionUpgrade** *(boolean) --*

              A value that indicates whether a database engine is upgraded to a major version.

        - **SupportedTimezones** *(list) --*

          A list of the time zones supported by this engine for the ``Timezone`` parameter of the
          ``CreateDBInstance`` action.

          - *(dict) --*

            A time zone associated with a  DBInstance .

            - **TimezoneName** *(string) --*

              The name of the time zone.

        - **ExportableLogTypes** *(list) --*

          The types of logs that the database engine has available for export to CloudWatch Logs.

          - *(string) --*

        - **SupportsLogExportsToCloudwatchLogs** *(boolean) --*

          A value that indicates whether the engine version supports exporting the log types
          specified by ExportableLogTypes to CloudWatch Logs.

        - **SupportsReadReplica** *(boolean) --*

          Indicates whether the database engine version supports read replicas.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBInstancesPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeDBInstancesPaginateFiltersTypeDef(
    _DescribeDBInstancesPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeDBInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBInstancesPaginatePaginationConfigTypeDef(
    _DescribeDBInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginate` `PaginationConfig`

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


_DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef",
    {"DBParameterGroupName": str, "ParameterApplyStatus": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `DBParameterGroups`

    The status of the DB parameter group.

    This data type is used as a response element in the following actions:

    *  CreateDBInstance

    *  DeleteDBInstance

    *  ModifyDBInstance

    *  RebootDBInstance

    - **DBParameterGroupName** *(string) --*

      The name of the DP parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.
    """


_DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef",
    {"DBSecurityGroupName": str, "Status": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `DBSecurityGroups`

    Specifies membership in a designated DB security group.

    - **DBSecurityGroupName** *(string) --*

      The name of the DB security group.

    - **Status** *(string) --*

      The status of the DB security group.
    """


_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the EC2 Availability Zone that the subnet is in.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroup` `Subnets`

    Specifies a subnet.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the EC2 Availability Zone that the subnet is in.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `DBSubnetGroup`

    Specifies information on the subnet group associated with the DB instance, including the
    name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the VpcId of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Contains a list of  Subnet elements.

      - *(dict) --*

        Specifies a subnet.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the EC2 Availability Zone that the subnet is in.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef",
    {"Domain": str, "Status": str, "FQDN": str, "IAMRoleName": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `DomainMemberships`

    An Active Directory Domain membership record associated with a DB instance.

    - **Domain** *(string) --*

      The identifier of the Active Directory Domain.

    - **Status** *(string) --*

      The status of the DB instance's Active Directory Domain membership, such as joined,
      pending-join, failed etc).

    - **FQDN** *(string) --*

      The fully qualified domain name of the Active Directory Domain.

    - **IAMRoleName** *(string) --*

      The name of the IAM role to be used when making API calls to the Directory Service.
    """


_DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef",
    {"OptionGroupName": str, "Status": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `OptionGroupMemberships`

    Provides information on the option groups the DB instance is a member of.

    - **OptionGroupName** *(string) --*

      The name of the option group that the instance belongs to.

    - **Status** *(string) --*

      The status of the DB instance's option group membership. Valid values are:
      ``in-sync`` , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply``
      , ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .
    """


_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValues` `PendingCloudwatchLogsExports`

    Specifies the CloudWatch logs to be exported.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to CloudWatch Logs.

      - *(string) --*
    """


_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is only included when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
      is currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently-in-progress change of the master credentials for the
      DB instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` | ``bring-your-own-license`` |
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
      is currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the CA certificate for the DB instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      Specifies the CloudWatch logs to be exported.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to CloudWatch Logs.

        - *(string) --*
    """


_DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "read replication."

    - **Normal** *(boolean) --*

      Boolean value that is true if the instance is operating normally, or false if the
      instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a StatusType of read replica, the values can be
      replicating, error, stopped, or terminated.

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `VpcSecurityGroups`

    This data type is used as a response element for queries on VPC security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_DescribeDBInstancesPaginateResponseDBInstancesTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List[
            DescribeDBInstancesPaginateResponseDBInstancesDBSecurityGroupsTypeDef
        ],
        "VpcSecurityGroups": List[
            DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef
        ],
        "DBParameterGroups": List[
            DescribeDBInstancesPaginateResponseDBInstancesDBParameterGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List[
            DescribeDBInstancesPaginateResponseDBInstancesOptionGroupMembershipsTypeDef
        ],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List[
            DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef
        ],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List[
            DescribeDBInstancesPaginateResponseDBInstancesDomainMembershipsTypeDef
        ],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponse` `DBInstances`

    Contains the details of an Amazon Neptune DB instance.

    This data type is used as a response element in the  DescribeDBInstances action.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-supplied database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **MasterUsername** *(string) --*

      Contains the master username for the DB instance.

    - **DBName** *(string) --*

      The database name.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **AllocatedStorage** *(integer) --*

      Specifies the allocated storage size specified in gibibytes.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBSecurityGroups** *(list) --*

      Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
      ``DBSecurityGroup.Status`` subelements.

      - *(dict) --*

        Specifies membership in a designated DB security group.

        - **DBSecurityGroupName** *(string) --*

          The name of the DB security group.

        - **Status** *(string) --*

          The status of the DB security group.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        This data type is used as a response element for queries on VPC security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **DBParameterGroups** *(list) --*

      Provides the list of DB parameter groups applied to this DB instance.

      - *(dict) --*

        The status of the DB parameter group.

        This data type is used as a response element in the following actions:

        *  CreateDBInstance

        *  DeleteDBInstance

        *  ModifyDBInstance

        *  RebootDBInstance

        - **DBParameterGroupName** *(string) --*

          The name of the DP parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group associated with the DB instance, including the
      name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the VpcId of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Contains a list of  Subnet elements.

        - *(dict) --*

          Specifies a subnet.

          This data type is used as a response element in the  DescribeDBSubnetGroups action.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the EC2 Availability Zone that the subnet is in.

            - **Name** *(string) --*

              The name of the availability zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is only included when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
        is currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently-in-progress change of the master credentials for the
        DB instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` | ``bring-your-own-license`` |
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
        is currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the CA certificate for the DB instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        Specifies the CloudWatch logs to be exported.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **MultiAZ** *(boolean) --*

      Specifies if the DB instance is a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

      Contains the identifier of the source DB instance if this DB instance is a Read Replica.

    - **ReadReplicaDBInstanceIdentifiers** *(list) --*

      Contains one or more identifiers of the Read Replicas associated with this DB instance.

      - *(string) --*

    - **ReadReplicaDBClusterIdentifiers** *(list) --*

      Contains one or more identifiers of DB clusters that are Read Replicas of this DB
      instance.

      - *(string) --*

    - **LicenseModel** *(string) --*

      License model information for this DB instance.

    - **Iops** *(integer) --*

      Specifies the Provisioned IOPS (I/O operations per second) value.

    - **OptionGroupMemberships** *(list) --*

      Provides the list of option group memberships for this DB instance.

      - *(dict) --*

        Provides information on the option groups the DB instance is a member of.

        - **OptionGroupName** *(string) --*

          The name of the option group that the instance belongs to.

        - **Status** *(string) --*

          The status of the DB instance's option group membership. Valid values are:
          ``in-sync`` , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply``
          , ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

    - **CharacterSetName** *(string) --*

      If present, specifies the name of the character set that this instance is associated with.

    - **SecondaryAvailabilityZone** *(string) --*

      If present, specifies the name of the secondary Availability Zone for a DB instance with
      multi-AZ support.

    - **PubliclyAccessible** *(boolean) --*

      This flag should no longer be used.

    - **StatusInfos** *(list) --*

      The status of a Read Replica. If the instance is not a Read Replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "read replication."

        - **Normal** *(boolean) --*

          Boolean value that is true if the instance is operating normally, or false if the
          instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a StatusType of read replica, the values can be
          replicating, error, stopped, or terminated.

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **StorageType** *(string) --*

      Specifies the storage type associated with DB instance.

    - **TdeCredentialArn** *(string) --*

      The ARN from the key store with which the instance is associated for TDE encryption.

    - **DbInstancePort** *(integer) --*

      Specifies the port that the DB instance listens on. If the DB instance is part of a DB
      cluster, this can be a different port than the DB cluster port.

    - **DBClusterIdentifier** *(string) --*

      If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
      the DB instance is a member of.

    - **StorageEncrypted** *(boolean) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **KmsKeyId** *(string) --*

      Not supported: The encryption for DB instances is managed by the DB cluster.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **DomainMemberships** *(list) --*

      Not supported

      - *(dict) --*

        An Active Directory Domain membership record associated with a DB instance.

        - **Domain** *(string) --*

          The identifier of the Active Directory Domain.

        - **Status** *(string) --*

          The status of the DB instance's Active Directory Domain membership, such as joined,
          pending-join, failed etc).

        - **FQDN** *(string) --*

          The fully qualified domain name of the Active Directory Domain.

        - **IAMRoleName** *(string) --*

          The name of the IAM role to be used when making API calls to the Directory Service.

    - **CopyTagsToSnapshot** *(boolean) --*

      Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

    - **MonitoringInterval** *(integer) --*

      The interval, in seconds, between points when Enhanced Monitoring metrics are collected
      for the DB instance.

    - **EnhancedMonitoringResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
      Enhanced Monitoring metrics data for the DB instance.

    - **MonitoringRoleArn** *(string) --*

      The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to
      Amazon CloudWatch Logs.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which a Read Replica is promoted to the primary
      instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **Timezone** *(string) --*

      Not supported.

    - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

      True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
      false.

    - **PerformanceInsightsEnabled** *(boolean) --*

      True if Performance Insights is enabled for the DB instance, and otherwise false.

    - **PerformanceInsightsKMSKeyId** *(string) --*

      The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
      the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
      encryption key.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to CloudWatch Logs.

      - *(string) --*
    """


_DescribeDBInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseTypeDef",
    {
        "DBInstances": List[DescribeDBInstancesPaginateResponseDBInstancesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseTypeDef(
    _DescribeDBInstancesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginate` `Response`

    - **DBInstances** *(list) --*

      A list of  DBInstance instances.

      - *(dict) --*

        Contains the details of an Amazon Neptune DB instance.

        This data type is used as a response element in the  DescribeDBInstances action.

        - **DBInstanceIdentifier** *(string) --*

          Contains a user-supplied database identifier. This identifier is the unique key that
          identifies a DB instance.

        - **DBInstanceClass** *(string) --*

          Contains the name of the compute and memory capacity class of the DB instance.

        - **Engine** *(string) --*

          Provides the name of the database engine to be used for this DB instance.

        - **DBInstanceStatus** *(string) --*

          Specifies the current state of this database.

        - **MasterUsername** *(string) --*

          Contains the master username for the DB instance.

        - **DBName** *(string) --*

          The database name.

        - **Endpoint** *(dict) --*

          Specifies the connection endpoint.

          - **Address** *(string) --*

            Specifies the DNS address of the DB instance.

          - **Port** *(integer) --*

            Specifies the port that the database engine is listening on.

          - **HostedZoneId** *(string) --*

            Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

        - **AllocatedStorage** *(integer) --*

          Specifies the allocated storage size specified in gibibytes.

        - **InstanceCreateTime** *(datetime) --*

          Provides the date and time the DB instance was created.

        - **PreferredBackupWindow** *(string) --*

          Specifies the daily time range during which automated backups are created if automated
          backups are enabled, as determined by the ``BackupRetentionPeriod`` .

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the number of days for which automatic DB snapshots are retained.

        - **DBSecurityGroups** *(list) --*

          Provides List of DB security group elements containing only ``DBSecurityGroup.Name`` and
          ``DBSecurityGroup.Status`` subelements.

          - *(dict) --*

            Specifies membership in a designated DB security group.

            - **DBSecurityGroupName** *(string) --*

              The name of the DB security group.

            - **Status** *(string) --*

              The status of the DB security group.

        - **VpcSecurityGroups** *(list) --*

          Provides a list of VPC security group elements that the DB instance belongs to.

          - *(dict) --*

            This data type is used as a response element for queries on VPC security group
            membership.

            - **VpcSecurityGroupId** *(string) --*

              The name of the VPC security group.

            - **Status** *(string) --*

              The status of the VPC security group.

        - **DBParameterGroups** *(list) --*

          Provides the list of DB parameter groups applied to this DB instance.

          - *(dict) --*

            The status of the DB parameter group.

            This data type is used as a response element in the following actions:

            *  CreateDBInstance

            *  DeleteDBInstance

            *  ModifyDBInstance

            *  RebootDBInstance

            - **DBParameterGroupName** *(string) --*

              The name of the DP parameter group.

            - **ParameterApplyStatus** *(string) --*

              The status of parameter updates.

        - **AvailabilityZone** *(string) --*

          Specifies the name of the Availability Zone the DB instance is located in.

        - **DBSubnetGroup** *(dict) --*

          Specifies information on the subnet group associated with the DB instance, including the
          name, description, and subnets in the subnet group.

          - **DBSubnetGroupName** *(string) --*

            The name of the DB subnet group.

          - **DBSubnetGroupDescription** *(string) --*

            Provides the description of the DB subnet group.

          - **VpcId** *(string) --*

            Provides the VpcId of the DB subnet group.

          - **SubnetGroupStatus** *(string) --*

            Provides the status of the DB subnet group.

          - **Subnets** *(list) --*

            Contains a list of  Subnet elements.

            - *(dict) --*

              Specifies a subnet.

              This data type is used as a response element in the  DescribeDBSubnetGroups action.

              - **SubnetIdentifier** *(string) --*

                Specifies the identifier of the subnet.

              - **SubnetAvailabilityZone** *(dict) --*

                Specifies the EC2 Availability Zone that the subnet is in.

                - **Name** *(string) --*

                  The name of the availability zone.

              - **SubnetStatus** *(string) --*

                Specifies the status of the subnet.

          - **DBSubnetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) for the DB subnet group.

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which system maintenance can occur, in Universal
          Coordinated Time (UTC).

        - **PendingModifiedValues** *(dict) --*

          Specifies that changes to the DB instance are pending. This element is only included when
          changes are pending. Specific changes are identified by subelements.

          - **DBInstanceClass** *(string) --*

            Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
            currently being applied.

          - **AllocatedStorage** *(integer) --*

            Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
            is currently being applied.

          - **MasterUserPassword** *(string) --*

            Contains the pending or currently-in-progress change of the master credentials for the
            DB instance.

          - **Port** *(integer) --*

            Specifies the pending port for the DB instance.

          - **BackupRetentionPeriod** *(integer) --*

            Specifies the pending number of days for which automated backups are retained.

          - **MultiAZ** *(boolean) --*

            Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

          - **EngineVersion** *(string) --*

            Indicates the database engine version.

          - **LicenseModel** *(string) --*

            The license model for the DB instance.

            Valid values: ``license-included`` | ``bring-your-own-license`` |
            ``general-public-license``

          - **Iops** *(integer) --*

            Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
            currently being applied.

          - **DBInstanceIdentifier** *(string) --*

            Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
            is currently being applied.

          - **StorageType** *(string) --*

            Specifies the storage type to be associated with the DB instance.

          - **CACertificateIdentifier** *(string) --*

            Specifies the identifier of the CA certificate for the DB instance.

          - **DBSubnetGroupName** *(string) --*

            The new DB subnet group for the DB instance.

          - **PendingCloudwatchLogsExports** *(dict) --*

            Specifies the CloudWatch logs to be exported.

            - **LogTypesToEnable** *(list) --*

              Log types that are in the process of being deactivated. After they are deactivated,
              these log types aren't exported to CloudWatch Logs.

              - *(string) --*

            - **LogTypesToDisable** *(list) --*

              Log types that are in the process of being enabled. After they are enabled, these log
              types are exported to CloudWatch Logs.

              - *(string) --*

        - **LatestRestorableTime** *(datetime) --*

          Specifies the latest time to which a database can be restored with point-in-time restore.

        - **MultiAZ** *(boolean) --*

          Specifies if the DB instance is a Multi-AZ deployment.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **AutoMinorVersionUpgrade** *(boolean) --*

          Indicates that minor version patches are applied automatically.

        - **ReadReplicaSourceDBInstanceIdentifier** *(string) --*

          Contains the identifier of the source DB instance if this DB instance is a Read Replica.

        - **ReadReplicaDBInstanceIdentifiers** *(list) --*

          Contains one or more identifiers of the Read Replicas associated with this DB instance.

          - *(string) --*

        - **ReadReplicaDBClusterIdentifiers** *(list) --*

          Contains one or more identifiers of DB clusters that are Read Replicas of this DB
          instance.

          - *(string) --*

        - **LicenseModel** *(string) --*

          License model information for this DB instance.

        - **Iops** *(integer) --*

          Specifies the Provisioned IOPS (I/O operations per second) value.

        - **OptionGroupMemberships** *(list) --*

          Provides the list of option group memberships for this DB instance.

          - *(dict) --*

            Provides information on the option groups the DB instance is a member of.

            - **OptionGroupName** *(string) --*

              The name of the option group that the instance belongs to.

            - **Status** *(string) --*

              The status of the DB instance's option group membership. Valid values are:
              ``in-sync`` , ``pending-apply`` , ``pending-removal`` , ``pending-maintenance-apply``
              , ``pending-maintenance-removal`` , ``applying`` , ``removing`` , and ``failed`` .

        - **CharacterSetName** *(string) --*

          If present, specifies the name of the character set that this instance is associated with.

        - **SecondaryAvailabilityZone** *(string) --*

          If present, specifies the name of the secondary Availability Zone for a DB instance with
          multi-AZ support.

        - **PubliclyAccessible** *(boolean) --*

          This flag should no longer be used.

        - **StatusInfos** *(list) --*

          The status of a Read Replica. If the instance is not a Read Replica, this is blank.

          - *(dict) --*

            Provides a list of status information for a DB instance.

            - **StatusType** *(string) --*

              This value is currently "read replication."

            - **Normal** *(boolean) --*

              Boolean value that is true if the instance is operating normally, or false if the
              instance is in an error state.

            - **Status** *(string) --*

              Status of the DB instance. For a StatusType of read replica, the values can be
              replicating, error, stopped, or terminated.

            - **Message** *(string) --*

              Details of the error if there is an error for the instance. If the instance is not in
              an error state, this value is blank.

        - **StorageType** *(string) --*

          Specifies the storage type associated with DB instance.

        - **TdeCredentialArn** *(string) --*

          The ARN from the key store with which the instance is associated for TDE encryption.

        - **DbInstancePort** *(integer) --*

          Specifies the port that the DB instance listens on. If the DB instance is part of a DB
          cluster, this can be a different port than the DB cluster port.

        - **DBClusterIdentifier** *(string) --*

          If the DB instance is a member of a DB cluster, contains the name of the DB cluster that
          the DB instance is a member of.

        - **StorageEncrypted** *(boolean) --*

          Not supported: The encryption for DB instances is managed by the DB cluster.

        - **KmsKeyId** *(string) --*

          Not supported: The encryption for DB instances is managed by the DB cluster.

        - **DbiResourceId** *(string) --*

          The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
          in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

        - **CACertificateIdentifier** *(string) --*

          The identifier of the CA certificate for this DB instance.

        - **DomainMemberships** *(list) --*

          Not supported

          - *(dict) --*

            An Active Directory Domain membership record associated with a DB instance.

            - **Domain** *(string) --*

              The identifier of the Active Directory Domain.

            - **Status** *(string) --*

              The status of the DB instance's Active Directory Domain membership, such as joined,
              pending-join, failed etc).

            - **FQDN** *(string) --*

              The fully qualified domain name of the Active Directory Domain.

            - **IAMRoleName** *(string) --*

              The name of the IAM role to be used when making API calls to the Directory Service.

        - **CopyTagsToSnapshot** *(boolean) --*

          Specifies whether tags are copied from the DB instance to snapshots of the DB instance.

        - **MonitoringInterval** *(integer) --*

          The interval, in seconds, between points when Enhanced Monitoring metrics are collected
          for the DB instance.

        - **EnhancedMonitoringResourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the
          Enhanced Monitoring metrics data for the DB instance.

        - **MonitoringRoleArn** *(string) --*

          The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to
          Amazon CloudWatch Logs.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which a Read Replica is promoted to the primary
          instance after a failure of the existing primary instance.

        - **DBInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB instance.

        - **Timezone** *(string) --*

          Not supported.

        - **IAMDatabaseAuthenticationEnabled** *(boolean) --*

          True if AWS Identity and Access Management (IAM) authentication is enabled, and otherwise
          false.

        - **PerformanceInsightsEnabled** *(boolean) --*

          True if Performance Insights is enabled for the DB instance, and otherwise false.

        - **PerformanceInsightsKMSKeyId** *(string) --*

          The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is
          the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS
          encryption key.

        - **EnabledCloudwatchLogsExports** *(list) --*

          A list of log types that this DB instance is configured to export to CloudWatch Logs.

          - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBParameterGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBParameterGroupsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeDBParameterGroupsPaginateFiltersTypeDef(
    _DescribeDBParameterGroupsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBParameterGroupsPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeDBParameterGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBParameterGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBParameterGroupsPaginatePaginationConfigTypeDef(
    _DescribeDBParameterGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBParameterGroupsPaginate` `PaginationConfig`

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


_DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef = TypedDict(
    "_DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)


class DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef(
    _DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef
):
    """
    Type definition for `DescribeDBParameterGroupsPaginateResponse` `DBParameterGroups`

    Contains the details of an Amazon Neptune DB parameter group.

    This data type is used as a response element in the  DescribeDBParameterGroups action.

    - **DBParameterGroupName** *(string) --*

      Provides the name of the DB parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB parameter group is
      compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB parameter group.

    - **DBParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB parameter group.
    """


_DescribeDBParameterGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBParameterGroupsPaginateResponseTypeDef",
    {
        "DBParameterGroups": List[
            DescribeDBParameterGroupsPaginateResponseDBParameterGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBParameterGroupsPaginateResponseTypeDef(
    _DescribeDBParameterGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBParameterGroupsPaginate` `Response`

    - **DBParameterGroups** *(list) --*

      A list of  DBParameterGroup instances.

      - *(dict) --*

        Contains the details of an Amazon Neptune DB parameter group.

        This data type is used as a response element in the  DescribeDBParameterGroups action.

        - **DBParameterGroupName** *(string) --*

          Provides the name of the DB parameter group.

        - **DBParameterGroupFamily** *(string) --*

          Provides the name of the DB parameter group family that this DB parameter group is
          compatible with.

        - **Description** *(string) --*

          Provides the customer-specified description for this DB parameter group.

        - **DBParameterGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB parameter group.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBParametersPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBParametersPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeDBParametersPaginateFiltersTypeDef(
    _DescribeDBParametersPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBParametersPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeDBParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBParametersPaginatePaginationConfigTypeDef(
    _DescribeDBParametersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBParametersPaginate` `PaginationConfig`

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


_DescribeDBParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeDBParametersPaginateResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class DescribeDBParametersPaginateResponseParametersTypeDef(
    _DescribeDBParametersPaginateResponseParametersTypeDef
):
    """
    Type definition for `DescribeDBParametersPaginateResponse` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_DescribeDBParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeDBParametersPaginateResponseTypeDef",
    {
        "Parameters": List[DescribeDBParametersPaginateResponseParametersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBParametersPaginateResponseTypeDef(
    _DescribeDBParametersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBParametersPaginate` `Response`

    - **Parameters** *(list) --*

      A list of  Parameter values.

      - *(dict) --*

        Specifies a parameter.

        - **ParameterName** *(string) --*

          Specifies the name of the parameter.

        - **ParameterValue** *(string) --*

          Specifies the value of the parameter.

        - **Description** *(string) --*

          Provides a description of the parameter.

        - **Source** *(string) --*

          Indicates the source of the parameter value.

        - **ApplyType** *(string) --*

          Specifies the engine specific parameters type.

        - **DataType** *(string) --*

          Specifies the valid data type for the parameter.

        - **AllowedValues** *(string) --*

          Specifies the valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest engine version to which the parameter can apply.

        - **ApplyMethod** *(string) --*

          Indicates when to apply parameter updates.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBSubnetGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeDBSubnetGroupsPaginateFiltersTypeDef(
    _DescribeDBSubnetGroupsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef(
    _DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginate` `PaginationConfig`

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


_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnets` `SubnetAvailabilityZone`

    Specifies the EC2 Availability Zone that the subnet is in.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginateResponseDBSubnetGroups` `Subnets`

    Specifies a subnet.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the EC2 Availability Zone that the subnet is in.

      - **Name** *(string) --*

        The name of the availability zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginateResponse` `DBSubnetGroups`

    Contains the details of an Amazon Neptune DB subnet group.

    This data type is used as a response element in the  DescribeDBSubnetGroups action.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the VpcId of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Contains a list of  Subnet elements.

      - *(dict) --*

        Specifies a subnet.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the EC2 Availability Zone that the subnet is in.

          - **Name** *(string) --*

            The name of the availability zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_DescribeDBSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseTypeDef",
    {
        "DBSubnetGroups": List[
            DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginate` `Response`

    - **DBSubnetGroups** *(list) --*

      A list of  DBSubnetGroup instances.

      - *(dict) --*

        Contains the details of an Amazon Neptune DB subnet group.

        This data type is used as a response element in the  DescribeDBSubnetGroups action.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the VpcId of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Contains a list of  Subnet elements.

          - *(dict) --*

            Specifies a subnet.

            This data type is used as a response element in the  DescribeDBSubnetGroups action.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the EC2 Availability Zone that the subnet is in.

              - **Name** *(string) --*

                The name of the availability zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeEngineDefaultParametersPaginateFiltersTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeEngineDefaultParametersPaginateFiltersTypeDef(
    _DescribeEngineDefaultParametersPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeEngineDefaultParametersPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef(
    _DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEngineDefaultParametersPaginate` `PaginationConfig`

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


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef
):
    """
    Type definition for `DescribeEngineDefaultParametersPaginateResponseEngineDefaults` `Parameters`

    Specifies a parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being
      changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef
        ],
    },
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef
):
    """
    Type definition for `DescribeEngineDefaultParametersPaginateResponse` `EngineDefaults`

    Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.

    - **DBParameterGroupFamily** *(string) --*

      Specifies the name of the DB parameter group family that the engine default parameters
      apply to.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous EngineDefaults request. If this
      parameter is specified, the response includes only records beyond the marker, up to the
      value specified by ``MaxRecords`` .

    - **Parameters** *(list) --*

      Contains a list of engine default parameters.

      - *(dict) --*

        Specifies a parameter.

        - **ParameterName** *(string) --*

          Specifies the name of the parameter.

        - **ParameterValue** *(string) --*

          Specifies the value of the parameter.

        - **Description** *(string) --*

          Provides a description of the parameter.

        - **Source** *(string) --*

          Indicates the source of the parameter value.

        - **ApplyType** *(string) --*

          Specifies the engine specific parameters type.

        - **DataType** *(string) --*

          Specifies the valid data type for the parameter.

        - **AllowedValues** *(string) --*

          Specifies the valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being
          changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest engine version to which the parameter can apply.

        - **ApplyMethod** *(string) --*

          Indicates when to apply parameter updates.
    """


_DescribeEngineDefaultParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseTypeDef",
    {
        "EngineDefaults": DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef,
        "NextToken": str,
    },
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEngineDefaultParametersPaginate` `Response`

    - **EngineDefaults** *(dict) --*

      Contains the result of a successful invocation of the  DescribeEngineDefaultParameters action.

      - **DBParameterGroupFamily** *(string) --*

        Specifies the name of the DB parameter group family that the engine default parameters
        apply to.

      - **Marker** *(string) --*

        An optional pagination token provided by a previous EngineDefaults request. If this
        parameter is specified, the response includes only records beyond the marker, up to the
        value specified by ``MaxRecords`` .

      - **Parameters** *(list) --*

        Contains a list of engine default parameters.

        - *(dict) --*

          Specifies a parameter.

          - **ParameterName** *(string) --*

            Specifies the name of the parameter.

          - **ParameterValue** *(string) --*

            Specifies the value of the parameter.

          - **Description** *(string) --*

            Provides a description of the parameter.

          - **Source** *(string) --*

            Indicates the source of the parameter value.

          - **ApplyType** *(string) --*

            Specifies the engine specific parameters type.

          - **DataType** *(string) --*

            Specifies the valid data type for the parameter.

          - **AllowedValues** *(string) --*

            Specifies the valid range of values for the parameter.

          - **IsModifiable** *(boolean) --*

            Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
            parameters have security or operational implications that prevent them from being
            changed.

          - **MinimumEngineVersion** *(string) --*

            The earliest engine version to which the parameter can apply.

          - **ApplyMethod** *(string) --*

            Indicates when to apply parameter updates.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeEventSubscriptionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeEventSubscriptionsPaginateFiltersTypeDef(
    _DescribeEventSubscriptionsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeEventSubscriptionsPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeEventSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventSubscriptionsPaginatePaginationConfigTypeDef(
    _DescribeEventSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEventSubscriptionsPaginate` `PaginationConfig`

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


_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)


class DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef(
    _DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef
):
    """
    Type definition for `DescribeEventSubscriptionsPaginateResponse` `EventSubscriptionsList`

    Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

    - **CustomerAwsId** *(string) --*

      The AWS customer account associated with the event notification subscription.

    - **CustSubscriptionId** *(string) --*

      The event notification subscription Id.

    - **SnsTopicArn** *(string) --*

      The topic ARN of the event notification subscription.

    - **Status** *(string) --*

      The status of the event notification subscription.

      Constraints:

      Can be one of the following: creating | modifying | deleting | active | no-permission |
      topic-not-exist

      The status "no-permission" indicates that Neptune no longer has permission to post to the
      SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
      subscription was created.

    - **SubscriptionCreationTime** *(string) --*

      The time the event notification subscription was created.

    - **SourceType** *(string) --*

      The source type for the event notification subscription.

    - **SourceIdsList** *(list) --*

      A list of source IDs for the event notification subscription.

      - *(string) --*

    - **EventCategoriesList** *(list) --*

      A list of event categories for the event notification subscription.

      - *(string) --*

    - **Enabled** *(boolean) --*

      A Boolean value indicating if the subscription is enabled. True indicates the
      subscription is enabled.

    - **EventSubscriptionArn** *(string) --*

      The Amazon Resource Name (ARN) for the event subscription.
    """


_DescribeEventSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventSubscriptionsPaginateResponseTypeDef",
    {
        "EventSubscriptionsList": List[
            DescribeEventSubscriptionsPaginateResponseEventSubscriptionsListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeEventSubscriptionsPaginateResponseTypeDef(
    _DescribeEventSubscriptionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEventSubscriptionsPaginate` `Response`

    - **EventSubscriptionsList** *(list) --*

      A list of EventSubscriptions data types.

      - *(dict) --*

        Contains the results of a successful invocation of the  DescribeEventSubscriptions action.

        - **CustomerAwsId** *(string) --*

          The AWS customer account associated with the event notification subscription.

        - **CustSubscriptionId** *(string) --*

          The event notification subscription Id.

        - **SnsTopicArn** *(string) --*

          The topic ARN of the event notification subscription.

        - **Status** *(string) --*

          The status of the event notification subscription.

          Constraints:

          Can be one of the following: creating | modifying | deleting | active | no-permission |
          topic-not-exist

          The status "no-permission" indicates that Neptune no longer has permission to post to the
          SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
          subscription was created.

        - **SubscriptionCreationTime** *(string) --*

          The time the event notification subscription was created.

        - **SourceType** *(string) --*

          The source type for the event notification subscription.

        - **SourceIdsList** *(list) --*

          A list of source IDs for the event notification subscription.

          - *(string) --*

        - **EventCategoriesList** *(list) --*

          A list of event categories for the event notification subscription.

          - *(string) --*

        - **Enabled** *(boolean) --*

          A Boolean value indicating if the subscription is enabled. True indicates the
          subscription is enabled.

        - **EventSubscriptionArn** *(string) --*

          The Amazon Resource Name (ARN) for the event subscription.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeEventsPaginateFiltersTypeDef = TypedDict(
    "_DescribeEventsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeEventsPaginateFiltersTypeDef(_DescribeEventsPaginateFiltersTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
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


_DescribeEventsPaginateResponseEventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(
    _DescribeEventsPaginateResponseEventsTypeDef
):
    """
    Type definition for `DescribeEventsPaginateResponse` `Events`

    This data type is used as a response element in the  DescribeEvents action.

    - **SourceIdentifier** *(string) --*

      Provides the identifier for the source of the event.

    - **SourceType** *(string) --*

      Specifies the source type for this event.

    - **Message** *(string) --*

      Provides the text of this event.

    - **EventCategories** *(list) --*

      Specifies the category for the event.

      - *(string) --*

    - **Date** *(datetime) --*

      Specifies the date and time of the event.

    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) for the event.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `Response`

    - **Events** *(list) --*

      A list of  Event instances.

      - *(dict) --*

        This data type is used as a response element in the  DescribeEvents action.

        - **SourceIdentifier** *(string) --*

          Provides the identifier for the source of the event.

        - **SourceType** *(string) --*

          Specifies the source type for this event.

        - **Message** *(string) --*

          Provides the text of this event.

        - **EventCategories** *(list) --*

          Specifies the category for the event.

          - *(string) --*

        - **Date** *(datetime) --*

          Specifies the date and time of the event.

        - **SourceArn** *(string) --*

          The Amazon Resource Name (ARN) for the event.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeOrderableDBInstanceOptionsPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeOrderableDBInstanceOptionsPaginate` `PaginationConfig`

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


_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
):
    """
    Type definition for `DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptions` `AvailabilityZones`

    Specifies an Availability Zone.

    - **Name** *(string) --*

      The name of the availability zone.
    """


_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List[
            DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
        ],
        "MultiAZCapable": bool,
        "ReadReplicaCapable": bool,
        "Vpc": bool,
        "SupportsStorageEncryption": bool,
        "StorageType": str,
        "SupportsIops": bool,
        "SupportsEnhancedMonitoring": bool,
        "SupportsIAMDatabaseAuthentication": bool,
        "SupportsPerformanceInsights": bool,
        "MinStorageSize": int,
        "MaxStorageSize": int,
        "MinIopsPerDbInstance": int,
        "MaxIopsPerDbInstance": int,
        "MinIopsPerGib": float,
        "MaxIopsPerGib": float,
    },
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef
):
    """
    Type definition for `DescribeOrderableDBInstanceOptionsPaginateResponse` `OrderableDBInstanceOptions`

    Contains a list of available options for a DB instance.

    This data type is used as a response element in the  DescribeOrderableDBInstanceOptions
    action.

    - **Engine** *(string) --*

      The engine type of a DB instance.

    - **EngineVersion** *(string) --*

      The engine version of a DB instance.

    - **DBInstanceClass** *(string) --*

      The DB instance class for a DB instance.

    - **LicenseModel** *(string) --*

      The license model for a DB instance.

    - **AvailabilityZones** *(list) --*

      A list of Availability Zones for a DB instance.

      - *(dict) --*

        Specifies an Availability Zone.

        - **Name** *(string) --*

          The name of the availability zone.

    - **MultiAZCapable** *(boolean) --*

      Indicates whether a DB instance is Multi-AZ capable.

    - **ReadReplicaCapable** *(boolean) --*

      Indicates whether a DB instance can have a Read Replica.

    - **Vpc** *(boolean) --*

      Indicates whether a DB instance is in a VPC.

    - **SupportsStorageEncryption** *(boolean) --*

      Indicates whether a DB instance supports encrypted storage.

    - **StorageType** *(string) --*

      Indicates the storage type for a DB instance.

    - **SupportsIops** *(boolean) --*

      Indicates whether a DB instance supports provisioned IOPS.

    - **SupportsEnhancedMonitoring** *(boolean) --*

      Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60
      seconds.

    - **SupportsIAMDatabaseAuthentication** *(boolean) --*

      Indicates whether a DB instance supports IAM database authentication.

    - **SupportsPerformanceInsights** *(boolean) --*

      True if a DB instance supports Performance Insights, otherwise false.

    - **MinStorageSize** *(integer) --*

      Minimum storage size for a DB instance.

    - **MaxStorageSize** *(integer) --*

      Maximum storage size for a DB instance.

    - **MinIopsPerDbInstance** *(integer) --*

      Minimum total provisioned IOPS for a DB instance.

    - **MaxIopsPerDbInstance** *(integer) --*

      Maximum total provisioned IOPS for a DB instance.

    - **MinIopsPerGib** *(float) --*

      Minimum provisioned IOPS per GiB for a DB instance.

    - **MaxIopsPerGib** *(float) --*

      Maximum provisioned IOPS per GiB for a DB instance.
    """


_DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef",
    {
        "OrderableDBInstanceOptions": List[
            DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeOrderableDBInstanceOptionsPaginate` `Response`

    - **OrderableDBInstanceOptions** *(list) --*

      An  OrderableDBInstanceOption structure containing information about orderable options for
      the DB instance.

      - *(dict) --*

        Contains a list of available options for a DB instance.

        This data type is used as a response element in the  DescribeOrderableDBInstanceOptions
        action.

        - **Engine** *(string) --*

          The engine type of a DB instance.

        - **EngineVersion** *(string) --*

          The engine version of a DB instance.

        - **DBInstanceClass** *(string) --*

          The DB instance class for a DB instance.

        - **LicenseModel** *(string) --*

          The license model for a DB instance.

        - **AvailabilityZones** *(list) --*

          A list of Availability Zones for a DB instance.

          - *(dict) --*

            Specifies an Availability Zone.

            - **Name** *(string) --*

              The name of the availability zone.

        - **MultiAZCapable** *(boolean) --*

          Indicates whether a DB instance is Multi-AZ capable.

        - **ReadReplicaCapable** *(boolean) --*

          Indicates whether a DB instance can have a Read Replica.

        - **Vpc** *(boolean) --*

          Indicates whether a DB instance is in a VPC.

        - **SupportsStorageEncryption** *(boolean) --*

          Indicates whether a DB instance supports encrypted storage.

        - **StorageType** *(string) --*

          Indicates the storage type for a DB instance.

        - **SupportsIops** *(boolean) --*

          Indicates whether a DB instance supports provisioned IOPS.

        - **SupportsEnhancedMonitoring** *(boolean) --*

          Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60
          seconds.

        - **SupportsIAMDatabaseAuthentication** *(boolean) --*

          Indicates whether a DB instance supports IAM database authentication.

        - **SupportsPerformanceInsights** *(boolean) --*

          True if a DB instance supports Performance Insights, otherwise false.

        - **MinStorageSize** *(integer) --*

          Minimum storage size for a DB instance.

        - **MaxStorageSize** *(integer) --*

          Maximum storage size for a DB instance.

        - **MinIopsPerDbInstance** *(integer) --*

          Minimum total provisioned IOPS for a DB instance.

        - **MaxIopsPerDbInstance** *(integer) --*

          Maximum total provisioned IOPS for a DB instance.

        - **MinIopsPerGib** *(float) --*

          Minimum provisioned IOPS per GiB for a DB instance.

        - **MaxIopsPerGib** *(float) --*

          Maximum provisioned IOPS per GiB for a DB instance.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribePendingMaintenanceActionsPaginateFiltersTypeDef = TypedDict(
    "_DescribePendingMaintenanceActionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribePendingMaintenanceActionsPaginateFiltersTypeDef(
    _DescribePendingMaintenanceActionsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribePendingMaintenanceActionsPaginate` `Filters`

    This type is not currently supported.

    - **Name** *(string) --* **[REQUIRED]**

      This parameter is not currently supported.

    - **Values** *(list) --* **[REQUIRED]**

      This parameter is not currently supported.

      - *(string) --*
    """


_DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef(
    _DescribePendingMaintenanceActionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribePendingMaintenanceActionsPaginate` `PaginationConfig`

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


_DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)


class DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    """
    Type definition for `DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActions` `PendingMaintenanceActionDetails`

    Provides information about a pending maintenance action for a resource.

    - **Action** *(string) --*

      The type of pending maintenance action that is available for the resource.

    - **AutoAppliedAfterDate** *(datetime) --*

      The date of the maintenance window when the action is applied. The maintenance action
      is applied to the resource during its first maintenance window after this date. If
      this date is specified, any ``next-maintenance`` opt-in requests are ignored.

    - **ForcedApplyDate** *(datetime) --*

      The date when the maintenance action is automatically applied. The maintenance action
      is applied to the resource on this date regardless of the maintenance window for the
      resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

    - **OptInStatus** *(string) --*

      Indicates the type of opt-in request that has been received for the resource.

    - **CurrentApplyDate** *(datetime) --*

      The effective date when the pending maintenance action is applied to the resource.
      This date takes into account opt-in requests received from the
      ApplyPendingMaintenanceAction API, the ``AutoAppliedAfterDate`` , and the
      ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
      and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

    - **Description** *(string) --*

      A description providing more detail about the maintenance action.
    """


_DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef = TypedDict(
    "_DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef(
    _DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef
):
    """
    Type definition for `DescribePendingMaintenanceActionsPaginateResponse` `PendingMaintenanceActions`

    Describes the pending maintenance actions for a resource.

    - **ResourceIdentifier** *(string) --*

      The ARN of the resource that has pending maintenance actions.

    - **PendingMaintenanceActionDetails** *(list) --*

      A list that provides details about the pending maintenance actions for the resource.

      - *(dict) --*

        Provides information about a pending maintenance action for a resource.

        - **Action** *(string) --*

          The type of pending maintenance action that is available for the resource.

        - **AutoAppliedAfterDate** *(datetime) --*

          The date of the maintenance window when the action is applied. The maintenance action
          is applied to the resource during its first maintenance window after this date. If
          this date is specified, any ``next-maintenance`` opt-in requests are ignored.

        - **ForcedApplyDate** *(datetime) --*

          The date when the maintenance action is automatically applied. The maintenance action
          is applied to the resource on this date regardless of the maintenance window for the
          resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

        - **OptInStatus** *(string) --*

          Indicates the type of opt-in request that has been received for the resource.

        - **CurrentApplyDate** *(datetime) --*

          The effective date when the pending maintenance action is applied to the resource.
          This date takes into account opt-in requests received from the
          ApplyPendingMaintenanceAction API, the ``AutoAppliedAfterDate`` , and the
          ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
          and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

        - **Description** *(string) --*

          A description providing more detail about the maintenance action.
    """


_DescribePendingMaintenanceActionsPaginateResponseTypeDef = TypedDict(
    "_DescribePendingMaintenanceActionsPaginateResponseTypeDef",
    {
        "PendingMaintenanceActions": List[
            DescribePendingMaintenanceActionsPaginateResponsePendingMaintenanceActionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribePendingMaintenanceActionsPaginateResponseTypeDef(
    _DescribePendingMaintenanceActionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribePendingMaintenanceActionsPaginate` `Response`

    - **PendingMaintenanceActions** *(list) --*

      A list of the pending maintenance actions for the resource.

      - *(dict) --*

        Describes the pending maintenance actions for a resource.

        - **ResourceIdentifier** *(string) --*

          The ARN of the resource that has pending maintenance actions.

        - **PendingMaintenanceActionDetails** *(list) --*

          A list that provides details about the pending maintenance actions for the resource.

          - *(dict) --*

            Provides information about a pending maintenance action for a resource.

            - **Action** *(string) --*

              The type of pending maintenance action that is available for the resource.

            - **AutoAppliedAfterDate** *(datetime) --*

              The date of the maintenance window when the action is applied. The maintenance action
              is applied to the resource during its first maintenance window after this date. If
              this date is specified, any ``next-maintenance`` opt-in requests are ignored.

            - **ForcedApplyDate** *(datetime) --*

              The date when the maintenance action is automatically applied. The maintenance action
              is applied to the resource on this date regardless of the maintenance window for the
              resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

            - **OptInStatus** *(string) --*

              Indicates the type of opt-in request that has been received for the resource.

            - **CurrentApplyDate** *(datetime) --*

              The effective date when the pending maintenance action is applied to the resource.
              This date takes into account opt-in requests received from the
              ApplyPendingMaintenanceAction API, the ``AutoAppliedAfterDate`` , and the
              ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
              and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

            - **Description** *(string) --*

              A description providing more detail about the maintenance action.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
