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
    def allocate_static_ip(self, staticIpName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_disk(
        self, diskName: str, instanceName: str, diskPath: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_instances_to_load_balancer(
        self, loadBalancerName: str, instanceNames: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_load_balancer_tls_certificate(
        self, loadBalancerName: str, certificateName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_static_ip(self, staticIpName: str, instanceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def close_instance_public_ports(
        self, portInfo: Dict[str, Any], instanceName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def copy_snapshot(
        self,
        targetSnapshotName: str,
        sourceRegion: str,
        sourceSnapshotName: str = None,
        sourceResourceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cloud_formation_stack(self, instances: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_disk(
        self,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        tags: List[Any] = None,
        addOns: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_disk_from_snapshot(
        self,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        diskSnapshotName: str = None,
        tags: List[Any] = None,
        addOns: List[Any] = None,
        sourceDiskName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_disk_snapshot(
        self,
        diskSnapshotName: str,
        diskName: str = None,
        instanceName: str = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_domain(self, domainName: str, tags: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_domain_entry(
        self, domainName: str, domainEntry: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_instance_snapshot(
        self, instanceSnapshotName: str, instanceName: str, tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_instances(
        self,
        instanceNames: List[Any],
        availabilityZone: str,
        blueprintId: str,
        bundleId: str,
        customImageName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List[Any] = None,
        addOns: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_instances_from_snapshot(
        self,
        instanceNames: List[Any],
        availabilityZone: str,
        bundleId: str,
        attachedDiskMapping: Dict[str, Any] = None,
        instanceSnapshotName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List[Any] = None,
        addOns: List[Any] = None,
        sourceInstanceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_key_pair(
        self, keyPairName: str, tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_load_balancer(
        self,
        loadBalancerName: str,
        instancePort: int,
        healthCheckPath: str = None,
        certificateName: str = None,
        certificateDomainName: str = None,
        certificateAlternativeNames: List[Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_load_balancer_tls_certificate(
        self,
        loadBalancerName: str,
        certificateName: str,
        certificateDomainName: str,
        certificateAlternativeNames: List[Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_relational_database(
        self,
        relationalDatabaseName: str,
        relationalDatabaseBlueprintId: str,
        relationalDatabaseBundleId: str,
        masterDatabaseName: str,
        masterUsername: str,
        availabilityZone: str = None,
        masterUserPassword: str = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        publiclyAccessible: bool = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_relational_database_from_snapshot(
        self,
        relationalDatabaseName: str,
        availabilityZone: str = None,
        publiclyAccessible: bool = None,
        relationalDatabaseSnapshotName: str = None,
        relationalDatabaseBundleId: str = None,
        sourceRelationalDatabaseName: str = None,
        restoreTime: datetime = None,
        useLatestRestorableTime: bool = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_relational_database_snapshot(
        self,
        relationalDatabaseName: str,
        relationalDatabaseSnapshotName: str,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_auto_snapshot(self, resourceName: str, date: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_disk(
        self, diskName: str, forceDeleteAddOns: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_disk_snapshot(self, diskSnapshotName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_domain(self, domainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_domain_entry(
        self, domainName: str, domainEntry: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_instance(
        self, instanceName: str, forceDeleteAddOns: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_instance_snapshot(self, instanceSnapshotName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_key_pair(self, keyPairName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_known_host_keys(self, instanceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_load_balancer(self, loadBalancerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_load_balancer_tls_certificate(
        self, loadBalancerName: str, certificateName: str, force: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_relational_database(
        self,
        relationalDatabaseName: str,
        skipFinalSnapshot: bool = None,
        finalRelationalDatabaseSnapshotName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_relational_database_snapshot(
        self, relationalDatabaseSnapshotName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_disk(self, diskName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_instances_from_load_balancer(
        self, loadBalancerName: str, instanceNames: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_static_ip(self, staticIpName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_add_on(self, addOnType: str, resourceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def download_default_key_pair(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_add_on(
        self, resourceName: str, addOnRequest: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def export_snapshot(self, sourceSnapshotName: str) -> Dict[str, Any]:
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
    def get_active_names(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_auto_snapshots(self, resourceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_blueprints(
        self, includeInactive: bool = None, pageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_bundles(
        self, includeInactive: bool = None, pageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_cloud_formation_stack_records(
        self, pageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_disk(self, diskName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_disk_snapshot(self, diskSnapshotName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_disk_snapshots(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_disks(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_domain(self, domainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_domains(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_export_snapshot_records(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_instance(self, instanceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_instance_access_details(
        self, instanceName: str, protocol: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_instance_metric_data(
        self,
        instanceName: str,
        metricName: str,
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: str,
        statistics: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_instance_port_states(self, instanceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_instance_snapshot(self, instanceSnapshotName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_instance_snapshots(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_instance_state(self, instanceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_instances(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_key_pair(self, keyPairName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_key_pairs(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_load_balancer(self, loadBalancerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_load_balancer_metric_data(
        self,
        loadBalancerName: str,
        metricName: str,
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: str,
        statistics: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_load_balancer_tls_certificates(
        self, loadBalancerName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_load_balancers(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_operation(self, operationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_operations(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_operations_for_resource(
        self, resourceName: str, pageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_regions(
        self,
        includeAvailabilityZones: bool = None,
        includeRelationalDatabaseAvailabilityZones: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database(self, relationalDatabaseName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database_blueprints(
        self, pageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database_bundles(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database_events(
        self,
        relationalDatabaseName: str,
        durationInMinutes: int = None,
        pageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database_log_events(
        self,
        relationalDatabaseName: str,
        logStreamName: str,
        startTime: datetime = None,
        endTime: datetime = None,
        startFromHead: bool = None,
        pageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database_log_streams(
        self, relationalDatabaseName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database_master_user_password(
        self, relationalDatabaseName: str, passwordVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database_metric_data(
        self,
        relationalDatabaseName: str,
        metricName: str,
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: str,
        statistics: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database_parameters(
        self, relationalDatabaseName: str, pageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database_snapshot(
        self, relationalDatabaseSnapshotName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_database_snapshots(
        self, pageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_relational_databases(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_static_ip(self, staticIpName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_static_ips(self, pageToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def import_key_pair(self, keyPairName: str, publicKeyBase64: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def is_vpc_peered(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def open_instance_public_ports(
        self, portInfo: Dict[str, Any], instanceName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def peer_vpc(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_instance_public_ports(
        self, portInfos: List[Any], instanceName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot_instance(self, instanceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot_relational_database(self, relationalDatabaseName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def release_static_ip(self, staticIpName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_instance(self, instanceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_relational_database(self, relationalDatabaseName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_instance(self, instanceName: str, force: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_relational_database(
        self, relationalDatabaseName: str, relationalDatabaseSnapshotName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(
        self, resourceName: str, tags: List[Any], resourceArn: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def unpeer_vpc(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(
        self, resourceName: str, tagKeys: List[Any], resourceArn: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_domain_entry(
        self, domainName: str, domainEntry: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_load_balancer_attribute(
        self, loadBalancerName: str, attributeName: str, attributeValue: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_relational_database(
        self,
        relationalDatabaseName: str,
        masterUserPassword: str = None,
        rotateMasterUserPassword: bool = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        enableBackupRetention: bool = None,
        disableBackupRetention: bool = None,
        publiclyAccessible: bool = None,
        applyImmediately: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_relational_database_parameters(
        self, relationalDatabaseName: str, parameters: List[Any]
    ) -> Dict[str, Any]:
        pass
