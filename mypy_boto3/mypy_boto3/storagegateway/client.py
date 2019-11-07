from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def activate_gateway(
        self,
        ActivationKey: str,
        GatewayName: str,
        GatewayTimezone: str,
        GatewayRegion: str,
        GatewayType: Optional[str] = None,
        TapeDriveType: Optional[str] = None,
        MediumChangerType: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def add_cache(
        self,
        GatewayARN: str,
        DiskIds: List,
    ) -> Dict:
        pass


    def add_tags_to_resource(
        self,
        ResourceARN: str,
        Tags: List,
    ) -> Dict:
        pass


    def add_upload_buffer(
        self,
        GatewayARN: str,
        DiskIds: List,
    ) -> Dict:
        pass


    def add_working_storage(
        self,
        GatewayARN: str,
        DiskIds: List,
    ) -> Dict:
        pass


    def assign_tape_pool(
        self,
        TapeARN: str,
        PoolId: str,
    ) -> Dict:
        pass


    def attach_volume(
        self,
        GatewayARN: str,
        VolumeARN: str,
        NetworkInterfaceId: str,
        TargetName: Optional[str] = None,
        DiskId: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_archival(
        self,
        GatewayARN: str,
        TapeARN: str,
    ) -> Dict:
        pass


    def cancel_retrieval(
        self,
        GatewayARN: str,
        TapeARN: str,
    ) -> Dict:
        pass


    def create_cached_iscsi_volume(
        self,
        GatewayARN: str,
        VolumeSizeInBytes: int,
        TargetName: str,
        NetworkInterfaceId: str,
        ClientToken: str,
        SnapshotId: Optional[str] = None,
        SourceVolumeARN: Optional[str] = None,
        KMSEncrypted: Optional[bool] = None,
        KMSKey: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_nfs_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        NFSFileShareDefaults: Optional[Dict] = None,
        KMSEncrypted: Optional[bool] = None,
        KMSKey: Optional[str] = None,
        DefaultStorageClass: Optional[str] = None,
        ObjectACL: Optional[str] = None,
        ClientList: Optional[List] = None,
        Squash: Optional[str] = None,
        ReadOnly: Optional[bool] = None,
        GuessMIMETypeEnabled: Optional[bool] = None,
        RequesterPays: Optional[bool] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_smb_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        KMSEncrypted: Optional[bool] = None,
        KMSKey: Optional[str] = None,
        DefaultStorageClass: Optional[str] = None,
        ObjectACL: Optional[str] = None,
        ReadOnly: Optional[bool] = None,
        GuessMIMETypeEnabled: Optional[bool] = None,
        RequesterPays: Optional[bool] = None,
        SMBACLEnabled: Optional[bool] = None,
        AdminUserList: Optional[List] = None,
        ValidUserList: Optional[List] = None,
        InvalidUserList: Optional[List] = None,
        Authentication: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_snapshot(
        self,
        VolumeARN: str,
        SnapshotDescription: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_snapshot_from_volume_recovery_point(
        self,
        VolumeARN: str,
        SnapshotDescription: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_stored_iscsi_volume(
        self,
        GatewayARN: str,
        DiskId: str,
        PreserveExistingData: bool,
        TargetName: str,
        NetworkInterfaceId: str,
        SnapshotId: Optional[str] = None,
        KMSEncrypted: Optional[bool] = None,
        KMSKey: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_tape_with_barcode(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        TapeBarcode: str,
        KMSEncrypted: Optional[bool] = None,
        KMSKey: Optional[str] = None,
        PoolId: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_tapes(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        ClientToken: str,
        NumTapesToCreate: int,
        TapeBarcodePrefix: str,
        KMSEncrypted: Optional[bool] = None,
        KMSKey: Optional[str] = None,
        PoolId: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_bandwidth_rate_limit(
        self,
        GatewayARN: str,
        BandwidthType: str,
    ) -> Dict:
        pass


    def delete_chap_credentials(
        self,
        TargetARN: str,
        InitiatorName: str,
    ) -> Dict:
        pass


    def delete_file_share(
        self,
        FileShareARN: str,
        ForceDelete: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_gateway(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def delete_snapshot_schedule(
        self,
        VolumeARN: str,
    ) -> Dict:
        pass


    def delete_tape(
        self,
        GatewayARN: str,
        TapeARN: str,
    ) -> Dict:
        pass


    def delete_tape_archive(
        self,
        TapeARN: str,
    ) -> Dict:
        pass


    def delete_volume(
        self,
        VolumeARN: str,
    ) -> Dict:
        pass


    def describe_bandwidth_rate_limit(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def describe_cache(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def describe_cached_iscsi_volumes(
        self,
        VolumeARNs: List,
    ) -> Dict:
        pass


    def describe_chap_credentials(
        self,
        TargetARN: str,
    ) -> Dict:
        pass


    def describe_gateway_information(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def describe_maintenance_start_time(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def describe_nfs_file_shares(
        self,
        FileShareARNList: List,
    ) -> Dict:
        pass


    def describe_smb_file_shares(
        self,
        FileShareARNList: List,
    ) -> Dict:
        pass


    def describe_smb_settings(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def describe_snapshot_schedule(
        self,
        VolumeARN: str,
    ) -> Dict:
        pass


    def describe_stored_iscsi_volumes(
        self,
        VolumeARNs: List,
    ) -> Dict:
        pass


    def describe_tape_archives(
        self,
        TapeARNs: Optional[List] = None,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_tape_recovery_points(
        self,
        GatewayARN: str,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_tapes(
        self,
        GatewayARN: str,
        TapeARNs: Optional[List] = None,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_upload_buffer(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def describe_vtl_devices(
        self,
        GatewayARN: str,
        VTLDeviceARNs: Optional[List] = None,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_working_storage(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def detach_volume(
        self,
        VolumeARN: str,
        ForceDetach: Optional[bool] = None,
    ) -> Dict:
        pass


    def disable_gateway(
        self,
        GatewayARN: str,
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


    def join_domain(
        self,
        GatewayARN: str,
        DomainName: str,
        UserName: str,
        Password: str,
        OrganizationalUnit: Optional[str] = None,
        DomainControllers: Optional[List] = None,
    ) -> Dict:
        pass


    def list_file_shares(
        self,
        GatewayARN: Optional[str] = None,
        Limit: Optional[int] = None,
        Marker: Optional[str] = None,
    ) -> Dict:
        pass


    def list_gateways(
        self,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_local_disks(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceARN: str,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tapes(
        self,
        TapeARNs: Optional[List] = None,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_volume_initiators(
        self,
        VolumeARN: str,
    ) -> Dict:
        pass


    def list_volume_recovery_points(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def list_volumes(
        self,
        GatewayARN: Optional[str] = None,
        Marker: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def notify_when_uploaded(
        self,
        FileShareARN: str,
    ) -> Dict:
        pass


    def refresh_cache(
        self,
        FileShareARN: str,
        FolderList: Optional[List] = None,
        Recursive: Optional[bool] = None,
    ) -> Dict:
        pass


    def remove_tags_from_resource(
        self,
        ResourceARN: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def reset_cache(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def retrieve_tape_archive(
        self,
        TapeARN: str,
        GatewayARN: str,
    ) -> Dict:
        pass


    def retrieve_tape_recovery_point(
        self,
        TapeARN: str,
        GatewayARN: str,
    ) -> Dict:
        pass


    def set_local_console_password(
        self,
        GatewayARN: str,
        LocalConsolePassword: str,
    ) -> Dict:
        pass


    def set_smb_guest_password(
        self,
        GatewayARN: str,
        Password: str,
    ) -> Dict:
        pass


    def shutdown_gateway(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def start_gateway(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def update_bandwidth_rate_limit(
        self,
        GatewayARN: str,
        AverageUploadRateLimitInBitsPerSec: Optional[int] = None,
        AverageDownloadRateLimitInBitsPerSec: Optional[int] = None,
    ) -> Dict:
        pass


    def update_chap_credentials(
        self,
        TargetARN: str,
        SecretToAuthenticateInitiator: str,
        InitiatorName: str,
        SecretToAuthenticateTarget: Optional[str] = None,
    ) -> Dict:
        pass


    def update_gateway_information(
        self,
        GatewayARN: str,
        GatewayName: Optional[str] = None,
        GatewayTimezone: Optional[str] = None,
        CloudWatchLogGroupARN: Optional[str] = None,
    ) -> Dict:
        pass


    def update_gateway_software_now(
        self,
        GatewayARN: str,
    ) -> Dict:
        pass


    def update_maintenance_start_time(
        self,
        GatewayARN: str,
        HourOfDay: int,
        MinuteOfHour: int,
        DayOfWeek: Optional[int] = None,
        DayOfMonth: Optional[int] = None,
    ) -> Dict:
        pass


    def update_nfs_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: Optional[bool] = None,
        KMSKey: Optional[str] = None,
        NFSFileShareDefaults: Optional[Dict] = None,
        DefaultStorageClass: Optional[str] = None,
        ObjectACL: Optional[str] = None,
        ClientList: Optional[List] = None,
        Squash: Optional[str] = None,
        ReadOnly: Optional[bool] = None,
        GuessMIMETypeEnabled: Optional[bool] = None,
        RequesterPays: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_smb_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: Optional[bool] = None,
        KMSKey: Optional[str] = None,
        DefaultStorageClass: Optional[str] = None,
        ObjectACL: Optional[str] = None,
        ReadOnly: Optional[bool] = None,
        GuessMIMETypeEnabled: Optional[bool] = None,
        RequesterPays: Optional[bool] = None,
        SMBACLEnabled: Optional[bool] = None,
        AdminUserList: Optional[List] = None,
        ValidUserList: Optional[List] = None,
        InvalidUserList: Optional[List] = None,
    ) -> Dict:
        pass


    def update_smb_security_strategy(
        self,
        GatewayARN: str,
        SMBSecurityStrategy: str,
    ) -> Dict:
        pass


    def update_snapshot_schedule(
        self,
        VolumeARN: str,
        StartAt: int,
        RecurrenceInHours: int,
        Description: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def update_vtl_device_type(
        self,
        VTLDeviceARN: str,
        DeviceType: str,
    ) -> Dict:
        pass

