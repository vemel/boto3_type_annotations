from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_flow_outputs(
        self,
        FlowArn: str,
        Outputs: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_flow(
        self,
        Name: str,
        Source: Dict,
        AvailabilityZone: Optional[str] = None,
        Entitlements: Optional[List] = None,
        Outputs: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_flow(
        self,
        FlowArn: str,
    ) -> Dict:
        pass


    def describe_flow(
        self,
        FlowArn: str,
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


    def grant_flow_entitlements(
        self,
        Entitlements: List,
        FlowArn: str,
    ) -> Dict:
        pass


    def list_entitlements(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_flows(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def remove_flow_output(
        self,
        FlowArn: str,
        OutputArn: str,
    ) -> Dict:
        pass


    def revoke_flow_entitlement(
        self,
        EntitlementArn: str,
        FlowArn: str,
    ) -> Dict:
        pass


    def start_flow(
        self,
        FlowArn: str,
    ) -> Dict:
        pass


    def stop_flow(
        self,
        FlowArn: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: Dict,
    ):
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass


    def update_flow_entitlement(
        self,
        EntitlementArn: str,
        FlowArn: str,
        Description: Optional[str] = None,
        Encryption: Optional[Dict] = None,
        Subscribers: Optional[List] = None,
    ) -> Dict:
        pass


    def update_flow_output(
        self,
        FlowArn: str,
        OutputArn: str,
        CidrAllowList: Optional[List] = None,
        Description: Optional[str] = None,
        Destination: Optional[str] = None,
        Encryption: Optional[Dict] = None,
        MaxLatency: Optional[int] = None,
        Port: Optional[int] = None,
        Protocol: Optional[str] = None,
        RemoteId: Optional[str] = None,
        SmoothingLatency: Optional[int] = None,
        StreamId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_flow_source(
        self,
        FlowArn: str,
        SourceArn: str,
        Decryption: Optional[Dict] = None,
        Description: Optional[str] = None,
        EntitlementArn: Optional[str] = None,
        IngestPort: Optional[int] = None,
        MaxBitrate: Optional[int] = None,
        MaxLatency: Optional[int] = None,
        Protocol: Optional[str] = None,
        StreamId: Optional[str] = None,
        WhitelistCidr: Optional[str] = None,
    ) -> Dict:
        pass

