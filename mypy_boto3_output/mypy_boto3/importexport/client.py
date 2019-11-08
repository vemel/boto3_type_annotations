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
    def cancel_job(self, JobId: str, APIVersion: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_job(
        self,
        JobType: str,
        Manifest: str,
        ValidateOnly: bool,
        ManifestAddendum: str = None,
        APIVersion: str = None,
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
    def get_shipping_label(
        self,
        jobIds: List[Any],
        name: str = None,
        company: str = None,
        phoneNumber: str = None,
        country: str = None,
        stateOrProvince: str = None,
        city: str = None,
        postalCode: str = None,
        street1: str = None,
        street2: str = None,
        street3: str = None,
        APIVersion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_status(self, JobId: str, APIVersion: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_jobs(
        self, MaxJobs: int = None, Marker: str = None, APIVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_job(
        self,
        JobId: str,
        Manifest: str,
        JobType: str,
        ValidateOnly: bool,
        APIVersion: str = None,
    ) -> Dict[str, Any]:
        pass
