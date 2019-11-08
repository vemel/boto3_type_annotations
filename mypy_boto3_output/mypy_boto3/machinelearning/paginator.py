from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class DescribeBatchPredictions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
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
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDataSources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
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
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEvaluations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
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
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMLModels(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
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
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
