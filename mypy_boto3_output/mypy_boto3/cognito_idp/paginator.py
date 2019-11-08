from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class AdminListGroupsForUser(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Username: str, UserPoolId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class AdminListUserAuthEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserPoolId: str, Username: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserPoolId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListIdentityProviders(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserPoolId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListResourceServers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserPoolId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUserPoolClients(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserPoolId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUserPools(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListUsers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        UserPoolId: str,
        AttributesToGet: List[Any] = None,
        Filter: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListUsersInGroup(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserPoolId: str, GroupName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
