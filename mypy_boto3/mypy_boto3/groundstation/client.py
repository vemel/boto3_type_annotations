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


    def cancel_contact(
        self,
        contactId: str,
    ) -> Dict:
        pass


    def create_config(
        self,
        configData: Dict,
        name: str,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_dataflow_endpoint_group(
        self,
        endpointDetails: List,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_mission_profile(
        self,
        dataflowEdges: List,
        minimumViableContactDurationSeconds: int,
        name: str,
        trackingConfigArn: str,
        contactPostPassDurationSeconds: Optional[int] = None,
        contactPrePassDurationSeconds: Optional[int] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_config(
        self,
        configId: str,
        configType: str,
    ) -> Dict:
        pass


    def delete_dataflow_endpoint_group(
        self,
        dataflowEndpointGroupId: str,
    ) -> Dict:
        pass


    def delete_mission_profile(
        self,
        missionProfileId: str,
    ) -> Dict:
        pass


    def describe_contact(
        self,
        contactId: str,
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


    def get_config(
        self,
        configId: str,
        configType: str,
    ) -> Dict:
        pass


    def get_dataflow_endpoint_group(
        self,
        dataflowEndpointGroupId: str,
    ) -> Dict:
        pass


    def get_minute_usage(
        self,
        month: int,
        year: int,
    ) -> Dict:
        pass


    def get_mission_profile(
        self,
        missionProfileId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_satellite(
        self,
        satelliteId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_configs(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_contacts(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List,
        groundStation: Optional[str] = None,
        maxResults: Optional[int] = None,
        missionProfileArn: Optional[str] = None,
        nextToken: Optional[str] = None,
        satelliteArn: Optional[str] = None,
    ) -> Dict:
        pass


    def list_dataflow_endpoint_groups(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_ground_stations(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_mission_profiles(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_satellites(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def reserve_contact(
        self,
        endTime: datetime,
        groundStation: str,
        missionProfileArn: str,
        satelliteArn: str,
        startTime: datetime,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_config(
        self,
        configData: Dict,
        configId: str,
        configType: str,
        name: str,
    ) -> Dict:
        pass


    def update_mission_profile(
        self,
        missionProfileId: str,
        contactPostPassDurationSeconds: Optional[int] = None,
        contactPrePassDurationSeconds: Optional[int] = None,
        dataflowEdges: Optional[List] = None,
        minimumViableContactDurationSeconds: Optional[int] = None,
        name: Optional[str] = None,
        trackingConfigArn: Optional[str] = None,
    ) -> Dict:
        pass

