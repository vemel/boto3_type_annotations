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


    def cancel_job(
        self,
        Id: str,
    ) -> Dict:
        pass


    def create_job(
        self,
        PipelineId: str,
        Input: Optional[Dict] = None,
        Inputs: Optional[List] = None,
        Output: Optional[Dict] = None,
        Outputs: Optional[List] = None,
        OutputKeyPrefix: Optional[str] = None,
        Playlists: Optional[List] = None,
        UserMetadata: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_pipeline(
        self,
        Name: str,
        InputBucket: str,
        Role: str,
        OutputBucket: Optional[str] = None,
        AwsKmsKeyArn: Optional[str] = None,
        Notifications: Optional[Dict] = None,
        ContentConfig: Optional[Dict] = None,
        ThumbnailConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_preset(
        self,
        Name: str,
        Container: str,
        Description: Optional[str] = None,
        Video: Optional[Dict] = None,
        Audio: Optional[Dict] = None,
        Thumbnails: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_pipeline(
        self,
        Id: str,
    ) -> Dict:
        pass


    def delete_preset(
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


    def list_jobs_by_pipeline(
        self,
        PipelineId: str,
        Ascending: Optional[str] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_jobs_by_status(
        self,
        Status: str,
        Ascending: Optional[str] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_pipelines(
        self,
        Ascending: Optional[str] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_presets(
        self,
        Ascending: Optional[str] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def read_job(
        self,
        Id: str,
    ) -> Dict:
        pass


    def read_pipeline(
        self,
        Id: str,
    ) -> Dict:
        pass


    def read_preset(
        self,
        Id: str,
    ) -> Dict:
        pass


    def test_role(
        self,
        Role: str,
        InputBucket: str,
        OutputBucket: str,
        Topics: List,
    ) -> Dict:
        pass


    def update_pipeline(
        self,
        Id: str,
        Name: Optional[str] = None,
        InputBucket: Optional[str] = None,
        Role: Optional[str] = None,
        AwsKmsKeyArn: Optional[str] = None,
        Notifications: Optional[Dict] = None,
        ContentConfig: Optional[Dict] = None,
        ThumbnailConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_pipeline_notifications(
        self,
        Id: str,
        Notifications: Dict,
    ) -> Dict:
        pass


    def update_pipeline_status(
        self,
        Id: str,
        Status: str,
    ) -> Dict:
        pass

