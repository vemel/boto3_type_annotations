from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeAddresses(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListClusterJobs(Paginator):
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListClusters(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListCompatibleImages(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListJobs(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

