"Main interface for docdb type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    "ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCopyDbClusterParameterGroupResponseTypeDef",
    "ClientCopyDbClusterParameterGroupTagsTypeDef",
    "ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCopyDbClusterSnapshotResponseTypeDef",
    "ClientCopyDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    "ClientCreateDbClusterParameterGroupResponseTypeDef",
    "ClientCreateDbClusterParameterGroupTagsTypeDef",
    "ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientCreateDbClusterResponseDBClusterTypeDef",
    "ClientCreateDbClusterResponseTypeDef",
    "ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientCreateDbClusterSnapshotResponseTypeDef",
    "ClientCreateDbClusterSnapshotTagsTypeDef",
    "ClientCreateDbClusterTagsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateDbInstanceResponseDBInstanceTypeDef",
    "ClientCreateDbInstanceResponseTypeDef",
    "ClientCreateDbInstanceTagsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientCreateDbSubnetGroupResponseTypeDef",
    "ClientCreateDbSubnetGroupTagsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientDeleteDbClusterResponseDBClusterTypeDef",
    "ClientDeleteDbClusterResponseTypeDef",
    "ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    "ClientDeleteDbClusterSnapshotResponseTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    "ClientDeleteDbInstanceResponseTypeDef",
    "ClientDescribeCertificatesFiltersTypeDef",
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    "ClientDescribeCertificatesResponseTypeDef",
    "ClientDescribeDbClusterParameterGroupsFiltersTypeDef",
    "ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef",
    "ClientDescribeDbClusterParameterGroupsResponseTypeDef",
    "ClientDescribeDbClusterParametersFiltersTypeDef",
    "ClientDescribeDbClusterParametersResponseParametersTypeDef",
    "ClientDescribeDbClusterParametersResponseTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientDescribeDbClusterSnapshotAttributesResponseTypeDef",
    "ClientDescribeDbClusterSnapshotsFiltersTypeDef",
    "ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef",
    "ClientDescribeDbClusterSnapshotsResponseTypeDef",
    "ClientDescribeDbClustersFiltersTypeDef",
    "ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef",
    "ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef",
    "ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef",
    "ClientDescribeDbClustersResponseDBClustersTypeDef",
    "ClientDescribeDbClustersResponseTypeDef",
    "ClientDescribeDbEngineVersionsFiltersTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    "ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef",
    "ClientDescribeDbEngineVersionsResponseTypeDef",
    "ClientDescribeDbInstancesFiltersTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    "ClientDescribeDbInstancesResponseTypeDef",
    "ClientDescribeDbSubnetGroupsFiltersTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef",
    "ClientDescribeDbSubnetGroupsResponseTypeDef",
    "ClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef",
    "ClientDescribeEngineDefaultClusterParametersResponseTypeDef",
    "ClientDescribeEventCategoriesFiltersTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventsFiltersTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef",
    "ClientDescribeOrderableDbInstanceOptionsResponseTypeDef",
    "ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    "ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientFailoverDbClusterResponseDBClusterTypeDef",
    "ClientFailoverDbClusterResponseTypeDef",
    "ClientListTagsForResourceFiltersTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    "ClientModifyDbClusterParameterGroupParametersTypeDef",
    "ClientModifyDbClusterParameterGroupResponseTypeDef",
    "ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientModifyDbClusterResponseDBClusterTypeDef",
    "ClientModifyDbClusterResponseTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    "ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyDbInstanceResponseDBInstanceTypeDef",
    "ClientModifyDbInstanceResponseTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    "ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    "ClientModifyDbSubnetGroupResponseTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootDbInstanceResponseDBInstanceTypeDef",
    "ClientRebootDbInstanceResponseTypeDef",
    "ClientResetDbClusterParameterGroupParametersTypeDef",
    "ClientResetDbClusterParameterGroupResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    "ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    "ClientRestoreDbClusterFromSnapshotTagsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    "ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    "ClientRestoreDbClusterToPointInTimeTagsTypeDef",
    "ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientStartDbClusterResponseDBClusterTypeDef",
    "ClientStartDbClusterResponseTypeDef",
    "ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef",
    "ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef",
    "ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    "ClientStopDbClusterResponseDBClusterTypeDef",
    "ClientStopDbClusterResponseTypeDef",
    "DbInstanceAvailableWaitFiltersTypeDef",
    "DbInstanceAvailableWaitWaiterConfigTypeDef",
    "DbInstanceDeletedWaitFiltersTypeDef",
    "DbInstanceDeletedWaitWaiterConfigTypeDef",
    "DescribeDBClustersPaginateFiltersTypeDef",
    "DescribeDBClustersPaginatePaginationConfigTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef",
    "DescribeDBClustersPaginateResponseDBClustersTypeDef",
    "DescribeDBClustersPaginateResponseTypeDef",
    "DescribeDBEngineVersionsPaginateFiltersTypeDef",
    "DescribeDBEngineVersionsPaginatePaginationConfigTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    "DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef",
    "DescribeDBEngineVersionsPaginateResponseTypeDef",
    "DescribeDBInstancesPaginateFiltersTypeDef",
    "DescribeDBInstancesPaginatePaginationConfigTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef",
    "DescribeDBInstancesPaginateResponseDBInstancesTypeDef",
    "DescribeDBInstancesPaginateResponseTypeDef",
    "DescribeDBSubnetGroupsPaginateFiltersTypeDef",
    "DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef",
    "DescribeDBSubnetGroupsPaginateResponseTypeDef",
    "DescribeEventsPaginateFiltersTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef",
    "DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef",
)


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    """
    Type definition for `ClientAddTagsToResource` `Tags`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    """
    Type definition for `ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActions` `PendingMaintenanceActionDetails`

    Provides information about a pending maintenance action for a resource.

    - **Action** *(string) --*

      The type of pending maintenance action that is available for the resource.

    - **AutoAppliedAfterDate** *(datetime) --*

      The date of the maintenance window when the action is applied. The maintenance action
      is applied to the resource during its first maintenance window after this date. If this
      date is specified, any ``next-maintenance`` opt-in requests are ignored.

    - **ForcedApplyDate** *(datetime) --*

      The date when the maintenance action is automatically applied. The maintenance action
      is applied to the resource on this date regardless of the maintenance window for the
      resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

    - **OptInStatus** *(string) --*

      Indicates the type of opt-in request that has been received for the resource.

    - **CurrentApplyDate** *(datetime) --*

      The effective date when the pending maintenance action is applied to the resource.

    - **Description** *(string) --*

      A description providing more detail about the maintenance action.
    """


_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef(
    _ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
):
    """
    Type definition for `ClientApplyPendingMaintenanceActionResponse` `ResourcePendingMaintenanceActions`

    Represents the output of  ApplyPendingMaintenanceAction .

    - **ResourceIdentifier** *(string) --*

      The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.

    - **PendingMaintenanceActionDetails** *(list) --*

      A list that provides details about the pending maintenance actions for the resource.

      - *(dict) --*

        Provides information about a pending maintenance action for a resource.

        - **Action** *(string) --*

          The type of pending maintenance action that is available for the resource.

        - **AutoAppliedAfterDate** *(datetime) --*

          The date of the maintenance window when the action is applied. The maintenance action
          is applied to the resource during its first maintenance window after this date. If this
          date is specified, any ``next-maintenance`` opt-in requests are ignored.

        - **ForcedApplyDate** *(datetime) --*

          The date when the maintenance action is automatically applied. The maintenance action
          is applied to the resource on this date regardless of the maintenance window for the
          resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

        - **OptInStatus** *(string) --*

          Indicates the type of opt-in request that has been received for the resource.

        - **CurrentApplyDate** *(datetime) --*

          The effective date when the pending maintenance action is applied to the resource.

        - **Description** *(string) --*

          A description providing more detail about the maintenance action.
    """


_ClientApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "_ClientApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
    },
    total=False,
)


class ClientApplyPendingMaintenanceActionResponseTypeDef(
    _ClientApplyPendingMaintenanceActionResponseTypeDef
):
    """
    Type definition for `ClientApplyPendingMaintenanceAction` `Response`

    - **ResourcePendingMaintenanceActions** *(dict) --*

      Represents the output of  ApplyPendingMaintenanceAction .

      - **ResourceIdentifier** *(string) --*

        The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.

      - **PendingMaintenanceActionDetails** *(list) --*

        A list that provides details about the pending maintenance actions for the resource.

        - *(dict) --*

          Provides information about a pending maintenance action for a resource.

          - **Action** *(string) --*

            The type of pending maintenance action that is available for the resource.

          - **AutoAppliedAfterDate** *(datetime) --*

            The date of the maintenance window when the action is applied. The maintenance action
            is applied to the resource during its first maintenance window after this date. If this
            date is specified, any ``next-maintenance`` opt-in requests are ignored.

          - **ForcedApplyDate** *(datetime) --*

            The date when the maintenance action is automatically applied. The maintenance action
            is applied to the resource on this date regardless of the maintenance window for the
            resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

          - **OptInStatus** *(string) --*

            Indicates the type of opt-in request that has been received for the resource.

          - **CurrentApplyDate** *(datetime) --*

            The effective date when the pending maintenance action is applied to the resource.

          - **Description** *(string) --*

            A description providing more detail about the maintenance action.
    """


_ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef = TypedDict(
    "_ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef(
    _ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
):
    """
    Type definition for `ClientCopyDbClusterParameterGroupResponse` `DBClusterParameterGroup`

    Detailed information about a DB cluster parameter group.

    - **DBClusterParameterGroupName** *(string) --*

      Provides the name of the DB cluster parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB cluster parameter group is
      compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB cluster parameter group.

    - **DBClusterParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientCopyDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientCopyDbClusterParameterGroupResponseTypeDef",
    {
        "DBClusterParameterGroup": ClientCopyDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
    },
    total=False,
)


