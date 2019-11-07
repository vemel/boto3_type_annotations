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


    def cancel_update_stack(
        self,
        StackName: str,
        ClientRequestToken: Optional[str] = None,
    ):
        pass


    def continue_update_rollback(
        self,
        StackName: str,
        RoleARN: Optional[str] = None,
        ResourcesToSkip: Optional[List] = None,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_change_set(
        self,
        StackName: str,
        ChangeSetName: str,
        TemplateBody: Optional[str] = None,
        TemplateURL: Optional[str] = None,
        UsePreviousTemplate: Optional[bool] = None,
        Parameters: Optional[List] = None,
        Capabilities: Optional[List] = None,
        ResourceTypes: Optional[List] = None,
        RoleARN: Optional[str] = None,
        RollbackConfiguration: Optional[Dict] = None,
        NotificationARNs: Optional[List] = None,
        Tags: Optional[List] = None,
        ClientToken: Optional[str] = None,
        Description: Optional[str] = None,
        ChangeSetType: Optional[str] = None,
    ) -> Dict:
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
    ) -> Dict:
        pass


    def create_stack_instances(
        self,
        StackSetName: str,
        Accounts: List,
        Regions: List,
        ParameterOverrides: Optional[List] = None,
        OperationPreferences: Optional[Dict] = None,
        OperationId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_stack_set(
        self,
        StackSetName: str,
        Description: Optional[str] = None,
        TemplateBody: Optional[str] = None,
        TemplateURL: Optional[str] = None,
        Parameters: Optional[List] = None,
        Capabilities: Optional[List] = None,
        Tags: Optional[List] = None,
        AdministrationRoleARN: Optional[str] = None,
        ExecutionRoleName: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_change_set(
        self,
        ChangeSetName: str,
        StackName: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_stack(
        self,
        StackName: str,
        RetainResources: Optional[List] = None,
        RoleARN: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
    ):
        pass


    def delete_stack_instances(
        self,
        StackSetName: str,
        Accounts: List,
        Regions: List,
        RetainStacks: bool,
        OperationPreferences: Optional[Dict] = None,
        OperationId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_stack_set(
        self,
        StackSetName: str,
    ) -> Dict:
        pass


    def describe_account_limits(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_change_set(
        self,
        ChangeSetName: str,
        StackName: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_stack_drift_detection_status(
        self,
        StackDriftDetectionId: str,
    ) -> Dict:
        pass


    def describe_stack_events(
        self,
        StackName: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_stack_instance(
        self,
        StackSetName: str,
        StackInstanceAccount: str,
        StackInstanceRegion: str,
    ) -> Dict:
        pass


    def describe_stack_resource(
        self,
        StackName: str,
        LogicalResourceId: str,
    ) -> Dict:
        pass


    def describe_stack_resource_drifts(
        self,
        StackName: str,
        StackResourceDriftStatusFilters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_stack_resources(
        self,
        StackName: Optional[str] = None,
        LogicalResourceId: Optional[str] = None,
        PhysicalResourceId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_stack_set(
        self,
        StackSetName: str,
    ) -> Dict:
        pass


    def describe_stack_set_operation(
        self,
        StackSetName: str,
        OperationId: str,
    ) -> Dict:
        pass


    def describe_stacks(
        self,
        StackName: Optional[str] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def detect_stack_drift(
        self,
        StackName: str,
        LogicalResourceIds: Optional[List] = None,
    ) -> Dict:
        pass


    def detect_stack_resource_drift(
        self,
        StackName: str,
        LogicalResourceId: str,
    ) -> Dict:
        pass


    def estimate_template_cost(
        self,
        TemplateBody: Optional[str] = None,
        TemplateURL: Optional[str] = None,
        Parameters: Optional[List] = None,
    ) -> Dict:
        pass


    def execute_change_set(
        self,
        ChangeSetName: str,
        StackName: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
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


    def get_stack_policy(
        self,
        StackName: str,
    ) -> Dict:
        pass


    def get_template(
        self,
        StackName: Optional[str] = None,
        ChangeSetName: Optional[str] = None,
        TemplateStage: Optional[str] = None,
    ) -> Dict:
        pass


    def get_template_summary(
        self,
        TemplateBody: Optional[str] = None,
        TemplateURL: Optional[str] = None,
        StackName: Optional[str] = None,
        StackSetName: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_change_sets(
        self,
        StackName: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_exports(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_imports(
        self,
        ExportName: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_stack_instances(
        self,
        StackSetName: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        StackInstanceAccount: Optional[str] = None,
        StackInstanceRegion: Optional[str] = None,
    ) -> Dict:
        pass


    def list_stack_resources(
        self,
        StackName: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_stack_set_operation_results(
        self,
        StackSetName: str,
        OperationId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_stack_set_operations(
        self,
        StackSetName: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_stack_sets(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Status: Optional[str] = None,
    ) -> Dict:
        pass


    def list_stacks(
        self,
        NextToken: Optional[str] = None,
        StackStatusFilter: Optional[List] = None,
    ) -> Dict:
        pass


    def set_stack_policy(
        self,
        StackName: str,
        StackPolicyBody: Optional[str] = None,
        StackPolicyURL: Optional[str] = None,
    ):
        pass


    def signal_resource(
        self,
        StackName: str,
        LogicalResourceId: str,
        UniqueId: str,
        Status: str,
    ):
        pass


    def stop_stack_set_operation(
        self,
        StackSetName: str,
        OperationId: str,
    ) -> Dict:
        pass


    def update_stack(
        self,
        StackName: str,
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


    def update_stack_instances(
        self,
        StackSetName: str,
        Accounts: List,
        Regions: List,
        ParameterOverrides: Optional[List] = None,
        OperationPreferences: Optional[Dict] = None,
        OperationId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_stack_set(
        self,
        StackSetName: str,
        Description: Optional[str] = None,
        TemplateBody: Optional[str] = None,
        TemplateURL: Optional[str] = None,
        UsePreviousTemplate: Optional[bool] = None,
        Parameters: Optional[List] = None,
        Capabilities: Optional[List] = None,
        Tags: Optional[List] = None,
        OperationPreferences: Optional[Dict] = None,
        AdministrationRoleARN: Optional[str] = None,
        ExecutionRoleName: Optional[str] = None,
        OperationId: Optional[str] = None,
        Accounts: Optional[List] = None,
        Regions: Optional[List] = None,
    ) -> Dict:
        pass


    def update_termination_protection(
        self,
        EnableTerminationProtection: bool,
        StackName: str,
    ) -> Dict:
        pass


    def validate_template(
        self,
        TemplateBody: Optional[str] = None,
        TemplateURL: Optional[str] = None,
    ) -> Dict:
        pass

