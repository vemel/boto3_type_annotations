from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeDirectoryConfigs(Paginator):
    def paginate(
        self,
        DirectoryNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeFleets(Paginator):
    def paginate(
        self,
        Names: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeImageBuilders(Paginator):
    def paginate(
        self,
        Names: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeImages(Paginator):
    def paginate(
        self,
        Names: Optional[List] = None,
        Arns: Optional[List] = None,
        Type: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSessions(Paginator):
    def paginate(
        self,
        StackName: str,
        FleetName: str,
        UserId: Optional[str] = None,
        AuthenticationType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeStacks(Paginator):
    def paginate(
        self,
        Names: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeUserStackAssociations(Paginator):
    def paginate(
        self,
        StackName: Optional[str] = None,
        UserName: Optional[str] = None,
        AuthenticationType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeUsers(Paginator):
    def paginate(
        self,
        AuthenticationType: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAssociatedFleets(Paginator):
    def paginate(
        self,
        StackName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAssociatedStacks(Paginator):
    def paginate(
        self,
        FleetName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

