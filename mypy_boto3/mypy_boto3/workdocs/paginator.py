from datetime import datetime
from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeActivities(Paginator):
    def paginate(
        self,
        AuthenticationToken: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        OrganizationId: Optional[str] = None,
        ActivityTypes: Optional[str] = None,
        ResourceId: Optional[str] = None,
        UserId: Optional[str] = None,
        IncludeIndirectActivities: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeComments(Paginator):
    def paginate(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDocumentVersions(Paginator):
    def paginate(
        self,
        DocumentId: str,
        AuthenticationToken: Optional[str] = None,
        Include: Optional[str] = None,
        Fields: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeFolderContents(Paginator):
    def paginate(
        self,
        FolderId: str,
        AuthenticationToken: Optional[str] = None,
        Sort: Optional[str] = None,
        Order: Optional[str] = None,
        Type: Optional[str] = None,
        Include: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeGroups(Paginator):
    def paginate(
        self,
        SearchQuery: str,
        AuthenticationToken: Optional[str] = None,
        OrganizationId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeNotificationSubscriptions(Paginator):
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeResourcePermissions(Paginator):
    def paginate(
        self,
        ResourceId: str,
        AuthenticationToken: Optional[str] = None,
        PrincipalId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeRootFolders(Paginator):
    def paginate(
        self,
        AuthenticationToken: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeUsers(Paginator):
    def paginate(
        self,
        AuthenticationToken: Optional[str] = None,
        OrganizationId: Optional[str] = None,
        UserIds: Optional[str] = None,
        Query: Optional[str] = None,
        Include: Optional[str] = None,
        Order: Optional[str] = None,
        Sort: Optional[str] = None,
        Fields: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

