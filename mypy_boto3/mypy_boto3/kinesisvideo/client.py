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


    def create_stream(
        self,
        StreamName: str,
        DeviceName: Optional[str] = None,
        MediaType: Optional[str] = None,
        KmsKeyId: Optional[str] = None,
        DataRetentionInHours: Optional[int] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_stream(
        self,
        StreamARN: str,
        CurrentVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_stream(
        self,
        StreamName: Optional[str] = None,
        StreamARN: Optional[str] = None,
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


    def get_data_endpoint(
        self,
        APIName: str,
        StreamName: Optional[str] = None,
        StreamARN: Optional[str] = None,
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


    def list_streams(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        StreamNameCondition: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_tags_for_stream(
        self,
        NextToken: Optional[str] = None,
        StreamARN: Optional[str] = None,
        StreamName: Optional[str] = None,
    ) -> Dict:
        pass


    def tag_stream(
        self,
        Tags: Dict,
        StreamARN: Optional[str] = None,
        StreamName: Optional[str] = None,
    ) -> Dict:
        pass


    def untag_stream(
        self,
        TagKeyList: List,
        StreamARN: Optional[str] = None,
        StreamName: Optional[str] = None,
    ) -> Dict:
        pass


    def update_data_retention(
        self,
        CurrentVersion: str,
        Operation: str,
        DataRetentionChangeInHours: int,
        StreamName: Optional[str] = None,
        StreamARN: Optional[str] = None,
    ) -> Dict:
        pass


    def update_stream(
        self,
        CurrentVersion: str,
        StreamName: Optional[str] = None,
        StreamARN: Optional[str] = None,
        DeviceName: Optional[str] = None,
        MediaType: Optional[str] = None,
    ) -> Dict:
        pass

