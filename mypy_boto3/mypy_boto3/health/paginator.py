from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeAffectedEntities(Paginator):
    def paginate(
        self,
        filter: Dict,
        locale: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEventAggregates(Paginator):
    def paginate(
        self,
        aggregateField: str,
        filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEventTypes(Paginator):
    def paginate(
        self,
        filter: Optional[Dict] = None,
        locale: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEvents(Paginator):
    def paginate(
        self,
        filter: Optional[Dict] = None,
        locale: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

