# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ssm.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ssm](index.md#ssm) / Client
    - [Client](#client)
        - [Client().add_tags_to_resource](#clientadd_tags_to_resource)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_command](#clientcancel_command)
        - [Client().cancel_maintenance_window_execution](#clientcancel_maintenance_window_execution)
        - [Client().create_activation](#clientcreate_activation)
        - [Client().create_association](#clientcreate_association)
        - [Client().create_association_batch](#clientcreate_association_batch)
        - [Client().create_document](#clientcreate_document)
        - [Client().create_maintenance_window](#clientcreate_maintenance_window)
        - [Client().create_ops_item](#clientcreate_ops_item)
        - [Client().create_patch_baseline](#clientcreate_patch_baseline)
        - [Client().create_resource_data_sync](#clientcreate_resource_data_sync)
        - [Client().delete_activation](#clientdelete_activation)
        - [Client().delete_association](#clientdelete_association)
        - [Client().delete_document](#clientdelete_document)
        - [Client().delete_inventory](#clientdelete_inventory)
        - [Client().delete_maintenance_window](#clientdelete_maintenance_window)
        - [Client().delete_parameter](#clientdelete_parameter)
        - [Client().delete_parameters](#clientdelete_parameters)
        - [Client().delete_patch_baseline](#clientdelete_patch_baseline)
        - [Client().delete_resource_data_sync](#clientdelete_resource_data_sync)
        - [Client().deregister_managed_instance](#clientderegister_managed_instance)
        - [Client().deregister_patch_baseline_for_patch_group](#clientderegister_patch_baseline_for_patch_group)
        - [Client().deregister_target_from_maintenance_window](#clientderegister_target_from_maintenance_window)
        - [Client().deregister_task_from_maintenance_window](#clientderegister_task_from_maintenance_window)
        - [Client().describe_activations](#clientdescribe_activations)
        - [Client().describe_association](#clientdescribe_association)
        - [Client().describe_association_execution_targets](#clientdescribe_association_execution_targets)
        - [Client().describe_association_executions](#clientdescribe_association_executions)
        - [Client().describe_automation_executions](#clientdescribe_automation_executions)
        - [Client().describe_automation_step_executions](#clientdescribe_automation_step_executions)
        - [Client().describe_available_patches](#clientdescribe_available_patches)
        - [Client().describe_document](#clientdescribe_document)
        - [Client().describe_document_permission](#clientdescribe_document_permission)
        - [Client().describe_effective_instance_associations](#clientdescribe_effective_instance_associations)
        - [Client().describe_effective_patches_for_patch_baseline](#clientdescribe_effective_patches_for_patch_baseline)
        - [Client().describe_instance_associations_status](#clientdescribe_instance_associations_status)
        - [Client().describe_instance_information](#clientdescribe_instance_information)
        - [Client().describe_instance_patch_states](#clientdescribe_instance_patch_states)
        - [Client().describe_instance_patch_states_for_patch_group](#clientdescribe_instance_patch_states_for_patch_group)
        - [Client().describe_instance_patches](#clientdescribe_instance_patches)
        - [Client().describe_inventory_deletions](#clientdescribe_inventory_deletions)
        - [Client().describe_maintenance_window_execution_task_invocations](#clientdescribe_maintenance_window_execution_task_invocations)
        - [Client().describe_maintenance_window_execution_tasks](#clientdescribe_maintenance_window_execution_tasks)
        - [Client().describe_maintenance_window_executions](#clientdescribe_maintenance_window_executions)
        - [Client().describe_maintenance_window_schedule](#clientdescribe_maintenance_window_schedule)
        - [Client().describe_maintenance_window_targets](#clientdescribe_maintenance_window_targets)
        - [Client().describe_maintenance_window_tasks](#clientdescribe_maintenance_window_tasks)
        - [Client().describe_maintenance_windows](#clientdescribe_maintenance_windows)
        - [Client().describe_maintenance_windows_for_target](#clientdescribe_maintenance_windows_for_target)
        - [Client().describe_ops_items](#clientdescribe_ops_items)
        - [Client().describe_parameters](#clientdescribe_parameters)
        - [Client().describe_patch_baselines](#clientdescribe_patch_baselines)
        - [Client().describe_patch_group_state](#clientdescribe_patch_group_state)
        - [Client().describe_patch_groups](#clientdescribe_patch_groups)
        - [Client().describe_patch_properties](#clientdescribe_patch_properties)
        - [Client().describe_sessions](#clientdescribe_sessions)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_automation_execution](#clientget_automation_execution)
        - [Client().get_command_invocation](#clientget_command_invocation)
        - [Client().get_connection_status](#clientget_connection_status)
        - [Client().get_default_patch_baseline](#clientget_default_patch_baseline)
        - [Client().get_deployable_patch_snapshot_for_instance](#clientget_deployable_patch_snapshot_for_instance)
        - [Client().get_document](#clientget_document)
        - [Client().get_inventory](#clientget_inventory)
        - [Client().get_inventory_schema](#clientget_inventory_schema)
        - [Client().get_maintenance_window](#clientget_maintenance_window)
        - [Client().get_maintenance_window_execution](#clientget_maintenance_window_execution)
        - [Client().get_maintenance_window_execution_task](#clientget_maintenance_window_execution_task)
        - [Client().get_maintenance_window_execution_task_invocation](#clientget_maintenance_window_execution_task_invocation)
        - [Client().get_maintenance_window_task](#clientget_maintenance_window_task)
        - [Client().get_ops_item](#clientget_ops_item)
        - [Client().get_ops_summary](#clientget_ops_summary)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_parameter](#clientget_parameter)
        - [Client().get_parameter_history](#clientget_parameter_history)
        - [Client().get_parameters](#clientget_parameters)
        - [Client().get_parameters_by_path](#clientget_parameters_by_path)
        - [Client().get_patch_baseline](#clientget_patch_baseline)
        - [Client().get_patch_baseline_for_patch_group](#clientget_patch_baseline_for_patch_group)
        - [Client().get_service_setting](#clientget_service_setting)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().label_parameter_version](#clientlabel_parameter_version)
        - [Client().list_association_versions](#clientlist_association_versions)
        - [Client().list_associations](#clientlist_associations)
        - [Client().list_command_invocations](#clientlist_command_invocations)
        - [Client().list_commands](#clientlist_commands)
        - [Client().list_compliance_items](#clientlist_compliance_items)
        - [Client().list_compliance_summaries](#clientlist_compliance_summaries)
        - [Client().list_document_versions](#clientlist_document_versions)
        - [Client().list_documents](#clientlist_documents)
        - [Client().list_inventory_entries](#clientlist_inventory_entries)
        - [Client().list_resource_compliance_summaries](#clientlist_resource_compliance_summaries)
        - [Client().list_resource_data_sync](#clientlist_resource_data_sync)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().modify_document_permission](#clientmodify_document_permission)
        - [Client().put_compliance_items](#clientput_compliance_items)
        - [Client().put_inventory](#clientput_inventory)
        - [Client().put_parameter](#clientput_parameter)
        - [Client().register_default_patch_baseline](#clientregister_default_patch_baseline)
        - [Client().register_patch_baseline_for_patch_group](#clientregister_patch_baseline_for_patch_group)
        - [Client().register_target_with_maintenance_window](#clientregister_target_with_maintenance_window)
        - [Client().register_task_with_maintenance_window](#clientregister_task_with_maintenance_window)
        - [Client().remove_tags_from_resource](#clientremove_tags_from_resource)
        - [Client().reset_service_setting](#clientreset_service_setting)
        - [Client().resume_session](#clientresume_session)
        - [Client().send_automation_signal](#clientsend_automation_signal)
        - [Client().send_command](#clientsend_command)
        - [Client().start_associations_once](#clientstart_associations_once)
        - [Client().start_automation_execution](#clientstart_automation_execution)
        - [Client().start_session](#clientstart_session)
        - [Client().stop_automation_execution](#clientstop_automation_execution)
        - [Client().terminate_session](#clientterminate_session)
        - [Client().update_association](#clientupdate_association)
        - [Client().update_association_status](#clientupdate_association_status)
        - [Client().update_document](#clientupdate_document)
        - [Client().update_document_default_version](#clientupdate_document_default_version)
        - [Client().update_maintenance_window](#clientupdate_maintenance_window)
        - [Client().update_maintenance_window_target](#clientupdate_maintenance_window_target)
        - [Client().update_maintenance_window_task](#clientupdate_maintenance_window_task)
        - [Client().update_managed_instance_role](#clientupdate_managed_instance_role)
        - [Client().update_ops_item](#clientupdate_ops_item)
        - [Client().update_patch_baseline](#clientupdate_patch_baseline)
        - [Client().update_service_setting](#clientupdate_service_setting)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_tags_to_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L16)

```python
def add_tags_to_resource(
    ResourceType: str,
    ResourceId: str,
    Tags: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L22)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_command

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L26)

```python
def cancel_command(
    CommandId: str,
    InstanceIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().cancel_maintenance_window_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L32)

```python
def cancel_maintenance_window_execution(
    WindowExecutionId: str,
) -> Dict[str, Any]:
```

### Client().create_activation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L38)

```python
def create_activation(
    IamRole: str,
    Description: str = None,
    DefaultInstanceName: str = None,
    RegistrationLimit: int = None,
    ExpirationDate: datetime = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L50)

```python
def create_association(
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
```

### Client().create_association_batch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L68)

```python
def create_association_batch(Entries: List[Any]) -> Dict[str, Any]:
```

### Client().create_document

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L72)

```python
def create_document(
    Content: str,
    Name: str,
    Attachments: List[Any] = None,
    VersionName: str = None,
    DocumentType: str = None,
    DocumentFormat: str = None,
    TargetType: str = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_maintenance_window

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L86)

```python
def create_maintenance_window(
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
```

### Client().create_ops_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L103)

```python
def create_ops_item(
    Description: str,
    Source: str,
    Title: str,
    OperationalData: Dict[str, Any] = None,
    Notifications: List[Any] = None,
    Priority: int = None,
    RelatedOpsItems: List[Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_patch_baseline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L117)

```python
def create_patch_baseline(
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
```

### Client().create_resource_data_sync

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L136)

```python
def create_resource_data_sync(
    SyncName: str,
    S3Destination: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_activation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L142)

```python
def delete_activation(ActivationId: str) -> Dict[str, Any]:
```

### Client().delete_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L146)

```python
def delete_association(
    Name: str = None,
    InstanceId: str = None,
    AssociationId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_document

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L152)

```python
def delete_document(
    Name: str,
    DocumentVersion: str = None,
    VersionName: str = None,
) -> Dict[str, Any]:
```

### Client().delete_inventory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L158)

```python
def delete_inventory(
    TypeName: str,
    SchemaDeleteOption: str = None,
    DryRun: bool = None,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().delete_maintenance_window

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L168)

```python
def delete_maintenance_window(WindowId: str) -> Dict[str, Any]:
```

### Client().delete_parameter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L172)

```python
def delete_parameter(Name: str) -> Dict[str, Any]:
```

### Client().delete_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L176)

```python
def delete_parameters(Names: List[Any]) -> Dict[str, Any]:
```

### Client().delete_patch_baseline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L180)

```python
def delete_patch_baseline(BaselineId: str) -> Dict[str, Any]:
```

### Client().delete_resource_data_sync

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L184)

```python
def delete_resource_data_sync(SyncName: str) -> Dict[str, Any]:
```

### Client().deregister_managed_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L188)

```python
def deregister_managed_instance(InstanceId: str) -> Dict[str, Any]:
```

### Client().deregister_patch_baseline_for_patch_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L192)

```python
def deregister_patch_baseline_for_patch_group(
    BaselineId: str,
    PatchGroup: str,
) -> Dict[str, Any]:
```

### Client().deregister_target_from_maintenance_window

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L198)

```python
def deregister_target_from_maintenance_window(
    WindowId: str,
    WindowTargetId: str,
    Safe: bool = None,
) -> Dict[str, Any]:
```

### Client().deregister_task_from_maintenance_window

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L204)

```python
def deregister_task_from_maintenance_window(
    WindowId: str,
    WindowTaskId: str,
) -> Dict[str, Any]:
```

### Client().describe_activations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L210)

```python
def describe_activations(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L216)

```python
def describe_association(
    Name: str = None,
    InstanceId: str = None,
    AssociationId: str = None,
    AssociationVersion: str = None,
) -> Dict[str, Any]:
```

### Client().describe_association_execution_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L226)

```python
def describe_association_execution_targets(
    AssociationId: str,
    ExecutionId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_association_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L237)

```python
def describe_association_executions(
    AssociationId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_automation_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L247)

```python
def describe_automation_executions(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_automation_step_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L253)

```python
def describe_automation_step_executions(
    AutomationExecutionId: str,
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
    ReverseOrder: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_available_patches

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L264)

```python
def describe_available_patches(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_document

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L270)

```python
def describe_document(
    Name: str,
    DocumentVersion: str = None,
    VersionName: str = None,
) -> Dict[str, Any]:
```

### Client().describe_document_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L276)

```python
def describe_document_permission(
    Name: str,
    PermissionType: str,
) -> Dict[str, Any]:
```

### Client().describe_effective_instance_associations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L282)

```python
def describe_effective_instance_associations(
    InstanceId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_effective_patches_for_patch_baseline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L288)

```python
def describe_effective_patches_for_patch_baseline(
    BaselineId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_instance_associations_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L294)

```python
def describe_instance_associations_status(
    InstanceId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_instance_information

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L300)

```python
def describe_instance_information(
    InstanceInformationFilterList: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_instance_patch_states

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L310)

```python
def describe_instance_patch_states(
    InstanceIds: List[Any],
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_instance_patch_states_for_patch_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L316)

```python
def describe_instance_patch_states_for_patch_group(
    PatchGroup: str,
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_instance_patches

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L326)

```python
def describe_instance_patches(
    InstanceId: str,
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_inventory_deletions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L336)

```python
def describe_inventory_deletions(
    DeletionId: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_maintenance_window_execution_task_invocations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L342)

```python
def describe_maintenance_window_execution_task_invocations(
    WindowExecutionId: str,
    TaskId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_maintenance_window_execution_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L353)

```python
def describe_maintenance_window_execution_tasks(
    WindowExecutionId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_maintenance_window_executions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L363)

```python
def describe_maintenance_window_executions(
    WindowId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_maintenance_window_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L373)

```python
def describe_maintenance_window_schedule(
    WindowId: str = None,
    Targets: List[Any] = None,
    ResourceType: str = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_maintenance_window_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L385)

```python
def describe_maintenance_window_targets(
    WindowId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_maintenance_window_tasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L395)

```python
def describe_maintenance_window_tasks(
    WindowId: str,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_maintenance_windows

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L405)

```python
def describe_maintenance_windows(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_maintenance_windows_for_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L411)

```python
def describe_maintenance_windows_for_target(
    Targets: List[Any],
    ResourceType: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_ops_items

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L421)

```python
def describe_ops_items(
    OpsItemFilters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L430)

```python
def describe_parameters(
    Filters: List[Any] = None,
    ParameterFilters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_patch_baselines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L440)

```python
def describe_patch_baselines(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_patch_group_state

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L446)

```python
def describe_patch_group_state(PatchGroup: str) -> Dict[str, Any]:
```

### Client().describe_patch_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L450)

```python
def describe_patch_groups(
    MaxResults: int = None,
    Filters: List[Any] = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_patch_properties

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L456)

```python
def describe_patch_properties(
    OperatingSystem: str,
    Property: str,
    PatchSet: str = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_sessions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L467)

```python
def describe_sessions(
    State: str,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L477)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_automation_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L487)

```python
def get_automation_execution(AutomationExecutionId: str) -> Dict[str, Any]:
```

### Client().get_command_invocation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L491)

```python
def get_command_invocation(
    CommandId: str,
    InstanceId: str,
    PluginName: str = None,
) -> Dict[str, Any]:
```

### Client().get_connection_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L497)

```python
def get_connection_status(Target: str) -> Dict[str, Any]:
```

### Client().get_default_patch_baseline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L501)

```python
def get_default_patch_baseline(OperatingSystem: str = None) -> Dict[str, Any]:
```

### Client().get_deployable_patch_snapshot_for_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L505)

```python
def get_deployable_patch_snapshot_for_instance(
    InstanceId: str,
    SnapshotId: str,
) -> Dict[str, Any]:
```

### Client().get_document

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L511)

```python
def get_document(
    Name: str,
    VersionName: str = None,
    DocumentVersion: str = None,
    DocumentFormat: str = None,
) -> Dict[str, Any]:
```

### Client().get_inventory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L521)

```python
def get_inventory(
    Filters: List[Any] = None,
    Aggregators: List[Any] = None,
    ResultAttributes: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_inventory_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L532)

```python
def get_inventory_schema(
    TypeName: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    Aggregator: bool = None,
    SubType: bool = None,
) -> Dict[str, Any]:
```

### Client().get_maintenance_window

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L543)

```python
def get_maintenance_window(WindowId: str) -> Dict[str, Any]:
```

### Client().get_maintenance_window_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L547)

```python
def get_maintenance_window_execution(
    WindowExecutionId: str,
) -> Dict[str, Any]:
```

### Client().get_maintenance_window_execution_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L553)

```python
def get_maintenance_window_execution_task(
    WindowExecutionId: str,
    TaskId: str,
) -> Dict[str, Any]:
```

### Client().get_maintenance_window_execution_task_invocation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L559)

```python
def get_maintenance_window_execution_task_invocation(
    WindowExecutionId: str,
    TaskId: str,
    InvocationId: str,
) -> Dict[str, Any]:
```

### Client().get_maintenance_window_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L565)

```python
def get_maintenance_window_task(
    WindowId: str,
    WindowTaskId: str,
) -> Dict[str, Any]:
```

### Client().get_ops_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L571)

```python
def get_ops_item(OpsItemId: str) -> Dict[str, Any]:
```

### Client().get_ops_summary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L575)

```python
def get_ops_summary(
    Aggregators: List[Any],
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L585)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_parameter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L589)

```python
def get_parameter(Name: str, WithDecryption: bool = None) -> Dict[str, Any]:
```

### Client().get_parameter_history

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L593)

```python
def get_parameter_history(
    Name: str,
    WithDecryption: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L603)

```python
def get_parameters(
    Names: List[Any],
    WithDecryption: bool = None,
) -> Dict[str, Any]:
```

### Client().get_parameters_by_path

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L609)

```python
def get_parameters_by_path(
    Path: str,
    Recursive: bool = None,
    ParameterFilters: List[Any] = None,
    WithDecryption: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_patch_baseline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L621)

```python
def get_patch_baseline(BaselineId: str) -> Dict[str, Any]:
```

### Client().get_patch_baseline_for_patch_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L625)

```python
def get_patch_baseline_for_patch_group(
    PatchGroup: str,
    OperatingSystem: str = None,
) -> Dict[str, Any]:
```

### Client().get_service_setting

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L631)

```python
def get_service_setting(SettingId: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L635)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().label_parameter_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L639)

```python
def label_parameter_version(
    Name: str,
    Labels: List[Any],
    ParameterVersion: int = None,
) -> Dict[str, Any]:
```

### Client().list_association_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L645)

```python
def list_association_versions(
    AssociationId: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_associations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L651)

```python
def list_associations(
    AssociationFilterList: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_command_invocations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L660)

```python
def list_command_invocations(
    CommandId: str = None,
    InstanceId: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
    Details: bool = None,
) -> Dict[str, Any]:
```

### Client().list_commands

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L672)

```python
def list_commands(
    CommandId: str = None,
    InstanceId: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_compliance_items

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L683)

```python
def list_compliance_items(
    Filters: List[Any] = None,
    ResourceIds: List[Any] = None,
    ResourceTypes: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_compliance_summaries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L694)

```python
def list_compliance_summaries(
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_document_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L700)

```python
def list_document_versions(
    Name: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_documents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L706)

```python
def list_documents(
    DocumentFilterList: List[Any] = None,
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_inventory_entries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L716)

```python
def list_inventory_entries(
    InstanceId: str,
    TypeName: str,
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_resource_compliance_summaries

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L727)

```python
def list_resource_compliance_summaries(
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_resource_data_sync

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L733)

```python
def list_resource_data_sync(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L739)

```python
def list_tags_for_resource(
    ResourceType: str,
    ResourceId: str,
) -> Dict[str, Any]:
```

### Client().modify_document_permission

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L745)

```python
def modify_document_permission(
    Name: str,
    PermissionType: str,
    AccountIdsToAdd: List[Any] = None,
    AccountIdsToRemove: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().put_compliance_items

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L755)

```python
def put_compliance_items(
    ResourceId: str,
    ResourceType: str,
    ComplianceType: str,
    ExecutionSummary: Dict[str, Any],
    Items: List[Any],
    ItemContentHash: str = None,
) -> Dict[str, Any]:
```

### Client().put_inventory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L767)

```python
def put_inventory(InstanceId: str, Items: List[Any]) -> Dict[str, Any]:
```

### Client().put_parameter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L771)

```python
def put_parameter(
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
```

### Client().register_default_patch_baseline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L787)

```python
def register_default_patch_baseline(BaselineId: str) -> Dict[str, Any]:
```

### Client().register_patch_baseline_for_patch_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L791)

```python
def register_patch_baseline_for_patch_group(
    BaselineId: str,
    PatchGroup: str,
) -> Dict[str, Any]:
```

### Client().register_target_with_maintenance_window

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L797)

```python
def register_target_with_maintenance_window(
    WindowId: str,
    ResourceType: str,
    Targets: List[Any],
    OwnerInformation: str = None,
    Name: str = None,
    Description: str = None,
    ClientToken: str = None,
) -> Dict[str, Any]:
```

### Client().register_task_with_maintenance_window

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L810)

```python
def register_task_with_maintenance_window(
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
```

### Client().remove_tags_from_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L830)

```python
def remove_tags_from_resource(
    ResourceType: str,
    ResourceId: str,
    TagKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().reset_service_setting

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L836)

```python
def reset_service_setting(SettingId: str) -> Dict[str, Any]:
```

### Client().resume_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L840)

```python
def resume_session(SessionId: str) -> Dict[str, Any]:
```

### Client().send_automation_signal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L844)

```python
def send_automation_signal(
    AutomationExecutionId: str,
    SignalType: str,
    Payload: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().send_command

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L853)

```python
def send_command(
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
```

### Client().start_associations_once

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L876)

```python
def start_associations_once(AssociationIds: List[Any]) -> Dict[str, Any]:
```

### Client().start_automation_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L880)

```python
def start_automation_execution(
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
```

### Client().start_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L897)

```python
def start_session(
    Target: str,
    DocumentName: str = None,
    Parameters: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().stop_automation_execution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L903)

```python
def stop_automation_execution(
    AutomationExecutionId: str,
    Type: str = None,
) -> Dict[str, Any]:
```

### Client().terminate_session

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L909)

```python
def terminate_session(SessionId: str) -> Dict[str, Any]:
```

### Client().update_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L913)

```python
def update_association(
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
```

### Client().update_association_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L932)

```python
def update_association_status(
    Name: str,
    InstanceId: str,
    AssociationStatus: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_document

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L938)

```python
def update_document(
    Content: str,
    Name: str,
    Attachments: List[Any] = None,
    VersionName: str = None,
    DocumentVersion: str = None,
    DocumentFormat: str = None,
    TargetType: str = None,
) -> Dict[str, Any]:
```

### Client().update_document_default_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L951)

```python
def update_document_default_version(
    Name: str,
    DocumentVersion: str,
) -> Dict[str, Any]:
```

### Client().update_maintenance_window

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L957)

```python
def update_maintenance_window(
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
```

### Client().update_maintenance_window_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L975)

```python
def update_maintenance_window_target(
    WindowId: str,
    WindowTargetId: str,
    Targets: List[Any] = None,
    OwnerInformation: str = None,
    Name: str = None,
    Description: str = None,
    Replace: bool = None,
) -> Dict[str, Any]:
```

### Client().update_maintenance_window_task

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L988)

```python
def update_maintenance_window_task(
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
```

### Client().update_managed_instance_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L1008)

```python
def update_managed_instance_role(
    InstanceId: str,
    IamRole: str,
) -> Dict[str, Any]:
```

### Client().update_ops_item

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L1014)

```python
def update_ops_item(
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
```

### Client().update_patch_baseline

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L1029)

```python
def update_patch_baseline(
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
```

### Client().update_service_setting

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ssm/client.py#L1047)

```python
def update_service_setting(
    SettingId: str,
    SettingValue: str,
) -> Dict[str, Any]:
```
