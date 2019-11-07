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


    def create_job(
        self,
        AccountId: str,
        Operation: Dict,
        Report: Dict,
        ClientRequestToken: str,
        Manifest: Dict,
        Priority: int,
        RoleArn: str,
        ConfirmationRequired: Optional[bool] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_public_access_block(
        self,
        AccountId: str,
    ):
        pass


    def describe_job(
        self,
        AccountId: str,
        JobId: str,
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


    def get_public_access_block(
        self,
        AccountId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_jobs(
        self,
        AccountId: str,
        JobStatuses: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def put_public_access_block(
        self,
        PublicAccessBlockConfiguration: Dict,
        AccountId: str,
    ):
        pass


    def update_job_priority(
        self,
        AccountId: str,
        JobId: str,
        Priority: int,
    ) -> Dict:
        pass


    def update_job_status(
        self,
        AccountId: str,
        JobId: str,
        RequestedJobStatus: str,
        StatusUpdateReason: Optional[str] = None,
    ) -> Dict:
        pass

