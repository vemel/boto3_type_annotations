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
    def create_job(
        self,
        AccountId: str,
        Operation: Dict[str, Any],
        Report: Dict[str, Any],
        ClientRequestToken: str,
        Manifest: Dict[str, Any],
        Priority: int,
        RoleArn: str,
        ConfirmationRequired: bool = None,
        Description: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_public_access_block(self, AccountId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_job(self, AccountId: str, JobId: str) -> Dict[str, Any]:
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
    def get_public_access_block(self, AccountId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_jobs(
        self,
        AccountId: str,
        JobStatuses: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_public_access_block(
        self, PublicAccessBlockConfiguration: Dict[str, Any], AccountId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_job_priority(
        self, AccountId: str, JobId: str, Priority: int
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_job_status(
        self,
        AccountId: str,
        JobId: str,
        RequestedJobStatus: str,
        StatusUpdateReason: str = None,
    ) -> Dict[str, Any]:
        pass
