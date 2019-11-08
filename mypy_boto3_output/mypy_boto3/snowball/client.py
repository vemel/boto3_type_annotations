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
    def cancel_cluster(self, ClusterId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def cancel_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_address(self, Address: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_cluster(
        self,
        JobType: str,
        Resources: Dict[str, Any],
        AddressId: str,
        RoleARN: str,
        ShippingOption: str,
        Description: str = None,
        KmsKeyARN: str = None,
        SnowballType: str = None,
        Notification: Dict[str, Any] = None,
        ForwardingAddressId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_job(
        self,
        JobType: str = None,
        Resources: Dict[str, Any] = None,
        Description: str = None,
        AddressId: str = None,
        KmsKeyARN: str = None,
        RoleARN: str = None,
        SnowballCapacityPreference: str = None,
        ShippingOption: str = None,
        Notification: Dict[str, Any] = None,
        ClusterId: str = None,
        SnowballType: str = None,
        ForwardingAddressId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_address(self, AddressId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_addresses(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_cluster(self, ClusterId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_job(self, JobId: str) -> Dict[str, Any]:
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
    def get_job_manifest(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_job_unlock_code(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_snowball_usage(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_software_updates(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_cluster_jobs(
        self, ClusterId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_clusters(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_compatible_images(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_jobs(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_cluster(
        self,
        ClusterId: str,
        RoleARN: str = None,
        Description: str = None,
        Resources: Dict[str, Any] = None,
        AddressId: str = None,
        ShippingOption: str = None,
        Notification: Dict[str, Any] = None,
        ForwardingAddressId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_job(
        self,
        JobId: str,
        RoleARN: str = None,
        Notification: Dict[str, Any] = None,
        Resources: Dict[str, Any] = None,
        AddressId: str = None,
        ShippingOption: str = None,
        Description: str = None,
        SnowballCapacityPreference: str = None,
        ForwardingAddressId: str = None,
    ) -> Dict[str, Any]:
        pass
