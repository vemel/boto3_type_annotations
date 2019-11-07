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


    def create_application(
        self,
        ResourceGroupName: str,
        OpsCenterEnabled: Optional[bool] = None,
        OpsItemSNSTopicArn: Optional[str] = None,
    ) -> Dict:
        pass


    def create_component(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        ResourceList: List,
    ) -> Dict:
        pass


    def delete_application(
        self,
        ResourceGroupName: str,
    ) -> Dict:
        pass


    def delete_component(
        self,
        ResourceGroupName: str,
        ComponentName: str,
    ) -> Dict:
        pass


    def describe_application(
        self,
        ResourceGroupName: str,
    ) -> Dict:
        pass


    def describe_component(
        self,
        ResourceGroupName: str,
        ComponentName: str,
    ) -> Dict:
        pass


    def describe_component_configuration(
        self,
        ResourceGroupName: str,
        ComponentName: str,
    ) -> Dict:
        pass


    def describe_component_configuration_recommendation(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        Tier: str,
    ) -> Dict:
        pass


    def describe_observation(
        self,
        ObservationId: str,
    ) -> Dict:
        pass


    def describe_problem(
        self,
        ProblemId: str,
    ) -> Dict:
        pass


    def describe_problem_observations(
        self,
        ProblemId: str,
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


    def list_applications(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_components(
        self,
        ResourceGroupName: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_problems(
        self,
        ResourceGroupName: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def update_application(
        self,
        ResourceGroupName: str,
        OpsCenterEnabled: Optional[bool] = None,
        OpsItemSNSTopicArn: Optional[str] = None,
        RemoveSNSTopic: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_component(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        NewComponentName: Optional[str] = None,
        ResourceList: Optional[List] = None,
    ) -> Dict:
        pass


    def update_component_configuration(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        Monitor: Optional[bool] = None,
        Tier: Optional[str] = None,
        ComponentConfiguration: Optional[str] = None,
    ) -> Dict:
        pass

