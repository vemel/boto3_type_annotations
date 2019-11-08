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
    def delete_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: str,
        ResourceId: str,
        ScalableDimension: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_scheduled_action(
        self,
        ServiceNamespace: str,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_scalable_target(
        self, ServiceNamespace: str, ResourceId: str, ScalableDimension: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_scalable_targets(
        self,
        ServiceNamespace: str,
        ResourceIds: List[Any] = None,
        ScalableDimension: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_scaling_activities(
        self,
        ServiceNamespace: str,
        ResourceId: str = None,
        ScalableDimension: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_scaling_policies(
        self,
        ServiceNamespace: str,
        PolicyNames: List[Any] = None,
        ResourceId: str = None,
        ScalableDimension: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_scheduled_actions(
        self,
        ServiceNamespace: str,
        ScheduledActionNames: List[Any] = None,
        ResourceId: str = None,
        ScalableDimension: str = None,
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
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def put_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: str,
        ResourceId: str,
        ScalableDimension: str,
        PolicyType: str = None,
        StepScalingPolicyConfiguration: Dict[str, Any] = None,
        TargetTrackingScalingPolicyConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_scheduled_action(
        self,
        ServiceNamespace: str,
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: str,
        Schedule: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        ScalableTargetAction: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_scalable_target(
        self,
        ServiceNamespace: str,
        ResourceId: str,
        ScalableDimension: str,
        MinCapacity: int = None,
        MaxCapacity: int = None,
        RoleARN: str = None,
        SuspendedState: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
