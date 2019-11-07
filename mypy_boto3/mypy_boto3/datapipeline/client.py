from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def activate_pipeline(
        self,
        pipelineId: str,
        parameterValues: Optional[List] = None,
        startTimestamp: Optional[datetime] = None,
    ) -> Dict:
        pass


    def add_tags(
        self,
        pipelineId: str,
        tags: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_pipeline(
        self,
        name: str,
        uniqueId: str,
        description: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def deactivate_pipeline(
        self,
        pipelineId: str,
        cancelActive: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_pipeline(
        self,
        pipelineId: str,
    ):
        pass


    def describe_objects(
        self,
        pipelineId: str,
        objectIds: List,
        evaluateExpressions: Optional[bool] = None,
        marker: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_pipelines(
        self,
        pipelineIds: List,
    ) -> Dict:
        pass


    def evaluate_expression(
        self,
        pipelineId: str,
        objectId: str,
        expression: str,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_pipeline_definition(
        self,
        pipelineId: str,
        version: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_pipelines(
        self,
        marker: Optional[str] = None,
    ) -> Dict:
        pass


    def poll_for_task(
        self,
        workerGroup: str,
        hostname: Optional[str] = None,
        instanceIdentity: Optional[Dict] = None,
    ) -> Dict:
        pass


    def put_pipeline_definition(
        self,
        pipelineId: str,
        pipelineObjects: List,
        parameterObjects: Optional[List] = None,
        parameterValues: Optional[List] = None,
    ) -> Dict:
        pass


    def query_objects(
        self,
        pipelineId: str,
        sphere: str,
        query: Optional[Dict] = None,
        marker: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict:
        pass


    def remove_tags(
        self,
        pipelineId: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def report_task_progress(
        self,
        taskId: str,
        fields: Optional[List] = None,
    ) -> Dict:
        pass


    def report_task_runner_heartbeat(
        self,
        taskrunnerId: str,
        workerGroup: Optional[str] = None,
        hostname: Optional[str] = None,
    ) -> Dict:
        pass


    def set_status(
        self,
        pipelineId: str,
        objectIds: List,
        status: str,
    ):
        pass


    def set_task_status(
        self,
        taskId: str,
        taskStatus: str,
        errorId: Optional[str] = None,
        errorMessage: Optional[str] = None,
        errorStackTrace: Optional[str] = None,
    ) -> Dict:
        pass


    def validate_pipeline_definition(
        self,
        pipelineId: str,
        pipelineObjects: List,
        parameterObjects: Optional[List] = None,
        parameterValues: Optional[List] = None,
    ) -> Dict:
        pass

