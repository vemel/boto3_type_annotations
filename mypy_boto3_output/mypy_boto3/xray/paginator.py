from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class BatchGetTraces(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, TraceIds: List[Any], PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetSamplingRules(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetSamplingStatisticSummaries(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetServiceGraph(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetTimeSeriesServiceStatistics(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        EntitySelectorExpression: str = None,
        Period: int = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetTraceGraph(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, TraceIds: List[Any], PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetTraceSummaries(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        TimeRangeType: str = None,
        Sampling: bool = None,
        SamplingStrategy: Dict[str, Any] = None,
        FilterExpression: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
