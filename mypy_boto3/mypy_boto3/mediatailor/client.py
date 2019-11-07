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


    def delete_playback_configuration(
        self,
        Name: str,
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


    def get_playback_configuration(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_playback_configurations(
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


    def put_playback_configuration(
        self,
        AdDecisionServerUrl: Optional[str] = None,
        CdnConfiguration: Optional[Dict] = None,
        DashConfiguration: Optional[Dict] = None,
        Name: Optional[str] = None,
        SlateAdUrl: Optional[str] = None,
        Tags: Optional[Dict] = None,
        TranscodeProfileName: Optional[str] = None,
        VideoContentSourceUrl: Optional[str] = None,
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

