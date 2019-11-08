from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class GetAccountAuthorizationDetails(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filter: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetGroup(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, GroupName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListAccessKeys(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListAccountAliases(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListAttachedGroupPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        GroupName: str,
        PathPrefix: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAttachedRolePolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        RoleName: str,
        PathPrefix: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAttachedUserPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        UserName: str,
        PathPrefix: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListEntitiesForPolicy(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        PolicyArn: str,
        EntityFilter: str = None,
        PathPrefix: str = None,
        PolicyUsageFilter: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListGroupPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, GroupName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PathPrefix: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListGroupsForUser(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListInstanceProfiles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PathPrefix: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListInstanceProfilesForRole(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, RoleName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListMFADevices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Scope: str = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPolicyVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PolicyArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListRolePolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, RoleName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListRoles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PathPrefix: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSSHPublicKeys(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListServerCertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PathPrefix: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSigningCertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUserPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, UserName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUsers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PathPrefix: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListVirtualMFADevices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AssignmentStatus: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class SimulateCustomPolicy(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        PolicyInputList: List[Any],
        ActionNames: List[Any],
        ResourceArns: List[Any] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[Any] = None,
        ResourceHandlingOption: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class SimulatePrincipalPolicy(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        PolicySourceArn: str,
        ActionNames: List[Any],
        PolicyInputList: List[Any] = None,
        ResourceArns: List[Any] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[Any] = None,
        ResourceHandlingOption: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
