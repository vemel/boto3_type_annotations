from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeBatchPredictions(Paginator):
    def paginate(
        self,
        FilterVariable: Optional[str] = None,
        EQ: Optional[str] = None,
        GT: Optional[str] = None,
        LT: Optional[str] = None,
        GE: Optional[str] = None,
        LE: Optional[str] = None,
        NE: Optional[str] = None,
        Prefix: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDataSources(Paginator):
    def paginate(
        self,
        FilterVariable: Optional[str] = None,
        EQ: Optional[str] = None,
        GT: Optional[str] = None,
        LT: Optional[str] = None,
        GE: Optional[str] = None,
        LE: Optional[str] = None,
        NE: Optional[str] = None,
        Prefix: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEvaluations(Paginator):
    def paginate(
        self,
        FilterVariable: Optional[str] = None,
        EQ: Optional[str] = None,
        GT: Optional[str] = None,
        LT: Optional[str] = None,
        GE: Optional[str] = None,
        LE: Optional[str] = None,
        NE: Optional[str] = None,
        Prefix: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMLModels(Paginator):
    def paginate(
        self,
        FilterVariable: Optional[str] = None,
        EQ: Optional[str] = None,
        GT: Optional[str] = None,
        LT: Optional[str] = None,
        GE: Optional[str] = None,
        LE: Optional[str] = None,
        NE: Optional[str] = None,
        Prefix: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

