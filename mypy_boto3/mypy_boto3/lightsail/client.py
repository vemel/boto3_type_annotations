from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def allocate_static_ip(
        self,
        staticIpName: str,
    ) -> Dict:
        pass


    def attach_disk(
        self,
        diskName: str,
        instanceName: str,
        diskPath: str,
    ) -> Dict:
        pass


    def attach_instances_to_load_balancer(
        self,
        loadBalancerName: str,
        instanceNames: List,
    ) -> Dict:
        pass


    def attach_load_balancer_tls_certificate(
        self,
        loadBalancerName: str,
        certificateName: str,
    ) -> Dict:
        pass


    def attach_static_ip(
        self,
        staticIpName: str,
        instanceName: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def close_instance_public_ports(
        self,
        portInfo: Dict,
        instanceName: str,
    ) -> Dict:
        pass


    def copy_snapshot(
        self,
        targetSnapshotName: str,
        sourceRegion: str,
        sourceSnapshotName: Optional[str] = None,
        sourceResourceName: Optional[str] = None,
        restoreDate: Optional[str] = None,
        useLatestRestorableAutoSnapshot: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_cloud_formation_stack(
        self,
        instances: List,
    ) -> Dict:
        pass


    def create_disk(
        self,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        tags: Optional[List] = None,
        addOns: Optional[List] = None,
    ) -> Dict:
        pass


    def create_disk_from_snapshot(
        self,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        diskSnapshotName: Optional[str] = None,
        tags: Optional[List] = None,
        addOns: Optional[List] = None,
        sourceDiskName: Optional[str] = None,
        restoreDate: Optional[str] = None,
        useLatestRestorableAutoSnapshot: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_disk_snapshot(
        self,
        diskSnapshotName: str,
        diskName: Optional[str] = None,
        instanceName: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_domain(
        self,
        domainName: str,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_domain_entry(
        self,
        domainName: str,
        domainEntry: Dict,
    ) -> Dict:
        pass


    def create_instance_snapshot(
        self,
        instanceSnapshotName: str,
        instanceName: str,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_instances(
        self,
        instanceNames: List,
        availabilityZone: str,
        blueprintId: str,
        bundleId: str,
        customImageName: Optional[str] = None,
        userData: Optional[str] = None,
        keyPairName: Optional[str] = None,
        tags: Optional[List] = None,
        addOns: Optional[List] = None,
    ) -> Dict:
        pass


    def create_instances_from_snapshot(
        self,
        instanceNames: List,
        availabilityZone: str,
        bundleId: str,
        attachedDiskMapping: Optional[Dict] = None,
        instanceSnapshotName: Optional[str] = None,
        userData: Optional[str] = None,
        keyPairName: Optional[str] = None,
        tags: Optional[List] = None,
        addOns: Optional[List] = None,
        sourceInstanceName: Optional[str] = None,
        restoreDate: Optional[str] = None,
        useLatestRestorableAutoSnapshot: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_key_pair(
        self,
        keyPairName: str,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_load_balancer(
        self,
        loadBalancerName: str,
        instancePort: int,
        healthCheckPath: Optional[str] = None,
        certificateName: Optional[str] = None,
        certificateDomainName: Optional[str] = None,
        certificateAlternativeNames: Optional[List] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_load_balancer_tls_certificate(
        self,
        loadBalancerName: str,
        certificateName: str,
        certificateDomainName: str,
        certificateAlternativeNames: Optional[List] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_relational_database(
        self,
        relationalDatabaseName: str,
        relationalDatabaseBlueprintId: str,
        relationalDatabaseBundleId: str,
        masterDatabaseName: str,
        masterUsername: str,
        availabilityZone: Optional[str] = None,
        masterUserPassword: Optional[str] = None,
        preferredBackupWindow: Optional[str] = None,
        preferredMaintenanceWindow: Optional[str] = None,
        publiclyAccessible: Optional[bool] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_relational_database_from_snapshot(
        self,
        relationalDatabaseName: str,
        availabilityZone: Optional[str] = None,
        publiclyAccessible: Optional[bool] = None,
        relationalDatabaseSnapshotName: Optional[str] = None,
        relationalDatabaseBundleId: Optional[str] = None,
        sourceRelationalDatabaseName: Optional[str] = None,
        restoreTime: Optional[datetime] = None,
        useLatestRestorableTime: Optional[bool] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_relational_database_snapshot(
        self,
        relationalDatabaseName: str,
        relationalDatabaseSnapshotName: str,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_auto_snapshot(
        self,
        resourceName: str,
        date: str,
    ) -> Dict:
        pass


    def delete_disk(
        self,
        diskName: str,
        forceDeleteAddOns: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_disk_snapshot(
        self,
        diskSnapshotName: str,
    ) -> Dict:
        pass


    def delete_domain(
        self,
        domainName: str,
    ) -> Dict:
        pass


    def delete_domain_entry(
        self,
        domainName: str,
        domainEntry: Dict,
    ) -> Dict:
        pass


    def delete_instance(
        self,
        instanceName: str,
        forceDeleteAddOns: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_instance_snapshot(
        self,
        instanceSnapshotName: str,
    ) -> Dict:
        pass


    def delete_key_pair(
        self,
        keyPairName: str,
    ) -> Dict:
        pass


    def delete_known_host_keys(
        self,
        instanceName: str,
    ) -> Dict:
        pass


    def delete_load_balancer(
        self,
        loadBalancerName: str,
    ) -> Dict:
        pass


    def delete_load_balancer_tls_certificate(
        self,
        loadBalancerName: str,
        certificateName: str,
        force: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_relational_database(
        self,
        relationalDatabaseName: str,
        skipFinalSnapshot: Optional[bool] = None,
        finalRelationalDatabaseSnapshotName: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_relational_database_snapshot(
        self,
        relationalDatabaseSnapshotName: str,
    ) -> Dict:
        pass


    def detach_disk(
        self,
        diskName: str,
    ) -> Dict:
        pass


    def detach_instances_from_load_balancer(
        self,
        loadBalancerName: str,
        instanceNames: List,
    ) -> Dict:
        pass


    def detach_static_ip(
        self,
        staticIpName: str,
    ) -> Dict:
        pass


    def disable_add_on(
        self,
        addOnType: str,
        resourceName: str,
    ) -> Dict:
        pass


    def download_default_key_pair(
        self,
    ) -> Dict:
        pass


    def enable_add_on(
        self,
        resourceName: str,
        addOnRequest: Dict,
    ) -> Dict:
        pass


    def export_snapshot(
        self,
        sourceSnapshotName: str,
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


    def get_active_names(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_auto_snapshots(
        self,
        resourceName: str,
    ) -> Dict:
        pass


    def get_blueprints(
        self,
        includeInactive: Optional[bool] = None,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_bundles(
        self,
        includeInactive: Optional[bool] = None,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_cloud_formation_stack_records(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_disk(
        self,
        diskName: str,
    ) -> Dict:
        pass


    def get_disk_snapshot(
        self,
        diskSnapshotName: str,
    ) -> Dict:
        pass


    def get_disk_snapshots(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_disks(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_domain(
        self,
        domainName: str,
    ) -> Dict:
        pass


    def get_domains(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_export_snapshot_records(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_instance(
        self,
        instanceName: str,
    ) -> Dict:
        pass


    def get_instance_access_details(
        self,
        instanceName: str,
        protocol: Optional[str] = None,
    ) -> Dict:
        pass


    def get_instance_metric_data(
        self,
        instanceName: str,
        metricName: str,
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: str,
        statistics: List,
    ) -> Dict:
        pass


    def get_instance_port_states(
        self,
        instanceName: str,
    ) -> Dict:
        pass


    def get_instance_snapshot(
        self,
        instanceSnapshotName: str,
    ) -> Dict:
        pass


    def get_instance_snapshots(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_instance_state(
        self,
        instanceName: str,
    ) -> Dict:
        pass


    def get_instances(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_key_pair(
        self,
        keyPairName: str,
    ) -> Dict:
        pass


    def get_key_pairs(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_load_balancer(
        self,
        loadBalancerName: str,
    ) -> Dict:
        pass


    def get_load_balancer_metric_data(
        self,
        loadBalancerName: str,
        metricName: str,
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: str,
        statistics: List,
    ) -> Dict:
        pass


    def get_load_balancer_tls_certificates(
        self,
        loadBalancerName: str,
    ) -> Dict:
        pass


    def get_load_balancers(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_operation(
        self,
        operationId: str,
    ) -> Dict:
        pass


    def get_operations(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_operations_for_resource(
        self,
        resourceName: str,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_regions(
        self,
        includeAvailabilityZones: Optional[bool] = None,
        includeRelationalDatabaseAvailabilityZones: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_relational_database(
        self,
        relationalDatabaseName: str,
    ) -> Dict:
        pass


    def get_relational_database_blueprints(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_relational_database_bundles(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_relational_database_events(
        self,
        relationalDatabaseName: str,
        durationInMinutes: Optional[int] = None,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_relational_database_log_events(
        self,
        relationalDatabaseName: str,
        logStreamName: str,
        startTime: Optional[datetime] = None,
        endTime: Optional[datetime] = None,
        startFromHead: Optional[bool] = None,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_relational_database_log_streams(
        self,
        relationalDatabaseName: str,
    ) -> Dict:
        pass


    def get_relational_database_master_user_password(
        self,
        relationalDatabaseName: str,
        passwordVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def get_relational_database_metric_data(
        self,
        relationalDatabaseName: str,
        metricName: str,
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: str,
        statistics: List,
    ) -> Dict:
        pass


    def get_relational_database_parameters(
        self,
        relationalDatabaseName: str,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_relational_database_snapshot(
        self,
        relationalDatabaseSnapshotName: str,
    ) -> Dict:
        pass


    def get_relational_database_snapshots(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_relational_databases(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_static_ip(
        self,
        staticIpName: str,
    ) -> Dict:
        pass


    def get_static_ips(
        self,
        pageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def import_key_pair(
        self,
        keyPairName: str,
        publicKeyBase64: str,
    ) -> Dict:
        pass


    def is_vpc_peered(
        self,
    ) -> Dict:
        pass


    def open_instance_public_ports(
        self,
        portInfo: Dict,
        instanceName: str,
    ) -> Dict:
        pass


    def peer_vpc(
        self,
    ) -> Dict:
        pass


    def put_instance_public_ports(
        self,
        portInfos: List,
        instanceName: str,
    ) -> Dict:
        pass


    def reboot_instance(
        self,
        instanceName: str,
    ) -> Dict:
        pass


    def reboot_relational_database(
        self,
        relationalDatabaseName: str,
    ) -> Dict:
        pass


    def release_static_ip(
        self,
        staticIpName: str,
    ) -> Dict:
        pass


    def start_instance(
        self,
        instanceName: str,
    ) -> Dict:
        pass


    def start_relational_database(
        self,
        relationalDatabaseName: str,
    ) -> Dict:
        pass


    def stop_instance(
        self,
        instanceName: str,
        force: Optional[bool] = None,
    ) -> Dict:
        pass


    def stop_relational_database(
        self,
        relationalDatabaseName: str,
        relationalDatabaseSnapshotName: Optional[str] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceName: str,
        tags: List,
        resourceArn: Optional[str] = None,
    ) -> Dict:
        pass


    def unpeer_vpc(
        self,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceName: str,
        tagKeys: List,
        resourceArn: Optional[str] = None,
    ) -> Dict:
        pass


    def update_domain_entry(
        self,
        domainName: str,
        domainEntry: Dict,
    ) -> Dict:
        pass


    def update_load_balancer_attribute(
        self,
        loadBalancerName: str,
        attributeName: str,
        attributeValue: str,
    ) -> Dict:
        pass


    def update_relational_database(
        self,
        relationalDatabaseName: str,
        masterUserPassword: Optional[str] = None,
        rotateMasterUserPassword: Optional[bool] = None,
        preferredBackupWindow: Optional[str] = None,
        preferredMaintenanceWindow: Optional[str] = None,
        enableBackupRetention: Optional[bool] = None,
        disableBackupRetention: Optional[bool] = None,
        publiclyAccessible: Optional[bool] = None,
        applyImmediately: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_relational_database_parameters(
        self,
        relationalDatabaseName: str,
        parameters: List,
    ) -> Dict:
        pass

