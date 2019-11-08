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
    def add_tags_to_resource(self, ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def apply_pending_maintenance_action(
        self, ReplicationInstanceArn: str, ApplyAction: str, OptInType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_endpoint(
        self,
        EndpointIdentifier: str,
        EndpointType: str,
        EngineName: str,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        KmsKeyId: str = None,
        Tags: List[Any] = None,
        CertificateArn: str = None,
        SslMode: str = None,
        ServiceAccessRoleArn: str = None,
        ExternalTableDefinition: str = None,
        DynamoDbSettings: Dict[str, Any] = None,
        S3Settings: Dict[str, Any] = None,
        DmsTransferSettings: Dict[str, Any] = None,
        MongoDbSettings: Dict[str, Any] = None,
        KinesisSettings: Dict[str, Any] = None,
        ElasticsearchSettings: Dict[str, Any] = None,
        RedshiftSettings: Dict[str, Any] = None,
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
    def create_replication_instance(
        self,
        ReplicationInstanceIdentifier: str,
        ReplicationInstanceClass: str,
        AllocatedStorage: int = None,
        VpcSecurityGroupIds: List[Any] = None,
        AvailabilityZone: str = None,
        ReplicationSubnetGroupIdentifier: str = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        Tags: List[Any] = None,
        KmsKeyId: str = None,
        PubliclyAccessible: bool = None,
        DnsNameServers: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        ReplicationSubnetGroupDescription: str,
        SubnetIds: List[Any],
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_replication_task(
        self,
        ReplicationTaskIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ReplicationInstanceArn: str,
        MigrationType: str,
        TableMappings: str,
        ReplicationTaskSettings: str = None,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_certificate(self, CertificateArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_connection(
        self, EndpointArn: str, ReplicationInstanceArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_endpoint(self, EndpointArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_event_subscription(self, SubscriptionName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_replication_instance(
        self, ReplicationInstanceArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_replication_subnet_group(
        self, ReplicationSubnetGroupIdentifier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_replication_task(self, ReplicationTaskArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_account_attributes(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_certificates(
        self, Filters: List[Any] = None, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_connections(
        self, Filters: List[Any] = None, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_endpoint_types(
        self, Filters: List[Any] = None, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_endpoints(
        self, Filters: List[Any] = None, MaxRecords: int = None, Marker: str = None
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
    def describe_orderable_replication_instances(
        self, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_pending_maintenance_actions(
        self,
        ReplicationInstanceArn: str = None,
        Filters: List[Any] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_refresh_schemas_status(self, EndpointArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_replication_instance_task_logs(
        self, ReplicationInstanceArn: str, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_replication_instances(
        self, Filters: List[Any] = None, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_replication_subnet_groups(
        self, Filters: List[Any] = None, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_replication_task_assessment_results(
        self, ReplicationTaskArn: str = None, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_replication_tasks(
        self,
        Filters: List[Any] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_schemas(
        self, EndpointArn: str, MaxRecords: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_table_statistics(
        self,
        ReplicationTaskArn: str,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List[Any] = None,
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
    def import_certificate(
        self,
        CertificateIdentifier: str,
        CertificatePem: str = None,
        CertificateWallet: bytes = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_endpoint(
        self,
        EndpointArn: str,
        EndpointIdentifier: str = None,
        EndpointType: str = None,
        EngineName: str = None,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        CertificateArn: str = None,
        SslMode: str = None,
        ServiceAccessRoleArn: str = None,
        ExternalTableDefinition: str = None,
        DynamoDbSettings: Dict[str, Any] = None,
        S3Settings: Dict[str, Any] = None,
        DmsTransferSettings: Dict[str, Any] = None,
        MongoDbSettings: Dict[str, Any] = None,
        KinesisSettings: Dict[str, Any] = None,
        ElasticsearchSettings: Dict[str, Any] = None,
        RedshiftSettings: Dict[str, Any] = None,
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
    def modify_replication_instance(
        self,
        ReplicationInstanceArn: str,
        AllocatedStorage: int = None,
        ApplyImmediately: bool = None,
        ReplicationInstanceClass: str = None,
        VpcSecurityGroupIds: List[Any] = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        ReplicationInstanceIdentifier: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        SubnetIds: List[Any],
        ReplicationSubnetGroupDescription: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_replication_task(
        self,
        ReplicationTaskArn: str,
        ReplicationTaskIdentifier: str = None,
        MigrationType: str = None,
        TableMappings: str = None,
        ReplicationTaskSettings: str = None,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot_replication_instance(
        self, ReplicationInstanceArn: str, ForceFailover: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def refresh_schemas(
        self, EndpointArn: str, ReplicationInstanceArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reload_tables(
        self,
        ReplicationTaskArn: str,
        TablesToReload: List[Any],
        ReloadOption: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags_from_resource(
        self, ResourceArn: str, TagKeys: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_replication_task(
        self,
        ReplicationTaskArn: str,
        StartReplicationTaskType: str,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_replication_task_assessment(
        self, ReplicationTaskArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_replication_task(self, ReplicationTaskArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def test_connection(
        self, ReplicationInstanceArn: str, EndpointArn: str
    ) -> Dict[str, Any]:
        pass
