from typing import Dict
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_configuration_set(
        self,
        ConfigurationSetName: Optional[str] = None,
    ) -> Dict:
        pass


    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: Optional[Dict] = None,
        EventDestinationName: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_configuration_set(
        self,
        ConfigurationSetName: str,
    ) -> Dict:
        pass


    def delete_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
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


    def get_configuration_set_event_destinations(
        self,
        ConfigurationSetName: str,
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


    def send_voice_message(
        self,
        CallerId: Optional[str] = None,
        ConfigurationSetName: Optional[str] = None,
        Content: Optional[Dict] = None,
        DestinationPhoneNumber: Optional[str] = None,
        OriginationPhoneNumber: Optional[str] = None,
    ) -> Dict:
        pass


    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: Optional[Dict] = None,
    ) -> Dict:
        pass

