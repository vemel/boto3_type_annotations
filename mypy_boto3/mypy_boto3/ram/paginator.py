from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class GetResourcePolicies(Paginator):
    def paginate(
        self,
        resourceArns: List,
        principal: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetResourceShareAssociations(Paginator):
    def paginate(
        self,
        associationType: str,
        resourceShareArns: Optional[List] = None,
        resourceArn: Optional[str] = None,
        principal: Optional[str] = None,
        associationStatus: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetResourceShareInvitations(Paginator):
    def paginate(
        self,
        resourceShareInvitationArns: Optional[List] = None,
        resourceShareArns: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetResourceShares(Paginator):
    def paginate(
        self,
        resourceOwner: str,
        resourceShareArns: Optional[List] = None,
        resourceShareStatus: Optional[str] = None,
        name: Optional[str] = None,
        tagFilters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPrincipals(Paginator):
    def paginate(
        self,
        resourceOwner: str,
        resourceArn: Optional[str] = None,
        principals: Optional[List] = None,
        resourceType: Optional[str] = None,
        resourceShareArns: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListResources(Paginator):
    def paginate(
        self,
        resourceOwner: str,
        principal: Optional[str] = None,
        resourceType: Optional[str] = None,
        resourceArns: Optional[List] = None,
        resourceShareArns: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

