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


    def delete_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: str,
        ResourceId: str,
        ScalableDimension: str,
    ) -> Dict:
        pass


    def delete_scheduled_action(
        self,
        ServiceNamespace: str,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: str,
    ) -> Dict:
        pass


    def deregister_scalable_target(
        self,
        ServiceNamespace: str,
        ResourceId: str,
        ScalableDimension: str,
    ) -> Dict:
        pass


    def describe_scalable_targets(
        self,
        ServiceNamespace: str,
        ResourceIds: Optional[List] = None,
        ScalableDimension: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_scaling_activities(
        self,
        ServiceNamespace: str,
        ResourceId: Optional[str] = None,
        ScalableDimension: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_scaling_policies(
        self,
        ServiceNamespace: str,
        PolicyNames: Optional[List] = None,
        ResourceId: Optional[str] = None,
        ScalableDimension: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_scheduled_actions(
        self,
        ServiceNamespace: str,
        ScheduledActionNames: Optional[List] = None,
        ResourceId: Optional[str] = None,
        ScalableDimension: Optional[str] = None,
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


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def put_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: str,
        ResourceId: str,
        ScalableDimension: str,
        PolicyType: Optional[str] = None,
        StepScalingPolicyConfiguration: Optional[Dict] = None,
        TargetTrackingScalingPolicyConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def put_scheduled_action(
        self,
        ServiceNamespace: str,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: str,
        Schedule: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        ScalableTargetAction: Optional[Dict] = None,
    ) -> Dict:
        pass


    def register_scalable_target(
        self,
        ServiceNamespace: str,
        ResourceId: str,
        ScalableDimension: str,
        MinCapacity: Optional[int] = None,
        MaxCapacity: Optional[int] = None,
        RoleARN: Optional[str] = None,
        SuspendedState: Optional[Dict] = None,
    ) -> Dict:
        pass

