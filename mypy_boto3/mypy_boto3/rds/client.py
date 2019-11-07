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
        FeatureName: Optional[str] = None,
    ):
        pass


    def add_role_to_db_instance(
        self,
        DBInstanceIdentifier: str,
        RoleArn: str,
        FeatureName: str,
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


    def authorize_db_security_group_ingress(
        self,
        DBSecurityGroupName: str,
        CIDRIP: Optional[str] = None,
        EC2SecurityGroupName: Optional[str] = None,
        EC2SecurityGroupId: Optional[str] = None,
        EC2SecurityGroupOwnerId: Optional[str] = None,
    ) -> Dict:
        pass


    def backtrack_db_cluster(
        self,
        DBClusterIdentifier: str,
        BacktrackTo: datetime,
        Force: Optional[bool] = None,
        UseEarliestTimeOnPointInTimeUnavailable: Optional[bool] = None,
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


    def copy_db_snapshot(
        self,
        SourceDBSnapshotIdentifier: str,
        TargetDBSnapshotIdentifier: str,
        KmsKeyId: Optional[str] = None,
        Tags: Optional[List] = None,
        CopyTags: Optional[bool] = None,
        PreSignedUrl: Optional[str] = None,
        OptionGroupName: Optional[str] = None,
        SourceRegion: Optional[str] = None,
    ) -> Dict:
        pass


    def copy_option_group(
        self,
        SourceOptionGroupIdentifier: str,
        TargetOptionGroupIdentifier: str,
        TargetOptionGroupDescription: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_custom_availability_zone(
        self,
        CustomAvailabilityZoneName: str,
        ExistingVpnId: Optional[str] = None,
        NewVpnTunnelName: Optional[str] = None,
        VpnTunnelOriginatorIP: Optional[str] = None,
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
        BacktrackWindow: Optional[int] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        EngineMode: Optional[str] = None,
        ScalingConfiguration: Optional[Dict] = None,
        DeletionProtection: Optional[bool] = None,
        GlobalClusterIdentifier: Optional[str] = None,
        EnableHttpEndpoint: Optional[bool] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
        SourceRegion: Optional[str] = None,
    ) -> Dict:
        pass


    def create_db_cluster_endpoint(
        self,
        DBClusterIdentifier: str,
        DBClusterEndpointIdentifier: str,
        EndpointType: str,
        StaticMembers: Optional[List] = None,
        ExcludedMembers: Optional[List] = None,
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
        PerformanceInsightsRetentionPeriod: Optional[int] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        ProcessorFeatures: Optional[List] = None,
        DeletionProtection: Optional[bool] = None,
        MaxAllocatedStorage: Optional[int] = None,
    ) -> Dict:
        pass


    def create_db_instance_read_replica(
        self,
        DBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str,
        DBInstanceClass: Optional[str] = None,
        AvailabilityZone: Optional[str] = None,
        Port: Optional[int] = None,
        MultiAZ: Optional[bool] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        Iops: Optional[int] = None,
        OptionGroupName: Optional[str] = None,
        DBParameterGroupName: Optional[str] = None,
        PubliclyAccessible: Optional[bool] = None,
        Tags: Optional[List] = None,
        DBSubnetGroupName: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        StorageType: Optional[str] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
        MonitoringInterval: Optional[int] = None,
        MonitoringRoleArn: Optional[str] = None,
        KmsKeyId: Optional[str] = None,
        PreSignedUrl: Optional[str] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        EnablePerformanceInsights: Optional[bool] = None,
        PerformanceInsightsKMSKeyId: Optional[str] = None,
        PerformanceInsightsRetentionPeriod: Optional[int] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        ProcessorFeatures: Optional[List] = None,
        UseDefaultProcessorFeatures: Optional[bool] = None,
        DeletionProtection: Optional[bool] = None,
        Domain: Optional[str] = None,
        DomainIAMRoleName: Optional[str] = None,
        SourceRegion: Optional[str] = None,
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


    def create_db_security_group(
        self,
        DBSecurityGroupName: str,
        DBSecurityGroupDescription: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_db_snapshot(
        self,
        DBSnapshotIdentifier: str,
        DBInstanceIdentifier: str,
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


    def create_global_cluster(
        self,
        GlobalClusterIdentifier: Optional[str] = None,
        SourceDBClusterIdentifier: Optional[str] = None,
        Engine: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        DeletionProtection: Optional[bool] = None,
        DatabaseName: Optional[str] = None,
        StorageEncrypted: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_option_group(
        self,
        OptionGroupName: str,
        EngineName: str,
        MajorEngineVersion: str,
        OptionGroupDescription: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_custom_availability_zone(
        self,
        CustomAvailabilityZoneId: str,
    ) -> Dict:
        pass


    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: Optional[bool] = None,
        FinalDBSnapshotIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_db_cluster_endpoint(
        self,
        DBClusterEndpointIdentifier: str,
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
        DeleteAutomatedBackups: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_db_instance_automated_backup(
        self,
        DbiResourceId: str,
    ) -> Dict:
        pass


    def delete_db_parameter_group(
        self,
        DBParameterGroupName: str,
    ):
        pass


    def delete_db_security_group(
        self,
        DBSecurityGroupName: str,
    ):
        pass


    def delete_db_snapshot(
        self,
        DBSnapshotIdentifier: str,
    ) -> Dict:
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


    def delete_global_cluster(
        self,
        GlobalClusterIdentifier: str,
    ) -> Dict:
        pass


    def delete_installation_media(
        self,
        InstallationMediaId: str,
    ) -> Dict:
        pass


    def delete_option_group(
        self,
        OptionGroupName: str,
    ):
        pass


    def describe_account_attributes(
        self,
    ) -> Dict:
        pass


    def describe_certificates(
        self,
        CertificateIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_custom_availability_zones(
        self,
        CustomAvailabilityZoneId: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_db_cluster_backtracks(
        self,
        DBClusterIdentifier: str,
        BacktrackIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_db_cluster_endpoints(
        self,
        DBClusterIdentifier: Optional[str] = None,
        DBClusterEndpointIdentifier: Optional[str] = None,
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
        IncludeShared: Optional[bool] = None,
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
        IncludeAll: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_db_instance_automated_backups(
        self,
        DbiResourceId: Optional[str] = None,
        DBInstanceIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
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


    def describe_db_log_files(
        self,
        DBInstanceIdentifier: str,
        FilenameContains: Optional[str] = None,
        FileLastWritten: Optional[int] = None,
        FileSize: Optional[int] = None,
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


    def describe_db_security_groups(
        self,
        DBSecurityGroupName: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_db_snapshot_attributes(
        self,
        DBSnapshotIdentifier: str,
    ) -> Dict:
        pass


    def describe_db_snapshots(
        self,
        DBInstanceIdentifier: Optional[str] = None,
        DBSnapshotIdentifier: Optional[str] = None,
        SnapshotType: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        IncludeShared: Optional[bool] = None,
        IncludePublic: Optional[bool] = None,
        DbiResourceId: Optional[str] = None,
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


    def describe_global_clusters(
        self,
        GlobalClusterIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_installation_media(
        self,
        InstallationMediaId: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_option_group_options(
        self,
        EngineName: str,
        MajorEngineVersion: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_option_groups(
        self,
        OptionGroupName: Optional[str] = None,
        Filters: Optional[List] = None,
        Marker: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        EngineName: Optional[str] = None,
        MajorEngineVersion: Optional[str] = None,
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


    def describe_reserved_db_instances(
        self,
        ReservedDBInstanceId: Optional[str] = None,
        ReservedDBInstancesOfferingId: Optional[str] = None,
        DBInstanceClass: Optional[str] = None,
        Duration: Optional[str] = None,
        ProductDescription: Optional[str] = None,
        OfferingType: Optional[str] = None,
        MultiAZ: Optional[bool] = None,
        LeaseId: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_reserved_db_instances_offerings(
        self,
        ReservedDBInstancesOfferingId: Optional[str] = None,
        DBInstanceClass: Optional[str] = None,
        Duration: Optional[str] = None,
        ProductDescription: Optional[str] = None,
        OfferingType: Optional[str] = None,
        MultiAZ: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_source_regions(
        self,
        RegionName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_valid_db_instance_modifications(
        self,
        DBInstanceIdentifier: str,
    ) -> Dict:
        pass


    def download_db_log_file_portion(
        self,
        DBInstanceIdentifier: str,
        LogFileName: str,
        Marker: Optional[str] = None,
        NumberOfLines: Optional[int] = None,
    ) -> Dict:
        pass


    def failover_db_cluster(
        self,
        DBClusterIdentifier: str,
        TargetDBInstanceIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def generate_db_auth_token(
        self,
        DBHostname: Optional[str] = None,
        Port: Optional[int] = None,
        DBUsername: Optional[str] = None,
        Region: Optional[str] = None,
    ):
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


    def import_installation_media(
        self,
        CustomAvailabilityZoneId: str,
        Engine: str,
        EngineVersion: str,
        EngineInstallationMediaPath: str,
        OSInstallationMediaPath: str,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceName: str,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_current_db_cluster_capacity(
        self,
        DBClusterIdentifier: str,
        Capacity: Optional[int] = None,
        SecondsBeforeTimeout: Optional[int] = None,
        TimeoutAction: Optional[str] = None,
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
        BacktrackWindow: Optional[int] = None,
        CloudwatchLogsExportConfiguration: Optional[Dict] = None,
        EngineVersion: Optional[str] = None,
        AllowMajorVersionUpgrade: Optional[bool] = None,
        DBInstanceParameterGroupName: Optional[str] = None,
        ScalingConfiguration: Optional[Dict] = None,
        DeletionProtection: Optional[bool] = None,
        EnableHttpEndpoint: Optional[bool] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_db_cluster_endpoint(
        self,
        DBClusterEndpointIdentifier: str,
        EndpointType: Optional[str] = None,
        StaticMembers: Optional[List] = None,
        ExcludedMembers: Optional[List] = None,
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
        PerformanceInsightsRetentionPeriod: Optional[int] = None,
        CloudwatchLogsExportConfiguration: Optional[Dict] = None,
        ProcessorFeatures: Optional[List] = None,
        UseDefaultProcessorFeatures: Optional[bool] = None,
        DeletionProtection: Optional[bool] = None,
        MaxAllocatedStorage: Optional[int] = None,
    ) -> Dict:
        pass


    def modify_db_parameter_group(
        self,
        DBParameterGroupName: str,
        Parameters: List,
    ) -> Dict:
        pass


    def modify_db_snapshot(
        self,
        DBSnapshotIdentifier: str,
        EngineVersion: Optional[str] = None,
        OptionGroupName: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_db_snapshot_attribute(
        self,
        DBSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: Optional[List] = None,
        ValuesToRemove: Optional[List] = None,
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


    def modify_global_cluster(
        self,
        GlobalClusterIdentifier: Optional[str] = None,
        NewGlobalClusterIdentifier: Optional[str] = None,
        DeletionProtection: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_option_group(
        self,
        OptionGroupName: str,
        OptionsToInclude: Optional[List] = None,
        OptionsToRemove: Optional[List] = None,
        ApplyImmediately: Optional[bool] = None,
    ) -> Dict:
        pass


    def promote_read_replica(
        self,
        DBInstanceIdentifier: str,
        BackupRetentionPeriod: Optional[int] = None,
        PreferredBackupWindow: Optional[str] = None,
    ) -> Dict:
        pass


    def promote_read_replica_db_cluster(
        self,
        DBClusterIdentifier: str,
    ) -> Dict:
        pass


    def purchase_reserved_db_instances_offering(
        self,
        ReservedDBInstancesOfferingId: str,
        ReservedDBInstanceId: Optional[str] = None,
        DBInstanceCount: Optional[int] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def reboot_db_instance(
        self,
        DBInstanceIdentifier: str,
        ForceFailover: Optional[bool] = None,
    ) -> Dict:
        pass


    def remove_from_global_cluster(
        self,
        GlobalClusterIdentifier: Optional[str] = None,
        DbClusterIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def remove_role_from_db_cluster(
        self,
        DBClusterIdentifier: str,
        RoleArn: str,
        FeatureName: Optional[str] = None,
    ):
        pass


    def remove_role_from_db_instance(
        self,
        DBInstanceIdentifier: str,
        RoleArn: str,
        FeatureName: str,
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


    def restore_db_cluster_from_s3(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        MasterUserPassword: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
        AvailabilityZones: Optional[List] = None,
        BackupRetentionPeriod: Optional[int] = None,
        CharacterSetName: Optional[str] = None,
        DatabaseName: Optional[str] = None,
        DBClusterParameterGroupName: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        DBSubnetGroupName: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        Port: Optional[int] = None,
        OptionGroupName: Optional[str] = None,
        PreferredBackupWindow: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        Tags: Optional[List] = None,
        StorageEncrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        S3Prefix: Optional[str] = None,
        BacktrackWindow: Optional[int] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        DeletionProtection: Optional[bool] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
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
        BacktrackWindow: Optional[int] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        EngineMode: Optional[str] = None,
        ScalingConfiguration: Optional[Dict] = None,
        DBClusterParameterGroupName: Optional[str] = None,
        DeletionProtection: Optional[bool] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
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
        BacktrackWindow: Optional[int] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        DBClusterParameterGroupName: Optional[str] = None,
        DeletionProtection: Optional[bool] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
    ) -> Dict:
        pass


    def restore_db_instance_from_db_snapshot(
        self,
        DBInstanceIdentifier: str,
        DBSnapshotIdentifier: str,
        DBInstanceClass: Optional[str] = None,
        Port: Optional[int] = None,
        AvailabilityZone: Optional[str] = None,
        DBSubnetGroupName: Optional[str] = None,
        MultiAZ: Optional[bool] = None,
        PubliclyAccessible: Optional[bool] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        LicenseModel: Optional[str] = None,
        DBName: Optional[str] = None,
        Engine: Optional[str] = None,
        Iops: Optional[int] = None,
        OptionGroupName: Optional[str] = None,
        Tags: Optional[List] = None,
        StorageType: Optional[str] = None,
        TdeCredentialArn: Optional[str] = None,
        TdeCredentialPassword: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        Domain: Optional[str] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
        DomainIAMRoleName: Optional[str] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        ProcessorFeatures: Optional[List] = None,
        UseDefaultProcessorFeatures: Optional[bool] = None,
        DBParameterGroupName: Optional[str] = None,
        DeletionProtection: Optional[bool] = None,
    ) -> Dict:
        pass


    def restore_db_instance_from_s3(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
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
        PubliclyAccessible: Optional[bool] = None,
        Tags: Optional[List] = None,
        StorageType: Optional[str] = None,
        StorageEncrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
        MonitoringInterval: Optional[int] = None,
        MonitoringRoleArn: Optional[str] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        S3Prefix: Optional[str] = None,
        EnablePerformanceInsights: Optional[bool] = None,
        PerformanceInsightsKMSKeyId: Optional[str] = None,
        PerformanceInsightsRetentionPeriod: Optional[int] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        ProcessorFeatures: Optional[List] = None,
        UseDefaultProcessorFeatures: Optional[bool] = None,
        DeletionProtection: Optional[bool] = None,
    ) -> Dict:
        pass


    def restore_db_instance_to_point_in_time(
        self,
        TargetDBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: Optional[str] = None,
        RestoreTime: Optional[datetime] = None,
        UseLatestRestorableTime: Optional[bool] = None,
        DBInstanceClass: Optional[str] = None,
        Port: Optional[int] = None,
        AvailabilityZone: Optional[str] = None,
        DBSubnetGroupName: Optional[str] = None,
        MultiAZ: Optional[bool] = None,
        PubliclyAccessible: Optional[bool] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        LicenseModel: Optional[str] = None,
        DBName: Optional[str] = None,
        Engine: Optional[str] = None,
        Iops: Optional[int] = None,
        OptionGroupName: Optional[str] = None,
        CopyTagsToSnapshot: Optional[bool] = None,
        Tags: Optional[List] = None,
        StorageType: Optional[str] = None,
        TdeCredentialArn: Optional[str] = None,
        TdeCredentialPassword: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        Domain: Optional[str] = None,
        DomainIAMRoleName: Optional[str] = None,
        EnableIAMDatabaseAuthentication: Optional[bool] = None,
        EnableCloudwatchLogsExports: Optional[List] = None,
        ProcessorFeatures: Optional[List] = None,
        UseDefaultProcessorFeatures: Optional[bool] = None,
        DBParameterGroupName: Optional[str] = None,
        DeletionProtection: Optional[bool] = None,
        SourceDbiResourceId: Optional[str] = None,
    ) -> Dict:
        pass


    def revoke_db_security_group_ingress(
        self,
        DBSecurityGroupName: str,
        CIDRIP: Optional[str] = None,
        EC2SecurityGroupName: Optional[str] = None,
        EC2SecurityGroupId: Optional[str] = None,
        EC2SecurityGroupOwnerId: Optional[str] = None,
    ) -> Dict:
        pass


    def start_activity_stream(
        self,
        ResourceArn: str,
        Mode: str,
        KmsKeyId: str,
        ApplyImmediately: Optional[bool] = None,
    ) -> Dict:
        pass


    def start_db_cluster(
        self,
        DBClusterIdentifier: str,
    ) -> Dict:
        pass


    def start_db_instance(
        self,
        DBInstanceIdentifier: str,
    ) -> Dict:
        pass


    def stop_activity_stream(
        self,
        ResourceArn: str,
        ApplyImmediately: Optional[bool] = None,
    ) -> Dict:
        pass


    def stop_db_cluster(
        self,
        DBClusterIdentifier: str,
    ) -> Dict:
        pass


    def stop_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBSnapshotIdentifier: Optional[str] = None,
    ) -> Dict:
        pass

