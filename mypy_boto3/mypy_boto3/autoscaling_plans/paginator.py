from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeScalingPlanResources(Paginator):
    def paginate(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeScalingPlans(Paginator):
    def paginate(
        self,
        ScalingPlanNames: Optional[List] = None,
        ScalingPlanVersion: Optional[int] = None,
        ApplicationSources: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

