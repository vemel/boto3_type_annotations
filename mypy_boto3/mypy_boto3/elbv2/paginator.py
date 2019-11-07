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



class DescribeListenerCertificates(Paginator):
    def paginate(
        self,
        ListenerArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeListeners(Paginator):
    def paginate(
        self,
        LoadBalancerArn: Optional[str] = None,
        ListenerArns: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeLoadBalancers(Paginator):
    def paginate(
        self,
        LoadBalancerArns: Optional[List] = None,
        Names: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeRules(Paginator):
    def paginate(
        self,
        ListenerArn: Optional[str] = None,
        RuleArns: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSSLPolicies(Paginator):
    def paginate(
        self,
        Names: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTargetGroups(Paginator):
    def paginate(
        self,
        LoadBalancerArn: Optional[str] = None,
        TargetGroupArns: Optional[List] = None,
        Names: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

