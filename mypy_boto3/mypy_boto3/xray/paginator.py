from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class BatchGetTraces(Paginator):
    def paginate(
        self,
        TraceIds: List,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetGroups(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetSamplingRules(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetSamplingStatisticSummaries(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetServiceGraph(Paginator):
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: Optional[str] = None,
        GroupARN: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTimeSeriesServiceStatistics(Paginator):
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: Optional[str] = None,
        GroupARN: Optional[str] = None,
        EntitySelectorExpression: Optional[str] = None,
        Period: Optional[int] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTraceGraph(Paginator):
    def paginate(
        self,
        TraceIds: List,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTraceSummaries(Paginator):
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        TimeRangeType: Optional[str] = None,
        Sampling: Optional[bool] = None,
        SamplingStrategy: Optional[Dict] = None,
        FilterExpression: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

