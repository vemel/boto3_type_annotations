from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListAWSServiceAccessForOrganization(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAccounts(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAccountsForParent(Paginator):
    def paginate(
        self,
        ParentId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListChildren(Paginator):
    def paginate(
        self,
        ParentId: str,
        ChildType: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListCreateAccountStatus(Paginator):
    def paginate(
        self,
        States: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListHandshakesForAccount(Paginator):
    def paginate(
        self,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListHandshakesForOrganization(Paginator):
    def paginate(
        self,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOrganizationalUnitsForParent(Paginator):
    def paginate(
        self,
        ParentId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListParents(Paginator):
    def paginate(
        self,
        ChildId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPolicies(Paginator):
    def paginate(
        self,
        Filter: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPoliciesForTarget(Paginator):
    def paginate(
        self,
        TargetId: str,
        Filter: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRoots(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTagsForResource(Paginator):
    def paginate(
        self,
        ResourceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTargetsForPolicy(Paginator):
    def paginate(
        self,
        PolicyId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

