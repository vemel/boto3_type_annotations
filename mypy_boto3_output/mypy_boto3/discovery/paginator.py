from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeAgents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        agentIds: List[Any] = None,
        filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeContinuousExports(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, exportIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeExportConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, exportIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeExportTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        exportIds: List[Any] = None,
        filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        configurationType: str,
        filters: List[Any] = None,
        orderBy: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
