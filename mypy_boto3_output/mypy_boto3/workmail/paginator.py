from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListAliases(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        OrganizationId: str,
        EntityId: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListGroupMembers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, OrganizationId: str, GroupId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, OrganizationId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListMailboxPermissions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        OrganizationId: str,
        EntityId: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListOrganizations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListResourceDelegates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        OrganizationId: str,
        ResourceId: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, OrganizationId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUsers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, OrganizationId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
