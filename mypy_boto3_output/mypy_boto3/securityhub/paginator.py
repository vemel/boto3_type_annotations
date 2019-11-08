from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class GetEnabledStandards(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StandardsSubscriptionArns: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetFindings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: Dict[str, Any] = None,
        SortCriteria: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetInsights(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, InsightArns: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListEnabledProductsForImport(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListInvitations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListMembers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, OnlyAssociated: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
