from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class GetQueryResults(Paginator):
    def paginate(
        self,
        QueryExecutionId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListNamedQueries(Paginator):
    def paginate(
        self,
        WorkGroup: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListQueryExecutions(Paginator):
    def paginate(
        self,
        WorkGroup: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

