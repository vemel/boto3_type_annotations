from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeCacheClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CacheClusterId: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeCacheEngineVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        DefaultOnly: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeCacheParameterGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CacheParameterGroupName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeCacheParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CacheParameterGroupName: str,
        Source: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeCacheSecurityGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CacheSecurityGroupName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeCacheSubnetGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, CacheSubnetGroupName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeEngineDefaultParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, CacheParameterGroupFamily: str, PaginationConfig: Dict[str, Any] = None
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


class DescribeReplicationGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ReplicationGroupId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeReservedCacheNodes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeReservedCacheNodesOfferings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeServiceUpdates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSnapshots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        ShowNodeGroupConfig: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeUpdateActions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[Any] = None,
        CacheClusterIds: List[Any] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[Any] = None,
        ServiceUpdateTimeRange: Dict[str, Any] = None,
        UpdateActionStatus: List[Any] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
