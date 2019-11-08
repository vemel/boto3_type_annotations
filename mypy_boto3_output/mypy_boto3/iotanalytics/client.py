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
    def batch_put_message(
        self, channelName: str, messages: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_pipeline_reprocessing(
        self, pipelineName: str, reprocessingId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_channel(
        self,
        channelName: str,
        channelStorage: Dict[str, Any] = None,
        retentionPeriod: Dict[str, Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_dataset(
        self,
        datasetName: str,
        actions: List[Any],
        triggers: List[Any] = None,
        contentDeliveryRules: List[Any] = None,
        retentionPeriod: Dict[str, Any] = None,
        versioningConfiguration: Dict[str, Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_dataset_content(self, datasetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_datastore(
        self,
        datastoreName: str,
        datastoreStorage: Dict[str, Any] = None,
        retentionPeriod: Dict[str, Any] = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_pipeline(
        self, pipelineName: str, pipelineActivities: List[Any], tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_channel(self, channelName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_dataset(self, datasetName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_dataset_content(self, datasetName: str, versionId: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_datastore(self, datastoreName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_pipeline(self, pipelineName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_channel(
        self, channelName: str, includeStatistics: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_dataset(self, datasetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_datastore(
        self, datastoreName: str, includeStatistics: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_logging_options(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_pipeline(self, pipelineName: str) -> Dict[str, Any]:
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
    def get_dataset_content(
        self, datasetName: str, versionId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_channels(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_dataset_contents(
        self,
        datasetName: str,
        nextToken: str = None,
        maxResults: int = None,
        scheduledOnOrAfter: datetime = None,
        scheduledBefore: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_datasets(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_datastores(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_pipelines(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, resourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_logging_options(self, loggingOptions: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def run_pipeline_activity(
        self, pipelineActivity: Dict[str, Any], payloads: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def sample_channel_data(
        self,
        channelName: str,
        maxMessages: int = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_pipeline_reprocessing(
        self, pipelineName: str, startTime: datetime = None, endTime: datetime = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_channel(
        self,
        channelName: str,
        channelStorage: Dict[str, Any] = None,
        retentionPeriod: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_dataset(
        self,
        datasetName: str,
        actions: List[Any],
        triggers: List[Any] = None,
        contentDeliveryRules: List[Any] = None,
        retentionPeriod: Dict[str, Any] = None,
        versioningConfiguration: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_datastore(
        self,
        datastoreName: str,
        retentionPeriod: Dict[str, Any] = None,
        datastoreStorage: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_pipeline(self, pipelineName: str, pipelineActivities: List[Any]) -> None:
        pass
