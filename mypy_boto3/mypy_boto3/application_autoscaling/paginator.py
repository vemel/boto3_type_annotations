from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeScalableTargets(Paginator):
    def paginate(
        self,
        ServiceNamespace: str,
        ResourceIds: Optional[List] = None,
        ScalableDimension: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeScalingActivities(Paginator):
    def paginate(
        self,
        ServiceNamespace: str,
        ResourceId: Optional[str] = None,
        ScalableDimension: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeScalingPolicies(Paginator):
    def paginate(
        self,
        ServiceNamespace: str,
        PolicyNames: Optional[List] = None,
        ResourceId: Optional[str] = None,
        ScalableDimension: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeScheduledActions(Paginator):
    def paginate(
        self,
        ServiceNamespace: str,
        ScheduledActionNames: Optional[List] = None,
        ResourceId: Optional[str] = None,
        ScalableDimension: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

