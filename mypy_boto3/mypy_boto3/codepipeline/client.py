from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def acknowledge_job(
        self,
        jobId: str,
        nonce: str,
    ) -> Dict:
        pass


    def acknowledge_third_party_job(
        self,
        jobId: str,
        nonce: str,
        clientToken: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_custom_action_type(
        self,
        category: str,
        provider: str,
        version: str,
        inputArtifactDetails: Dict,
        outputArtifactDetails: Dict,
        settings: Optional[Dict] = None,
        configurationProperties: Optional[List] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_pipeline(
        self,
        pipeline: Dict,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_custom_action_type(
        self,
        category: str,
        provider: str,
        version: str,
    ):
        pass


    def delete_pipeline(
        self,
        name: str,
    ):
        pass


    def delete_webhook(
        self,
        name: str,
    ) -> Dict:
        pass


    def deregister_webhook_with_third_party(
        self,
        webhookName: Optional[str] = None,
    ) -> Dict:
        pass


    def disable_stage_transition(
        self,
        pipelineName: str,
        stageName: str,
        transitionType: str,
        reason: str,
    ):
        pass


    def enable_stage_transition(
        self,
        pipelineName: str,
        stageName: str,
        transitionType: str,
    ):
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_job_details(
        self,
        jobId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_pipeline(
        self,
        name: str,
        version: Optional[int] = None,
    ) -> Dict:
        pass


    def get_pipeline_execution(
        self,
        pipelineName: str,
        pipelineExecutionId: str,
    ) -> Dict:
        pass


    def get_pipeline_state(
        self,
        name: str,
    ) -> Dict:
        pass


    def get_third_party_job_details(
        self,
        jobId: str,
        clientToken: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_action_executions(
        self,
        pipelineName: str,
        filter: Optional[Dict] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_action_types(
        self,
        actionOwnerFilter: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_pipeline_executions(
        self,
        pipelineName: str,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_pipelines(
        self,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_webhooks(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def poll_for_jobs(
        self,
        actionTypeId: Dict,
        maxBatchSize: Optional[int] = None,
        queryParam: Optional[Dict] = None,
    ) -> Dict:
        pass


    def poll_for_third_party_jobs(
        self,
        actionTypeId: Dict,
        maxBatchSize: Optional[int] = None,
    ) -> Dict:
        pass


    def put_action_revision(
        self,
        pipelineName: str,
        stageName: str,
        actionName: str,
        actionRevision: Dict,
    ) -> Dict:
        pass


    def put_approval_result(
        self,
        pipelineName: str,
        stageName: str,
        actionName: str,
        result: Dict,
        token: str,
    ) -> Dict:
        pass


    def put_job_failure_result(
        self,
        jobId: str,
        failureDetails: Dict,
    ):
        pass


    def put_job_success_result(
        self,
        jobId: str,
        currentRevision: Optional[Dict] = None,
        continuationToken: Optional[str] = None,
        executionDetails: Optional[Dict] = None,
    ):
        pass


    def put_third_party_job_failure_result(
        self,
        jobId: str,
        clientToken: str,
        failureDetails: Dict,
    ):
        pass


    def put_third_party_job_success_result(
        self,
        jobId: str,
        clientToken: str,
        currentRevision: Optional[Dict] = None,
        continuationToken: Optional[str] = None,
        executionDetails: Optional[Dict] = None,
    ):
        pass


    def put_webhook(
        self,
        webhook: Dict,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def register_webhook_with_third_party(
        self,
        webhookName: Optional[str] = None,
    ) -> Dict:
        pass


    def retry_stage_execution(
        self,
        pipelineName: str,
        stageName: str,
        pipelineExecutionId: str,
        retryMode: str,
    ) -> Dict:
        pass


    def start_pipeline_execution(
        self,
        name: str,
        clientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_pipeline(
        self,
        pipeline: Dict,
    ) -> Dict:
        pass

