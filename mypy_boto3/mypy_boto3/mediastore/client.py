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


    def create_container(
        self,
        ContainerName: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_container(
        self,
        ContainerName: str,
    ) -> Dict:
        pass


    def delete_container_policy(
        self,
        ContainerName: str,
    ) -> Dict:
        pass


    def delete_cors_policy(
        self,
        ContainerName: str,
    ) -> Dict:
        pass


    def delete_lifecycle_policy(
        self,
        ContainerName: str,
    ) -> Dict:
        pass


    def describe_container(
        self,
        ContainerName: Optional[str] = None,
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


    def get_container_policy(
        self,
        ContainerName: str,
    ) -> Dict:
        pass


    def get_cors_policy(
        self,
        ContainerName: str,
    ) -> Dict:
        pass


    def get_lifecycle_policy(
        self,
        ContainerName: str,
    ) -> Dict:
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


    def list_containers(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        Resource: str,
    ) -> Dict:
        pass


    def put_container_policy(
        self,
        ContainerName: str,
        Policy: str,
    ) -> Dict:
        pass


    def put_cors_policy(
        self,
        ContainerName: str,
        CorsPolicy: List,
    ) -> Dict:
        pass


    def put_lifecycle_policy(
        self,
        ContainerName: str,
        LifecyclePolicy: str,
    ) -> Dict:
        pass


    def start_access_logging(
        self,
        ContainerName: str,
    ) -> Dict:
        pass


    def stop_access_logging(
        self,
        ContainerName: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        Resource: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        Resource: str,
        TagKeys: List,
    ) -> Dict:
        pass

