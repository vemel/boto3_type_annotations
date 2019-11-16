"Main interface for elasticache type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "CacheClusterAvailableWaitWaiterConfigTypeDef",
    "CacheClusterDeletedWaitWaiterConfigTypeDef",
    "ClientAddTagsToResourceResponseTagListTypeDef",
    "ClientAddTagsToResourceResponseTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    "ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef",
    "ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef",
    "ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    "ClientBatchApplyUpdateActionResponseTypeDef",
    "ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef",
    "ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    "ClientBatchStopUpdateActionResponseTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientCompleteMigrationResponseReplicationGroupTypeDef",
    "ClientCompleteMigrationResponseTypeDef",
    "ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef",
    "ClientCopySnapshotResponseSnapshotTypeDef",
    "ClientCopySnapshotResponseTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientCreateCacheClusterResponseCacheClusterTypeDef",
    "ClientCreateCacheClusterResponseTypeDef",
    "ClientCreateCacheClusterTagsTypeDef",
    "ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef",
    "ClientCreateCacheParameterGroupResponseTypeDef",
    "ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef",
    "ClientCreateCacheSecurityGroupResponseTypeDef",
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    "ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    "ClientCreateCacheSubnetGroupResponseTypeDef",
    "ClientCreateReplicationGroupNodeGroupConfigurationTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientCreateReplicationGroupResponseReplicationGroupTypeDef",
    "ClientCreateReplicationGroupResponseTypeDef",
    "ClientCreateReplicationGroupTagsTypeDef",
    "ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    "ClientCreateSnapshotResponseSnapshotTypeDef",
    "ClientCreateSnapshotResponseTypeDef",
    "ClientDecreaseReplicaCountReplicaConfigurationTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientDecreaseReplicaCountResponseReplicationGroupTypeDef",
    "ClientDecreaseReplicaCountResponseTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientDeleteCacheClusterResponseCacheClusterTypeDef",
    "ClientDeleteCacheClusterResponseTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientDeleteReplicationGroupResponseReplicationGroupTypeDef",
    "ClientDeleteReplicationGroupResponseTypeDef",
    "ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    "ClientDeleteSnapshotResponseSnapshotTypeDef",
    "ClientDeleteSnapshotResponseTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef",
    "ClientDescribeCacheClustersResponseCacheClustersTypeDef",
    "ClientDescribeCacheClustersResponseTypeDef",
    "ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef",
    "ClientDescribeCacheEngineVersionsResponseTypeDef",
    "ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef",
    "ClientDescribeCacheParameterGroupsResponseTypeDef",
    "ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    "ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef",
    "ClientDescribeCacheParametersResponseParametersTypeDef",
    "ClientDescribeCacheParametersResponseTypeDef",
    "ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    "ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef",
    "ClientDescribeCacheSecurityGroupsResponseTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef",
    "ClientDescribeCacheSubnetGroupsResponseTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultParametersResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef",
    "ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef",
    "ClientDescribeReplicationGroupsResponseTypeDef",
    "ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    "ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef",
    "ClientDescribeReservedCacheNodesOfferingsResponseTypeDef",
    "ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef",
    "ClientDescribeServiceUpdatesResponseTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    "ClientDescribeSnapshotsResponseTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    "ClientDescribeUpdateActionsResponseUpdateActionsTypeDef",
    "ClientDescribeUpdateActionsResponseTypeDef",
    "ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef",
    "ClientIncreaseReplicaCountReplicaConfigurationTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientIncreaseReplicaCountResponseReplicationGroupTypeDef",
    "ClientIncreaseReplicaCountResponseTypeDef",
    "ClientListAllowedNodeTypeModificationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientModifyCacheClusterResponseCacheClusterTypeDef",
    "ClientModifyCacheClusterResponseTypeDef",
    "ClientModifyCacheParameterGroupParameterNameValuesTypeDef",
    "ClientModifyCacheParameterGroupResponseTypeDef",
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    "ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    "ClientModifyCacheSubnetGroupResponseTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientModifyReplicationGroupResponseReplicationGroupTypeDef",
    "ClientModifyReplicationGroupResponseTypeDef",
    "ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef",
    "ClientModifyReplicationGroupShardConfigurationResponseTypeDef",
    "ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef",
    "ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef",
    "ClientPurchaseReservedCacheNodesOfferingResponseTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    "ClientRebootCacheClusterResponseCacheClusterTypeDef",
    "ClientRebootCacheClusterResponseTypeDef",
    "ClientRemoveTagsFromResourceResponseTagListTypeDef",
    "ClientRemoveTagsFromResourceResponseTypeDef",
    "ClientResetCacheParameterGroupParameterNameValuesTypeDef",
    "ClientResetCacheParameterGroupResponseTypeDef",
    "ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    "ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    "ClientRevokeCacheSecurityGroupIngressResponseTypeDef",
    "ClientStartMigrationCustomerNodeEndpointListTypeDef",
    "ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef",
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientStartMigrationResponseReplicationGroupTypeDef",
    "ClientStartMigrationResponseTypeDef",
    "ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    "ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef",
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    "ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef",
    "ClientTestFailoverResponseReplicationGroupTypeDef",
    "ClientTestFailoverResponseTypeDef",
    "DescribeCacheClustersPaginatePaginationConfigTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef",
    "DescribeCacheClustersPaginateResponseCacheClustersTypeDef",
    "DescribeCacheClustersPaginateResponseTypeDef",
    "DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef",
    "DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef",
    "DescribeCacheEngineVersionsPaginateResponseTypeDef",
    "DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef",
    "DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef",
    "DescribeCacheParameterGroupsPaginateResponseTypeDef",
    "DescribeCacheParametersPaginatePaginationConfigTypeDef",
    "DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    "DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef",
    "DescribeCacheParametersPaginateResponseParametersTypeDef",
    "DescribeCacheParametersPaginateResponseTypeDef",
    "DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef",
    "DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    "DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef",
    "DescribeCacheSecurityGroupsPaginateResponseTypeDef",
    "DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef",
    "DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef",
    "DescribeCacheSubnetGroupsPaginateResponseTypeDef",
    "DescribeEngineDefaultParametersPaginatePaginationConfigTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef",
    "DescribeEngineDefaultParametersPaginateResponseTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeReplicationGroupsPaginatePaginationConfigTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef",
    "DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef",
    "DescribeReplicationGroupsPaginateResponseTypeDef",
    "DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef",
    "DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    "DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef",
    "DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef",
    "DescribeReservedCacheNodesPaginatePaginationConfigTypeDef",
    "DescribeServiceUpdatesPaginatePaginationConfigTypeDef",
    "DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef",
    "DescribeServiceUpdatesPaginateResponseTypeDef",
    "DescribeSnapshotsPaginatePaginationConfigTypeDef",
    "DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    "DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef",
    "DescribeSnapshotsPaginateResponseSnapshotsTypeDef",
    "DescribeSnapshotsPaginateResponseTypeDef",
    "DescribeUpdateActionsPaginatePaginationConfigTypeDef",
    "DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
    "DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
    "DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    "DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef",
    "DescribeUpdateActionsPaginateResponseTypeDef",
    "DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef",
    "ReplicationGroupAvailableWaitWaiterConfigTypeDef",
    "ReplicationGroupDeletedWaitWaiterConfigTypeDef",
)


_CacheClusterAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_CacheClusterAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class CacheClusterAvailableWaitWaiterConfigTypeDef(
    _CacheClusterAvailableWaitWaiterConfigTypeDef
):
    """
    Type definition for `CacheClusterAvailableWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_CacheClusterDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_CacheClusterDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class CacheClusterDeletedWaitWaiterConfigTypeDef(
    _CacheClusterDeletedWaitWaiterConfigTypeDef
):
    """
    Type definition for `CacheClusterDeletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_ClientAddTagsToResourceResponseTagListTypeDef = TypedDict(
    "_ClientAddTagsToResourceResponseTagListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientAddTagsToResourceResponseTagListTypeDef(
    _ClientAddTagsToResourceResponseTagListTypeDef
):
    """
    Type definition for `ClientAddTagsToResourceResponse` `TagList`

    A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
    Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

    - **Key** *(string) --*

      The key for the tag. May not be null.

    - **Value** *(string) --*

      The tag's value. May be null.
    """


_ClientAddTagsToResourceResponseTypeDef = TypedDict(
    "_ClientAddTagsToResourceResponseTypeDef",
    {"TagList": List[ClientAddTagsToResourceResponseTagListTypeDef]},
    total=False,
)


class ClientAddTagsToResourceResponseTypeDef(_ClientAddTagsToResourceResponseTypeDef):
    """
    Type definition for `ClientAddTagsToResource` `Response`

    Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and
    ``RemoveTagsFromResource`` operations.

    - **TagList** *(list) --*

      A list of cost allocation tags as key-value pairs.

      - *(dict) --*

        A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
        Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

        - **Key** *(string) --*

          The key for the tag. May not be null.

        - **Value** *(string) --*

          The tag's value. May be null.
    """


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    Type definition for `ClientAddTagsToResource` `Tags`

    A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
    are composed of a Key/Value pair. A tag with a null Value is permitted.

    - **Key** *(string) --*

      The key for the tag. May not be null.

    - **Value** *(string) --*

      The tag's value. May be null.
    """


_ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)


class ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
):
    """
    Type definition for `ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroup` `EC2SecurityGroups`

    Provides ownership and status information for an Amazon EC2 security group.

    - **Status** *(string) --*

      The status of the Amazon EC2 security group.

    - **EC2SecurityGroupName** *(string) --*

      The name of the Amazon EC2 security group.

    - **EC2SecurityGroupOwnerId** *(string) --*

      The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef = TypedDict(
    "_ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef(
    _ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef
):
    """
    Type definition for `ClientAuthorizeCacheSecurityGroupIngressResponse` `CacheSecurityGroup`

    Represents the output of one of the following operations:

    * ``AuthorizeCacheSecurityGroupIngress``

    * ``CreateCacheSecurityGroup``

    * ``RevokeCacheSecurityGroupIngress``

    - **OwnerId** *(string) --*

      The AWS account ID of the cache security group owner.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Description** *(string) --*

      The description of the cache security group.

    - **EC2SecurityGroups** *(list) --*

      A list of Amazon EC2 security groups that are associated with this cache security group.

      - *(dict) --*

        Provides ownership and status information for an Amazon EC2 security group.

        - **Status** *(string) --*

          The status of the Amazon EC2 security group.

        - **EC2SecurityGroupName** *(string) --*

          The name of the Amazon EC2 security group.

        - **EC2SecurityGroupOwnerId** *(string) --*

          The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef = TypedDict(
    "_ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef",
    {
        "CacheSecurityGroup": ClientAuthorizeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef
    },
    total=False,
)


class ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef(
    _ClientAuthorizeCacheSecurityGroupIngressResponseTypeDef
):
    """
    Type definition for `ClientAuthorizeCacheSecurityGroupIngress` `Response`

    - **CacheSecurityGroup** *(dict) --*

      Represents the output of one of the following operations:

      * ``AuthorizeCacheSecurityGroupIngress``

      * ``CreateCacheSecurityGroup``

      * ``RevokeCacheSecurityGroupIngress``

      - **OwnerId** *(string) --*

        The AWS account ID of the cache security group owner.

      - **CacheSecurityGroupName** *(string) --*

        The name of the cache security group.

      - **Description** *(string) --*

        The description of the cache security group.

      - **EC2SecurityGroups** *(list) --*

        A list of Amazon EC2 security groups that are associated with this cache security group.

        - *(dict) --*

          Provides ownership and status information for an Amazon EC2 security group.

          - **Status** *(string) --*

            The status of the Amazon EC2 security group.

          - **EC2SecurityGroupName** *(string) --*

            The name of the Amazon EC2 security group.

          - **EC2SecurityGroupOwnerId** *(string) --*

            The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef = TypedDict(
    "_ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "UpdateActionStatus": str,
    },
    total=False,
)


class ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef(
    _ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef
):
    """
    Type definition for `ClientBatchApplyUpdateActionResponse` `ProcessedUpdateActions`

    Update action that has been processed for the corresponding apply/stop request

    - **ReplicationGroupId** *(string) --*

      The ID of the replication group

    - **CacheClusterId** *(string) --*

      The ID of the cache cluster

    - **ServiceUpdateName** *(string) --*

      The unique ID of the service update

    - **UpdateActionStatus** *(string) --*

      The status of the update action on the Redis cluster
    """


_ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef = TypedDict(
    "_ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef(
    _ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef
):
    """
    Type definition for `ClientBatchApplyUpdateActionResponse` `UnprocessedUpdateActions`

    Update action that has failed to be processed for the corresponding apply/stop request

    - **ReplicationGroupId** *(string) --*

      The replication group ID

    - **CacheClusterId** *(string) --*

      The ID of the cache cluster

    - **ServiceUpdateName** *(string) --*

      The unique ID of the service update

    - **ErrorType** *(string) --*

      The error type for requests that are not processed

    - **ErrorMessage** *(string) --*

      The error message that describes the reason the request was not processed
    """


_ClientBatchApplyUpdateActionResponseTypeDef = TypedDict(
    "_ClientBatchApplyUpdateActionResponseTypeDef",
    {
        "ProcessedUpdateActions": List[
            ClientBatchApplyUpdateActionResponseProcessedUpdateActionsTypeDef
        ],
        "UnprocessedUpdateActions": List[
            ClientBatchApplyUpdateActionResponseUnprocessedUpdateActionsTypeDef
        ],
    },
    total=False,
)


class ClientBatchApplyUpdateActionResponseTypeDef(
    _ClientBatchApplyUpdateActionResponseTypeDef
):
    """
    Type definition for `ClientBatchApplyUpdateAction` `Response`

    - **ProcessedUpdateActions** *(list) --*

      Update actions that have been processed successfully

      - *(dict) --*

        Update action that has been processed for the corresponding apply/stop request

        - **ReplicationGroupId** *(string) --*

          The ID of the replication group

        - **CacheClusterId** *(string) --*

          The ID of the cache cluster

        - **ServiceUpdateName** *(string) --*

          The unique ID of the service update

        - **UpdateActionStatus** *(string) --*

          The status of the update action on the Redis cluster

    - **UnprocessedUpdateActions** *(list) --*

      Update actions that haven't been processed successfully

      - *(dict) --*

        Update action that has failed to be processed for the corresponding apply/stop request

        - **ReplicationGroupId** *(string) --*

          The replication group ID

        - **CacheClusterId** *(string) --*

          The ID of the cache cluster

        - **ServiceUpdateName** *(string) --*

          The unique ID of the service update

        - **ErrorType** *(string) --*

          The error type for requests that are not processed

        - **ErrorMessage** *(string) --*

          The error message that describes the reason the request was not processed
    """


_ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef = TypedDict(
    "_ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "UpdateActionStatus": str,
    },
    total=False,
)


class ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef(
    _ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef
):
    """
    Type definition for `ClientBatchStopUpdateActionResponse` `ProcessedUpdateActions`

    Update action that has been processed for the corresponding apply/stop request

    - **ReplicationGroupId** *(string) --*

      The ID of the replication group

    - **CacheClusterId** *(string) --*

      The ID of the cache cluster

    - **ServiceUpdateName** *(string) --*

      The unique ID of the service update

    - **UpdateActionStatus** *(string) --*

      The status of the update action on the Redis cluster
    """


_ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef = TypedDict(
    "_ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef(
    _ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef
):
    """
    Type definition for `ClientBatchStopUpdateActionResponse` `UnprocessedUpdateActions`

    Update action that has failed to be processed for the corresponding apply/stop request

    - **ReplicationGroupId** *(string) --*

      The replication group ID

    - **CacheClusterId** *(string) --*

      The ID of the cache cluster

    - **ServiceUpdateName** *(string) --*

      The unique ID of the service update

    - **ErrorType** *(string) --*

      The error type for requests that are not processed

    - **ErrorMessage** *(string) --*

      The error message that describes the reason the request was not processed
    """


_ClientBatchStopUpdateActionResponseTypeDef = TypedDict(
    "_ClientBatchStopUpdateActionResponseTypeDef",
    {
        "ProcessedUpdateActions": List[
            ClientBatchStopUpdateActionResponseProcessedUpdateActionsTypeDef
        ],
        "UnprocessedUpdateActions": List[
            ClientBatchStopUpdateActionResponseUnprocessedUpdateActionsTypeDef
        ],
    },
    total=False,
)


class ClientBatchStopUpdateActionResponseTypeDef(
    _ClientBatchStopUpdateActionResponseTypeDef
):
    """
    Type definition for `ClientBatchStopUpdateAction` `Response`

    - **ProcessedUpdateActions** *(list) --*

      Update actions that have been processed successfully

      - *(dict) --*

        Update action that has been processed for the corresponding apply/stop request

        - **ReplicationGroupId** *(string) --*

          The ID of the replication group

        - **CacheClusterId** *(string) --*

          The ID of the cache cluster

        - **ServiceUpdateName** *(string) --*

          The unique ID of the service update

        - **UpdateActionStatus** *(string) --*

          The status of the update action on the Redis cluster

    - **UnprocessedUpdateActions** *(list) --*

      Update actions that haven't been processed successfully

      - *(dict) --*

        Update action that has failed to be processed for the corresponding apply/stop request

        - **ReplicationGroupId** *(string) --*

          The replication group ID

        - **CacheClusterId** *(string) --*

          The ID of the cache cluster

        - **ServiceUpdateName** *(string) --*

          The unique ID of the service update

        - **ErrorType** *(string) --*

          The error type for requests that are not processed

        - **ErrorMessage** *(string) --*

          The error message that describes the reason the request was not processed
    """


_ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientCompleteMigrationResponseReplicationGroup` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `ClientCompleteMigrationResponseReplicationGroupNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` . This
      member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `ClientCompleteMigrationResponseReplicationGroupNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `ClientCompleteMigrationResponseReplicationGroupNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientCompleteMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientCompleteMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientCompleteMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef
):
    """
    Type definition for `ClientCompleteMigrationResponseReplicationGroup` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node group
    is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled) replication
      group contains only 1 node group; therefore, the node group ID is 0001. A Redis
      (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
      0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` . This
          member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `ClientCompleteMigrationResponseReplicationGroupPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientCompleteMigrationResponseReplicationGroup` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientCompleteMigrationResponseReplicationGroupTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientCompleteMigrationResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientCompleteMigrationResponseReplicationGroupNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": ClientCompleteMigrationResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientCompleteMigrationResponseReplicationGroupTypeDef(
    _ClientCompleteMigrationResponseReplicationGroupTypeDef
):
    """
    Type definition for `ClientCompleteMigrationResponse` `ReplicationGroup`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , ``modifying``
      , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node group
        is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled) replication
          group contains only 1 node group; therefore, the node group ID is 0001. A Redis
          (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
          0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` . This
              member is only applicable for Redis (cluster mode disabled) replication groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
      range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientCompleteMigrationResponseTypeDef = TypedDict(
    "_ClientCompleteMigrationResponseTypeDef",
    {"ReplicationGroup": ClientCompleteMigrationResponseReplicationGroupTypeDef},
    total=False,
)


class ClientCompleteMigrationResponseTypeDef(_ClientCompleteMigrationResponseTypeDef):
    """
    Type definition for `ClientCompleteMigration` `Response`

    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.

      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.

      - **Description** *(string) --*

        The user supplied description of the replication group.

      - **Status** *(string) --*

        The current state of this replication group - ``creating`` , ``available`` , ``modifying``
        , ``deleting`` , ``create-failed`` , ``snapshotting`` .

      - **PendingModifiedValues** *(dict) --*

        A group of settings to be applied to the replication group, either immediately or during
        the next maintenance window.

        - **PrimaryClusterId** *(string) --*

          The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
          specified), or during the next maintenance window.

        - **AutomaticFailoverStatus** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **Resharding** *(dict) --*

          The status of an online resharding operation.

          - **SlotMigration** *(dict) --*

            Represents the progress of an online resharding operation.

            - **ProgressPercentage** *(float) --*

              The percentage of the slot migration that is complete.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **MemberClusters** *(list) --*

        The names of all the cache clusters that are part of this replication group.

        - *(string) --*

      - **NodeGroups** *(list) --*

        A list of node groups in this replication group. For Redis (cluster mode disabled)
        replication groups, this is a single-element list. For Redis (cluster mode enabled)
        replication groups, the list contains an entry for each node group (shard).

        - *(dict) --*

          Represents a collection of cache nodes in a replication group. One node in the node group
          is the read/write primary node. All the other nodes are read-only Replica nodes.

          - **NodeGroupId** *(string) --*

            The identifier for the node group (shard). A Redis (cluster mode disabled) replication
            group contains only 1 node group; therefore, the node group ID is 0001. A Redis
            (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
            0090. Optionally, the user can provide the id for a node group.

          - **Status** *(string) --*

            The current state of this replication group - ``creating`` , ``available`` , etc.

          - **PrimaryEndpoint** *(dict) --*

            The endpoint of the primary node in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ReaderEndpoint** *(dict) --*

            The endpoint of the replica nodes in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **Slots** *(string) --*

            The keyspace for this node group (shard).

          - **NodeGroupMembers** *(list) --*

            A list containing information about individual nodes within the node group (shard).

            - *(dict) --*

              Represents a single node within a node group (shard).

              - **CacheClusterId** *(string) --*

                The ID of the cluster to which the node belongs.

              - **CacheNodeId** *(string) --*

                The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                0002, etc.).

              - **ReadEndpoint** *(dict) --*

                The information required for client programs to connect to a node for read
                operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                clusters.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the node is located.

              - **CurrentRole** *(string) --*

                The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                member is only applicable for Redis (cluster mode disabled) replication groups.

      - **SnapshottingClusterId** *(string) --*

        The cluster ID that is used as the daily snapshot source for the replication group.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **ConfigurationEndpoint** *(dict) --*

        The configuration endpoint for this replication group. Use the configuration endpoint to
        connect to this replication group.

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
        range.

        .. note::

          This parameter is only valid if the ``Engine`` parameter is ``redis`` .

      - **ClusterEnabled** *(boolean) --*

        A flag indicating whether or not this replication group is cluster enabled; i.e., whether
        its data can be partitioned across multiple shards (API/CLI: node groups).

        Valid values: ``true`` | ``false``

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for each node in the replication
        group.

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "_ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef(
    _ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef
):
    """
    Type definition for `ClientCopySnapshotResponseSnapshotNodeSnapshots` `NodeGroupConfiguration`

    The configuration for the source node group (shard).

    - **NodeGroupId** *(string) --*

      Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
      node group these configuration values apply to.

    - **Slots** *(string) --*

      A string that specifies the keyspace for a particular node group. Keyspaces range
      from 0 to 16,383. The string is in the format ``startkey-endkey`` .

      Example: ``"0-3999"``

    - **ReplicaCount** *(integer) --*

      The number of read replica nodes in this node group (shard).

    - **PrimaryAvailabilityZone** *(string) --*

      The Availability Zone where the primary node of this node group (shard) is launched.

    - **ReplicaAvailabilityZones** *(list) --*

      A list of Availability Zones to be used for the read replicas. The number of
      Availability Zones in this list must match the value of ``ReplicaCount`` or
      ``ReplicasPerNodeGroup`` if not specified.

      - *(string) --*
    """


_ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "_ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientCopySnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)


class ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef(
    _ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef
):
    """
    Type definition for `ClientCopySnapshotResponseSnapshot` `NodeSnapshots`

    Represents an individual cache node in a snapshot of a cluster.

    - **CacheClusterId** *(string) --*

      A unique identifier for the source cluster.

    - **NodeGroupId** *(string) --*

      A unique identifier for the source node group (shard).

    - **CacheNodeId** *(string) --*

      The cache node identifier for the node in the source cluster.

    - **NodeGroupConfiguration** *(dict) --*

      The configuration for the source node group (shard).

      - **NodeGroupId** *(string) --*

        Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
        node group these configuration values apply to.

      - **Slots** *(string) --*

        A string that specifies the keyspace for a particular node group. Keyspaces range
        from 0 to 16,383. The string is in the format ``startkey-endkey`` .

        Example: ``"0-3999"``

      - **ReplicaCount** *(integer) --*

        The number of read replica nodes in this node group (shard).

      - **PrimaryAvailabilityZone** *(string) --*

        The Availability Zone where the primary node of this node group (shard) is launched.

      - **ReplicaAvailabilityZones** *(list) --*

        A list of Availability Zones to be used for the read replicas. The number of
        Availability Zones in this list must match the value of ``ReplicaCount`` or
        ``ReplicasPerNodeGroup`` if not specified.

        - *(string) --*

    - **CacheSize** *(string) --*

      The size of the cache on the source cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created in the source cluster.

    - **SnapshotCreateTime** *(datetime) --*

      The date and time when the source node's metadata and cache data set was obtained for
      the snapshot.
    """


_ClientCopySnapshotResponseSnapshotTypeDef = TypedDict(
    "_ClientCopySnapshotResponseSnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": str,
        "NodeSnapshots": List[ClientCopySnapshotResponseSnapshotNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)


class ClientCopySnapshotResponseSnapshotTypeDef(
    _ClientCopySnapshotResponseSnapshotTypeDef
):
    """
    Type definition for `ClientCopySnapshotResponse` `Snapshot`

    Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

    - **SnapshotName** *(string) --*

      The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
      manual snapshot, this is the user-provided name.

    - **ReplicationGroupId** *(string) --*

      The unique identifier of the source replication group.

    - **ReplicationGroupDescription** *(string) --*

      A description of the source replication group.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the source cluster.

    - **SnapshotStatus** *(string) --*

      The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
      ``copying`` | ``deleting`` .

    - **SnapshotSource** *(string) --*

      Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created
      manually (``manual`` ).

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the source cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared to
      their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
         ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
        node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine version that is used by the source cluster.

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the source cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the source cluster is located.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the source cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It is
      specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
      maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
      notifications.

    - **Port** *(integer) --*

      The port number used by each cache nodes in the source cluster.

    - **CacheParameterGroupName** *(string) --*

      The cache parameter group that is associated with the source cluster.

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the source cluster.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
      source cluster.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SnapshotRetentionLimit** *(integer) --*

      For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
      before deleting it.

      For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
      cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do
      not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

       **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
       turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range during which ElastiCache takes daily snapshots of the source cluster.

    - **NumNodeGroups** *(integer) --*

      The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
      number of node groups (shards) in the snapshot and in the restored replication group must
      be the same.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for the source Redis replication
      group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **NodeSnapshots** *(list) --*

      A list of the cache nodes in the source cluster.

      - *(dict) --*

        Represents an individual cache node in a snapshot of a cluster.

        - **CacheClusterId** *(string) --*

          A unique identifier for the source cluster.

        - **NodeGroupId** *(string) --*

          A unique identifier for the source node group (shard).

        - **CacheNodeId** *(string) --*

          The cache node identifier for the node in the source cluster.

        - **NodeGroupConfiguration** *(dict) --*

          The configuration for the source node group (shard).

          - **NodeGroupId** *(string) --*

            Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
            node group these configuration values apply to.

          - **Slots** *(string) --*

            A string that specifies the keyspace for a particular node group. Keyspaces range
            from 0 to 16,383. The string is in the format ``startkey-endkey`` .

            Example: ``"0-3999"``

          - **ReplicaCount** *(integer) --*

            The number of read replica nodes in this node group (shard).

          - **PrimaryAvailabilityZone** *(string) --*

            The Availability Zone where the primary node of this node group (shard) is launched.

          - **ReplicaAvailabilityZones** *(list) --*

            A list of Availability Zones to be used for the read replicas. The number of
            Availability Zones in this list must match the value of ``ReplicaCount`` or
            ``ReplicasPerNodeGroup`` if not specified.

            - *(string) --*

        - **CacheSize** *(string) --*

          The size of the cache on the source cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created in the source cluster.

        - **SnapshotCreateTime** *(datetime) --*

          The date and time when the source node's metadata and cache data set was obtained for
          the snapshot.

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the snapshot.
    """


_ClientCopySnapshotResponseTypeDef = TypedDict(
    "_ClientCopySnapshotResponseTypeDef",
    {"Snapshot": ClientCopySnapshotResponseSnapshotTypeDef},
    total=False,
)


class ClientCopySnapshotResponseTypeDef(_ClientCopySnapshotResponseTypeDef):
    """
    Type definition for `ClientCopySnapshot` `Response`

    - **Snapshot** *(dict) --*

      Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

      - **SnapshotName** *(string) --*

        The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
        manual snapshot, this is the user-provided name.

      - **ReplicationGroupId** *(string) --*

        The unique identifier of the source replication group.

      - **ReplicationGroupDescription** *(string) --*

        A description of the source replication group.

      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the source cluster.

      - **SnapshotStatus** *(string) --*

        The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
        ``copying`` | ``deleting`` .

      - **SnapshotSource** *(string) --*

        Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created
        manually (``manual`` ).

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for the source cluster.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared to
        their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
           ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
          node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

      - **Engine** *(string) --*

        The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

      - **EngineVersion** *(string) --*

        The version of the cache engine version that is used by the source cluster.

      - **NumCacheNodes** *(integer) --*

        The number of cache nodes in the source cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **PreferredAvailabilityZone** *(string) --*

        The name of the Availability Zone in which the source cluster is located.

      - **CacheClusterCreateTime** *(datetime) --*

        The date and time when the source cluster was created.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which maintenance on the cluster is performed. It is
        specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
        maintenance window is a 60 minute period.

        Valid values for ``ddd`` are:

        * ``sun``

        * ``mon``

        * ``tue``

        * ``wed``

        * ``thu``

        * ``fri``

        * ``sat``

        Example: ``sun:23:00-mon:01:30``

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
        notifications.

      - **Port** *(integer) --*

        The port number used by each cache nodes in the source cluster.

      - **CacheParameterGroupName** *(string) --*

        The cache parameter group that is associated with the source cluster.

      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group associated with the source cluster.

      - **VpcId** *(string) --*

        The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
        source cluster.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        This parameter is currently disabled.

      - **SnapshotRetentionLimit** *(integer) --*

        For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
        before deleting it.

        For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
        cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do
        not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

         **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
         turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range during which ElastiCache takes daily snapshots of the source cluster.

      - **NumNodeGroups** *(integer) --*

        The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
        number of node groups (shards) in the snapshot and in the restored replication group must
        be the same.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for the source Redis replication
        group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **NodeSnapshots** *(list) --*

        A list of the cache nodes in the source cluster.

        - *(dict) --*

          Represents an individual cache node in a snapshot of a cluster.

          - **CacheClusterId** *(string) --*

            A unique identifier for the source cluster.

          - **NodeGroupId** *(string) --*

            A unique identifier for the source node group (shard).

          - **CacheNodeId** *(string) --*

            The cache node identifier for the node in the source cluster.

          - **NodeGroupConfiguration** *(dict) --*

            The configuration for the source node group (shard).

            - **NodeGroupId** *(string) --*

              Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
              node group these configuration values apply to.

            - **Slots** *(string) --*

              A string that specifies the keyspace for a particular node group. Keyspaces range
              from 0 to 16,383. The string is in the format ``startkey-endkey`` .

              Example: ``"0-3999"``

            - **ReplicaCount** *(integer) --*

              The number of read replica nodes in this node group (shard).

            - **PrimaryAvailabilityZone** *(string) --*

              The Availability Zone where the primary node of this node group (shard) is launched.

            - **ReplicaAvailabilityZones** *(list) --*

              A list of Availability Zones to be used for the read replicas. The number of
              Availability Zones in this list must match the value of ``ReplicaCount`` or
              ``ReplicasPerNodeGroup`` if not specified.

              - *(string) --*

          - **CacheSize** *(string) --*

            The size of the cache on the source cache node.

          - **CacheNodeCreateTime** *(datetime) --*

            The date and time when the cache node was created in the source cluster.

          - **SnapshotCreateTime** *(datetime) --*

            The date and time when the source node's metadata and cache data set was obtained for
            the snapshot.

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the snapshot.
    """


_ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef
):
    """
    Type definition for `ClientCreateCacheClusterResponseCacheClusterCacheNodes` `Endpoint`

    The hostname for connecting to this cache node.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientCreateCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef
):
    """
    Type definition for `ClientCreateCacheClusterResponseCacheCluster` `CacheNodes`

    Represents an individual cache node within a cluster. Each cache node runs its own
    instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

    The following node types are supported by ElastiCache. Generally speaking, the current
    generation types provide more memory and computational power at lower cost when compared
    to their equivalent previous generation counterparts.

    * General purpose:

      * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
      ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
      ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
      ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
      types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

      * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
      **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
      ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
      ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

    * Compute optimized:

      * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

    * Memory optimized:

      * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
      ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
      ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
      ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
      ``cache.r4.16xlarge``

      * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
      ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
      ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

     **Additional node type info**

    * All current generation instance types are created in Amazon VPC by default.

    * Redis append-only files (AOF) are not supported for T1 or T2 instances.

    * Redis Multi-AZ with automatic failover is not supported on T1 instances.

    * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
    Redis version 2.8.22 and later.

    - **CacheNodeId** *(string) --*

      The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
      combination of cluster ID and node ID uniquely identifies every cache node used in a
      customer's AWS account.

    - **CacheNodeStatus** *(string) --*

      The current state of this cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created.

    - **Endpoint** *(dict) --*

      The hostname for connecting to this cache node.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group applied to this cache node.

    - **SourceCacheNodeId** *(string) --*

      The ID of the primary node to which this read replica node is synchronized. If this
      field is empty, this node is not associated with a primary cluster.

    - **CustomerAvailabilityZone** *(string) --*

      The Availability Zone where this node was created and now resides.
    """


_ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef
):
    """
    Type definition for `ClientCreateCacheClusterResponseCacheCluster` `CacheParameterGroup`

    Status of the cache parameter group.

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **CacheNodeIdsToReboot** *(list) --*

      A list of the cache node IDs which need to be rebooted for parameter changes to be
      applied. A node ID is a numeric identifier (0001, 0002, etc.).

      - *(string) --*
    """


_ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
):
    """
    Type definition for `ClientCreateCacheClusterResponseCacheCluster` `CacheSecurityGroups`

    Represents a cluster's status within a particular cache security group.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Status** *(string) --*

      The membership status in the cache security group. The status changes when a cache
      security group is modified, or when the cache security groups assigned to a cluster are
      modified.
    """


_ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientCreateCacheClusterResponseCacheCluster` `ConfigurationEndpoint`

    Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
    cluster, can be used by an application to connect to any node in the cluster. The
    configuration endpoint will always have ``.cfg`` in it.

    Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientCreateCacheClusterResponseCacheCluster` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for publishing
    ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientCreateCacheClusterResponseCacheCluster` `PendingModifiedValues`

    A group of settings that are applied to the cluster in the future, or that are currently
    being applied.

    - **NumCacheNodes** *(integer) --*

      The new number of cache nodes for the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **CacheNodeIdsToRemove** *(list) --*

      A list of cache node IDs that are being removed (or will be removed) from the cluster. A
      node ID is a 4-digit numeric identifier (0001, 0002, etc.).

      - *(string) --*

    - **EngineVersion** *(string) --*

      The new cache engine version that the cluster runs.

    - **CacheNodeType** *(string) --*

      The cache node type that this cluster or replication group is scaled to.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef
):
    """
    Type definition for `ClientCreateCacheClusterResponseCacheCluster` `SecurityGroups`

    Represents a single cache security group and its status.

    - **SecurityGroupId** *(string) --*

      The identifier of the cache security group.

    - **Status** *(string) --*

      The status of the cache security group membership. The status changes whenever a cache
      security group is modified, or when the cache security groups assigned to a cluster are
      modified.
    """


_ClientCreateCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientCreateCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientCreateCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientCreateCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientCreateCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[
            ClientCreateCacheClusterResponseCacheClusterCacheNodesTypeDef
        ],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[
            ClientCreateCacheClusterResponseCacheClusterSecurityGroupsTypeDef
        ],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class ClientCreateCacheClusterResponseCacheClusterTypeDef(
    _ClientCreateCacheClusterResponseCacheClusterTypeDef
):
    """
    Type definition for `ClientCreateCacheClusterResponse` `CacheCluster`

    Contains all of the attributes of a specific cluster.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the cluster. This identifier is a unique key that
      identifies a cluster.

    - **ConfigurationEndpoint** *(dict) --*

      Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
      cluster, can be used by an application to connect to any node in the cluster. The
      configuration endpoint will always have ``.cfg`` in it.

      Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ClientDownloadLandingPage** *(string) --*

      The URL of the web page where you can download the latest ElastiCache client library.

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared to
      their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
         ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
        node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine that is used in this cluster.

    - **CacheClusterStatus** *(string) --*

      The current state of this cluster, one of the following values: ``available`` ,
      ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
      ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the cluster is located or "Multiple" if the
      cache nodes are located in different Availability Zones.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It is
      specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
      maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **PendingModifiedValues** *(dict) --*

      A group of settings that are applied to the cluster in the future, or that are currently
      being applied.

      - **NumCacheNodes** *(integer) --*

        The new number of cache nodes for the cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **CacheNodeIdsToRemove** *(list) --*

        A list of cache node IDs that are being removed (or will be removed) from the cluster. A
        node ID is a 4-digit numeric identifier (0001, 0002, etc.).

        - *(string) --*

      - **EngineVersion** *(string) --*

        The new cache engine version that the cluster runs.

      - **CacheNodeType** *(string) --*

        The cache node type that this cluster or replication group is scaled to.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for publishing
      ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **CacheSecurityGroups** *(list) --*

      A list of cache security group elements, composed of name and status sub-elements.

      - *(dict) --*

        Represents a cluster's status within a particular cache security group.

        - **CacheSecurityGroupName** *(string) --*

          The name of the cache security group.

        - **Status** *(string) --*

          The membership status in the cache security group. The status changes when a cache
          security group is modified, or when the cache security groups assigned to a cluster are
          modified.

    - **CacheParameterGroup** *(dict) --*

      Status of the cache parameter group.

      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **CacheNodeIdsToReboot** *(list) --*

        A list of the cache node IDs which need to be rebooted for parameter changes to be
        applied. A node ID is a numeric identifier (0001, 0002, etc.).

        - *(string) --*

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the cluster.

    - **CacheNodes** *(list) --*

      A list of cache nodes that are members of the cluster.

      - *(dict) --*

        Represents an individual cache node within a cluster. Each cache node runs its own
        instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared
        to their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
          types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
          **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
          ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

        - **CacheNodeId** *(string) --*

          The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
          combination of cluster ID and node ID uniquely identifies every cache node used in a
          customer's AWS account.

        - **CacheNodeStatus** *(string) --*

          The current state of this cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created.

        - **Endpoint** *(dict) --*

          The hostname for connecting to this cache node.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group applied to this cache node.

        - **SourceCacheNodeId** *(string) --*

          The ID of the primary node to which this read replica node is synchronized. If this
          field is empty, this node is not associated with a primary cluster.

        - **CustomerAvailabilityZone** *(string) --*

          The Availability Zone where this node was created and now resides.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SecurityGroups** *(list) --*

      A list of VPC Security Groups associated with the cluster.

      - *(dict) --*

        Represents a single cache security group and its status.

        - **SecurityGroupId** *(string) --*

          The identifier of the cache security group.

        - **Status** *(string) --*

          The status of the cache security group membership. The status changes whenever a cache
          security group is modified, or when the cache security groups assigned to a cluster are
          modified.

    - **ReplicationGroupId** *(string) --*

      The replication group to which this cluster belongs. If this field is empty, the cluster is
      not associated with any replication group.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your cluster.

      Example: ``05:00-09:00``

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``
    """


_ClientCreateCacheClusterResponseTypeDef = TypedDict(
    "_ClientCreateCacheClusterResponseTypeDef",
    {"CacheCluster": ClientCreateCacheClusterResponseCacheClusterTypeDef},
    total=False,
)


class ClientCreateCacheClusterResponseTypeDef(_ClientCreateCacheClusterResponseTypeDef):
    """
    Type definition for `ClientCreateCacheCluster` `Response`

    - **CacheCluster** *(dict) --*

      Contains all of the attributes of a specific cluster.

      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the cluster. This identifier is a unique key that
        identifies a cluster.

      - **ConfigurationEndpoint** *(dict) --*

        Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
        cluster, can be used by an application to connect to any node in the cluster. The
        configuration endpoint will always have ``.cfg`` in it.

        Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **ClientDownloadLandingPage** *(string) --*

        The URL of the web page where you can download the latest ElastiCache client library.

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for the cluster.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared to
        their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
           ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
          node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

      - **Engine** *(string) --*

        The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

      - **EngineVersion** *(string) --*

        The version of the cache engine that is used in this cluster.

      - **CacheClusterStatus** *(string) --*

        The current state of this cluster, one of the following values: ``available`` ,
        ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
        ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

      - **NumCacheNodes** *(integer) --*

        The number of cache nodes in the cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **PreferredAvailabilityZone** *(string) --*

        The name of the Availability Zone in which the cluster is located or "Multiple" if the
        cache nodes are located in different Availability Zones.

      - **CacheClusterCreateTime** *(datetime) --*

        The date and time when the cluster was created.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which maintenance on the cluster is performed. It is
        specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
        maintenance window is a 60 minute period.

        Valid values for ``ddd`` are:

        * ``sun``

        * ``mon``

        * ``tue``

        * ``wed``

        * ``thu``

        * ``fri``

        * ``sat``

        Example: ``sun:23:00-mon:01:30``

      - **PendingModifiedValues** *(dict) --*

        A group of settings that are applied to the cluster in the future, or that are currently
        being applied.

        - **NumCacheNodes** *(integer) --*

          The new number of cache nodes for the cluster.

          For clusters running Redis, this value must be 1. For clusters running Memcached, this
          value must be between 1 and 20.

        - **CacheNodeIdsToRemove** *(list) --*

          A list of cache node IDs that are being removed (or will be removed) from the cluster. A
          node ID is a 4-digit numeric identifier (0001, 0002, etc.).

          - *(string) --*

        - **EngineVersion** *(string) --*

          The new cache engine version that the cluster runs.

        - **CacheNodeType** *(string) --*

          The cache node type that this cluster or replication group is scaled to.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **NotificationConfiguration** *(dict) --*

        Describes a notification topic and its status. Notification topics are used for publishing
        ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the topic.

        - **TopicStatus** *(string) --*

          The current state of the topic.

      - **CacheSecurityGroups** *(list) --*

        A list of cache security group elements, composed of name and status sub-elements.

        - *(dict) --*

          Represents a cluster's status within a particular cache security group.

          - **CacheSecurityGroupName** *(string) --*

            The name of the cache security group.

          - **Status** *(string) --*

            The membership status in the cache security group. The status changes when a cache
            security group is modified, or when the cache security groups assigned to a cluster are
            modified.

      - **CacheParameterGroup** *(dict) --*

        Status of the cache parameter group.

        - **CacheParameterGroupName** *(string) --*

          The name of the cache parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

        - **CacheNodeIdsToReboot** *(list) --*

          A list of the cache node IDs which need to be rebooted for parameter changes to be
          applied. A node ID is a numeric identifier (0001, 0002, etc.).

          - *(string) --*

      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group associated with the cluster.

      - **CacheNodes** *(list) --*

        A list of cache nodes that are members of the cluster.

        - *(dict) --*

          Represents an individual cache node within a cluster. Each cache node runs its own
          instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

          The following node types are supported by ElastiCache. Generally speaking, the current
          generation types provide more memory and computational power at lower cost when compared
          to their equivalent previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
            ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
            ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
            types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
            **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
            ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
            ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
            ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
            ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
            ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
          Redis version 2.8.22 and later.

          - **CacheNodeId** *(string) --*

            The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
            combination of cluster ID and node ID uniquely identifies every cache node used in a
            customer's AWS account.

          - **CacheNodeStatus** *(string) --*

            The current state of this cache node.

          - **CacheNodeCreateTime** *(datetime) --*

            The date and time when the cache node was created.

          - **Endpoint** *(dict) --*

            The hostname for connecting to this cache node.

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ParameterGroupStatus** *(string) --*

            The status of the parameter group applied to this cache node.

          - **SourceCacheNodeId** *(string) --*

            The ID of the primary node to which this read replica node is synchronized. If this
            field is empty, this node is not associated with a primary cluster.

          - **CustomerAvailabilityZone** *(string) --*

            The Availability Zone where this node was created and now resides.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        This parameter is currently disabled.

      - **SecurityGroups** *(list) --*

        A list of VPC Security Groups associated with the cluster.

        - *(dict) --*

          Represents a single cache security group and its status.

          - **SecurityGroupId** *(string) --*

            The identifier of the cache security group.

          - **Status** *(string) --*

            The status of the cache security group membership. The status changes whenever a cache
            security group is modified, or when the cache security groups assigned to a cluster are
            modified.

      - **ReplicationGroupId** *(string) --*

        The replication group to which this cluster belongs. If this field is empty, the cluster is
        not associated with any replication group.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your cluster.

        Example: ``05:00-09:00``

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``
    """


_ClientCreateCacheClusterTagsTypeDef = TypedDict(
    "_ClientCreateCacheClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateCacheClusterTagsTypeDef(_ClientCreateCacheClusterTagsTypeDef):
    """
    Type definition for `ClientCreateCacheCluster` `Tags`

    A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
    are composed of a Key/Value pair. A tag with a null Value is permitted.

    - **Key** *(string) --*

      The key for the tag. May not be null.

    - **Value** *(string) --*

      The tag's value. May be null.
    """


_ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef = TypedDict(
    "_ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "CacheParameterGroupFamily": str,
        "Description": str,
    },
    total=False,
)


class ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef(
    _ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef
):
    """
    Type definition for `ClientCreateCacheParameterGroupResponse` `CacheParameterGroup`

    Represents the output of a ``CreateCacheParameterGroup`` operation.

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.

    - **CacheParameterGroupFamily** *(string) --*

      The name of the cache parameter group family that this cache parameter group is compatible
      with.

      Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
      ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

    - **Description** *(string) --*

      The description for this cache parameter group.
    """


_ClientCreateCacheParameterGroupResponseTypeDef = TypedDict(
    "_ClientCreateCacheParameterGroupResponseTypeDef",
    {
        "CacheParameterGroup": ClientCreateCacheParameterGroupResponseCacheParameterGroupTypeDef
    },
    total=False,
)


class ClientCreateCacheParameterGroupResponseTypeDef(
    _ClientCreateCacheParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateCacheParameterGroup` `Response`

    - **CacheParameterGroup** *(dict) --*

      Represents the output of a ``CreateCacheParameterGroup`` operation.

      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.

      - **CacheParameterGroupFamily** *(string) --*

        The name of the cache parameter group family that this cache parameter group is compatible
        with.

        Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
        ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

      - **Description** *(string) --*

        The description for this cache parameter group.
    """


_ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)


class ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
):
    """
    Type definition for `ClientCreateCacheSecurityGroupResponseCacheSecurityGroup` `EC2SecurityGroups`

    Provides ownership and status information for an Amazon EC2 security group.

    - **Status** *(string) --*

      The status of the Amazon EC2 security group.

    - **EC2SecurityGroupName** *(string) --*

      The name of the Amazon EC2 security group.

    - **EC2SecurityGroupOwnerId** *(string) --*

      The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef = TypedDict(
    "_ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientCreateCacheSecurityGroupResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef(
    _ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef
):
    """
    Type definition for `ClientCreateCacheSecurityGroupResponse` `CacheSecurityGroup`

    Represents the output of one of the following operations:

    * ``AuthorizeCacheSecurityGroupIngress``

    * ``CreateCacheSecurityGroup``

    * ``RevokeCacheSecurityGroupIngress``

    - **OwnerId** *(string) --*

      The AWS account ID of the cache security group owner.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Description** *(string) --*

      The description of the cache security group.

    - **EC2SecurityGroups** *(list) --*

      A list of Amazon EC2 security groups that are associated with this cache security group.

      - *(dict) --*

        Provides ownership and status information for an Amazon EC2 security group.

        - **Status** *(string) --*

          The status of the Amazon EC2 security group.

        - **EC2SecurityGroupName** *(string) --*

          The name of the Amazon EC2 security group.

        - **EC2SecurityGroupOwnerId** *(string) --*

          The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientCreateCacheSecurityGroupResponseTypeDef = TypedDict(
    "_ClientCreateCacheSecurityGroupResponseTypeDef",
    {
        "CacheSecurityGroup": ClientCreateCacheSecurityGroupResponseCacheSecurityGroupTypeDef
    },
    total=False,
)


class ClientCreateCacheSecurityGroupResponseTypeDef(
    _ClientCreateCacheSecurityGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateCacheSecurityGroup` `Response`

    - **CacheSecurityGroup** *(dict) --*

      Represents the output of one of the following operations:

      * ``AuthorizeCacheSecurityGroupIngress``

      * ``CreateCacheSecurityGroup``

      * ``RevokeCacheSecurityGroupIngress``

      - **OwnerId** *(string) --*

        The AWS account ID of the cache security group owner.

      - **CacheSecurityGroupName** *(string) --*

        The name of the cache security group.

      - **Description** *(string) --*

        The description of the cache security group.

      - **EC2SecurityGroups** *(list) --*

        A list of Amazon EC2 security groups that are associated with this cache security group.

        - *(dict) --*

          Provides ownership and status information for an Amazon EC2 security group.

          - **Status** *(string) --*

            The status of the Amazon EC2 security group.

          - **EC2SecurityGroupName** *(string) --*

            The name of the Amazon EC2 security group.

          - **EC2SecurityGroupOwnerId** *(string) --*

            The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnets` `SubnetAvailabilityZone`

    The Availability Zone associated with the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)


class ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef(
    _ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientCreateCacheSubnetGroupResponseCacheSubnetGroup` `Subnets`

    Represents the subnet associated with a cluster. This parameter refers to subnets defined
    in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

    - **SubnetIdentifier** *(string) --*

      The unique identifier for the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone associated with the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.
    """


_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef = TypedDict(
    "_ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[
            ClientCreateCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef(
    _ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef
):
    """
    Type definition for `ClientCreateCacheSubnetGroupResponse` `CacheSubnetGroup`

    Represents the output of one of the following operations:

    * ``CreateCacheSubnetGroup``

    * ``ModifyCacheSubnetGroup``

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group.

    - **CacheSubnetGroupDescription** *(string) --*

      The description of the cache subnet group.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

    - **Subnets** *(list) --*

      A list of subnets associated with the cache subnet group.

      - *(dict) --*

        Represents the subnet associated with a cluster. This parameter refers to subnets defined
        in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

        - **SubnetIdentifier** *(string) --*

          The unique identifier for the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone associated with the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.
    """


_ClientCreateCacheSubnetGroupResponseTypeDef = TypedDict(
    "_ClientCreateCacheSubnetGroupResponseTypeDef",
    {"CacheSubnetGroup": ClientCreateCacheSubnetGroupResponseCacheSubnetGroupTypeDef},
    total=False,
)


class ClientCreateCacheSubnetGroupResponseTypeDef(
    _ClientCreateCacheSubnetGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateCacheSubnetGroup` `Response`

    - **CacheSubnetGroup** *(dict) --*

      Represents the output of one of the following operations:

      * ``CreateCacheSubnetGroup``

      * ``ModifyCacheSubnetGroup``

      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group.

      - **CacheSubnetGroupDescription** *(string) --*

        The description of the cache subnet group.

      - **VpcId** *(string) --*

        The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

      - **Subnets** *(list) --*

        A list of subnets associated with the cache subnet group.

        - *(dict) --*

          Represents the subnet associated with a cluster. This parameter refers to subnets defined
          in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

          - **SubnetIdentifier** *(string) --*

            The unique identifier for the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            The Availability Zone associated with the subnet.

            - **Name** *(string) --*

              The name of the Availability Zone.
    """


_ClientCreateReplicationGroupNodeGroupConfigurationTypeDef = TypedDict(
    "_ClientCreateReplicationGroupNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class ClientCreateReplicationGroupNodeGroupConfigurationTypeDef(
    _ClientCreateReplicationGroupNodeGroupConfigurationTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroup` `NodeGroupConfiguration`

    Node group (shard) configuration options. Each node group (shard) configuration has the
    following: ``Slots`` , ``PrimaryAvailabilityZone`` , ``ReplicaAvailabilityZones`` ,
    ``ReplicaCount`` .

    - **NodeGroupId** *(string) --*

      Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group
      these configuration values apply to.

    - **Slots** *(string) --*

      A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to
      16,383. The string is in the format ``startkey-endkey`` .

      Example: ``"0-3999"``

    - **ReplicaCount** *(integer) --*

      The number of read replica nodes in this node group (shard).

    - **PrimaryAvailabilityZone** *(string) --*

      The Availability Zone where the primary node of this node group (shard) is launched.

    - **ReplicaAvailabilityZones** *(list) --*

      A list of Availability Zones to be used for the read replicas. The number of Availability
      Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if
      not specified.

      - *(string) --*
    """


_ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroupResponseReplicationGroup` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroupResponseReplicationGroupNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` . This
      member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroupResponseReplicationGroupNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroupResponseReplicationGroupNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroupResponseReplicationGroup` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node group
    is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled) replication
      group contains only 1 node group; therefore, the node group ID is 0001. A Redis
      (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
      0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` . This
          member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroupResponseReplicationGroup` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientCreateReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientCreateReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientCreateReplicationGroupResponseReplicationGroupNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": ClientCreateReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientCreateReplicationGroupResponseReplicationGroupTypeDef(
    _ClientCreateReplicationGroupResponseReplicationGroupTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroupResponse` `ReplicationGroup`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , ``modifying``
      , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node group
        is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled) replication
          group contains only 1 node group; therefore, the node group ID is 0001. A Redis
          (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
          0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` . This
              member is only applicable for Redis (cluster mode disabled) replication groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
      range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientCreateReplicationGroupResponseTypeDef = TypedDict(
    "_ClientCreateReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientCreateReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)


class ClientCreateReplicationGroupResponseTypeDef(
    _ClientCreateReplicationGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateReplicationGroup` `Response`

    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.

      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.

      - **Description** *(string) --*

        The user supplied description of the replication group.

      - **Status** *(string) --*

        The current state of this replication group - ``creating`` , ``available`` , ``modifying``
        , ``deleting`` , ``create-failed`` , ``snapshotting`` .

      - **PendingModifiedValues** *(dict) --*

        A group of settings to be applied to the replication group, either immediately or during
        the next maintenance window.

        - **PrimaryClusterId** *(string) --*

          The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
          specified), or during the next maintenance window.

        - **AutomaticFailoverStatus** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **Resharding** *(dict) --*

          The status of an online resharding operation.

          - **SlotMigration** *(dict) --*

            Represents the progress of an online resharding operation.

            - **ProgressPercentage** *(float) --*

              The percentage of the slot migration that is complete.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **MemberClusters** *(list) --*

        The names of all the cache clusters that are part of this replication group.

        - *(string) --*

      - **NodeGroups** *(list) --*

        A list of node groups in this replication group. For Redis (cluster mode disabled)
        replication groups, this is a single-element list. For Redis (cluster mode enabled)
        replication groups, the list contains an entry for each node group (shard).

        - *(dict) --*

          Represents a collection of cache nodes in a replication group. One node in the node group
          is the read/write primary node. All the other nodes are read-only Replica nodes.

          - **NodeGroupId** *(string) --*

            The identifier for the node group (shard). A Redis (cluster mode disabled) replication
            group contains only 1 node group; therefore, the node group ID is 0001. A Redis
            (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
            0090. Optionally, the user can provide the id for a node group.

          - **Status** *(string) --*

            The current state of this replication group - ``creating`` , ``available`` , etc.

          - **PrimaryEndpoint** *(dict) --*

            The endpoint of the primary node in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ReaderEndpoint** *(dict) --*

            The endpoint of the replica nodes in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **Slots** *(string) --*

            The keyspace for this node group (shard).

          - **NodeGroupMembers** *(list) --*

            A list containing information about individual nodes within the node group (shard).

            - *(dict) --*

              Represents a single node within a node group (shard).

              - **CacheClusterId** *(string) --*

                The ID of the cluster to which the node belongs.

              - **CacheNodeId** *(string) --*

                The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                0002, etc.).

              - **ReadEndpoint** *(dict) --*

                The information required for client programs to connect to a node for read
                operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                clusters.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the node is located.

              - **CurrentRole** *(string) --*

                The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                member is only applicable for Redis (cluster mode disabled) replication groups.

      - **SnapshottingClusterId** *(string) --*

        The cluster ID that is used as the daily snapshot source for the replication group.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **ConfigurationEndpoint** *(dict) --*

        The configuration endpoint for this replication group. Use the configuration endpoint to
        connect to this replication group.

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
        range.

        .. note::

          This parameter is only valid if the ``Engine`` parameter is ``redis`` .

      - **ClusterEnabled** *(boolean) --*

        A flag indicating whether or not this replication group is cluster enabled; i.e., whether
        its data can be partitioned across multiple shards (API/CLI: node groups).

        Valid values: ``true`` | ``false``

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for each node in the replication
        group.

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientCreateReplicationGroupTagsTypeDef = TypedDict(
    "_ClientCreateReplicationGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateReplicationGroupTagsTypeDef(_ClientCreateReplicationGroupTagsTypeDef):
    """
    Type definition for `ClientCreateReplicationGroup` `Tags`

    A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags
    are composed of a Key/Value pair. A tag with a null Value is permitted.

    - **Key** *(string) --*

      The key for the tag. May not be null.

    - **Value** *(string) --*

      The tag's value. May be null.
    """


_ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef(
    _ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef
):
    """
    Type definition for `ClientCreateSnapshotResponseSnapshotNodeSnapshots` `NodeGroupConfiguration`

    The configuration for the source node group (shard).

    - **NodeGroupId** *(string) --*

      Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
      node group these configuration values apply to.

    - **Slots** *(string) --*

      A string that specifies the keyspace for a particular node group. Keyspaces range
      from 0 to 16,383. The string is in the format ``startkey-endkey`` .

      Example: ``"0-3999"``

    - **ReplicaCount** *(integer) --*

      The number of read replica nodes in this node group (shard).

    - **PrimaryAvailabilityZone** *(string) --*

      The Availability Zone where the primary node of this node group (shard) is launched.

    - **ReplicaAvailabilityZones** *(list) --*

      A list of Availability Zones to be used for the read replicas. The number of
      Availability Zones in this list must match the value of ``ReplicaCount`` or
      ``ReplicasPerNodeGroup`` if not specified.

      - *(string) --*
    """


_ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientCreateSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)


class ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef(
    _ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef
):
    """
    Type definition for `ClientCreateSnapshotResponseSnapshot` `NodeSnapshots`

    Represents an individual cache node in a snapshot of a cluster.

    - **CacheClusterId** *(string) --*

      A unique identifier for the source cluster.

    - **NodeGroupId** *(string) --*

      A unique identifier for the source node group (shard).

    - **CacheNodeId** *(string) --*

      The cache node identifier for the node in the source cluster.

    - **NodeGroupConfiguration** *(dict) --*

      The configuration for the source node group (shard).

      - **NodeGroupId** *(string) --*

        Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
        node group these configuration values apply to.

      - **Slots** *(string) --*

        A string that specifies the keyspace for a particular node group. Keyspaces range
        from 0 to 16,383. The string is in the format ``startkey-endkey`` .

        Example: ``"0-3999"``

      - **ReplicaCount** *(integer) --*

        The number of read replica nodes in this node group (shard).

      - **PrimaryAvailabilityZone** *(string) --*

        The Availability Zone where the primary node of this node group (shard) is launched.

      - **ReplicaAvailabilityZones** *(list) --*

        A list of Availability Zones to be used for the read replicas. The number of
        Availability Zones in this list must match the value of ``ReplicaCount`` or
        ``ReplicasPerNodeGroup`` if not specified.

        - *(string) --*

    - **CacheSize** *(string) --*

      The size of the cache on the source cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created in the source cluster.

    - **SnapshotCreateTime** *(datetime) --*

      The date and time when the source node's metadata and cache data set was obtained for
      the snapshot.
    """


_ClientCreateSnapshotResponseSnapshotTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": str,
        "NodeSnapshots": List[ClientCreateSnapshotResponseSnapshotNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)


class ClientCreateSnapshotResponseSnapshotTypeDef(
    _ClientCreateSnapshotResponseSnapshotTypeDef
):
    """
    Type definition for `ClientCreateSnapshotResponse` `Snapshot`

    Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

    - **SnapshotName** *(string) --*

      The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
      manual snapshot, this is the user-provided name.

    - **ReplicationGroupId** *(string) --*

      The unique identifier of the source replication group.

    - **ReplicationGroupDescription** *(string) --*

      A description of the source replication group.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the source cluster.

    - **SnapshotStatus** *(string) --*

      The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
      ``copying`` | ``deleting`` .

    - **SnapshotSource** *(string) --*

      Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created
      manually (``manual`` ).

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the source cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared to
      their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
         ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
        node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine version that is used by the source cluster.

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the source cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the source cluster is located.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the source cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It is
      specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
      maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
      notifications.

    - **Port** *(integer) --*

      The port number used by each cache nodes in the source cluster.

    - **CacheParameterGroupName** *(string) --*

      The cache parameter group that is associated with the source cluster.

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the source cluster.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
      source cluster.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SnapshotRetentionLimit** *(integer) --*

      For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
      before deleting it.

      For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
      cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do
      not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

       **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
       turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range during which ElastiCache takes daily snapshots of the source cluster.

    - **NumNodeGroups** *(integer) --*

      The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
      number of node groups (shards) in the snapshot and in the restored replication group must
      be the same.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for the source Redis replication
      group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **NodeSnapshots** *(list) --*

      A list of the cache nodes in the source cluster.

      - *(dict) --*

        Represents an individual cache node in a snapshot of a cluster.

        - **CacheClusterId** *(string) --*

          A unique identifier for the source cluster.

        - **NodeGroupId** *(string) --*

          A unique identifier for the source node group (shard).

        - **CacheNodeId** *(string) --*

          The cache node identifier for the node in the source cluster.

        - **NodeGroupConfiguration** *(dict) --*

          The configuration for the source node group (shard).

          - **NodeGroupId** *(string) --*

            Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
            node group these configuration values apply to.

          - **Slots** *(string) --*

            A string that specifies the keyspace for a particular node group. Keyspaces range
            from 0 to 16,383. The string is in the format ``startkey-endkey`` .

            Example: ``"0-3999"``

          - **ReplicaCount** *(integer) --*

            The number of read replica nodes in this node group (shard).

          - **PrimaryAvailabilityZone** *(string) --*

            The Availability Zone where the primary node of this node group (shard) is launched.

          - **ReplicaAvailabilityZones** *(list) --*

            A list of Availability Zones to be used for the read replicas. The number of
            Availability Zones in this list must match the value of ``ReplicaCount`` or
            ``ReplicasPerNodeGroup`` if not specified.

            - *(string) --*

        - **CacheSize** *(string) --*

          The size of the cache on the source cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created in the source cluster.

        - **SnapshotCreateTime** *(datetime) --*

          The date and time when the source node's metadata and cache data set was obtained for
          the snapshot.

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the snapshot.
    """


_ClientCreateSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseTypeDef",
    {"Snapshot": ClientCreateSnapshotResponseSnapshotTypeDef},
    total=False,
)


class ClientCreateSnapshotResponseTypeDef(_ClientCreateSnapshotResponseTypeDef):
    """
    Type definition for `ClientCreateSnapshot` `Response`

    - **Snapshot** *(dict) --*

      Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

      - **SnapshotName** *(string) --*

        The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
        manual snapshot, this is the user-provided name.

      - **ReplicationGroupId** *(string) --*

        The unique identifier of the source replication group.

      - **ReplicationGroupDescription** *(string) --*

        A description of the source replication group.

      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the source cluster.

      - **SnapshotStatus** *(string) --*

        The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
        ``copying`` | ``deleting`` .

      - **SnapshotSource** *(string) --*

        Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created
        manually (``manual`` ).

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for the source cluster.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared to
        their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
           ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
          node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

      - **Engine** *(string) --*

        The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

      - **EngineVersion** *(string) --*

        The version of the cache engine version that is used by the source cluster.

      - **NumCacheNodes** *(integer) --*

        The number of cache nodes in the source cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **PreferredAvailabilityZone** *(string) --*

        The name of the Availability Zone in which the source cluster is located.

      - **CacheClusterCreateTime** *(datetime) --*

        The date and time when the source cluster was created.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which maintenance on the cluster is performed. It is
        specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
        maintenance window is a 60 minute period.

        Valid values for ``ddd`` are:

        * ``sun``

        * ``mon``

        * ``tue``

        * ``wed``

        * ``thu``

        * ``fri``

        * ``sat``

        Example: ``sun:23:00-mon:01:30``

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
        notifications.

      - **Port** *(integer) --*

        The port number used by each cache nodes in the source cluster.

      - **CacheParameterGroupName** *(string) --*

        The cache parameter group that is associated with the source cluster.

      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group associated with the source cluster.

      - **VpcId** *(string) --*

        The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
        source cluster.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        This parameter is currently disabled.

      - **SnapshotRetentionLimit** *(integer) --*

        For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
        before deleting it.

        For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
        cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do
        not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

         **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
         turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range during which ElastiCache takes daily snapshots of the source cluster.

      - **NumNodeGroups** *(integer) --*

        The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
        number of node groups (shards) in the snapshot and in the restored replication group must
        be the same.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for the source Redis replication
        group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **NodeSnapshots** *(list) --*

        A list of the cache nodes in the source cluster.

        - *(dict) --*

          Represents an individual cache node in a snapshot of a cluster.

          - **CacheClusterId** *(string) --*

            A unique identifier for the source cluster.

          - **NodeGroupId** *(string) --*

            A unique identifier for the source node group (shard).

          - **CacheNodeId** *(string) --*

            The cache node identifier for the node in the source cluster.

          - **NodeGroupConfiguration** *(dict) --*

            The configuration for the source node group (shard).

            - **NodeGroupId** *(string) --*

              Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
              node group these configuration values apply to.

            - **Slots** *(string) --*

              A string that specifies the keyspace for a particular node group. Keyspaces range
              from 0 to 16,383. The string is in the format ``startkey-endkey`` .

              Example: ``"0-3999"``

            - **ReplicaCount** *(integer) --*

              The number of read replica nodes in this node group (shard).

            - **PrimaryAvailabilityZone** *(string) --*

              The Availability Zone where the primary node of this node group (shard) is launched.

            - **ReplicaAvailabilityZones** *(list) --*

              A list of Availability Zones to be used for the read replicas. The number of
              Availability Zones in this list must match the value of ``ReplicaCount`` or
              ``ReplicasPerNodeGroup`` if not specified.

              - *(string) --*

          - **CacheSize** *(string) --*

            The size of the cache on the source cache node.

          - **CacheNodeCreateTime** *(datetime) --*

            The date and time when the cache node was created in the source cluster.

          - **SnapshotCreateTime** *(datetime) --*

            The date and time when the source node's metadata and cache data set was obtained for
            the snapshot.

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the snapshot.
    """


_RequiredClientDecreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_RequiredClientDecreaseReplicaCountReplicaConfigurationTypeDef",
    {"NodeGroupId": str, "NewReplicaCount": int},
)
_OptionalClientDecreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_OptionalClientDecreaseReplicaCountReplicaConfigurationTypeDef",
    {"PreferredAvailabilityZones": List[str]},
    total=False,
)


class ClientDecreaseReplicaCountReplicaConfigurationTypeDef(
    _RequiredClientDecreaseReplicaCountReplicaConfigurationTypeDef,
    _OptionalClientDecreaseReplicaCountReplicaConfigurationTypeDef,
):
    """
    Type definition for `ClientDecreaseReplicaCount` `ReplicaConfiguration`

    Node group (shard) configuration options when adding or removing replicas. Each node group
    (shard) configuration has the following members: NodeGroupId, NewReplicaCount, and
    PreferredAvailabilityZones.

    - **NodeGroupId** *(string) --* **[REQUIRED]**

      The 4-digit id for the node group you are configuring. For Redis (cluster mode disabled)
      replication groups, the node group id is always 0001. To find a Redis (cluster mode
      enabled)'s node group's (shard's) id, see `Finding a Shard's Id
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/shard-find-id.html>`__ .

    - **NewReplicaCount** *(integer) --* **[REQUIRED]**

      The number of replicas you want in this node group at the end of this operation. The maximum
      value for ``NewReplicaCount`` is 5. The minimum value depends upon the type of Redis
      replication group you are working with.

      The minimum number of replicas in a shard or replication group is:

      * Redis (cluster mode disabled)

        * If Multi-AZ with Automatic Failover is enabled: 1

        * If Multi-AZ with Automatic Failover is not enable: 0

      * Redis (cluster mode enabled): 0 (though you will not be able to failover to a replica if
      your primary node fails)

    - **PreferredAvailabilityZones** *(list) --*

      A list of ``PreferredAvailabilityZone`` strings that specify which availability zones the
      replication group's nodes are to be in. The nummber of ``PreferredAvailabilityZone`` values
      must equal the value of ``NewReplicaCount`` plus 1 to account for the primary node. If this
      member of ``ReplicaConfiguration`` is omitted, ElastiCache for Redis selects the availability
      zone for each of the replicas.

      - *(string) --*
    """


_ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCountResponseReplicationGroup` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCountResponseReplicationGroupNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` . This
      member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCountResponseReplicationGroupNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCountResponseReplicationGroupNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCountResponseReplicationGroup` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node group
    is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled) replication
      group contains only 1 node group; therefore, the node group ID is 0001. A Redis
      (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
      0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` . This
          member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCountResponseReplicationGroup` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientDecreaseReplicaCountResponseReplicationGroupTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientDecreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientDecreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": ClientDecreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDecreaseReplicaCountResponseReplicationGroupTypeDef(
    _ClientDecreaseReplicaCountResponseReplicationGroupTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCountResponse` `ReplicationGroup`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , ``modifying``
      , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node group
        is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled) replication
          group contains only 1 node group; therefore, the node group ID is 0001. A Redis
          (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
          0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` . This
              member is only applicable for Redis (cluster mode disabled) replication groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
      range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientDecreaseReplicaCountResponseTypeDef = TypedDict(
    "_ClientDecreaseReplicaCountResponseTypeDef",
    {"ReplicationGroup": ClientDecreaseReplicaCountResponseReplicationGroupTypeDef},
    total=False,
)


class ClientDecreaseReplicaCountResponseTypeDef(
    _ClientDecreaseReplicaCountResponseTypeDef
):
    """
    Type definition for `ClientDecreaseReplicaCount` `Response`

    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.

      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.

      - **Description** *(string) --*

        The user supplied description of the replication group.

      - **Status** *(string) --*

        The current state of this replication group - ``creating`` , ``available`` , ``modifying``
        , ``deleting`` , ``create-failed`` , ``snapshotting`` .

      - **PendingModifiedValues** *(dict) --*

        A group of settings to be applied to the replication group, either immediately or during
        the next maintenance window.

        - **PrimaryClusterId** *(string) --*

          The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
          specified), or during the next maintenance window.

        - **AutomaticFailoverStatus** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **Resharding** *(dict) --*

          The status of an online resharding operation.

          - **SlotMigration** *(dict) --*

            Represents the progress of an online resharding operation.

            - **ProgressPercentage** *(float) --*

              The percentage of the slot migration that is complete.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **MemberClusters** *(list) --*

        The names of all the cache clusters that are part of this replication group.

        - *(string) --*

      - **NodeGroups** *(list) --*

        A list of node groups in this replication group. For Redis (cluster mode disabled)
        replication groups, this is a single-element list. For Redis (cluster mode enabled)
        replication groups, the list contains an entry for each node group (shard).

        - *(dict) --*

          Represents a collection of cache nodes in a replication group. One node in the node group
          is the read/write primary node. All the other nodes are read-only Replica nodes.

          - **NodeGroupId** *(string) --*

            The identifier for the node group (shard). A Redis (cluster mode disabled) replication
            group contains only 1 node group; therefore, the node group ID is 0001. A Redis
            (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
            0090. Optionally, the user can provide the id for a node group.

          - **Status** *(string) --*

            The current state of this replication group - ``creating`` , ``available`` , etc.

          - **PrimaryEndpoint** *(dict) --*

            The endpoint of the primary node in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ReaderEndpoint** *(dict) --*

            The endpoint of the replica nodes in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **Slots** *(string) --*

            The keyspace for this node group (shard).

          - **NodeGroupMembers** *(list) --*

            A list containing information about individual nodes within the node group (shard).

            - *(dict) --*

              Represents a single node within a node group (shard).

              - **CacheClusterId** *(string) --*

                The ID of the cluster to which the node belongs.

              - **CacheNodeId** *(string) --*

                The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                0002, etc.).

              - **ReadEndpoint** *(dict) --*

                The information required for client programs to connect to a node for read
                operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                clusters.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the node is located.

              - **CurrentRole** *(string) --*

                The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                member is only applicable for Redis (cluster mode disabled) replication groups.

      - **SnapshottingClusterId** *(string) --*

        The cluster ID that is used as the daily snapshot source for the replication group.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **ConfigurationEndpoint** *(dict) --*

        The configuration endpoint for this replication group. Use the configuration endpoint to
        connect to this replication group.

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
        range.

        .. note::

          This parameter is only valid if the ``Engine`` parameter is ``redis`` .

      - **ClusterEnabled** *(boolean) --*

        A flag indicating whether or not this replication group is cluster enabled; i.e., whether
        its data can be partitioned across multiple shards (API/CLI: node groups).

        Valid values: ``true`` | ``false``

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for each node in the replication
        group.

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef
):
    """
    Type definition for `ClientDeleteCacheClusterResponseCacheClusterCacheNodes` `Endpoint`

    The hostname for connecting to this cache node.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientDeleteCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef
):
    """
    Type definition for `ClientDeleteCacheClusterResponseCacheCluster` `CacheNodes`

    Represents an individual cache node within a cluster. Each cache node runs its own
    instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

    The following node types are supported by ElastiCache. Generally speaking, the current
    generation types provide more memory and computational power at lower cost when compared
    to their equivalent previous generation counterparts.

    * General purpose:

      * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
      ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
      ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
      ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
      types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

      * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
      **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
      ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
      ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

    * Compute optimized:

      * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

    * Memory optimized:

      * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
      ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
      ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
      ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
      ``cache.r4.16xlarge``

      * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
      ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
      ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

     **Additional node type info**

    * All current generation instance types are created in Amazon VPC by default.

    * Redis append-only files (AOF) are not supported for T1 or T2 instances.

    * Redis Multi-AZ with automatic failover is not supported on T1 instances.

    * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
    Redis version 2.8.22 and later.

    - **CacheNodeId** *(string) --*

      The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
      combination of cluster ID and node ID uniquely identifies every cache node used in a
      customer's AWS account.

    - **CacheNodeStatus** *(string) --*

      The current state of this cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created.

    - **Endpoint** *(dict) --*

      The hostname for connecting to this cache node.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group applied to this cache node.

    - **SourceCacheNodeId** *(string) --*

      The ID of the primary node to which this read replica node is synchronized. If this
      field is empty, this node is not associated with a primary cluster.

    - **CustomerAvailabilityZone** *(string) --*

      The Availability Zone where this node was created and now resides.
    """


_ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef
):
    """
    Type definition for `ClientDeleteCacheClusterResponseCacheCluster` `CacheParameterGroup`

    Status of the cache parameter group.

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **CacheNodeIdsToReboot** *(list) --*

      A list of the cache node IDs which need to be rebooted for parameter changes to be
      applied. A node ID is a numeric identifier (0001, 0002, etc.).

      - *(string) --*
    """


_ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDeleteCacheClusterResponseCacheCluster` `CacheSecurityGroups`

    Represents a cluster's status within a particular cache security group.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Status** *(string) --*

      The membership status in the cache security group. The status changes when a cache
      security group is modified, or when the cache security groups assigned to a cluster are
      modified.
    """


_ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientDeleteCacheClusterResponseCacheCluster` `ConfigurationEndpoint`

    Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
    cluster, can be used by an application to connect to any node in the cluster. The
    configuration endpoint will always have ``.cfg`` in it.

    Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientDeleteCacheClusterResponseCacheCluster` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for publishing
    ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDeleteCacheClusterResponseCacheCluster` `PendingModifiedValues`

    A group of settings that are applied to the cluster in the future, or that are currently
    being applied.

    - **NumCacheNodes** *(integer) --*

      The new number of cache nodes for the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **CacheNodeIdsToRemove** *(list) --*

      A list of cache node IDs that are being removed (or will be removed) from the cluster. A
      node ID is a 4-digit numeric identifier (0001, 0002, etc.).

      - *(string) --*

    - **EngineVersion** *(string) --*

      The new cache engine version that the cluster runs.

    - **CacheNodeType** *(string) --*

      The cache node type that this cluster or replication group is scaled to.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDeleteCacheClusterResponseCacheCluster` `SecurityGroups`

    Represents a single cache security group and its status.

    - **SecurityGroupId** *(string) --*

      The identifier of the cache security group.

    - **Status** *(string) --*

      The status of the cache security group membership. The status changes whenever a cache
      security group is modified, or when the cache security groups assigned to a cluster are
      modified.
    """


_ClientDeleteCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientDeleteCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientDeleteCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientDeleteCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientDeleteCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[
            ClientDeleteCacheClusterResponseCacheClusterCacheNodesTypeDef
        ],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[
            ClientDeleteCacheClusterResponseCacheClusterSecurityGroupsTypeDef
        ],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class ClientDeleteCacheClusterResponseCacheClusterTypeDef(
    _ClientDeleteCacheClusterResponseCacheClusterTypeDef
):
    """
    Type definition for `ClientDeleteCacheClusterResponse` `CacheCluster`

    Contains all of the attributes of a specific cluster.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the cluster. This identifier is a unique key that
      identifies a cluster.

    - **ConfigurationEndpoint** *(dict) --*

      Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
      cluster, can be used by an application to connect to any node in the cluster. The
      configuration endpoint will always have ``.cfg`` in it.

      Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ClientDownloadLandingPage** *(string) --*

      The URL of the web page where you can download the latest ElastiCache client library.

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared to
      their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
         ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
        node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine that is used in this cluster.

    - **CacheClusterStatus** *(string) --*

      The current state of this cluster, one of the following values: ``available`` ,
      ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
      ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the cluster is located or "Multiple" if the
      cache nodes are located in different Availability Zones.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It is
      specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
      maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **PendingModifiedValues** *(dict) --*

      A group of settings that are applied to the cluster in the future, or that are currently
      being applied.

      - **NumCacheNodes** *(integer) --*

        The new number of cache nodes for the cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **CacheNodeIdsToRemove** *(list) --*

        A list of cache node IDs that are being removed (or will be removed) from the cluster. A
        node ID is a 4-digit numeric identifier (0001, 0002, etc.).

        - *(string) --*

      - **EngineVersion** *(string) --*

        The new cache engine version that the cluster runs.

      - **CacheNodeType** *(string) --*

        The cache node type that this cluster or replication group is scaled to.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for publishing
      ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **CacheSecurityGroups** *(list) --*

      A list of cache security group elements, composed of name and status sub-elements.

      - *(dict) --*

        Represents a cluster's status within a particular cache security group.

        - **CacheSecurityGroupName** *(string) --*

          The name of the cache security group.

        - **Status** *(string) --*

          The membership status in the cache security group. The status changes when a cache
          security group is modified, or when the cache security groups assigned to a cluster are
          modified.

    - **CacheParameterGroup** *(dict) --*

      Status of the cache parameter group.

      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **CacheNodeIdsToReboot** *(list) --*

        A list of the cache node IDs which need to be rebooted for parameter changes to be
        applied. A node ID is a numeric identifier (0001, 0002, etc.).

        - *(string) --*

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the cluster.

    - **CacheNodes** *(list) --*

      A list of cache nodes that are members of the cluster.

      - *(dict) --*

        Represents an individual cache node within a cluster. Each cache node runs its own
        instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared
        to their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
          types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
          **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
          ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

        - **CacheNodeId** *(string) --*

          The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
          combination of cluster ID and node ID uniquely identifies every cache node used in a
          customer's AWS account.

        - **CacheNodeStatus** *(string) --*

          The current state of this cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created.

        - **Endpoint** *(dict) --*

          The hostname for connecting to this cache node.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group applied to this cache node.

        - **SourceCacheNodeId** *(string) --*

          The ID of the primary node to which this read replica node is synchronized. If this
          field is empty, this node is not associated with a primary cluster.

        - **CustomerAvailabilityZone** *(string) --*

          The Availability Zone where this node was created and now resides.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SecurityGroups** *(list) --*

      A list of VPC Security Groups associated with the cluster.

      - *(dict) --*

        Represents a single cache security group and its status.

        - **SecurityGroupId** *(string) --*

          The identifier of the cache security group.

        - **Status** *(string) --*

          The status of the cache security group membership. The status changes whenever a cache
          security group is modified, or when the cache security groups assigned to a cluster are
          modified.

    - **ReplicationGroupId** *(string) --*

      The replication group to which this cluster belongs. If this field is empty, the cluster is
      not associated with any replication group.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your cluster.

      Example: ``05:00-09:00``

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``
    """


_ClientDeleteCacheClusterResponseTypeDef = TypedDict(
    "_ClientDeleteCacheClusterResponseTypeDef",
    {"CacheCluster": ClientDeleteCacheClusterResponseCacheClusterTypeDef},
    total=False,
)


class ClientDeleteCacheClusterResponseTypeDef(_ClientDeleteCacheClusterResponseTypeDef):
    """
    Type definition for `ClientDeleteCacheCluster` `Response`

    - **CacheCluster** *(dict) --*

      Contains all of the attributes of a specific cluster.

      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the cluster. This identifier is a unique key that
        identifies a cluster.

      - **ConfigurationEndpoint** *(dict) --*

        Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
        cluster, can be used by an application to connect to any node in the cluster. The
        configuration endpoint will always have ``.cfg`` in it.

        Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **ClientDownloadLandingPage** *(string) --*

        The URL of the web page where you can download the latest ElastiCache client library.

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for the cluster.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared to
        their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
           ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
          node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

      - **Engine** *(string) --*

        The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

      - **EngineVersion** *(string) --*

        The version of the cache engine that is used in this cluster.

      - **CacheClusterStatus** *(string) --*

        The current state of this cluster, one of the following values: ``available`` ,
        ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
        ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

      - **NumCacheNodes** *(integer) --*

        The number of cache nodes in the cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **PreferredAvailabilityZone** *(string) --*

        The name of the Availability Zone in which the cluster is located or "Multiple" if the
        cache nodes are located in different Availability Zones.

      - **CacheClusterCreateTime** *(datetime) --*

        The date and time when the cluster was created.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which maintenance on the cluster is performed. It is
        specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
        maintenance window is a 60 minute period.

        Valid values for ``ddd`` are:

        * ``sun``

        * ``mon``

        * ``tue``

        * ``wed``

        * ``thu``

        * ``fri``

        * ``sat``

        Example: ``sun:23:00-mon:01:30``

      - **PendingModifiedValues** *(dict) --*

        A group of settings that are applied to the cluster in the future, or that are currently
        being applied.

        - **NumCacheNodes** *(integer) --*

          The new number of cache nodes for the cluster.

          For clusters running Redis, this value must be 1. For clusters running Memcached, this
          value must be between 1 and 20.

        - **CacheNodeIdsToRemove** *(list) --*

          A list of cache node IDs that are being removed (or will be removed) from the cluster. A
          node ID is a 4-digit numeric identifier (0001, 0002, etc.).

          - *(string) --*

        - **EngineVersion** *(string) --*

          The new cache engine version that the cluster runs.

        - **CacheNodeType** *(string) --*

          The cache node type that this cluster or replication group is scaled to.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **NotificationConfiguration** *(dict) --*

        Describes a notification topic and its status. Notification topics are used for publishing
        ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the topic.

        - **TopicStatus** *(string) --*

          The current state of the topic.

      - **CacheSecurityGroups** *(list) --*

        A list of cache security group elements, composed of name and status sub-elements.

        - *(dict) --*

          Represents a cluster's status within a particular cache security group.

          - **CacheSecurityGroupName** *(string) --*

            The name of the cache security group.

          - **Status** *(string) --*

            The membership status in the cache security group. The status changes when a cache
            security group is modified, or when the cache security groups assigned to a cluster are
            modified.

      - **CacheParameterGroup** *(dict) --*

        Status of the cache parameter group.

        - **CacheParameterGroupName** *(string) --*

          The name of the cache parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

        - **CacheNodeIdsToReboot** *(list) --*

          A list of the cache node IDs which need to be rebooted for parameter changes to be
          applied. A node ID is a numeric identifier (0001, 0002, etc.).

          - *(string) --*

      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group associated with the cluster.

      - **CacheNodes** *(list) --*

        A list of cache nodes that are members of the cluster.

        - *(dict) --*

          Represents an individual cache node within a cluster. Each cache node runs its own
          instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

          The following node types are supported by ElastiCache. Generally speaking, the current
          generation types provide more memory and computational power at lower cost when compared
          to their equivalent previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
            ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
            ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
            types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
            **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
            ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
            ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
            ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
            ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
            ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
          Redis version 2.8.22 and later.

          - **CacheNodeId** *(string) --*

            The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
            combination of cluster ID and node ID uniquely identifies every cache node used in a
            customer's AWS account.

          - **CacheNodeStatus** *(string) --*

            The current state of this cache node.

          - **CacheNodeCreateTime** *(datetime) --*

            The date and time when the cache node was created.

          - **Endpoint** *(dict) --*

            The hostname for connecting to this cache node.

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ParameterGroupStatus** *(string) --*

            The status of the parameter group applied to this cache node.

          - **SourceCacheNodeId** *(string) --*

            The ID of the primary node to which this read replica node is synchronized. If this
            field is empty, this node is not associated with a primary cluster.

          - **CustomerAvailabilityZone** *(string) --*

            The Availability Zone where this node was created and now resides.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        This parameter is currently disabled.

      - **SecurityGroups** *(list) --*

        A list of VPC Security Groups associated with the cluster.

        - *(dict) --*

          Represents a single cache security group and its status.

          - **SecurityGroupId** *(string) --*

            The identifier of the cache security group.

          - **Status** *(string) --*

            The status of the cache security group membership. The status changes whenever a cache
            security group is modified, or when the cache security groups assigned to a cluster are
            modified.

      - **ReplicationGroupId** *(string) --*

        The replication group to which this cluster belongs. If this field is empty, the cluster is
        not associated with any replication group.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your cluster.

        Example: ``05:00-09:00``

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``
    """


_ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroupResponseReplicationGroup` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroupResponseReplicationGroupNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` . This
      member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroupResponseReplicationGroupNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroupResponseReplicationGroupNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroupResponseReplicationGroup` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node group
    is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled) replication
      group contains only 1 node group; therefore, the node group ID is 0001. A Redis
      (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
      0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` . This
          member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroupResponseReplicationGroup` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientDeleteReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientDeleteReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientDeleteReplicationGroupResponseReplicationGroupNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": ClientDeleteReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDeleteReplicationGroupResponseReplicationGroupTypeDef(
    _ClientDeleteReplicationGroupResponseReplicationGroupTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroupResponse` `ReplicationGroup`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , ``modifying``
      , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node group
        is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled) replication
          group contains only 1 node group; therefore, the node group ID is 0001. A Redis
          (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
          0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` . This
              member is only applicable for Redis (cluster mode disabled) replication groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
      range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientDeleteReplicationGroupResponseTypeDef = TypedDict(
    "_ClientDeleteReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientDeleteReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)


class ClientDeleteReplicationGroupResponseTypeDef(
    _ClientDeleteReplicationGroupResponseTypeDef
):
    """
    Type definition for `ClientDeleteReplicationGroup` `Response`

    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.

      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.

      - **Description** *(string) --*

        The user supplied description of the replication group.

      - **Status** *(string) --*

        The current state of this replication group - ``creating`` , ``available`` , ``modifying``
        , ``deleting`` , ``create-failed`` , ``snapshotting`` .

      - **PendingModifiedValues** *(dict) --*

        A group of settings to be applied to the replication group, either immediately or during
        the next maintenance window.

        - **PrimaryClusterId** *(string) --*

          The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
          specified), or during the next maintenance window.

        - **AutomaticFailoverStatus** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **Resharding** *(dict) --*

          The status of an online resharding operation.

          - **SlotMigration** *(dict) --*

            Represents the progress of an online resharding operation.

            - **ProgressPercentage** *(float) --*

              The percentage of the slot migration that is complete.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **MemberClusters** *(list) --*

        The names of all the cache clusters that are part of this replication group.

        - *(string) --*

      - **NodeGroups** *(list) --*

        A list of node groups in this replication group. For Redis (cluster mode disabled)
        replication groups, this is a single-element list. For Redis (cluster mode enabled)
        replication groups, the list contains an entry for each node group (shard).

        - *(dict) --*

          Represents a collection of cache nodes in a replication group. One node in the node group
          is the read/write primary node. All the other nodes are read-only Replica nodes.

          - **NodeGroupId** *(string) --*

            The identifier for the node group (shard). A Redis (cluster mode disabled) replication
            group contains only 1 node group; therefore, the node group ID is 0001. A Redis
            (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
            0090. Optionally, the user can provide the id for a node group.

          - **Status** *(string) --*

            The current state of this replication group - ``creating`` , ``available`` , etc.

          - **PrimaryEndpoint** *(dict) --*

            The endpoint of the primary node in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ReaderEndpoint** *(dict) --*

            The endpoint of the replica nodes in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **Slots** *(string) --*

            The keyspace for this node group (shard).

          - **NodeGroupMembers** *(list) --*

            A list containing information about individual nodes within the node group (shard).

            - *(dict) --*

              Represents a single node within a node group (shard).

              - **CacheClusterId** *(string) --*

                The ID of the cluster to which the node belongs.

              - **CacheNodeId** *(string) --*

                The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                0002, etc.).

              - **ReadEndpoint** *(dict) --*

                The information required for client programs to connect to a node for read
                operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                clusters.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the node is located.

              - **CurrentRole** *(string) --*

                The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                member is only applicable for Redis (cluster mode disabled) replication groups.

      - **SnapshottingClusterId** *(string) --*

        The cluster ID that is used as the daily snapshot source for the replication group.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **ConfigurationEndpoint** *(dict) --*

        The configuration endpoint for this replication group. Use the configuration endpoint to
        connect to this replication group.

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
        range.

        .. note::

          This parameter is only valid if the ``Engine`` parameter is ``redis`` .

      - **ClusterEnabled** *(boolean) --*

        A flag indicating whether or not this replication group is cluster enabled; i.e., whether
        its data can be partitioned across multiple shards (API/CLI: node groups).

        Valid values: ``true`` | ``false``

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for each node in the replication
        group.

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "_ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef(
    _ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef
):
    """
    Type definition for `ClientDeleteSnapshotResponseSnapshotNodeSnapshots` `NodeGroupConfiguration`

    The configuration for the source node group (shard).

    - **NodeGroupId** *(string) --*

      Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
      node group these configuration values apply to.

    - **Slots** *(string) --*

      A string that specifies the keyspace for a particular node group. Keyspaces range
      from 0 to 16,383. The string is in the format ``startkey-endkey`` .

      Example: ``"0-3999"``

    - **ReplicaCount** *(integer) --*

      The number of read replica nodes in this node group (shard).

    - **PrimaryAvailabilityZone** *(string) --*

      The Availability Zone where the primary node of this node group (shard) is launched.

    - **ReplicaAvailabilityZones** *(list) --*

      A list of Availability Zones to be used for the read replicas. The number of
      Availability Zones in this list must match the value of ``ReplicaCount`` or
      ``ReplicasPerNodeGroup`` if not specified.

      - *(string) --*
    """


_ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef = TypedDict(
    "_ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientDeleteSnapshotResponseSnapshotNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)


class ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef(
    _ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef
):
    """
    Type definition for `ClientDeleteSnapshotResponseSnapshot` `NodeSnapshots`

    Represents an individual cache node in a snapshot of a cluster.

    - **CacheClusterId** *(string) --*

      A unique identifier for the source cluster.

    - **NodeGroupId** *(string) --*

      A unique identifier for the source node group (shard).

    - **CacheNodeId** *(string) --*

      The cache node identifier for the node in the source cluster.

    - **NodeGroupConfiguration** *(dict) --*

      The configuration for the source node group (shard).

      - **NodeGroupId** *(string) --*

        Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
        node group these configuration values apply to.

      - **Slots** *(string) --*

        A string that specifies the keyspace for a particular node group. Keyspaces range
        from 0 to 16,383. The string is in the format ``startkey-endkey`` .

        Example: ``"0-3999"``

      - **ReplicaCount** *(integer) --*

        The number of read replica nodes in this node group (shard).

      - **PrimaryAvailabilityZone** *(string) --*

        The Availability Zone where the primary node of this node group (shard) is launched.

      - **ReplicaAvailabilityZones** *(list) --*

        A list of Availability Zones to be used for the read replicas. The number of
        Availability Zones in this list must match the value of ``ReplicaCount`` or
        ``ReplicasPerNodeGroup`` if not specified.

        - *(string) --*

    - **CacheSize** *(string) --*

      The size of the cache on the source cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created in the source cluster.

    - **SnapshotCreateTime** *(datetime) --*

      The date and time when the source node's metadata and cache data set was obtained for
      the snapshot.
    """


_ClientDeleteSnapshotResponseSnapshotTypeDef = TypedDict(
    "_ClientDeleteSnapshotResponseSnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": str,
        "NodeSnapshots": List[ClientDeleteSnapshotResponseSnapshotNodeSnapshotsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDeleteSnapshotResponseSnapshotTypeDef(
    _ClientDeleteSnapshotResponseSnapshotTypeDef
):
    """
    Type definition for `ClientDeleteSnapshotResponse` `Snapshot`

    Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

    - **SnapshotName** *(string) --*

      The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
      manual snapshot, this is the user-provided name.

    - **ReplicationGroupId** *(string) --*

      The unique identifier of the source replication group.

    - **ReplicationGroupDescription** *(string) --*

      A description of the source replication group.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the source cluster.

    - **SnapshotStatus** *(string) --*

      The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
      ``copying`` | ``deleting`` .

    - **SnapshotSource** *(string) --*

      Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created
      manually (``manual`` ).

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the source cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared to
      their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
         ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
        node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine version that is used by the source cluster.

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the source cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the source cluster is located.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the source cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It is
      specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
      maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
      notifications.

    - **Port** *(integer) --*

      The port number used by each cache nodes in the source cluster.

    - **CacheParameterGroupName** *(string) --*

      The cache parameter group that is associated with the source cluster.

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the source cluster.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
      source cluster.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SnapshotRetentionLimit** *(integer) --*

      For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
      before deleting it.

      For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
      cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do
      not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

       **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
       turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range during which ElastiCache takes daily snapshots of the source cluster.

    - **NumNodeGroups** *(integer) --*

      The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
      number of node groups (shards) in the snapshot and in the restored replication group must
      be the same.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for the source Redis replication
      group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **NodeSnapshots** *(list) --*

      A list of the cache nodes in the source cluster.

      - *(dict) --*

        Represents an individual cache node in a snapshot of a cluster.

        - **CacheClusterId** *(string) --*

          A unique identifier for the source cluster.

        - **NodeGroupId** *(string) --*

          A unique identifier for the source node group (shard).

        - **CacheNodeId** *(string) --*

          The cache node identifier for the node in the source cluster.

        - **NodeGroupConfiguration** *(dict) --*

          The configuration for the source node group (shard).

          - **NodeGroupId** *(string) --*

            Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
            node group these configuration values apply to.

          - **Slots** *(string) --*

            A string that specifies the keyspace for a particular node group. Keyspaces range
            from 0 to 16,383. The string is in the format ``startkey-endkey`` .

            Example: ``"0-3999"``

          - **ReplicaCount** *(integer) --*

            The number of read replica nodes in this node group (shard).

          - **PrimaryAvailabilityZone** *(string) --*

            The Availability Zone where the primary node of this node group (shard) is launched.

          - **ReplicaAvailabilityZones** *(list) --*

            A list of Availability Zones to be used for the read replicas. The number of
            Availability Zones in this list must match the value of ``ReplicaCount`` or
            ``ReplicasPerNodeGroup`` if not specified.

            - *(string) --*

        - **CacheSize** *(string) --*

          The size of the cache on the source cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created in the source cluster.

        - **SnapshotCreateTime** *(datetime) --*

          The date and time when the source node's metadata and cache data set was obtained for
          the snapshot.

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the snapshot.
    """


_ClientDeleteSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteSnapshotResponseTypeDef",
    {"Snapshot": ClientDeleteSnapshotResponseSnapshotTypeDef},
    total=False,
)


class ClientDeleteSnapshotResponseTypeDef(_ClientDeleteSnapshotResponseTypeDef):
    """
    Type definition for `ClientDeleteSnapshot` `Response`

    - **Snapshot** *(dict) --*

      Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

      - **SnapshotName** *(string) --*

        The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
        manual snapshot, this is the user-provided name.

      - **ReplicationGroupId** *(string) --*

        The unique identifier of the source replication group.

      - **ReplicationGroupDescription** *(string) --*

        A description of the source replication group.

      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the source cluster.

      - **SnapshotStatus** *(string) --*

        The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
        ``copying`` | ``deleting`` .

      - **SnapshotSource** *(string) --*

        Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created
        manually (``manual`` ).

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for the source cluster.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared to
        their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
           ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
          node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

      - **Engine** *(string) --*

        The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

      - **EngineVersion** *(string) --*

        The version of the cache engine version that is used by the source cluster.

      - **NumCacheNodes** *(integer) --*

        The number of cache nodes in the source cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **PreferredAvailabilityZone** *(string) --*

        The name of the Availability Zone in which the source cluster is located.

      - **CacheClusterCreateTime** *(datetime) --*

        The date and time when the source cluster was created.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which maintenance on the cluster is performed. It is
        specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
        maintenance window is a 60 minute period.

        Valid values for ``ddd`` are:

        * ``sun``

        * ``mon``

        * ``tue``

        * ``wed``

        * ``thu``

        * ``fri``

        * ``sat``

        Example: ``sun:23:00-mon:01:30``

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
        notifications.

      - **Port** *(integer) --*

        The port number used by each cache nodes in the source cluster.

      - **CacheParameterGroupName** *(string) --*

        The cache parameter group that is associated with the source cluster.

      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group associated with the source cluster.

      - **VpcId** *(string) --*

        The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
        source cluster.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        This parameter is currently disabled.

      - **SnapshotRetentionLimit** *(integer) --*

        For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
        before deleting it.

        For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
        cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do
        not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

         **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
         turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range during which ElastiCache takes daily snapshots of the source cluster.

      - **NumNodeGroups** *(integer) --*

        The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
        number of node groups (shards) in the snapshot and in the restored replication group must
        be the same.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for the source Redis replication
        group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **NodeSnapshots** *(list) --*

        A list of the cache nodes in the source cluster.

        - *(dict) --*

          Represents an individual cache node in a snapshot of a cluster.

          - **CacheClusterId** *(string) --*

            A unique identifier for the source cluster.

          - **NodeGroupId** *(string) --*

            A unique identifier for the source node group (shard).

          - **CacheNodeId** *(string) --*

            The cache node identifier for the node in the source cluster.

          - **NodeGroupConfiguration** *(dict) --*

            The configuration for the source node group (shard).

            - **NodeGroupId** *(string) --*

              Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
              node group these configuration values apply to.

            - **Slots** *(string) --*

              A string that specifies the keyspace for a particular node group. Keyspaces range
              from 0 to 16,383. The string is in the format ``startkey-endkey`` .

              Example: ``"0-3999"``

            - **ReplicaCount** *(integer) --*

              The number of read replica nodes in this node group (shard).

            - **PrimaryAvailabilityZone** *(string) --*

              The Availability Zone where the primary node of this node group (shard) is launched.

            - **ReplicaAvailabilityZones** *(list) --*

              A list of Availability Zones to be used for the read replicas. The number of
              Availability Zones in this list must match the value of ``ReplicaCount`` or
              ``ReplicasPerNodeGroup`` if not specified.

              - *(string) --*

          - **CacheSize** *(string) --*

            The size of the cache on the source cache node.

          - **CacheNodeCreateTime** *(datetime) --*

            The date and time when the cache node was created in the source cluster.

          - **SnapshotCreateTime** *(datetime) --*

            The date and time when the source node's metadata and cache data set was obtained for
            the snapshot.

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the snapshot.
    """


_ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef
):
    """
    Type definition for `ClientDescribeCacheClustersResponseCacheClustersCacheNodes` `Endpoint`

    The hostname for connecting to this cache node.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientDescribeCacheClustersResponseCacheClustersCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef
):
    """
    Type definition for `ClientDescribeCacheClustersResponseCacheClusters` `CacheNodes`

    Represents an individual cache node within a cluster. Each cache node runs its own
    instance of the cluster's protocol-compliant caching software - either Memcached or
    Redis.

    The following node types are supported by ElastiCache. Generally speaking, the current
    generation types provide more memory and computational power at lower cost when
    compared to their equivalent previous generation counterparts.

    * General purpose:

      * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge``
      , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
      ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge``
      , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
      types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

      * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
      **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
      ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
      ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

    * Compute optimized:

      * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

    * Memory optimized:

      * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge``
      , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
      ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge``
      , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
      ``cache.r4.16xlarge``

      * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
      ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large``
      , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` ,
      ``cache.r3.8xlarge``

     **Additional node type info**

    * All current generation instance types are created in Amazon VPC by default.

    * Redis append-only files (AOF) are not supported for T1 or T2 instances.

    * Redis Multi-AZ with automatic failover is not supported on T1 instances.

    * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
    Redis version 2.8.22 and later.

    - **CacheNodeId** *(string) --*

      The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
      combination of cluster ID and node ID uniquely identifies every cache node used in a
      customer's AWS account.

    - **CacheNodeStatus** *(string) --*

      The current state of this cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created.

    - **Endpoint** *(dict) --*

      The hostname for connecting to this cache node.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group applied to this cache node.

    - **SourceCacheNodeId** *(string) --*

      The ID of the primary node to which this read replica node is synchronized. If this
      field is empty, this node is not associated with a primary cluster.

    - **CustomerAvailabilityZone** *(string) --*

      The Availability Zone where this node was created and now resides.
    """


_ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef
):
    """
    Type definition for `ClientDescribeCacheClustersResponseCacheClusters` `CacheParameterGroup`

    Status of the cache parameter group.

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **CacheNodeIdsToReboot** *(list) --*

      A list of the cache node IDs which need to be rebooted for parameter changes to be
      applied. A node ID is a numeric identifier (0001, 0002, etc.).

      - *(string) --*
    """


_ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeCacheClustersResponseCacheClusters` `CacheSecurityGroups`

    Represents a cluster's status within a particular cache security group.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Status** *(string) --*

      The membership status in the cache security group. The status changes when a cache
      security group is modified, or when the cache security groups assigned to a cluster
      are modified.
    """


_ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientDescribeCacheClustersResponseCacheClusters` `ConfigurationEndpoint`

    Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
    cluster, can be used by an application to connect to any node in the cluster. The
    configuration endpoint will always have ``.cfg`` in it.

    Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeCacheClustersResponseCacheClusters` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for
    publishing ElastiCache events to subscribers using Amazon Simple Notification Service
    (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDescribeCacheClustersResponseCacheClusters` `PendingModifiedValues`

    A group of settings that are applied to the cluster in the future, or that are currently
    being applied.

    - **NumCacheNodes** *(integer) --*

      The new number of cache nodes for the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **CacheNodeIdsToRemove** *(list) --*

      A list of cache node IDs that are being removed (or will be removed) from the cluster.
      A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

      - *(string) --*

    - **EngineVersion** *(string) --*

      The new cache engine version that the cluster runs.

    - **CacheNodeType** *(string) --*

      The cache node type that this cluster or replication group is scaled to.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeCacheClustersResponseCacheClusters` `SecurityGroups`

    Represents a single cache security group and its status.

    - **SecurityGroupId** *(string) --*

      The identifier of the cache security group.

    - **Status** *(string) --*

      The status of the cache security group membership. The status changes whenever a
      cache security group is modified, or when the cache security groups assigned to a
      cluster are modified.
    """


_ClientDescribeCacheClustersResponseCacheClustersTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseCacheClustersTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientDescribeCacheClustersResponseCacheClustersConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeCacheClustersResponseCacheClustersPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientDescribeCacheClustersResponseCacheClustersNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientDescribeCacheClustersResponseCacheClustersCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientDescribeCacheClustersResponseCacheClustersCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[
            ClientDescribeCacheClustersResponseCacheClustersCacheNodesTypeDef
        ],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[
            ClientDescribeCacheClustersResponseCacheClustersSecurityGroupsTypeDef
        ],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class ClientDescribeCacheClustersResponseCacheClustersTypeDef(
    _ClientDescribeCacheClustersResponseCacheClustersTypeDef
):
    """
    Type definition for `ClientDescribeCacheClustersResponse` `CacheClusters`

    Contains all of the attributes of a specific cluster.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the cluster. This identifier is a unique key that
      identifies a cluster.

    - **ConfigurationEndpoint** *(dict) --*

      Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
      cluster, can be used by an application to connect to any node in the cluster. The
      configuration endpoint will always have ``.cfg`` in it.

      Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ClientDownloadLandingPage** *(string) --*

      The URL of the web page where you can download the latest ElastiCache client library.

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared
      to their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
        types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
        **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
        ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine that is used in this cluster.

    - **CacheClusterStatus** *(string) --*

      The current state of this cluster, one of the following values: ``available`` ,
      ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
      ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the cluster is located or "Multiple" if the
      cache nodes are located in different Availability Zones.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It
      is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The
      minimum maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **PendingModifiedValues** *(dict) --*

      A group of settings that are applied to the cluster in the future, or that are currently
      being applied.

      - **NumCacheNodes** *(integer) --*

        The new number of cache nodes for the cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **CacheNodeIdsToRemove** *(list) --*

        A list of cache node IDs that are being removed (or will be removed) from the cluster.
        A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

        - *(string) --*

      - **EngineVersion** *(string) --*

        The new cache engine version that the cluster runs.

      - **CacheNodeType** *(string) --*

        The cache node type that this cluster or replication group is scaled to.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for
      publishing ElastiCache events to subscribers using Amazon Simple Notification Service
      (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **CacheSecurityGroups** *(list) --*

      A list of cache security group elements, composed of name and status sub-elements.

      - *(dict) --*

        Represents a cluster's status within a particular cache security group.

        - **CacheSecurityGroupName** *(string) --*

          The name of the cache security group.

        - **Status** *(string) --*

          The membership status in the cache security group. The status changes when a cache
          security group is modified, or when the cache security groups assigned to a cluster
          are modified.

    - **CacheParameterGroup** *(dict) --*

      Status of the cache parameter group.

      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **CacheNodeIdsToReboot** *(list) --*

        A list of the cache node IDs which need to be rebooted for parameter changes to be
        applied. A node ID is a numeric identifier (0001, 0002, etc.).

        - *(string) --*

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the cluster.

    - **CacheNodes** *(list) --*

      A list of cache nodes that are members of the cluster.

      - *(dict) --*

        Represents an individual cache node within a cluster. Each cache node runs its own
        instance of the cluster's protocol-compliant caching software - either Memcached or
        Redis.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when
        compared to their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge``
          , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge``
          , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
          types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
          **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge``
          , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge``
          , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
          ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large``
          , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` ,
          ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

        - **CacheNodeId** *(string) --*

          The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
          combination of cluster ID and node ID uniquely identifies every cache node used in a
          customer's AWS account.

        - **CacheNodeStatus** *(string) --*

          The current state of this cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created.

        - **Endpoint** *(dict) --*

          The hostname for connecting to this cache node.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group applied to this cache node.

        - **SourceCacheNodeId** *(string) --*

          The ID of the primary node to which this read replica node is synchronized. If this
          field is empty, this node is not associated with a primary cluster.

        - **CustomerAvailabilityZone** *(string) --*

          The Availability Zone where this node was created and now resides.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SecurityGroups** *(list) --*

      A list of VPC Security Groups associated with the cluster.

      - *(dict) --*

        Represents a single cache security group and its status.

        - **SecurityGroupId** *(string) --*

          The identifier of the cache security group.

        - **Status** *(string) --*

          The status of the cache security group membership. The status changes whenever a
          cache security group is modified, or when the cache security groups assigned to a
          cluster are modified.

    - **ReplicationGroupId** *(string) --*

      The replication group to which this cluster belongs. If this field is empty, the cluster
      is not associated with any replication group.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that
      was taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your cluster.

      Example: ``05:00-09:00``

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created.
      To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``
    """


_ClientDescribeCacheClustersResponseTypeDef = TypedDict(
    "_ClientDescribeCacheClustersResponseTypeDef",
    {
        "Marker": str,
        "CacheClusters": List[ClientDescribeCacheClustersResponseCacheClustersTypeDef],
    },
    total=False,
)


class ClientDescribeCacheClustersResponseTypeDef(
    _ClientDescribeCacheClustersResponseTypeDef
):
    """
    Type definition for `ClientDescribeCacheClusters` `Response`

    Represents the output of a ``DescribeCacheClusters`` operation.

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **CacheClusters** *(list) --*

      A list of clusters. Each item in the list contains detailed information about one cluster.

      - *(dict) --*

        Contains all of the attributes of a specific cluster.

        - **CacheClusterId** *(string) --*

          The user-supplied identifier of the cluster. This identifier is a unique key that
          identifies a cluster.

        - **ConfigurationEndpoint** *(dict) --*

          Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
          cluster, can be used by an application to connect to any node in the cluster. The
          configuration endpoint will always have ``.cfg`` in it.

          Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ClientDownloadLandingPage** *(string) --*

          The URL of the web page where you can download the latest ElastiCache client library.

        - **CacheNodeType** *(string) --*

          The name of the compute and memory capacity node type for the cluster.

          The following node types are supported by ElastiCache. Generally speaking, the current
          generation types provide more memory and computational power at lower cost when compared
          to their equivalent previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
            ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
            ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
            types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
            **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
            ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
            ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
            ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
            ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
            ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
          Redis version 2.8.22 and later.

        - **Engine** *(string) --*

          The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

        - **EngineVersion** *(string) --*

          The version of the cache engine that is used in this cluster.

        - **CacheClusterStatus** *(string) --*

          The current state of this cluster, one of the following values: ``available`` ,
          ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
          ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

        - **NumCacheNodes** *(integer) --*

          The number of cache nodes in the cluster.

          For clusters running Redis, this value must be 1. For clusters running Memcached, this
          value must be between 1 and 20.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the cluster is located or "Multiple" if the
          cache nodes are located in different Availability Zones.

        - **CacheClusterCreateTime** *(datetime) --*

          The date and time when the cluster was created.

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which maintenance on the cluster is performed. It
          is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The
          minimum maintenance window is a 60 minute period.

          Valid values for ``ddd`` are:

          * ``sun``

          * ``mon``

          * ``tue``

          * ``wed``

          * ``thu``

          * ``fri``

          * ``sat``

          Example: ``sun:23:00-mon:01:30``

        - **PendingModifiedValues** *(dict) --*

          A group of settings that are applied to the cluster in the future, or that are currently
          being applied.

          - **NumCacheNodes** *(integer) --*

            The new number of cache nodes for the cluster.

            For clusters running Redis, this value must be 1. For clusters running Memcached, this
            value must be between 1 and 20.

          - **CacheNodeIdsToRemove** *(list) --*

            A list of cache node IDs that are being removed (or will be removed) from the cluster.
            A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

            - *(string) --*

          - **EngineVersion** *(string) --*

            The new cache engine version that the cluster runs.

          - **CacheNodeType** *(string) --*

            The cache node type that this cluster or replication group is scaled to.

          - **AuthTokenStatus** *(string) --*

            The auth token status

        - **NotificationConfiguration** *(dict) --*

          Describes a notification topic and its status. Notification topics are used for
          publishing ElastiCache events to subscribers using Amazon Simple Notification Service
          (SNS).

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the topic.

          - **TopicStatus** *(string) --*

            The current state of the topic.

        - **CacheSecurityGroups** *(list) --*

          A list of cache security group elements, composed of name and status sub-elements.

          - *(dict) --*

            Represents a cluster's status within a particular cache security group.

            - **CacheSecurityGroupName** *(string) --*

              The name of the cache security group.

            - **Status** *(string) --*

              The membership status in the cache security group. The status changes when a cache
              security group is modified, or when the cache security groups assigned to a cluster
              are modified.

        - **CacheParameterGroup** *(dict) --*

          Status of the cache parameter group.

          - **CacheParameterGroupName** *(string) --*

            The name of the cache parameter group.

          - **ParameterApplyStatus** *(string) --*

            The status of parameter updates.

          - **CacheNodeIdsToReboot** *(list) --*

            A list of the cache node IDs which need to be rebooted for parameter changes to be
            applied. A node ID is a numeric identifier (0001, 0002, etc.).

            - *(string) --*

        - **CacheSubnetGroupName** *(string) --*

          The name of the cache subnet group associated with the cluster.

        - **CacheNodes** *(list) --*

          A list of cache nodes that are members of the cluster.

          - *(dict) --*

            Represents an individual cache node within a cluster. Each cache node runs its own
            instance of the cluster's protocol-compliant caching software - either Memcached or
            Redis.

            The following node types are supported by ElastiCache. Generally speaking, the current
            generation types provide more memory and computational power at lower cost when
            compared to their equivalent previous generation counterparts.

            * General purpose:

              * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge``
              , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
              ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge``
              , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
              types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

              * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
              **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
              ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
              ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

            * Compute optimized:

              * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

            * Memory optimized:

              * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge``
              , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
              ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge``
              , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
              ``cache.r4.16xlarge``

              * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
              ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large``
              , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` ,
              ``cache.r3.8xlarge``

             **Additional node type info**

            * All current generation instance types are created in Amazon VPC by default.

            * Redis append-only files (AOF) are not supported for T1 or T2 instances.

            * Redis Multi-AZ with automatic failover is not supported on T1 instances.

            * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
            Redis version 2.8.22 and later.

            - **CacheNodeId** *(string) --*

              The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
              combination of cluster ID and node ID uniquely identifies every cache node used in a
              customer's AWS account.

            - **CacheNodeStatus** *(string) --*

              The current state of this cache node.

            - **CacheNodeCreateTime** *(datetime) --*

              The date and time when the cache node was created.

            - **Endpoint** *(dict) --*

              The hostname for connecting to this cache node.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **ParameterGroupStatus** *(string) --*

              The status of the parameter group applied to this cache node.

            - **SourceCacheNodeId** *(string) --*

              The ID of the primary node to which this read replica node is synchronized. If this
              field is empty, this node is not associated with a primary cluster.

            - **CustomerAvailabilityZone** *(string) --*

              The Availability Zone where this node was created and now resides.

        - **AutoMinorVersionUpgrade** *(boolean) --*

          This parameter is currently disabled.

        - **SecurityGroups** *(list) --*

          A list of VPC Security Groups associated with the cluster.

          - *(dict) --*

            Represents a single cache security group and its status.

            - **SecurityGroupId** *(string) --*

              The identifier of the cache security group.

            - **Status** *(string) --*

              The status of the cache security group membership. The status changes whenever a
              cache security group is modified, or when the cache security groups assigned to a
              cluster are modified.

        - **ReplicationGroupId** *(string) --*

          The replication group to which this cluster belongs. If this field is empty, the cluster
          is not associated with any replication group.

        - **SnapshotRetentionLimit** *(integer) --*

          The number of days for which ElastiCache retains automatic cluster snapshots before
          deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that
          was taken today is retained for 5 days before being deleted.

          .. warning::

            If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

        - **SnapshotWindow** *(string) --*

          The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
          your cluster.

          Example: ``05:00-09:00``

        - **AuthTokenEnabled** *(boolean) --*

          A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

          Default: ``false``

        - **AuthTokenLastModifiedDate** *(datetime) --*

          The date the auth token was last modified

        - **TransitEncryptionEnabled** *(boolean) --*

          A flag that enables in-transit encryption when set to ``true`` .

          You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
          To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
          ``true`` when you create a cluster.

           **Required:** Only available when creating a replication group in an Amazon VPC using
           redis version ``3.2.6`` , ``4.x`` or later.

          Default: ``false``

        - **AtRestEncryptionEnabled** *(boolean) --*

          A flag that enables encryption at-rest when set to ``true`` .

          You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created.
          To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to
          ``true`` when you create a cluster.

           **Required:** Only available when creating a replication group in an Amazon VPC using
           redis version ``3.2.6`` , ``4.x`` or later.

          Default: ``false``
    """


_ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef = TypedDict(
    "_ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "CacheEngineDescription": str,
        "CacheEngineVersionDescription": str,
    },
    total=False,
)


class ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef(
    _ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef
):
    """
    Type definition for `ClientDescribeCacheEngineVersionsResponse` `CacheEngineVersions`

    Provides all of the details about a particular cache engine version.

    - **Engine** *(string) --*

      The name of the cache engine.

    - **EngineVersion** *(string) --*

      The version number of the cache engine.

    - **CacheParameterGroupFamily** *(string) --*

      The name of the cache parameter group family associated with this cache engine.

      Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
      ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

    - **CacheEngineDescription** *(string) --*

      The description of the cache engine.

    - **CacheEngineVersionDescription** *(string) --*

      The description of the cache engine version.
    """


_ClientDescribeCacheEngineVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeCacheEngineVersionsResponseTypeDef",
    {
        "Marker": str,
        "CacheEngineVersions": List[
            ClientDescribeCacheEngineVersionsResponseCacheEngineVersionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheEngineVersionsResponseTypeDef(
    _ClientDescribeCacheEngineVersionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeCacheEngineVersions` `Response`

    Represents the output of a  DescribeCacheEngineVersions operation.

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **CacheEngineVersions** *(list) --*

      A list of cache engine version details. Each element in the list contains detailed
      information about one cache engine version.

      - *(dict) --*

        Provides all of the details about a particular cache engine version.

        - **Engine** *(string) --*

          The name of the cache engine.

        - **EngineVersion** *(string) --*

          The version number of the cache engine.

        - **CacheParameterGroupFamily** *(string) --*

          The name of the cache parameter group family associated with this cache engine.

          Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
          ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

        - **CacheEngineDescription** *(string) --*

          The description of the cache engine.

        - **CacheEngineVersionDescription** *(string) --*

          The description of the cache engine version.
    """


_ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef",
    {
        "CacheParameterGroupName": str,
        "CacheParameterGroupFamily": str,
        "Description": str,
    },
    total=False,
)


class ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef(
    _ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef
):
    """
    Type definition for `ClientDescribeCacheParameterGroupsResponse` `CacheParameterGroups`

    Represents the output of a ``CreateCacheParameterGroup`` operation.

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.

    - **CacheParameterGroupFamily** *(string) --*

      The name of the cache parameter group family that this cache parameter group is
      compatible with.

      Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
      ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

    - **Description** *(string) --*

      The description for this cache parameter group.
    """


_ClientDescribeCacheParameterGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeCacheParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheParameterGroups": List[
            ClientDescribeCacheParameterGroupsResponseCacheParameterGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheParameterGroupsResponseTypeDef(
    _ClientDescribeCacheParameterGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeCacheParameterGroups` `Response`

    Represents the output of a ``DescribeCacheParameterGroups`` operation.

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **CacheParameterGroups** *(list) --*

      A list of cache parameter groups. Each element in the list contains detailed information
      about one cache parameter group.

      - *(dict) --*

        Represents the output of a ``CreateCacheParameterGroup`` operation.

        - **CacheParameterGroupName** *(string) --*

          The name of the cache parameter group.

        - **CacheParameterGroupFamily** *(string) --*

          The name of the cache parameter group family that this cache parameter group is
          compatible with.

          Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
          ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

        - **Description** *(string) --*

          The description for this cache parameter group.
    """


_ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "_ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)


class ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef(
    _ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
):
    """
    Type definition for `ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParameters` `CacheNodeTypeSpecificValues`

    A value that applies only to a certain cache node type.

    - **CacheNodeType** *(string) --*

      The cache node type for which this value applies.

    - **Value** *(string) --*

      The value for the cache node type.
    """


_ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "_ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[
            ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
        ],
        "ChangeType": str,
    },
    total=False,
)


class ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef(
    _ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef
):
    """
    Type definition for `ClientDescribeCacheParametersResponse` `CacheNodeTypeSpecificParameters`

    A parameter that has a different value for each cache node type it is applied to. For
    example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
    ``maxmemory`` value than a ``cache.m1.small`` type.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **Description** *(string) --*

      A description of the parameter.

    - **Source** *(string) --*

      The source of the parameter value.

    - **DataType** *(string) --*

      The valid data type for the parameter.

    - **AllowedValues** *(string) --*

      The valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest cache engine version to which the parameter can apply.

    - **CacheNodeTypeSpecificValues** *(list) --*

      A list of cache node types and their corresponding values for this parameter.

      - *(dict) --*

        A value that applies only to a certain cache node type.

        - **CacheNodeType** *(string) --*

          The cache node type for which this value applies.

        - **Value** *(string) --*

          The value for the cache node type.

    - **ChangeType** *(string) --*

      Indicates whether a change to the parameter is applied immediately or requires a reboot
      for the change to be applied. You can force a reboot or wait until the next maintenance
      window's reboot. For more information, see `Rebooting a Cluster
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .
    """


_ClientDescribeCacheParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeCacheParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": str,
    },
    total=False,
)


class ClientDescribeCacheParametersResponseParametersTypeDef(
    _ClientDescribeCacheParametersResponseParametersTypeDef
):
    """
    Type definition for `ClientDescribeCacheParametersResponse` `Parameters`

    Describes an individual setting that controls some aspect of ElastiCache behavior.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The value of the parameter.

    - **Description** *(string) --*

      A description of the parameter.

    - **Source** *(string) --*

      The source of the parameter.

    - **DataType** *(string) --*

      The valid data type for the parameter.

    - **AllowedValues** *(string) --*

      The valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest cache engine version to which the parameter can apply.

    - **ChangeType** *(string) --*

      Indicates whether a change to the parameter is applied immediately or requires a reboot
      for the change to be applied. You can force a reboot or wait until the next maintenance
      window's reboot. For more information, see `Rebooting a Cluster
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .
    """


_ClientDescribeCacheParametersResponseTypeDef = TypedDict(
    "_ClientDescribeCacheParametersResponseTypeDef",
    {
        "Marker": str,
        "Parameters": List[ClientDescribeCacheParametersResponseParametersTypeDef],
        "CacheNodeTypeSpecificParameters": List[
            ClientDescribeCacheParametersResponseCacheNodeTypeSpecificParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheParametersResponseTypeDef(
    _ClientDescribeCacheParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeCacheParameters` `Response`

    Represents the output of a ``DescribeCacheParameters`` operation.

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **Parameters** *(list) --*

      A list of  Parameter instances.

      - *(dict) --*

        Describes an individual setting that controls some aspect of ElastiCache behavior.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterValue** *(string) --*

          The value of the parameter.

        - **Description** *(string) --*

          A description of the parameter.

        - **Source** *(string) --*

          The source of the parameter.

        - **DataType** *(string) --*

          The valid data type for the parameter.

        - **AllowedValues** *(string) --*

          The valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest cache engine version to which the parameter can apply.

        - **ChangeType** *(string) --*

          Indicates whether a change to the parameter is applied immediately or requires a reboot
          for the change to be applied. You can force a reboot or wait until the next maintenance
          window's reboot. For more information, see `Rebooting a Cluster
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .

    - **CacheNodeTypeSpecificParameters** *(list) --*

      A list of parameters specific to a particular cache node type. Each element in the list
      contains detailed information about one parameter.

      - *(dict) --*

        A parameter that has a different value for each cache node type it is applied to. For
        example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
        ``maxmemory`` value than a ``cache.m1.small`` type.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **Description** *(string) --*

          A description of the parameter.

        - **Source** *(string) --*

          The source of the parameter value.

        - **DataType** *(string) --*

          The valid data type for the parameter.

        - **AllowedValues** *(string) --*

          The valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest cache engine version to which the parameter can apply.

        - **CacheNodeTypeSpecificValues** *(list) --*

          A list of cache node types and their corresponding values for this parameter.

          - *(dict) --*

            A value that applies only to a certain cache node type.

            - **CacheNodeType** *(string) --*

              The cache node type for which this value applies.

            - **Value** *(string) --*

              The value for the cache node type.

        - **ChangeType** *(string) --*

          Indicates whether a change to the parameter is applied immediately or requires a reboot
          for the change to be applied. You can force a reboot or wait until the next maintenance
          window's reboot. For more information, see `Rebooting a Cluster
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .
    """


_ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)


class ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef(
    _ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroups` `EC2SecurityGroups`

    Provides ownership and status information for an Amazon EC2 security group.

    - **Status** *(string) --*

      The status of the Amazon EC2 security group.

    - **EC2SecurityGroupName** *(string) --*

      The name of the Amazon EC2 security group.

    - **EC2SecurityGroupOwnerId** *(string) --*

      The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef(
    _ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeCacheSecurityGroupsResponse` `CacheSecurityGroups`

    Represents the output of one of the following operations:

    * ``AuthorizeCacheSecurityGroupIngress``

    * ``CreateCacheSecurityGroup``

    * ``RevokeCacheSecurityGroupIngress``

    - **OwnerId** *(string) --*

      The AWS account ID of the cache security group owner.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Description** *(string) --*

      The description of the cache security group.

    - **EC2SecurityGroups** *(list) --*

      A list of Amazon EC2 security groups that are associated with this cache security group.

      - *(dict) --*

        Provides ownership and status information for an Amazon EC2 security group.

        - **Status** *(string) --*

          The status of the Amazon EC2 security group.

        - **EC2SecurityGroupName** *(string) --*

          The name of the Amazon EC2 security group.

        - **EC2SecurityGroupOwnerId** *(string) --*

          The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientDescribeCacheSecurityGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeCacheSecurityGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheSecurityGroups": List[
            ClientDescribeCacheSecurityGroupsResponseCacheSecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheSecurityGroupsResponseTypeDef(
    _ClientDescribeCacheSecurityGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeCacheSecurityGroups` `Response`

    Represents the output of a ``DescribeCacheSecurityGroups`` operation.

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **CacheSecurityGroups** *(list) --*

      A list of cache security groups. Each element in the list contains detailed information about
      one group.

      - *(dict) --*

        Represents the output of one of the following operations:

        * ``AuthorizeCacheSecurityGroupIngress``

        * ``CreateCacheSecurityGroup``

        * ``RevokeCacheSecurityGroupIngress``

        - **OwnerId** *(string) --*

          The AWS account ID of the cache security group owner.

        - **CacheSecurityGroupName** *(string) --*

          The name of the cache security group.

        - **Description** *(string) --*

          The description of the cache security group.

        - **EC2SecurityGroups** *(list) --*

          A list of Amazon EC2 security groups that are associated with this cache security group.

          - *(dict) --*

            Provides ownership and status information for an Amazon EC2 security group.

            - **Status** *(string) --*

              The status of the Amazon EC2 security group.

            - **EC2SecurityGroupName** *(string) --*

              The name of the Amazon EC2 security group.

            - **EC2SecurityGroupOwnerId** *(string) --*

              The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnets` `SubnetAvailabilityZone`

    The Availability Zone associated with the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef = TypedDict(
    "_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)


class ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef(
    _ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef
):
    """
    Type definition for `ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroups` `Subnets`

    Represents the subnet associated with a cluster. This parameter refers to subnets
    defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

    - **SubnetIdentifier** *(string) --*

      The unique identifier for the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone associated with the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.
    """


_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef = TypedDict(
    "_ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[
            ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef(
    _ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef
):
    """
    Type definition for `ClientDescribeCacheSubnetGroupsResponse` `CacheSubnetGroups`

    Represents the output of one of the following operations:

    * ``CreateCacheSubnetGroup``

    * ``ModifyCacheSubnetGroup``

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group.

    - **CacheSubnetGroupDescription** *(string) --*

      The description of the cache subnet group.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

    - **Subnets** *(list) --*

      A list of subnets associated with the cache subnet group.

      - *(dict) --*

        Represents the subnet associated with a cluster. This parameter refers to subnets
        defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

        - **SubnetIdentifier** *(string) --*

          The unique identifier for the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone associated with the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.
    """


_ClientDescribeCacheSubnetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeCacheSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "CacheSubnetGroups": List[
            ClientDescribeCacheSubnetGroupsResponseCacheSubnetGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeCacheSubnetGroupsResponseTypeDef(
    _ClientDescribeCacheSubnetGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeCacheSubnetGroups` `Response`

    Represents the output of a ``DescribeCacheSubnetGroups`` operation.

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **CacheSubnetGroups** *(list) --*

      A list of cache subnet groups. Each element in the list contains detailed information about
      one group.

      - *(dict) --*

        Represents the output of one of the following operations:

        * ``CreateCacheSubnetGroup``

        * ``ModifyCacheSubnetGroup``

        - **CacheSubnetGroupName** *(string) --*

          The name of the cache subnet group.

        - **CacheSubnetGroupDescription** *(string) --*

          The description of the cache subnet group.

        - **VpcId** *(string) --*

          The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

        - **Subnets** *(list) --*

          A list of subnets associated with the cache subnet group.

          - *(dict) --*

            Represents the subnet associated with a cluster. This parameter refers to subnets
            defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

            - **SubnetIdentifier** *(string) --*

              The unique identifier for the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              The Availability Zone associated with the subnet.

              - **Name** *(string) --*

                The name of the Availability Zone.
    """


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParameters` `CacheNodeTypeSpecificValues`

    A value that applies only to a certain cache node type.

    - **CacheNodeType** *(string) --*

      The cache node type for which this value applies.

    - **Value** *(string) --*

      The value for the cache node type.
    """


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
        ],
        "ChangeType": str,
    },
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultParametersResponseEngineDefaults` `CacheNodeTypeSpecificParameters`

    A parameter that has a different value for each cache node type it is applied to. For
    example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
    ``maxmemory`` value than a ``cache.m1.small`` type.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **Description** *(string) --*

      A description of the parameter.

    - **Source** *(string) --*

      The source of the parameter value.

    - **DataType** *(string) --*

      The valid data type for the parameter.

    - **AllowedValues** *(string) --*

      The valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being
      changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest cache engine version to which the parameter can apply.

    - **CacheNodeTypeSpecificValues** *(list) --*

      A list of cache node types and their corresponding values for this parameter.

      - *(dict) --*

        A value that applies only to a certain cache node type.

        - **CacheNodeType** *(string) --*

          The cache node type for which this value applies.

        - **Value** *(string) --*

          The value for the cache node type.

    - **ChangeType** *(string) --*

      Indicates whether a change to the parameter is applied immediately or requires a reboot
      for the change to be applied. You can force a reboot or wait until the next maintenance
      window's reboot. For more information, see `Rebooting a Cluster
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
      .
    """


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": str,
    },
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultParametersResponseEngineDefaults` `Parameters`

    Describes an individual setting that controls some aspect of ElastiCache behavior.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The value of the parameter.

    - **Description** *(string) --*

      A description of the parameter.

    - **Source** *(string) --*

      The source of the parameter.

    - **DataType** *(string) --*

      The valid data type for the parameter.

    - **AllowedValues** *(string) --*

      The valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being
      changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest cache engine version to which the parameter can apply.

    - **ChangeType** *(string) --*

      Indicates whether a change to the parameter is applied immediately or requires a reboot
      for the change to be applied. You can force a reboot or wait until the next maintenance
      window's reboot. For more information, see `Rebooting a Cluster
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
      .
    """


_ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef",
    {
        "CacheParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsParametersTypeDef
        ],
        "CacheNodeTypeSpecificParameters": List[
            ClientDescribeEngineDefaultParametersResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef(
    _ClientDescribeEngineDefaultParametersResponseEngineDefaultsTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultParametersResponse` `EngineDefaults`

    Represents the output of a ``DescribeEngineDefaultParameters`` operation.

    - **CacheParameterGroupFamily** *(string) --*

      Specifies the name of the cache parameter group family to which the engine default
      parameters apply.

      Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
      ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **Parameters** *(list) --*

      Contains a list of engine default parameters.

      - *(dict) --*

        Describes an individual setting that controls some aspect of ElastiCache behavior.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterValue** *(string) --*

          The value of the parameter.

        - **Description** *(string) --*

          A description of the parameter.

        - **Source** *(string) --*

          The source of the parameter.

        - **DataType** *(string) --*

          The valid data type for the parameter.

        - **AllowedValues** *(string) --*

          The valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being
          changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest cache engine version to which the parameter can apply.

        - **ChangeType** *(string) --*

          Indicates whether a change to the parameter is applied immediately or requires a reboot
          for the change to be applied. You can force a reboot or wait until the next maintenance
          window's reboot. For more information, see `Rebooting a Cluster
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
          .

    - **CacheNodeTypeSpecificParameters** *(list) --*

      A list of parameters specific to a particular cache node type. Each element in the list
      contains detailed information about one parameter.

      - *(dict) --*

        A parameter that has a different value for each cache node type it is applied to. For
        example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
        ``maxmemory`` value than a ``cache.m1.small`` type.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **Description** *(string) --*

          A description of the parameter.

        - **Source** *(string) --*

          The source of the parameter value.

        - **DataType** *(string) --*

          The valid data type for the parameter.

        - **AllowedValues** *(string) --*

          The valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being
          changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest cache engine version to which the parameter can apply.

        - **CacheNodeTypeSpecificValues** *(list) --*

          A list of cache node types and their corresponding values for this parameter.

          - *(dict) --*

            A value that applies only to a certain cache node type.

            - **CacheNodeType** *(string) --*

              The cache node type for which this value applies.

            - **Value** *(string) --*

              The value for the cache node type.

        - **ChangeType** *(string) --*

          Indicates whether a change to the parameter is applied immediately or requires a reboot
          for the change to be applied. You can force a reboot or wait until the next maintenance
          window's reboot. For more information, see `Rebooting a Cluster
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
          .
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

      Represents the output of a ``DescribeEngineDefaultParameters`` operation.

      - **CacheParameterGroupFamily** *(string) --*

        Specifies the name of the cache parameter group family to which the engine default
        parameters apply.

        Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
        ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.

      - **Parameters** *(list) --*

        Contains a list of engine default parameters.

        - *(dict) --*

          Describes an individual setting that controls some aspect of ElastiCache behavior.

          - **ParameterName** *(string) --*

            The name of the parameter.

          - **ParameterValue** *(string) --*

            The value of the parameter.

          - **Description** *(string) --*

            A description of the parameter.

          - **Source** *(string) --*

            The source of the parameter.

          - **DataType** *(string) --*

            The valid data type for the parameter.

          - **AllowedValues** *(string) --*

            The valid range of values for the parameter.

          - **IsModifiable** *(boolean) --*

            Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
            parameters have security or operational implications that prevent them from being
            changed.

          - **MinimumEngineVersion** *(string) --*

            The earliest cache engine version to which the parameter can apply.

          - **ChangeType** *(string) --*

            Indicates whether a change to the parameter is applied immediately or requires a reboot
            for the change to be applied. You can force a reboot or wait until the next maintenance
            window's reboot. For more information, see `Rebooting a Cluster
            <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
            .

      - **CacheNodeTypeSpecificParameters** *(list) --*

        A list of parameters specific to a particular cache node type. Each element in the list
        contains detailed information about one parameter.

        - *(dict) --*

          A parameter that has a different value for each cache node type it is applied to. For
          example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
          ``maxmemory`` value than a ``cache.m1.small`` type.

          - **ParameterName** *(string) --*

            The name of the parameter.

          - **Description** *(string) --*

            A description of the parameter.

          - **Source** *(string) --*

            The source of the parameter value.

          - **DataType** *(string) --*

            The valid data type for the parameter.

          - **AllowedValues** *(string) --*

            The valid range of values for the parameter.

          - **IsModifiable** *(boolean) --*

            Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
            parameters have security or operational implications that prevent them from being
            changed.

          - **MinimumEngineVersion** *(string) --*

            The earliest cache engine version to which the parameter can apply.

          - **CacheNodeTypeSpecificValues** *(list) --*

            A list of cache node types and their corresponding values for this parameter.

            - *(dict) --*

              A value that applies only to a certain cache node type.

              - **CacheNodeType** *(string) --*

                The cache node type for which this value applies.

              - **Value** *(string) --*

                The value for the cache node type.

          - **ChangeType** *(string) --*

            Indicates whether a change to the parameter is applied immediately or requires a reboot
            for the change to be applied. You can force a reboot or wait until the next maintenance
            window's reboot. For more information, see `Rebooting a Cluster
            <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
            .
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {"SourceIdentifier": str, "SourceType": str, "Message": str, "Date": datetime},
    total=False,
)


class ClientDescribeEventsResponseEventsTypeDef(
    _ClientDescribeEventsResponseEventsTypeDef
):
    """
    Type definition for `ClientDescribeEventsResponse` `Events`

    Represents a single occurrence of something interesting within the system. Some examples of
    events are creating a cluster, adding or removing a cache node, or rebooting a node.

    - **SourceIdentifier** *(string) --*

      The identifier for the source of the event. For example, if the event occurred at the
      cluster level, the identifier would be the name of the cluster.

    - **SourceType** *(string) --*

      Specifies the origin of this event - a cluster, a parameter group, a security group, etc.

    - **Message** *(string) --*

      The text of the event.

    - **Date** *(datetime) --*

      The date and time when the event occurred.
    """


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    Type definition for `ClientDescribeEvents` `Response`

    Represents the output of a ``DescribeEvents`` operation.

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **Events** *(list) --*

      A list of events. Each element in the list contains detailed information about one event.

      - *(dict) --*

        Represents a single occurrence of something interesting within the system. Some examples of
        events are creating a cluster, adding or removing a cache node, or rebooting a node.

        - **SourceIdentifier** *(string) --*

          The identifier for the source of the event. For example, if the event occurred at the
          cluster level, the identifier would be the name of the cluster.

        - **SourceType** *(string) --*

          Specifies the origin of this event - a cluster, a parameter group, a security group, etc.

        - **Message** *(string) --*

          The text of the event.

        - **Date** *(datetime) --*

          The date and time when the event occurred.
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroupsResponseReplicationGroups` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` .
      This member is only applicable for Redis (cluster mode disabled) replication
      groups.
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroupsResponseReplicationGroups` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node
    group is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled)
      replication group contains only 1 node group; therefore, the node group ID is 0001. A
      Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered
      0001 to 0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` .
          This member is only applicable for Redis (cluster mode disabled) replication
          groups.
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroupsResponseReplicationGroups` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication
      group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientDescribeReplicationGroupsResponseReplicationGroupsPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientDescribeReplicationGroupsResponseReplicationGroupsNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": ClientDescribeReplicationGroupsResponseReplicationGroupsConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef(
    _ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroupsResponse` `ReplicationGroups`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` ,
      ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication
        group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node
        group is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled)
          replication group contains only 1 node group; therefore, the node group ID is 0001. A
          Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered
          0001 to 0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` .
              This member is only applicable for Redis (cluster mode disabled) replication
              groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that
      was taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate
      time range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created.
      To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientDescribeReplicationGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeReplicationGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationGroups": List[
            ClientDescribeReplicationGroupsResponseReplicationGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReplicationGroupsResponseTypeDef(
    _ClientDescribeReplicationGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeReplicationGroups` `Response`

    Represents the output of a ``DescribeReplicationGroups`` operation.

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **ReplicationGroups** *(list) --*

      A list of replication groups. Each item in the list contains detailed information about one
      replication group.

      - *(dict) --*

        Contains all of the attributes of a specific Redis replication group.

        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.

        - **Description** *(string) --*

          The user supplied description of the replication group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` ,
          ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

        - **PendingModifiedValues** *(dict) --*

          A group of settings to be applied to the replication group, either immediately or during
          the next maintenance window.

          - **PrimaryClusterId** *(string) --*

            The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
            specified), or during the next maintenance window.

          - **AutomaticFailoverStatus** *(string) --*

            Indicates the status of Multi-AZ with automatic failover for this Redis replication
            group.

            Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

            * Redis versions earlier than 2.8.6.

            * Redis (cluster mode disabled): T1 node types.

            * Redis (cluster mode enabled): T1 node types.

          - **Resharding** *(dict) --*

            The status of an online resharding operation.

            - **SlotMigration** *(dict) --*

              Represents the progress of an online resharding operation.

              - **ProgressPercentage** *(float) --*

                The percentage of the slot migration that is complete.

          - **AuthTokenStatus** *(string) --*

            The auth token status

        - **MemberClusters** *(list) --*

          The names of all the cache clusters that are part of this replication group.

          - *(string) --*

        - **NodeGroups** *(list) --*

          A list of node groups in this replication group. For Redis (cluster mode disabled)
          replication groups, this is a single-element list. For Redis (cluster mode enabled)
          replication groups, the list contains an entry for each node group (shard).

          - *(dict) --*

            Represents a collection of cache nodes in a replication group. One node in the node
            group is the read/write primary node. All the other nodes are read-only Replica nodes.

            - **NodeGroupId** *(string) --*

              The identifier for the node group (shard). A Redis (cluster mode disabled)
              replication group contains only 1 node group; therefore, the node group ID is 0001. A
              Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered
              0001 to 0090. Optionally, the user can provide the id for a node group.

            - **Status** *(string) --*

              The current state of this replication group - ``creating`` , ``available`` , etc.

            - **PrimaryEndpoint** *(dict) --*

              The endpoint of the primary node in this node group (shard).

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **ReaderEndpoint** *(dict) --*

              The endpoint of the replica nodes in this node group (shard).

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **Slots** *(string) --*

              The keyspace for this node group (shard).

            - **NodeGroupMembers** *(list) --*

              A list containing information about individual nodes within the node group (shard).

              - *(dict) --*

                Represents a single node within a node group (shard).

                - **CacheClusterId** *(string) --*

                  The ID of the cluster to which the node belongs.

                - **CacheNodeId** *(string) --*

                  The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                  0002, etc.).

                - **ReadEndpoint** *(dict) --*

                  The information required for client programs to connect to a node for read
                  operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                  clusters.

                  - **Address** *(string) --*

                    The DNS hostname of the cache node.

                  - **Port** *(integer) --*

                    The port number that the cache engine is listening on.

                - **PreferredAvailabilityZone** *(string) --*

                  The name of the Availability Zone in which the node is located.

                - **CurrentRole** *(string) --*

                  The role that is currently assigned to the node - ``primary`` or ``replica`` .
                  This member is only applicable for Redis (cluster mode disabled) replication
                  groups.

        - **SnapshottingClusterId** *(string) --*

          The cluster ID that is used as the daily snapshot source for the replication group.

        - **AutomaticFailover** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **ConfigurationEndpoint** *(dict) --*

          The configuration endpoint for this replication group. Use the configuration endpoint to
          connect to this replication group.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **SnapshotRetentionLimit** *(integer) --*

          The number of days for which ElastiCache retains automatic cluster snapshots before
          deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that
          was taken today is retained for 5 days before being deleted.

          .. warning::

            If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

        - **SnapshotWindow** *(string) --*

          The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
          your node group (shard).

          Example: ``05:00-09:00``

          If you do not specify this parameter, ElastiCache automatically chooses an appropriate
          time range.

          .. note::

            This parameter is only valid if the ``Engine`` parameter is ``redis`` .

        - **ClusterEnabled** *(boolean) --*

          A flag indicating whether or not this replication group is cluster enabled; i.e., whether
          its data can be partitioned across multiple shards (API/CLI: node groups).

          Valid values: ``true`` | ``false``

        - **CacheNodeType** *(string) --*

          The name of the compute and memory capacity node type for each node in the replication
          group.

        - **AuthTokenEnabled** *(boolean) --*

          A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

          Default: ``false``

        - **AuthTokenLastModifiedDate** *(datetime) --*

          The date the auth token was last modified

        - **TransitEncryptionEnabled** *(boolean) --*

          A flag that enables in-transit encryption when set to ``true`` .

          You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
          To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
          ``true`` when you create a cluster.

           **Required:** Only available when creating a replication group in an Amazon VPC using
           redis version ``3.2.6`` , ``4.x`` or later.

          Default: ``false``

        - **AtRestEncryptionEnabled** *(boolean) --*

          A flag that enables encryption at-rest when set to ``true`` .

          You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created.
          To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to
          ``true`` when you create a cluster.

           **Required:** Only available when creating a replication group in an Amazon VPC using
           redis version ``3.2.6`` , ``4.x`` or later.

          Default: ``false``

        - **KmsKeyId** *(string) --*

          The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef(
    _ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef
):
    """
    Type definition for `ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferings` `RecurringCharges`

    Contains the specific price and frequency of a recurring charges for a reserved cache
    node, or for a reserved cache node offering.

    - **RecurringChargeAmount** *(float) --*

      The monetary amount of the recurring charge.

    - **RecurringChargeFrequency** *(string) --*

      The frequency of the recurring charge.
    """


_ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef = TypedDict(
    "_ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "ProductDescription": str,
        "OfferingType": str,
        "RecurringCharges": List[
            ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef(
    _ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef
):
    """
    Type definition for `ClientDescribeReservedCacheNodesOfferingsResponse` `ReservedCacheNodesOfferings`

    Describes all of the attributes of a reserved cache node offering.

    - **ReservedCacheNodesOfferingId** *(string) --*

      A unique identifier for the reserved cache node offering.

    - **CacheNodeType** *(string) --*

      The cache node type for the reserved cache node.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared
      to their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
        types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
        **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
        ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Duration** *(integer) --*

      The duration of the offering. in seconds.

    - **FixedPrice** *(float) --*

      The fixed price charged for this offering.

    - **UsagePrice** *(float) --*

      The hourly price charged for this offering.

    - **ProductDescription** *(string) --*

      The cache engine used by the offering.

    - **OfferingType** *(string) --*

      The offering type.

    - **RecurringCharges** *(list) --*

      The recurring price charged to run this reserved cache node.

      - *(dict) --*

        Contains the specific price and frequency of a recurring charges for a reserved cache
        node, or for a reserved cache node offering.

        - **RecurringChargeAmount** *(float) --*

          The monetary amount of the recurring charge.

        - **RecurringChargeFrequency** *(string) --*

          The frequency of the recurring charge.
    """


_ClientDescribeReservedCacheNodesOfferingsResponseTypeDef = TypedDict(
    "_ClientDescribeReservedCacheNodesOfferingsResponseTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodesOfferings": List[
            ClientDescribeReservedCacheNodesOfferingsResponseReservedCacheNodesOfferingsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedCacheNodesOfferingsResponseTypeDef(
    _ClientDescribeReservedCacheNodesOfferingsResponseTypeDef
):
    """
    Type definition for `ClientDescribeReservedCacheNodesOfferings` `Response`

    Represents the output of a ``DescribeReservedCacheNodesOfferings`` operation.

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **ReservedCacheNodesOfferings** *(list) --*

      A list of reserved cache node offerings. Each element in the list contains detailed
      information about one offering.

      - *(dict) --*

        Describes all of the attributes of a reserved cache node offering.

        - **ReservedCacheNodesOfferingId** *(string) --*

          A unique identifier for the reserved cache node offering.

        - **CacheNodeType** *(string) --*

          The cache node type for the reserved cache node.

          The following node types are supported by ElastiCache. Generally speaking, the current
          generation types provide more memory and computational power at lower cost when compared
          to their equivalent previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
            ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
            ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
            types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
            **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
            ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
            ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
            ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
            ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
            ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
          Redis version 2.8.22 and later.

        - **Duration** *(integer) --*

          The duration of the offering. in seconds.

        - **FixedPrice** *(float) --*

          The fixed price charged for this offering.

        - **UsagePrice** *(float) --*

          The hourly price charged for this offering.

        - **ProductDescription** *(string) --*

          The cache engine used by the offering.

        - **OfferingType** *(string) --*

          The offering type.

        - **RecurringCharges** *(list) --*

          The recurring price charged to run this reserved cache node.

          - *(dict) --*

            Contains the specific price and frequency of a recurring charges for a reserved cache
            node, or for a reserved cache node offering.

            - **RecurringChargeAmount** *(float) --*

              The monetary amount of the recurring charge.

            - **RecurringChargeFrequency** *(string) --*

              The frequency of the recurring charge.
    """


_ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef = TypedDict(
    "_ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef",
    {
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateEndDate": datetime,
        "ServiceUpdateSeverity": str,
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateStatus": str,
        "ServiceUpdateDescription": str,
        "ServiceUpdateType": str,
        "Engine": str,
        "EngineVersion": str,
        "AutoUpdateAfterRecommendedApplyByDate": bool,
        "EstimatedUpdateTime": str,
    },
    total=False,
)


class ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef(
    _ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef
):
    """
    Type definition for `ClientDescribeServiceUpdatesResponse` `ServiceUpdates`

    An update that you can apply to your Redis clusters.

    - **ServiceUpdateName** *(string) --*

      The unique ID of the service update

    - **ServiceUpdateReleaseDate** *(datetime) --*

      The date when the service update is initially available

    - **ServiceUpdateEndDate** *(datetime) --*

      The date after which the service update is no longer available

    - **ServiceUpdateSeverity** *(string) --*

      The severity of the service update

    - **ServiceUpdateRecommendedApplyByDate** *(datetime) --*

      The recommendend date to apply the service update in order to ensure compliance. For
      information on compliance, see `Self-Service Security Updates for Compliance
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-compliance.html#elasticache-compliance-self-service>`__
      .

    - **ServiceUpdateStatus** *(string) --*

      The status of the service update

    - **ServiceUpdateDescription** *(string) --*

      Provides details of the service update

    - **ServiceUpdateType** *(string) --*

      Reflects the nature of the service update

    - **Engine** *(string) --*

      The Elasticache engine to which the update applies. Either Redis or Memcached

    - **EngineVersion** *(string) --*

      The Elasticache engine version to which the update applies. Either Redis or Memcached
      engine version

    - **AutoUpdateAfterRecommendedApplyByDate** *(boolean) --*

      Indicates whether the service update will be automatically applied once the recommended
      apply-by date has expired.

    - **EstimatedUpdateTime** *(string) --*

      The estimated length of time the service update will take
    """


_ClientDescribeServiceUpdatesResponseTypeDef = TypedDict(
    "_ClientDescribeServiceUpdatesResponseTypeDef",
    {
        "Marker": str,
        "ServiceUpdates": List[
            ClientDescribeServiceUpdatesResponseServiceUpdatesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeServiceUpdatesResponseTypeDef(
    _ClientDescribeServiceUpdatesResponseTypeDef
):
    """
    Type definition for `ClientDescribeServiceUpdates` `Response`

    - **Marker** *(string) --*

      An optional marker returned from a prior request. Use this marker for pagination of results
      from this operation. If this parameter is specified, the response includes only records
      beyond the marker, up to the value specified by ``MaxRecords`` .

    - **ServiceUpdates** *(list) --*

      A list of service updates

      - *(dict) --*

        An update that you can apply to your Redis clusters.

        - **ServiceUpdateName** *(string) --*

          The unique ID of the service update

        - **ServiceUpdateReleaseDate** *(datetime) --*

          The date when the service update is initially available

        - **ServiceUpdateEndDate** *(datetime) --*

          The date after which the service update is no longer available

        - **ServiceUpdateSeverity** *(string) --*

          The severity of the service update

        - **ServiceUpdateRecommendedApplyByDate** *(datetime) --*

          The recommendend date to apply the service update in order to ensure compliance. For
          information on compliance, see `Self-Service Security Updates for Compliance
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-compliance.html#elasticache-compliance-self-service>`__
          .

        - **ServiceUpdateStatus** *(string) --*

          The status of the service update

        - **ServiceUpdateDescription** *(string) --*

          Provides details of the service update

        - **ServiceUpdateType** *(string) --*

          Reflects the nature of the service update

        - **Engine** *(string) --*

          The Elasticache engine to which the update applies. Either Redis or Memcached

        - **EngineVersion** *(string) --*

          The Elasticache engine version to which the update applies. Either Redis or Memcached
          engine version

        - **AutoUpdateAfterRecommendedApplyByDate** *(boolean) --*

          Indicates whether the service update will be automatically applied once the recommended
          apply-by date has expired.

        - **EstimatedUpdateTime** *(string) --*

          The estimated length of time the service update will take
    """


_ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef(
    _ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeSnapshotsResponseSnapshotsNodeSnapshots` `NodeGroupConfiguration`

    The configuration for the source node group (shard).

    - **NodeGroupId** *(string) --*

      Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
      node group these configuration values apply to.

    - **Slots** *(string) --*

      A string that specifies the keyspace for a particular node group. Keyspaces range
      from 0 to 16,383. The string is in the format ``startkey-endkey`` .

      Example: ``"0-3999"``

    - **ReplicaCount** *(integer) --*

      The number of read replica nodes in this node group (shard).

    - **PrimaryAvailabilityZone** *(string) --*

      The Availability Zone where the primary node of this node group (shard) is launched.

    - **ReplicaAvailabilityZones** *(list) --*

      A list of Availability Zones to be used for the read replicas. The number of
      Availability Zones in this list must match the value of ``ReplicaCount`` or
      ``ReplicasPerNodeGroup`` if not specified.

      - *(string) --*
    """


_ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)


class ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef(
    _ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef
):
    """
    Type definition for `ClientDescribeSnapshotsResponseSnapshots` `NodeSnapshots`

    Represents an individual cache node in a snapshot of a cluster.

    - **CacheClusterId** *(string) --*

      A unique identifier for the source cluster.

    - **NodeGroupId** *(string) --*

      A unique identifier for the source node group (shard).

    - **CacheNodeId** *(string) --*

      The cache node identifier for the node in the source cluster.

    - **NodeGroupConfiguration** *(dict) --*

      The configuration for the source node group (shard).

      - **NodeGroupId** *(string) --*

        Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
        node group these configuration values apply to.

      - **Slots** *(string) --*

        A string that specifies the keyspace for a particular node group. Keyspaces range
        from 0 to 16,383. The string is in the format ``startkey-endkey`` .

        Example: ``"0-3999"``

      - **ReplicaCount** *(integer) --*

        The number of read replica nodes in this node group (shard).

      - **PrimaryAvailabilityZone** *(string) --*

        The Availability Zone where the primary node of this node group (shard) is launched.

      - **ReplicaAvailabilityZones** *(list) --*

        A list of Availability Zones to be used for the read replicas. The number of
        Availability Zones in this list must match the value of ``ReplicaCount`` or
        ``ReplicasPerNodeGroup`` if not specified.

        - *(string) --*

    - **CacheSize** *(string) --*

      The size of the cache on the source cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created in the source cluster.

    - **SnapshotCreateTime** *(datetime) --*

      The date and time when the source node's metadata and cache data set was obtained for
      the snapshot.
    """


_ClientDescribeSnapshotsResponseSnapshotsTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": str,
        "NodeSnapshots": List[
            ClientDescribeSnapshotsResponseSnapshotsNodeSnapshotsTypeDef
        ],
        "KmsKeyId": str,
    },
    total=False,
)


class ClientDescribeSnapshotsResponseSnapshotsTypeDef(
    _ClientDescribeSnapshotsResponseSnapshotsTypeDef
):
    """
    Type definition for `ClientDescribeSnapshotsResponse` `Snapshots`

    Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

    - **SnapshotName** *(string) --*

      The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
      manual snapshot, this is the user-provided name.

    - **ReplicationGroupId** *(string) --*

      The unique identifier of the source replication group.

    - **ReplicationGroupDescription** *(string) --*

      A description of the source replication group.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the source cluster.

    - **SnapshotStatus** *(string) --*

      The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
      ``copying`` | ``deleting`` .

    - **SnapshotSource** *(string) --*

      Indicates whether the snapshot is from an automatic backup (``automated`` ) or was
      created manually (``manual`` ).

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the source cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared
      to their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
        types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
        **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
        ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine version that is used by the source cluster.

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the source cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the source cluster is located.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the source cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It
      is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The
      minimum maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
      notifications.

    - **Port** *(integer) --*

      The port number used by each cache nodes in the source cluster.

    - **CacheParameterGroupName** *(string) --*

      The cache parameter group that is associated with the source cluster.

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the source cluster.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
      source cluster.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SnapshotRetentionLimit** *(integer) --*

      For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
      before deleting it.

      For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
      cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots
      do not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

       **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
       turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range during which ElastiCache takes daily snapshots of the source cluster.

    - **NumNodeGroups** *(integer) --*

      The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
      number of node groups (shards) in the snapshot and in the restored replication group must
      be the same.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for the source Redis replication
      group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **NodeSnapshots** *(list) --*

      A list of the cache nodes in the source cluster.

      - *(dict) --*

        Represents an individual cache node in a snapshot of a cluster.

        - **CacheClusterId** *(string) --*

          A unique identifier for the source cluster.

        - **NodeGroupId** *(string) --*

          A unique identifier for the source node group (shard).

        - **CacheNodeId** *(string) --*

          The cache node identifier for the node in the source cluster.

        - **NodeGroupConfiguration** *(dict) --*

          The configuration for the source node group (shard).

          - **NodeGroupId** *(string) --*

            Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
            node group these configuration values apply to.

          - **Slots** *(string) --*

            A string that specifies the keyspace for a particular node group. Keyspaces range
            from 0 to 16,383. The string is in the format ``startkey-endkey`` .

            Example: ``"0-3999"``

          - **ReplicaCount** *(integer) --*

            The number of read replica nodes in this node group (shard).

          - **PrimaryAvailabilityZone** *(string) --*

            The Availability Zone where the primary node of this node group (shard) is launched.

          - **ReplicaAvailabilityZones** *(list) --*

            A list of Availability Zones to be used for the read replicas. The number of
            Availability Zones in this list must match the value of ``ReplicaCount`` or
            ``ReplicasPerNodeGroup`` if not specified.

            - *(string) --*

        - **CacheSize** *(string) --*

          The size of the cache on the source cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created in the source cluster.

        - **SnapshotCreateTime** *(datetime) --*

          The date and time when the source node's metadata and cache data set was obtained for
          the snapshot.

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the snapshot.
    """


_ClientDescribeSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseTypeDef",
    {"Marker": str, "Snapshots": List[ClientDescribeSnapshotsResponseSnapshotsTypeDef]},
    total=False,
)


class ClientDescribeSnapshotsResponseTypeDef(_ClientDescribeSnapshotsResponseTypeDef):
    """
    Type definition for `ClientDescribeSnapshots` `Response`

    Represents the output of a ``DescribeSnapshots`` operation.

    - **Marker** *(string) --*

      An optional marker returned from a prior request. Use this marker for pagination of results
      from this operation. If this parameter is specified, the response includes only records
      beyond the marker, up to the value specified by ``MaxRecords`` .

    - **Snapshots** *(list) --*

      A list of snapshots. Each item in the list contains detailed information about one snapshot.

      - *(dict) --*

        Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

        - **SnapshotName** *(string) --*

          The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
          manual snapshot, this is the user-provided name.

        - **ReplicationGroupId** *(string) --*

          The unique identifier of the source replication group.

        - **ReplicationGroupDescription** *(string) --*

          A description of the source replication group.

        - **CacheClusterId** *(string) --*

          The user-supplied identifier of the source cluster.

        - **SnapshotStatus** *(string) --*

          The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
          ``copying`` | ``deleting`` .

        - **SnapshotSource** *(string) --*

          Indicates whether the snapshot is from an automatic backup (``automated`` ) or was
          created manually (``manual`` ).

        - **CacheNodeType** *(string) --*

          The name of the compute and memory capacity node type for the source cluster.

          The following node types are supported by ElastiCache. Generally speaking, the current
          generation types provide more memory and computational power at lower cost when compared
          to their equivalent previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
            ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
            ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
            types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
            **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
            ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
            ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
            ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
            ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
            ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
          Redis version 2.8.22 and later.

        - **Engine** *(string) --*

          The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

        - **EngineVersion** *(string) --*

          The version of the cache engine version that is used by the source cluster.

        - **NumCacheNodes** *(integer) --*

          The number of cache nodes in the source cluster.

          For clusters running Redis, this value must be 1. For clusters running Memcached, this
          value must be between 1 and 20.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the source cluster is located.

        - **CacheClusterCreateTime** *(datetime) --*

          The date and time when the source cluster was created.

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which maintenance on the cluster is performed. It
          is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The
          minimum maintenance window is a 60 minute period.

          Valid values for ``ddd`` are:

          * ``sun``

          * ``mon``

          * ``tue``

          * ``wed``

          * ``thu``

          * ``fri``

          * ``sat``

          Example: ``sun:23:00-mon:01:30``

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
          notifications.

        - **Port** *(integer) --*

          The port number used by each cache nodes in the source cluster.

        - **CacheParameterGroupName** *(string) --*

          The cache parameter group that is associated with the source cluster.

        - **CacheSubnetGroupName** *(string) --*

          The name of the cache subnet group associated with the source cluster.

        - **VpcId** *(string) --*

          The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
          source cluster.

        - **AutoMinorVersionUpgrade** *(boolean) --*

          This parameter is currently disabled.

        - **SnapshotRetentionLimit** *(integer) --*

          For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
          before deleting it.

          For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
          cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots
          do not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

           **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
           turned off.

        - **SnapshotWindow** *(string) --*

          The daily time range during which ElastiCache takes daily snapshots of the source cluster.

        - **NumNodeGroups** *(integer) --*

          The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
          number of node groups (shards) in the snapshot and in the restored replication group must
          be the same.

        - **AutomaticFailover** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for the source Redis replication
          group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **NodeSnapshots** *(list) --*

          A list of the cache nodes in the source cluster.

          - *(dict) --*

            Represents an individual cache node in a snapshot of a cluster.

            - **CacheClusterId** *(string) --*

              A unique identifier for the source cluster.

            - **NodeGroupId** *(string) --*

              A unique identifier for the source node group (shard).

            - **CacheNodeId** *(string) --*

              The cache node identifier for the node in the source cluster.

            - **NodeGroupConfiguration** *(dict) --*

              The configuration for the source node group (shard).

              - **NodeGroupId** *(string) --*

                Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
                node group these configuration values apply to.

              - **Slots** *(string) --*

                A string that specifies the keyspace for a particular node group. Keyspaces range
                from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                Example: ``"0-3999"``

              - **ReplicaCount** *(integer) --*

                The number of read replica nodes in this node group (shard).

              - **PrimaryAvailabilityZone** *(string) --*

                The Availability Zone where the primary node of this node group (shard) is launched.

              - **ReplicaAvailabilityZones** *(list) --*

                A list of Availability Zones to be used for the read replicas. The number of
                Availability Zones in this list must match the value of ``ReplicaCount`` or
                ``ReplicasPerNodeGroup`` if not specified.

                - *(string) --*

            - **CacheSize** *(string) --*

              The size of the cache on the source cache node.

            - **CacheNodeCreateTime** *(datetime) --*

              The date and time when the cache node was created in the source cluster.

            - **SnapshotCreateTime** *(datetime) --*

              The date and time when the source node's metadata and cache data set was obtained for
              the snapshot.

        - **KmsKeyId** *(string) --*

          The ID of the KMS key used to encrypt the snapshot.
    """


_ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
    {
        "CacheNodeId": str,
        "NodeUpdateStatus": str,
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": str,
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef(
    _ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef
):
    """
    Type definition for `ClientDescribeUpdateActionsResponseUpdateActions` `CacheNodeUpdateStatus`

    The status of the service update on the cache node

    - **CacheNodeId** *(string) --*

      The node ID of the cache cluster

    - **NodeUpdateStatus** *(string) --*

      The update status of the node

    - **NodeDeletionDate** *(datetime) --*

      The deletion date of the node

    - **NodeUpdateStartDate** *(datetime) --*

      The start date of the update for a node

    - **NodeUpdateEndDate** *(datetime) --*

      The end date of the update for a node

    - **NodeUpdateInitiatedBy** *(string) --*

      Reflects whether the update was initiated by the customer or automatically applied

    - **NodeUpdateInitiatedDate** *(datetime) --*

      The date when the update is triggered

    - **NodeUpdateStatusModifiedDate** *(datetime) --*

      The date when the NodeUpdateStatus was last modified>
    """


_ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "NodeUpdateStatus": str,
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": str,
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef(
    _ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
):
    """
    Type definition for `ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatus` `NodeGroupMemberUpdateStatus`

    The status of the service update on the node group member

    - **CacheClusterId** *(string) --*

      The cache cluster ID

    - **CacheNodeId** *(string) --*

      The node ID of the cache cluster

    - **NodeUpdateStatus** *(string) --*

      The update status of the node

    - **NodeDeletionDate** *(datetime) --*

      The deletion date of the node

    - **NodeUpdateStartDate** *(datetime) --*

      The start date of the update for a node

    - **NodeUpdateEndDate** *(datetime) --*

      The end date of the update for a node

    - **NodeUpdateInitiatedBy** *(string) --*

      Reflects whether the update was initiated by the customer or automatically applied

    - **NodeUpdateInitiatedDate** *(datetime) --*

      The date when the update is triggered

    - **NodeUpdateStatusModifiedDate** *(datetime) --*

      The date when the NodeUpdateStatus was last modified
    """


_ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": str,
        "NodeGroupMemberUpdateStatus": List[
            ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
        ],
    },
    total=False,
)


class ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef(
    _ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef
):
    """
    Type definition for `ClientDescribeUpdateActionsResponseUpdateActions` `NodeGroupUpdateStatus`

    The status of the service update on the node group

    - **NodeGroupId** *(string) --*

      The ID of the node group

    - **NodeGroupMemberUpdateStatus** *(list) --*

      The status of the service update on the node group member

      - *(dict) --*

        The status of the service update on the node group member

        - **CacheClusterId** *(string) --*

          The cache cluster ID

        - **CacheNodeId** *(string) --*

          The node ID of the cache cluster

        - **NodeUpdateStatus** *(string) --*

          The update status of the node

        - **NodeDeletionDate** *(datetime) --*

          The deletion date of the node

        - **NodeUpdateStartDate** *(datetime) --*

          The start date of the update for a node

        - **NodeUpdateEndDate** *(datetime) --*

          The end date of the update for a node

        - **NodeUpdateInitiatedBy** *(string) --*

          Reflects whether the update was initiated by the customer or automatically applied

        - **NodeUpdateInitiatedDate** *(datetime) --*

          The date when the update is triggered

        - **NodeUpdateStatusModifiedDate** *(datetime) --*

          The date when the NodeUpdateStatus was last modified
    """


_ClientDescribeUpdateActionsResponseUpdateActionsTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsResponseUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateSeverity": str,
        "ServiceUpdateStatus": str,
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateType": str,
        "UpdateActionAvailableDate": datetime,
        "UpdateActionStatus": str,
        "NodesUpdated": str,
        "UpdateActionStatusModifiedDate": datetime,
        "SlaMet": str,
        "NodeGroupUpdateStatus": List[
            ClientDescribeUpdateActionsResponseUpdateActionsNodeGroupUpdateStatusTypeDef
        ],
        "CacheNodeUpdateStatus": List[
            ClientDescribeUpdateActionsResponseUpdateActionsCacheNodeUpdateStatusTypeDef
        ],
        "EstimatedUpdateTime": str,
        "Engine": str,
    },
    total=False,
)


class ClientDescribeUpdateActionsResponseUpdateActionsTypeDef(
    _ClientDescribeUpdateActionsResponseUpdateActionsTypeDef
):
    """
    Type definition for `ClientDescribeUpdateActionsResponse` `UpdateActions`

    The status of the service update for a specific replication group

    - **ReplicationGroupId** *(string) --*

      The ID of the replication group

    - **CacheClusterId** *(string) --*

      The ID of the cache cluster

    - **ServiceUpdateName** *(string) --*

      The unique ID of the service update

    - **ServiceUpdateReleaseDate** *(datetime) --*

      The date the update is first available

    - **ServiceUpdateSeverity** *(string) --*

      The severity of the service update

    - **ServiceUpdateStatus** *(string) --*

      The status of the service update

    - **ServiceUpdateRecommendedApplyByDate** *(datetime) --*

      The recommended date to apply the service update to ensure compliance. For information on
      compliance, see `Self-Service Security Updates for Compliance
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-compliance.html#elasticache-compliance-self-service>`__
      .

    - **ServiceUpdateType** *(string) --*

      Reflects the nature of the service update

    - **UpdateActionAvailableDate** *(datetime) --*

      The date that the service update is available to a replication group

    - **UpdateActionStatus** *(string) --*

      The status of the update action

    - **NodesUpdated** *(string) --*

      The progress of the service update on the replication group

    - **UpdateActionStatusModifiedDate** *(datetime) --*

      The date when the UpdateActionStatus was last modified

    - **SlaMet** *(string) --*

      If yes, all nodes in the replication group have been updated by the recommended apply-by
      date. If no, at least one node in the replication group have not been updated by the
      recommended apply-by date. If N/A, the replication group was created after the
      recommended apply-by date.

    - **NodeGroupUpdateStatus** *(list) --*

      The status of the service update on the node group

      - *(dict) --*

        The status of the service update on the node group

        - **NodeGroupId** *(string) --*

          The ID of the node group

        - **NodeGroupMemberUpdateStatus** *(list) --*

          The status of the service update on the node group member

          - *(dict) --*

            The status of the service update on the node group member

            - **CacheClusterId** *(string) --*

              The cache cluster ID

            - **CacheNodeId** *(string) --*

              The node ID of the cache cluster

            - **NodeUpdateStatus** *(string) --*

              The update status of the node

            - **NodeDeletionDate** *(datetime) --*

              The deletion date of the node

            - **NodeUpdateStartDate** *(datetime) --*

              The start date of the update for a node

            - **NodeUpdateEndDate** *(datetime) --*

              The end date of the update for a node

            - **NodeUpdateInitiatedBy** *(string) --*

              Reflects whether the update was initiated by the customer or automatically applied

            - **NodeUpdateInitiatedDate** *(datetime) --*

              The date when the update is triggered

            - **NodeUpdateStatusModifiedDate** *(datetime) --*

              The date when the NodeUpdateStatus was last modified

    - **CacheNodeUpdateStatus** *(list) --*

      The status of the service update on the cache node

      - *(dict) --*

        The status of the service update on the cache node

        - **CacheNodeId** *(string) --*

          The node ID of the cache cluster

        - **NodeUpdateStatus** *(string) --*

          The update status of the node

        - **NodeDeletionDate** *(datetime) --*

          The deletion date of the node

        - **NodeUpdateStartDate** *(datetime) --*

          The start date of the update for a node

        - **NodeUpdateEndDate** *(datetime) --*

          The end date of the update for a node

        - **NodeUpdateInitiatedBy** *(string) --*

          Reflects whether the update was initiated by the customer or automatically applied

        - **NodeUpdateInitiatedDate** *(datetime) --*

          The date when the update is triggered

        - **NodeUpdateStatusModifiedDate** *(datetime) --*

          The date when the NodeUpdateStatus was last modified>

    - **EstimatedUpdateTime** *(string) --*

      The estimated length of time for the update to complete

    - **Engine** *(string) --*

      The Elasticache engine to which the update applies. Either Redis or Memcached
    """


_ClientDescribeUpdateActionsResponseTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsResponseTypeDef",
    {
        "Marker": str,
        "UpdateActions": List[ClientDescribeUpdateActionsResponseUpdateActionsTypeDef],
    },
    total=False,
)


class ClientDescribeUpdateActionsResponseTypeDef(
    _ClientDescribeUpdateActionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeUpdateActions` `Response`

    - **Marker** *(string) --*

      An optional marker returned from a prior request. Use this marker for pagination of results
      from this operation. If this parameter is specified, the response includes only records
      beyond the marker, up to the value specified by ``MaxRecords`` .

    - **UpdateActions** *(list) --*

      Returns a list of update actions

      - *(dict) --*

        The status of the service update for a specific replication group

        - **ReplicationGroupId** *(string) --*

          The ID of the replication group

        - **CacheClusterId** *(string) --*

          The ID of the cache cluster

        - **ServiceUpdateName** *(string) --*

          The unique ID of the service update

        - **ServiceUpdateReleaseDate** *(datetime) --*

          The date the update is first available

        - **ServiceUpdateSeverity** *(string) --*

          The severity of the service update

        - **ServiceUpdateStatus** *(string) --*

          The status of the service update

        - **ServiceUpdateRecommendedApplyByDate** *(datetime) --*

          The recommended date to apply the service update to ensure compliance. For information on
          compliance, see `Self-Service Security Updates for Compliance
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-compliance.html#elasticache-compliance-self-service>`__
          .

        - **ServiceUpdateType** *(string) --*

          Reflects the nature of the service update

        - **UpdateActionAvailableDate** *(datetime) --*

          The date that the service update is available to a replication group

        - **UpdateActionStatus** *(string) --*

          The status of the update action

        - **NodesUpdated** *(string) --*

          The progress of the service update on the replication group

        - **UpdateActionStatusModifiedDate** *(datetime) --*

          The date when the UpdateActionStatus was last modified

        - **SlaMet** *(string) --*

          If yes, all nodes in the replication group have been updated by the recommended apply-by
          date. If no, at least one node in the replication group have not been updated by the
          recommended apply-by date. If N/A, the replication group was created after the
          recommended apply-by date.

        - **NodeGroupUpdateStatus** *(list) --*

          The status of the service update on the node group

          - *(dict) --*

            The status of the service update on the node group

            - **NodeGroupId** *(string) --*

              The ID of the node group

            - **NodeGroupMemberUpdateStatus** *(list) --*

              The status of the service update on the node group member

              - *(dict) --*

                The status of the service update on the node group member

                - **CacheClusterId** *(string) --*

                  The cache cluster ID

                - **CacheNodeId** *(string) --*

                  The node ID of the cache cluster

                - **NodeUpdateStatus** *(string) --*

                  The update status of the node

                - **NodeDeletionDate** *(datetime) --*

                  The deletion date of the node

                - **NodeUpdateStartDate** *(datetime) --*

                  The start date of the update for a node

                - **NodeUpdateEndDate** *(datetime) --*

                  The end date of the update for a node

                - **NodeUpdateInitiatedBy** *(string) --*

                  Reflects whether the update was initiated by the customer or automatically applied

                - **NodeUpdateInitiatedDate** *(datetime) --*

                  The date when the update is triggered

                - **NodeUpdateStatusModifiedDate** *(datetime) --*

                  The date when the NodeUpdateStatus was last modified

        - **CacheNodeUpdateStatus** *(list) --*

          The status of the service update on the cache node

          - *(dict) --*

            The status of the service update on the cache node

            - **CacheNodeId** *(string) --*

              The node ID of the cache cluster

            - **NodeUpdateStatus** *(string) --*

              The update status of the node

            - **NodeDeletionDate** *(datetime) --*

              The deletion date of the node

            - **NodeUpdateStartDate** *(datetime) --*

              The start date of the update for a node

            - **NodeUpdateEndDate** *(datetime) --*

              The end date of the update for a node

            - **NodeUpdateInitiatedBy** *(string) --*

              Reflects whether the update was initiated by the customer or automatically applied

            - **NodeUpdateInitiatedDate** *(datetime) --*

              The date when the update is triggered

            - **NodeUpdateStatusModifiedDate** *(datetime) --*

              The date when the NodeUpdateStatus was last modified>

        - **EstimatedUpdateTime** *(string) --*

          The estimated length of time for the update to complete

        - **Engine** *(string) --*

          The Elasticache engine to which the update applies. Either Redis or Memcached
    """


_ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef = TypedDict(
    "_ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)


class ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef(
    _ClientDescribeUpdateActionsServiceUpdateTimeRangeTypeDef
):
    """
    Type definition for `ClientDescribeUpdateActions` `ServiceUpdateTimeRange`

    The range of time specified to search for service updates that are in available status

    - **StartTime** *(datetime) --*

      The start time of the time range filter

    - **EndTime** *(datetime) --*

      The end time of the time range filter
    """


_RequiredClientIncreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_RequiredClientIncreaseReplicaCountReplicaConfigurationTypeDef",
    {"NodeGroupId": str, "NewReplicaCount": int},
)
_OptionalClientIncreaseReplicaCountReplicaConfigurationTypeDef = TypedDict(
    "_OptionalClientIncreaseReplicaCountReplicaConfigurationTypeDef",
    {"PreferredAvailabilityZones": List[str]},
    total=False,
)


class ClientIncreaseReplicaCountReplicaConfigurationTypeDef(
    _RequiredClientIncreaseReplicaCountReplicaConfigurationTypeDef,
    _OptionalClientIncreaseReplicaCountReplicaConfigurationTypeDef,
):
    """
    Type definition for `ClientIncreaseReplicaCount` `ReplicaConfiguration`

    Node group (shard) configuration options when adding or removing replicas. Each node group
    (shard) configuration has the following members: NodeGroupId, NewReplicaCount, and
    PreferredAvailabilityZones.

    - **NodeGroupId** *(string) --* **[REQUIRED]**

      The 4-digit id for the node group you are configuring. For Redis (cluster mode disabled)
      replication groups, the node group id is always 0001. To find a Redis (cluster mode
      enabled)'s node group's (shard's) id, see `Finding a Shard's Id
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/shard-find-id.html>`__ .

    - **NewReplicaCount** *(integer) --* **[REQUIRED]**

      The number of replicas you want in this node group at the end of this operation. The maximum
      value for ``NewReplicaCount`` is 5. The minimum value depends upon the type of Redis
      replication group you are working with.

      The minimum number of replicas in a shard or replication group is:

      * Redis (cluster mode disabled)

        * If Multi-AZ with Automatic Failover is enabled: 1

        * If Multi-AZ with Automatic Failover is not enable: 0

      * Redis (cluster mode enabled): 0 (though you will not be able to failover to a replica if
      your primary node fails)

    - **PreferredAvailabilityZones** *(list) --*

      A list of ``PreferredAvailabilityZone`` strings that specify which availability zones the
      replication group's nodes are to be in. The nummber of ``PreferredAvailabilityZone`` values
      must equal the value of ``NewReplicaCount`` plus 1 to account for the primary node. If this
      member of ``ReplicaConfiguration`` is omitted, ElastiCache for Redis selects the availability
      zone for each of the replicas.

      - *(string) --*
    """


_ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCountResponseReplicationGroup` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCountResponseReplicationGroupNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` . This
      member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCountResponseReplicationGroupNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCountResponseReplicationGroupNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCountResponseReplicationGroup` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node group
    is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled) replication
      group contains only 1 node group; therefore, the node group ID is 0001. A Redis
      (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
      0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` . This
          member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCountResponseReplicationGroup` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientIncreaseReplicaCountResponseReplicationGroupTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientIncreaseReplicaCountResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientIncreaseReplicaCountResponseReplicationGroupNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": ClientIncreaseReplicaCountResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientIncreaseReplicaCountResponseReplicationGroupTypeDef(
    _ClientIncreaseReplicaCountResponseReplicationGroupTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCountResponse` `ReplicationGroup`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , ``modifying``
      , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node group
        is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled) replication
          group contains only 1 node group; therefore, the node group ID is 0001. A Redis
          (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
          0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` . This
              member is only applicable for Redis (cluster mode disabled) replication groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
      range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientIncreaseReplicaCountResponseTypeDef = TypedDict(
    "_ClientIncreaseReplicaCountResponseTypeDef",
    {"ReplicationGroup": ClientIncreaseReplicaCountResponseReplicationGroupTypeDef},
    total=False,
)


class ClientIncreaseReplicaCountResponseTypeDef(
    _ClientIncreaseReplicaCountResponseTypeDef
):
    """
    Type definition for `ClientIncreaseReplicaCount` `Response`

    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.

      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.

      - **Description** *(string) --*

        The user supplied description of the replication group.

      - **Status** *(string) --*

        The current state of this replication group - ``creating`` , ``available`` , ``modifying``
        , ``deleting`` , ``create-failed`` , ``snapshotting`` .

      - **PendingModifiedValues** *(dict) --*

        A group of settings to be applied to the replication group, either immediately or during
        the next maintenance window.

        - **PrimaryClusterId** *(string) --*

          The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
          specified), or during the next maintenance window.

        - **AutomaticFailoverStatus** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **Resharding** *(dict) --*

          The status of an online resharding operation.

          - **SlotMigration** *(dict) --*

            Represents the progress of an online resharding operation.

            - **ProgressPercentage** *(float) --*

              The percentage of the slot migration that is complete.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **MemberClusters** *(list) --*

        The names of all the cache clusters that are part of this replication group.

        - *(string) --*

      - **NodeGroups** *(list) --*

        A list of node groups in this replication group. For Redis (cluster mode disabled)
        replication groups, this is a single-element list. For Redis (cluster mode enabled)
        replication groups, the list contains an entry for each node group (shard).

        - *(dict) --*

          Represents a collection of cache nodes in a replication group. One node in the node group
          is the read/write primary node. All the other nodes are read-only Replica nodes.

          - **NodeGroupId** *(string) --*

            The identifier for the node group (shard). A Redis (cluster mode disabled) replication
            group contains only 1 node group; therefore, the node group ID is 0001. A Redis
            (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
            0090. Optionally, the user can provide the id for a node group.

          - **Status** *(string) --*

            The current state of this replication group - ``creating`` , ``available`` , etc.

          - **PrimaryEndpoint** *(dict) --*

            The endpoint of the primary node in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ReaderEndpoint** *(dict) --*

            The endpoint of the replica nodes in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **Slots** *(string) --*

            The keyspace for this node group (shard).

          - **NodeGroupMembers** *(list) --*

            A list containing information about individual nodes within the node group (shard).

            - *(dict) --*

              Represents a single node within a node group (shard).

              - **CacheClusterId** *(string) --*

                The ID of the cluster to which the node belongs.

              - **CacheNodeId** *(string) --*

                The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                0002, etc.).

              - **ReadEndpoint** *(dict) --*

                The information required for client programs to connect to a node for read
                operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                clusters.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the node is located.

              - **CurrentRole** *(string) --*

                The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                member is only applicable for Redis (cluster mode disabled) replication groups.

      - **SnapshottingClusterId** *(string) --*

        The cluster ID that is used as the daily snapshot source for the replication group.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **ConfigurationEndpoint** *(dict) --*

        The configuration endpoint for this replication group. Use the configuration endpoint to
        connect to this replication group.

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
        range.

        .. note::

          This parameter is only valid if the ``Engine`` parameter is ``redis`` .

      - **ClusterEnabled** *(boolean) --*

        A flag indicating whether or not this replication group is cluster enabled; i.e., whether
        its data can be partitioned across multiple shards (API/CLI: node groups).

        Valid values: ``true`` | ``false``

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for each node in the replication
        group.

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientListAllowedNodeTypeModificationsResponseTypeDef = TypedDict(
    "_ClientListAllowedNodeTypeModificationsResponseTypeDef",
    {"ScaleUpModifications": List[str], "ScaleDownModifications": List[str]},
    total=False,
)


class ClientListAllowedNodeTypeModificationsResponseTypeDef(
    _ClientListAllowedNodeTypeModificationsResponseTypeDef
):
    """
    Type definition for `ClientListAllowedNodeTypeModifications` `Response`

    Represents the allowed node types you can use to modify your cluster or replication group.

    - **ScaleUpModifications** *(list) --*

      A string list, each element of which specifies a cache node type which you can use to scale
      your cluster or replication group.

      When scaling up a Redis cluster or replication group using ``ModifyCacheCluster`` or
      ``ModifyReplicationGroup`` , use a value from this list for the ``CacheNodeType`` parameter.

      - *(string) --*

    - **ScaleDownModifications** *(list) --*

      A string list, each element of which specifies a cache node type which you can use to scale
      your cluster or replication group.

      When scaling down on a Redis cluster or replication group using ``ModifyCacheCluster`` or
      ``ModifyReplicationGroup`` , use a value from this list for the ``CacheNodeType`` parameter.

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

    A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
    Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

    - **Key** *(string) --*

      The key for the tag. May not be null.

    - **Value** *(string) --*

      The tag's value. May be null.
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

    Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and
    ``RemoveTagsFromResource`` operations.

    - **TagList** *(list) --*

      A list of cost allocation tags as key-value pairs.

      - *(dict) --*

        A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
        Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

        - **Key** *(string) --*

          The key for the tag. May not be null.

        - **Value** *(string) --*

          The tag's value. May be null.
    """


_ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef
):
    """
    Type definition for `ClientModifyCacheClusterResponseCacheClusterCacheNodes` `Endpoint`

    The hostname for connecting to this cache node.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientModifyCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef
):
    """
    Type definition for `ClientModifyCacheClusterResponseCacheCluster` `CacheNodes`

    Represents an individual cache node within a cluster. Each cache node runs its own
    instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

    The following node types are supported by ElastiCache. Generally speaking, the current
    generation types provide more memory and computational power at lower cost when compared
    to their equivalent previous generation counterparts.

    * General purpose:

      * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
      ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
      ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
      ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
      types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

      * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
      **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
      ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
      ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

    * Compute optimized:

      * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

    * Memory optimized:

      * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
      ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
      ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
      ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
      ``cache.r4.16xlarge``

      * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
      ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
      ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

     **Additional node type info**

    * All current generation instance types are created in Amazon VPC by default.

    * Redis append-only files (AOF) are not supported for T1 or T2 instances.

    * Redis Multi-AZ with automatic failover is not supported on T1 instances.

    * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
    Redis version 2.8.22 and later.

    - **CacheNodeId** *(string) --*

      The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
      combination of cluster ID and node ID uniquely identifies every cache node used in a
      customer's AWS account.

    - **CacheNodeStatus** *(string) --*

      The current state of this cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created.

    - **Endpoint** *(dict) --*

      The hostname for connecting to this cache node.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group applied to this cache node.

    - **SourceCacheNodeId** *(string) --*

      The ID of the primary node to which this read replica node is synchronized. If this
      field is empty, this node is not associated with a primary cluster.

    - **CustomerAvailabilityZone** *(string) --*

      The Availability Zone where this node was created and now resides.
    """


_ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef
):
    """
    Type definition for `ClientModifyCacheClusterResponseCacheCluster` `CacheParameterGroup`

    Status of the cache parameter group.

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **CacheNodeIdsToReboot** *(list) --*

      A list of the cache node IDs which need to be rebooted for parameter changes to be
      applied. A node ID is a numeric identifier (0001, 0002, etc.).

      - *(string) --*
    """


_ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
):
    """
    Type definition for `ClientModifyCacheClusterResponseCacheCluster` `CacheSecurityGroups`

    Represents a cluster's status within a particular cache security group.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Status** *(string) --*

      The membership status in the cache security group. The status changes when a cache
      security group is modified, or when the cache security groups assigned to a cluster are
      modified.
    """


_ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientModifyCacheClusterResponseCacheCluster` `ConfigurationEndpoint`

    Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
    cluster, can be used by an application to connect to any node in the cluster. The
    configuration endpoint will always have ``.cfg`` in it.

    Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientModifyCacheClusterResponseCacheCluster` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for publishing
    ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientModifyCacheClusterResponseCacheCluster` `PendingModifiedValues`

    A group of settings that are applied to the cluster in the future, or that are currently
    being applied.

    - **NumCacheNodes** *(integer) --*

      The new number of cache nodes for the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **CacheNodeIdsToRemove** *(list) --*

      A list of cache node IDs that are being removed (or will be removed) from the cluster. A
      node ID is a 4-digit numeric identifier (0001, 0002, etc.).

      - *(string) --*

    - **EngineVersion** *(string) --*

      The new cache engine version that the cluster runs.

    - **CacheNodeType** *(string) --*

      The cache node type that this cluster or replication group is scaled to.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef
):
    """
    Type definition for `ClientModifyCacheClusterResponseCacheCluster` `SecurityGroups`

    Represents a single cache security group and its status.

    - **SecurityGroupId** *(string) --*

      The identifier of the cache security group.

    - **Status** *(string) --*

      The status of the cache security group membership. The status changes whenever a cache
      security group is modified, or when the cache security groups assigned to a cluster are
      modified.
    """


_ClientModifyCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientModifyCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientModifyCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientModifyCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientModifyCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[
            ClientModifyCacheClusterResponseCacheClusterCacheNodesTypeDef
        ],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[
            ClientModifyCacheClusterResponseCacheClusterSecurityGroupsTypeDef
        ],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class ClientModifyCacheClusterResponseCacheClusterTypeDef(
    _ClientModifyCacheClusterResponseCacheClusterTypeDef
):
    """
    Type definition for `ClientModifyCacheClusterResponse` `CacheCluster`

    Contains all of the attributes of a specific cluster.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the cluster. This identifier is a unique key that
      identifies a cluster.

    - **ConfigurationEndpoint** *(dict) --*

      Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
      cluster, can be used by an application to connect to any node in the cluster. The
      configuration endpoint will always have ``.cfg`` in it.

      Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ClientDownloadLandingPage** *(string) --*

      The URL of the web page where you can download the latest ElastiCache client library.

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared to
      their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
         ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
        node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine that is used in this cluster.

    - **CacheClusterStatus** *(string) --*

      The current state of this cluster, one of the following values: ``available`` ,
      ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
      ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the cluster is located or "Multiple" if the
      cache nodes are located in different Availability Zones.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It is
      specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
      maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **PendingModifiedValues** *(dict) --*

      A group of settings that are applied to the cluster in the future, or that are currently
      being applied.

      - **NumCacheNodes** *(integer) --*

        The new number of cache nodes for the cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **CacheNodeIdsToRemove** *(list) --*

        A list of cache node IDs that are being removed (or will be removed) from the cluster. A
        node ID is a 4-digit numeric identifier (0001, 0002, etc.).

        - *(string) --*

      - **EngineVersion** *(string) --*

        The new cache engine version that the cluster runs.

      - **CacheNodeType** *(string) --*

        The cache node type that this cluster or replication group is scaled to.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for publishing
      ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **CacheSecurityGroups** *(list) --*

      A list of cache security group elements, composed of name and status sub-elements.

      - *(dict) --*

        Represents a cluster's status within a particular cache security group.

        - **CacheSecurityGroupName** *(string) --*

          The name of the cache security group.

        - **Status** *(string) --*

          The membership status in the cache security group. The status changes when a cache
          security group is modified, or when the cache security groups assigned to a cluster are
          modified.

    - **CacheParameterGroup** *(dict) --*

      Status of the cache parameter group.

      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **CacheNodeIdsToReboot** *(list) --*

        A list of the cache node IDs which need to be rebooted for parameter changes to be
        applied. A node ID is a numeric identifier (0001, 0002, etc.).

        - *(string) --*

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the cluster.

    - **CacheNodes** *(list) --*

      A list of cache nodes that are members of the cluster.

      - *(dict) --*

        Represents an individual cache node within a cluster. Each cache node runs its own
        instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared
        to their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
          types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
          **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
          ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

        - **CacheNodeId** *(string) --*

          The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
          combination of cluster ID and node ID uniquely identifies every cache node used in a
          customer's AWS account.

        - **CacheNodeStatus** *(string) --*

          The current state of this cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created.

        - **Endpoint** *(dict) --*

          The hostname for connecting to this cache node.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group applied to this cache node.

        - **SourceCacheNodeId** *(string) --*

          The ID of the primary node to which this read replica node is synchronized. If this
          field is empty, this node is not associated with a primary cluster.

        - **CustomerAvailabilityZone** *(string) --*

          The Availability Zone where this node was created and now resides.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SecurityGroups** *(list) --*

      A list of VPC Security Groups associated with the cluster.

      - *(dict) --*

        Represents a single cache security group and its status.

        - **SecurityGroupId** *(string) --*

          The identifier of the cache security group.

        - **Status** *(string) --*

          The status of the cache security group membership. The status changes whenever a cache
          security group is modified, or when the cache security groups assigned to a cluster are
          modified.

    - **ReplicationGroupId** *(string) --*

      The replication group to which this cluster belongs. If this field is empty, the cluster is
      not associated with any replication group.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your cluster.

      Example: ``05:00-09:00``

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``
    """


_ClientModifyCacheClusterResponseTypeDef = TypedDict(
    "_ClientModifyCacheClusterResponseTypeDef",
    {"CacheCluster": ClientModifyCacheClusterResponseCacheClusterTypeDef},
    total=False,
)


class ClientModifyCacheClusterResponseTypeDef(_ClientModifyCacheClusterResponseTypeDef):
    """
    Type definition for `ClientModifyCacheCluster` `Response`

    - **CacheCluster** *(dict) --*

      Contains all of the attributes of a specific cluster.

      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the cluster. This identifier is a unique key that
        identifies a cluster.

      - **ConfigurationEndpoint** *(dict) --*

        Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
        cluster, can be used by an application to connect to any node in the cluster. The
        configuration endpoint will always have ``.cfg`` in it.

        Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **ClientDownloadLandingPage** *(string) --*

        The URL of the web page where you can download the latest ElastiCache client library.

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for the cluster.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared to
        their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
           ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
          node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

      - **Engine** *(string) --*

        The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

      - **EngineVersion** *(string) --*

        The version of the cache engine that is used in this cluster.

      - **CacheClusterStatus** *(string) --*

        The current state of this cluster, one of the following values: ``available`` ,
        ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
        ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

      - **NumCacheNodes** *(integer) --*

        The number of cache nodes in the cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **PreferredAvailabilityZone** *(string) --*

        The name of the Availability Zone in which the cluster is located or "Multiple" if the
        cache nodes are located in different Availability Zones.

      - **CacheClusterCreateTime** *(datetime) --*

        The date and time when the cluster was created.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which maintenance on the cluster is performed. It is
        specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
        maintenance window is a 60 minute period.

        Valid values for ``ddd`` are:

        * ``sun``

        * ``mon``

        * ``tue``

        * ``wed``

        * ``thu``

        * ``fri``

        * ``sat``

        Example: ``sun:23:00-mon:01:30``

      - **PendingModifiedValues** *(dict) --*

        A group of settings that are applied to the cluster in the future, or that are currently
        being applied.

        - **NumCacheNodes** *(integer) --*

          The new number of cache nodes for the cluster.

          For clusters running Redis, this value must be 1. For clusters running Memcached, this
          value must be between 1 and 20.

        - **CacheNodeIdsToRemove** *(list) --*

          A list of cache node IDs that are being removed (or will be removed) from the cluster. A
          node ID is a 4-digit numeric identifier (0001, 0002, etc.).

          - *(string) --*

        - **EngineVersion** *(string) --*

          The new cache engine version that the cluster runs.

        - **CacheNodeType** *(string) --*

          The cache node type that this cluster or replication group is scaled to.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **NotificationConfiguration** *(dict) --*

        Describes a notification topic and its status. Notification topics are used for publishing
        ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the topic.

        - **TopicStatus** *(string) --*

          The current state of the topic.

      - **CacheSecurityGroups** *(list) --*

        A list of cache security group elements, composed of name and status sub-elements.

        - *(dict) --*

          Represents a cluster's status within a particular cache security group.

          - **CacheSecurityGroupName** *(string) --*

            The name of the cache security group.

          - **Status** *(string) --*

            The membership status in the cache security group. The status changes when a cache
            security group is modified, or when the cache security groups assigned to a cluster are
            modified.

      - **CacheParameterGroup** *(dict) --*

        Status of the cache parameter group.

        - **CacheParameterGroupName** *(string) --*

          The name of the cache parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

        - **CacheNodeIdsToReboot** *(list) --*

          A list of the cache node IDs which need to be rebooted for parameter changes to be
          applied. A node ID is a numeric identifier (0001, 0002, etc.).

          - *(string) --*

      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group associated with the cluster.

      - **CacheNodes** *(list) --*

        A list of cache nodes that are members of the cluster.

        - *(dict) --*

          Represents an individual cache node within a cluster. Each cache node runs its own
          instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

          The following node types are supported by ElastiCache. Generally speaking, the current
          generation types provide more memory and computational power at lower cost when compared
          to their equivalent previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
            ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
            ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
            types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
            **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
            ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
            ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
            ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
            ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
            ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
          Redis version 2.8.22 and later.

          - **CacheNodeId** *(string) --*

            The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
            combination of cluster ID and node ID uniquely identifies every cache node used in a
            customer's AWS account.

          - **CacheNodeStatus** *(string) --*

            The current state of this cache node.

          - **CacheNodeCreateTime** *(datetime) --*

            The date and time when the cache node was created.

          - **Endpoint** *(dict) --*

            The hostname for connecting to this cache node.

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ParameterGroupStatus** *(string) --*

            The status of the parameter group applied to this cache node.

          - **SourceCacheNodeId** *(string) --*

            The ID of the primary node to which this read replica node is synchronized. If this
            field is empty, this node is not associated with a primary cluster.

          - **CustomerAvailabilityZone** *(string) --*

            The Availability Zone where this node was created and now resides.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        This parameter is currently disabled.

      - **SecurityGroups** *(list) --*

        A list of VPC Security Groups associated with the cluster.

        - *(dict) --*

          Represents a single cache security group and its status.

          - **SecurityGroupId** *(string) --*

            The identifier of the cache security group.

          - **Status** *(string) --*

            The status of the cache security group membership. The status changes whenever a cache
            security group is modified, or when the cache security groups assigned to a cluster are
            modified.

      - **ReplicationGroupId** *(string) --*

        The replication group to which this cluster belongs. If this field is empty, the cluster is
        not associated with any replication group.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your cluster.

        Example: ``05:00-09:00``

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``
    """


_ClientModifyCacheParameterGroupParameterNameValuesTypeDef = TypedDict(
    "_ClientModifyCacheParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientModifyCacheParameterGroupParameterNameValuesTypeDef(
    _ClientModifyCacheParameterGroupParameterNameValuesTypeDef
):
    """
    Type definition for `ClientModifyCacheParameterGroup` `ParameterNameValues`

    Describes a name-value pair that is used to update the value of a parameter.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The value of the parameter.
    """


_ClientModifyCacheParameterGroupResponseTypeDef = TypedDict(
    "_ClientModifyCacheParameterGroupResponseTypeDef",
    {"CacheParameterGroupName": str},
    total=False,
)


class ClientModifyCacheParameterGroupResponseTypeDef(
    _ClientModifyCacheParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientModifyCacheParameterGroup` `Response`

    Represents the output of one of the following operations:

    * ``ModifyCacheParameterGroup``

    * ``ResetCacheParameterGroup``

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.
    """


_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnets` `SubnetAvailabilityZone`

    The Availability Zone associated with the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)


class ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef(
    _ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientModifyCacheSubnetGroupResponseCacheSubnetGroup` `Subnets`

    Represents the subnet associated with a cluster. This parameter refers to subnets defined
    in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

    - **SubnetIdentifier** *(string) --*

      The unique identifier for the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone associated with the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.
    """


_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef = TypedDict(
    "_ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[
            ClientModifyCacheSubnetGroupResponseCacheSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)


class ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef(
    _ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef
):
    """
    Type definition for `ClientModifyCacheSubnetGroupResponse` `CacheSubnetGroup`

    Represents the output of one of the following operations:

    * ``CreateCacheSubnetGroup``

    * ``ModifyCacheSubnetGroup``

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group.

    - **CacheSubnetGroupDescription** *(string) --*

      The description of the cache subnet group.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

    - **Subnets** *(list) --*

      A list of subnets associated with the cache subnet group.

      - *(dict) --*

        Represents the subnet associated with a cluster. This parameter refers to subnets defined
        in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

        - **SubnetIdentifier** *(string) --*

          The unique identifier for the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone associated with the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.
    """


_ClientModifyCacheSubnetGroupResponseTypeDef = TypedDict(
    "_ClientModifyCacheSubnetGroupResponseTypeDef",
    {"CacheSubnetGroup": ClientModifyCacheSubnetGroupResponseCacheSubnetGroupTypeDef},
    total=False,
)


class ClientModifyCacheSubnetGroupResponseTypeDef(
    _ClientModifyCacheSubnetGroupResponseTypeDef
):
    """
    Type definition for `ClientModifyCacheSubnetGroup` `Response`

    - **CacheSubnetGroup** *(dict) --*

      Represents the output of one of the following operations:

      * ``CreateCacheSubnetGroup``

      * ``ModifyCacheSubnetGroup``

      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group.

      - **CacheSubnetGroupDescription** *(string) --*

        The description of the cache subnet group.

      - **VpcId** *(string) --*

        The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

      - **Subnets** *(list) --*

        A list of subnets associated with the cache subnet group.

        - *(dict) --*

          Represents the subnet associated with a cluster. This parameter refers to subnets defined
          in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

          - **SubnetIdentifier** *(string) --*

            The unique identifier for the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            The Availability Zone associated with the subnet.

            - **Name** *(string) --*

              The name of the Availability Zone.
    """


_ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupResponseReplicationGroup` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupResponseReplicationGroupNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` . This
      member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupResponseReplicationGroupNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupResponseReplicationGroupNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupResponseReplicationGroup` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node group
    is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled) replication
      group contains only 1 node group; therefore, the node group ID is 0001. A Redis
      (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
      0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` . This
          member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupResponseReplicationGroup` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientModifyReplicationGroupResponseReplicationGroupTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientModifyReplicationGroupResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientModifyReplicationGroupResponseReplicationGroupNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": ClientModifyReplicationGroupResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientModifyReplicationGroupResponseReplicationGroupTypeDef(
    _ClientModifyReplicationGroupResponseReplicationGroupTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupResponse` `ReplicationGroup`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , ``modifying``
      , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node group
        is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled) replication
          group contains only 1 node group; therefore, the node group ID is 0001. A Redis
          (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
          0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` . This
              member is only applicable for Redis (cluster mode disabled) replication groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
      range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientModifyReplicationGroupResponseTypeDef = TypedDict(
    "_ClientModifyReplicationGroupResponseTypeDef",
    {"ReplicationGroup": ClientModifyReplicationGroupResponseReplicationGroupTypeDef},
    total=False,
)


class ClientModifyReplicationGroupResponseTypeDef(
    _ClientModifyReplicationGroupResponseTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroup` `Response`

    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.

      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.

      - **Description** *(string) --*

        The user supplied description of the replication group.

      - **Status** *(string) --*

        The current state of this replication group - ``creating`` , ``available`` , ``modifying``
        , ``deleting`` , ``create-failed`` , ``snapshotting`` .

      - **PendingModifiedValues** *(dict) --*

        A group of settings to be applied to the replication group, either immediately or during
        the next maintenance window.

        - **PrimaryClusterId** *(string) --*

          The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
          specified), or during the next maintenance window.

        - **AutomaticFailoverStatus** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **Resharding** *(dict) --*

          The status of an online resharding operation.

          - **SlotMigration** *(dict) --*

            Represents the progress of an online resharding operation.

            - **ProgressPercentage** *(float) --*

              The percentage of the slot migration that is complete.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **MemberClusters** *(list) --*

        The names of all the cache clusters that are part of this replication group.

        - *(string) --*

      - **NodeGroups** *(list) --*

        A list of node groups in this replication group. For Redis (cluster mode disabled)
        replication groups, this is a single-element list. For Redis (cluster mode enabled)
        replication groups, the list contains an entry for each node group (shard).

        - *(dict) --*

          Represents a collection of cache nodes in a replication group. One node in the node group
          is the read/write primary node. All the other nodes are read-only Replica nodes.

          - **NodeGroupId** *(string) --*

            The identifier for the node group (shard). A Redis (cluster mode disabled) replication
            group contains only 1 node group; therefore, the node group ID is 0001. A Redis
            (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
            0090. Optionally, the user can provide the id for a node group.

          - **Status** *(string) --*

            The current state of this replication group - ``creating`` , ``available`` , etc.

          - **PrimaryEndpoint** *(dict) --*

            The endpoint of the primary node in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ReaderEndpoint** *(dict) --*

            The endpoint of the replica nodes in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **Slots** *(string) --*

            The keyspace for this node group (shard).

          - **NodeGroupMembers** *(list) --*

            A list containing information about individual nodes within the node group (shard).

            - *(dict) --*

              Represents a single node within a node group (shard).

              - **CacheClusterId** *(string) --*

                The ID of the cluster to which the node belongs.

              - **CacheNodeId** *(string) --*

                The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                0002, etc.).

              - **ReadEndpoint** *(dict) --*

                The information required for client programs to connect to a node for read
                operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                clusters.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the node is located.

              - **CurrentRole** *(string) --*

                The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                member is only applicable for Redis (cluster mode disabled) replication groups.

      - **SnapshottingClusterId** *(string) --*

        The cluster ID that is used as the daily snapshot source for the replication group.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **ConfigurationEndpoint** *(dict) --*

        The configuration endpoint for this replication group. Use the configuration endpoint to
        connect to this replication group.

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
        range.

        .. note::

          This parameter is only valid if the ``Engine`` parameter is ``redis`` .

      - **ClusterEnabled** *(boolean) --*

        A flag indicating whether or not this replication group is cluster enabled; i.e., whether
        its data can be partitioned across multiple shards (API/CLI: node groups).

        Valid values: ``true`` | ``false``

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for each node in the replication
        group.

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef",
    {"NodeGroupId": str, "PreferredAvailabilityZones": List[str]},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef(
    _ClientModifyReplicationGroupShardConfigurationReshardingConfigurationTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfiguration` `ReshardingConfiguration`

    A list of ``PreferredAvailabilityZones`` objects that specifies the configuration of a node
    group in the resharded cluster.

    - **NodeGroupId** *(string) --*

      Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the node group
      these configuration values apply to.

    - **PreferredAvailabilityZones** *(list) --*

      A list of preferred availability zones for the nodes in this cluster.

      - *(string) --*
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfigurationResponseReplicationGroup` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` . This
      member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfigurationResponseReplicationGroup` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node group
    is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled) replication
      group contains only 1 node group; therefore, the node group ID is 0001. A Redis
      (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
      0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` . This
          member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfigurationResponseReplicationGroup` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfigurationResponse` `ReplicationGroup`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , ``modifying``
      , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node group
        is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled) replication
          group contains only 1 node group; therefore, the node group ID is 0001. A Redis
          (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
          0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` . This
              member is only applicable for Redis (cluster mode disabled) replication groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
      range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientModifyReplicationGroupShardConfigurationResponseTypeDef = TypedDict(
    "_ClientModifyReplicationGroupShardConfigurationResponseTypeDef",
    {
        "ReplicationGroup": ClientModifyReplicationGroupShardConfigurationResponseReplicationGroupTypeDef
    },
    total=False,
)


class ClientModifyReplicationGroupShardConfigurationResponseTypeDef(
    _ClientModifyReplicationGroupShardConfigurationResponseTypeDef
):
    """
    Type definition for `ClientModifyReplicationGroupShardConfiguration` `Response`

    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.

      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.

      - **Description** *(string) --*

        The user supplied description of the replication group.

      - **Status** *(string) --*

        The current state of this replication group - ``creating`` , ``available`` , ``modifying``
        , ``deleting`` , ``create-failed`` , ``snapshotting`` .

      - **PendingModifiedValues** *(dict) --*

        A group of settings to be applied to the replication group, either immediately or during
        the next maintenance window.

        - **PrimaryClusterId** *(string) --*

          The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
          specified), or during the next maintenance window.

        - **AutomaticFailoverStatus** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **Resharding** *(dict) --*

          The status of an online resharding operation.

          - **SlotMigration** *(dict) --*

            Represents the progress of an online resharding operation.

            - **ProgressPercentage** *(float) --*

              The percentage of the slot migration that is complete.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **MemberClusters** *(list) --*

        The names of all the cache clusters that are part of this replication group.

        - *(string) --*

      - **NodeGroups** *(list) --*

        A list of node groups in this replication group. For Redis (cluster mode disabled)
        replication groups, this is a single-element list. For Redis (cluster mode enabled)
        replication groups, the list contains an entry for each node group (shard).

        - *(dict) --*

          Represents a collection of cache nodes in a replication group. One node in the node group
          is the read/write primary node. All the other nodes are read-only Replica nodes.

          - **NodeGroupId** *(string) --*

            The identifier for the node group (shard). A Redis (cluster mode disabled) replication
            group contains only 1 node group; therefore, the node group ID is 0001. A Redis
            (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
            0090. Optionally, the user can provide the id for a node group.

          - **Status** *(string) --*

            The current state of this replication group - ``creating`` , ``available`` , etc.

          - **PrimaryEndpoint** *(dict) --*

            The endpoint of the primary node in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ReaderEndpoint** *(dict) --*

            The endpoint of the replica nodes in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **Slots** *(string) --*

            The keyspace for this node group (shard).

          - **NodeGroupMembers** *(list) --*

            A list containing information about individual nodes within the node group (shard).

            - *(dict) --*

              Represents a single node within a node group (shard).

              - **CacheClusterId** *(string) --*

                The ID of the cluster to which the node belongs.

              - **CacheNodeId** *(string) --*

                The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                0002, etc.).

              - **ReadEndpoint** *(dict) --*

                The information required for client programs to connect to a node for read
                operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                clusters.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the node is located.

              - **CurrentRole** *(string) --*

                The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                member is only applicable for Redis (cluster mode disabled) replication groups.

      - **SnapshottingClusterId** *(string) --*

        The cluster ID that is used as the daily snapshot source for the replication group.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **ConfigurationEndpoint** *(dict) --*

        The configuration endpoint for this replication group. Use the configuration endpoint to
        connect to this replication group.

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
        range.

        .. note::

          This parameter is only valid if the ``Engine`` parameter is ``redis`` .

      - **ClusterEnabled** *(boolean) --*

        A flag indicating whether or not this replication group is cluster enabled; i.e., whether
        its data can be partitioned across multiple shards (API/CLI: node groups).

        Valid values: ``true`` | ``false``

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for each node in the replication
        group.

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef = TypedDict(
    "_ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef(
    _ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef
):
    """
    Type definition for `ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNode` `RecurringCharges`

    Contains the specific price and frequency of a recurring charges for a reserved cache
    node, or for a reserved cache node offering.

    - **RecurringChargeAmount** *(float) --*

      The monetary amount of the recurring charge.

    - **RecurringChargeFrequency** *(string) --*

      The frequency of the recurring charge.
    """


_ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef = TypedDict(
    "_ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CacheNodeCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "State": str,
        "RecurringCharges": List[
            ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeRecurringChargesTypeDef
        ],
        "ReservationARN": str,
    },
    total=False,
)


class ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef(
    _ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef
):
    """
    Type definition for `ClientPurchaseReservedCacheNodesOfferingResponse` `ReservedCacheNode`

    Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.

    - **ReservedCacheNodeId** *(string) --*

      The unique identifier for the reservation.

    - **ReservedCacheNodesOfferingId** *(string) --*

      The offering identifier.

    - **CacheNodeType** *(string) --*

      The cache node type for the reserved cache nodes.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared to
      their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
         ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
        node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **StartTime** *(datetime) --*

      The time the reservation started.

    - **Duration** *(integer) --*

      The duration of the reservation in seconds.

    - **FixedPrice** *(float) --*

      The fixed price charged for this reserved cache node.

    - **UsagePrice** *(float) --*

      The hourly price charged for this reserved cache node.

    - **CacheNodeCount** *(integer) --*

      The number of cache nodes that have been reserved.

    - **ProductDescription** *(string) --*

      The description of the reserved cache node.

    - **OfferingType** *(string) --*

      The offering type of this reserved cache node.

    - **State** *(string) --*

      The state of the reserved cache node.

    - **RecurringCharges** *(list) --*

      The recurring price charged to run this reserved cache node.

      - *(dict) --*

        Contains the specific price and frequency of a recurring charges for a reserved cache
        node, or for a reserved cache node offering.

        - **RecurringChargeAmount** *(float) --*

          The monetary amount of the recurring charge.

        - **RecurringChargeFrequency** *(string) --*

          The frequency of the recurring charge.

    - **ReservationARN** *(string) --*

      The Amazon Resource Name (ARN) of the reserved cache node.

      Example:
      ``arn:aws:elasticache:us-east-1:123456789012:reserved-instance:ri-2017-03-27-08-33-25-582``
    """


_ClientPurchaseReservedCacheNodesOfferingResponseTypeDef = TypedDict(
    "_ClientPurchaseReservedCacheNodesOfferingResponseTypeDef",
    {
        "ReservedCacheNode": ClientPurchaseReservedCacheNodesOfferingResponseReservedCacheNodeTypeDef
    },
    total=False,
)


class ClientPurchaseReservedCacheNodesOfferingResponseTypeDef(
    _ClientPurchaseReservedCacheNodesOfferingResponseTypeDef
):
    """
    Type definition for `ClientPurchaseReservedCacheNodesOffering` `Response`

    - **ReservedCacheNode** *(dict) --*

      Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.

      - **ReservedCacheNodeId** *(string) --*

        The unique identifier for the reservation.

      - **ReservedCacheNodesOfferingId** *(string) --*

        The offering identifier.

      - **CacheNodeType** *(string) --*

        The cache node type for the reserved cache nodes.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared to
        their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
           ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
          node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

      - **StartTime** *(datetime) --*

        The time the reservation started.

      - **Duration** *(integer) --*

        The duration of the reservation in seconds.

      - **FixedPrice** *(float) --*

        The fixed price charged for this reserved cache node.

      - **UsagePrice** *(float) --*

        The hourly price charged for this reserved cache node.

      - **CacheNodeCount** *(integer) --*

        The number of cache nodes that have been reserved.

      - **ProductDescription** *(string) --*

        The description of the reserved cache node.

      - **OfferingType** *(string) --*

        The offering type of this reserved cache node.

      - **State** *(string) --*

        The state of the reserved cache node.

      - **RecurringCharges** *(list) --*

        The recurring price charged to run this reserved cache node.

        - *(dict) --*

          Contains the specific price and frequency of a recurring charges for a reserved cache
          node, or for a reserved cache node offering.

          - **RecurringChargeAmount** *(float) --*

            The monetary amount of the recurring charge.

          - **RecurringChargeFrequency** *(string) --*

            The frequency of the recurring charge.

      - **ReservationARN** *(string) --*

        The Amazon Resource Name (ARN) of the reserved cache node.

        Example:
        ``arn:aws:elasticache:us-east-1:123456789012:reserved-instance:ri-2017-03-27-08-33-25-582``
    """


_ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef
):
    """
    Type definition for `ClientRebootCacheClusterResponseCacheClusterCacheNodes` `Endpoint`

    The hostname for connecting to this cache node.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": ClientRebootCacheClusterResponseCacheClusterCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef
):
    """
    Type definition for `ClientRebootCacheClusterResponseCacheCluster` `CacheNodes`

    Represents an individual cache node within a cluster. Each cache node runs its own
    instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

    The following node types are supported by ElastiCache. Generally speaking, the current
    generation types provide more memory and computational power at lower cost when compared
    to their equivalent previous generation counterparts.

    * General purpose:

      * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
      ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
      ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
      ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
      types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

      * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
      **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
      ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
      ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

    * Compute optimized:

      * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

    * Memory optimized:

      * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
      ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
      ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
      ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
      ``cache.r4.16xlarge``

      * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
      ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
      ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

     **Additional node type info**

    * All current generation instance types are created in Amazon VPC by default.

    * Redis append-only files (AOF) are not supported for T1 or T2 instances.

    * Redis Multi-AZ with automatic failover is not supported on T1 instances.

    * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
    Redis version 2.8.22 and later.

    - **CacheNodeId** *(string) --*

      The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
      combination of cluster ID and node ID uniquely identifies every cache node used in a
      customer's AWS account.

    - **CacheNodeStatus** *(string) --*

      The current state of this cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created.

    - **Endpoint** *(dict) --*

      The hostname for connecting to this cache node.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group applied to this cache node.

    - **SourceCacheNodeId** *(string) --*

      The ID of the primary node to which this read replica node is synchronized. If this
      field is empty, this node is not associated with a primary cluster.

    - **CustomerAvailabilityZone** *(string) --*

      The Availability Zone where this node was created and now resides.
    """


_ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef
):
    """
    Type definition for `ClientRebootCacheClusterResponseCacheCluster` `CacheParameterGroup`

    Status of the cache parameter group.

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **CacheNodeIdsToReboot** *(list) --*

      A list of the cache node IDs which need to be rebooted for parameter changes to be
      applied. A node ID is a numeric identifier (0001, 0002, etc.).

      - *(string) --*
    """


_ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRebootCacheClusterResponseCacheCluster` `CacheSecurityGroups`

    Represents a cluster's status within a particular cache security group.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Status** *(string) --*

      The membership status in the cache security group. The status changes when a cache
      security group is modified, or when the cache security groups assigned to a cluster are
      modified.
    """


_ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientRebootCacheClusterResponseCacheCluster` `ConfigurationEndpoint`

    Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
    cluster, can be used by an application to connect to any node in the cluster. The
    configuration endpoint will always have ``.cfg`` in it.

    Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef
):
    """
    Type definition for `ClientRebootCacheClusterResponseCacheCluster` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for publishing
    ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientRebootCacheClusterResponseCacheCluster` `PendingModifiedValues`

    A group of settings that are applied to the cluster in the future, or that are currently
    being applied.

    - **NumCacheNodes** *(integer) --*

      The new number of cache nodes for the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **CacheNodeIdsToRemove** *(list) --*

      A list of cache node IDs that are being removed (or will be removed) from the cluster. A
      node ID is a 4-digit numeric identifier (0001, 0002, etc.).

      - *(string) --*

    - **EngineVersion** *(string) --*

      The new cache engine version that the cluster runs.

    - **CacheNodeType** *(string) --*

      The cache node type that this cluster or replication group is scaled to.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRebootCacheClusterResponseCacheCluster` `SecurityGroups`

    Represents a single cache security group and its status.

    - **SecurityGroupId** *(string) --*

      The identifier of the cache security group.

    - **Status** *(string) --*

      The status of the cache security group membership. The status changes whenever a cache
      security group is modified, or when the cache security groups assigned to a cluster are
      modified.
    """


_ClientRebootCacheClusterResponseCacheClusterTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseCacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": ClientRebootCacheClusterResponseCacheClusterConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootCacheClusterResponseCacheClusterPendingModifiedValuesTypeDef,
        "NotificationConfiguration": ClientRebootCacheClusterResponseCacheClusterNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            ClientRebootCacheClusterResponseCacheClusterCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": ClientRebootCacheClusterResponseCacheClusterCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[
            ClientRebootCacheClusterResponseCacheClusterCacheNodesTypeDef
        ],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[
            ClientRebootCacheClusterResponseCacheClusterSecurityGroupsTypeDef
        ],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class ClientRebootCacheClusterResponseCacheClusterTypeDef(
    _ClientRebootCacheClusterResponseCacheClusterTypeDef
):
    """
    Type definition for `ClientRebootCacheClusterResponse` `CacheCluster`

    Contains all of the attributes of a specific cluster.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the cluster. This identifier is a unique key that
      identifies a cluster.

    - **ConfigurationEndpoint** *(dict) --*

      Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
      cluster, can be used by an application to connect to any node in the cluster. The
      configuration endpoint will always have ``.cfg`` in it.

      Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ClientDownloadLandingPage** *(string) --*

      The URL of the web page where you can download the latest ElastiCache client library.

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared to
      their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
         ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
        node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine that is used in this cluster.

    - **CacheClusterStatus** *(string) --*

      The current state of this cluster, one of the following values: ``available`` ,
      ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
      ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the cluster is located or "Multiple" if the
      cache nodes are located in different Availability Zones.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It is
      specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
      maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **PendingModifiedValues** *(dict) --*

      A group of settings that are applied to the cluster in the future, or that are currently
      being applied.

      - **NumCacheNodes** *(integer) --*

        The new number of cache nodes for the cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **CacheNodeIdsToRemove** *(list) --*

        A list of cache node IDs that are being removed (or will be removed) from the cluster. A
        node ID is a 4-digit numeric identifier (0001, 0002, etc.).

        - *(string) --*

      - **EngineVersion** *(string) --*

        The new cache engine version that the cluster runs.

      - **CacheNodeType** *(string) --*

        The cache node type that this cluster or replication group is scaled to.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for publishing
      ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **CacheSecurityGroups** *(list) --*

      A list of cache security group elements, composed of name and status sub-elements.

      - *(dict) --*

        Represents a cluster's status within a particular cache security group.

        - **CacheSecurityGroupName** *(string) --*

          The name of the cache security group.

        - **Status** *(string) --*

          The membership status in the cache security group. The status changes when a cache
          security group is modified, or when the cache security groups assigned to a cluster are
          modified.

    - **CacheParameterGroup** *(dict) --*

      Status of the cache parameter group.

      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **CacheNodeIdsToReboot** *(list) --*

        A list of the cache node IDs which need to be rebooted for parameter changes to be
        applied. A node ID is a numeric identifier (0001, 0002, etc.).

        - *(string) --*

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the cluster.

    - **CacheNodes** *(list) --*

      A list of cache nodes that are members of the cluster.

      - *(dict) --*

        Represents an individual cache node within a cluster. Each cache node runs its own
        instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared
        to their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
          types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
          **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
          ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

        - **CacheNodeId** *(string) --*

          The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
          combination of cluster ID and node ID uniquely identifies every cache node used in a
          customer's AWS account.

        - **CacheNodeStatus** *(string) --*

          The current state of this cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created.

        - **Endpoint** *(dict) --*

          The hostname for connecting to this cache node.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group applied to this cache node.

        - **SourceCacheNodeId** *(string) --*

          The ID of the primary node to which this read replica node is synchronized. If this
          field is empty, this node is not associated with a primary cluster.

        - **CustomerAvailabilityZone** *(string) --*

          The Availability Zone where this node was created and now resides.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SecurityGroups** *(list) --*

      A list of VPC Security Groups associated with the cluster.

      - *(dict) --*

        Represents a single cache security group and its status.

        - **SecurityGroupId** *(string) --*

          The identifier of the cache security group.

        - **Status** *(string) --*

          The status of the cache security group membership. The status changes whenever a cache
          security group is modified, or when the cache security groups assigned to a cluster are
          modified.

    - **ReplicationGroupId** *(string) --*

      The replication group to which this cluster belongs. If this field is empty, the cluster is
      not associated with any replication group.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your cluster.

      Example: ``05:00-09:00``

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``
    """


_ClientRebootCacheClusterResponseTypeDef = TypedDict(
    "_ClientRebootCacheClusterResponseTypeDef",
    {"CacheCluster": ClientRebootCacheClusterResponseCacheClusterTypeDef},
    total=False,
)


class ClientRebootCacheClusterResponseTypeDef(_ClientRebootCacheClusterResponseTypeDef):
    """
    Type definition for `ClientRebootCacheCluster` `Response`

    - **CacheCluster** *(dict) --*

      Contains all of the attributes of a specific cluster.

      - **CacheClusterId** *(string) --*

        The user-supplied identifier of the cluster. This identifier is a unique key that
        identifies a cluster.

      - **ConfigurationEndpoint** *(dict) --*

        Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
        cluster, can be used by an application to connect to any node in the cluster. The
        configuration endpoint will always have ``.cfg`` in it.

        Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **ClientDownloadLandingPage** *(string) --*

        The URL of the web page where you can download the latest ElastiCache client library.

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for the cluster.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when compared to
        their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
          ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
          ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node types:**
           ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1
          node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
          ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
          ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` , ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
          ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

      - **Engine** *(string) --*

        The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

      - **EngineVersion** *(string) --*

        The version of the cache engine that is used in this cluster.

      - **CacheClusterStatus** *(string) --*

        The current state of this cluster, one of the following values: ``available`` ,
        ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
        ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

      - **NumCacheNodes** *(integer) --*

        The number of cache nodes in the cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **PreferredAvailabilityZone** *(string) --*

        The name of the Availability Zone in which the cluster is located or "Multiple" if the
        cache nodes are located in different Availability Zones.

      - **CacheClusterCreateTime** *(datetime) --*

        The date and time when the cluster was created.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which maintenance on the cluster is performed. It is
        specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum
        maintenance window is a 60 minute period.

        Valid values for ``ddd`` are:

        * ``sun``

        * ``mon``

        * ``tue``

        * ``wed``

        * ``thu``

        * ``fri``

        * ``sat``

        Example: ``sun:23:00-mon:01:30``

      - **PendingModifiedValues** *(dict) --*

        A group of settings that are applied to the cluster in the future, or that are currently
        being applied.

        - **NumCacheNodes** *(integer) --*

          The new number of cache nodes for the cluster.

          For clusters running Redis, this value must be 1. For clusters running Memcached, this
          value must be between 1 and 20.

        - **CacheNodeIdsToRemove** *(list) --*

          A list of cache node IDs that are being removed (or will be removed) from the cluster. A
          node ID is a 4-digit numeric identifier (0001, 0002, etc.).

          - *(string) --*

        - **EngineVersion** *(string) --*

          The new cache engine version that the cluster runs.

        - **CacheNodeType** *(string) --*

          The cache node type that this cluster or replication group is scaled to.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **NotificationConfiguration** *(dict) --*

        Describes a notification topic and its status. Notification topics are used for publishing
        ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the topic.

        - **TopicStatus** *(string) --*

          The current state of the topic.

      - **CacheSecurityGroups** *(list) --*

        A list of cache security group elements, composed of name and status sub-elements.

        - *(dict) --*

          Represents a cluster's status within a particular cache security group.

          - **CacheSecurityGroupName** *(string) --*

            The name of the cache security group.

          - **Status** *(string) --*

            The membership status in the cache security group. The status changes when a cache
            security group is modified, or when the cache security groups assigned to a cluster are
            modified.

      - **CacheParameterGroup** *(dict) --*

        Status of the cache parameter group.

        - **CacheParameterGroupName** *(string) --*

          The name of the cache parameter group.

        - **ParameterApplyStatus** *(string) --*

          The status of parameter updates.

        - **CacheNodeIdsToReboot** *(list) --*

          A list of the cache node IDs which need to be rebooted for parameter changes to be
          applied. A node ID is a numeric identifier (0001, 0002, etc.).

          - *(string) --*

      - **CacheSubnetGroupName** *(string) --*

        The name of the cache subnet group associated with the cluster.

      - **CacheNodes** *(list) --*

        A list of cache nodes that are members of the cluster.

        - *(dict) --*

          Represents an individual cache node within a cluster. Each cache node runs its own
          instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

          The following node types are supported by ElastiCache. Generally speaking, the current
          generation types provide more memory and computational power at lower cost when compared
          to their equivalent previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
            ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
            ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
            types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
            **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
            ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
            ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
            ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
            ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
            ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
          Redis version 2.8.22 and later.

          - **CacheNodeId** *(string) --*

            The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
            combination of cluster ID and node ID uniquely identifies every cache node used in a
            customer's AWS account.

          - **CacheNodeStatus** *(string) --*

            The current state of this cache node.

          - **CacheNodeCreateTime** *(datetime) --*

            The date and time when the cache node was created.

          - **Endpoint** *(dict) --*

            The hostname for connecting to this cache node.

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ParameterGroupStatus** *(string) --*

            The status of the parameter group applied to this cache node.

          - **SourceCacheNodeId** *(string) --*

            The ID of the primary node to which this read replica node is synchronized. If this
            field is empty, this node is not associated with a primary cluster.

          - **CustomerAvailabilityZone** *(string) --*

            The Availability Zone where this node was created and now resides.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        This parameter is currently disabled.

      - **SecurityGroups** *(list) --*

        A list of VPC Security Groups associated with the cluster.

        - *(dict) --*

          Represents a single cache security group and its status.

          - **SecurityGroupId** *(string) --*

            The identifier of the cache security group.

          - **Status** *(string) --*

            The status of the cache security group membership. The status changes whenever a cache
            security group is modified, or when the cache security groups assigned to a cluster are
            modified.

      - **ReplicationGroupId** *(string) --*

        The replication group to which this cluster belongs. If this field is empty, the cluster is
        not associated with any replication group.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your cluster.

        Example: ``05:00-09:00``

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``
    """


_ClientRemoveTagsFromResourceResponseTagListTypeDef = TypedDict(
    "_ClientRemoveTagsFromResourceResponseTagListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRemoveTagsFromResourceResponseTagListTypeDef(
    _ClientRemoveTagsFromResourceResponseTagListTypeDef
):
    """
    Type definition for `ClientRemoveTagsFromResourceResponse` `TagList`

    A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
    Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

    - **Key** *(string) --*

      The key for the tag. May not be null.

    - **Value** *(string) --*

      The tag's value. May be null.
    """


_ClientRemoveTagsFromResourceResponseTypeDef = TypedDict(
    "_ClientRemoveTagsFromResourceResponseTypeDef",
    {"TagList": List[ClientRemoveTagsFromResourceResponseTagListTypeDef]},
    total=False,
)


class ClientRemoveTagsFromResourceResponseTypeDef(
    _ClientRemoveTagsFromResourceResponseTypeDef
):
    """
    Type definition for `ClientRemoveTagsFromResource` `Response`

    Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and
    ``RemoveTagsFromResource`` operations.

    - **TagList** *(list) --*

      A list of cost allocation tags as key-value pairs.

      - *(dict) --*

        A cost allocation Tag that can be added to an ElastiCache cluster or replication group.
        Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

        - **Key** *(string) --*

          The key for the tag. May not be null.

        - **Value** *(string) --*

          The tag's value. May be null.
    """


_ClientResetCacheParameterGroupParameterNameValuesTypeDef = TypedDict(
    "_ClientResetCacheParameterGroupParameterNameValuesTypeDef",
    {"ParameterName": str, "ParameterValue": str},
    total=False,
)


class ClientResetCacheParameterGroupParameterNameValuesTypeDef(
    _ClientResetCacheParameterGroupParameterNameValuesTypeDef
):
    """
    Type definition for `ClientResetCacheParameterGroup` `ParameterNameValues`

    Describes a name-value pair that is used to update the value of a parameter.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The value of the parameter.
    """


_ClientResetCacheParameterGroupResponseTypeDef = TypedDict(
    "_ClientResetCacheParameterGroupResponseTypeDef",
    {"CacheParameterGroupName": str},
    total=False,
)


class ClientResetCacheParameterGroupResponseTypeDef(
    _ClientResetCacheParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientResetCacheParameterGroup` `Response`

    Represents the output of one of the following operations:

    * ``ModifyCacheParameterGroup``

    * ``ResetCacheParameterGroup``

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.
    """


_ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef = TypedDict(
    "_ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)


class ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef(
    _ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
):
    """
    Type definition for `ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroup` `EC2SecurityGroups`

    Provides ownership and status information for an Amazon EC2 security group.

    - **Status** *(string) --*

      The status of the Amazon EC2 security group.

    - **EC2SecurityGroupName** *(string) --*

      The name of the Amazon EC2 security group.

    - **EC2SecurityGroupOwnerId** *(string) --*

      The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef = TypedDict(
    "_ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)


class ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef(
    _ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef
):
    """
    Type definition for `ClientRevokeCacheSecurityGroupIngressResponse` `CacheSecurityGroup`

    Represents the output of one of the following operations:

    * ``AuthorizeCacheSecurityGroupIngress``

    * ``CreateCacheSecurityGroup``

    * ``RevokeCacheSecurityGroupIngress``

    - **OwnerId** *(string) --*

      The AWS account ID of the cache security group owner.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Description** *(string) --*

      The description of the cache security group.

    - **EC2SecurityGroups** *(list) --*

      A list of Amazon EC2 security groups that are associated with this cache security group.

      - *(dict) --*

        Provides ownership and status information for an Amazon EC2 security group.

        - **Status** *(string) --*

          The status of the Amazon EC2 security group.

        - **EC2SecurityGroupName** *(string) --*

          The name of the Amazon EC2 security group.

        - **EC2SecurityGroupOwnerId** *(string) --*

          The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientRevokeCacheSecurityGroupIngressResponseTypeDef = TypedDict(
    "_ClientRevokeCacheSecurityGroupIngressResponseTypeDef",
    {
        "CacheSecurityGroup": ClientRevokeCacheSecurityGroupIngressResponseCacheSecurityGroupTypeDef
    },
    total=False,
)


class ClientRevokeCacheSecurityGroupIngressResponseTypeDef(
    _ClientRevokeCacheSecurityGroupIngressResponseTypeDef
):
    """
    Type definition for `ClientRevokeCacheSecurityGroupIngress` `Response`

    - **CacheSecurityGroup** *(dict) --*

      Represents the output of one of the following operations:

      * ``AuthorizeCacheSecurityGroupIngress``

      * ``CreateCacheSecurityGroup``

      * ``RevokeCacheSecurityGroupIngress``

      - **OwnerId** *(string) --*

        The AWS account ID of the cache security group owner.

      - **CacheSecurityGroupName** *(string) --*

        The name of the cache security group.

      - **Description** *(string) --*

        The description of the cache security group.

      - **EC2SecurityGroups** *(list) --*

        A list of Amazon EC2 security groups that are associated with this cache security group.

        - *(dict) --*

          Provides ownership and status information for an Amazon EC2 security group.

          - **Status** *(string) --*

            The status of the Amazon EC2 security group.

          - **EC2SecurityGroupName** *(string) --*

            The name of the Amazon EC2 security group.

          - **EC2SecurityGroupOwnerId** *(string) --*

            The AWS account ID of the Amazon EC2 security group owner.
    """


_ClientStartMigrationCustomerNodeEndpointListTypeDef = TypedDict(
    "_ClientStartMigrationCustomerNodeEndpointListTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientStartMigrationCustomerNodeEndpointListTypeDef(
    _ClientStartMigrationCustomerNodeEndpointListTypeDef
):
    """
    Type definition for `ClientStartMigration` `CustomerNodeEndpointList`

    The endpoint from which data should be migrated.

    - **Address** *(string) --*

      The address of the node endpoint

    - **Port** *(integer) --*

      The port of the node endpoint
    """


_ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientStartMigrationResponseReplicationGroup` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `ClientStartMigrationResponseReplicationGroupNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` . This
      member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `ClientStartMigrationResponseReplicationGroupNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `ClientStartMigrationResponseReplicationGroupNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientStartMigrationResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientStartMigrationResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientStartMigrationResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef(
    _ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef
):
    """
    Type definition for `ClientStartMigrationResponseReplicationGroup` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node group
    is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled) replication
      group contains only 1 node group; therefore, the node group ID is 0001. A Redis
      (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
      0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` . This
          member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `ClientStartMigrationResponseReplicationGroupPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `ClientStartMigrationResponseReplicationGroupPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientStartMigrationResponseReplicationGroup` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientStartMigrationResponseReplicationGroupTypeDef = TypedDict(
    "_ClientStartMigrationResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientStartMigrationResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            ClientStartMigrationResponseReplicationGroupNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": ClientStartMigrationResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientStartMigrationResponseReplicationGroupTypeDef(
    _ClientStartMigrationResponseReplicationGroupTypeDef
):
    """
    Type definition for `ClientStartMigrationResponse` `ReplicationGroup`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , ``modifying``
      , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node group
        is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled) replication
          group contains only 1 node group; therefore, the node group ID is 0001. A Redis
          (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
          0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` . This
              member is only applicable for Redis (cluster mode disabled) replication groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
      range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientStartMigrationResponseTypeDef = TypedDict(
    "_ClientStartMigrationResponseTypeDef",
    {"ReplicationGroup": ClientStartMigrationResponseReplicationGroupTypeDef},
    total=False,
)


class ClientStartMigrationResponseTypeDef(_ClientStartMigrationResponseTypeDef):
    """
    Type definition for `ClientStartMigration` `Response`

    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.

      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.

      - **Description** *(string) --*

        The user supplied description of the replication group.

      - **Status** *(string) --*

        The current state of this replication group - ``creating`` , ``available`` , ``modifying``
        , ``deleting`` , ``create-failed`` , ``snapshotting`` .

      - **PendingModifiedValues** *(dict) --*

        A group of settings to be applied to the replication group, either immediately or during
        the next maintenance window.

        - **PrimaryClusterId** *(string) --*

          The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
          specified), or during the next maintenance window.

        - **AutomaticFailoverStatus** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **Resharding** *(dict) --*

          The status of an online resharding operation.

          - **SlotMigration** *(dict) --*

            Represents the progress of an online resharding operation.

            - **ProgressPercentage** *(float) --*

              The percentage of the slot migration that is complete.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **MemberClusters** *(list) --*

        The names of all the cache clusters that are part of this replication group.

        - *(string) --*

      - **NodeGroups** *(list) --*

        A list of node groups in this replication group. For Redis (cluster mode disabled)
        replication groups, this is a single-element list. For Redis (cluster mode enabled)
        replication groups, the list contains an entry for each node group (shard).

        - *(dict) --*

          Represents a collection of cache nodes in a replication group. One node in the node group
          is the read/write primary node. All the other nodes are read-only Replica nodes.

          - **NodeGroupId** *(string) --*

            The identifier for the node group (shard). A Redis (cluster mode disabled) replication
            group contains only 1 node group; therefore, the node group ID is 0001. A Redis
            (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
            0090. Optionally, the user can provide the id for a node group.

          - **Status** *(string) --*

            The current state of this replication group - ``creating`` , ``available`` , etc.

          - **PrimaryEndpoint** *(dict) --*

            The endpoint of the primary node in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ReaderEndpoint** *(dict) --*

            The endpoint of the replica nodes in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **Slots** *(string) --*

            The keyspace for this node group (shard).

          - **NodeGroupMembers** *(list) --*

            A list containing information about individual nodes within the node group (shard).

            - *(dict) --*

              Represents a single node within a node group (shard).

              - **CacheClusterId** *(string) --*

                The ID of the cluster to which the node belongs.

              - **CacheNodeId** *(string) --*

                The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                0002, etc.).

              - **ReadEndpoint** *(dict) --*

                The information required for client programs to connect to a node for read
                operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                clusters.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the node is located.

              - **CurrentRole** *(string) --*

                The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                member is only applicable for Redis (cluster mode disabled) replication groups.

      - **SnapshottingClusterId** *(string) --*

        The cluster ID that is used as the daily snapshot source for the replication group.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **ConfigurationEndpoint** *(dict) --*

        The configuration endpoint for this replication group. Use the configuration endpoint to
        connect to this replication group.

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
        range.

        .. note::

          This parameter is only valid if the ``Engine`` parameter is ``redis`` .

      - **ClusterEnabled** *(boolean) --*

        A flag indicating whether or not this replication group is cluster enabled; i.e., whether
        its data can be partitioned across multiple shards (API/CLI: node groups).

        Valid values: ``true`` | ``false``

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for each node in the replication
        group.

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef(
    _ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef
):
    """
    Type definition for `ClientTestFailoverResponseReplicationGroup` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef(
    _ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `ClientTestFailoverResponseReplicationGroupNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` . This
      member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef(
    _ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `ClientTestFailoverResponseReplicationGroupNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef(
    _ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `ClientTestFailoverResponseReplicationGroupNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": ClientTestFailoverResponseReplicationGroupNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": ClientTestFailoverResponseReplicationGroupNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            ClientTestFailoverResponseReplicationGroupNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef(
    _ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef
):
    """
    Type definition for `ClientTestFailoverResponseReplicationGroup` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node group
    is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled) replication
      group contains only 1 node group; therefore, the node group ID is 0001. A Redis
      (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
      0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` . This
          member is only applicable for Redis (cluster mode disabled) replication groups.
    """


_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `ClientTestFailoverResponseReplicationGroupPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef(
    _ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `ClientTestFailoverResponseReplicationGroupPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef(
    _ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientTestFailoverResponseReplicationGroup` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_ClientTestFailoverResponseReplicationGroupTypeDef = TypedDict(
    "_ClientTestFailoverResponseReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": ClientTestFailoverResponseReplicationGroupPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[ClientTestFailoverResponseReplicationGroupNodeGroupsTypeDef],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": ClientTestFailoverResponseReplicationGroupConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class ClientTestFailoverResponseReplicationGroupTypeDef(
    _ClientTestFailoverResponseReplicationGroupTypeDef
):
    """
    Type definition for `ClientTestFailoverResponse` `ReplicationGroup`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , ``modifying``
      , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node group
        is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled) replication
          group contains only 1 node group; therefore, the node group ID is 0001. A Redis
          (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
          0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` . This
              member is only applicable for Redis (cluster mode disabled) replication groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
      taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
      range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
      enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
      when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_ClientTestFailoverResponseTypeDef = TypedDict(
    "_ClientTestFailoverResponseTypeDef",
    {"ReplicationGroup": ClientTestFailoverResponseReplicationGroupTypeDef},
    total=False,
)


class ClientTestFailoverResponseTypeDef(_ClientTestFailoverResponseTypeDef):
    """
    Type definition for `ClientTestFailover` `Response`

    - **ReplicationGroup** *(dict) --*

      Contains all of the attributes of a specific Redis replication group.

      - **ReplicationGroupId** *(string) --*

        The identifier for the replication group.

      - **Description** *(string) --*

        The user supplied description of the replication group.

      - **Status** *(string) --*

        The current state of this replication group - ``creating`` , ``available`` , ``modifying``
        , ``deleting`` , ``create-failed`` , ``snapshotting`` .

      - **PendingModifiedValues** *(dict) --*

        A group of settings to be applied to the replication group, either immediately or during
        the next maintenance window.

        - **PrimaryClusterId** *(string) --*

          The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
          specified), or during the next maintenance window.

        - **AutomaticFailoverStatus** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **Resharding** *(dict) --*

          The status of an online resharding operation.

          - **SlotMigration** *(dict) --*

            Represents the progress of an online resharding operation.

            - **ProgressPercentage** *(float) --*

              The percentage of the slot migration that is complete.

        - **AuthTokenStatus** *(string) --*

          The auth token status

      - **MemberClusters** *(list) --*

        The names of all the cache clusters that are part of this replication group.

        - *(string) --*

      - **NodeGroups** *(list) --*

        A list of node groups in this replication group. For Redis (cluster mode disabled)
        replication groups, this is a single-element list. For Redis (cluster mode enabled)
        replication groups, the list contains an entry for each node group (shard).

        - *(dict) --*

          Represents a collection of cache nodes in a replication group. One node in the node group
          is the read/write primary node. All the other nodes are read-only Replica nodes.

          - **NodeGroupId** *(string) --*

            The identifier for the node group (shard). A Redis (cluster mode disabled) replication
            group contains only 1 node group; therefore, the node group ID is 0001. A Redis
            (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to
            0090. Optionally, the user can provide the id for a node group.

          - **Status** *(string) --*

            The current state of this replication group - ``creating`` , ``available`` , etc.

          - **PrimaryEndpoint** *(dict) --*

            The endpoint of the primary node in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **ReaderEndpoint** *(dict) --*

            The endpoint of the replica nodes in this node group (shard).

            - **Address** *(string) --*

              The DNS hostname of the cache node.

            - **Port** *(integer) --*

              The port number that the cache engine is listening on.

          - **Slots** *(string) --*

            The keyspace for this node group (shard).

          - **NodeGroupMembers** *(list) --*

            A list containing information about individual nodes within the node group (shard).

            - *(dict) --*

              Represents a single node within a node group (shard).

              - **CacheClusterId** *(string) --*

                The ID of the cluster to which the node belongs.

              - **CacheNodeId** *(string) --*

                The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                0002, etc.).

              - **ReadEndpoint** *(dict) --*

                The information required for client programs to connect to a node for read
                operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                clusters.

                - **Address** *(string) --*

                  The DNS hostname of the cache node.

                - **Port** *(integer) --*

                  The port number that the cache engine is listening on.

              - **PreferredAvailabilityZone** *(string) --*

                The name of the Availability Zone in which the node is located.

              - **CurrentRole** *(string) --*

                The role that is currently assigned to the node - ``primary`` or ``replica`` . This
                member is only applicable for Redis (cluster mode disabled) replication groups.

      - **SnapshottingClusterId** *(string) --*

        The cluster ID that is used as the daily snapshot source for the replication group.

      - **AutomaticFailover** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **ConfigurationEndpoint** *(dict) --*

        The configuration endpoint for this replication group. Use the configuration endpoint to
        connect to this replication group.

        - **Address** *(string) --*

          The DNS hostname of the cache node.

        - **Port** *(integer) --*

          The port number that the cache engine is listening on.

      - **SnapshotRetentionLimit** *(integer) --*

        The number of days for which ElastiCache retains automatic cluster snapshots before
        deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was
        taken today is retained for 5 days before being deleted.

        .. warning::

          If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

      - **SnapshotWindow** *(string) --*

        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
        your node group (shard).

        Example: ``05:00-09:00``

        If you do not specify this parameter, ElastiCache automatically chooses an appropriate time
        range.

        .. note::

          This parameter is only valid if the ``Engine`` parameter is ``redis`` .

      - **ClusterEnabled** *(boolean) --*

        A flag indicating whether or not this replication group is cluster enabled; i.e., whether
        its data can be partitioned across multiple shards (API/CLI: node groups).

        Valid values: ``true`` | ``false``

      - **CacheNodeType** *(string) --*

        The name of the compute and memory capacity node type for each node in the replication
        group.

      - **AuthTokenEnabled** *(boolean) --*

        A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

        Default: ``false``

      - **AuthTokenLastModifiedDate** *(datetime) --*

        The date the auth token was last modified

      - **TransitEncryptionEnabled** *(boolean) --*

        A flag that enables in-transit encryption when set to ``true`` .

        You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
        To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
        ``true`` when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **AtRestEncryptionEnabled** *(boolean) --*

        A flag that enables encryption at-rest when set to ``true`` .

        You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To
        enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true``
        when you create a cluster.

         **Required:** Only available when creating a replication group in an Amazon VPC using
         redis version ``3.2.6`` , ``4.x`` or later.

        Default: ``false``

      - **KmsKeyId** *(string) --*

        The ID of the KMS key used to encrypt the disk in the cluster.
    """


_DescribeCacheClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheClustersPaginatePaginationConfigTypeDef(
    _DescribeCacheClustersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginate` `PaginationConfig`

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


_DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginateResponseCacheClustersCacheNodes` `Endpoint`

    The hostname for connecting to this cache node.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": DescribeCacheClustersPaginateResponseCacheClustersCacheNodesEndpointTypeDef,
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
    },
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginateResponseCacheClusters` `CacheNodes`

    Represents an individual cache node within a cluster. Each cache node runs its own
    instance of the cluster's protocol-compliant caching software - either Memcached or
    Redis.

    The following node types are supported by ElastiCache. Generally speaking, the current
    generation types provide more memory and computational power at lower cost when
    compared to their equivalent previous generation counterparts.

    * General purpose:

      * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge``
      , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
      ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge``
      , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
      types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

      * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
      **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
      ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
      ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

    * Compute optimized:

      * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

    * Memory optimized:

      * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge``
      , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
      ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge``
      , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
      ``cache.r4.16xlarge``

      * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
      ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large``
      , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` ,
      ``cache.r3.8xlarge``

     **Additional node type info**

    * All current generation instance types are created in Amazon VPC by default.

    * Redis append-only files (AOF) are not supported for T1 or T2 instances.

    * Redis Multi-AZ with automatic failover is not supported on T1 instances.

    * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
    Redis version 2.8.22 and later.

    - **CacheNodeId** *(string) --*

      The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
      combination of cluster ID and node ID uniquely identifies every cache node used in a
      customer's AWS account.

    - **CacheNodeStatus** *(string) --*

      The current state of this cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created.

    - **Endpoint** *(dict) --*

      The hostname for connecting to this cache node.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ParameterGroupStatus** *(string) --*

      The status of the parameter group applied to this cache node.

    - **SourceCacheNodeId** *(string) --*

      The ID of the primary node to which this read replica node is synchronized. If this
      field is empty, this node is not associated with a primary cluster.

    - **CustomerAvailabilityZone** *(string) --*

      The Availability Zone where this node was created and now resides.
    """


_DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginateResponseCacheClusters` `CacheParameterGroup`

    Status of the cache parameter group.

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.

    - **ParameterApplyStatus** *(string) --*

      The status of parameter updates.

    - **CacheNodeIdsToReboot** *(list) --*

      A list of the cache node IDs which need to be rebooted for parameter changes to be
      applied. A node ID is a numeric identifier (0001, 0002, etc.).

      - *(string) --*
    """


_DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef",
    {"CacheSecurityGroupName": str, "Status": str},
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginateResponseCacheClusters` `CacheSecurityGroups`

    Represents a cluster's status within a particular cache security group.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Status** *(string) --*

      The membership status in the cache security group. The status changes when a cache
      security group is modified, or when the cache security groups assigned to a cluster
      are modified.
    """


_DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginateResponseCacheClusters` `ConfigurationEndpoint`

    Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
    cluster, can be used by an application to connect to any node in the cluster. The
    configuration endpoint will always have ``.cfg`` in it.

    Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef",
    {"TopicArn": str, "TopicStatus": str},
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginateResponseCacheClusters` `NotificationConfiguration`

    Describes a notification topic and its status. Notification topics are used for
    publishing ElastiCache events to subscribers using Amazon Simple Notification Service
    (SNS).

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the topic.

    - **TopicStatus** *(string) --*

      The current state of the topic.
    """


_DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": str,
    },
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginateResponseCacheClusters` `PendingModifiedValues`

    A group of settings that are applied to the cluster in the future, or that are currently
    being applied.

    - **NumCacheNodes** *(integer) --*

      The new number of cache nodes for the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **CacheNodeIdsToRemove** *(list) --*

      A list of cache node IDs that are being removed (or will be removed) from the cluster.
      A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

      - *(string) --*

    - **EngineVersion** *(string) --*

      The new cache engine version that the cluster runs.

    - **CacheNodeType** *(string) --*

      The cache node type that this cluster or replication group is scaled to.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef",
    {"SecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginateResponseCacheClusters` `SecurityGroups`

    Represents a single cache security group and its status.

    - **SecurityGroupId** *(string) --*

      The identifier of the cache security group.

    - **Status** *(string) --*

      The status of the cache security group membership. The status changes whenever a
      cache security group is modified, or when the cache security groups assigned to a
      cluster are modified.
    """


_DescribeCacheClustersPaginateResponseCacheClustersTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseCacheClustersTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": DescribeCacheClustersPaginateResponseCacheClustersConfigurationEndpointTypeDef,
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": DescribeCacheClustersPaginateResponseCacheClustersPendingModifiedValuesTypeDef,
        "NotificationConfiguration": DescribeCacheClustersPaginateResponseCacheClustersNotificationConfigurationTypeDef,
        "CacheSecurityGroups": List[
            DescribeCacheClustersPaginateResponseCacheClustersCacheSecurityGroupsTypeDef
        ],
        "CacheParameterGroup": DescribeCacheClustersPaginateResponseCacheClustersCacheParameterGroupTypeDef,
        "CacheSubnetGroupName": str,
        "CacheNodes": List[
            DescribeCacheClustersPaginateResponseCacheClustersCacheNodesTypeDef
        ],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List[
            DescribeCacheClustersPaginateResponseCacheClustersSecurityGroupsTypeDef
        ],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
    },
    total=False,
)


class DescribeCacheClustersPaginateResponseCacheClustersTypeDef(
    _DescribeCacheClustersPaginateResponseCacheClustersTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginateResponse` `CacheClusters`

    Contains all of the attributes of a specific cluster.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the cluster. This identifier is a unique key that
      identifies a cluster.

    - **ConfigurationEndpoint** *(dict) --*

      Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
      cluster, can be used by an application to connect to any node in the cluster. The
      configuration endpoint will always have ``.cfg`` in it.

      Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ClientDownloadLandingPage** *(string) --*

      The URL of the web page where you can download the latest ElastiCache client library.

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared
      to their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
        types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
        **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
        ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine that is used in this cluster.

    - **CacheClusterStatus** *(string) --*

      The current state of this cluster, one of the following values: ``available`` ,
      ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
      ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the cluster is located or "Multiple" if the
      cache nodes are located in different Availability Zones.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It
      is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The
      minimum maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **PendingModifiedValues** *(dict) --*

      A group of settings that are applied to the cluster in the future, or that are currently
      being applied.

      - **NumCacheNodes** *(integer) --*

        The new number of cache nodes for the cluster.

        For clusters running Redis, this value must be 1. For clusters running Memcached, this
        value must be between 1 and 20.

      - **CacheNodeIdsToRemove** *(list) --*

        A list of cache node IDs that are being removed (or will be removed) from the cluster.
        A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

        - *(string) --*

      - **EngineVersion** *(string) --*

        The new cache engine version that the cluster runs.

      - **CacheNodeType** *(string) --*

        The cache node type that this cluster or replication group is scaled to.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **NotificationConfiguration** *(dict) --*

      Describes a notification topic and its status. Notification topics are used for
      publishing ElastiCache events to subscribers using Amazon Simple Notification Service
      (SNS).

      - **TopicArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the topic.

      - **TopicStatus** *(string) --*

        The current state of the topic.

    - **CacheSecurityGroups** *(list) --*

      A list of cache security group elements, composed of name and status sub-elements.

      - *(dict) --*

        Represents a cluster's status within a particular cache security group.

        - **CacheSecurityGroupName** *(string) --*

          The name of the cache security group.

        - **Status** *(string) --*

          The membership status in the cache security group. The status changes when a cache
          security group is modified, or when the cache security groups assigned to a cluster
          are modified.

    - **CacheParameterGroup** *(dict) --*

      Status of the cache parameter group.

      - **CacheParameterGroupName** *(string) --*

        The name of the cache parameter group.

      - **ParameterApplyStatus** *(string) --*

        The status of parameter updates.

      - **CacheNodeIdsToReboot** *(list) --*

        A list of the cache node IDs which need to be rebooted for parameter changes to be
        applied. A node ID is a numeric identifier (0001, 0002, etc.).

        - *(string) --*

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the cluster.

    - **CacheNodes** *(list) --*

      A list of cache nodes that are members of the cluster.

      - *(dict) --*

        Represents an individual cache node within a cluster. Each cache node runs its own
        instance of the cluster's protocol-compliant caching software - either Memcached or
        Redis.

        The following node types are supported by ElastiCache. Generally speaking, the current
        generation types provide more memory and computational power at lower cost when
        compared to their equivalent previous generation counterparts.

        * General purpose:

          * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge``
          , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
          ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge``
          , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
          types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

          * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
          **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
          ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
          ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

        * Compute optimized:

          * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

        * Memory optimized:

          * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge``
          , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
          ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge``
          , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
          ``cache.r4.16xlarge``

          * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
          ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large``
          , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` ,
          ``cache.r3.8xlarge``

         **Additional node type info**

        * All current generation instance types are created in Amazon VPC by default.

        * Redis append-only files (AOF) are not supported for T1 or T2 instances.

        * Redis Multi-AZ with automatic failover is not supported on T1 instances.

        * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
        Redis version 2.8.22 and later.

        - **CacheNodeId** *(string) --*

          The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
          combination of cluster ID and node ID uniquely identifies every cache node used in a
          customer's AWS account.

        - **CacheNodeStatus** *(string) --*

          The current state of this cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created.

        - **Endpoint** *(dict) --*

          The hostname for connecting to this cache node.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ParameterGroupStatus** *(string) --*

          The status of the parameter group applied to this cache node.

        - **SourceCacheNodeId** *(string) --*

          The ID of the primary node to which this read replica node is synchronized. If this
          field is empty, this node is not associated with a primary cluster.

        - **CustomerAvailabilityZone** *(string) --*

          The Availability Zone where this node was created and now resides.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SecurityGroups** *(list) --*

      A list of VPC Security Groups associated with the cluster.

      - *(dict) --*

        Represents a single cache security group and its status.

        - **SecurityGroupId** *(string) --*

          The identifier of the cache security group.

        - **Status** *(string) --*

          The status of the cache security group membership. The status changes whenever a
          cache security group is modified, or when the cache security groups assigned to a
          cluster are modified.

    - **ReplicationGroupId** *(string) --*

      The replication group to which this cluster belongs. If this field is empty, the cluster
      is not associated with any replication group.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that
      was taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your cluster.

      Example: ``05:00-09:00``

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created.
      To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``
    """


_DescribeCacheClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheClustersPaginateResponseTypeDef",
    {
        "CacheClusters": List[
            DescribeCacheClustersPaginateResponseCacheClustersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheClustersPaginateResponseTypeDef(
    _DescribeCacheClustersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeCacheClustersPaginate` `Response`

    Represents the output of a ``DescribeCacheClusters`` operation.

    - **CacheClusters** *(list) --*

      A list of clusters. Each item in the list contains detailed information about one cluster.

      - *(dict) --*

        Contains all of the attributes of a specific cluster.

        - **CacheClusterId** *(string) --*

          The user-supplied identifier of the cluster. This identifier is a unique key that
          identifies a cluster.

        - **ConfigurationEndpoint** *(dict) --*

          Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the
          cluster, can be used by an application to connect to any node in the cluster. The
          configuration endpoint will always have ``.cfg`` in it.

          Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ClientDownloadLandingPage** *(string) --*

          The URL of the web page where you can download the latest ElastiCache client library.

        - **CacheNodeType** *(string) --*

          The name of the compute and memory capacity node type for the cluster.

          The following node types are supported by ElastiCache. Generally speaking, the current
          generation types provide more memory and computational power at lower cost when compared
          to their equivalent previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
            ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
            ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
            types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
            **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
            ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
            ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
            ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
            ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
            ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
          Redis version 2.8.22 and later.

        - **Engine** *(string) --*

          The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

        - **EngineVersion** *(string) --*

          The version of the cache engine that is used in this cluster.

        - **CacheClusterStatus** *(string) --*

          The current state of this cluster, one of the following values: ``available`` ,
          ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` ,
          ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

        - **NumCacheNodes** *(integer) --*

          The number of cache nodes in the cluster.

          For clusters running Redis, this value must be 1. For clusters running Memcached, this
          value must be between 1 and 20.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the cluster is located or "Multiple" if the
          cache nodes are located in different Availability Zones.

        - **CacheClusterCreateTime** *(datetime) --*

          The date and time when the cluster was created.

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which maintenance on the cluster is performed. It
          is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The
          minimum maintenance window is a 60 minute period.

          Valid values for ``ddd`` are:

          * ``sun``

          * ``mon``

          * ``tue``

          * ``wed``

          * ``thu``

          * ``fri``

          * ``sat``

          Example: ``sun:23:00-mon:01:30``

        - **PendingModifiedValues** *(dict) --*

          A group of settings that are applied to the cluster in the future, or that are currently
          being applied.

          - **NumCacheNodes** *(integer) --*

            The new number of cache nodes for the cluster.

            For clusters running Redis, this value must be 1. For clusters running Memcached, this
            value must be between 1 and 20.

          - **CacheNodeIdsToRemove** *(list) --*

            A list of cache node IDs that are being removed (or will be removed) from the cluster.
            A node ID is a 4-digit numeric identifier (0001, 0002, etc.).

            - *(string) --*

          - **EngineVersion** *(string) --*

            The new cache engine version that the cluster runs.

          - **CacheNodeType** *(string) --*

            The cache node type that this cluster or replication group is scaled to.

          - **AuthTokenStatus** *(string) --*

            The auth token status

        - **NotificationConfiguration** *(dict) --*

          Describes a notification topic and its status. Notification topics are used for
          publishing ElastiCache events to subscribers using Amazon Simple Notification Service
          (SNS).

          - **TopicArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the topic.

          - **TopicStatus** *(string) --*

            The current state of the topic.

        - **CacheSecurityGroups** *(list) --*

          A list of cache security group elements, composed of name and status sub-elements.

          - *(dict) --*

            Represents a cluster's status within a particular cache security group.

            - **CacheSecurityGroupName** *(string) --*

              The name of the cache security group.

            - **Status** *(string) --*

              The membership status in the cache security group. The status changes when a cache
              security group is modified, or when the cache security groups assigned to a cluster
              are modified.

        - **CacheParameterGroup** *(dict) --*

          Status of the cache parameter group.

          - **CacheParameterGroupName** *(string) --*

            The name of the cache parameter group.

          - **ParameterApplyStatus** *(string) --*

            The status of parameter updates.

          - **CacheNodeIdsToReboot** *(list) --*

            A list of the cache node IDs which need to be rebooted for parameter changes to be
            applied. A node ID is a numeric identifier (0001, 0002, etc.).

            - *(string) --*

        - **CacheSubnetGroupName** *(string) --*

          The name of the cache subnet group associated with the cluster.

        - **CacheNodes** *(list) --*

          A list of cache nodes that are members of the cluster.

          - *(dict) --*

            Represents an individual cache node within a cluster. Each cache node runs its own
            instance of the cluster's protocol-compliant caching software - either Memcached or
            Redis.

            The following node types are supported by ElastiCache. Generally speaking, the current
            generation types provide more memory and computational power at lower cost when
            compared to their equivalent previous generation counterparts.

            * General purpose:

              * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge``
              , ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
              ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge``
              , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
              types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

              * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
              **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
              ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
              ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

            * Compute optimized:

              * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

            * Memory optimized:

              * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge``
              , ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
              ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge``
              , ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
              ``cache.r4.16xlarge``

              * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
              ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large``
              , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` ,
              ``cache.r3.8xlarge``

             **Additional node type info**

            * All current generation instance types are created in Amazon VPC by default.

            * Redis append-only files (AOF) are not supported for T1 or T2 instances.

            * Redis Multi-AZ with automatic failover is not supported on T1 instances.

            * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
            Redis version 2.8.22 and later.

            - **CacheNodeId** *(string) --*

              The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The
              combination of cluster ID and node ID uniquely identifies every cache node used in a
              customer's AWS account.

            - **CacheNodeStatus** *(string) --*

              The current state of this cache node.

            - **CacheNodeCreateTime** *(datetime) --*

              The date and time when the cache node was created.

            - **Endpoint** *(dict) --*

              The hostname for connecting to this cache node.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **ParameterGroupStatus** *(string) --*

              The status of the parameter group applied to this cache node.

            - **SourceCacheNodeId** *(string) --*

              The ID of the primary node to which this read replica node is synchronized. If this
              field is empty, this node is not associated with a primary cluster.

            - **CustomerAvailabilityZone** *(string) --*

              The Availability Zone where this node was created and now resides.

        - **AutoMinorVersionUpgrade** *(boolean) --*

          This parameter is currently disabled.

        - **SecurityGroups** *(list) --*

          A list of VPC Security Groups associated with the cluster.

          - *(dict) --*

            Represents a single cache security group and its status.

            - **SecurityGroupId** *(string) --*

              The identifier of the cache security group.

            - **Status** *(string) --*

              The status of the cache security group membership. The status changes whenever a
              cache security group is modified, or when the cache security groups assigned to a
              cluster are modified.

        - **ReplicationGroupId** *(string) --*

          The replication group to which this cluster belongs. If this field is empty, the cluster
          is not associated with any replication group.

        - **SnapshotRetentionLimit** *(integer) --*

          The number of days for which ElastiCache retains automatic cluster snapshots before
          deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that
          was taken today is retained for 5 days before being deleted.

          .. warning::

            If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

        - **SnapshotWindow** *(string) --*

          The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
          your cluster.

          Example: ``05:00-09:00``

        - **AuthTokenEnabled** *(boolean) --*

          A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

          Default: ``false``

        - **AuthTokenLastModifiedDate** *(datetime) --*

          The date the auth token was last modified

        - **TransitEncryptionEnabled** *(boolean) --*

          A flag that enables in-transit encryption when set to ``true`` .

          You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
          To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
          ``true`` when you create a cluster.

           **Required:** Only available when creating a replication group in an Amazon VPC using
           redis version ``3.2.6`` , ``4.x`` or later.

          Default: ``false``

        - **AtRestEncryptionEnabled** *(boolean) --*

          A flag that enables encryption at-rest when set to ``true`` .

          You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created.
          To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to
          ``true`` when you create a cluster.

           **Required:** Only available when creating a replication group in an Amazon VPC using
           redis version ``3.2.6`` , ``4.x`` or later.

          Default: ``false``

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef(
    _DescribeCacheEngineVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeCacheEngineVersionsPaginate` `PaginationConfig`

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


_DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef = TypedDict(
    "_DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "CacheEngineDescription": str,
        "CacheEngineVersionDescription": str,
    },
    total=False,
)


class DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef(
    _DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef
):
    """
    Type definition for `DescribeCacheEngineVersionsPaginateResponse` `CacheEngineVersions`

    Provides all of the details about a particular cache engine version.

    - **Engine** *(string) --*

      The name of the cache engine.

    - **EngineVersion** *(string) --*

      The version number of the cache engine.

    - **CacheParameterGroupFamily** *(string) --*

      The name of the cache parameter group family associated with this cache engine.

      Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
      ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

    - **CacheEngineDescription** *(string) --*

      The description of the cache engine.

    - **CacheEngineVersionDescription** *(string) --*

      The description of the cache engine version.
    """


_DescribeCacheEngineVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheEngineVersionsPaginateResponseTypeDef",
    {
        "CacheEngineVersions": List[
            DescribeCacheEngineVersionsPaginateResponseCacheEngineVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheEngineVersionsPaginateResponseTypeDef(
    _DescribeCacheEngineVersionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeCacheEngineVersionsPaginate` `Response`

    Represents the output of a  DescribeCacheEngineVersions operation.

    - **CacheEngineVersions** *(list) --*

      A list of cache engine version details. Each element in the list contains detailed
      information about one cache engine version.

      - *(dict) --*

        Provides all of the details about a particular cache engine version.

        - **Engine** *(string) --*

          The name of the cache engine.

        - **EngineVersion** *(string) --*

          The version number of the cache engine.

        - **CacheParameterGroupFamily** *(string) --*

          The name of the cache parameter group family associated with this cache engine.

          Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
          ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

        - **CacheEngineDescription** *(string) --*

          The description of the cache engine.

        - **CacheEngineVersionDescription** *(string) --*

          The description of the cache engine version.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef(
    _DescribeCacheParameterGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeCacheParameterGroupsPaginate` `PaginationConfig`

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


_DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef = TypedDict(
    "_DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef",
    {
        "CacheParameterGroupName": str,
        "CacheParameterGroupFamily": str,
        "Description": str,
    },
    total=False,
)


class DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef(
    _DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef
):
    """
    Type definition for `DescribeCacheParameterGroupsPaginateResponse` `CacheParameterGroups`

    Represents the output of a ``CreateCacheParameterGroup`` operation.

    - **CacheParameterGroupName** *(string) --*

      The name of the cache parameter group.

    - **CacheParameterGroupFamily** *(string) --*

      The name of the cache parameter group family that this cache parameter group is
      compatible with.

      Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
      ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

    - **Description** *(string) --*

      The description for this cache parameter group.
    """


_DescribeCacheParameterGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheParameterGroupsPaginateResponseTypeDef",
    {
        "CacheParameterGroups": List[
            DescribeCacheParameterGroupsPaginateResponseCacheParameterGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheParameterGroupsPaginateResponseTypeDef(
    _DescribeCacheParameterGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeCacheParameterGroupsPaginate` `Response`

    Represents the output of a ``DescribeCacheParameterGroups`` operation.

    - **CacheParameterGroups** *(list) --*

      A list of cache parameter groups. Each element in the list contains detailed information
      about one cache parameter group.

      - *(dict) --*

        Represents the output of a ``CreateCacheParameterGroup`` operation.

        - **CacheParameterGroupName** *(string) --*

          The name of the cache parameter group.

        - **CacheParameterGroupFamily** *(string) --*

          The name of the cache parameter group family that this cache parameter group is
          compatible with.

          Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
          ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

        - **Description** *(string) --*

          The description for this cache parameter group.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeCacheParametersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheParametersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheParametersPaginatePaginationConfigTypeDef(
    _DescribeCacheParametersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeCacheParametersPaginate` `PaginationConfig`

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


_DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "_DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)


class DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef(
    _DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
):
    """
    Type definition for `DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParameters` `CacheNodeTypeSpecificValues`

    A value that applies only to a certain cache node type.

    - **CacheNodeType** *(string) --*

      The cache node type for which this value applies.

    - **Value** *(string) --*

      The value for the cache node type.
    """


_DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "_DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[
            DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
        ],
        "ChangeType": str,
    },
    total=False,
)


class DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef(
    _DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef
):
    """
    Type definition for `DescribeCacheParametersPaginateResponse` `CacheNodeTypeSpecificParameters`

    A parameter that has a different value for each cache node type it is applied to. For
    example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
    ``maxmemory`` value than a ``cache.m1.small`` type.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **Description** *(string) --*

      A description of the parameter.

    - **Source** *(string) --*

      The source of the parameter value.

    - **DataType** *(string) --*

      The valid data type for the parameter.

    - **AllowedValues** *(string) --*

      The valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest cache engine version to which the parameter can apply.

    - **CacheNodeTypeSpecificValues** *(list) --*

      A list of cache node types and their corresponding values for this parameter.

      - *(dict) --*

        A value that applies only to a certain cache node type.

        - **CacheNodeType** *(string) --*

          The cache node type for which this value applies.

        - **Value** *(string) --*

          The value for the cache node type.

    - **ChangeType** *(string) --*

      Indicates whether a change to the parameter is applied immediately or requires a reboot
      for the change to be applied. You can force a reboot or wait until the next maintenance
      window's reboot. For more information, see `Rebooting a Cluster
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .
    """


_DescribeCacheParametersPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeCacheParametersPaginateResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": str,
    },
    total=False,
)


class DescribeCacheParametersPaginateResponseParametersTypeDef(
    _DescribeCacheParametersPaginateResponseParametersTypeDef
):
    """
    Type definition for `DescribeCacheParametersPaginateResponse` `Parameters`

    Describes an individual setting that controls some aspect of ElastiCache behavior.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The value of the parameter.

    - **Description** *(string) --*

      A description of the parameter.

    - **Source** *(string) --*

      The source of the parameter.

    - **DataType** *(string) --*

      The valid data type for the parameter.

    - **AllowedValues** *(string) --*

      The valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest cache engine version to which the parameter can apply.

    - **ChangeType** *(string) --*

      Indicates whether a change to the parameter is applied immediately or requires a reboot
      for the change to be applied. You can force a reboot or wait until the next maintenance
      window's reboot. For more information, see `Rebooting a Cluster
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .
    """


_DescribeCacheParametersPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheParametersPaginateResponseTypeDef",
    {
        "Parameters": List[DescribeCacheParametersPaginateResponseParametersTypeDef],
        "CacheNodeTypeSpecificParameters": List[
            DescribeCacheParametersPaginateResponseCacheNodeTypeSpecificParametersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheParametersPaginateResponseTypeDef(
    _DescribeCacheParametersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeCacheParametersPaginate` `Response`

    Represents the output of a ``DescribeCacheParameters`` operation.

    - **Parameters** *(list) --*

      A list of  Parameter instances.

      - *(dict) --*

        Describes an individual setting that controls some aspect of ElastiCache behavior.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterValue** *(string) --*

          The value of the parameter.

        - **Description** *(string) --*

          A description of the parameter.

        - **Source** *(string) --*

          The source of the parameter.

        - **DataType** *(string) --*

          The valid data type for the parameter.

        - **AllowedValues** *(string) --*

          The valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest cache engine version to which the parameter can apply.

        - **ChangeType** *(string) --*

          Indicates whether a change to the parameter is applied immediately or requires a reboot
          for the change to be applied. You can force a reboot or wait until the next maintenance
          window's reboot. For more information, see `Rebooting a Cluster
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .

    - **CacheNodeTypeSpecificParameters** *(list) --*

      A list of parameters specific to a particular cache node type. Each element in the list
      contains detailed information about one parameter.

      - *(dict) --*

        A parameter that has a different value for each cache node type it is applied to. For
        example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
        ``maxmemory`` value than a ``cache.m1.small`` type.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **Description** *(string) --*

          A description of the parameter.

        - **Source** *(string) --*

          The source of the parameter value.

        - **DataType** *(string) --*

          The valid data type for the parameter.

        - **AllowedValues** *(string) --*

          The valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest cache engine version to which the parameter can apply.

        - **CacheNodeTypeSpecificValues** *(list) --*

          A list of cache node types and their corresponding values for this parameter.

          - *(dict) --*

            A value that applies only to a certain cache node type.

            - **CacheNodeType** *(string) --*

              The cache node type for which this value applies.

            - **Value** *(string) --*

              The value for the cache node type.

        - **ChangeType** *(string) --*

          Indicates whether a change to the parameter is applied immediately or requires a reboot
          for the change to be applied. You can force a reboot or wait until the next maintenance
          window's reboot. For more information, see `Rebooting a Cluster
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__ .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef(
    _DescribeCacheSecurityGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeCacheSecurityGroupsPaginate` `PaginationConfig`

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


_DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef = TypedDict(
    "_DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef",
    {"Status": str, "EC2SecurityGroupName": str, "EC2SecurityGroupOwnerId": str},
    total=False,
)


class DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef(
    _DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef
):
    """
    Type definition for `DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroups` `EC2SecurityGroups`

    Provides ownership and status information for an Amazon EC2 security group.

    - **Status** *(string) --*

      The status of the Amazon EC2 security group.

    - **EC2SecurityGroupName** *(string) --*

      The name of the Amazon EC2 security group.

    - **EC2SecurityGroupOwnerId** *(string) --*

      The AWS account ID of the Amazon EC2 security group owner.
    """


_DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef = TypedDict(
    "_DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List[
            DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsEC2SecurityGroupsTypeDef
        ],
    },
    total=False,
)


class DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef(
    _DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef
):
    """
    Type definition for `DescribeCacheSecurityGroupsPaginateResponse` `CacheSecurityGroups`

    Represents the output of one of the following operations:

    * ``AuthorizeCacheSecurityGroupIngress``

    * ``CreateCacheSecurityGroup``

    * ``RevokeCacheSecurityGroupIngress``

    - **OwnerId** *(string) --*

      The AWS account ID of the cache security group owner.

    - **CacheSecurityGroupName** *(string) --*

      The name of the cache security group.

    - **Description** *(string) --*

      The description of the cache security group.

    - **EC2SecurityGroups** *(list) --*

      A list of Amazon EC2 security groups that are associated with this cache security group.

      - *(dict) --*

        Provides ownership and status information for an Amazon EC2 security group.

        - **Status** *(string) --*

          The status of the Amazon EC2 security group.

        - **EC2SecurityGroupName** *(string) --*

          The name of the Amazon EC2 security group.

        - **EC2SecurityGroupOwnerId** *(string) --*

          The AWS account ID of the Amazon EC2 security group owner.
    """


_DescribeCacheSecurityGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheSecurityGroupsPaginateResponseTypeDef",
    {
        "CacheSecurityGroups": List[
            DescribeCacheSecurityGroupsPaginateResponseCacheSecurityGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheSecurityGroupsPaginateResponseTypeDef(
    _DescribeCacheSecurityGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeCacheSecurityGroupsPaginate` `Response`

    Represents the output of a ``DescribeCacheSecurityGroups`` operation.

    - **CacheSecurityGroups** *(list) --*

      A list of cache security groups. Each element in the list contains detailed information about
      one group.

      - *(dict) --*

        Represents the output of one of the following operations:

        * ``AuthorizeCacheSecurityGroupIngress``

        * ``CreateCacheSecurityGroup``

        * ``RevokeCacheSecurityGroupIngress``

        - **OwnerId** *(string) --*

          The AWS account ID of the cache security group owner.

        - **CacheSecurityGroupName** *(string) --*

          The name of the cache security group.

        - **Description** *(string) --*

          The description of the cache security group.

        - **EC2SecurityGroups** *(list) --*

          A list of Amazon EC2 security groups that are associated with this cache security group.

          - *(dict) --*

            Provides ownership and status information for an Amazon EC2 security group.

            - **Status** *(string) --*

              The status of the Amazon EC2 security group.

            - **EC2SecurityGroupName** *(string) --*

              The name of the Amazon EC2 security group.

            - **EC2SecurityGroupOwnerId** *(string) --*

              The AWS account ID of the Amazon EC2 security group owner.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef(
    _DescribeCacheSubnetGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeCacheSubnetGroupsPaginate` `PaginationConfig`

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


_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnets` `SubnetAvailabilityZone`

    The Availability Zone associated with the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef = TypedDict(
    "_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
    },
    total=False,
)


class DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef(
    _DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef
):
    """
    Type definition for `DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroups` `Subnets`

    Represents the subnet associated with a cluster. This parameter refers to subnets
    defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

    - **SubnetIdentifier** *(string) --*

      The unique identifier for the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      The Availability Zone associated with the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.
    """


_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef = TypedDict(
    "_DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List[
            DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsSubnetsTypeDef
        ],
    },
    total=False,
)


class DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef(
    _DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef
):
    """
    Type definition for `DescribeCacheSubnetGroupsPaginateResponse` `CacheSubnetGroups`

    Represents the output of one of the following operations:

    * ``CreateCacheSubnetGroup``

    * ``ModifyCacheSubnetGroup``

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group.

    - **CacheSubnetGroupDescription** *(string) --*

      The description of the cache subnet group.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

    - **Subnets** *(list) --*

      A list of subnets associated with the cache subnet group.

      - *(dict) --*

        Represents the subnet associated with a cluster. This parameter refers to subnets
        defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

        - **SubnetIdentifier** *(string) --*

          The unique identifier for the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          The Availability Zone associated with the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.
    """


_DescribeCacheSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeCacheSubnetGroupsPaginateResponseTypeDef",
    {
        "CacheSubnetGroups": List[
            DescribeCacheSubnetGroupsPaginateResponseCacheSubnetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeCacheSubnetGroupsPaginateResponseTypeDef(
    _DescribeCacheSubnetGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeCacheSubnetGroupsPaginate` `Response`

    Represents the output of a ``DescribeCacheSubnetGroups`` operation.

    - **CacheSubnetGroups** *(list) --*

      A list of cache subnet groups. Each element in the list contains detailed information about
      one group.

      - *(dict) --*

        Represents the output of one of the following operations:

        * ``CreateCacheSubnetGroup``

        * ``ModifyCacheSubnetGroup``

        - **CacheSubnetGroupName** *(string) --*

          The name of the cache subnet group.

        - **CacheSubnetGroupDescription** *(string) --*

          The description of the cache subnet group.

        - **VpcId** *(string) --*

          The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

        - **Subnets** *(list) --*

          A list of subnets associated with the cache subnet group.

          - *(dict) --*

            Represents the subnet associated with a cluster. This parameter refers to subnets
            defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

            - **SubnetIdentifier** *(string) --*

              The unique identifier for the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              The Availability Zone associated with the subnet.

              - **Name** *(string) --*

                The name of the Availability Zone.

    - **NextToken** *(string) --*

      A token to resume pagination.
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


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef",
    {"CacheNodeType": str, "Value": str},
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
):
    """
    Type definition for `DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParameters` `CacheNodeTypeSpecificValues`

    A value that applies only to a certain cache node type.

    - **CacheNodeType** *(string) --*

      The cache node type for which this value applies.

    - **Value** *(string) --*

      The value for the cache node type.
    """


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List[
            DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersCacheNodeTypeSpecificValuesTypeDef
        ],
        "ChangeType": str,
    },
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef
):
    """
    Type definition for `DescribeEngineDefaultParametersPaginateResponseEngineDefaults` `CacheNodeTypeSpecificParameters`

    A parameter that has a different value for each cache node type it is applied to. For
    example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
    ``maxmemory`` value than a ``cache.m1.small`` type.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **Description** *(string) --*

      A description of the parameter.

    - **Source** *(string) --*

      The source of the parameter value.

    - **DataType** *(string) --*

      The valid data type for the parameter.

    - **AllowedValues** *(string) --*

      The valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being
      changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest cache engine version to which the parameter can apply.

    - **CacheNodeTypeSpecificValues** *(list) --*

      A list of cache node types and their corresponding values for this parameter.

      - *(dict) --*

        A value that applies only to a certain cache node type.

        - **CacheNodeType** *(string) --*

          The cache node type for which this value applies.

        - **Value** *(string) --*

          The value for the cache node type.

    - **ChangeType** *(string) --*

      Indicates whether a change to the parameter is applied immediately or requires a reboot
      for the change to be applied. You can force a reboot or wait until the next maintenance
      window's reboot. For more information, see `Rebooting a Cluster
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
      .
    """


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": str,
    },
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef
):
    """
    Type definition for `DescribeEngineDefaultParametersPaginateResponseEngineDefaults` `Parameters`

    Describes an individual setting that controls some aspect of ElastiCache behavior.

    - **ParameterName** *(string) --*

      The name of the parameter.

    - **ParameterValue** *(string) --*

      The value of the parameter.

    - **Description** *(string) --*

      A description of the parameter.

    - **Source** *(string) --*

      The source of the parameter.

    - **DataType** *(string) --*

      The valid data type for the parameter.

    - **AllowedValues** *(string) --*

      The valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being
      changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest cache engine version to which the parameter can apply.

    - **ChangeType** *(string) --*

      Indicates whether a change to the parameter is applied immediately or requires a reboot
      for the change to be applied. You can force a reboot or wait until the next maintenance
      window's reboot. For more information, see `Rebooting a Cluster
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
      .
    """


_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef = TypedDict(
    "_DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef",
    {
        "CacheParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            DescribeEngineDefaultParametersPaginateResponseEngineDefaultsParametersTypeDef
        ],
        "CacheNodeTypeSpecificParameters": List[
            DescribeEngineDefaultParametersPaginateResponseEngineDefaultsCacheNodeTypeSpecificParametersTypeDef
        ],
    },
    total=False,
)


class DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef(
    _DescribeEngineDefaultParametersPaginateResponseEngineDefaultsTypeDef
):
    """
    Type definition for `DescribeEngineDefaultParametersPaginateResponse` `EngineDefaults`

    Represents the output of a ``DescribeEngineDefaultParameters`` operation.

    - **CacheParameterGroupFamily** *(string) --*

      Specifies the name of the cache parameter group family to which the engine default
      parameters apply.

      Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
      ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

    - **Marker** *(string) --*

      Provides an identifier to allow retrieval of paginated results.

    - **Parameters** *(list) --*

      Contains a list of engine default parameters.

      - *(dict) --*

        Describes an individual setting that controls some aspect of ElastiCache behavior.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **ParameterValue** *(string) --*

          The value of the parameter.

        - **Description** *(string) --*

          A description of the parameter.

        - **Source** *(string) --*

          The source of the parameter.

        - **DataType** *(string) --*

          The valid data type for the parameter.

        - **AllowedValues** *(string) --*

          The valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being
          changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest cache engine version to which the parameter can apply.

        - **ChangeType** *(string) --*

          Indicates whether a change to the parameter is applied immediately or requires a reboot
          for the change to be applied. You can force a reboot or wait until the next maintenance
          window's reboot. For more information, see `Rebooting a Cluster
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
          .

    - **CacheNodeTypeSpecificParameters** *(list) --*

      A list of parameters specific to a particular cache node type. Each element in the list
      contains detailed information about one parameter.

      - *(dict) --*

        A parameter that has a different value for each cache node type it is applied to. For
        example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
        ``maxmemory`` value than a ``cache.m1.small`` type.

        - **ParameterName** *(string) --*

          The name of the parameter.

        - **Description** *(string) --*

          A description of the parameter.

        - **Source** *(string) --*

          The source of the parameter value.

        - **DataType** *(string) --*

          The valid data type for the parameter.

        - **AllowedValues** *(string) --*

          The valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being
          changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest cache engine version to which the parameter can apply.

        - **CacheNodeTypeSpecificValues** *(list) --*

          A list of cache node types and their corresponding values for this parameter.

          - *(dict) --*

            A value that applies only to a certain cache node type.

            - **CacheNodeType** *(string) --*

              The cache node type for which this value applies.

            - **Value** *(string) --*

              The value for the cache node type.

        - **ChangeType** *(string) --*

          Indicates whether a change to the parameter is applied immediately or requires a reboot
          for the change to be applied. You can force a reboot or wait until the next maintenance
          window's reboot. For more information, see `Rebooting a Cluster
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
          .
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

      Represents the output of a ``DescribeEngineDefaultParameters`` operation.

      - **CacheParameterGroupFamily** *(string) --*

        Specifies the name of the cache parameter group family to which the engine default
        parameters apply.

        Valid values are: ``memcached1.4`` | ``memcached1.5`` | ``redis2.6`` | ``redis2.8`` |
        ``redis3.2`` | ``redis4.0`` | ``redis5.0`` |

      - **Marker** *(string) --*

        Provides an identifier to allow retrieval of paginated results.

      - **Parameters** *(list) --*

        Contains a list of engine default parameters.

        - *(dict) --*

          Describes an individual setting that controls some aspect of ElastiCache behavior.

          - **ParameterName** *(string) --*

            The name of the parameter.

          - **ParameterValue** *(string) --*

            The value of the parameter.

          - **Description** *(string) --*

            A description of the parameter.

          - **Source** *(string) --*

            The source of the parameter.

          - **DataType** *(string) --*

            The valid data type for the parameter.

          - **AllowedValues** *(string) --*

            The valid range of values for the parameter.

          - **IsModifiable** *(boolean) --*

            Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
            parameters have security or operational implications that prevent them from being
            changed.

          - **MinimumEngineVersion** *(string) --*

            The earliest cache engine version to which the parameter can apply.

          - **ChangeType** *(string) --*

            Indicates whether a change to the parameter is applied immediately or requires a reboot
            for the change to be applied. You can force a reboot or wait until the next maintenance
            window's reboot. For more information, see `Rebooting a Cluster
            <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
            .

      - **CacheNodeTypeSpecificParameters** *(list) --*

        A list of parameters specific to a particular cache node type. Each element in the list
        contains detailed information about one parameter.

        - *(dict) --*

          A parameter that has a different value for each cache node type it is applied to. For
          example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger
          ``maxmemory`` value than a ``cache.m1.small`` type.

          - **ParameterName** *(string) --*

            The name of the parameter.

          - **Description** *(string) --*

            A description of the parameter.

          - **Source** *(string) --*

            The source of the parameter value.

          - **DataType** *(string) --*

            The valid data type for the parameter.

          - **AllowedValues** *(string) --*

            The valid range of values for the parameter.

          - **IsModifiable** *(boolean) --*

            Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
            parameters have security or operational implications that prevent them from being
            changed.

          - **MinimumEngineVersion** *(string) --*

            The earliest cache engine version to which the parameter can apply.

          - **CacheNodeTypeSpecificValues** *(list) --*

            A list of cache node types and their corresponding values for this parameter.

            - *(dict) --*

              A value that applies only to a certain cache node type.

              - **CacheNodeType** *(string) --*

                The cache node type for which this value applies.

              - **Value** *(string) --*

                The value for the cache node type.

          - **ChangeType** *(string) --*

            Indicates whether a change to the parameter is applied immediately or requires a reboot
            for the change to be applied. You can force a reboot or wait until the next maintenance
            window's reboot. For more information, see `Rebooting a Cluster
            <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Rebooting.html>`__
            .

    - **NextToken** *(string) --*

      A token to resume pagination.
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
    {"SourceIdentifier": str, "SourceType": str, "Message": str, "Date": datetime},
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(
    _DescribeEventsPaginateResponseEventsTypeDef
):
    """
    Type definition for `DescribeEventsPaginateResponse` `Events`

    Represents a single occurrence of something interesting within the system. Some examples of
    events are creating a cluster, adding or removing a cache node, or rebooting a node.

    - **SourceIdentifier** *(string) --*

      The identifier for the source of the event. For example, if the event occurred at the
      cluster level, the identifier would be the name of the cluster.

    - **SourceType** *(string) --*

      Specifies the origin of this event - a cluster, a parameter group, a security group, etc.

    - **Message** *(string) --*

      The text of the event.

    - **Date** *(datetime) --*

      The date and time when the event occurred.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `Response`

    Represents the output of a ``DescribeEvents`` operation.

    - **Events** *(list) --*

      A list of events. Each element in the list contains detailed information about one event.

      - *(dict) --*

        Represents a single occurrence of something interesting within the system. Some examples of
        events are creating a cluster, adding or removing a cache node, or rebooting a node.

        - **SourceIdentifier** *(string) --*

          The identifier for the source of the event. For example, if the event occurred at the
          cluster level, the identifier would be the name of the cluster.

        - **SourceType** *(string) --*

          Specifies the origin of this event - a cluster, a parameter group, a security group, etc.

        - **Message** *(string) --*

          The text of the event.

        - **Date** *(datetime) --*

          The date and time when the event occurred.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeReplicationGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReplicationGroupsPaginatePaginationConfigTypeDef(
    _DescribeReplicationGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginate` `PaginationConfig`

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


_DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginateResponseReplicationGroups` `ConfigurationEndpoint`

    The configuration endpoint for this replication group. Use the configuration endpoint to
    connect to this replication group.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembers` `ReadEndpoint`

    The information required for client programs to connect to a node for read
    operations. The read endpoint is only applicable on Redis (cluster mode disabled)
    clusters.

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersReadEndpointTypeDef,
        "PreferredAvailabilityZone": str,
        "CurrentRole": str,
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroups` `NodeGroupMembers`

    Represents a single node within a node group (shard).

    - **CacheClusterId** *(string) --*

      The ID of the cluster to which the node belongs.

    - **CacheNodeId** *(string) --*

      The ID of the node within its cluster. A node ID is a numeric identifier (0001,
      0002, etc.).

    - **ReadEndpoint** *(dict) --*

      The information required for client programs to connect to a node for read
      operations. The read endpoint is only applicable on Redis (cluster mode disabled)
      clusters.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the node is located.

    - **CurrentRole** *(string) --*

      The role that is currently assigned to the node - ``primary`` or ``replica`` .
      This member is only applicable for Redis (cluster mode disabled) replication
      groups.
    """


_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroups` `PrimaryEndpoint`

    The endpoint of the primary node in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef",
    {"Address": str, "Port": int},
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroups` `ReaderEndpoint`

    The endpoint of the replica nodes in this node group (shard).

    - **Address** *(string) --*

      The DNS hostname of the cache node.

    - **Port** *(integer) --*

      The port number that the cache engine is listening on.
    """


_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsPrimaryEndpointTypeDef,
        "ReaderEndpoint": DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsReaderEndpointTypeDef,
        "Slots": str,
        "NodeGroupMembers": List[
            DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsNodeGroupMembersTypeDef
        ],
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginateResponseReplicationGroups` `NodeGroups`

    Represents a collection of cache nodes in a replication group. One node in the node
    group is the read/write primary node. All the other nodes are read-only Replica nodes.

    - **NodeGroupId** *(string) --*

      The identifier for the node group (shard). A Redis (cluster mode disabled)
      replication group contains only 1 node group; therefore, the node group ID is 0001. A
      Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered
      0001 to 0090. Optionally, the user can provide the id for a node group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` , etc.

    - **PrimaryEndpoint** *(dict) --*

      The endpoint of the primary node in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **ReaderEndpoint** *(dict) --*

      The endpoint of the replica nodes in this node group (shard).

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **Slots** *(string) --*

      The keyspace for this node group (shard).

    - **NodeGroupMembers** *(list) --*

      A list containing information about individual nodes within the node group (shard).

      - *(dict) --*

        Represents a single node within a node group (shard).

        - **CacheClusterId** *(string) --*

          The ID of the cluster to which the node belongs.

        - **CacheNodeId** *(string) --*

          The ID of the node within its cluster. A node ID is a numeric identifier (0001,
          0002, etc.).

        - **ReadEndpoint** *(dict) --*

          The information required for client programs to connect to a node for read
          operations. The read endpoint is only applicable on Redis (cluster mode disabled)
          clusters.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the node is located.

        - **CurrentRole** *(string) --*

          The role that is currently assigned to the node - ``primary`` or ``replica`` .
          This member is only applicable for Redis (cluster mode disabled) replication
          groups.
    """


_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef",
    {"ProgressPercentage": float},
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesResharding` `SlotMigration`

    Represents the progress of an online resharding operation.

    - **ProgressPercentage** *(float) --*

      The percentage of the slot migration that is complete.
    """


_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef",
    {
        "SlotMigration": DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingSlotMigrationTypeDef
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValues` `Resharding`

    The status of an online resharding operation.

    - **SlotMigration** *(dict) --*

      Represents the progress of an online resharding operation.

      - **ProgressPercentage** *(float) --*

        The percentage of the slot migration that is complete.
    """


_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": str,
        "Resharding": DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesReshardingTypeDef,
        "AuthTokenStatus": str,
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginateResponseReplicationGroups` `PendingModifiedValues`

    A group of settings to be applied to the replication group, either immediately or during
    the next maintenance window.

    - **PrimaryClusterId** *(string) --*

      The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
      specified), or during the next maintenance window.

    - **AutomaticFailoverStatus** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication
      group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **Resharding** *(dict) --*

      The status of an online resharding operation.

      - **SlotMigration** *(dict) --*

        Represents the progress of an online resharding operation.

        - **ProgressPercentage** *(float) --*

          The percentage of the slot migration that is complete.

    - **AuthTokenStatus** *(string) --*

      The auth token status
    """


_DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "Status": str,
        "PendingModifiedValues": DescribeReplicationGroupsPaginateResponseReplicationGroupsPendingModifiedValuesTypeDef,
        "MemberClusters": List[str],
        "NodeGroups": List[
            DescribeReplicationGroupsPaginateResponseReplicationGroupsNodeGroupsTypeDef
        ],
        "SnapshottingClusterId": str,
        "AutomaticFailover": str,
        "ConfigurationEndpoint": DescribeReplicationGroupsPaginateResponseReplicationGroupsConfigurationEndpointTypeDef,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef(
    _DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginateResponse` `ReplicationGroups`

    Contains all of the attributes of a specific Redis replication group.

    - **ReplicationGroupId** *(string) --*

      The identifier for the replication group.

    - **Description** *(string) --*

      The user supplied description of the replication group.

    - **Status** *(string) --*

      The current state of this replication group - ``creating`` , ``available`` ,
      ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

    - **PendingModifiedValues** *(dict) --*

      A group of settings to be applied to the replication group, either immediately or during
      the next maintenance window.

      - **PrimaryClusterId** *(string) --*

        The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
        specified), or during the next maintenance window.

      - **AutomaticFailoverStatus** *(string) --*

        Indicates the status of Multi-AZ with automatic failover for this Redis replication
        group.

        Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

        * Redis versions earlier than 2.8.6.

        * Redis (cluster mode disabled): T1 node types.

        * Redis (cluster mode enabled): T1 node types.

      - **Resharding** *(dict) --*

        The status of an online resharding operation.

        - **SlotMigration** *(dict) --*

          Represents the progress of an online resharding operation.

          - **ProgressPercentage** *(float) --*

            The percentage of the slot migration that is complete.

      - **AuthTokenStatus** *(string) --*

        The auth token status

    - **MemberClusters** *(list) --*

      The names of all the cache clusters that are part of this replication group.

      - *(string) --*

    - **NodeGroups** *(list) --*

      A list of node groups in this replication group. For Redis (cluster mode disabled)
      replication groups, this is a single-element list. For Redis (cluster mode enabled)
      replication groups, the list contains an entry for each node group (shard).

      - *(dict) --*

        Represents a collection of cache nodes in a replication group. One node in the node
        group is the read/write primary node. All the other nodes are read-only Replica nodes.

        - **NodeGroupId** *(string) --*

          The identifier for the node group (shard). A Redis (cluster mode disabled)
          replication group contains only 1 node group; therefore, the node group ID is 0001. A
          Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered
          0001 to 0090. Optionally, the user can provide the id for a node group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` , etc.

        - **PrimaryEndpoint** *(dict) --*

          The endpoint of the primary node in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **ReaderEndpoint** *(dict) --*

          The endpoint of the replica nodes in this node group (shard).

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **Slots** *(string) --*

          The keyspace for this node group (shard).

        - **NodeGroupMembers** *(list) --*

          A list containing information about individual nodes within the node group (shard).

          - *(dict) --*

            Represents a single node within a node group (shard).

            - **CacheClusterId** *(string) --*

              The ID of the cluster to which the node belongs.

            - **CacheNodeId** *(string) --*

              The ID of the node within its cluster. A node ID is a numeric identifier (0001,
              0002, etc.).

            - **ReadEndpoint** *(dict) --*

              The information required for client programs to connect to a node for read
              operations. The read endpoint is only applicable on Redis (cluster mode disabled)
              clusters.

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **PreferredAvailabilityZone** *(string) --*

              The name of the Availability Zone in which the node is located.

            - **CurrentRole** *(string) --*

              The role that is currently assigned to the node - ``primary`` or ``replica`` .
              This member is only applicable for Redis (cluster mode disabled) replication
              groups.

    - **SnapshottingClusterId** *(string) --*

      The cluster ID that is used as the daily snapshot source for the replication group.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **ConfigurationEndpoint** *(dict) --*

      The configuration endpoint for this replication group. Use the configuration endpoint to
      connect to this replication group.

      - **Address** *(string) --*

        The DNS hostname of the cache node.

      - **Port** *(integer) --*

        The port number that the cache engine is listening on.

    - **SnapshotRetentionLimit** *(integer) --*

      The number of days for which ElastiCache retains automatic cluster snapshots before
      deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that
      was taken today is retained for 5 days before being deleted.

      .. warning::

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
      your node group (shard).

      Example: ``05:00-09:00``

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate
      time range.

      .. note::

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

    - **ClusterEnabled** *(boolean) --*

      A flag indicating whether or not this replication group is cluster enabled; i.e., whether
      its data can be partitioned across multiple shards (API/CLI: node groups).

      Valid values: ``true`` | ``false``

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for each node in the replication
      group.

    - **AuthTokenEnabled** *(boolean) --*

      A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

      Default: ``false``

    - **AuthTokenLastModifiedDate** *(datetime) --*

      The date the auth token was last modified

    - **TransitEncryptionEnabled** *(boolean) --*

      A flag that enables in-transit encryption when set to ``true`` .

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
      To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **AtRestEncryptionEnabled** *(boolean) --*

      A flag that enables encryption at-rest when set to ``true`` .

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created.
      To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to
      ``true`` when you create a cluster.

       **Required:** Only available when creating a replication group in an Amazon VPC using
       redis version ``3.2.6`` , ``4.x`` or later.

      Default: ``false``

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the disk in the cluster.
    """


_DescribeReplicationGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeReplicationGroupsPaginateResponseTypeDef",
    {
        "ReplicationGroups": List[
            DescribeReplicationGroupsPaginateResponseReplicationGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReplicationGroupsPaginateResponseTypeDef(
    _DescribeReplicationGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeReplicationGroupsPaginate` `Response`

    Represents the output of a ``DescribeReplicationGroups`` operation.

    - **ReplicationGroups** *(list) --*

      A list of replication groups. Each item in the list contains detailed information about one
      replication group.

      - *(dict) --*

        Contains all of the attributes of a specific Redis replication group.

        - **ReplicationGroupId** *(string) --*

          The identifier for the replication group.

        - **Description** *(string) --*

          The user supplied description of the replication group.

        - **Status** *(string) --*

          The current state of this replication group - ``creating`` , ``available`` ,
          ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

        - **PendingModifiedValues** *(dict) --*

          A group of settings to be applied to the replication group, either immediately or during
          the next maintenance window.

          - **PrimaryClusterId** *(string) --*

            The primary cluster ID that is applied immediately (if ``--apply-immediately`` was
            specified), or during the next maintenance window.

          - **AutomaticFailoverStatus** *(string) --*

            Indicates the status of Multi-AZ with automatic failover for this Redis replication
            group.

            Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

            * Redis versions earlier than 2.8.6.

            * Redis (cluster mode disabled): T1 node types.

            * Redis (cluster mode enabled): T1 node types.

          - **Resharding** *(dict) --*

            The status of an online resharding operation.

            - **SlotMigration** *(dict) --*

              Represents the progress of an online resharding operation.

              - **ProgressPercentage** *(float) --*

                The percentage of the slot migration that is complete.

          - **AuthTokenStatus** *(string) --*

            The auth token status

        - **MemberClusters** *(list) --*

          The names of all the cache clusters that are part of this replication group.

          - *(string) --*

        - **NodeGroups** *(list) --*

          A list of node groups in this replication group. For Redis (cluster mode disabled)
          replication groups, this is a single-element list. For Redis (cluster mode enabled)
          replication groups, the list contains an entry for each node group (shard).

          - *(dict) --*

            Represents a collection of cache nodes in a replication group. One node in the node
            group is the read/write primary node. All the other nodes are read-only Replica nodes.

            - **NodeGroupId** *(string) --*

              The identifier for the node group (shard). A Redis (cluster mode disabled)
              replication group contains only 1 node group; therefore, the node group ID is 0001. A
              Redis (cluster mode enabled) replication group contains 1 to 90 node groups numbered
              0001 to 0090. Optionally, the user can provide the id for a node group.

            - **Status** *(string) --*

              The current state of this replication group - ``creating`` , ``available`` , etc.

            - **PrimaryEndpoint** *(dict) --*

              The endpoint of the primary node in this node group (shard).

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **ReaderEndpoint** *(dict) --*

              The endpoint of the replica nodes in this node group (shard).

              - **Address** *(string) --*

                The DNS hostname of the cache node.

              - **Port** *(integer) --*

                The port number that the cache engine is listening on.

            - **Slots** *(string) --*

              The keyspace for this node group (shard).

            - **NodeGroupMembers** *(list) --*

              A list containing information about individual nodes within the node group (shard).

              - *(dict) --*

                Represents a single node within a node group (shard).

                - **CacheClusterId** *(string) --*

                  The ID of the cluster to which the node belongs.

                - **CacheNodeId** *(string) --*

                  The ID of the node within its cluster. A node ID is a numeric identifier (0001,
                  0002, etc.).

                - **ReadEndpoint** *(dict) --*

                  The information required for client programs to connect to a node for read
                  operations. The read endpoint is only applicable on Redis (cluster mode disabled)
                  clusters.

                  - **Address** *(string) --*

                    The DNS hostname of the cache node.

                  - **Port** *(integer) --*

                    The port number that the cache engine is listening on.

                - **PreferredAvailabilityZone** *(string) --*

                  The name of the Availability Zone in which the node is located.

                - **CurrentRole** *(string) --*

                  The role that is currently assigned to the node - ``primary`` or ``replica`` .
                  This member is only applicable for Redis (cluster mode disabled) replication
                  groups.

        - **SnapshottingClusterId** *(string) --*

          The cluster ID that is used as the daily snapshot source for the replication group.

        - **AutomaticFailover** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **ConfigurationEndpoint** *(dict) --*

          The configuration endpoint for this replication group. Use the configuration endpoint to
          connect to this replication group.

          - **Address** *(string) --*

            The DNS hostname of the cache node.

          - **Port** *(integer) --*

            The port number that the cache engine is listening on.

        - **SnapshotRetentionLimit** *(integer) --*

          The number of days for which ElastiCache retains automatic cluster snapshots before
          deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that
          was taken today is retained for 5 days before being deleted.

          .. warning::

            If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

        - **SnapshotWindow** *(string) --*

          The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of
          your node group (shard).

          Example: ``05:00-09:00``

          If you do not specify this parameter, ElastiCache automatically chooses an appropriate
          time range.

          .. note::

            This parameter is only valid if the ``Engine`` parameter is ``redis`` .

        - **ClusterEnabled** *(boolean) --*

          A flag indicating whether or not this replication group is cluster enabled; i.e., whether
          its data can be partitioned across multiple shards (API/CLI: node groups).

          Valid values: ``true`` | ``false``

        - **CacheNodeType** *(string) --*

          The name of the compute and memory capacity node type for each node in the replication
          group.

        - **AuthTokenEnabled** *(boolean) --*

          A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

          Default: ``false``

        - **AuthTokenLastModifiedDate** *(datetime) --*

          The date the auth token was last modified

        - **TransitEncryptionEnabled** *(boolean) --*

          A flag that enables in-transit encryption when set to ``true`` .

          You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created.
          To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to
          ``true`` when you create a cluster.

           **Required:** Only available when creating a replication group in an Amazon VPC using
           redis version ``3.2.6`` , ``4.x`` or later.

          Default: ``false``

        - **AtRestEncryptionEnabled** *(boolean) --*

          A flag that enables encryption at-rest when set to ``true`` .

          You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created.
          To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to
          ``true`` when you create a cluster.

           **Required:** Only available when creating a replication group in an Amazon VPC using
           redis version ``3.2.6`` , ``4.x`` or later.

          Default: ``false``

        - **KmsKeyId** *(string) --*

          The ID of the KMS key used to encrypt the disk in the cluster.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef(
    _DescribeReservedCacheNodesOfferingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeReservedCacheNodesOfferingsPaginate` `PaginationConfig`

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


_DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef(
    _DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef
):
    """
    Type definition for `DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferings` `RecurringCharges`

    Contains the specific price and frequency of a recurring charges for a reserved cache
    node, or for a reserved cache node offering.

    - **RecurringChargeAmount** *(float) --*

      The monetary amount of the recurring charge.

    - **RecurringChargeFrequency** *(string) --*

      The frequency of the recurring charge.
    """


_DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef = TypedDict(
    "_DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "ProductDescription": str,
        "OfferingType": str,
        "RecurringCharges": List[
            DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)


class DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef(
    _DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef
):
    """
    Type definition for `DescribeReservedCacheNodesOfferingsPaginateResponse` `ReservedCacheNodesOfferings`

    Describes all of the attributes of a reserved cache node offering.

    - **ReservedCacheNodesOfferingId** *(string) --*

      A unique identifier for the reserved cache node offering.

    - **CacheNodeType** *(string) --*

      The cache node type for the reserved cache node.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared
      to their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
        types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
        **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
        ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Duration** *(integer) --*

      The duration of the offering. in seconds.

    - **FixedPrice** *(float) --*

      The fixed price charged for this offering.

    - **UsagePrice** *(float) --*

      The hourly price charged for this offering.

    - **ProductDescription** *(string) --*

      The cache engine used by the offering.

    - **OfferingType** *(string) --*

      The offering type.

    - **RecurringCharges** *(list) --*

      The recurring price charged to run this reserved cache node.

      - *(dict) --*

        Contains the specific price and frequency of a recurring charges for a reserved cache
        node, or for a reserved cache node offering.

        - **RecurringChargeAmount** *(float) --*

          The monetary amount of the recurring charge.

        - **RecurringChargeFrequency** *(string) --*

          The frequency of the recurring charge.
    """


_DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef",
    {
        "ReservedCacheNodesOfferings": List[
            DescribeReservedCacheNodesOfferingsPaginateResponseReservedCacheNodesOfferingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef(
    _DescribeReservedCacheNodesOfferingsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeReservedCacheNodesOfferingsPaginate` `Response`

    Represents the output of a ``DescribeReservedCacheNodesOfferings`` operation.

    - **ReservedCacheNodesOfferings** *(list) --*

      A list of reserved cache node offerings. Each element in the list contains detailed
      information about one offering.

      - *(dict) --*

        Describes all of the attributes of a reserved cache node offering.

        - **ReservedCacheNodesOfferingId** *(string) --*

          A unique identifier for the reserved cache node offering.

        - **CacheNodeType** *(string) --*

          The cache node type for the reserved cache node.

          The following node types are supported by ElastiCache. Generally speaking, the current
          generation types provide more memory and computational power at lower cost when compared
          to their equivalent previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
            ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
            ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
            types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
            **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
            ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
            ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
            ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
            ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
            ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
          Redis version 2.8.22 and later.

        - **Duration** *(integer) --*

          The duration of the offering. in seconds.

        - **FixedPrice** *(float) --*

          The fixed price charged for this offering.

        - **UsagePrice** *(float) --*

          The hourly price charged for this offering.

        - **ProductDescription** *(string) --*

          The cache engine used by the offering.

        - **OfferingType** *(string) --*

          The offering type.

        - **RecurringCharges** *(list) --*

          The recurring price charged to run this reserved cache node.

          - *(dict) --*

            Contains the specific price and frequency of a recurring charges for a reserved cache
            node, or for a reserved cache node offering.

            - **RecurringChargeAmount** *(float) --*

              The monetary amount of the recurring charge.

            - **RecurringChargeFrequency** *(string) --*

              The frequency of the recurring charge.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeReservedCacheNodesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedCacheNodesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedCacheNodesPaginatePaginationConfigTypeDef(
    _DescribeReservedCacheNodesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeReservedCacheNodesPaginate` `PaginationConfig`

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


_DescribeServiceUpdatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeServiceUpdatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeServiceUpdatesPaginatePaginationConfigTypeDef(
    _DescribeServiceUpdatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeServiceUpdatesPaginate` `PaginationConfig`

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


_DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef = TypedDict(
    "_DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef",
    {
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateEndDate": datetime,
        "ServiceUpdateSeverity": str,
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateStatus": str,
        "ServiceUpdateDescription": str,
        "ServiceUpdateType": str,
        "Engine": str,
        "EngineVersion": str,
        "AutoUpdateAfterRecommendedApplyByDate": bool,
        "EstimatedUpdateTime": str,
    },
    total=False,
)


class DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef(
    _DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef
):
    """
    Type definition for `DescribeServiceUpdatesPaginateResponse` `ServiceUpdates`

    An update that you can apply to your Redis clusters.

    - **ServiceUpdateName** *(string) --*

      The unique ID of the service update

    - **ServiceUpdateReleaseDate** *(datetime) --*

      The date when the service update is initially available

    - **ServiceUpdateEndDate** *(datetime) --*

      The date after which the service update is no longer available

    - **ServiceUpdateSeverity** *(string) --*

      The severity of the service update

    - **ServiceUpdateRecommendedApplyByDate** *(datetime) --*

      The recommendend date to apply the service update in order to ensure compliance. For
      information on compliance, see `Self-Service Security Updates for Compliance
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-compliance.html#elasticache-compliance-self-service>`__
      .

    - **ServiceUpdateStatus** *(string) --*

      The status of the service update

    - **ServiceUpdateDescription** *(string) --*

      Provides details of the service update

    - **ServiceUpdateType** *(string) --*

      Reflects the nature of the service update

    - **Engine** *(string) --*

      The Elasticache engine to which the update applies. Either Redis or Memcached

    - **EngineVersion** *(string) --*

      The Elasticache engine version to which the update applies. Either Redis or Memcached
      engine version

    - **AutoUpdateAfterRecommendedApplyByDate** *(boolean) --*

      Indicates whether the service update will be automatically applied once the recommended
      apply-by date has expired.

    - **EstimatedUpdateTime** *(string) --*

      The estimated length of time the service update will take
    """


_DescribeServiceUpdatesPaginateResponseTypeDef = TypedDict(
    "_DescribeServiceUpdatesPaginateResponseTypeDef",
    {
        "ServiceUpdates": List[
            DescribeServiceUpdatesPaginateResponseServiceUpdatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeServiceUpdatesPaginateResponseTypeDef(
    _DescribeServiceUpdatesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeServiceUpdatesPaginate` `Response`

    - **ServiceUpdates** *(list) --*

      A list of service updates

      - *(dict) --*

        An update that you can apply to your Redis clusters.

        - **ServiceUpdateName** *(string) --*

          The unique ID of the service update

        - **ServiceUpdateReleaseDate** *(datetime) --*

          The date when the service update is initially available

        - **ServiceUpdateEndDate** *(datetime) --*

          The date after which the service update is no longer available

        - **ServiceUpdateSeverity** *(string) --*

          The severity of the service update

        - **ServiceUpdateRecommendedApplyByDate** *(datetime) --*

          The recommendend date to apply the service update in order to ensure compliance. For
          information on compliance, see `Self-Service Security Updates for Compliance
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-compliance.html#elasticache-compliance-self-service>`__
          .

        - **ServiceUpdateStatus** *(string) --*

          The status of the service update

        - **ServiceUpdateDescription** *(string) --*

          Provides details of the service update

        - **ServiceUpdateType** *(string) --*

          Reflects the nature of the service update

        - **Engine** *(string) --*

          The Elasticache engine to which the update applies. Either Redis or Memcached

        - **EngineVersion** *(string) --*

          The Elasticache engine version to which the update applies. Either Redis or Memcached
          engine version

        - **AutoUpdateAfterRecommendedApplyByDate** *(boolean) --*

          Indicates whether the service update will be automatically applied once the recommended
          apply-by date has expired.

        - **EstimatedUpdateTime** *(string) --*

          The estimated length of time the service update will take

    - **NextToken** *(string) --*

      A token to resume pagination.
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


_DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
    },
    total=False,
)


class DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef(
    _DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef
):
    """
    Type definition for `DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshots` `NodeGroupConfiguration`

    The configuration for the source node group (shard).

    - **NodeGroupId** *(string) --*

      Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
      node group these configuration values apply to.

    - **Slots** *(string) --*

      A string that specifies the keyspace for a particular node group. Keyspaces range
      from 0 to 16,383. The string is in the format ``startkey-endkey`` .

      Example: ``"0-3999"``

    - **ReplicaCount** *(integer) --*

      The number of read replica nodes in this node group (shard).

    - **PrimaryAvailabilityZone** *(string) --*

      The Availability Zone where the primary node of this node group (shard) is launched.

    - **ReplicaAvailabilityZones** *(list) --*

      A list of Availability Zones to be used for the read replicas. The number of
      Availability Zones in this list must match the value of ``ReplicaCount`` or
      ``ReplicasPerNodeGroup`` if not specified.

      - *(string) --*
    """


_DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsNodeGroupConfigurationTypeDef,
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)


class DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef(
    _DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef
):
    """
    Type definition for `DescribeSnapshotsPaginateResponseSnapshots` `NodeSnapshots`

    Represents an individual cache node in a snapshot of a cluster.

    - **CacheClusterId** *(string) --*

      A unique identifier for the source cluster.

    - **NodeGroupId** *(string) --*

      A unique identifier for the source node group (shard).

    - **CacheNodeId** *(string) --*

      The cache node identifier for the node in the source cluster.

    - **NodeGroupConfiguration** *(dict) --*

      The configuration for the source node group (shard).

      - **NodeGroupId** *(string) --*

        Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
        node group these configuration values apply to.

      - **Slots** *(string) --*

        A string that specifies the keyspace for a particular node group. Keyspaces range
        from 0 to 16,383. The string is in the format ``startkey-endkey`` .

        Example: ``"0-3999"``

      - **ReplicaCount** *(integer) --*

        The number of read replica nodes in this node group (shard).

      - **PrimaryAvailabilityZone** *(string) --*

        The Availability Zone where the primary node of this node group (shard) is launched.

      - **ReplicaAvailabilityZones** *(list) --*

        A list of Availability Zones to be used for the read replicas. The number of
        Availability Zones in this list must match the value of ``ReplicaCount`` or
        ``ReplicasPerNodeGroup`` if not specified.

        - *(string) --*

    - **CacheSize** *(string) --*

      The size of the cache on the source cache node.

    - **CacheNodeCreateTime** *(datetime) --*

      The date and time when the cache node was created in the source cluster.

    - **SnapshotCreateTime** *(datetime) --*

      The date and time when the source node's metadata and cache data set was obtained for
      the snapshot.
    """


_DescribeSnapshotsPaginateResponseSnapshotsTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseSnapshotsTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": str,
        "NodeSnapshots": List[
            DescribeSnapshotsPaginateResponseSnapshotsNodeSnapshotsTypeDef
        ],
        "KmsKeyId": str,
    },
    total=False,
)


class DescribeSnapshotsPaginateResponseSnapshotsTypeDef(
    _DescribeSnapshotsPaginateResponseSnapshotsTypeDef
):
    """
    Type definition for `DescribeSnapshotsPaginateResponse` `Snapshots`

    Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

    - **SnapshotName** *(string) --*

      The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
      manual snapshot, this is the user-provided name.

    - **ReplicationGroupId** *(string) --*

      The unique identifier of the source replication group.

    - **ReplicationGroupDescription** *(string) --*

      A description of the source replication group.

    - **CacheClusterId** *(string) --*

      The user-supplied identifier of the source cluster.

    - **SnapshotStatus** *(string) --*

      The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
      ``copying`` | ``deleting`` .

    - **SnapshotSource** *(string) --*

      Indicates whether the snapshot is from an automatic backup (``automated`` ) or was
      created manually (``manual`` ).

    - **CacheNodeType** *(string) --*

      The name of the compute and memory capacity node type for the source cluster.

      The following node types are supported by ElastiCache. Generally speaking, the current
      generation types provide more memory and computational power at lower cost when compared
      to their equivalent previous generation counterparts.

      * General purpose:

        * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
        ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
        ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
        ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
        types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
        **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
        ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
        ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

      * Compute optimized:

        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

      * Memory optimized:

        * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
        ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
        ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
        ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
        ``cache.r4.16xlarge``

        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
        ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
        ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

       **Additional node type info**

      * All current generation instance types are created in Amazon VPC by default.

      * Redis append-only files (AOF) are not supported for T1 or T2 instances.

      * Redis Multi-AZ with automatic failover is not supported on T1 instances.

      * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
      Redis version 2.8.22 and later.

    - **Engine** *(string) --*

      The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

    - **EngineVersion** *(string) --*

      The version of the cache engine version that is used by the source cluster.

    - **NumCacheNodes** *(integer) --*

      The number of cache nodes in the source cluster.

      For clusters running Redis, this value must be 1. For clusters running Memcached, this
      value must be between 1 and 20.

    - **PreferredAvailabilityZone** *(string) --*

      The name of the Availability Zone in which the source cluster is located.

    - **CacheClusterCreateTime** *(datetime) --*

      The date and time when the source cluster was created.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which maintenance on the cluster is performed. It
      is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The
      minimum maintenance window is a 60 minute period.

      Valid values for ``ddd`` are:

      * ``sun``

      * ``mon``

      * ``tue``

      * ``wed``

      * ``thu``

      * ``fri``

      * ``sat``

      Example: ``sun:23:00-mon:01:30``

    - **TopicArn** *(string) --*

      The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
      notifications.

    - **Port** *(integer) --*

      The port number used by each cache nodes in the source cluster.

    - **CacheParameterGroupName** *(string) --*

      The cache parameter group that is associated with the source cluster.

    - **CacheSubnetGroupName** *(string) --*

      The name of the cache subnet group associated with the source cluster.

    - **VpcId** *(string) --*

      The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
      source cluster.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      This parameter is currently disabled.

    - **SnapshotRetentionLimit** *(integer) --*

      For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
      before deleting it.

      For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
      cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots
      do not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

       **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
       turned off.

    - **SnapshotWindow** *(string) --*

      The daily time range during which ElastiCache takes daily snapshots of the source cluster.

    - **NumNodeGroups** *(integer) --*

      The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
      number of node groups (shards) in the snapshot and in the restored replication group must
      be the same.

    - **AutomaticFailover** *(string) --*

      Indicates the status of Multi-AZ with automatic failover for the source Redis replication
      group.

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

      * Redis versions earlier than 2.8.6.

      * Redis (cluster mode disabled): T1 node types.

      * Redis (cluster mode enabled): T1 node types.

    - **NodeSnapshots** *(list) --*

      A list of the cache nodes in the source cluster.

      - *(dict) --*

        Represents an individual cache node in a snapshot of a cluster.

        - **CacheClusterId** *(string) --*

          A unique identifier for the source cluster.

        - **NodeGroupId** *(string) --*

          A unique identifier for the source node group (shard).

        - **CacheNodeId** *(string) --*

          The cache node identifier for the node in the source cluster.

        - **NodeGroupConfiguration** *(dict) --*

          The configuration for the source node group (shard).

          - **NodeGroupId** *(string) --*

            Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
            node group these configuration values apply to.

          - **Slots** *(string) --*

            A string that specifies the keyspace for a particular node group. Keyspaces range
            from 0 to 16,383. The string is in the format ``startkey-endkey`` .

            Example: ``"0-3999"``

          - **ReplicaCount** *(integer) --*

            The number of read replica nodes in this node group (shard).

          - **PrimaryAvailabilityZone** *(string) --*

            The Availability Zone where the primary node of this node group (shard) is launched.

          - **ReplicaAvailabilityZones** *(list) --*

            A list of Availability Zones to be used for the read replicas. The number of
            Availability Zones in this list must match the value of ``ReplicaCount`` or
            ``ReplicasPerNodeGroup`` if not specified.

            - *(string) --*

        - **CacheSize** *(string) --*

          The size of the cache on the source cache node.

        - **CacheNodeCreateTime** *(datetime) --*

          The date and time when the cache node was created in the source cluster.

        - **SnapshotCreateTime** *(datetime) --*

          The date and time when the source node's metadata and cache data set was obtained for
          the snapshot.

    - **KmsKeyId** *(string) --*

      The ID of the KMS key used to encrypt the snapshot.
    """


_DescribeSnapshotsPaginateResponseTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseTypeDef",
    {
        "Snapshots": List[DescribeSnapshotsPaginateResponseSnapshotsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeSnapshotsPaginateResponseTypeDef(
    _DescribeSnapshotsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeSnapshotsPaginate` `Response`

    Represents the output of a ``DescribeSnapshots`` operation.

    - **Snapshots** *(list) --*

      A list of snapshots. Each item in the list contains detailed information about one snapshot.

      - *(dict) --*

        Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

        - **SnapshotName** *(string) --*

          The name of a snapshot. For an automatic snapshot, the name is system-generated. For a
          manual snapshot, this is the user-provided name.

        - **ReplicationGroupId** *(string) --*

          The unique identifier of the source replication group.

        - **ReplicationGroupDescription** *(string) --*

          A description of the source replication group.

        - **CacheClusterId** *(string) --*

          The user-supplied identifier of the source cluster.

        - **SnapshotStatus** *(string) --*

          The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` |
          ``copying`` | ``deleting`` .

        - **SnapshotSource** *(string) --*

          Indicates whether the snapshot is from an automatic backup (``automated`` ) or was
          created manually (``manual`` ).

        - **CacheNodeType** *(string) --*

          The name of the compute and memory capacity node type for the source cluster.

          The following node types are supported by ElastiCache. Generally speaking, the current
          generation types provide more memory and computational power at lower cost when compared
          to their equivalent previous generation counterparts.

          * General purpose:

            * Current generation:   **M5 node types:**  ``cache.m5.large`` , ``cache.m5.xlarge`` ,
            ``cache.m5.2xlarge`` , ``cache.m5.4xlarge`` , ``cache.m5.12xlarge`` ,
            ``cache.m5.24xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` ,
            ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``    **T2 node
            types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``

            * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``
            **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` ,
            ``cache.m1.xlarge``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` ,
            ``cache.m3.xlarge`` , ``cache.m3.2xlarge``

          * Compute optimized:

            * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``

          * Memory optimized:

            * Current generation:   **R5 node types:**  ``cache.r5.large`` , ``cache.r5.xlarge`` ,
            ``cache.r5.2xlarge`` , ``cache.r5.4xlarge`` , ``cache.r5.12xlarge`` ,
            ``cache.r5.24xlarge``    **R4 node types:**  ``cache.r4.large`` , ``cache.r4.xlarge`` ,
            ``cache.r4.2xlarge`` , ``cache.r4.4xlarge`` , ``cache.r4.8xlarge`` ,
            ``cache.r4.16xlarge``

            * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` ,
            ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``    **R3 node types:**  ``cache.r3.large`` ,
            ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``

           **Additional node type info**

          * All current generation instance types are created in Amazon VPC by default.

          * Redis append-only files (AOF) are not supported for T1 or T2 instances.

          * Redis Multi-AZ with automatic failover is not supported on T1 instances.

          * Redis configuration variables ``appendonly`` and ``appendfsync`` are not supported on
          Redis version 2.8.22 and later.

        - **Engine** *(string) --*

          The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

        - **EngineVersion** *(string) --*

          The version of the cache engine version that is used by the source cluster.

        - **NumCacheNodes** *(integer) --*

          The number of cache nodes in the source cluster.

          For clusters running Redis, this value must be 1. For clusters running Memcached, this
          value must be between 1 and 20.

        - **PreferredAvailabilityZone** *(string) --*

          The name of the Availability Zone in which the source cluster is located.

        - **CacheClusterCreateTime** *(datetime) --*

          The date and time when the source cluster was created.

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which maintenance on the cluster is performed. It
          is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The
          minimum maintenance window is a 60 minute period.

          Valid values for ``ddd`` are:

          * ``sun``

          * ``mon``

          * ``tue``

          * ``wed``

          * ``thu``

          * ``fri``

          * ``sat``

          Example: ``sun:23:00-mon:01:30``

        - **TopicArn** *(string) --*

          The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing
          notifications.

        - **Port** *(integer) --*

          The port number used by each cache nodes in the source cluster.

        - **CacheParameterGroupName** *(string) --*

          The cache parameter group that is associated with the source cluster.

        - **CacheSubnetGroupName** *(string) --*

          The name of the cache subnet group associated with the source cluster.

        - **VpcId** *(string) --*

          The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the
          source cluster.

        - **AutoMinorVersionUpgrade** *(boolean) --*

          This parameter is currently disabled.

        - **SnapshotRetentionLimit** *(integer) --*

          For an automatic snapshot, the number of days for which ElastiCache retains the snapshot
          before deleting it.

          For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source
          cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots
          do not expire, and can only be deleted using the ``DeleteSnapshot`` operation.

           **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are
           turned off.

        - **SnapshotWindow** *(string) --*

          The daily time range during which ElastiCache takes daily snapshots of the source cluster.

        - **NumNodeGroups** *(integer) --*

          The number of node groups (shards) in this snapshot. When restoring from a snapshot, the
          number of node groups (shards) in the snapshot and in the restored replication group must
          be the same.

        - **AutomaticFailover** *(string) --*

          Indicates the status of Multi-AZ with automatic failover for the source Redis replication
          group.

          Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

          * Redis versions earlier than 2.8.6.

          * Redis (cluster mode disabled): T1 node types.

          * Redis (cluster mode enabled): T1 node types.

        - **NodeSnapshots** *(list) --*

          A list of the cache nodes in the source cluster.

          - *(dict) --*

            Represents an individual cache node in a snapshot of a cluster.

            - **CacheClusterId** *(string) --*

              A unique identifier for the source cluster.

            - **NodeGroupId** *(string) --*

              A unique identifier for the source node group (shard).

            - **CacheNodeId** *(string) --*

              The cache node identifier for the node in the source cluster.

            - **NodeGroupConfiguration** *(dict) --*

              The configuration for the source node group (shard).

              - **NodeGroupId** *(string) --*

                Either the ElastiCache for Redis supplied 4-digit id or a user supplied id for the
                node group these configuration values apply to.

              - **Slots** *(string) --*

                A string that specifies the keyspace for a particular node group. Keyspaces range
                from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                Example: ``"0-3999"``

              - **ReplicaCount** *(integer) --*

                The number of read replica nodes in this node group (shard).

              - **PrimaryAvailabilityZone** *(string) --*

                The Availability Zone where the primary node of this node group (shard) is launched.

              - **ReplicaAvailabilityZones** *(list) --*

                A list of Availability Zones to be used for the read replicas. The number of
                Availability Zones in this list must match the value of ``ReplicaCount`` or
                ``ReplicasPerNodeGroup`` if not specified.

                - *(string) --*

            - **CacheSize** *(string) --*

              The size of the cache on the source cache node.

            - **CacheNodeCreateTime** *(datetime) --*

              The date and time when the cache node was created in the source cluster.

            - **SnapshotCreateTime** *(datetime) --*

              The date and time when the source node's metadata and cache data set was obtained for
              the snapshot.

        - **KmsKeyId** *(string) --*

          The ID of the KMS key used to encrypt the snapshot.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeUpdateActionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeUpdateActionsPaginatePaginationConfigTypeDef(
    _DescribeUpdateActionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeUpdateActionsPaginate` `PaginationConfig`

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


_DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef",
    {
        "CacheNodeId": str,
        "NodeUpdateStatus": str,
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": str,
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)


class DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef(
    _DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef
):
    """
    Type definition for `DescribeUpdateActionsPaginateResponseUpdateActions` `CacheNodeUpdateStatus`

    The status of the service update on the cache node

    - **CacheNodeId** *(string) --*

      The node ID of the cache cluster

    - **NodeUpdateStatus** *(string) --*

      The update status of the node

    - **NodeDeletionDate** *(datetime) --*

      The deletion date of the node

    - **NodeUpdateStartDate** *(datetime) --*

      The start date of the update for a node

    - **NodeUpdateEndDate** *(datetime) --*

      The end date of the update for a node

    - **NodeUpdateInitiatedBy** *(string) --*

      Reflects whether the update was initiated by the customer or automatically applied

    - **NodeUpdateInitiatedDate** *(datetime) --*

      The date when the update is triggered

    - **NodeUpdateStatusModifiedDate** *(datetime) --*

      The date when the NodeUpdateStatus was last modified>
    """


_DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "NodeUpdateStatus": str,
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": str,
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)


class DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef(
    _DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
):
    """
    Type definition for `DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatus` `NodeGroupMemberUpdateStatus`

    The status of the service update on the node group member

    - **CacheClusterId** *(string) --*

      The cache cluster ID

    - **CacheNodeId** *(string) --*

      The node ID of the cache cluster

    - **NodeUpdateStatus** *(string) --*

      The update status of the node

    - **NodeDeletionDate** *(datetime) --*

      The deletion date of the node

    - **NodeUpdateStartDate** *(datetime) --*

      The start date of the update for a node

    - **NodeUpdateEndDate** *(datetime) --*

      The end date of the update for a node

    - **NodeUpdateInitiatedBy** *(string) --*

      Reflects whether the update was initiated by the customer or automatically applied

    - **NodeUpdateInitiatedDate** *(datetime) --*

      The date when the update is triggered

    - **NodeUpdateStatusModifiedDate** *(datetime) --*

      The date when the NodeUpdateStatus was last modified
    """


_DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": str,
        "NodeGroupMemberUpdateStatus": List[
            DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusNodeGroupMemberUpdateStatusTypeDef
        ],
    },
    total=False,
)


class DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef(
    _DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef
):
    """
    Type definition for `DescribeUpdateActionsPaginateResponseUpdateActions` `NodeGroupUpdateStatus`

    The status of the service update on the node group

    - **NodeGroupId** *(string) --*

      The ID of the node group

    - **NodeGroupMemberUpdateStatus** *(list) --*

      The status of the service update on the node group member

      - *(dict) --*

        The status of the service update on the node group member

        - **CacheClusterId** *(string) --*

          The cache cluster ID

        - **CacheNodeId** *(string) --*

          The node ID of the cache cluster

        - **NodeUpdateStatus** *(string) --*

          The update status of the node

        - **NodeDeletionDate** *(datetime) --*

          The deletion date of the node

        - **NodeUpdateStartDate** *(datetime) --*

          The start date of the update for a node

        - **NodeUpdateEndDate** *(datetime) --*

          The end date of the update for a node

        - **NodeUpdateInitiatedBy** *(string) --*

          Reflects whether the update was initiated by the customer or automatically applied

        - **NodeUpdateInitiatedDate** *(datetime) --*

          The date when the update is triggered

        - **NodeUpdateStatusModifiedDate** *(datetime) --*

          The date when the NodeUpdateStatus was last modified
    """


_DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateSeverity": str,
        "ServiceUpdateStatus": str,
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateType": str,
        "UpdateActionAvailableDate": datetime,
        "UpdateActionStatus": str,
        "NodesUpdated": str,
        "UpdateActionStatusModifiedDate": datetime,
        "SlaMet": str,
        "NodeGroupUpdateStatus": List[
            DescribeUpdateActionsPaginateResponseUpdateActionsNodeGroupUpdateStatusTypeDef
        ],
        "CacheNodeUpdateStatus": List[
            DescribeUpdateActionsPaginateResponseUpdateActionsCacheNodeUpdateStatusTypeDef
        ],
        "EstimatedUpdateTime": str,
        "Engine": str,
    },
    total=False,
)


class DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef(
    _DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef
):
    """
    Type definition for `DescribeUpdateActionsPaginateResponse` `UpdateActions`

    The status of the service update for a specific replication group

    - **ReplicationGroupId** *(string) --*

      The ID of the replication group

    - **CacheClusterId** *(string) --*

      The ID of the cache cluster

    - **ServiceUpdateName** *(string) --*

      The unique ID of the service update

    - **ServiceUpdateReleaseDate** *(datetime) --*

      The date the update is first available

    - **ServiceUpdateSeverity** *(string) --*

      The severity of the service update

    - **ServiceUpdateStatus** *(string) --*

      The status of the service update

    - **ServiceUpdateRecommendedApplyByDate** *(datetime) --*

      The recommended date to apply the service update to ensure compliance. For information on
      compliance, see `Self-Service Security Updates for Compliance
      <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-compliance.html#elasticache-compliance-self-service>`__
      .

    - **ServiceUpdateType** *(string) --*

      Reflects the nature of the service update

    - **UpdateActionAvailableDate** *(datetime) --*

      The date that the service update is available to a replication group

    - **UpdateActionStatus** *(string) --*

      The status of the update action

    - **NodesUpdated** *(string) --*

      The progress of the service update on the replication group

    - **UpdateActionStatusModifiedDate** *(datetime) --*

      The date when the UpdateActionStatus was last modified

    - **SlaMet** *(string) --*

      If yes, all nodes in the replication group have been updated by the recommended apply-by
      date. If no, at least one node in the replication group have not been updated by the
      recommended apply-by date. If N/A, the replication group was created after the
      recommended apply-by date.

    - **NodeGroupUpdateStatus** *(list) --*

      The status of the service update on the node group

      - *(dict) --*

        The status of the service update on the node group

        - **NodeGroupId** *(string) --*

          The ID of the node group

        - **NodeGroupMemberUpdateStatus** *(list) --*

          The status of the service update on the node group member

          - *(dict) --*

            The status of the service update on the node group member

            - **CacheClusterId** *(string) --*

              The cache cluster ID

            - **CacheNodeId** *(string) --*

              The node ID of the cache cluster

            - **NodeUpdateStatus** *(string) --*

              The update status of the node

            - **NodeDeletionDate** *(datetime) --*

              The deletion date of the node

            - **NodeUpdateStartDate** *(datetime) --*

              The start date of the update for a node

            - **NodeUpdateEndDate** *(datetime) --*

              The end date of the update for a node

            - **NodeUpdateInitiatedBy** *(string) --*

              Reflects whether the update was initiated by the customer or automatically applied

            - **NodeUpdateInitiatedDate** *(datetime) --*

              The date when the update is triggered

            - **NodeUpdateStatusModifiedDate** *(datetime) --*

              The date when the NodeUpdateStatus was last modified

    - **CacheNodeUpdateStatus** *(list) --*

      The status of the service update on the cache node

      - *(dict) --*

        The status of the service update on the cache node

        - **CacheNodeId** *(string) --*

          The node ID of the cache cluster

        - **NodeUpdateStatus** *(string) --*

          The update status of the node

        - **NodeDeletionDate** *(datetime) --*

          The deletion date of the node

        - **NodeUpdateStartDate** *(datetime) --*

          The start date of the update for a node

        - **NodeUpdateEndDate** *(datetime) --*

          The end date of the update for a node

        - **NodeUpdateInitiatedBy** *(string) --*

          Reflects whether the update was initiated by the customer or automatically applied

        - **NodeUpdateInitiatedDate** *(datetime) --*

          The date when the update is triggered

        - **NodeUpdateStatusModifiedDate** *(datetime) --*

          The date when the NodeUpdateStatus was last modified>

    - **EstimatedUpdateTime** *(string) --*

      The estimated length of time for the update to complete

    - **Engine** *(string) --*

      The Elasticache engine to which the update applies. Either Redis or Memcached
    """


_DescribeUpdateActionsPaginateResponseTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateResponseTypeDef",
    {
        "UpdateActions": List[
            DescribeUpdateActionsPaginateResponseUpdateActionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeUpdateActionsPaginateResponseTypeDef(
    _DescribeUpdateActionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeUpdateActionsPaginate` `Response`

    - **UpdateActions** *(list) --*

      Returns a list of update actions

      - *(dict) --*

        The status of the service update for a specific replication group

        - **ReplicationGroupId** *(string) --*

          The ID of the replication group

        - **CacheClusterId** *(string) --*

          The ID of the cache cluster

        - **ServiceUpdateName** *(string) --*

          The unique ID of the service update

        - **ServiceUpdateReleaseDate** *(datetime) --*

          The date the update is first available

        - **ServiceUpdateSeverity** *(string) --*

          The severity of the service update

        - **ServiceUpdateStatus** *(string) --*

          The status of the service update

        - **ServiceUpdateRecommendedApplyByDate** *(datetime) --*

          The recommended date to apply the service update to ensure compliance. For information on
          compliance, see `Self-Service Security Updates for Compliance
          <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/elasticache-compliance.html#elasticache-compliance-self-service>`__
          .

        - **ServiceUpdateType** *(string) --*

          Reflects the nature of the service update

        - **UpdateActionAvailableDate** *(datetime) --*

          The date that the service update is available to a replication group

        - **UpdateActionStatus** *(string) --*

          The status of the update action

        - **NodesUpdated** *(string) --*

          The progress of the service update on the replication group

        - **UpdateActionStatusModifiedDate** *(datetime) --*

          The date when the UpdateActionStatus was last modified

        - **SlaMet** *(string) --*

          If yes, all nodes in the replication group have been updated by the recommended apply-by
          date. If no, at least one node in the replication group have not been updated by the
          recommended apply-by date. If N/A, the replication group was created after the
          recommended apply-by date.

        - **NodeGroupUpdateStatus** *(list) --*

          The status of the service update on the node group

          - *(dict) --*

            The status of the service update on the node group

            - **NodeGroupId** *(string) --*

              The ID of the node group

            - **NodeGroupMemberUpdateStatus** *(list) --*

              The status of the service update on the node group member

              - *(dict) --*

                The status of the service update on the node group member

                - **CacheClusterId** *(string) --*

                  The cache cluster ID

                - **CacheNodeId** *(string) --*

                  The node ID of the cache cluster

                - **NodeUpdateStatus** *(string) --*

                  The update status of the node

                - **NodeDeletionDate** *(datetime) --*

                  The deletion date of the node

                - **NodeUpdateStartDate** *(datetime) --*

                  The start date of the update for a node

                - **NodeUpdateEndDate** *(datetime) --*

                  The end date of the update for a node

                - **NodeUpdateInitiatedBy** *(string) --*

                  Reflects whether the update was initiated by the customer or automatically applied

                - **NodeUpdateInitiatedDate** *(datetime) --*

                  The date when the update is triggered

                - **NodeUpdateStatusModifiedDate** *(datetime) --*

                  The date when the NodeUpdateStatus was last modified

        - **CacheNodeUpdateStatus** *(list) --*

          The status of the service update on the cache node

          - *(dict) --*

            The status of the service update on the cache node

            - **CacheNodeId** *(string) --*

              The node ID of the cache cluster

            - **NodeUpdateStatus** *(string) --*

              The update status of the node

            - **NodeDeletionDate** *(datetime) --*

              The deletion date of the node

            - **NodeUpdateStartDate** *(datetime) --*

              The start date of the update for a node

            - **NodeUpdateEndDate** *(datetime) --*

              The end date of the update for a node

            - **NodeUpdateInitiatedBy** *(string) --*

              Reflects whether the update was initiated by the customer or automatically applied

            - **NodeUpdateInitiatedDate** *(datetime) --*

              The date when the update is triggered

            - **NodeUpdateStatusModifiedDate** *(datetime) --*

              The date when the NodeUpdateStatus was last modified>

        - **EstimatedUpdateTime** *(string) --*

          The estimated length of time for the update to complete

        - **Engine** *(string) --*

          The Elasticache engine to which the update applies. Either Redis or Memcached

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef = TypedDict(
    "_DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)


class DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef(
    _DescribeUpdateActionsPaginateServiceUpdateTimeRangeTypeDef
):
    """
    Type definition for `DescribeUpdateActionsPaginate` `ServiceUpdateTimeRange`

    The range of time specified to search for service updates that are in available status

    - **StartTime** *(datetime) --*

      The start time of the time range filter

    - **EndTime** *(datetime) --*

      The end time of the time range filter
    """


_ReplicationGroupAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationGroupAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationGroupAvailableWaitWaiterConfigTypeDef(
    _ReplicationGroupAvailableWaitWaiterConfigTypeDef
):
    """
    Type definition for `ReplicationGroupAvailableWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_ReplicationGroupDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_ReplicationGroupDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ReplicationGroupDeletedWaitWaiterConfigTypeDef(
    _ReplicationGroupDeletedWaitWaiterConfigTypeDef
):
    """
    Type definition for `ReplicationGroupDeletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """
