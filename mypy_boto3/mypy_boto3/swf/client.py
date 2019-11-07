from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def count_closed_workflow_executions(
        self,
        domain: str,
        startTimeFilter: Optional[Dict] = None,
        closeTimeFilter: Optional[Dict] = None,
        executionFilter: Optional[Dict] = None,
        typeFilter: Optional[Dict] = None,
        tagFilter: Optional[Dict] = None,
        closeStatusFilter: Optional[Dict] = None,
    ) -> Dict:
        pass


    def count_open_workflow_executions(
        self,
        domain: str,
        startTimeFilter: Dict,
        typeFilter: Optional[Dict] = None,
        tagFilter: Optional[Dict] = None,
        executionFilter: Optional[Dict] = None,
    ) -> Dict:
        pass


    def count_pending_activity_tasks(
        self,
        domain: str,
        taskList: Dict,
    ) -> Dict:
        pass


    def count_pending_decision_tasks(
        self,
        domain: str,
        taskList: Dict,
    ) -> Dict:
        pass


    def deprecate_activity_type(
        self,
        domain: str,
        activityType: Dict,
    ):
        pass


    def deprecate_domain(
        self,
        name: str,
    ):
        pass


    def deprecate_workflow_type(
        self,
        domain: str,
        workflowType: Dict,
    ):
        pass


    def describe_activity_type(
        self,
        domain: str,
        activityType: Dict,
    ) -> Dict:
        pass


    def describe_domain(
        self,
        name: str,
    ) -> Dict:
        pass


    def describe_workflow_execution(
        self,
        domain: str,
        execution: Dict,
    ) -> Dict:
        pass


    def describe_workflow_type(
        self,
        domain: str,
        workflowType: Dict,
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


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def get_workflow_execution_history(
        self,
        domain: str,
        execution: Dict,
        nextPageToken: Optional[str] = None,
        maximumPageSize: Optional[int] = None,
        reverseOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_activity_types(
        self,
        domain: str,
        registrationStatus: str,
        name: Optional[str] = None,
        nextPageToken: Optional[str] = None,
        maximumPageSize: Optional[int] = None,
        reverseOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_closed_workflow_executions(
        self,
        domain: str,
        startTimeFilter: Optional[Dict] = None,
        closeTimeFilter: Optional[Dict] = None,
        executionFilter: Optional[Dict] = None,
        closeStatusFilter: Optional[Dict] = None,
        typeFilter: Optional[Dict] = None,
        tagFilter: Optional[Dict] = None,
        nextPageToken: Optional[str] = None,
        maximumPageSize: Optional[int] = None,
        reverseOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_domains(
        self,
        registrationStatus: str,
        nextPageToken: Optional[str] = None,
        maximumPageSize: Optional[int] = None,
        reverseOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_open_workflow_executions(
        self,
        domain: str,
        startTimeFilter: Dict,
        typeFilter: Optional[Dict] = None,
        tagFilter: Optional[Dict] = None,
        nextPageToken: Optional[str] = None,
        maximumPageSize: Optional[int] = None,
        reverseOrder: Optional[bool] = None,
        executionFilter: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def list_workflow_types(
        self,
        domain: str,
        registrationStatus: str,
        name: Optional[str] = None,
        nextPageToken: Optional[str] = None,
        maximumPageSize: Optional[int] = None,
        reverseOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def poll_for_activity_task(
        self,
        domain: str,
        taskList: Dict,
        identity: Optional[str] = None,
    ) -> Dict:
        pass


    def poll_for_decision_task(
        self,
        domain: str,
        taskList: Dict,
        identity: Optional[str] = None,
        nextPageToken: Optional[str] = None,
        maximumPageSize: Optional[int] = None,
        reverseOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def record_activity_task_heartbeat(
        self,
        taskToken: str,
        details: Optional[str] = None,
    ) -> Dict:
        pass


    def register_activity_type(
        self,
        domain: str,
        name: str,
        version: str,
        description: Optional[str] = None,
        defaultTaskStartToCloseTimeout: Optional[str] = None,
        defaultTaskHeartbeatTimeout: Optional[str] = None,
        defaultTaskList: Optional[Dict] = None,
        defaultTaskPriority: Optional[str] = None,
        defaultTaskScheduleToStartTimeout: Optional[str] = None,
        defaultTaskScheduleToCloseTimeout: Optional[str] = None,
    ):
        pass


    def register_domain(
        self,
        name: str,
        workflowExecutionRetentionPeriodInDays: str,
        description: Optional[str] = None,
        tags: Optional[List] = None,
    ):
        pass


    def register_workflow_type(
        self,
        domain: str,
        name: str,
        version: str,
        description: Optional[str] = None,
        defaultTaskStartToCloseTimeout: Optional[str] = None,
        defaultExecutionStartToCloseTimeout: Optional[str] = None,
        defaultTaskList: Optional[Dict] = None,
        defaultTaskPriority: Optional[str] = None,
        defaultChildPolicy: Optional[str] = None,
        defaultLambdaRole: Optional[str] = None,
    ):
        pass


    def request_cancel_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        runId: Optional[str] = None,
    ):
        pass


    def respond_activity_task_canceled(
        self,
        taskToken: str,
        details: Optional[str] = None,
    ):
        pass


    def respond_activity_task_completed(
        self,
        taskToken: str,
        result: Optional[str] = None,
    ):
        pass


    def respond_activity_task_failed(
        self,
        taskToken: str,
        reason: Optional[str] = None,
        details: Optional[str] = None,
    ):
        pass


    def respond_decision_task_completed(
        self,
        taskToken: str,
        decisions: Optional[List] = None,
        executionContext: Optional[str] = None,
    ):
        pass


    def signal_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        signalName: str,
        runId: Optional[str] = None,
        input: Optional[str] = None,
    ):
        pass


    def start_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        workflowType: Dict,
        taskList: Optional[Dict] = None,
        taskPriority: Optional[str] = None,
        input: Optional[str] = None,
        executionStartToCloseTimeout: Optional[str] = None,
        tagList: Optional[List] = None,
        taskStartToCloseTimeout: Optional[str] = None,
        childPolicy: Optional[str] = None,
        lambdaRole: Optional[str] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: List,
    ):
        pass


    def terminate_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        runId: Optional[str] = None,
        reason: Optional[str] = None,
        details: Optional[str] = None,
        childPolicy: Optional[str] = None,
    ):
        pass


    def undeprecate_activity_type(
        self,
        domain: str,
        activityType: Dict,
    ):
        pass


    def undeprecate_domain(
        self,
        name: str,
    ):
        pass


    def undeprecate_workflow_type(
        self,
        domain: str,
        workflowType: Dict,
    ):
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ):
        pass

