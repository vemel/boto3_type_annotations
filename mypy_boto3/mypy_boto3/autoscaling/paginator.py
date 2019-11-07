from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeAutoScalingGroups(Paginator):
    def paginate(
        self,
        AutoScalingGroupNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeAutoScalingInstances(Paginator):
    def paginate(
        self,
        InstanceIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeLaunchConfigurations(Paginator):
    def paginate(
        self,
        LaunchConfigurationNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeLoadBalancerTargetGroups(Paginator):
    def paginate(
        self,
        AutoScalingGroupName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeLoadBalancers(Paginator):
    def paginate(
        self,
        AutoScalingGroupName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeNotificationConfigurations(Paginator):
    def paginate(
        self,
        AutoScalingGroupNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribePolicies(Paginator):
    def paginate(
        self,
        AutoScalingGroupName: Optional[str] = None,
        PolicyNames: Optional[List] = None,
        PolicyTypes: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeScalingActivities(Paginator):
    def paginate(
        self,
        ActivityIds: Optional[List] = None,
        AutoScalingGroupName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeScheduledActions(Paginator):
    def paginate(
        self,
        AutoScalingGroupName: Optional[str] = None,
        ScheduledActionNames: Optional[List] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTags(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

