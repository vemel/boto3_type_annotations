from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_reserved_node_exchange(
        self,
        ReservedNodeId: str,
        TargetReservedNodeOfferingId: str,
    ) -> Dict:
        pass


    def authorize_cluster_security_group_ingress(
        self,
        ClusterSecurityGroupName: str,
        CIDRIP: Optional[str] = None,
        EC2SecurityGroupName: Optional[str] = None,
        EC2SecurityGroupOwnerId: Optional[str] = None,
    ) -> Dict:
        pass


    def authorize_snapshot_access(
        self,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_delete_cluster_snapshots(
        self,
        Identifiers: List,
    ) -> Dict:
        pass


    def batch_modify_cluster_snapshots(
        self,
        SnapshotIdentifierList: List,
        ManualSnapshotRetentionPeriod: Optional[int] = None,
        Force: Optional[bool] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_resize(
        self,
        ClusterIdentifier: str,
    ) -> Dict:
        pass


    def copy_cluster_snapshot(
        self,
        SourceSnapshotIdentifier: str,
        TargetSnapshotIdentifier: str,
        SourceSnapshotClusterIdentifier: Optional[str] = None,
        ManualSnapshotRetentionPeriod: Optional[int] = None,
    ) -> Dict:
        pass


    def create_cluster(
        self,
        ClusterIdentifier: str,
        NodeType: str,
        MasterUsername: str,
        MasterUserPassword: str,
        DBName: Optional[str] = None,
        ClusterType: Optional[str] = None,
        ClusterSecurityGroups: Optional[List] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        ClusterSubnetGroupName: Optional[str] = None,
        AvailabilityZone: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        ClusterParameterGroupName: Optional[str] = None,
        AutomatedSnapshotRetentionPeriod: Optional[int] = None,
        ManualSnapshotRetentionPeriod: Optional[int] = None,
        Port: Optional[int] = None,
        ClusterVersion: Optional[str] = None,
        AllowVersionUpgrade: Optional[bool] = None,
        NumberOfNodes: Optional[int] = None,
        PubliclyAccessible: Optional[bool] = None,
        Encrypted: Optional[bool] = None,
        HsmClientCertificateIdentifier: Optional[str] = None,
        HsmConfigurationIdentifier: Optional[str] = None,
        ElasticIp: Optional[str] = None,
        Tags: Optional[List] = None,
        KmsKeyId: Optional[str] = None,
        EnhancedVpcRouting: Optional[bool] = None,
        AdditionalInfo: Optional[str] = None,
        IamRoles: Optional[List] = None,
        MaintenanceTrackName: Optional[str] = None,
        SnapshotScheduleIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def create_cluster_parameter_group(
        self,
        ParameterGroupName: str,
        ParameterGroupFamily: str,
        Description: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_cluster_security_group(
        self,
        ClusterSecurityGroupName: str,
        Description: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_cluster_snapshot(
        self,
        SnapshotIdentifier: str,
        ClusterIdentifier: str,
        ManualSnapshotRetentionPeriod: Optional[int] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_cluster_subnet_group(
        self,
        ClusterSubnetGroupName: str,
        Description: str,
        SubnetIds: List,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: Optional[str] = None,
        SourceIds: Optional[List] = None,
        EventCategories: Optional[List] = None,
        Severity: Optional[str] = None,
        Enabled: Optional[bool] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_hsm_client_certificate(
        self,
        HsmClientCertificateIdentifier: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_hsm_configuration(
        self,
        HsmConfigurationIdentifier: str,
        Description: str,
        HsmIpAddress: str,
        HsmPartitionName: str,
        HsmPartitionPassword: str,
        HsmServerPublicCertificate: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_snapshot_copy_grant(
        self,
        SnapshotCopyGrantName: str,
        KmsKeyId: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_snapshot_schedule(
        self,
        ScheduleDefinitions: Optional[List] = None,
        ScheduleIdentifier: Optional[str] = None,
        ScheduleDescription: Optional[str] = None,
        Tags: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextInvocations: Optional[int] = None,
    ) -> Dict:
        pass


    def create_tags(
        self,
        ResourceName: str,
        Tags: List,
    ):
        pass


    def delete_cluster(
        self,
        ClusterIdentifier: str,
        SkipFinalClusterSnapshot: Optional[bool] = None,
        FinalClusterSnapshotIdentifier: Optional[str] = None,
        FinalClusterSnapshotRetentionPeriod: Optional[int] = None,
    ) -> Dict:
        pass


    def delete_cluster_parameter_group(
        self,
        ParameterGroupName: str,
    ):
        pass


    def delete_cluster_security_group(
        self,
        ClusterSecurityGroupName: str,
    ):
        pass


    def delete_cluster_snapshot(
        self,
        SnapshotIdentifier: str,
        SnapshotClusterIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_cluster_subnet_group(
        self,
        ClusterSubnetGroupName: str,
    ):
        pass


    def delete_event_subscription(
        self,
        SubscriptionName: str,
    ):
        pass


    def delete_hsm_client_certificate(
        self,
        HsmClientCertificateIdentifier: str,
    ):
        pass


    def delete_hsm_configuration(
        self,
        HsmConfigurationIdentifier: str,
    ):
        pass


    def delete_snapshot_copy_grant(
        self,
        SnapshotCopyGrantName: str,
    ):
        pass


    def delete_snapshot_schedule(
        self,
        ScheduleIdentifier: str,
    ):
        pass


    def delete_tags(
        self,
        ResourceName: str,
        TagKeys: List,
    ):
        pass


    def describe_account_attributes(
        self,
        AttributeNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_cluster_db_revisions(
        self,
        ClusterIdentifier: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_cluster_parameter_groups(
        self,
        ParameterGroupName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_cluster_parameters(
        self,
        ParameterGroupName: str,
        Source: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_cluster_security_groups(
        self,
        ClusterSecurityGroupName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_cluster_snapshots(
        self,
        ClusterIdentifier: Optional[str] = None,
        SnapshotIdentifier: Optional[str] = None,
        SnapshotType: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        OwnerAccount: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        ClusterExists: Optional[bool] = None,
        SortingEntities: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_cluster_subnet_groups(
        self,
        ClusterSubnetGroupName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_cluster_tracks(
        self,
        MaintenanceTrackName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_cluster_versions(
        self,
        ClusterVersion: Optional[str] = None,
        ClusterParameterGroupFamily: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_clusters(
        self,
        ClusterIdentifier: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_default_cluster_parameters(
        self,
        ParameterGroupFamily: str,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_event_categories(
        self,
        SourceType: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_event_subscriptions(
        self,
        SubscriptionName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
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


    def describe_hsm_client_certificates(
        self,
        HsmClientCertificateIdentifier: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_hsm_configurations(
        self,
        HsmConfigurationIdentifier: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_logging_status(
        self,
        ClusterIdentifier: str,
    ) -> Dict:
        pass


    def describe_node_configuration_options(
        self,
        ActionType: str,
        SnapshotIdentifier: Optional[str] = None,
        OwnerAccount: Optional[str] = None,
        Filters: Optional[List] = None,
        Marker: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_orderable_cluster_options(
        self,
        ClusterVersion: Optional[str] = None,
        NodeType: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_reserved_node_offerings(
        self,
        ReservedNodeOfferingId: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_reserved_nodes(
        self,
        ReservedNodeId: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_resize(
        self,
        ClusterIdentifier: str,
    ) -> Dict:
        pass


    def describe_snapshot_copy_grants(
        self,
        SnapshotCopyGrantName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_snapshot_schedules(
        self,
        ClusterIdentifier: Optional[str] = None,
        ScheduleIdentifier: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        Marker: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_storage(
        self,
    ) -> Dict:
        pass


    def describe_table_restore_status(
        self,
        ClusterIdentifier: Optional[str] = None,
        TableRestoreRequestId: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_tags(
        self,
        ResourceName: Optional[str] = None,
        ResourceType: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
    ) -> Dict:
        pass


    def disable_logging(
        self,
        ClusterIdentifier: str,
    ) -> Dict:
        pass


    def disable_snapshot_copy(
        self,
        ClusterIdentifier: str,
    ) -> Dict:
        pass


    def enable_logging(
        self,
        ClusterIdentifier: str,
        BucketName: str,
        S3KeyPrefix: Optional[str] = None,
    ) -> Dict:
        pass


    def enable_snapshot_copy(
        self,
        ClusterIdentifier: str,
        DestinationRegion: str,
        RetentionPeriod: Optional[int] = None,
        SnapshotCopyGrantName: Optional[str] = None,
        ManualSnapshotRetentionPeriod: Optional[int] = None,
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


    def get_cluster_credentials(
        self,
        DbUser: str,
        ClusterIdentifier: str,
        DbName: Optional[str] = None,
        DurationSeconds: Optional[int] = None,
        AutoCreate: Optional[bool] = None,
        DbGroups: Optional[List] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_reserved_node_exchange_offerings(
        self,
        ReservedNodeId: str,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def modify_cluster(
        self,
        ClusterIdentifier: str,
        ClusterType: Optional[str] = None,
        NodeType: Optional[str] = None,
        NumberOfNodes: Optional[int] = None,
        ClusterSecurityGroups: Optional[List] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        MasterUserPassword: Optional[str] = None,
        ClusterParameterGroupName: Optional[str] = None,
        AutomatedSnapshotRetentionPeriod: Optional[int] = None,
        ManualSnapshotRetentionPeriod: Optional[int] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        ClusterVersion: Optional[str] = None,
        AllowVersionUpgrade: Optional[bool] = None,
        HsmClientCertificateIdentifier: Optional[str] = None,
        HsmConfigurationIdentifier: Optional[str] = None,
        NewClusterIdentifier: Optional[str] = None,
        PubliclyAccessible: Optional[bool] = None,
        ElasticIp: Optional[str] = None,
        EnhancedVpcRouting: Optional[bool] = None,
        MaintenanceTrackName: Optional[str] = None,
        Encrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_cluster_db_revision(
        self,
        ClusterIdentifier: str,
        RevisionTarget: str,
    ) -> Dict:
        pass


    def modify_cluster_iam_roles(
        self,
        ClusterIdentifier: str,
        AddIamRoles: Optional[List] = None,
        RemoveIamRoles: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_cluster_maintenance(
        self,
        ClusterIdentifier: str,
        DeferMaintenance: Optional[bool] = None,
        DeferMaintenanceIdentifier: Optional[str] = None,
        DeferMaintenanceStartTime: Optional[datetime] = None,
        DeferMaintenanceEndTime: Optional[datetime] = None,
        DeferMaintenanceDuration: Optional[int] = None,
    ) -> Dict:
        pass


    def modify_cluster_parameter_group(
        self,
        ParameterGroupName: str,
        Parameters: List,
    ) -> Dict:
        pass


    def modify_cluster_snapshot(
        self,
        SnapshotIdentifier: str,
        ManualSnapshotRetentionPeriod: Optional[int] = None,
        Force: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_cluster_snapshot_schedule(
        self,
        ClusterIdentifier: str,
        ScheduleIdentifier: Optional[str] = None,
        DisassociateSchedule: Optional[bool] = None,
    ):
        pass


    def modify_cluster_subnet_group(
        self,
        ClusterSubnetGroupName: str,
        SubnetIds: List,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: Optional[str] = None,
        SourceType: Optional[str] = None,
        SourceIds: Optional[List] = None,
        EventCategories: Optional[List] = None,
        Severity: Optional[str] = None,
        Enabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_snapshot_copy_retention_period(
        self,
        ClusterIdentifier: str,
        RetentionPeriod: int,
        Manual: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_snapshot_schedule(
        self,
        ScheduleIdentifier: str,
        ScheduleDefinitions: List,
    ) -> Dict:
        pass


    def purchase_reserved_node_offering(
        self,
        ReservedNodeOfferingId: str,
        NodeCount: Optional[int] = None,
    ) -> Dict:
        pass


    def reboot_cluster(
        self,
        ClusterIdentifier: str,
    ) -> Dict:
        pass


    def reset_cluster_parameter_group(
        self,
        ParameterGroupName: str,
        ResetAllParameters: Optional[bool] = None,
        Parameters: Optional[List] = None,
    ) -> Dict:
        pass


    def resize_cluster(
        self,
        ClusterIdentifier: str,
        NumberOfNodes: int,
        ClusterType: Optional[str] = None,
        NodeType: Optional[str] = None,
        Classic: Optional[bool] = None,
    ) -> Dict:
        pass


    def restore_from_cluster_snapshot(
        self,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SnapshotClusterIdentifier: Optional[str] = None,
        Port: Optional[int] = None,
        AvailabilityZone: Optional[str] = None,
        AllowVersionUpgrade: Optional[bool] = None,
        ClusterSubnetGroupName: Optional[str] = None,
        PubliclyAccessible: Optional[bool] = None,
        OwnerAccount: Optional[str] = None,
        HsmClientCertificateIdentifier: Optional[str] = None,
        HsmConfigurationIdentifier: Optional[str] = None,
        ElasticIp: Optional[str] = None,
        ClusterParameterGroupName: Optional[str] = None,
        ClusterSecurityGroups: Optional[List] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        AutomatedSnapshotRetentionPeriod: Optional[int] = None,
        ManualSnapshotRetentionPeriod: Optional[int] = None,
        KmsKeyId: Optional[str] = None,
        NodeType: Optional[str] = None,
        EnhancedVpcRouting: Optional[bool] = None,
        AdditionalInfo: Optional[str] = None,
        IamRoles: Optional[List] = None,
        MaintenanceTrackName: Optional[str] = None,
        SnapshotScheduleIdentifier: Optional[str] = None,
        NumberOfNodes: Optional[int] = None,
    ) -> Dict:
        pass


    def restore_table_from_cluster_snapshot(
        self,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SourceDatabaseName: str,
        SourceTableName: str,
        NewTableName: str,
        SourceSchemaName: Optional[str] = None,
        TargetDatabaseName: Optional[str] = None,
        TargetSchemaName: Optional[str] = None,
    ) -> Dict:
        pass


    def revoke_cluster_security_group_ingress(
        self,
        ClusterSecurityGroupName: str,
        CIDRIP: Optional[str] = None,
        EC2SecurityGroupName: Optional[str] = None,
        EC2SecurityGroupOwnerId: Optional[str] = None,
    ) -> Dict:
        pass


    def revoke_snapshot_access(
        self,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def rotate_encryption_key(
        self,
        ClusterIdentifier: str,
    ) -> Dict:
        pass

