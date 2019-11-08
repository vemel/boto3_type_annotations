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
    def add_tags(self, ResourceId: str, TagsList: List[Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_trail(
        self,
        Name: str,
        S3BucketName: str,
        S3KeyPrefix: str = None,
        SnsTopicName: str = None,
        IncludeGlobalServiceEvents: bool = None,
        IsMultiRegionTrail: bool = None,
        EnableLogFileValidation: bool = None,
        CloudWatchLogsLogGroupArn: str = None,
        CloudWatchLogsRoleArn: str = None,
        KmsKeyId: str = None,
        IsOrganizationTrail: bool = None,
        TagsList: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_trail(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_trails(
        self, trailNameList: List[Any] = None, includeShadowTrails: bool = None
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
    def get_event_selectors(self, TrailName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_trail(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_trail_status(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_public_keys(
        self,
        StartTime: datetime = None,
        EndTime: datetime = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags(
        self, ResourceIdList: List[Any], NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_trails(self, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def lookup_events(
        self,
        LookupAttributes: List[Any] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_event_selectors(
        self, TrailName: str, EventSelectors: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags(
        self, ResourceId: str, TagsList: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_logging(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_logging(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_trail(
        self,
        Name: str,
        S3BucketName: str = None,
        S3KeyPrefix: str = None,
        SnsTopicName: str = None,
        IncludeGlobalServiceEvents: bool = None,
        IsMultiRegionTrail: bool = None,
        EnableLogFileValidation: bool = None,
        CloudWatchLogsLogGroupArn: str = None,
        CloudWatchLogsRoleArn: str = None,
        KmsKeyId: str = None,
        IsOrganizationTrail: bool = None,
    ) -> Dict[str, Any]:
        pass
