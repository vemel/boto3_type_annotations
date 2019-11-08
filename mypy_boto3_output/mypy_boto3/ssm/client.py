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
    def add_tags_to_resource(
        self, ResourceType: str, ResourceId: str, Tags: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_command(
        self, CommandId: str, InstanceIds: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def cancel_maintenance_window_execution(
        self, WindowExecutionId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_activation(
        self,
        IamRole: str,
        Description: str = None,
        DefaultInstanceName: str = None,
        RegistrationLimit: int = None,
        ExpirationDate: datetime = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_association(
        self,
        Name: str,
        DocumentVersion: str = None,
        InstanceId: str = None,
        Parameters: Dict[str, Any] = None,
        Targets: List[Any] = None,
        ScheduleExpression: str = None,
        OutputLocation: Dict[str, Any] = None,
        AssociationName: str = None,
        AutomationTargetParameterName: str = None,
        MaxErrors: str = None,
        MaxConcurrency: str = None,
        ComplianceSeverity: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_association_batch(self, Entries: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_document(
        self,
        Content: str,
        Name: str,
        Attachments: List[Any] = None,
        VersionName: str = None,
        DocumentType: str = None,
        DocumentFormat: str = None,
        TargetType: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_maintenance_window(
        self,
        Name: str,
        Schedule: str,
        Duration: int,
        Cutoff: int,
        AllowUnassociatedTargets: bool,
        Description: str = None,
        StartDate: str = None,
        EndDate: str = None,
        ScheduleTimezone: str = None,
        ClientToken: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_ops_item(
        self,
        Description: str,
        Source: str,
        Title: str,
        OperationalData: Dict[str, Any] = None,
        Notifications: List[Any] = None,
        Priority: int = None,
        RelatedOpsItems: List[Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_patch_baseline(
        self,
        Name: str,
        OperatingSystem: str = None,
        GlobalFilters: Dict[str, Any] = None,
        ApprovalRules: Dict[str, Any] = None,
        ApprovedPatches: List[Any] = None,
        ApprovedPatchesComplianceLevel: str = None,
        ApprovedPatchesEnableNonSecurity: bool = None,
        RejectedPatches: List[Any] = None,
        RejectedPatchesAction: str = None,
        Description: str = None,
        Sources: List[Any] = None,
        ClientToken: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_resource_data_sync(
        self, SyncName: str, S3Destination: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_activation(self, ActivationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_association(
        self, Name: str = None, InstanceId: str = None, AssociationId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_document(
        self, Name: str, DocumentVersion: str = None, VersionName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_inventory(
        self,
        TypeName: str,
        SchemaDeleteOption: str = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_maintenance_window(self, WindowId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_parameter(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_parameters(self, Names: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_patch_baseline(self, BaselineId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_resource_data_sync(self, SyncName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_managed_instance(self, InstanceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_patch_baseline_for_patch_group(
        self, BaselineId: str, PatchGroup: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_target_from_maintenance_window(
        self, WindowId: str, WindowTargetId: str, Safe: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_task_from_maintenance_window(
        self, WindowId: str, WindowTaskId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_activations(
        self, Filters: List[Any] = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_association(
        self,
        Name: str = None,
        InstanceId: str = None,
        AssociationId: str = None,
        AssociationVersion: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_association_execution_targets(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_association_executions(
        self,
        AssociationId: str,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_automation_executions(
        self, Filters: List[Any] = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_automation_step_executions(
        self,
        AutomationExecutionId: str,
        Filters: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
        ReverseOrder: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_available_patches(
        self, Filters: List[Any] = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_document(
        self, Name: str, DocumentVersion: str = None, VersionName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_document_permission(
        self, Name: str, PermissionType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_effective_instance_associations(
        self, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_effective_patches_for_patch_baseline(
        self, BaselineId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_instance_associations_status(
        self, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_instance_information(
        self,
        InstanceInformationFilterList: List[Any] = None,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_instance_patch_states(
        self, InstanceIds: List[Any], NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_instance_patch_states_for_patch_group(
        self,
        PatchGroup: str,
        Filters: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_instance_patches(
        self,
        InstanceId: str,
        Filters: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_inventory_deletions(
        self, DeletionId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_maintenance_window_execution_task_invocations(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_maintenance_window_execution_tasks(
        self,
        WindowExecutionId: str,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_maintenance_window_executions(
        self,
        WindowId: str,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_maintenance_window_schedule(
        self,
        WindowId: str = None,
        Targets: List[Any] = None,
        ResourceType: str = None,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_maintenance_window_targets(
        self,
        WindowId: str,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_maintenance_window_tasks(
        self,
        WindowId: str,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_maintenance_windows(
        self, Filters: List[Any] = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_maintenance_windows_for_target(
        self,
        Targets: List[Any],
        ResourceType: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_ops_items(
        self,
        OpsItemFilters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_parameters(
        self,
        Filters: List[Any] = None,
        ParameterFilters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_patch_baselines(
        self, Filters: List[Any] = None, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_patch_group_state(self, PatchGroup: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_patch_groups(
        self, MaxResults: int = None, Filters: List[Any] = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_patch_properties(
        self,
        OperatingSystem: str,
        Property: str,
        PatchSet: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_sessions(
        self,
        State: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[Any] = None,
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
    def get_automation_execution(self, AutomationExecutionId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_command_invocation(
        self, CommandId: str, InstanceId: str, PluginName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_connection_status(self, Target: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_default_patch_baseline(self, OperatingSystem: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_deployable_patch_snapshot_for_instance(
        self, InstanceId: str, SnapshotId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_document(
        self,
        Name: str,
        VersionName: str = None,
        DocumentVersion: str = None,
        DocumentFormat: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_inventory(
        self,
        Filters: List[Any] = None,
        Aggregators: List[Any] = None,
        ResultAttributes: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_inventory_schema(
        self,
        TypeName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Aggregator: bool = None,
        SubType: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_maintenance_window(self, WindowId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_maintenance_window_execution(
        self, WindowExecutionId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_maintenance_window_execution_task(
        self, WindowExecutionId: str, TaskId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_maintenance_window_execution_task_invocation(
        self, WindowExecutionId: str, TaskId: str, InvocationId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_maintenance_window_task(
        self, WindowId: str, WindowTaskId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_ops_item(self, OpsItemId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_ops_summary(
        self,
        Aggregators: List[Any],
        Filters: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_parameter(self, Name: str, WithDecryption: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_parameter_history(
        self,
        Name: str,
        WithDecryption: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_parameters(
        self, Names: List[Any], WithDecryption: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_parameters_by_path(
        self,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List[Any] = None,
        WithDecryption: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_patch_baseline(self, BaselineId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_patch_baseline_for_patch_group(
        self, PatchGroup: str, OperatingSystem: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_service_setting(self, SettingId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def label_parameter_version(
        self, Name: str, Labels: List[Any], ParameterVersion: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_association_versions(
        self, AssociationId: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_associations(
        self,
        AssociationFilterList: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_command_invocations(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[Any] = None,
        Details: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_commands(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_compliance_items(
        self,
        Filters: List[Any] = None,
        ResourceIds: List[Any] = None,
        ResourceTypes: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_compliance_summaries(
        self, Filters: List[Any] = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_document_versions(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_documents(
        self,
        DocumentFilterList: List[Any] = None,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_inventory_entries(
        self,
        InstanceId: str,
        TypeName: str,
        Filters: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resource_compliance_summaries(
        self, Filters: List[Any] = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resource_data_sync(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, ResourceType: str, ResourceId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def modify_document_permission(
        self,
        Name: str,
        PermissionType: str,
        AccountIdsToAdd: List[Any] = None,
        AccountIdsToRemove: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_compliance_items(
        self,
        ResourceId: str,
        ResourceType: str,
        ComplianceType: str,
        ExecutionSummary: Dict[str, Any],
        Items: List[Any],
        ItemContentHash: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_inventory(self, InstanceId: str, Items: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_parameter(
        self,
        Name: str,
        Value: str,
        Type: str,
        Description: str = None,
        KeyId: str = None,
        Overwrite: bool = None,
        AllowedPattern: str = None,
        Tags: List[Any] = None,
        Tier: str = None,
        Policies: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_default_patch_baseline(self, BaselineId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_patch_baseline_for_patch_group(
        self, BaselineId: str, PatchGroup: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_target_with_maintenance_window(
        self,
        WindowId: str,
        ResourceType: str,
        Targets: List[Any],
        OwnerInformation: str = None,
        Name: str = None,
        Description: str = None,
        ClientToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_task_with_maintenance_window(
        self,
        WindowId: str,
        Targets: List[Any],
        TaskArn: str,
        TaskType: str,
        MaxConcurrency: str,
        MaxErrors: str,
        ServiceRoleArn: str = None,
        TaskParameters: Dict[str, Any] = None,
        TaskInvocationParameters: Dict[str, Any] = None,
        Priority: int = None,
        LoggingInfo: Dict[str, Any] = None,
        Name: str = None,
        Description: str = None,
        ClientToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags_from_resource(
        self, ResourceType: str, ResourceId: str, TagKeys: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reset_service_setting(self, SettingId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def resume_session(self, SessionId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_automation_signal(
        self,
        AutomationExecutionId: str,
        SignalType: str,
        Payload: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def send_command(
        self,
        DocumentName: str,
        InstanceIds: List[Any] = None,
        Targets: List[Any] = None,
        DocumentVersion: str = None,
        DocumentHash: str = None,
        DocumentHashType: str = None,
        TimeoutSeconds: int = None,
        Comment: str = None,
        Parameters: Dict[str, Any] = None,
        OutputS3Region: str = None,
        OutputS3BucketName: str = None,
        OutputS3KeyPrefix: str = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        ServiceRoleArn: str = None,
        NotificationConfig: Dict[str, Any] = None,
        CloudWatchOutputConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_associations_once(self, AssociationIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_automation_execution(
        self,
        DocumentName: str,
        DocumentVersion: str = None,
        Parameters: Dict[str, Any] = None,
        ClientToken: str = None,
        Mode: str = None,
        TargetParameterName: str = None,
        Targets: List[Any] = None,
        TargetMaps: List[Any] = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        TargetLocations: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_session(
        self, Target: str, DocumentName: str = None, Parameters: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_automation_execution(
        self, AutomationExecutionId: str, Type: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def terminate_session(self, SessionId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_association(
        self,
        AssociationId: str,
        Parameters: Dict[str, Any] = None,
        DocumentVersion: str = None,
        ScheduleExpression: str = None,
        OutputLocation: Dict[str, Any] = None,
        Name: str = None,
        Targets: List[Any] = None,
        AssociationName: str = None,
        AssociationVersion: str = None,
        AutomationTargetParameterName: str = None,
        MaxErrors: str = None,
        MaxConcurrency: str = None,
        ComplianceSeverity: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_association_status(
        self, Name: str, InstanceId: str, AssociationStatus: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_document(
        self,
        Content: str,
        Name: str,
        Attachments: List[Any] = None,
        VersionName: str = None,
        DocumentVersion: str = None,
        DocumentFormat: str = None,
        TargetType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_document_default_version(
        self, Name: str, DocumentVersion: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_maintenance_window(
        self,
        WindowId: str,
        Name: str = None,
        Description: str = None,
        StartDate: str = None,
        EndDate: str = None,
        Schedule: str = None,
        ScheduleTimezone: str = None,
        Duration: int = None,
        Cutoff: int = None,
        AllowUnassociatedTargets: bool = None,
        Enabled: bool = None,
        Replace: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_maintenance_window_target(
        self,
        WindowId: str,
        WindowTargetId: str,
        Targets: List[Any] = None,
        OwnerInformation: str = None,
        Name: str = None,
        Description: str = None,
        Replace: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_maintenance_window_task(
        self,
        WindowId: str,
        WindowTaskId: str,
        Targets: List[Any] = None,
        TaskArn: str = None,
        ServiceRoleArn: str = None,
        TaskParameters: Dict[str, Any] = None,
        TaskInvocationParameters: Dict[str, Any] = None,
        Priority: int = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        LoggingInfo: Dict[str, Any] = None,
        Name: str = None,
        Description: str = None,
        Replace: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_managed_instance_role(
        self, InstanceId: str, IamRole: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_ops_item(
        self,
        OpsItemId: str,
        Description: str = None,
        OperationalData: Dict[str, Any] = None,
        OperationalDataToDelete: List[Any] = None,
        Notifications: List[Any] = None,
        Priority: int = None,
        RelatedOpsItems: List[Any] = None,
        Status: str = None,
        Title: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_patch_baseline(
        self,
        BaselineId: str,
        Name: str = None,
        GlobalFilters: Dict[str, Any] = None,
        ApprovalRules: Dict[str, Any] = None,
        ApprovedPatches: List[Any] = None,
        ApprovedPatchesComplianceLevel: str = None,
        ApprovedPatchesEnableNonSecurity: bool = None,
        RejectedPatches: List[Any] = None,
        RejectedPatchesAction: str = None,
        Description: str = None,
        Sources: List[Any] = None,
        Replace: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_service_setting(
        self, SettingId: str, SettingValue: str
    ) -> Dict[str, Any]:
        pass
