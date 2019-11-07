from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeAgents(Paginator):
    def paginate(
        self,
        agentIds: Optional[List] = None,
        filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeContinuousExports(Paginator):
    def paginate(
        self,
        exportIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeExportConfigurations(Paginator):
    def paginate(
        self,
        exportIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeExportTasks(Paginator):
    def paginate(
        self,
        exportIds: Optional[List] = None,
        filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTags(Paginator):
    def paginate(
        self,
        filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListConfigurations(Paginator):
    def paginate(
        self,
        configurationType: str,
        filters: Optional[List] = None,
        orderBy: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

