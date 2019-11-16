"Main interface for storagegateway type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientActivateGatewayResponseTypeDef",
    "ClientActivateGatewayTagsTypeDef",
    "ClientAddCacheResponseTypeDef",
    "ClientAddTagsToResourceResponseTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientAddUploadBufferResponseTypeDef",
    "ClientAddWorkingStorageResponseTypeDef",
    "ClientAssignTapePoolResponseTypeDef",
    "ClientAttachVolumeResponseTypeDef",
    "ClientCancelArchivalResponseTypeDef",
    "ClientCancelRetrievalResponseTypeDef",
    "ClientCreateCachedIscsiVolumeResponseTypeDef",
    "ClientCreateCachedIscsiVolumeTagsTypeDef",
    "ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef",
    "ClientCreateNfsFileShareResponseTypeDef",
    "ClientCreateNfsFileShareTagsTypeDef",
    "ClientCreateSmbFileShareResponseTypeDef",
    "ClientCreateSmbFileShareTagsTypeDef",
    "ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef",
    "ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef",
    "ClientCreateSnapshotResponseTypeDef",
    "ClientCreateSnapshotTagsTypeDef",
    "ClientCreateStoredIscsiVolumeResponseTypeDef",
    "ClientCreateStoredIscsiVolumeTagsTypeDef",
    "ClientCreateTapeWithBarcodeResponseTypeDef",
    "ClientCreateTapeWithBarcodeTagsTypeDef",
    "ClientCreateTapesResponseTypeDef",
    "ClientCreateTapesTagsTypeDef",
    "ClientDeleteBandwidthRateLimitResponseTypeDef",
    "ClientDeleteChapCredentialsResponseTypeDef",
    "ClientDeleteFileShareResponseTypeDef",
    "ClientDeleteGatewayResponseTypeDef",
    "ClientDeleteSnapshotScheduleResponseTypeDef",
    "ClientDeleteTapeArchiveResponseTypeDef",
    "ClientDeleteTapeResponseTypeDef",
    "ClientDeleteVolumeResponseTypeDef",
    "ClientDescribeBandwidthRateLimitResponseTypeDef",
    "ClientDescribeCacheResponseTypeDef",
    "ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    "ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef",
    "ClientDescribeCachedIscsiVolumesResponseTypeDef",
    "ClientDescribeChapCredentialsResponseChapCredentialsTypeDef",
    "ClientDescribeChapCredentialsResponseTypeDef",
    "ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef",
    "ClientDescribeGatewayInformationResponseTagsTypeDef",
    "ClientDescribeGatewayInformationResponseTypeDef",
    "ClientDescribeMaintenanceStartTimeResponseTypeDef",
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef",
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef",
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef",
    "ClientDescribeNfsFileSharesResponseTypeDef",
    "ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef",
    "ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef",
    "ClientDescribeSmbFileSharesResponseTypeDef",
    "ClientDescribeSmbSettingsResponseTypeDef",
    "ClientDescribeSnapshotScheduleResponseTagsTypeDef",
    "ClientDescribeSnapshotScheduleResponseTypeDef",
    "ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    "ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef",
    "ClientDescribeStoredIscsiVolumesResponseTypeDef",
    "ClientDescribeTapeArchivesResponseTapeArchivesTypeDef",
    "ClientDescribeTapeArchivesResponseTypeDef",
    "ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef",
    "ClientDescribeTapeRecoveryPointsResponseTypeDef",
    "ClientDescribeTapesResponseTapesTypeDef",
    "ClientDescribeTapesResponseTypeDef",
    "ClientDescribeUploadBufferResponseTypeDef",
    "ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef",
    "ClientDescribeVtlDevicesResponseVTLDevicesTypeDef",
    "ClientDescribeVtlDevicesResponseTypeDef",
    "ClientDescribeWorkingStorageResponseTypeDef",
    "ClientDetachVolumeResponseTypeDef",
    "ClientDisableGatewayResponseTypeDef",
    "ClientJoinDomainResponseTypeDef",
    "ClientListFileSharesResponseFileShareInfoListTypeDef",
    "ClientListFileSharesResponseTypeDef",
    "ClientListGatewaysResponseGatewaysTypeDef",
    "ClientListGatewaysResponseTypeDef",
    "ClientListLocalDisksResponseDisksTypeDef",
    "ClientListLocalDisksResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTapesResponseTapeInfosTypeDef",
    "ClientListTapesResponseTypeDef",
    "ClientListVolumeInitiatorsResponseTypeDef",
    "ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef",
    "ClientListVolumeRecoveryPointsResponseTypeDef",
    "ClientNotifyWhenUploadedResponseTypeDef",
    "ClientRefreshCacheResponseTypeDef",
    "ClientRemoveTagsFromResourceResponseTypeDef",
    "ClientResetCacheResponseTypeDef",
    "ClientRetrieveTapeArchiveResponseTypeDef",
    "ClientRetrieveTapeRecoveryPointResponseTypeDef",
    "ClientSetLocalConsolePasswordResponseTypeDef",
    "ClientSetSmbGuestPasswordResponseTypeDef",
    "ClientShutdownGatewayResponseTypeDef",
    "ClientStartGatewayResponseTypeDef",
    "ClientUpdateBandwidthRateLimitResponseTypeDef",
    "ClientUpdateChapCredentialsResponseTypeDef",
    "ClientUpdateGatewayInformationResponseTypeDef",
    "ClientUpdateGatewaySoftwareNowResponseTypeDef",
    "ClientUpdateMaintenanceStartTimeResponseTypeDef",
    "ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef",
    "ClientUpdateNfsFileShareResponseTypeDef",
    "ClientUpdateSmbFileShareResponseTypeDef",
    "ClientUpdateSmbSecurityStrategyResponseTypeDef",
    "ClientUpdateSnapshotScheduleResponseTypeDef",
    "ClientUpdateSnapshotScheduleTagsTypeDef",
    "ClientUpdateVtlDeviceTypeResponseTypeDef",
    "DescribeTapeArchivesPaginatePaginationConfigTypeDef",
    "DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef",
    "DescribeTapeArchivesPaginateResponseTypeDef",
    "DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef",
    "DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef",
    "DescribeTapeRecoveryPointsPaginateResponseTypeDef",
    "DescribeTapesPaginatePaginationConfigTypeDef",
    "DescribeTapesPaginateResponseTapesTypeDef",
    "DescribeTapesPaginateResponseTypeDef",
    "DescribeVTLDevicesPaginatePaginationConfigTypeDef",
    "DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef",
    "DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef",
    "DescribeVTLDevicesPaginateResponseTypeDef",
    "ListFileSharesPaginatePaginationConfigTypeDef",
    "ListFileSharesPaginateResponseFileShareInfoListTypeDef",
    "ListFileSharesPaginateResponseTypeDef",
    "ListGatewaysPaginatePaginationConfigTypeDef",
    "ListGatewaysPaginateResponseGatewaysTypeDef",
    "ListGatewaysPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListTapesPaginatePaginationConfigTypeDef",
    "ListTapesPaginateResponseTapeInfosTypeDef",
    "ListTapesPaginateResponseTypeDef",
    "ListVolumesPaginatePaginationConfigTypeDef",
)


