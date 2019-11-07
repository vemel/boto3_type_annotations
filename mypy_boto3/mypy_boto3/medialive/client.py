from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_update_schedule(
        self,
        ChannelId: str,
        Creates: Optional[Dict] = None,
        Deletes: Optional[Dict] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_channel(
        self,
        ChannelClass: Optional[str] = None,
        Destinations: Optional[List] = None,
        EncoderSettings: Optional[Dict] = None,
        InputAttachments: Optional[List] = None,
        InputSpecification: Optional[Dict] = None,
        LogLevel: Optional[str] = None,
        Name: Optional[str] = None,
        RequestId: Optional[str] = None,
        Reserved: Optional[str] = None,
        RoleArn: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_input(
        self,
        Destinations: Optional[List] = None,
        InputSecurityGroups: Optional[List] = None,
        MediaConnectFlows: Optional[List] = None,
        Name: Optional[str] = None,
        RequestId: Optional[str] = None,
        RoleArn: Optional[str] = None,
        Sources: Optional[List] = None,
        Tags: Optional[Dict] = None,
        Type: Optional[str] = None,
        Vpc: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_input_security_group(
        self,
        Tags: Optional[Dict] = None,
        WhitelistRules: Optional[List] = None,
    ) -> Dict:
        pass


    def create_tags(
        self,
        ResourceArn: str,
        Tags: Optional[Dict] = None,
    ):
        pass


    def delete_channel(
        self,
        ChannelId: str,
    ) -> Dict:
        pass


    def delete_input(
        self,
        InputId: str,
    ) -> Dict:
        pass


    def delete_input_security_group(
        self,
        InputSecurityGroupId: str,
    ) -> Dict:
        pass


    def delete_reservation(
        self,
        ReservationId: str,
    ) -> Dict:
        pass


    def delete_schedule(
        self,
        ChannelId: str,
    ) -> Dict:
        pass


    def delete_tags(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass


    def describe_channel(
        self,
        ChannelId: str,
    ) -> Dict:
        pass


    def describe_input(
        self,
        InputId: str,
    ) -> Dict:
        pass


    def describe_input_security_group(
        self,
        InputSecurityGroupId: str,
    ) -> Dict:
        pass


    def describe_offering(
        self,
        OfferingId: str,
    ) -> Dict:
        pass


    def describe_reservation(
        self,
        ReservationId: str,
    ) -> Dict:
        pass


    def describe_schedule(
        self,
        ChannelId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
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


    def list_channels(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_input_security_groups(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_inputs(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_offerings(
        self,
        ChannelClass: Optional[str] = None,
        ChannelConfiguration: Optional[str] = None,
        Codec: Optional[str] = None,
        MaxResults: Optional[int] = None,
        MaximumBitrate: Optional[str] = None,
        MaximumFramerate: Optional[str] = None,
        NextToken: Optional[str] = None,
        Resolution: Optional[str] = None,
        ResourceType: Optional[str] = None,
        SpecialFeature: Optional[str] = None,
        VideoQuality: Optional[str] = None,
    ) -> Dict:
        pass


    def list_reservations(
        self,
        ChannelClass: Optional[str] = None,
        Codec: Optional[str] = None,
        MaxResults: Optional[int] = None,
        MaximumBitrate: Optional[str] = None,
        MaximumFramerate: Optional[str] = None,
        NextToken: Optional[str] = None,
        Resolution: Optional[str] = None,
        ResourceType: Optional[str] = None,
        SpecialFeature: Optional[str] = None,
        VideoQuality: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def purchase_offering(
        self,
        Count: int,
        OfferingId: str,
        Name: Optional[str] = None,
        RequestId: Optional[str] = None,
        Start: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_channel(
        self,
        ChannelId: str,
    ) -> Dict:
        pass


    def stop_channel(
        self,
        ChannelId: str,
    ) -> Dict:
        pass


    def update_channel(
        self,
        ChannelId: str,
        Destinations: Optional[List] = None,
        EncoderSettings: Optional[Dict] = None,
        InputAttachments: Optional[List] = None,
        InputSpecification: Optional[Dict] = None,
        LogLevel: Optional[str] = None,
        Name: Optional[str] = None,
        RoleArn: Optional[str] = None,
    ) -> Dict:
        pass


    def update_channel_class(
        self,
        ChannelClass: str,
        ChannelId: str,
        Destinations: Optional[List] = None,
    ) -> Dict:
        pass


    def update_input(
        self,
        InputId: str,
        Destinations: Optional[List] = None,
        InputSecurityGroups: Optional[List] = None,
        MediaConnectFlows: Optional[List] = None,
        Name: Optional[str] = None,
        RoleArn: Optional[str] = None,
        Sources: Optional[List] = None,
    ) -> Dict:
        pass


    def update_input_security_group(
        self,
        InputSecurityGroupId: str,
        Tags: Optional[Dict] = None,
        WhitelistRules: Optional[List] = None,
    ) -> Dict:
        pass


    def update_reservation(
        self,
        ReservationId: str,
        Name: Optional[str] = None,
    ) -> Dict:
        pass

