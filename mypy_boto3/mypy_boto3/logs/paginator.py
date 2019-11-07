from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeDestinations(Paginator):
    def paginate(
        self,
        DestinationNamePrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeExportTasks(Paginator):
    def paginate(
        self,
        taskId: Optional[str] = None,
        statusCode: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeLogGroups(Paginator):
    def paginate(
        self,
        logGroupNamePrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeLogStreams(Paginator):
    def paginate(
        self,
        logGroupName: str,
        logStreamNamePrefix: Optional[str] = None,
        orderBy: Optional[str] = None,
        descending: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMetricFilters(Paginator):
    def paginate(
        self,
        logGroupName: Optional[str] = None,
        filterNamePrefix: Optional[str] = None,
        metricName: Optional[str] = None,
        metricNamespace: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeQueries(Paginator):
    def paginate(
        self,
        logGroupName: Optional[str] = None,
        status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeResourcePolicies(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSubscriptionFilters(Paginator):
    def paginate(
        self,
        logGroupName: str,
        filterNamePrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class FilterLogEvents(Paginator):
    def paginate(
        self,
        logGroupName: str,
        logStreamNames: Optional[List] = None,
        logStreamNamePrefix: Optional[str] = None,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        filterPattern: Optional[str] = None,
        interleaved: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

