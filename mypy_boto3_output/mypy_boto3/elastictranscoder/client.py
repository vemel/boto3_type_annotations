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
    def cancel_job(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_job(
        self,
        PipelineId: str,
        Input: Dict[str, Any] = None,
        Inputs: List[Any] = None,
        Output: Dict[str, Any] = None,
        Outputs: List[Any] = None,
        OutputKeyPrefix: str = None,
        Playlists: List[Any] = None,
        UserMetadata: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_pipeline(
        self,
        Name: str,
        InputBucket: str,
        Role: str,
        OutputBucket: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: Dict[str, Any] = None,
        ContentConfig: Dict[str, Any] = None,
        ThumbnailConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_preset(
        self,
        Name: str,
        Container: str,
        Description: str = None,
        Video: Dict[str, Any] = None,
        Audio: Dict[str, Any] = None,
        Thumbnails: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_pipeline(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_preset(self, Id: str) -> Dict[str, Any]:
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
    def list_jobs_by_pipeline(
        self, PipelineId: str, Ascending: str = None, PageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_jobs_by_status(
        self, Status: str, Ascending: str = None, PageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_pipelines(
        self, Ascending: str = None, PageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_presets(
        self, Ascending: str = None, PageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def read_job(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def read_pipeline(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def read_preset(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def test_role(
        self, Role: str, InputBucket: str, OutputBucket: str, Topics: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_pipeline(
        self,
        Id: str,
        Name: str = None,
        InputBucket: str = None,
        Role: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: Dict[str, Any] = None,
        ContentConfig: Dict[str, Any] = None,
        ThumbnailConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_pipeline_notifications(
        self, Id: str, Notifications: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_pipeline_status(self, Id: str, Status: str) -> Dict[str, Any]:
        pass
