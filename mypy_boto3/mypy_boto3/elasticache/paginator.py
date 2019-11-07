from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeCacheClusters(Paginator):
    def paginate(
        self,
        CacheClusterId: Optional[str] = None,
        ShowCacheNodeInfo: Optional[bool] = None,
        ShowCacheClustersNotInReplicationGroups: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeCacheEngineVersions(Paginator):
    def paginate(
        self,
        Engine: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        CacheParameterGroupFamily: Optional[str] = None,
        DefaultOnly: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeCacheParameterGroups(Paginator):
    def paginate(
        self,
        CacheParameterGroupName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeCacheParameters(Paginator):
    def paginate(
        self,
        CacheParameterGroupName: str,
        Source: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeCacheSecurityGroups(Paginator):
    def paginate(
        self,
        CacheSecurityGroupName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeCacheSubnetGroups(Paginator):
    def paginate(
        self,
        CacheSubnetGroupName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEngineDefaultParameters(Paginator):
    def paginate(
        self,
        CacheParameterGroupFamily: str,
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



class DescribeReplicationGroups(Paginator):
    def paginate(
        self,
        ReplicationGroupId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeReservedCacheNodes(Paginator):
    def paginate(
        self,
        ReservedCacheNodeId: Optional[str] = None,
        ReservedCacheNodesOfferingId: Optional[str] = None,
        CacheNodeType: Optional[str] = None,
        Duration: Optional[str] = None,
        ProductDescription: Optional[str] = None,
        OfferingType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeReservedCacheNodesOfferings(Paginator):
    def paginate(
        self,
        ReservedCacheNodesOfferingId: Optional[str] = None,
        CacheNodeType: Optional[str] = None,
        Duration: Optional[str] = None,
        ProductDescription: Optional[str] = None,
        OfferingType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeServiceUpdates(Paginator):
    def paginate(
        self,
        ServiceUpdateName: Optional[str] = None,
        ServiceUpdateStatus: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSnapshots(Paginator):
    def paginate(
        self,
        ReplicationGroupId: Optional[str] = None,
        CacheClusterId: Optional[str] = None,
        SnapshotName: Optional[str] = None,
        SnapshotSource: Optional[str] = None,
        ShowNodeGroupConfig: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeUpdateActions(Paginator):
    def paginate(
        self,
        ServiceUpdateName: Optional[str] = None,
        ReplicationGroupIds: Optional[List] = None,
        CacheClusterIds: Optional[List] = None,
        Engine: Optional[str] = None,
        ServiceUpdateStatus: Optional[List] = None,
        ServiceUpdateTimeRange: Optional[Dict] = None,
        UpdateActionStatus: Optional[List] = None,
        ShowNodeLevelUpdateStatus: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

