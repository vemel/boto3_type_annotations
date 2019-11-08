from __future__ import annotations

from datetime import datetime
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
    def claim_devices_by_claim_code(self, ClaimCode: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_device(self, DeviceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def finalize_device_claim(
        self, DeviceId: str, Tags: Dict[str, Any] = None
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
    def get_device_methods(self, DeviceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def initiate_device_claim(self, DeviceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def invoke_device_method(
        self,
        DeviceId: str,
        DeviceMethod: Dict[str, Any] = None,
        DeviceMethodParameters: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_device_events(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_devices(
        self, DeviceType: str = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def unclaim_device(self, DeviceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_device_state(
        self, DeviceId: str, Enabled: bool = None
    ) -> Dict[str, Any]:
        pass
