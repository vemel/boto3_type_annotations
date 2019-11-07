from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeClusterDbRevisions(Paginator):
    def paginate(
        self,
        ClusterIdentifier: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClusterParameterGroups(Paginator):
    def paginate(
        self,
        ParameterGroupName: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClusterParameters(Paginator):
    def paginate(
        self,
        ParameterGroupName: str,
        Source: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClusterSecurityGroups(Paginator):
    def paginate(
        self,
        ClusterSecurityGroupName: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClusterSnapshots(Paginator):
    def paginate(
        self,
        ClusterIdentifier: Optional[str] = None,
        SnapshotIdentifier: Optional[str] = None,
        SnapshotType: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        OwnerAccount: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        ClusterExists: Optional[bool] = None,
        SortingEntities: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClusterSubnetGroups(Paginator):
    def paginate(
        self,
        ClusterSubnetGroupName: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClusterTracks(Paginator):
    def paginate(
        self,
        MaintenanceTrackName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClusterVersions(Paginator):
    def paginate(
        self,
        ClusterVersion: Optional[str] = None,
        ClusterParameterGroupFamily: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClusters(Paginator):
    def paginate(
        self,
        ClusterIdentifier: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDefaultClusterParameters(Paginator):
    def paginate(
        self,
        ParameterGroupFamily: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEventSubscriptions(Paginator):
    def paginate(
        self,
        SubscriptionName: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEvents(Paginator):
    def paginate(
        self,
        SourceIdentifier: Optional[str] = None,
        SourceType: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        Duration: Optional[int] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeHsmClientCertificates(Paginator):
    def paginate(
        self,
        HsmClientCertificateIdentifier: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeHsmConfigurations(Paginator):
    def paginate(
        self,
        HsmConfigurationIdentifier: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeNodeConfigurationOptions(Paginator):
    def paginate(
        self,
        ActionType: str,
        SnapshotIdentifier: Optional[str] = None,
        OwnerAccount: Optional[str] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeOrderableClusterOptions(Paginator):
    def paginate(
        self,
        ClusterVersion: Optional[str] = None,
        NodeType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeReservedNodeOfferings(Paginator):
    def paginate(
        self,
        ReservedNodeOfferingId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeReservedNodes(Paginator):
    def paginate(
        self,
        ReservedNodeId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSnapshotCopyGrants(Paginator):
    def paginate(
        self,
        SnapshotCopyGrantName: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSnapshotSchedules(Paginator):
    def paginate(
        self,
        ClusterIdentifier: Optional[str] = None,
        ScheduleIdentifier: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTableRestoreStatus(Paginator):
    def paginate(
        self,
        ClusterIdentifier: Optional[str] = None,
        TableRestoreRequestId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTags(Paginator):
    def paginate(
        self,
        ResourceName: Optional[str] = None,
        ResourceType: Optional[str] = None,
        TagKeys: Optional[List] = None,
        TagValues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetReservedNodeExchangeOfferings(Paginator):
    def paginate(
        self,
        ReservedNodeId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

