from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class BatchPredictionAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        FilterVariable: str = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class DataSourceAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        FilterVariable: str = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class EvaluationAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        FilterVariable: str = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class MLModelAvailable(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        FilterVariable: str = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass
