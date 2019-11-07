from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags_to_resource(
        self,
        ResourceName: str,
        Tags: List,
    ) -> Dict:
        pass


    def authorize_cache_security_group_ingress(
        self,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        EC2SecurityGroupOwnerId: str,
    ) -> Dict:
        pass


    def batch_apply_update_action(
        self,
        ServiceUpdateName: str,
        ReplicationGroupIds: Optional[List] = None,
        CacheClusterIds: Optional[List] = None,
    ) -> Dict:
        pass


    def batch_stop_update_action(
        self,
        ServiceUpdateName: str,
        ReplicationGroupIds: Optional[List] = None,
        CacheClusterIds: Optional[List] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def complete_migration(
        self,
        ReplicationGroupId: str,
        Force: Optional[bool] = None,
    ) -> Dict:
        pass


    def copy_snapshot(
        self,
        SourceSnapshotName: str,
        TargetSnapshotName: str,
        TargetBucket: Optional[str] = None,
        KmsKeyId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_cache_cluster(
        self,
        CacheClusterId: str,
        ReplicationGroupId: Optional[str] = None,
        AZMode: Optional[str] = None,
        PreferredAvailabilityZone: Optional[str] = None,
        PreferredAvailabilityZones: Optional[List] = None,
        NumCacheNodes: Optional[int] = None,
        CacheNodeType: Optional[str] = None,
        Engine: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        CacheParameterGroupName: Optional[str] = None,
        CacheSubnetGroupName: Optional[str] = None,
        CacheSecurityGroupNames: Optional[List] = None,
        SecurityGroupIds: Optional[List] = None,
        Tags: Optional[List] = None,
        SnapshotArns: Optional[List] = None,
        SnapshotName: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        Port: Optional[int] = None,
        NotificationTopicArn: Optional[str] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        SnapshotRetentionLimit: Optional[int] = None,
        SnapshotWindow: Optional[str] = None,
        AuthToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        CacheParameterGroupFamily: str,
        Description: str,
    ) -> Dict:
        pass


    def create_cache_security_group(
        self,
        CacheSecurityGroupName: str,
        Description: str,
    ) -> Dict:
        pass


    def create_cache_subnet_group(
        self,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: str,
        SubnetIds: List,
    ) -> Dict:
        pass


    def create_replication_group(
        self,
        ReplicationGroupId: str,
        ReplicationGroupDescription: str,
        PrimaryClusterId: Optional[str] = None,
        AutomaticFailoverEnabled: Optional[bool] = None,
        NumCacheClusters: Optional[int] = None,
        PreferredCacheClusterAZs: Optional[List] = None,
        NumNodeGroups: Optional[int] = None,
        ReplicasPerNodeGroup: Optional[int] = None,
        NodeGroupConfiguration: Optional[List] = None,
        CacheNodeType: Optional[str] = None,
        Engine: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        CacheParameterGroupName: Optional[str] = None,
        CacheSubnetGroupName: Optional[str] = None,
        CacheSecurityGroupNames: Optional[List] = None,
        SecurityGroupIds: Optional[List] = None,
        Tags: Optional[List] = None,
        SnapshotArns: Optional[List] = None,
        SnapshotName: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        Port: Optional[int] = None,
        NotificationTopicArn: Optional[str] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        SnapshotRetentionLimit: Optional[int] = None,
        SnapshotWindow: Optional[str] = None,
        AuthToken: Optional[str] = None,
        TransitEncryptionEnabled: Optional[bool] = None,
        AtRestEncryptionEnabled: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_snapshot(
        self,
        SnapshotName: str,
        ReplicationGroupId: Optional[str] = None,
        CacheClusterId: Optional[str] = None,
        KmsKeyId: Optional[str] = None,
    ) -> Dict:
        pass


    def decrease_replica_count(
        self,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: Optional[int] = None,
        ReplicaConfiguration: Optional[List] = None,
        ReplicasToRemove: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_cache_cluster(
        self,
        CacheClusterId: str,
        FinalSnapshotIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
    ):
        pass


    def delete_cache_security_group(
        self,
        CacheSecurityGroupName: str,
    ):
        pass


    def delete_cache_subnet_group(
        self,
        CacheSubnetGroupName: str,
    ):
        pass


    def delete_replication_group(
        self,
        ReplicationGroupId: str,
        RetainPrimaryCluster: Optional[bool] = None,
        FinalSnapshotIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_snapshot(
        self,
        SnapshotName: str,
    ) -> Dict:
        pass


    def describe_cache_clusters(
        self,
        CacheClusterId: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        ShowCacheNodeInfo: Optional[bool] = None,
        ShowCacheClustersNotInReplicationGroups: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_cache_engine_versions(
        self,
        Engine: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        CacheParameterGroupFamily: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        DefaultOnly: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_cache_parameter_groups(
        self,
        CacheParameterGroupName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_cache_parameters(
        self,
        CacheParameterGroupName: str,
        Source: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_cache_security_groups(
        self,
        CacheSecurityGroupName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_cache_subnet_groups(
        self,
        CacheSubnetGroupName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_engine_default_parameters(
        self,
        CacheParameterGroupFamily: str,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_events(
        self,
        SourceIdentifier: Optional[str] = None,
        SourceType: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        Duration: Optional[int] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_replication_groups(
        self,
        ReplicationGroupId: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_reserved_cache_nodes(
        self,
        ReservedCacheNodeId: Optional[str] = None,
        ReservedCacheNodesOfferingId: Optional[str] = None,
        CacheNodeType: Optional[str] = None,
        Duration: Optional[str] = None,
        ProductDescription: Optional[str] = None,
        OfferingType: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_reserved_cache_nodes_offerings(
        self,
        ReservedCacheNodesOfferingId: Optional[str] = None,
        CacheNodeType: Optional[str] = None,
        Duration: Optional[str] = None,
        ProductDescription: Optional[str] = None,
        OfferingType: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_service_updates(
        self,
        ServiceUpdateName: Optional[str] = None,
        ServiceUpdateStatus: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_snapshots(
        self,
        ReplicationGroupId: Optional[str] = None,
        CacheClusterId: Optional[str] = None,
        SnapshotName: Optional[str] = None,
        SnapshotSource: Optional[str] = None,
        Marker: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        ShowNodeGroupConfig: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_update_actions(
        self,
        ServiceUpdateName: Optional[str] = None,
        ReplicationGroupIds: Optional[List] = None,
        CacheClusterIds: Optional[List] = None,
        Engine: Optional[str] = None,
        ServiceUpdateStatus: Optional[List] = None,
        ServiceUpdateTimeRange: Optional[Dict] = None,
        UpdateActionStatus: Optional[List] = None,
        ShowNodeLevelUpdateStatus: Optional[bool] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def increase_replica_count(
        self,
        ReplicationGroupId: str,
        ApplyImmediately: bool,
        NewReplicaCount: Optional[int] = None,
        ReplicaConfiguration: Optional[List] = None,
    ) -> Dict:
        pass


    def list_allowed_node_type_modifications(
        self,
        CacheClusterId: Optional[str] = None,
        ReplicationGroupId: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceName: str,
    ) -> Dict:
        pass


    def modify_cache_cluster(
        self,
        CacheClusterId: str,
        NumCacheNodes: Optional[int] = None,
        CacheNodeIdsToRemove: Optional[List] = None,
        AZMode: Optional[str] = None,
        NewAvailabilityZones: Optional[List] = None,
        CacheSecurityGroupNames: Optional[List] = None,
        SecurityGroupIds: Optional[List] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        NotificationTopicArn: Optional[str] = None,
        CacheParameterGroupName: Optional[str] = None,
        NotificationTopicStatus: Optional[str] = None,
        ApplyImmediately: Optional[bool] = None,
        EngineVersion: Optional[str] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        SnapshotRetentionLimit: Optional[int] = None,
        SnapshotWindow: Optional[str] = None,
        CacheNodeType: Optional[str] = None,
        AuthToken: Optional[str] = None,
        AuthTokenUpdateStrategy: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        ParameterNameValues: List,
    ) -> Dict:
        pass


    def modify_cache_subnet_group(
        self,
        CacheSubnetGroupName: str,
        CacheSubnetGroupDescription: Optional[str] = None,
        SubnetIds: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_replication_group(
        self,
        ReplicationGroupId: str,
        ReplicationGroupDescription: Optional[str] = None,
        PrimaryClusterId: Optional[str] = None,
        SnapshottingClusterId: Optional[str] = None,
        AutomaticFailoverEnabled: Optional[bool] = None,
        NodeGroupId: Optional[str] = None,
        CacheSecurityGroupNames: Optional[List] = None,
        SecurityGroupIds: Optional[List] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        NotificationTopicArn: Optional[str] = None,
        CacheParameterGroupName: Optional[str] = None,
        NotificationTopicStatus: Optional[str] = None,
        ApplyImmediately: Optional[bool] = None,
        EngineVersion: Optional[str] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        SnapshotRetentionLimit: Optional[int] = None,
        SnapshotWindow: Optional[str] = None,
        CacheNodeType: Optional[str] = None,
        AuthToken: Optional[str] = None,
        AuthTokenUpdateStrategy: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_replication_group_shard_configuration(
        self,
        ReplicationGroupId: str,
        NodeGroupCount: int,
        ApplyImmediately: bool,
        ReshardingConfiguration: Optional[List] = None,
        NodeGroupsToRemove: Optional[List] = None,
        NodeGroupsToRetain: Optional[List] = None,
    ) -> Dict:
        pass


    def purchase_reserved_cache_nodes_offering(
        self,
        ReservedCacheNodesOfferingId: str,
        ReservedCacheNodeId: Optional[str] = None,
        CacheNodeCount: Optional[int] = None,
    ) -> Dict:
        pass


    def reboot_cache_cluster(
        self,
        CacheClusterId: str,
        CacheNodeIdsToReboot: List,
    ) -> Dict:
        pass


    def remove_tags_from_resource(
        self,
        ResourceName: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def reset_cache_parameter_group(
        self,
        CacheParameterGroupName: str,
        ResetAllParameters: Optional[bool] = None,
        ParameterNameValues: Optional[List] = None,
    ) -> Dict:
        pass


    def revoke_cache_security_group_ingress(
        self,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        EC2SecurityGroupOwnerId: str,
    ) -> Dict:
        pass


    def start_migration(
        self,
        ReplicationGroupId: str,
        CustomerNodeEndpointList: List,
    ) -> Dict:
        pass


    def test_failover(
        self,
        ReplicationGroupId: str,
        NodeGroupId: str,
    ) -> Dict:
        pass

