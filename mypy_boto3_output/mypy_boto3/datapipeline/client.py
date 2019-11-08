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
    def activate_pipeline(
        self,
        pipelineId: str,
        parameterValues: List[Any] = None,
        startTimestamp: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def add_tags(self, pipelineId: str, tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_pipeline(
        self, name: str, uniqueId: str, description: str = None, tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deactivate_pipeline(
        self, pipelineId: str, cancelActive: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_pipeline(self, pipelineId: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_objects(
        self,
        pipelineId: str,
        objectIds: List[Any],
        evaluateExpressions: bool = None,
        marker: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_pipelines(self, pipelineIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def evaluate_expression(
        self, pipelineId: str, objectId: str, expression: str
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
    def get_pipeline_definition(
        self, pipelineId: str, version: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_pipelines(self, marker: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def poll_for_task(
        self,
        workerGroup: str,
        hostname: str = None,
        instanceIdentity: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_pipeline_definition(
        self,
        pipelineId: str,
        pipelineObjects: List[Any],
        parameterObjects: List[Any] = None,
        parameterValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def query_objects(
        self,
        pipelineId: str,
        sphere: str,
        query: Dict[str, Any] = None,
        marker: str = None,
        limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags(self, pipelineId: str, tagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def report_task_progress(
        self, taskId: str, fields: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def report_task_runner_heartbeat(
        self, taskrunnerId: str, workerGroup: str = None, hostname: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_status(self, pipelineId: str, objectIds: List[Any], status: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def set_task_status(
        self,
        taskId: str,
        taskStatus: str,
        errorId: str = None,
        errorMessage: str = None,
        errorStackTrace: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def validate_pipeline_definition(
        self,
        pipelineId: str,
        pipelineObjects: List[Any],
        parameterObjects: List[Any] = None,
        parameterValues: List[Any] = None,
    ) -> Dict[str, Any]:
        pass
