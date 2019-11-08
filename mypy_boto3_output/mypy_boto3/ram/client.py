from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def accept_resource_share_invitation(
        self, resourceShareInvitationArn: str, clientToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_resource_share(
        self,
        resourceShareArn: str,
        resourceArns: List[Any] = None,
        principals: List[Any] = None,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_resource_share(
        self,
        name: str,
        resourceArns: List[Any] = None,
        principals: List[Any] = None,
        tags: List[Any] = None,
        allowExternalPrincipals: bool = None,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_resource_share(
        self, resourceShareArn: str, clientToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_resource_share(
        self,
        resourceShareArn: str,
        resourceArns: List[Any] = None,
        principals: List[Any] = None,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_sharing_with_aws_organization(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_resource_policies(
        self,
        resourceArns: List[Any],
        principal: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_resource_share_associations(
        self,
        associationType: str,
        resourceShareArns: List[Any] = None,
        resourceArn: str = None,
        principal: str = None,
        associationStatus: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_resource_share_invitations(
        self,
        resourceShareInvitationArns: List[Any] = None,
        resourceShareArns: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_resource_shares(
        self,
        resourceOwner: str,
        resourceShareArns: List[Any] = None,
        resourceShareStatus: str = None,
        name: str = None,
        tagFilters: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_pending_invitation_resources(
        self,
        resourceShareInvitationArn: str,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_principals(
        self,
        resourceOwner: str,
        resourceArn: str = None,
        principals: List[Any] = None,
        resourceType: str = None,
        resourceShareArns: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resources(
        self,
        resourceOwner: str,
        principal: str = None,
        resourceType: str = None,
        resourceArns: List[Any] = None,
        resourceShareArns: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reject_resource_share_invitation(
        self, resourceShareInvitationArn: str, clientToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceShareArn: str, tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(
        self, resourceShareArn: str, tagKeys: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_resource_share(
        self,
        resourceShareArn: str,
        name: str = None,
        allowExternalPrincipals: bool = None,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        pass