class ClientCopyDbClusterParameterGroupResponseTypeDef(
    _ClientCopyDbClusterParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientCopyDbClusterParameterGroup` `Response`

    - **DBClusterParameterGroup** *(dict) --*

      Detailed information about a DB cluster parameter group.

      - **DBClusterParameterGroupName** *(string) --*

        Provides the name of the DB cluster parameter group.

      - **DBParameterGroupFamily** *(string) --*

        Provides the name of the DB parameter group family that this DB cluster parameter group is
        compatible with.

      - **Description** *(string) --*

        Provides the customer-specified description for this DB cluster parameter group.

      - **DBClusterParameterGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientCopyDbClusterParameterGroupTagsTypeDef = TypedDict(
    "_ClientCopyDbClusterParameterGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCopyDbClusterParameterGroupTagsTypeDef(
    _ClientCopyDbClusterParameterGroupTagsTypeDef
):
    """
    Type definition for `ClientCopyDbClusterParameterGroup` `Tags`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)


class ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    Type definition for `ClientCopyDbClusterSnapshotResponse` `DBClusterSnapshot`

    Detailed information about a DB cluster snapshot.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
      snapshot can be restored in.

      - *(string) --*

    - **DBClusterSnapshotIdentifier** *(string) --*

      Specifies the identifier for the DB cluster snapshot.

    - **DBClusterIdentifier** *(string) --*

      Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
      created from.

    - **SnapshotCreateTime** *(datetime) --*

      Provides the time when the snapshot was taken, in UTC.

    - **Engine** *(string) --*

      Specifies the name of the database engine.

    - **Status** *(string) --*

      Specifies the status of this DB cluster snapshot.

    - **Port** *(integer) --*

      Specifies the port that the DB cluster was listening on at the time of the snapshot.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID that is associated with the DB cluster snapshot.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **MasterUsername** *(string) --*

      Provides the master user name for the DB cluster snapshot.

    - **EngineVersion** *(string) --*

      Provides the version of the database engine for this DB cluster snapshot.

    - **SnapshotType** *(string) --*

      Provides the type of the DB cluster snapshot.

    - **PercentProgress** *(integer) --*

      Specifies the percentage of the estimated data that has been transferred.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster snapshot is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster snapshot.

    - **DBClusterSnapshotArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster snapshot.

    - **SourceDBClusterSnapshotArn** *(string) --*

      If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the
      source DB cluster snapshot; otherwise, a null value.
    """


_ClientCopyDbClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotResponseTypeDef",
    {"DBClusterSnapshot": ClientCopyDbClusterSnapshotResponseDBClusterSnapshotTypeDef},
    total=False,
)


class ClientCopyDbClusterSnapshotResponseTypeDef(
    _ClientCopyDbClusterSnapshotResponseTypeDef
):
    """
    Type definition for `ClientCopyDbClusterSnapshot` `Response`

    - **DBClusterSnapshot** *(dict) --*

      Detailed information about a DB cluster snapshot.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
        snapshot can be restored in.

        - *(string) --*

      - **DBClusterSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB cluster snapshot.

      - **DBClusterIdentifier** *(string) --*

        Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
        created from.

      - **SnapshotCreateTime** *(datetime) --*

        Provides the time when the snapshot was taken, in UTC.

      - **Engine** *(string) --*

        Specifies the name of the database engine.

      - **Status** *(string) --*

        Specifies the status of this DB cluster snapshot.

      - **Port** *(integer) --*

        Specifies the port that the DB cluster was listening on at the time of the snapshot.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID that is associated with the DB cluster snapshot.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **MasterUsername** *(string) --*

        Provides the master user name for the DB cluster snapshot.

      - **EngineVersion** *(string) --*

        Provides the version of the database engine for this DB cluster snapshot.

      - **SnapshotType** *(string) --*

        Provides the type of the DB cluster snapshot.

      - **PercentProgress** *(integer) --*

        Specifies the percentage of the estimated data that has been transferred.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster snapshot is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster snapshot.

      - **DBClusterSnapshotArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster snapshot.

      - **SourceDBClusterSnapshotArn** *(string) --*

        If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the
        source DB cluster snapshot; otherwise, a null value.
    """


_ClientCopyDbClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCopyDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCopyDbClusterSnapshotTagsTypeDef(_ClientCopyDbClusterSnapshotTagsTypeDef):
    """
    Type definition for `ClientCopyDbClusterSnapshot` `Tags`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef = TypedDict(
    "_ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef(
    _ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
):
    """
    Type definition for `ClientCreateDbClusterParameterGroupResponse` `DBClusterParameterGroup`

    Detailed information about a DB cluster parameter group.

    - **DBClusterParameterGroupName** *(string) --*

      Provides the name of the DB cluster parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB cluster parameter group is
      compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB cluster parameter group.

    - **DBClusterParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientCreateDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientCreateDbClusterParameterGroupResponseTypeDef",
    {
        "DBClusterParameterGroup": ClientCreateDbClusterParameterGroupResponseDBClusterParameterGroupTypeDef
    },
    total=False,
)


class ClientCreateDbClusterParameterGroupResponseTypeDef(
    _ClientCreateDbClusterParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateDbClusterParameterGroup` `Response`

    - **DBClusterParameterGroup** *(dict) --*

      Detailed information about a DB cluster parameter group.

      - **DBClusterParameterGroupName** *(string) --*

        Provides the name of the DB cluster parameter group.

      - **DBParameterGroupFamily** *(string) --*

        Provides the name of the DB parameter group family that this DB cluster parameter group is
        compatible with.

      - **Description** *(string) --*

        Provides the customer-specified description for this DB cluster parameter group.

      - **DBClusterParameterGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientCreateDbClusterParameterGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterParameterGroupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateDbClusterParameterGroupTagsTypeDef(
    _ClientCreateDbClusterParameterGroupTagsTypeDef
):
    """
    Type definition for `ClientCreateDbClusterParameterGroup` `Tags`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientCreateDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      ``Status`` property returns one of the following values:

      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
      cannot assume the IAM role to access other AWS services on your behalf.
    """


_ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientCreateDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      A value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to
      the primary instance after a failure of the existing primary instance.
    """


_ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientCreateDbClusterResponseDBCluster` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientCreateDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientCreateDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientCreateDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientCreateDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientCreateDbClusterResponseDBClusterTypeDef(
    _ClientCreateDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientCreateDbClusterResponse` `DBCluster`

    Detailed information about a DB cluster.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
      created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group that is associated with the DB cluster, including
      the name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      The earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
      connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
      clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
      connection requests among the Amazon DocumentDB replicas in the DB cluster. This
      functionality can help balance your read workload across multiple Amazon DocumentDB
      replicas in your DB cluster.

      If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
      promoted to be the primary instance, your connection is dropped. To continue sending your
      read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
      the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master user name for the DB cluster.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          A value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to
          the primary instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
      to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          ``Status`` property returns one of the following values:

          * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
          cannot assume the IAM role to access other AWS services on your behalf.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

      - *(string) --*

    - **DeletionProtection** *(boolean) --*

      Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
      cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
      ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientCreateDbClusterResponseTypeDef = TypedDict(
    "_ClientCreateDbClusterResponseTypeDef",
    {"DBCluster": ClientCreateDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientCreateDbClusterResponseTypeDef(_ClientCreateDbClusterResponseTypeDef):
    """
    Type definition for `ClientCreateDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group that is associated with the DB cluster, including
        the name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        The earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
        connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
        clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
        connection requests among the Amazon DocumentDB replicas in the DB cluster. This
        functionality can help balance your read workload across multiple Amazon DocumentDB
        replicas in your DB cluster.

        If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
        promoted to be the primary instance, your connection is dropped. To continue sending your
        read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
        the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master user name for the DB cluster.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            A value that is ``true`` if the cluster member is the primary instance for the DB
            cluster and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which an Amazon DocumentDB replica is promoted to
            the primary instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
        to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The
            ``Status`` property returns one of the following values:

            * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
            cannot assume the IAM role to access other AWS services on your behalf.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

        - *(string) --*

      - **DeletionProtection** *(boolean) --*

        Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
        cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
        ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)


class ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    Type definition for `ClientCreateDbClusterSnapshotResponse` `DBClusterSnapshot`

    Detailed information about a DB cluster snapshot.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
      snapshot can be restored in.

      - *(string) --*

    - **DBClusterSnapshotIdentifier** *(string) --*

      Specifies the identifier for the DB cluster snapshot.

    - **DBClusterIdentifier** *(string) --*

      Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
      created from.

    - **SnapshotCreateTime** *(datetime) --*

      Provides the time when the snapshot was taken, in UTC.

    - **Engine** *(string) --*

      Specifies the name of the database engine.

    - **Status** *(string) --*

      Specifies the status of this DB cluster snapshot.

    - **Port** *(integer) --*

      Specifies the port that the DB cluster was listening on at the time of the snapshot.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID that is associated with the DB cluster snapshot.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **MasterUsername** *(string) --*

      Provides the master user name for the DB cluster snapshot.

    - **EngineVersion** *(string) --*

      Provides the version of the database engine for this DB cluster snapshot.

    - **SnapshotType** *(string) --*

      Provides the type of the DB cluster snapshot.

    - **PercentProgress** *(integer) --*

      Specifies the percentage of the estimated data that has been transferred.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster snapshot is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster snapshot.

    - **DBClusterSnapshotArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster snapshot.

    - **SourceDBClusterSnapshotArn** *(string) --*

      If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the
      source DB cluster snapshot; otherwise, a null value.
    """


_ClientCreateDbClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotResponseTypeDef",
    {
        "DBClusterSnapshot": ClientCreateDbClusterSnapshotResponseDBClusterSnapshotTypeDef
    },
    total=False,
)


class ClientCreateDbClusterSnapshotResponseTypeDef(
    _ClientCreateDbClusterSnapshotResponseTypeDef
):
    """
    Type definition for `ClientCreateDbClusterSnapshot` `Response`

    - **DBClusterSnapshot** *(dict) --*

      Detailed information about a DB cluster snapshot.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
        snapshot can be restored in.

        - *(string) --*

      - **DBClusterSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB cluster snapshot.

      - **DBClusterIdentifier** *(string) --*

        Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
        created from.

      - **SnapshotCreateTime** *(datetime) --*

        Provides the time when the snapshot was taken, in UTC.

      - **Engine** *(string) --*

        Specifies the name of the database engine.

      - **Status** *(string) --*

        Specifies the status of this DB cluster snapshot.

      - **Port** *(integer) --*

        Specifies the port that the DB cluster was listening on at the time of the snapshot.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID that is associated with the DB cluster snapshot.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **MasterUsername** *(string) --*

        Provides the master user name for the DB cluster snapshot.

      - **EngineVersion** *(string) --*

        Provides the version of the database engine for this DB cluster snapshot.

      - **SnapshotType** *(string) --*

        Provides the type of the DB cluster snapshot.

      - **PercentProgress** *(integer) --*

        Specifies the percentage of the estimated data that has been transferred.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster snapshot is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster snapshot.

      - **DBClusterSnapshotArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster snapshot.

      - **SourceDBClusterSnapshotArn** *(string) --*

        If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the
        source DB cluster snapshot; otherwise, a null value.
    """


_ClientCreateDbClusterSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterSnapshotTagsTypeDef(
    _ClientCreateDbClusterSnapshotTagsTypeDef
):
    """
    Type definition for `ClientCreateDbClusterSnapshot` `Tags`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbClusterTagsTypeDef = TypedDict(
    "_ClientCreateDbClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbClusterTagsTypeDef(_ClientCreateDbClusterTagsTypeDef):
    """
    Type definition for `ClientCreateDbCluster` `Tags`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the Availability Zone for the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstanceDBSubnetGroup` `Subnets`

    Detailed information about a subnet.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the Availability Zone for the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `DBSubnetGroup`

    Specifies information on the subnet group that is associated with the DB instance,
    including the name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Detailed information about one or more subnets within a DB subnet group.

      - *(dict) --*

        Detailed information about a subnet.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the Availability Zone for the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstancePendingModifiedValues` `PendingCloudwatchLogsExports`

    A list of the log types whose configuration is still pending. These log types are in the
    process of being activated or deactivated.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to Amazon CloudWatch Logs.

      - *(string) --*
    """


_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is included only when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
      currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently in-progress change of the master credentials for the DB
      instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` , ``bring-your-own-license`` ,
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
      currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the certificate authority (CA) certificate for the DB
      instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      A list of the log types whose configuration is still pending. These log types are in the
      process of being activated or deactivated.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to Amazon CloudWatch Logs.

        - *(string) --*
    """


_ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "``read replication`` ."

    - **Normal** *(boolean) --*

      A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
      the instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a ``StatusType`` of read replica, the values can be
      ``replicating`` , error, ``stopped`` , or ``terminated`` .

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponseDBInstance` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientCreateDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientCreateDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[
            ClientCreateDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientCreateDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientCreateDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientCreateDbInstanceResponseDBInstanceTypeDef(
    _ClientCreateDbInstanceResponseDBInstanceTypeDef
):
    """
    Type definition for `ClientCreateDbInstanceResponse` `DBInstance`

    Detailed information about a DB instance.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-provided database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time that the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone that the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group that is associated with the DB instance,
      including the name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Detailed information about one or more subnets within a DB subnet group.

        - *(dict) --*

          Detailed information about a subnet.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the Availability Zone for the subnet.

            - **Name** *(string) --*

              The name of the Availability Zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is included only when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
        currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently in-progress change of the master credentials for the DB
        instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` , ``bring-your-own-license`` ,
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
        currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the certificate authority (CA) certificate for the DB
        instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        A list of the log types whose configuration is still pending. These log types are in the
        process of being activated or deactivated.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to Amazon CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **PubliclyAccessible** *(boolean) --*

      Not supported. Amazon DocumentDB does not currently support public endpoints. The value of
      ``PubliclyAccessible`` is always ``false`` .

    - **StatusInfos** *(list) --*

      The status of a read replica. If the instance is not a read replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "``read replication`` ."

        - **Normal** *(boolean) --*

          A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
          the instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a ``StatusType`` of read replica, the values can be
          ``replicating`` , error, ``stopped`` , or ``terminated`` .

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **DBClusterIdentifier** *(string) --*

      Contains the name of the DB cluster that the DB instance is a member of if the DB instance
      is a member of a DB cluster.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether or not the DB instance is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      instance.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
      primary instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to Amazon CloudWatch Logs.

      - *(string) --*
    """


_ClientCreateDbInstanceResponseTypeDef = TypedDict(
    "_ClientCreateDbInstanceResponseTypeDef",
    {"DBInstance": ClientCreateDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientCreateDbInstanceResponseTypeDef(_ClientCreateDbInstanceResponseTypeDef):
    """
    Type definition for `ClientCreateDbInstance` `Response`

    - **DBInstance** *(dict) --*

      Detailed information about a DB instance.

      - **DBInstanceIdentifier** *(string) --*

        Contains a user-provided database identifier. This identifier is the unique key that
        identifies a DB instance.

      - **DBInstanceClass** *(string) --*

        Contains the name of the compute and memory capacity class of the DB instance.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB instance.

      - **DBInstanceStatus** *(string) --*

        Specifies the current state of this database.

      - **Endpoint** *(dict) --*

        Specifies the connection endpoint.

        - **Address** *(string) --*

          Specifies the DNS address of the DB instance.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **InstanceCreateTime** *(datetime) --*

        Provides the date and time that the DB instance was created.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security group elements that the DB instance belongs to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **AvailabilityZone** *(string) --*

        Specifies the name of the Availability Zone that the DB instance is located in.

      - **DBSubnetGroup** *(dict) --*

        Specifies information on the subnet group that is associated with the DB instance,
        including the name, description, and subnets in the subnet group.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the virtual private cloud (VPC) ID of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Detailed information about one or more subnets within a DB subnet group.

          - *(dict) --*

            Detailed information about a subnet.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the Availability Zone for the subnet.

              - **Name** *(string) --*

                The name of the Availability Zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **PendingModifiedValues** *(dict) --*

        Specifies that changes to the DB instance are pending. This element is included only when
        changes are pending. Specific changes are identified by subelements.

        - **DBInstanceClass** *(string) --*

          Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
          currently being applied.

        - **AllocatedStorage** *(integer) --*

          Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
          currently being applied.

        - **MasterUserPassword** *(string) --*

          Contains the pending or currently in-progress change of the master credentials for the DB
          instance.

        - **Port** *(integer) --*

          Specifies the pending port for the DB instance.

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the pending number of days for which automated backups are retained.

        - **MultiAZ** *(boolean) --*

          Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LicenseModel** *(string) --*

          The license model for the DB instance.

          Valid values: ``license-included`` , ``bring-your-own-license`` ,
          ``general-public-license``

        - **Iops** *(integer) --*

          Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
          currently being applied.

        - **DBInstanceIdentifier** *(string) --*

          Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
          currently being applied.

        - **StorageType** *(string) --*

          Specifies the storage type to be associated with the DB instance.

        - **CACertificateIdentifier** *(string) --*

          Specifies the identifier of the certificate authority (CA) certificate for the DB
          instance.

        - **DBSubnetGroupName** *(string) --*

          The new DB subnet group for the DB instance.

        - **PendingCloudwatchLogsExports** *(dict) --*

          A list of the log types whose configuration is still pending. These log types are in the
          process of being activated or deactivated.

          - **LogTypesToEnable** *(list) --*

            Log types that are in the process of being deactivated. After they are deactivated,
            these log types aren't exported to CloudWatch Logs.

            - *(string) --*

          - **LogTypesToDisable** *(list) --*

            Log types that are in the process of being enabled. After they are enabled, these log
            types are exported to Amazon CloudWatch Logs.

            - *(string) --*

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Indicates that minor version patches are applied automatically.

      - **PubliclyAccessible** *(boolean) --*

        Not supported. Amazon DocumentDB does not currently support public endpoints. The value of
        ``PubliclyAccessible`` is always ``false`` .

      - **StatusInfos** *(list) --*

        The status of a read replica. If the instance is not a read replica, this is blank.

        - *(dict) --*

          Provides a list of status information for a DB instance.

          - **StatusType** *(string) --*

            This value is currently "``read replication`` ."

          - **Normal** *(boolean) --*

            A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
            the instance is in an error state.

          - **Status** *(string) --*

            Status of the DB instance. For a ``StatusType`` of read replica, the values can be
            ``replicating`` , error, ``stopped`` , or ``terminated`` .

          - **Message** *(string) --*

            Details of the error if there is an error for the instance. If the instance is not in
            an error state, this value is blank.

      - **DBClusterIdentifier** *(string) --*

        Contains the name of the DB cluster that the DB instance is a member of if the DB instance
        is a member of a DB cluster.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether or not the DB instance is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        instance.

      - **DbiResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
        in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

      - **CACertificateIdentifier** *(string) --*

        The identifier of the CA certificate for this DB instance.

      - **PromotionTier** *(integer) --*

        A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
        primary instance after a failure of the existing primary instance.

      - **DBInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB instance.

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB instance is configured to export to Amazon CloudWatch Logs.

        - *(string) --*
    """


_ClientCreateDbInstanceTagsTypeDef = TypedDict(
    "_ClientCreateDbInstanceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbInstanceTagsTypeDef(_ClientCreateDbInstanceTagsTypeDef):
    """
    Type definition for `ClientCreateDbInstance` `Tags`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the Availability Zone for the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef(
    _ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientCreateDbSubnetGroupResponseDBSubnetGroup` `Subnets`

    Detailed information about a subnet.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the Availability Zone for the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientCreateDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef(
    _ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientCreateDbSubnetGroupResponse` `DBSubnetGroup`

    Detailed information about a DB subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Detailed information about one or more subnets within a DB subnet group.

      - *(dict) --*

        Detailed information about a subnet.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the Availability Zone for the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientCreateDbSubnetGroupResponseTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupResponseTypeDef",
    {"DBSubnetGroup": ClientCreateDbSubnetGroupResponseDBSubnetGroupTypeDef},
    total=False,
)


class ClientCreateDbSubnetGroupResponseTypeDef(
    _ClientCreateDbSubnetGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateDbSubnetGroup` `Response`

    - **DBSubnetGroup** *(dict) --*

      Detailed information about a DB subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Detailed information about one or more subnets within a DB subnet group.

        - *(dict) --*

          Detailed information about a subnet.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the Availability Zone for the subnet.

            - **Name** *(string) --*

              The name of the Availability Zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientCreateDbSubnetGroupTagsTypeDef = TypedDict(
    "_ClientCreateDbSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDbSubnetGroupTagsTypeDef(_ClientCreateDbSubnetGroupTagsTypeDef):
    """
    Type definition for `ClientCreateDbSubnetGroup` `Tags`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      ``Status`` property returns one of the following values:

      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
      cannot assume the IAM role to access other AWS services on your behalf.
    """


_ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      A value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to
      the primary instance after a failure of the existing primary instance.
    """


_ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterResponseDBCluster` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientDeleteDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientDeleteDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientDeleteDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientDeleteDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientDeleteDbClusterResponseDBClusterTypeDef(
    _ClientDeleteDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterResponse` `DBCluster`

    Detailed information about a DB cluster.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
      created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group that is associated with the DB cluster, including
      the name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      The earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
      connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
      clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
      connection requests among the Amazon DocumentDB replicas in the DB cluster. This
      functionality can help balance your read workload across multiple Amazon DocumentDB
      replicas in your DB cluster.

      If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
      promoted to be the primary instance, your connection is dropped. To continue sending your
      read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
      the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master user name for the DB cluster.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          A value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to
          the primary instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
      to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          ``Status`` property returns one of the following values:

          * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
          cannot assume the IAM role to access other AWS services on your behalf.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

      - *(string) --*

    - **DeletionProtection** *(boolean) --*

      Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
      cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
      ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientDeleteDbClusterResponseTypeDef = TypedDict(
    "_ClientDeleteDbClusterResponseTypeDef",
    {"DBCluster": ClientDeleteDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientDeleteDbClusterResponseTypeDef(_ClientDeleteDbClusterResponseTypeDef):
    """
    Type definition for `ClientDeleteDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group that is associated with the DB cluster, including
        the name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        The earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
        connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
        clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
        connection requests among the Amazon DocumentDB replicas in the DB cluster. This
        functionality can help balance your read workload across multiple Amazon DocumentDB
        replicas in your DB cluster.

        If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
        promoted to be the primary instance, your connection is dropped. To continue sending your
        read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
        the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master user name for the DB cluster.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            A value that is ``true`` if the cluster member is the primary instance for the DB
            cluster and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which an Amazon DocumentDB replica is promoted to
            the primary instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
        to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The
            ``Status`` property returns one of the following values:

            * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
            cannot assume the IAM role to access other AWS services on your behalf.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

        - *(string) --*

      - **DeletionProtection** *(boolean) --*

        Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
        cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
        ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef = TypedDict(
    "_ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)


class ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef(
    _ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterSnapshotResponse` `DBClusterSnapshot`

    Detailed information about a DB cluster snapshot.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
      snapshot can be restored in.

      - *(string) --*

    - **DBClusterSnapshotIdentifier** *(string) --*

      Specifies the identifier for the DB cluster snapshot.

    - **DBClusterIdentifier** *(string) --*

      Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
      created from.

    - **SnapshotCreateTime** *(datetime) --*

      Provides the time when the snapshot was taken, in UTC.

    - **Engine** *(string) --*

      Specifies the name of the database engine.

    - **Status** *(string) --*

      Specifies the status of this DB cluster snapshot.

    - **Port** *(integer) --*

      Specifies the port that the DB cluster was listening on at the time of the snapshot.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID that is associated with the DB cluster snapshot.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **MasterUsername** *(string) --*

      Provides the master user name for the DB cluster snapshot.

    - **EngineVersion** *(string) --*

      Provides the version of the database engine for this DB cluster snapshot.

    - **SnapshotType** *(string) --*

      Provides the type of the DB cluster snapshot.

    - **PercentProgress** *(integer) --*

      Specifies the percentage of the estimated data that has been transferred.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster snapshot is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster snapshot.

    - **DBClusterSnapshotArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster snapshot.

    - **SourceDBClusterSnapshotArn** *(string) --*

      If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the
      source DB cluster snapshot; otherwise, a null value.
    """


_ClientDeleteDbClusterSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteDbClusterSnapshotResponseTypeDef",
    {
        "DBClusterSnapshot": ClientDeleteDbClusterSnapshotResponseDBClusterSnapshotTypeDef
    },
    total=False,
)


class ClientDeleteDbClusterSnapshotResponseTypeDef(
    _ClientDeleteDbClusterSnapshotResponseTypeDef
):
    """
    Type definition for `ClientDeleteDbClusterSnapshot` `Response`

    - **DBClusterSnapshot** *(dict) --*

      Detailed information about a DB cluster snapshot.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
        snapshot can be restored in.

        - *(string) --*

      - **DBClusterSnapshotIdentifier** *(string) --*

        Specifies the identifier for the DB cluster snapshot.

      - **DBClusterIdentifier** *(string) --*

        Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
        created from.

      - **SnapshotCreateTime** *(datetime) --*

        Provides the time when the snapshot was taken, in UTC.

      - **Engine** *(string) --*

        Specifies the name of the database engine.

      - **Status** *(string) --*

        Specifies the status of this DB cluster snapshot.

      - **Port** *(integer) --*

        Specifies the port that the DB cluster was listening on at the time of the snapshot.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID that is associated with the DB cluster snapshot.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **MasterUsername** *(string) --*

        Provides the master user name for the DB cluster snapshot.

      - **EngineVersion** *(string) --*

        Provides the version of the database engine for this DB cluster snapshot.

      - **SnapshotType** *(string) --*

        Provides the type of the DB cluster snapshot.

      - **PercentProgress** *(integer) --*

        Specifies the percentage of the estimated data that has been transferred.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster snapshot is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster snapshot.

      - **DBClusterSnapshotArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster snapshot.

      - **SourceDBClusterSnapshotArn** *(string) --*

        If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the
        source DB cluster snapshot; otherwise, a null value.
    """


_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the Availability Zone for the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroup` `Subnets`

    Detailed information about a subnet.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the Availability Zone for the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `DBSubnetGroup`

    Specifies information on the subnet group that is associated with the DB instance,
    including the name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Detailed information about one or more subnets within a DB subnet group.

      - *(dict) --*

        Detailed information about a subnet.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the Availability Zone for the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstancePendingModifiedValues` `PendingCloudwatchLogsExports`

    A list of the log types whose configuration is still pending. These log types are in the
    process of being activated or deactivated.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to Amazon CloudWatch Logs.

      - *(string) --*
    """


_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is included only when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
      currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently in-progress change of the master credentials for the DB
      instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` , ``bring-your-own-license`` ,
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
      currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the certificate authority (CA) certificate for the DB
      instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      A list of the log types whose configuration is still pending. These log types are in the
      process of being activated or deactivated.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to Amazon CloudWatch Logs.

        - *(string) --*
    """


_ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "``read replication`` ."

    - **Normal** *(boolean) --*

      A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
      the instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a ``StatusType`` of read replica, the values can be
      ``replicating`` , error, ``stopped`` , or ``terminated`` .

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponseDBInstance` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientDeleteDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientDeleteDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[
            ClientDeleteDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDeleteDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientDeleteDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientDeleteDbInstanceResponseDBInstanceTypeDef(
    _ClientDeleteDbInstanceResponseDBInstanceTypeDef
):
    """
    Type definition for `ClientDeleteDbInstanceResponse` `DBInstance`

    Detailed information about a DB instance.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-provided database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time that the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone that the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group that is associated with the DB instance,
      including the name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Detailed information about one or more subnets within a DB subnet group.

        - *(dict) --*

          Detailed information about a subnet.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the Availability Zone for the subnet.

            - **Name** *(string) --*

              The name of the Availability Zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is included only when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
        currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently in-progress change of the master credentials for the DB
        instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` , ``bring-your-own-license`` ,
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
        currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the certificate authority (CA) certificate for the DB
        instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        A list of the log types whose configuration is still pending. These log types are in the
        process of being activated or deactivated.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to Amazon CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **PubliclyAccessible** *(boolean) --*

      Not supported. Amazon DocumentDB does not currently support public endpoints. The value of
      ``PubliclyAccessible`` is always ``false`` .

    - **StatusInfos** *(list) --*

      The status of a read replica. If the instance is not a read replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "``read replication`` ."

        - **Normal** *(boolean) --*

          A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
          the instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a ``StatusType`` of read replica, the values can be
          ``replicating`` , error, ``stopped`` , or ``terminated`` .

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **DBClusterIdentifier** *(string) --*

      Contains the name of the DB cluster that the DB instance is a member of if the DB instance
      is a member of a DB cluster.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether or not the DB instance is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      instance.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
      primary instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to Amazon CloudWatch Logs.

      - *(string) --*
    """


_ClientDeleteDbInstanceResponseTypeDef = TypedDict(
    "_ClientDeleteDbInstanceResponseTypeDef",
    {"DBInstance": ClientDeleteDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientDeleteDbInstanceResponseTypeDef(_ClientDeleteDbInstanceResponseTypeDef):
    """
    Type definition for `ClientDeleteDbInstance` `Response`

    - **DBInstance** *(dict) --*

      Detailed information about a DB instance.

      - **DBInstanceIdentifier** *(string) --*

        Contains a user-provided database identifier. This identifier is the unique key that
        identifies a DB instance.

      - **DBInstanceClass** *(string) --*

        Contains the name of the compute and memory capacity class of the DB instance.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB instance.

      - **DBInstanceStatus** *(string) --*

        Specifies the current state of this database.

      - **Endpoint** *(dict) --*

        Specifies the connection endpoint.

        - **Address** *(string) --*

          Specifies the DNS address of the DB instance.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **InstanceCreateTime** *(datetime) --*

        Provides the date and time that the DB instance was created.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security group elements that the DB instance belongs to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **AvailabilityZone** *(string) --*

        Specifies the name of the Availability Zone that the DB instance is located in.

      - **DBSubnetGroup** *(dict) --*

        Specifies information on the subnet group that is associated with the DB instance,
        including the name, description, and subnets in the subnet group.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the virtual private cloud (VPC) ID of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Detailed information about one or more subnets within a DB subnet group.

          - *(dict) --*

            Detailed information about a subnet.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the Availability Zone for the subnet.

              - **Name** *(string) --*

                The name of the Availability Zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **PendingModifiedValues** *(dict) --*

        Specifies that changes to the DB instance are pending. This element is included only when
        changes are pending. Specific changes are identified by subelements.

        - **DBInstanceClass** *(string) --*

          Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
          currently being applied.

        - **AllocatedStorage** *(integer) --*

          Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
          currently being applied.

        - **MasterUserPassword** *(string) --*

          Contains the pending or currently in-progress change of the master credentials for the DB
          instance.

        - **Port** *(integer) --*

          Specifies the pending port for the DB instance.

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the pending number of days for which automated backups are retained.

        - **MultiAZ** *(boolean) --*

          Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LicenseModel** *(string) --*

          The license model for the DB instance.

          Valid values: ``license-included`` , ``bring-your-own-license`` ,
          ``general-public-license``

        - **Iops** *(integer) --*

          Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
          currently being applied.

        - **DBInstanceIdentifier** *(string) --*

          Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
          currently being applied.

        - **StorageType** *(string) --*

          Specifies the storage type to be associated with the DB instance.

        - **CACertificateIdentifier** *(string) --*

          Specifies the identifier of the certificate authority (CA) certificate for the DB
          instance.

        - **DBSubnetGroupName** *(string) --*

          The new DB subnet group for the DB instance.

        - **PendingCloudwatchLogsExports** *(dict) --*

          A list of the log types whose configuration is still pending. These log types are in the
          process of being activated or deactivated.

          - **LogTypesToEnable** *(list) --*

            Log types that are in the process of being deactivated. After they are deactivated,
            these log types aren't exported to CloudWatch Logs.

            - *(string) --*

          - **LogTypesToDisable** *(list) --*

            Log types that are in the process of being enabled. After they are enabled, these log
            types are exported to Amazon CloudWatch Logs.

            - *(string) --*

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Indicates that minor version patches are applied automatically.

      - **PubliclyAccessible** *(boolean) --*

        Not supported. Amazon DocumentDB does not currently support public endpoints. The value of
        ``PubliclyAccessible`` is always ``false`` .

      - **StatusInfos** *(list) --*

        The status of a read replica. If the instance is not a read replica, this is blank.

        - *(dict) --*

          Provides a list of status information for a DB instance.

          - **StatusType** *(string) --*

            This value is currently "``read replication`` ."

          - **Normal** *(boolean) --*

            A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
            the instance is in an error state.

          - **Status** *(string) --*

            Status of the DB instance. For a ``StatusType`` of read replica, the values can be
            ``replicating`` , error, ``stopped`` , or ``terminated`` .

          - **Message** *(string) --*

            Details of the error if there is an error for the instance. If the instance is not in
            an error state, this value is blank.

      - **DBClusterIdentifier** *(string) --*

        Contains the name of the DB cluster that the DB instance is a member of if the DB instance
        is a member of a DB cluster.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether or not the DB instance is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        instance.

      - **DbiResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
        in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

      - **CACertificateIdentifier** *(string) --*

        The identifier of the CA certificate for this DB instance.

      - **PromotionTier** *(integer) --*

        A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
        primary instance after a failure of the existing primary instance.

      - **DBInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB instance.

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB instance is configured to export to Amazon CloudWatch Logs.

        - *(string) --*
    """


_ClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_ClientDescribeCertificatesFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeCertificatesFiltersTypeDef(
    _ClientDescribeCertificatesFiltersTypeDef
):
    """
    Type definition for `ClientDescribeCertificates` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeCertificatesResponseCertificatesTypeDef = TypedDict(
    "_ClientDescribeCertificatesResponseCertificatesTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateType": str,
        "Thumbprint": str,
        "ValidFrom": datetime,
        "ValidTill": datetime,
        "CertificateArn": str,
    },
    total=False,
)


class ClientDescribeCertificatesResponseCertificatesTypeDef(
    _ClientDescribeCertificatesResponseCertificatesTypeDef
):
    """
    Type definition for `ClientDescribeCertificatesResponse` `Certificates`

    A certificate authority (CA) certificate for an AWS account.

    - **CertificateIdentifier** *(string) --*

      The unique key that identifies a certificate.

      Example: ``rds-ca-2019``

    - **CertificateType** *(string) --*

      The type of the certificate.

      Example: ``CA``

    - **Thumbprint** *(string) --*

      The thumbprint of the certificate.

    - **ValidFrom** *(datetime) --*

      The starting date-time from which the certificate is valid.

      Example: ``2019-07-31T17:57:09Z``

    - **ValidTill** *(datetime) --*

      The date-time after which the certificate is no longer valid.

      Example: ``2024-07-31T17:57:09Z``

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) for the certificate.

      Example: ``arn:aws:rds:us-east-1::cert:rds-ca-2019``
    """


_ClientDescribeCertificatesResponseTypeDef = TypedDict(
    "_ClientDescribeCertificatesResponseTypeDef",
    {
        "Certificates": List[ClientDescribeCertificatesResponseCertificatesTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeCertificatesResponseTypeDef(
    _ClientDescribeCertificatesResponseTypeDef
):
    """
    Type definition for `ClientDescribeCertificates` `Response`

    - **Certificates** *(list) --*

      A list of certificates for this AWS account.

      - *(dict) --*

        A certificate authority (CA) certificate for an AWS account.

        - **CertificateIdentifier** *(string) --*

          The unique key that identifies a certificate.

          Example: ``rds-ca-2019``

        - **CertificateType** *(string) --*

          The type of the certificate.

          Example: ``CA``

        - **Thumbprint** *(string) --*

          The thumbprint of the certificate.

        - **ValidFrom** *(datetime) --*

          The starting date-time from which the certificate is valid.

          Example: ``2019-07-31T17:57:09Z``

        - **ValidTill** *(datetime) --*

          The date-time after which the certificate is no longer valid.

          Example: ``2024-07-31T17:57:09Z``

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) for the certificate.

          Example: ``arn:aws:rds:us-east-1::cert:rds-ca-2019``

    - **Marker** *(string) --*

      An optional pagination token provided if the number of records retrieved is greater than
      ``MaxRecords`` . If this parameter is specified, the marker specifies the next record in the
      list. Including the value of ``Marker`` in the next call to ``DescribeCertificates`` results
      in the next page of certificates.
    """


_ClientDescribeDbClusterParameterGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterParameterGroupsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeDbClusterParameterGroupsFiltersTypeDef(
    _ClientDescribeDbClusterParameterGroupsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParameterGroups` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef = TypedDict(
    "_ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef(
    _ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParameterGroupsResponse` `DBClusterParameterGroups`

    Detailed information about a DB cluster parameter group.

    - **DBClusterParameterGroupName** *(string) --*

      Provides the name of the DB cluster parameter group.

    - **DBParameterGroupFamily** *(string) --*

      Provides the name of the DB parameter group family that this DB cluster parameter group
      is compatible with.

    - **Description** *(string) --*

      Provides the customer-specified description for this DB cluster parameter group.

    - **DBClusterParameterGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientDescribeDbClusterParameterGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterParameterGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List[
            ClientDescribeDbClusterParameterGroupsResponseDBClusterParameterGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterParameterGroupsResponseTypeDef(
    _ClientDescribeDbClusterParameterGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParameterGroups` `Response`

    Represents the output of  DBClusterParameterGroups .

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **DBClusterParameterGroups** *(list) --*

      A list of DB cluster parameter groups.

      - *(dict) --*

        Detailed information about a DB cluster parameter group.

        - **DBClusterParameterGroupName** *(string) --*

          Provides the name of the DB cluster parameter group.

        - **DBParameterGroupFamily** *(string) --*

          Provides the name of the DB parameter group family that this DB cluster parameter group
          is compatible with.

        - **Description** *(string) --*

          Provides the customer-specified description for this DB cluster parameter group.

        - **DBClusterParameterGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB cluster parameter group.
    """


_ClientDescribeDbClusterParametersFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeDbClusterParametersFiltersTypeDef(
    _ClientDescribeDbClusterParametersFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParameters` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeDbClusterParametersResponseParametersTypeDef = TypedDict(
    "_ClientDescribeDbClusterParametersResponseParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientDescribeDbClusterParametersResponseParametersTypeDef(
    _ClientDescribeDbClusterParametersResponseParametersTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParametersResponse` `Parameters`

    Detailed information about an individual parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine-specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientDescribeDbClusterParametersResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterParametersResponseTypeDef",
    {
        "Parameters": List[ClientDescribeDbClusterParametersResponseParametersTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeDbClusterParametersResponseTypeDef(
    _ClientDescribeDbClusterParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterParameters` `Response`

    Represents the output of  DBClusterParameterGroup .

    - **Parameters** *(list) --*

      Provides a list of parameters for the DB cluster parameter group.

      - *(dict) --*

        Detailed information about an individual parameter.

        - **ParameterName** *(string) --*

          Specifies the name of the parameter.

        - **ParameterValue** *(string) --*

          Specifies the value of the parameter.

        - **Description** *(string) --*

          Provides a description of the parameter.

        - **Source** *(string) --*

          Indicates the source of the parameter value.

        - **ApplyType** *(string) --*

          Specifies the engine-specific parameters type.

        - **DataType** *(string) --*

          Specifies the valid data type for the parameter.

        - **AllowedValues** *(string) --*

          Specifies the valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest engine version to which the parameter can apply.

        - **ApplyMethod** *(string) --*

          Indicates when to apply parameter updates.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .
    """


_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)


class ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef(
    _ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResult` `DBClusterSnapshotAttributes`

    Contains the name and values of a manual DB cluster snapshot attribute.

    Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
    a manual DB cluster snapshot.

    - **AttributeName** *(string) --*

      The name of the manual DB cluster snapshot attribute.

      The attribute named ``restore`` refers to the list of AWS accounts that have permission
      to copy or restore the manual DB cluster snapshot.

    - **AttributeValues** *(list) --*

      The values for the manual DB cluster snapshot attribute.

      If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
      of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
      snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
      public and available for any AWS account to copy or restore.

      - *(string) --*
    """


_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List[
            ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef(
    _ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshotAttributesResponse` `DBClusterSnapshotAttributesResult`

    Detailed information about the attributes that are associated with a DB cluster snapshot.

    - **DBClusterSnapshotIdentifier** *(string) --*

      The identifier of the DB cluster snapshot that the attributes apply to.

    - **DBClusterSnapshotAttributes** *(list) --*

      The list of attributes and values for the DB cluster snapshot.

      - *(dict) --*

        Contains the name and values of a manual DB cluster snapshot attribute.

        Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
        a manual DB cluster snapshot.

        - **AttributeName** *(string) --*

          The name of the manual DB cluster snapshot attribute.

          The attribute named ``restore`` refers to the list of AWS accounts that have permission
          to copy or restore the manual DB cluster snapshot.

        - **AttributeValues** *(list) --*

          The values for the manual DB cluster snapshot attribute.

          If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
          of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
          snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
          public and available for any AWS account to copy or restore.

          - *(string) --*
    """


_ClientDescribeDbClusterSnapshotAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotAttributesResponseTypeDef",
    {
        "DBClusterSnapshotAttributesResult": ClientDescribeDbClusterSnapshotAttributesResponseDBClusterSnapshotAttributesResultTypeDef
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotAttributesResponseTypeDef(
    _ClientDescribeDbClusterSnapshotAttributesResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshotAttributes` `Response`

    - **DBClusterSnapshotAttributesResult** *(dict) --*

      Detailed information about the attributes that are associated with a DB cluster snapshot.

      - **DBClusterSnapshotIdentifier** *(string) --*

        The identifier of the DB cluster snapshot that the attributes apply to.

      - **DBClusterSnapshotAttributes** *(list) --*

        The list of attributes and values for the DB cluster snapshot.

        - *(dict) --*

          Contains the name and values of a manual DB cluster snapshot attribute.

          Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
          a manual DB cluster snapshot.

          - **AttributeName** *(string) --*

            The name of the manual DB cluster snapshot attribute.

            The attribute named ``restore`` refers to the list of AWS accounts that have permission
            to copy or restore the manual DB cluster snapshot.

          - **AttributeValues** *(list) --*

            The values for the manual DB cluster snapshot attribute.

            If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
            of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
            snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
            public and available for any AWS account to copy or restore.

            - *(string) --*
    """


_ClientDescribeDbClusterSnapshotsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeDbClusterSnapshotsFiltersTypeDef(
    _ClientDescribeDbClusterSnapshotsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshots` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef(
    _ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshotsResponse` `DBClusterSnapshots`

    Detailed information about a DB cluster snapshot.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
      snapshot can be restored in.

      - *(string) --*

    - **DBClusterSnapshotIdentifier** *(string) --*

      Specifies the identifier for the DB cluster snapshot.

    - **DBClusterIdentifier** *(string) --*

      Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
      created from.

    - **SnapshotCreateTime** *(datetime) --*

      Provides the time when the snapshot was taken, in UTC.

    - **Engine** *(string) --*

      Specifies the name of the database engine.

    - **Status** *(string) --*

      Specifies the status of this DB cluster snapshot.

    - **Port** *(integer) --*

      Specifies the port that the DB cluster was listening on at the time of the snapshot.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID that is associated with the DB cluster
      snapshot.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **MasterUsername** *(string) --*

      Provides the master user name for the DB cluster snapshot.

    - **EngineVersion** *(string) --*

      Provides the version of the database engine for this DB cluster snapshot.

    - **SnapshotType** *(string) --*

      Provides the type of the DB cluster snapshot.

    - **PercentProgress** *(integer) --*

      Specifies the percentage of the estimated data that has been transferred.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster snapshot is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster snapshot.

    - **DBClusterSnapshotArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster snapshot.

    - **SourceDBClusterSnapshotArn** *(string) --*

      If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the
      source DB cluster snapshot; otherwise, a null value.
    """


_ClientDescribeDbClusterSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeDbClusterSnapshotsResponseTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List[
            ClientDescribeDbClusterSnapshotsResponseDBClusterSnapshotsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbClusterSnapshotsResponseTypeDef(
    _ClientDescribeDbClusterSnapshotsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbClusterSnapshots` `Response`

    Represents the output of  DescribeDBClusterSnapshots .

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **DBClusterSnapshots** *(list) --*

      Provides a list of DB cluster snapshots.

      - *(dict) --*

        Detailed information about a DB cluster snapshot.

        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster
          snapshot can be restored in.

          - *(string) --*

        - **DBClusterSnapshotIdentifier** *(string) --*

          Specifies the identifier for the DB cluster snapshot.

        - **DBClusterIdentifier** *(string) --*

          Specifies the DB cluster identifier of the DB cluster that this DB cluster snapshot was
          created from.

        - **SnapshotCreateTime** *(datetime) --*

          Provides the time when the snapshot was taken, in UTC.

        - **Engine** *(string) --*

          Specifies the name of the database engine.

        - **Status** *(string) --*

          Specifies the status of this DB cluster snapshot.

        - **Port** *(integer) --*

          Specifies the port that the DB cluster was listening on at the time of the snapshot.

        - **VpcId** *(string) --*

          Provides the virtual private cloud (VPC) ID that is associated with the DB cluster
          snapshot.

        - **ClusterCreateTime** *(datetime) --*

          Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

        - **MasterUsername** *(string) --*

          Provides the master user name for the DB cluster snapshot.

        - **EngineVersion** *(string) --*

          Provides the version of the database engine for this DB cluster snapshot.

        - **SnapshotType** *(string) --*

          Provides the type of the DB cluster snapshot.

        - **PercentProgress** *(integer) --*

          Specifies the percentage of the estimated data that has been transferred.

        - **StorageEncrypted** *(boolean) --*

          Specifies whether the DB cluster snapshot is encrypted.

        - **KmsKeyId** *(string) --*

          If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
          cluster snapshot.

        - **DBClusterSnapshotArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB cluster snapshot.

        - **SourceDBClusterSnapshotArn** *(string) --*

          If the DB cluster snapshot was copied from a source DB cluster snapshot, the ARN for the
          source DB cluster snapshot; otherwise, a null value.
    """


_ClientDescribeDbClustersFiltersTypeDef = TypedDict(
    "_ClientDescribeDbClustersFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeDbClustersFiltersTypeDef(_ClientDescribeDbClustersFiltersTypeDef):
    """
    Type definition for `ClientDescribeDbClusters` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef(
    _ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef
):
    """
    Type definition for `ClientDescribeDbClustersResponseDBClusters` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      ``Status`` property returns one of the following values:

      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB
      cluster cannot assume the IAM role to access other AWS services on your behalf.
    """


_ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef(
    _ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef
):
    """
    Type definition for `ClientDescribeDbClustersResponseDBClusters` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      A value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to
      the primary instance after a failure of the existing primary instance.
    """


_ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef(
    _ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbClustersResponseDBClusters` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientDescribeDbClustersResponseDBClustersTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseDBClustersTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientDescribeDbClustersResponseDBClustersDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientDescribeDbClustersResponseDBClustersVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientDescribeDbClustersResponseDBClustersAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientDescribeDbClustersResponseDBClustersTypeDef(
    _ClientDescribeDbClustersResponseDBClustersTypeDef
):
    """
    Type definition for `ClientDescribeDbClustersResponse` `DBClusters`

    Detailed information about a DB cluster.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can
      be created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group that is associated with the DB cluster,
      including the name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      The earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load
      balances connections across the Amazon DocumentDB replicas that are available in a DB
      cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB
      distributes the connection requests among the Amazon DocumentDB replicas in the DB
      cluster. This functionality can help balance your read workload across multiple Amazon
      DocumentDB replicas in your DB cluster.

      If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
      promoted to be the primary instance, your connection is dropped. To continue sending your
      read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect
      to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master user name for the DB cluster.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          A value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to
          the primary instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of virtual private cloud (VPC) security groups that the DB cluster
      belongs to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          ``Status`` property returns one of the following values:

          * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB
          cluster cannot assume the IAM role to access other AWS services on your behalf.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to Amazon CloudWatch
      Logs.

      - *(string) --*

    - **DeletionProtection** *(boolean) --*

      Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
      cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
      ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientDescribeDbClustersResponseTypeDef = TypedDict(
    "_ClientDescribeDbClustersResponseTypeDef",
    {
        "Marker": str,
        "DBClusters": List[ClientDescribeDbClustersResponseDBClustersTypeDef],
    },
    total=False,
)


class ClientDescribeDbClustersResponseTypeDef(_ClientDescribeDbClustersResponseTypeDef):
    """
    Type definition for `ClientDescribeDbClusters` `Response`

    Represents the output of  DescribeDBClusters .

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **DBClusters** *(list) --*

      A list of DB clusters.

      - *(dict) --*

        Detailed information about a DB cluster.

        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can
          be created in.

          - *(string) --*

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the number of days for which automatic DB snapshots are retained.

        - **DBClusterIdentifier** *(string) --*

          Contains a user-supplied DB cluster identifier. This identifier is the unique key that
          identifies a DB cluster.

        - **DBClusterParameterGroup** *(string) --*

          Specifies the name of the DB cluster parameter group for the DB cluster.

        - **DBSubnetGroup** *(string) --*

          Specifies information on the subnet group that is associated with the DB cluster,
          including the name, description, and subnets in the subnet group.

        - **Status** *(string) --*

          Specifies the current state of this DB cluster.

        - **PercentProgress** *(string) --*

          Specifies the progress of the operation as a percentage.

        - **EarliestRestorableTime** *(datetime) --*

          The earliest time to which a database can be restored with point-in-time restore.

        - **Endpoint** *(string) --*

          Specifies the connection endpoint for the primary instance of the DB cluster.

        - **ReaderEndpoint** *(string) --*

          The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load
          balances connections across the Amazon DocumentDB replicas that are available in a DB
          cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB
          distributes the connection requests among the Amazon DocumentDB replicas in the DB
          cluster. This functionality can help balance your read workload across multiple Amazon
          DocumentDB replicas in your DB cluster.

          If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
          promoted to be the primary instance, your connection is dropped. To continue sending your
          read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect
          to the reader endpoint.

        - **MultiAZ** *(boolean) --*

          Specifies whether the DB cluster has instances in multiple Availability Zones.

        - **Engine** *(string) --*

          Provides the name of the database engine to be used for this DB cluster.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LatestRestorableTime** *(datetime) --*

          Specifies the latest time to which a database can be restored with point-in-time restore.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **MasterUsername** *(string) --*

          Contains the master user name for the DB cluster.

        - **PreferredBackupWindow** *(string) --*

          Specifies the daily time range during which automated backups are created if automated
          backups are enabled, as determined by the ``BackupRetentionPeriod`` .

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which system maintenance can occur, in Universal
          Coordinated Time (UTC).

        - **DBClusterMembers** *(list) --*

          Provides the list of instances that make up the DB cluster.

          - *(dict) --*

            Contains information about an instance that is part of a DB cluster.

            - **DBInstanceIdentifier** *(string) --*

              Specifies the instance identifier for this member of the DB cluster.

            - **IsClusterWriter** *(boolean) --*

              A value that is ``true`` if the cluster member is the primary instance for the DB
              cluster and ``false`` otherwise.

            - **DBClusterParameterGroupStatus** *(string) --*

              Specifies the status of the DB cluster parameter group for this member of the DB
              cluster.

            - **PromotionTier** *(integer) --*

              A value that specifies the order in which an Amazon DocumentDB replica is promoted to
              the primary instance after a failure of the existing primary instance.

        - **VpcSecurityGroups** *(list) --*

          Provides a list of virtual private cloud (VPC) security groups that the DB cluster
          belongs to.

          - *(dict) --*

            Used as a response element for queries on virtual private cloud (VPC) security group
            membership.

            - **VpcSecurityGroupId** *(string) --*

              The name of the VPC security group.

            - **Status** *(string) --*

              The status of the VPC security group.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

        - **StorageEncrypted** *(boolean) --*

          Specifies whether the DB cluster is encrypted.

        - **KmsKeyId** *(string) --*

          If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
          cluster.

        - **DbClusterResourceId** *(string) --*

          The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found
          in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

        - **DBClusterArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB cluster.

        - **AssociatedRoles** *(list) --*

          Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
          with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
          the DB cluster to access other AWS services on your behalf.

          - *(dict) --*

            Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
            cluster.

            - **RoleArn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

            - **Status** *(string) --*

              Describes the state of association between the IAM role and the DB cluster. The
              ``Status`` property returns one of the following values:

              * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
              access other AWS services on your behalf.

              * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

              * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB
              cluster cannot assume the IAM role to access other AWS services on your behalf.

        - **ClusterCreateTime** *(datetime) --*

          Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

        - **EnabledCloudwatchLogsExports** *(list) --*

          A list of log types that this DB cluster is configured to export to Amazon CloudWatch
          Logs.

          - *(string) --*

        - **DeletionProtection** *(boolean) --*

          Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
          cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
          ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientDescribeDbEngineVersionsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeDbEngineVersionsFiltersTypeDef(
    _ClientDescribeDbEngineVersionsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersions` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
    },
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersionsResponseDBEngineVersions` `ValidUpgradeTarget`

    The version of the database engine that a DB instance can be upgraded to.

    - **Engine** *(string) --*

      The name of the upgrade target database engine.

    - **EngineVersion** *(string) --*

      The version number of the upgrade target database engine.

    - **Description** *(string) --*

      The version of the database engine that a DB instance can be upgraded to.

    - **AutoUpgrade** *(boolean) --*

      A value that indicates whether the target version is applied to any source DB
      instances that have ``AutoMinorVersionUpgrade`` set to ``true`` .

    - **IsMajorVersionUpgrade** *(boolean) --*

      A value that indicates whether a database engine is upgraded to a major version.
    """


_ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "ValidUpgradeTarget": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsValidUpgradeTargetTypeDef
        ],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
    },
    total=False,
)


class ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef(
    _ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersionsResponse` `DBEngineVersions`

    Detailed information about a DB engine version.

    - **Engine** *(string) --*

      The name of the database engine.

    - **EngineVersion** *(string) --*

      The version number of the database engine.

    - **DBParameterGroupFamily** *(string) --*

      The name of the DB parameter group family for the database engine.

    - **DBEngineDescription** *(string) --*

      The description of the database engine.

    - **DBEngineVersionDescription** *(string) --*

      The description of the database engine version.

    - **ValidUpgradeTarget** *(list) --*

      A list of engine versions that this database engine version can be upgraded to.

      - *(dict) --*

        The version of the database engine that a DB instance can be upgraded to.

        - **Engine** *(string) --*

          The name of the upgrade target database engine.

        - **EngineVersion** *(string) --*

          The version number of the upgrade target database engine.

        - **Description** *(string) --*

          The version of the database engine that a DB instance can be upgraded to.

        - **AutoUpgrade** *(boolean) --*

          A value that indicates whether the target version is applied to any source DB
          instances that have ``AutoMinorVersionUpgrade`` set to ``true`` .

        - **IsMajorVersionUpgrade** *(boolean) --*

          A value that indicates whether a database engine is upgraded to a major version.

    - **ExportableLogTypes** *(list) --*

      The types of logs that the database engine has available for export to Amazon CloudWatch
      Logs.

      - *(string) --*

    - **SupportsLogExportsToCloudwatchLogs** *(boolean) --*

      A value that indicates whether the engine version supports exporting the log types
      specified by ``ExportableLogTypes`` to CloudWatch Logs.
    """


_ClientDescribeDbEngineVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeDbEngineVersionsResponseTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List[
            ClientDescribeDbEngineVersionsResponseDBEngineVersionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbEngineVersionsResponseTypeDef(
    _ClientDescribeDbEngineVersionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbEngineVersions` `Response`

    Represents the output of  DescribeDBEngineVersions .

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **DBEngineVersions** *(list) --*

      Detailed information about one or more DB engine versions.

      - *(dict) --*

        Detailed information about a DB engine version.

        - **Engine** *(string) --*

          The name of the database engine.

        - **EngineVersion** *(string) --*

          The version number of the database engine.

        - **DBParameterGroupFamily** *(string) --*

          The name of the DB parameter group family for the database engine.

        - **DBEngineDescription** *(string) --*

          The description of the database engine.

        - **DBEngineVersionDescription** *(string) --*

          The description of the database engine version.

        - **ValidUpgradeTarget** *(list) --*

          A list of engine versions that this database engine version can be upgraded to.

          - *(dict) --*

            The version of the database engine that a DB instance can be upgraded to.

            - **Engine** *(string) --*

              The name of the upgrade target database engine.

            - **EngineVersion** *(string) --*

              The version number of the upgrade target database engine.

            - **Description** *(string) --*

              The version of the database engine that a DB instance can be upgraded to.

            - **AutoUpgrade** *(boolean) --*

              A value that indicates whether the target version is applied to any source DB
              instances that have ``AutoMinorVersionUpgrade`` set to ``true`` .

            - **IsMajorVersionUpgrade** *(boolean) --*

              A value that indicates whether a database engine is upgraded to a major version.

        - **ExportableLogTypes** *(list) --*

          The types of logs that the database engine has available for export to Amazon CloudWatch
          Logs.

          - *(string) --*

        - **SupportsLogExportsToCloudwatchLogs** *(boolean) --*

          A value that indicates whether the engine version supports exporting the log types
          specified by ``ExportableLogTypes`` to CloudWatch Logs.
    """


_ClientDescribeDbInstancesFiltersTypeDef = TypedDict(
    "_ClientDescribeDbInstancesFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeDbInstancesFiltersTypeDef(_ClientDescribeDbInstancesFiltersTypeDef):
    """
    Type definition for `ClientDescribeDbInstances` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the Availability Zone for the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroup` `Subnets`

    Detailed information about a subnet.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the Availability Zone for the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `DBSubnetGroup`

    Specifies information on the subnet group that is associated with the DB instance,
    including the name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Detailed information about one or more subnets within a DB subnet group.

      - *(dict) --*

        Detailed information about a subnet.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the Availability Zone for the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValues` `PendingCloudwatchLogsExports`

    A list of the log types whose configuration is still pending. These log types are in
    the process of being activated or deactivated.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to Amazon CloudWatch Logs.

      - *(string) --*
    """


_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is included only when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
      is currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently in-progress change of the master credentials for the
      DB instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` , ``bring-your-own-license`` ,
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
      is currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the certificate authority (CA) certificate for the DB
      instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      A list of the log types whose configuration is still pending. These log types are in
      the process of being activated or deactivated.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to Amazon CloudWatch Logs.

        - *(string) --*
    """


_ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "``read replication`` ."

    - **Normal** *(boolean) --*

      A Boolean value that is ``true`` if the instance is operating normally, or ``false``
      if the instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a ``StatusType`` of read replica, the values can be
      ``replicating`` , error, ``stopped`` , or ``terminated`` .

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponseDBInstances` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientDescribeDbInstancesResponseDBInstancesTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseDBInstancesTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientDescribeDbInstancesResponseDBInstancesEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[
            ClientDescribeDbInstancesResponseDBInstancesVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientDescribeDbInstancesResponseDBInstancesDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeDbInstancesResponseDBInstancesPendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[
            ClientDescribeDbInstancesResponseDBInstancesStatusInfosTypeDef
        ],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientDescribeDbInstancesResponseDBInstancesTypeDef(
    _ClientDescribeDbInstancesResponseDBInstancesTypeDef
):
    """
    Type definition for `ClientDescribeDbInstancesResponse` `DBInstances`

    Detailed information about a DB instance.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-provided database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time that the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone that the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group that is associated with the DB instance,
      including the name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Detailed information about one or more subnets within a DB subnet group.

        - *(dict) --*

          Detailed information about a subnet.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the Availability Zone for the subnet.

            - **Name** *(string) --*

              The name of the Availability Zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is included only when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
        is currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently in-progress change of the master credentials for the
        DB instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` , ``bring-your-own-license`` ,
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
        is currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the certificate authority (CA) certificate for the DB
        instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        A list of the log types whose configuration is still pending. These log types are in
        the process of being activated or deactivated.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to Amazon CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **PubliclyAccessible** *(boolean) --*

      Not supported. Amazon DocumentDB does not currently support public endpoints. The value
      of ``PubliclyAccessible`` is always ``false`` .

    - **StatusInfos** *(list) --*

      The status of a read replica. If the instance is not a read replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "``read replication`` ."

        - **Normal** *(boolean) --*

          A Boolean value that is ``true`` if the instance is operating normally, or ``false``
          if the instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a ``StatusType`` of read replica, the values can be
          ``replicating`` , error, ``stopped`` , or ``terminated`` .

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **DBClusterIdentifier** *(string) --*

      Contains the name of the DB cluster that the DB instance is a member of if the DB
      instance is a member of a DB cluster.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether or not the DB instance is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      instance.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
      primary instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to Amazon CloudWatch
      Logs.

      - *(string) --*
    """


_ClientDescribeDbInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeDbInstancesResponseTypeDef",
    {
        "Marker": str,
        "DBInstances": List[ClientDescribeDbInstancesResponseDBInstancesTypeDef],
    },
    total=False,
)


class ClientDescribeDbInstancesResponseTypeDef(
    _ClientDescribeDbInstancesResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbInstances` `Response`

    Represents the output of  DescribeDBInstances .

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **DBInstances** *(list) --*

      Detailed information about one or more DB instances.

      - *(dict) --*

        Detailed information about a DB instance.

        - **DBInstanceIdentifier** *(string) --*

          Contains a user-provided database identifier. This identifier is the unique key that
          identifies a DB instance.

        - **DBInstanceClass** *(string) --*

          Contains the name of the compute and memory capacity class of the DB instance.

        - **Engine** *(string) --*

          Provides the name of the database engine to be used for this DB instance.

        - **DBInstanceStatus** *(string) --*

          Specifies the current state of this database.

        - **Endpoint** *(dict) --*

          Specifies the connection endpoint.

          - **Address** *(string) --*

            Specifies the DNS address of the DB instance.

          - **Port** *(integer) --*

            Specifies the port that the database engine is listening on.

          - **HostedZoneId** *(string) --*

            Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

        - **InstanceCreateTime** *(datetime) --*

          Provides the date and time that the DB instance was created.

        - **PreferredBackupWindow** *(string) --*

          Specifies the daily time range during which automated backups are created if automated
          backups are enabled, as determined by the ``BackupRetentionPeriod`` .

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the number of days for which automatic DB snapshots are retained.

        - **VpcSecurityGroups** *(list) --*

          Provides a list of VPC security group elements that the DB instance belongs to.

          - *(dict) --*

            Used as a response element for queries on virtual private cloud (VPC) security group
            membership.

            - **VpcSecurityGroupId** *(string) --*

              The name of the VPC security group.

            - **Status** *(string) --*

              The status of the VPC security group.

        - **AvailabilityZone** *(string) --*

          Specifies the name of the Availability Zone that the DB instance is located in.

        - **DBSubnetGroup** *(dict) --*

          Specifies information on the subnet group that is associated with the DB instance,
          including the name, description, and subnets in the subnet group.

          - **DBSubnetGroupName** *(string) --*

            The name of the DB subnet group.

          - **DBSubnetGroupDescription** *(string) --*

            Provides the description of the DB subnet group.

          - **VpcId** *(string) --*

            Provides the virtual private cloud (VPC) ID of the DB subnet group.

          - **SubnetGroupStatus** *(string) --*

            Provides the status of the DB subnet group.

          - **Subnets** *(list) --*

            Detailed information about one or more subnets within a DB subnet group.

            - *(dict) --*

              Detailed information about a subnet.

              - **SubnetIdentifier** *(string) --*

                Specifies the identifier of the subnet.

              - **SubnetAvailabilityZone** *(dict) --*

                Specifies the Availability Zone for the subnet.

                - **Name** *(string) --*

                  The name of the Availability Zone.

              - **SubnetStatus** *(string) --*

                Specifies the status of the subnet.

          - **DBSubnetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) for the DB subnet group.

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which system maintenance can occur, in Universal
          Coordinated Time (UTC).

        - **PendingModifiedValues** *(dict) --*

          Specifies that changes to the DB instance are pending. This element is included only when
          changes are pending. Specific changes are identified by subelements.

          - **DBInstanceClass** *(string) --*

            Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
            currently being applied.

          - **AllocatedStorage** *(integer) --*

            Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
            is currently being applied.

          - **MasterUserPassword** *(string) --*

            Contains the pending or currently in-progress change of the master credentials for the
            DB instance.

          - **Port** *(integer) --*

            Specifies the pending port for the DB instance.

          - **BackupRetentionPeriod** *(integer) --*

            Specifies the pending number of days for which automated backups are retained.

          - **MultiAZ** *(boolean) --*

            Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

          - **EngineVersion** *(string) --*

            Indicates the database engine version.

          - **LicenseModel** *(string) --*

            The license model for the DB instance.

            Valid values: ``license-included`` , ``bring-your-own-license`` ,
            ``general-public-license``

          - **Iops** *(integer) --*

            Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
            currently being applied.

          - **DBInstanceIdentifier** *(string) --*

            Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
            is currently being applied.

          - **StorageType** *(string) --*

            Specifies the storage type to be associated with the DB instance.

          - **CACertificateIdentifier** *(string) --*

            Specifies the identifier of the certificate authority (CA) certificate for the DB
            instance.

          - **DBSubnetGroupName** *(string) --*

            The new DB subnet group for the DB instance.

          - **PendingCloudwatchLogsExports** *(dict) --*

            A list of the log types whose configuration is still pending. These log types are in
            the process of being activated or deactivated.

            - **LogTypesToEnable** *(list) --*

              Log types that are in the process of being deactivated. After they are deactivated,
              these log types aren't exported to CloudWatch Logs.

              - *(string) --*

            - **LogTypesToDisable** *(list) --*

              Log types that are in the process of being enabled. After they are enabled, these log
              types are exported to Amazon CloudWatch Logs.

              - *(string) --*

        - **LatestRestorableTime** *(datetime) --*

          Specifies the latest time to which a database can be restored with point-in-time restore.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **AutoMinorVersionUpgrade** *(boolean) --*

          Indicates that minor version patches are applied automatically.

        - **PubliclyAccessible** *(boolean) --*

          Not supported. Amazon DocumentDB does not currently support public endpoints. The value
          of ``PubliclyAccessible`` is always ``false`` .

        - **StatusInfos** *(list) --*

          The status of a read replica. If the instance is not a read replica, this is blank.

          - *(dict) --*

            Provides a list of status information for a DB instance.

            - **StatusType** *(string) --*

              This value is currently "``read replication`` ."

            - **Normal** *(boolean) --*

              A Boolean value that is ``true`` if the instance is operating normally, or ``false``
              if the instance is in an error state.

            - **Status** *(string) --*

              Status of the DB instance. For a ``StatusType`` of read replica, the values can be
              ``replicating`` , error, ``stopped`` , or ``terminated`` .

            - **Message** *(string) --*

              Details of the error if there is an error for the instance. If the instance is not in
              an error state, this value is blank.

        - **DBClusterIdentifier** *(string) --*

          Contains the name of the DB cluster that the DB instance is a member of if the DB
          instance is a member of a DB cluster.

        - **StorageEncrypted** *(boolean) --*

          Specifies whether or not the DB instance is encrypted.

        - **KmsKeyId** *(string) --*

          If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
          instance.

        - **DbiResourceId** *(string) --*

          The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
          in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

        - **CACertificateIdentifier** *(string) --*

          The identifier of the CA certificate for this DB instance.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
          primary instance after a failure of the existing primary instance.

        - **DBInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB instance.

        - **EnabledCloudwatchLogsExports** *(list) --*

          A list of log types that this DB instance is configured to export to Amazon CloudWatch
          Logs.

          - *(string) --*
    """


_ClientDescribeDbSubnetGroupsFiltersTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeDbSubnetGroupsFiltersTypeDef(
    _ClientDescribeDbSubnetGroupsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeDbSubnetGroups` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnets` `SubnetAvailabilityZone`

    Specifies the Availability Zone for the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef(
    _ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef
):
    """
    Type definition for `ClientDescribeDbSubnetGroupsResponseDBSubnetGroups` `Subnets`

    Detailed information about a subnet.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the Availability Zone for the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef(
    _ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef
):
    """
    Type definition for `ClientDescribeDbSubnetGroupsResponse` `DBSubnetGroups`

    Detailed information about a DB subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Detailed information about one or more subnets within a DB subnet group.

      - *(dict) --*

        Detailed information about a subnet.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the Availability Zone for the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientDescribeDbSubnetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeDbSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List[
            ClientDescribeDbSubnetGroupsResponseDBSubnetGroupsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDbSubnetGroupsResponseTypeDef(
    _ClientDescribeDbSubnetGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDbSubnetGroups` `Response`

    Represents the output of  DescribeDBSubnetGroups .

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **DBSubnetGroups** *(list) --*

      Detailed information about one or more DB subnet groups.

      - *(dict) --*

        Detailed information about a DB subnet group.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the virtual private cloud (VPC) ID of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Detailed information about one or more subnets within a DB subnet group.

          - *(dict) --*

            Detailed information about a subnet.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the Availability Zone for the subnet.

              - **Name** *(string) --*

                The name of the Availability Zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientDescribeEngineDefaultClusterParametersFiltersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeEngineDefaultClusterParametersFiltersTypeDef(
    _ClientDescribeEngineDefaultClusterParametersFiltersTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultClusterParameters` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef(
    _ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultClusterParametersResponseEngineDefaults` `Parameters`

    Detailed information about an individual parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine-specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being
      changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List[
            ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsParametersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef(
    _ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultClusterParametersResponse` `EngineDefaults`

    Contains the result of a successful invocation of the
    ``DescribeEngineDefaultClusterParameters`` operation.

    - **DBParameterGroupFamily** *(string) --*

      The name of the DB cluster parameter group family to return the engine parameter
      information for.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is
      specified, the response includes only records beyond the marker, up to the value specified
      by ``MaxRecords`` .

    - **Parameters** *(list) --*

      The parameters of a particular DB cluster parameter group family.

      - *(dict) --*

        Detailed information about an individual parameter.

        - **ParameterName** *(string) --*

          Specifies the name of the parameter.

        - **ParameterValue** *(string) --*

          Specifies the value of the parameter.

        - **Description** *(string) --*

          Provides a description of the parameter.

        - **Source** *(string) --*

          Indicates the source of the parameter value.

        - **ApplyType** *(string) --*

          Specifies the engine-specific parameters type.

        - **DataType** *(string) --*

          Specifies the valid data type for the parameter.

        - **AllowedValues** *(string) --*

          Specifies the valid range of values for the parameter.

        - **IsModifiable** *(boolean) --*

          Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
          parameters have security or operational implications that prevent them from being
          changed.

        - **MinimumEngineVersion** *(string) --*

          The earliest engine version to which the parameter can apply.

        - **ApplyMethod** *(string) --*

          Indicates when to apply parameter updates.
    """


_ClientDescribeEngineDefaultClusterParametersResponseTypeDef = TypedDict(
    "_ClientDescribeEngineDefaultClusterParametersResponseTypeDef",
    {
        "EngineDefaults": ClientDescribeEngineDefaultClusterParametersResponseEngineDefaultsTypeDef
    },
    total=False,
)


class ClientDescribeEngineDefaultClusterParametersResponseTypeDef(
    _ClientDescribeEngineDefaultClusterParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeEngineDefaultClusterParameters` `Response`

    - **EngineDefaults** *(dict) --*

      Contains the result of a successful invocation of the
      ``DescribeEngineDefaultClusterParameters`` operation.

      - **DBParameterGroupFamily** *(string) --*

        The name of the DB cluster parameter group family to return the engine parameter
        information for.

      - **Marker** *(string) --*

        An optional pagination token provided by a previous request. If this parameter is
        specified, the response includes only records beyond the marker, up to the value specified
        by ``MaxRecords`` .

      - **Parameters** *(list) --*

        The parameters of a particular DB cluster parameter group family.

        - *(dict) --*

          Detailed information about an individual parameter.

          - **ParameterName** *(string) --*

            Specifies the name of the parameter.

          - **ParameterValue** *(string) --*

            Specifies the value of the parameter.

          - **Description** *(string) --*

            Provides a description of the parameter.

          - **Source** *(string) --*

            Indicates the source of the parameter value.

          - **ApplyType** *(string) --*

            Specifies the engine-specific parameters type.

          - **DataType** *(string) --*

            Specifies the valid data type for the parameter.

          - **AllowedValues** *(string) --*

            Specifies the valid range of values for the parameter.

          - **IsModifiable** *(boolean) --*

            Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
            parameters have security or operational implications that prevent them from being
            changed.

          - **MinimumEngineVersion** *(string) --*

            The earliest engine version to which the parameter can apply.

          - **ApplyMethod** *(string) --*

            Indicates when to apply parameter updates.
    """


_ClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeEventCategoriesFiltersTypeDef(
    _ClientDescribeEventCategoriesFiltersTypeDef
):
    """
    Type definition for `ClientDescribeEventCategories` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef",
    {"SourceType": str, "EventCategories": List[str]},
    total=False,
)


class ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef(
    _ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef
):
    """
    Type definition for `ClientDescribeEventCategoriesResponse` `EventCategoriesMapList`

    An event source type, accompanied by one or more event category names.

    - **SourceType** *(string) --*

      The source type that the returned categories belong to.

    - **EventCategories** *(list) --*

      The event categories for the specified source type.

      - *(string) --*
    """


_ClientDescribeEventCategoriesResponseTypeDef = TypedDict(
    "_ClientDescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoriesMapList": List[
            ClientDescribeEventCategoriesResponseEventCategoriesMapListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeEventCategoriesResponseTypeDef(
    _ClientDescribeEventCategoriesResponseTypeDef
):
    """
    Type definition for `ClientDescribeEventCategories` `Response`

    Represents the output of  DescribeEventCategories .

    - **EventCategoriesMapList** *(list) --*

      A list of event category maps.

      - *(dict) --*

        An event source type, accompanied by one or more event category names.

        - **SourceType** *(string) --*

          The source type that the returned categories belong to.

        - **EventCategories** *(list) --*

          The event categories for the specified source type.

          - *(string) --*
    """


_ClientDescribeEventsFiltersTypeDef = TypedDict(
    "_ClientDescribeEventsFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientDescribeEventsFiltersTypeDef(_ClientDescribeEventsFiltersTypeDef):
    """
    Type definition for `ClientDescribeEvents` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)


class ClientDescribeEventsResponseEventsTypeDef(
    _ClientDescribeEventsResponseEventsTypeDef
):
    """
    Type definition for `ClientDescribeEventsResponse` `Events`

    Detailed information about an event.

    - **SourceIdentifier** *(string) --*

      Provides the identifier for the source of the event.

    - **SourceType** *(string) --*

      Specifies the source type for this event.

    - **Message** *(string) --*

      Provides the text of this event.

    - **EventCategories** *(list) --*

      Specifies the category for the event.

      - *(string) --*

    - **Date** *(datetime) --*

      Specifies the date and time of the event.

    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) for the event.
    """


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    Type definition for `ClientDescribeEvents` `Response`

    Represents the output of  DescribeEvents .

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .

    - **Events** *(list) --*

      Detailed information about one or more events.

      - *(dict) --*

        Detailed information about an event.

        - **SourceIdentifier** *(string) --*

          Provides the identifier for the source of the event.

        - **SourceType** *(string) --*

          Specifies the source type for this event.

        - **Message** *(string) --*

          Provides the text of this event.

        - **EventCategories** *(list) --*

          Specifies the category for the event.

          - *(string) --*

        - **Date** *(datetime) --*

          Specifies the date and time of the event.

        - **SourceArn** *(string) --*

          The Amazon Resource Name (ARN) for the event.
    """


_ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsFiltersTypeDef
):
    """
    Type definition for `ClientDescribeOrderableDbInstanceOptions` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
):
    """
    Type definition for `ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptions` `AvailabilityZones`

    Information about an Availability Zone.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List[
            ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
        ],
        "Vpc": bool,
    },
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef
):
    """
    Type definition for `ClientDescribeOrderableDbInstanceOptionsResponse` `OrderableDBInstanceOptions`

    The options that are available for a DB instance.

    - **Engine** *(string) --*

      The engine type of a DB instance.

    - **EngineVersion** *(string) --*

      The engine version of a DB instance.

    - **DBInstanceClass** *(string) --*

      The DB instance class for a DB instance.

    - **LicenseModel** *(string) --*

      The license model for a DB instance.

    - **AvailabilityZones** *(list) --*

      A list of Availability Zones for a DB instance.

      - *(dict) --*

        Information about an Availability Zone.

        - **Name** *(string) --*

          The name of the Availability Zone.

    - **Vpc** *(boolean) --*

      Indicates whether a DB instance is in a virtual private cloud (VPC).
    """


_ClientDescribeOrderableDbInstanceOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeOrderableDbInstanceOptionsResponseTypeDef",
    {
        "OrderableDBInstanceOptions": List[
            ClientDescribeOrderableDbInstanceOptionsResponseOrderableDBInstanceOptionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeOrderableDbInstanceOptionsResponseTypeDef(
    _ClientDescribeOrderableDbInstanceOptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeOrderableDbInstanceOptions` `Response`

    Represents the output of  DescribeOrderableDBInstanceOptions .

    - **OrderableDBInstanceOptions** *(list) --*

      The options that are available for a particular orderable DB instance.

      - *(dict) --*

        The options that are available for a DB instance.

        - **Engine** *(string) --*

          The engine type of a DB instance.

        - **EngineVersion** *(string) --*

          The engine version of a DB instance.

        - **DBInstanceClass** *(string) --*

          The DB instance class for a DB instance.

        - **LicenseModel** *(string) --*

          The license model for a DB instance.

        - **AvailabilityZones** *(list) --*

          A list of Availability Zones for a DB instance.

          - *(dict) --*

            Information about an Availability Zone.

            - **Name** *(string) --*

              The name of the Availability Zone.

        - **Vpc** *(boolean) --*

          Indicates whether a DB instance is in a virtual private cloud (VPC).

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .
    """


_ClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class ClientDescribePendingMaintenanceActionsFiltersTypeDef(
    _ClientDescribePendingMaintenanceActionsFiltersTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActions` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef(
    _ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActions` `PendingMaintenanceActionDetails`

    Provides information about a pending maintenance action for a resource.

    - **Action** *(string) --*

      The type of pending maintenance action that is available for the resource.

    - **AutoAppliedAfterDate** *(datetime) --*

      The date of the maintenance window when the action is applied. The maintenance action
      is applied to the resource during its first maintenance window after this date. If
      this date is specified, any ``next-maintenance`` opt-in requests are ignored.

    - **ForcedApplyDate** *(datetime) --*

      The date when the maintenance action is automatically applied. The maintenance action
      is applied to the resource on this date regardless of the maintenance window for the
      resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

    - **OptInStatus** *(string) --*

      Indicates the type of opt-in request that has been received for the resource.

    - **CurrentApplyDate** *(datetime) --*

      The effective date when the pending maintenance action is applied to the resource.

    - **Description** *(string) --*

      A description providing more detail about the maintenance action.
    """


_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef(
    _ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActionsResponse` `PendingMaintenanceActions`

    Represents the output of  ApplyPendingMaintenanceAction .

    - **ResourceIdentifier** *(string) --*

      The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.

    - **PendingMaintenanceActionDetails** *(list) --*

      A list that provides details about the pending maintenance actions for the resource.

      - *(dict) --*

        Provides information about a pending maintenance action for a resource.

        - **Action** *(string) --*

          The type of pending maintenance action that is available for the resource.

        - **AutoAppliedAfterDate** *(datetime) --*

          The date of the maintenance window when the action is applied. The maintenance action
          is applied to the resource during its first maintenance window after this date. If
          this date is specified, any ``next-maintenance`` opt-in requests are ignored.

        - **ForcedApplyDate** *(datetime) --*

          The date when the maintenance action is automatically applied. The maintenance action
          is applied to the resource on this date regardless of the maintenance window for the
          resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

        - **OptInStatus** *(string) --*

          Indicates the type of opt-in request that has been received for the resource.

        - **CurrentApplyDate** *(datetime) --*

          The effective date when the pending maintenance action is applied to the resource.

        - **Description** *(string) --*

          A description providing more detail about the maintenance action.
    """


_ClientDescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "_ClientDescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribePendingMaintenanceActionsResponseTypeDef(
    _ClientDescribePendingMaintenanceActionsResponseTypeDef
):
    """
    Type definition for `ClientDescribePendingMaintenanceActions` `Response`

    Represents the output of  DescribePendingMaintenanceActions .

    - **PendingMaintenanceActions** *(list) --*

      The maintenance actions to be applied.

      - *(dict) --*

        Represents the output of  ApplyPendingMaintenanceAction .

        - **ResourceIdentifier** *(string) --*

          The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.

        - **PendingMaintenanceActionDetails** *(list) --*

          A list that provides details about the pending maintenance actions for the resource.

          - *(dict) --*

            Provides information about a pending maintenance action for a resource.

            - **Action** *(string) --*

              The type of pending maintenance action that is available for the resource.

            - **AutoAppliedAfterDate** *(datetime) --*

              The date of the maintenance window when the action is applied. The maintenance action
              is applied to the resource during its first maintenance window after this date. If
              this date is specified, any ``next-maintenance`` opt-in requests are ignored.

            - **ForcedApplyDate** *(datetime) --*

              The date when the maintenance action is automatically applied. The maintenance action
              is applied to the resource on this date regardless of the maintenance window for the
              resource. If this date is specified, any ``immediate`` opt-in requests are ignored.

            - **OptInStatus** *(string) --*

              Indicates the type of opt-in request that has been received for the resource.

            - **CurrentApplyDate** *(datetime) --*

              The effective date when the pending maintenance action is applied to the resource.

            - **Description** *(string) --*

              A description providing more detail about the maintenance action.

    - **Marker** *(string) --*

      An optional pagination token provided by a previous request. If this parameter is specified,
      the response includes only records beyond the marker, up to the value specified by
      ``MaxRecords`` .
    """


_ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientFailoverDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      ``Status`` property returns one of the following values:

      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
      cannot assume the IAM role to access other AWS services on your behalf.
    """


_ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientFailoverDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      A value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to
      the primary instance after a failure of the existing primary instance.
    """


_ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientFailoverDbClusterResponseDBCluster` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientFailoverDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientFailoverDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientFailoverDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientFailoverDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientFailoverDbClusterResponseDBClusterTypeDef(
    _ClientFailoverDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientFailoverDbClusterResponse` `DBCluster`

    Detailed information about a DB cluster.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
      created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group that is associated with the DB cluster, including
      the name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      The earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
      connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
      clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
      connection requests among the Amazon DocumentDB replicas in the DB cluster. This
      functionality can help balance your read workload across multiple Amazon DocumentDB
      replicas in your DB cluster.

      If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
      promoted to be the primary instance, your connection is dropped. To continue sending your
      read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
      the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master user name for the DB cluster.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          A value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to
          the primary instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
      to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          ``Status`` property returns one of the following values:

          * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
          cannot assume the IAM role to access other AWS services on your behalf.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

      - *(string) --*

    - **DeletionProtection** *(boolean) --*

      Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
      cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
      ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientFailoverDbClusterResponseTypeDef = TypedDict(
    "_ClientFailoverDbClusterResponseTypeDef",
    {"DBCluster": ClientFailoverDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientFailoverDbClusterResponseTypeDef(_ClientFailoverDbClusterResponseTypeDef):
    """
    Type definition for `ClientFailoverDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group that is associated with the DB cluster, including
        the name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        The earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
        connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
        clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
        connection requests among the Amazon DocumentDB replicas in the DB cluster. This
        functionality can help balance your read workload across multiple Amazon DocumentDB
        replicas in your DB cluster.

        If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
        promoted to be the primary instance, your connection is dropped. To continue sending your
        read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
        the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master user name for the DB cluster.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            A value that is ``true`` if the cluster member is the primary instance for the DB
            cluster and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which an Amazon DocumentDB replica is promoted to
            the primary instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
        to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The
            ``Status`` property returns one of the following values:

            * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
            cannot assume the IAM role to access other AWS services on your behalf.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

        - *(string) --*

      - **DeletionProtection** *(boolean) --*

        Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
        cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
        ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientListTagsForResourceFiltersTypeDef = TypedDict(
    "_ClientListTagsForResourceFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class ClientListTagsForResourceFiltersTypeDef(_ClientListTagsForResourceFiltersTypeDef):
    """
    Type definition for `ClientListTagsForResource` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagListTypeDef(
    _ClientListTagsForResourceResponseTagListTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `TagList`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set
      of Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters
      in length and can't be prefixed with "aws:" or "rds:". The string can contain only the
      set of Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    Represents the output of  ListTagsForResource .

    - **TagList** *(list) --*

      A list of one or more tags.

      - *(dict) --*

        Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

        - **Key** *(string) --*

          The required name of the tag. The string value can be from 1 to 128 Unicode characters in
          length and can't be prefixed with "aws:" or "rds:". The string can contain only the set
          of Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
          "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        - **Value** *(string) --*

          The optional value of the tag. The string value can be from 1 to 256 Unicode characters
          in length and can't be prefixed with "aws:" or "rds:". The string can contain only the
          set of Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
          "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "_ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef",
    {"EnableLogTypes": List[str], "DisableLogTypes": List[str]},
    total=False,
)


class ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef(
    _ClientModifyDbClusterCloudwatchLogsExportConfigurationTypeDef
):
    """
    Type definition for `ClientModifyDbCluster` `CloudwatchLogsExportConfiguration`

    The configuration setting for the log types to be enabled for export to Amazon CloudWatch Logs
    for a specific DB instance or DB cluster. The ``EnableLogTypes`` and ``DisableLogTypes`` arrays
    determine which logs are exported (or not exported) to CloudWatch Logs.

    - **EnableLogTypes** *(list) --*

      The list of log types to enable.

      - *(string) --*

    - **DisableLogTypes** *(list) --*

      The list of log types to disable.

      - *(string) --*
    """


_ClientModifyDbClusterParameterGroupParametersTypeDef = TypedDict(
    "_ClientModifyDbClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientModifyDbClusterParameterGroupParametersTypeDef(
    _ClientModifyDbClusterParameterGroupParametersTypeDef
):
    """
    Type definition for `ClientModifyDbClusterParameterGroup` `Parameters`

    Detailed information about an individual parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine-specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientModifyDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientModifyDbClusterParameterGroupResponseTypeDef",
    {"DBClusterParameterGroupName": str},
    total=False,
)


class ClientModifyDbClusterParameterGroupResponseTypeDef(
    _ClientModifyDbClusterParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientModifyDbClusterParameterGroup` `Response`

    Contains the name of a DB cluster parameter group.

    - **DBClusterParameterGroupName** *(string) --*

      The name of a DB cluster parameter group.

      Constraints:

      * Must be from 1 to 255 letters or numbers.

      * The first character must be a letter.

      * Cannot end with a hyphen or contain two consecutive hyphens.

      .. note::

        This value is stored as a lowercase string.
    """


_ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientModifyDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      ``Status`` property returns one of the following values:

      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
      cannot assume the IAM role to access other AWS services on your behalf.
    """


_ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientModifyDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      A value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to
      the primary instance after a failure of the existing primary instance.
    """


_ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientModifyDbClusterResponseDBCluster` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientModifyDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientModifyDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientModifyDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientModifyDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientModifyDbClusterResponseDBClusterTypeDef(
    _ClientModifyDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientModifyDbClusterResponse` `DBCluster`

    Detailed information about a DB cluster.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
      created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group that is associated with the DB cluster, including
      the name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      The earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
      connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
      clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
      connection requests among the Amazon DocumentDB replicas in the DB cluster. This
      functionality can help balance your read workload across multiple Amazon DocumentDB
      replicas in your DB cluster.

      If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
      promoted to be the primary instance, your connection is dropped. To continue sending your
      read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
      the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master user name for the DB cluster.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          A value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to
          the primary instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
      to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          ``Status`` property returns one of the following values:

          * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
          cannot assume the IAM role to access other AWS services on your behalf.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

      - *(string) --*

    - **DeletionProtection** *(boolean) --*

      Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
      cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
      ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientModifyDbClusterResponseTypeDef = TypedDict(
    "_ClientModifyDbClusterResponseTypeDef",
    {"DBCluster": ClientModifyDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientModifyDbClusterResponseTypeDef(_ClientModifyDbClusterResponseTypeDef):
    """
    Type definition for `ClientModifyDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group that is associated with the DB cluster, including
        the name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        The earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
        connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
        clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
        connection requests among the Amazon DocumentDB replicas in the DB cluster. This
        functionality can help balance your read workload across multiple Amazon DocumentDB
        replicas in your DB cluster.

        If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
        promoted to be the primary instance, your connection is dropped. To continue sending your
        read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
        the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master user name for the DB cluster.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            A value that is ``true`` if the cluster member is the primary instance for the DB
            cluster and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which an Amazon DocumentDB replica is promoted to
            the primary instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
        to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The
            ``Status`` property returns one of the following values:

            * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
            cannot assume the IAM role to access other AWS services on your behalf.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

        - *(string) --*

      - **DeletionProtection** *(boolean) --*

        Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
        cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
        ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef = TypedDict(
    "_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef",
    {"AttributeName": str, "AttributeValues": List[str]},
    total=False,
)


class ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef(
    _ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
):
    """
    Type definition for `ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResult` `DBClusterSnapshotAttributes`

    Contains the name and values of a manual DB cluster snapshot attribute.

    Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
    a manual DB cluster snapshot.

    - **AttributeName** *(string) --*

      The name of the manual DB cluster snapshot attribute.

      The attribute named ``restore`` refers to the list of AWS accounts that have permission
      to copy or restore the manual DB cluster snapshot.

    - **AttributeValues** *(list) --*

      The values for the manual DB cluster snapshot attribute.

      If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
      of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
      snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
      public and available for any AWS account to copy or restore.

      - *(string) --*
    """


_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "_ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List[
            ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultDBClusterSnapshotAttributesTypeDef
        ],
    },
    total=False,
)


class ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef(
    _ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef
):
    """
    Type definition for `ClientModifyDbClusterSnapshotAttributeResponse` `DBClusterSnapshotAttributesResult`

    Detailed information about the attributes that are associated with a DB cluster snapshot.

    - **DBClusterSnapshotIdentifier** *(string) --*

      The identifier of the DB cluster snapshot that the attributes apply to.

    - **DBClusterSnapshotAttributes** *(list) --*

      The list of attributes and values for the DB cluster snapshot.

      - *(dict) --*

        Contains the name and values of a manual DB cluster snapshot attribute.

        Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
        a manual DB cluster snapshot.

        - **AttributeName** *(string) --*

          The name of the manual DB cluster snapshot attribute.

          The attribute named ``restore`` refers to the list of AWS accounts that have permission
          to copy or restore the manual DB cluster snapshot.

        - **AttributeValues** *(list) --*

          The values for the manual DB cluster snapshot attribute.

          If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
          of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
          snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
          public and available for any AWS account to copy or restore.

          - *(string) --*
    """


_ClientModifyDbClusterSnapshotAttributeResponseTypeDef = TypedDict(
    "_ClientModifyDbClusterSnapshotAttributeResponseTypeDef",
    {
        "DBClusterSnapshotAttributesResult": ClientModifyDbClusterSnapshotAttributeResponseDBClusterSnapshotAttributesResultTypeDef
    },
    total=False,
)


class ClientModifyDbClusterSnapshotAttributeResponseTypeDef(
    _ClientModifyDbClusterSnapshotAttributeResponseTypeDef
):
    """
    Type definition for `ClientModifyDbClusterSnapshotAttribute` `Response`

    - **DBClusterSnapshotAttributesResult** *(dict) --*

      Detailed information about the attributes that are associated with a DB cluster snapshot.

      - **DBClusterSnapshotIdentifier** *(string) --*

        The identifier of the DB cluster snapshot that the attributes apply to.

      - **DBClusterSnapshotAttributes** *(list) --*

        The list of attributes and values for the DB cluster snapshot.

        - *(dict) --*

          Contains the name and values of a manual DB cluster snapshot attribute.

          Manual DB cluster snapshot attributes are used to authorize other AWS accounts to restore
          a manual DB cluster snapshot.

          - **AttributeName** *(string) --*

            The name of the manual DB cluster snapshot attribute.

            The attribute named ``restore`` refers to the list of AWS accounts that have permission
            to copy or restore the manual DB cluster snapshot.

          - **AttributeValues** *(list) --*

            The values for the manual DB cluster snapshot attribute.

            If the ``AttributeName`` field is set to ``restore`` , then this element returns a list
            of IDs of the AWS accounts that are authorized to copy or restore the manual DB cluster
            snapshot. If a value of ``all`` is in the list, then the manual DB cluster snapshot is
            public and available for any AWS account to copy or restore.

            - *(string) --*
    """


_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the Availability Zone for the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstanceDBSubnetGroup` `Subnets`

    Detailed information about a subnet.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the Availability Zone for the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `DBSubnetGroup`

    Specifies information on the subnet group that is associated with the DB instance,
    including the name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Detailed information about one or more subnets within a DB subnet group.

      - *(dict) --*

        Detailed information about a subnet.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the Availability Zone for the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstancePendingModifiedValues` `PendingCloudwatchLogsExports`

    A list of the log types whose configuration is still pending. These log types are in the
    process of being activated or deactivated.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to Amazon CloudWatch Logs.

      - *(string) --*
    """


_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is included only when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
      currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently in-progress change of the master credentials for the DB
      instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` , ``bring-your-own-license`` ,
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
      currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the certificate authority (CA) certificate for the DB
      instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      A list of the log types whose configuration is still pending. These log types are in the
      process of being activated or deactivated.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to Amazon CloudWatch Logs.

        - *(string) --*
    """


_ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "``read replication`` ."

    - **Normal** *(boolean) --*

      A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
      the instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a ``StatusType`` of read replica, the values can be
      ``replicating`` , error, ``stopped`` , or ``terminated`` .

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponseDBInstance` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientModifyDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientModifyDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[
            ClientModifyDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientModifyDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientModifyDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientModifyDbInstanceResponseDBInstanceTypeDef(
    _ClientModifyDbInstanceResponseDBInstanceTypeDef
):
    """
    Type definition for `ClientModifyDbInstanceResponse` `DBInstance`

    Detailed information about a DB instance.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-provided database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time that the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone that the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group that is associated with the DB instance,
      including the name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Detailed information about one or more subnets within a DB subnet group.

        - *(dict) --*

          Detailed information about a subnet.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the Availability Zone for the subnet.

            - **Name** *(string) --*

              The name of the Availability Zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is included only when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
        currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently in-progress change of the master credentials for the DB
        instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` , ``bring-your-own-license`` ,
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
        currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the certificate authority (CA) certificate for the DB
        instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        A list of the log types whose configuration is still pending. These log types are in the
        process of being activated or deactivated.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to Amazon CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **PubliclyAccessible** *(boolean) --*

      Not supported. Amazon DocumentDB does not currently support public endpoints. The value of
      ``PubliclyAccessible`` is always ``false`` .

    - **StatusInfos** *(list) --*

      The status of a read replica. If the instance is not a read replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "``read replication`` ."

        - **Normal** *(boolean) --*

          A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
          the instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a ``StatusType`` of read replica, the values can be
          ``replicating`` , error, ``stopped`` , or ``terminated`` .

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **DBClusterIdentifier** *(string) --*

      Contains the name of the DB cluster that the DB instance is a member of if the DB instance
      is a member of a DB cluster.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether or not the DB instance is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      instance.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
      primary instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to Amazon CloudWatch Logs.

      - *(string) --*
    """


_ClientModifyDbInstanceResponseTypeDef = TypedDict(
    "_ClientModifyDbInstanceResponseTypeDef",
    {"DBInstance": ClientModifyDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientModifyDbInstanceResponseTypeDef(_ClientModifyDbInstanceResponseTypeDef):
    """
    Type definition for `ClientModifyDbInstance` `Response`

    - **DBInstance** *(dict) --*

      Detailed information about a DB instance.

      - **DBInstanceIdentifier** *(string) --*

        Contains a user-provided database identifier. This identifier is the unique key that
        identifies a DB instance.

      - **DBInstanceClass** *(string) --*

        Contains the name of the compute and memory capacity class of the DB instance.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB instance.

      - **DBInstanceStatus** *(string) --*

        Specifies the current state of this database.

      - **Endpoint** *(dict) --*

        Specifies the connection endpoint.

        - **Address** *(string) --*

          Specifies the DNS address of the DB instance.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **InstanceCreateTime** *(datetime) --*

        Provides the date and time that the DB instance was created.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security group elements that the DB instance belongs to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **AvailabilityZone** *(string) --*

        Specifies the name of the Availability Zone that the DB instance is located in.

      - **DBSubnetGroup** *(dict) --*

        Specifies information on the subnet group that is associated with the DB instance,
        including the name, description, and subnets in the subnet group.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the virtual private cloud (VPC) ID of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Detailed information about one or more subnets within a DB subnet group.

          - *(dict) --*

            Detailed information about a subnet.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the Availability Zone for the subnet.

              - **Name** *(string) --*

                The name of the Availability Zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **PendingModifiedValues** *(dict) --*

        Specifies that changes to the DB instance are pending. This element is included only when
        changes are pending. Specific changes are identified by subelements.

        - **DBInstanceClass** *(string) --*

          Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
          currently being applied.

        - **AllocatedStorage** *(integer) --*

          Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
          currently being applied.

        - **MasterUserPassword** *(string) --*

          Contains the pending or currently in-progress change of the master credentials for the DB
          instance.

        - **Port** *(integer) --*

          Specifies the pending port for the DB instance.

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the pending number of days for which automated backups are retained.

        - **MultiAZ** *(boolean) --*

          Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LicenseModel** *(string) --*

          The license model for the DB instance.

          Valid values: ``license-included`` , ``bring-your-own-license`` ,
          ``general-public-license``

        - **Iops** *(integer) --*

          Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
          currently being applied.

        - **DBInstanceIdentifier** *(string) --*

          Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
          currently being applied.

        - **StorageType** *(string) --*

          Specifies the storage type to be associated with the DB instance.

        - **CACertificateIdentifier** *(string) --*

          Specifies the identifier of the certificate authority (CA) certificate for the DB
          instance.

        - **DBSubnetGroupName** *(string) --*

          The new DB subnet group for the DB instance.

        - **PendingCloudwatchLogsExports** *(dict) --*

          A list of the log types whose configuration is still pending. These log types are in the
          process of being activated or deactivated.

          - **LogTypesToEnable** *(list) --*

            Log types that are in the process of being deactivated. After they are deactivated,
            these log types aren't exported to CloudWatch Logs.

            - *(string) --*

          - **LogTypesToDisable** *(list) --*

            Log types that are in the process of being enabled. After they are enabled, these log
            types are exported to Amazon CloudWatch Logs.

            - *(string) --*

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Indicates that minor version patches are applied automatically.

      - **PubliclyAccessible** *(boolean) --*

        Not supported. Amazon DocumentDB does not currently support public endpoints. The value of
        ``PubliclyAccessible`` is always ``false`` .

      - **StatusInfos** *(list) --*

        The status of a read replica. If the instance is not a read replica, this is blank.

        - *(dict) --*

          Provides a list of status information for a DB instance.

          - **StatusType** *(string) --*

            This value is currently "``read replication`` ."

          - **Normal** *(boolean) --*

            A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
            the instance is in an error state.

          - **Status** *(string) --*

            Status of the DB instance. For a ``StatusType`` of read replica, the values can be
            ``replicating`` , error, ``stopped`` , or ``terminated`` .

          - **Message** *(string) --*

            Details of the error if there is an error for the instance. If the instance is not in
            an error state, this value is blank.

      - **DBClusterIdentifier** *(string) --*

        Contains the name of the DB cluster that the DB instance is a member of if the DB instance
        is a member of a DB cluster.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether or not the DB instance is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        instance.

      - **DbiResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
        in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

      - **CACertificateIdentifier** *(string) --*

        The identifier of the CA certificate for this DB instance.

      - **PromotionTier** *(integer) --*

        A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
        primary instance after a failure of the existing primary instance.

      - **DBInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB instance.

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB instance is configured to export to Amazon CloudWatch Logs.

        - *(string) --*
    """


_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the Availability Zone for the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef(
    _ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientModifyDbSubnetGroupResponseDBSubnetGroup` `Subnets`

    Detailed information about a subnet.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the Availability Zone for the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[ClientModifyDbSubnetGroupResponseDBSubnetGroupSubnetsTypeDef],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef(
    _ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientModifyDbSubnetGroupResponse` `DBSubnetGroup`

    Detailed information about a DB subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Detailed information about one or more subnets within a DB subnet group.

      - *(dict) --*

        Detailed information about a subnet.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the Availability Zone for the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientModifyDbSubnetGroupResponseTypeDef = TypedDict(
    "_ClientModifyDbSubnetGroupResponseTypeDef",
    {"DBSubnetGroup": ClientModifyDbSubnetGroupResponseDBSubnetGroupTypeDef},
    total=False,
)


class ClientModifyDbSubnetGroupResponseTypeDef(
    _ClientModifyDbSubnetGroupResponseTypeDef
):
    """
    Type definition for `ClientModifyDbSubnetGroup` `Response`

    - **DBSubnetGroup** *(dict) --*

      Detailed information about a DB subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Detailed information about one or more subnets within a DB subnet group.

        - *(dict) --*

          Detailed information about a subnet.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the Availability Zone for the subnet.

            - **Name** *(string) --*

              The name of the Availability Zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the Availability Zone for the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstanceDBSubnetGroup` `Subnets`

    Detailed information about a subnet.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the Availability Zone for the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `DBSubnetGroup`

    Specifies information on the subnet group that is associated with the DB instance,
    including the name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Detailed information about one or more subnets within a DB subnet group.

      - *(dict) --*

        Detailed information about a subnet.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the Availability Zone for the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstancePendingModifiedValues` `PendingCloudwatchLogsExports`

    A list of the log types whose configuration is still pending. These log types are in the
    process of being activated or deactivated.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to Amazon CloudWatch Logs.

      - *(string) --*
    """


_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef(
    _ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is included only when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
      currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently in-progress change of the master credentials for the DB
      instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` , ``bring-your-own-license`` ,
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
      currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the certificate authority (CA) certificate for the DB
      instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      A list of the log types whose configuration is still pending. These log types are in the
      process of being activated or deactivated.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to Amazon CloudWatch Logs.

        - *(string) --*
    """


_ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "``read replication`` ."

    - **Normal** *(boolean) --*

      A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
      the instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a ``StatusType`` of read replica, the values can be
      ``replicating`` , error, ``stopped`` , or ``terminated`` .

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponseDBInstance` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientRebootDbInstanceResponseDBInstanceTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseDBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": ClientRebootDbInstanceResponseDBInstanceEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[
            ClientRebootDbInstanceResponseDBInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": ClientRebootDbInstanceResponseDBInstanceDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootDbInstanceResponseDBInstancePendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[ClientRebootDbInstanceResponseDBInstanceStatusInfosTypeDef],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class ClientRebootDbInstanceResponseDBInstanceTypeDef(
    _ClientRebootDbInstanceResponseDBInstanceTypeDef
):
    """
    Type definition for `ClientRebootDbInstanceResponse` `DBInstance`

    Detailed information about a DB instance.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-provided database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time that the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone that the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group that is associated with the DB instance,
      including the name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Detailed information about one or more subnets within a DB subnet group.

        - *(dict) --*

          Detailed information about a subnet.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the Availability Zone for the subnet.

            - **Name** *(string) --*

              The name of the Availability Zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is included only when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
        currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently in-progress change of the master credentials for the DB
        instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` , ``bring-your-own-license`` ,
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
        currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the certificate authority (CA) certificate for the DB
        instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        A list of the log types whose configuration is still pending. These log types are in the
        process of being activated or deactivated.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to Amazon CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **PubliclyAccessible** *(boolean) --*

      Not supported. Amazon DocumentDB does not currently support public endpoints. The value of
      ``PubliclyAccessible`` is always ``false`` .

    - **StatusInfos** *(list) --*

      The status of a read replica. If the instance is not a read replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "``read replication`` ."

        - **Normal** *(boolean) --*

          A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
          the instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a ``StatusType`` of read replica, the values can be
          ``replicating`` , error, ``stopped`` , or ``terminated`` .

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **DBClusterIdentifier** *(string) --*

      Contains the name of the DB cluster that the DB instance is a member of if the DB instance
      is a member of a DB cluster.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether or not the DB instance is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      instance.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
      primary instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to Amazon CloudWatch Logs.

      - *(string) --*
    """


_ClientRebootDbInstanceResponseTypeDef = TypedDict(
    "_ClientRebootDbInstanceResponseTypeDef",
    {"DBInstance": ClientRebootDbInstanceResponseDBInstanceTypeDef},
    total=False,
)


class ClientRebootDbInstanceResponseTypeDef(_ClientRebootDbInstanceResponseTypeDef):
    """
    Type definition for `ClientRebootDbInstance` `Response`

    - **DBInstance** *(dict) --*

      Detailed information about a DB instance.

      - **DBInstanceIdentifier** *(string) --*

        Contains a user-provided database identifier. This identifier is the unique key that
        identifies a DB instance.

      - **DBInstanceClass** *(string) --*

        Contains the name of the compute and memory capacity class of the DB instance.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB instance.

      - **DBInstanceStatus** *(string) --*

        Specifies the current state of this database.

      - **Endpoint** *(dict) --*

        Specifies the connection endpoint.

        - **Address** *(string) --*

          Specifies the DNS address of the DB instance.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **InstanceCreateTime** *(datetime) --*

        Provides the date and time that the DB instance was created.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of VPC security group elements that the DB instance belongs to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **AvailabilityZone** *(string) --*

        Specifies the name of the Availability Zone that the DB instance is located in.

      - **DBSubnetGroup** *(dict) --*

        Specifies information on the subnet group that is associated with the DB instance,
        including the name, description, and subnets in the subnet group.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the virtual private cloud (VPC) ID of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Detailed information about one or more subnets within a DB subnet group.

          - *(dict) --*

            Detailed information about a subnet.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the Availability Zone for the subnet.

              - **Name** *(string) --*

                The name of the Availability Zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **PendingModifiedValues** *(dict) --*

        Specifies that changes to the DB instance are pending. This element is included only when
        changes are pending. Specific changes are identified by subelements.

        - **DBInstanceClass** *(string) --*

          Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
          currently being applied.

        - **AllocatedStorage** *(integer) --*

          Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or is
          currently being applied.

        - **MasterUserPassword** *(string) --*

          Contains the pending or currently in-progress change of the master credentials for the DB
          instance.

        - **Port** *(integer) --*

          Specifies the pending port for the DB instance.

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the pending number of days for which automated backups are retained.

        - **MultiAZ** *(boolean) --*

          Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LicenseModel** *(string) --*

          The license model for the DB instance.

          Valid values: ``license-included`` , ``bring-your-own-license`` ,
          ``general-public-license``

        - **Iops** *(integer) --*

          Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
          currently being applied.

        - **DBInstanceIdentifier** *(string) --*

          Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or is
          currently being applied.

        - **StorageType** *(string) --*

          Specifies the storage type to be associated with the DB instance.

        - **CACertificateIdentifier** *(string) --*

          Specifies the identifier of the certificate authority (CA) certificate for the DB
          instance.

        - **DBSubnetGroupName** *(string) --*

          The new DB subnet group for the DB instance.

        - **PendingCloudwatchLogsExports** *(dict) --*

          A list of the log types whose configuration is still pending. These log types are in the
          process of being activated or deactivated.

          - **LogTypesToEnable** *(list) --*

            Log types that are in the process of being deactivated. After they are deactivated,
            these log types aren't exported to CloudWatch Logs.

            - *(string) --*

          - **LogTypesToDisable** *(list) --*

            Log types that are in the process of being enabled. After they are enabled, these log
            types are exported to Amazon CloudWatch Logs.

            - *(string) --*

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **AutoMinorVersionUpgrade** *(boolean) --*

        Indicates that minor version patches are applied automatically.

      - **PubliclyAccessible** *(boolean) --*

        Not supported. Amazon DocumentDB does not currently support public endpoints. The value of
        ``PubliclyAccessible`` is always ``false`` .

      - **StatusInfos** *(list) --*

        The status of a read replica. If the instance is not a read replica, this is blank.

        - *(dict) --*

          Provides a list of status information for a DB instance.

          - **StatusType** *(string) --*

            This value is currently "``read replication`` ."

          - **Normal** *(boolean) --*

            A Boolean value that is ``true`` if the instance is operating normally, or ``false`` if
            the instance is in an error state.

          - **Status** *(string) --*

            Status of the DB instance. For a ``StatusType`` of read replica, the values can be
            ``replicating`` , error, ``stopped`` , or ``terminated`` .

          - **Message** *(string) --*

            Details of the error if there is an error for the instance. If the instance is not in
            an error state, this value is blank.

      - **DBClusterIdentifier** *(string) --*

        Contains the name of the DB cluster that the DB instance is a member of if the DB instance
        is a member of a DB cluster.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether or not the DB instance is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        instance.

      - **DbiResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
        in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

      - **CACertificateIdentifier** *(string) --*

        The identifier of the CA certificate for this DB instance.

      - **PromotionTier** *(integer) --*

        A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
        primary instance after a failure of the existing primary instance.

      - **DBInstanceArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB instance.

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB instance is configured to export to Amazon CloudWatch Logs.

        - *(string) --*
    """


_ClientResetDbClusterParameterGroupParametersTypeDef = TypedDict(
    "_ClientResetDbClusterParameterGroupParametersTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": str,
    },
    total=False,
)


class ClientResetDbClusterParameterGroupParametersTypeDef(
    _ClientResetDbClusterParameterGroupParametersTypeDef
):
    """
    Type definition for `ClientResetDbClusterParameterGroup` `Parameters`

    Detailed information about an individual parameter.

    - **ParameterName** *(string) --*

      Specifies the name of the parameter.

    - **ParameterValue** *(string) --*

      Specifies the value of the parameter.

    - **Description** *(string) --*

      Provides a description of the parameter.

    - **Source** *(string) --*

      Indicates the source of the parameter value.

    - **ApplyType** *(string) --*

      Specifies the engine-specific parameters type.

    - **DataType** *(string) --*

      Specifies the valid data type for the parameter.

    - **AllowedValues** *(string) --*

      Specifies the valid range of values for the parameter.

    - **IsModifiable** *(boolean) --*

      Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some
      parameters have security or operational implications that prevent them from being changed.

    - **MinimumEngineVersion** *(string) --*

      The earliest engine version to which the parameter can apply.

    - **ApplyMethod** *(string) --*

      Indicates when to apply parameter updates.
    """


_ClientResetDbClusterParameterGroupResponseTypeDef = TypedDict(
    "_ClientResetDbClusterParameterGroupResponseTypeDef",
    {"DBClusterParameterGroupName": str},
    total=False,
)


class ClientResetDbClusterParameterGroupResponseTypeDef(
    _ClientResetDbClusterParameterGroupResponseTypeDef
):
    """
    Type definition for `ClientResetDbClusterParameterGroup` `Response`

    Contains the name of a DB cluster parameter group.

    - **DBClusterParameterGroupName** *(string) --*

      The name of a DB cluster parameter group.

      Constraints:

      * Must be from 1 to 255 letters or numbers.

      * The first character must be a letter.

      * Cannot end with a hyphen or contain two consecutive hyphens.

      .. note::

        This value is stored as a lowercase string.
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshotResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      ``Status`` property returns one of the following values:

      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
      cannot assume the IAM role to access other AWS services on your behalf.
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshotResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      A value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to
      the primary instance after a failure of the existing primary instance.
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshotResponseDBCluster` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientRestoreDbClusterFromSnapshotResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshotResponse` `DBCluster`

    Detailed information about a DB cluster.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
      created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group that is associated with the DB cluster, including
      the name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      The earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
      connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
      clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
      connection requests among the Amazon DocumentDB replicas in the DB cluster. This
      functionality can help balance your read workload across multiple Amazon DocumentDB
      replicas in your DB cluster.

      If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
      promoted to be the primary instance, your connection is dropped. To continue sending your
      read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
      the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master user name for the DB cluster.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          A value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to
          the primary instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
      to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          ``Status`` property returns one of the following values:

          * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
          cannot assume the IAM role to access other AWS services on your behalf.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

      - *(string) --*

    - **DeletionProtection** *(boolean) --*

      Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
      cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
      ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientRestoreDbClusterFromSnapshotResponseTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterFromSnapshotResponseDBClusterTypeDef},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotResponseTypeDef(
    _ClientRestoreDbClusterFromSnapshotResponseTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshot` `Response`

    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group that is associated with the DB cluster, including
        the name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        The earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
        connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
        clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
        connection requests among the Amazon DocumentDB replicas in the DB cluster. This
        functionality can help balance your read workload across multiple Amazon DocumentDB
        replicas in your DB cluster.

        If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
        promoted to be the primary instance, your connection is dropped. To continue sending your
        read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
        the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master user name for the DB cluster.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            A value that is ``true`` if the cluster member is the primary instance for the DB
            cluster and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which an Amazon DocumentDB replica is promoted to
            the primary instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
        to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The
            ``Status`` property returns one of the following values:

            * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
            cannot assume the IAM role to access other AWS services on your behalf.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

        - *(string) --*

      - **DeletionProtection** *(boolean) --*

        Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
        cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
        ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientRestoreDbClusterFromSnapshotTagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterFromSnapshotTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRestoreDbClusterFromSnapshotTagsTypeDef(
    _ClientRestoreDbClusterFromSnapshotTagsTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterFromSnapshot` `Tags`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTimeResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      ``Status`` property returns one of the following values:

      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
      cannot assume the IAM role to access other AWS services on your behalf.
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTimeResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      A value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to
      the primary instance after a failure of the existing primary instance.
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTimeResponseDBCluster` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientRestoreDbClusterToPointInTimeResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTimeResponse` `DBCluster`

    Detailed information about a DB cluster.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
      created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group that is associated with the DB cluster, including
      the name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      The earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
      connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
      clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
      connection requests among the Amazon DocumentDB replicas in the DB cluster. This
      functionality can help balance your read workload across multiple Amazon DocumentDB
      replicas in your DB cluster.

      If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
      promoted to be the primary instance, your connection is dropped. To continue sending your
      read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
      the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master user name for the DB cluster.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          A value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to
          the primary instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
      to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          ``Status`` property returns one of the following values:

          * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
          cannot assume the IAM role to access other AWS services on your behalf.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

      - *(string) --*

    - **DeletionProtection** *(boolean) --*

      Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
      cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
      ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientRestoreDbClusterToPointInTimeResponseTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeResponseTypeDef",
    {"DBCluster": ClientRestoreDbClusterToPointInTimeResponseDBClusterTypeDef},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeResponseTypeDef(
    _ClientRestoreDbClusterToPointInTimeResponseTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTime` `Response`

    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group that is associated with the DB cluster, including
        the name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        The earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
        connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
        clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
        connection requests among the Amazon DocumentDB replicas in the DB cluster. This
        functionality can help balance your read workload across multiple Amazon DocumentDB
        replicas in your DB cluster.

        If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
        promoted to be the primary instance, your connection is dropped. To continue sending your
        read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
        the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master user name for the DB cluster.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            A value that is ``true`` if the cluster member is the primary instance for the DB
            cluster and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which an Amazon DocumentDB replica is promoted to
            the primary instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
        to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The
            ``Status`` property returns one of the following values:

            * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
            cannot assume the IAM role to access other AWS services on your behalf.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

        - *(string) --*

      - **DeletionProtection** *(boolean) --*

        Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
        cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
        ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientRestoreDbClusterToPointInTimeTagsTypeDef = TypedDict(
    "_ClientRestoreDbClusterToPointInTimeTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientRestoreDbClusterToPointInTimeTagsTypeDef(
    _ClientRestoreDbClusterToPointInTimeTagsTypeDef
):
    """
    Type definition for `ClientRestoreDbClusterToPointInTime` `Tags`

    Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

    - **Key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    - **Value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length and can't be prefixed with "aws:" or "rds:". The string can contain only the set of
      Unicode letters, digits, white space, '_', '.', '/', '=', '+', '-' (Java regex:
      "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientStartDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      ``Status`` property returns one of the following values:

      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
      cannot assume the IAM role to access other AWS services on your behalf.
    """


_ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientStartDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      A value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to
      the primary instance after a failure of the existing primary instance.
    """


_ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientStartDbClusterResponseDBCluster` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientStartDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientStartDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientStartDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientStartDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientStartDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientStartDbClusterResponseDBClusterTypeDef(
    _ClientStartDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientStartDbClusterResponse` `DBCluster`

    Detailed information about a DB cluster.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
      created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group that is associated with the DB cluster, including
      the name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      The earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
      connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
      clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
      connection requests among the Amazon DocumentDB replicas in the DB cluster. This
      functionality can help balance your read workload across multiple Amazon DocumentDB
      replicas in your DB cluster.

      If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
      promoted to be the primary instance, your connection is dropped. To continue sending your
      read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
      the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master user name for the DB cluster.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          A value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to
          the primary instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
      to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          ``Status`` property returns one of the following values:

          * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
          cannot assume the IAM role to access other AWS services on your behalf.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

      - *(string) --*

    - **DeletionProtection** *(boolean) --*

      Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
      cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
      ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientStartDbClusterResponseTypeDef = TypedDict(
    "_ClientStartDbClusterResponseTypeDef",
    {"DBCluster": ClientStartDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientStartDbClusterResponseTypeDef(_ClientStartDbClusterResponseTypeDef):
    """
    Type definition for `ClientStartDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group that is associated with the DB cluster, including
        the name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        The earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
        connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
        clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
        connection requests among the Amazon DocumentDB replicas in the DB cluster. This
        functionality can help balance your read workload across multiple Amazon DocumentDB
        replicas in your DB cluster.

        If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
        promoted to be the primary instance, your connection is dropped. To continue sending your
        read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
        the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master user name for the DB cluster.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            A value that is ``true`` if the cluster member is the primary instance for the DB
            cluster and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which an Amazon DocumentDB replica is promoted to
            the primary instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
        to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The
            ``Status`` property returns one of the following values:

            * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
            cannot assume the IAM role to access other AWS services on your behalf.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

        - *(string) --*

      - **DeletionProtection** *(boolean) --*

        Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
        cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
        ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef(
    _ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef
):
    """
    Type definition for `ClientStopDbClusterResponseDBCluster` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      ``Status`` property returns one of the following values:

      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
      cannot assume the IAM role to access other AWS services on your behalf.
    """


_ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef(
    _ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef
):
    """
    Type definition for `ClientStopDbClusterResponseDBCluster` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      A value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to
      the primary instance after a failure of the existing primary instance.
    """


_ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef(
    _ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
):
    """
    Type definition for `ClientStopDbClusterResponseDBCluster` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_ClientStopDbClusterResponseDBClusterTypeDef = TypedDict(
    "_ClientStopDbClusterResponseDBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            ClientStopDbClusterResponseDBClusterDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            ClientStopDbClusterResponseDBClusterVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            ClientStopDbClusterResponseDBClusterAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientStopDbClusterResponseDBClusterTypeDef(
    _ClientStopDbClusterResponseDBClusterTypeDef
):
    """
    Type definition for `ClientStopDbClusterResponse` `DBCluster`

    Detailed information about a DB cluster.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
      created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group that is associated with the DB cluster, including
      the name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      The earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
      connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
      clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
      connection requests among the Amazon DocumentDB replicas in the DB cluster. This
      functionality can help balance your read workload across multiple Amazon DocumentDB
      replicas in your DB cluster.

      If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
      promoted to be the primary instance, your connection is dropped. To continue sending your
      read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
      the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master user name for the DB cluster.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          A value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to
          the primary instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
      to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
      AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          ``Status`` property returns one of the following values:

          * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
          cannot assume the IAM role to access other AWS services on your behalf.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

      - *(string) --*

    - **DeletionProtection** *(boolean) --*

      Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
      cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
      ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_ClientStopDbClusterResponseTypeDef = TypedDict(
    "_ClientStopDbClusterResponseTypeDef",
    {"DBCluster": ClientStopDbClusterResponseDBClusterTypeDef},
    total=False,
)


class ClientStopDbClusterResponseTypeDef(_ClientStopDbClusterResponseTypeDef):
    """
    Type definition for `ClientStopDbCluster` `Response`

    - **DBCluster** *(dict) --*

      Detailed information about a DB cluster.

      - **AvailabilityZones** *(list) --*

        Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can be
        created in.

        - *(string) --*

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the number of days for which automatic DB snapshots are retained.

      - **DBClusterIdentifier** *(string) --*

        Contains a user-supplied DB cluster identifier. This identifier is the unique key that
        identifies a DB cluster.

      - **DBClusterParameterGroup** *(string) --*

        Specifies the name of the DB cluster parameter group for the DB cluster.

      - **DBSubnetGroup** *(string) --*

        Specifies information on the subnet group that is associated with the DB cluster, including
        the name, description, and subnets in the subnet group.

      - **Status** *(string) --*

        Specifies the current state of this DB cluster.

      - **PercentProgress** *(string) --*

        Specifies the progress of the operation as a percentage.

      - **EarliestRestorableTime** *(datetime) --*

        The earliest time to which a database can be restored with point-in-time restore.

      - **Endpoint** *(string) --*

        Specifies the connection endpoint for the primary instance of the DB cluster.

      - **ReaderEndpoint** *(string) --*

        The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load balances
        connections across the Amazon DocumentDB replicas that are available in a DB cluster. As
        clients request new connections to the reader endpoint, Amazon DocumentDB distributes the
        connection requests among the Amazon DocumentDB replicas in the DB cluster. This
        functionality can help balance your read workload across multiple Amazon DocumentDB
        replicas in your DB cluster.

        If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
        promoted to be the primary instance, your connection is dropped. To continue sending your
        read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect to
        the reader endpoint.

      - **MultiAZ** *(boolean) --*

        Specifies whether the DB cluster has instances in multiple Availability Zones.

      - **Engine** *(string) --*

        Provides the name of the database engine to be used for this DB cluster.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LatestRestorableTime** *(datetime) --*

        Specifies the latest time to which a database can be restored with point-in-time restore.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **MasterUsername** *(string) --*

        Contains the master user name for the DB cluster.

      - **PreferredBackupWindow** *(string) --*

        Specifies the daily time range during which automated backups are created if automated
        backups are enabled, as determined by the ``BackupRetentionPeriod`` .

      - **PreferredMaintenanceWindow** *(string) --*

        Specifies the weekly time range during which system maintenance can occur, in Universal
        Coordinated Time (UTC).

      - **DBClusterMembers** *(list) --*

        Provides the list of instances that make up the DB cluster.

        - *(dict) --*

          Contains information about an instance that is part of a DB cluster.

          - **DBInstanceIdentifier** *(string) --*

            Specifies the instance identifier for this member of the DB cluster.

          - **IsClusterWriter** *(boolean) --*

            A value that is ``true`` if the cluster member is the primary instance for the DB
            cluster and ``false`` otherwise.

          - **DBClusterParameterGroupStatus** *(string) --*

            Specifies the status of the DB cluster parameter group for this member of the DB
            cluster.

          - **PromotionTier** *(integer) --*

            A value that specifies the order in which an Amazon DocumentDB replica is promoted to
            the primary instance after a failure of the existing primary instance.

      - **VpcSecurityGroups** *(list) --*

        Provides a list of virtual private cloud (VPC) security groups that the DB cluster belongs
        to.

        - *(dict) --*

          Used as a response element for queries on virtual private cloud (VPC) security group
          membership.

          - **VpcSecurityGroupId** *(string) --*

            The name of the VPC security group.

          - **Status** *(string) --*

            The status of the VPC security group.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

      - **StorageEncrypted** *(boolean) --*

        Specifies whether the DB cluster is encrypted.

      - **KmsKeyId** *(string) --*

        If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
        cluster.

      - **DbClusterResourceId** *(string) --*

        The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found in
        AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

      - **DBClusterArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB cluster.

      - **AssociatedRoles** *(list) --*

        Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
        with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
        the DB cluster to access other AWS services on your behalf.

        - *(dict) --*

          Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
          cluster.

          - **RoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

          - **Status** *(string) --*

            Describes the state of association between the IAM role and the DB cluster. The
            ``Status`` property returns one of the following values:

            * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
            access other AWS services on your behalf.

            * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

            * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB cluster
            cannot assume the IAM role to access other AWS services on your behalf.

      - **ClusterCreateTime** *(datetime) --*

        Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

      - **EnabledCloudwatchLogsExports** *(list) --*

        A list of log types that this DB cluster is configured to export to Amazon CloudWatch Logs.

        - *(string) --*

      - **DeletionProtection** *(boolean) --*

        Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
        cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
        ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_DbInstanceAvailableWaitFiltersTypeDef = TypedDict(
    "_DbInstanceAvailableWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DbInstanceAvailableWaitFiltersTypeDef(_DbInstanceAvailableWaitFiltersTypeDef):
    """
    Type definition for `DbInstanceAvailableWait` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_DbInstanceAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_DbInstanceAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class DbInstanceAvailableWaitWaiterConfigTypeDef(
    _DbInstanceAvailableWaitWaiterConfigTypeDef
):
    """
    Type definition for `DbInstanceAvailableWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_DbInstanceDeletedWaitFiltersTypeDef = TypedDict(
    "_DbInstanceDeletedWaitFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DbInstanceDeletedWaitFiltersTypeDef(_DbInstanceDeletedWaitFiltersTypeDef):
    """
    Type definition for `DbInstanceDeletedWait` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_DbInstanceDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_DbInstanceDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class DbInstanceDeletedWaitWaiterConfigTypeDef(
    _DbInstanceDeletedWaitWaiterConfigTypeDef
):
    """
    Type definition for `DbInstanceDeletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """


_DescribeDBClustersPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBClustersPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeDBClustersPaginateFiltersTypeDef(
    _DescribeDBClustersPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginate` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_DescribeDBClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBClustersPaginatePaginationConfigTypeDef(
    _DescribeDBClustersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginate` `PaginationConfig`

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


_DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef",
    {"RoleArn": str, "Status": str},
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginateResponseDBClusters` `AssociatedRoles`

    Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
    cluster.

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

    - **Status** *(string) --*

      Describes the state of association between the IAM role and the DB cluster. The
      ``Status`` property returns one of the following values:

      * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
      access other AWS services on your behalf.

      * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

      * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB
      cluster cannot assume the IAM role to access other AWS services on your behalf.
    """


_DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginateResponseDBClusters` `DBClusterMembers`

    Contains information about an instance that is part of a DB cluster.

    - **DBInstanceIdentifier** *(string) --*

      Specifies the instance identifier for this member of the DB cluster.

    - **IsClusterWriter** *(boolean) --*

      A value that is ``true`` if the cluster member is the primary instance for the DB
      cluster and ``false`` otherwise.

    - **DBClusterParameterGroupStatus** *(string) --*

      Specifies the status of the DB cluster parameter group for this member of the DB
      cluster.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to
      the primary instance after a failure of the existing primary instance.
    """


_DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginateResponseDBClusters` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_DescribeDBClustersPaginateResponseDBClustersTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseDBClustersTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "DBClusterMembers": List[
            DescribeDBClustersPaginateResponseDBClustersDBClusterMembersTypeDef
        ],
        "VpcSecurityGroups": List[
            DescribeDBClustersPaginateResponseDBClustersVpcSecurityGroupsTypeDef
        ],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List[
            DescribeDBClustersPaginateResponseDBClustersAssociatedRolesTypeDef
        ],
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class DescribeDBClustersPaginateResponseDBClustersTypeDef(
    _DescribeDBClustersPaginateResponseDBClustersTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginateResponse` `DBClusters`

    Detailed information about a DB cluster.

    - **AvailabilityZones** *(list) --*

      Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can
      be created in.

      - *(string) --*

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **DBClusterIdentifier** *(string) --*

      Contains a user-supplied DB cluster identifier. This identifier is the unique key that
      identifies a DB cluster.

    - **DBClusterParameterGroup** *(string) --*

      Specifies the name of the DB cluster parameter group for the DB cluster.

    - **DBSubnetGroup** *(string) --*

      Specifies information on the subnet group that is associated with the DB cluster,
      including the name, description, and subnets in the subnet group.

    - **Status** *(string) --*

      Specifies the current state of this DB cluster.

    - **PercentProgress** *(string) --*

      Specifies the progress of the operation as a percentage.

    - **EarliestRestorableTime** *(datetime) --*

      The earliest time to which a database can be restored with point-in-time restore.

    - **Endpoint** *(string) --*

      Specifies the connection endpoint for the primary instance of the DB cluster.

    - **ReaderEndpoint** *(string) --*

      The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load
      balances connections across the Amazon DocumentDB replicas that are available in a DB
      cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB
      distributes the connection requests among the Amazon DocumentDB replicas in the DB
      cluster. This functionality can help balance your read workload across multiple Amazon
      DocumentDB replicas in your DB cluster.

      If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
      promoted to be the primary instance, your connection is dropped. To continue sending your
      read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect
      to the reader endpoint.

    - **MultiAZ** *(boolean) --*

      Specifies whether the DB cluster has instances in multiple Availability Zones.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB cluster.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **MasterUsername** *(string) --*

      Contains the master user name for the DB cluster.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **DBClusterMembers** *(list) --*

      Provides the list of instances that make up the DB cluster.

      - *(dict) --*

        Contains information about an instance that is part of a DB cluster.

        - **DBInstanceIdentifier** *(string) --*

          Specifies the instance identifier for this member of the DB cluster.

        - **IsClusterWriter** *(boolean) --*

          A value that is ``true`` if the cluster member is the primary instance for the DB
          cluster and ``false`` otherwise.

        - **DBClusterParameterGroupStatus** *(string) --*

          Specifies the status of the DB cluster parameter group for this member of the DB
          cluster.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to
          the primary instance after a failure of the existing primary instance.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of virtual private cloud (VPC) security groups that the DB cluster
      belongs to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether the DB cluster is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      cluster.

    - **DbClusterResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

    - **DBClusterArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB cluster.

    - **AssociatedRoles** *(list) --*

      Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
      with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
      the DB cluster to access other AWS services on your behalf.

      - *(dict) --*

        Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
        cluster.

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

        - **Status** *(string) --*

          Describes the state of association between the IAM role and the DB cluster. The
          ``Status`` property returns one of the following values:

          * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
          access other AWS services on your behalf.

          * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

          * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB
          cluster cannot assume the IAM role to access other AWS services on your behalf.

    - **ClusterCreateTime** *(datetime) --*

      Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB cluster is configured to export to Amazon CloudWatch
      Logs.

      - *(string) --*

    - **DeletionProtection** *(boolean) --*

      Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
      cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
      ``DeletionProtection`` protects clusters from being accidentally deleted.
    """


_DescribeDBClustersPaginateResponseTypeDef = TypedDict(
    "_DescribeDBClustersPaginateResponseTypeDef",
    {
        "DBClusters": List[DescribeDBClustersPaginateResponseDBClustersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBClustersPaginateResponseTypeDef(
    _DescribeDBClustersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBClustersPaginate` `Response`

    Represents the output of  DescribeDBClusters .

    - **DBClusters** *(list) --*

      A list of DB clusters.

      - *(dict) --*

        Detailed information about a DB cluster.

        - **AvailabilityZones** *(list) --*

          Provides the list of Amazon EC2 Availability Zones that instances in the DB cluster can
          be created in.

          - *(string) --*

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the number of days for which automatic DB snapshots are retained.

        - **DBClusterIdentifier** *(string) --*

          Contains a user-supplied DB cluster identifier. This identifier is the unique key that
          identifies a DB cluster.

        - **DBClusterParameterGroup** *(string) --*

          Specifies the name of the DB cluster parameter group for the DB cluster.

        - **DBSubnetGroup** *(string) --*

          Specifies information on the subnet group that is associated with the DB cluster,
          including the name, description, and subnets in the subnet group.

        - **Status** *(string) --*

          Specifies the current state of this DB cluster.

        - **PercentProgress** *(string) --*

          Specifies the progress of the operation as a percentage.

        - **EarliestRestorableTime** *(datetime) --*

          The earliest time to which a database can be restored with point-in-time restore.

        - **Endpoint** *(string) --*

          Specifies the connection endpoint for the primary instance of the DB cluster.

        - **ReaderEndpoint** *(string) --*

          The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load
          balances connections across the Amazon DocumentDB replicas that are available in a DB
          cluster. As clients request new connections to the reader endpoint, Amazon DocumentDB
          distributes the connection requests among the Amazon DocumentDB replicas in the DB
          cluster. This functionality can help balance your read workload across multiple Amazon
          DocumentDB replicas in your DB cluster.

          If a failover occurs, and the Amazon DocumentDB replica that you are connected to is
          promoted to be the primary instance, your connection is dropped. To continue sending your
          read workload to other Amazon DocumentDB replicas in the cluster, you can then reconnect
          to the reader endpoint.

        - **MultiAZ** *(boolean) --*

          Specifies whether the DB cluster has instances in multiple Availability Zones.

        - **Engine** *(string) --*

          Provides the name of the database engine to be used for this DB cluster.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **LatestRestorableTime** *(datetime) --*

          Specifies the latest time to which a database can be restored with point-in-time restore.

        - **Port** *(integer) --*

          Specifies the port that the database engine is listening on.

        - **MasterUsername** *(string) --*

          Contains the master user name for the DB cluster.

        - **PreferredBackupWindow** *(string) --*

          Specifies the daily time range during which automated backups are created if automated
          backups are enabled, as determined by the ``BackupRetentionPeriod`` .

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which system maintenance can occur, in Universal
          Coordinated Time (UTC).

        - **DBClusterMembers** *(list) --*

          Provides the list of instances that make up the DB cluster.

          - *(dict) --*

            Contains information about an instance that is part of a DB cluster.

            - **DBInstanceIdentifier** *(string) --*

              Specifies the instance identifier for this member of the DB cluster.

            - **IsClusterWriter** *(boolean) --*

              A value that is ``true`` if the cluster member is the primary instance for the DB
              cluster and ``false`` otherwise.

            - **DBClusterParameterGroupStatus** *(string) --*

              Specifies the status of the DB cluster parameter group for this member of the DB
              cluster.

            - **PromotionTier** *(integer) --*

              A value that specifies the order in which an Amazon DocumentDB replica is promoted to
              the primary instance after a failure of the existing primary instance.

        - **VpcSecurityGroups** *(list) --*

          Provides a list of virtual private cloud (VPC) security groups that the DB cluster
          belongs to.

          - *(dict) --*

            Used as a response element for queries on virtual private cloud (VPC) security group
            membership.

            - **VpcSecurityGroupId** *(string) --*

              The name of the VPC security group.

            - **Status** *(string) --*

              The status of the VPC security group.

        - **HostedZoneId** *(string) --*

          Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

        - **StorageEncrypted** *(boolean) --*

          Specifies whether the DB cluster is encrypted.

        - **KmsKeyId** *(string) --*

          If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
          cluster.

        - **DbClusterResourceId** *(string) --*

          The AWS Region-unique, immutable identifier for the DB cluster. This identifier is found
          in AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed.

        - **DBClusterArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB cluster.

        - **AssociatedRoles** *(list) --*

          Provides a list of the AWS Identity and Access Management (IAM) roles that are associated
          with the DB cluster. IAM roles that are associated with a DB cluster grant permission for
          the DB cluster to access other AWS services on your behalf.

          - *(dict) --*

            Describes an AWS Identity and Access Management (IAM) role that is associated with a DB
            cluster.

            - **RoleArn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.

            - **Status** *(string) --*

              Describes the state of association between the IAM role and the DB cluster. The
              ``Status`` property returns one of the following values:

              * ``ACTIVE`` - The IAM role ARN is associated with the DB cluster and can be used to
              access other AWS services on your behalf.

              * ``PENDING`` - The IAM role ARN is being associated with the DB cluster.

              * ``INVALID`` - The IAM role ARN is associated with the DB cluster, but the DB
              cluster cannot assume the IAM role to access other AWS services on your behalf.

        - **ClusterCreateTime** *(datetime) --*

          Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).

        - **EnabledCloudwatchLogsExports** *(list) --*

          A list of log types that this DB cluster is configured to export to Amazon CloudWatch
          Logs.

          - *(string) --*

        - **DeletionProtection** *(boolean) --*

          Specifies whether this cluster can be deleted. If ``DeletionProtection`` is enabled, the
          cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
          ``DeletionProtection`` protects clusters from being accidentally deleted.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBEngineVersionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeDBEngineVersionsPaginateFiltersTypeDef(
    _DescribeDBEngineVersionsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginate` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_DescribeDBEngineVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBEngineVersionsPaginatePaginationConfigTypeDef(
    _DescribeDBEngineVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginate` `PaginationConfig`

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


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginateResponseDBEngineVersions` `ValidUpgradeTarget`

    The version of the database engine that a DB instance can be upgraded to.

    - **Engine** *(string) --*

      The name of the upgrade target database engine.

    - **EngineVersion** *(string) --*

      The version number of the upgrade target database engine.

    - **Description** *(string) --*

      The version of the database engine that a DB instance can be upgraded to.

    - **AutoUpgrade** *(boolean) --*

      A value that indicates whether the target version is applied to any source DB
      instances that have ``AutoMinorVersionUpgrade`` set to ``true`` .

    - **IsMajorVersionUpgrade** *(boolean) --*

      A value that indicates whether a database engine is upgraded to a major version.
    """


_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "ValidUpgradeTarget": List[
            DescribeDBEngineVersionsPaginateResponseDBEngineVersionsValidUpgradeTargetTypeDef
        ],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef(
    _DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginateResponse` `DBEngineVersions`

    Detailed information about a DB engine version.

    - **Engine** *(string) --*

      The name of the database engine.

    - **EngineVersion** *(string) --*

      The version number of the database engine.

    - **DBParameterGroupFamily** *(string) --*

      The name of the DB parameter group family for the database engine.

    - **DBEngineDescription** *(string) --*

      The description of the database engine.

    - **DBEngineVersionDescription** *(string) --*

      The description of the database engine version.

    - **ValidUpgradeTarget** *(list) --*

      A list of engine versions that this database engine version can be upgraded to.

      - *(dict) --*

        The version of the database engine that a DB instance can be upgraded to.

        - **Engine** *(string) --*

          The name of the upgrade target database engine.

        - **EngineVersion** *(string) --*

          The version number of the upgrade target database engine.

        - **Description** *(string) --*

          The version of the database engine that a DB instance can be upgraded to.

        - **AutoUpgrade** *(boolean) --*

          A value that indicates whether the target version is applied to any source DB
          instances that have ``AutoMinorVersionUpgrade`` set to ``true`` .

        - **IsMajorVersionUpgrade** *(boolean) --*

          A value that indicates whether a database engine is upgraded to a major version.

    - **ExportableLogTypes** *(list) --*

      The types of logs that the database engine has available for export to Amazon CloudWatch
      Logs.

      - *(string) --*

    - **SupportsLogExportsToCloudwatchLogs** *(boolean) --*

      A value that indicates whether the engine version supports exporting the log types
      specified by ``ExportableLogTypes`` to CloudWatch Logs.
    """


_DescribeDBEngineVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBEngineVersionsPaginateResponseTypeDef",
    {
        "DBEngineVersions": List[
            DescribeDBEngineVersionsPaginateResponseDBEngineVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBEngineVersionsPaginateResponseTypeDef(
    _DescribeDBEngineVersionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBEngineVersionsPaginate` `Response`

    Represents the output of  DescribeDBEngineVersions .

    - **DBEngineVersions** *(list) --*

      Detailed information about one or more DB engine versions.

      - *(dict) --*

        Detailed information about a DB engine version.

        - **Engine** *(string) --*

          The name of the database engine.

        - **EngineVersion** *(string) --*

          The version number of the database engine.

        - **DBParameterGroupFamily** *(string) --*

          The name of the DB parameter group family for the database engine.

        - **DBEngineDescription** *(string) --*

          The description of the database engine.

        - **DBEngineVersionDescription** *(string) --*

          The description of the database engine version.

        - **ValidUpgradeTarget** *(list) --*

          A list of engine versions that this database engine version can be upgraded to.

          - *(dict) --*

            The version of the database engine that a DB instance can be upgraded to.

            - **Engine** *(string) --*

              The name of the upgrade target database engine.

            - **EngineVersion** *(string) --*

              The version number of the upgrade target database engine.

            - **Description** *(string) --*

              The version of the database engine that a DB instance can be upgraded to.

            - **AutoUpgrade** *(boolean) --*

              A value that indicates whether the target version is applied to any source DB
              instances that have ``AutoMinorVersionUpgrade`` set to ``true`` .

            - **IsMajorVersionUpgrade** *(boolean) --*

              A value that indicates whether a database engine is upgraded to a major version.

        - **ExportableLogTypes** *(list) --*

          The types of logs that the database engine has available for export to Amazon CloudWatch
          Logs.

          - *(string) --*

        - **SupportsLogExportsToCloudwatchLogs** *(boolean) --*

          A value that indicates whether the engine version supports exporting the log types
          specified by ``ExportableLogTypes`` to CloudWatch Logs.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBInstancesPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeDBInstancesPaginateFiltersTypeDef(
    _DescribeDBInstancesPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginate` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_DescribeDBInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBInstancesPaginatePaginationConfigTypeDef(
    _DescribeDBInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginate` `PaginationConfig`

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


_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnets` `SubnetAvailabilityZone`

    Specifies the Availability Zone for the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroup` `Subnets`

    Detailed information about a subnet.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the Availability Zone for the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `DBSubnetGroup`

    Specifies information on the subnet group that is associated with the DB instance,
    including the name, description, and subnets in the subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Detailed information about one or more subnets within a DB subnet group.

      - *(dict) --*

        Detailed information about a subnet.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the Availability Zone for the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef",
    {"Address": str, "Port": int, "HostedZoneId": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `Endpoint`

    Specifies the connection endpoint.

    - **Address** *(string) --*

      Specifies the DNS address of the DB instance.

    - **Port** *(integer) --*

      Specifies the port that the database engine is listening on.

    - **HostedZoneId** *(string) --*

      Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
    """


_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef",
    {"LogTypesToEnable": List[str], "LogTypesToDisable": List[str]},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValues` `PendingCloudwatchLogsExports`

    A list of the log types whose configuration is still pending. These log types are in
    the process of being activated or deactivated.

    - **LogTypesToEnable** *(list) --*

      Log types that are in the process of being deactivated. After they are deactivated,
      these log types aren't exported to CloudWatch Logs.

      - *(string) --*

    - **LogTypesToDisable** *(list) --*

      Log types that are in the process of being enabled. After they are enabled, these log
      types are exported to Amazon CloudWatch Logs.

      - *(string) --*
    """


_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesPendingCloudwatchLogsExportsTypeDef,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `PendingModifiedValues`

    Specifies that changes to the DB instance are pending. This element is included only when
    changes are pending. Specific changes are identified by subelements.

    - **DBInstanceClass** *(string) --*

      Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
      currently being applied.

    - **AllocatedStorage** *(integer) --*

      Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
      is currently being applied.

    - **MasterUserPassword** *(string) --*

      Contains the pending or currently in-progress change of the master credentials for the
      DB instance.

    - **Port** *(integer) --*

      Specifies the pending port for the DB instance.

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the pending number of days for which automated backups are retained.

    - **MultiAZ** *(boolean) --*

      Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **LicenseModel** *(string) --*

      The license model for the DB instance.

      Valid values: ``license-included`` , ``bring-your-own-license`` ,
      ``general-public-license``

    - **Iops** *(integer) --*

      Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
      currently being applied.

    - **DBInstanceIdentifier** *(string) --*

      Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
      is currently being applied.

    - **StorageType** *(string) --*

      Specifies the storage type to be associated with the DB instance.

    - **CACertificateIdentifier** *(string) --*

      Specifies the identifier of the certificate authority (CA) certificate for the DB
      instance.

    - **DBSubnetGroupName** *(string) --*

      The new DB subnet group for the DB instance.

    - **PendingCloudwatchLogsExports** *(dict) --*

      A list of the log types whose configuration is still pending. These log types are in
      the process of being activated or deactivated.

      - **LogTypesToEnable** *(list) --*

        Log types that are in the process of being deactivated. After they are deactivated,
        these log types aren't exported to CloudWatch Logs.

        - *(string) --*

      - **LogTypesToDisable** *(list) --*

        Log types that are in the process of being enabled. After they are enabled, these log
        types are exported to Amazon CloudWatch Logs.

        - *(string) --*
    """


_DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef",
    {"StatusType": str, "Normal": bool, "Status": str, "Message": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `StatusInfos`

    Provides a list of status information for a DB instance.

    - **StatusType** *(string) --*

      This value is currently "``read replication`` ."

    - **Normal** *(boolean) --*

      A Boolean value that is ``true`` if the instance is operating normally, or ``false``
      if the instance is in an error state.

    - **Status** *(string) --*

      Status of the DB instance. For a ``StatusType`` of read replica, the values can be
      ``replicating`` , error, ``stopped`` , or ``terminated`` .

    - **Message** *(string) --*

      Details of the error if there is an error for the instance. If the instance is not in
      an error state, this value is blank.
    """


_DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponseDBInstances` `VpcSecurityGroups`

    Used as a response element for queries on virtual private cloud (VPC) security group
    membership.

    - **VpcSecurityGroupId** *(string) --*

      The name of the VPC security group.

    - **Status** *(string) --*

      The status of the VPC security group.
    """


_DescribeDBInstancesPaginateResponseDBInstancesTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseDBInstancesTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "Endpoint": DescribeDBInstancesPaginateResponseDBInstancesEndpointTypeDef,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List[
            DescribeDBInstancesPaginateResponseDBInstancesVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "DBSubnetGroup": DescribeDBInstancesPaginateResponseDBInstancesDBSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": DescribeDBInstancesPaginateResponseDBInstancesPendingModifiedValuesTypeDef,
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List[
            DescribeDBInstancesPaginateResponseDBInstancesStatusInfosTypeDef
        ],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseDBInstancesTypeDef(
    _DescribeDBInstancesPaginateResponseDBInstancesTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginateResponse` `DBInstances`

    Detailed information about a DB instance.

    - **DBInstanceIdentifier** *(string) --*

      Contains a user-provided database identifier. This identifier is the unique key that
      identifies a DB instance.

    - **DBInstanceClass** *(string) --*

      Contains the name of the compute and memory capacity class of the DB instance.

    - **Engine** *(string) --*

      Provides the name of the database engine to be used for this DB instance.

    - **DBInstanceStatus** *(string) --*

      Specifies the current state of this database.

    - **Endpoint** *(dict) --*

      Specifies the connection endpoint.

      - **Address** *(string) --*

        Specifies the DNS address of the DB instance.

      - **Port** *(integer) --*

        Specifies the port that the database engine is listening on.

      - **HostedZoneId** *(string) --*

        Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

    - **InstanceCreateTime** *(datetime) --*

      Provides the date and time that the DB instance was created.

    - **PreferredBackupWindow** *(string) --*

      Specifies the daily time range during which automated backups are created if automated
      backups are enabled, as determined by the ``BackupRetentionPeriod`` .

    - **BackupRetentionPeriod** *(integer) --*

      Specifies the number of days for which automatic DB snapshots are retained.

    - **VpcSecurityGroups** *(list) --*

      Provides a list of VPC security group elements that the DB instance belongs to.

      - *(dict) --*

        Used as a response element for queries on virtual private cloud (VPC) security group
        membership.

        - **VpcSecurityGroupId** *(string) --*

          The name of the VPC security group.

        - **Status** *(string) --*

          The status of the VPC security group.

    - **AvailabilityZone** *(string) --*

      Specifies the name of the Availability Zone that the DB instance is located in.

    - **DBSubnetGroup** *(dict) --*

      Specifies information on the subnet group that is associated with the DB instance,
      including the name, description, and subnets in the subnet group.

      - **DBSubnetGroupName** *(string) --*

        The name of the DB subnet group.

      - **DBSubnetGroupDescription** *(string) --*

        Provides the description of the DB subnet group.

      - **VpcId** *(string) --*

        Provides the virtual private cloud (VPC) ID of the DB subnet group.

      - **SubnetGroupStatus** *(string) --*

        Provides the status of the DB subnet group.

      - **Subnets** *(list) --*

        Detailed information about one or more subnets within a DB subnet group.

        - *(dict) --*

          Detailed information about a subnet.

          - **SubnetIdentifier** *(string) --*

            Specifies the identifier of the subnet.

          - **SubnetAvailabilityZone** *(dict) --*

            Specifies the Availability Zone for the subnet.

            - **Name** *(string) --*

              The name of the Availability Zone.

          - **SubnetStatus** *(string) --*

            Specifies the status of the subnet.

      - **DBSubnetGroupArn** *(string) --*

        The Amazon Resource Name (ARN) for the DB subnet group.

    - **PreferredMaintenanceWindow** *(string) --*

      Specifies the weekly time range during which system maintenance can occur, in Universal
      Coordinated Time (UTC).

    - **PendingModifiedValues** *(dict) --*

      Specifies that changes to the DB instance are pending. This element is included only when
      changes are pending. Specific changes are identified by subelements.

      - **DBInstanceClass** *(string) --*

        Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
        currently being applied.

      - **AllocatedStorage** *(integer) --*

        Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
        is currently being applied.

      - **MasterUserPassword** *(string) --*

        Contains the pending or currently in-progress change of the master credentials for the
        DB instance.

      - **Port** *(integer) --*

        Specifies the pending port for the DB instance.

      - **BackupRetentionPeriod** *(integer) --*

        Specifies the pending number of days for which automated backups are retained.

      - **MultiAZ** *(boolean) --*

        Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

      - **EngineVersion** *(string) --*

        Indicates the database engine version.

      - **LicenseModel** *(string) --*

        The license model for the DB instance.

        Valid values: ``license-included`` , ``bring-your-own-license`` ,
        ``general-public-license``

      - **Iops** *(integer) --*

        Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
        currently being applied.

      - **DBInstanceIdentifier** *(string) --*

        Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
        is currently being applied.

      - **StorageType** *(string) --*

        Specifies the storage type to be associated with the DB instance.

      - **CACertificateIdentifier** *(string) --*

        Specifies the identifier of the certificate authority (CA) certificate for the DB
        instance.

      - **DBSubnetGroupName** *(string) --*

        The new DB subnet group for the DB instance.

      - **PendingCloudwatchLogsExports** *(dict) --*

        A list of the log types whose configuration is still pending. These log types are in
        the process of being activated or deactivated.

        - **LogTypesToEnable** *(list) --*

          Log types that are in the process of being deactivated. After they are deactivated,
          these log types aren't exported to CloudWatch Logs.

          - *(string) --*

        - **LogTypesToDisable** *(list) --*

          Log types that are in the process of being enabled. After they are enabled, these log
          types are exported to Amazon CloudWatch Logs.

          - *(string) --*

    - **LatestRestorableTime** *(datetime) --*

      Specifies the latest time to which a database can be restored with point-in-time restore.

    - **EngineVersion** *(string) --*

      Indicates the database engine version.

    - **AutoMinorVersionUpgrade** *(boolean) --*

      Indicates that minor version patches are applied automatically.

    - **PubliclyAccessible** *(boolean) --*

      Not supported. Amazon DocumentDB does not currently support public endpoints. The value
      of ``PubliclyAccessible`` is always ``false`` .

    - **StatusInfos** *(list) --*

      The status of a read replica. If the instance is not a read replica, this is blank.

      - *(dict) --*

        Provides a list of status information for a DB instance.

        - **StatusType** *(string) --*

          This value is currently "``read replication`` ."

        - **Normal** *(boolean) --*

          A Boolean value that is ``true`` if the instance is operating normally, or ``false``
          if the instance is in an error state.

        - **Status** *(string) --*

          Status of the DB instance. For a ``StatusType`` of read replica, the values can be
          ``replicating`` , error, ``stopped`` , or ``terminated`` .

        - **Message** *(string) --*

          Details of the error if there is an error for the instance. If the instance is not in
          an error state, this value is blank.

    - **DBClusterIdentifier** *(string) --*

      Contains the name of the DB cluster that the DB instance is a member of if the DB
      instance is a member of a DB cluster.

    - **StorageEncrypted** *(boolean) --*

      Specifies whether or not the DB instance is encrypted.

    - **KmsKeyId** *(string) --*

      If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
      instance.

    - **DbiResourceId** *(string) --*

      The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
      in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

    - **CACertificateIdentifier** *(string) --*

      The identifier of the CA certificate for this DB instance.

    - **PromotionTier** *(integer) --*

      A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
      primary instance after a failure of the existing primary instance.

    - **DBInstanceArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB instance.

    - **EnabledCloudwatchLogsExports** *(list) --*

      A list of log types that this DB instance is configured to export to Amazon CloudWatch
      Logs.

      - *(string) --*
    """


_DescribeDBInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeDBInstancesPaginateResponseTypeDef",
    {
        "DBInstances": List[DescribeDBInstancesPaginateResponseDBInstancesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBInstancesPaginateResponseTypeDef(
    _DescribeDBInstancesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBInstancesPaginate` `Response`

    Represents the output of  DescribeDBInstances .

    - **DBInstances** *(list) --*

      Detailed information about one or more DB instances.

      - *(dict) --*

        Detailed information about a DB instance.

        - **DBInstanceIdentifier** *(string) --*

          Contains a user-provided database identifier. This identifier is the unique key that
          identifies a DB instance.

        - **DBInstanceClass** *(string) --*

          Contains the name of the compute and memory capacity class of the DB instance.

        - **Engine** *(string) --*

          Provides the name of the database engine to be used for this DB instance.

        - **DBInstanceStatus** *(string) --*

          Specifies the current state of this database.

        - **Endpoint** *(dict) --*

          Specifies the connection endpoint.

          - **Address** *(string) --*

            Specifies the DNS address of the DB instance.

          - **Port** *(integer) --*

            Specifies the port that the database engine is listening on.

          - **HostedZoneId** *(string) --*

            Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.

        - **InstanceCreateTime** *(datetime) --*

          Provides the date and time that the DB instance was created.

        - **PreferredBackupWindow** *(string) --*

          Specifies the daily time range during which automated backups are created if automated
          backups are enabled, as determined by the ``BackupRetentionPeriod`` .

        - **BackupRetentionPeriod** *(integer) --*

          Specifies the number of days for which automatic DB snapshots are retained.

        - **VpcSecurityGroups** *(list) --*

          Provides a list of VPC security group elements that the DB instance belongs to.

          - *(dict) --*

            Used as a response element for queries on virtual private cloud (VPC) security group
            membership.

            - **VpcSecurityGroupId** *(string) --*

              The name of the VPC security group.

            - **Status** *(string) --*

              The status of the VPC security group.

        - **AvailabilityZone** *(string) --*

          Specifies the name of the Availability Zone that the DB instance is located in.

        - **DBSubnetGroup** *(dict) --*

          Specifies information on the subnet group that is associated with the DB instance,
          including the name, description, and subnets in the subnet group.

          - **DBSubnetGroupName** *(string) --*

            The name of the DB subnet group.

          - **DBSubnetGroupDescription** *(string) --*

            Provides the description of the DB subnet group.

          - **VpcId** *(string) --*

            Provides the virtual private cloud (VPC) ID of the DB subnet group.

          - **SubnetGroupStatus** *(string) --*

            Provides the status of the DB subnet group.

          - **Subnets** *(list) --*

            Detailed information about one or more subnets within a DB subnet group.

            - *(dict) --*

              Detailed information about a subnet.

              - **SubnetIdentifier** *(string) --*

                Specifies the identifier of the subnet.

              - **SubnetAvailabilityZone** *(dict) --*

                Specifies the Availability Zone for the subnet.

                - **Name** *(string) --*

                  The name of the Availability Zone.

              - **SubnetStatus** *(string) --*

                Specifies the status of the subnet.

          - **DBSubnetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) for the DB subnet group.

        - **PreferredMaintenanceWindow** *(string) --*

          Specifies the weekly time range during which system maintenance can occur, in Universal
          Coordinated Time (UTC).

        - **PendingModifiedValues** *(dict) --*

          Specifies that changes to the DB instance are pending. This element is included only when
          changes are pending. Specific changes are identified by subelements.

          - **DBInstanceClass** *(string) --*

            Contains the new ``DBInstanceClass`` for the DB instance that will be applied or is
            currently being applied.

          - **AllocatedStorage** *(integer) --*

            Contains the new ``AllocatedStorage`` size for the DB instance that will be applied or
            is currently being applied.

          - **MasterUserPassword** *(string) --*

            Contains the pending or currently in-progress change of the master credentials for the
            DB instance.

          - **Port** *(integer) --*

            Specifies the pending port for the DB instance.

          - **BackupRetentionPeriod** *(integer) --*

            Specifies the pending number of days for which automated backups are retained.

          - **MultiAZ** *(boolean) --*

            Indicates that the Single-AZ DB instance is to change to a Multi-AZ deployment.

          - **EngineVersion** *(string) --*

            Indicates the database engine version.

          - **LicenseModel** *(string) --*

            The license model for the DB instance.

            Valid values: ``license-included`` , ``bring-your-own-license`` ,
            ``general-public-license``

          - **Iops** *(integer) --*

            Specifies the new Provisioned IOPS value for the DB instance that will be applied or is
            currently being applied.

          - **DBInstanceIdentifier** *(string) --*

            Contains the new ``DBInstanceIdentifier`` for the DB instance that will be applied or
            is currently being applied.

          - **StorageType** *(string) --*

            Specifies the storage type to be associated with the DB instance.

          - **CACertificateIdentifier** *(string) --*

            Specifies the identifier of the certificate authority (CA) certificate for the DB
            instance.

          - **DBSubnetGroupName** *(string) --*

            The new DB subnet group for the DB instance.

          - **PendingCloudwatchLogsExports** *(dict) --*

            A list of the log types whose configuration is still pending. These log types are in
            the process of being activated or deactivated.

            - **LogTypesToEnable** *(list) --*

              Log types that are in the process of being deactivated. After they are deactivated,
              these log types aren't exported to CloudWatch Logs.

              - *(string) --*

            - **LogTypesToDisable** *(list) --*

              Log types that are in the process of being enabled. After they are enabled, these log
              types are exported to Amazon CloudWatch Logs.

              - *(string) --*

        - **LatestRestorableTime** *(datetime) --*

          Specifies the latest time to which a database can be restored with point-in-time restore.

        - **EngineVersion** *(string) --*

          Indicates the database engine version.

        - **AutoMinorVersionUpgrade** *(boolean) --*

          Indicates that minor version patches are applied automatically.

        - **PubliclyAccessible** *(boolean) --*

          Not supported. Amazon DocumentDB does not currently support public endpoints. The value
          of ``PubliclyAccessible`` is always ``false`` .

        - **StatusInfos** *(list) --*

          The status of a read replica. If the instance is not a read replica, this is blank.

          - *(dict) --*

            Provides a list of status information for a DB instance.

            - **StatusType** *(string) --*

              This value is currently "``read replication`` ."

            - **Normal** *(boolean) --*

              A Boolean value that is ``true`` if the instance is operating normally, or ``false``
              if the instance is in an error state.

            - **Status** *(string) --*

              Status of the DB instance. For a ``StatusType`` of read replica, the values can be
              ``replicating`` , error, ``stopped`` , or ``terminated`` .

            - **Message** *(string) --*

              Details of the error if there is an error for the instance. If the instance is not in
              an error state, this value is blank.

        - **DBClusterIdentifier** *(string) --*

          Contains the name of the DB cluster that the DB instance is a member of if the DB
          instance is a member of a DB cluster.

        - **StorageEncrypted** *(boolean) --*

          Specifies whether or not the DB instance is encrypted.

        - **KmsKeyId** *(string) --*

          If ``StorageEncrypted`` is ``true`` , the AWS KMS key identifier for the encrypted DB
          instance.

        - **DbiResourceId** *(string) --*

          The AWS Region-unique, immutable identifier for the DB instance. This identifier is found
          in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

        - **CACertificateIdentifier** *(string) --*

          The identifier of the CA certificate for this DB instance.

        - **PromotionTier** *(integer) --*

          A value that specifies the order in which an Amazon DocumentDB replica is promoted to the
          primary instance after a failure of the existing primary instance.

        - **DBInstanceArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB instance.

        - **EnabledCloudwatchLogsExports** *(list) --*

          A list of log types that this DB instance is configured to export to Amazon CloudWatch
          Logs.

          - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDBSubnetGroupsPaginateFiltersTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeDBSubnetGroupsPaginateFiltersTypeDef(
    _DescribeDBSubnetGroupsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginate` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef(
    _DescribeDBSubnetGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginate` `PaginationConfig`

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


_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnets` `SubnetAvailabilityZone`

    Specifies the Availability Zone for the subnet.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginateResponseDBSubnetGroups` `Subnets`

    Detailed information about a subnet.

    - **SubnetIdentifier** *(string) --*

      Specifies the identifier of the subnet.

    - **SubnetAvailabilityZone** *(dict) --*

      Specifies the Availability Zone for the subnet.

      - **Name** *(string) --*

        The name of the Availability Zone.

    - **SubnetStatus** *(string) --*

      Specifies the status of the subnet.
    """


_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsSubnetsTypeDef
        ],
        "DBSubnetGroupArn": str,
    },
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginateResponse` `DBSubnetGroups`

    Detailed information about a DB subnet group.

    - **DBSubnetGroupName** *(string) --*

      The name of the DB subnet group.

    - **DBSubnetGroupDescription** *(string) --*

      Provides the description of the DB subnet group.

    - **VpcId** *(string) --*

      Provides the virtual private cloud (VPC) ID of the DB subnet group.

    - **SubnetGroupStatus** *(string) --*

      Provides the status of the DB subnet group.

    - **Subnets** *(list) --*

      Detailed information about one or more subnets within a DB subnet group.

      - *(dict) --*

        Detailed information about a subnet.

        - **SubnetIdentifier** *(string) --*

          Specifies the identifier of the subnet.

        - **SubnetAvailabilityZone** *(dict) --*

          Specifies the Availability Zone for the subnet.

          - **Name** *(string) --*

            The name of the Availability Zone.

        - **SubnetStatus** *(string) --*

          Specifies the status of the subnet.

    - **DBSubnetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) for the DB subnet group.
    """


_DescribeDBSubnetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeDBSubnetGroupsPaginateResponseTypeDef",
    {
        "DBSubnetGroups": List[
            DescribeDBSubnetGroupsPaginateResponseDBSubnetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDBSubnetGroupsPaginateResponseTypeDef(
    _DescribeDBSubnetGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDBSubnetGroupsPaginate` `Response`

    Represents the output of  DescribeDBSubnetGroups .

    - **DBSubnetGroups** *(list) --*

      Detailed information about one or more DB subnet groups.

      - *(dict) --*

        Detailed information about a DB subnet group.

        - **DBSubnetGroupName** *(string) --*

          The name of the DB subnet group.

        - **DBSubnetGroupDescription** *(string) --*

          Provides the description of the DB subnet group.

        - **VpcId** *(string) --*

          Provides the virtual private cloud (VPC) ID of the DB subnet group.

        - **SubnetGroupStatus** *(string) --*

          Provides the status of the DB subnet group.

        - **Subnets** *(list) --*

          Detailed information about one or more subnets within a DB subnet group.

          - *(dict) --*

            Detailed information about a subnet.

            - **SubnetIdentifier** *(string) --*

              Specifies the identifier of the subnet.

            - **SubnetAvailabilityZone** *(dict) --*

              Specifies the Availability Zone for the subnet.

              - **Name** *(string) --*

                The name of the Availability Zone.

            - **SubnetStatus** *(string) --*

              Specifies the status of the subnet.

        - **DBSubnetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) for the DB subnet group.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeEventsPaginateFiltersTypeDef = TypedDict(
    "_DescribeEventsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)


class DescribeEventsPaginateFiltersTypeDef(_DescribeEventsPaginateFiltersTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventsPaginatePaginationConfigTypeDef(
    _DescribeEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEventsPaginate` `PaginationConfig`

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


_DescribeEventsPaginateResponseEventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
    },
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(
    _DescribeEventsPaginateResponseEventsTypeDef
):
    """
    Type definition for `DescribeEventsPaginateResponse` `Events`

    Detailed information about an event.

    - **SourceIdentifier** *(string) --*

      Provides the identifier for the source of the event.

    - **SourceType** *(string) --*

      Specifies the source type for this event.

    - **Message** *(string) --*

      Provides the text of this event.

    - **EventCategories** *(list) --*

      Specifies the category for the event.

      - *(string) --*

    - **Date** *(datetime) --*

      Specifies the date and time of the event.

    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) for the event.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `Response`

    Represents the output of  DescribeEvents .

    - **Events** *(list) --*

      Detailed information about one or more events.

      - *(dict) --*

        Detailed information about an event.

        - **SourceIdentifier** *(string) --*

          Provides the identifier for the source of the event.

        - **SourceType** *(string) --*

          Specifies the source type for this event.

        - **Message** *(string) --*

          Provides the text of this event.

        - **EventCategories** *(list) --*

          Specifies the category for the event.

          - *(string) --*

        - **Date** *(datetime) --*

          Specifies the date and time of the event.

        - **SourceArn** *(string) --*

          The Amazon Resource Name (ARN) for the event.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
)


class DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateFiltersTypeDef
):
    """
    Type definition for `DescribeOrderableDBInstanceOptionsPaginate` `Filters`

    A named set of filter values, used to return a more specific list of results. You can use a
    filter to match a set of resources by specific criteria, such as IDs.

    Wildcards are not supported in filters.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the filter. Filter names are case sensitive.

    - **Values** *(list) --* **[REQUIRED]**

      One or more filter values. Filter values are case sensitive.

      - *(string) --*
    """


_DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeOrderableDBInstanceOptionsPaginate` `PaginationConfig`

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


_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
):
    """
    Type definition for `DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptions` `AvailabilityZones`

    Information about an Availability Zone.

    - **Name** *(string) --*

      The name of the Availability Zone.
    """


_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List[
            DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsAvailabilityZonesTypeDef
        ],
        "Vpc": bool,
    },
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef
):
    """
    Type definition for `DescribeOrderableDBInstanceOptionsPaginateResponse` `OrderableDBInstanceOptions`

    The options that are available for a DB instance.

    - **Engine** *(string) --*

      The engine type of a DB instance.

    - **EngineVersion** *(string) --*

      The engine version of a DB instance.

    - **DBInstanceClass** *(string) --*

      The DB instance class for a DB instance.

    - **LicenseModel** *(string) --*

      The license model for a DB instance.

    - **AvailabilityZones** *(list) --*

      A list of Availability Zones for a DB instance.

      - *(dict) --*

        Information about an Availability Zone.

        - **Name** *(string) --*

          The name of the Availability Zone.

    - **Vpc** *(boolean) --*

      Indicates whether a DB instance is in a virtual private cloud (VPC).
    """


_DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef = TypedDict(
    "_DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef",
    {
        "OrderableDBInstanceOptions": List[
            DescribeOrderableDBInstanceOptionsPaginateResponseOrderableDBInstanceOptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef(
    _DescribeOrderableDBInstanceOptionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeOrderableDBInstanceOptionsPaginate` `Response`

    Represents the output of  DescribeOrderableDBInstanceOptions .

    - **OrderableDBInstanceOptions** *(list) --*

      The options that are available for a particular orderable DB instance.

      - *(dict) --*

        The options that are available for a DB instance.

        - **Engine** *(string) --*

          The engine type of a DB instance.

        - **EngineVersion** *(string) --*

          The engine version of a DB instance.

        - **DBInstanceClass** *(string) --*

          The DB instance class for a DB instance.

        - **LicenseModel** *(string) --*

          The license model for a DB instance.

        - **AvailabilityZones** *(list) --*

          A list of Availability Zones for a DB instance.

          - *(dict) --*

            Information about an Availability Zone.

            - **Name** *(string) --*

              The name of the Availability Zone.

        - **Vpc** *(boolean) --*

          Indicates whether a DB instance is in a virtual private cloud (VPC).

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
