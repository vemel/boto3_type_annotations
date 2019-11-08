from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeClusterDbRevisions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ClusterIdentifier: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeClusterParameterGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ParameterGroupName: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClusterParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ParameterGroupName: str,
        Source: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClusterSecurityGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClusterSecurityGroupName: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClusterSnapshots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OwnerAccount: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        ClusterExists: bool = None,
        SortingEntities: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClusterSubnetGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClusterSubnetGroupName: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClusterTracks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, MaintenanceTrackName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeClusterVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClusterVersion: str = None,
        ClusterParameterGroupFamily: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClusterIdentifier: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDefaultClusterParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ParameterGroupFamily: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeEventSubscriptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SubscriptionName: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeHsmClientCertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        HsmClientCertificateIdentifier: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeHsmConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        HsmConfigurationIdentifier: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeNodeConfigurationOptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ActionType: str,
        SnapshotIdentifier: str = None,
        OwnerAccount: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeOrderableClusterOptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClusterVersion: str = None,
        NodeType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeReservedNodeOfferings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ReservedNodeOfferingId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeReservedNodes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ReservedNodeId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeSnapshotCopyGrants(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SnapshotCopyGrantName: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSnapshotSchedules(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClusterIdentifier: str = None,
        ScheduleIdentifier: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTableRestoreStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClusterIdentifier: str = None,
        TableRestoreRequestId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ResourceName: str = None,
        ResourceType: str = None,
        TagKeys: List[Any] = None,
        TagValues: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetReservedNodeExchangeOfferings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ReservedNodeId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
