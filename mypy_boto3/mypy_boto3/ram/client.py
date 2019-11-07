from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_resource_share_invitation(
        self,
        resourceShareInvitationArn: str,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_resource_share(
        self,
        resourceShareArn: str,
        resourceArns: Optional[List] = None,
        principals: Optional[List] = None,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_resource_share(
        self,
        name: str,
        resourceArns: Optional[List] = None,
        principals: Optional[List] = None,
        tags: Optional[List] = None,
        allowExternalPrincipals: Optional[bool] = None,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_resource_share(
        self,
        resourceShareArn: str,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_resource_share(
        self,
        resourceShareArn: str,
        resourceArns: Optional[List] = None,
        principals: Optional[List] = None,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def enable_sharing_with_aws_organization(
        self,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_resource_policies(
        self,
        resourceArns: List,
        principal: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_resource_share_associations(
        self,
        associationType: str,
        resourceShareArns: Optional[List] = None,
        resourceArn: Optional[str] = None,
        principal: Optional[str] = None,
        associationStatus: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_resource_share_invitations(
        self,
        resourceShareInvitationArns: Optional[List] = None,
        resourceShareArns: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_resource_shares(
        self,
        resourceOwner: str,
        resourceShareArns: Optional[List] = None,
        resourceShareStatus: Optional[str] = None,
        name: Optional[str] = None,
        tagFilters: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_pending_invitation_resources(
        self,
        resourceShareInvitationArn: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_principals(
        self,
        resourceOwner: str,
        resourceArn: Optional[str] = None,
        principals: Optional[List] = None,
        resourceType: Optional[str] = None,
        resourceShareArns: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_resources(
        self,
        resourceOwner: str,
        principal: Optional[str] = None,
        resourceType: Optional[str] = None,
        resourceArns: Optional[List] = None,
        resourceShareArns: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def reject_resource_share_invitation(
        self,
        resourceShareInvitationArn: str,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceShareArn: str,
        tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceShareArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_resource_share(
        self,
        resourceShareArn: str,
        name: Optional[str] = None,
        allowExternalPrincipals: Optional[bool] = None,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass

