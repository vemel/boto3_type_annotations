from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeBackups(Paginator):
    def paginate(
        self,
        Filters: Optional[Dict] = None,
        SortAscending: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClusters(Paginator):
    def paginate(
        self,
        Filters: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTags(Paginator):
    def paginate(
        self,
        ResourceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

