# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.lightsail.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Lightsail](index.md#lightsail) / Client
    - [Client](#client)
        - [Client().allocate_static_ip](#clientallocate_static_ip)
        - [Client().attach_disk](#clientattach_disk)
        - [Client().attach_instances_to_load_balancer](#clientattach_instances_to_load_balancer)
        - [Client().attach_load_balancer_tls_certificate](#clientattach_load_balancer_tls_certificate)
        - [Client().attach_static_ip](#clientattach_static_ip)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().close_instance_public_ports](#clientclose_instance_public_ports)
        - [Client().copy_snapshot](#clientcopy_snapshot)
        - [Client().create_cloud_formation_stack](#clientcreate_cloud_formation_stack)
        - [Client().create_disk](#clientcreate_disk)
        - [Client().create_disk_from_snapshot](#clientcreate_disk_from_snapshot)
        - [Client().create_disk_snapshot](#clientcreate_disk_snapshot)
        - [Client().create_domain](#clientcreate_domain)
        - [Client().create_domain_entry](#clientcreate_domain_entry)
        - [Client().create_instance_snapshot](#clientcreate_instance_snapshot)
        - [Client().create_instances](#clientcreate_instances)
        - [Client().create_instances_from_snapshot](#clientcreate_instances_from_snapshot)
        - [Client().create_key_pair](#clientcreate_key_pair)
        - [Client().create_load_balancer](#clientcreate_load_balancer)
        - [Client().create_load_balancer_tls_certificate](#clientcreate_load_balancer_tls_certificate)
        - [Client().create_relational_database](#clientcreate_relational_database)
        - [Client().create_relational_database_from_snapshot](#clientcreate_relational_database_from_snapshot)
        - [Client().create_relational_database_snapshot](#clientcreate_relational_database_snapshot)
        - [Client().delete_auto_snapshot](#clientdelete_auto_snapshot)
        - [Client().delete_disk](#clientdelete_disk)
        - [Client().delete_disk_snapshot](#clientdelete_disk_snapshot)
        - [Client().delete_domain](#clientdelete_domain)
        - [Client().delete_domain_entry](#clientdelete_domain_entry)
        - [Client().delete_instance](#clientdelete_instance)
        - [Client().delete_instance_snapshot](#clientdelete_instance_snapshot)
        - [Client().delete_key_pair](#clientdelete_key_pair)
        - [Client().delete_known_host_keys](#clientdelete_known_host_keys)
        - [Client().delete_load_balancer](#clientdelete_load_balancer)
        - [Client().delete_load_balancer_tls_certificate](#clientdelete_load_balancer_tls_certificate)
        - [Client().delete_relational_database](#clientdelete_relational_database)
        - [Client().delete_relational_database_snapshot](#clientdelete_relational_database_snapshot)
        - [Client().detach_disk](#clientdetach_disk)
        - [Client().detach_instances_from_load_balancer](#clientdetach_instances_from_load_balancer)
        - [Client().detach_static_ip](#clientdetach_static_ip)
        - [Client().disable_add_on](#clientdisable_add_on)
        - [Client().download_default_key_pair](#clientdownload_default_key_pair)
        - [Client().enable_add_on](#clientenable_add_on)
        - [Client().export_snapshot](#clientexport_snapshot)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_active_names](#clientget_active_names)
        - [Client().get_auto_snapshots](#clientget_auto_snapshots)
        - [Client().get_blueprints](#clientget_blueprints)
        - [Client().get_bundles](#clientget_bundles)
        - [Client().get_cloud_formation_stack_records](#clientget_cloud_formation_stack_records)
        - [Client().get_disk](#clientget_disk)
        - [Client().get_disk_snapshot](#clientget_disk_snapshot)
        - [Client().get_disk_snapshots](#clientget_disk_snapshots)
        - [Client().get_disks](#clientget_disks)
        - [Client().get_domain](#clientget_domain)
        - [Client().get_domains](#clientget_domains)
        - [Client().get_export_snapshot_records](#clientget_export_snapshot_records)
        - [Client().get_instance](#clientget_instance)
        - [Client().get_instance_access_details](#clientget_instance_access_details)
        - [Client().get_instance_metric_data](#clientget_instance_metric_data)
        - [Client().get_instance_port_states](#clientget_instance_port_states)
        - [Client().get_instance_snapshot](#clientget_instance_snapshot)
        - [Client().get_instance_snapshots](#clientget_instance_snapshots)
        - [Client().get_instance_state](#clientget_instance_state)
        - [Client().get_instances](#clientget_instances)
        - [Client().get_key_pair](#clientget_key_pair)
        - [Client().get_key_pairs](#clientget_key_pairs)
        - [Client().get_load_balancer](#clientget_load_balancer)
        - [Client().get_load_balancer_metric_data](#clientget_load_balancer_metric_data)
        - [Client().get_load_balancer_tls_certificates](#clientget_load_balancer_tls_certificates)
        - [Client().get_load_balancers](#clientget_load_balancers)
        - [Client().get_operation](#clientget_operation)
        - [Client().get_operations](#clientget_operations)
        - [Client().get_operations_for_resource](#clientget_operations_for_resource)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_regions](#clientget_regions)
        - [Client().get_relational_database](#clientget_relational_database)
        - [Client().get_relational_database_blueprints](#clientget_relational_database_blueprints)
        - [Client().get_relational_database_bundles](#clientget_relational_database_bundles)
        - [Client().get_relational_database_events](#clientget_relational_database_events)
        - [Client().get_relational_database_log_events](#clientget_relational_database_log_events)
        - [Client().get_relational_database_log_streams](#clientget_relational_database_log_streams)
        - [Client().get_relational_database_master_user_password](#clientget_relational_database_master_user_password)
        - [Client().get_relational_database_metric_data](#clientget_relational_database_metric_data)
        - [Client().get_relational_database_parameters](#clientget_relational_database_parameters)
        - [Client().get_relational_database_snapshot](#clientget_relational_database_snapshot)
        - [Client().get_relational_database_snapshots](#clientget_relational_database_snapshots)
        - [Client().get_relational_databases](#clientget_relational_databases)
        - [Client().get_static_ip](#clientget_static_ip)
        - [Client().get_static_ips](#clientget_static_ips)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_key_pair](#clientimport_key_pair)
        - [Client().is_vpc_peered](#clientis_vpc_peered)
        - [Client().open_instance_public_ports](#clientopen_instance_public_ports)
        - [Client().peer_vpc](#clientpeer_vpc)
        - [Client().put_instance_public_ports](#clientput_instance_public_ports)
        - [Client().reboot_instance](#clientreboot_instance)
        - [Client().reboot_relational_database](#clientreboot_relational_database)
        - [Client().release_static_ip](#clientrelease_static_ip)
        - [Client().start_instance](#clientstart_instance)
        - [Client().start_relational_database](#clientstart_relational_database)
        - [Client().stop_instance](#clientstop_instance)
        - [Client().stop_relational_database](#clientstop_relational_database)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().unpeer_vpc](#clientunpeer_vpc)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_domain_entry](#clientupdate_domain_entry)
        - [Client().update_load_balancer_attribute](#clientupdate_load_balancer_attribute)
        - [Client().update_relational_database](#clientupdate_relational_database)
        - [Client().update_relational_database_parameters](#clientupdate_relational_database_parameters)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L13)

```python
class Client(BaseClient):
```

### Client().allocate_static_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L16)

```python
def allocate_static_ip(staticIpName: str) -> Dict[str, Any]:
```

### Client().attach_disk

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L20)

```python
def attach_disk(
    diskName: str,
    instanceName: str,
    diskPath: str,
) -> Dict[str, Any]:
```

### Client().attach_instances_to_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L26)

```python
def attach_instances_to_load_balancer(
    loadBalancerName: str,
    instanceNames: List[Any],
) -> Dict[str, Any]:
```

### Client().attach_load_balancer_tls_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L32)

```python
def attach_load_balancer_tls_certificate(
    loadBalancerName: str,
    certificateName: str,
) -> Dict[str, Any]:
```

### Client().attach_static_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L38)

```python
def attach_static_ip(staticIpName: str, instanceName: str) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L42)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().close_instance_public_ports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L46)

```python
def close_instance_public_ports(
    portInfo: Dict[str, Any],
    instanceName: str,
) -> Dict[str, Any]:
```

### Client().copy_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L52)

```python
def copy_snapshot(
    targetSnapshotName: str,
    sourceRegion: str,
    sourceSnapshotName: str = None,
    sourceResourceName: str = None,
    restoreDate: str = None,
    useLatestRestorableAutoSnapshot: bool = None,
) -> Dict[str, Any]:
```

### Client().create_cloud_formation_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L64)

```python
def create_cloud_formation_stack(instances: List[Any]) -> Dict[str, Any]:
```

### Client().create_disk

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L68)

```python
def create_disk(
    diskName: str,
    availabilityZone: str,
    sizeInGb: int,
    tags: List[Any] = None,
    addOns: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_disk_from_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L79)

```python
def create_disk_from_snapshot(
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
```

### Client().create_disk_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L94)

```python
def create_disk_snapshot(
    diskSnapshotName: str,
    diskName: str = None,
    instanceName: str = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L104)

```python
def create_domain(domainName: str, tags: List[Any] = None) -> Dict[str, Any]:
```

### Client().create_domain_entry

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L108)

```python
def create_domain_entry(
    domainName: str,
    domainEntry: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_instance_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L114)

```python
def create_instance_snapshot(
    instanceSnapshotName: str,
    instanceName: str,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L120)

```python
def create_instances(
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
```

### Client().create_instances_from_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L135)

```python
def create_instances_from_snapshot(
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
```

### Client().create_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L153)

```python
def create_key_pair(
    keyPairName: str,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L159)

```python
def create_load_balancer(
    loadBalancerName: str,
    instancePort: int,
    healthCheckPath: str = None,
    certificateName: str = None,
    certificateDomainName: str = None,
    certificateAlternativeNames: List[Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_load_balancer_tls_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L172)

```python
def create_load_balancer_tls_certificate(
    loadBalancerName: str,
    certificateName: str,
    certificateDomainName: str,
    certificateAlternativeNames: List[Any] = None,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_relational_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L183)

```python
def create_relational_database(
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
```

### Client().create_relational_database_from_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L200)

```python
def create_relational_database_from_snapshot(
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
```

### Client().create_relational_database_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L215)

```python
def create_relational_database_snapshot(
    relationalDatabaseName: str,
    relationalDatabaseSnapshotName: str,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_auto_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L224)

```python
def delete_auto_snapshot(resourceName: str, date: str) -> Dict[str, Any]:
```

### Client().delete_disk

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L228)

```python
def delete_disk(
    diskName: str,
    forceDeleteAddOns: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_disk_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L234)

```python
def delete_disk_snapshot(diskSnapshotName: str) -> Dict[str, Any]:
```

### Client().delete_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L238)

```python
def delete_domain(domainName: str) -> Dict[str, Any]:
```

### Client().delete_domain_entry

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L242)

```python
def delete_domain_entry(
    domainName: str,
    domainEntry: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L248)

```python
def delete_instance(
    instanceName: str,
    forceDeleteAddOns: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_instance_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L254)

```python
def delete_instance_snapshot(instanceSnapshotName: str) -> Dict[str, Any]:
```

### Client().delete_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L258)

```python
def delete_key_pair(keyPairName: str) -> Dict[str, Any]:
```

### Client().delete_known_host_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L262)

```python
def delete_known_host_keys(instanceName: str) -> Dict[str, Any]:
```

### Client().delete_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L266)

```python
def delete_load_balancer(loadBalancerName: str) -> Dict[str, Any]:
```

### Client().delete_load_balancer_tls_certificate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L270)

```python
def delete_load_balancer_tls_certificate(
    loadBalancerName: str,
    certificateName: str,
    force: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_relational_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L276)

```python
def delete_relational_database(
    relationalDatabaseName: str,
    skipFinalSnapshot: bool = None,
    finalRelationalDatabaseSnapshotName: str = None,
) -> Dict[str, Any]:
```

### Client().delete_relational_database_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L285)

```python
def delete_relational_database_snapshot(
    relationalDatabaseSnapshotName: str,
) -> Dict[str, Any]:
```

### Client().detach_disk

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L291)

```python
def detach_disk(diskName: str) -> Dict[str, Any]:
```

### Client().detach_instances_from_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L295)

```python
def detach_instances_from_load_balancer(
    loadBalancerName: str,
    instanceNames: List[Any],
) -> Dict[str, Any]:
```

### Client().detach_static_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L301)

```python
def detach_static_ip(staticIpName: str) -> Dict[str, Any]:
```

### Client().disable_add_on

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L305)

```python
def disable_add_on(addOnType: str, resourceName: str) -> Dict[str, Any]:
```

### Client().download_default_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L309)

```python
def download_default_key_pair() -> Dict[str, Any]:
```

### Client().enable_add_on

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L313)

```python
def enable_add_on(
    resourceName: str,
    addOnRequest: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().export_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L319)

```python
def export_snapshot(sourceSnapshotName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L323)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_active_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L333)

```python
def get_active_names(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_auto_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L337)

```python
def get_auto_snapshots(resourceName: str) -> Dict[str, Any]:
```

### Client().get_blueprints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L341)

```python
def get_blueprints(
    includeInactive: bool = None,
    pageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_bundles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L347)

```python
def get_bundles(
    includeInactive: bool = None,
    pageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_cloud_formation_stack_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L353)

```python
def get_cloud_formation_stack_records(
    pageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_disk

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L359)

```python
def get_disk(diskName: str) -> Dict[str, Any]:
```

### Client().get_disk_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L363)

```python
def get_disk_snapshot(diskSnapshotName: str) -> Dict[str, Any]:
```

### Client().get_disk_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L367)

```python
def get_disk_snapshots(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_disks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L371)

```python
def get_disks(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L375)

```python
def get_domain(domainName: str) -> Dict[str, Any]:
```

### Client().get_domains

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L379)

```python
def get_domains(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_export_snapshot_records

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L383)

```python
def get_export_snapshot_records(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L387)

```python
def get_instance(instanceName: str) -> Dict[str, Any]:
```

### Client().get_instance_access_details

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L391)

```python
def get_instance_access_details(
    instanceName: str,
    protocol: str = None,
) -> Dict[str, Any]:
```

### Client().get_instance_metric_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L397)

```python
def get_instance_metric_data(
    instanceName: str,
    metricName: str,
    period: int,
    startTime: datetime,
    endTime: datetime,
    unit: str,
    statistics: List[Any],
) -> Dict[str, Any]:
```

### Client().get_instance_port_states

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L410)

```python
def get_instance_port_states(instanceName: str) -> Dict[str, Any]:
```

### Client().get_instance_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L414)

```python
def get_instance_snapshot(instanceSnapshotName: str) -> Dict[str, Any]:
```

### Client().get_instance_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L418)

```python
def get_instance_snapshots(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_instance_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L422)

```python
def get_instance_state(instanceName: str) -> Dict[str, Any]:
```

### Client().get_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L426)

```python
def get_instances(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L430)

```python
def get_key_pair(keyPairName: str) -> Dict[str, Any]:
```

### Client().get_key_pairs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L434)

```python
def get_key_pairs(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_load_balancer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L438)

```python
def get_load_balancer(loadBalancerName: str) -> Dict[str, Any]:
```

### Client().get_load_balancer_metric_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L442)

```python
def get_load_balancer_metric_data(
    loadBalancerName: str,
    metricName: str,
    period: int,
    startTime: datetime,
    endTime: datetime,
    unit: str,
    statistics: List[Any],
) -> Dict[str, Any]:
```

### Client().get_load_balancer_tls_certificates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L455)

```python
def get_load_balancer_tls_certificates(
    loadBalancerName: str,
) -> Dict[str, Any]:
```

### Client().get_load_balancers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L461)

```python
def get_load_balancers(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_operation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L465)

```python
def get_operation(operationId: str) -> Dict[str, Any]:
```

### Client().get_operations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L469)

```python
def get_operations(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_operations_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L473)

```python
def get_operations_for_resource(
    resourceName: str,
    pageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L479)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_regions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L483)

```python
def get_regions(
    includeAvailabilityZones: bool = None,
    includeRelationalDatabaseAvailabilityZones: bool = None,
) -> Dict[str, Any]:
```

### Client().get_relational_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L491)

```python
def get_relational_database(relationalDatabaseName: str) -> Dict[str, Any]:
```

### Client().get_relational_database_blueprints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L495)

```python
def get_relational_database_blueprints(
    pageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_relational_database_bundles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L501)

```python
def get_relational_database_bundles(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_relational_database_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L505)

```python
def get_relational_database_events(
    relationalDatabaseName: str,
    durationInMinutes: int = None,
    pageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_relational_database_log_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L514)

```python
def get_relational_database_log_events(
    relationalDatabaseName: str,
    logStreamName: str,
    startTime: datetime = None,
    endTime: datetime = None,
    startFromHead: bool = None,
    pageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_relational_database_log_streams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L526)

```python
def get_relational_database_log_streams(
    relationalDatabaseName: str,
) -> Dict[str, Any]:
```

### Client().get_relational_database_master_user_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L532)

```python
def get_relational_database_master_user_password(
    relationalDatabaseName: str,
    passwordVersion: str = None,
) -> Dict[str, Any]:
```

### Client().get_relational_database_metric_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L538)

```python
def get_relational_database_metric_data(
    relationalDatabaseName: str,
    metricName: str,
    period: int,
    startTime: datetime,
    endTime: datetime,
    unit: str,
    statistics: List[Any],
) -> Dict[str, Any]:
```

### Client().get_relational_database_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L551)

```python
def get_relational_database_parameters(
    relationalDatabaseName: str,
    pageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_relational_database_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L557)

```python
def get_relational_database_snapshot(
    relationalDatabaseSnapshotName: str,
) -> Dict[str, Any]:
```

### Client().get_relational_database_snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L563)

```python
def get_relational_database_snapshots(
    pageToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_relational_databases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L569)

```python
def get_relational_databases(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_static_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L573)

```python
def get_static_ip(staticIpName: str) -> Dict[str, Any]:
```

### Client().get_static_ips

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L577)

```python
def get_static_ips(pageToken: str = None) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L581)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L585)

```python
def import_key_pair(keyPairName: str, publicKeyBase64: str) -> Dict[str, Any]:
```

### Client().is_vpc_peered

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L589)

```python
def is_vpc_peered() -> Dict[str, Any]:
```

### Client().open_instance_public_ports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L593)

```python
def open_instance_public_ports(
    portInfo: Dict[str, Any],
    instanceName: str,
) -> Dict[str, Any]:
```

### Client().peer_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L599)

```python
def peer_vpc() -> Dict[str, Any]:
```

### Client().put_instance_public_ports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L603)

```python
def put_instance_public_ports(
    portInfos: List[Any],
    instanceName: str,
) -> Dict[str, Any]:
```

### Client().reboot_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L609)

```python
def reboot_instance(instanceName: str) -> Dict[str, Any]:
```

### Client().reboot_relational_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L613)

```python
def reboot_relational_database(relationalDatabaseName: str) -> Dict[str, Any]:
```

### Client().release_static_ip

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L617)

```python
def release_static_ip(staticIpName: str) -> Dict[str, Any]:
```

### Client().start_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L621)

```python
def start_instance(instanceName: str) -> Dict[str, Any]:
```

### Client().start_relational_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L625)

```python
def start_relational_database(relationalDatabaseName: str) -> Dict[str, Any]:
```

### Client().stop_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L629)

```python
def stop_instance(instanceName: str, force: bool = None) -> Dict[str, Any]:
```

### Client().stop_relational_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L633)

```python
def stop_relational_database(
    relationalDatabaseName: str,
    relationalDatabaseSnapshotName: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L639)

```python
def tag_resource(
    resourceName: str,
    tags: List[Any],
    resourceArn: str = None,
) -> Dict[str, Any]:
```

### Client().unpeer_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L645)

```python
def unpeer_vpc() -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L649)

```python
def untag_resource(
    resourceName: str,
    tagKeys: List[Any],
    resourceArn: str = None,
) -> Dict[str, Any]:
```

### Client().update_domain_entry

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L655)

```python
def update_domain_entry(
    domainName: str,
    domainEntry: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_load_balancer_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L661)

```python
def update_load_balancer_attribute(
    loadBalancerName: str,
    attributeName: str,
    attributeValue: str,
) -> Dict[str, Any]:
```

### Client().update_relational_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L667)

```python
def update_relational_database(
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
```

### Client().update_relational_database_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lightsail/client.py#L682)

```python
def update_relational_database_parameters(
    relationalDatabaseName: str,
    parameters: List[Any],
) -> Dict[str, Any]:
```
