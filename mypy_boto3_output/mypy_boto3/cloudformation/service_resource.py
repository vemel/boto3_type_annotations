from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3.cloudformation.service_resource as cloudformation_service_resource_scope


class ServiceResource(Boto3ServiceResource):
    stacks: cloudformation_service_resource_scope.stacks

    # pylint: disable=arguments-differ
    def Event(self, id: str = None) -> cloudformation_service_resource_scope.Event:
        pass

    # pylint: disable=arguments-differ
    def Stack(self, name: str = None) -> cloudformation_service_resource_scope.Stack:
        pass

    # pylint: disable=arguments-differ
    def StackResource(
        self, stack_name: str = None, logical_id: str = None
    ) -> cloudformation_service_resource_scope.StackResource:
        pass

    # pylint: disable=arguments-differ
    def StackResourceSummary(
        self, stack_name: str = None, logical_id: str = None
    ) -> cloudformation_service_resource_scope.StackResourceSummary:
        pass

    # pylint: disable=arguments-differ
    def create_stack(
        self,
        StackName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List[Any] = None,
        DisableRollback: bool = None,
        RollbackConfiguration: Dict[str, Any] = None,
        TimeoutInMinutes: int = None,
        NotificationARNs: List[Any] = None,
        Capabilities: List[Any] = None,
        ResourceTypes: List[Any] = None,
        RoleARN: str = None,
        OnFailure: str = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        Tags: List[Any] = None,
        ClientRequestToken: str = None,
        EnableTerminationProtection: bool = None,
    ) -> cloudformation_service_resource_scope.Stack:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class Event(Boto3ServiceResource):
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

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class Stack(Boto3ServiceResource):
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
    events: cloudformation_service_resource_scope.events
    resource_summaries: cloudformation_service_resource_scope.resource_summaries

    # pylint: disable=arguments-differ
    def cancel_update(self, ClientRequestToken: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete(
        self,
        RetainResources: List[Any] = None,
        RoleARN: str = None,
        ClientRequestToken: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def update(
        self,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        StackPolicyDuringUpdateBody: str = None,
        StackPolicyDuringUpdateURL: str = None,
        Parameters: List[Any] = None,
        Capabilities: List[Any] = None,
        ResourceTypes: List[Any] = None,
        RoleARN: str = None,
        RollbackConfiguration: Dict[str, Any] = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        NotificationARNs: List[Any] = None,
        Tags: List[Any] = None,
        ClientRequestToken: str = None,
    ) -> Dict[str, Any]:
        pass


class StackResource(Boto3ServiceResource):
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

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class StackResourceSummary(Boto3ServiceResource):
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    drift_information: Dict
    stack_name: str
    logical_id: str

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class stacks(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[cloudformation_service_resource_scope.Stack]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, StackName: str = None, NextToken: str = None
    ) -> List[cloudformation_service_resource_scope.Stack]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[cloudformation_service_resource_scope.Stack]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[cloudformation_service_resource_scope.Stack]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class events(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[cloudformation_service_resource_scope.Event]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, NextToken: str = None
    ) -> List[cloudformation_service_resource_scope.Event]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[cloudformation_service_resource_scope.Event]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[cloudformation_service_resource_scope.Event]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class resource_summaries(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[cloudformation_service_resource_scope.StackResourceSummary]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, NextToken: str = None
    ) -> List[cloudformation_service_resource_scope.StackResourceSummary]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[cloudformation_service_resource_scope.StackResourceSummary]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[cloudformation_service_resource_scope.StackResourceSummary]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass
