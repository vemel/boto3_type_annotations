# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudformation.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudformation](index.md#cloudformation) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_update_stack](#clientcancel_update_stack)
        - [Client().continue_update_rollback](#clientcontinue_update_rollback)
        - [Client().create_change_set](#clientcreate_change_set)
        - [Client().create_stack](#clientcreate_stack)
        - [Client().create_stack_instances](#clientcreate_stack_instances)
        - [Client().create_stack_set](#clientcreate_stack_set)
        - [Client().delete_change_set](#clientdelete_change_set)
        - [Client().delete_stack](#clientdelete_stack)
        - [Client().delete_stack_instances](#clientdelete_stack_instances)
        - [Client().delete_stack_set](#clientdelete_stack_set)
        - [Client().describe_account_limits](#clientdescribe_account_limits)
        - [Client().describe_change_set](#clientdescribe_change_set)
        - [Client().describe_stack_drift_detection_status](#clientdescribe_stack_drift_detection_status)
        - [Client().describe_stack_events](#clientdescribe_stack_events)
        - [Client().describe_stack_instance](#clientdescribe_stack_instance)
        - [Client().describe_stack_resource](#clientdescribe_stack_resource)
        - [Client().describe_stack_resource_drifts](#clientdescribe_stack_resource_drifts)
        - [Client().describe_stack_resources](#clientdescribe_stack_resources)
        - [Client().describe_stack_set](#clientdescribe_stack_set)
        - [Client().describe_stack_set_operation](#clientdescribe_stack_set_operation)
        - [Client().describe_stacks](#clientdescribe_stacks)
        - [Client().detect_stack_drift](#clientdetect_stack_drift)
        - [Client().detect_stack_resource_drift](#clientdetect_stack_resource_drift)
        - [Client().estimate_template_cost](#clientestimate_template_cost)
        - [Client().execute_change_set](#clientexecute_change_set)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_stack_policy](#clientget_stack_policy)
        - [Client().get_template](#clientget_template)
        - [Client().get_template_summary](#clientget_template_summary)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_change_sets](#clientlist_change_sets)
        - [Client().list_exports](#clientlist_exports)
        - [Client().list_imports](#clientlist_imports)
        - [Client().list_stack_instances](#clientlist_stack_instances)
        - [Client().list_stack_resources](#clientlist_stack_resources)
        - [Client().list_stack_set_operation_results](#clientlist_stack_set_operation_results)
        - [Client().list_stack_set_operations](#clientlist_stack_set_operations)
        - [Client().list_stack_sets](#clientlist_stack_sets)
        - [Client().list_stacks](#clientlist_stacks)
        - [Client().set_stack_policy](#clientset_stack_policy)
        - [Client().signal_resource](#clientsignal_resource)
        - [Client().stop_stack_set_operation](#clientstop_stack_set_operation)
        - [Client().update_stack](#clientupdate_stack)
        - [Client().update_stack_instances](#clientupdate_stack_instances)
        - [Client().update_stack_set](#clientupdate_stack_set)
        - [Client().update_termination_protection](#clientupdate_termination_protection)
        - [Client().validate_template](#clientvalidate_template)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_update_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L19)

```python
def cancel_update_stack(
    StackName: str,
    ClientRequestToken: str = None,
) -> None:
```

### Client().continue_update_rollback

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L25)

```python
def continue_update_rollback(
    StackName: str,
    RoleARN: str = None,
    ResourcesToSkip: List[Any] = None,
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().create_change_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L35)

```python
def create_change_set(
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
```

### Client().create_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L56)

```python
def create_stack(
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
```

### Client().create_stack_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L79)

```python
def create_stack_instances(
    StackSetName: str,
    Accounts: List[Any],
    Regions: List[Any],
    ParameterOverrides: List[Any] = None,
    OperationPreferences: Dict[str, Any] = None,
    OperationId: str = None,
) -> Dict[str, Any]:
```

### Client().create_stack_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L91)

```python
def create_stack_set(
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
```

### Client().delete_change_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L107)

```python
def delete_change_set(
    ChangeSetName: str,
    StackName: str = None,
) -> Dict[str, Any]:
```

### Client().delete_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L113)

```python
def delete_stack(
    StackName: str,
    RetainResources: List[Any] = None,
    RoleARN: str = None,
    ClientRequestToken: str = None,
) -> None:
```

### Client().delete_stack_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L123)

```python
def delete_stack_instances(
    StackSetName: str,
    Accounts: List[Any],
    Regions: List[Any],
    RetainStacks: bool,
    OperationPreferences: Dict[str, Any] = None,
    OperationId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_stack_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L135)

```python
def delete_stack_set(StackSetName: str) -> Dict[str, Any]:
```

### Client().describe_account_limits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L139)

```python
def describe_account_limits(NextToken: str = None) -> Dict[str, Any]:
```

### Client().describe_change_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L143)

```python
def describe_change_set(
    ChangeSetName: str,
    StackName: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_stack_drift_detection_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L149)

```python
def describe_stack_drift_detection_status(
    StackDriftDetectionId: str,
) -> Dict[str, Any]:
```

### Client().describe_stack_events

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L155)

```python
def describe_stack_events(
    StackName: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_stack_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L161)

```python
def describe_stack_instance(
    StackSetName: str,
    StackInstanceAccount: str,
    StackInstanceRegion: str,
) -> Dict[str, Any]:
```

### Client().describe_stack_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L167)

```python
def describe_stack_resource(
    StackName: str,
    LogicalResourceId: str,
) -> Dict[str, Any]:
```

### Client().describe_stack_resource_drifts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L173)

```python
def describe_stack_resource_drifts(
    StackName: str,
    StackResourceDriftStatusFilters: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_stack_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L183)

```python
def describe_stack_resources(
    StackName: str = None,
    LogicalResourceId: str = None,
    PhysicalResourceId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_stack_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L192)

```python
def describe_stack_set(StackSetName: str) -> Dict[str, Any]:
```

### Client().describe_stack_set_operation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L196)

```python
def describe_stack_set_operation(
    StackSetName: str,
    OperationId: str,
) -> Dict[str, Any]:
```

### Client().describe_stacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L202)

```python
def describe_stacks(
    StackName: str = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().detect_stack_drift

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L208)

```python
def detect_stack_drift(
    StackName: str,
    LogicalResourceIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().detect_stack_resource_drift

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L214)

```python
def detect_stack_resource_drift(
    StackName: str,
    LogicalResourceId: str,
) -> Dict[str, Any]:
```

### Client().estimate_template_cost

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L220)

```python
def estimate_template_cost(
    TemplateBody: str = None,
    TemplateURL: str = None,
    Parameters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().execute_change_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L229)

```python
def execute_change_set(
    ChangeSetName: str,
    StackName: str = None,
    ClientRequestToken: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L235)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L245)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_stack_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L249)

```python
def get_stack_policy(StackName: str) -> Dict[str, Any]:
```

### Client().get_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L253)

```python
def get_template(
    StackName: str = None,
    ChangeSetName: str = None,
    TemplateStage: str = None,
) -> Dict[str, Any]:
```

### Client().get_template_summary

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L262)

```python
def get_template_summary(
    TemplateBody: str = None,
    TemplateURL: str = None,
    StackName: str = None,
    StackSetName: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L272)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_change_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L276)

```python
def list_change_sets(StackName: str, NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_exports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L280)

```python
def list_exports(NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_imports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L284)

```python
def list_imports(ExportName: str, NextToken: str = None) -> Dict[str, Any]:
```

### Client().list_stack_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L288)

```python
def list_stack_instances(
    StackSetName: str,
    NextToken: str = None,
    MaxResults: int = None,
    StackInstanceAccount: str = None,
    StackInstanceRegion: str = None,
) -> Dict[str, Any]:
```

### Client().list_stack_resources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L299)

```python
def list_stack_resources(
    StackName: str,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_stack_set_operation_results

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L305)

```python
def list_stack_set_operation_results(
    StackSetName: str,
    OperationId: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_stack_set_operations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L315)

```python
def list_stack_set_operations(
    StackSetName: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_stack_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L321)

```python
def list_stack_sets(
    NextToken: str = None,
    MaxResults: int = None,
    Status: str = None,
) -> Dict[str, Any]:
```

### Client().list_stacks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L327)

```python
def list_stacks(
    NextToken: str = None,
    StackStatusFilter: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().set_stack_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L333)

```python
def set_stack_policy(
    StackName: str,
    StackPolicyBody: str = None,
    StackPolicyURL: str = None,
) -> None:
```

### Client().signal_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L339)

```python
def signal_resource(
    StackName: str,
    LogicalResourceId: str,
    UniqueId: str,
    Status: str,
) -> None:
```

### Client().stop_stack_set_operation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L345)

```python
def stop_stack_set_operation(
    StackSetName: str,
    OperationId: str,
) -> Dict[str, Any]:
```

### Client().update_stack

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L351)

```python
def update_stack(
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
```

### Client().update_stack_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L373)

```python
def update_stack_instances(
    StackSetName: str,
    Accounts: List[Any],
    Regions: List[Any],
    ParameterOverrides: List[Any] = None,
    OperationPreferences: Dict[str, Any] = None,
    OperationId: str = None,
) -> Dict[str, Any]:
```

### Client().update_stack_set

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L385)

```python
def update_stack_set(
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
```

### Client().update_termination_protection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L405)

```python
def update_termination_protection(
    EnableTerminationProtection: bool,
    StackName: str,
) -> Dict[str, Any]:
```

### Client().validate_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudformation/client.py#L411)

```python
def validate_template(
    TemplateBody: str = None,
    TemplateURL: str = None,
) -> Dict[str, Any]:
```
