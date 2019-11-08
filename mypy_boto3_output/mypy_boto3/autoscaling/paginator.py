from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeAutoScalingGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AutoScalingGroupNames: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeAutoScalingInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, InstanceIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeLaunchConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        LaunchConfigurationNames: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeLoadBalancerTargetGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AutoScalingGroupName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeLoadBalancers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AutoScalingGroupName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeNotificationConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AutoScalingGroupNames: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribePolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AutoScalingGroupName: str = None,
        PolicyNames: List[Any] = None,
        PolicyTypes: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeScalingActivities(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ActivityIds: List[Any] = None,
        AutoScalingGroupName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeScheduledActions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AutoScalingGroupName: str = None,
        ScheduledActionNames: List[Any] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
