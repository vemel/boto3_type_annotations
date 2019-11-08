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
    def create_channel(
        self, Id: str, Description: str = None, Tags: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_harvest_job(
        self,
        EndTime: str,
        Id: str,
        OriginEndpointId: str,
        S3Destination: Dict[str, Any],
        StartTime: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_origin_endpoint(
        self,
        ChannelId: str,
        Id: str,
        CmafPackage: Dict[str, Any] = None,
        DashPackage: Dict[str, Any] = None,
        Description: str = None,
        HlsPackage: Dict[str, Any] = None,
        ManifestName: str = None,
        MssPackage: Dict[str, Any] = None,
        Origination: str = None,
        StartoverWindowSeconds: int = None,
        Tags: Dict[str, Any] = None,
        TimeDelaySeconds: int = None,
        Whitelist: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_channel(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_origin_endpoint(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_channel(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_harvest_job(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_origin_endpoint(self, Id: str) -> Dict[str, Any]:
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
    def list_channels(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_harvest_jobs(
        self,
        IncludeChannelId: str = None,
        IncludeStatus: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_origin_endpoints(
        self, ChannelId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def rotate_channel_credentials(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def rotate_ingest_endpoint_credentials(
        self, Id: str, IngestEndpointId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_channel(self, Id: str, Description: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_origin_endpoint(
        self,
        Id: str,
        CmafPackage: Dict[str, Any] = None,
        DashPackage: Dict[str, Any] = None,
        Description: str = None,
        HlsPackage: Dict[str, Any] = None,
        ManifestName: str = None,
        MssPackage: Dict[str, Any] = None,
        Origination: str = None,
        StartoverWindowSeconds: int = None,
        TimeDelaySeconds: int = None,
        Whitelist: List[Any] = None,
    ) -> Dict[str, Any]:
        pass
