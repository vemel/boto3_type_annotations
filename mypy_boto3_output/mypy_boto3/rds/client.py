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
    def add_role_to_db_cluster(
        self, DBClusterIdentifier: str, RoleArn: str, FeatureName: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def add_role_to_db_instance(
        self, DBInstanceIdentifier: str, RoleArn: str, FeatureName: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def add_source_identifier_to_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_tags_to_resource(self, ResourceName: str, Tags: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def apply_pending_maintenance_action(
        self, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def authorize_db_security_group_ingress(
        self,
        DBSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupId: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def backtrack_db_cluster(
        self,
        DBClusterIdentifier: str,
        BacktrackTo: datetime,
        Force: bool = None,
        UseEarliestTimeOnPointInTimeUnavailable: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def copy_db_cluster_parameter_group(
        self,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def copy_db_cluster_snapshot(
        self,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        CopyTags: bool = None,
        Tags: List[Any] = None,
        SourceRegion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def copy_db_parameter_group(
        self,
        SourceDBParameterGroupIdentifier: str,
        TargetDBParameterGroupIdentifier: str,
        TargetDBParameterGroupDescription: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def copy_db_snapshot(
        self,
        SourceDBSnapshotIdentifier: str,
        TargetDBSnapshotIdentifier: str,
        KmsKeyId: str = None,
        Tags: List[Any] = None,
        CopyTags: bool = None,
        PreSignedUrl: str = None,
        OptionGroupName: str = None,
        SourceRegion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def copy_option_group(
        self,
        SourceOptionGroupIdentifier: str,
        TargetOptionGroupIdentifier: str,
        TargetOptionGroupDescription: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_custom_availability_zone(
        self,
        CustomAvailabilityZoneName: str,
        ExistingVpnId: str = None,
        NewVpnTunnelName: str = None,
        VpnTunnelOriginatorIP: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        AvailabilityZones: List[Any] = None,
        BackupRetentionPeriod: int = None,
        CharacterSetName: str = None,
        DatabaseName: str = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        ReplicationSourceIdentifier: str = None,
        Tags: List[Any] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        EngineMode: str = None,
        ScalingConfiguration: Dict[str, Any] = None,
        DeletionProtection: bool = None,
        GlobalClusterIdentifier: str = None,
        EnableHttpEndpoint: bool = None,
        CopyTagsToSnapshot: bool = None,
        SourceRegion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_cluster_endpoint(
        self,
        DBClusterIdentifier: str,
        DBClusterEndpointIdentifier: str,
        EndpointType: str,
        StaticMembers: List[Any] = None,
        ExcludedMembers: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBName: str = None,
        AllocatedStorage: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        DBSecurityGroups: List[Any] = None,
        VpcSecurityGroupIds: List[Any] = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        PreferredMaintenanceWindow: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        CharacterSetName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List[Any] = None,
        DBClusterIdentifier: str = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        DomainIAMRoleName: str = None,
        PromotionTier: int = None,
        Timezone: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        ProcessorFeatures: List[Any] = None,
        DeletionProtection: bool = None,
        MaxAllocatedStorage: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_instance_read_replica(
        self,
        DBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str,
        DBInstanceClass: str = None,
        AvailabilityZone: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        Iops: int = None,
        OptionGroupName: str = None,
        DBParameterGroupName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List[Any] = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        StorageType: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        ProcessorFeatures: List[Any] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
        SourceRegion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_parameter_group(
        self,
        DBParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_security_group(
        self,
        DBSecurityGroupName: str,
        DBSecurityGroupDescription: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_snapshot(
        self,
        DBSnapshotIdentifier: str,
        DBInstanceIdentifier: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
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
        EventCategories: List[Any] = None,
        SourceIds: List[Any] = None,
        Enabled: bool = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_global_cluster(
        self,
        GlobalClusterIdentifier: str = None,
        SourceDBClusterIdentifier: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
        DatabaseName: str = None,
        StorageEncrypted: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_option_group(
        self,
        OptionGroupName: str,
        EngineName: str,
        MajorEngineVersion: str,
        OptionGroupDescription: str,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_custom_availability_zone(
        self, CustomAvailabilityZoneId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_db_cluster_endpoint(
        self, DBClusterEndpointIdentifier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_db_cluster_parameter_group(
        self, DBClusterParameterGroupName: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_db_cluster_snapshot(
        self, DBClusterSnapshotIdentifier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_db_instance(
        self,
        DBInstanceIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
        DeleteAutomatedBackups: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_db_instance_automated_backup(self, DbiResourceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_db_parameter_group(self, DBParameterGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_db_security_group(self, DBSecurityGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_db_snapshot(self, DBSnapshotIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_event_subscription(self, SubscriptionName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_global_cluster(self, GlobalClusterIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_installation_media(self, InstallationMediaId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_option_group(self, OptionGroupName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_account_attributes(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_certificates(
        self,
        CertificateIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_custom_availability_zones(
        self,
        CustomAvailabilityZoneId: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_cluster_backtracks(
        self,
        DBClusterIdentifier: str,
        BacktrackIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_cluster_endpoints(
        self,
        DBClusterIdentifier: str = None,
        DBClusterEndpointIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_cluster_parameter_groups(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_cluster_parameters(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_cluster_snapshot_attributes(
        self, DBClusterSnapshotIdentifier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_cluster_snapshots(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_clusters(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        IncludeAll: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_instance_automated_backups(
        self,
        DbiResourceId: str = None,
        DBInstanceIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_instances(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_log_files(
        self,
        DBInstanceIdentifier: str,
        FilenameContains: str = None,
        FileLastWritten: int = None,
        FileSize: int = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_parameter_groups(
        self,
        DBParameterGroupName: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_parameters(
        self,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_security_groups(
        self,
        DBSecurityGroupName: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_snapshot_attributes(
        self, DBSnapshotIdentifier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_snapshots(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_db_subnet_groups(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_engine_default_cluster_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_engine_default_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_event_categories(
        self, SourceType: str = None, Filters: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
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
        EventCategories: List[Any] = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_global_clusters(
        self,
        GlobalClusterIdentifier: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_installation_media(
        self,
        InstallationMediaId: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_option_group_options(
        self,
        EngineName: str,
        MajorEngineVersion: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_option_groups(
        self,
        OptionGroupName: str = None,
        Filters: List[Any] = None,
        Marker: str = None,
        MaxRecords: int = None,
        EngineName: str = None,
        MajorEngineVersion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_orderable_db_instance_options(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_pending_maintenance_actions(
        self,
        ResourceIdentifier: str = None,
        Filters: List[Any] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_reserved_db_instances(
        self,
        ReservedDBInstanceId: str = None,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        LeaseId: str = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_reserved_db_instances_offerings(
        self,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_source_regions(
        self,
        RegionName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_valid_db_instance_modifications(
        self, DBInstanceIdentifier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def download_db_log_file_portion(
        self,
        DBInstanceIdentifier: str,
        LogFileName: str,
        Marker: str = None,
        NumberOfLines: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def failover_db_cluster(
        self, DBClusterIdentifier: str, TargetDBInstanceIdentifier: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_db_auth_token(
        self,
        DBHostname: str = None,
        Port: int = None,
        DBUsername: str = None,
        Region: str = None,
    ) -> None:
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
    def import_installation_media(
        self,
        CustomAvailabilityZoneId: str,
        Engine: str,
        EngineVersion: str,
        EngineInstallationMediaPath: str,
        OSInstallationMediaPath: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, ResourceName: str, Filters: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_current_db_cluster_capacity(
        self,
        DBClusterIdentifier: str,
        Capacity: int = None,
        SecondsBeforeTimeout: int = None,
        TimeoutAction: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_db_cluster(
        self,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str = None,
        ApplyImmediately: bool = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        Port: int = None,
        MasterUserPassword: str = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        CloudwatchLogsExportConfiguration: Dict[str, Any] = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        DBInstanceParameterGroupName: str = None,
        ScalingConfiguration: Dict[str, Any] = None,
        DeletionProtection: bool = None,
        EnableHttpEndpoint: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_db_cluster_endpoint(
        self,
        DBClusterEndpointIdentifier: str,
        EndpointType: str = None,
        StaticMembers: List[Any] = None,
        ExcludedMembers: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_db_cluster_parameter_group(
        self, DBClusterParameterGroupName: str, Parameters: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_db_cluster_snapshot_attribute(
        self,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[Any] = None,
        ValuesToRemove: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_db_instance(
        self,
        DBInstanceIdentifier: str,
        AllocatedStorage: int = None,
        DBInstanceClass: str = None,
        DBSubnetGroupName: str = None,
        DBSecurityGroups: List[Any] = None,
        VpcSecurityGroupIds: List[Any] = None,
        ApplyImmediately: bool = None,
        MasterUserPassword: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        NewDBInstanceIdentifier: str = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        CACertificateIdentifier: str = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        DBPortNumber: int = None,
        PubliclyAccessible: bool = None,
        MonitoringRoleArn: str = None,
        DomainIAMRoleName: str = None,
        PromotionTier: int = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        CloudwatchLogsExportConfiguration: Dict[str, Any] = None,
        ProcessorFeatures: List[Any] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
        MaxAllocatedStorage: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_db_parameter_group(
        self, DBParameterGroupName: str, Parameters: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_db_snapshot(
        self,
        DBSnapshotIdentifier: str,
        EngineVersion: str = None,
        OptionGroupName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_db_snapshot_attribute(
        self,
        DBSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[Any] = None,
        ValuesToRemove: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        SubnetIds: List[Any],
        DBSubnetGroupDescription: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[Any] = None,
        Enabled: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_global_cluster(
        self,
        GlobalClusterIdentifier: str = None,
        NewGlobalClusterIdentifier: str = None,
        DeletionProtection: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_option_group(
        self,
        OptionGroupName: str,
        OptionsToInclude: List[Any] = None,
        OptionsToRemove: List[Any] = None,
        ApplyImmediately: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def promote_read_replica(
        self,
        DBInstanceIdentifier: str,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def promote_read_replica_db_cluster(
        self, DBClusterIdentifier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def purchase_reserved_db_instances_offering(
        self,
        ReservedDBInstancesOfferingId: str,
        ReservedDBInstanceId: str = None,
        DBInstanceCount: int = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot_db_instance(
        self, DBInstanceIdentifier: str, ForceFailover: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_from_global_cluster(
        self, GlobalClusterIdentifier: str = None, DbClusterIdentifier: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_role_from_db_cluster(
        self, DBClusterIdentifier: str, RoleArn: str, FeatureName: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def remove_role_from_db_instance(
        self, DBInstanceIdentifier: str, RoleArn: str, FeatureName: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def remove_source_identifier_from_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def reset_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reset_db_parameter_group(
        self,
        DBParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
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
        AvailabilityZones: List[Any] = None,
        BackupRetentionPeriod: int = None,
        CharacterSetName: str = None,
        DatabaseName: str = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        Tags: List[Any] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        S3Prefix: str = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_db_cluster_from_snapshot(
        self,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: List[Any] = None,
        EngineVersion: str = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        DatabaseName: str = None,
        OptionGroupName: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        Tags: List[Any] = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        EngineMode: str = None,
        ScalingConfiguration: Dict[str, Any] = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreType: str = None,
        RestoreToTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        OptionGroupName: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        Tags: List[Any] = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_db_instance_from_db_snapshot(
        self,
        DBInstanceIdentifier: str,
        DBSnapshotIdentifier: str,
        DBInstanceClass: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        MultiAZ: bool = None,
        PubliclyAccessible: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        DBName: str = None,
        Engine: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        Tags: List[Any] = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        DomainIAMRoleName: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        ProcessorFeatures: List[Any] = None,
        UseDefaultProcessorFeatures: bool = None,
        DBParameterGroupName: str = None,
        DeletionProtection: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_db_instance_from_s3(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
        DBName: str = None,
        AllocatedStorage: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        DBSecurityGroups: List[Any] = None,
        VpcSecurityGroupIds: List[Any] = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        PreferredMaintenanceWindow: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List[Any] = None,
        StorageType: str = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        S3Prefix: str = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        ProcessorFeatures: List[Any] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_db_instance_to_point_in_time(
        self,
        TargetDBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str = None,
        RestoreTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        DBInstanceClass: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        MultiAZ: bool = None,
        PubliclyAccessible: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        DBName: str = None,
        Engine: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        CopyTagsToSnapshot: bool = None,
        Tags: List[Any] = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        ProcessorFeatures: List[Any] = None,
        UseDefaultProcessorFeatures: bool = None,
        DBParameterGroupName: str = None,
        DeletionProtection: bool = None,
        SourceDbiResourceId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def revoke_db_security_group_ingress(
        self,
        DBSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupId: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_activity_stream(
        self, ResourceArn: str, Mode: str, KmsKeyId: str, ApplyImmediately: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_db_cluster(self, DBClusterIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_db_instance(self, DBInstanceIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_activity_stream(
        self, ResourceArn: str, ApplyImmediately: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_db_cluster(self, DBClusterIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_db_instance(
        self, DBInstanceIdentifier: str, DBSnapshotIdentifier: str = None
    ) -> Dict[str, Any]:
        pass
