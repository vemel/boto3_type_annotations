from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeComputeEnvironments(Paginator):
    def paginate(
        self,
        computeEnvironments: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeJobDefinitions(Paginator):
    def paginate(
        self,
        jobDefinitions: Optional[List] = None,
        jobDefinitionName: Optional[str] = None,
        status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeJobQueues(Paginator):
    def paginate(
        self,
        jobQueues: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListJobs(Paginator):
    def paginate(
        self,
        jobQueue: Optional[str] = None,
        arrayJobId: Optional[str] = None,
        multiNodeJobId: Optional[str] = None,
        jobStatus: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

