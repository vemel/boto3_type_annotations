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
    def accept_reserved_node_exchange(
        self, ReservedNodeId: str, TargetReservedNodeOfferingId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def authorize_cluster_security_group_ingress(
        self,
        ClusterSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def authorize_snapshot_access(
        self,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_delete_cluster_snapshots(self, Identifiers: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_modify_cluster_snapshots(
        self,
        SnapshotIdentifierList: List[Any],
        ManualSnapshotRetentionPeriod: int = None,
        Force: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_resize(self, ClusterIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def copy_cluster_snapshot(
        self,
        SourceSnapshotIdentifier: str,
        TargetSnapshotIdentifier: str,
        SourceSnapshotClusterIdentifier: str = None,
        ManualSnapshotRetentionPeriod: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cluster(
        self,
        ClusterIdentifier: str,
        NodeType: str,
        MasterUsername: str,
        MasterUserPassword: str,
        DBName: str = None,
        ClusterType: str = None,
        ClusterSecurityGroups: List[Any] = None,
        VpcSecurityGroupIds: List[Any] = None,
        ClusterSubnetGroupName: str = None,
        AvailabilityZone: str = None,
        PreferredMaintenanceWindow: str = None,
        ClusterParameterGroupName: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        Port: int = None,
        ClusterVersion: str = None,
        AllowVersionUpgrade: bool = None,
        NumberOfNodes: int = None,
        PubliclyAccessible: bool = None,
        Encrypted: bool = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        ElasticIp: str = None,
        Tags: List[Any] = None,
        KmsKeyId: str = None,
        EnhancedVpcRouting: bool = None,
        AdditionalInfo: str = None,
        IamRoles: List[Any] = None,
        MaintenanceTrackName: str = None,
        SnapshotScheduleIdentifier: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cluster_parameter_group(
        self,
        ParameterGroupName: str,
        ParameterGroupFamily: str,
        Description: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cluster_security_group(
        self, ClusterSecurityGroupName: str, Description: str, Tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cluster_snapshot(
        self,
        SnapshotIdentifier: str,
        ClusterIdentifier: str,
        ManualSnapshotRetentionPeriod: int = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cluster_subnet_group(
        self,
        ClusterSubnetGroupName: str,
        Description: str,
        SubnetIds: List[Any],
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        SourceIds: List[Any] = None,
        EventCategories: List[Any] = None,
        Severity: str = None,
        Enabled: bool = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_hsm_client_certificate(
        self, HsmClientCertificateIdentifier: str, Tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_hsm_configuration(
        self,
        HsmConfigurationIdentifier: str,
        Description: str,
        HsmIpAddress: str,
        HsmPartitionName: str,
        HsmPartitionPassword: str,
        HsmServerPublicCertificate: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_snapshot_copy_grant(
        self, SnapshotCopyGrantName: str, KmsKeyId: str = None, Tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_snapshot_schedule(
        self,
        ScheduleDefinitions: List[Any] = None,
        ScheduleIdentifier: str = None,
        ScheduleDescription: str = None,
        Tags: List[Any] = None,
        DryRun: bool = None,
        NextInvocations: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_tags(self, ResourceName: str, Tags: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_cluster(
        self,
        ClusterIdentifier: str,
        SkipFinalClusterSnapshot: bool = None,
        FinalClusterSnapshotIdentifier: str = None,
        FinalClusterSnapshotRetentionPeriod: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_cluster_parameter_group(self, ParameterGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_cluster_security_group(self, ClusterSecurityGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_cluster_snapshot(
        self, SnapshotIdentifier: str, SnapshotClusterIdentifier: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_cluster_subnet_group(self, ClusterSubnetGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_event_subscription(self, SubscriptionName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_hsm_client_certificate(
        self, HsmClientCertificateIdentifier: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_hsm_configuration(self, HsmConfigurationIdentifier: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_snapshot_copy_grant(self, SnapshotCopyGrantName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_snapshot_schedule(self, ScheduleIdentifier: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_tags(self, ResourceName: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_account_attributes(
        self, AttributeNames: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cluster_db_revisions(
        self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cluster_parameter_groups(
        self,
        ParameterGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cluster_parameters(
        self,
        ParameterGroupName: str,
        Source: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cluster_security_groups(
        self,
        ClusterSecurityGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cluster_snapshots(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        Marker: str = None,
        OwnerAccount: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        ClusterExists: bool = None,
        SortingEntities: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cluster_subnet_groups(
        self,
        ClusterSubnetGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cluster_tracks(
        self,
        MaintenanceTrackName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cluster_versions(
        self,
        ClusterVersion: str = None,
        ClusterParameterGroupFamily: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_clusters(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_default_cluster_parameters(
        self, ParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_event_categories(self, SourceType: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
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
    def describe_hsm_client_certificates(
        self,
        HsmClientCertificateIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_hsm_configurations(
        self,
        HsmConfigurationIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_logging_status(self, ClusterIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_node_configuration_options(
        self,
        ActionType: str,
        SnapshotIdentifier: str = None,
        OwnerAccount: str = None,
        Filters: List[Any] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_orderable_cluster_options(
        self,
        ClusterVersion: str = None,
        NodeType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_reserved_node_offerings(
        self,
        ReservedNodeOfferingId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_reserved_nodes(
        self, ReservedNodeId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_resize(self, ClusterIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_snapshot_copy_grants(
        self,
        SnapshotCopyGrantName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_snapshot_schedules(
        self,
        ClusterIdentifier: str = None,
        ScheduleIdentifier: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_storage(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_table_restore_status(
        self,
        ClusterIdentifier: str = None,
        TableRestoreRequestId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_tags(
        self,
        ResourceName: str = None,
        ResourceType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_logging(self, ClusterIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_snapshot_copy(self, ClusterIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_logging(
        self, ClusterIdentifier: str, BucketName: str, S3KeyPrefix: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_snapshot_copy(
        self,
        ClusterIdentifier: str,
        DestinationRegion: str,
        RetentionPeriod: int = None,
        SnapshotCopyGrantName: str = None,
        ManualSnapshotRetentionPeriod: int = None,
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
    def get_cluster_credentials(
        self,
        DbUser: str,
        ClusterIdentifier: str,
        DbName: str = None,
        DurationSeconds: int = None,
        AutoCreate: bool = None,
        DbGroups: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_reserved_node_exchange_offerings(
        self, ReservedNodeId: str, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def modify_cluster(
        self,
        ClusterIdentifier: str,
        ClusterType: str = None,
        NodeType: str = None,
        NumberOfNodes: int = None,
        ClusterSecurityGroups: List[Any] = None,
        VpcSecurityGroupIds: List[Any] = None,
        MasterUserPassword: str = None,
        ClusterParameterGroupName: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        PreferredMaintenanceWindow: str = None,
        ClusterVersion: str = None,
        AllowVersionUpgrade: bool = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        NewClusterIdentifier: str = None,
        PubliclyAccessible: bool = None,
        ElasticIp: str = None,
        EnhancedVpcRouting: bool = None,
        MaintenanceTrackName: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_cluster_db_revision(
        self, ClusterIdentifier: str, RevisionTarget: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_cluster_iam_roles(
        self,
        ClusterIdentifier: str,
        AddIamRoles: List[Any] = None,
        RemoveIamRoles: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_cluster_maintenance(
        self,
        ClusterIdentifier: str,
        DeferMaintenance: bool = None,
        DeferMaintenanceIdentifier: str = None,
        DeferMaintenanceStartTime: datetime = None,
        DeferMaintenanceEndTime: datetime = None,
        DeferMaintenanceDuration: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_cluster_parameter_group(
        self, ParameterGroupName: str, Parameters: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_cluster_snapshot(
        self,
        SnapshotIdentifier: str,
        ManualSnapshotRetentionPeriod: int = None,
        Force: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_cluster_snapshot_schedule(
        self,
        ClusterIdentifier: str,
        ScheduleIdentifier: str = None,
        DisassociateSchedule: bool = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def modify_cluster_subnet_group(
        self, ClusterSubnetGroupName: str, SubnetIds: List[Any], Description: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        SourceIds: List[Any] = None,
        EventCategories: List[Any] = None,
        Severity: str = None,
        Enabled: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_snapshot_copy_retention_period(
        self, ClusterIdentifier: str, RetentionPeriod: int, Manual: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_snapshot_schedule(
        self, ScheduleIdentifier: str, ScheduleDefinitions: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def purchase_reserved_node_offering(
        self, ReservedNodeOfferingId: str, NodeCount: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot_cluster(self, ClusterIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reset_cluster_parameter_group(
        self,
        ParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def resize_cluster(
        self,
        ClusterIdentifier: str,
        NumberOfNodes: int,
        ClusterType: str = None,
        NodeType: str = None,
        Classic: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_from_cluster_snapshot(
        self,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SnapshotClusterIdentifier: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        AllowVersionUpgrade: bool = None,
        ClusterSubnetGroupName: str = None,
        PubliclyAccessible: bool = None,
        OwnerAccount: str = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        ElasticIp: str = None,
        ClusterParameterGroupName: str = None,
        ClusterSecurityGroups: List[Any] = None,
        VpcSecurityGroupIds: List[Any] = None,
        PreferredMaintenanceWindow: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        KmsKeyId: str = None,
        NodeType: str = None,
        EnhancedVpcRouting: bool = None,
        AdditionalInfo: str = None,
        IamRoles: List[Any] = None,
        MaintenanceTrackName: str = None,
        SnapshotScheduleIdentifier: str = None,
        NumberOfNodes: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_table_from_cluster_snapshot(
        self,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SourceDatabaseName: str,
        SourceTableName: str,
        NewTableName: str,
        SourceSchemaName: str = None,
        TargetDatabaseName: str = None,
        TargetSchemaName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def revoke_cluster_security_group_ingress(
        self,
        ClusterSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def revoke_snapshot_access(
        self,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def rotate_encryption_key(self, ClusterIdentifier: str) -> Dict[str, Any]:
        pass
