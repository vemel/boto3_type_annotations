from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeAlarmHistory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AlarmName: str = None,
        HistoryItemType: str = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeAlarms(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AlarmNames: List[Any] = None,
        AlarmNamePrefix: str = None,
        StateValue: str = None,
        ActionPrefix: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetMetricData(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        MetricDataQueries: List[Any],
        StartTime: datetime,
        EndTime: datetime,
        ScanBy: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListDashboards(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DashboardNamePrefix: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListMetrics(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
