from __future__ import annotations

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
    def create_savings_plan(
        self,
        savingsPlanOfferingId: str,
        commitment: str,
        upfrontPaymentAmount: str = None,
        clientToken: str = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_savings_plan_rates(
        self,
        savingsPlanId: str,
        filters: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_savings_plans(
        self,
        savingsPlanArns: List[Any] = None,
        savingsPlanIds: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
        states: List[Any] = None,
        filters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_savings_plans_offering_rates(
        self,
        savingsPlanOfferingIds: List[Any] = None,
        savingsPlanPaymentOptions: List[Any] = None,
        savingsPlanTypes: List[Any] = None,
        products: List[Any] = None,
        serviceCodes: List[Any] = None,
        usageTypes: List[Any] = None,
        operations: List[Any] = None,
        filters: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_savings_plans_offerings(
        self,
        offeringIds: List[Any] = None,
        paymentOptions: List[Any] = None,
        productType: str = None,
        planTypes: List[Any] = None,
        durations: List[Any] = None,
        currencies: List[Any] = None,
        descriptions: List[Any] = None,
        serviceCodes: List[Any] = None,
        usageTypes: List[Any] = None,
        operations: List[Any] = None,
        filters: List[Any] = None,
        nextToken: str = None,
        maxResults: int = None,
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
    def list_tags_for_resource(self, resourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
        pass
