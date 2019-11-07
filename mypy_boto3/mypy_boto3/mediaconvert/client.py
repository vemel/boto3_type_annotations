from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_certificate(
        self,
        Arn: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_job(
        self,
        Id: str,
    ) -> Dict:
        pass


    def create_job(
        self,
        Role: str,
        Settings: Dict,
        AccelerationSettings: Optional[Dict] = None,
        BillingTagsSource: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        JobTemplate: Optional[str] = None,
        Priority: Optional[int] = None,
        Queue: Optional[str] = None,
        SimulateReservedQueue: Optional[str] = None,
        StatusUpdateInterval: Optional[str] = None,
        Tags: Optional[Dict] = None,
        UserMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_job_template(
        self,
        Name: str,
        Settings: Dict,
        AccelerationSettings: Optional[Dict] = None,
        Category: Optional[str] = None,
        Description: Optional[str] = None,
        Priority: Optional[int] = None,
        Queue: Optional[str] = None,
        StatusUpdateInterval: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_preset(
        self,
        Name: str,
        Settings: Dict,
        Category: Optional[str] = None,
        Description: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_queue(
        self,
        Name: str,
        Description: Optional[str] = None,
        PricingPlan: Optional[str] = None,
        ReservationPlanSettings: Optional[Dict] = None,
        Status: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_job_template(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_preset(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_queue(
        self,
        Name: str,
    ) -> Dict:
        pass


    def describe_endpoints(
        self,
        MaxResults: Optional[int] = None,
        Mode: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_certificate(
        self,
        Arn: str,
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


    def get_job(
        self,
        Id: str,
    ) -> Dict:
        pass


    def get_job_template(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_preset(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_queue(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_job_templates(
        self,
        Category: Optional[str] = None,
        ListBy: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Order: Optional[str] = None,
    ) -> Dict:
        pass


    def list_jobs(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Order: Optional[str] = None,
        Queue: Optional[str] = None,
        Status: Optional[str] = None,
    ) -> Dict:
        pass


    def list_presets(
        self,
        Category: Optional[str] = None,
        ListBy: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Order: Optional[str] = None,
    ) -> Dict:
        pass


    def list_queues(
        self,
        ListBy: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Order: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        Arn: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        Arn: str,
        Tags: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        Arn: str,
        TagKeys: Optional[List] = None,
    ) -> Dict:
        pass


    def update_job_template(
        self,
        Name: str,
        AccelerationSettings: Optional[Dict] = None,
        Category: Optional[str] = None,
        Description: Optional[str] = None,
        Priority: Optional[int] = None,
        Queue: Optional[str] = None,
        Settings: Optional[Dict] = None,
        StatusUpdateInterval: Optional[str] = None,
    ) -> Dict:
        pass


    def update_preset(
        self,
        Name: str,
        Category: Optional[str] = None,
        Description: Optional[str] = None,
        Settings: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_queue(
        self,
        Name: str,
        Description: Optional[str] = None,
        ReservationPlanSettings: Optional[Dict] = None,
        Status: Optional[str] = None,
    ) -> Dict:
        pass

