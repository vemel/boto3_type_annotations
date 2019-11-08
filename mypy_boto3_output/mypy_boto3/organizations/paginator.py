from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListAWSServiceAccessForOrganization(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListAccounts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListAccountsForParent(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ParentId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListChildren(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ParentId: str, ChildType: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListCreateAccountStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, States: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListHandshakesForAccount(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListHandshakesForOrganization(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListOrganizationalUnitsForParent(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ParentId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListParents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ChildId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPoliciesForTarget(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, TargetId: str, Filter: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListRoots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListTagsForResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTargetsForPolicy(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PolicyId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
