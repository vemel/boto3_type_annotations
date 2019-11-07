from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListAliases(Paginator):
    def paginate(
        self,
        OrganizationId: str,
        EntityId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListGroupMembers(Paginator):
    def paginate(
        self,
        OrganizationId: str,
        GroupId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListGroups(Paginator):
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListMailboxPermissions(Paginator):
    def paginate(
        self,
        OrganizationId: str,
        EntityId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOrganizations(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListResourceDelegates(Paginator):
    def paginate(
        self,
        OrganizationId: str,
        ResourceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListResources(Paginator):
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUsers(Paginator):
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

