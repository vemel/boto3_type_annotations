from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeClusters(Paginator):
    def paginate(
        self,
        ClusterNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDefaultParameters(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEvents(Paginator):
    def paginate(
        self,
        SourceName: Optional[str] = None,
        SourceType: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        Duration: Optional[int] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeParameterGroups(Paginator):
    def paginate(
        self,
        ParameterGroupNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeParameters(Paginator):
    def paginate(
        self,
        ParameterGroupName: str,
        Source: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSubnetGroups(Paginator):
    def paginate(
        self,
        SubnetGroupNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTags(Paginator):
    def paginate(
        self,
        ResourceName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

