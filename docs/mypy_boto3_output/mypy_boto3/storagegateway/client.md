# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.storagegateway.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Storagegateway](index.md#storagegateway) / Client
    - [Client](#client)
        - [Client().activate_gateway](#clientactivate_gateway)
        - [Client().add_cache](#clientadd_cache)
        - [Client().add_tags_to_resource](#clientadd_tags_to_resource)
        - [Client().add_upload_buffer](#clientadd_upload_buffer)
        - [Client().add_working_storage](#clientadd_working_storage)
        - [Client().assign_tape_pool](#clientassign_tape_pool)
        - [Client().attach_volume](#clientattach_volume)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_archival](#clientcancel_archival)
        - [Client().cancel_retrieval](#clientcancel_retrieval)
        - [Client().create_cached_iscsi_volume](#clientcreate_cached_iscsi_volume)
        - [Client().create_nfs_file_share](#clientcreate_nfs_file_share)
        - [Client().create_smb_file_share](#clientcreate_smb_file_share)
        - [Client().create_snapshot](#clientcreate_snapshot)
        - [Client().create_snapshot_from_volume_recovery_point](#clientcreate_snapshot_from_volume_recovery_point)
        - [Client().create_stored_iscsi_volume](#clientcreate_stored_iscsi_volume)
        - [Client().create_tape_with_barcode](#clientcreate_tape_with_barcode)
        - [Client().create_tapes](#clientcreate_tapes)
        - [Client().delete_bandwidth_rate_limit](#clientdelete_bandwidth_rate_limit)
        - [Client().delete_chap_credentials](#clientdelete_chap_credentials)
        - [Client().delete_file_share](#clientdelete_file_share)
        - [Client().delete_gateway](#clientdelete_gateway)
        - [Client().delete_snapshot_schedule](#clientdelete_snapshot_schedule)
        - [Client().delete_tape](#clientdelete_tape)
        - [Client().delete_tape_archive](#clientdelete_tape_archive)
        - [Client().delete_volume](#clientdelete_volume)
        - [Client().describe_bandwidth_rate_limit](#clientdescribe_bandwidth_rate_limit)
        - [Client().describe_cache](#clientdescribe_cache)
        - [Client().describe_cached_iscsi_volumes](#clientdescribe_cached_iscsi_volumes)
        - [Client().describe_chap_credentials](#clientdescribe_chap_credentials)
        - [Client().describe_gateway_information](#clientdescribe_gateway_information)
        - [Client().describe_maintenance_start_time](#clientdescribe_maintenance_start_time)
        - [Client().describe_nfs_file_shares](#clientdescribe_nfs_file_shares)
        - [Client().describe_smb_file_shares](#clientdescribe_smb_file_shares)
        - [Client().describe_smb_settings](#clientdescribe_smb_settings)
        - [Client().describe_snapshot_schedule](#clientdescribe_snapshot_schedule)
        - [Client().describe_stored_iscsi_volumes](#clientdescribe_stored_iscsi_volumes)
        - [Client().describe_tape_archives](#clientdescribe_tape_archives)
        - [Client().describe_tape_recovery_points](#clientdescribe_tape_recovery_points)
        - [Client().describe_tapes](#clientdescribe_tapes)
        - [Client().describe_upload_buffer](#clientdescribe_upload_buffer)
        - [Client().describe_vtl_devices](#clientdescribe_vtl_devices)
        - [Client().describe_working_storage](#clientdescribe_working_storage)
        - [Client().detach_volume](#clientdetach_volume)
        - [Client().disable_gateway](#clientdisable_gateway)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().join_domain](#clientjoin_domain)
        - [Client().list_file_shares](#clientlist_file_shares)
        - [Client().list_gateways](#clientlist_gateways)
        - [Client().list_local_disks](#clientlist_local_disks)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_tapes](#clientlist_tapes)
        - [Client().list_volume_initiators](#clientlist_volume_initiators)
        - [Client().list_volume_recovery_points](#clientlist_volume_recovery_points)
        - [Client().list_volumes](#clientlist_volumes)
        - [Client().notify_when_uploaded](#clientnotify_when_uploaded)
        - [Client().refresh_cache](#clientrefresh_cache)
        - [Client().remove_tags_from_resource](#clientremove_tags_from_resource)
        - [Client().reset_cache](#clientreset_cache)
        - [Client().retrieve_tape_archive](#clientretrieve_tape_archive)
        - [Client().retrieve_tape_recovery_point](#clientretrieve_tape_recovery_point)
        - [Client().set_local_console_password](#clientset_local_console_password)
        - [Client().set_smb_guest_password](#clientset_smb_guest_password)
        - [Client().shutdown_gateway](#clientshutdown_gateway)
        - [Client().start_gateway](#clientstart_gateway)
        - [Client().update_bandwidth_rate_limit](#clientupdate_bandwidth_rate_limit)
        - [Client().update_chap_credentials](#clientupdate_chap_credentials)
        - [Client().update_gateway_information](#clientupdate_gateway_information)
        - [Client().update_gateway_software_now](#clientupdate_gateway_software_now)
        - [Client().update_maintenance_start_time](#clientupdate_maintenance_start_time)
        - [Client().update_nfs_file_share](#clientupdate_nfs_file_share)
        - [Client().update_smb_file_share](#clientupdate_smb_file_share)
        - [Client().update_smb_security_strategy](#clientupdate_smb_security_strategy)
        - [Client().update_snapshot_schedule](#clientupdate_snapshot_schedule)
        - [Client().update_vtl_device_type](#clientupdate_vtl_device_type)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L12)

```python
class Client(BaseClient):
```

### Client().activate_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L15)

```python
def activate_gateway(
    ActivationKey: str,
    GatewayName: str,
    GatewayTimezone: str,
    GatewayRegion: str,
    GatewayType: str = None,
    TapeDriveType: str = None,
    MediumChangerType: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().add_cache

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L29)

```python
def add_cache(GatewayARN: str, DiskIds: List[Any]) -> Dict[str, Any]:
```

### Client().add_tags_to_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L33)

```python
def add_tags_to_resource(ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().add_upload_buffer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L37)

```python
def add_upload_buffer(GatewayARN: str, DiskIds: List[Any]) -> Dict[str, Any]:
```

### Client().add_working_storage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L41)

```python
def add_working_storage(
    GatewayARN: str,
    DiskIds: List[Any],
) -> Dict[str, Any]:
```

### Client().assign_tape_pool

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L47)

```python
def assign_tape_pool(TapeARN: str, PoolId: str) -> Dict[str, Any]:
```

### Client().attach_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L51)

```python
def attach_volume(
    GatewayARN: str,
    VolumeARN: str,
    NetworkInterfaceId: str,
    TargetName: str = None,
    DiskId: str = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L62)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_archival

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L66)

```python
def cancel_archival(GatewayARN: str, TapeARN: str) -> Dict[str, Any]:
```

### Client().cancel_retrieval

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L70)

```python
def cancel_retrieval(GatewayARN: str, TapeARN: str) -> Dict[str, Any]:
```

### Client().create_cached_iscsi_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L74)

```python
def create_cached_iscsi_volume(
    GatewayARN: str,
    VolumeSizeInBytes: int,
    TargetName: str,
    NetworkInterfaceId: str,
    ClientToken: str,
    SnapshotId: str = None,
    SourceVolumeARN: str = None,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_nfs_file_share

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L90)

```python
def create_nfs_file_share(
    ClientToken: str,
    GatewayARN: str,
    Role: str,
    LocationARN: str,
    NFSFileShareDefaults: Dict[str, Any] = None,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    DefaultStorageClass: str = None,
    ObjectACL: str = None,
    ClientList: List[Any] = None,
    Squash: str = None,
    ReadOnly: bool = None,
    GuessMIMETypeEnabled: bool = None,
    RequesterPays: bool = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_smb_file_share

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L111)

```python
def create_smb_file_share(
    ClientToken: str,
    GatewayARN: str,
    Role: str,
    LocationARN: str,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    DefaultStorageClass: str = None,
    ObjectACL: str = None,
    ReadOnly: bool = None,
    GuessMIMETypeEnabled: bool = None,
    RequesterPays: bool = None,
    SMBACLEnabled: bool = None,
    AdminUserList: List[Any] = None,
    ValidUserList: List[Any] = None,
    InvalidUserList: List[Any] = None,
    Authentication: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L134)

```python
def create_snapshot(
    VolumeARN: str,
    SnapshotDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_snapshot_from_volume_recovery_point

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L140)

```python
def create_snapshot_from_volume_recovery_point(
    VolumeARN: str,
    SnapshotDescription: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_stored_iscsi_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L146)

```python
def create_stored_iscsi_volume(
    GatewayARN: str,
    DiskId: str,
    PreserveExistingData: bool,
    TargetName: str,
    NetworkInterfaceId: str,
    SnapshotId: str = None,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_tape_with_barcode

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L161)

```python
def create_tape_with_barcode(
    GatewayARN: str,
    TapeSizeInBytes: int,
    TapeBarcode: str,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    PoolId: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_tapes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L174)

```python
def create_tapes(
    GatewayARN: str,
    TapeSizeInBytes: int,
    ClientToken: str,
    NumTapesToCreate: int,
    TapeBarcodePrefix: str,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    PoolId: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_bandwidth_rate_limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L189)

```python
def delete_bandwidth_rate_limit(
    GatewayARN: str,
    BandwidthType: str,
) -> Dict[str, Any]:
```

### Client().delete_chap_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L195)

```python
def delete_chap_credentials(
    TargetARN: str,
    InitiatorName: str,
) -> Dict[str, Any]:
```

### Client().delete_file_share

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L201)

```python
def delete_file_share(
    FileShareARN: str,
    ForceDelete: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L207)

```python
def delete_gateway(GatewayARN: str) -> Dict[str, Any]:
```

### Client().delete_snapshot_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L211)

```python
def delete_snapshot_schedule(VolumeARN: str) -> Dict[str, Any]:
```

### Client().delete_tape

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L215)

```python
def delete_tape(GatewayARN: str, TapeARN: str) -> Dict[str, Any]:
```

### Client().delete_tape_archive

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L219)

```python
def delete_tape_archive(TapeARN: str) -> Dict[str, Any]:
```

### Client().delete_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L223)

```python
def delete_volume(VolumeARN: str) -> Dict[str, Any]:
```

### Client().describe_bandwidth_rate_limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L227)

```python
def describe_bandwidth_rate_limit(GatewayARN: str) -> Dict[str, Any]:
```

### Client().describe_cache

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L231)

```python
def describe_cache(GatewayARN: str) -> Dict[str, Any]:
```

### Client().describe_cached_iscsi_volumes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L235)

```python
def describe_cached_iscsi_volumes(VolumeARNs: List[Any]) -> Dict[str, Any]:
```

### Client().describe_chap_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L239)

```python
def describe_chap_credentials(TargetARN: str) -> Dict[str, Any]:
```

### Client().describe_gateway_information

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L243)

```python
def describe_gateway_information(GatewayARN: str) -> Dict[str, Any]:
```

### Client().describe_maintenance_start_time

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L247)

```python
def describe_maintenance_start_time(GatewayARN: str) -> Dict[str, Any]:
```

### Client().describe_nfs_file_shares

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L251)

```python
def describe_nfs_file_shares(FileShareARNList: List[Any]) -> Dict[str, Any]:
```

### Client().describe_smb_file_shares

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L255)

```python
def describe_smb_file_shares(FileShareARNList: List[Any]) -> Dict[str, Any]:
```

### Client().describe_smb_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L259)

```python
def describe_smb_settings(GatewayARN: str) -> Dict[str, Any]:
```

### Client().describe_snapshot_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L263)

```python
def describe_snapshot_schedule(VolumeARN: str) -> Dict[str, Any]:
```

### Client().describe_stored_iscsi_volumes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L267)

```python
def describe_stored_iscsi_volumes(VolumeARNs: List[Any]) -> Dict[str, Any]:
```

### Client().describe_tape_archives

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L271)

```python
def describe_tape_archives(
    TapeARNs: List[Any] = None,
    Marker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_tape_recovery_points

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L277)

```python
def describe_tape_recovery_points(
    GatewayARN: str,
    Marker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_tapes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L283)

```python
def describe_tapes(
    GatewayARN: str,
    TapeARNs: List[Any] = None,
    Marker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_upload_buffer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L293)

```python
def describe_upload_buffer(GatewayARN: str) -> Dict[str, Any]:
```

### Client().describe_vtl_devices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L297)

```python
def describe_vtl_devices(
    GatewayARN: str,
    VTLDeviceARNs: List[Any] = None,
    Marker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_working_storage

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L307)

```python
def describe_working_storage(GatewayARN: str) -> Dict[str, Any]:
```

### Client().detach_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L311)

```python
def detach_volume(VolumeARN: str, ForceDetach: bool = None) -> Dict[str, Any]:
```

### Client().disable_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L315)

```python
def disable_gateway(GatewayARN: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L319)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L329)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L333)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().join_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L337)

```python
def join_domain(
    GatewayARN: str,
    DomainName: str,
    UserName: str,
    Password: str,
    OrganizationalUnit: str = None,
    DomainControllers: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_file_shares

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L349)

```python
def list_file_shares(
    GatewayARN: str = None,
    Limit: int = None,
    Marker: str = None,
) -> Dict[str, Any]:
```

### Client().list_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L355)

```python
def list_gateways(Marker: str = None, Limit: int = None) -> Dict[str, Any]:
```

### Client().list_local_disks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L359)

```python
def list_local_disks(GatewayARN: str) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L363)

```python
def list_tags_for_resource(
    ResourceARN: str,
    Marker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_tapes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L369)

```python
def list_tapes(
    TapeARNs: List[Any] = None,
    Marker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().list_volume_initiators

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L375)

```python
def list_volume_initiators(VolumeARN: str) -> Dict[str, Any]:
```

### Client().list_volume_recovery_points

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L379)

```python
def list_volume_recovery_points(GatewayARN: str) -> Dict[str, Any]:
```

### Client().list_volumes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L383)

```python
def list_volumes(
    GatewayARN: str = None,
    Marker: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().notify_when_uploaded

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L389)

```python
def notify_when_uploaded(FileShareARN: str) -> Dict[str, Any]:
```

### Client().refresh_cache

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L393)

```python
def refresh_cache(
    FileShareARN: str,
    FolderList: List[Any] = None,
    Recursive: bool = None,
) -> Dict[str, Any]:
```

### Client().remove_tags_from_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L399)

```python
def remove_tags_from_resource(
    ResourceARN: str,
    TagKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().reset_cache

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L405)

```python
def reset_cache(GatewayARN: str) -> Dict[str, Any]:
```

### Client().retrieve_tape_archive

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L409)

```python
def retrieve_tape_archive(TapeARN: str, GatewayARN: str) -> Dict[str, Any]:
```

### Client().retrieve_tape_recovery_point

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L413)

```python
def retrieve_tape_recovery_point(
    TapeARN: str,
    GatewayARN: str,
) -> Dict[str, Any]:
```

### Client().set_local_console_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L419)

```python
def set_local_console_password(
    GatewayARN: str,
    LocalConsolePassword: str,
) -> Dict[str, Any]:
```

### Client().set_smb_guest_password

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L425)

```python
def set_smb_guest_password(GatewayARN: str, Password: str) -> Dict[str, Any]:
```

### Client().shutdown_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L429)

```python
def shutdown_gateway(GatewayARN: str) -> Dict[str, Any]:
```

### Client().start_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L433)

```python
def start_gateway(GatewayARN: str) -> Dict[str, Any]:
```

### Client().update_bandwidth_rate_limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L437)

```python
def update_bandwidth_rate_limit(
    GatewayARN: str,
    AverageUploadRateLimitInBitsPerSec: int = None,
    AverageDownloadRateLimitInBitsPerSec: int = None,
) -> Dict[str, Any]:
```

### Client().update_chap_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L446)

```python
def update_chap_credentials(
    TargetARN: str,
    SecretToAuthenticateInitiator: str,
    InitiatorName: str,
    SecretToAuthenticateTarget: str = None,
) -> Dict[str, Any]:
```

### Client().update_gateway_information

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L456)

```python
def update_gateway_information(
    GatewayARN: str,
    GatewayName: str = None,
    GatewayTimezone: str = None,
    CloudWatchLogGroupARN: str = None,
) -> Dict[str, Any]:
```

### Client().update_gateway_software_now

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L466)

```python
def update_gateway_software_now(GatewayARN: str) -> Dict[str, Any]:
```

### Client().update_maintenance_start_time

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L470)

```python
def update_maintenance_start_time(
    GatewayARN: str,
    HourOfDay: int,
    MinuteOfHour: int,
    DayOfWeek: int = None,
    DayOfMonth: int = None,
) -> Dict[str, Any]:
```

### Client().update_nfs_file_share

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L481)

```python
def update_nfs_file_share(
    FileShareARN: str,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    NFSFileShareDefaults: Dict[str, Any] = None,
    DefaultStorageClass: str = None,
    ObjectACL: str = None,
    ClientList: List[Any] = None,
    Squash: str = None,
    ReadOnly: bool = None,
    GuessMIMETypeEnabled: bool = None,
    RequesterPays: bool = None,
) -> Dict[str, Any]:
```

### Client().update_smb_file_share

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L498)

```python
def update_smb_file_share(
    FileShareARN: str,
    KMSEncrypted: bool = None,
    KMSKey: str = None,
    DefaultStorageClass: str = None,
    ObjectACL: str = None,
    ReadOnly: bool = None,
    GuessMIMETypeEnabled: bool = None,
    RequesterPays: bool = None,
    SMBACLEnabled: bool = None,
    AdminUserList: List[Any] = None,
    ValidUserList: List[Any] = None,
    InvalidUserList: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_smb_security_strategy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L516)

```python
def update_smb_security_strategy(
    GatewayARN: str,
    SMBSecurityStrategy: str,
) -> Dict[str, Any]:
```

### Client().update_snapshot_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L522)

```python
def update_snapshot_schedule(
    VolumeARN: str,
    StartAt: int,
    RecurrenceInHours: int,
    Description: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_vtl_device_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/storagegateway/client.py#L533)

```python
def update_vtl_device_type(
    VTLDeviceARN: str,
    DeviceType: str,
) -> Dict[str, Any]:
```
