from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags(
        self,
        ResourceId: str,
        TagsList: Optional[List] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_trail(
        self,
        Name: str,
        S3BucketName: str,
        S3KeyPrefix: Optional[str] = None,
        SnsTopicName: Optional[str] = None,
        IncludeGlobalServiceEvents: Optional[bool] = None,
        IsMultiRegionTrail: Optional[bool] = None,
        EnableLogFileValidation: Optional[bool] = None,
        CloudWatchLogsLogGroupArn: Optional[str] = None,
        CloudWatchLogsRoleArn: Optional[str] = None,
        KmsKeyId: Optional[str] = None,
        IsOrganizationTrail: Optional[bool] = None,
        TagsList: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_trail(
        self,
        Name: str,
    ) -> Dict:
        pass


    def describe_trails(
        self,
        trailNameList: Optional[List] = None,
        includeShadowTrails: Optional[bool] = None,
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


    def get_event_selectors(
        self,
        TrailName: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_trail(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_trail_status(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_public_keys(
        self,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags(
        self,
        ResourceIdList: List,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_trails(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def lookup_events(
        self,
        LookupAttributes: Optional[List] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_event_selectors(
        self,
        TrailName: str,
        EventSelectors: List,
    ) -> Dict:
        pass


    def remove_tags(
        self,
        ResourceId: str,
        TagsList: Optional[List] = None,
    ) -> Dict:
        pass


    def start_logging(
        self,
        Name: str,
    ) -> Dict:
        pass


    def stop_logging(
        self,
        Name: str,
    ) -> Dict:
        pass


    def update_trail(
        self,
        Name: str,
        S3BucketName: Optional[str] = None,
        S3KeyPrefix: Optional[str] = None,
        SnsTopicName: Optional[str] = None,
        IncludeGlobalServiceEvents: Optional[bool] = None,
        IsMultiRegionTrail: Optional[bool] = None,
        EnableLogFileValidation: Optional[bool] = None,
        CloudWatchLogsLogGroupArn: Optional[str] = None,
        CloudWatchLogsRoleArn: Optional[str] = None,
        KmsKeyId: Optional[str] = None,
        IsOrganizationTrail: Optional[bool] = None,
    ) -> Dict:
        pass

