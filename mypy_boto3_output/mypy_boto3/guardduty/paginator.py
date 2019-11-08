from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListDetectors(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListFilters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DetectorId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListFindings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DetectorId: str,
        FindingCriteria: Dict[str, Any] = None,
        SortCriteria: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListIPSets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DetectorId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListInvitations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListMembers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DetectorId: str,
        OnlyAssociated: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListThreatIntelSets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DetectorId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
