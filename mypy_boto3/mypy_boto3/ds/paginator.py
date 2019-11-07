from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeDirectories(Paginator):
    def paginate(
        self,
        DirectoryIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDomainControllers(Paginator):
    def paginate(
        self,
        DirectoryId: str,
        DomainControllerIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSharedDirectories(Paginator):
    def paginate(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSnapshots(Paginator):
    def paginate(
        self,
        DirectoryId: Optional[str] = None,
        SnapshotIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTrusts(Paginator):
    def paginate(
        self,
        DirectoryId: Optional[str] = None,
        TrustIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListIpRoutes(Paginator):
    def paginate(
        self,
        DirectoryId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListLogSubscriptions(Paginator):
    def paginate(
        self,
        DirectoryId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSchemaExtensions(Paginator):
    def paginate(
        self,
        DirectoryId: str,
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

