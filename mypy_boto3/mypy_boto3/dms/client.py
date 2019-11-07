from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags_to_resource(
        self,
        ResourceArn: str,
        Tags: List,
    ) -> Dict:
        pass


    def apply_pending_maintenance_action(
        self,
        ReplicationInstanceArn: str,
        ApplyAction: str,
        OptInType: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_endpoint(
        self,
        EndpointIdentifier: str,
        EndpointType: str,
        EngineName: str,
        Username: Optional[str] = None,
        Password: Optional[str] = None,
        ServerName: Optional[str] = None,
        Port: Optional[int] = None,
        DatabaseName: Optional[str] = None,
        ExtraConnectionAttributes: Optional[str] = None,
        KmsKeyId: Optional[str] = None,
        Tags: Optional[List] = None,
        CertificateArn: Optional[str] = None,
        SslMode: Optional[str] = None,
        ServiceAccessRoleArn: Optional[str] = None,
        ExternalTableDefinition: Optional[str] = None,
        DynamoDbSettings: Optional[Dict] = None,
        S3Settings: Optional[Dict] = None,
        DmsTransferSettings: Optional[Dict] = None,
        MongoDbSettings: Optional[Dict] = None,
        KinesisSettings: Optional[Dict] = None,
        ElasticsearchSettings: Optional[Dict] = None,
        RedshiftSettings: Optional[Dict] = None,
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


    def create_replication_instance(
        self,
        ReplicationInstanceIdentifier: str,
        ReplicationInstanceClass: str,
        AllocatedStorage: Optional[int] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        AvailabilityZone: Optional[str] = None,
        ReplicationSubnetGroupIdentifier: Optional[str] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        MultiAZ: Optional[bool] = None,
        EngineVersion: Optional[str] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        Tags: Optional[List] = None,
        KmsKeyId: Optional[str] = None,
        PubliclyAccessible: Optional[bool] = None,
        DnsNameServers: Optional[str] = None,
    ) -> Dict:
        pass


    def create_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        ReplicationSubnetGroupDescription: str,
        SubnetIds: List,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_replication_task(
        self,
        ReplicationTaskIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ReplicationInstanceArn: str,
        MigrationType: str,
        TableMappings: str,
        ReplicationTaskSettings: Optional[str] = None,
        CdcStartTime: Optional[datetime] = None,
        CdcStartPosition: Optional[str] = None,
        CdcStopPosition: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_certificate(
        self,
        CertificateArn: str,
    ) -> Dict:
        pass


    def delete_connection(
        self,
        EndpointArn: str,
        ReplicationInstanceArn: str,
    ) -> Dict:
        pass


    def delete_endpoint(
        self,
        EndpointArn: str,
    ) -> Dict:
        pass


    def delete_event_subscription(
        self,
        SubscriptionName: str,
    ) -> Dict:
        pass


    def delete_replication_instance(
        self,
        ReplicationInstanceArn: str,
    ) -> Dict:
        pass


    def delete_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
    ) -> Dict:
        pass


    def delete_replication_task(
        self,
        ReplicationTaskArn: str,
    ) -> Dict:
        pass


    def describe_account_attributes(
        self,
    ) -> Dict:
        pass


    def describe_certificates(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_connections(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_endpoint_types(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_endpoints(
        self,
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


    def describe_orderable_replication_instances(
        self,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_pending_maintenance_actions(
        self,
        ReplicationInstanceArn: Optional[str] = None,
        Filters: Optional[List] = None,
        Marker: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_refresh_schemas_status(
        self,
        EndpointArn: str,
    ) -> Dict:
        pass


    def describe_replication_instance_task_logs(
        self,
        ReplicationInstanceArn: str,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_replication_instances(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_replication_subnet_groups(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_replication_task_assessment_results(
        self,
        ReplicationTaskArn: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_replication_tasks(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WithoutSettings: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_schemas(
        self,
        EndpointArn: str,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_table_statistics(
        self,
        ReplicationTaskArn: str,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        Filters: Optional[List] = None,
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


    def import_certificate(
        self,
        CertificateIdentifier: str,
        CertificatePem: Optional[str] = None,
        CertificateWallet: Optional[bytes] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def modify_endpoint(
        self,
        EndpointArn: str,
        EndpointIdentifier: Optional[str] = None,
        EndpointType: Optional[str] = None,
        EngineName: Optional[str] = None,
        Username: Optional[str] = None,
        Password: Optional[str] = None,
        ServerName: Optional[str] = None,
        Port: Optional[int] = None,
        DatabaseName: Optional[str] = None,
        ExtraConnectionAttributes: Optional[str] = None,
        CertificateArn: Optional[str] = None,
        SslMode: Optional[str] = None,
        ServiceAccessRoleArn: Optional[str] = None,
        ExternalTableDefinition: Optional[str] = None,
        DynamoDbSettings: Optional[Dict] = None,
        S3Settings: Optional[Dict] = None,
        DmsTransferSettings: Optional[Dict] = None,
        MongoDbSettings: Optional[Dict] = None,
        KinesisSettings: Optional[Dict] = None,
        ElasticsearchSettings: Optional[Dict] = None,
        RedshiftSettings: Optional[Dict] = None,
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


    def modify_replication_instance(
        self,
        ReplicationInstanceArn: str,
        AllocatedStorage: Optional[int] = None,
        ApplyImmediately: Optional[bool] = None,
        ReplicationInstanceClass: Optional[str] = None,
        VpcSecurityGroupIds: Optional[List] = None,
        PreferredMaintenanceWindow: Optional[str] = None,
        MultiAZ: Optional[bool] = None,
        EngineVersion: Optional[str] = None,
        AllowMajorVersionUpgrade: Optional[bool] = None,
        AutoMinorVersionUpgrade: Optional[bool] = None,
        ReplicationInstanceIdentifier: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        SubnetIds: List,
        ReplicationSubnetGroupDescription: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_replication_task(
        self,
        ReplicationTaskArn: str,
        ReplicationTaskIdentifier: Optional[str] = None,
        MigrationType: Optional[str] = None,
        TableMappings: Optional[str] = None,
        ReplicationTaskSettings: Optional[str] = None,
        CdcStartTime: Optional[datetime] = None,
        CdcStartPosition: Optional[str] = None,
        CdcStopPosition: Optional[str] = None,
    ) -> Dict:
        pass


    def reboot_replication_instance(
        self,
        ReplicationInstanceArn: str,
        ForceFailover: Optional[bool] = None,
    ) -> Dict:
        pass


    def refresh_schemas(
        self,
        EndpointArn: str,
        ReplicationInstanceArn: str,
    ) -> Dict:
        pass


    def reload_tables(
        self,
        ReplicationTaskArn: str,
        TablesToReload: List,
        ReloadOption: Optional[str] = None,
    ) -> Dict:
        pass


    def remove_tags_from_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def start_replication_task(
        self,
        ReplicationTaskArn: str,
        StartReplicationTaskType: str,
        CdcStartTime: Optional[datetime] = None,
        CdcStartPosition: Optional[str] = None,
        CdcStopPosition: Optional[str] = None,
    ) -> Dict:
        pass


    def start_replication_task_assessment(
        self,
        ReplicationTaskArn: str,
    ) -> Dict:
        pass


    def stop_replication_task(
        self,
        ReplicationTaskArn: str,
    ) -> Dict:
        pass


    def test_connection(
        self,
        ReplicationInstanceArn: str,
        EndpointArn: str,
    ) -> Dict:
        pass

