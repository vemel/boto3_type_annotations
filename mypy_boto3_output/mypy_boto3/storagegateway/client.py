from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def activate_gateway(
        self,
        ActivationKey: str,
        GatewayName: str,
        GatewayTimezone: str,
        GatewayRegion: str,
        GatewayType: str = None,
        TapeDriveType: str = None,
        MediumChangerType: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_cache(self, GatewayARN: str, DiskIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_tags_to_resource(self, ResourceARN: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_upload_buffer(self, GatewayARN: str, DiskIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_working_storage(
        self, GatewayARN: str, DiskIds: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def assign_tape_pool(self, TapeARN: str, PoolId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_volume(
        self,
        GatewayARN: str,
        VolumeARN: str,
        NetworkInterfaceId: str,
        TargetName: str = None,
        DiskId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_archival(self, GatewayARN: str, TapeARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def cancel_retrieval(self, GatewayARN: str, TapeARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cached_iscsi_volume(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_nfs_file_share(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_smb_file_share(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_snapshot(
        self, VolumeARN: str, SnapshotDescription: str, Tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_snapshot_from_volume_recovery_point(
        self, VolumeARN: str, SnapshotDescription: str, Tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_stored_iscsi_volume(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_tape_with_barcode(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        TapeBarcode: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_tapes(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def delete_bandwidth_rate_limit(
        self, GatewayARN: str, BandwidthType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_chap_credentials(
        self, TargetARN: str, InitiatorName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_file_share(
        self, FileShareARN: str, ForceDelete: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_gateway(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_snapshot_schedule(self, VolumeARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_tape(self, GatewayARN: str, TapeARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_tape_archive(self, TapeARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_volume(self, VolumeARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_bandwidth_rate_limit(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cache(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cached_iscsi_volumes(self, VolumeARNs: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_chap_credentials(self, TargetARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_gateway_information(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_maintenance_start_time(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_nfs_file_shares(self, FileShareARNList: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_smb_file_shares(self, FileShareARNList: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_smb_settings(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_snapshot_schedule(self, VolumeARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stored_iscsi_volumes(self, VolumeARNs: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_tape_archives(
        self, TapeARNs: List[Any] = None, Marker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_tape_recovery_points(
        self, GatewayARN: str, Marker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_tapes(
        self,
        GatewayARN: str,
        TapeARNs: List[Any] = None,
        Marker: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_upload_buffer(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_vtl_devices(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[Any] = None,
        Marker: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_working_storage(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_volume(self, VolumeARN: str, ForceDetach: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_gateway(self, GatewayARN: str) -> Dict[str, Any]:
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
    def join_domain(
        self,
        GatewayARN: str,
        DomainName: str,
        UserName: str,
        Password: str,
        OrganizationalUnit: str = None,
        DomainControllers: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_file_shares(
        self, GatewayARN: str = None, Limit: int = None, Marker: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_gateways(self, Marker: str = None, Limit: int = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_local_disks(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, ResourceARN: str, Marker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tapes(
        self, TapeARNs: List[Any] = None, Marker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_volume_initiators(self, VolumeARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_volume_recovery_points(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_volumes(
        self, GatewayARN: str = None, Marker: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def notify_when_uploaded(self, FileShareARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def refresh_cache(
        self, FileShareARN: str, FolderList: List[Any] = None, Recursive: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags_from_resource(
        self, ResourceARN: str, TagKeys: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reset_cache(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def retrieve_tape_archive(self, TapeARN: str, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def retrieve_tape_recovery_point(
        self, TapeARN: str, GatewayARN: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_local_console_password(
        self, GatewayARN: str, LocalConsolePassword: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_smb_guest_password(self, GatewayARN: str, Password: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def shutdown_gateway(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_gateway(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_bandwidth_rate_limit(
        self,
        GatewayARN: str,
        AverageUploadRateLimitInBitsPerSec: int = None,
        AverageDownloadRateLimitInBitsPerSec: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_chap_credentials(
        self,
        TargetARN: str,
        SecretToAuthenticateInitiator: str,
        InitiatorName: str,
        SecretToAuthenticateTarget: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_gateway_information(
        self,
        GatewayARN: str,
        GatewayName: str = None,
        GatewayTimezone: str = None,
        CloudWatchLogGroupARN: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_gateway_software_now(self, GatewayARN: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_maintenance_start_time(
        self,
        GatewayARN: str,
        HourOfDay: int,
        MinuteOfHour: int,
        DayOfWeek: int = None,
        DayOfMonth: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_nfs_file_share(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def update_smb_file_share(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def update_smb_security_strategy(
        self, GatewayARN: str, SMBSecurityStrategy: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_snapshot_schedule(
        self,
        VolumeARN: str,
        StartAt: int,
        RecurrenceInHours: int,
        Description: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_vtl_device_type(
        self, VTLDeviceARN: str, DeviceType: str
    ) -> Dict[str, Any]:
        pass
