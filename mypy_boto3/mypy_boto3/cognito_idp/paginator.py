from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class AdminListGroupsForUser(Paginator):
    def paginate(
        self,
        Username: str,
        UserPoolId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class AdminListUserAuthEvents(Paginator):
    def paginate(
        self,
        UserPoolId: str,
        Username: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListGroups(Paginator):
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListIdentityProviders(Paginator):
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListResourceServers(Paginator):
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUserPoolClients(Paginator):
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUserPools(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUsers(Paginator):
    def paginate(
        self,
        UserPoolId: str,
        AttributesToGet: Optional[List] = None,
        Filter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUsersInGroup(Paginator):
    def paginate(
        self,
        UserPoolId: str,
        GroupName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

