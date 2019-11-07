from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeAccountModifications(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeIpGroups(Paginator):
    def paginate(
        self,
        GroupIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeWorkspaceBundles(Paginator):
    def paginate(
        self,
        BundleIds: Optional[List] = None,
        Owner: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeWorkspaceDirectories(Paginator):
    def paginate(
        self,
        DirectoryIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeWorkspaceImages(Paginator):
    def paginate(
        self,
        ImageIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeWorkspaces(Paginator):
    def paginate(
        self,
        WorkspaceIds: Optional[List] = None,
        DirectoryId: Optional[str] = None,
        UserName: Optional[str] = None,
        BundleId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeWorkspacesConnectionStatus(Paginator):
    def paginate(
        self,
        WorkspaceIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAvailableManagementCidrRanges(Paginator):
    def paginate(
        self,
        ManagementCidrRangeConstraint: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

