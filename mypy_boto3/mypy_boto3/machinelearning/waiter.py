from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class BatchPredictionAvailable(Waiter):
    def wait(
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
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class DataSourceAvailable(Waiter):
    def wait(
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
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class EvaluationAvailable(Waiter):
    def wait(
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
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class MLModelAvailable(Waiter):
    def wait(
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
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass

