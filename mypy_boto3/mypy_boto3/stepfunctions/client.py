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


    def create_activity(
        self,
        name: str,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_state_machine(
        self,
        name: str,
        definition: str,
        roleArn: str,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_activity(
        self,
        activityArn: str,
    ) -> Dict:
        pass


    def delete_state_machine(
        self,
        stateMachineArn: str,
    ) -> Dict:
        pass


    def describe_activity(
        self,
        activityArn: str,
    ) -> Dict:
        pass


    def describe_execution(
        self,
        executionArn: str,
    ) -> Dict:
        pass


    def describe_state_machine(
        self,
        stateMachineArn: str,
    ) -> Dict:
        pass


    def describe_state_machine_for_execution(
        self,
        executionArn: str,
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


    def get_activity_task(
        self,
        activityArn: str,
        workerName: Optional[str] = None,
    ) -> Dict:
        pass


    def get_execution_history(
        self,
        executionArn: str,
        maxResults: Optional[int] = None,
        reverseOrder: Optional[bool] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
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


    def list_activities(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_executions(
        self,
        stateMachineArn: str,
        statusFilter: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_state_machines(
        self,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def send_task_failure(
        self,
        taskToken: str,
        error: Optional[str] = None,
        cause: Optional[str] = None,
    ) -> Dict:
        pass


    def send_task_heartbeat(
        self,
        taskToken: str,
    ) -> Dict:
        pass


    def send_task_success(
        self,
        taskToken: str,
        output: str,
    ) -> Dict:
        pass


    def start_execution(
        self,
        stateMachineArn: str,
        name: Optional[str] = None,
        input: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_execution(
        self,
        executionArn: str,
        error: Optional[str] = None,
        cause: Optional[str] = None,
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


    def update_state_machine(
        self,
        stateMachineArn: str,
        definition: Optional[str] = None,
        roleArn: Optional[str] = None,
    ) -> Dict:
        pass

