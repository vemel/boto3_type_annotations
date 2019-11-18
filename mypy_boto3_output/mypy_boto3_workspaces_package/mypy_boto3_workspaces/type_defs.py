"Main interface for workspaces type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAuthorizeIpRulesUserRulesTypeDef",
    "ClientCopyWorkspaceImageResponseTypeDef",
    "ClientCopyWorkspaceImageTagsTypeDef",
    "ClientCreateIpGroupResponseTypeDef",
    "ClientCreateIpGroupTagsTypeDef",
    "ClientCreateIpGroupUserRulesTypeDef",
    "ClientCreateTagsTagsTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsTypeDef",
    "ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef",
    "ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef",
    "ClientCreateWorkspacesResponsePendingRequestsTypeDef",
    "ClientCreateWorkspacesResponseTypeDef",
    "ClientCreateWorkspacesWorkspacesTagsTypeDef",
    "ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef",
    "ClientCreateWorkspacesWorkspacesTypeDef",
    "ClientDescribeAccountModificationsResponseAccountModificationsTypeDef",
    "ClientDescribeAccountModificationsResponseTypeDef",
    "ClientDescribeAccountResponseTypeDef",
    "ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef",
    "ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef",
    "ClientDescribeClientPropertiesResponseTypeDef",
    "ClientDescribeIpGroupsResponseResultuserRulesTypeDef",
    "ClientDescribeIpGroupsResponseResultTypeDef",
    "ClientDescribeIpGroupsResponseTypeDef",
    "ClientDescribeTagsResponseTagListTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesTypeDef",
    "ClientDescribeWorkspaceBundlesResponseTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseTypeDef",
    "ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef",
    "ClientDescribeWorkspaceImagesResponseImagesTypeDef",
    "ClientDescribeWorkspaceImagesResponseTypeDef",
    "ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef",
    "ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef",
    "ClientDescribeWorkspaceSnapshotsResponseTypeDef",
    "ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef",
    "ClientDescribeWorkspacesConnectionStatusResponseTypeDef",
    "ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef",
    "ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef",
    "ClientDescribeWorkspacesResponseWorkspacesTypeDef",
    "ClientDescribeWorkspacesResponseTypeDef",
    "ClientImportWorkspaceImageResponseTypeDef",
    "ClientImportWorkspaceImageTagsTypeDef",
    "ClientListAvailableManagementCidrRangesResponseTypeDef",
    "ClientModifyClientPropertiesClientPropertiesTypeDef",
    "ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef",
    "ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef",
    "ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef",
    "ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef",
    "ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef",
    "ClientRebootWorkspacesResponseFailedRequestsTypeDef",
    "ClientRebootWorkspacesResponseTypeDef",
    "ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef",
    "ClientRebuildWorkspacesResponseFailedRequestsTypeDef",
    "ClientRebuildWorkspacesResponseTypeDef",
    "ClientRegisterWorkspaceDirectoryTagsTypeDef",
    "ClientStartWorkspacesResponseFailedRequestsTypeDef",
    "ClientStartWorkspacesResponseTypeDef",
    "ClientStartWorkspacesStartWorkspaceRequestsTypeDef",
    "ClientStopWorkspacesResponseFailedRequestsTypeDef",
    "ClientStopWorkspacesResponseTypeDef",
    "ClientStopWorkspacesStopWorkspaceRequestsTypeDef",
    "ClientTerminateWorkspacesResponseFailedRequestsTypeDef",
    "ClientTerminateWorkspacesResponseTypeDef",
    "ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef",
    "ClientUpdateRulesOfIpGroupUserRulesTypeDef",
    "DescribeAccountModificationsPaginatePaginationConfigTypeDef",
    "DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef",
    "DescribeAccountModificationsPaginateResponseTypeDef",
    "DescribeIpGroupsPaginatePaginationConfigTypeDef",
    "DescribeIpGroupsPaginateResponseResultuserRulesTypeDef",
    "DescribeIpGroupsPaginateResponseResultTypeDef",
    "DescribeIpGroupsPaginateResponseTypeDef",
    "DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef",
    "DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef",
    "DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef",
    "DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef",
    "DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef",
    "DescribeWorkspaceBundlesPaginateResponseTypeDef",
    "DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef",
    "DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef",
    "DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef",
    "DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef",
    "DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef",
    "DescribeWorkspaceDirectoriesPaginateResponseTypeDef",
    "DescribeWorkspaceImagesPaginatePaginationConfigTypeDef",
    "DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef",
    "DescribeWorkspaceImagesPaginateResponseImagesTypeDef",
    "DescribeWorkspaceImagesPaginateResponseTypeDef",
    "DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef",
    "DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef",
    "DescribeWorkspacesConnectionStatusPaginateResponseTypeDef",
    "DescribeWorkspacesPaginatePaginationConfigTypeDef",
    "DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef",
    "DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef",
    "DescribeWorkspacesPaginateResponseWorkspacesTypeDef",
    "DescribeWorkspacesPaginateResponseTypeDef",
    "ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef",
    "ListAvailableManagementCidrRangesPaginateResponseTypeDef",
)


_ClientAuthorizeIpRulesUserRulesTypeDef = TypedDict(
    "_ClientAuthorizeIpRulesUserRulesTypeDef",
    {"ipRule": str, "ruleDesc": str},
    total=False,
)


class ClientAuthorizeIpRulesUserRulesTypeDef(_ClientAuthorizeIpRulesUserRulesTypeDef):
    """
    Type definition for `ClientAuthorizeIpRules` `UserRules`

    Describes a rule for an IP access control group.

    - **ipRule** *(string) --*

      The IP address range, in CIDR notation.

    - **ruleDesc** *(string) --*

      The description.
    """


_ClientCopyWorkspaceImageResponseTypeDef = TypedDict(
    "_ClientCopyWorkspaceImageResponseTypeDef", {"ImageId": str}, total=False
)


class ClientCopyWorkspaceImageResponseTypeDef(_ClientCopyWorkspaceImageResponseTypeDef):
    """
    Type definition for `ClientCopyWorkspaceImage` `Response`

    - **ImageId** *(string) --*

      The identifier of the image.
    """


_RequiredClientCopyWorkspaceImageTagsTypeDef = TypedDict(
    "_RequiredClientCopyWorkspaceImageTagsTypeDef", {"Key": str}
)
_OptionalClientCopyWorkspaceImageTagsTypeDef = TypedDict(
    "_OptionalClientCopyWorkspaceImageTagsTypeDef", {"Value": str}, total=False
)


class ClientCopyWorkspaceImageTagsTypeDef(
    _RequiredClientCopyWorkspaceImageTagsTypeDef,
    _OptionalClientCopyWorkspaceImageTagsTypeDef,
):
    """
    Type definition for `ClientCopyWorkspaceImage` `Tags`

    Describes a tag.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientCreateIpGroupResponseTypeDef = TypedDict(
    "_ClientCreateIpGroupResponseTypeDef", {"GroupId": str}, total=False
)


class ClientCreateIpGroupResponseTypeDef(_ClientCreateIpGroupResponseTypeDef):
    """
    Type definition for `ClientCreateIpGroup` `Response`

    - **GroupId** *(string) --*

      The identifier of the group.
    """


_RequiredClientCreateIpGroupTagsTypeDef = TypedDict(
    "_RequiredClientCreateIpGroupTagsTypeDef", {"Key": str}
)
_OptionalClientCreateIpGroupTagsTypeDef = TypedDict(
    "_OptionalClientCreateIpGroupTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateIpGroupTagsTypeDef(
    _RequiredClientCreateIpGroupTagsTypeDef, _OptionalClientCreateIpGroupTagsTypeDef
):
    """
    Type definition for `ClientCreateIpGroup` `Tags`

    Describes a tag.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientCreateIpGroupUserRulesTypeDef = TypedDict(
    "_ClientCreateIpGroupUserRulesTypeDef",
    {"ipRule": str, "ruleDesc": str},
    total=False,
)


class ClientCreateIpGroupUserRulesTypeDef(_ClientCreateIpGroupUserRulesTypeDef):
    """
    Type definition for `ClientCreateIpGroup` `UserRules`

    Describes a rule for an IP access control group.

    - **ipRule** *(string) --*

      The IP address range, in CIDR notation.

    - **ruleDesc** *(string) --*

      The description.
    """


_RequiredClientCreateTagsTagsTypeDef = TypedDict(
    "_RequiredClientCreateTagsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTagsTagsTypeDef = TypedDict(
    "_OptionalClientCreateTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTagsTagsTypeDef(
    _RequiredClientCreateTagsTagsTypeDef, _OptionalClientCreateTagsTagsTypeDef
):
    """
    Type definition for `ClientCreateTags` `Tags`

    Describes a tag.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef(
    _ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef
):
    """
    Type definition for `ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequest` `Tags`

    Describes a tag.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef",
    {
        "RunningMode": str,
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": str,
    },
    total=False,
)


class ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef(
    _ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef
):
    """
    Type definition for `ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequest` `WorkspaceProperties`

    The WorkSpace properties.

    - **RunningMode** *(string) --*

      The running mode. For more information, see `Manage the WorkSpace Running Mode
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

    - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

      The time after a user logs off when WorkSpaces are automatically stopped. Configured
      in 60-minute intervals.

    - **RootVolumeSizeGib** *(integer) --*

      The size of the root volume.

    - **UserVolumeSizeGib** *(integer) --*

      The size of the user storage.

    - **ComputeTypeName** *(string) --*

      The compute type. For more information, see `Amazon WorkSpaces Bundles
      <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
    """


_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "BundleId": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef,
        "Tags": List[
            ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef
        ],
    },
    total=False,
)


class ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef(
    _ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef
):
    """
    Type definition for `ClientCreateWorkspacesResponseFailedRequests` `WorkspaceRequest`

    Information about the WorkSpace.

    - **DirectoryId** *(string) --*

      The identifier of the AWS Directory Service directory for the WorkSpace. You can use
      DescribeWorkspaceDirectories to list the available directories.

    - **UserName** *(string) --*

      The user name of the user for the WorkSpace. This user name must exist in the AWS
      Directory Service directory for the WorkSpace.

    - **BundleId** *(string) --*

      The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles
      to list the available bundles.

    - **VolumeEncryptionKey** *(string) --*

      The KMS key used to encrypt data stored on your WorkSpace.

    - **UserVolumeEncryptionEnabled** *(boolean) --*

      Indicates whether the data stored on the user volume is encrypted.

    - **RootVolumeEncryptionEnabled** *(boolean) --*

      Indicates whether the data stored on the root volume is encrypted.

    - **WorkspaceProperties** *(dict) --*

      The WorkSpace properties.

      - **RunningMode** *(string) --*

        The running mode. For more information, see `Manage the WorkSpace Running Mode
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

      - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

        The time after a user logs off when WorkSpaces are automatically stopped. Configured
        in 60-minute intervals.

      - **RootVolumeSizeGib** *(integer) --*

        The size of the root volume.

      - **UserVolumeSizeGib** *(integer) --*

        The size of the user storage.

      - **ComputeTypeName** *(string) --*

        The compute type. For more information, see `Amazon WorkSpaces Bundles
        <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

    - **Tags** *(list) --*

      The tags for the WorkSpace.

      - *(dict) --*

        Describes a tag.

        - **Key** *(string) --*

          The key of the tag.

        - **Value** *(string) --*

          The value of the tag.
    """


_ClientCreateWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponseFailedRequestsTypeDef",
    {
        "WorkspaceRequest": ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientCreateWorkspacesResponseFailedRequestsTypeDef(
    _ClientCreateWorkspacesResponseFailedRequestsTypeDef
):
    """
    Type definition for `ClientCreateWorkspacesResponse` `FailedRequests`

    Describes a WorkSpace that cannot be created.

    - **WorkspaceRequest** *(dict) --*

      Information about the WorkSpace.

      - **DirectoryId** *(string) --*

        The identifier of the AWS Directory Service directory for the WorkSpace. You can use
        DescribeWorkspaceDirectories to list the available directories.

      - **UserName** *(string) --*

        The user name of the user for the WorkSpace. This user name must exist in the AWS
        Directory Service directory for the WorkSpace.

      - **BundleId** *(string) --*

        The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles
        to list the available bundles.

      - **VolumeEncryptionKey** *(string) --*

        The KMS key used to encrypt data stored on your WorkSpace.

      - **UserVolumeEncryptionEnabled** *(boolean) --*

        Indicates whether the data stored on the user volume is encrypted.

      - **RootVolumeEncryptionEnabled** *(boolean) --*

        Indicates whether the data stored on the root volume is encrypted.

      - **WorkspaceProperties** *(dict) --*

        The WorkSpace properties.

        - **RunningMode** *(string) --*

          The running mode. For more information, see `Manage the WorkSpace Running Mode
          <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

        - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

          The time after a user logs off when WorkSpaces are automatically stopped. Configured
          in 60-minute intervals.

        - **RootVolumeSizeGib** *(integer) --*

          The size of the root volume.

        - **UserVolumeSizeGib** *(integer) --*

          The size of the user storage.

        - **ComputeTypeName** *(string) --*

          The compute type. For more information, see `Amazon WorkSpaces Bundles
          <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

      - **Tags** *(list) --*

        The tags for the WorkSpace.

        - *(dict) --*

          Describes a tag.

          - **Key** *(string) --*

            The key of the tag.

          - **Value** *(string) --*

            The value of the tag.

    - **ErrorCode** *(string) --*

      The error code that is returned if the WorkSpace cannot be created.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the WorkSpace cannot be created.
    """


_ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef",
    {"Resource": str, "State": str},
    total=False,
)


class ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef(
    _ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef
):
    """
    Type definition for `ClientCreateWorkspacesResponsePendingRequests` `ModificationStates`

    Describes a WorkSpace modification.

    - **Resource** *(string) --*

      The resource.

    - **State** *(string) --*

      The modification state.
    """


_ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef",
    {
        "RunningMode": str,
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": str,
    },
    total=False,
)


class ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef(
    _ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef
):
    """
    Type definition for `ClientCreateWorkspacesResponsePendingRequests` `WorkspaceProperties`

    The properties of the WorkSpace.

    - **RunningMode** *(string) --*

      The running mode. For more information, see `Manage the WorkSpace Running Mode
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

    - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

      The time after a user logs off when WorkSpaces are automatically stopped. Configured in
      60-minute intervals.

    - **RootVolumeSizeGib** *(integer) --*

      The size of the root volume.

    - **UserVolumeSizeGib** *(integer) --*

      The size of the user storage.

    - **ComputeTypeName** *(string) --*

      The compute type. For more information, see `Amazon WorkSpaces Bundles
      <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
    """


_ClientCreateWorkspacesResponsePendingRequestsTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponsePendingRequestsTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": str,
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef,
        "ModificationStates": List[
            ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef
        ],
    },
    total=False,
)


