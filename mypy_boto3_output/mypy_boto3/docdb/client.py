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
    def add_tags_to_resource(self, ResourceName: str, Tags: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def apply_pending_maintenance_action(
        self, ResourceIdentifier: str, ApplyAction: str, OptInType: str
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
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        MasterUserPassword: str,
        AvailabilityZones: List[Any] = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        Tags: List[Any] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        DeletionProtection: bool = None,
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
        DBClusterIdentifier: str,
        AvailabilityZone: str = None,
        PreferredMaintenanceWindow: str = None,
        AutoMinorVersionUpgrade: bool = None,
        Tags: List[Any] = None,
        PromotionTier: int = None,
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
    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
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
    def delete_db_instance(self, DBInstanceIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> None:
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
    def describe_event_categories(
        self, SourceType: str = None, Filters: List[Any] = None
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
    def failover_db_cluster(
        self, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None
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
    def list_tags_for_resource(
        self, ResourceName: str, Filters: List[Any] = None
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
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        CloudwatchLogsExportConfiguration: Dict[str, Any] = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
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
        DBInstanceClass: str = None,
        ApplyImmediately: bool = None,
        PreferredMaintenanceWindow: str = None,
        AutoMinorVersionUpgrade: bool = None,
        NewDBInstanceIdentifier: str = None,
        CACertificateIdentifier: str = None,
        PromotionTier: int = None,
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
    def reboot_db_instance(
        self, DBInstanceIdentifier: str, ForceFailover: bool = None
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
    def restore_db_cluster_from_snapshot(
        self,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: List[Any] = None,
        EngineVersion: str = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        Tags: List[Any] = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        DeletionProtection: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreToTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        Tags: List[Any] = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[Any] = None,
        DeletionProtection: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_db_cluster(self, DBClusterIdentifier: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_db_cluster(self, DBClusterIdentifier: str) -> Dict[str, Any]:
        pass
