from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class GetAccountAuthorizationDetails(Paginator):
    def paginate(
        self,
        Filter: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetGroup(Paginator):
    def paginate(
        self,
        GroupName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAccessKeys(Paginator):
    def paginate(
        self,
        UserName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAccountAliases(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAttachedGroupPolicies(Paginator):
    def paginate(
        self,
        GroupName: str,
        PathPrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAttachedRolePolicies(Paginator):
    def paginate(
        self,
        RoleName: str,
        PathPrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAttachedUserPolicies(Paginator):
    def paginate(
        self,
        UserName: str,
        PathPrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEntitiesForPolicy(Paginator):
    def paginate(
        self,
        PolicyArn: str,
        EntityFilter: Optional[str] = None,
        PathPrefix: Optional[str] = None,
        PolicyUsageFilter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListGroupPolicies(Paginator):
    def paginate(
        self,
        GroupName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListGroups(Paginator):
    def paginate(
        self,
        PathPrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListGroupsForUser(Paginator):
    def paginate(
        self,
        UserName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListInstanceProfiles(Paginator):
    def paginate(
        self,
        PathPrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListInstanceProfilesForRole(Paginator):
    def paginate(
        self,
        RoleName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListMFADevices(Paginator):
    def paginate(
        self,
        UserName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPolicies(Paginator):
    def paginate(
        self,
        Scope: Optional[str] = None,
        OnlyAttached: Optional[bool] = None,
        PathPrefix: Optional[str] = None,
        PolicyUsageFilter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPolicyVersions(Paginator):
    def paginate(
        self,
        PolicyArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRolePolicies(Paginator):
    def paginate(
        self,
        RoleName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRoles(Paginator):
    def paginate(
        self,
        PathPrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSSHPublicKeys(Paginator):
    def paginate(
        self,
        UserName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListServerCertificates(Paginator):
    def paginate(
        self,
        PathPrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSigningCertificates(Paginator):
    def paginate(
        self,
        UserName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUserPolicies(Paginator):
    def paginate(
        self,
        UserName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUsers(Paginator):
    def paginate(
        self,
        PathPrefix: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListVirtualMFADevices(Paginator):
    def paginate(
        self,
        AssignmentStatus: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SimulateCustomPolicy(Paginator):
    def paginate(
        self,
        PolicyInputList: List,
        ActionNames: List,
        ResourceArns: Optional[List] = None,
        ResourcePolicy: Optional[str] = None,
        ResourceOwner: Optional[str] = None,
        CallerArn: Optional[str] = None,
        ContextEntries: Optional[List] = None,
        ResourceHandlingOption: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SimulatePrincipalPolicy(Paginator):
    def paginate(
        self,
        PolicySourceArn: str,
        ActionNames: List,
        PolicyInputList: Optional[List] = None,
        ResourceArns: Optional[List] = None,
        ResourcePolicy: Optional[str] = None,
        ResourceOwner: Optional[str] = None,
        CallerArn: Optional[str] = None,
        ContextEntries: Optional[List] = None,
        ResourceHandlingOption: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