_ClientActivateGatewayResponseTypeDef = TypedDict(
    "_ClientActivateGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientActivateGatewayResponseTypeDef(_ClientActivateGatewayResponseTypeDef):
    """
    Type definition for `ClientActivateGateway` `Response`

    AWS Storage Gateway returns the Amazon Resource Name (ARN) of the activated gateway. It is a
    string made of information such as your account, gateway name, and AWS Region. This ARN is used
    to reference the gateway in other API operations as well as resource-based authorization.

    .. note::

      For gateways activated prior to September 02, 2015, the gateway ARN contains the gateway name
      rather than the gateway ID. Changing the name of the gateway has no effect on the gateway ARN.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientActivateGatewayTagsTypeDef = TypedDict(
    "_ClientActivateGatewayTagsTypeDef", {"Key": str, "Value": str}
)


class ClientActivateGatewayTagsTypeDef(_ClientActivateGatewayTagsTypeDef):
    """
    Type definition for `ClientActivateGateway` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientAddCacheResponseTypeDef = TypedDict(
    "_ClientAddCacheResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientAddCacheResponseTypeDef(_ClientAddCacheResponseTypeDef):
    """
    Type definition for `ClientAddCache` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientAddTagsToResourceResponseTypeDef = TypedDict(
    "_ClientAddTagsToResourceResponseTypeDef", {"ResourceARN": str}, total=False
)


class ClientAddTagsToResourceResponseTypeDef(_ClientAddTagsToResourceResponseTypeDef):
    """
    Type definition for `ClientAddTagsToResource` `Response`

    AddTagsToResourceOutput

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the resource you want to add tags to.
    """


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    Type definition for `ClientAddTagsToResource` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientAddUploadBufferResponseTypeDef = TypedDict(
    "_ClientAddUploadBufferResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientAddUploadBufferResponseTypeDef(_ClientAddUploadBufferResponseTypeDef):
    """
    Type definition for `ClientAddUploadBuffer` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientAddWorkingStorageResponseTypeDef = TypedDict(
    "_ClientAddWorkingStorageResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientAddWorkingStorageResponseTypeDef(_ClientAddWorkingStorageResponseTypeDef):
    """
    Type definition for `ClientAddWorkingStorage` `Response`

    A JSON object containing the of the gateway for which working storage was configured.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientAssignTapePoolResponseTypeDef = TypedDict(
    "_ClientAssignTapePoolResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientAssignTapePoolResponseTypeDef(_ClientAssignTapePoolResponseTypeDef):
    """
    Type definition for `ClientAssignTapePool` `Response`

    - **TapeARN** *(string) --*

      The unique Amazon Resource Names (ARN) of the virtual tape that was added to the tape pool.
    """


_ClientAttachVolumeResponseTypeDef = TypedDict(
    "_ClientAttachVolumeResponseTypeDef",
    {"VolumeARN": str, "TargetARN": str},
    total=False,
)


class ClientAttachVolumeResponseTypeDef(_ClientAttachVolumeResponseTypeDef):
    """
    Type definition for `ClientAttachVolume` `Response`

    AttachVolumeOutput

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume that was attached to the gateway.

    - **TargetARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name for the
      initiator that was used to connect to the target.
    """


_ClientCancelArchivalResponseTypeDef = TypedDict(
    "_ClientCancelArchivalResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientCancelArchivalResponseTypeDef(_ClientCancelArchivalResponseTypeDef):
    """
    Type definition for `ClientCancelArchival` `Response`

    CancelArchivalOutput

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of the virtual tape for which archiving was canceled.
    """


_ClientCancelRetrievalResponseTypeDef = TypedDict(
    "_ClientCancelRetrievalResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientCancelRetrievalResponseTypeDef(_ClientCancelRetrievalResponseTypeDef):
    """
    Type definition for `ClientCancelRetrieval` `Response`

    CancelRetrievalOutput

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of the virtual tape for which retrieval was canceled.
    """


_ClientCreateCachedIscsiVolumeResponseTypeDef = TypedDict(
    "_ClientCreateCachedIscsiVolumeResponseTypeDef",
    {"VolumeARN": str, "TargetARN": str},
    total=False,
)


class ClientCreateCachedIscsiVolumeResponseTypeDef(
    _ClientCreateCachedIscsiVolumeResponseTypeDef
):
    """
    Type definition for `ClientCreateCachedIscsiVolume` `Response`

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the configured volume.

    - **TargetARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name that
      initiators can use to connect to the target.
    """


_ClientCreateCachedIscsiVolumeTagsTypeDef = TypedDict(
    "_ClientCreateCachedIscsiVolumeTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateCachedIscsiVolumeTagsTypeDef(
    _ClientCreateCachedIscsiVolumeTagsTypeDef
):
    """
    Type definition for `ClientCreateCachedIscsiVolume` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef = TypedDict(
    "_ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef",
    {"FileMode": str, "DirectoryMode": str, "GroupId": int, "OwnerId": int},
    total=False,
)


class ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef(
    _ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef
):
    """
    Type definition for `ClientCreateNfsFileShare` `NFSFileShareDefaults`

    File share default values. Optional.

    - **FileMode** *(string) --*

      The Unix file mode in the form "nnnn". For example, "0666" represents the default file mode
      inside the file share. The default value is 0666.

    - **DirectoryMode** *(string) --*

      The Unix directory mode in the form "nnnn". For example, "0666" represents the default access
      mode for all directories inside the file share. The default value is 0777.

    - **GroupId** *(integer) --*

      The default group ID for the file share (unless the files have another group ID specified). The
      default value is nfsnobody.

    - **OwnerId** *(integer) --*

      The default owner ID for files in the file share (unless the files have another owner ID
      specified). The default value is nfsnobody.
    """


_ClientCreateNfsFileShareResponseTypeDef = TypedDict(
    "_ClientCreateNfsFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)


class ClientCreateNfsFileShareResponseTypeDef(_ClientCreateNfsFileShareResponseTypeDef):
    """
    Type definition for `ClientCreateNfsFileShare` `Response`

    CreateNFSFileShareOutput

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the newly created file share.
    """


_ClientCreateNfsFileShareTagsTypeDef = TypedDict(
    "_ClientCreateNfsFileShareTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateNfsFileShareTagsTypeDef(_ClientCreateNfsFileShareTagsTypeDef):
    """
    Type definition for `ClientCreateNfsFileShare` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientCreateSmbFileShareResponseTypeDef = TypedDict(
    "_ClientCreateSmbFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)


class ClientCreateSmbFileShareResponseTypeDef(_ClientCreateSmbFileShareResponseTypeDef):
    """
    Type definition for `ClientCreateSmbFileShare` `Response`

    CreateSMBFileShareOutput

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the newly created file share.
    """


_ClientCreateSmbFileShareTagsTypeDef = TypedDict(
    "_ClientCreateSmbFileShareTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateSmbFileShareTagsTypeDef(_ClientCreateSmbFileShareTagsTypeDef):
    """
    Type definition for `ClientCreateSmbFileShare` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef = TypedDict(
    "_ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef",
    {"SnapshotId": str, "VolumeARN": str, "VolumeRecoveryPointTime": str},
    total=False,
)


class ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef(
    _ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef
):
    """
    Type definition for `ClientCreateSnapshotFromVolumeRecoveryPoint` `Response`

    - **SnapshotId** *(string) --*

      The ID of the snapshot.

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the iSCSI volume target. Use the
      DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified
      VolumeARN.

    - **VolumeRecoveryPointTime** *(string) --*

      The time the volume was created from the recovery point.
    """


_ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef = TypedDict(
    "_ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef",
    {"Key": str, "Value": str},
)


class ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef(
    _ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef
):
    """
    Type definition for `ClientCreateSnapshotFromVolumeRecoveryPoint` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientCreateSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseTypeDef",
    {"VolumeARN": str, "SnapshotId": str},
    total=False,
)


class ClientCreateSnapshotResponseTypeDef(_ClientCreateSnapshotResponseTypeDef):
    """
    Type definition for `ClientCreateSnapshot` `Response`

    A JSON object containing the following fields:

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume of which the snapshot was taken.

    - **SnapshotId** *(string) --*

      The snapshot ID that is used to refer to the snapshot in future operations such as describing
      snapshots (Amazon Elastic Compute Cloud API ``DescribeSnapshots`` ) or creating a volume from
      a snapshot ( CreateStorediSCSIVolume ).
    """


_ClientCreateSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateSnapshotTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateSnapshotTagsTypeDef(_ClientCreateSnapshotTagsTypeDef):
    """
    Type definition for `ClientCreateSnapshot` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientCreateStoredIscsiVolumeResponseTypeDef = TypedDict(
    "_ClientCreateStoredIscsiVolumeResponseTypeDef",
    {"VolumeARN": str, "VolumeSizeInBytes": int, "TargetARN": str},
    total=False,
)


class ClientCreateStoredIscsiVolumeResponseTypeDef(
    _ClientCreateStoredIscsiVolumeResponseTypeDef
):
    """
    Type definition for `ClientCreateStoredIscsiVolume` `Response`

    A JSON object containing the following fields:

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the configured volume.

    - **VolumeSizeInBytes** *(integer) --*

      The size of the volume in bytes.

    - **TargetARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name that
      initiators can use to connect to the target.
    """


_ClientCreateStoredIscsiVolumeTagsTypeDef = TypedDict(
    "_ClientCreateStoredIscsiVolumeTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateStoredIscsiVolumeTagsTypeDef(
    _ClientCreateStoredIscsiVolumeTagsTypeDef
):
    """
    Type definition for `ClientCreateStoredIscsiVolume` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientCreateTapeWithBarcodeResponseTypeDef = TypedDict(
    "_ClientCreateTapeWithBarcodeResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientCreateTapeWithBarcodeResponseTypeDef(
    _ClientCreateTapeWithBarcodeResponseTypeDef
):
    """
    Type definition for `ClientCreateTapeWithBarcode` `Response`

    CreateTapeOutput

    - **TapeARN** *(string) --*

      A unique Amazon Resource Name (ARN) that represents the virtual tape that was created.
    """


_ClientCreateTapeWithBarcodeTagsTypeDef = TypedDict(
    "_ClientCreateTapeWithBarcodeTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateTapeWithBarcodeTagsTypeDef(_ClientCreateTapeWithBarcodeTagsTypeDef):
    """
    Type definition for `ClientCreateTapeWithBarcode` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientCreateTapesResponseTypeDef = TypedDict(
    "_ClientCreateTapesResponseTypeDef", {"TapeARNs": List[str]}, total=False
)


class ClientCreateTapesResponseTypeDef(_ClientCreateTapesResponseTypeDef):
    """
    Type definition for `ClientCreateTapes` `Response`

    CreateTapeOutput

    - **TapeARNs** *(list) --*

      A list of unique Amazon Resource Names (ARNs) that represents the virtual tapes that were
      created.

      - *(string) --*
    """


_ClientCreateTapesTagsTypeDef = TypedDict(
    "_ClientCreateTapesTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateTapesTagsTypeDef(_ClientCreateTapesTagsTypeDef):
    """
    Type definition for `ClientCreateTapes` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientDeleteBandwidthRateLimitResponseTypeDef = TypedDict(
    "_ClientDeleteBandwidthRateLimitResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientDeleteBandwidthRateLimitResponseTypeDef(
    _ClientDeleteBandwidthRateLimitResponseTypeDef
):
    """
    Type definition for `ClientDeleteBandwidthRateLimit` `Response`

    A JSON object containing the of the gateway whose bandwidth rate information was deleted.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientDeleteChapCredentialsResponseTypeDef = TypedDict(
    "_ClientDeleteChapCredentialsResponseTypeDef",
    {"TargetARN": str, "InitiatorName": str},
    total=False,
)


class ClientDeleteChapCredentialsResponseTypeDef(
    _ClientDeleteChapCredentialsResponseTypeDef
):
    """
    Type definition for `ClientDeleteChapCredentials` `Response`

    A JSON object containing the following fields:

    - **TargetARN** *(string) --*

      The Amazon Resource Name (ARN) of the target.

    - **InitiatorName** *(string) --*

      The iSCSI initiator that connects to the target.
    """


_ClientDeleteFileShareResponseTypeDef = TypedDict(
    "_ClientDeleteFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)


class ClientDeleteFileShareResponseTypeDef(_ClientDeleteFileShareResponseTypeDef):
    """
    Type definition for `ClientDeleteFileShare` `Response`

    DeleteFileShareOutput

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the deleted file share.
    """


_ClientDeleteGatewayResponseTypeDef = TypedDict(
    "_ClientDeleteGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientDeleteGatewayResponseTypeDef(_ClientDeleteGatewayResponseTypeDef):
    """
    Type definition for `ClientDeleteGateway` `Response`

    A JSON object containing the ID of the deleted gateway.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientDeleteSnapshotScheduleResponseTypeDef = TypedDict(
    "_ClientDeleteSnapshotScheduleResponseTypeDef", {"VolumeARN": str}, total=False
)


class ClientDeleteSnapshotScheduleResponseTypeDef(
    _ClientDeleteSnapshotScheduleResponseTypeDef
):
    """
    Type definition for `ClientDeleteSnapshotSchedule` `Response`

    - **VolumeARN** *(string) --*

      The volume which snapshot schedule was deleted.
    """


_ClientDeleteTapeArchiveResponseTypeDef = TypedDict(
    "_ClientDeleteTapeArchiveResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientDeleteTapeArchiveResponseTypeDef(_ClientDeleteTapeArchiveResponseTypeDef):
    """
    Type definition for `ClientDeleteTapeArchive` `Response`

    DeleteTapeArchiveOutput

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of the virtual tape that was deleted from the virtual tape
      shelf (VTS).
    """


_ClientDeleteTapeResponseTypeDef = TypedDict(
    "_ClientDeleteTapeResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientDeleteTapeResponseTypeDef(_ClientDeleteTapeResponseTypeDef):
    """
    Type definition for `ClientDeleteTape` `Response`

    DeleteTapeOutput

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of the deleted virtual tape.
    """


_ClientDeleteVolumeResponseTypeDef = TypedDict(
    "_ClientDeleteVolumeResponseTypeDef", {"VolumeARN": str}, total=False
)


class ClientDeleteVolumeResponseTypeDef(_ClientDeleteVolumeResponseTypeDef):
    """
    Type definition for `ClientDeleteVolume` `Response`

    A JSON object containing the of the storage volume that was deleted

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the storage volume that was deleted. It is the same ARN you
      provided in the request.
    """


_ClientDescribeBandwidthRateLimitResponseTypeDef = TypedDict(
    "_ClientDescribeBandwidthRateLimitResponseTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
    },
    total=False,
)


class ClientDescribeBandwidthRateLimitResponseTypeDef(
    _ClientDescribeBandwidthRateLimitResponseTypeDef
):
    """
    Type definition for `ClientDescribeBandwidthRateLimit` `Response`

    A JSON object containing the following fields:

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **AverageUploadRateLimitInBitsPerSec** *(integer) --*

      The average upload bandwidth rate limit in bits per second. This field does not appear in the
      response if the upload rate limit is not set.

    - **AverageDownloadRateLimitInBitsPerSec** *(integer) --*

      The average download bandwidth rate limit in bits per second. This field does not appear in
      the response if the download rate limit is not set.
    """


_ClientDescribeCacheResponseTypeDef = TypedDict(
    "_ClientDescribeCacheResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "CacheAllocatedInBytes": int,
        "CacheUsedPercentage": float,
        "CacheDirtyPercentage": float,
        "CacheHitPercentage": float,
        "CacheMissPercentage": float,
    },
    total=False,
)


class ClientDescribeCacheResponseTypeDef(_ClientDescribeCacheResponseTypeDef):
    """
    Type definition for `ClientDescribeCache` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **DiskIds** *(list) --*

      An array of strings that identify disks that are to be configured as working storage. Each
      string have a minimum length of 1 and maximum length of 300. You can get the disk IDs from
      the  ListLocalDisks API.

      - *(string) --*

    - **CacheAllocatedInBytes** *(integer) --*

      The amount of cache in bytes allocated to the a gateway.

    - **CacheUsedPercentage** *(float) --*

      Percent use of the gateway's cache storage. This metric applies only to the gateway-cached
      volume setup. The sample is taken at the end of the reporting period.

    - **CacheDirtyPercentage** *(float) --*

      The file share's contribution to the overall percentage of the gateway's cache that has not
      been persisted to AWS. The sample is taken at the end of the reporting period.

    - **CacheHitPercentage** *(float) --*

      Percent of application read operations from the file shares that are served from cache. The
      sample is taken at the end of the reporting period.

    - **CacheMissPercentage** *(float) --*

      Percent of application read operations from the file shares that are not served from cache.
      The sample is taken at the end of the reporting period.
    """


_ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef = TypedDict(
    "_ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "LunNumber": int,
        "ChapEnabled": bool,
    },
    total=False,
)


class ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef(
    _ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef
):
    """
    Type definition for `ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumes` `VolumeiSCSIAttributes`

    An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one
    stored volume.

    - **TargetARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume target.

    - **NetworkInterfaceId** *(string) --*

      The network interface identifier.

    - **NetworkInterfacePort** *(integer) --*

      The port used to communicate with iSCSI targets.

    - **LunNumber** *(integer) --*

      The logical disk number.

    - **ChapEnabled** *(boolean) --*

      Indicates whether mutual CHAP is enabled for the iSCSI target.
    """


_ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef = TypedDict(
    "_ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "SourceSnapshotId": str,
        "VolumeiSCSIAttributes": ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef,
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)


class ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef(
    _ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef
):
    """
    Type definition for `ClientDescribeCachedIscsiVolumesResponse` `CachediSCSIVolumes`

    Describes an iSCSI cached volume.

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the storage volume.

    - **VolumeId** *(string) --*

      The unique identifier of the volume, e.g. vol-AE4B946D.

    - **VolumeType** *(string) --*

      One of the VolumeType enumeration values that describes the type of the volume.

    - **VolumeStatus** *(string) --*

      One of the VolumeStatus values that indicates the state of the storage volume.

    - **VolumeAttachmentStatus** *(string) --*

      A value that indicates whether a storage volume is attached to or detached from a
      gateway. For more information, see `Moving Your Volumes to a Different Gateway
      <https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#attach-detach-volume>`__
      .

    - **VolumeSizeInBytes** *(integer) --*

      The size, in bytes, of the volume capacity.

    - **VolumeProgress** *(float) --*

      Represents the percentage complete if the volume is restoring or bootstrapping that
      represents the percent of data transferred. This field does not appear in the response if
      the cached volume is not restoring or bootstrapping.

    - **SourceSnapshotId** *(string) --*

      If the cached volume was created from a snapshot, this field contains the snapshot ID
      used, e.g. snap-78e22663. Otherwise, this field is not included.

    - **VolumeiSCSIAttributes** *(dict) --*

      An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one
      stored volume.

      - **TargetARN** *(string) --*

        The Amazon Resource Name (ARN) of the volume target.

      - **NetworkInterfaceId** *(string) --*

        The network interface identifier.

      - **NetworkInterfacePort** *(integer) --*

        The port used to communicate with iSCSI targets.

      - **LunNumber** *(integer) --*

        The logical disk number.

      - **ChapEnabled** *(boolean) --*

        Indicates whether mutual CHAP is enabled for the iSCSI target.

    - **CreatedDate** *(datetime) --*

      The date the volume was created. Volumes created prior to March 28, 2017 don’t have this
      time stamp.

    - **VolumeUsedInBytes** *(integer) --*

      The size of the data stored on the volume in bytes. This value is calculated based on the
      number of blocks that are touched, instead of the actual amount of data written. This
      value can be useful for sequential write patterns but less accurate for random write
      patterns. ``VolumeUsedInBytes`` is different from the compressed size of the volume,
      which is the value that is used to calculate your bill.

      .. note::

        This value is not available for volumes created prior to May 13, 2015, until you store
        data on the volume.

    - **KMSKey** *(string) --*

      The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
      encryption. This value can only be set when KMSEncrypted is true. Optional.

    - **TargetName** *(string) --*

      The name of the iSCSI target used by an initiator to connect to a volume and used as a
      suffix for the target ARN. For example, specifying ``TargetName`` as *myvolume* results
      in the target ARN of
      ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume``
      . The target name must be unique across all volumes on a gateway.

      If you don't specify a value, Storage Gateway uses the value that was previously used for
      this volume as the new target name.
    """


_ClientDescribeCachedIscsiVolumesResponseTypeDef = TypedDict(
    "_ClientDescribeCachedIscsiVolumesResponseTypeDef",
    {
        "CachediSCSIVolumes": List[
            ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeCachedIscsiVolumesResponseTypeDef(
    _ClientDescribeCachedIscsiVolumesResponseTypeDef
):
    """
    Type definition for `ClientDescribeCachedIscsiVolumes` `Response`

    A JSON object containing the following fields:

    - **CachediSCSIVolumes** *(list) --*

      An array of objects where each object contains metadata about one cached volume.

      - *(dict) --*

        Describes an iSCSI cached volume.

        - **VolumeARN** *(string) --*

          The Amazon Resource Name (ARN) of the storage volume.

        - **VolumeId** *(string) --*

          The unique identifier of the volume, e.g. vol-AE4B946D.

        - **VolumeType** *(string) --*

          One of the VolumeType enumeration values that describes the type of the volume.

        - **VolumeStatus** *(string) --*

          One of the VolumeStatus values that indicates the state of the storage volume.

        - **VolumeAttachmentStatus** *(string) --*

          A value that indicates whether a storage volume is attached to or detached from a
          gateway. For more information, see `Moving Your Volumes to a Different Gateway
          <https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#attach-detach-volume>`__
          .

        - **VolumeSizeInBytes** *(integer) --*

          The size, in bytes, of the volume capacity.

        - **VolumeProgress** *(float) --*

          Represents the percentage complete if the volume is restoring or bootstrapping that
          represents the percent of data transferred. This field does not appear in the response if
          the cached volume is not restoring or bootstrapping.

        - **SourceSnapshotId** *(string) --*

          If the cached volume was created from a snapshot, this field contains the snapshot ID
          used, e.g. snap-78e22663. Otherwise, this field is not included.

        - **VolumeiSCSIAttributes** *(dict) --*

          An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one
          stored volume.

          - **TargetARN** *(string) --*

            The Amazon Resource Name (ARN) of the volume target.

          - **NetworkInterfaceId** *(string) --*

            The network interface identifier.

          - **NetworkInterfacePort** *(integer) --*

            The port used to communicate with iSCSI targets.

          - **LunNumber** *(integer) --*

            The logical disk number.

          - **ChapEnabled** *(boolean) --*

            Indicates whether mutual CHAP is enabled for the iSCSI target.

        - **CreatedDate** *(datetime) --*

          The date the volume was created. Volumes created prior to March 28, 2017 don’t have this
          time stamp.

        - **VolumeUsedInBytes** *(integer) --*

          The size of the data stored on the volume in bytes. This value is calculated based on the
          number of blocks that are touched, instead of the actual amount of data written. This
          value can be useful for sequential write patterns but less accurate for random write
          patterns. ``VolumeUsedInBytes`` is different from the compressed size of the volume,
          which is the value that is used to calculate your bill.

          .. note::

            This value is not available for volumes created prior to May 13, 2015, until you store
            data on the volume.

        - **KMSKey** *(string) --*

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        - **TargetName** *(string) --*

          The name of the iSCSI target used by an initiator to connect to a volume and used as a
          suffix for the target ARN. For example, specifying ``TargetName`` as *myvolume* results
          in the target ARN of
          ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume``
          . The target name must be unique across all volumes on a gateway.

          If you don't specify a value, Storage Gateway uses the value that was previously used for
          this volume as the new target name.
    """


_ClientDescribeChapCredentialsResponseChapCredentialsTypeDef = TypedDict(
    "_ClientDescribeChapCredentialsResponseChapCredentialsTypeDef",
    {
        "TargetARN": str,
        "SecretToAuthenticateInitiator": str,
        "InitiatorName": str,
        "SecretToAuthenticateTarget": str,
    },
    total=False,
)


class ClientDescribeChapCredentialsResponseChapCredentialsTypeDef(
    _ClientDescribeChapCredentialsResponseChapCredentialsTypeDef
):
    """
    Type definition for `ClientDescribeChapCredentialsResponse` `ChapCredentials`

    Describes Challenge-Handshake Authentication Protocol (CHAP) information that supports
    authentication between your gateway and iSCSI initiators.

    - **TargetARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume.

      Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

    - **SecretToAuthenticateInitiator** *(string) --*

      The secret key that the initiator (for example, the Windows client) must provide to
      participate in mutual CHAP with the target.

    - **InitiatorName** *(string) --*

      The iSCSI initiator that connects to the target.

    - **SecretToAuthenticateTarget** *(string) --*

      The secret key that the target must provide to participate in mutual CHAP with the
      initiator (e.g. Windows client).
    """


_ClientDescribeChapCredentialsResponseTypeDef = TypedDict(
    "_ClientDescribeChapCredentialsResponseTypeDef",
    {
        "ChapCredentials": List[
            ClientDescribeChapCredentialsResponseChapCredentialsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeChapCredentialsResponseTypeDef(
    _ClientDescribeChapCredentialsResponseTypeDef
):
    """
    Type definition for `ClientDescribeChapCredentials` `Response`

    A JSON object containing a .

    - **ChapCredentials** *(list) --*

      An array of  ChapInfo objects that represent CHAP credentials. Each object in the array
      contains CHAP credential information for one target-initiator pair. If no CHAP credentials
      are set, an empty array is returned. CHAP credential information is provided in a JSON object
      with the following fields:

      * **InitiatorName** : The iSCSI initiator that connects to the target.

      * **SecretToAuthenticateInitiator** : The secret key that the initiator (for example, the
      Windows client) must provide to participate in mutual CHAP with the target.

      * **SecretToAuthenticateTarget** : The secret key that the target must provide to participate
      in mutual CHAP with the initiator (e.g. Windows client).

      * **TargetARN** : The Amazon Resource Name (ARN) of the storage volume.

      - *(dict) --*

        Describes Challenge-Handshake Authentication Protocol (CHAP) information that supports
        authentication between your gateway and iSCSI initiators.

        - **TargetARN** *(string) --*

          The Amazon Resource Name (ARN) of the volume.

          Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

        - **SecretToAuthenticateInitiator** *(string) --*

          The secret key that the initiator (for example, the Windows client) must provide to
          participate in mutual CHAP with the target.

        - **InitiatorName** *(string) --*

          The iSCSI initiator that connects to the target.

        - **SecretToAuthenticateTarget** *(string) --*

          The secret key that the target must provide to participate in mutual CHAP with the
          initiator (e.g. Windows client).
    """


_ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef = TypedDict(
    "_ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef",
    {"Ipv4Address": str, "MacAddress": str, "Ipv6Address": str},
    total=False,
)


class ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef(
    _ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef
):
    """
    Type definition for `ClientDescribeGatewayInformationResponse` `GatewayNetworkInterfaces`

    Describes a gateway's network interface.

    - **Ipv4Address** *(string) --*

      The Internet Protocol version 4 (IPv4) address of the interface.

    - **MacAddress** *(string) --*

      The Media Access Control (MAC) address of the interface.

      .. note::

        This is currently unsupported and will not be returned in output.

    - **Ipv6Address** *(string) --*

      The Internet Protocol version 6 (IPv6) address of the interface. *Currently not
      supported* .
    """


_ClientDescribeGatewayInformationResponseTagsTypeDef = TypedDict(
    "_ClientDescribeGatewayInformationResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeGatewayInformationResponseTagsTypeDef(
    _ClientDescribeGatewayInformationResponseTagsTypeDef
):
    """
    Type definition for `ClientDescribeGatewayInformationResponse` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --*

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --*

      Value of the tag key.
    """


_ClientDescribeGatewayInformationResponseTypeDef = TypedDict(
    "_ClientDescribeGatewayInformationResponseTypeDef",
    {
        "GatewayARN": str,
        "GatewayId": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayState": str,
        "GatewayNetworkInterfaces": List[
            ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef
        ],
        "GatewayType": str,
        "NextUpdateAvailabilityDate": str,
        "LastSoftwareUpdate": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
        "Tags": List[ClientDescribeGatewayInformationResponseTagsTypeDef],
        "VPCEndpoint": str,
        "CloudWatchLogGroupARN": str,
    },
    total=False,
)


class ClientDescribeGatewayInformationResponseTypeDef(
    _ClientDescribeGatewayInformationResponseTypeDef
):
    """
    Type definition for `ClientDescribeGatewayInformation` `Response`

    A JSON object containing the following fields:

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **GatewayId** *(string) --*

      The unique identifier assigned to your gateway during activation. This ID becomes part of the
      gateway Amazon Resource Name (ARN), which you use as input for other operations.

    - **GatewayName** *(string) --*

      The name you configured for your gateway.

    - **GatewayTimezone** *(string) --*

      A value that indicates the time zone configured for the gateway.

    - **GatewayState** *(string) --*

      A value that indicates the operating state of the gateway.

    - **GatewayNetworkInterfaces** *(list) --*

      A  NetworkInterface array that contains descriptions of the gateway network interfaces.

      - *(dict) --*

        Describes a gateway's network interface.

        - **Ipv4Address** *(string) --*

          The Internet Protocol version 4 (IPv4) address of the interface.

        - **MacAddress** *(string) --*

          The Media Access Control (MAC) address of the interface.

          .. note::

            This is currently unsupported and will not be returned in output.

        - **Ipv6Address** *(string) --*

          The Internet Protocol version 6 (IPv6) address of the interface. *Currently not
          supported* .

    - **GatewayType** *(string) --*

      The type of the gateway.

    - **NextUpdateAvailabilityDate** *(string) --*

      The date on which an update to the gateway is available. This date is in the time zone of the
      gateway. If the gateway is not available for an update this field is not returned in the
      response.

    - **LastSoftwareUpdate** *(string) --*

      The date on which the last software update was applied to the gateway. If the gateway has
      never been updated, this field does not return a value in the response.

    - **Ec2InstanceId** *(string) --*

      The ID of the Amazon EC2 instance that was used to launch the gateway.

    - **Ec2InstanceRegion** *(string) --*

      The AWS Region where the Amazon EC2 instance is located.

    - **Tags** *(list) --*

      A list of up to 50 tags assigned to the gateway, sorted alphabetically by key name. Each tag
      is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags
      using the ``ListTagsForResource`` API operation.

      - *(dict) --*

        A key-value pair that helps you manage, filter, and search for your resource. Allowed
        characters: letters, white space, and numbers, representable in UTF-8, and the following
        characters: + - = . _ : /

        - **Key** *(string) --*

          Tag key (String). The key can't start with aws:.

        - **Value** *(string) --*

          Value of the tag key.

    - **VPCEndpoint** *(string) --*

      The configuration settings for the virtual private cloud (VPC) endpoint for your gateway.

    - **CloudWatchLogGroupARN** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that was used to monitor
      and log events in the gateway.
    """


_ClientDescribeMaintenanceStartTimeResponseTypeDef = TypedDict(
    "_ClientDescribeMaintenanceStartTimeResponseTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfWeek": int,
        "DayOfMonth": int,
        "Timezone": str,
    },
    total=False,
)


class ClientDescribeMaintenanceStartTimeResponseTypeDef(
    _ClientDescribeMaintenanceStartTimeResponseTypeDef
):
    """
    Type definition for `ClientDescribeMaintenanceStartTime` `Response`

    A JSON object containing the following fields:

    *  DescribeMaintenanceStartTimeOutput$DayOfMonth

    *  DescribeMaintenanceStartTimeOutput$DayOfWeek

    *  DescribeMaintenanceStartTimeOutput$HourOfDay

    *  DescribeMaintenanceStartTimeOutput$MinuteOfHour

    *  DescribeMaintenanceStartTimeOutput$Timezone

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **HourOfDay** *(integer) --*

      The hour component of the maintenance start time represented as *hh* , where *hh* is the hour
      (0 to 23). The hour of the day is in the time zone of the gateway.

    - **MinuteOfHour** *(integer) --*

      The minute component of the maintenance start time represented as *mm* , where *mm* is the
      minute (0 to 59). The minute of the hour is in the time zone of the gateway.

    - **DayOfWeek** *(integer) --*

      An ordinal number between 0 and 6 that represents the day of the week, where 0 represents
      Sunday and 6 represents Saturday. The day of week is in the time zone of the gateway.

    - **DayOfMonth** *(integer) --*

      The day of the month component of the maintenance start time represented as an ordinal number
      from 1 to 28, where 1 represents the first day of the month and 28 represents the last day of
      the month.

      .. note::

        This value is only available for tape and volume gateways.

    - **Timezone** *(string) --*

      A value that indicates the time zone that is set for the gateway. The start time and day of
      week specified should be in the time zone of the gateway.
    """


_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef = TypedDict(
    "_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef",
    {"FileMode": str, "DirectoryMode": str, "GroupId": int, "OwnerId": int},
    total=False,
)


class ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef(
    _ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef
):
    """
    Type definition for `ClientDescribeNfsFileSharesResponseNFSFileShareInfoList` `NFSFileShareDefaults`

    Describes Network File System (NFS) file share default values. Files and folders stored
    as Amazon S3 objects in S3 buckets don't, by default, have Unix file permissions assigned
    to them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent
    files and folders are assigned these default Unix permissions. This operation is only
    supported for file gateways.

    - **FileMode** *(string) --*

      The Unix file mode in the form "nnnn". For example, "0666" represents the default file
      mode inside the file share. The default value is 0666.

    - **DirectoryMode** *(string) --*

      The Unix directory mode in the form "nnnn". For example, "0666" represents the default
      access mode for all directories inside the file share. The default value is 0777.

    - **GroupId** *(integer) --*

      The default group ID for the file share (unless the files have another group ID
      specified). The default value is nfsnobody.

    - **OwnerId** *(integer) --*

      The default owner ID for files in the file share (unless the files have another owner
      ID specified). The default value is nfsnobody.
    """


_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef = TypedDict(
    "_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef(
    _ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef
):
    """
    Type definition for `ClientDescribeNfsFileSharesResponseNFSFileShareInfoList` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the
    following characters: + - = . _ : /

    - **Key** *(string) --*

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --*

      Value of the tag key.
    """


_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef = TypedDict(
    "_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef",
    {
        "NFSFileShareDefaults": ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef,
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": str,
        "ClientList": List[str],
        "Squash": str,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "Tags": List[
            ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef(
    _ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef
):
    """
    Type definition for `ClientDescribeNfsFileSharesResponse` `NFSFileShareInfoList`

    The Unix file permissions and ownership information assigned, by default, to native S3
    objects when file gateway discovers them in S3 buckets. This operation is only supported in
    file gateways.

    - **NFSFileShareDefaults** *(dict) --*

      Describes Network File System (NFS) file share default values. Files and folders stored
      as Amazon S3 objects in S3 buckets don't, by default, have Unix file permissions assigned
      to them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent
      files and folders are assigned these default Unix permissions. This operation is only
      supported for file gateways.

      - **FileMode** *(string) --*

        The Unix file mode in the form "nnnn". For example, "0666" represents the default file
        mode inside the file share. The default value is 0666.

      - **DirectoryMode** *(string) --*

        The Unix directory mode in the form "nnnn". For example, "0666" represents the default
        access mode for all directories inside the file share. The default value is 0777.

      - **GroupId** *(integer) --*

        The default group ID for the file share (unless the files have another group ID
        specified). The default value is nfsnobody.

      - **OwnerId** *(integer) --*

        The default owner ID for files in the file share (unless the files have another owner
        ID specified). The default value is nfsnobody.

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the file share.

    - **FileShareId** *(string) --*

      The ID of the file share.

    - **FileShareStatus** *(string) --*

      The status of the file share. Possible values are ``CREATING`` , ``UPDATING`` ,
      ``AVAILABLE`` and ``DELETING`` .

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
      a list of gateways for your account and AWS Region.

    - **KMSEncrypted** *(boolean) --*

      True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a
      key managed by Amazon S3. Optional.

    - **KMSKey** *(string) --*

      The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
      encryption. This value can only be set when KMSEncrypted is true. Optional.

    - **Path** *(string) --*

      The file share path used by the NFS client to identify the mount point.

    - **Role** *(string) --*

      The ARN of the IAM role that file gateway assumes when it accesses the underlying storage.

    - **LocationARN** *(string) --*

      The ARN of the backend storage used for storing file data.

    - **DefaultStorageClass** *(string) --*

      The default storage class for objects put into an Amazon S3 bucket by the file gateway.
      Possible values are ``S3_STANDARD`` , ``S3_STANDARD_IA`` , or ``S3_ONEZONE_IA`` . If this
      field is not populated, the default value ``S3_STANDARD`` is used. Optional.

    - **ObjectACL** *(string) --*

      A value that sets the access control list permission for objects in the S3 bucket that a
      file gateway puts objects into. The default value is "private".

    - **ClientList** *(list) --*

      The list of clients that are allowed to access the file gateway. The list must contain
      either valid IP addresses or valid CIDR blocks.

      - *(string) --*

    - **Squash** *(string) --*

      The user mapped to anonymous user. Valid options are the following:

      * ``RootSquash`` - Only root is mapped to anonymous user.

      * ``NoSquash`` - No one is mapped to anonymous user

      * ``AllSquash`` - Everyone is mapped to anonymous user.

    - **ReadOnly** *(boolean) --*

      A value that sets the write status of a file share. This value is true if the write
      status is read-only, and otherwise false.

    - **GuessMIMETypeEnabled** *(boolean) --*

      A value that enables guessing of the MIME type for uploaded objects based on file
      extensions. Set this value to true to enable MIME type guessing, and otherwise to false.
      The default value is true.

    - **RequesterPays** *(boolean) --*

      A value that sets who pays the cost of the request and the cost associated with data
      download from the S3 bucket. If this value is set to true, the requester pays the costs.
      Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of
      storing data.

      .. note::

         ``RequesterPays`` is a configuration for the S3 bucket that backs the file share, so
         make sure that the configuration on the file share is the same as the S3 bucket
         configuration.

    - **Tags** *(list) --*

      A list of up to 50 tags assigned to the NFS file share, sorted alphabetically by key
      name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you
      can view all tags using the ``ListTagsForResource`` API operation.

      - *(dict) --*

        A key-value pair that helps you manage, filter, and search for your resource. Allowed
        characters: letters, white space, and numbers, representable in UTF-8, and the
        following characters: + - = . _ : /

        - **Key** *(string) --*

          Tag key (String). The key can't start with aws:.

        - **Value** *(string) --*

          Value of the tag key.
    """


_ClientDescribeNfsFileSharesResponseTypeDef = TypedDict(
    "_ClientDescribeNfsFileSharesResponseTypeDef",
    {
        "NFSFileShareInfoList": List[
            ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeNfsFileSharesResponseTypeDef(
    _ClientDescribeNfsFileSharesResponseTypeDef
):
    """
    Type definition for `ClientDescribeNfsFileShares` `Response`

    DescribeNFSFileSharesOutput

    - **NFSFileShareInfoList** *(list) --*

      An array containing a description for each requested file share.

      - *(dict) --*

        The Unix file permissions and ownership information assigned, by default, to native S3
        objects when file gateway discovers them in S3 buckets. This operation is only supported in
        file gateways.

        - **NFSFileShareDefaults** *(dict) --*

          Describes Network File System (NFS) file share default values. Files and folders stored
          as Amazon S3 objects in S3 buckets don't, by default, have Unix file permissions assigned
          to them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent
          files and folders are assigned these default Unix permissions. This operation is only
          supported for file gateways.

          - **FileMode** *(string) --*

            The Unix file mode in the form "nnnn". For example, "0666" represents the default file
            mode inside the file share. The default value is 0666.

          - **DirectoryMode** *(string) --*

            The Unix directory mode in the form "nnnn". For example, "0666" represents the default
            access mode for all directories inside the file share. The default value is 0777.

          - **GroupId** *(integer) --*

            The default group ID for the file share (unless the files have another group ID
            specified). The default value is nfsnobody.

          - **OwnerId** *(integer) --*

            The default owner ID for files in the file share (unless the files have another owner
            ID specified). The default value is nfsnobody.

        - **FileShareARN** *(string) --*

          The Amazon Resource Name (ARN) of the file share.

        - **FileShareId** *(string) --*

          The ID of the file share.

        - **FileShareStatus** *(string) --*

          The status of the file share. Possible values are ``CREATING`` , ``UPDATING`` ,
          ``AVAILABLE`` and ``DELETING`` .

        - **GatewayARN** *(string) --*

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
          a list of gateways for your account and AWS Region.

        - **KMSEncrypted** *(boolean) --*

          True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a
          key managed by Amazon S3. Optional.

        - **KMSKey** *(string) --*

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        - **Path** *(string) --*

          The file share path used by the NFS client to identify the mount point.

        - **Role** *(string) --*

          The ARN of the IAM role that file gateway assumes when it accesses the underlying storage.

        - **LocationARN** *(string) --*

          The ARN of the backend storage used for storing file data.

        - **DefaultStorageClass** *(string) --*

          The default storage class for objects put into an Amazon S3 bucket by the file gateway.
          Possible values are ``S3_STANDARD`` , ``S3_STANDARD_IA`` , or ``S3_ONEZONE_IA`` . If this
          field is not populated, the default value ``S3_STANDARD`` is used. Optional.

        - **ObjectACL** *(string) --*

          A value that sets the access control list permission for objects in the S3 bucket that a
          file gateway puts objects into. The default value is "private".

        - **ClientList** *(list) --*

          The list of clients that are allowed to access the file gateway. The list must contain
          either valid IP addresses or valid CIDR blocks.

          - *(string) --*

        - **Squash** *(string) --*

          The user mapped to anonymous user. Valid options are the following:

          * ``RootSquash`` - Only root is mapped to anonymous user.

          * ``NoSquash`` - No one is mapped to anonymous user

          * ``AllSquash`` - Everyone is mapped to anonymous user.

        - **ReadOnly** *(boolean) --*

          A value that sets the write status of a file share. This value is true if the write
          status is read-only, and otherwise false.

        - **GuessMIMETypeEnabled** *(boolean) --*

          A value that enables guessing of the MIME type for uploaded objects based on file
          extensions. Set this value to true to enable MIME type guessing, and otherwise to false.
          The default value is true.

        - **RequesterPays** *(boolean) --*

          A value that sets who pays the cost of the request and the cost associated with data
          download from the S3 bucket. If this value is set to true, the requester pays the costs.
          Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of
          storing data.

          .. note::

             ``RequesterPays`` is a configuration for the S3 bucket that backs the file share, so
             make sure that the configuration on the file share is the same as the S3 bucket
             configuration.

        - **Tags** *(list) --*

          A list of up to 50 tags assigned to the NFS file share, sorted alphabetically by key
          name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you
          can view all tags using the ``ListTagsForResource`` API operation.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the
            following characters: + - = . _ : /

            - **Key** *(string) --*

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --*

              Value of the tag key.
    """


_ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef = TypedDict(
    "_ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef(
    _ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef
):
    """
    Type definition for `ClientDescribeSmbFileSharesResponseSMBFileShareInfoList` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the
    following characters: + - = . _ : /

    - **Key** *(string) --*

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --*

      Value of the tag key.
    """


_ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef = TypedDict(
    "_ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef",
    {
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": str,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "SMBACLEnabled": bool,
        "AdminUserList": List[str],
        "ValidUserList": List[str],
        "InvalidUserList": List[str],
        "Authentication": str,
        "Tags": List[
            ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef(
    _ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef
):
    """
    Type definition for `ClientDescribeSmbFileSharesResponse` `SMBFileShareInfoList`

    The Windows file permissions and ownership information assigned, by default, to native S3
    objects when file gateway discovers them in S3 buckets. This operation is only supported
    for file gateways.

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the file share.

    - **FileShareId** *(string) --*

      The ID of the file share.

    - **FileShareStatus** *(string) --*

      The status of the file share. Possible values are ``CREATING`` , ``UPDATING`` ,
      ``AVAILABLE`` and ``DELETING`` .

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
      a list of gateways for your account and AWS Region.

    - **KMSEncrypted** *(boolean) --*

      True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a
      key managed by Amazon S3. Optional.

    - **KMSKey** *(string) --*

      The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
      encryption. This value can only be set when KMSEncrypted is true. Optional.

    - **Path** *(string) --*

      The file share path used by the SMB client to identify the mount point.

    - **Role** *(string) --*

      The ARN of the IAM role that file gateway assumes when it accesses the underlying storage.

    - **LocationARN** *(string) --*

      The ARN of the backend storage used for storing file data.

    - **DefaultStorageClass** *(string) --*

      The default storage class for objects put into an Amazon S3 bucket by the file gateway.
      Possible values are ``S3_STANDARD`` , ``S3_STANDARD_IA`` , or ``S3_ONEZONE_IA`` . If this
      field is not populated, the default value ``S3_STANDARD`` is used. Optional.

    - **ObjectACL** *(string) --*

      A value that sets the access control list permission for objects in the S3 bucket that a
      file gateway puts objects into. The default value is "private".

    - **ReadOnly** *(boolean) --*

      A value that sets the write status of a file share. This value is true if the write
      status is read-only, and otherwise false.

    - **GuessMIMETypeEnabled** *(boolean) --*

      A value that enables guessing of the MIME type for uploaded objects based on file
      extensions. Set this value to true to enable MIME type guessing, and otherwise to false.
      The default value is true.

    - **RequesterPays** *(boolean) --*

      A value that sets who pays the cost of the request and the cost associated with data
      download from the S3 bucket. If this value is set to true, the requester pays the costs.
      Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of
      storing data.

      .. note::

         ``RequesterPays`` is a configuration for the S3 bucket that backs the file share, so
         make sure that the configuration on the file share is the same as the S3 bucket
         configuration.

    - **SMBACLEnabled** *(boolean) --*

      If this value is set to "true", indicates that ACL (access control list) is enabled on
      the SMB file share. If it is set to "false", it indicates that file and directory
      permissions are mapped to the POSIX permission.

      For more information, see
      https://docs.aws.amazon.com/storagegateway/latest/userguide/smb-acl.html in the Storage
      Gateway User Guide.

    - **AdminUserList** *(list) --*

      A list of users or groups in the Active Directory that have administrator rights to the
      file share. A group must be prefixed with the @ character. For example ``@group1`` . Can
      only be set if Authentication is set to ``ActiveDirectory`` .

      - *(string) --*

    - **ValidUserList** *(list) --*

      A list of users or groups in the Active Directory that are allowed to access the file
      share. A group must be prefixed with the @ character. For example ``@group1`` . Can only
      be set if Authentication is set to ``ActiveDirectory`` .

      - *(string) --*

    - **InvalidUserList** *(list) --*

      A list of users or groups in the Active Directory that are not allowed to access the file
      share. A group must be prefixed with the @ character. For example ``@group1`` . Can only
      be set if Authentication is set to ``ActiveDirectory`` .

      - *(string) --*

    - **Authentication** *(string) --*

      The authentication method of the file share.

      Valid values are ``ActiveDirectory`` or ``GuestAccess`` . The default is
      ``ActiveDirectory`` .

    - **Tags** *(list) --*

      A list of up to 50 tags assigned to the SMB file share, sorted alphabetically by key
      name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you
      can view all tags using the ``ListTagsForResource`` API operation.

      - *(dict) --*

        A key-value pair that helps you manage, filter, and search for your resource. Allowed
        characters: letters, white space, and numbers, representable in UTF-8, and the
        following characters: + - = . _ : /

        - **Key** *(string) --*

          Tag key (String). The key can't start with aws:.

        - **Value** *(string) --*

          Value of the tag key.
    """


_ClientDescribeSmbFileSharesResponseTypeDef = TypedDict(
    "_ClientDescribeSmbFileSharesResponseTypeDef",
    {
        "SMBFileShareInfoList": List[
            ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeSmbFileSharesResponseTypeDef(
    _ClientDescribeSmbFileSharesResponseTypeDef
):
    """
    Type definition for `ClientDescribeSmbFileShares` `Response`

    DescribeSMBFileSharesOutput

    - **SMBFileShareInfoList** *(list) --*

      An array containing a description for each requested file share.

      - *(dict) --*

        The Windows file permissions and ownership information assigned, by default, to native S3
        objects when file gateway discovers them in S3 buckets. This operation is only supported
        for file gateways.

        - **FileShareARN** *(string) --*

          The Amazon Resource Name (ARN) of the file share.

        - **FileShareId** *(string) --*

          The ID of the file share.

        - **FileShareStatus** *(string) --*

          The status of the file share. Possible values are ``CREATING`` , ``UPDATING`` ,
          ``AVAILABLE`` and ``DELETING`` .

        - **GatewayARN** *(string) --*

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
          a list of gateways for your account and AWS Region.

        - **KMSEncrypted** *(boolean) --*

          True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a
          key managed by Amazon S3. Optional.

        - **KMSKey** *(string) --*

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        - **Path** *(string) --*

          The file share path used by the SMB client to identify the mount point.

        - **Role** *(string) --*

          The ARN of the IAM role that file gateway assumes when it accesses the underlying storage.

        - **LocationARN** *(string) --*

          The ARN of the backend storage used for storing file data.

        - **DefaultStorageClass** *(string) --*

          The default storage class for objects put into an Amazon S3 bucket by the file gateway.
          Possible values are ``S3_STANDARD`` , ``S3_STANDARD_IA`` , or ``S3_ONEZONE_IA`` . If this
          field is not populated, the default value ``S3_STANDARD`` is used. Optional.

        - **ObjectACL** *(string) --*

          A value that sets the access control list permission for objects in the S3 bucket that a
          file gateway puts objects into. The default value is "private".

        - **ReadOnly** *(boolean) --*

          A value that sets the write status of a file share. This value is true if the write
          status is read-only, and otherwise false.

        - **GuessMIMETypeEnabled** *(boolean) --*

          A value that enables guessing of the MIME type for uploaded objects based on file
          extensions. Set this value to true to enable MIME type guessing, and otherwise to false.
          The default value is true.

        - **RequesterPays** *(boolean) --*

          A value that sets who pays the cost of the request and the cost associated with data
          download from the S3 bucket. If this value is set to true, the requester pays the costs.
          Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of
          storing data.

          .. note::

             ``RequesterPays`` is a configuration for the S3 bucket that backs the file share, so
             make sure that the configuration on the file share is the same as the S3 bucket
             configuration.

        - **SMBACLEnabled** *(boolean) --*

          If this value is set to "true", indicates that ACL (access control list) is enabled on
          the SMB file share. If it is set to "false", it indicates that file and directory
          permissions are mapped to the POSIX permission.

          For more information, see
          https://docs.aws.amazon.com/storagegateway/latest/userguide/smb-acl.html in the Storage
          Gateway User Guide.

        - **AdminUserList** *(list) --*

          A list of users or groups in the Active Directory that have administrator rights to the
          file share. A group must be prefixed with the @ character. For example ``@group1`` . Can
          only be set if Authentication is set to ``ActiveDirectory`` .

          - *(string) --*

        - **ValidUserList** *(list) --*

          A list of users or groups in the Active Directory that are allowed to access the file
          share. A group must be prefixed with the @ character. For example ``@group1`` . Can only
          be set if Authentication is set to ``ActiveDirectory`` .

          - *(string) --*

        - **InvalidUserList** *(list) --*

          A list of users or groups in the Active Directory that are not allowed to access the file
          share. A group must be prefixed with the @ character. For example ``@group1`` . Can only
          be set if Authentication is set to ``ActiveDirectory`` .

          - *(string) --*

        - **Authentication** *(string) --*

          The authentication method of the file share.

          Valid values are ``ActiveDirectory`` or ``GuestAccess`` . The default is
          ``ActiveDirectory`` .

        - **Tags** *(list) --*

          A list of up to 50 tags assigned to the SMB file share, sorted alphabetically by key
          name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you
          can view all tags using the ``ListTagsForResource`` API operation.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the
            following characters: + - = . _ : /

            - **Key** *(string) --*

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --*

              Value of the tag key.
    """


_ClientDescribeSmbSettingsResponseTypeDef = TypedDict(
    "_ClientDescribeSmbSettingsResponseTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "SMBGuestPasswordSet": bool,
        "SMBSecurityStrategy": str,
    },
    total=False,
)


class ClientDescribeSmbSettingsResponseTypeDef(
    _ClientDescribeSmbSettingsResponseTypeDef
):
    """
    Type definition for `ClientDescribeSmbSettings` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **DomainName** *(string) --*

      The name of the domain that the gateway is joined to.

    - **SMBGuestPasswordSet** *(boolean) --*

      This value is true if a password for the guest user “smbguest” is set, and otherwise false.

    - **SMBSecurityStrategy** *(string) --*

      The type of security strategy that was specified for file gateway.

      ClientSpecified: if you use this option, requests are established based on what is negotiated
      by the client. This option is recommended when you want to maximize compatibility across
      different clients in your environment.

      MandatorySigning: if you use this option, file gateway only allows connections from SMBv2 or
      SMBv3 clients that have signing enabled. This option works with SMB clients on Microsoft
      Windows Vista, Windows Server 2008 or newer.

      MandatoryEncryption: if you use this option, file gateway only allows connections from SMBv3
      clients that have encryption enabled. This option is highly recommended for environments that
      handle sensitive data. This option works with SMB clients on Microsoft Windows 8, Windows
      Server 2012 or newer.
    """


_ClientDescribeSnapshotScheduleResponseTagsTypeDef = TypedDict(
    "_ClientDescribeSnapshotScheduleResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeSnapshotScheduleResponseTagsTypeDef(
    _ClientDescribeSnapshotScheduleResponseTagsTypeDef
):
    """
    Type definition for `ClientDescribeSnapshotScheduleResponse` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --*

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --*

      Value of the tag key.
    """


_ClientDescribeSnapshotScheduleResponseTypeDef = TypedDict(
    "_ClientDescribeSnapshotScheduleResponseTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
        "Description": str,
        "Timezone": str,
        "Tags": List[ClientDescribeSnapshotScheduleResponseTagsTypeDef],
    },
    total=False,
)


class ClientDescribeSnapshotScheduleResponseTypeDef(
    _ClientDescribeSnapshotScheduleResponseTypeDef
):
    """
    Type definition for `ClientDescribeSnapshotSchedule` `Response`

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume that was specified in the request.

    - **StartAt** *(integer) --*

      The hour of the day at which the snapshot schedule begins represented as *hh* , where *hh* is
      the hour (0 to 23). The hour of the day is in the time zone of the gateway.

    - **RecurrenceInHours** *(integer) --*

      The number of hours between snapshots.

    - **Description** *(string) --*

      The snapshot description.

    - **Timezone** *(string) --*

      A value that indicates the time zone of the gateway.

    - **Tags** *(list) --*

      A list of up to 50 tags assigned to the snapshot schedule, sorted alphabetically by key name.
      Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all
      tags using the ``ListTagsForResource`` API operation.

      - *(dict) --*

        A key-value pair that helps you manage, filter, and search for your resource. Allowed
        characters: letters, white space, and numbers, representable in UTF-8, and the following
        characters: + - = . _ : /

        - **Key** *(string) --*

          Tag key (String). The key can't start with aws:.

        - **Value** *(string) --*

          Value of the tag key.
    """


_ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef = TypedDict(
    "_ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "LunNumber": int,
        "ChapEnabled": bool,
    },
    total=False,
)


class ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef(
    _ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef
):
    """
    Type definition for `ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumes` `VolumeiSCSIAttributes`

    An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one
    stored volume.

    - **TargetARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume target.

    - **NetworkInterfaceId** *(string) --*

      The network interface identifier.

    - **NetworkInterfacePort** *(integer) --*

      The port used to communicate with iSCSI targets.

    - **LunNumber** *(integer) --*

      The logical disk number.

    - **ChapEnabled** *(boolean) --*

      Indicates whether mutual CHAP is enabled for the iSCSI target.
    """


_ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef = TypedDict(
    "_ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "VolumeDiskId": str,
        "SourceSnapshotId": str,
        "PreservedExistingData": bool,
        "VolumeiSCSIAttributes": ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef,
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)


class ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef(
    _ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef
):
    """
    Type definition for `ClientDescribeStoredIscsiVolumesResponse` `StorediSCSIVolumes`

    Describes an iSCSI stored volume.

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the storage volume.

    - **VolumeId** *(string) --*

      The unique identifier of the volume, e.g. vol-AE4B946D.

    - **VolumeType** *(string) --*

      One of the VolumeType enumeration values describing the type of the volume.

    - **VolumeStatus** *(string) --*

      One of the VolumeStatus values that indicates the state of the storage volume.

    - **VolumeAttachmentStatus** *(string) --*

      A value that indicates whether a storage volume is attached to, detached from, or is in
      the process of detaching from a gateway. For more information, see `Moving Your Volumes
      to a Different Gateway
      <https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#attach-detach-volume>`__
      .

    - **VolumeSizeInBytes** *(integer) --*

      The size of the volume in bytes.

    - **VolumeProgress** *(float) --*

      Represents the percentage complete if the volume is restoring or bootstrapping that
      represents the percent of data transferred. This field does not appear in the response if
      the stored volume is not restoring or bootstrapping.

    - **VolumeDiskId** *(string) --*

      The ID of the local disk that was specified in the  CreateStorediSCSIVolume operation.

    - **SourceSnapshotId** *(string) --*

      If the stored volume was created from a snapshot, this field contains the snapshot ID
      used, e.g. snap-78e22663. Otherwise, this field is not included.

    - **PreservedExistingData** *(boolean) --*

      Indicates if when the stored volume was created, existing data on the underlying local
      disk was preserved.

      Valid Values: true, false

    - **VolumeiSCSIAttributes** *(dict) --*

      An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one
      stored volume.

      - **TargetARN** *(string) --*

        The Amazon Resource Name (ARN) of the volume target.

      - **NetworkInterfaceId** *(string) --*

        The network interface identifier.

      - **NetworkInterfacePort** *(integer) --*

        The port used to communicate with iSCSI targets.

      - **LunNumber** *(integer) --*

        The logical disk number.

      - **ChapEnabled** *(boolean) --*

        Indicates whether mutual CHAP is enabled for the iSCSI target.

    - **CreatedDate** *(datetime) --*

      The date the volume was created. Volumes created prior to March 28, 2017 don’t have this
      time stamp.

    - **VolumeUsedInBytes** *(integer) --*

      The size of the data stored on the volume in bytes. This value is calculated based on the
      number of blocks that are touched, instead of the actual amount of data written. This
      value can be useful for sequential write patterns but less accurate for random write
      patterns. ``VolumeUsedInBytes`` is different from the compressed size of the volume,
      which is the value that is used to calculate your bill.

      .. note::

        This value is not available for volumes created prior to May 13, 2015, until you store
        data on the volume.

    - **KMSKey** *(string) --*

      The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
      encryption. This value can only be set when KMSEncrypted is true. Optional.

    - **TargetName** *(string) --*

      The name of the iSCSI target used by an initiator to connect to a volume and used as a
      suffix for the target ARN. For example, specifying ``TargetName`` as *myvolume* results
      in the target ARN of
      ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume``
      . The target name must be unique across all volumes on a gateway.

      If you don't specify a value, Storage Gateway uses the value that was previously used for
      this volume as the new target name.
    """


_ClientDescribeStoredIscsiVolumesResponseTypeDef = TypedDict(
    "_ClientDescribeStoredIscsiVolumesResponseTypeDef",
    {
        "StorediSCSIVolumes": List[
            ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeStoredIscsiVolumesResponseTypeDef(
    _ClientDescribeStoredIscsiVolumesResponseTypeDef
):
    """
    Type definition for `ClientDescribeStoredIscsiVolumes` `Response`

    - **StorediSCSIVolumes** *(list) --*

      Describes a single unit of output from  DescribeStorediSCSIVolumes . The following fields are
      returned:

      * **ChapEnabled** : Indicates whether mutual CHAP is enabled for the iSCSI target.

      * **LunNumber** : The logical disk number.

      * **NetworkInterfaceId** : The network interface ID of the stored volume that initiator use
      to map the stored volume as an iSCSI target.

      * **NetworkInterfacePort** : The port used to communicate with iSCSI targets.

      * **PreservedExistingData** : Indicates if when the stored volume was created, existing data
      on the underlying local disk was preserved.

      * **SourceSnapshotId** : If the stored volume was created from a snapshot, this field
      contains the snapshot ID used, e.g. snap-1122aabb. Otherwise, this field is not included.

      * **StorediSCSIVolumes** : An array of StorediSCSIVolume objects where each object contains
      metadata about one stored volume.

      * **TargetARN** : The Amazon Resource Name (ARN) of the volume target.

      * **VolumeARN** : The Amazon Resource Name (ARN) of the stored volume.

      * **VolumeDiskId** : The disk ID of the local disk that was specified in the
      CreateStorediSCSIVolume operation.

      * **VolumeId** : The unique identifier of the storage volume, e.g. vol-1122AABB.

      * **VolumeiSCSIAttributes** : An  VolumeiSCSIAttributes object that represents a collection
      of iSCSI attributes for one stored volume.

      * **VolumeProgress** : Represents the percentage complete if the volume is restoring or
      bootstrapping that represents the percent of data transferred. This field does not appear in
      the response if the stored volume is not restoring or bootstrapping.

      * **VolumeSizeInBytes** : The size of the volume in bytes.

      * **VolumeStatus** : One of the ``VolumeStatus`` values that indicates the state of the
      volume.

      * **VolumeType** : One of the enumeration values describing the type of the volume.
      Currently, on STORED volumes are supported.

      - *(dict) --*

        Describes an iSCSI stored volume.

        - **VolumeARN** *(string) --*

          The Amazon Resource Name (ARN) of the storage volume.

        - **VolumeId** *(string) --*

          The unique identifier of the volume, e.g. vol-AE4B946D.

        - **VolumeType** *(string) --*

          One of the VolumeType enumeration values describing the type of the volume.

        - **VolumeStatus** *(string) --*

          One of the VolumeStatus values that indicates the state of the storage volume.

        - **VolumeAttachmentStatus** *(string) --*

          A value that indicates whether a storage volume is attached to, detached from, or is in
          the process of detaching from a gateway. For more information, see `Moving Your Volumes
          to a Different Gateway
          <https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#attach-detach-volume>`__
          .

        - **VolumeSizeInBytes** *(integer) --*

          The size of the volume in bytes.

        - **VolumeProgress** *(float) --*

          Represents the percentage complete if the volume is restoring or bootstrapping that
          represents the percent of data transferred. This field does not appear in the response if
          the stored volume is not restoring or bootstrapping.

        - **VolumeDiskId** *(string) --*

          The ID of the local disk that was specified in the  CreateStorediSCSIVolume operation.

        - **SourceSnapshotId** *(string) --*

          If the stored volume was created from a snapshot, this field contains the snapshot ID
          used, e.g. snap-78e22663. Otherwise, this field is not included.

        - **PreservedExistingData** *(boolean) --*

          Indicates if when the stored volume was created, existing data on the underlying local
          disk was preserved.

          Valid Values: true, false

        - **VolumeiSCSIAttributes** *(dict) --*

          An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one
          stored volume.

          - **TargetARN** *(string) --*

            The Amazon Resource Name (ARN) of the volume target.

          - **NetworkInterfaceId** *(string) --*

            The network interface identifier.

          - **NetworkInterfacePort** *(integer) --*

            The port used to communicate with iSCSI targets.

          - **LunNumber** *(integer) --*

            The logical disk number.

          - **ChapEnabled** *(boolean) --*

            Indicates whether mutual CHAP is enabled for the iSCSI target.

        - **CreatedDate** *(datetime) --*

          The date the volume was created. Volumes created prior to March 28, 2017 don’t have this
          time stamp.

        - **VolumeUsedInBytes** *(integer) --*

          The size of the data stored on the volume in bytes. This value is calculated based on the
          number of blocks that are touched, instead of the actual amount of data written. This
          value can be useful for sequential write patterns but less accurate for random write
          patterns. ``VolumeUsedInBytes`` is different from the compressed size of the volume,
          which is the value that is used to calculate your bill.

          .. note::

            This value is not available for volumes created prior to May 13, 2015, until you store
            data on the volume.

        - **KMSKey** *(string) --*

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        - **TargetName** *(string) --*

          The name of the iSCSI target used by an initiator to connect to a volume and used as a
          suffix for the target ARN. For example, specifying ``TargetName`` as *myvolume* results
          in the target ARN of
          ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume``
          . The target name must be unique across all volumes on a gateway.

          If you don't specify a value, Storage Gateway uses the value that was previously used for
          this volume as the new target name.
    """


_ClientDescribeTapeArchivesResponseTapeArchivesTypeDef = TypedDict(
    "_ClientDescribeTapeArchivesResponseTapeArchivesTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "CompletionTime": datetime,
        "RetrievedTo": str,
        "TapeStatus": str,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)


class ClientDescribeTapeArchivesResponseTapeArchivesTypeDef(
    _ClientDescribeTapeArchivesResponseTapeArchivesTypeDef
):
    """
    Type definition for `ClientDescribeTapeArchivesResponse` `TapeArchives`

    Represents a virtual tape that is archived in the virtual tape shelf (VTS).

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of an archived virtual tape.

    - **TapeBarcode** *(string) --*

      The barcode that identifies the archived virtual tape.

    - **TapeCreatedDate** *(datetime) --*

      The date the virtual tape was created.

    - **TapeSizeInBytes** *(integer) --*

      The size, in bytes, of the archived virtual tape.

    - **CompletionTime** *(datetime) --*

      The time that the archiving of the virtual tape was completed.

      The default time stamp format is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.

    - **RetrievedTo** *(string) --*

      The Amazon Resource Name (ARN) of the tape gateway that the virtual tape is being
      retrieved to.

      The virtual tape is retrieved from the virtual tape shelf (VTS).

    - **TapeStatus** *(string) --*

      The current state of the archived virtual tape.

    - **TapeUsedInBytes** *(integer) --*

      The size, in bytes, of data stored on the virtual tape.

      .. note::

        This value is not available for tapes created prior to May 13, 2015.

    - **KMSKey** *(string) --*

      The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
      encryption. This value can only be set when KMSEncrypted is true. Optional.

    - **PoolId** *(string) --*

      The ID of the pool that was used to archive the tape. The tapes in this pool are archived
      in the S3 storage class that is associated with the pool.

      Valid values: "GLACIER", "DEEP_ARCHIVE"
    """


_ClientDescribeTapeArchivesResponseTypeDef = TypedDict(
    "_ClientDescribeTapeArchivesResponseTypeDef",
    {
        "TapeArchives": List[ClientDescribeTapeArchivesResponseTapeArchivesTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeTapeArchivesResponseTypeDef(
    _ClientDescribeTapeArchivesResponseTypeDef
):
    """
    Type definition for `ClientDescribeTapeArchives` `Response`

    DescribeTapeArchivesOutput

    - **TapeArchives** *(list) --*

      An array of virtual tape objects in the virtual tape shelf (VTS). The description includes of
      the Amazon Resource Name (ARN) of the virtual tapes. The information returned includes the
      Amazon Resource Names (ARNs) of the tapes, size of the tapes, status of the tapes, progress
      of the description and tape barcode.

      - *(dict) --*

        Represents a virtual tape that is archived in the virtual tape shelf (VTS).

        - **TapeARN** *(string) --*

          The Amazon Resource Name (ARN) of an archived virtual tape.

        - **TapeBarcode** *(string) --*

          The barcode that identifies the archived virtual tape.

        - **TapeCreatedDate** *(datetime) --*

          The date the virtual tape was created.

        - **TapeSizeInBytes** *(integer) --*

          The size, in bytes, of the archived virtual tape.

        - **CompletionTime** *(datetime) --*

          The time that the archiving of the virtual tape was completed.

          The default time stamp format is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.

        - **RetrievedTo** *(string) --*

          The Amazon Resource Name (ARN) of the tape gateway that the virtual tape is being
          retrieved to.

          The virtual tape is retrieved from the virtual tape shelf (VTS).

        - **TapeStatus** *(string) --*

          The current state of the archived virtual tape.

        - **TapeUsedInBytes** *(integer) --*

          The size, in bytes, of data stored on the virtual tape.

          .. note::

            This value is not available for tapes created prior to May 13, 2015.

        - **KMSKey** *(string) --*

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        - **PoolId** *(string) --*

          The ID of the pool that was used to archive the tape. The tapes in this pool are archived
          in the S3 storage class that is associated with the pool.

          Valid values: "GLACIER", "DEEP_ARCHIVE"

    - **Marker** *(string) --*

      An opaque string that indicates the position at which the virtual tapes that were fetched for
      description ended. Use this marker in your next request to fetch the next set of virtual
      tapes in the virtual tape shelf (VTS). If there are no more virtual tapes to describe, this
      field does not appear in the response.
    """


_ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef = TypedDict(
    "_ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef",
    {
        "TapeARN": str,
        "TapeRecoveryPointTime": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
    },
    total=False,
)


class ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef(
    _ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef
):
    """
    Type definition for `ClientDescribeTapeRecoveryPointsResponse` `TapeRecoveryPointInfos`

    Describes a recovery point.

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of the virtual tape.

    - **TapeRecoveryPointTime** *(datetime) --*

      The time when the point-in-time view of the virtual tape was replicated for later
      recovery.

      The default time stamp format of the tape recovery point time is in the ISO8601 extended
      YYYY-MM-DD'T'HH:MM:SS'Z' format.

    - **TapeSizeInBytes** *(integer) --*

      The size, in bytes, of the virtual tapes to recover.

    - **TapeStatus** *(string) --*

      The status of the virtual tapes.
    """


_ClientDescribeTapeRecoveryPointsResponseTypeDef = TypedDict(
    "_ClientDescribeTapeRecoveryPointsResponseTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List[
            ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeTapeRecoveryPointsResponseTypeDef(
    _ClientDescribeTapeRecoveryPointsResponseTypeDef
):
    """
    Type definition for `ClientDescribeTapeRecoveryPoints` `Response`

    DescribeTapeRecoveryPointsOutput

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **TapeRecoveryPointInfos** *(list) --*

      An array of TapeRecoveryPointInfos that are available for the specified gateway.

      - *(dict) --*

        Describes a recovery point.

        - **TapeARN** *(string) --*

          The Amazon Resource Name (ARN) of the virtual tape.

        - **TapeRecoveryPointTime** *(datetime) --*

          The time when the point-in-time view of the virtual tape was replicated for later
          recovery.

          The default time stamp format of the tape recovery point time is in the ISO8601 extended
          YYYY-MM-DD'T'HH:MM:SS'Z' format.

        - **TapeSizeInBytes** *(integer) --*

          The size, in bytes, of the virtual tapes to recover.

        - **TapeStatus** *(string) --*

          The status of the virtual tapes.

    - **Marker** *(string) --*

      An opaque string that indicates the position at which the virtual tape recovery points that
      were listed for description ended.

      Use this marker in your next request to list the next set of virtual tape recovery points in
      the list. If there are no more recovery points to describe, this field does not appear in the
      response.
    """


_ClientDescribeTapesResponseTapesTypeDef = TypedDict(
    "_ClientDescribeTapesResponseTapesTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "VTLDevice": str,
        "Progress": float,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)


class ClientDescribeTapesResponseTapesTypeDef(_ClientDescribeTapesResponseTapesTypeDef):
    """
    Type definition for `ClientDescribeTapesResponse` `Tapes`

    Describes a virtual tape object.

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of the virtual tape.

    - **TapeBarcode** *(string) --*

      The barcode that identifies a specific virtual tape.

    - **TapeCreatedDate** *(datetime) --*

      The date the virtual tape was created.

    - **TapeSizeInBytes** *(integer) --*

      The size, in bytes, of the virtual tape capacity.

    - **TapeStatus** *(string) --*

      The current state of the virtual tape.

    - **VTLDevice** *(string) --*

      The virtual tape library (VTL) device that the virtual tape is associated with.

    - **Progress** *(float) --*

      For archiving virtual tapes, indicates how much data remains to be uploaded before
      archiving is complete.

      Range: 0 (not started) to 100 (complete).

    - **TapeUsedInBytes** *(integer) --*

      The size, in bytes, of data stored on the virtual tape.

      .. note::

        This value is not available for tapes created prior to May 13, 2015.

    - **KMSKey** *(string) --*

      The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
      encryption. This value can only be set when KMSEncrypted is true. Optional.

    - **PoolId** *(string) --*

      The ID of the pool that contains tapes that will be archived. The tapes in this pool are
      archived in the S3 storage class that is associated with the pool. When you use your
      backup application to eject the tape, the tape is archived directly into the storage
      class (Glacier or Deep Archive) that corresponds to the pool.

      Valid values: "GLACIER", "DEEP_ARCHIVE"
    """


_ClientDescribeTapesResponseTypeDef = TypedDict(
    "_ClientDescribeTapesResponseTypeDef",
    {"Tapes": List[ClientDescribeTapesResponseTapesTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeTapesResponseTypeDef(_ClientDescribeTapesResponseTypeDef):
    """
    Type definition for `ClientDescribeTapes` `Response`

    DescribeTapesOutput

    - **Tapes** *(list) --*

      An array of virtual tape descriptions.

      - *(dict) --*

        Describes a virtual tape object.

        - **TapeARN** *(string) --*

          The Amazon Resource Name (ARN) of the virtual tape.

        - **TapeBarcode** *(string) --*

          The barcode that identifies a specific virtual tape.

        - **TapeCreatedDate** *(datetime) --*

          The date the virtual tape was created.

        - **TapeSizeInBytes** *(integer) --*

          The size, in bytes, of the virtual tape capacity.

        - **TapeStatus** *(string) --*

          The current state of the virtual tape.

        - **VTLDevice** *(string) --*

          The virtual tape library (VTL) device that the virtual tape is associated with.

        - **Progress** *(float) --*

          For archiving virtual tapes, indicates how much data remains to be uploaded before
          archiving is complete.

          Range: 0 (not started) to 100 (complete).

        - **TapeUsedInBytes** *(integer) --*

          The size, in bytes, of data stored on the virtual tape.

          .. note::

            This value is not available for tapes created prior to May 13, 2015.

        - **KMSKey** *(string) --*

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        - **PoolId** *(string) --*

          The ID of the pool that contains tapes that will be archived. The tapes in this pool are
          archived in the S3 storage class that is associated with the pool. When you use your
          backup application to eject the tape, the tape is archived directly into the storage
          class (Glacier or Deep Archive) that corresponds to the pool.

          Valid values: "GLACIER", "DEEP_ARCHIVE"

    - **Marker** *(string) --*

      An opaque string which can be used as part of a subsequent DescribeTapes call to retrieve the
      next page of results.

      If a response does not contain a marker, then there are no more results to be retrieved.
    """


_ClientDescribeUploadBufferResponseTypeDef = TypedDict(
    "_ClientDescribeUploadBufferResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "UploadBufferUsedInBytes": int,
        "UploadBufferAllocatedInBytes": int,
    },
    total=False,
)


class ClientDescribeUploadBufferResponseTypeDef(
    _ClientDescribeUploadBufferResponseTypeDef
):
    """
    Type definition for `ClientDescribeUploadBuffer` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **DiskIds** *(list) --*

      An array of the gateway's local disk IDs that are configured as working storage. Each local
      disk ID is specified as a string (minimum length of 1 and maximum length of 300). If no local
      disks are configured as working storage, then the DiskIds array is empty.

      - *(string) --*

    - **UploadBufferUsedInBytes** *(integer) --*

      The total number of bytes being used in the gateway's upload buffer.

    - **UploadBufferAllocatedInBytes** *(integer) --*

      The total number of bytes allocated in the gateway's as upload buffer.
    """


_ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef = TypedDict(
    "_ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "ChapEnabled": bool,
    },
    total=False,
)


class ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef(
    _ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef
):
    """
    Type definition for `ClientDescribeVtlDevicesResponseVTLDevices` `DeviceiSCSIAttributes`

    A list of iSCSI information about a VTL device.

    - **TargetARN** *(string) --*

      Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified
      name(iqn) of a tape drive or media changer target.

    - **NetworkInterfaceId** *(string) --*

      The network interface identifier of the VTL device.

    - **NetworkInterfacePort** *(integer) --*

      The port used to communicate with iSCSI VTL device targets.

    - **ChapEnabled** *(boolean) --*

      Indicates whether mutual CHAP is enabled for the iSCSI target.
    """


_ClientDescribeVtlDevicesResponseVTLDevicesTypeDef = TypedDict(
    "_ClientDescribeVtlDevicesResponseVTLDevicesTypeDef",
    {
        "VTLDeviceARN": str,
        "VTLDeviceType": str,
        "VTLDeviceVendor": str,
        "VTLDeviceProductIdentifier": str,
        "DeviceiSCSIAttributes": ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef,
    },
    total=False,
)


class ClientDescribeVtlDevicesResponseVTLDevicesTypeDef(
    _ClientDescribeVtlDevicesResponseVTLDevicesTypeDef
):
    """
    Type definition for `ClientDescribeVtlDevicesResponse` `VTLDevices`

    Represents a device object associated with a tape gateway.

    - **VTLDeviceARN** *(string) --*

      Specifies the unique Amazon Resource Name (ARN) of the device (tape drive or media
      changer).

    - **VTLDeviceType** *(string) --*

      Specifies the type of device that the VTL device emulates.

    - **VTLDeviceVendor** *(string) --*

      Specifies the vendor of the device that the VTL device object emulates.

    - **VTLDeviceProductIdentifier** *(string) --*

      Specifies the model number of device that the VTL device emulates.

    - **DeviceiSCSIAttributes** *(dict) --*

      A list of iSCSI information about a VTL device.

      - **TargetARN** *(string) --*

        Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified
        name(iqn) of a tape drive or media changer target.

      - **NetworkInterfaceId** *(string) --*

        The network interface identifier of the VTL device.

      - **NetworkInterfacePort** *(integer) --*

        The port used to communicate with iSCSI VTL device targets.

      - **ChapEnabled** *(boolean) --*

        Indicates whether mutual CHAP is enabled for the iSCSI target.
    """


_ClientDescribeVtlDevicesResponseTypeDef = TypedDict(
    "_ClientDescribeVtlDevicesResponseTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List[ClientDescribeVtlDevicesResponseVTLDevicesTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeVtlDevicesResponseTypeDef(_ClientDescribeVtlDevicesResponseTypeDef):
    """
    Type definition for `ClientDescribeVtlDevices` `Response`

    DescribeVTLDevicesOutput

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **VTLDevices** *(list) --*

      An array of VTL device objects composed of the Amazon Resource Name(ARN) of the VTL devices.

      - *(dict) --*

        Represents a device object associated with a tape gateway.

        - **VTLDeviceARN** *(string) --*

          Specifies the unique Amazon Resource Name (ARN) of the device (tape drive or media
          changer).

        - **VTLDeviceType** *(string) --*

          Specifies the type of device that the VTL device emulates.

        - **VTLDeviceVendor** *(string) --*

          Specifies the vendor of the device that the VTL device object emulates.

        - **VTLDeviceProductIdentifier** *(string) --*

          Specifies the model number of device that the VTL device emulates.

        - **DeviceiSCSIAttributes** *(dict) --*

          A list of iSCSI information about a VTL device.

          - **TargetARN** *(string) --*

            Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified
            name(iqn) of a tape drive or media changer target.

          - **NetworkInterfaceId** *(string) --*

            The network interface identifier of the VTL device.

          - **NetworkInterfacePort** *(integer) --*

            The port used to communicate with iSCSI VTL device targets.

          - **ChapEnabled** *(boolean) --*

            Indicates whether mutual CHAP is enabled for the iSCSI target.

    - **Marker** *(string) --*

      An opaque string that indicates the position at which the VTL devices that were fetched for
      description ended. Use the marker in your next request to fetch the next set of VTL devices
      in the list. If there are no more VTL devices to describe, this field does not appear in the
      response.
    """


_ClientDescribeWorkingStorageResponseTypeDef = TypedDict(
    "_ClientDescribeWorkingStorageResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "WorkingStorageUsedInBytes": int,
        "WorkingStorageAllocatedInBytes": int,
    },
    total=False,
)


class ClientDescribeWorkingStorageResponseTypeDef(
    _ClientDescribeWorkingStorageResponseTypeDef
):
    """
    Type definition for `ClientDescribeWorkingStorage` `Response`

    A JSON object containing the following fields:

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **DiskIds** *(list) --*

      An array of the gateway's local disk IDs that are configured as working storage. Each local
      disk ID is specified as a string (minimum length of 1 and maximum length of 300). If no local
      disks are configured as working storage, then the DiskIds array is empty.

      - *(string) --*

    - **WorkingStorageUsedInBytes** *(integer) --*

      The total working storage in bytes in use by the gateway. If no working storage is configured
      for the gateway, this field returns 0.

    - **WorkingStorageAllocatedInBytes** *(integer) --*

      The total working storage in bytes allocated for the gateway. If no working storage is
      configured for the gateway, this field returns 0.
    """


_ClientDetachVolumeResponseTypeDef = TypedDict(
    "_ClientDetachVolumeResponseTypeDef", {"VolumeARN": str}, total=False
)


class ClientDetachVolumeResponseTypeDef(_ClientDetachVolumeResponseTypeDef):
    """
    Type definition for `ClientDetachVolume` `Response`

    AttachVolumeOutput

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume that was detached.
    """


_ClientDisableGatewayResponseTypeDef = TypedDict(
    "_ClientDisableGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientDisableGatewayResponseTypeDef(_ClientDisableGatewayResponseTypeDef):
    """
    Type definition for `ClientDisableGateway` `Response`

    DisableGatewayOutput

    - **GatewayARN** *(string) --*

      The unique Amazon Resource Name (ARN) of the disabled gateway.
    """


_ClientJoinDomainResponseTypeDef = TypedDict(
    "_ClientJoinDomainResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientJoinDomainResponseTypeDef(_ClientJoinDomainResponseTypeDef):
    """
    Type definition for `ClientJoinDomain` `Response`

    JoinDomainOutput

    - **GatewayARN** *(string) --*

      The unique Amazon Resource Name (ARN) of the gateway that joined the domain.
    """


_ClientListFileSharesResponseFileShareInfoListTypeDef = TypedDict(
    "_ClientListFileSharesResponseFileShareInfoListTypeDef",
    {
        "FileShareType": str,
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
    },
    total=False,
)


class ClientListFileSharesResponseFileShareInfoListTypeDef(
    _ClientListFileSharesResponseFileShareInfoListTypeDef
):
    """
    Type definition for `ClientListFileSharesResponse` `FileShareInfoList`

    Describes a file share.

    - **FileShareType** *(string) --*

      The type of the file share.

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the file share.

    - **FileShareId** *(string) --*

      The ID of the file share.

    - **FileShareStatus** *(string) --*

      The status of the file share. Possible values are ``CREATING`` , ``UPDATING`` ,
      ``AVAILABLE`` and ``DELETING`` .

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
      a list of gateways for your account and AWS Region.
    """


_ClientListFileSharesResponseTypeDef = TypedDict(
    "_ClientListFileSharesResponseTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileShareInfoList": List[ClientListFileSharesResponseFileShareInfoListTypeDef],
    },
    total=False,
)


class ClientListFileSharesResponseTypeDef(_ClientListFileSharesResponseTypeDef):
    """
    Type definition for `ClientListFileShares` `Response`

    ListFileShareOutput

    - **Marker** *(string) --*

      If the request includes ``Marker`` , the response returns that value in this field.

    - **NextMarker** *(string) --*

      If a value is present, there are more file shares to return. In a subsequent request, use
      ``NextMarker`` as the value for ``Marker`` to retrieve the next set of file shares.

    - **FileShareInfoList** *(list) --*

      An array of information about the file gateway's file shares.

      - *(dict) --*

        Describes a file share.

        - **FileShareType** *(string) --*

          The type of the file share.

        - **FileShareARN** *(string) --*

          The Amazon Resource Name (ARN) of the file share.

        - **FileShareId** *(string) --*

          The ID of the file share.

        - **FileShareStatus** *(string) --*

          The status of the file share. Possible values are ``CREATING`` , ``UPDATING`` ,
          ``AVAILABLE`` and ``DELETING`` .

        - **GatewayARN** *(string) --*

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
          a list of gateways for your account and AWS Region.
    """


_ClientListGatewaysResponseGatewaysTypeDef = TypedDict(
    "_ClientListGatewaysResponseGatewaysTypeDef",
    {
        "GatewayId": str,
        "GatewayARN": str,
        "GatewayType": str,
        "GatewayOperationalState": str,
        "GatewayName": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
    },
    total=False,
)


class ClientListGatewaysResponseGatewaysTypeDef(
    _ClientListGatewaysResponseGatewaysTypeDef
):
    """
    Type definition for `ClientListGatewaysResponse` `Gateways`

    Describes a gateway object.

    - **GatewayId** *(string) --*

      The unique identifier assigned to your gateway during activation. This ID becomes part of
      the gateway Amazon Resource Name (ARN), which you use as input for other operations.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
      a list of gateways for your account and AWS Region.

    - **GatewayType** *(string) --*

      The type of the gateway.

    - **GatewayOperationalState** *(string) --*

      The state of the gateway.

      Valid Values: DISABLED or ACTIVE

    - **GatewayName** *(string) --*

      The name of the gateway.

    - **Ec2InstanceId** *(string) --*

      The ID of the Amazon EC2 instance that was used to launch the gateway.

    - **Ec2InstanceRegion** *(string) --*

      The AWS Region where the Amazon EC2 instance is located.
    """


_ClientListGatewaysResponseTypeDef = TypedDict(
    "_ClientListGatewaysResponseTypeDef",
    {"Gateways": List[ClientListGatewaysResponseGatewaysTypeDef], "Marker": str},
    total=False,
)


class ClientListGatewaysResponseTypeDef(_ClientListGatewaysResponseTypeDef):
    """
    Type definition for `ClientListGateways` `Response`

    - **Gateways** *(list) --*

      An array of  GatewayInfo objects.

      - *(dict) --*

        Describes a gateway object.

        - **GatewayId** *(string) --*

          The unique identifier assigned to your gateway during activation. This ID becomes part of
          the gateway Amazon Resource Name (ARN), which you use as input for other operations.

        - **GatewayARN** *(string) --*

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
          a list of gateways for your account and AWS Region.

        - **GatewayType** *(string) --*

          The type of the gateway.

        - **GatewayOperationalState** *(string) --*

          The state of the gateway.

          Valid Values: DISABLED or ACTIVE

        - **GatewayName** *(string) --*

          The name of the gateway.

        - **Ec2InstanceId** *(string) --*

          The ID of the Amazon EC2 instance that was used to launch the gateway.

        - **Ec2InstanceRegion** *(string) --*

          The AWS Region where the Amazon EC2 instance is located.

    - **Marker** *(string) --*

      Use the marker in your next request to fetch the next set of gateways in the list. If there
      are no more gateways to list, this field does not appear in the response.
    """


_ClientListLocalDisksResponseDisksTypeDef = TypedDict(
    "_ClientListLocalDisksResponseDisksTypeDef",
    {
        "DiskId": str,
        "DiskPath": str,
        "DiskNode": str,
        "DiskStatus": str,
        "DiskSizeInBytes": int,
        "DiskAllocationType": str,
        "DiskAllocationResource": str,
        "DiskAttributeList": List[str],
    },
    total=False,
)


class ClientListLocalDisksResponseDisksTypeDef(
    _ClientListLocalDisksResponseDisksTypeDef
):
    """
    Type definition for `ClientListLocalDisksResponse` `Disks`

    Represents a gateway's local disk.

    - **DiskId** *(string) --*

      The unique device ID or other distinguishing data that identifies a local disk.

    - **DiskPath** *(string) --*

      The path of a local disk in the gateway virtual machine (VM).

    - **DiskNode** *(string) --*

      The device node of a local disk as assigned by the virtualization environment.

    - **DiskStatus** *(string) --*

      A value that represents the status of a local disk.

    - **DiskSizeInBytes** *(integer) --*

      The local disk size in bytes.

    - **DiskAllocationType** *(string) --*

      One of the ``DiskAllocationType`` enumeration values that identifies how a local disk is
      used. Valid values: ``UPLOAD_BUFFER`` , ``CACHE_STORAGE``

    - **DiskAllocationResource** *(string) --*

      The iSCSI qualified name (IQN) that is defined for a disk. This field is not included in
      the response if the local disk is not defined as an iSCSI target. The format of this
      field is *targetIqn::LUNNumber::region-volumeId* .

    - **DiskAttributeList** *(list) --*

      A list of values that represents attributes of a local disk.

      - *(string) --*
    """


_ClientListLocalDisksResponseTypeDef = TypedDict(
    "_ClientListLocalDisksResponseTypeDef",
    {"GatewayARN": str, "Disks": List[ClientListLocalDisksResponseDisksTypeDef]},
    total=False,
)


class ClientListLocalDisksResponseTypeDef(_ClientListLocalDisksResponseTypeDef):
    """
    Type definition for `ClientListLocalDisks` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **Disks** *(list) --*

      A JSON object containing the following fields:

      *  ListLocalDisksOutput$Disks

      - *(dict) --*

        Represents a gateway's local disk.

        - **DiskId** *(string) --*

          The unique device ID or other distinguishing data that identifies a local disk.

        - **DiskPath** *(string) --*

          The path of a local disk in the gateway virtual machine (VM).

        - **DiskNode** *(string) --*

          The device node of a local disk as assigned by the virtualization environment.

        - **DiskStatus** *(string) --*

          A value that represents the status of a local disk.

        - **DiskSizeInBytes** *(integer) --*

          The local disk size in bytes.

        - **DiskAllocationType** *(string) --*

          One of the ``DiskAllocationType`` enumeration values that identifies how a local disk is
          used. Valid values: ``UPLOAD_BUFFER`` , ``CACHE_STORAGE``

        - **DiskAllocationResource** *(string) --*

          The iSCSI qualified name (IQN) that is defined for a disk. This field is not included in
          the response if the local disk is not defined as an iSCSI target. The format of this
          field is *targetIqn::LUNNumber::region-volumeId* .

        - **DiskAttributeList** *(list) --*

          A list of values that represents attributes of a local disk.

          - *(string) --*
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --*

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --*

      Value of the tag key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {
        "ResourceARN": str,
        "Marker": str,
        "Tags": List[ClientListTagsForResourceResponseTagsTypeDef],
    },
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    ListTagsForResourceOutput

    - **ResourceARN** *(string) --*

      he Amazon Resource Name (ARN) of the resource for which you want to list tags.

    - **Marker** *(string) --*

      An opaque string that indicates the position at which to stop returning the list of tags.

    - **Tags** *(list) --*

      An array that contains the tags for the specified resource.

      - *(dict) --*

        A key-value pair that helps you manage, filter, and search for your resource. Allowed
        characters: letters, white space, and numbers, representable in UTF-8, and the following
        characters: + - = . _ : /

        - **Key** *(string) --*

          Tag key (String). The key can't start with aws:.

        - **Value** *(string) --*

          Value of the tag key.
    """


_ClientListTapesResponseTapeInfosTypeDef = TypedDict(
    "_ClientListTapesResponseTapeInfosTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "GatewayARN": str,
        "PoolId": str,
    },
    total=False,
)


class ClientListTapesResponseTapeInfosTypeDef(_ClientListTapesResponseTapeInfosTypeDef):
    """
    Type definition for `ClientListTapesResponse` `TapeInfos`

    Describes a virtual tape.

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of a virtual tape.

    - **TapeBarcode** *(string) --*

      The barcode that identifies a specific virtual tape.

    - **TapeSizeInBytes** *(integer) --*

      The size, in bytes, of a virtual tape.

    - **TapeStatus** *(string) --*

      The status of the tape.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
      a list of gateways for your account and AWS Region.

    - **PoolId** *(string) --*

      The ID of the pool that you want to add your tape to for archiving. The tape in this pool
      is archived in the S3 storage class that is associated with the pool. When you use your
      backup application to eject the tape, the tape is archived directly into the storage
      class (Glacier or Deep Archive) that corresponds to the pool.

      Valid values: "GLACIER", "DEEP_ARCHIVE"
    """


_ClientListTapesResponseTypeDef = TypedDict(
    "_ClientListTapesResponseTypeDef",
    {"TapeInfos": List[ClientListTapesResponseTapeInfosTypeDef], "Marker": str},
    total=False,
)


class ClientListTapesResponseTypeDef(_ClientListTapesResponseTypeDef):
    """
    Type definition for `ClientListTapes` `Response`

    A JSON object containing the following fields:

    *  ListTapesOutput$Marker

    *  ListTapesOutput$VolumeInfos

    - **TapeInfos** *(list) --*

      An array of  TapeInfo objects, where each object describes an a single tape. If there not
      tapes in the tape library or VTS, then the ``TapeInfos`` is an empty array.

      - *(dict) --*

        Describes a virtual tape.

        - **TapeARN** *(string) --*

          The Amazon Resource Name (ARN) of a virtual tape.

        - **TapeBarcode** *(string) --*

          The barcode that identifies a specific virtual tape.

        - **TapeSizeInBytes** *(integer) --*

          The size, in bytes, of a virtual tape.

        - **TapeStatus** *(string) --*

          The status of the tape.

        - **GatewayARN** *(string) --*

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
          a list of gateways for your account and AWS Region.

        - **PoolId** *(string) --*

          The ID of the pool that you want to add your tape to for archiving. The tape in this pool
          is archived in the S3 storage class that is associated with the pool. When you use your
          backup application to eject the tape, the tape is archived directly into the storage
          class (Glacier or Deep Archive) that corresponds to the pool.

          Valid values: "GLACIER", "DEEP_ARCHIVE"

    - **Marker** *(string) --*

      A string that indicates the position at which to begin returning the next list of tapes. Use
      the marker in your next request to continue pagination of tapes. If there are no more tapes
      to list, this element does not appear in the response body.
    """


_ClientListVolumeInitiatorsResponseTypeDef = TypedDict(
    "_ClientListVolumeInitiatorsResponseTypeDef", {"Initiators": List[str]}, total=False
)


class ClientListVolumeInitiatorsResponseTypeDef(
    _ClientListVolumeInitiatorsResponseTypeDef
):
    """
    Type definition for `ClientListVolumeInitiators` `Response`

    ListVolumeInitiatorsOutput

    - **Initiators** *(list) --*

      The host names and port numbers of all iSCSI initiators that are connected to the gateway.

      - *(string) --*
    """


_ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef = TypedDict(
    "_ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "VolumeUsageInBytes": int,
        "VolumeRecoveryPointTime": str,
    },
    total=False,
)


class ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef(
    _ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef
):
    """
    Type definition for `ClientListVolumeRecoveryPointsResponse` `VolumeRecoveryPointInfos`

    Describes a storage volume recovery point object.

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume target.

    - **VolumeSizeInBytes** *(integer) --*

      The size of the volume in bytes.

    - **VolumeUsageInBytes** *(integer) --*

      The size of the data stored on the volume in bytes.

      .. note::

        This value is not available for volumes created prior to May 13, 2015, until you store
        data on the volume.

    - **VolumeRecoveryPointTime** *(string) --*

      The time the recovery point was taken.
    """


_ClientListVolumeRecoveryPointsResponseTypeDef = TypedDict(
    "_ClientListVolumeRecoveryPointsResponseTypeDef",
    {
        "GatewayARN": str,
        "VolumeRecoveryPointInfos": List[
            ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef
        ],
    },
    total=False,
)


class ClientListVolumeRecoveryPointsResponseTypeDef(
    _ClientListVolumeRecoveryPointsResponseTypeDef
):
    """
    Type definition for `ClientListVolumeRecoveryPoints` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **VolumeRecoveryPointInfos** *(list) --*

      An array of  VolumeRecoveryPointInfo objects.

      - *(dict) --*

        Describes a storage volume recovery point object.

        - **VolumeARN** *(string) --*

          The Amazon Resource Name (ARN) of the volume target.

        - **VolumeSizeInBytes** *(integer) --*

          The size of the volume in bytes.

        - **VolumeUsageInBytes** *(integer) --*

          The size of the data stored on the volume in bytes.

          .. note::

            This value is not available for volumes created prior to May 13, 2015, until you store
            data on the volume.

        - **VolumeRecoveryPointTime** *(string) --*

          The time the recovery point was taken.
    """


_ClientNotifyWhenUploadedResponseTypeDef = TypedDict(
    "_ClientNotifyWhenUploadedResponseTypeDef",
    {"FileShareARN": str, "NotificationId": str},
    total=False,
)


class ClientNotifyWhenUploadedResponseTypeDef(_ClientNotifyWhenUploadedResponseTypeDef):
    """
    Type definition for `ClientNotifyWhenUploaded` `Response`

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the file share.

    - **NotificationId** *(string) --*

      The randomly generated ID of the notification that was sent. This ID is in UUID format.
    """


_ClientRefreshCacheResponseTypeDef = TypedDict(
    "_ClientRefreshCacheResponseTypeDef",
    {"FileShareARN": str, "NotificationId": str},
    total=False,
)


class ClientRefreshCacheResponseTypeDef(_ClientRefreshCacheResponseTypeDef):
    """
    Type definition for `ClientRefreshCache` `Response`

    RefreshCacheOutput

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the file share.

    - **NotificationId** *(string) --*

      The randomly generated ID of the notification that was sent. This ID is in UUID format.
    """


_ClientRemoveTagsFromResourceResponseTypeDef = TypedDict(
    "_ClientRemoveTagsFromResourceResponseTypeDef", {"ResourceARN": str}, total=False
)


class ClientRemoveTagsFromResourceResponseTypeDef(
    _ClientRemoveTagsFromResourceResponseTypeDef
):
    """
    Type definition for `ClientRemoveTagsFromResource` `Response`

    RemoveTagsFromResourceOutput

    - **ResourceARN** *(string) --*

      The Amazon Resource Name (ARN) of the resource that the tags were removed from.
    """


_ClientResetCacheResponseTypeDef = TypedDict(
    "_ClientResetCacheResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientResetCacheResponseTypeDef(_ClientResetCacheResponseTypeDef):
    """
    Type definition for `ClientResetCache` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientRetrieveTapeArchiveResponseTypeDef = TypedDict(
    "_ClientRetrieveTapeArchiveResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientRetrieveTapeArchiveResponseTypeDef(
    _ClientRetrieveTapeArchiveResponseTypeDef
):
    """
    Type definition for `ClientRetrieveTapeArchive` `Response`

    RetrieveTapeArchiveOutput

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of the retrieved virtual tape.
    """


_ClientRetrieveTapeRecoveryPointResponseTypeDef = TypedDict(
    "_ClientRetrieveTapeRecoveryPointResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientRetrieveTapeRecoveryPointResponseTypeDef(
    _ClientRetrieveTapeRecoveryPointResponseTypeDef
):
    """
    Type definition for `ClientRetrieveTapeRecoveryPoint` `Response`

    RetrieveTapeRecoveryPointOutput

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of the virtual tape for which the recovery point was retrieved.
    """


_ClientSetLocalConsolePasswordResponseTypeDef = TypedDict(
    "_ClientSetLocalConsolePasswordResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientSetLocalConsolePasswordResponseTypeDef(
    _ClientSetLocalConsolePasswordResponseTypeDef
):
    """
    Type definition for `ClientSetLocalConsolePassword` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientSetSmbGuestPasswordResponseTypeDef = TypedDict(
    "_ClientSetSmbGuestPasswordResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientSetSmbGuestPasswordResponseTypeDef(
    _ClientSetSmbGuestPasswordResponseTypeDef
):
    """
    Type definition for `ClientSetSmbGuestPassword` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientShutdownGatewayResponseTypeDef = TypedDict(
    "_ClientShutdownGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientShutdownGatewayResponseTypeDef(_ClientShutdownGatewayResponseTypeDef):
    """
    Type definition for `ClientShutdownGateway` `Response`

    A JSON object containing the of the gateway that was shut down.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientStartGatewayResponseTypeDef = TypedDict(
    "_ClientStartGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientStartGatewayResponseTypeDef(_ClientStartGatewayResponseTypeDef):
    """
    Type definition for `ClientStartGateway` `Response`

    A JSON object containing the of the gateway that was restarted.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientUpdateBandwidthRateLimitResponseTypeDef = TypedDict(
    "_ClientUpdateBandwidthRateLimitResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientUpdateBandwidthRateLimitResponseTypeDef(
    _ClientUpdateBandwidthRateLimitResponseTypeDef
):
    """
    Type definition for `ClientUpdateBandwidthRateLimit` `Response`

    A JSON object containing the of the gateway whose throttle information was updated.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientUpdateChapCredentialsResponseTypeDef = TypedDict(
    "_ClientUpdateChapCredentialsResponseTypeDef",
    {"TargetARN": str, "InitiatorName": str},
    total=False,
)


class ClientUpdateChapCredentialsResponseTypeDef(
    _ClientUpdateChapCredentialsResponseTypeDef
):
    """
    Type definition for `ClientUpdateChapCredentials` `Response`

    A JSON object containing the following fields:

    - **TargetARN** *(string) --*

      The Amazon Resource Name (ARN) of the target. This is the same target specified in the
      request.

    - **InitiatorName** *(string) --*

      The iSCSI initiator that connects to the target. This is the same initiator name specified in
      the request.
    """


_ClientUpdateGatewayInformationResponseTypeDef = TypedDict(
    "_ClientUpdateGatewayInformationResponseTypeDef",
    {"GatewayARN": str, "GatewayName": str},
    total=False,
)


class ClientUpdateGatewayInformationResponseTypeDef(
    _ClientUpdateGatewayInformationResponseTypeDef
):
    """
    Type definition for `ClientUpdateGatewayInformation` `Response`

    A JSON object containing the ARN of the gateway that was updated.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **GatewayName** *(string) --*

      The name you configured for your gateway.
    """


_ClientUpdateGatewaySoftwareNowResponseTypeDef = TypedDict(
    "_ClientUpdateGatewaySoftwareNowResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientUpdateGatewaySoftwareNowResponseTypeDef(
    _ClientUpdateGatewaySoftwareNowResponseTypeDef
):
    """
    Type definition for `ClientUpdateGatewaySoftwareNow` `Response`

    A JSON object containing the of the gateway that was updated.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientUpdateMaintenanceStartTimeResponseTypeDef = TypedDict(
    "_ClientUpdateMaintenanceStartTimeResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientUpdateMaintenanceStartTimeResponseTypeDef(
    _ClientUpdateMaintenanceStartTimeResponseTypeDef
):
    """
    Type definition for `ClientUpdateMaintenanceStartTime` `Response`

    A JSON object containing the of the gateway whose maintenance start time is updated.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef = TypedDict(
    "_ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef",
    {"FileMode": str, "DirectoryMode": str, "GroupId": int, "OwnerId": int},
    total=False,
)


class ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef(
    _ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef
):
    """
    Type definition for `ClientUpdateNfsFileShare` `NFSFileShareDefaults`

    The default values for the file share. Optional.

    - **FileMode** *(string) --*

      The Unix file mode in the form "nnnn". For example, "0666" represents the default file mode
      inside the file share. The default value is 0666.

    - **DirectoryMode** *(string) --*

      The Unix directory mode in the form "nnnn". For example, "0666" represents the default access
      mode for all directories inside the file share. The default value is 0777.

    - **GroupId** *(integer) --*

      The default group ID for the file share (unless the files have another group ID specified). The
      default value is nfsnobody.

    - **OwnerId** *(integer) --*

      The default owner ID for files in the file share (unless the files have another owner ID
      specified). The default value is nfsnobody.
    """


_ClientUpdateNfsFileShareResponseTypeDef = TypedDict(
    "_ClientUpdateNfsFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)


class ClientUpdateNfsFileShareResponseTypeDef(_ClientUpdateNfsFileShareResponseTypeDef):
    """
    Type definition for `ClientUpdateNfsFileShare` `Response`

    UpdateNFSFileShareOutput

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the updated file share.
    """


_ClientUpdateSmbFileShareResponseTypeDef = TypedDict(
    "_ClientUpdateSmbFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)


class ClientUpdateSmbFileShareResponseTypeDef(_ClientUpdateSmbFileShareResponseTypeDef):
    """
    Type definition for `ClientUpdateSmbFileShare` `Response`

    UpdateSMBFileShareOutput

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the updated SMB file share.
    """


_ClientUpdateSmbSecurityStrategyResponseTypeDef = TypedDict(
    "_ClientUpdateSmbSecurityStrategyResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientUpdateSmbSecurityStrategyResponseTypeDef(
    _ClientUpdateSmbSecurityStrategyResponseTypeDef
):
    """
    Type definition for `ClientUpdateSmbSecurityStrategy` `Response`

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.
    """


_ClientUpdateSnapshotScheduleResponseTypeDef = TypedDict(
    "_ClientUpdateSnapshotScheduleResponseTypeDef", {"VolumeARN": str}, total=False
)


class ClientUpdateSnapshotScheduleResponseTypeDef(
    _ClientUpdateSnapshotScheduleResponseTypeDef
):
    """
    Type definition for `ClientUpdateSnapshotSchedule` `Response`

    A JSON object containing the of the updated storage volume.

    - **VolumeARN** *(string) --*

      The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return a list
      of gateway volumes.
    """


_ClientUpdateSnapshotScheduleTagsTypeDef = TypedDict(
    "_ClientUpdateSnapshotScheduleTagsTypeDef", {"Key": str, "Value": str}
)


class ClientUpdateSnapshotScheduleTagsTypeDef(_ClientUpdateSnapshotScheduleTagsTypeDef):
    """
    Type definition for `ClientUpdateSnapshotSchedule` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --* **[REQUIRED]**

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --* **[REQUIRED]**

      Value of the tag key.
    """


_ClientUpdateVtlDeviceTypeResponseTypeDef = TypedDict(
    "_ClientUpdateVtlDeviceTypeResponseTypeDef", {"VTLDeviceARN": str}, total=False
)


class ClientUpdateVtlDeviceTypeResponseTypeDef(
    _ClientUpdateVtlDeviceTypeResponseTypeDef
):
    """
    Type definition for `ClientUpdateVtlDeviceType` `Response`

    UpdateVTLDeviceTypeOutput

    - **VTLDeviceARN** *(string) --*

      The Amazon Resource Name (ARN) of the medium changer you have selected.
    """


_DescribeTapeArchivesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTapeArchivesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTapeArchivesPaginatePaginationConfigTypeDef(
    _DescribeTapeArchivesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeTapeArchivesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef = TypedDict(
    "_DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "CompletionTime": datetime,
        "RetrievedTo": str,
        "TapeStatus": str,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)


class DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef(
    _DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef
):
    """
    Type definition for `DescribeTapeArchivesPaginateResponse` `TapeArchives`

    Represents a virtual tape that is archived in the virtual tape shelf (VTS).

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of an archived virtual tape.

    - **TapeBarcode** *(string) --*

      The barcode that identifies the archived virtual tape.

    - **TapeCreatedDate** *(datetime) --*

      The date the virtual tape was created.

    - **TapeSizeInBytes** *(integer) --*

      The size, in bytes, of the archived virtual tape.

    - **CompletionTime** *(datetime) --*

      The time that the archiving of the virtual tape was completed.

      The default time stamp format is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.

    - **RetrievedTo** *(string) --*

      The Amazon Resource Name (ARN) of the tape gateway that the virtual tape is being
      retrieved to.

      The virtual tape is retrieved from the virtual tape shelf (VTS).

    - **TapeStatus** *(string) --*

      The current state of the archived virtual tape.

    - **TapeUsedInBytes** *(integer) --*

      The size, in bytes, of data stored on the virtual tape.

      .. note::

        This value is not available for tapes created prior to May 13, 2015.

    - **KMSKey** *(string) --*

      The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
      encryption. This value can only be set when KMSEncrypted is true. Optional.

    - **PoolId** *(string) --*

      The ID of the pool that was used to archive the tape. The tapes in this pool are archived
      in the S3 storage class that is associated with the pool.

      Valid values: "GLACIER", "DEEP_ARCHIVE"
    """


_DescribeTapeArchivesPaginateResponseTypeDef = TypedDict(
    "_DescribeTapeArchivesPaginateResponseTypeDef",
    {
        "TapeArchives": List[DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeTapeArchivesPaginateResponseTypeDef(
    _DescribeTapeArchivesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeTapeArchivesPaginate` `Response`

    DescribeTapeArchivesOutput

    - **TapeArchives** *(list) --*

      An array of virtual tape objects in the virtual tape shelf (VTS). The description includes of
      the Amazon Resource Name (ARN) of the virtual tapes. The information returned includes the
      Amazon Resource Names (ARNs) of the tapes, size of the tapes, status of the tapes, progress
      of the description and tape barcode.

      - *(dict) --*

        Represents a virtual tape that is archived in the virtual tape shelf (VTS).

        - **TapeARN** *(string) --*

          The Amazon Resource Name (ARN) of an archived virtual tape.

        - **TapeBarcode** *(string) --*

          The barcode that identifies the archived virtual tape.

        - **TapeCreatedDate** *(datetime) --*

          The date the virtual tape was created.

        - **TapeSizeInBytes** *(integer) --*

          The size, in bytes, of the archived virtual tape.

        - **CompletionTime** *(datetime) --*

          The time that the archiving of the virtual tape was completed.

          The default time stamp format is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.

        - **RetrievedTo** *(string) --*

          The Amazon Resource Name (ARN) of the tape gateway that the virtual tape is being
          retrieved to.

          The virtual tape is retrieved from the virtual tape shelf (VTS).

        - **TapeStatus** *(string) --*

          The current state of the archived virtual tape.

        - **TapeUsedInBytes** *(integer) --*

          The size, in bytes, of data stored on the virtual tape.

          .. note::

            This value is not available for tapes created prior to May 13, 2015.

        - **KMSKey** *(string) --*

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        - **PoolId** *(string) --*

          The ID of the pool that was used to archive the tape. The tapes in this pool are archived
          in the S3 storage class that is associated with the pool.

          Valid values: "GLACIER", "DEEP_ARCHIVE"

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef(
    _DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeTapeRecoveryPointsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef = TypedDict(
    "_DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef",
    {
        "TapeARN": str,
        "TapeRecoveryPointTime": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
    },
    total=False,
)


class DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef(
    _DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef
):
    """
    Type definition for `DescribeTapeRecoveryPointsPaginateResponse` `TapeRecoveryPointInfos`

    Describes a recovery point.

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of the virtual tape.

    - **TapeRecoveryPointTime** *(datetime) --*

      The time when the point-in-time view of the virtual tape was replicated for later
      recovery.

      The default time stamp format of the tape recovery point time is in the ISO8601 extended
      YYYY-MM-DD'T'HH:MM:SS'Z' format.

    - **TapeSizeInBytes** *(integer) --*

      The size, in bytes, of the virtual tapes to recover.

    - **TapeStatus** *(string) --*

      The status of the virtual tapes.
    """


_DescribeTapeRecoveryPointsPaginateResponseTypeDef = TypedDict(
    "_DescribeTapeRecoveryPointsPaginateResponseTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List[
            DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeTapeRecoveryPointsPaginateResponseTypeDef(
    _DescribeTapeRecoveryPointsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeTapeRecoveryPointsPaginate` `Response`

    DescribeTapeRecoveryPointsOutput

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **TapeRecoveryPointInfos** *(list) --*

      An array of TapeRecoveryPointInfos that are available for the specified gateway.

      - *(dict) --*

        Describes a recovery point.

        - **TapeARN** *(string) --*

          The Amazon Resource Name (ARN) of the virtual tape.

        - **TapeRecoveryPointTime** *(datetime) --*

          The time when the point-in-time view of the virtual tape was replicated for later
          recovery.

          The default time stamp format of the tape recovery point time is in the ISO8601 extended
          YYYY-MM-DD'T'HH:MM:SS'Z' format.

        - **TapeSizeInBytes** *(integer) --*

          The size, in bytes, of the virtual tapes to recover.

        - **TapeStatus** *(string) --*

          The status of the virtual tapes.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeTapesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTapesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTapesPaginatePaginationConfigTypeDef(
    _DescribeTapesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeTapesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeTapesPaginateResponseTapesTypeDef = TypedDict(
    "_DescribeTapesPaginateResponseTapesTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "VTLDevice": str,
        "Progress": float,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)


class DescribeTapesPaginateResponseTapesTypeDef(
    _DescribeTapesPaginateResponseTapesTypeDef
):
    """
    Type definition for `DescribeTapesPaginateResponse` `Tapes`

    Describes a virtual tape object.

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of the virtual tape.

    - **TapeBarcode** *(string) --*

      The barcode that identifies a specific virtual tape.

    - **TapeCreatedDate** *(datetime) --*

      The date the virtual tape was created.

    - **TapeSizeInBytes** *(integer) --*

      The size, in bytes, of the virtual tape capacity.

    - **TapeStatus** *(string) --*

      The current state of the virtual tape.

    - **VTLDevice** *(string) --*

      The virtual tape library (VTL) device that the virtual tape is associated with.

    - **Progress** *(float) --*

      For archiving virtual tapes, indicates how much data remains to be uploaded before
      archiving is complete.

      Range: 0 (not started) to 100 (complete).

    - **TapeUsedInBytes** *(integer) --*

      The size, in bytes, of data stored on the virtual tape.

      .. note::

        This value is not available for tapes created prior to May 13, 2015.

    - **KMSKey** *(string) --*

      The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
      encryption. This value can only be set when KMSEncrypted is true. Optional.

    - **PoolId** *(string) --*

      The ID of the pool that contains tapes that will be archived. The tapes in this pool are
      archived in the S3 storage class that is associated with the pool. When you use your
      backup application to eject the tape, the tape is archived directly into the storage
      class (Glacier or Deep Archive) that corresponds to the pool.

      Valid values: "GLACIER", "DEEP_ARCHIVE"
    """


_DescribeTapesPaginateResponseTypeDef = TypedDict(
    "_DescribeTapesPaginateResponseTypeDef",
    {"Tapes": List[DescribeTapesPaginateResponseTapesTypeDef], "NextToken": str},
    total=False,
)


class DescribeTapesPaginateResponseTypeDef(_DescribeTapesPaginateResponseTypeDef):
    """
    Type definition for `DescribeTapesPaginate` `Response`

    DescribeTapesOutput

    - **Tapes** *(list) --*

      An array of virtual tape descriptions.

      - *(dict) --*

        Describes a virtual tape object.

        - **TapeARN** *(string) --*

          The Amazon Resource Name (ARN) of the virtual tape.

        - **TapeBarcode** *(string) --*

          The barcode that identifies a specific virtual tape.

        - **TapeCreatedDate** *(datetime) --*

          The date the virtual tape was created.

        - **TapeSizeInBytes** *(integer) --*

          The size, in bytes, of the virtual tape capacity.

        - **TapeStatus** *(string) --*

          The current state of the virtual tape.

        - **VTLDevice** *(string) --*

          The virtual tape library (VTL) device that the virtual tape is associated with.

        - **Progress** *(float) --*

          For archiving virtual tapes, indicates how much data remains to be uploaded before
          archiving is complete.

          Range: 0 (not started) to 100 (complete).

        - **TapeUsedInBytes** *(integer) --*

          The size, in bytes, of data stored on the virtual tape.

          .. note::

            This value is not available for tapes created prior to May 13, 2015.

        - **KMSKey** *(string) --*

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        - **PoolId** *(string) --*

          The ID of the pool that contains tapes that will be archived. The tapes in this pool are
          archived in the S3 storage class that is associated with the pool. When you use your
          backup application to eject the tape, the tape is archived directly into the storage
          class (Glacier or Deep Archive) that corresponds to the pool.

          Valid values: "GLACIER", "DEEP_ARCHIVE"

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeVTLDevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeVTLDevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeVTLDevicesPaginatePaginationConfigTypeDef(
    _DescribeVTLDevicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeVTLDevicesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef = TypedDict(
    "_DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "ChapEnabled": bool,
    },
    total=False,
)


class DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef(
    _DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef
):
    """
    Type definition for `DescribeVTLDevicesPaginateResponseVTLDevices` `DeviceiSCSIAttributes`

    A list of iSCSI information about a VTL device.

    - **TargetARN** *(string) --*

      Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified
      name(iqn) of a tape drive or media changer target.

    - **NetworkInterfaceId** *(string) --*

      The network interface identifier of the VTL device.

    - **NetworkInterfacePort** *(integer) --*

      The port used to communicate with iSCSI VTL device targets.

    - **ChapEnabled** *(boolean) --*

      Indicates whether mutual CHAP is enabled for the iSCSI target.
    """


_DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef = TypedDict(
    "_DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef",
    {
        "VTLDeviceARN": str,
        "VTLDeviceType": str,
        "VTLDeviceVendor": str,
        "VTLDeviceProductIdentifier": str,
        "DeviceiSCSIAttributes": DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef,
    },
    total=False,
)


class DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef(
    _DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef
):
    """
    Type definition for `DescribeVTLDevicesPaginateResponse` `VTLDevices`

    Represents a device object associated with a tape gateway.

    - **VTLDeviceARN** *(string) --*

      Specifies the unique Amazon Resource Name (ARN) of the device (tape drive or media
      changer).

    - **VTLDeviceType** *(string) --*

      Specifies the type of device that the VTL device emulates.

    - **VTLDeviceVendor** *(string) --*

      Specifies the vendor of the device that the VTL device object emulates.

    - **VTLDeviceProductIdentifier** *(string) --*

      Specifies the model number of device that the VTL device emulates.

    - **DeviceiSCSIAttributes** *(dict) --*

      A list of iSCSI information about a VTL device.

      - **TargetARN** *(string) --*

        Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified
        name(iqn) of a tape drive or media changer target.

      - **NetworkInterfaceId** *(string) --*

        The network interface identifier of the VTL device.

      - **NetworkInterfacePort** *(integer) --*

        The port used to communicate with iSCSI VTL device targets.

      - **ChapEnabled** *(boolean) --*

        Indicates whether mutual CHAP is enabled for the iSCSI target.
    """


_DescribeVTLDevicesPaginateResponseTypeDef = TypedDict(
    "_DescribeVTLDevicesPaginateResponseTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List[DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeVTLDevicesPaginateResponseTypeDef(
    _DescribeVTLDevicesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeVTLDevicesPaginate` `Response`

    DescribeVTLDevicesOutput

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
      list of gateways for your account and AWS Region.

    - **VTLDevices** *(list) --*

      An array of VTL device objects composed of the Amazon Resource Name(ARN) of the VTL devices.

      - *(dict) --*

        Represents a device object associated with a tape gateway.

        - **VTLDeviceARN** *(string) --*

          Specifies the unique Amazon Resource Name (ARN) of the device (tape drive or media
          changer).

        - **VTLDeviceType** *(string) --*

          Specifies the type of device that the VTL device emulates.

        - **VTLDeviceVendor** *(string) --*

          Specifies the vendor of the device that the VTL device object emulates.

        - **VTLDeviceProductIdentifier** *(string) --*

          Specifies the model number of device that the VTL device emulates.

        - **DeviceiSCSIAttributes** *(dict) --*

          A list of iSCSI information about a VTL device.

          - **TargetARN** *(string) --*

            Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified
            name(iqn) of a tape drive or media changer target.

          - **NetworkInterfaceId** *(string) --*

            The network interface identifier of the VTL device.

          - **NetworkInterfacePort** *(integer) --*

            The port used to communicate with iSCSI VTL device targets.

          - **ChapEnabled** *(boolean) --*

            Indicates whether mutual CHAP is enabled for the iSCSI target.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListFileSharesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFileSharesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFileSharesPaginatePaginationConfigTypeDef(
    _ListFileSharesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFileSharesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListFileSharesPaginateResponseFileShareInfoListTypeDef = TypedDict(
    "_ListFileSharesPaginateResponseFileShareInfoListTypeDef",
    {
        "FileShareType": str,
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
    },
    total=False,
)


class ListFileSharesPaginateResponseFileShareInfoListTypeDef(
    _ListFileSharesPaginateResponseFileShareInfoListTypeDef
):
    """
    Type definition for `ListFileSharesPaginateResponse` `FileShareInfoList`

    Describes a file share.

    - **FileShareType** *(string) --*

      The type of the file share.

    - **FileShareARN** *(string) --*

      The Amazon Resource Name (ARN) of the file share.

    - **FileShareId** *(string) --*

      The ID of the file share.

    - **FileShareStatus** *(string) --*

      The status of the file share. Possible values are ``CREATING`` , ``UPDATING`` ,
      ``AVAILABLE`` and ``DELETING`` .

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
      a list of gateways for your account and AWS Region.
    """


_ListFileSharesPaginateResponseTypeDef = TypedDict(
    "_ListFileSharesPaginateResponseTypeDef",
    {
        "Marker": str,
        "FileShareInfoList": List[
            ListFileSharesPaginateResponseFileShareInfoListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListFileSharesPaginateResponseTypeDef(_ListFileSharesPaginateResponseTypeDef):
    """
    Type definition for `ListFileSharesPaginate` `Response`

    ListFileShareOutput

    - **Marker** *(string) --*

      If the request includes ``Marker`` , the response returns that value in this field.

    - **FileShareInfoList** *(list) --*

      An array of information about the file gateway's file shares.

      - *(dict) --*

        Describes a file share.

        - **FileShareType** *(string) --*

          The type of the file share.

        - **FileShareARN** *(string) --*

          The Amazon Resource Name (ARN) of the file share.

        - **FileShareId** *(string) --*

          The ID of the file share.

        - **FileShareStatus** *(string) --*

          The status of the file share. Possible values are ``CREATING`` , ``UPDATING`` ,
          ``AVAILABLE`` and ``DELETING`` .

        - **GatewayARN** *(string) --*

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
          a list of gateways for your account and AWS Region.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListGatewaysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGatewaysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGatewaysPaginatePaginationConfigTypeDef(
    _ListGatewaysPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGatewaysPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListGatewaysPaginateResponseGatewaysTypeDef = TypedDict(
    "_ListGatewaysPaginateResponseGatewaysTypeDef",
    {
        "GatewayId": str,
        "GatewayARN": str,
        "GatewayType": str,
        "GatewayOperationalState": str,
        "GatewayName": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
    },
    total=False,
)


class ListGatewaysPaginateResponseGatewaysTypeDef(
    _ListGatewaysPaginateResponseGatewaysTypeDef
):
    """
    Type definition for `ListGatewaysPaginateResponse` `Gateways`

    Describes a gateway object.

    - **GatewayId** *(string) --*

      The unique identifier assigned to your gateway during activation. This ID becomes part of
      the gateway Amazon Resource Name (ARN), which you use as input for other operations.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
      a list of gateways for your account and AWS Region.

    - **GatewayType** *(string) --*

      The type of the gateway.

    - **GatewayOperationalState** *(string) --*

      The state of the gateway.

      Valid Values: DISABLED or ACTIVE

    - **GatewayName** *(string) --*

      The name of the gateway.

    - **Ec2InstanceId** *(string) --*

      The ID of the Amazon EC2 instance that was used to launch the gateway.

    - **Ec2InstanceRegion** *(string) --*

      The AWS Region where the Amazon EC2 instance is located.
    """


_ListGatewaysPaginateResponseTypeDef = TypedDict(
    "_ListGatewaysPaginateResponseTypeDef",
    {"Gateways": List[ListGatewaysPaginateResponseGatewaysTypeDef], "NextToken": str},
    total=False,
)


class ListGatewaysPaginateResponseTypeDef(_ListGatewaysPaginateResponseTypeDef):
    """
    Type definition for `ListGatewaysPaginate` `Response`

    - **Gateways** *(list) --*

      An array of  GatewayInfo objects.

      - *(dict) --*

        Describes a gateway object.

        - **GatewayId** *(string) --*

          The unique identifier assigned to your gateway during activation. This ID becomes part of
          the gateway Amazon Resource Name (ARN), which you use as input for other operations.

        - **GatewayARN** *(string) --*

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
          a list of gateways for your account and AWS Region.

        - **GatewayType** *(string) --*

          The type of the gateway.

        - **GatewayOperationalState** *(string) --*

          The state of the gateway.

          Valid Values: DISABLED or ACTIVE

        - **GatewayName** *(string) --*

          The name of the gateway.

        - **Ec2InstanceId** *(string) --*

          The ID of the Amazon EC2 instance that was used to launch the gateway.

        - **Ec2InstanceRegion** *(string) --*

          The AWS Region where the Amazon EC2 instance is located.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginateResponse` `Tags`

    A key-value pair that helps you manage, filter, and search for your resource. Allowed
    characters: letters, white space, and numbers, representable in UTF-8, and the following
    characters: + - = . _ : /

    - **Key** *(string) --*

      Tag key (String). The key can't start with aws:.

    - **Value** *(string) --*

      Value of the tag key.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {
        "ResourceARN": str,
        "Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(
    _ListTagsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `Response`

    ListTagsForResourceOutput

    - **ResourceARN** *(string) --*

      he Amazon Resource Name (ARN) of the resource for which you want to list tags.

    - **Tags** *(list) --*

      An array that contains the tags for the specified resource.

      - *(dict) --*

        A key-value pair that helps you manage, filter, and search for your resource. Allowed
        characters: letters, white space, and numbers, representable in UTF-8, and the following
        characters: + - = . _ : /

        - **Key** *(string) --*

          Tag key (String). The key can't start with aws:.

        - **Value** *(string) --*

          Value of the tag key.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListTapesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTapesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTapesPaginatePaginationConfigTypeDef(
    _ListTapesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTapesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListTapesPaginateResponseTapeInfosTypeDef = TypedDict(
    "_ListTapesPaginateResponseTapeInfosTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "GatewayARN": str,
        "PoolId": str,
    },
    total=False,
)


class ListTapesPaginateResponseTapeInfosTypeDef(
    _ListTapesPaginateResponseTapeInfosTypeDef
):
    """
    Type definition for `ListTapesPaginateResponse` `TapeInfos`

    Describes a virtual tape.

    - **TapeARN** *(string) --*

      The Amazon Resource Name (ARN) of a virtual tape.

    - **TapeBarcode** *(string) --*

      The barcode that identifies a specific virtual tape.

    - **TapeSizeInBytes** *(integer) --*

      The size, in bytes, of a virtual tape.

    - **TapeStatus** *(string) --*

      The status of the tape.

    - **GatewayARN** *(string) --*

      The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
      a list of gateways for your account and AWS Region.

    - **PoolId** *(string) --*

      The ID of the pool that you want to add your tape to for archiving. The tape in this pool
      is archived in the S3 storage class that is associated with the pool. When you use your
      backup application to eject the tape, the tape is archived directly into the storage
      class (Glacier or Deep Archive) that corresponds to the pool.

      Valid values: "GLACIER", "DEEP_ARCHIVE"
    """


_ListTapesPaginateResponseTypeDef = TypedDict(
    "_ListTapesPaginateResponseTypeDef",
    {"TapeInfos": List[ListTapesPaginateResponseTapeInfosTypeDef], "NextToken": str},
    total=False,
)


class ListTapesPaginateResponseTypeDef(_ListTapesPaginateResponseTypeDef):
    """
    Type definition for `ListTapesPaginate` `Response`

    A JSON object containing the following fields:

    *  ListTapesOutput$Marker

    *  ListTapesOutput$VolumeInfos

    - **TapeInfos** *(list) --*

      An array of  TapeInfo objects, where each object describes an a single tape. If there not
      tapes in the tape library or VTS, then the ``TapeInfos`` is an empty array.

      - *(dict) --*

        Describes a virtual tape.

        - **TapeARN** *(string) --*

          The Amazon Resource Name (ARN) of a virtual tape.

        - **TapeBarcode** *(string) --*

          The barcode that identifies a specific virtual tape.

        - **TapeSizeInBytes** *(integer) --*

          The size, in bytes, of a virtual tape.

        - **TapeStatus** *(string) --*

          The status of the tape.

        - **GatewayARN** *(string) --*

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return
          a list of gateways for your account and AWS Region.

        - **PoolId** *(string) --*

          The ID of the pool that you want to add your tape to for archiving. The tape in this pool
          is archived in the S3 storage class that is associated with the pool. When you use your
          backup application to eject the tape, the tape is archived directly into the storage
          class (Glacier or Deep Archive) that corresponds to the pool.

          Valid values: "GLACIER", "DEEP_ARCHIVE"

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListVolumesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVolumesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVolumesPaginatePaginationConfigTypeDef(
    _ListVolumesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListVolumesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """
