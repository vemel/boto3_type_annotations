from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_scaling_plan(
        self,
        ScalingPlanName: str,
        ApplicationSource: Dict,
        ScalingInstructions: List,
    ) -> Dict:
        pass


    def delete_scaling_plan(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
    ) -> Dict:
        pass


    def describe_scaling_plan_resources(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_scaling_plans(
        self,
        ScalingPlanNames: Optional[List] = None,
        ScalingPlanVersion: Optional[int] = None,
        ApplicationSources: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


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
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def update_scaling_plan(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        ApplicationSource: Optional[Dict] = None,
        ScalingInstructions: Optional[List] = None,
    ) -> Dict:
        pass

