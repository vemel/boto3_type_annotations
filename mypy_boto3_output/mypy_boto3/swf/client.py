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
    def count_closed_workflow_executions(
        self,
        domain: str,
        startTimeFilter: Dict[str, Any] = None,
        closeTimeFilter: Dict[str, Any] = None,
        executionFilter: Dict[str, Any] = None,
        typeFilter: Dict[str, Any] = None,
        tagFilter: Dict[str, Any] = None,
        closeStatusFilter: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def count_open_workflow_executions(
        self,
        domain: str,
        startTimeFilter: Dict[str, Any],
        typeFilter: Dict[str, Any] = None,
        tagFilter: Dict[str, Any] = None,
        executionFilter: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def count_pending_activity_tasks(
        self, domain: str, taskList: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def count_pending_decision_tasks(
        self, domain: str, taskList: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deprecate_activity_type(
        self, domain: str, activityType: Dict[str, Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def deprecate_domain(self, name: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def deprecate_workflow_type(
        self, domain: str, workflowType: Dict[str, Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_activity_type(
        self, domain: str, activityType: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_domain(self, name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_workflow_execution(
        self, domain: str, execution: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_workflow_type(
        self, domain: str, workflowType: Dict[str, Any]
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
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def get_workflow_execution_history(
        self,
        domain: str,
        execution: Dict[str, Any],
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_activity_types(
        self,
        domain: str,
        registrationStatus: str,
        name: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_closed_workflow_executions(
        self,
        domain: str,
        startTimeFilter: Dict[str, Any] = None,
        closeTimeFilter: Dict[str, Any] = None,
        executionFilter: Dict[str, Any] = None,
        closeStatusFilter: Dict[str, Any] = None,
        typeFilter: Dict[str, Any] = None,
        tagFilter: Dict[str, Any] = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_domains(
        self,
        registrationStatus: str,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_open_workflow_executions(
        self,
        domain: str,
        startTimeFilter: Dict[str, Any],
        typeFilter: Dict[str, Any] = None,
        tagFilter: Dict[str, Any] = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
        executionFilter: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, resourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_workflow_types(
        self,
        domain: str,
        registrationStatus: str,
        name: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def poll_for_activity_task(
        self, domain: str, taskList: Dict[str, Any], identity: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def poll_for_decision_task(
        self,
        domain: str,
        taskList: Dict[str, Any],
        identity: str = None,
        nextPageToken: str = None,
        maximumPageSize: int = None,
        reverseOrder: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def record_activity_task_heartbeat(
        self, taskToken: str, details: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_activity_type(
        self,
        domain: str,
        name: str,
        version: str,
        description: str = None,
        defaultTaskStartToCloseTimeout: str = None,
        defaultTaskHeartbeatTimeout: str = None,
        defaultTaskList: Dict[str, Any] = None,
        defaultTaskPriority: str = None,
        defaultTaskScheduleToStartTimeout: str = None,
        defaultTaskScheduleToCloseTimeout: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def register_domain(
        self,
        name: str,
        workflowExecutionRetentionPeriodInDays: str,
        description: str = None,
        tags: List[Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def register_workflow_type(
        self,
        domain: str,
        name: str,
        version: str,
        description: str = None,
        defaultTaskStartToCloseTimeout: str = None,
        defaultExecutionStartToCloseTimeout: str = None,
        defaultTaskList: Dict[str, Any] = None,
        defaultTaskPriority: str = None,
        defaultChildPolicy: str = None,
        defaultLambdaRole: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def request_cancel_workflow_execution(
        self, domain: str, workflowId: str, runId: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def respond_activity_task_canceled(
        self, taskToken: str, details: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def respond_activity_task_completed(
        self, taskToken: str, result: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def respond_activity_task_failed(
        self, taskToken: str, reason: str = None, details: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def respond_decision_task_completed(
        self, taskToken: str, decisions: List[Any] = None, executionContext: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def signal_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        signalName: str,
        runId: str = None,
        input: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def start_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        workflowType: Dict[str, Any],
        taskList: Dict[str, Any] = None,
        taskPriority: str = None,
        input: str = None,
        executionStartToCloseTimeout: str = None,
        tagList: List[Any] = None,
        taskStartToCloseTimeout: str = None,
        childPolicy: str = None,
        lambdaRole: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def terminate_workflow_execution(
        self,
        domain: str,
        workflowId: str,
        runId: str = None,
        reason: str = None,
        details: str = None,
        childPolicy: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def undeprecate_activity_type(
        self, domain: str, activityType: Dict[str, Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def undeprecate_domain(self, name: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def undeprecate_workflow_type(
        self, domain: str, workflowType: Dict[str, Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> None:
        pass
