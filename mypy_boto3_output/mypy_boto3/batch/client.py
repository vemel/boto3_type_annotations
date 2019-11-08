from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_job(self, jobId: str, reason: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_compute_environment(
        self,
        computeEnvironmentName: str,
        type: str,
        serviceRole: str,
        state: str = None,
        computeResources: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_job_queue(
        self,
        jobQueueName: str,
        priority: int,
        computeEnvironmentOrder: List[Any],
        state: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_compute_environment(self, computeEnvironment: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_job_queue(self, jobQueue: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_job_definition(self, jobDefinition: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_compute_environments(
        self,
        computeEnvironments: List[Any] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_job_definitions(
        self,
        jobDefinitions: List[Any] = None,
        maxResults: int = None,
        jobDefinitionName: str = None,
        status: str = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_job_queues(
        self, jobQueues: List[Any] = None, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_jobs(self, jobs: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_jobs(
        self,
        jobQueue: str = None,
        arrayJobId: str = None,
        multiNodeJobId: str = None,
        jobStatus: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_job_definition(
        self,
        jobDefinitionName: str,
        type: str,
        parameters: Dict[str, Any] = None,
        containerProperties: Dict[str, Any] = None,
        nodeProperties: Dict[str, Any] = None,
        retryStrategy: Dict[str, Any] = None,
        timeout: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def submit_job(
        self,
        jobName: str,
        jobQueue: str,
        jobDefinition: str,
        arrayProperties: Dict[str, Any] = None,
        dependsOn: List[Any] = None,
        parameters: Dict[str, Any] = None,
        containerOverrides: Dict[str, Any] = None,
        nodeOverrides: Dict[str, Any] = None,
        retryStrategy: Dict[str, Any] = None,
        timeout: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def terminate_job(self, jobId: str, reason: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_compute_environment(
        self,
        computeEnvironment: str,
        state: str = None,
        computeResources: Dict[str, Any] = None,
        serviceRole: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_job_queue(
        self,
        jobQueue: str,
        state: str = None,
        priority: int = None,
        computeEnvironmentOrder: List[Any] = None,
    ) -> Dict[str, Any]:
        pass
