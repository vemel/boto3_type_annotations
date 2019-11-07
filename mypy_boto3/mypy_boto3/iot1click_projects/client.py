from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_device_with_placement(
        self,
        projectName: str,
        placementName: str,
        deviceId: str,
        deviceTemplateName: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_placement(
        self,
        placementName: str,
        projectName: str,
        attributes: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_project(
        self,
        projectName: str,
        description: Optional[str] = None,
        placementTemplate: Optional[Dict] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_placement(
        self,
        placementName: str,
        projectName: str,
    ) -> Dict:
        pass


    def delete_project(
        self,
        projectName: str,
    ) -> Dict:
        pass


    def describe_placement(
        self,
        placementName: str,
        projectName: str,
    ) -> Dict:
        pass


    def describe_project(
        self,
        projectName: str,
    ) -> Dict:
        pass


    def disassociate_device_from_placement(
        self,
        projectName: str,
        placementName: str,
        deviceTemplateName: str,
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


    def get_devices_in_placement(
        self,
        projectName: str,
        placementName: str,
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


    def list_placements(
        self,
        projectName: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_projects(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
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


    def update_placement(
        self,
        placementName: str,
        projectName: str,
        attributes: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_project(
        self,
        projectName: str,
        description: Optional[str] = None,
        placementTemplate: Optional[Dict] = None,
    ) -> Dict:
        pass

