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
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_cost_and_usage(
        self,
        TimePeriod: Dict[str, Any],
        Granularity: str = None,
        Filter: Dict[str, Any] = None,
        Metrics: List[Any] = None,
        GroupBy: List[Any] = None,
        NextPageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_cost_forecast(
        self,
        TimePeriod: Dict[str, Any],
        Metric: str,
        Granularity: str,
        Filter: Dict[str, Any] = None,
        PredictionIntervalLevel: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_dimension_values(
        self,
        TimePeriod: Dict[str, Any],
        Dimension: str,
        SearchString: str = None,
        Context: str = None,
        NextPageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_reservation_coverage(
        self,
        TimePeriod: Dict[str, Any],
        GroupBy: List[Any] = None,
        Granularity: str = None,
        Filter: Dict[str, Any] = None,
        Metrics: List[Any] = None,
        NextPageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_reservation_purchase_recommendation(
        self,
        Service: str,
        AccountId: str = None,
        AccountScope: str = None,
        LookbackPeriodInDays: str = None,
        TermInYears: str = None,
        PaymentOption: str = None,
        ServiceSpecification: Dict[str, Any] = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_reservation_utilization(
        self,
        TimePeriod: Dict[str, Any],
        GroupBy: List[Any] = None,
        Granularity: str = None,
        Filter: Dict[str, Any] = None,
        NextPageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_rightsizing_recommendation(
        self,
        Service: str,
        Filter: Dict[str, Any] = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_savings_plans_coverage(
        self,
        TimePeriod: Dict[str, Any],
        GroupBy: List[Any] = None,
        Granularity: str = None,
        Filter: Dict[str, Any] = None,
        Metrics: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_savings_plans_purchase_recommendation(
        self,
        SavingsPlansType: str,
        TermInYears: str,
        PaymentOption: str,
        LookbackPeriodInDays: str,
        NextPageToken: str = None,
        PageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_savings_plans_utilization(
        self,
        TimePeriod: Dict[str, Any],
        Granularity: str = None,
        Filter: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_savings_plans_utilization_details(
        self,
        TimePeriod: Dict[str, Any],
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_tags(
        self,
        TimePeriod: Dict[str, Any],
        SearchString: str = None,
        TagKey: str = None,
        NextPageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_usage_forecast(
        self,
        TimePeriod: Dict[str, Any],
        Metric: str,
        Granularity: str,
        Filter: Dict[str, Any] = None,
        PredictionIntervalLevel: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass
