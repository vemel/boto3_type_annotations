from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeScalingPlanResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeScalingPlans(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ScalingPlanNames: List[Any] = None,
        ScalingPlanVersion: int = None,
        ApplicationSources: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
