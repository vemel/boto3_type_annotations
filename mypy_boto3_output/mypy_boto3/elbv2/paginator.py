from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeAccountLimits(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class DescribeListenerCertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ListenerArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeListeners(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        LoadBalancerArn: str = None,
        ListenerArns: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeLoadBalancers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        LoadBalancerArns: List[Any] = None,
        Names: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeRules(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ListenerArn: str = None,
        RuleArns: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSSLPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Names: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeTargetGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[Any] = None,
        Names: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
