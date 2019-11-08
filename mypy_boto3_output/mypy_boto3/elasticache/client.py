from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_tags_to_resource(
        self, ResourceName: str, Tags: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def authorize_cache_security_group_ingress(
        self,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        EC2SecurityGroupOwnerId: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_apply_update_action(
        self,
        ServiceUpdateName: str,
        ReplicationGroupIds: List[Any] = None,
        CacheClusterIds: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_stop_update_action(
        self,
        ServiceUpdateName: str,
        ReplicationGroupIds: List[Any] = None,
        CacheClusterIds: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def complete_migration(
        self, ReplicationGroupId: str, Force: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def copy_snapshot(
        self,
        SourceSnapshotName: str,
        TargetSnapshotName: str,
        TargetBucket: str = None,
        KmsKeyId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cache_cluster(
        self,
        CacheClusterId: str,
        ReplicationGroupId: str = None,
        AZMode: str = None,
        PreferredAvailabilityZone: str = None,
        PreferredAvailabilityZones: List[Any] = None,
        NumCacheNodes: int = None,
        CacheNodeType: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupName: str = None,
        CacheSubnetGroupName: str = None,
        CacheSecurityGroupNames: List[Any] = None,
        SecurityGroupIds: List[Any] = None,
        Tags: List[Any] = None,
        SnapshotArns: List[Any] = None,
        SnapshotName: str = None,
        PreferredMaintenanceWindow: str = None,
        Port: int = None,
        NotificationTopicArn: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        AuthToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        CacheParameterGroupFamily: str,
        Description: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cache_security_group(
        self, CacheSecurityGroupName: str, Description: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cache_subnet_group(
        self,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str,
        SubnetIds: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_replication_group(
        self,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str,
        PrimaryClusterId: str = None,
        AutomaticFailoverEnabled: bool = None,
        NumCacheClusters: int = None,
        PreferredCacheClusterAZs: List[Any] = None,
        NumNodeGroups: int = None,
        ReplicasPerNodeGroup: int = None,
        NodeGroupConfiguration: List[Any] = None,
        CacheNodeType: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupName: str = None,
        CacheSubnetGroupName: str = None,
        CacheSecurityGroupNames: List[Any] = None,
        SecurityGroupIds: List[Any] = None,
        Tags: List[Any] = None,
        SnapshotArns: List[Any] = None,
        SnapshotName: str = None,
        PreferredMaintenanceWindow: str = None,
        Port: int = None,
        NotificationTopicArn: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        AuthToken: str = None,
        TransitEncryptionEnabled: bool = None,
        AtRestEncryptionEnabled: bool = None,
        KmsKeyId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_snapshot(
        self,
        SnapshotName: str,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        KmsKeyId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def decrease_replica_count(
        self,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int = None,
        ReplicaConfiguration: List[Any] = None,
        ReplicasToRemove: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_cache_cluster(
        self, CacheClusterId: str, FinalSnapshotIdentifier: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_cache_parameter_group(self, CacheParameterGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_cache_security_group(self, CacheSecurityGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_cache_subnet_group(self, CacheSubnetGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_replication_group(
        self,
        ReplicationGroupId: str,
        RetainPrimaryCluster: bool = None,
        FinalSnapshotIdentifier: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_snapshot(self, SnapshotName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cache_clusters(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cache_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cache_parameter_groups(
        self,
        CacheParameterGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cache_parameters(
        self,
        CacheParameterGroupName: str,
        Source: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cache_security_groups(
        self,
        CacheSecurityGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cache_subnet_groups(
        self,
        CacheSubnetGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_engine_default_parameters(
        self, CacheParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_replication_groups(
        self, ReplicationGroupId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_reserved_cache_nodes(
        self,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_reserved_cache_nodes_offerings(
        self,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_service_updates(
        self,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_snapshots(
        self,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        Marker: str = None,
        MaxRecords: int = None,
        ShowNodeGroupConfig: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_update_actions(
        self,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[Any] = None,
        CacheClusterIds: List[Any] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[Any] = None,
        ServiceUpdateTimeRange: Dict[str, Any] = None,
        UpdateActionStatus: List[Any] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def increase_replica_count(
        self,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: int = None,
        ReplicaConfiguration: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_allowed_node_type_modifications(
        self, CacheClusterId: str = None, ReplicationGroupId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_cache_cluster(
        self,
        CacheClusterId: str,
        NumCacheNodes: int = None,
        CacheNodeIdsToRemove: List[Any] = None,
        AZMode: str = None,
        NewAvailabilityZones: List[Any] = None,
        CacheSecurityGroupNames: List[Any] = None,
        SecurityGroupIds: List[Any] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        CacheParameterGroupName: str = None,
        NotificationTopicStatus: str = None,
        ApplyImmediately: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        CacheNodeType: str = None,
        AuthToken: str = None,
        AuthTokenUpdateStrategy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_cache_parameter_group(
        self, CacheParameterGroupName: str, ParameterNameValues: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_cache_subnet_group(
        self,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str = None,
        SubnetIds: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_replication_group(
        self,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str = None,
        PrimaryClusterId: str = None,
        SnapshottingClusterId: str = None,
        AutomaticFailoverEnabled: bool = None,
        NodeGroupId: str = None,
        CacheSecurityGroupNames: List[Any] = None,
        SecurityGroupIds: List[Any] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        CacheParameterGroupName: str = None,
        NotificationTopicStatus: str = None,
        ApplyImmediately: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        SnapshotRetentionLimit: int = None,
        SnapshotWindow: str = None,
        CacheNodeType: str = None,
        AuthToken: str = None,
        AuthTokenUpdateStrategy: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_replication_group_shard_configuration(
        self,
        ReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        ReshardingConfiguration: List[Any] = None,
        NodeGroupsToRemove: List[Any] = None,
        NodeGroupsToRetain: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def purchase_reserved_cache_nodes_offering(
        self,
        ReservedCacheNodesOfferingId: str,
        ReservedCacheNodeId: str = None,
        CacheNodeCount: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot_cache_cluster(
        self, CacheClusterId: str, CacheNodeIdsToReboot: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags_from_resource(
        self, ResourceName: str, TagKeys: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reset_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        ResetAllParameters: bool = None,
        ParameterNameValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def revoke_cache_security_group_ingress(
        self,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        EC2SecurityGroupOwnerId: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_migration(
        self, ReplicationGroupId: str, CustomerNodeEndpointList: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def test_failover(
        self, ReplicationGroupId: str, NodeGroupId: str
    ) -> Dict[str, Any]:
        pass
