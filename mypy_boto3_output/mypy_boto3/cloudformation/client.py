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
    def cancel_update_stack(
        self, StackName: str, ClientRequestToken: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def continue_update_rollback(
        self,
        StackName: str,
        RoleARN: str = None,
        ResourcesToSkip: List[Any] = None,
        ClientRequestToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_change_set(
        self,
        StackName: str,
        ChangeSetName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        Parameters: List[Any] = None,
        Capabilities: List[Any] = None,
        ResourceTypes: List[Any] = None,
        RoleARN: str = None,
        RollbackConfiguration: Dict[str, Any] = None,
        NotificationARNs: List[Any] = None,
        Tags: List[Any] = None,
        ClientToken: str = None,
        Description: str = None,
        ChangeSetType: str = None,
    ) -> Dict[str, Any]:
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
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_stack_instances(
        self,
        StackSetName: str,
        Accounts: List[Any],
        Regions: List[Any],
        ParameterOverrides: List[Any] = None,
        OperationPreferences: Dict[str, Any] = None,
        OperationId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_stack_set(
        self,
        StackSetName: str,
        Description: str = None,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List[Any] = None,
        Capabilities: List[Any] = None,
        Tags: List[Any] = None,
        AdministrationRoleARN: str = None,
        ExecutionRoleName: str = None,
        ClientRequestToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_change_set(
        self, ChangeSetName: str, StackName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_stack(
        self,
        StackName: str,
        RetainResources: List[Any] = None,
        RoleARN: str = None,
        ClientRequestToken: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_stack_instances(
        self,
        StackSetName: str,
        Accounts: List[Any],
        Regions: List[Any],
        RetainStacks: bool,
        OperationPreferences: Dict[str, Any] = None,
        OperationId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_stack_set(self, StackSetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_account_limits(self, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_change_set(
        self, ChangeSetName: str, StackName: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stack_drift_detection_status(
        self, StackDriftDetectionId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stack_events(
        self, StackName: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stack_instance(
        self, StackSetName: str, StackInstanceAccount: str, StackInstanceRegion: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stack_resource(
        self, StackName: str, LogicalResourceId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stack_resource_drifts(
        self,
        StackName: str,
        StackResourceDriftStatusFilters: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stack_resources(
        self,
        StackName: str = None,
        LogicalResourceId: str = None,
        PhysicalResourceId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stack_set(self, StackSetName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stack_set_operation(
        self, StackSetName: str, OperationId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stacks(
        self, StackName: str = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_stack_drift(
        self, StackName: str, LogicalResourceIds: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_stack_resource_drift(
        self, StackName: str, LogicalResourceId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def estimate_template_cost(
        self,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def execute_change_set(
        self, ChangeSetName: str, StackName: str = None, ClientRequestToken: str = None
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
    def get_stack_policy(self, StackName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_template(
        self,
        StackName: str = None,
        ChangeSetName: str = None,
        TemplateStage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_template_summary(
        self,
        TemplateBody: str = None,
        TemplateURL: str = None,
        StackName: str = None,
        StackSetName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_change_sets(self, StackName: str, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_exports(self, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_imports(self, ExportName: str, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_stack_instances(
        self,
        StackSetName: str,
        NextToken: str = None,
        MaxResults: int = None,
        StackInstanceAccount: str = None,
        StackInstanceRegion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_stack_resources(
        self, StackName: str, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_stack_set_operation_results(
        self,
        StackSetName: str,
        OperationId: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_stack_set_operations(
        self, StackSetName: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_stack_sets(
        self, NextToken: str = None, MaxResults: int = None, Status: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_stacks(
        self, NextToken: str = None, StackStatusFilter: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def set_stack_policy(
        self, StackName: str, StackPolicyBody: str = None, StackPolicyURL: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def signal_resource(
        self, StackName: str, LogicalResourceId: str, UniqueId: str, Status: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_stack_set_operation(
        self, StackSetName: str, OperationId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_stack(
        self,
        StackName: str,
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

    # pylint: disable=arguments-differ
    def update_stack_instances(
        self,
        StackSetName: str,
        Accounts: List[Any],
        Regions: List[Any],
        ParameterOverrides: List[Any] = None,
        OperationPreferences: Dict[str, Any] = None,
        OperationId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_stack_set(
        self,
        StackSetName: str,
        Description: str = None,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        Parameters: List[Any] = None,
        Capabilities: List[Any] = None,
        Tags: List[Any] = None,
        OperationPreferences: Dict[str, Any] = None,
        AdministrationRoleARN: str = None,
        ExecutionRoleName: str = None,
        OperationId: str = None,
        Accounts: List[Any] = None,
        Regions: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_termination_protection(
        self, EnableTerminationProtection: bool, StackName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def validate_template(
        self, TemplateBody: str = None, TemplateURL: str = None
    ) -> Dict[str, Any]:
        pass
