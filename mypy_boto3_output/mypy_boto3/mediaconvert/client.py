from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def associate_certificate(self, Arn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_job(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_job(
        self,
        Role: str,
        Settings: Dict[str, Any],
        AccelerationSettings: Dict[str, Any] = None,
        BillingTagsSource: str = None,
        ClientRequestToken: str = None,
        JobTemplate: str = None,
        Priority: int = None,
        Queue: str = None,
        SimulateReservedQueue: str = None,
        StatusUpdateInterval: str = None,
        Tags: Dict[str, Any] = None,
        UserMetadata: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_job_template(
        self,
        Name: str,
        Settings: Dict[str, Any],
        AccelerationSettings: Dict[str, Any] = None,
        Category: str = None,
        Description: str = None,
        Priority: int = None,
        Queue: str = None,
        StatusUpdateInterval: str = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_preset(
        self,
        Name: str,
        Settings: Dict[str, Any],
        Category: str = None,
        Description: str = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_queue(
        self,
        Name: str,
        Description: str = None,
        PricingPlan: str = None,
        ReservationPlanSettings: Dict[str, Any] = None,
        Status: str = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_job_template(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_preset(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_queue(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_endpoints(
        self, MaxResults: int = None, Mode: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_certificate(self, Arn: str) -> Dict[str, Any]:
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
    def get_job(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_job_template(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_preset(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_queue(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_job_templates(
        self,
        Category: str = None,
        ListBy: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Order: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_jobs(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Order: str = None,
        Queue: str = None,
        Status: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_presets(
        self,
        Category: str = None,
        ListBy: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Order: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_queues(
        self,
        ListBy: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Order: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, Arn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, Arn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, Arn: str, TagKeys: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_job_template(
        self,
        Name: str,
        AccelerationSettings: Dict[str, Any] = None,
        Category: str = None,
        Description: str = None,
        Priority: int = None,
        Queue: str = None,
        Settings: Dict[str, Any] = None,
        StatusUpdateInterval: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_preset(
        self,
        Name: str,
        Category: str = None,
        Description: str = None,
        Settings: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_queue(
        self,
        Name: str,
        Description: str = None,
        ReservationPlanSettings: Dict[str, Any] = None,
        Status: str = None,
    ) -> Dict[str, Any]:
        pass
