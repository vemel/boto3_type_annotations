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


    def create_environment_ec2(
        self,
        name: str,
        instanceType: str,
        description: Optional[str] = None,
        clientRequestToken: Optional[str] = None,
        subnetId: Optional[str] = None,
        automaticStopTimeMinutes: Optional[int] = None,
        ownerArn: Optional[str] = None,
    ) -> Dict:
        pass


    def create_environment_membership(
        self,
        environmentId: str,
        userArn: str,
        permissions: str,
    ) -> Dict:
        pass


    def delete_environment(
        self,
        environmentId: str,
    ) -> Dict:
        pass


    def delete_environment_membership(
        self,
        environmentId: str,
        userArn: str,
    ) -> Dict:
        pass


    def describe_environment_memberships(
        self,
        userArn: Optional[str] = None,
        environmentId: Optional[str] = None,
        permissions: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_environment_status(
        self,
        environmentId: str,
    ) -> Dict:
        pass


    def describe_environments(
        self,
        environmentIds: List,
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


    def list_environments(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def update_environment(
        self,
        environmentId: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_environment_membership(
        self,
        environmentId: str,
        userArn: str,
        permissions: str,
    ) -> Dict:
        pass

