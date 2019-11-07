from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeObjects(Paginator):
    def paginate(
        self,
        pipelineId: str,
        objectIds: List,
        evaluateExpressions: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPipelines(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class QueryObjects(Paginator):
    def paginate(
        self,
        pipelineId: str,
        sphere: str,
        query: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

