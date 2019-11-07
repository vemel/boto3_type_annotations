from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def attach_instances(
        self,
        AutoScalingGroupName: str,
        InstanceIds: Optional[List] = None,
    ):
        pass


    def attach_load_balancer_target_groups(
        self,
        AutoScalingGroupName: str,
        TargetGroupARNs: List,
    ) -> Dict:
        pass


    def attach_load_balancers(
        self,
        AutoScalingGroupName: str,
        LoadBalancerNames: List,
    ) -> Dict:
        pass


    def batch_delete_scheduled_action(
        self,
        AutoScalingGroupName: str,
        ScheduledActionNames: List,
    ) -> Dict:
        pass


    def batch_put_scheduled_update_group_action(
        self,
        AutoScalingGroupName: str,
        ScheduledUpdateGroupActions: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def complete_lifecycle_action(
        self,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleActionResult: str,
        LifecycleActionToken: Optional[str] = None,
        InstanceId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_auto_scaling_group(
        self,
        AutoScalingGroupName: str,
        MinSize: int,
        MaxSize: int,
        LaunchConfigurationName: Optional[str] = None,
        LaunchTemplate: Optional[Dict] = None,
        MixedInstancesPolicy: Optional[Dict] = None,
        InstanceId: Optional[str] = None,
        DesiredCapacity: Optional[int] = None,
        DefaultCooldown: Optional[int] = None,
        AvailabilityZones: Optional[List] = None,
        LoadBalancerNames: Optional[List] = None,
        TargetGroupARNs: Optional[List] = None,
        HealthCheckType: Optional[str] = None,
        HealthCheckGracePeriod: Optional[int] = None,
        PlacementGroup: Optional[str] = None,
        VPCZoneIdentifier: Optional[str] = None,
        TerminationPolicies: Optional[List] = None,
        NewInstancesProtectedFromScaleIn: Optional[bool] = None,
        LifecycleHookSpecificationList: Optional[List] = None,
        Tags: Optional[List] = None,
        ServiceLinkedRoleARN: Optional[str] = None,
    ):
        pass


    def create_launch_configuration(
        self,
        LaunchConfigurationName: str,
        ImageId: Optional[str] = None,
        KeyName: Optional[str] = None,
        SecurityGroups: Optional[List] = None,
        ClassicLinkVPCId: Optional[str] = None,
        ClassicLinkVPCSecurityGroups: Optional[List] = None,
        UserData: Optional[str] = None,
        InstanceId: Optional[str] = None,
        InstanceType: Optional[str] = None,
        KernelId: Optional[str] = None,
        RamdiskId: Optional[str] = None,
        BlockDeviceMappings: Optional[List] = None,
        InstanceMonitoring: Optional[Dict] = None,
        SpotPrice: Optional[str] = None,
        IamInstanceProfile: Optional[str] = None,
        EbsOptimized: Optional[bool] = None,
        AssociatePublicIpAddress: Optional[bool] = None,
        PlacementTenancy: Optional[str] = None,
    ):
        pass


    def create_or_update_tags(
        self,
        Tags: List,
    ):
        pass


    def delete_auto_scaling_group(
        self,
        AutoScalingGroupName: str,
        ForceDelete: Optional[bool] = None,
    ):
        pass


    def delete_launch_configuration(
        self,
        LaunchConfigurationName: str,
    ):
        pass


    def delete_lifecycle_hook(
        self,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
    ) -> Dict:
        pass


    def delete_notification_configuration(
        self,
        AutoScalingGroupName: str,
        TopicARN: str,
    ):
        pass


    def delete_policy(
        self,
        PolicyName: str,
        AutoScalingGroupName: Optional[str] = None,
    ):
        pass


    def delete_scheduled_action(
        self,
        AutoScalingGroupName: str,
        ScheduledActionName: str,
    ):
        pass


    def delete_tags(
        self,
        Tags: List,
    ):
        pass


    def describe_account_limits(
        self,
    ) -> Dict:
        pass


    def describe_adjustment_types(
        self,
    ) -> Dict:
        pass


    def describe_auto_scaling_groups(
        self,
        AutoScalingGroupNames: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_auto_scaling_instances(
        self,
        InstanceIds: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_auto_scaling_notification_types(
        self,
    ) -> Dict:
        pass


    def describe_launch_configurations(
        self,
        LaunchConfigurationNames: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_lifecycle_hook_types(
        self,
    ) -> Dict:
        pass


    def describe_lifecycle_hooks(
        self,
        AutoScalingGroupName: str,
        LifecycleHookNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_load_balancer_target_groups(
        self,
        AutoScalingGroupName: str,
        NextToken: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_load_balancers(
        self,
        AutoScalingGroupName: str,
        NextToken: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_metric_collection_types(
        self,
    ) -> Dict:
        pass


    def describe_notification_configurations(
        self,
        AutoScalingGroupNames: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_policies(
        self,
        AutoScalingGroupName: Optional[str] = None,
        PolicyNames: Optional[List] = None,
        PolicyTypes: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_scaling_activities(
        self,
        ActivityIds: Optional[List] = None,
        AutoScalingGroupName: Optional[str] = None,
        MaxRecords: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_scaling_process_types(
        self,
    ) -> Dict:
        pass


    def describe_scheduled_actions(
        self,
        AutoScalingGroupName: Optional[str] = None,
        ScheduledActionNames: Optional[List] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        NextToken: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_tags(
        self,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxRecords: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_termination_policy_types(
        self,
    ) -> Dict:
        pass


    def detach_instances(
        self,
        AutoScalingGroupName: str,
        ShouldDecrementDesiredCapacity: bool,
        InstanceIds: Optional[List] = None,
    ) -> Dict:
        pass


    def detach_load_balancer_target_groups(
        self,
        AutoScalingGroupName: str,
        TargetGroupARNs: List,
    ) -> Dict:
        pass


    def detach_load_balancers(
        self,
        AutoScalingGroupName: str,
        LoadBalancerNames: List,
    ) -> Dict:
        pass


    def disable_metrics_collection(
        self,
        AutoScalingGroupName: str,
        Metrics: Optional[List] = None,
    ):
        pass


    def enable_metrics_collection(
        self,
        AutoScalingGroupName: str,
        Granularity: str,
        Metrics: Optional[List] = None,
    ):
        pass


    def enter_standby(
        self,
        AutoScalingGroupName: str,
        ShouldDecrementDesiredCapacity: bool,
        InstanceIds: Optional[List] = None,
    ) -> Dict:
        pass


    def execute_policy(
        self,
        PolicyName: str,
        AutoScalingGroupName: Optional[str] = None,
        HonorCooldown: Optional[bool] = None,
        MetricValue: Optional[float] = None,
        BreachThreshold: Optional[float] = None,
    ):
        pass


    def exit_standby(
        self,
        AutoScalingGroupName: str,
        InstanceIds: Optional[List] = None,
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


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def put_lifecycle_hook(
        self,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleTransition: Optional[str] = None,
        RoleARN: Optional[str] = None,
        NotificationTargetARN: Optional[str] = None,
        NotificationMetadata: Optional[str] = None,
        HeartbeatTimeout: Optional[int] = None,
        DefaultResult: Optional[str] = None,
    ) -> Dict:
        pass


    def put_notification_configuration(
        self,
        AutoScalingGroupName: str,
        TopicARN: str,
        NotificationTypes: List,
    ):
        pass


    def put_scaling_policy(
        self,
        AutoScalingGroupName: str,
        PolicyName: str,
        PolicyType: Optional[str] = None,
        AdjustmentType: Optional[str] = None,
        MinAdjustmentStep: Optional[int] = None,
        MinAdjustmentMagnitude: Optional[int] = None,
        ScalingAdjustment: Optional[int] = None,
        Cooldown: Optional[int] = None,
        MetricAggregationType: Optional[str] = None,
        StepAdjustments: Optional[List] = None,
        EstimatedInstanceWarmup: Optional[int] = None,
        TargetTrackingConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


    def put_scheduled_update_group_action(
        self,
        AutoScalingGroupName: str,
        ScheduledActionName: str,
        Time: Optional[datetime] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        Recurrence: Optional[str] = None,
        MinSize: Optional[int] = None,
        MaxSize: Optional[int] = None,
        DesiredCapacity: Optional[int] = None,
    ):
        pass


    def record_lifecycle_action_heartbeat(
        self,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleActionToken: Optional[str] = None,
        InstanceId: Optional[str] = None,
    ) -> Dict:
        pass


    def resume_processes(
        self,
        AutoScalingGroupName: str,
        ScalingProcesses: Optional[List] = None,
    ):
        pass


    def set_desired_capacity(
        self,
        AutoScalingGroupName: str,
        DesiredCapacity: int,
        HonorCooldown: Optional[bool] = None,
    ):
        pass


    def set_instance_health(
        self,
        InstanceId: str,
        HealthStatus: str,
        ShouldRespectGracePeriod: Optional[bool] = None,
    ):
        pass


    def set_instance_protection(
        self,
        InstanceIds: List,
        AutoScalingGroupName: str,
        ProtectedFromScaleIn: bool,
    ) -> Dict:
        pass


    def suspend_processes(
        self,
        AutoScalingGroupName: str,
        ScalingProcesses: Optional[List] = None,
    ):
        pass


    def terminate_instance_in_auto_scaling_group(
        self,
        InstanceId: str,
        ShouldDecrementDesiredCapacity: bool,
    ) -> Dict:
        pass


    def update_auto_scaling_group(
        self,
        AutoScalingGroupName: str,
        LaunchConfigurationName: Optional[str] = None,
        LaunchTemplate: Optional[Dict] = None,
        MixedInstancesPolicy: Optional[Dict] = None,
        MinSize: Optional[int] = None,
        MaxSize: Optional[int] = None,
        DesiredCapacity: Optional[int] = None,
        DefaultCooldown: Optional[int] = None,
        AvailabilityZones: Optional[List] = None,
        HealthCheckType: Optional[str] = None,
        HealthCheckGracePeriod: Optional[int] = None,
        PlacementGroup: Optional[str] = None,
        VPCZoneIdentifier: Optional[str] = None,
        TerminationPolicies: Optional[List] = None,
        NewInstancesProtectedFromScaleIn: Optional[bool] = None,
        ServiceLinkedRoleARN: Optional[str] = None,
    ):
        pass

