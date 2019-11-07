from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeAlarmHistory(Paginator):
    def paginate(
        self,
        AlarmName: Optional[str] = None,
        HistoryItemType: Optional[str] = None,
        StartDate: Optional[datetime] = None,
        EndDate: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeAlarms(Paginator):
    def paginate(
        self,
        AlarmNames: Optional[List] = None,
        AlarmNamePrefix: Optional[str] = None,
        StateValue: Optional[str] = None,
        ActionPrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetMetricData(Paginator):
    def paginate(
        self,
        MetricDataQueries: List,
        StartTime: datetime,
        EndTime: datetime,
        ScanBy: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDashboards(Paginator):
    def paginate(
        self,
        DashboardNamePrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListMetrics(Paginator):
    def paginate(
        self,
        Namespace: Optional[str] = None,
        MetricName: Optional[str] = None,
        Dimensions: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

