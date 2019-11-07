from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from boto3.resources.base import ServiceResource
from boto3.resources.collection import ResourceCollection


class ServiceResource(base.ServiceResource):
    stacks: 'stacks'

    def Event(
        self,
        id: Optional[str] = None,
    ) -> 'Event':
        pass


    def Stack(
        self,
        name: Optional[str] = None,
    ) -> 'Stack':
        pass


    def StackResource(
        self,
        stack_name: Optional[str] = None,
        logical_id: Optional[str] = None,
    ) -> 'StackResource':
        pass


    def StackResourceSummary(
        self,
        stack_name: Optional[str] = None,
        logical_id: Optional[str] = None,
    ) -> 'StackResourceSummary':
        pass


    def create_stack(
        self,
        StackName: str,
        TemplateBody: Optional[str] = None,
        TemplateURL: Optional[str] = None,
        Parameters: Optional[List] = None,
        DisableRollback: Optional[bool] = None,
        RollbackConfiguration: Optional[Dict] = None,
        TimeoutInMinutes: Optional[int] = None,
        NotificationARNs: Optional[List] = None,
        Capabilities: Optional[List] = None,
        ResourceTypes: Optional[List] = None,
        RoleARN: Optional[str] = None,
        OnFailure: Optional[str] = None,
        StackPolicyBody: Optional[str] = None,
        StackPolicyURL: Optional[str] = None,
        Tags: Optional[List] = None,
        ClientRequestToken: Optional[str] = None,
        EnableTerminationProtection: Optional[bool] = None,
    ) -> 'Stack':
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass



class Event(base.ServiceResource):
    stack_id: str
    event_id: str
    stack_name: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    timestamp: datetime
    resource_status: str
    resource_status_reason: str
    resource_properties: str
    client_request_token: str
    id: str

    def get_available_subresources(
        self,
    ) -> List[str]:
        pass



class Stack(base.ServiceResource):
    stack_id: str
    stack_name: str
    change_set_id: str
    description: str
    parameters: List
    creation_time: datetime
    deletion_time: datetime
    last_updated_time: datetime
    rollback_configuration: Dict
    stack_status: str
    stack_status_reason: str
    disable_rollback: bool
    notification_arns: List
    timeout_in_minutes: int
    capabilities: List
    outputs: List
    role_arn: str
    tags: List
    enable_termination_protection: bool
    parent_id: str
    root_id: str
    drift_information: Dict
    name: str
    events: 'events'
    resource_summaries: 'resource_summaries'

    def cancel_update(
        self,
        ClientRequestToken: Optional[str] = None,
    ):
        pass


    def delete(
        self,
        RetainResources: Optional[List] = None,
        RoleARN: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass


    def update(
        self,
        TemplateBody: Optional[str] = None,
        TemplateURL: Optional[str] = None,
        UsePreviousTemplate: Optional[bool] = None,
        StackPolicyDuringUpdateBody: Optional[str] = None,
        StackPolicyDuringUpdateURL: Optional[str] = None,
        Parameters: Optional[List] = None,
        Capabilities: Optional[List] = None,
        ResourceTypes: Optional[List] = None,
        RoleARN: Optional[str] = None,
        RollbackConfiguration: Optional[Dict] = None,
        StackPolicyBody: Optional[str] = None,
        StackPolicyURL: Optional[str] = None,
        NotificationARNs: Optional[List] = None,
        Tags: Optional[List] = None,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass



class StackResource(base.ServiceResource):
    stack_id: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    description: str
    metadata: str
    drift_information: Dict
    stack_name: str
    logical_id: str

    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class StackResourceSummary(base.ServiceResource):
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    drift_information: Dict
    stack_name: str
    logical_id: str

    def get_available_subresources(
        self,
    ) -> List[str]:
        pass



class stacks(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Stack']:
        pass


    @classmethod
    def filter(
        cls,
        StackName: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> List['Stack']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Stack']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Stack']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass

