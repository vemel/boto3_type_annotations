from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeAccountLimits(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        pass


class DescribeLoadBalancers(Paginator):
    def paginate(self, LoadBalancerNames: List = None, PaginationConfig: Dict = None) -> Dict:
        pass
