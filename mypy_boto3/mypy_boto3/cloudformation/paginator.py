from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeAccountLimits(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeChangeSet(Paginator):
    def paginate(
        self,
        ChangeSetName: str,
        StackName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeStackEvents(Paginator):
    def paginate(
        self,
        StackName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeStacks(Paginator):
    def paginate(
        self,
        StackName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListChangeSets(Paginator):
    def paginate(
        self,
        StackName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListExports(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListImports(Paginator):
    def paginate(
        self,
        ExportName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStackInstances(Paginator):
    def paginate(
        self,
        StackSetName: str,
        StackInstanceAccount: Optional[str] = None,
        StackInstanceRegion: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStackResources(Paginator):
    def paginate(
        self,
        StackName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStackSetOperationResults(Paginator):
    def paginate(
        self,
        StackSetName: str,
        OperationId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStackSetOperations(Paginator):
    def paginate(
        self,
        StackSetName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStackSets(Paginator):
    def paginate(
        self,
        Status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStacks(Paginator):
    def paginate(
        self,
        StackStatusFilter: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

