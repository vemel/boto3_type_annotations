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
    def create_application(
        self,
        ResourceGroupName: str,
        OpsCenterEnabled: bool = None,
        OpsItemSNSTopicArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_component(
        self, ResourceGroupName: str, ComponentName: str, ResourceList: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_application(self, ResourceGroupName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_component(
        self, ResourceGroupName: str, ComponentName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_application(self, ResourceGroupName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_component(
        self, ResourceGroupName: str, ComponentName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_component_configuration(
        self, ResourceGroupName: str, ComponentName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_component_configuration_recommendation(
        self, ResourceGroupName: str, ComponentName: str, Tier: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_observation(self, ObservationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_problem(self, ProblemId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_problem_observations(self, ProblemId: str) -> Dict[str, Any]:
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
    def list_applications(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_components(
        self, ResourceGroupName: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_problems(
        self,
        ResourceGroupName: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_application(
        self,
        ResourceGroupName: str,
        OpsCenterEnabled: bool = None,
        OpsItemSNSTopicArn: str = None,
        RemoveSNSTopic: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_component(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        NewComponentName: str = None,
        ResourceList: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_component_configuration(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        Monitor: bool = None,
        Tier: str = None,
        ComponentConfiguration: str = None,
    ) -> Dict[str, Any]:
        pass
