from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListGroupResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        GroupName: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class SearchResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceQuery: Dict[str, Any], PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
