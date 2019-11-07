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


    def create_savings_plan(
        self,
        savingsPlanOfferingId: str,
        commitment: str,
        upfrontPaymentAmount: Optional[str] = None,
        clientToken: Optional[str] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def describe_savings_plan_rates(
        self,
        savingsPlanId: str,
        filters: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_savings_plans(
        self,
        savingsPlanArns: Optional[List] = None,
        savingsPlanIds: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        states: Optional[List] = None,
        filters: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_savings_plans_offering_rates(
        self,
        savingsPlanOfferingIds: Optional[List] = None,
        savingsPlanPaymentOptions: Optional[List] = None,
        savingsPlanTypes: Optional[List] = None,
        products: Optional[List] = None,
        serviceCodes: Optional[List] = None,
        usageTypes: Optional[List] = None,
        operations: Optional[List] = None,
        filters: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_savings_plans_offerings(
        self,
        offeringIds: Optional[List] = None,
        paymentOptions: Optional[List] = None,
        productType: Optional[str] = None,
        planTypes: Optional[List] = None,
        durations: Optional[List] = None,
        currencies: Optional[List] = None,
        descriptions: Optional[List] = None,
        serviceCodes: Optional[List] = None,
        usageTypes: Optional[List] = None,
        operations: Optional[List] = None,
        filters: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
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


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass

