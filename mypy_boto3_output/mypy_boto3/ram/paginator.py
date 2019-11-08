from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class GetResourcePolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        resourceArns: List[Any],
        principal: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetResourceShareAssociations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        associationType: str,
        resourceShareArns: List[Any] = None,
        resourceArn: str = None,
        principal: str = None,
        associationStatus: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetResourceShareInvitations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        resourceShareInvitationArns: List[Any] = None,
        resourceShareArns: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetResourceShares(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        resourceOwner: str,
        resourceShareArns: List[Any] = None,
        resourceShareStatus: str = None,
        name: str = None,
        tagFilters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPrincipals(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        resourceOwner: str,
        resourceArn: str = None,
        principals: List[Any] = None,
        resourceType: str = None,
        resourceShareArns: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        resourceOwner: str,
        principal: str = None,
        resourceType: str = None,
        resourceArns: List[Any] = None,
        resourceShareArns: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
