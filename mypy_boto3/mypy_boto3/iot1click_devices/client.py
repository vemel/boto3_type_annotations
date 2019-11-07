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


    def claim_devices_by_claim_code(
        self,
        ClaimCode: str,
    ) -> Dict:
        pass


    def describe_device(
        self,
        DeviceId: str,
    ) -> Dict:
        pass


    def finalize_device_claim(
        self,
        DeviceId: str,
        Tags: Optional[Dict] = None,
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


    def get_device_methods(
        self,
        DeviceId: str,
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


    def initiate_device_claim(
        self,
        DeviceId: str,
    ) -> Dict:
        pass


    def invoke_device_method(
        self,
        DeviceId: str,
        DeviceMethod: Optional[Dict] = None,
        DeviceMethodParameters: Optional[str] = None,
    ) -> Dict:
        pass


    def list_device_events(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_devices(
        self,
        DeviceType: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Dict,
    ):
        pass


    def unclaim_device(
        self,
        DeviceId: str,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass


    def update_device_state(
        self,
        DeviceId: str,
        Enabled: Optional[bool] = None,
    ) -> Dict:
        pass

