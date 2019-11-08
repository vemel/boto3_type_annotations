from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeCertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeConnections(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeEndpointTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeEndpoints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeEventSubscriptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[Any] = None,
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
        EventCategories: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeOrderableReplicationInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class DescribeReplicationInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeReplicationSubnetGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeReplicationTaskAssessmentResults(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ReplicationTaskArn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeReplicationTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        WithoutSettings: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSchemas(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, EndpointArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeTableStatistics(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ReplicationTaskArn: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
