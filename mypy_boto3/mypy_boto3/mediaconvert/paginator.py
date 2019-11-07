from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeEndpoints(Paginator):
    def paginate(
        self,
        Mode: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListJobTemplates(Paginator):
    def paginate(
        self,
        Category: Optional[str] = None,
        ListBy: Optional[str] = None,
        Order: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListJobs(Paginator):
    def paginate(
        self,
        Order: Optional[str] = None,
        Queue: Optional[str] = None,
        Status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPresets(Paginator):
    def paginate(
        self,
        Category: Optional[str] = None,
        ListBy: Optional[str] = None,
        Order: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListQueues(Paginator):
    def paginate(
        self,
        ListBy: Optional[str] = None,
        Order: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

