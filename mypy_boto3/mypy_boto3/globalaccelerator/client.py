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


    def create_accelerator(
        self,
        Name: str,
        IdempotencyToken: str,
        IpAddressType: Optional[str] = None,
        Enabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_endpoint_group(
        self,
        ListenerArn: str,
        EndpointGroupRegion: str,
        IdempotencyToken: str,
        EndpointConfigurations: Optional[List] = None,
        TrafficDialPercentage: Optional[float] = None,
        HealthCheckPort: Optional[int] = None,
        HealthCheckProtocol: Optional[str] = None,
        HealthCheckPath: Optional[str] = None,
        HealthCheckIntervalSeconds: Optional[int] = None,
        ThresholdCount: Optional[int] = None,
    ) -> Dict:
        pass


    def create_listener(
        self,
        AcceleratorArn: str,
        PortRanges: List,
        Protocol: str,
        IdempotencyToken: str,
        ClientAffinity: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_accelerator(
        self,
        AcceleratorArn: str,
    ):
        pass


    def delete_endpoint_group(
        self,
        EndpointGroupArn: str,
    ):
        pass


    def delete_listener(
        self,
        ListenerArn: str,
    ):
        pass


    def describe_accelerator(
        self,
        AcceleratorArn: str,
    ) -> Dict:
        pass


    def describe_accelerator_attributes(
        self,
        AcceleratorArn: str,
    ) -> Dict:
        pass


    def describe_endpoint_group(
        self,
        EndpointGroupArn: str,
    ) -> Dict:
        pass


    def describe_listener(
        self,
        ListenerArn: str,
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


    def list_accelerators(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_endpoint_groups(
        self,
        ListenerArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_listeners(
        self,
        AcceleratorArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def update_accelerator(
        self,
        AcceleratorArn: str,
        Name: Optional[str] = None,
        IpAddressType: Optional[str] = None,
        Enabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_accelerator_attributes(
        self,
        AcceleratorArn: str,
        FlowLogsEnabled: Optional[bool] = None,
        FlowLogsS3Bucket: Optional[str] = None,
        FlowLogsS3Prefix: Optional[str] = None,
    ) -> Dict:
        pass


    def update_endpoint_group(
        self,
        EndpointGroupArn: str,
        EndpointConfigurations: Optional[List] = None,
        TrafficDialPercentage: Optional[float] = None,
        HealthCheckPort: Optional[int] = None,
        HealthCheckProtocol: Optional[str] = None,
        HealthCheckPath: Optional[str] = None,
        HealthCheckIntervalSeconds: Optional[int] = None,
        ThresholdCount: Optional[int] = None,
    ) -> Dict:
        pass


    def update_listener(
        self,
        ListenerArn: str,
        PortRanges: Optional[List] = None,
        Protocol: Optional[str] = None,
        ClientAffinity: Optional[str] = None,
    ) -> Dict:
        pass

