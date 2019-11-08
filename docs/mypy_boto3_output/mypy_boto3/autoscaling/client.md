# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.autoscaling.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Autoscaling](index.md#autoscaling) / Client
    - [Client](#client)
        - [Client().attach_instances](#clientattach_instances)
        - [Client().attach_load_balancer_target_groups](#clientattach_load_balancer_target_groups)
        - [Client().attach_load_balancers](#clientattach_load_balancers)
        - [Client().batch_delete_scheduled_action](#clientbatch_delete_scheduled_action)
        - [Client().batch_put_scheduled_update_group_action](#clientbatch_put_scheduled_update_group_action)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().complete_lifecycle_action](#clientcomplete_lifecycle_action)
        - [Client().create_auto_scaling_group](#clientcreate_auto_scaling_group)
        - [Client().create_launch_configuration](#clientcreate_launch_configuration)
        - [Client().create_or_update_tags](#clientcreate_or_update_tags)
        - [Client().delete_auto_scaling_group](#clientdelete_auto_scaling_group)
        - [Client().delete_launch_configuration](#clientdelete_launch_configuration)
        - [Client().delete_lifecycle_hook](#clientdelete_lifecycle_hook)
        - [Client().delete_notification_configuration](#clientdelete_notification_configuration)
        - [Client().delete_policy](#clientdelete_policy)
        - [Client().delete_scheduled_action](#clientdelete_scheduled_action)
        - [Client().delete_tags](#clientdelete_tags)
        - [Client().describe_account_limits](#clientdescribe_account_limits)
        - [Client().describe_adjustment_types](#clientdescribe_adjustment_types)
        - [Client().describe_auto_scaling_groups](#clientdescribe_auto_scaling_groups)
        - [Client().describe_auto_scaling_instances](#clientdescribe_auto_scaling_instances)
        - [Client().describe_auto_scaling_notification_types](#clientdescribe_auto_scaling_notification_types)
        - [Client().describe_launch_configurations](#clientdescribe_launch_configurations)
        - [Client().describe_lifecycle_hook_types](#clientdescribe_lifecycle_hook_types)
        - [Client().describe_lifecycle_hooks](#clientdescribe_lifecycle_hooks)
        - [Client().describe_load_balancer_target_groups](#clientdescribe_load_balancer_target_groups)
        - [Client().describe_load_balancers](#clientdescribe_load_balancers)
        - [Client().describe_metric_collection_types](#clientdescribe_metric_collection_types)
        - [Client().describe_notification_configurations](#clientdescribe_notification_configurations)
        - [Client().describe_policies](#clientdescribe_policies)
        - [Client().describe_scaling_activities](#clientdescribe_scaling_activities)
        - [Client().describe_scaling_process_types](#clientdescribe_scaling_process_types)
        - [Client().describe_scheduled_actions](#clientdescribe_scheduled_actions)
        - [Client().describe_tags](#clientdescribe_tags)
        - [Client().describe_termination_policy_types](#clientdescribe_termination_policy_types)
        - [Client().detach_instances](#clientdetach_instances)
        - [Client().detach_load_balancer_target_groups](#clientdetach_load_balancer_target_groups)
        - [Client().detach_load_balancers](#clientdetach_load_balancers)
        - [Client().disable_metrics_collection](#clientdisable_metrics_collection)
        - [Client().enable_metrics_collection](#clientenable_metrics_collection)
        - [Client().enter_standby](#cliententer_standby)
        - [Client().execute_policy](#clientexecute_policy)
        - [Client().exit_standby](#clientexit_standby)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().put_lifecycle_hook](#clientput_lifecycle_hook)
        - [Client().put_notification_configuration](#clientput_notification_configuration)
        - [Client().put_scaling_policy](#clientput_scaling_policy)
        - [Client().put_scheduled_update_group_action](#clientput_scheduled_update_group_action)
        - [Client().record_lifecycle_action_heartbeat](#clientrecord_lifecycle_action_heartbeat)
        - [Client().resume_processes](#clientresume_processes)
        - [Client().set_desired_capacity](#clientset_desired_capacity)
        - [Client().set_instance_health](#clientset_instance_health)
        - [Client().set_instance_protection](#clientset_instance_protection)
        - [Client().suspend_processes](#clientsuspend_processes)
        - [Client().terminate_instance_in_auto_scaling_group](#clientterminate_instance_in_auto_scaling_group)
        - [Client().update_auto_scaling_group](#clientupdate_auto_scaling_group)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L13)

```python
class Client(BaseClient):
```

### Client().attach_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L16)

```python
def attach_instances(
    AutoScalingGroupName: str,
    InstanceIds: List[Any] = None,
) -> None:
```

### Client().attach_load_balancer_target_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L22)

```python
def attach_load_balancer_target_groups(
    AutoScalingGroupName: str,
    TargetGroupARNs: List[Any],
) -> Dict[str, Any]:
```

### Client().attach_load_balancers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L28)

```python
def attach_load_balancers(
    AutoScalingGroupName: str,
    LoadBalancerNames: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_delete_scheduled_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L34)

```python
def batch_delete_scheduled_action(
    AutoScalingGroupName: str,
    ScheduledActionNames: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_put_scheduled_update_group_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L40)

```python
def batch_put_scheduled_update_group_action(
    AutoScalingGroupName: str,
    ScheduledUpdateGroupActions: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L46)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().complete_lifecycle_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L50)

```python
def complete_lifecycle_action(
    LifecycleHookName: str,
    AutoScalingGroupName: str,
    LifecycleActionResult: str,
    LifecycleActionToken: str = None,
    InstanceId: str = None,
) -> Dict[str, Any]:
```

### Client().create_auto_scaling_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L61)

```python
def create_auto_scaling_group(
    AutoScalingGroupName: str,
    MinSize: int,
    MaxSize: int,
    LaunchConfigurationName: str = None,
    LaunchTemplate: Dict[str, Any] = None,
    MixedInstancesPolicy: Dict[str, Any] = None,
    InstanceId: str = None,
    DesiredCapacity: int = None,
    DefaultCooldown: int = None,
    AvailabilityZones: List[Any] = None,
    LoadBalancerNames: List[Any] = None,
    TargetGroupARNs: List[Any] = None,
    HealthCheckType: str = None,
    HealthCheckGracePeriod: int = None,
    PlacementGroup: str = None,
    VPCZoneIdentifier: str = None,
    TerminationPolicies: List[Any] = None,
    NewInstancesProtectedFromScaleIn: bool = None,
    LifecycleHookSpecificationList: List[Any] = None,
    Tags: List[Any] = None,
    ServiceLinkedRoleARN: str = None,
) -> None:
```

### Client().create_launch_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L88)

```python
def create_launch_configuration(
    LaunchConfigurationName: str,
    ImageId: str = None,
    KeyName: str = None,
    SecurityGroups: List[Any] = None,
    ClassicLinkVPCId: str = None,
    ClassicLinkVPCSecurityGroups: List[Any] = None,
    UserData: str = None,
    InstanceId: str = None,
    InstanceType: str = None,
    KernelId: str = None,
    RamdiskId: str = None,
    BlockDeviceMappings: List[Any] = None,
    InstanceMonitoring: Dict[str, Any] = None,
    SpotPrice: str = None,
    IamInstanceProfile: str = None,
    EbsOptimized: bool = None,
    AssociatePublicIpAddress: bool = None,
    PlacementTenancy: str = None,
) -> None:
```

### Client().create_or_update_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L112)

```python
def create_or_update_tags(Tags: List[Any]) -> None:
```

### Client().delete_auto_scaling_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L116)

```python
def delete_auto_scaling_group(
    AutoScalingGroupName: str,
    ForceDelete: bool = None,
) -> None:
```

### Client().delete_launch_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L122)

```python
def delete_launch_configuration(LaunchConfigurationName: str) -> None:
```

### Client().delete_lifecycle_hook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L126)

```python
def delete_lifecycle_hook(
    LifecycleHookName: str,
    AutoScalingGroupName: str,
) -> Dict[str, Any]:
```

### Client().delete_notification_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L132)

```python
def delete_notification_configuration(
    AutoScalingGroupName: str,
    TopicARN: str,
) -> None:
```

### Client().delete_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L138)

```python
def delete_policy(PolicyName: str, AutoScalingGroupName: str = None) -> None:
```

### Client().delete_scheduled_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L142)

```python
def delete_scheduled_action(
    AutoScalingGroupName: str,
    ScheduledActionName: str,
) -> None:
```

### Client().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L148)

```python
def delete_tags(Tags: List[Any]) -> None:
```

### Client().describe_account_limits

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L152)

```python
def describe_account_limits() -> Dict[str, Any]:
```

### Client().describe_adjustment_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L156)

```python
def describe_adjustment_types() -> Dict[str, Any]:
```

### Client().describe_auto_scaling_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L160)

```python
def describe_auto_scaling_groups(
    AutoScalingGroupNames: List[Any] = None,
    NextToken: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_auto_scaling_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L169)

```python
def describe_auto_scaling_instances(
    InstanceIds: List[Any] = None,
    MaxRecords: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_auto_scaling_notification_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L178)

```python
def describe_auto_scaling_notification_types() -> Dict[str, Any]:
```

### Client().describe_launch_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L182)

```python
def describe_launch_configurations(
    LaunchConfigurationNames: List[Any] = None,
    NextToken: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_lifecycle_hook_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L191)

```python
def describe_lifecycle_hook_types() -> Dict[str, Any]:
```

### Client().describe_lifecycle_hooks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L195)

```python
def describe_lifecycle_hooks(
    AutoScalingGroupName: str,
    LifecycleHookNames: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_load_balancer_target_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L201)

```python
def describe_load_balancer_target_groups(
    AutoScalingGroupName: str,
    NextToken: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_load_balancers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L207)

```python
def describe_load_balancers(
    AutoScalingGroupName: str,
    NextToken: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_metric_collection_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L213)

```python
def describe_metric_collection_types() -> Dict[str, Any]:
```

### Client().describe_notification_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L217)

```python
def describe_notification_configurations(
    AutoScalingGroupNames: List[Any] = None,
    NextToken: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L226)

```python
def describe_policies(
    AutoScalingGroupName: str = None,
    PolicyNames: List[Any] = None,
    PolicyTypes: List[Any] = None,
    NextToken: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_scaling_activities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L237)

```python
def describe_scaling_activities(
    ActivityIds: List[Any] = None,
    AutoScalingGroupName: str = None,
    MaxRecords: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_scaling_process_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L247)

```python
def describe_scaling_process_types() -> Dict[str, Any]:
```

### Client().describe_scheduled_actions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L251)

```python
def describe_scheduled_actions(
    AutoScalingGroupName: str = None,
    ScheduledActionNames: List[Any] = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    NextToken: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L263)

```python
def describe_tags(
    Filters: List[Any] = None,
    NextToken: str = None,
    MaxRecords: int = None,
) -> Dict[str, Any]:
```

### Client().describe_termination_policy_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L269)

```python
def describe_termination_policy_types() -> Dict[str, Any]:
```

### Client().detach_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L273)

```python
def detach_instances(
    AutoScalingGroupName: str,
    ShouldDecrementDesiredCapacity: bool,
    InstanceIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().detach_load_balancer_target_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L282)

```python
def detach_load_balancer_target_groups(
    AutoScalingGroupName: str,
    TargetGroupARNs: List[Any],
) -> Dict[str, Any]:
```

### Client().detach_load_balancers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L288)

```python
def detach_load_balancers(
    AutoScalingGroupName: str,
    LoadBalancerNames: List[Any],
) -> Dict[str, Any]:
```

### Client().disable_metrics_collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L294)

```python
def disable_metrics_collection(
    AutoScalingGroupName: str,
    Metrics: List[Any] = None,
) -> None:
```

### Client().enable_metrics_collection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L300)

```python
def enable_metrics_collection(
    AutoScalingGroupName: str,
    Granularity: str,
    Metrics: List[Any] = None,
) -> None:
```

### Client().enter_standby

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L306)

```python
def enter_standby(
    AutoScalingGroupName: str,
    ShouldDecrementDesiredCapacity: bool,
    InstanceIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().execute_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L315)

```python
def execute_policy(
    PolicyName: str,
    AutoScalingGroupName: str = None,
    HonorCooldown: bool = None,
    MetricValue: float = None,
    BreachThreshold: float = None,
) -> None:
```

### Client().exit_standby

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L326)

```python
def exit_standby(
    AutoScalingGroupName: str,
    InstanceIds: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L332)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L342)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L346)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().put_lifecycle_hook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L350)

```python
def put_lifecycle_hook(
    LifecycleHookName: str,
    AutoScalingGroupName: str,
    LifecycleTransition: str = None,
    RoleARN: str = None,
    NotificationTargetARN: str = None,
    NotificationMetadata: str = None,
    HeartbeatTimeout: int = None,
    DefaultResult: str = None,
) -> Dict[str, Any]:
```

### Client().put_notification_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L364)

```python
def put_notification_configuration(
    AutoScalingGroupName: str,
    TopicARN: str,
    NotificationTypes: List[Any],
) -> None:
```

### Client().put_scaling_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L370)

```python
def put_scaling_policy(
    AutoScalingGroupName: str,
    PolicyName: str,
    PolicyType: str = None,
    AdjustmentType: str = None,
    MinAdjustmentStep: int = None,
    MinAdjustmentMagnitude: int = None,
    ScalingAdjustment: int = None,
    Cooldown: int = None,
    MetricAggregationType: str = None,
    StepAdjustments: List[Any] = None,
    EstimatedInstanceWarmup: int = None,
    TargetTrackingConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().put_scheduled_update_group_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L388)

```python
def put_scheduled_update_group_action(
    AutoScalingGroupName: str,
    ScheduledActionName: str,
    Time: datetime = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Recurrence: str = None,
    MinSize: int = None,
    MaxSize: int = None,
    DesiredCapacity: int = None,
) -> None:
```

### Client().record_lifecycle_action_heartbeat

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L403)

```python
def record_lifecycle_action_heartbeat(
    LifecycleHookName: str,
    AutoScalingGroupName: str,
    LifecycleActionToken: str = None,
    InstanceId: str = None,
) -> Dict[str, Any]:
```

### Client().resume_processes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L413)

```python
def resume_processes(
    AutoScalingGroupName: str,
    ScalingProcesses: List[Any] = None,
) -> None:
```

### Client().set_desired_capacity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L419)

```python
def set_desired_capacity(
    AutoScalingGroupName: str,
    DesiredCapacity: int,
    HonorCooldown: bool = None,
) -> None:
```

### Client().set_instance_health

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L428)

```python
def set_instance_health(
    InstanceId: str,
    HealthStatus: str,
    ShouldRespectGracePeriod: bool = None,
) -> None:
```

### Client().set_instance_protection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L434)

```python
def set_instance_protection(
    InstanceIds: List[Any],
    AutoScalingGroupName: str,
    ProtectedFromScaleIn: bool,
) -> Dict[str, Any]:
```

### Client().suspend_processes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L443)

```python
def suspend_processes(
    AutoScalingGroupName: str,
    ScalingProcesses: List[Any] = None,
) -> None:
```

### Client().terminate_instance_in_auto_scaling_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L449)

```python
def terminate_instance_in_auto_scaling_group(
    InstanceId: str,
    ShouldDecrementDesiredCapacity: bool,
) -> Dict[str, Any]:
```

### Client().update_auto_scaling_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/autoscaling/client.py#L455)

```python
def update_auto_scaling_group(
    AutoScalingGroupName: str,
    LaunchConfigurationName: str = None,
    LaunchTemplate: Dict[str, Any] = None,
    MixedInstancesPolicy: Dict[str, Any] = None,
    MinSize: int = None,
    MaxSize: int = None,
    DesiredCapacity: int = None,
    DefaultCooldown: int = None,
    AvailabilityZones: List[Any] = None,
    HealthCheckType: str = None,
    HealthCheckGracePeriod: int = None,
    PlacementGroup: str = None,
    VPCZoneIdentifier: str = None,
    TerminationPolicies: List[Any] = None,
    NewInstancesProtectedFromScaleIn: bool = None,
    ServiceLinkedRoleARN: str = None,
) -> None:
```
