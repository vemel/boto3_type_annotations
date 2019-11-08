from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeScalableTargets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceNamespace: str,
        ResourceIds: List[Any] = None,
        ScalableDimension: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeScalingActivities(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceNamespace: str,
        ResourceId: str = None,
        ScalableDimension: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeScalingPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceNamespace: str,
        PolicyNames: List[Any] = None,
        ResourceId: str = None,
        ScalableDimension: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeScheduledActions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceNamespace: str,
        ScheduledActionNames: List[Any] = None,
        ResourceId: str = None,
        ScalableDimension: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
