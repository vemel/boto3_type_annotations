from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_scaling_plan(
        self,
        ScalingPlanName: str,
        ApplicationSource: Dict[str, Any],
        ScalingInstructions: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_scaling_plan(
        self, ScalingPlanName: str, ScalingPlanVersion: int
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_scaling_plan_resources(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_scaling_plans(
        self,
        ScalingPlanNames: List[Any] = None,
        ScalingPlanVersion: int = None,
        ApplicationSources: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_scaling_plan_resource_forecast_data(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        ServiceNamespace: str,
        ResourceId: str,
        ScalableDimension: str,
        ForecastDataType: str,
        StartTime: datetime,
        EndTime: datetime,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def update_scaling_plan(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        ApplicationSource: Dict[str, Any] = None,
        ScalingInstructions: List[Any] = None,
    ) -> Dict[str, Any]:
        pass
