from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class DescribeBackups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: Dict[str, Any] = None,
        SortAscending: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
