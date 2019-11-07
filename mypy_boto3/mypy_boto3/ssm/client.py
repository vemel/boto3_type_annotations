from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags_to_resource(
        self,
        ResourceType: str,
        ResourceId: str,
        Tags: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_command(
        self,
        CommandId: str,
        InstanceIds: Optional[List] = None,
    ) -> Dict:
        pass


    def cancel_maintenance_window_execution(
        self,
        WindowExecutionId: str,
    ) -> Dict:
        pass


    def create_activation(
        self,
        IamRole: str,
        Description: Optional[str] = None,
        DefaultInstanceName: Optional[str] = None,
        RegistrationLimit: Optional[int] = None,
        ExpirationDate: Optional[datetime] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_association(
        self,
        Name: str,
        DocumentVersion: Optional[str] = None,
        InstanceId: Optional[str] = None,
        Parameters: Optional[Dict] = None,
        Targets: Optional[List] = None,
        ScheduleExpression: Optional[str] = None,
        OutputLocation: Optional[Dict] = None,
        AssociationName: Optional[str] = None,
        AutomationTargetParameterName: Optional[str] = None,
        MaxErrors: Optional[str] = None,
        MaxConcurrency: Optional[str] = None,
        ComplianceSeverity: Optional[str] = None,
    ) -> Dict:
        pass


    def create_association_batch(
        self,
        Entries: List,
    ) -> Dict:
        pass


    def create_document(
        self,
        Content: str,
        Name: str,
        Attachments: Optional[List] = None,
        VersionName: Optional[str] = None,
        DocumentType: Optional[str] = None,
        DocumentFormat: Optional[str] = None,
        TargetType: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_maintenance_window(
        self,
        Name: str,
        Schedule: str,
        Duration: int,
        Cutoff: int,
        AllowUnassociatedTargets: bool,
        Description: Optional[str] = None,
        StartDate: Optional[str] = None,
        EndDate: Optional[str] = None,
        ScheduleTimezone: Optional[str] = None,
        ClientToken: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_ops_item(
        self,
        Description: str,
        Source: str,
        Title: str,
        OperationalData: Optional[Dict] = None,
        Notifications: Optional[List] = None,
        Priority: Optional[int] = None,
        RelatedOpsItems: Optional[List] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_patch_baseline(
        self,
        Name: str,
        OperatingSystem: Optional[str] = None,
        GlobalFilters: Optional[Dict] = None,
        ApprovalRules: Optional[Dict] = None,
        ApprovedPatches: Optional[List] = None,
        ApprovedPatchesComplianceLevel: Optional[str] = None,
        ApprovedPatchesEnableNonSecurity: Optional[bool] = None,
        RejectedPatches: Optional[List] = None,
        RejectedPatchesAction: Optional[str] = None,
        Description: Optional[str] = None,
        Sources: Optional[List] = None,
        ClientToken: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_resource_data_sync(
        self,
        SyncName: str,
        S3Destination: Dict,
    ) -> Dict:
        pass


    def delete_activation(
        self,
        ActivationId: str,
    ) -> Dict:
        pass


    def delete_association(
        self,
        Name: Optional[str] = None,
        InstanceId: Optional[str] = None,
        AssociationId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_document(
        self,
        Name: str,
        DocumentVersion: Optional[str] = None,
        VersionName: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_inventory(
        self,
        TypeName: str,
        SchemaDeleteOption: Optional[str] = None,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_maintenance_window(
        self,
        WindowId: str,
    ) -> Dict:
        pass


    def delete_parameter(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_parameters(
        self,
        Names: List,
    ) -> Dict:
        pass


    def delete_patch_baseline(
        self,
        BaselineId: str,
    ) -> Dict:
        pass


    def delete_resource_data_sync(
        self,
        SyncName: str,
    ) -> Dict:
        pass


    def deregister_managed_instance(
        self,
        InstanceId: str,
    ) -> Dict:
        pass


    def deregister_patch_baseline_for_patch_group(
        self,
        BaselineId: str,
        PatchGroup: str,
    ) -> Dict:
        pass


    def deregister_target_from_maintenance_window(
        self,
        WindowId: str,
        WindowTargetId: str,
        Safe: Optional[bool] = None,
    ) -> Dict:
        pass


    def deregister_task_from_maintenance_window(
        self,
        WindowId: str,
        WindowTaskId: str,
    ) -> Dict:
        pass


    def describe_activations(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_association(
        self,
        Name: Optional[str] = None,
        InstanceId: Optional[str] = None,
        AssociationId: Optional[str] = None,
        AssociationVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_association_execution_targets(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_association_executions(
        self,
        AssociationId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_automation_executions(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_automation_step_executions(
        self,
        AutomationExecutionId: str,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        ReverseOrder: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_available_patches(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_document(
        self,
        Name: str,
        DocumentVersion: Optional[str] = None,
        VersionName: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_document_permission(
        self,
        Name: str,
        PermissionType: str,
    ) -> Dict:
        pass


    def describe_effective_instance_associations(
        self,
        InstanceId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_effective_patches_for_patch_baseline(
        self,
        BaselineId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_instance_associations_status(
        self,
        InstanceId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_instance_information(
        self,
        InstanceInformationFilterList: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_instance_patch_states(
        self,
        InstanceIds: List,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_instance_patch_states_for_patch_group(
        self,
        PatchGroup: str,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_instance_patches(
        self,
        InstanceId: str,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_inventory_deletions(
        self,
        DeletionId: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_maintenance_window_execution_task_invocations(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_maintenance_window_execution_tasks(
        self,
        WindowExecutionId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_maintenance_window_executions(
        self,
        WindowId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_maintenance_window_schedule(
        self,
        WindowId: Optional[str] = None,
        Targets: Optional[List] = None,
        ResourceType: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_maintenance_window_targets(
        self,
        WindowId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_maintenance_window_tasks(
        self,
        WindowId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_maintenance_windows(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_maintenance_windows_for_target(
        self,
        Targets: List,
        ResourceType: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_ops_items(
        self,
        OpsItemFilters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_parameters(
        self,
        Filters: Optional[List] = None,
        ParameterFilters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_patch_baselines(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_patch_group_state(
        self,
        PatchGroup: str,
    ) -> Dict:
        pass


    def describe_patch_groups(
        self,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_patch_properties(
        self,
        OperatingSystem: str,
        Property: str,
        PatchSet: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_sessions(
        self,
        State: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
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


    def get_automation_execution(
        self,
        AutomationExecutionId: str,
    ) -> Dict:
        pass


    def get_command_invocation(
        self,
        CommandId: str,
        InstanceId: str,
        PluginName: Optional[str] = None,
    ) -> Dict:
        pass


    def get_connection_status(
        self,
        Target: str,
    ) -> Dict:
        pass


    def get_default_patch_baseline(
        self,
        OperatingSystem: Optional[str] = None,
    ) -> Dict:
        pass


    def get_deployable_patch_snapshot_for_instance(
        self,
        InstanceId: str,
        SnapshotId: str,
    ) -> Dict:
        pass


    def get_document(
        self,
        Name: str,
        VersionName: Optional[str] = None,
        DocumentVersion: Optional[str] = None,
        DocumentFormat: Optional[str] = None,
    ) -> Dict:
        pass


    def get_inventory(
        self,
        Filters: Optional[List] = None,
        Aggregators: Optional[List] = None,
        ResultAttributes: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_inventory_schema(
        self,
        TypeName: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Aggregator: Optional[bool] = None,
        SubType: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_maintenance_window(
        self,
        WindowId: str,
    ) -> Dict:
        pass


    def get_maintenance_window_execution(
        self,
        WindowExecutionId: str,
    ) -> Dict:
        pass


    def get_maintenance_window_execution_task(
        self,
        WindowExecutionId: str,
        TaskId: str,
    ) -> Dict:
        pass


    def get_maintenance_window_execution_task_invocation(
        self,
        WindowExecutionId: str,
        TaskId: str,
        InvocationId: str,
    ) -> Dict:
        pass


    def get_maintenance_window_task(
        self,
        WindowId: str,
        WindowTaskId: str,
    ) -> Dict:
        pass


    def get_ops_item(
        self,
        OpsItemId: str,
    ) -> Dict:
        pass


    def get_ops_summary(
        self,
        Aggregators: List,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_parameter(
        self,
        Name: str,
        WithDecryption: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_parameter_history(
        self,
        Name: str,
        WithDecryption: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_parameters(
        self,
        Names: List,
        WithDecryption: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_parameters_by_path(
        self,
        Path: str,
        Recursive: Optional[bool] = None,
        ParameterFilters: Optional[List] = None,
        WithDecryption: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_patch_baseline(
        self,
        BaselineId: str,
    ) -> Dict:
        pass


    def get_patch_baseline_for_patch_group(
        self,
        PatchGroup: str,
        OperatingSystem: Optional[str] = None,
    ) -> Dict:
        pass


    def get_service_setting(
        self,
        SettingId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def label_parameter_version(
        self,
        Name: str,
        Labels: List,
        ParameterVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def list_association_versions(
        self,
        AssociationId: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_associations(
        self,
        AssociationFilterList: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_command_invocations(
        self,
        CommandId: Optional[str] = None,
        InstanceId: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
        Details: Optional[bool] = None,
    ) -> Dict:
        pass


    def list_commands(
        self,
        CommandId: Optional[str] = None,
        InstanceId: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_compliance_items(
        self,
        Filters: Optional[List] = None,
        ResourceIds: Optional[List] = None,
        ResourceTypes: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_compliance_summaries(
        self,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_document_versions(
        self,
        Name: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_documents(
        self,
        DocumentFilterList: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_inventory_entries(
        self,
        InstanceId: str,
        TypeName: str,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_resource_compliance_summaries(
        self,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_resource_data_sync(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceType: str,
        ResourceId: str,
    ) -> Dict:
        pass


    def modify_document_permission(
        self,
        Name: str,
        PermissionType: str,
        AccountIdsToAdd: Optional[List] = None,
        AccountIdsToRemove: Optional[List] = None,
    ) -> Dict:
        pass


    def put_compliance_items(
        self,
        ResourceId: str,
        ResourceType: str,
        ComplianceType: str,
        ExecutionSummary: Dict,
        Items: List,
        ItemContentHash: Optional[str] = None,
    ) -> Dict:
        pass


    def put_inventory(
        self,
        InstanceId: str,
        Items: List,
    ) -> Dict:
        pass


    def put_parameter(
        self,
        Name: str,
        Value: str,
        Type: str,
        Description: Optional[str] = None,
        KeyId: Optional[str] = None,
        Overwrite: Optional[bool] = None,
        AllowedPattern: Optional[str] = None,
        Tags: Optional[List] = None,
        Tier: Optional[str] = None,
        Policies: Optional[str] = None,
    ) -> Dict:
        pass


    def register_default_patch_baseline(
        self,
        BaselineId: str,
    ) -> Dict:
        pass


    def register_patch_baseline_for_patch_group(
        self,
        BaselineId: str,
        PatchGroup: str,
    ) -> Dict:
        pass


    def register_target_with_maintenance_window(
        self,
        WindowId: str,
        ResourceType: str,
        Targets: List,
        OwnerInformation: Optional[str] = None,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def register_task_with_maintenance_window(
        self,
        WindowId: str,
        Targets: List,
        TaskArn: str,
        TaskType: str,
        MaxConcurrency: str,
        MaxErrors: str,
        ServiceRoleArn: Optional[str] = None,
        TaskParameters: Optional[Dict] = None,
        TaskInvocationParameters: Optional[Dict] = None,
        Priority: Optional[int] = None,
        LoggingInfo: Optional[Dict] = None,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def remove_tags_from_resource(
        self,
        ResourceType: str,
        ResourceId: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def reset_service_setting(
        self,
        SettingId: str,
    ) -> Dict:
        pass


    def resume_session(
        self,
        SessionId: str,
    ) -> Dict:
        pass


    def send_automation_signal(
        self,
        AutomationExecutionId: str,
        SignalType: str,
        Payload: Optional[Dict] = None,
    ) -> Dict:
        pass


    def send_command(
        self,
        DocumentName: str,
        InstanceIds: Optional[List] = None,
        Targets: Optional[List] = None,
        DocumentVersion: Optional[str] = None,
        DocumentHash: Optional[str] = None,
        DocumentHashType: Optional[str] = None,
        TimeoutSeconds: Optional[int] = None,
        Comment: Optional[str] = None,
        Parameters: Optional[Dict] = None,
        OutputS3Region: Optional[str] = None,
        OutputS3BucketName: Optional[str] = None,
        OutputS3KeyPrefix: Optional[str] = None,
        MaxConcurrency: Optional[str] = None,
        MaxErrors: Optional[str] = None,
        ServiceRoleArn: Optional[str] = None,
        NotificationConfig: Optional[Dict] = None,
        CloudWatchOutputConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_associations_once(
        self,
        AssociationIds: List,
    ) -> Dict:
        pass


    def start_automation_execution(
        self,
        DocumentName: str,
        DocumentVersion: Optional[str] = None,
        Parameters: Optional[Dict] = None,
        ClientToken: Optional[str] = None,
        Mode: Optional[str] = None,
        TargetParameterName: Optional[str] = None,
        Targets: Optional[List] = None,
        TargetMaps: Optional[List] = None,
        MaxConcurrency: Optional[str] = None,
        MaxErrors: Optional[str] = None,
        TargetLocations: Optional[List] = None,
    ) -> Dict:
        pass


    def start_session(
        self,
        Target: str,
        DocumentName: Optional[str] = None,
        Parameters: Optional[Dict] = None,
    ) -> Dict:
        pass


    def stop_automation_execution(
        self,
        AutomationExecutionId: str,
        Type: Optional[str] = None,
    ) -> Dict:
        pass


    def terminate_session(
        self,
        SessionId: str,
    ) -> Dict:
        pass


    def update_association(
        self,
        AssociationId: str,
        Parameters: Optional[Dict] = None,
        DocumentVersion: Optional[str] = None,
        ScheduleExpression: Optional[str] = None,
        OutputLocation: Optional[Dict] = None,
        Name: Optional[str] = None,
        Targets: Optional[List] = None,
        AssociationName: Optional[str] = None,
        AssociationVersion: Optional[str] = None,
        AutomationTargetParameterName: Optional[str] = None,
        MaxErrors: Optional[str] = None,
        MaxConcurrency: Optional[str] = None,
        ComplianceSeverity: Optional[str] = None,
    ) -> Dict:
        pass


    def update_association_status(
        self,
        Name: str,
        InstanceId: str,
        AssociationStatus: Dict,
    ) -> Dict:
        pass


    def update_document(
        self,
        Content: str,
        Name: str,
        Attachments: Optional[List] = None,
        VersionName: Optional[str] = None,
        DocumentVersion: Optional[str] = None,
        DocumentFormat: Optional[str] = None,
        TargetType: Optional[str] = None,
    ) -> Dict:
        pass


    def update_document_default_version(
        self,
        Name: str,
        DocumentVersion: str,
    ) -> Dict:
        pass


    def update_maintenance_window(
        self,
        WindowId: str,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        StartDate: Optional[str] = None,
        EndDate: Optional[str] = None,
        Schedule: Optional[str] = None,
        ScheduleTimezone: Optional[str] = None,
        Duration: Optional[int] = None,
        Cutoff: Optional[int] = None,
        AllowUnassociatedTargets: Optional[bool] = None,
        Enabled: Optional[bool] = None,
        Replace: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_maintenance_window_target(
        self,
        WindowId: str,
        WindowTargetId: str,
        Targets: Optional[List] = None,
        OwnerInformation: Optional[str] = None,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        Replace: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_maintenance_window_task(
        self,
        WindowId: str,
        WindowTaskId: str,
        Targets: Optional[List] = None,
        TaskArn: Optional[str] = None,
        ServiceRoleArn: Optional[str] = None,
        TaskParameters: Optional[Dict] = None,
        TaskInvocationParameters: Optional[Dict] = None,
        Priority: Optional[int] = None,
        MaxConcurrency: Optional[str] = None,
        MaxErrors: Optional[str] = None,
        LoggingInfo: Optional[Dict] = None,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        Replace: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_managed_instance_role(
        self,
        InstanceId: str,
        IamRole: str,
    ) -> Dict:
        pass


    def update_ops_item(
        self,
        OpsItemId: str,
        Description: Optional[str] = None,
        OperationalData: Optional[Dict] = None,
        OperationalDataToDelete: Optional[List] = None,
        Notifications: Optional[List] = None,
        Priority: Optional[int] = None,
        RelatedOpsItems: Optional[List] = None,
        Status: Optional[str] = None,
        Title: Optional[str] = None,
    ) -> Dict:
        pass


    def update_patch_baseline(
        self,
        BaselineId: str,
        Name: Optional[str] = None,
        GlobalFilters: Optional[Dict] = None,
        ApprovalRules: Optional[Dict] = None,
        ApprovedPatches: Optional[List] = None,
        ApprovedPatchesComplianceLevel: Optional[str] = None,
        ApprovedPatchesEnableNonSecurity: Optional[bool] = None,
        RejectedPatches: Optional[List] = None,
        RejectedPatchesAction: Optional[str] = None,
        Description: Optional[str] = None,
        Sources: Optional[List] = None,
        Replace: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_service_setting(
        self,
        SettingId: str,
        SettingValue: str,
    ) -> Dict:
        pass

