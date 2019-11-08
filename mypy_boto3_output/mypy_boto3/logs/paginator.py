from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeDestinations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DestinationNamePrefix: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeExportTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        taskId: str = None,
        statusCode: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeLogGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, logGroupNamePrefix: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeLogStreams(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: str = None,
        descending: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMetricFilters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        metricName: str = None,
        metricNamespace: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeQueries(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        logGroupName: str = None,
        status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeResourcePolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class DescribeSubscriptionFilters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        logGroupName: str,
        filterNamePrefix: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class FilterLogEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        logGroupName: str,
        logStreamNames: List[Any] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        interleaved: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
