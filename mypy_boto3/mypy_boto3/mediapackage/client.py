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


    def create_channel(
        self,
        Id: str,
        Description: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_harvest_job(
        self,
        EndTime: str,
        Id: str,
        OriginEndpointId: str,
        S3Destination: Dict,
        StartTime: str,
    ) -> Dict:
        pass


    def create_origin_endpoint(
        self,
        ChannelId: str,
        Id: str,
        CmafPackage: Optional[Dict] = None,
        DashPackage: Optional[Dict] = None,
        Description: Optional[str] = None,
        HlsPackage: Optional[Dict] = None,
        ManifestName: Optional[str] = None,
        MssPackage: Optional[Dict] = None,
        Origination: Optional[str] = None,
        StartoverWindowSeconds: Optional[int] = None,
        Tags: Optional[Dict] = None,
        TimeDelaySeconds: Optional[int] = None,
        Whitelist: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_channel(
        self,
        Id: str,
    ) -> Dict:
        pass


    def delete_origin_endpoint(
        self,
        Id: str,
    ) -> Dict:
        pass


    def describe_channel(
        self,
        Id: str,
    ) -> Dict:
        pass


    def describe_harvest_job(
        self,
        Id: str,
    ) -> Dict:
        pass


    def describe_origin_endpoint(
        self,
        Id: str,
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


    def list_harvest_jobs(
        self,
        IncludeChannelId: Optional[str] = None,
        IncludeStatus: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_origin_endpoints(
        self,
        ChannelId: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def rotate_channel_credentials(
        self,
        Id: str,
    ) -> Dict:
        pass


    def rotate_ingest_endpoint_credentials(
        self,
        Id: str,
        IngestEndpointId: str,
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


    def update_channel(
        self,
        Id: str,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def update_origin_endpoint(
        self,
        Id: str,
        CmafPackage: Optional[Dict] = None,
        DashPackage: Optional[Dict] = None,
        Description: Optional[str] = None,
        HlsPackage: Optional[Dict] = None,
        ManifestName: Optional[str] = None,
        MssPackage: Optional[Dict] = None,
        Origination: Optional[str] = None,
        StartoverWindowSeconds: Optional[int] = None,
        TimeDelaySeconds: Optional[int] = None,
        Whitelist: Optional[List] = None,
    ) -> Dict:
        pass

