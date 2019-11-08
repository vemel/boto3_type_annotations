from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_job_execution(
        self,
        jobId: str,
        thingName: str,
        includeJobDocument: bool = None,
        executionNumber: int = None,
    ) -> Dict[str, Any]:
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
    def get_pending_job_executions(self, thingName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def start_next_pending_job_execution(
        self,
        thingName: str,
        statusDetails: Dict[str, Any] = None,
        stepTimeoutInMinutes: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_job_execution(
        self,
        jobId: str,
        thingName: str,
        status: str,
        statusDetails: Dict[str, Any] = None,
        stepTimeoutInMinutes: int = None,
        expectedVersion: int = None,
        includeJobExecutionState: bool = None,
        includeJobDocument: bool = None,
        executionNumber: int = None,
    ) -> Dict[str, Any]:
        pass
