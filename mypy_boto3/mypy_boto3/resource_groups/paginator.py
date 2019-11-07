from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListGroupResources(Paginator):
    def paginate(
        self,
        GroupName: str,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListGroups(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchResources(Paginator):
    def paginate(
        self,
        ResourceQuery: Dict,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

