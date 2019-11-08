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
    def cancel_contact(self, contactId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_config(
        self, configData: Dict[str, Any], name: str, tags: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_dataflow_endpoint_group(
        self, endpointDetails: List[Any], tags: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_mission_profile(
        self,
        dataflowEdges: List[Any],
        minimumViableContactDurationSeconds: int,
        name: str,
        trackingConfigArn: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_config(self, configId: str, configType: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_dataflow_endpoint_group(
        self, dataflowEndpointGroupId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_mission_profile(self, missionProfileId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_contact(self, contactId: str) -> Dict[str, Any]:
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
    def get_config(self, configId: str, configType: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_dataflow_endpoint_group(
        self, dataflowEndpointGroupId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_minute_usage(self, month: int, year: int) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_mission_profile(self, missionProfileId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_satellite(self, satelliteId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_configs(
        self, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_contacts(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List[Any],
        groundStation: str = None,
        maxResults: int = None,
        missionProfileArn: str = None,
        nextToken: str = None,
        satelliteArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_dataflow_endpoint_groups(
        self, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_ground_stations(
        self, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_mission_profiles(
        self, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_satellites(
        self, maxResults: int = None, nextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, resourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reserve_contact(
        self,
        endTime: datetime,
        groundStation: str,
        missionProfileArn: str,
        satelliteArn: str,
        startTime: datetime,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(
        self, resourceArn: str, tags: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_config(
        self, configData: Dict[str, Any], configId: str, configType: str, name: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_mission_profile(
        self,
        missionProfileId: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        dataflowEdges: List[Any] = None,
        minimumViableContactDurationSeconds: int = None,
        name: str = None,
        trackingConfigArn: str = None,
    ) -> Dict[str, Any]:
        pass
