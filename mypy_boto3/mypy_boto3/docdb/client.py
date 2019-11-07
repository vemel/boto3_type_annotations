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
    ):
        pass


    def apply_pending_maintenance_action(
        self,
        ResourceIdentifier: str,
        ApplyAction: str,
        OptInType: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def copy_db_cluster_parameter_group(
        self,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def copy_db_cluster_snapshot(
        self,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: Optional[str] = None,
        PreSignedUrl: Optional[str] = None,
        CopyTags: Optional[bool] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        MasterUserPassword: str,
        AvailabilityZones: Optional[List] = None,
        BackupRetentionPeriod: Optional[int] = None,
        DBClusterParameterGroupName: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        DBSubnetGroupName: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        Port: Optional[int] = None,
        PreferredBackupWindow: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        Tags: Optional[List] = None,
        StorageEncrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        DeletionProtection: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBClusterIdentifier: str,
        AvailabilityZone: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        Tags: Optional[List] = None,
        PromotionTier: Optional[int] = None,
    ) -> Dict:
        pass


    def create_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: List,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: Optional[bool] = None,
        FinalDBSnapshotIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
    ):
        pass


    def delete_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
    ) -> Dict:
        pass


    def delete_db_instance(
        self,
        DBInstanceIdentifier: str,
    ) -> Dict:
        pass


    def delete_db_subnet_group(
        self,
        DBSubnetGroupName: str,
    ):
        pass


    def describe_certificates(
        self,
        CertificateIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_db_cluster_parameter_groups(
        self,
        DBClusterParameterGroupName: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_db_cluster_parameters(
        self,
        DBClusterParameterGroupName: str,
        Source: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_db_cluster_snapshot_attributes(
        self,
        DBClusterSnapshotIdentifier: str,
    ) -> Dict:
        pass


    def describe_db_cluster_snapshots(
        self,
        DBClusterIdentifier: Optional[str] = None,
        DBClusterSnapshotIdentifier: Optional[str] = None,
        SnapshotType: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        IncludeShared: Optional[bool] = None,
        IncludePublic: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_db_clusters(
        self,
        DBClusterIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_db_engine_versions(
        self,
        Engine: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        DBParameterGroupFamily: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        DefaultOnly: Optional[bool] = None,
        ListSupportedCharacterSets: Optional[bool] = None,
        ListSupportedTimezones: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_db_instances(
        self,
        DBInstanceIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_db_subnet_groups(
        self,
        DBSubnetGroupName: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_engine_default_cluster_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_event_categories(
        self,
        SourceType: Optional[str] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_events(
        self,
        SourceIdentifier: Optional[str] = None,
        SourceType: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        Duration: Optional[int] = None,
        EventCategories: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_orderable_db_instance_options(
        self,
        Engine: str,
        EngineVersion: Optional[str] = None,
        DBInstanceClass: Optional[str] = None,
        LicenseModel: Optional[str] = None,
        Vpc: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_pending_maintenance_actions(
        self,
        ResourceIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        Marker: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def failover_db_cluster(
        self,
        DBClusterIdentifier: Optional[str] = None,
        TargetDBInstanceIdentifier: Optional[str] = None,
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


    def list_tags_for_resource(
        self,
        ResourceName: str,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_db_cluster(
        self,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: Optional[str] = None,
        ApplyImmediately: Optional[bool] = None,
        BackupRetentionPeriod: Optional[int] = None,
        DBClusterParameterGroupName: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        Port: Optional[int] = None,
        MasterUserPassword: Optional[str] = None,
        PreferredBackupWindow: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        CloudwatchLogsExportConfiguration: Optional[Dict] = None,
        EngineVersion: Optional[str] = None,
        DeletionProtection: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        Parameters: List,
    ) -> Dict:
        pass


    def modify_db_cluster_snapshot_attribute(
        self,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: Optional[List] = None,
        ValuesToRemove: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: Optional[str] = None,
        ApplyImmediately: Optional[bool] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        NewDBInstanceIdentifier: Optional[str] = None,
        CACertificateIdentifier: Optional[str] = None,
        PromotionTier: Optional[int] = None,
    ) -> Dict:
        pass


    def modify_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        SubnetIds: List,
        DBSubnetGroupDescription: Optional[str] = None,
    ) -> Dict:
        pass


    def reboot_db_instance(
        self,
        DBInstanceIdentifier: str,
        ForceFailover: Optional[bool] = None,
    ) -> Dict:
        pass


    def remove_tags_from_resource(
        self,
        ResourceName: str,
        TagKeys: List,
    ):
        pass


    def reset_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        ResetAllParameters: Optional[bool] = None,
        Parameters: Optional[List] = None,
    ) -> Dict:
        pass


    def restore_db_cluster_from_snapshot(
        self,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: Optional[List] = None,
        EngineVersion: Optional[str] = None,
        Port: Optional[int] = None,
        DBSubnetGroupName: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        Tags: Optional[List] = None,
        KmsKeyId: Optional[str] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        DeletionProtection: Optional[bool] = None,
    ) -> Dict:
        pass


    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreToTime: Optional[datetime] = None,
        UseLatestRestorableTime: Optional[bool] = None,
        Port: Optional[int] = None,
        DBSubnetGroupName: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        Tags: Optional[List] = None,
        KmsKeyId: Optional[str] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        DeletionProtection: Optional[bool] = None,
    ) -> Dict:
        pass


    def start_db_cluster(
        self,
        DBClusterIdentifier: str,
    ) -> Dict:
        pass


    def stop_db_cluster(
        self,
        DBClusterIdentifier: str,
    ) -> Dict:
        pass

