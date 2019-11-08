from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListAssignmentsForHIT(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        HITId: str,
        AssignmentStatuses: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListBonusPayments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        HITId: str = None,
        AssignmentId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListHITs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListHITsForQualificationType(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, QualificationTypeId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListQualificationRequests(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, QualificationTypeId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListQualificationTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        MustBeRequestable: bool,
        Query: str = None,
        MustBeOwnedByCaller: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListReviewableHITs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        HITTypeId: str = None,
        Status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListWorkerBlocks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListWorkersWithQualificationType(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        QualificationTypeId: str,
        Status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