class ClientCreateWorkspacesResponsePendingRequestsTypeDef(
    _ClientCreateWorkspacesResponsePendingRequestsTypeDef
):
    """
    Type definition for `ClientCreateWorkspacesResponse` `PendingRequests`

    Describes a WorkSpace.

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.

    - **DirectoryId** *(string) --*

      The identifier of the AWS Directory Service directory for the WorkSpace.

    - **UserName** *(string) --*

      The user for the WorkSpace.

    - **IpAddress** *(string) --*

      The IP address of the WorkSpace.

    - **State** *(string) --*

      The operational state of the WorkSpace.

    - **BundleId** *(string) --*

      The identifier of the bundle used to create the WorkSpace.

    - **SubnetId** *(string) --*

      The identifier of the subnet for the WorkSpace.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the WorkSpace cannot be created.

    - **ErrorCode** *(string) --*

      The error code that is returned if the WorkSpace cannot be created.

    - **ComputerName** *(string) --*

      The name of the WorkSpace, as seen by the operating system.

    - **VolumeEncryptionKey** *(string) --*

      The KMS key used to encrypt data stored on your WorkSpace.

    - **UserVolumeEncryptionEnabled** *(boolean) --*

      Indicates whether the data stored on the user volume is encrypted.

    - **RootVolumeEncryptionEnabled** *(boolean) --*

      Indicates whether the data stored on the root volume is encrypted.

    - **WorkspaceProperties** *(dict) --*

      The properties of the WorkSpace.

      - **RunningMode** *(string) --*

        The running mode. For more information, see `Manage the WorkSpace Running Mode
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

      - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

        The time after a user logs off when WorkSpaces are automatically stopped. Configured in
        60-minute intervals.

      - **RootVolumeSizeGib** *(integer) --*

        The size of the root volume.

      - **UserVolumeSizeGib** *(integer) --*

        The size of the user storage.

      - **ComputeTypeName** *(string) --*

        The compute type. For more information, see `Amazon WorkSpaces Bundles
        <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

    - **ModificationStates** *(list) --*

      The modification states of the WorkSpace.

      - *(dict) --*

        Describes a WorkSpace modification.

        - **Resource** *(string) --*

          The resource.

        - **State** *(string) --*

          The modification state.
    """


_ClientCreateWorkspacesResponseTypeDef = TypedDict(
    "_ClientCreateWorkspacesResponseTypeDef",
    {
        "FailedRequests": List[ClientCreateWorkspacesResponseFailedRequestsTypeDef],
        "PendingRequests": List[ClientCreateWorkspacesResponsePendingRequestsTypeDef],
    },
    total=False,
)


class ClientCreateWorkspacesResponseTypeDef(_ClientCreateWorkspacesResponseTypeDef):
    """
    Type definition for `ClientCreateWorkspaces` `Response`

    - **FailedRequests** *(list) --*

      Information about the WorkSpaces that could not be created.

      - *(dict) --*

        Describes a WorkSpace that cannot be created.

        - **WorkspaceRequest** *(dict) --*

          Information about the WorkSpace.

          - **DirectoryId** *(string) --*

            The identifier of the AWS Directory Service directory for the WorkSpace. You can use
            DescribeWorkspaceDirectories to list the available directories.

          - **UserName** *(string) --*

            The user name of the user for the WorkSpace. This user name must exist in the AWS
            Directory Service directory for the WorkSpace.

          - **BundleId** *(string) --*

            The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles
            to list the available bundles.

          - **VolumeEncryptionKey** *(string) --*

            The KMS key used to encrypt data stored on your WorkSpace.

          - **UserVolumeEncryptionEnabled** *(boolean) --*

            Indicates whether the data stored on the user volume is encrypted.

          - **RootVolumeEncryptionEnabled** *(boolean) --*

            Indicates whether the data stored on the root volume is encrypted.

          - **WorkspaceProperties** *(dict) --*

            The WorkSpace properties.

            - **RunningMode** *(string) --*

              The running mode. For more information, see `Manage the WorkSpace Running Mode
              <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

            - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

              The time after a user logs off when WorkSpaces are automatically stopped. Configured
              in 60-minute intervals.

            - **RootVolumeSizeGib** *(integer) --*

              The size of the root volume.

            - **UserVolumeSizeGib** *(integer) --*

              The size of the user storage.

            - **ComputeTypeName** *(string) --*

              The compute type. For more information, see `Amazon WorkSpaces Bundles
              <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

          - **Tags** *(list) --*

            The tags for the WorkSpace.

            - *(dict) --*

              Describes a tag.

              - **Key** *(string) --*

                The key of the tag.

              - **Value** *(string) --*

                The value of the tag.

        - **ErrorCode** *(string) --*

          The error code that is returned if the WorkSpace cannot be created.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the WorkSpace cannot be created.

    - **PendingRequests** *(list) --*

      Information about the WorkSpaces that were created.

      Because this operation is asynchronous, the identifier returned is not immediately available
      for use with other operations. For example, if you call  DescribeWorkspaces before the
      WorkSpace is created, the information returned can be incomplete.

      - *(dict) --*

        Describes a WorkSpace.

        - **WorkspaceId** *(string) --*

          The identifier of the WorkSpace.

        - **DirectoryId** *(string) --*

          The identifier of the AWS Directory Service directory for the WorkSpace.

        - **UserName** *(string) --*

          The user for the WorkSpace.

        - **IpAddress** *(string) --*

          The IP address of the WorkSpace.

        - **State** *(string) --*

          The operational state of the WorkSpace.

        - **BundleId** *(string) --*

          The identifier of the bundle used to create the WorkSpace.

        - **SubnetId** *(string) --*

          The identifier of the subnet for the WorkSpace.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the WorkSpace cannot be created.

        - **ErrorCode** *(string) --*

          The error code that is returned if the WorkSpace cannot be created.

        - **ComputerName** *(string) --*

          The name of the WorkSpace, as seen by the operating system.

        - **VolumeEncryptionKey** *(string) --*

          The KMS key used to encrypt data stored on your WorkSpace.

        - **UserVolumeEncryptionEnabled** *(boolean) --*

          Indicates whether the data stored on the user volume is encrypted.

        - **RootVolumeEncryptionEnabled** *(boolean) --*

          Indicates whether the data stored on the root volume is encrypted.

        - **WorkspaceProperties** *(dict) --*

          The properties of the WorkSpace.

          - **RunningMode** *(string) --*

            The running mode. For more information, see `Manage the WorkSpace Running Mode
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

          - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

            The time after a user logs off when WorkSpaces are automatically stopped. Configured in
            60-minute intervals.

          - **RootVolumeSizeGib** *(integer) --*

            The size of the root volume.

          - **UserVolumeSizeGib** *(integer) --*

            The size of the user storage.

          - **ComputeTypeName** *(string) --*

            The compute type. For more information, see `Amazon WorkSpaces Bundles
            <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

        - **ModificationStates** *(list) --*

          The modification states of the WorkSpace.

          - *(dict) --*

            Describes a WorkSpace modification.

            - **Resource** *(string) --*

              The resource.

            - **State** *(string) --*

              The modification state.
    """


_RequiredClientCreateWorkspacesWorkspacesTagsTypeDef = TypedDict(
    "_RequiredClientCreateWorkspacesWorkspacesTagsTypeDef", {"Key": str}
)
_OptionalClientCreateWorkspacesWorkspacesTagsTypeDef = TypedDict(
    "_OptionalClientCreateWorkspacesWorkspacesTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateWorkspacesWorkspacesTagsTypeDef(
    _RequiredClientCreateWorkspacesWorkspacesTagsTypeDef,
    _OptionalClientCreateWorkspacesWorkspacesTagsTypeDef,
):
    """
    Type definition for `ClientCreateWorkspacesWorkspaces` `Tags`

    Describes a tag.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef = TypedDict(
    "_ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef",
    {
        "RunningMode": str,
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": str,
    },
    total=False,
)


class ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef(
    _ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef
):
    """
    Type definition for `ClientCreateWorkspacesWorkspaces` `WorkspaceProperties`

    The WorkSpace properties.

    - **RunningMode** *(string) --*

      The running mode. For more information, see `Manage the WorkSpace Running Mode
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

    - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

      The time after a user logs off when WorkSpaces are automatically stopped. Configured in
      60-minute intervals.

    - **RootVolumeSizeGib** *(integer) --*

      The size of the root volume.

    - **UserVolumeSizeGib** *(integer) --*

      The size of the user storage.

    - **ComputeTypeName** *(string) --*

      The compute type. For more information, see `Amazon WorkSpaces Bundles
      <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
    """


_RequiredClientCreateWorkspacesWorkspacesTypeDef = TypedDict(
    "_RequiredClientCreateWorkspacesWorkspacesTypeDef",
    {"DirectoryId": str, "UserName": str, "BundleId": str},
)
_OptionalClientCreateWorkspacesWorkspacesTypeDef = TypedDict(
    "_OptionalClientCreateWorkspacesWorkspacesTypeDef",
    {
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef,
        "Tags": List[ClientCreateWorkspacesWorkspacesTagsTypeDef],
    },
    total=False,
)


class ClientCreateWorkspacesWorkspacesTypeDef(
    _RequiredClientCreateWorkspacesWorkspacesTypeDef,
    _OptionalClientCreateWorkspacesWorkspacesTypeDef,
):
    """
    Type definition for `ClientCreateWorkspaces` `Workspaces`

    Describes the information used to create a WorkSpace.

    - **DirectoryId** *(string) --* **[REQUIRED]**

      The identifier of the AWS Directory Service directory for the WorkSpace. You can use
      DescribeWorkspaceDirectories to list the available directories.

    - **UserName** *(string) --* **[REQUIRED]**

      The user name of the user for the WorkSpace. This user name must exist in the AWS Directory
      Service directory for the WorkSpace.

    - **BundleId** *(string) --* **[REQUIRED]**

      The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles to list
      the available bundles.

    - **VolumeEncryptionKey** *(string) --*

      The KMS key used to encrypt data stored on your WorkSpace.

    - **UserVolumeEncryptionEnabled** *(boolean) --*

      Indicates whether the data stored on the user volume is encrypted.

    - **RootVolumeEncryptionEnabled** *(boolean) --*

      Indicates whether the data stored on the root volume is encrypted.

    - **WorkspaceProperties** *(dict) --*

      The WorkSpace properties.

      - **RunningMode** *(string) --*

        The running mode. For more information, see `Manage the WorkSpace Running Mode
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

      - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

        The time after a user logs off when WorkSpaces are automatically stopped. Configured in
        60-minute intervals.

      - **RootVolumeSizeGib** *(integer) --*

        The size of the root volume.

      - **UserVolumeSizeGib** *(integer) --*

        The size of the user storage.

      - **ComputeTypeName** *(string) --*

        The compute type. For more information, see `Amazon WorkSpaces Bundles
        <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

    - **Tags** *(list) --*

      The tags for the WorkSpace.

      - *(dict) --*

        Describes a tag.

        - **Key** *(string) --* **[REQUIRED]**

          The key of the tag.

        - **Value** *(string) --*

          The value of the tag.
    """


_ClientDescribeAccountModificationsResponseAccountModificationsTypeDef = TypedDict(
    "_ClientDescribeAccountModificationsResponseAccountModificationsTypeDef",
    {
        "ModificationState": str,
        "DedicatedTenancySupport": str,
        "DedicatedTenancyManagementCidrRange": str,
        "StartTime": datetime,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientDescribeAccountModificationsResponseAccountModificationsTypeDef(
    _ClientDescribeAccountModificationsResponseAccountModificationsTypeDef
):
    """
    Type definition for `ClientDescribeAccountModificationsResponse` `AccountModifications`

    Describes a modification to the configuration of Bring Your Own License (BYOL) for the
    specified account.

    - **ModificationState** *(string) --*

      The state of the modification to the configuration of BYOL.

    - **DedicatedTenancySupport** *(string) --*

      The status of BYOL (whether BYOL is being enabled or disabled).

    - **DedicatedTenancyManagementCidrRange** *(string) --*

      The IP address range, specified as an IPv4 CIDR block, for the management network
      interface used for the account.

    - **StartTime** *(datetime) --*

      The timestamp when the modification of the BYOL configuration was started.

    - **ErrorCode** *(string) --*

      The error code that is returned if the configuration of BYOL cannot be modified.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the configuration of BYOL cannot be
      modified.
    """


_ClientDescribeAccountModificationsResponseTypeDef = TypedDict(
    "_ClientDescribeAccountModificationsResponseTypeDef",
    {
        "AccountModifications": List[
            ClientDescribeAccountModificationsResponseAccountModificationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAccountModificationsResponseTypeDef(
    _ClientDescribeAccountModificationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAccountModifications` `Response`

    - **AccountModifications** *(list) --*

      The list of modifications to the configuration of BYOL.

      - *(dict) --*

        Describes a modification to the configuration of Bring Your Own License (BYOL) for the
        specified account.

        - **ModificationState** *(string) --*

          The state of the modification to the configuration of BYOL.

        - **DedicatedTenancySupport** *(string) --*

          The status of BYOL (whether BYOL is being enabled or disabled).

        - **DedicatedTenancyManagementCidrRange** *(string) --*

          The IP address range, specified as an IPv4 CIDR block, for the management network
          interface used for the account.

        - **StartTime** *(datetime) --*

          The timestamp when the modification of the BYOL configuration was started.

        - **ErrorCode** *(string) --*

          The error code that is returned if the configuration of BYOL cannot be modified.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the configuration of BYOL cannot be
          modified.

    - **NextToken** *(string) --*

      The token to use to retrieve the next set of results, or null if no more results are
      available.
    """


_ClientDescribeAccountResponseTypeDef = TypedDict(
    "_ClientDescribeAccountResponseTypeDef",
    {"DedicatedTenancySupport": str, "DedicatedTenancyManagementCidrRange": str},
    total=False,
)


class ClientDescribeAccountResponseTypeDef(_ClientDescribeAccountResponseTypeDef):
    """
    Type definition for `ClientDescribeAccount` `Response`

    - **DedicatedTenancySupport** *(string) --*

      The status of BYOL (whether BYOL is enabled or disabled).

    - **DedicatedTenancyManagementCidrRange** *(string) --*

      The IP address range, specified as an IPv4 CIDR block, used for the management network
      interface.

      The management network interface is connected to a secure Amazon WorkSpaces management
      network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces
      clients, and to allow Amazon WorkSpaces to manage the WorkSpace.
    """


_ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef = TypedDict(
    "_ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef",
    {"ReconnectEnabled": str},
    total=False,
)


class ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef(
    _ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeClientPropertiesResponseClientPropertiesList` `ClientProperties`

    Information about the Amazon WorkSpaces client.

    - **ReconnectEnabled** *(string) --*

      Specifies whether users can cache their credentials on the Amazon WorkSpaces client.
      When enabled, users can choose to reconnect to their WorkSpaces without re-entering
      their credentials.
    """


_ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef = TypedDict(
    "_ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef",
    {
        "ResourceId": str,
        "ClientProperties": ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef,
    },
    total=False,
)


class ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef(
    _ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef
):
    """
    Type definition for `ClientDescribeClientPropertiesResponse` `ClientPropertiesList`

    Information about the Amazon WorkSpaces client.

    - **ResourceId** *(string) --*

      The resource identifier, in the form of a directory ID.

    - **ClientProperties** *(dict) --*

      Information about the Amazon WorkSpaces client.

      - **ReconnectEnabled** *(string) --*

        Specifies whether users can cache their credentials on the Amazon WorkSpaces client.
        When enabled, users can choose to reconnect to their WorkSpaces without re-entering
        their credentials.
    """


_ClientDescribeClientPropertiesResponseTypeDef = TypedDict(
    "_ClientDescribeClientPropertiesResponseTypeDef",
    {
        "ClientPropertiesList": List[
            ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeClientPropertiesResponseTypeDef(
    _ClientDescribeClientPropertiesResponseTypeDef
):
    """
    Type definition for `ClientDescribeClientProperties` `Response`

    - **ClientPropertiesList** *(list) --*

      Information about the specified Amazon WorkSpaces clients.

      - *(dict) --*

        Information about the Amazon WorkSpaces client.

        - **ResourceId** *(string) --*

          The resource identifier, in the form of a directory ID.

        - **ClientProperties** *(dict) --*

          Information about the Amazon WorkSpaces client.

          - **ReconnectEnabled** *(string) --*

            Specifies whether users can cache their credentials on the Amazon WorkSpaces client.
            When enabled, users can choose to reconnect to their WorkSpaces without re-entering
            their credentials.
    """


_ClientDescribeIpGroupsResponseResultuserRulesTypeDef = TypedDict(
    "_ClientDescribeIpGroupsResponseResultuserRulesTypeDef",
    {"ipRule": str, "ruleDesc": str},
    total=False,
)


class ClientDescribeIpGroupsResponseResultuserRulesTypeDef(
    _ClientDescribeIpGroupsResponseResultuserRulesTypeDef
):
    """
    Type definition for `ClientDescribeIpGroupsResponseResult` `userRules`

    Describes a rule for an IP access control group.

    - **ipRule** *(string) --*

      The IP address range, in CIDR notation.

    - **ruleDesc** *(string) --*

      The description.
    """


_ClientDescribeIpGroupsResponseResultTypeDef = TypedDict(
    "_ClientDescribeIpGroupsResponseResultTypeDef",
    {
        "groupId": str,
        "groupName": str,
        "groupDesc": str,
        "userRules": List[ClientDescribeIpGroupsResponseResultuserRulesTypeDef],
    },
    total=False,
)


class ClientDescribeIpGroupsResponseResultTypeDef(
    _ClientDescribeIpGroupsResponseResultTypeDef
):
    """
    Type definition for `ClientDescribeIpGroupsResponse` `Result`

    Describes an IP access control group.

    - **groupId** *(string) --*

      The identifier of the group.

    - **groupName** *(string) --*

      The name of the group.

    - **groupDesc** *(string) --*

      The description of the group.

    - **userRules** *(list) --*

      The rules.

      - *(dict) --*

        Describes a rule for an IP access control group.

        - **ipRule** *(string) --*

          The IP address range, in CIDR notation.

        - **ruleDesc** *(string) --*

          The description.
    """


_ClientDescribeIpGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeIpGroupsResponseTypeDef",
    {"Result": List[ClientDescribeIpGroupsResponseResultTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeIpGroupsResponseTypeDef(_ClientDescribeIpGroupsResponseTypeDef):
    """
    Type definition for `ClientDescribeIpGroups` `Response`

    - **Result** *(list) --*

      Information about the IP access control groups.

      - *(dict) --*

        Describes an IP access control group.

        - **groupId** *(string) --*

          The identifier of the group.

        - **groupName** *(string) --*

          The name of the group.

        - **groupDesc** *(string) --*

          The description of the group.

        - **userRules** *(list) --*

          The rules.

          - *(dict) --*

            Describes a rule for an IP access control group.

            - **ipRule** *(string) --*

              The IP address range, in CIDR notation.

            - **ruleDesc** *(string) --*

              The description.

    - **NextToken** *(string) --*

      The token to use to retrieve the next set of results, or null if no more results are
      available.
    """


_ClientDescribeTagsResponseTagListTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeTagsResponseTagListTypeDef(
    _ClientDescribeTagsResponseTagListTypeDef
):
    """
    Type definition for `ClientDescribeTagsResponse` `TagList`

    Describes a tag.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"TagList": List[ClientDescribeTagsResponseTagListTypeDef]},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    Type definition for `ClientDescribeTags` `Response`

    - **TagList** *(list) --*

      The tags.

      - *(dict) --*

        Describes a tag.

        - **Key** *(string) --*

          The key of the tag.

        - **Value** *(string) --*

          The value of the tag.
    """


_ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef = TypedDict(
    "_ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef(
    _ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceBundlesResponseBundles` `ComputeType`

    The compute type. For more information, see `Amazon WorkSpaces Bundles
    <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

    - **Name** *(string) --*

      The compute type.
    """


_ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef = TypedDict(
    "_ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef",
    {"Capacity": str},
    total=False,
)


class ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef(
    _ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceBundlesResponseBundles` `RootStorage`

    The size of the root volume.

    - **Capacity** *(string) --*

      The size of the root volume.
    """


_ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef = TypedDict(
    "_ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef",
    {"Capacity": str},
    total=False,
)


class ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef(
    _ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceBundlesResponseBundles` `UserStorage`

    The size of the user storage.

    - **Capacity** *(string) --*

      The size of the user storage.
    """


_ClientDescribeWorkspaceBundlesResponseBundlesTypeDef = TypedDict(
    "_ClientDescribeWorkspaceBundlesResponseBundlesTypeDef",
    {
        "BundleId": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "RootStorage": ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef,
        "UserStorage": ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef,
        "ComputeType": ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef,
    },
    total=False,
)


class ClientDescribeWorkspaceBundlesResponseBundlesTypeDef(
    _ClientDescribeWorkspaceBundlesResponseBundlesTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceBundlesResponse` `Bundles`

    Describes a WorkSpace bundle.

    - **BundleId** *(string) --*

      The bundle identifier.

    - **Name** *(string) --*

      The name of the bundle.

    - **Owner** *(string) --*

      The owner of the bundle. This is the account identifier of the owner, or ``AMAZON`` if
      the bundle is provided by AWS.

    - **Description** *(string) --*

      A description.

    - **RootStorage** *(dict) --*

      The size of the root volume.

      - **Capacity** *(string) --*

        The size of the root volume.

    - **UserStorage** *(dict) --*

      The size of the user storage.

      - **Capacity** *(string) --*

        The size of the user storage.

    - **ComputeType** *(dict) --*

      The compute type. For more information, see `Amazon WorkSpaces Bundles
      <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

      - **Name** *(string) --*

        The compute type.
    """


_ClientDescribeWorkspaceBundlesResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspaceBundlesResponseTypeDef",
    {
        "Bundles": List[ClientDescribeWorkspaceBundlesResponseBundlesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeWorkspaceBundlesResponseTypeDef(
    _ClientDescribeWorkspaceBundlesResponseTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceBundles` `Response`

    - **Bundles** *(list) --*

      Information about the bundles.

      - *(dict) --*

        Describes a WorkSpace bundle.

        - **BundleId** *(string) --*

          The bundle identifier.

        - **Name** *(string) --*

          The name of the bundle.

        - **Owner** *(string) --*

          The owner of the bundle. This is the account identifier of the owner, or ``AMAZON`` if
          the bundle is provided by AWS.

        - **Description** *(string) --*

          A description.

        - **RootStorage** *(dict) --*

          The size of the root volume.

          - **Capacity** *(string) --*

            The size of the root volume.

        - **UserStorage** *(dict) --*

          The size of the user storage.

          - **Capacity** *(string) --*

            The size of the user storage.

        - **ComputeType** *(dict) --*

          The compute type. For more information, see `Amazon WorkSpaces Bundles
          <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

          - **Name** *(string) --*

            The compute type.

    - **NextToken** *(string) --*

      The token to use to retrieve the next set of results, or null if there are no more results
      available. This token is valid for one day and must be used within that time frame.
    """


_ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef = TypedDict(
    "_ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": str,
        "IncreaseVolumeSize": str,
        "ChangeComputeType": str,
        "SwitchRunningMode": str,
        "RebuildWorkspace": str,
    },
    total=False,
)


class ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef(
    _ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceDirectoriesResponseDirectories` `SelfservicePermissions`

    The default self-service permissions for WorkSpaces in the directory.

    - **RestartWorkspace** *(string) --*

      Specifies whether users can restart their WorkSpace.

    - **IncreaseVolumeSize** *(string) --*

      Specifies whether users can increase the volume size of the drives on their WorkSpace.

    - **ChangeComputeType** *(string) --*

      Specifies whether users can change the compute type (bundle) for their WorkSpace.

    - **SwitchRunningMode** *(string) --*

      Specifies whether users can switch the running mode of their WorkSpace.

    - **RebuildWorkspace** *(string) --*

      Specifies whether users can rebuild the operating system of a WorkSpace to its original
      state.
    """


_ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef = TypedDict(
    "_ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": str,
        "DeviceTypeOsx": str,
        "DeviceTypeWeb": str,
        "DeviceTypeIos": str,
        "DeviceTypeAndroid": str,
        "DeviceTypeChromeOs": str,
        "DeviceTypeZeroClient": str,
    },
    total=False,
)


class ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef(
    _ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceDirectoriesResponseDirectories` `WorkspaceAccessProperties`

    The devices and operating systems that users can use to access Workspaces.

    - **DeviceTypeWindows** *(string) --*

      Indicates whether users can use Windows clients to access their WorkSpaces. To restrict
      WorkSpaces access to trusted devices (also known as managed devices) with valid
      certificates, specify a value of ``TRUST`` . For more information, see `Restrict
      WorkSpaces Access to Trusted Devices
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

    - **DeviceTypeOsx** *(string) --*

      Indicates whether users can use macOS clients to access their WorkSpaces. To restrict
      WorkSpaces access to trusted devices (also known as managed devices) with valid
      certificates, specify a value of ``TRUST`` . For more information, see `Restrict
      WorkSpaces Access to Trusted Devices
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

    - **DeviceTypeWeb** *(string) --*

      Indicates whether users can access their WorkSpaces through a web browser.

    - **DeviceTypeIos** *(string) --*

      Indicates whether users can use iOS devices to access their WorkSpaces.

    - **DeviceTypeAndroid** *(string) --*

      Indicates whether users can use Android devices to access their WorkSpaces.

    - **DeviceTypeChromeOs** *(string) --*

      Indicates whether users can use Chromebooks to access their WorkSpaces.

    - **DeviceTypeZeroClient** *(string) --*

      Indicates whether users can use zero client devices to access their WorkSpaces.
    """


_ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef = TypedDict(
    "_ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)


class ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef(
    _ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceDirectoriesResponseDirectories` `WorkspaceCreationProperties`

    The default creation properties for all WorkSpaces in the directory.

    - **EnableWorkDocs** *(boolean) --*

      Specifies whether the directory is enabled for Amazon WorkDocs.

    - **EnableInternetAccess** *(boolean) --*

      Specifies whether to automatically assign a public IP address to WorkSpaces in this
      directory by default. If enabled, the public IP address allows outbound internet access
      from your WorkSpaces when you’re using an internet gateway in the Amazon VPC in which
      your WorkSpaces are located. If you're using a Network Address Translation (NAT)
      gateway for outbound internet access from your VPC, or if your WorkSpaces are in public
      subnets and you manually assign them Elastic IP addresses, you should disable this
      setting. This setting applies to new WorkSpaces that you launch or to existing
      WorkSpaces that you rebuild. For more information, see `Configure a VPC for Amazon
      WorkSpaces
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html>`__
      .

    - **DefaultOu** *(string) --*

      The organizational unit (OU) in the directory for the WorkSpace machine accounts.

    - **CustomSecurityGroupId** *(string) --*

      The identifier of any security groups to apply to WorkSpaces when they are created.

    - **UserEnabledAsLocalAdministrator** *(boolean) --*

      Specifies whether WorkSpace users are local administrators on their WorkSpaces.

    - **EnableMaintenanceMode** *(boolean) --*

      Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see
      `WorkSpace Maintenance
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html>`__
      .
    """


_ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef = TypedDict(
    "_ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "DirectoryName": str,
        "RegistrationCode": str,
        "SubnetIds": List[str],
        "DnsIpAddresses": List[str],
        "CustomerUserName": str,
        "IamRoleId": str,
        "DirectoryType": str,
        "WorkspaceSecurityGroupId": str,
        "State": str,
        "WorkspaceCreationProperties": ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef,
        "ipGroupIds": List[str],
        "WorkspaceAccessProperties": ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef,
        "Tenancy": str,
        "SelfservicePermissions": ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef,
    },
    total=False,
)


class ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef(
    _ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceDirectoriesResponse` `Directories`

    Describes a directory that is used with Amazon WorkSpaces.

    - **DirectoryId** *(string) --*

      The directory identifier.

    - **Alias** *(string) --*

      The directory alias.

    - **DirectoryName** *(string) --*

      The name of the directory.

    - **RegistrationCode** *(string) --*

      The registration code for the directory. This is the code that users enter in their
      Amazon WorkSpaces client application to connect to the directory.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets used with the directory.

      - *(string) --*

    - **DnsIpAddresses** *(list) --*

      The IP addresses of the DNS servers for the directory.

      - *(string) --*

    - **CustomerUserName** *(string) --*

      The user name for the service account.

    - **IamRoleId** *(string) --*

      The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make
      calls to other services, such as Amazon EC2, on your behalf.

    - **DirectoryType** *(string) --*

      The directory type.

    - **WorkspaceSecurityGroupId** *(string) --*

      The identifier of the security group that is assigned to new WorkSpaces.

    - **State** *(string) --*

      The state of the directory's registration with Amazon WorkSpaces.

    - **WorkspaceCreationProperties** *(dict) --*

      The default creation properties for all WorkSpaces in the directory.

      - **EnableWorkDocs** *(boolean) --*

        Specifies whether the directory is enabled for Amazon WorkDocs.

      - **EnableInternetAccess** *(boolean) --*

        Specifies whether to automatically assign a public IP address to WorkSpaces in this
        directory by default. If enabled, the public IP address allows outbound internet access
        from your WorkSpaces when you’re using an internet gateway in the Amazon VPC in which
        your WorkSpaces are located. If you're using a Network Address Translation (NAT)
        gateway for outbound internet access from your VPC, or if your WorkSpaces are in public
        subnets and you manually assign them Elastic IP addresses, you should disable this
        setting. This setting applies to new WorkSpaces that you launch or to existing
        WorkSpaces that you rebuild. For more information, see `Configure a VPC for Amazon
        WorkSpaces
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html>`__
        .

      - **DefaultOu** *(string) --*

        The organizational unit (OU) in the directory for the WorkSpace machine accounts.

      - **CustomSecurityGroupId** *(string) --*

        The identifier of any security groups to apply to WorkSpaces when they are created.

      - **UserEnabledAsLocalAdministrator** *(boolean) --*

        Specifies whether WorkSpace users are local administrators on their WorkSpaces.

      - **EnableMaintenanceMode** *(boolean) --*

        Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see
        `WorkSpace Maintenance
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html>`__
        .

    - **ipGroupIds** *(list) --*

      The identifiers of the IP access control groups associated with the directory.

      - *(string) --*

    - **WorkspaceAccessProperties** *(dict) --*

      The devices and operating systems that users can use to access Workspaces.

      - **DeviceTypeWindows** *(string) --*

        Indicates whether users can use Windows clients to access their WorkSpaces. To restrict
        WorkSpaces access to trusted devices (also known as managed devices) with valid
        certificates, specify a value of ``TRUST`` . For more information, see `Restrict
        WorkSpaces Access to Trusted Devices
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

      - **DeviceTypeOsx** *(string) --*

        Indicates whether users can use macOS clients to access their WorkSpaces. To restrict
        WorkSpaces access to trusted devices (also known as managed devices) with valid
        certificates, specify a value of ``TRUST`` . For more information, see `Restrict
        WorkSpaces Access to Trusted Devices
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

      - **DeviceTypeWeb** *(string) --*

        Indicates whether users can access their WorkSpaces through a web browser.

      - **DeviceTypeIos** *(string) --*

        Indicates whether users can use iOS devices to access their WorkSpaces.

      - **DeviceTypeAndroid** *(string) --*

        Indicates whether users can use Android devices to access their WorkSpaces.

      - **DeviceTypeChromeOs** *(string) --*

        Indicates whether users can use Chromebooks to access their WorkSpaces.

      - **DeviceTypeZeroClient** *(string) --*

        Indicates whether users can use zero client devices to access their WorkSpaces.

    - **Tenancy** *(string) --*

      Specifies whether the directory is dedicated or shared. To use Bring Your Own License
      (BYOL), this value must be set to ``DEDICATED`` . For more information, see `Bring Your
      Own Windows Desktop Images
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html>`__ .

    - **SelfservicePermissions** *(dict) --*

      The default self-service permissions for WorkSpaces in the directory.

      - **RestartWorkspace** *(string) --*

        Specifies whether users can restart their WorkSpace.

      - **IncreaseVolumeSize** *(string) --*

        Specifies whether users can increase the volume size of the drives on their WorkSpace.

      - **ChangeComputeType** *(string) --*

        Specifies whether users can change the compute type (bundle) for their WorkSpace.

      - **SwitchRunningMode** *(string) --*

        Specifies whether users can switch the running mode of their WorkSpace.

      - **RebuildWorkspace** *(string) --*

        Specifies whether users can rebuild the operating system of a WorkSpace to its original
        state.
    """


_ClientDescribeWorkspaceDirectoriesResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspaceDirectoriesResponseTypeDef",
    {
        "Directories": List[
            ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeWorkspaceDirectoriesResponseTypeDef(
    _ClientDescribeWorkspaceDirectoriesResponseTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceDirectories` `Response`

    - **Directories** *(list) --*

      Information about the directories.

      - *(dict) --*

        Describes a directory that is used with Amazon WorkSpaces.

        - **DirectoryId** *(string) --*

          The directory identifier.

        - **Alias** *(string) --*

          The directory alias.

        - **DirectoryName** *(string) --*

          The name of the directory.

        - **RegistrationCode** *(string) --*

          The registration code for the directory. This is the code that users enter in their
          Amazon WorkSpaces client application to connect to the directory.

        - **SubnetIds** *(list) --*

          The identifiers of the subnets used with the directory.

          - *(string) --*

        - **DnsIpAddresses** *(list) --*

          The IP addresses of the DNS servers for the directory.

          - *(string) --*

        - **CustomerUserName** *(string) --*

          The user name for the service account.

        - **IamRoleId** *(string) --*

          The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make
          calls to other services, such as Amazon EC2, on your behalf.

        - **DirectoryType** *(string) --*

          The directory type.

        - **WorkspaceSecurityGroupId** *(string) --*

          The identifier of the security group that is assigned to new WorkSpaces.

        - **State** *(string) --*

          The state of the directory's registration with Amazon WorkSpaces.

        - **WorkspaceCreationProperties** *(dict) --*

          The default creation properties for all WorkSpaces in the directory.

          - **EnableWorkDocs** *(boolean) --*

            Specifies whether the directory is enabled for Amazon WorkDocs.

          - **EnableInternetAccess** *(boolean) --*

            Specifies whether to automatically assign a public IP address to WorkSpaces in this
            directory by default. If enabled, the public IP address allows outbound internet access
            from your WorkSpaces when you’re using an internet gateway in the Amazon VPC in which
            your WorkSpaces are located. If you're using a Network Address Translation (NAT)
            gateway for outbound internet access from your VPC, or if your WorkSpaces are in public
            subnets and you manually assign them Elastic IP addresses, you should disable this
            setting. This setting applies to new WorkSpaces that you launch or to existing
            WorkSpaces that you rebuild. For more information, see `Configure a VPC for Amazon
            WorkSpaces
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html>`__
            .

          - **DefaultOu** *(string) --*

            The organizational unit (OU) in the directory for the WorkSpace machine accounts.

          - **CustomSecurityGroupId** *(string) --*

            The identifier of any security groups to apply to WorkSpaces when they are created.

          - **UserEnabledAsLocalAdministrator** *(boolean) --*

            Specifies whether WorkSpace users are local administrators on their WorkSpaces.

          - **EnableMaintenanceMode** *(boolean) --*

            Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see
            `WorkSpace Maintenance
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html>`__
            .

        - **ipGroupIds** *(list) --*

          The identifiers of the IP access control groups associated with the directory.

          - *(string) --*

        - **WorkspaceAccessProperties** *(dict) --*

          The devices and operating systems that users can use to access Workspaces.

          - **DeviceTypeWindows** *(string) --*

            Indicates whether users can use Windows clients to access their WorkSpaces. To restrict
            WorkSpaces access to trusted devices (also known as managed devices) with valid
            certificates, specify a value of ``TRUST`` . For more information, see `Restrict
            WorkSpaces Access to Trusted Devices
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

          - **DeviceTypeOsx** *(string) --*

            Indicates whether users can use macOS clients to access their WorkSpaces. To restrict
            WorkSpaces access to trusted devices (also known as managed devices) with valid
            certificates, specify a value of ``TRUST`` . For more information, see `Restrict
            WorkSpaces Access to Trusted Devices
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

          - **DeviceTypeWeb** *(string) --*

            Indicates whether users can access their WorkSpaces through a web browser.

          - **DeviceTypeIos** *(string) --*

            Indicates whether users can use iOS devices to access their WorkSpaces.

          - **DeviceTypeAndroid** *(string) --*

            Indicates whether users can use Android devices to access their WorkSpaces.

          - **DeviceTypeChromeOs** *(string) --*

            Indicates whether users can use Chromebooks to access their WorkSpaces.

          - **DeviceTypeZeroClient** *(string) --*

            Indicates whether users can use zero client devices to access their WorkSpaces.

        - **Tenancy** *(string) --*

          Specifies whether the directory is dedicated or shared. To use Bring Your Own License
          (BYOL), this value must be set to ``DEDICATED`` . For more information, see `Bring Your
          Own Windows Desktop Images
          <https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html>`__ .

        - **SelfservicePermissions** *(dict) --*

          The default self-service permissions for WorkSpaces in the directory.

          - **RestartWorkspace** *(string) --*

            Specifies whether users can restart their WorkSpace.

          - **IncreaseVolumeSize** *(string) --*

            Specifies whether users can increase the volume size of the drives on their WorkSpace.

          - **ChangeComputeType** *(string) --*

            Specifies whether users can change the compute type (bundle) for their WorkSpace.

          - **SwitchRunningMode** *(string) --*

            Specifies whether users can switch the running mode of their WorkSpace.

          - **RebuildWorkspace** *(string) --*

            Specifies whether users can rebuild the operating system of a WorkSpace to its original
            state.

    - **NextToken** *(string) --*

      The token to use to retrieve the next set of results, or null if no more results are
      available.
    """


_ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef = TypedDict(
    "_ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef",
    {"Type": str},
    total=False,
)


class ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef(
    _ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceImagesResponseImages` `OperatingSystem`

    The operating system that the image is running.

    - **Type** *(string) --*

      The operating system.
    """


_ClientDescribeWorkspaceImagesResponseImagesTypeDef = TypedDict(
    "_ClientDescribeWorkspaceImagesResponseImagesTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef,
        "State": str,
        "RequiredTenancy": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientDescribeWorkspaceImagesResponseImagesTypeDef(
    _ClientDescribeWorkspaceImagesResponseImagesTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceImagesResponse` `Images`

    Describes a WorkSpace image.

    - **ImageId** *(string) --*

      The identifier of the image.

    - **Name** *(string) --*

      The name of the image.

    - **Description** *(string) --*

      The description of the image.

    - **OperatingSystem** *(dict) --*

      The operating system that the image is running.

      - **Type** *(string) --*

        The operating system.

    - **State** *(string) --*

      The status of the image.

    - **RequiredTenancy** *(string) --*

      Specifies whether the image is running on dedicated hardware. When Bring Your Own License
      (BYOL) is enabled, this value is set to ``DEDICATED`` . For more information, see `Bring
      Your Own Windows Desktop Images
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html>`__ .

    - **ErrorCode** *(string) --*

      The error code that is returned for the image.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned for the image.
    """


_ClientDescribeWorkspaceImagesResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspaceImagesResponseTypeDef",
    {
        "Images": List[ClientDescribeWorkspaceImagesResponseImagesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeWorkspaceImagesResponseTypeDef(
    _ClientDescribeWorkspaceImagesResponseTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceImages` `Response`

    - **Images** *(list) --*

      Information about the images.

      - *(dict) --*

        Describes a WorkSpace image.

        - **ImageId** *(string) --*

          The identifier of the image.

        - **Name** *(string) --*

          The name of the image.

        - **Description** *(string) --*

          The description of the image.

        - **OperatingSystem** *(dict) --*

          The operating system that the image is running.

          - **Type** *(string) --*

            The operating system.

        - **State** *(string) --*

          The status of the image.

        - **RequiredTenancy** *(string) --*

          Specifies whether the image is running on dedicated hardware. When Bring Your Own License
          (BYOL) is enabled, this value is set to ``DEDICATED`` . For more information, see `Bring
          Your Own Windows Desktop Images
          <https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html>`__ .

        - **ErrorCode** *(string) --*

          The error code that is returned for the image.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned for the image.

    - **NextToken** *(string) --*

      The token to use to retrieve the next set of results, or null if no more results are
      available.
    """


_ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef = TypedDict(
    "_ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef",
    {"SnapshotTime": datetime},
    total=False,
)


class ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef(
    _ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceSnapshotsResponse` `RebuildSnapshots`

    Describes a snapshot.

    - **SnapshotTime** *(datetime) --*

      The time when the snapshot was created.
    """


_ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef = TypedDict(
    "_ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef",
    {"SnapshotTime": datetime},
    total=False,
)


class ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef(
    _ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceSnapshotsResponse` `RestoreSnapshots`

    Describes a snapshot.

    - **SnapshotTime** *(datetime) --*

      The time when the snapshot was created.
    """


_ClientDescribeWorkspaceSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspaceSnapshotsResponseTypeDef",
    {
        "RebuildSnapshots": List[
            ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef
        ],
        "RestoreSnapshots": List[
            ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeWorkspaceSnapshotsResponseTypeDef(
    _ClientDescribeWorkspaceSnapshotsResponseTypeDef
):
    """
    Type definition for `ClientDescribeWorkspaceSnapshots` `Response`

    - **RebuildSnapshots** *(list) --*

      Information about the snapshots that can be used to rebuild a WorkSpace. These snapshots
      include the user volume.

      - *(dict) --*

        Describes a snapshot.

        - **SnapshotTime** *(datetime) --*

          The time when the snapshot was created.

    - **RestoreSnapshots** *(list) --*

      Information about the snapshots that can be used to restore a WorkSpace. These snapshots
      include both the root volume and the user volume.

      - *(dict) --*

        Describes a snapshot.

        - **SnapshotTime** *(datetime) --*

          The time when the snapshot was created.
    """


_ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef = TypedDict(
    "_ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef",
    {
        "WorkspaceId": str,
        "ConnectionState": str,
        "ConnectionStateCheckTimestamp": datetime,
        "LastKnownUserConnectionTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef(
    _ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef
):
    """
    Type definition for `ClientDescribeWorkspacesConnectionStatusResponse` `WorkspacesConnectionStatus`

    Describes the connection status of a WorkSpace.

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.

    - **ConnectionState** *(string) --*

      The connection state of the WorkSpace. The connection state is unknown if the WorkSpace
      is stopped.

    - **ConnectionStateCheckTimestamp** *(datetime) --*

      The timestamp of the connection status check.

    - **LastKnownUserConnectionTimestamp** *(datetime) --*

      The timestamp of the last known user connection.
    """


_ClientDescribeWorkspacesConnectionStatusResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspacesConnectionStatusResponseTypeDef",
    {
        "WorkspacesConnectionStatus": List[
            ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeWorkspacesConnectionStatusResponseTypeDef(
    _ClientDescribeWorkspacesConnectionStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeWorkspacesConnectionStatus` `Response`

    - **WorkspacesConnectionStatus** *(list) --*

      Information about the connection status of the WorkSpace.

      - *(dict) --*

        Describes the connection status of a WorkSpace.

        - **WorkspaceId** *(string) --*

          The identifier of the WorkSpace.

        - **ConnectionState** *(string) --*

          The connection state of the WorkSpace. The connection state is unknown if the WorkSpace
          is stopped.

        - **ConnectionStateCheckTimestamp** *(datetime) --*

          The timestamp of the connection status check.

        - **LastKnownUserConnectionTimestamp** *(datetime) --*

          The timestamp of the last known user connection.

    - **NextToken** *(string) --*

      The token to use to retrieve the next set of results, or null if no more results are
      available.
    """


_ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef = TypedDict(
    "_ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef",
    {"Resource": str, "State": str},
    total=False,
)


class ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef(
    _ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef
):
    """
    Type definition for `ClientDescribeWorkspacesResponseWorkspaces` `ModificationStates`

    Describes a WorkSpace modification.

    - **Resource** *(string) --*

      The resource.

    - **State** *(string) --*

      The modification state.
    """


_ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef = TypedDict(
    "_ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef",
    {
        "RunningMode": str,
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": str,
    },
    total=False,
)


class ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef(
    _ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef
):
    """
    Type definition for `ClientDescribeWorkspacesResponseWorkspaces` `WorkspaceProperties`

    The properties of the WorkSpace.

    - **RunningMode** *(string) --*

      The running mode. For more information, see `Manage the WorkSpace Running Mode
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

    - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

      The time after a user logs off when WorkSpaces are automatically stopped. Configured in
      60-minute intervals.

    - **RootVolumeSizeGib** *(integer) --*

      The size of the root volume.

    - **UserVolumeSizeGib** *(integer) --*

      The size of the user storage.

    - **ComputeTypeName** *(string) --*

      The compute type. For more information, see `Amazon WorkSpaces Bundles
      <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
    """


_ClientDescribeWorkspacesResponseWorkspacesTypeDef = TypedDict(
    "_ClientDescribeWorkspacesResponseWorkspacesTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": str,
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef,
        "ModificationStates": List[
            ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeWorkspacesResponseWorkspacesTypeDef(
    _ClientDescribeWorkspacesResponseWorkspacesTypeDef
):
    """
    Type definition for `ClientDescribeWorkspacesResponse` `Workspaces`

    Describes a WorkSpace.

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.

    - **DirectoryId** *(string) --*

      The identifier of the AWS Directory Service directory for the WorkSpace.

    - **UserName** *(string) --*

      The user for the WorkSpace.

    - **IpAddress** *(string) --*

      The IP address of the WorkSpace.

    - **State** *(string) --*

      The operational state of the WorkSpace.

    - **BundleId** *(string) --*

      The identifier of the bundle used to create the WorkSpace.

    - **SubnetId** *(string) --*

      The identifier of the subnet for the WorkSpace.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the WorkSpace cannot be created.

    - **ErrorCode** *(string) --*

      The error code that is returned if the WorkSpace cannot be created.

    - **ComputerName** *(string) --*

      The name of the WorkSpace, as seen by the operating system.

    - **VolumeEncryptionKey** *(string) --*

      The KMS key used to encrypt data stored on your WorkSpace.

    - **UserVolumeEncryptionEnabled** *(boolean) --*

      Indicates whether the data stored on the user volume is encrypted.

    - **RootVolumeEncryptionEnabled** *(boolean) --*

      Indicates whether the data stored on the root volume is encrypted.

    - **WorkspaceProperties** *(dict) --*

      The properties of the WorkSpace.

      - **RunningMode** *(string) --*

        The running mode. For more information, see `Manage the WorkSpace Running Mode
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

      - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

        The time after a user logs off when WorkSpaces are automatically stopped. Configured in
        60-minute intervals.

      - **RootVolumeSizeGib** *(integer) --*

        The size of the root volume.

      - **UserVolumeSizeGib** *(integer) --*

        The size of the user storage.

      - **ComputeTypeName** *(string) --*

        The compute type. For more information, see `Amazon WorkSpaces Bundles
        <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

    - **ModificationStates** *(list) --*

      The modification states of the WorkSpace.

      - *(dict) --*

        Describes a WorkSpace modification.

        - **Resource** *(string) --*

          The resource.

        - **State** *(string) --*

          The modification state.
    """


_ClientDescribeWorkspacesResponseTypeDef = TypedDict(
    "_ClientDescribeWorkspacesResponseTypeDef",
    {
        "Workspaces": List[ClientDescribeWorkspacesResponseWorkspacesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeWorkspacesResponseTypeDef(_ClientDescribeWorkspacesResponseTypeDef):
    """
    Type definition for `ClientDescribeWorkspaces` `Response`

    - **Workspaces** *(list) --*

      Information about the WorkSpaces.

      Because  CreateWorkspaces is an asynchronous operation, some of the returned information
      could be incomplete.

      - *(dict) --*

        Describes a WorkSpace.

        - **WorkspaceId** *(string) --*

          The identifier of the WorkSpace.

        - **DirectoryId** *(string) --*

          The identifier of the AWS Directory Service directory for the WorkSpace.

        - **UserName** *(string) --*

          The user for the WorkSpace.

        - **IpAddress** *(string) --*

          The IP address of the WorkSpace.

        - **State** *(string) --*

          The operational state of the WorkSpace.

        - **BundleId** *(string) --*

          The identifier of the bundle used to create the WorkSpace.

        - **SubnetId** *(string) --*

          The identifier of the subnet for the WorkSpace.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the WorkSpace cannot be created.

        - **ErrorCode** *(string) --*

          The error code that is returned if the WorkSpace cannot be created.

        - **ComputerName** *(string) --*

          The name of the WorkSpace, as seen by the operating system.

        - **VolumeEncryptionKey** *(string) --*

          The KMS key used to encrypt data stored on your WorkSpace.

        - **UserVolumeEncryptionEnabled** *(boolean) --*

          Indicates whether the data stored on the user volume is encrypted.

        - **RootVolumeEncryptionEnabled** *(boolean) --*

          Indicates whether the data stored on the root volume is encrypted.

        - **WorkspaceProperties** *(dict) --*

          The properties of the WorkSpace.

          - **RunningMode** *(string) --*

            The running mode. For more information, see `Manage the WorkSpace Running Mode
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

          - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

            The time after a user logs off when WorkSpaces are automatically stopped. Configured in
            60-minute intervals.

          - **RootVolumeSizeGib** *(integer) --*

            The size of the root volume.

          - **UserVolumeSizeGib** *(integer) --*

            The size of the user storage.

          - **ComputeTypeName** *(string) --*

            The compute type. For more information, see `Amazon WorkSpaces Bundles
            <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

        - **ModificationStates** *(list) --*

          The modification states of the WorkSpace.

          - *(dict) --*

            Describes a WorkSpace modification.

            - **Resource** *(string) --*

              The resource.

            - **State** *(string) --*

              The modification state.

    - **NextToken** *(string) --*

      The token to use to retrieve the next set of results, or null if no more results are
      available.
    """


_ClientImportWorkspaceImageResponseTypeDef = TypedDict(
    "_ClientImportWorkspaceImageResponseTypeDef", {"ImageId": str}, total=False
)


class ClientImportWorkspaceImageResponseTypeDef(
    _ClientImportWorkspaceImageResponseTypeDef
):
    """
    Type definition for `ClientImportWorkspaceImage` `Response`

    - **ImageId** *(string) --*

      The identifier of the WorkSpace image.
    """


_RequiredClientImportWorkspaceImageTagsTypeDef = TypedDict(
    "_RequiredClientImportWorkspaceImageTagsTypeDef", {"Key": str}
)
_OptionalClientImportWorkspaceImageTagsTypeDef = TypedDict(
    "_OptionalClientImportWorkspaceImageTagsTypeDef", {"Value": str}, total=False
)


class ClientImportWorkspaceImageTagsTypeDef(
    _RequiredClientImportWorkspaceImageTagsTypeDef,
    _OptionalClientImportWorkspaceImageTagsTypeDef,
):
    """
    Type definition for `ClientImportWorkspaceImage` `Tags`

    Describes a tag.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientListAvailableManagementCidrRangesResponseTypeDef = TypedDict(
    "_ClientListAvailableManagementCidrRangesResponseTypeDef",
    {"ManagementCidrRanges": List[str], "NextToken": str},
    total=False,
)


class ClientListAvailableManagementCidrRangesResponseTypeDef(
    _ClientListAvailableManagementCidrRangesResponseTypeDef
):
    """
    Type definition for `ClientListAvailableManagementCidrRanges` `Response`

    - **ManagementCidrRanges** *(list) --*

      The list of available IP address ranges, specified as IPv4 CIDR blocks.

      - *(string) --*

    - **NextToken** *(string) --*

      The token to use to retrieve the next set of results, or null if no more results are
      available.
    """


_ClientModifyClientPropertiesClientPropertiesTypeDef = TypedDict(
    "_ClientModifyClientPropertiesClientPropertiesTypeDef",
    {"ReconnectEnabled": str},
    total=False,
)


class ClientModifyClientPropertiesClientPropertiesTypeDef(
    _ClientModifyClientPropertiesClientPropertiesTypeDef
):
    """
    Type definition for `ClientModifyClientProperties` `ClientProperties`

    Information about the Amazon WorkSpaces client.

    - **ReconnectEnabled** *(string) --*

      Specifies whether users can cache their credentials on the Amazon WorkSpaces client. When
      enabled, users can choose to reconnect to their WorkSpaces without re-entering their
      credentials.
    """


_ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef = TypedDict(
    "_ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": str,
        "IncreaseVolumeSize": str,
        "ChangeComputeType": str,
        "SwitchRunningMode": str,
        "RebuildWorkspace": str,
    },
    total=False,
)


class ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef(
    _ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef
):
    """
    Type definition for `ClientModifySelfservicePermissions` `SelfservicePermissions`

    The permissions to enable or disable self-service capabilities.

    - **RestartWorkspace** *(string) --*

      Specifies whether users can restart their WorkSpace.

    - **IncreaseVolumeSize** *(string) --*

      Specifies whether users can increase the volume size of the drives on their WorkSpace.

    - **ChangeComputeType** *(string) --*

      Specifies whether users can change the compute type (bundle) for their WorkSpace.

    - **SwitchRunningMode** *(string) --*

      Specifies whether users can switch the running mode of their WorkSpace.

    - **RebuildWorkspace** *(string) --*

      Specifies whether users can rebuild the operating system of a WorkSpace to its original state.
    """


_ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef = TypedDict(
    "_ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": str,
        "DeviceTypeOsx": str,
        "DeviceTypeWeb": str,
        "DeviceTypeIos": str,
        "DeviceTypeAndroid": str,
        "DeviceTypeChromeOs": str,
        "DeviceTypeZeroClient": str,
    },
    total=False,
)


class ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef(
    _ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef
):
    """
    Type definition for `ClientModifyWorkspaceAccessProperties` `WorkspaceAccessProperties`

    The device types and operating systems to enable or disable for access.

    - **DeviceTypeWindows** *(string) --*

      Indicates whether users can use Windows clients to access their WorkSpaces. To restrict
      WorkSpaces access to trusted devices (also known as managed devices) with valid certificates,
      specify a value of ``TRUST`` . For more information, see `Restrict WorkSpaces Access to Trusted
      Devices <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

    - **DeviceTypeOsx** *(string) --*

      Indicates whether users can use macOS clients to access their WorkSpaces. To restrict
      WorkSpaces access to trusted devices (also known as managed devices) with valid certificates,
      specify a value of ``TRUST`` . For more information, see `Restrict WorkSpaces Access to Trusted
      Devices <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

    - **DeviceTypeWeb** *(string) --*

      Indicates whether users can access their WorkSpaces through a web browser.

    - **DeviceTypeIos** *(string) --*

      Indicates whether users can use iOS devices to access their WorkSpaces.

    - **DeviceTypeAndroid** *(string) --*

      Indicates whether users can use Android devices to access their WorkSpaces.

    - **DeviceTypeChromeOs** *(string) --*

      Indicates whether users can use Chromebooks to access their WorkSpaces.

    - **DeviceTypeZeroClient** *(string) --*

      Indicates whether users can use zero client devices to access their WorkSpaces.
    """


_ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef = TypedDict(
    "_ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef",
    {
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)


class ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef(
    _ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef
):
    """
    Type definition for `ClientModifyWorkspaceCreationProperties` `WorkspaceCreationProperties`

    The default properties for creating WorkSpaces.

    - **EnableInternetAccess** *(boolean) --*

      Indicates whether internet access is enabled for your WorkSpaces.

    - **DefaultOu** *(string) --*

      The default organizational unit (OU) for your WorkSpace directories.

    - **CustomSecurityGroupId** *(string) --*

      The identifier of your custom security group.

    - **UserEnabledAsLocalAdministrator** *(boolean) --*

      Indicates whether users are local administrators of their WorkSpaces.

    - **EnableMaintenanceMode** *(boolean) --*

      Indicates whether maintenance mode is enabled for your WorkSpaces. For more information, see
      `WorkSpace Maintenance
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html>`__ .
    """


_ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef = TypedDict(
    "_ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef",
    {
        "RunningMode": str,
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": str,
    },
    total=False,
)


class ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef(
    _ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef
):
    """
    Type definition for `ClientModifyWorkspaceProperties` `WorkspaceProperties`

    The properties of the WorkSpace.

    - **RunningMode** *(string) --*

      The running mode. For more information, see `Manage the WorkSpace Running Mode
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

    - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

      The time after a user logs off when WorkSpaces are automatically stopped. Configured in
      60-minute intervals.

    - **RootVolumeSizeGib** *(integer) --*

      The size of the root volume.

    - **UserVolumeSizeGib** *(integer) --*

      The size of the user storage.

    - **ComputeTypeName** *(string) --*

      The compute type. For more information, see `Amazon WorkSpaces Bundles
      <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
    """


_ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef = TypedDict(
    "_ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef", {"WorkspaceId": str}
)


class ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef(
    _ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef
):
    """
    Type definition for `ClientRebootWorkspaces` `RebootWorkspaceRequests`

    Describes the information used to reboot a WorkSpace.

    - **WorkspaceId** *(string) --* **[REQUIRED]**

      The identifier of the WorkSpace.
    """


_ClientRebootWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientRebootWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientRebootWorkspacesResponseFailedRequestsTypeDef(
    _ClientRebootWorkspacesResponseFailedRequestsTypeDef
):
    """
    Type definition for `ClientRebootWorkspacesResponse` `FailedRequests`

    Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
    RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
    started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.

    - **ErrorCode** *(string) --*

      The error code that is returned if the WorkSpace cannot be rebooted.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the WorkSpace cannot be rebooted.
    """


_ClientRebootWorkspacesResponseTypeDef = TypedDict(
    "_ClientRebootWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientRebootWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)


class ClientRebootWorkspacesResponseTypeDef(_ClientRebootWorkspacesResponseTypeDef):
    """
    Type definition for `ClientRebootWorkspaces` `Response`

    - **FailedRequests** *(list) --*

      Information about the WorkSpaces that could not be rebooted.

      - *(dict) --*

        Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
        RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
        started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

        - **WorkspaceId** *(string) --*

          The identifier of the WorkSpace.

        - **ErrorCode** *(string) --*

          The error code that is returned if the WorkSpace cannot be rebooted.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the WorkSpace cannot be rebooted.
    """


_ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef = TypedDict(
    "_ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef", {"WorkspaceId": str}
)


class ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef(
    _ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef
):
    """
    Type definition for `ClientRebuildWorkspaces` `RebuildWorkspaceRequests`

    Describes the information used to rebuild a WorkSpace.

    - **WorkspaceId** *(string) --* **[REQUIRED]**

      The identifier of the WorkSpace.
    """


_ClientRebuildWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientRebuildWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientRebuildWorkspacesResponseFailedRequestsTypeDef(
    _ClientRebuildWorkspacesResponseFailedRequestsTypeDef
):
    """
    Type definition for `ClientRebuildWorkspacesResponse` `FailedRequests`

    Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
    RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
    started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.

    - **ErrorCode** *(string) --*

      The error code that is returned if the WorkSpace cannot be rebooted.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the WorkSpace cannot be rebooted.
    """


_ClientRebuildWorkspacesResponseTypeDef = TypedDict(
    "_ClientRebuildWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientRebuildWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)


class ClientRebuildWorkspacesResponseTypeDef(_ClientRebuildWorkspacesResponseTypeDef):
    """
    Type definition for `ClientRebuildWorkspaces` `Response`

    - **FailedRequests** *(list) --*

      Information about the WorkSpace that could not be rebuilt.

      - *(dict) --*

        Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
        RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
        started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

        - **WorkspaceId** *(string) --*

          The identifier of the WorkSpace.

        - **ErrorCode** *(string) --*

          The error code that is returned if the WorkSpace cannot be rebooted.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the WorkSpace cannot be rebooted.
    """


_RequiredClientRegisterWorkspaceDirectoryTagsTypeDef = TypedDict(
    "_RequiredClientRegisterWorkspaceDirectoryTagsTypeDef", {"Key": str}
)
_OptionalClientRegisterWorkspaceDirectoryTagsTypeDef = TypedDict(
    "_OptionalClientRegisterWorkspaceDirectoryTagsTypeDef", {"Value": str}, total=False
)


class ClientRegisterWorkspaceDirectoryTagsTypeDef(
    _RequiredClientRegisterWorkspaceDirectoryTagsTypeDef,
    _OptionalClientRegisterWorkspaceDirectoryTagsTypeDef,
):
    """
    Type definition for `ClientRegisterWorkspaceDirectory` `Tags`

    Describes a tag.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientStartWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientStartWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientStartWorkspacesResponseFailedRequestsTypeDef(
    _ClientStartWorkspacesResponseFailedRequestsTypeDef
):
    """
    Type definition for `ClientStartWorkspacesResponse` `FailedRequests`

    Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
    RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
    started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.

    - **ErrorCode** *(string) --*

      The error code that is returned if the WorkSpace cannot be rebooted.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the WorkSpace cannot be rebooted.
    """


_ClientStartWorkspacesResponseTypeDef = TypedDict(
    "_ClientStartWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientStartWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)


class ClientStartWorkspacesResponseTypeDef(_ClientStartWorkspacesResponseTypeDef):
    """
    Type definition for `ClientStartWorkspaces` `Response`

    - **FailedRequests** *(list) --*

      Information about the WorkSpaces that could not be started.

      - *(dict) --*

        Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
        RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
        started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

        - **WorkspaceId** *(string) --*

          The identifier of the WorkSpace.

        - **ErrorCode** *(string) --*

          The error code that is returned if the WorkSpace cannot be rebooted.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the WorkSpace cannot be rebooted.
    """


_ClientStartWorkspacesStartWorkspaceRequestsTypeDef = TypedDict(
    "_ClientStartWorkspacesStartWorkspaceRequestsTypeDef",
    {"WorkspaceId": str},
    total=False,
)


class ClientStartWorkspacesStartWorkspaceRequestsTypeDef(
    _ClientStartWorkspacesStartWorkspaceRequestsTypeDef
):
    """
    Type definition for `ClientStartWorkspaces` `StartWorkspaceRequests`

    Information used to start a WorkSpace.

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.
    """


_ClientStopWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientStopWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientStopWorkspacesResponseFailedRequestsTypeDef(
    _ClientStopWorkspacesResponseFailedRequestsTypeDef
):
    """
    Type definition for `ClientStopWorkspacesResponse` `FailedRequests`

    Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
    RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
    started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.

    - **ErrorCode** *(string) --*

      The error code that is returned if the WorkSpace cannot be rebooted.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the WorkSpace cannot be rebooted.
    """


_ClientStopWorkspacesResponseTypeDef = TypedDict(
    "_ClientStopWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientStopWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)


class ClientStopWorkspacesResponseTypeDef(_ClientStopWorkspacesResponseTypeDef):
    """
    Type definition for `ClientStopWorkspaces` `Response`

    - **FailedRequests** *(list) --*

      Information about the WorkSpaces that could not be stopped.

      - *(dict) --*

        Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
        RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
        started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

        - **WorkspaceId** *(string) --*

          The identifier of the WorkSpace.

        - **ErrorCode** *(string) --*

          The error code that is returned if the WorkSpace cannot be rebooted.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the WorkSpace cannot be rebooted.
    """


_ClientStopWorkspacesStopWorkspaceRequestsTypeDef = TypedDict(
    "_ClientStopWorkspacesStopWorkspaceRequestsTypeDef",
    {"WorkspaceId": str},
    total=False,
)


class ClientStopWorkspacesStopWorkspaceRequestsTypeDef(
    _ClientStopWorkspacesStopWorkspaceRequestsTypeDef
):
    """
    Type definition for `ClientStopWorkspaces` `StopWorkspaceRequests`

    Describes the information used to stop a WorkSpace.

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.
    """


_ClientTerminateWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "_ClientTerminateWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientTerminateWorkspacesResponseFailedRequestsTypeDef(
    _ClientTerminateWorkspacesResponseFailedRequestsTypeDef
):
    """
    Type definition for `ClientTerminateWorkspacesResponse` `FailedRequests`

    Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
    RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
    started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.

    - **ErrorCode** *(string) --*

      The error code that is returned if the WorkSpace cannot be rebooted.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the WorkSpace cannot be rebooted.
    """


_ClientTerminateWorkspacesResponseTypeDef = TypedDict(
    "_ClientTerminateWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientTerminateWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)


class ClientTerminateWorkspacesResponseTypeDef(
    _ClientTerminateWorkspacesResponseTypeDef
):
    """
    Type definition for `ClientTerminateWorkspaces` `Response`

    - **FailedRequests** *(list) --*

      Information about the WorkSpaces that could not be terminated.

      - *(dict) --*

        Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt (
        RebuildWorkspaces ), restored ( RestoreWorkspace ), terminated ( TerminateWorkspaces ),
        started ( StartWorkspaces ), or stopped ( StopWorkspaces ).

        - **WorkspaceId** *(string) --*

          The identifier of the WorkSpace.

        - **ErrorCode** *(string) --*

          The error code that is returned if the WorkSpace cannot be rebooted.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the WorkSpace cannot be rebooted.
    """


_ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef = TypedDict(
    "_ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef", {"WorkspaceId": str}
)


class ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef(
    _ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef
):
    """
    Type definition for `ClientTerminateWorkspaces` `TerminateWorkspaceRequests`

    Describes the information used to terminate a WorkSpace.

    - **WorkspaceId** *(string) --* **[REQUIRED]**

      The identifier of the WorkSpace.
    """


_ClientUpdateRulesOfIpGroupUserRulesTypeDef = TypedDict(
    "_ClientUpdateRulesOfIpGroupUserRulesTypeDef",
    {"ipRule": str, "ruleDesc": str},
    total=False,
)


class ClientUpdateRulesOfIpGroupUserRulesTypeDef(
    _ClientUpdateRulesOfIpGroupUserRulesTypeDef
):
    """
    Type definition for `ClientUpdateRulesOfIpGroup` `UserRules`

    Describes a rule for an IP access control group.

    - **ipRule** *(string) --*

      The IP address range, in CIDR notation.

    - **ruleDesc** *(string) --*

      The description.
    """


_DescribeAccountModificationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAccountModificationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeAccountModificationsPaginatePaginationConfigTypeDef(
    _DescribeAccountModificationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAccountModificationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef = TypedDict(
    "_DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef",
    {
        "ModificationState": str,
        "DedicatedTenancySupport": str,
        "DedicatedTenancyManagementCidrRange": str,
        "StartTime": datetime,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef(
    _DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef
):
    """
    Type definition for `DescribeAccountModificationsPaginateResponse` `AccountModifications`

    Describes a modification to the configuration of Bring Your Own License (BYOL) for the
    specified account.

    - **ModificationState** *(string) --*

      The state of the modification to the configuration of BYOL.

    - **DedicatedTenancySupport** *(string) --*

      The status of BYOL (whether BYOL is being enabled or disabled).

    - **DedicatedTenancyManagementCidrRange** *(string) --*

      The IP address range, specified as an IPv4 CIDR block, for the management network
      interface used for the account.

    - **StartTime** *(datetime) --*

      The timestamp when the modification of the BYOL configuration was started.

    - **ErrorCode** *(string) --*

      The error code that is returned if the configuration of BYOL cannot be modified.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the configuration of BYOL cannot be
      modified.
    """


_DescribeAccountModificationsPaginateResponseTypeDef = TypedDict(
    "_DescribeAccountModificationsPaginateResponseTypeDef",
    {
        "AccountModifications": List[
            DescribeAccountModificationsPaginateResponseAccountModificationsTypeDef
        ]
    },
    total=False,
)


class DescribeAccountModificationsPaginateResponseTypeDef(
    _DescribeAccountModificationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeAccountModificationsPaginate` `Response`

    - **AccountModifications** *(list) --*

      The list of modifications to the configuration of BYOL.

      - *(dict) --*

        Describes a modification to the configuration of Bring Your Own License (BYOL) for the
        specified account.

        - **ModificationState** *(string) --*

          The state of the modification to the configuration of BYOL.

        - **DedicatedTenancySupport** *(string) --*

          The status of BYOL (whether BYOL is being enabled or disabled).

        - **DedicatedTenancyManagementCidrRange** *(string) --*

          The IP address range, specified as an IPv4 CIDR block, for the management network
          interface used for the account.

        - **StartTime** *(datetime) --*

          The timestamp when the modification of the BYOL configuration was started.

        - **ErrorCode** *(string) --*

          The error code that is returned if the configuration of BYOL cannot be modified.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the configuration of BYOL cannot be
          modified.
    """


_DescribeIpGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeIpGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeIpGroupsPaginatePaginationConfigTypeDef(
    _DescribeIpGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeIpGroupsPaginate` `PaginationConfig`

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


_DescribeIpGroupsPaginateResponseResultuserRulesTypeDef = TypedDict(
    "_DescribeIpGroupsPaginateResponseResultuserRulesTypeDef",
    {"ipRule": str, "ruleDesc": str},
    total=False,
)


class DescribeIpGroupsPaginateResponseResultuserRulesTypeDef(
    _DescribeIpGroupsPaginateResponseResultuserRulesTypeDef
):
    """
    Type definition for `DescribeIpGroupsPaginateResponseResult` `userRules`

    Describes a rule for an IP access control group.

    - **ipRule** *(string) --*

      The IP address range, in CIDR notation.

    - **ruleDesc** *(string) --*

      The description.
    """


_DescribeIpGroupsPaginateResponseResultTypeDef = TypedDict(
    "_DescribeIpGroupsPaginateResponseResultTypeDef",
    {
        "groupId": str,
        "groupName": str,
        "groupDesc": str,
        "userRules": List[DescribeIpGroupsPaginateResponseResultuserRulesTypeDef],
    },
    total=False,
)


class DescribeIpGroupsPaginateResponseResultTypeDef(
    _DescribeIpGroupsPaginateResponseResultTypeDef
):
    """
    Type definition for `DescribeIpGroupsPaginateResponse` `Result`

    Describes an IP access control group.

    - **groupId** *(string) --*

      The identifier of the group.

    - **groupName** *(string) --*

      The name of the group.

    - **groupDesc** *(string) --*

      The description of the group.

    - **userRules** *(list) --*

      The rules.

      - *(dict) --*

        Describes a rule for an IP access control group.

        - **ipRule** *(string) --*

          The IP address range, in CIDR notation.

        - **ruleDesc** *(string) --*

          The description.
    """


_DescribeIpGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeIpGroupsPaginateResponseTypeDef",
    {"Result": List[DescribeIpGroupsPaginateResponseResultTypeDef]},
    total=False,
)


class DescribeIpGroupsPaginateResponseTypeDef(_DescribeIpGroupsPaginateResponseTypeDef):
    """
    Type definition for `DescribeIpGroupsPaginate` `Response`

    - **Result** *(list) --*

      Information about the IP access control groups.

      - *(dict) --*

        Describes an IP access control group.

        - **groupId** *(string) --*

          The identifier of the group.

        - **groupName** *(string) --*

          The name of the group.

        - **groupDesc** *(string) --*

          The description of the group.

        - **userRules** *(list) --*

          The rules.

          - *(dict) --*

            Describes a rule for an IP access control group.

            - **ipRule** *(string) --*

              The IP address range, in CIDR notation.

            - **ruleDesc** *(string) --*

              The description.
    """


_DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef(
    _DescribeWorkspaceBundlesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeWorkspaceBundlesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef",
    {"Name": str},
    total=False,
)


class DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef(
    _DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef
):
    """
    Type definition for `DescribeWorkspaceBundlesPaginateResponseBundles` `ComputeType`

    The compute type. For more information, see `Amazon WorkSpaces Bundles
    <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

    - **Name** *(string) --*

      The compute type.
    """


_DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef",
    {"Capacity": str},
    total=False,
)


class DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef(
    _DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef
):
    """
    Type definition for `DescribeWorkspaceBundlesPaginateResponseBundles` `RootStorage`

    The size of the root volume.

    - **Capacity** *(string) --*

      The size of the root volume.
    """


_DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef",
    {"Capacity": str},
    total=False,
)


class DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef(
    _DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef
):
    """
    Type definition for `DescribeWorkspaceBundlesPaginateResponseBundles` `UserStorage`

    The size of the user storage.

    - **Capacity** *(string) --*

      The size of the user storage.
    """


_DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef",
    {
        "BundleId": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "RootStorage": DescribeWorkspaceBundlesPaginateResponseBundlesRootStorageTypeDef,
        "UserStorage": DescribeWorkspaceBundlesPaginateResponseBundlesUserStorageTypeDef,
        "ComputeType": DescribeWorkspaceBundlesPaginateResponseBundlesComputeTypeTypeDef,
    },
    total=False,
)


class DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef(
    _DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef
):
    """
    Type definition for `DescribeWorkspaceBundlesPaginateResponse` `Bundles`

    Describes a WorkSpace bundle.

    - **BundleId** *(string) --*

      The bundle identifier.

    - **Name** *(string) --*

      The name of the bundle.

    - **Owner** *(string) --*

      The owner of the bundle. This is the account identifier of the owner, or ``AMAZON`` if
      the bundle is provided by AWS.

    - **Description** *(string) --*

      A description.

    - **RootStorage** *(dict) --*

      The size of the root volume.

      - **Capacity** *(string) --*

        The size of the root volume.

    - **UserStorage** *(dict) --*

      The size of the user storage.

      - **Capacity** *(string) --*

        The size of the user storage.

    - **ComputeType** *(dict) --*

      The compute type. For more information, see `Amazon WorkSpaces Bundles
      <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

      - **Name** *(string) --*

        The compute type.
    """


_DescribeWorkspaceBundlesPaginateResponseTypeDef = TypedDict(
    "_DescribeWorkspaceBundlesPaginateResponseTypeDef",
    {"Bundles": List[DescribeWorkspaceBundlesPaginateResponseBundlesTypeDef]},
    total=False,
)


class DescribeWorkspaceBundlesPaginateResponseTypeDef(
    _DescribeWorkspaceBundlesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeWorkspaceBundlesPaginate` `Response`

    - **Bundles** *(list) --*

      Information about the bundles.

      - *(dict) --*

        Describes a WorkSpace bundle.

        - **BundleId** *(string) --*

          The bundle identifier.

        - **Name** *(string) --*

          The name of the bundle.

        - **Owner** *(string) --*

          The owner of the bundle. This is the account identifier of the owner, or ``AMAZON`` if
          the bundle is provided by AWS.

        - **Description** *(string) --*

          A description.

        - **RootStorage** *(dict) --*

          The size of the root volume.

          - **Capacity** *(string) --*

            The size of the root volume.

        - **UserStorage** *(dict) --*

          The size of the user storage.

          - **Capacity** *(string) --*

            The size of the user storage.

        - **ComputeType** *(dict) --*

          The compute type. For more information, see `Amazon WorkSpaces Bundles
          <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

          - **Name** *(string) --*

            The compute type.
    """


_DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef(
    _DescribeWorkspaceDirectoriesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeWorkspaceDirectoriesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": str,
        "IncreaseVolumeSize": str,
        "ChangeComputeType": str,
        "SwitchRunningMode": str,
        "RebuildWorkspace": str,
    },
    total=False,
)


class DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef(
    _DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef
):
    """
    Type definition for `DescribeWorkspaceDirectoriesPaginateResponseDirectories` `SelfservicePermissions`

    The default self-service permissions for WorkSpaces in the directory.

    - **RestartWorkspace** *(string) --*

      Specifies whether users can restart their WorkSpace.

    - **IncreaseVolumeSize** *(string) --*

      Specifies whether users can increase the volume size of the drives on their WorkSpace.

    - **ChangeComputeType** *(string) --*

      Specifies whether users can change the compute type (bundle) for their WorkSpace.

    - **SwitchRunningMode** *(string) --*

      Specifies whether users can switch the running mode of their WorkSpace.

    - **RebuildWorkspace** *(string) --*

      Specifies whether users can rebuild the operating system of a WorkSpace to its original
      state.
    """


_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": str,
        "DeviceTypeOsx": str,
        "DeviceTypeWeb": str,
        "DeviceTypeIos": str,
        "DeviceTypeAndroid": str,
        "DeviceTypeChromeOs": str,
        "DeviceTypeZeroClient": str,
    },
    total=False,
)


class DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef(
    _DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef
):
    """
    Type definition for `DescribeWorkspaceDirectoriesPaginateResponseDirectories` `WorkspaceAccessProperties`

    The devices and operating systems that users can use to access Workspaces.

    - **DeviceTypeWindows** *(string) --*

      Indicates whether users can use Windows clients to access their WorkSpaces. To restrict
      WorkSpaces access to trusted devices (also known as managed devices) with valid
      certificates, specify a value of ``TRUST`` . For more information, see `Restrict
      WorkSpaces Access to Trusted Devices
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

    - **DeviceTypeOsx** *(string) --*

      Indicates whether users can use macOS clients to access their WorkSpaces. To restrict
      WorkSpaces access to trusted devices (also known as managed devices) with valid
      certificates, specify a value of ``TRUST`` . For more information, see `Restrict
      WorkSpaces Access to Trusted Devices
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

    - **DeviceTypeWeb** *(string) --*

      Indicates whether users can access their WorkSpaces through a web browser.

    - **DeviceTypeIos** *(string) --*

      Indicates whether users can use iOS devices to access their WorkSpaces.

    - **DeviceTypeAndroid** *(string) --*

      Indicates whether users can use Android devices to access their WorkSpaces.

    - **DeviceTypeChromeOs** *(string) --*

      Indicates whether users can use Chromebooks to access their WorkSpaces.

    - **DeviceTypeZeroClient** *(string) --*

      Indicates whether users can use zero client devices to access their WorkSpaces.
    """


_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)


class DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef(
    _DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef
):
    """
    Type definition for `DescribeWorkspaceDirectoriesPaginateResponseDirectories` `WorkspaceCreationProperties`

    The default creation properties for all WorkSpaces in the directory.

    - **EnableWorkDocs** *(boolean) --*

      Specifies whether the directory is enabled for Amazon WorkDocs.

    - **EnableInternetAccess** *(boolean) --*

      Specifies whether to automatically assign a public IP address to WorkSpaces in this
      directory by default. If enabled, the public IP address allows outbound internet access
      from your WorkSpaces when you’re using an internet gateway in the Amazon VPC in which
      your WorkSpaces are located. If you're using a Network Address Translation (NAT)
      gateway for outbound internet access from your VPC, or if your WorkSpaces are in public
      subnets and you manually assign them Elastic IP addresses, you should disable this
      setting. This setting applies to new WorkSpaces that you launch or to existing
      WorkSpaces that you rebuild. For more information, see `Configure a VPC for Amazon
      WorkSpaces
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html>`__
      .

    - **DefaultOu** *(string) --*

      The organizational unit (OU) in the directory for the WorkSpace machine accounts.

    - **CustomSecurityGroupId** *(string) --*

      The identifier of any security groups to apply to WorkSpaces when they are created.

    - **UserEnabledAsLocalAdministrator** *(boolean) --*

      Specifies whether WorkSpace users are local administrators on their WorkSpaces.

    - **EnableMaintenanceMode** *(boolean) --*

      Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see
      `WorkSpace Maintenance
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html>`__
      .
    """


_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "DirectoryName": str,
        "RegistrationCode": str,
        "SubnetIds": List[str],
        "DnsIpAddresses": List[str],
        "CustomerUserName": str,
        "IamRoleId": str,
        "DirectoryType": str,
        "WorkspaceSecurityGroupId": str,
        "State": str,
        "WorkspaceCreationProperties": DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceCreationPropertiesTypeDef,
        "ipGroupIds": List[str],
        "WorkspaceAccessProperties": DescribeWorkspaceDirectoriesPaginateResponseDirectoriesWorkspaceAccessPropertiesTypeDef,
        "Tenancy": str,
        "SelfservicePermissions": DescribeWorkspaceDirectoriesPaginateResponseDirectoriesSelfservicePermissionsTypeDef,
    },
    total=False,
)


class DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef(
    _DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef
):
    """
    Type definition for `DescribeWorkspaceDirectoriesPaginateResponse` `Directories`

    Describes a directory that is used with Amazon WorkSpaces.

    - **DirectoryId** *(string) --*

      The directory identifier.

    - **Alias** *(string) --*

      The directory alias.

    - **DirectoryName** *(string) --*

      The name of the directory.

    - **RegistrationCode** *(string) --*

      The registration code for the directory. This is the code that users enter in their
      Amazon WorkSpaces client application to connect to the directory.

    - **SubnetIds** *(list) --*

      The identifiers of the subnets used with the directory.

      - *(string) --*

    - **DnsIpAddresses** *(list) --*

      The IP addresses of the DNS servers for the directory.

      - *(string) --*

    - **CustomerUserName** *(string) --*

      The user name for the service account.

    - **IamRoleId** *(string) --*

      The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make
      calls to other services, such as Amazon EC2, on your behalf.

    - **DirectoryType** *(string) --*

      The directory type.

    - **WorkspaceSecurityGroupId** *(string) --*

      The identifier of the security group that is assigned to new WorkSpaces.

    - **State** *(string) --*

      The state of the directory's registration with Amazon WorkSpaces.

    - **WorkspaceCreationProperties** *(dict) --*

      The default creation properties for all WorkSpaces in the directory.

      - **EnableWorkDocs** *(boolean) --*

        Specifies whether the directory is enabled for Amazon WorkDocs.

      - **EnableInternetAccess** *(boolean) --*

        Specifies whether to automatically assign a public IP address to WorkSpaces in this
        directory by default. If enabled, the public IP address allows outbound internet access
        from your WorkSpaces when you’re using an internet gateway in the Amazon VPC in which
        your WorkSpaces are located. If you're using a Network Address Translation (NAT)
        gateway for outbound internet access from your VPC, or if your WorkSpaces are in public
        subnets and you manually assign them Elastic IP addresses, you should disable this
        setting. This setting applies to new WorkSpaces that you launch or to existing
        WorkSpaces that you rebuild. For more information, see `Configure a VPC for Amazon
        WorkSpaces
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html>`__
        .

      - **DefaultOu** *(string) --*

        The organizational unit (OU) in the directory for the WorkSpace machine accounts.

      - **CustomSecurityGroupId** *(string) --*

        The identifier of any security groups to apply to WorkSpaces when they are created.

      - **UserEnabledAsLocalAdministrator** *(boolean) --*

        Specifies whether WorkSpace users are local administrators on their WorkSpaces.

      - **EnableMaintenanceMode** *(boolean) --*

        Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see
        `WorkSpace Maintenance
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html>`__
        .

    - **ipGroupIds** *(list) --*

      The identifiers of the IP access control groups associated with the directory.

      - *(string) --*

    - **WorkspaceAccessProperties** *(dict) --*

      The devices and operating systems that users can use to access Workspaces.

      - **DeviceTypeWindows** *(string) --*

        Indicates whether users can use Windows clients to access their WorkSpaces. To restrict
        WorkSpaces access to trusted devices (also known as managed devices) with valid
        certificates, specify a value of ``TRUST`` . For more information, see `Restrict
        WorkSpaces Access to Trusted Devices
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

      - **DeviceTypeOsx** *(string) --*

        Indicates whether users can use macOS clients to access their WorkSpaces. To restrict
        WorkSpaces access to trusted devices (also known as managed devices) with valid
        certificates, specify a value of ``TRUST`` . For more information, see `Restrict
        WorkSpaces Access to Trusted Devices
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

      - **DeviceTypeWeb** *(string) --*

        Indicates whether users can access their WorkSpaces through a web browser.

      - **DeviceTypeIos** *(string) --*

        Indicates whether users can use iOS devices to access their WorkSpaces.

      - **DeviceTypeAndroid** *(string) --*

        Indicates whether users can use Android devices to access their WorkSpaces.

      - **DeviceTypeChromeOs** *(string) --*

        Indicates whether users can use Chromebooks to access their WorkSpaces.

      - **DeviceTypeZeroClient** *(string) --*

        Indicates whether users can use zero client devices to access their WorkSpaces.

    - **Tenancy** *(string) --*

      Specifies whether the directory is dedicated or shared. To use Bring Your Own License
      (BYOL), this value must be set to ``DEDICATED`` . For more information, see `Bring Your
      Own Windows Desktop Images
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html>`__ .

    - **SelfservicePermissions** *(dict) --*

      The default self-service permissions for WorkSpaces in the directory.

      - **RestartWorkspace** *(string) --*

        Specifies whether users can restart their WorkSpace.

      - **IncreaseVolumeSize** *(string) --*

        Specifies whether users can increase the volume size of the drives on their WorkSpace.

      - **ChangeComputeType** *(string) --*

        Specifies whether users can change the compute type (bundle) for their WorkSpace.

      - **SwitchRunningMode** *(string) --*

        Specifies whether users can switch the running mode of their WorkSpace.

      - **RebuildWorkspace** *(string) --*

        Specifies whether users can rebuild the operating system of a WorkSpace to its original
        state.
    """


_DescribeWorkspaceDirectoriesPaginateResponseTypeDef = TypedDict(
    "_DescribeWorkspaceDirectoriesPaginateResponseTypeDef",
    {
        "Directories": List[
            DescribeWorkspaceDirectoriesPaginateResponseDirectoriesTypeDef
        ]
    },
    total=False,
)


class DescribeWorkspaceDirectoriesPaginateResponseTypeDef(
    _DescribeWorkspaceDirectoriesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeWorkspaceDirectoriesPaginate` `Response`

    - **Directories** *(list) --*

      Information about the directories.

      - *(dict) --*

        Describes a directory that is used with Amazon WorkSpaces.

        - **DirectoryId** *(string) --*

          The directory identifier.

        - **Alias** *(string) --*

          The directory alias.

        - **DirectoryName** *(string) --*

          The name of the directory.

        - **RegistrationCode** *(string) --*

          The registration code for the directory. This is the code that users enter in their
          Amazon WorkSpaces client application to connect to the directory.

        - **SubnetIds** *(list) --*

          The identifiers of the subnets used with the directory.

          - *(string) --*

        - **DnsIpAddresses** *(list) --*

          The IP addresses of the DNS servers for the directory.

          - *(string) --*

        - **CustomerUserName** *(string) --*

          The user name for the service account.

        - **IamRoleId** *(string) --*

          The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make
          calls to other services, such as Amazon EC2, on your behalf.

        - **DirectoryType** *(string) --*

          The directory type.

        - **WorkspaceSecurityGroupId** *(string) --*

          The identifier of the security group that is assigned to new WorkSpaces.

        - **State** *(string) --*

          The state of the directory's registration with Amazon WorkSpaces.

        - **WorkspaceCreationProperties** *(dict) --*

          The default creation properties for all WorkSpaces in the directory.

          - **EnableWorkDocs** *(boolean) --*

            Specifies whether the directory is enabled for Amazon WorkDocs.

          - **EnableInternetAccess** *(boolean) --*

            Specifies whether to automatically assign a public IP address to WorkSpaces in this
            directory by default. If enabled, the public IP address allows outbound internet access
            from your WorkSpaces when you’re using an internet gateway in the Amazon VPC in which
            your WorkSpaces are located. If you're using a Network Address Translation (NAT)
            gateway for outbound internet access from your VPC, or if your WorkSpaces are in public
            subnets and you manually assign them Elastic IP addresses, you should disable this
            setting. This setting applies to new WorkSpaces that you launch or to existing
            WorkSpaces that you rebuild. For more information, see `Configure a VPC for Amazon
            WorkSpaces
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html>`__
            .

          - **DefaultOu** *(string) --*

            The organizational unit (OU) in the directory for the WorkSpace machine accounts.

          - **CustomSecurityGroupId** *(string) --*

            The identifier of any security groups to apply to WorkSpaces when they are created.

          - **UserEnabledAsLocalAdministrator** *(boolean) --*

            Specifies whether WorkSpace users are local administrators on their WorkSpaces.

          - **EnableMaintenanceMode** *(boolean) --*

            Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see
            `WorkSpace Maintenance
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html>`__
            .

        - **ipGroupIds** *(list) --*

          The identifiers of the IP access control groups associated with the directory.

          - *(string) --*

        - **WorkspaceAccessProperties** *(dict) --*

          The devices and operating systems that users can use to access Workspaces.

          - **DeviceTypeWindows** *(string) --*

            Indicates whether users can use Windows clients to access their WorkSpaces. To restrict
            WorkSpaces access to trusted devices (also known as managed devices) with valid
            certificates, specify a value of ``TRUST`` . For more information, see `Restrict
            WorkSpaces Access to Trusted Devices
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

          - **DeviceTypeOsx** *(string) --*

            Indicates whether users can use macOS clients to access their WorkSpaces. To restrict
            WorkSpaces access to trusted devices (also known as managed devices) with valid
            certificates, specify a value of ``TRUST`` . For more information, see `Restrict
            WorkSpaces Access to Trusted Devices
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html>`__ .

          - **DeviceTypeWeb** *(string) --*

            Indicates whether users can access their WorkSpaces through a web browser.

          - **DeviceTypeIos** *(string) --*

            Indicates whether users can use iOS devices to access their WorkSpaces.

          - **DeviceTypeAndroid** *(string) --*

            Indicates whether users can use Android devices to access their WorkSpaces.

          - **DeviceTypeChromeOs** *(string) --*

            Indicates whether users can use Chromebooks to access their WorkSpaces.

          - **DeviceTypeZeroClient** *(string) --*

            Indicates whether users can use zero client devices to access their WorkSpaces.

        - **Tenancy** *(string) --*

          Specifies whether the directory is dedicated or shared. To use Bring Your Own License
          (BYOL), this value must be set to ``DEDICATED`` . For more information, see `Bring Your
          Own Windows Desktop Images
          <https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html>`__ .

        - **SelfservicePermissions** *(dict) --*

          The default self-service permissions for WorkSpaces in the directory.

          - **RestartWorkspace** *(string) --*

            Specifies whether users can restart their WorkSpace.

          - **IncreaseVolumeSize** *(string) --*

            Specifies whether users can increase the volume size of the drives on their WorkSpace.

          - **ChangeComputeType** *(string) --*

            Specifies whether users can change the compute type (bundle) for their WorkSpace.

          - **SwitchRunningMode** *(string) --*

            Specifies whether users can switch the running mode of their WorkSpace.

          - **RebuildWorkspace** *(string) --*

            Specifies whether users can rebuild the operating system of a WorkSpace to its original
            state.
    """


_DescribeWorkspaceImagesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeWorkspaceImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeWorkspaceImagesPaginatePaginationConfigTypeDef(
    _DescribeWorkspaceImagesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeWorkspaceImagesPaginate` `PaginationConfig`

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


_DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef = TypedDict(
    "_DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef",
    {"Type": str},
    total=False,
)


class DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef(
    _DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef
):
    """
    Type definition for `DescribeWorkspaceImagesPaginateResponseImages` `OperatingSystem`

    The operating system that the image is running.

    - **Type** *(string) --*

      The operating system.
    """


_DescribeWorkspaceImagesPaginateResponseImagesTypeDef = TypedDict(
    "_DescribeWorkspaceImagesPaginateResponseImagesTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": DescribeWorkspaceImagesPaginateResponseImagesOperatingSystemTypeDef,
        "State": str,
        "RequiredTenancy": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class DescribeWorkspaceImagesPaginateResponseImagesTypeDef(
    _DescribeWorkspaceImagesPaginateResponseImagesTypeDef
):
    """
    Type definition for `DescribeWorkspaceImagesPaginateResponse` `Images`

    Describes a WorkSpace image.

    - **ImageId** *(string) --*

      The identifier of the image.

    - **Name** *(string) --*

      The name of the image.

    - **Description** *(string) --*

      The description of the image.

    - **OperatingSystem** *(dict) --*

      The operating system that the image is running.

      - **Type** *(string) --*

        The operating system.

    - **State** *(string) --*

      The status of the image.

    - **RequiredTenancy** *(string) --*

      Specifies whether the image is running on dedicated hardware. When Bring Your Own License
      (BYOL) is enabled, this value is set to ``DEDICATED`` . For more information, see `Bring
      Your Own Windows Desktop Images
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html>`__ .

    - **ErrorCode** *(string) --*

      The error code that is returned for the image.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned for the image.
    """


_DescribeWorkspaceImagesPaginateResponseTypeDef = TypedDict(
    "_DescribeWorkspaceImagesPaginateResponseTypeDef",
    {"Images": List[DescribeWorkspaceImagesPaginateResponseImagesTypeDef]},
    total=False,
)


class DescribeWorkspaceImagesPaginateResponseTypeDef(
    _DescribeWorkspaceImagesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeWorkspaceImagesPaginate` `Response`

    - **Images** *(list) --*

      Information about the images.

      - *(dict) --*

        Describes a WorkSpace image.

        - **ImageId** *(string) --*

          The identifier of the image.

        - **Name** *(string) --*

          The name of the image.

        - **Description** *(string) --*

          The description of the image.

        - **OperatingSystem** *(dict) --*

          The operating system that the image is running.

          - **Type** *(string) --*

            The operating system.

        - **State** *(string) --*

          The status of the image.

        - **RequiredTenancy** *(string) --*

          Specifies whether the image is running on dedicated hardware. When Bring Your Own License
          (BYOL) is enabled, this value is set to ``DEDICATED`` . For more information, see `Bring
          Your Own Windows Desktop Images
          <https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html>`__ .

        - **ErrorCode** *(string) --*

          The error code that is returned for the image.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned for the image.
    """


_DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef(
    _DescribeWorkspacesConnectionStatusPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeWorkspacesConnectionStatusPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef = TypedDict(
    "_DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef",
    {
        "WorkspaceId": str,
        "ConnectionState": str,
        "ConnectionStateCheckTimestamp": datetime,
        "LastKnownUserConnectionTimestamp": datetime,
    },
    total=False,
)


class DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef(
    _DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef
):
    """
    Type definition for `DescribeWorkspacesConnectionStatusPaginateResponse` `WorkspacesConnectionStatus`

    Describes the connection status of a WorkSpace.

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.

    - **ConnectionState** *(string) --*

      The connection state of the WorkSpace. The connection state is unknown if the WorkSpace
      is stopped.

    - **ConnectionStateCheckTimestamp** *(datetime) --*

      The timestamp of the connection status check.

    - **LastKnownUserConnectionTimestamp** *(datetime) --*

      The timestamp of the last known user connection.
    """


_DescribeWorkspacesConnectionStatusPaginateResponseTypeDef = TypedDict(
    "_DescribeWorkspacesConnectionStatusPaginateResponseTypeDef",
    {
        "WorkspacesConnectionStatus": List[
            DescribeWorkspacesConnectionStatusPaginateResponseWorkspacesConnectionStatusTypeDef
        ]
    },
    total=False,
)


class DescribeWorkspacesConnectionStatusPaginateResponseTypeDef(
    _DescribeWorkspacesConnectionStatusPaginateResponseTypeDef
):
    """
    Type definition for `DescribeWorkspacesConnectionStatusPaginate` `Response`

    - **WorkspacesConnectionStatus** *(list) --*

      Information about the connection status of the WorkSpace.

      - *(dict) --*

        Describes the connection status of a WorkSpace.

        - **WorkspaceId** *(string) --*

          The identifier of the WorkSpace.

        - **ConnectionState** *(string) --*

          The connection state of the WorkSpace. The connection state is unknown if the WorkSpace
          is stopped.

        - **ConnectionStateCheckTimestamp** *(datetime) --*

          The timestamp of the connection status check.

        - **LastKnownUserConnectionTimestamp** *(datetime) --*

          The timestamp of the last known user connection.
    """


_DescribeWorkspacesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeWorkspacesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeWorkspacesPaginatePaginationConfigTypeDef(
    _DescribeWorkspacesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeWorkspacesPaginate` `PaginationConfig`

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


_DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef = TypedDict(
    "_DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef",
    {"Resource": str, "State": str},
    total=False,
)


class DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef(
    _DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef
):
    """
    Type definition for `DescribeWorkspacesPaginateResponseWorkspaces` `ModificationStates`

    Describes a WorkSpace modification.

    - **Resource** *(string) --*

      The resource.

    - **State** *(string) --*

      The modification state.
    """


_DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef = TypedDict(
    "_DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef",
    {
        "RunningMode": str,
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": str,
    },
    total=False,
)


class DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef(
    _DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef
):
    """
    Type definition for `DescribeWorkspacesPaginateResponseWorkspaces` `WorkspaceProperties`

    The properties of the WorkSpace.

    - **RunningMode** *(string) --*

      The running mode. For more information, see `Manage the WorkSpace Running Mode
      <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

    - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

      The time after a user logs off when WorkSpaces are automatically stopped. Configured in
      60-minute intervals.

    - **RootVolumeSizeGib** *(integer) --*

      The size of the root volume.

    - **UserVolumeSizeGib** *(integer) --*

      The size of the user storage.

    - **ComputeTypeName** *(string) --*

      The compute type. For more information, see `Amazon WorkSpaces Bundles
      <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
    """


_DescribeWorkspacesPaginateResponseWorkspacesTypeDef = TypedDict(
    "_DescribeWorkspacesPaginateResponseWorkspacesTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": str,
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": DescribeWorkspacesPaginateResponseWorkspacesWorkspacePropertiesTypeDef,
        "ModificationStates": List[
            DescribeWorkspacesPaginateResponseWorkspacesModificationStatesTypeDef
        ],
    },
    total=False,
)


class DescribeWorkspacesPaginateResponseWorkspacesTypeDef(
    _DescribeWorkspacesPaginateResponseWorkspacesTypeDef
):
    """
    Type definition for `DescribeWorkspacesPaginateResponse` `Workspaces`

    Describes a WorkSpace.

    - **WorkspaceId** *(string) --*

      The identifier of the WorkSpace.

    - **DirectoryId** *(string) --*

      The identifier of the AWS Directory Service directory for the WorkSpace.

    - **UserName** *(string) --*

      The user for the WorkSpace.

    - **IpAddress** *(string) --*

      The IP address of the WorkSpace.

    - **State** *(string) --*

      The operational state of the WorkSpace.

    - **BundleId** *(string) --*

      The identifier of the bundle used to create the WorkSpace.

    - **SubnetId** *(string) --*

      The identifier of the subnet for the WorkSpace.

    - **ErrorMessage** *(string) --*

      The text of the error message that is returned if the WorkSpace cannot be created.

    - **ErrorCode** *(string) --*

      The error code that is returned if the WorkSpace cannot be created.

    - **ComputerName** *(string) --*

      The name of the WorkSpace, as seen by the operating system.

    - **VolumeEncryptionKey** *(string) --*

      The KMS key used to encrypt data stored on your WorkSpace.

    - **UserVolumeEncryptionEnabled** *(boolean) --*

      Indicates whether the data stored on the user volume is encrypted.

    - **RootVolumeEncryptionEnabled** *(boolean) --*

      Indicates whether the data stored on the root volume is encrypted.

    - **WorkspaceProperties** *(dict) --*

      The properties of the WorkSpace.

      - **RunningMode** *(string) --*

        The running mode. For more information, see `Manage the WorkSpace Running Mode
        <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

      - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

        The time after a user logs off when WorkSpaces are automatically stopped. Configured in
        60-minute intervals.

      - **RootVolumeSizeGib** *(integer) --*

        The size of the root volume.

      - **UserVolumeSizeGib** *(integer) --*

        The size of the user storage.

      - **ComputeTypeName** *(string) --*

        The compute type. For more information, see `Amazon WorkSpaces Bundles
        <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

    - **ModificationStates** *(list) --*

      The modification states of the WorkSpace.

      - *(dict) --*

        Describes a WorkSpace modification.

        - **Resource** *(string) --*

          The resource.

        - **State** *(string) --*

          The modification state.
    """


_DescribeWorkspacesPaginateResponseTypeDef = TypedDict(
    "_DescribeWorkspacesPaginateResponseTypeDef",
    {"Workspaces": List[DescribeWorkspacesPaginateResponseWorkspacesTypeDef]},
    total=False,
)


class DescribeWorkspacesPaginateResponseTypeDef(
    _DescribeWorkspacesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeWorkspacesPaginate` `Response`

    - **Workspaces** *(list) --*

      Information about the WorkSpaces.

      Because  CreateWorkspaces is an asynchronous operation, some of the returned information
      could be incomplete.

      - *(dict) --*

        Describes a WorkSpace.

        - **WorkspaceId** *(string) --*

          The identifier of the WorkSpace.

        - **DirectoryId** *(string) --*

          The identifier of the AWS Directory Service directory for the WorkSpace.

        - **UserName** *(string) --*

          The user for the WorkSpace.

        - **IpAddress** *(string) --*

          The IP address of the WorkSpace.

        - **State** *(string) --*

          The operational state of the WorkSpace.

        - **BundleId** *(string) --*

          The identifier of the bundle used to create the WorkSpace.

        - **SubnetId** *(string) --*

          The identifier of the subnet for the WorkSpace.

        - **ErrorMessage** *(string) --*

          The text of the error message that is returned if the WorkSpace cannot be created.

        - **ErrorCode** *(string) --*

          The error code that is returned if the WorkSpace cannot be created.

        - **ComputerName** *(string) --*

          The name of the WorkSpace, as seen by the operating system.

        - **VolumeEncryptionKey** *(string) --*

          The KMS key used to encrypt data stored on your WorkSpace.

        - **UserVolumeEncryptionEnabled** *(boolean) --*

          Indicates whether the data stored on the user volume is encrypted.

        - **RootVolumeEncryptionEnabled** *(boolean) --*

          Indicates whether the data stored on the root volume is encrypted.

        - **WorkspaceProperties** *(dict) --*

          The properties of the WorkSpace.

          - **RunningMode** *(string) --*

            The running mode. For more information, see `Manage the WorkSpace Running Mode
            <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .

          - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*

            The time after a user logs off when WorkSpaces are automatically stopped. Configured in
            60-minute intervals.

          - **RootVolumeSizeGib** *(integer) --*

            The size of the root volume.

          - **UserVolumeSizeGib** *(integer) --*

            The size of the user storage.

          - **ComputeTypeName** *(string) --*

            The compute type. For more information, see `Amazon WorkSpaces Bundles
            <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .

        - **ModificationStates** *(list) --*

          The modification states of the WorkSpace.

          - *(dict) --*

            Describes a WorkSpace modification.

            - **Resource** *(string) --*

              The resource.

            - **State** *(string) --*

              The modification state.
    """


_ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef(
    _ListAvailableManagementCidrRangesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAvailableManagementCidrRangesPaginate` `PaginationConfig`

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


_ListAvailableManagementCidrRangesPaginateResponseTypeDef = TypedDict(
    "_ListAvailableManagementCidrRangesPaginateResponseTypeDef",
    {"ManagementCidrRanges": List[str]},
    total=False,
)


class ListAvailableManagementCidrRangesPaginateResponseTypeDef(
    _ListAvailableManagementCidrRangesPaginateResponseTypeDef
):
    """
    Type definition for `ListAvailableManagementCidrRangesPaginate` `Response`

    - **ManagementCidrRanges** *(list) --*

      The list of available IP address ranges, specified as IPv4 CIDR blocks.

      - *(string) --*
    """
