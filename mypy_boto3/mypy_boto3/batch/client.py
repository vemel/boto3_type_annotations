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
        jobId: str,
        reason: str,
    ) -> Dict:
        pass


    def create_compute_environment(
        self,
        computeEnvironmentName: str,
        type: str,
        serviceRole: str,
        state: Optional[str] = None,
        computeResources: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_job_queue(
        self,
        jobQueueName: str,
        priority: int,
        computeEnvironmentOrder: List,
        state: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_compute_environment(
        self,
        computeEnvironment: str,
    ) -> Dict:
        pass


    def delete_job_queue(
        self,
        jobQueue: str,
    ) -> Dict:
        pass


    def deregister_job_definition(
        self,
        jobDefinition: str,
    ) -> Dict:
        pass


    def describe_compute_environments(
        self,
        computeEnvironments: Optional[List] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_job_definitions(
        self,
        jobDefinitions: Optional[List] = None,
        maxResults: Optional[int] = None,
        jobDefinitionName: Optional[str] = None,
        status: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_job_queues(
        self,
        jobQueues: Optional[List] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_jobs(
        self,
        jobs: List,
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


    def list_jobs(
        self,
        jobQueue: Optional[str] = None,
        arrayJobId: Optional[str] = None,
        multiNodeJobId: Optional[str] = None,
        jobStatus: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def register_job_definition(
        self,
        jobDefinitionName: str,
        type: str,
        parameters: Optional[Dict] = None,
        containerProperties: Optional[Dict] = None,
        nodeProperties: Optional[Dict] = None,
        retryStrategy: Optional[Dict] = None,
        timeout: Optional[Dict] = None,
    ) -> Dict:
        pass


    def submit_job(
        self,
        jobName: str,
        jobQueue: str,
        jobDefinition: str,
        arrayProperties: Optional[Dict] = None,
        dependsOn: Optional[List] = None,
        parameters: Optional[Dict] = None,
        containerOverrides: Optional[Dict] = None,
        nodeOverrides: Optional[Dict] = None,
        retryStrategy: Optional[Dict] = None,
        timeout: Optional[Dict] = None,
    ) -> Dict:
        pass


    def terminate_job(
        self,
        jobId: str,
        reason: str,
    ) -> Dict:
        pass


    def update_compute_environment(
        self,
        computeEnvironment: str,
        state: Optional[str] = None,
        computeResources: Optional[Dict] = None,
        serviceRole: Optional[str] = None,
    ) -> Dict:
        pass


    def update_job_queue(
        self,
        jobQueue: str,
        state: Optional[str] = None,
        priority: Optional[int] = None,
        computeEnvironmentOrder: Optional[List] = None,
    ) -> Dict:
        pass

