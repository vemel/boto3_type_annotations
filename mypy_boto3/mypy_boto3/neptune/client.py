from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_role_to_db_cluster(
        self,
        DBClusterIdentifier: str,
        RoleArn: str,
    ):
        pass


    def add_source_identifier_to_subscription(
        self,
        SubscriptionName: str,
        SourceIdentifier: str,
    ) -> Dict:
        pass


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
        SourceRegion: Optional[str] = None,
    ) -> Dict:
        pass


    def copy_db_parameter_group(
        self,
        SourceDBParameterGroupIdentifier: str,
        TargetDBParameterGroupIdentifier: str,
        TargetDBParameterGroupDescription: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        AvailabilityZones: Optional[List] = None,
        BackupRetentionPeriod: Optional[int] = None,
        CharacterSetName: Optional[str] = None,
        DatabaseName: Optional[str] = None,
        DBClusterParameterGroupName: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        DBSubnetGroupName: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        Port: Optional[int] = None,
        MasterUsername: Optional[str] = None,
        MasterUserPassword: Optional[str] = None,
        OptionGroupName: Optional[str] = None,
        PreferredBackupWindow: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        ReplicationSourceIdentifier: Optional[str] = None,
        Tags: Optional[List] = None,
        StorageEncrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
        PreSignedUrl: Optional[str] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        SourceRegion: Optional[str] = None,
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
        DBName: Optional[str] = None,
        AllocatedStorage: Optional[int] = None,
        MasterUsername: Optional[str] = None,
        MasterUserPassword: Optional[str] = None,
        DBSecurityGroups: Optional[List] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        AvailabilityZone: Optional[str] = None,
        DBSubnetGroupName: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        DBParameterGroupName: Optional[str] = None,
        BackupRetentionPeriod: Optional[int] = None,
        PreferredBackupWindow: Optional[str] = None,
        Port: Optional[int] = None,
        MultiAZ: Optional[bool] = None,
        EngineVersion: Optional[str] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        LicenseModel: Optional[str] = None,
        Iops: Optional[int] = None,
        OptionGroupName: Optional[str] = None,
        CharacterSetName: Optional[str] = None,
        PubliclyAccessible: Optional[bool] = None,
        Tags: Optional[List] = None,
        DBClusterIdentifier: Optional[str] = None,
        StorageType: Optional[str] = None,
        TdeCredentialArn: Optional[str] = None,
        TdeCredentialPassword: Optional[str] = None,
        StorageEncrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
        Domain: Optional[str] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
        MonitoringInterval: Optional[int] = None,
        MonitoringRoleArn: Optional[str] = None,
        DomainIAMRoleName: Optional[str] = None,
        PromotionTier: Optional[int] = None,
        Timezone: Optional[str] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        EnablePerformanceInsights: Optional[bool] = None,
        PerformanceInsightsKMSKeyId: Optional[str] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
    ) -> Dict:
        pass


    def create_db_parameter_group(
        self,
        DBParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: Optional[List] = None,
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


    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: Optional[str] = None,
        EventCategories: Optional[List] = None,
        SourceIds: Optional[List] = None,
        Enabled: Optional[bool] = None,
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
        SkipFinalSnapshot: Optional[bool] = None,
        FinalDBSnapshotIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_db_parameter_group(
        self,
        DBParameterGroupName: str,
    ):
        pass


    def delete_db_subnet_group(
        self,
        DBSubnetGroupName: str,
    ):
        pass


    def delete_event_subscription(
        self,
        SubscriptionName: str,
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


    def describe_db_parameter_groups(
        self,
        DBParameterGroupName: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_db_parameters(
        self,
        DBParameterGroupName: str,
        Source: Optional[str] = None,
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


    def describe_engine_default_parameters(
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


    def describe_event_subscriptions(
        self,
        SubscriptionName: Optional[str] = None,
        Filters: Optional[List] = None,
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


    def describe_valid_db_instance_modifications(
        self,
        DBInstanceIdentifier: str,
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
        OptionGroupName: Optional[str] = None,
        PreferredBackupWindow: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        CloudwatchLogsExportConfiguration: Optional[Dict] = None,
        EngineVersion: Optional[str] = None,
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
        AllocatedStorage: Optional[int] = None,
        DBInstanceClass: Optional[str] = None,
        DBSubnetGroupName: Optional[str] = None,
        DBSecurityGroups: Optional[List] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        ApplyImmediately: Optional[bool] = None,
        MasterUserPassword: Optional[str] = None,
        DBParameterGroupName: Optional[str] = None,
        BackupRetentionPeriod: Optional[int] = None,
        PreferredBackupWindow: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        MultiAZ: Optional[bool] = None,
        EngineVersion: Optional[str] = None,
        AllowMajorVersionUpgrade: Optional[bool] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        LicenseModel: Optional[str] = None,
        Iops: Optional[int] = None,
        OptionGroupName: Optional[str] = None,
        NewDBInstanceIdentifier: Optional[str] = None,
        StorageType: Optional[str] = None,
        TdeCredentialArn: Optional[str] = None,
        TdeCredentialPassword: Optional[str] = None,
        CACertificateIdentifier: Optional[str] = None,
        Domain: Optional[str] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
        MonitoringInterval: Optional[int] = None,
        DBPortNumber: Optional[int] = None,
        PubliclyAccessible: Optional[bool] = None,
        MonitoringRoleArn: Optional[str] = None,
        DomainIAMRoleName: Optional[str] = None,
        PromotionTier: Optional[int] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        EnablePerformanceInsights: Optional[bool] = None,
        PerformanceInsightsKMSKeyId: Optional[str] = None,
        CloudwatchLogsExportConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def modify_db_parameter_group(
        self,
        DBParameterGroupName: str,
        Parameters: List,
    ) -> Dict:
        pass


    def modify_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        SubnetIds: List,
        DBSubnetGroupDescription: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: Optional[str] = None,
        SourceType: Optional[str] = None,
        EventCategories: Optional[List] = None,
        Enabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def promote_read_replica_db_cluster(
        self,
        DBClusterIdentifier: str,
    ) -> Dict:
        pass


    def reboot_db_instance(
        self,
        DBInstanceIdentifier: str,
        ForceFailover: Optional[bool] = None,
    ) -> Dict:
        pass


    def remove_role_from_db_cluster(
        self,
        DBClusterIdentifier: str,
        RoleArn: str,
    ):
        pass


    def remove_source_identifier_from_subscription(
        self,
        SubscriptionName: str,
        SourceIdentifier: str,
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


    def reset_db_parameter_group(
        self,
        DBParameterGroupName: str,
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
        DatabaseName: Optional[str] = None,
        OptionGroupName: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        Tags: Optional[List] = None,
        KmsKeyId: Optional[str] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        DBClusterParameterGroupName: Optional[str] = None,
    ) -> Dict:
        pass


    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreType: Optional[str] = None,
        RestoreToTime: Optional[datetime] = None,
        UseLatestRestorableTime: Optional[bool] = None,
        Port: Optional[int] = None,
        DBSubnetGroupName: Optional[str] = None,
        OptionGroupName: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        Tags: Optional[List] = None,
        KmsKeyId: Optional[str] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        DBClusterParameterGroupName: Optional[str] = None,
    ) -> Dict:
        pass

