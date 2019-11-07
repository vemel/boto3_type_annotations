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



class DescribeLoadBalancers(Paginator):
    def paginate(
        self,
        LoadBalancerNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

