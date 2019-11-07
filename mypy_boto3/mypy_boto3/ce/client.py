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


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_cost_and_usage(
        self,
        TimePeriod: Dict,
        Granularity: Optional[str] = None,
        Filter: Optional[Dict] = None,
        Metrics: Optional[List] = None,
        GroupBy: Optional[List] = None,
        NextPageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_cost_forecast(
        self,
        TimePeriod: Dict,
        Metric: str,
        Granularity: str,
        Filter: Optional[Dict] = None,
        PredictionIntervalLevel: Optional[int] = None,
    ) -> Dict:
        pass


    def get_dimension_values(
        self,
        TimePeriod: Dict,
        Dimension: str,
        SearchString: Optional[str] = None,
        Context: Optional[str] = None,
        NextPageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_reservation_coverage(
        self,
        TimePeriod: Dict,
        GroupBy: Optional[List] = None,
        Granularity: Optional[str] = None,
        Filter: Optional[Dict] = None,
        Metrics: Optional[List] = None,
        NextPageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_reservation_purchase_recommendation(
        self,
        Service: str,
        AccountId: Optional[str] = None,
        AccountScope: Optional[str] = None,
        LookbackPeriodInDays: Optional[str] = None,
        TermInYears: Optional[str] = None,
        PaymentOption: Optional[str] = None,
        ServiceSpecification: Optional[Dict] = None,
        PageSize: Optional[int] = None,
        NextPageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_reservation_utilization(
        self,
        TimePeriod: Dict,
        GroupBy: Optional[List] = None,
        Granularity: Optional[str] = None,
        Filter: Optional[Dict] = None,
        NextPageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_rightsizing_recommendation(
        self,
        Service: str,
        Filter: Optional[Dict] = None,
        PageSize: Optional[int] = None,
        NextPageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_savings_plans_coverage(
        self,
        TimePeriod: Dict,
        GroupBy: Optional[List] = None,
        Granularity: Optional[str] = None,
        Filter: Optional[Dict] = None,
        Metrics: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_savings_plans_purchase_recommendation(
        self,
        SavingsPlansType: str,
        TermInYears: str,
        PaymentOption: str,
        LookbackPeriodInDays: str,
        NextPageToken: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def get_savings_plans_utilization(
        self,
        TimePeriod: Dict,
        Granularity: Optional[str] = None,
        Filter: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_savings_plans_utilization_details(
        self,
        TimePeriod: Dict,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_tags(
        self,
        TimePeriod: Dict,
        SearchString: Optional[str] = None,
        TagKey: Optional[str] = None,
        NextPageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_usage_forecast(
        self,
        TimePeriod: Dict,
        Metric: str,
        Granularity: str,
        Filter: Optional[Dict] = None,
        PredictionIntervalLevel: Optional[int] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass

