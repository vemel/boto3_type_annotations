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


    def describe_job_execution(
        self,
        jobId: str,
        thingName: str,
        includeJobDocument: Optional[bool] = None,
        executionNumber: Optional[int] = None,
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


    def get_pending_job_executions(
        self,
        thingName: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def start_next_pending_job_execution(
        self,
        thingName: str,
        statusDetails: Optional[Dict] = None,
        stepTimeoutInMinutes: Optional[int] = None,
    ) -> Dict:
        pass


    def update_job_execution(
        self,
        jobId: str,
        thingName: str,
        status: str,
        statusDetails: Optional[Dict] = None,
        stepTimeoutInMinutes: Optional[int] = None,
        expectedVersion: Optional[int] = None,
        includeJobExecutionState: Optional[bool] = None,
        includeJobDocument: Optional[bool] = None,
        executionNumber: Optional[int] = None,
    ) -> Dict:
        pass

