"Main interface for autoscaling type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef",
    "ClientBatchDeleteScheduledActionResponseTypeDef",
    "ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef",
    "ClientBatchPutScheduledUpdateGroupActionResponseTypeDef",
    "ClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef",
    "ClientCreateAutoScalingGroupLaunchTemplateTypeDef",
    "ClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef",
    "ClientCreateAutoScalingGroupTagsTypeDef",
    "ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef",
    "ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef",
    "ClientCreateLaunchConfigurationInstanceMonitoringTypeDef",
    "ClientCreateOrUpdateTagsTagsTypeDef",
    "ClientDeleteTagsTagsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef",
    "ClientDescribeAdjustmentTypesResponseTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef",
    "ClientDescribeAutoScalingGroupsResponseTypeDef",
    "ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef",
    "ClientDescribeAutoScalingInstancesResponseTypeDef",
    "ClientDescribeAutoScalingNotificationTypesResponseTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef",
    "ClientDescribeLaunchConfigurationsResponseTypeDef",
    "ClientDescribeLifecycleHookTypesResponseTypeDef",
    "ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef",
    "ClientDescribeLifecycleHooksResponseTypeDef",
    "ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef",
    "ClientDescribeLoadBalancerTargetGroupsResponseTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    "ClientDescribeLoadBalancersResponseTypeDef",
    "ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef",
    "ClientDescribeMetricCollectionTypesResponseMetricsTypeDef",
    "ClientDescribeMetricCollectionTypesResponseTypeDef",
    "ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef",
    "ClientDescribeNotificationConfigurationsResponseTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTypeDef",
    "ClientDescribePoliciesResponseTypeDef",
    "ClientDescribeScalingActivitiesResponseActivitiesTypeDef",
    "ClientDescribeScalingActivitiesResponseTypeDef",
    "ClientDescribeScalingProcessTypesResponseProcessesTypeDef",
    "ClientDescribeScalingProcessTypesResponseTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef",
    "ClientDescribeScheduledActionsResponseTypeDef",
    "ClientDescribeTagsFiltersTypeDef",
    "ClientDescribeTagsResponseTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeTerminationPolicyTypesResponseTypeDef",
    "ClientDetachInstancesResponseActivitiesTypeDef",
    "ClientDetachInstancesResponseTypeDef",
    "ClientEnterStandbyResponseActivitiesTypeDef",
    "ClientEnterStandbyResponseTypeDef",
    "ClientExitStandbyResponseActivitiesTypeDef",
    "ClientExitStandbyResponseTypeDef",
    "ClientPutScalingPolicyResponseAlarmsTypeDef",
    "ClientPutScalingPolicyResponseTypeDef",
    "ClientPutScalingPolicyStepAdjustmentsTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationTypeDef",
    "ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef",
    "ClientTerminateInstanceInAutoScalingGroupResponseTypeDef",
    "ClientUpdateAutoScalingGroupLaunchTemplateTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef",
    "DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef",
    "DescribeAutoScalingGroupsPaginateResponseTypeDef",
    "DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef",
    "DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef",
    "DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef",
    "DescribeAutoScalingInstancesPaginateResponseTypeDef",
    "DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    "DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef",
    "DescribeLaunchConfigurationsPaginateResponseTypeDef",
    "DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef",
    "DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef",
    "DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef",
    "DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef",
    "DescribeLoadBalancersPaginateResponseTypeDef",
    "DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef",
    "DescribeNotificationConfigurationsPaginateResponseTypeDef",
    "DescribePoliciesPaginatePaginationConfigTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    "DescribePoliciesPaginateResponseScalingPoliciesTypeDef",
    "DescribePoliciesPaginateResponseTypeDef",
    "DescribeScalingActivitiesPaginatePaginationConfigTypeDef",
    "DescribeScalingActivitiesPaginateResponseActivitiesTypeDef",
    "DescribeScalingActivitiesPaginateResponseTypeDef",
    "DescribeScheduledActionsPaginatePaginationConfigTypeDef",
    "DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef",
    "DescribeScheduledActionsPaginateResponseTypeDef",
    "DescribeTagsPaginateFiltersTypeDef",
    "DescribeTagsPaginatePaginationConfigTypeDef",
    "DescribeTagsPaginateResponseTagsTypeDef",
    "DescribeTagsPaginateResponseTypeDef",
)


_ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef = TypedDict(
    "_ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef",
    {"ScheduledActionName": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef(
    _ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef
):
    """
    Type definition for `ClientBatchDeleteScheduledActionResponse` `FailedScheduledActions`

    Describes a scheduled action that could not be created, updated, or deleted.

    - **ScheduledActionName** *(string) --*

      The name of the scheduled action.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message accompanying the error code.
    """


_ClientBatchDeleteScheduledActionResponseTypeDef = TypedDict(
    "_ClientBatchDeleteScheduledActionResponseTypeDef",
    {
        "FailedScheduledActions": List[
            ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef
        ]
    },
    total=False,
)


class ClientBatchDeleteScheduledActionResponseTypeDef(
    _ClientBatchDeleteScheduledActionResponseTypeDef
):
    """
    Type definition for `ClientBatchDeleteScheduledAction` `Response`

    - **FailedScheduledActions** *(list) --*

      The names of the scheduled actions that could not be deleted, including an error message.

      - *(dict) --*

        Describes a scheduled action that could not be created, updated, or deleted.

        - **ScheduledActionName** *(string) --*

          The name of the scheduled action.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message accompanying the error code.
    """


_ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef",
    {"ScheduledActionName": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef(
    _ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef
):
    """
    Type definition for `ClientBatchPutScheduledUpdateGroupActionResponse` `FailedScheduledUpdateGroupActions`

    Describes a scheduled action that could not be created, updated, or deleted.

    - **ScheduledActionName** *(string) --*

      The name of the scheduled action.

    - **ErrorCode** *(string) --*

      The error code.

    - **ErrorMessage** *(string) --*

      The error message accompanying the error code.
    """


_ClientBatchPutScheduledUpdateGroupActionResponseTypeDef = TypedDict(
    "_ClientBatchPutScheduledUpdateGroupActionResponseTypeDef",
    {
        "FailedScheduledUpdateGroupActions": List[
            ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef
        ]
    },
    total=False,
)


class ClientBatchPutScheduledUpdateGroupActionResponseTypeDef(
    _ClientBatchPutScheduledUpdateGroupActionResponseTypeDef
):
    """
    Type definition for `ClientBatchPutScheduledUpdateGroupAction` `Response`

    - **FailedScheduledUpdateGroupActions** *(list) --*

      The names of the scheduled actions that could not be created or updated, including an error
      message.

      - *(dict) --*

        Describes a scheduled action that could not be created, updated, or deleted.

        - **ScheduledActionName** *(string) --*

          The name of the scheduled action.

        - **ErrorCode** *(string) --*

          The error code.

        - **ErrorMessage** *(string) --*

          The error message accompanying the error code.
    """


_RequiredClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_RequiredClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef",
    {"ScheduledActionName": str},
)
_OptionalClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_OptionalClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
    },
    total=False,
)


class ClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef(
    _RequiredClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef,
    _OptionalClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef,
):
    """
    Type definition for `ClientBatchPutScheduledUpdateGroupAction` `ScheduledUpdateGroupActions`

    Describes one or more scheduled scaling action updates for a specified Auto Scaling group. Used
    in combination with  BatchPutScheduledUpdateGroupAction .

    When updating a scheduled scaling action, all optional parameters are left unchanged if not
    specified.

    - **ScheduledActionName** *(string) --* **[REQUIRED]**

      The name of the scaling action.

    - **StartTime** *(datetime) --*

      The date and time for the action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and
      in quotes (for example, ``"2019-06-01T00:00:00Z"`` ).

      If you specify ``Recurrence`` and ``StartTime`` , Amazon EC2 Auto Scaling performs the action
      at this time, and then performs the action based on the specified recurrence.

      If you try to schedule the action in the past, Amazon EC2 Auto Scaling returns an error
      message.

    - **EndTime** *(datetime) --*

      The date and time for the recurring schedule to end. Amazon EC2 Auto Scaling does not perform
      the action after this time.

    - **Recurrence** *(string) --*

      The recurring schedule for the action, in Unix cron syntax format. This format consists of
      five fields separated by white spaces: [Minute] [Hour] [Day_of_Month] [Month_of_Year]
      [Day_of_Week]. The value must be in quotes (for example, ``"30 0 1 1,6,12 *"`` ). For more
      information about this format, see `Crontab <http://crontab.org>`__ .

      When ``StartTime`` and ``EndTime`` are specified with ``Recurrence`` , they form the
      boundaries of when the recurring action starts and stops.

    - **MinSize** *(integer) --*

      The minimum number of instances in the Auto Scaling group.

    - **MaxSize** *(integer) --*

      The maximum number of instances in the Auto Scaling group.

    - **DesiredCapacity** *(integer) --*

      The number of EC2 instances that should be running in the group.
    """


_ClientCreateAutoScalingGroupLaunchTemplateTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientCreateAutoScalingGroupLaunchTemplateTypeDef(
    _ClientCreateAutoScalingGroupLaunchTemplateTypeDef
):
    """
    Type definition for `ClientCreateAutoScalingGroup` `LaunchTemplate`

    The launch template to use to launch instances.

    For more information, see `LaunchTemplateSpecification
    <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchTemplateSpecification.html>`__
    in the *Amazon EC2 Auto Scaling API Reference* .

    If you do not specify ``LaunchTemplate`` , you must specify one of the following parameters:
    ``InstanceId`` , ``LaunchConfigurationName`` , or ``MixedInstancesPolicy`` .

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a template ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2
      Auto Scaling selects the latest version of the launch template when launching instances. If the
      value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch
      template when launching instances. The default value is ``$Default`` .
    """


_RequiredClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef = TypedDict(
    "_RequiredClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef",
    {"LifecycleHookName": str, "LifecycleTransition": str},
)
_OptionalClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef = TypedDict(
    "_OptionalClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef",
    {
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "DefaultResult": str,
        "NotificationTargetARN": str,
        "RoleARN": str,
    },
    total=False,
)


class ClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef(
    _RequiredClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef,
    _OptionalClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef,
):
    """
    Type definition for `ClientCreateAutoScalingGroup` `LifecycleHookSpecificationList`

    Describes a lifecycle hook. Used in combination with  CreateAutoScalingGroup .

    A lifecycle hook tells Amazon EC2 Auto Scaling to perform an action on an instance when the
    instance launches (before it is put into service) or as the instance terminates (before it is
    fully terminated).

    This step is a part of the procedure for creating a lifecycle hook for an Auto Scaling group:

    * (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your
    Lambda function when Amazon EC2 Auto Scaling launches or terminates instances.

    * (Optional) Create a notification target and an IAM role. The target can be either an Amazon
    SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle
    notifications to the target.

    * **Create the lifecycle hook. Specify whether the hook is used when the instances launch or
    terminate.**

    * If you need more time, record the lifecycle action heartbeat to keep the instance in a
    pending state using  RecordLifecycleActionHeartbeat .

    * If you finish before the timeout period ends, complete the lifecycle action using
    CompleteLifecycleAction .

    For more information, see `Amazon EC2 Auto Scaling Lifecycle Hooks
    <https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html>`__ in the *Amazon
    EC2 Auto Scaling User Guide* .

    You can view the lifecycle hooks for an Auto Scaling group using  DescribeLifecycleHooks . You
    can modify an existing lifecycle hook or create new lifecycle hooks using  PutLifecycleHook .
    If you are no longer using a lifecycle hook, you can delete it using  DeleteLifecycleHook .

    - **LifecycleHookName** *(string) --* **[REQUIRED]**

      The name of the lifecycle hook.

    - **LifecycleTransition** *(string) --* **[REQUIRED]**

      The state of the EC2 instance to which you want to attach the lifecycle hook. The valid
      values are:

      * autoscaling:EC2_INSTANCE_LAUNCHING

      * autoscaling:EC2_INSTANCE_TERMINATING

    - **NotificationMetadata** *(string) --*

      Additional information that you want to include any time Amazon EC2 Auto Scaling sends a
      message to the notification target.

    - **HeartbeatTimeout** *(integer) --*

      The maximum time, in seconds, that can elapse before the lifecycle hook times out.

      If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you
      specified in the ``DefaultResult`` parameter. You can prevent the lifecycle hook from timing
      out by calling  RecordLifecycleActionHeartbeat .

    - **DefaultResult** *(string) --*

      Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses
      or if an unexpected failure occurs. The valid values are ``CONTINUE`` and ``ABANDON`` . The
      default value is ``ABANDON`` .

    - **NotificationTargetARN** *(string) --*

      The ARN of the target that Amazon EC2 Auto Scaling sends notifications to when an instance is
      in the transition state for the lifecycle hook. The notification target can be either an SQS
      queue or an SNS topic.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that allows the Auto Scaling group to publish to the specified
      notification target, for example, an Amazon SNS topic or an Amazon SQS queue.
    """


_ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)


class ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef(
    _ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef
):
    """
    Type definition for `ClientCreateAutoScalingGroupMixedInstancesPolicy` `InstancesDistribution`

    The instances distribution to use.

    If you leave this parameter unspecified, the value for each parameter in
    ``InstancesDistribution`` uses a default value.

    - **OnDemandAllocationStrategy** *(string) --*

      Indicates how to allocate instance types to fulfill On-Demand capacity.

      The only valid value is ``prioritized`` , which is also the default value. This strategy uses
      the order of instance type overrides for the  LaunchTemplate to define the launch priority of
      each instance type. The first instance type in the array is prioritized higher than the last.
      If all your On-Demand capacity cannot be fulfilled using your highest priority instance, then
      the Auto Scaling groups launches the remaining capacity using the second priority instance
      type, and so on.

    - **OnDemandBaseCapacity** *(integer) --*

      The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand
      Instances. This base portion is provisioned first as your group scales.

      Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched as a
      percentage of the Auto Scaling group's desired capacity, per the
      ``OnDemandPercentageAboveBaseCapacity`` setting.

      .. note::

        An update to this setting means a gradual replacement of instances to maintain the
        specified number of On-Demand Instances for your base capacity. When replacing instances,
        Amazon EC2 Auto Scaling launches new instances before terminating the old ones.

    - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

      Controls the percentages of On-Demand Instances and Spot Instances for your additional
      capacity beyond ``OnDemandBaseCapacity`` .

      Default if not set is 100. If you leave it set to 100, the percentages are 100% for On-Demand
      Instances and 0% for Spot Instances.

      .. note::

        An update to this setting means a gradual replacement of instances to maintain the
        percentage of On-Demand Instances for your additional capacity above the base capacity.
        When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating
        the old ones.

      Valid Range: Minimum value of 0. Maximum value of 100.

    - **SpotAllocationStrategy** *(string) --*

      Indicates how to allocate instances across Spot Instance pools.

      If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches instances
      using the Spot pools with the lowest price, and evenly allocates your instances across the
      number of Spot pools that you specify. If the allocation strategy is ``capacity-optimized`` ,
      the Auto Scaling group launches instances using Spot pools that are optimally chosen based on
      the available Spot capacity.

      The default Spot allocation strategy for calls that you make through the API, the AWS CLI, or
      the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for the AWS
      Management Console is ``capacity-optimized`` .

      Valid values: ``lowest-price`` | ``capacity-optimized``

    - **SpotInstancePools** *(integer) --*

      The number of Spot Instance pools across which to allocate your Spot Instances. The Spot
      pools are determined from the different instance types in the Overrides array of
      LaunchTemplate . Default if not set is 2.

      Used only when the Spot allocation strategy is ``lowest-price`` .

      Valid Range: Minimum value of 1. Maximum value of 20.

    - **SpotMaxPrice** *(string) --*

      The maximum price per unit hour that you are willing to pay for a Spot Instance. If you leave
      the value of this parameter blank (which is the default), the maximum Spot price is set at
      the On-Demand price.

      To remove a value that you previously set, include the parameter but leave the value blank.
    """


_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(
    _ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
):
    """
    Type definition for `ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplate` `LaunchTemplateSpecification`

    The launch template to use. You must specify either the launch template ID or launch template
    name in the request.

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a template ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon
      EC2 Auto Scaling selects the latest version of the launch template when launching
      instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default
      version of the launch template when launching instances. The default value is ``$Default`` .
    """


_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)


class ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef(
    _ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
):
    """
    Type definition for `ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplate` `Overrides`

    Describes an override for a launch template.

    - **InstanceType** *(string) --*

      The instance type.

      For information about available instance types, see `Available Instance Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
      in the *Amazon Elastic Compute Cloud User Guide.*

    - **WeightedCapacity** *(string) --*

      The number of capacity units, which gives the instance type a proportional weight to
      other instance types. For example, larger instance types are generally weighted more than
      smaller instance types. These are the same units that you chose to set the desired
      capacity in terms of instances, or a performance attribute such as vCPUs, memory, or I/O.

      Valid Range: Minimum value of 1. Maximum value of 999.
    """


_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)


class ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef(
    _ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef
):
    """
    Type definition for `ClientCreateAutoScalingGroupMixedInstancesPolicy` `LaunchTemplate`

    The launch template and instance types (overrides).

    This parameter must be specified when creating a mixed instances policy.

    - **LaunchTemplateSpecification** *(dict) --*

      The launch template to use. You must specify either the launch template ID or launch template
      name in the request.

      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template name.

      - **LaunchTemplateName** *(string) --*

        The name of the launch template. You must specify either a template name or a template ID.

      - **Version** *(string) --*

        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon
        EC2 Auto Scaling selects the latest version of the launch template when launching
        instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default
        version of the launch template when launching instances. The default value is ``$Default`` .

    - **Overrides** *(list) --*

      An optional setting. Any parameters that you specify override the same parameters in the
      launch template. Currently, the only supported override is instance type. You can specify
      between 1 and 20 instance types.

      - *(dict) --*

        Describes an override for a launch template.

        - **InstanceType** *(string) --*

          The instance type.

          For information about available instance types, see `Available Instance Types
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
          in the *Amazon Elastic Compute Cloud User Guide.*

        - **WeightedCapacity** *(string) --*

          The number of capacity units, which gives the instance type a proportional weight to
          other instance types. For example, larger instance types are generally weighted more than
          smaller instance types. These are the same units that you chose to set the desired
          capacity in terms of instances, or a performance attribute such as vCPUs, memory, or I/O.

          Valid Range: Minimum value of 1. Maximum value of 999.
    """


_ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef = TypedDict(
    "_ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)


class ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef(
    _ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef
):
    """
    Type definition for `ClientCreateAutoScalingGroup` `MixedInstancesPolicy`

    An embedded object that specifies a mixed instances policy. The required parameters must be
    specified. If optional parameters are unspecified, their default values are used.

    The policy includes parameters that not only define the distribution of On-Demand Instances and
    Spot Instances, the maximum price to pay for Spot Instances, and how the Auto Scaling group
    allocates instance types to fulfill On-Demand and Spot capacity, but also the parameters that
    specify the instance configuration information—the launch template and instance types.

    For more information, see `MixedInstancesPolicy
    <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_MixedInstancesPolicy.html>`__ in
    the *Amazon EC2 Auto Scaling API Reference* and `Auto Scaling Groups with Multiple Instance Types
    and Purchase Options
    <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html>`__ in the
    *Amazon EC2 Auto Scaling User Guide* .

    You must specify one of the following parameters in your request: ``LaunchConfigurationName`` ,
    ``LaunchTemplate`` , ``InstanceId`` , or ``MixedInstancesPolicy`` .

    - **LaunchTemplate** *(dict) --*

      The launch template and instance types (overrides).

      This parameter must be specified when creating a mixed instances policy.

      - **LaunchTemplateSpecification** *(dict) --*

        The launch template to use. You must specify either the launch template ID or launch template
        name in the request.

        - **LaunchTemplateId** *(string) --*

          The ID of the launch template. You must specify either a template ID or a template name.

        - **LaunchTemplateName** *(string) --*

          The name of the launch template. You must specify either a template name or a template ID.

        - **Version** *(string) --*

          The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon
          EC2 Auto Scaling selects the latest version of the launch template when launching
          instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default
          version of the launch template when launching instances. The default value is ``$Default`` .

      - **Overrides** *(list) --*

        An optional setting. Any parameters that you specify override the same parameters in the
        launch template. Currently, the only supported override is instance type. You can specify
        between 1 and 20 instance types.

        - *(dict) --*

          Describes an override for a launch template.

          - **InstanceType** *(string) --*

            The instance type.

            For information about available instance types, see `Available Instance Types
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
            in the *Amazon Elastic Compute Cloud User Guide.*

          - **WeightedCapacity** *(string) --*

            The number of capacity units, which gives the instance type a proportional weight to
            other instance types. For example, larger instance types are generally weighted more than
            smaller instance types. These are the same units that you chose to set the desired
            capacity in terms of instances, or a performance attribute such as vCPUs, memory, or I/O.

            Valid Range: Minimum value of 1. Maximum value of 999.

    - **InstancesDistribution** *(dict) --*

      The instances distribution to use.

      If you leave this parameter unspecified, the value for each parameter in
      ``InstancesDistribution`` uses a default value.

      - **OnDemandAllocationStrategy** *(string) --*

        Indicates how to allocate instance types to fulfill On-Demand capacity.

        The only valid value is ``prioritized`` , which is also the default value. This strategy uses
        the order of instance type overrides for the  LaunchTemplate to define the launch priority of
        each instance type. The first instance type in the array is prioritized higher than the last.
        If all your On-Demand capacity cannot be fulfilled using your highest priority instance, then
        the Auto Scaling groups launches the remaining capacity using the second priority instance
        type, and so on.

      - **OnDemandBaseCapacity** *(integer) --*

        The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand
        Instances. This base portion is provisioned first as your group scales.

        Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched as a
        percentage of the Auto Scaling group's desired capacity, per the
        ``OnDemandPercentageAboveBaseCapacity`` setting.

        .. note::

          An update to this setting means a gradual replacement of instances to maintain the
          specified number of On-Demand Instances for your base capacity. When replacing instances,
          Amazon EC2 Auto Scaling launches new instances before terminating the old ones.

      - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

        Controls the percentages of On-Demand Instances and Spot Instances for your additional
        capacity beyond ``OnDemandBaseCapacity`` .

        Default if not set is 100. If you leave it set to 100, the percentages are 100% for On-Demand
        Instances and 0% for Spot Instances.

        .. note::

          An update to this setting means a gradual replacement of instances to maintain the
          percentage of On-Demand Instances for your additional capacity above the base capacity.
          When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating
          the old ones.

        Valid Range: Minimum value of 0. Maximum value of 100.

      - **SpotAllocationStrategy** *(string) --*

        Indicates how to allocate instances across Spot Instance pools.

        If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches instances
        using the Spot pools with the lowest price, and evenly allocates your instances across the
        number of Spot pools that you specify. If the allocation strategy is ``capacity-optimized`` ,
        the Auto Scaling group launches instances using Spot pools that are optimally chosen based on
        the available Spot capacity.

        The default Spot allocation strategy for calls that you make through the API, the AWS CLI, or
        the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for the AWS
        Management Console is ``capacity-optimized`` .

        Valid values: ``lowest-price`` | ``capacity-optimized``

      - **SpotInstancePools** *(integer) --*

        The number of Spot Instance pools across which to allocate your Spot Instances. The Spot
        pools are determined from the different instance types in the Overrides array of
        LaunchTemplate . Default if not set is 2.

        Used only when the Spot allocation strategy is ``lowest-price`` .

        Valid Range: Minimum value of 1. Maximum value of 20.

      - **SpotMaxPrice** *(string) --*

        The maximum price per unit hour that you are willing to pay for a Spot Instance. If you leave
        the value of this parameter blank (which is the default), the maximum Spot price is set at
        the On-Demand price.

        To remove a value that you previously set, include the parameter but leave the value blank.
    """


_RequiredClientCreateAutoScalingGroupTagsTypeDef = TypedDict(
    "_RequiredClientCreateAutoScalingGroupTagsTypeDef", {"Key": str}
)
_OptionalClientCreateAutoScalingGroupTagsTypeDef = TypedDict(
    "_OptionalClientCreateAutoScalingGroupTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class ClientCreateAutoScalingGroupTagsTypeDef(
    _RequiredClientCreateAutoScalingGroupTagsTypeDef,
    _OptionalClientCreateAutoScalingGroupTagsTypeDef,
):
    """
    Type definition for `ClientCreateAutoScalingGroup` `Tags`

    Describes a tag for an Auto Scaling group.

    - **ResourceId** *(string) --*

      The name of the group.

    - **ResourceType** *(string) --*

      The type of resource. The only supported value is ``auto-scaling-group`` .

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --*

      The tag value.

    - **PropagateAtLaunch** *(boolean) --*

      Determines whether the tag is added to new instances as they are launched in the group.
    """


_ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef = TypedDict(
    "_ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef(
    _ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef
):
    """
    Type definition for `ClientCreateLaunchConfigurationBlockDeviceMappings` `Ebs`

    The information about the Amazon EBS volume.

    - **SnapshotId** *(string) --*

      The snapshot ID of the volume to use.

      Conditional: This parameter is optional if you specify a volume size. If you specify both
      ``SnapshotId`` and ``VolumeSize`` , ``VolumeSize`` must be equal or greater than the size
      of the snapshot.

    - **VolumeSize** *(integer) --*

      The volume size, in Gibibytes (GiB).

      This can be a number from 1-1,024 for ``standard`` , 4-16,384 for ``io1`` , 1-16,384 for
      ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a snapshot, the volume
      size must be equal to or larger than the snapshot size.

      Default: If you create a volume from a snapshot and you don't specify a volume size, the
      default is the snapshot size.

      .. note::

        At least one of VolumeSize or SnapshotId is required.

    - **VolumeType** *(string) --*

      The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned IOPS SSD,
      ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or ``sc1`` for Cold
      HDD. For more information, see `Amazon EBS Volume Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon
      EC2 User Guide for Linux Instances* .

      Valid Values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``

    - **DeleteOnTermination** *(boolean) --*

      Indicates whether the volume is deleted on instance termination. For Amazon EC2 Auto
      Scaling, the default value is ``true`` .

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) to provision for the volume. The maximum
      ratio of IOPS to volume size (in GiB) is 50:1. For more information, see `Amazon EBS Volume
      Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

      Conditional: This parameter is required when the volume type is ``io1`` . (Not used with
      ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.)

    - **Encrypted** *(boolean) --*

      Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be
      attached to instances that support Amazon EBS encryption. For more information, see
      `Supported Instance Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances>`__
      . If your AMI uses encrypted volumes, you can also only launch it on supported instance
      types.

      .. note::

        If you are creating a volume from a snapshot, you cannot specify an encryption value.
        Volumes that are created from encrypted snapshots are automatically encrypted, and
        volumes that are created from unencrypted snapshots are automatically unencrypted. By
        default, encrypted snapshots use the AWS managed CMK that is used for EBS encryption, but
        you can specify a custom CMK when you create the snapshot. The ability to encrypt a
        snapshot during copying also allows you to apply a new CMK to an already-encrypted
        snapshot. Volumes restored from the resulting copy are only accessible using the new CMK.

        Enabling `encryption by default
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default>`__
        results in all EBS volumes being encrypted with the AWS managed CMK or a customer managed
        CMK, whether or not the snapshot was encrypted.

      For more information, see `Using Encryption with EBS-Backed AMIs
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html>`__ in the *Amazon
      EC2 User Guide for Linux Instances* and `Required CMK Key Policy for Use with Encrypted
      Volumes
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html>`__
      in the *Amazon EC2 Auto Scaling User Guide* .
    """


_RequiredClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef = TypedDict(
    "_RequiredClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef",
    {"DeviceName": str},
)
_OptionalClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef = TypedDict(
    "_OptionalClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "Ebs": ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)


class ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef(
    _RequiredClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef,
    _OptionalClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef,
):
    """
    Type definition for `ClientCreateLaunchConfiguration` `BlockDeviceMappings`

    Describes a block device mapping.

    - **VirtualName** *(string) --*

      The name of the virtual device (for example, ``ephemeral0`` ).

    - **DeviceName** *(string) --* **[REQUIRED]**

      The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ). For
      more information, see `Device Naming on Linux Instances
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html>`__ in the *Amazon
      EC2 User Guide for Linux Instances* .

    - **Ebs** *(dict) --*

      The information about the Amazon EBS volume.

      - **SnapshotId** *(string) --*

        The snapshot ID of the volume to use.

        Conditional: This parameter is optional if you specify a volume size. If you specify both
        ``SnapshotId`` and ``VolumeSize`` , ``VolumeSize`` must be equal or greater than the size
        of the snapshot.

      - **VolumeSize** *(integer) --*

        The volume size, in Gibibytes (GiB).

        This can be a number from 1-1,024 for ``standard`` , 4-16,384 for ``io1`` , 1-16,384 for
        ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a snapshot, the volume
        size must be equal to or larger than the snapshot size.

        Default: If you create a volume from a snapshot and you don't specify a volume size, the
        default is the snapshot size.

        .. note::

          At least one of VolumeSize or SnapshotId is required.

      - **VolumeType** *(string) --*

        The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned IOPS SSD,
        ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or ``sc1`` for Cold
        HDD. For more information, see `Amazon EBS Volume Types
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon
        EC2 User Guide for Linux Instances* .

        Valid Values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``

      - **DeleteOnTermination** *(boolean) --*

        Indicates whether the volume is deleted on instance termination. For Amazon EC2 Auto
        Scaling, the default value is ``true`` .

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) to provision for the volume. The maximum
        ratio of IOPS to volume size (in GiB) is 50:1. For more information, see `Amazon EBS Volume
        Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
        *Amazon EC2 User Guide for Linux Instances* .

        Conditional: This parameter is required when the volume type is ``io1`` . (Not used with
        ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.)

      - **Encrypted** *(boolean) --*

        Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be
        attached to instances that support Amazon EBS encryption. For more information, see
        `Supported Instance Types
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances>`__
        . If your AMI uses encrypted volumes, you can also only launch it on supported instance
        types.

        .. note::

          If you are creating a volume from a snapshot, you cannot specify an encryption value.
          Volumes that are created from encrypted snapshots are automatically encrypted, and
          volumes that are created from unencrypted snapshots are automatically unencrypted. By
          default, encrypted snapshots use the AWS managed CMK that is used for EBS encryption, but
          you can specify a custom CMK when you create the snapshot. The ability to encrypt a
          snapshot during copying also allows you to apply a new CMK to an already-encrypted
          snapshot. Volumes restored from the resulting copy are only accessible using the new CMK.

          Enabling `encryption by default
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default>`__
          results in all EBS volumes being encrypted with the AWS managed CMK or a customer managed
          CMK, whether or not the snapshot was encrypted.

        For more information, see `Using Encryption with EBS-Backed AMIs
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html>`__ in the *Amazon
        EC2 User Guide for Linux Instances* and `Required CMK Key Policy for Use with Encrypted
        Volumes
        <https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html>`__
        in the *Amazon EC2 Auto Scaling User Guide* .

    - **NoDevice** *(boolean) --*

      Suppresses a device mapping.

      If this parameter is true for the root device, the instance might fail the EC2 health check.
      In that case, Amazon EC2 Auto Scaling launches a replacement instance.
    """


_ClientCreateLaunchConfigurationInstanceMonitoringTypeDef = TypedDict(
    "_ClientCreateLaunchConfigurationInstanceMonitoringTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientCreateLaunchConfigurationInstanceMonitoringTypeDef(
    _ClientCreateLaunchConfigurationInstanceMonitoringTypeDef
):
    """
    Type definition for `ClientCreateLaunchConfiguration` `InstanceMonitoring`

    Controls whether instances in this group are launched with detailed (``true`` ) or basic
    (``false`` ) monitoring.

    The default value is ``true`` (enabled).

    .. warning::

      When detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your
      account is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics
      every 5 minutes. For more information, see `Configure Monitoring for Auto Scaling Instances
      <https://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html#enable-as-instance-metrics>`__
      in the *Amazon EC2 Auto Scaling User Guide* .

    - **Enabled** *(boolean) --*

      If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
    """


_RequiredClientCreateOrUpdateTagsTagsTypeDef = TypedDict(
    "_RequiredClientCreateOrUpdateTagsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateOrUpdateTagsTagsTypeDef = TypedDict(
    "_OptionalClientCreateOrUpdateTagsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class ClientCreateOrUpdateTagsTagsTypeDef(
    _RequiredClientCreateOrUpdateTagsTagsTypeDef,
    _OptionalClientCreateOrUpdateTagsTagsTypeDef,
):
    """
    Type definition for `ClientCreateOrUpdateTags` `Tags`

    Describes a tag for an Auto Scaling group.

    - **ResourceId** *(string) --*

      The name of the group.

    - **ResourceType** *(string) --*

      The type of resource. The only supported value is ``auto-scaling-group`` .

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --*

      The tag value.

    - **PropagateAtLaunch** *(boolean) --*

      Determines whether the tag is added to new instances as they are launched in the group.
    """


_RequiredClientDeleteTagsTagsTypeDef = TypedDict(
    "_RequiredClientDeleteTagsTagsTypeDef", {"Key": str}
)
_OptionalClientDeleteTagsTagsTypeDef = TypedDict(
    "_OptionalClientDeleteTagsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)


class ClientDeleteTagsTagsTypeDef(
    _RequiredClientDeleteTagsTagsTypeDef, _OptionalClientDeleteTagsTagsTypeDef
):
    """
    Type definition for `ClientDeleteTags` `Tags`

    Describes a tag for an Auto Scaling group.

    - **ResourceId** *(string) --*

      The name of the group.

    - **ResourceType** *(string) --*

      The type of resource. The only supported value is ``auto-scaling-group`` .

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --*

      The tag value.

    - **PropagateAtLaunch** *(boolean) --*

      Determines whether the tag is added to new instances as they are launched in the group.
    """


_ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeAccountLimitsResponseTypeDef",
    {
        "MaxNumberOfAutoScalingGroups": int,
        "MaxNumberOfLaunchConfigurations": int,
        "NumberOfAutoScalingGroups": int,
        "NumberOfLaunchConfigurations": int,
    },
    total=False,
)


class ClientDescribeAccountLimitsResponseTypeDef(
    _ClientDescribeAccountLimitsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAccountLimits` `Response`

    - **MaxNumberOfAutoScalingGroups** *(integer) --*

      The maximum number of groups allowed for your AWS account. The default limit is 200 per AWS
      Region.

    - **MaxNumberOfLaunchConfigurations** *(integer) --*

      The maximum number of launch configurations allowed for your AWS account. The default limit
      is 200 per AWS Region.

    - **NumberOfAutoScalingGroups** *(integer) --*

      The current number of groups for your AWS account.

    - **NumberOfLaunchConfigurations** *(integer) --*

      The current number of launch configurations for your AWS account.
    """


_ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef = TypedDict(
    "_ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef",
    {"AdjustmentType": str},
    total=False,
)


class ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef(
    _ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef
):
    """
    Type definition for `ClientDescribeAdjustmentTypesResponse` `AdjustmentTypes`

    Describes a policy adjustment type.

    - **AdjustmentType** *(string) --*

      The policy adjustment type. The valid values are ``ChangeInCapacity`` , ``ExactCapacity``
      , and ``PercentChangeInCapacity`` .
    """


_ClientDescribeAdjustmentTypesResponseTypeDef = TypedDict(
    "_ClientDescribeAdjustmentTypesResponseTypeDef",
    {
        "AdjustmentTypes": List[
            ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeAdjustmentTypesResponseTypeDef(
    _ClientDescribeAdjustmentTypesResponseTypeDef
):
    """
    Type definition for `ClientDescribeAdjustmentTypes` `Response`

    - **AdjustmentTypes** *(list) --*

      The policy adjustment types.

      - *(dict) --*

        Describes a policy adjustment type.

        - **AdjustmentType** *(string) --*

          The policy adjustment type. The valid values are ``ChangeInCapacity`` , ``ExactCapacity``
          , and ``PercentChangeInCapacity`` .
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef",
    {"Metric": str, "Granularity": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroups` `EnabledMetrics`

    Describes an enabled metric.

    - **Metric** *(string) --*

      One of the following metrics:

      * ``GroupMinSize``

      * ``GroupMaxSize``

      * ``GroupDesiredCapacity``

      * ``GroupInServiceInstances``

      * ``GroupPendingInstances``

      * ``GroupStandbyInstances``

      * ``GroupTerminatingInstances``

      * ``GroupTotalInstances``

    - **Granularity** *(string) --*

      The granularity of the metric. The only valid value is ``1Minute`` .
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstances` `LaunchTemplate`

    The launch template for the instance.

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template
      name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a
      template ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
      Amazon EC2 Auto Scaling selects the latest version of the launch template when
      launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
      the default version of the launch template when launching instances. The default
      value is ``$Default`` .
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef,
        "ProtectedFromScaleIn": bool,
        "WeightedCapacity": str,
    },
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroups` `Instances`

    Describes an EC2 instance.

    - **InstanceId** *(string) --*

      The ID of the instance.

    - **InstanceType** *(string) --*

      The instance type of the EC2 instance.

    - **AvailabilityZone** *(string) --*

      The Availability Zone in which the instance is running.

    - **LifecycleState** *(string) --*

      A description of the current lifecycle state. The ``Quarantined`` state is not used.

    - **HealthStatus** *(string) --*

      The last reported health status of the instance. "Healthy" means that the instance is
      healthy and should remain in service. "Unhealthy" means that the instance is
      unhealthy and that Amazon EC2 Auto Scaling should terminate and replace it.

    - **LaunchConfigurationName** *(string) --*

      The launch configuration associated with the instance.

    - **LaunchTemplate** *(dict) --*

      The launch template for the instance.

      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template
        name.

      - **LaunchTemplateName** *(string) --*

        The name of the launch template. You must specify either a template name or a
        template ID.

      - **Version** *(string) --*

        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
        Amazon EC2 Auto Scaling selects the latest version of the launch template when
        launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
        the default version of the launch template when launching instances. The default
        value is ``$Default`` .

    - **ProtectedFromScaleIn** *(boolean) --*

      Indicates whether the instance is protected from termination by Amazon EC2 Auto
      Scaling when scaling in.

    - **WeightedCapacity** *(string) --*

      The number of capacity units contributed by the instance based on its instance type.

      Valid Range: Minimum value of 1. Maximum value of 999.
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroups` `LaunchTemplate`

    The launch template for the group.

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a template
      ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
      Amazon EC2 Auto Scaling selects the latest version of the launch template when
      launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
      default version of the launch template when launching instances. The default value is
      ``$Default`` .
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicy` `InstancesDistribution`

    The instances distribution to use.

    If you leave this parameter unspecified, the value for each parameter in
    ``InstancesDistribution`` uses a default value.

    - **OnDemandAllocationStrategy** *(string) --*

      Indicates how to allocate instance types to fulfill On-Demand capacity.

      The only valid value is ``prioritized`` , which is also the default value. This
      strategy uses the order of instance type overrides for the  LaunchTemplate to define
      the launch priority of each instance type. The first instance type in the array is
      prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled
      using your highest priority instance, then the Auto Scaling groups launches the
      remaining capacity using the second priority instance type, and so on.

    - **OnDemandBaseCapacity** *(integer) --*

      The minimum amount of the Auto Scaling group's capacity that must be fulfilled by
      On-Demand Instances. This base portion is provisioned first as your group scales.

      Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched
      as a percentage of the Auto Scaling group's desired capacity, per the
      ``OnDemandPercentageAboveBaseCapacity`` setting.

      .. note::

        An update to this setting means a gradual replacement of instances to maintain the
        specified number of On-Demand Instances for your base capacity. When replacing
        instances, Amazon EC2 Auto Scaling launches new instances before terminating the
        old ones.

    - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

      Controls the percentages of On-Demand Instances and Spot Instances for your
      additional capacity beyond ``OnDemandBaseCapacity`` .

      Default if not set is 100. If you leave it set to 100, the percentages are 100% for
      On-Demand Instances and 0% for Spot Instances.

      .. note::

        An update to this setting means a gradual replacement of instances to maintain the
        percentage of On-Demand Instances for your additional capacity above the base
        capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances
        before terminating the old ones.

      Valid Range: Minimum value of 0. Maximum value of 100.

    - **SpotAllocationStrategy** *(string) --*

      Indicates how to allocate instances across Spot Instance pools.

      If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches
      instances using the Spot pools with the lowest price, and evenly allocates your
      instances across the number of Spot pools that you specify. If the allocation
      strategy is ``capacity-optimized`` , the Auto Scaling group launches instances using
      Spot pools that are optimally chosen based on the available Spot capacity.

      The default Spot allocation strategy for calls that you make through the API, the AWS
      CLI, or the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for
      the AWS Management Console is ``capacity-optimized`` .

      Valid values: ``lowest-price`` | ``capacity-optimized``

    - **SpotInstancePools** *(integer) --*

      The number of Spot Instance pools across which to allocate your Spot Instances. The
      Spot pools are determined from the different instance types in the Overrides array of
       LaunchTemplate . Default if not set is 2.

      Used only when the Spot allocation strategy is ``lowest-price`` .

      Valid Range: Minimum value of 1. Maximum value of 20.

    - **SpotMaxPrice** *(string) --*

      The maximum price per unit hour that you are willing to pay for a Spot Instance. If
      you leave the value of this parameter blank (which is the default), the maximum Spot
      price is set at the On-Demand price.

      To remove a value that you previously set, include the parameter but leave the value
      blank.
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplate` `LaunchTemplateSpecification`

    The launch template to use. You must specify either the launch template ID or launch
    template name in the request.

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template
      name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a
      template ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
      Amazon EC2 Auto Scaling selects the latest version of the launch template when
      launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
      the default version of the launch template when launching instances. The default
      value is ``$Default`` .
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplate` `Overrides`

    Describes an override for a launch template.

    - **InstanceType** *(string) --*

      The instance type.

      For information about available instance types, see `Available Instance Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
      in the *Amazon Elastic Compute Cloud User Guide.*

    - **WeightedCapacity** *(string) --*

      The number of capacity units, which gives the instance type a proportional weight
      to other instance types. For example, larger instance types are generally
      weighted more than smaller instance types. These are the same units that you
      chose to set the desired capacity in terms of instances, or a performance
      attribute such as vCPUs, memory, or I/O.

      Valid Range: Minimum value of 1. Maximum value of 999.
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicy` `LaunchTemplate`

    The launch template and instance types (overrides).

    This parameter must be specified when creating a mixed instances policy.

    - **LaunchTemplateSpecification** *(dict) --*

      The launch template to use. You must specify either the launch template ID or launch
      template name in the request.

      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template
        name.

      - **LaunchTemplateName** *(string) --*

        The name of the launch template. You must specify either a template name or a
        template ID.

      - **Version** *(string) --*

        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
        Amazon EC2 Auto Scaling selects the latest version of the launch template when
        launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
        the default version of the launch template when launching instances. The default
        value is ``$Default`` .

    - **Overrides** *(list) --*

      An optional setting. Any parameters that you specify override the same parameters in
      the launch template. Currently, the only supported override is instance type. You can
      specify between 1 and 20 instance types.

      - *(dict) --*

        Describes an override for a launch template.

        - **InstanceType** *(string) --*

          The instance type.

          For information about available instance types, see `Available Instance Types
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
          in the *Amazon Elastic Compute Cloud User Guide.*

        - **WeightedCapacity** *(string) --*

          The number of capacity units, which gives the instance type a proportional weight
          to other instance types. For example, larger instance types are generally
          weighted more than smaller instance types. These are the same units that you
          chose to set the desired capacity in terms of instances, or a performance
          attribute such as vCPUs, memory, or I/O.

          Valid Range: Minimum value of 1. Maximum value of 999.
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroups` `MixedInstancesPolicy`

    The mixed instances policy for the group.

    - **LaunchTemplate** *(dict) --*

      The launch template and instance types (overrides).

      This parameter must be specified when creating a mixed instances policy.

      - **LaunchTemplateSpecification** *(dict) --*

        The launch template to use. You must specify either the launch template ID or launch
        template name in the request.

        - **LaunchTemplateId** *(string) --*

          The ID of the launch template. You must specify either a template ID or a template
          name.

        - **LaunchTemplateName** *(string) --*

          The name of the launch template. You must specify either a template name or a
          template ID.

        - **Version** *(string) --*

          The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
          Amazon EC2 Auto Scaling selects the latest version of the launch template when
          launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
          the default version of the launch template when launching instances. The default
          value is ``$Default`` .

      - **Overrides** *(list) --*

        An optional setting. Any parameters that you specify override the same parameters in
        the launch template. Currently, the only supported override is instance type. You can
        specify between 1 and 20 instance types.

        - *(dict) --*

          Describes an override for a launch template.

          - **InstanceType** *(string) --*

            The instance type.

            For information about available instance types, see `Available Instance Types
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
            in the *Amazon Elastic Compute Cloud User Guide.*

          - **WeightedCapacity** *(string) --*

            The number of capacity units, which gives the instance type a proportional weight
            to other instance types. For example, larger instance types are generally
            weighted more than smaller instance types. These are the same units that you
            chose to set the desired capacity in terms of instances, or a performance
            attribute such as vCPUs, memory, or I/O.

            Valid Range: Minimum value of 1. Maximum value of 999.

    - **InstancesDistribution** *(dict) --*

      The instances distribution to use.

      If you leave this parameter unspecified, the value for each parameter in
      ``InstancesDistribution`` uses a default value.

      - **OnDemandAllocationStrategy** *(string) --*

        Indicates how to allocate instance types to fulfill On-Demand capacity.

        The only valid value is ``prioritized`` , which is also the default value. This
        strategy uses the order of instance type overrides for the  LaunchTemplate to define
        the launch priority of each instance type. The first instance type in the array is
        prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled
        using your highest priority instance, then the Auto Scaling groups launches the
        remaining capacity using the second priority instance type, and so on.

      - **OnDemandBaseCapacity** *(integer) --*

        The minimum amount of the Auto Scaling group's capacity that must be fulfilled by
        On-Demand Instances. This base portion is provisioned first as your group scales.

        Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched
        as a percentage of the Auto Scaling group's desired capacity, per the
        ``OnDemandPercentageAboveBaseCapacity`` setting.

        .. note::

          An update to this setting means a gradual replacement of instances to maintain the
          specified number of On-Demand Instances for your base capacity. When replacing
          instances, Amazon EC2 Auto Scaling launches new instances before terminating the
          old ones.

      - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

        Controls the percentages of On-Demand Instances and Spot Instances for your
        additional capacity beyond ``OnDemandBaseCapacity`` .

        Default if not set is 100. If you leave it set to 100, the percentages are 100% for
        On-Demand Instances and 0% for Spot Instances.

        .. note::

          An update to this setting means a gradual replacement of instances to maintain the
          percentage of On-Demand Instances for your additional capacity above the base
          capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances
          before terminating the old ones.

        Valid Range: Minimum value of 0. Maximum value of 100.

      - **SpotAllocationStrategy** *(string) --*

        Indicates how to allocate instances across Spot Instance pools.

        If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches
        instances using the Spot pools with the lowest price, and evenly allocates your
        instances across the number of Spot pools that you specify. If the allocation
        strategy is ``capacity-optimized`` , the Auto Scaling group launches instances using
        Spot pools that are optimally chosen based on the available Spot capacity.

        The default Spot allocation strategy for calls that you make through the API, the AWS
        CLI, or the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for
        the AWS Management Console is ``capacity-optimized`` .

        Valid values: ``lowest-price`` | ``capacity-optimized``

      - **SpotInstancePools** *(integer) --*

        The number of Spot Instance pools across which to allocate your Spot Instances. The
        Spot pools are determined from the different instance types in the Overrides array of
         LaunchTemplate . Default if not set is 2.

        Used only when the Spot allocation strategy is ``lowest-price`` .

        Valid Range: Minimum value of 1. Maximum value of 20.

      - **SpotMaxPrice** *(string) --*

        The maximum price per unit hour that you are willing to pay for a Spot Instance. If
        you leave the value of this parameter blank (which is the default), the maximum Spot
        price is set at the On-Demand price.

        To remove a value that you previously set, include the parameter but leave the value
        blank.
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    {"ProcessName": str, "SuspensionReason": str},
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroups` `SuspendedProcesses`

    Describes an automatic scaling process that has been suspended. For more information,
    see  ProcessType .

    - **ProcessName** *(string) --*

      The name of the suspended process.

    - **SuspensionReason** *(string) --*

      The reason that the process was suspended.
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "Key": str,
        "Value": str,
        "PropagateAtLaunch": bool,
    },
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponseAutoScalingGroups` `Tags`

    Describes a tag for an Auto Scaling group.

    - **ResourceId** *(string) --*

      The name of the group.

    - **ResourceType** *(string) --*

      The type of resource. The only supported value is ``auto-scaling-group`` .

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The tag value.

    - **PropagateAtLaunch** *(boolean) --*

      Determines whether the tag is added to new instances as they are launched in the
      group.
    """


_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef",
    {
        "AutoScalingGroupName": str,
        "AutoScalingGroupARN": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef,
        "MixedInstancesPolicy": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "LoadBalancerNames": List[str],
        "TargetGroupARNs": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "Instances": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef
        ],
        "CreatedTime": datetime,
        "SuspendedProcesses": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef
        ],
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "EnabledMetrics": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef
        ],
        "Status": str,
        "Tags": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef
        ],
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
    },
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef(
    _ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroupsResponse` `AutoScalingGroups`

    Describes an Auto Scaling group.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **AutoScalingGroupARN** *(string) --*

      The Amazon Resource Name (ARN) of the Auto Scaling group.

    - **LaunchConfigurationName** *(string) --*

      The name of the associated launch configuration.

    - **LaunchTemplate** *(dict) --*

      The launch template for the group.

      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template name.

      - **LaunchTemplateName** *(string) --*

        The name of the launch template. You must specify either a template name or a template
        ID.

      - **Version** *(string) --*

        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
        Amazon EC2 Auto Scaling selects the latest version of the launch template when
        launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
        default version of the launch template when launching instances. The default value is
        ``$Default`` .

    - **MixedInstancesPolicy** *(dict) --*

      The mixed instances policy for the group.

      - **LaunchTemplate** *(dict) --*

        The launch template and instance types (overrides).

        This parameter must be specified when creating a mixed instances policy.

        - **LaunchTemplateSpecification** *(dict) --*

          The launch template to use. You must specify either the launch template ID or launch
          template name in the request.

          - **LaunchTemplateId** *(string) --*

            The ID of the launch template. You must specify either a template ID or a template
            name.

          - **LaunchTemplateName** *(string) --*

            The name of the launch template. You must specify either a template name or a
            template ID.

          - **Version** *(string) --*

            The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
            Amazon EC2 Auto Scaling selects the latest version of the launch template when
            launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
            the default version of the launch template when launching instances. The default
            value is ``$Default`` .

        - **Overrides** *(list) --*

          An optional setting. Any parameters that you specify override the same parameters in
          the launch template. Currently, the only supported override is instance type. You can
          specify between 1 and 20 instance types.

          - *(dict) --*

            Describes an override for a launch template.

            - **InstanceType** *(string) --*

              The instance type.

              For information about available instance types, see `Available Instance Types
              <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
              in the *Amazon Elastic Compute Cloud User Guide.*

            - **WeightedCapacity** *(string) --*

              The number of capacity units, which gives the instance type a proportional weight
              to other instance types. For example, larger instance types are generally
              weighted more than smaller instance types. These are the same units that you
              chose to set the desired capacity in terms of instances, or a performance
              attribute such as vCPUs, memory, or I/O.

              Valid Range: Minimum value of 1. Maximum value of 999.

      - **InstancesDistribution** *(dict) --*

        The instances distribution to use.

        If you leave this parameter unspecified, the value for each parameter in
        ``InstancesDistribution`` uses a default value.

        - **OnDemandAllocationStrategy** *(string) --*

          Indicates how to allocate instance types to fulfill On-Demand capacity.

          The only valid value is ``prioritized`` , which is also the default value. This
          strategy uses the order of instance type overrides for the  LaunchTemplate to define
          the launch priority of each instance type. The first instance type in the array is
          prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled
          using your highest priority instance, then the Auto Scaling groups launches the
          remaining capacity using the second priority instance type, and so on.

        - **OnDemandBaseCapacity** *(integer) --*

          The minimum amount of the Auto Scaling group's capacity that must be fulfilled by
          On-Demand Instances. This base portion is provisioned first as your group scales.

          Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched
          as a percentage of the Auto Scaling group's desired capacity, per the
          ``OnDemandPercentageAboveBaseCapacity`` setting.

          .. note::

            An update to this setting means a gradual replacement of instances to maintain the
            specified number of On-Demand Instances for your base capacity. When replacing
            instances, Amazon EC2 Auto Scaling launches new instances before terminating the
            old ones.

        - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

          Controls the percentages of On-Demand Instances and Spot Instances for your
          additional capacity beyond ``OnDemandBaseCapacity`` .

          Default if not set is 100. If you leave it set to 100, the percentages are 100% for
          On-Demand Instances and 0% for Spot Instances.

          .. note::

            An update to this setting means a gradual replacement of instances to maintain the
            percentage of On-Demand Instances for your additional capacity above the base
            capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances
            before terminating the old ones.

          Valid Range: Minimum value of 0. Maximum value of 100.

        - **SpotAllocationStrategy** *(string) --*

          Indicates how to allocate instances across Spot Instance pools.

          If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches
          instances using the Spot pools with the lowest price, and evenly allocates your
          instances across the number of Spot pools that you specify. If the allocation
          strategy is ``capacity-optimized`` , the Auto Scaling group launches instances using
          Spot pools that are optimally chosen based on the available Spot capacity.

          The default Spot allocation strategy for calls that you make through the API, the AWS
          CLI, or the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for
          the AWS Management Console is ``capacity-optimized`` .

          Valid values: ``lowest-price`` | ``capacity-optimized``

        - **SpotInstancePools** *(integer) --*

          The number of Spot Instance pools across which to allocate your Spot Instances. The
          Spot pools are determined from the different instance types in the Overrides array of
           LaunchTemplate . Default if not set is 2.

          Used only when the Spot allocation strategy is ``lowest-price`` .

          Valid Range: Minimum value of 1. Maximum value of 20.

        - **SpotMaxPrice** *(string) --*

          The maximum price per unit hour that you are willing to pay for a Spot Instance. If
          you leave the value of this parameter blank (which is the default), the maximum Spot
          price is set at the On-Demand price.

          To remove a value that you previously set, include the parameter but leave the value
          blank.

    - **MinSize** *(integer) --*

      The minimum size of the group.

    - **MaxSize** *(integer) --*

      The maximum size of the group.

    - **DesiredCapacity** *(integer) --*

      The desired size of the group.

    - **DefaultCooldown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes before another scaling
      activity can start.

    - **AvailabilityZones** *(list) --*

      One or more Availability Zones for the group.

      - *(string) --*

    - **LoadBalancerNames** *(list) --*

      One or more load balancers associated with the group.

      - *(string) --*

    - **TargetGroupARNs** *(list) --*

      The Amazon Resource Names (ARN) of the target groups for your load balancer.

      - *(string) --*

    - **HealthCheckType** *(string) --*

      The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` . If
      you configure an Auto Scaling group to use ELB health checks, it considers the instance
      unhealthy if it fails either the EC2 status checks or the load balancer health checks.

    - **HealthCheckGracePeriod** *(integer) --*

      The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the
      health status of an EC2 instance that has come into service.

    - **Instances** *(list) --*

      The EC2 instances associated with the group.

      - *(dict) --*

        Describes an EC2 instance.

        - **InstanceId** *(string) --*

          The ID of the instance.

        - **InstanceType** *(string) --*

          The instance type of the EC2 instance.

        - **AvailabilityZone** *(string) --*

          The Availability Zone in which the instance is running.

        - **LifecycleState** *(string) --*

          A description of the current lifecycle state. The ``Quarantined`` state is not used.

        - **HealthStatus** *(string) --*

          The last reported health status of the instance. "Healthy" means that the instance is
          healthy and should remain in service. "Unhealthy" means that the instance is
          unhealthy and that Amazon EC2 Auto Scaling should terminate and replace it.

        - **LaunchConfigurationName** *(string) --*

          The launch configuration associated with the instance.

        - **LaunchTemplate** *(dict) --*

          The launch template for the instance.

          - **LaunchTemplateId** *(string) --*

            The ID of the launch template. You must specify either a template ID or a template
            name.

          - **LaunchTemplateName** *(string) --*

            The name of the launch template. You must specify either a template name or a
            template ID.

          - **Version** *(string) --*

            The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
            Amazon EC2 Auto Scaling selects the latest version of the launch template when
            launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
            the default version of the launch template when launching instances. The default
            value is ``$Default`` .

        - **ProtectedFromScaleIn** *(boolean) --*

          Indicates whether the instance is protected from termination by Amazon EC2 Auto
          Scaling when scaling in.

        - **WeightedCapacity** *(string) --*

          The number of capacity units contributed by the instance based on its instance type.

          Valid Range: Minimum value of 1. Maximum value of 999.

    - **CreatedTime** *(datetime) --*

      The date and time the group was created.

    - **SuspendedProcesses** *(list) --*

      The suspended processes associated with the group.

      - *(dict) --*

        Describes an automatic scaling process that has been suspended. For more information,
        see  ProcessType .

        - **ProcessName** *(string) --*

          The name of the suspended process.

        - **SuspensionReason** *(string) --*

          The reason that the process was suspended.

    - **PlacementGroup** *(string) --*

      The name of the placement group into which to launch your instances, if any.

    - **VPCZoneIdentifier** *(string) --*

      One or more subnet IDs, if applicable, separated by commas.

    - **EnabledMetrics** *(list) --*

      The metrics enabled for the group.

      - *(dict) --*

        Describes an enabled metric.

        - **Metric** *(string) --*

          One of the following metrics:

          * ``GroupMinSize``

          * ``GroupMaxSize``

          * ``GroupDesiredCapacity``

          * ``GroupInServiceInstances``

          * ``GroupPendingInstances``

          * ``GroupStandbyInstances``

          * ``GroupTerminatingInstances``

          * ``GroupTotalInstances``

        - **Granularity** *(string) --*

          The granularity of the metric. The only valid value is ``1Minute`` .

    - **Status** *(string) --*

      The current state of the group when  DeleteAutoScalingGroup is in progress.

    - **Tags** *(list) --*

      The tags for the group.

      - *(dict) --*

        Describes a tag for an Auto Scaling group.

        - **ResourceId** *(string) --*

          The name of the group.

        - **ResourceType** *(string) --*

          The type of resource. The only supported value is ``auto-scaling-group`` .

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The tag value.

        - **PropagateAtLaunch** *(boolean) --*

          Determines whether the tag is added to new instances as they are launched in the
          group.

    - **TerminationPolicies** *(list) --*

      The termination policies for the group.

      - *(string) --*

    - **NewInstancesProtectedFromScaleIn** *(boolean) --*

      Indicates whether newly launched instances are protected from termination by Amazon EC2
      Auto Scaling when scaling in.

    - **ServiceLinkedRoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group
      uses to call other AWS services on your behalf.

    - **MaxInstanceLifetime** *(integer) --*

      The maximum amount of time, in seconds, that an instance can be in service.

      Valid Range: Minimum value of 604800.
    """


_ClientDescribeAutoScalingGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeAutoScalingGroupsResponseTypeDef",
    {
        "AutoScalingGroups": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAutoScalingGroupsResponseTypeDef(
    _ClientDescribeAutoScalingGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingGroups` `Response`

    - **AutoScalingGroups** *(list) --*

      The groups.

      - *(dict) --*

        Describes an Auto Scaling group.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **AutoScalingGroupARN** *(string) --*

          The Amazon Resource Name (ARN) of the Auto Scaling group.

        - **LaunchConfigurationName** *(string) --*

          The name of the associated launch configuration.

        - **LaunchTemplate** *(dict) --*

          The launch template for the group.

          - **LaunchTemplateId** *(string) --*

            The ID of the launch template. You must specify either a template ID or a template name.

          - **LaunchTemplateName** *(string) --*

            The name of the launch template. You must specify either a template name or a template
            ID.

          - **Version** *(string) --*

            The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
            Amazon EC2 Auto Scaling selects the latest version of the launch template when
            launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
            default version of the launch template when launching instances. The default value is
            ``$Default`` .

        - **MixedInstancesPolicy** *(dict) --*

          The mixed instances policy for the group.

          - **LaunchTemplate** *(dict) --*

            The launch template and instance types (overrides).

            This parameter must be specified when creating a mixed instances policy.

            - **LaunchTemplateSpecification** *(dict) --*

              The launch template to use. You must specify either the launch template ID or launch
              template name in the request.

              - **LaunchTemplateId** *(string) --*

                The ID of the launch template. You must specify either a template ID or a template
                name.

              - **LaunchTemplateName** *(string) --*

                The name of the launch template. You must specify either a template name or a
                template ID.

              - **Version** *(string) --*

                The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
                Amazon EC2 Auto Scaling selects the latest version of the launch template when
                launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
                the default version of the launch template when launching instances. The default
                value is ``$Default`` .

            - **Overrides** *(list) --*

              An optional setting. Any parameters that you specify override the same parameters in
              the launch template. Currently, the only supported override is instance type. You can
              specify between 1 and 20 instance types.

              - *(dict) --*

                Describes an override for a launch template.

                - **InstanceType** *(string) --*

                  The instance type.

                  For information about available instance types, see `Available Instance Types
                  <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
                  in the *Amazon Elastic Compute Cloud User Guide.*

                - **WeightedCapacity** *(string) --*

                  The number of capacity units, which gives the instance type a proportional weight
                  to other instance types. For example, larger instance types are generally
                  weighted more than smaller instance types. These are the same units that you
                  chose to set the desired capacity in terms of instances, or a performance
                  attribute such as vCPUs, memory, or I/O.

                  Valid Range: Minimum value of 1. Maximum value of 999.

          - **InstancesDistribution** *(dict) --*

            The instances distribution to use.

            If you leave this parameter unspecified, the value for each parameter in
            ``InstancesDistribution`` uses a default value.

            - **OnDemandAllocationStrategy** *(string) --*

              Indicates how to allocate instance types to fulfill On-Demand capacity.

              The only valid value is ``prioritized`` , which is also the default value. This
              strategy uses the order of instance type overrides for the  LaunchTemplate to define
              the launch priority of each instance type. The first instance type in the array is
              prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled
              using your highest priority instance, then the Auto Scaling groups launches the
              remaining capacity using the second priority instance type, and so on.

            - **OnDemandBaseCapacity** *(integer) --*

              The minimum amount of the Auto Scaling group's capacity that must be fulfilled by
              On-Demand Instances. This base portion is provisioned first as your group scales.

              Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched
              as a percentage of the Auto Scaling group's desired capacity, per the
              ``OnDemandPercentageAboveBaseCapacity`` setting.

              .. note::

                An update to this setting means a gradual replacement of instances to maintain the
                specified number of On-Demand Instances for your base capacity. When replacing
                instances, Amazon EC2 Auto Scaling launches new instances before terminating the
                old ones.

            - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

              Controls the percentages of On-Demand Instances and Spot Instances for your
              additional capacity beyond ``OnDemandBaseCapacity`` .

              Default if not set is 100. If you leave it set to 100, the percentages are 100% for
              On-Demand Instances and 0% for Spot Instances.

              .. note::

                An update to this setting means a gradual replacement of instances to maintain the
                percentage of On-Demand Instances for your additional capacity above the base
                capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances
                before terminating the old ones.

              Valid Range: Minimum value of 0. Maximum value of 100.

            - **SpotAllocationStrategy** *(string) --*

              Indicates how to allocate instances across Spot Instance pools.

              If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches
              instances using the Spot pools with the lowest price, and evenly allocates your
              instances across the number of Spot pools that you specify. If the allocation
              strategy is ``capacity-optimized`` , the Auto Scaling group launches instances using
              Spot pools that are optimally chosen based on the available Spot capacity.

              The default Spot allocation strategy for calls that you make through the API, the AWS
              CLI, or the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for
              the AWS Management Console is ``capacity-optimized`` .

              Valid values: ``lowest-price`` | ``capacity-optimized``

            - **SpotInstancePools** *(integer) --*

              The number of Spot Instance pools across which to allocate your Spot Instances. The
              Spot pools are determined from the different instance types in the Overrides array of
               LaunchTemplate . Default if not set is 2.

              Used only when the Spot allocation strategy is ``lowest-price`` .

              Valid Range: Minimum value of 1. Maximum value of 20.

            - **SpotMaxPrice** *(string) --*

              The maximum price per unit hour that you are willing to pay for a Spot Instance. If
              you leave the value of this parameter blank (which is the default), the maximum Spot
              price is set at the On-Demand price.

              To remove a value that you previously set, include the parameter but leave the value
              blank.

        - **MinSize** *(integer) --*

          The minimum size of the group.

        - **MaxSize** *(integer) --*

          The maximum size of the group.

        - **DesiredCapacity** *(integer) --*

          The desired size of the group.

        - **DefaultCooldown** *(integer) --*

          The amount of time, in seconds, after a scaling activity completes before another scaling
          activity can start.

        - **AvailabilityZones** *(list) --*

          One or more Availability Zones for the group.

          - *(string) --*

        - **LoadBalancerNames** *(list) --*

          One or more load balancers associated with the group.

          - *(string) --*

        - **TargetGroupARNs** *(list) --*

          The Amazon Resource Names (ARN) of the target groups for your load balancer.

          - *(string) --*

        - **HealthCheckType** *(string) --*

          The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` . If
          you configure an Auto Scaling group to use ELB health checks, it considers the instance
          unhealthy if it fails either the EC2 status checks or the load balancer health checks.

        - **HealthCheckGracePeriod** *(integer) --*

          The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the
          health status of an EC2 instance that has come into service.

        - **Instances** *(list) --*

          The EC2 instances associated with the group.

          - *(dict) --*

            Describes an EC2 instance.

            - **InstanceId** *(string) --*

              The ID of the instance.

            - **InstanceType** *(string) --*

              The instance type of the EC2 instance.

            - **AvailabilityZone** *(string) --*

              The Availability Zone in which the instance is running.

            - **LifecycleState** *(string) --*

              A description of the current lifecycle state. The ``Quarantined`` state is not used.

            - **HealthStatus** *(string) --*

              The last reported health status of the instance. "Healthy" means that the instance is
              healthy and should remain in service. "Unhealthy" means that the instance is
              unhealthy and that Amazon EC2 Auto Scaling should terminate and replace it.

            - **LaunchConfigurationName** *(string) --*

              The launch configuration associated with the instance.

            - **LaunchTemplate** *(dict) --*

              The launch template for the instance.

              - **LaunchTemplateId** *(string) --*

                The ID of the launch template. You must specify either a template ID or a template
                name.

              - **LaunchTemplateName** *(string) --*

                The name of the launch template. You must specify either a template name or a
                template ID.

              - **Version** *(string) --*

                The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
                Amazon EC2 Auto Scaling selects the latest version of the launch template when
                launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
                the default version of the launch template when launching instances. The default
                value is ``$Default`` .

            - **ProtectedFromScaleIn** *(boolean) --*

              Indicates whether the instance is protected from termination by Amazon EC2 Auto
              Scaling when scaling in.

            - **WeightedCapacity** *(string) --*

              The number of capacity units contributed by the instance based on its instance type.

              Valid Range: Minimum value of 1. Maximum value of 999.

        - **CreatedTime** *(datetime) --*

          The date and time the group was created.

        - **SuspendedProcesses** *(list) --*

          The suspended processes associated with the group.

          - *(dict) --*

            Describes an automatic scaling process that has been suspended. For more information,
            see  ProcessType .

            - **ProcessName** *(string) --*

              The name of the suspended process.

            - **SuspensionReason** *(string) --*

              The reason that the process was suspended.

        - **PlacementGroup** *(string) --*

          The name of the placement group into which to launch your instances, if any.

        - **VPCZoneIdentifier** *(string) --*

          One or more subnet IDs, if applicable, separated by commas.

        - **EnabledMetrics** *(list) --*

          The metrics enabled for the group.

          - *(dict) --*

            Describes an enabled metric.

            - **Metric** *(string) --*

              One of the following metrics:

              * ``GroupMinSize``

              * ``GroupMaxSize``

              * ``GroupDesiredCapacity``

              * ``GroupInServiceInstances``

              * ``GroupPendingInstances``

              * ``GroupStandbyInstances``

              * ``GroupTerminatingInstances``

              * ``GroupTotalInstances``

            - **Granularity** *(string) --*

              The granularity of the metric. The only valid value is ``1Minute`` .

        - **Status** *(string) --*

          The current state of the group when  DeleteAutoScalingGroup is in progress.

        - **Tags** *(list) --*

          The tags for the group.

          - *(dict) --*

            Describes a tag for an Auto Scaling group.

            - **ResourceId** *(string) --*

              The name of the group.

            - **ResourceType** *(string) --*

              The type of resource. The only supported value is ``auto-scaling-group`` .

            - **Key** *(string) --*

              The tag key.

            - **Value** *(string) --*

              The tag value.

            - **PropagateAtLaunch** *(boolean) --*

              Determines whether the tag is added to new instances as they are launched in the
              group.

        - **TerminationPolicies** *(list) --*

          The termination policies for the group.

          - *(string) --*

        - **NewInstancesProtectedFromScaleIn** *(boolean) --*

          Indicates whether newly launched instances are protected from termination by Amazon EC2
          Auto Scaling when scaling in.

        - **ServiceLinkedRoleARN** *(string) --*

          The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group
          uses to call other AWS services on your behalf.

        - **MaxInstanceLifetime** *(integer) --*

          The maximum amount of time, in seconds, that an instance can be in service.

          Valid Range: Minimum value of 604800.

    - **NextToken** *(string) --*

      A string that indicates that the response contains more items than can be returned in a
      single response. To receive additional items, specify this string for the ``NextToken`` value
      when requesting the next set of items. This value is null when there are no more items to
      return.
    """


_ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef = TypedDict(
    "_ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef(
    _ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingInstancesResponseAutoScalingInstances` `LaunchTemplate`

    The launch template for the instance.

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a template
      ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
      Amazon EC2 Auto Scaling selects the latest version of the launch template when
      launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
      default version of the launch template when launching instances. The default value is
      ``$Default`` .
    """


_ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef = TypedDict(
    "_ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "AutoScalingGroupName": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef,
        "ProtectedFromScaleIn": bool,
        "WeightedCapacity": str,
    },
    total=False,
)


class ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef(
    _ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingInstancesResponse` `AutoScalingInstances`

    Describes an EC2 instance associated with an Auto Scaling group.

    - **InstanceId** *(string) --*

      The ID of the instance.

    - **InstanceType** *(string) --*

      The instance type of the EC2 instance.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group for the instance.

    - **AvailabilityZone** *(string) --*

      The Availability Zone for the instance.

    - **LifecycleState** *(string) --*

      The lifecycle state for the instance.

    - **HealthStatus** *(string) --*

      The last reported health status of this instance. "Healthy" means that the instance is
      healthy and should remain in service. "Unhealthy" means that the instance is unhealthy
      and Amazon EC2 Auto Scaling should terminate and replace it.

    - **LaunchConfigurationName** *(string) --*

      The launch configuration used to launch the instance. This value is not available if you
      attached the instance to the Auto Scaling group.

    - **LaunchTemplate** *(dict) --*

      The launch template for the instance.

      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template name.

      - **LaunchTemplateName** *(string) --*

        The name of the launch template. You must specify either a template name or a template
        ID.

      - **Version** *(string) --*

        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
        Amazon EC2 Auto Scaling selects the latest version of the launch template when
        launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
        default version of the launch template when launching instances. The default value is
        ``$Default`` .

    - **ProtectedFromScaleIn** *(boolean) --*

      Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling
      when scaling in.

    - **WeightedCapacity** *(string) --*

      The number of capacity units contributed by the instance based on its instance type.

      Valid Range: Minimum value of 1. Maximum value of 999.
    """


_ClientDescribeAutoScalingInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeAutoScalingInstancesResponseTypeDef",
    {
        "AutoScalingInstances": List[
            ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAutoScalingInstancesResponseTypeDef(
    _ClientDescribeAutoScalingInstancesResponseTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingInstances` `Response`

    - **AutoScalingInstances** *(list) --*

      The instances.

      - *(dict) --*

        Describes an EC2 instance associated with an Auto Scaling group.

        - **InstanceId** *(string) --*

          The ID of the instance.

        - **InstanceType** *(string) --*

          The instance type of the EC2 instance.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group for the instance.

        - **AvailabilityZone** *(string) --*

          The Availability Zone for the instance.

        - **LifecycleState** *(string) --*

          The lifecycle state for the instance.

        - **HealthStatus** *(string) --*

          The last reported health status of this instance. "Healthy" means that the instance is
          healthy and should remain in service. "Unhealthy" means that the instance is unhealthy
          and Amazon EC2 Auto Scaling should terminate and replace it.

        - **LaunchConfigurationName** *(string) --*

          The launch configuration used to launch the instance. This value is not available if you
          attached the instance to the Auto Scaling group.

        - **LaunchTemplate** *(dict) --*

          The launch template for the instance.

          - **LaunchTemplateId** *(string) --*

            The ID of the launch template. You must specify either a template ID or a template name.

          - **LaunchTemplateName** *(string) --*

            The name of the launch template. You must specify either a template name or a template
            ID.

          - **Version** *(string) --*

            The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
            Amazon EC2 Auto Scaling selects the latest version of the launch template when
            launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
            default version of the launch template when launching instances. The default value is
            ``$Default`` .

        - **ProtectedFromScaleIn** *(boolean) --*

          Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling
          when scaling in.

        - **WeightedCapacity** *(string) --*

          The number of capacity units contributed by the instance based on its instance type.

          Valid Range: Minimum value of 1. Maximum value of 999.

    - **NextToken** *(string) --*

      A string that indicates that the response contains more items than can be returned in a
      single response. To receive additional items, specify this string for the ``NextToken`` value
      when requesting the next set of items. This value is null when there are no more items to
      return.
    """


_ClientDescribeAutoScalingNotificationTypesResponseTypeDef = TypedDict(
    "_ClientDescribeAutoScalingNotificationTypesResponseTypeDef",
    {"AutoScalingNotificationTypes": List[str]},
    total=False,
)


class ClientDescribeAutoScalingNotificationTypesResponseTypeDef(
    _ClientDescribeAutoScalingNotificationTypesResponseTypeDef
):
    """
    Type definition for `ClientDescribeAutoScalingNotificationTypes` `Response`

    - **AutoScalingNotificationTypes** *(list) --*

      The notification types.

      - *(string) --*
    """


_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef = TypedDict(
    "_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef(
    _ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef
):
    """
    Type definition for `ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappings` `Ebs`

    The information about the Amazon EBS volume.

    - **SnapshotId** *(string) --*

      The snapshot ID of the volume to use.

      Conditional: This parameter is optional if you specify a volume size. If you
      specify both ``SnapshotId`` and ``VolumeSize`` , ``VolumeSize`` must be equal or
      greater than the size of the snapshot.

    - **VolumeSize** *(integer) --*

      The volume size, in Gibibytes (GiB).

      This can be a number from 1-1,024 for ``standard`` , 4-16,384 for ``io1`` ,
      1-16,384 for ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a
      snapshot, the volume size must be equal to or larger than the snapshot size.

      Default: If you create a volume from a snapshot and you don't specify a volume
      size, the default is the snapshot size.

      .. note::

        At least one of VolumeSize or SnapshotId is required.

    - **VolumeType** *(string) --*

      The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned
      IOPS SSD, ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or
      ``sc1`` for Cold HDD. For more information, see `Amazon EBS Volume Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

      Valid Values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``

    - **DeleteOnTermination** *(boolean) --*

      Indicates whether the volume is deleted on instance termination. For Amazon EC2
      Auto Scaling, the default value is ``true`` .

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) to provision for the volume. The
      maximum ratio of IOPS to volume size (in GiB) is 50:1. For more information, see
      `Amazon EBS Volume Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

      Conditional: This parameter is required when the volume type is ``io1`` . (Not used
      with ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.)

    - **Encrypted** *(boolean) --*

      Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be
      attached to instances that support Amazon EBS encryption. For more information, see
      `Supported Instance Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances>`__
      . If your AMI uses encrypted volumes, you can also only launch it on supported
      instance types.

      .. note::

        If you are creating a volume from a snapshot, you cannot specify an encryption
        value. Volumes that are created from encrypted snapshots are automatically
        encrypted, and volumes that are created from unencrypted snapshots are
        automatically unencrypted. By default, encrypted snapshots use the AWS managed
        CMK that is used for EBS encryption, but you can specify a custom CMK when you
        create the snapshot. The ability to encrypt a snapshot during copying also allows
        you to apply a new CMK to an already-encrypted snapshot. Volumes restored from
        the resulting copy are only accessible using the new CMK.

        Enabling `encryption by default
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default>`__
        results in all EBS volumes being encrypted with the AWS managed CMK or a customer
        managed CMK, whether or not the snapshot was encrypted.

      For more information, see `Using Encryption with EBS-Backed AMIs
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* and `Required CMK Key Policy for Use
      with Encrypted Volumes
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html>`__
      in the *Amazon EC2 Auto Scaling User Guide* .
    """


_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef = TypedDict(
    "_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "DeviceName": str,
        "Ebs": ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)


class ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef(
    _ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef
):
    """
    Type definition for `ClientDescribeLaunchConfigurationsResponseLaunchConfigurations` `BlockDeviceMappings`

    Describes a block device mapping.

    - **VirtualName** *(string) --*

      The name of the virtual device (for example, ``ephemeral0`` ).

    - **DeviceName** *(string) --*

      The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ).
      For more information, see `Device Naming on Linux Instances
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

    - **Ebs** *(dict) --*

      The information about the Amazon EBS volume.

      - **SnapshotId** *(string) --*

        The snapshot ID of the volume to use.

        Conditional: This parameter is optional if you specify a volume size. If you
        specify both ``SnapshotId`` and ``VolumeSize`` , ``VolumeSize`` must be equal or
        greater than the size of the snapshot.

      - **VolumeSize** *(integer) --*

        The volume size, in Gibibytes (GiB).

        This can be a number from 1-1,024 for ``standard`` , 4-16,384 for ``io1`` ,
        1-16,384 for ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a
        snapshot, the volume size must be equal to or larger than the snapshot size.

        Default: If you create a volume from a snapshot and you don't specify a volume
        size, the default is the snapshot size.

        .. note::

          At least one of VolumeSize or SnapshotId is required.

      - **VolumeType** *(string) --*

        The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned
        IOPS SSD, ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or
        ``sc1`` for Cold HDD. For more information, see `Amazon EBS Volume Types
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
        *Amazon EC2 User Guide for Linux Instances* .

        Valid Values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``

      - **DeleteOnTermination** *(boolean) --*

        Indicates whether the volume is deleted on instance termination. For Amazon EC2
        Auto Scaling, the default value is ``true`` .

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) to provision for the volume. The
        maximum ratio of IOPS to volume size (in GiB) is 50:1. For more information, see
        `Amazon EBS Volume Types
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
        *Amazon EC2 User Guide for Linux Instances* .

        Conditional: This parameter is required when the volume type is ``io1`` . (Not used
        with ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.)

      - **Encrypted** *(boolean) --*

        Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be
        attached to instances that support Amazon EBS encryption. For more information, see
        `Supported Instance Types
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances>`__
        . If your AMI uses encrypted volumes, you can also only launch it on supported
        instance types.

        .. note::

          If you are creating a volume from a snapshot, you cannot specify an encryption
          value. Volumes that are created from encrypted snapshots are automatically
          encrypted, and volumes that are created from unencrypted snapshots are
          automatically unencrypted. By default, encrypted snapshots use the AWS managed
          CMK that is used for EBS encryption, but you can specify a custom CMK when you
          create the snapshot. The ability to encrypt a snapshot during copying also allows
          you to apply a new CMK to an already-encrypted snapshot. Volumes restored from
          the resulting copy are only accessible using the new CMK.

          Enabling `encryption by default
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default>`__
          results in all EBS volumes being encrypted with the AWS managed CMK or a customer
          managed CMK, whether or not the snapshot was encrypted.

        For more information, see `Using Encryption with EBS-Backed AMIs
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html>`__ in the
        *Amazon EC2 User Guide for Linux Instances* and `Required CMK Key Policy for Use
        with Encrypted Volumes
        <https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html>`__
        in the *Amazon EC2 Auto Scaling User Guide* .

    - **NoDevice** *(boolean) --*

      Suppresses a device mapping.

      If this parameter is true for the root device, the instance might fail the EC2 health
      check. In that case, Amazon EC2 Auto Scaling launches a replacement instance.
    """


_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef = TypedDict(
    "_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef(
    _ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef
):
    """
    Type definition for `ClientDescribeLaunchConfigurationsResponseLaunchConfigurations` `InstanceMonitoring`

    Controls whether instances in this group are launched with detailed (``true`` ) or basic
    (``false`` ) monitoring.

    For more information, see `Configure Monitoring for Auto Scaling Instances
    <https://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html#enable-as-instance-metrics>`__
    in the *Amazon EC2 Auto Scaling User Guide* .

    - **Enabled** *(boolean) --*

      If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
    """


_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef = TypedDict(
    "_ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef",
    {
        "LaunchConfigurationName": str,
        "LaunchConfigurationARN": str,
        "ImageId": str,
        "KeyName": str,
        "SecurityGroups": List[str],
        "ClassicLinkVPCId": str,
        "ClassicLinkVPCSecurityGroups": List[str],
        "UserData": str,
        "InstanceType": str,
        "KernelId": str,
        "RamdiskId": str,
        "BlockDeviceMappings": List[
            ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef
        ],
        "InstanceMonitoring": ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef,
        "SpotPrice": str,
        "IamInstanceProfile": str,
        "CreatedTime": datetime,
        "EbsOptimized": bool,
        "AssociatePublicIpAddress": bool,
        "PlacementTenancy": str,
    },
    total=False,
)


class ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef(
    _ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeLaunchConfigurationsResponse` `LaunchConfigurations`

    Describes a launch configuration.

    - **LaunchConfigurationName** *(string) --*

      The name of the launch configuration.

    - **LaunchConfigurationARN** *(string) --*

      The Amazon Resource Name (ARN) of the launch configuration.

    - **ImageId** *(string) --*

      The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances.

      For more information, see `Finding an AMI
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

    - **KeyName** *(string) --*

      The name of the key pair.

      For more information, see `Amazon EC2 Key Pairs
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

    - **SecurityGroups** *(list) --*

      A list that contains the security groups to assign to the instances in the Auto Scaling
      group.

      For more information, see `Security Groups for Your VPC
      <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`__ in
      the *Amazon Virtual Private Cloud User Guide* .

      - *(string) --*

    - **ClassicLinkVPCId** *(string) --*

      The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.

      For more information, see `ClassicLink
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__
      in the *Amazon EC2 Auto Scaling User Guide* .

    - **ClassicLinkVPCSecurityGroups** *(list) --*

      The IDs of one or more security groups for the VPC specified in ``ClassicLinkVPCId`` .

      For more information, see `ClassicLink
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__
      in the *Amazon EC2 Auto Scaling User Guide* .

      - *(string) --*

    - **UserData** *(string) --*

      The Base64-encoded user data to make available to the launched EC2 instances.

      For more information, see `Instance Metadata and User Data
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html>`__ in
      the *Amazon EC2 User Guide for Linux Instances* .

    - **InstanceType** *(string) --*

      The instance type for the instances.

      For information about available instance types, see `Available Instance Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
      in the *Amazon EC2 User Guide for Linux Instances.*

    - **KernelId** *(string) --*

      The ID of the kernel associated with the AMI.

    - **RamdiskId** *(string) --*

      The ID of the RAM disk associated with the AMI.

    - **BlockDeviceMappings** *(list) --*

      A block device mapping, which specifies the block devices for the instance.

      For more information, see `Block Device Mapping
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html>`__
      in the *Amazon EC2 User Guide for Linux Instances* .

      - *(dict) --*

        Describes a block device mapping.

        - **VirtualName** *(string) --*

          The name of the virtual device (for example, ``ephemeral0`` ).

        - **DeviceName** *(string) --*

          The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ).
          For more information, see `Device Naming on Linux Instances
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html>`__ in the
          *Amazon EC2 User Guide for Linux Instances* .

        - **Ebs** *(dict) --*

          The information about the Amazon EBS volume.

          - **SnapshotId** *(string) --*

            The snapshot ID of the volume to use.

            Conditional: This parameter is optional if you specify a volume size. If you
            specify both ``SnapshotId`` and ``VolumeSize`` , ``VolumeSize`` must be equal or
            greater than the size of the snapshot.

          - **VolumeSize** *(integer) --*

            The volume size, in Gibibytes (GiB).

            This can be a number from 1-1,024 for ``standard`` , 4-16,384 for ``io1`` ,
            1-16,384 for ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a
            snapshot, the volume size must be equal to or larger than the snapshot size.

            Default: If you create a volume from a snapshot and you don't specify a volume
            size, the default is the snapshot size.

            .. note::

              At least one of VolumeSize or SnapshotId is required.

          - **VolumeType** *(string) --*

            The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned
            IOPS SSD, ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or
            ``sc1`` for Cold HDD. For more information, see `Amazon EBS Volume Types
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
            *Amazon EC2 User Guide for Linux Instances* .

            Valid Values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``

          - **DeleteOnTermination** *(boolean) --*

            Indicates whether the volume is deleted on instance termination. For Amazon EC2
            Auto Scaling, the default value is ``true`` .

          - **Iops** *(integer) --*

            The number of I/O operations per second (IOPS) to provision for the volume. The
            maximum ratio of IOPS to volume size (in GiB) is 50:1. For more information, see
            `Amazon EBS Volume Types
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
            *Amazon EC2 User Guide for Linux Instances* .

            Conditional: This parameter is required when the volume type is ``io1`` . (Not used
            with ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.)

          - **Encrypted** *(boolean) --*

            Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be
            attached to instances that support Amazon EBS encryption. For more information, see
            `Supported Instance Types
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances>`__
            . If your AMI uses encrypted volumes, you can also only launch it on supported
            instance types.

            .. note::

              If you are creating a volume from a snapshot, you cannot specify an encryption
              value. Volumes that are created from encrypted snapshots are automatically
              encrypted, and volumes that are created from unencrypted snapshots are
              automatically unencrypted. By default, encrypted snapshots use the AWS managed
              CMK that is used for EBS encryption, but you can specify a custom CMK when you
              create the snapshot. The ability to encrypt a snapshot during copying also allows
              you to apply a new CMK to an already-encrypted snapshot. Volumes restored from
              the resulting copy are only accessible using the new CMK.

              Enabling `encryption by default
              <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default>`__
              results in all EBS volumes being encrypted with the AWS managed CMK or a customer
              managed CMK, whether or not the snapshot was encrypted.

            For more information, see `Using Encryption with EBS-Backed AMIs
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html>`__ in the
            *Amazon EC2 User Guide for Linux Instances* and `Required CMK Key Policy for Use
            with Encrypted Volumes
            <https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html>`__
            in the *Amazon EC2 Auto Scaling User Guide* .

        - **NoDevice** *(boolean) --*

          Suppresses a device mapping.

          If this parameter is true for the root device, the instance might fail the EC2 health
          check. In that case, Amazon EC2 Auto Scaling launches a replacement instance.

    - **InstanceMonitoring** *(dict) --*

      Controls whether instances in this group are launched with detailed (``true`` ) or basic
      (``false`` ) monitoring.

      For more information, see `Configure Monitoring for Auto Scaling Instances
      <https://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html#enable-as-instance-metrics>`__
      in the *Amazon EC2 Auto Scaling User Guide* .

      - **Enabled** *(boolean) --*

        If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

    - **SpotPrice** *(string) --*

      The maximum hourly price to be paid for any Spot Instance launched to fulfill the
      request. Spot Instances are launched when the price you specify exceeds the current Spot
      price.

      For more information, see `Launching Spot Instances in Your Auto Scaling Group
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-launch-spot-instances.html>`__
      in the *Amazon EC2 Auto Scaling User Guide* .

    - **IamInstanceProfile** *(string) --*

      The name or the Amazon Resource Name (ARN) of the instance profile associated with the
      IAM role for the instance. The instance profile contains the IAM role.

      For more information, see `IAM Role for Applications That Run on Amazon EC2 Instances
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html>`__ in the
      *Amazon EC2 Auto Scaling User Guide* .

    - **CreatedTime** *(datetime) --*

      The creation date and time for the launch configuration.

    - **EbsOptimized** *(boolean) --*

      Specifies whether the launch configuration is optimized for EBS I/O (``true`` ) or not
      (``false`` ).

      For more information, see `Amazon EBS-Optimized Instances
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html>`__ in the *Amazon
      EC2 User Guide for Linux Instances* .

    - **AssociatePublicIpAddress** *(boolean) --*

      For Auto Scaling groups that are running in a VPC, specifies whether to assign a public
      IP address to the group's instances.

      For more information, see `Launching Auto Scaling Instances in a VPC
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html>`__ in the *Amazon
      EC2 Auto Scaling User Guide* .

    - **PlacementTenancy** *(string) --*

      The tenancy of the instance, either ``default`` or ``dedicated`` . An instance with
      ``dedicated`` tenancy runs on isolated, single-tenant hardware and can only be launched
      into a VPC.

      For more information, see `Instance Placement Tenancy
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-vpc-tenancy>`__
      in the *Amazon EC2 Auto Scaling User Guide* .
    """


_ClientDescribeLaunchConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeLaunchConfigurationsResponseTypeDef",
    {
        "LaunchConfigurations": List[
            ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeLaunchConfigurationsResponseTypeDef(
    _ClientDescribeLaunchConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeLaunchConfigurations` `Response`

    - **LaunchConfigurations** *(list) --*

      The launch configurations.

      - *(dict) --*

        Describes a launch configuration.

        - **LaunchConfigurationName** *(string) --*

          The name of the launch configuration.

        - **LaunchConfigurationARN** *(string) --*

          The Amazon Resource Name (ARN) of the launch configuration.

        - **ImageId** *(string) --*

          The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances.

          For more information, see `Finding an AMI
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html>`__ in the
          *Amazon EC2 User Guide for Linux Instances* .

        - **KeyName** *(string) --*

          The name of the key pair.

          For more information, see `Amazon EC2 Key Pairs
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
          *Amazon EC2 User Guide for Linux Instances* .

        - **SecurityGroups** *(list) --*

          A list that contains the security groups to assign to the instances in the Auto Scaling
          group.

          For more information, see `Security Groups for Your VPC
          <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`__ in
          the *Amazon Virtual Private Cloud User Guide* .

          - *(string) --*

        - **ClassicLinkVPCId** *(string) --*

          The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.

          For more information, see `ClassicLink
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the
          *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__
          in the *Amazon EC2 Auto Scaling User Guide* .

        - **ClassicLinkVPCSecurityGroups** *(list) --*

          The IDs of one or more security groups for the VPC specified in ``ClassicLinkVPCId`` .

          For more information, see `ClassicLink
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the
          *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__
          in the *Amazon EC2 Auto Scaling User Guide* .

          - *(string) --*

        - **UserData** *(string) --*

          The Base64-encoded user data to make available to the launched EC2 instances.

          For more information, see `Instance Metadata and User Data
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html>`__ in
          the *Amazon EC2 User Guide for Linux Instances* .

        - **InstanceType** *(string) --*

          The instance type for the instances.

          For information about available instance types, see `Available Instance Types
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
          in the *Amazon EC2 User Guide for Linux Instances.*

        - **KernelId** *(string) --*

          The ID of the kernel associated with the AMI.

        - **RamdiskId** *(string) --*

          The ID of the RAM disk associated with the AMI.

        - **BlockDeviceMappings** *(list) --*

          A block device mapping, which specifies the block devices for the instance.

          For more information, see `Block Device Mapping
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html>`__
          in the *Amazon EC2 User Guide for Linux Instances* .

          - *(dict) --*

            Describes a block device mapping.

            - **VirtualName** *(string) --*

              The name of the virtual device (for example, ``ephemeral0`` ).

            - **DeviceName** *(string) --*

              The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ).
              For more information, see `Device Naming on Linux Instances
              <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html>`__ in the
              *Amazon EC2 User Guide for Linux Instances* .

            - **Ebs** *(dict) --*

              The information about the Amazon EBS volume.

              - **SnapshotId** *(string) --*

                The snapshot ID of the volume to use.

                Conditional: This parameter is optional if you specify a volume size. If you
                specify both ``SnapshotId`` and ``VolumeSize`` , ``VolumeSize`` must be equal or
                greater than the size of the snapshot.

              - **VolumeSize** *(integer) --*

                The volume size, in Gibibytes (GiB).

                This can be a number from 1-1,024 for ``standard`` , 4-16,384 for ``io1`` ,
                1-16,384 for ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a
                snapshot, the volume size must be equal to or larger than the snapshot size.

                Default: If you create a volume from a snapshot and you don't specify a volume
                size, the default is the snapshot size.

                .. note::

                  At least one of VolumeSize or SnapshotId is required.

              - **VolumeType** *(string) --*

                The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned
                IOPS SSD, ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or
                ``sc1`` for Cold HDD. For more information, see `Amazon EBS Volume Types
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
                *Amazon EC2 User Guide for Linux Instances* .

                Valid Values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``

              - **DeleteOnTermination** *(boolean) --*

                Indicates whether the volume is deleted on instance termination. For Amazon EC2
                Auto Scaling, the default value is ``true`` .

              - **Iops** *(integer) --*

                The number of I/O operations per second (IOPS) to provision for the volume. The
                maximum ratio of IOPS to volume size (in GiB) is 50:1. For more information, see
                `Amazon EBS Volume Types
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
                *Amazon EC2 User Guide for Linux Instances* .

                Conditional: This parameter is required when the volume type is ``io1`` . (Not used
                with ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.)

              - **Encrypted** *(boolean) --*

                Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be
                attached to instances that support Amazon EBS encryption. For more information, see
                `Supported Instance Types
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances>`__
                . If your AMI uses encrypted volumes, you can also only launch it on supported
                instance types.

                .. note::

                  If you are creating a volume from a snapshot, you cannot specify an encryption
                  value. Volumes that are created from encrypted snapshots are automatically
                  encrypted, and volumes that are created from unencrypted snapshots are
                  automatically unencrypted. By default, encrypted snapshots use the AWS managed
                  CMK that is used for EBS encryption, but you can specify a custom CMK when you
                  create the snapshot. The ability to encrypt a snapshot during copying also allows
                  you to apply a new CMK to an already-encrypted snapshot. Volumes restored from
                  the resulting copy are only accessible using the new CMK.

                  Enabling `encryption by default
                  <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default>`__
                  results in all EBS volumes being encrypted with the AWS managed CMK or a customer
                  managed CMK, whether or not the snapshot was encrypted.

                For more information, see `Using Encryption with EBS-Backed AMIs
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html>`__ in the
                *Amazon EC2 User Guide for Linux Instances* and `Required CMK Key Policy for Use
                with Encrypted Volumes
                <https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html>`__
                in the *Amazon EC2 Auto Scaling User Guide* .

            - **NoDevice** *(boolean) --*

              Suppresses a device mapping.

              If this parameter is true for the root device, the instance might fail the EC2 health
              check. In that case, Amazon EC2 Auto Scaling launches a replacement instance.

        - **InstanceMonitoring** *(dict) --*

          Controls whether instances in this group are launched with detailed (``true`` ) or basic
          (``false`` ) monitoring.

          For more information, see `Configure Monitoring for Auto Scaling Instances
          <https://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html#enable-as-instance-metrics>`__
          in the *Amazon EC2 Auto Scaling User Guide* .

          - **Enabled** *(boolean) --*

            If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

        - **SpotPrice** *(string) --*

          The maximum hourly price to be paid for any Spot Instance launched to fulfill the
          request. Spot Instances are launched when the price you specify exceeds the current Spot
          price.

          For more information, see `Launching Spot Instances in Your Auto Scaling Group
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-launch-spot-instances.html>`__
          in the *Amazon EC2 Auto Scaling User Guide* .

        - **IamInstanceProfile** *(string) --*

          The name or the Amazon Resource Name (ARN) of the instance profile associated with the
          IAM role for the instance. The instance profile contains the IAM role.

          For more information, see `IAM Role for Applications That Run on Amazon EC2 Instances
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html>`__ in the
          *Amazon EC2 Auto Scaling User Guide* .

        - **CreatedTime** *(datetime) --*

          The creation date and time for the launch configuration.

        - **EbsOptimized** *(boolean) --*

          Specifies whether the launch configuration is optimized for EBS I/O (``true`` ) or not
          (``false`` ).

          For more information, see `Amazon EBS-Optimized Instances
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html>`__ in the *Amazon
          EC2 User Guide for Linux Instances* .

        - **AssociatePublicIpAddress** *(boolean) --*

          For Auto Scaling groups that are running in a VPC, specifies whether to assign a public
          IP address to the group's instances.

          For more information, see `Launching Auto Scaling Instances in a VPC
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html>`__ in the *Amazon
          EC2 Auto Scaling User Guide* .

        - **PlacementTenancy** *(string) --*

          The tenancy of the instance, either ``default`` or ``dedicated`` . An instance with
          ``dedicated`` tenancy runs on isolated, single-tenant hardware and can only be launched
          into a VPC.

          For more information, see `Instance Placement Tenancy
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-vpc-tenancy>`__
          in the *Amazon EC2 Auto Scaling User Guide* .

    - **NextToken** *(string) --*

      A string that indicates that the response contains more items than can be returned in a
      single response. To receive additional items, specify this string for the ``NextToken`` value
      when requesting the next set of items. This value is null when there are no more items to
      return.
    """


_ClientDescribeLifecycleHookTypesResponseTypeDef = TypedDict(
    "_ClientDescribeLifecycleHookTypesResponseTypeDef",
    {"LifecycleHookTypes": List[str]},
    total=False,
)


class ClientDescribeLifecycleHookTypesResponseTypeDef(
    _ClientDescribeLifecycleHookTypesResponseTypeDef
):
    """
    Type definition for `ClientDescribeLifecycleHookTypes` `Response`

    - **LifecycleHookTypes** *(list) --*

      The lifecycle hook types.

      - *(string) --*
    """


_ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef = TypedDict(
    "_ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleTransition": str,
        "NotificationTargetARN": str,
        "RoleARN": str,
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "GlobalTimeout": int,
        "DefaultResult": str,
    },
    total=False,
)


class ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef(
    _ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef
):
    """
    Type definition for `ClientDescribeLifecycleHooksResponse` `LifecycleHooks`

    Describes a lifecycle hook, which tells Amazon EC2 Auto Scaling that you want to perform an
    action whenever it launches instances or terminates instances. Used in response to
    DescribeLifecycleHooks .

    - **LifecycleHookName** *(string) --*

      The name of the lifecycle hook.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group for the lifecycle hook.

    - **LifecycleTransition** *(string) --*

      The state of the EC2 instance to which to attach the lifecycle hook. The following are
      possible values:

      * autoscaling:EC2_INSTANCE_LAUNCHING

      * autoscaling:EC2_INSTANCE_TERMINATING

    - **NotificationTargetARN** *(string) --*

      The ARN of the target that Amazon EC2 Auto Scaling sends notifications to when an
      instance is in the transition state for the lifecycle hook. The notification target can
      be either an SQS queue or an SNS topic.

    - **RoleARN** *(string) --*

      The ARN of the IAM role that allows the Auto Scaling group to publish to the specified
      notification target.

    - **NotificationMetadata** *(string) --*

      Additional information that is included any time Amazon EC2 Auto Scaling sends a message
      to the notification target.

    - **HeartbeatTimeout** *(integer) --*

      The maximum time, in seconds, that can elapse before the lifecycle hook times out. If the
      lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified
      in the ``DefaultResult`` parameter.

    - **GlobalTimeout** *(integer) --*

      The maximum time, in seconds, that an instance can remain in a ``Pending:Wait`` or
      ``Terminating:Wait`` state. The maximum is 172800 seconds (48 hours) or 100 times
      ``HeartbeatTimeout`` , whichever is smaller.

    - **DefaultResult** *(string) --*

      Defines the action the Auto Scaling group should take when the lifecycle hook timeout
      elapses or if an unexpected failure occurs. The possible values are ``CONTINUE`` and
      ``ABANDON`` .
    """


_ClientDescribeLifecycleHooksResponseTypeDef = TypedDict(
    "_ClientDescribeLifecycleHooksResponseTypeDef",
    {"LifecycleHooks": List[ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef]},
    total=False,
)


class ClientDescribeLifecycleHooksResponseTypeDef(
    _ClientDescribeLifecycleHooksResponseTypeDef
):
    """
    Type definition for `ClientDescribeLifecycleHooks` `Response`

    - **LifecycleHooks** *(list) --*

      The lifecycle hooks for the specified group.

      - *(dict) --*

        Describes a lifecycle hook, which tells Amazon EC2 Auto Scaling that you want to perform an
        action whenever it launches instances or terminates instances. Used in response to
        DescribeLifecycleHooks .

        - **LifecycleHookName** *(string) --*

          The name of the lifecycle hook.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group for the lifecycle hook.

        - **LifecycleTransition** *(string) --*

          The state of the EC2 instance to which to attach the lifecycle hook. The following are
          possible values:

          * autoscaling:EC2_INSTANCE_LAUNCHING

          * autoscaling:EC2_INSTANCE_TERMINATING

        - **NotificationTargetARN** *(string) --*

          The ARN of the target that Amazon EC2 Auto Scaling sends notifications to when an
          instance is in the transition state for the lifecycle hook. The notification target can
          be either an SQS queue or an SNS topic.

        - **RoleARN** *(string) --*

          The ARN of the IAM role that allows the Auto Scaling group to publish to the specified
          notification target.

        - **NotificationMetadata** *(string) --*

          Additional information that is included any time Amazon EC2 Auto Scaling sends a message
          to the notification target.

        - **HeartbeatTimeout** *(integer) --*

          The maximum time, in seconds, that can elapse before the lifecycle hook times out. If the
          lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified
          in the ``DefaultResult`` parameter.

        - **GlobalTimeout** *(integer) --*

          The maximum time, in seconds, that an instance can remain in a ``Pending:Wait`` or
          ``Terminating:Wait`` state. The maximum is 172800 seconds (48 hours) or 100 times
          ``HeartbeatTimeout`` , whichever is smaller.

        - **DefaultResult** *(string) --*

          Defines the action the Auto Scaling group should take when the lifecycle hook timeout
          elapses or if an unexpected failure occurs. The possible values are ``CONTINUE`` and
          ``ABANDON`` .
    """


_ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef",
    {"LoadBalancerTargetGroupARN": str, "State": str},
    total=False,
)


class ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef(
    _ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerTargetGroupsResponse` `LoadBalancerTargetGroups`

    Describes the state of a target group.

    If you attach a target group to an existing Auto Scaling group, the initial state is
    ``Adding`` . The state transitions to ``Added`` after all Auto Scaling instances are
    registered with the target group. If Elastic Load Balancing health checks are enabled, the
    state transitions to ``InService`` after at least one Auto Scaling instance passes the
    health check. If EC2 health checks are enabled instead, the target group remains in the
    ``Added`` state.

    - **LoadBalancerTargetGroupARN** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **State** *(string) --*

      The state of the target group.

      * ``Adding`` - The Auto Scaling instances are being registered with the target group.

      * ``Added`` - All Auto Scaling instances are registered with the target group.

      * ``InService`` - At least one Auto Scaling instance passed an ELB health check.

      * ``Removing`` - The Auto Scaling instances are being deregistered from the target group.
      If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to
      complete before deregistering the instances.

      * ``Removed`` - All Auto Scaling instances are deregistered from the target group.
    """


_ClientDescribeLoadBalancerTargetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerTargetGroupsResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List[
            ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeLoadBalancerTargetGroupsResponseTypeDef(
    _ClientDescribeLoadBalancerTargetGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerTargetGroups` `Response`

    - **LoadBalancerTargetGroups** *(list) --*

      Information about the target groups.

      - *(dict) --*

        Describes the state of a target group.

        If you attach a target group to an existing Auto Scaling group, the initial state is
        ``Adding`` . The state transitions to ``Added`` after all Auto Scaling instances are
        registered with the target group. If Elastic Load Balancing health checks are enabled, the
        state transitions to ``InService`` after at least one Auto Scaling instance passes the
        health check. If EC2 health checks are enabled instead, the target group remains in the
        ``Added`` state.

        - **LoadBalancerTargetGroupARN** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **State** *(string) --*

          The state of the target group.

          * ``Adding`` - The Auto Scaling instances are being registered with the target group.

          * ``Added`` - All Auto Scaling instances are registered with the target group.

          * ``InService`` - At least one Auto Scaling instance passed an ELB health check.

          * ``Removing`` - The Auto Scaling instances are being deregistered from the target group.
          If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to
          complete before deregistering the instances.

          * ``Removed`` - All Auto Scaling instances are deregistered from the target group.

    - **NextToken** *(string) --*

      A string that indicates that the response contains more items than can be returned in a
      single response. To receive additional items, specify this string for the ``NextToken`` value
      when requesting the next set of items. This value is null when there are no more items to
      return.
    """


_ClientDescribeLoadBalancersResponseLoadBalancersTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    {"LoadBalancerName": str, "State": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancersTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancersTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponse` `LoadBalancers`

    Describes the state of a Classic Load Balancer.

    If you specify a load balancer when creating the Auto Scaling group, the state of the load
    balancer is ``InService`` .

    If you attach a load balancer to an existing Auto Scaling group, the initial state is
    ``Adding`` . The state transitions to ``Added`` after all instances in the group are
    registered with the load balancer. If Elastic Load Balancing health checks are enabled for
    the load balancer, the state transitions to ``InService`` after at least one instance in
    the group passes the health check. If EC2 health checks are enabled instead, the load
    balancer remains in the ``Added`` state.

    - **LoadBalancerName** *(string) --*

      The name of the load balancer.

    - **State** *(string) --*

      One of the following load balancer states:

      * ``Adding`` - The instances in the group are being registered with the load balancer.

      * ``Added`` - All instances in the group are registered with the load balancer.

      * ``InService`` - At least one instance in the group passed an ELB health check.

      * ``Removing`` - The instances in the group are being deregistered from the load
      balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight
      requests to complete before deregistering the instances.

      * ``Removed`` - All instances in the group are deregistered from the load balancer.
    """


_ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancers": List[ClientDescribeLoadBalancersResponseLoadBalancersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseTypeDef(
    _ClientDescribeLoadBalancersResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancers` `Response`

    - **LoadBalancers** *(list) --*

      The load balancers.

      - *(dict) --*

        Describes the state of a Classic Load Balancer.

        If you specify a load balancer when creating the Auto Scaling group, the state of the load
        balancer is ``InService`` .

        If you attach a load balancer to an existing Auto Scaling group, the initial state is
        ``Adding`` . The state transitions to ``Added`` after all instances in the group are
        registered with the load balancer. If Elastic Load Balancing health checks are enabled for
        the load balancer, the state transitions to ``InService`` after at least one instance in
        the group passes the health check. If EC2 health checks are enabled instead, the load
        balancer remains in the ``Added`` state.

        - **LoadBalancerName** *(string) --*

          The name of the load balancer.

        - **State** *(string) --*

          One of the following load balancer states:

          * ``Adding`` - The instances in the group are being registered with the load balancer.

          * ``Added`` - All instances in the group are registered with the load balancer.

          * ``InService`` - At least one instance in the group passed an ELB health check.

          * ``Removing`` - The instances in the group are being deregistered from the load
          balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight
          requests to complete before deregistering the instances.

          * ``Removed`` - All instances in the group are deregistered from the load balancer.

    - **NextToken** *(string) --*

      A string that indicates that the response contains more items than can be returned in a
      single response. To receive additional items, specify this string for the ``NextToken`` value
      when requesting the next set of items. This value is null when there are no more items to
      return.
    """


_ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef = TypedDict(
    "_ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef",
    {"Granularity": str},
    total=False,
)


class ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef(
    _ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef
):
    """
    Type definition for `ClientDescribeMetricCollectionTypesResponse` `Granularities`

    Describes a granularity of a metric.

    - **Granularity** *(string) --*

      The granularity. The only valid value is ``1Minute`` .
    """


_ClientDescribeMetricCollectionTypesResponseMetricsTypeDef = TypedDict(
    "_ClientDescribeMetricCollectionTypesResponseMetricsTypeDef",
    {"Metric": str},
    total=False,
)


class ClientDescribeMetricCollectionTypesResponseMetricsTypeDef(
    _ClientDescribeMetricCollectionTypesResponseMetricsTypeDef
):
    """
    Type definition for `ClientDescribeMetricCollectionTypesResponse` `Metrics`

    Describes a metric.

    - **Metric** *(string) --*

      One of the following metrics:

      * ``GroupMinSize``

      * ``GroupMaxSize``

      * ``GroupDesiredCapacity``

      * ``GroupInServiceInstances``

      * ``GroupPendingInstances``

      * ``GroupStandbyInstances``

      * ``GroupTerminatingInstances``

      * ``GroupTotalInstances``
    """


_ClientDescribeMetricCollectionTypesResponseTypeDef = TypedDict(
    "_ClientDescribeMetricCollectionTypesResponseTypeDef",
    {
        "Metrics": List[ClientDescribeMetricCollectionTypesResponseMetricsTypeDef],
        "Granularities": List[
            ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeMetricCollectionTypesResponseTypeDef(
    _ClientDescribeMetricCollectionTypesResponseTypeDef
):
    """
    Type definition for `ClientDescribeMetricCollectionTypes` `Response`

    - **Metrics** *(list) --*

      One or more metrics.

      - *(dict) --*

        Describes a metric.

        - **Metric** *(string) --*

          One of the following metrics:

          * ``GroupMinSize``

          * ``GroupMaxSize``

          * ``GroupDesiredCapacity``

          * ``GroupInServiceInstances``

          * ``GroupPendingInstances``

          * ``GroupStandbyInstances``

          * ``GroupTerminatingInstances``

          * ``GroupTotalInstances``

    - **Granularities** *(list) --*

      The granularities for the metrics.

      - *(dict) --*

        Describes a granularity of a metric.

        - **Granularity** *(string) --*

          The granularity. The only valid value is ``1Minute`` .
    """


_ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef = TypedDict(
    "_ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef",
    {"AutoScalingGroupName": str, "TopicARN": str, "NotificationType": str},
    total=False,
)


class ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef(
    _ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeNotificationConfigurationsResponse` `NotificationConfigurations`

    Describes a notification.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **TopicARN** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS)
      topic.

    - **NotificationType** *(string) --*

      One of the following event notification types:

      * ``autoscaling:EC2_INSTANCE_LAUNCH``

      * ``autoscaling:EC2_INSTANCE_LAUNCH_ERROR``

      * ``autoscaling:EC2_INSTANCE_TERMINATE``

      * ``autoscaling:EC2_INSTANCE_TERMINATE_ERROR``

      * ``autoscaling:TEST_NOTIFICATION``
    """


_ClientDescribeNotificationConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeNotificationConfigurationsResponseTypeDef",
    {
        "NotificationConfigurations": List[
            ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeNotificationConfigurationsResponseTypeDef(
    _ClientDescribeNotificationConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeNotificationConfigurations` `Response`

    - **NotificationConfigurations** *(list) --*

      The notification configurations.

      - *(dict) --*

        Describes a notification.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **TopicARN** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS)
          topic.

        - **NotificationType** *(string) --*

          One of the following event notification types:

          * ``autoscaling:EC2_INSTANCE_LAUNCH``

          * ``autoscaling:EC2_INSTANCE_LAUNCH_ERROR``

          * ``autoscaling:EC2_INSTANCE_TERMINATE``

          * ``autoscaling:EC2_INSTANCE_TERMINATE_ERROR``

          * ``autoscaling:TEST_NOTIFICATION``

    - **NextToken** *(string) --*

      A string that indicates that the response contains more items than can be returned in a
      single response. To receive additional items, specify this string for the ``NextToken`` value
      when requesting the next set of items. This value is null when there are no more items to
      return.
    """


_ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef
):
    """
    Type definition for `ClientDescribePoliciesResponseScalingPolicies` `Alarms`

    Describes an alarm.

    - **AlarmName** *(string) --*

      The name of the alarm.

    - **AlarmARN** *(string) --*

      The Amazon Resource Name (ARN) of the alarm.
    """


_ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef
):
    """
    Type definition for `ClientDescribePoliciesResponseScalingPolicies` `StepAdjustments`

    Describes an adjustment based on the difference between the value of the aggregated
    CloudWatch metric and the breach threshold that you've defined for the alarm. Used in
    combination with  PutScalingPolicy .

    For the following examples, suppose that you have an alarm with a breach threshold of
    50:

    * To trigger the adjustment when the metric is greater than or equal to 50 and less
    than 60, specify a lower bound of 0 and an upper bound of 10.

    * To trigger the adjustment when the metric is greater than 40 and less than or equal
    to 50, specify a lower bound of -10 and an upper bound of 0.

    There are a few rules for the step adjustments for your step policy:

    * The ranges of your step adjustments can't overlap or have a gap.

    * At most, one step adjustment can have a null lower bound. If one step adjustment has
    a negative lower bound, then there must be a step adjustment with a null lower bound.

    * At most, one step adjustment can have a null upper bound. If one step adjustment has
    a positive upper bound, then there must be a step adjustment with a null upper bound.

    * The upper and lower bound can't be null in the same step adjustment.

    - **MetricIntervalLowerBound** *(float) --*

      The lower bound for the difference between the alarm threshold and the CloudWatch
      metric. If the metric value is above the breach threshold, the lower bound is
      inclusive (the metric must be greater than or equal to the threshold plus the lower
      bound). Otherwise, it is exclusive (the metric must be greater than the threshold
      plus the lower bound). A null value indicates negative infinity.

    - **MetricIntervalUpperBound** *(float) --*

      The upper bound for the difference between the alarm threshold and the CloudWatch
      metric. If the metric value is above the breach threshold, the upper bound is
      exclusive (the metric must be less than the threshold plus the upper bound).
      Otherwise, it is inclusive (the metric must be less than or equal to the threshold
      plus the upper bound). A null value indicates positive infinity.

      The upper bound must be greater than the lower bound.

    - **ScalingAdjustment** *(integer) --*

      The amount by which to scale, based on the specified adjustment type. A positive
      value adds to the current capacity while a negative number removes from the current
      capacity.
    """


_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecification` `Dimensions`

    Describes the dimension of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value of the dimension.
    """


_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef
):
    """
    Type definition for `ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfiguration` `CustomizedMetricSpecification`

    A customized metric. You must specify either a predefined metric or a customized metric.

    - **MetricName** *(string) --*

      The name of the metric.

    - **Namespace** *(string) --*

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the same
      dimensions in your scaling policy.

      - *(dict) --*

        Describes the dimension of a metric.

        - **Name** *(string) --*

          The name of the dimension.

        - **Value** *(string) --*

          The value of the dimension.

    - **Statistic** *(string) --*

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {"PredefinedMetricType": str, "ResourceLabel": str},
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef
):
    """
    Type definition for `ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfiguration` `PredefinedMetricSpecification`

    A predefined metric. You must specify either a predefined metric or a customized metric.

    - **PredefinedMetricType** *(string) --*

      The metric type. The following predefined metrics are available:

      * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.

      * ``ASGAverageNetworkIn`` - Average number of bytes received on all network
      interfaces by the Auto Scaling group.

      * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network
      interfaces by the Auto Scaling group.

      * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an
      Application Load Balancer target group.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a resource
      label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
      group attached to the Auto Scaling group.

      The format is ``app/*load-balancer-name* /*load-balancer-id*
      /targetgroup/*target-group-name* /*target-group-id* `` , where

      * ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load
      balancer ARN, and

      * ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the
      target group ARN.
    """


_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
    },
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef
):
    """
    Type definition for `ClientDescribePoliciesResponseScalingPolicies` `TargetTrackingConfiguration`

    A target tracking scaling policy.

    - **PredefinedMetricSpecification** *(dict) --*

      A predefined metric. You must specify either a predefined metric or a customized metric.

      - **PredefinedMetricType** *(string) --*

        The metric type. The following predefined metrics are available:

        * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.

        * ``ASGAverageNetworkIn`` - Average number of bytes received on all network
        interfaces by the Auto Scaling group.

        * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network
        interfaces by the Auto Scaling group.

        * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an
        Application Load Balancer target group.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a resource
        label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
        group attached to the Auto Scaling group.

        The format is ``app/*load-balancer-name* /*load-balancer-id*
        /targetgroup/*target-group-name* /*target-group-id* `` , where

        * ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load
        balancer ARN, and

        * ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the
        target group ARN.

    - **CustomizedMetricSpecification** *(dict) --*

      A customized metric. You must specify either a predefined metric or a customized metric.

      - **MetricName** *(string) --*

        The name of the metric.

      - **Namespace** *(string) --*

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the same
        dimensions in your scaling policy.

        - *(dict) --*

          Describes the dimension of a metric.

          - **Name** *(string) --*

            The name of the dimension.

          - **Value** *(string) --*

            The value of the dimension.

      - **Statistic** *(string) --*

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **TargetValue** *(float) --*

      The target value for the metric.

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scaling in by the target tracking scaling policy is disabled. If
      scaling in is disabled, the target tracking scaling policy doesn't remove instances
      from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove
      instances from the Auto Scaling group. The default is ``false`` .
    """


_ClientDescribePoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseScalingPoliciesTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "PolicyARN": str,
        "PolicyType": str,
        "AdjustmentType": str,
        "MinAdjustmentStep": int,
        "MinAdjustmentMagnitude": int,
        "ScalingAdjustment": int,
        "Cooldown": int,
        "StepAdjustments": List[
            ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef
        ],
        "MetricAggregationType": str,
        "EstimatedInstanceWarmup": int,
        "Alarms": List[ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef],
        "TargetTrackingConfiguration": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribePoliciesResponseScalingPoliciesTypeDef(
    _ClientDescribePoliciesResponseScalingPoliciesTypeDef
):
    """
    Type definition for `ClientDescribePoliciesResponse` `ScalingPolicies`

    Describes a scaling policy.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **PolicyName** *(string) --*

      The name of the scaling policy.

    - **PolicyARN** *(string) --*

      The Amazon Resource Name (ARN) of the policy.

    - **PolicyType** *(string) --*

      The policy type. The valid values are ``SimpleScaling`` , ``StepScaling`` , and
      ``TargetTrackingScaling`` .

    - **AdjustmentType** *(string) --*

      The adjustment type, which specifies how ``ScalingAdjustment`` is interpreted. The valid
      values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .

    - **MinAdjustmentStep** *(integer) --*

      Available for backward compatibility. Use ``MinAdjustmentMagnitude`` instead.

    - **MinAdjustmentMagnitude** *(integer) --*

      The minimum number of instances to scale. If the value of ``AdjustmentType`` is
      ``PercentChangeInCapacity`` , the scaling policy changes the ``DesiredCapacity`` of the
      Auto Scaling group by at least this many instances. Otherwise, the error is
      ``ValidationError`` .

    - **ScalingAdjustment** *(integer) --*

      The amount by which to scale, based on the specified adjustment type. A positive value
      adds to the current capacity while a negative number removes from the current capacity.

    - **Cooldown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes before any further
      dynamic scaling activities can start.

    - **StepAdjustments** *(list) --*

      A set of adjustments that enable you to scale based on the size of the alarm breach.

      - *(dict) --*

        Describes an adjustment based on the difference between the value of the aggregated
        CloudWatch metric and the breach threshold that you've defined for the alarm. Used in
        combination with  PutScalingPolicy .

        For the following examples, suppose that you have an alarm with a breach threshold of
        50:

        * To trigger the adjustment when the metric is greater than or equal to 50 and less
        than 60, specify a lower bound of 0 and an upper bound of 10.

        * To trigger the adjustment when the metric is greater than 40 and less than or equal
        to 50, specify a lower bound of -10 and an upper bound of 0.

        There are a few rules for the step adjustments for your step policy:

        * The ranges of your step adjustments can't overlap or have a gap.

        * At most, one step adjustment can have a null lower bound. If one step adjustment has
        a negative lower bound, then there must be a step adjustment with a null lower bound.

        * At most, one step adjustment can have a null upper bound. If one step adjustment has
        a positive upper bound, then there must be a step adjustment with a null upper bound.

        * The upper and lower bound can't be null in the same step adjustment.

        - **MetricIntervalLowerBound** *(float) --*

          The lower bound for the difference between the alarm threshold and the CloudWatch
          metric. If the metric value is above the breach threshold, the lower bound is
          inclusive (the metric must be greater than or equal to the threshold plus the lower
          bound). Otherwise, it is exclusive (the metric must be greater than the threshold
          plus the lower bound). A null value indicates negative infinity.

        - **MetricIntervalUpperBound** *(float) --*

          The upper bound for the difference between the alarm threshold and the CloudWatch
          metric. If the metric value is above the breach threshold, the upper bound is
          exclusive (the metric must be less than the threshold plus the upper bound).
          Otherwise, it is inclusive (the metric must be less than or equal to the threshold
          plus the upper bound). A null value indicates positive infinity.

          The upper bound must be greater than the lower bound.

        - **ScalingAdjustment** *(integer) --*

          The amount by which to scale, based on the specified adjustment type. A positive
          value adds to the current capacity while a negative number removes from the current
          capacity.

    - **MetricAggregationType** *(string) --*

      The aggregation type for the CloudWatch metrics. The valid values are ``Minimum`` ,
      ``Maximum`` , and ``Average`` .

    - **EstimatedInstanceWarmup** *(integer) --*

      The estimated time, in seconds, until a newly launched instance can contribute to the
      CloudWatch metrics.

    - **Alarms** *(list) --*

      The CloudWatch alarms related to the policy.

      - *(dict) --*

        Describes an alarm.

        - **AlarmName** *(string) --*

          The name of the alarm.

        - **AlarmARN** *(string) --*

          The Amazon Resource Name (ARN) of the alarm.

    - **TargetTrackingConfiguration** *(dict) --*

      A target tracking scaling policy.

      - **PredefinedMetricSpecification** *(dict) --*

        A predefined metric. You must specify either a predefined metric or a customized metric.

        - **PredefinedMetricType** *(string) --*

          The metric type. The following predefined metrics are available:

          * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.

          * ``ASGAverageNetworkIn`` - Average number of bytes received on all network
          interfaces by the Auto Scaling group.

          * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network
          interfaces by the Auto Scaling group.

          * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an
          Application Load Balancer target group.

        - **ResourceLabel** *(string) --*

          Identifies the resource associated with the metric type. You can't specify a resource
          label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
          group attached to the Auto Scaling group.

          The format is ``app/*load-balancer-name* /*load-balancer-id*
          /targetgroup/*target-group-name* /*target-group-id* `` , where

          * ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load
          balancer ARN, and

          * ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the
          target group ARN.

      - **CustomizedMetricSpecification** *(dict) --*

        A customized metric. You must specify either a predefined metric or a customized metric.

        - **MetricName** *(string) --*

          The name of the metric.

        - **Namespace** *(string) --*

          The namespace of the metric.

        - **Dimensions** *(list) --*

          The dimensions of the metric.

          Conditional: If you published your metric with dimensions, you must specify the same
          dimensions in your scaling policy.

          - *(dict) --*

            Describes the dimension of a metric.

            - **Name** *(string) --*

              The name of the dimension.

            - **Value** *(string) --*

              The value of the dimension.

        - **Statistic** *(string) --*

          The statistic of the metric.

        - **Unit** *(string) --*

          The unit of the metric.

      - **TargetValue** *(float) --*

        The target value for the metric.

      - **DisableScaleIn** *(boolean) --*

        Indicates whether scaling in by the target tracking scaling policy is disabled. If
        scaling in is disabled, the target tracking scaling policy doesn't remove instances
        from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove
        instances from the Auto Scaling group. The default is ``false`` .
    """


_ClientDescribePoliciesResponseTypeDef = TypedDict(
    "_ClientDescribePoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[ClientDescribePoliciesResponseScalingPoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribePoliciesResponseTypeDef(_ClientDescribePoliciesResponseTypeDef):
    """
    Type definition for `ClientDescribePolicies` `Response`

    - **ScalingPolicies** *(list) --*

      The scaling policies.

      - *(dict) --*

        Describes a scaling policy.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **PolicyName** *(string) --*

          The name of the scaling policy.

        - **PolicyARN** *(string) --*

          The Amazon Resource Name (ARN) of the policy.

        - **PolicyType** *(string) --*

          The policy type. The valid values are ``SimpleScaling`` , ``StepScaling`` , and
          ``TargetTrackingScaling`` .

        - **AdjustmentType** *(string) --*

          The adjustment type, which specifies how ``ScalingAdjustment`` is interpreted. The valid
          values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .

        - **MinAdjustmentStep** *(integer) --*

          Available for backward compatibility. Use ``MinAdjustmentMagnitude`` instead.

        - **MinAdjustmentMagnitude** *(integer) --*

          The minimum number of instances to scale. If the value of ``AdjustmentType`` is
          ``PercentChangeInCapacity`` , the scaling policy changes the ``DesiredCapacity`` of the
          Auto Scaling group by at least this many instances. Otherwise, the error is
          ``ValidationError`` .

        - **ScalingAdjustment** *(integer) --*

          The amount by which to scale, based on the specified adjustment type. A positive value
          adds to the current capacity while a negative number removes from the current capacity.

        - **Cooldown** *(integer) --*

          The amount of time, in seconds, after a scaling activity completes before any further
          dynamic scaling activities can start.

        - **StepAdjustments** *(list) --*

          A set of adjustments that enable you to scale based on the size of the alarm breach.

          - *(dict) --*

            Describes an adjustment based on the difference between the value of the aggregated
            CloudWatch metric and the breach threshold that you've defined for the alarm. Used in
            combination with  PutScalingPolicy .

            For the following examples, suppose that you have an alarm with a breach threshold of
            50:

            * To trigger the adjustment when the metric is greater than or equal to 50 and less
            than 60, specify a lower bound of 0 and an upper bound of 10.

            * To trigger the adjustment when the metric is greater than 40 and less than or equal
            to 50, specify a lower bound of -10 and an upper bound of 0.

            There are a few rules for the step adjustments for your step policy:

            * The ranges of your step adjustments can't overlap or have a gap.

            * At most, one step adjustment can have a null lower bound. If one step adjustment has
            a negative lower bound, then there must be a step adjustment with a null lower bound.

            * At most, one step adjustment can have a null upper bound. If one step adjustment has
            a positive upper bound, then there must be a step adjustment with a null upper bound.

            * The upper and lower bound can't be null in the same step adjustment.

            - **MetricIntervalLowerBound** *(float) --*

              The lower bound for the difference between the alarm threshold and the CloudWatch
              metric. If the metric value is above the breach threshold, the lower bound is
              inclusive (the metric must be greater than or equal to the threshold plus the lower
              bound). Otherwise, it is exclusive (the metric must be greater than the threshold
              plus the lower bound). A null value indicates negative infinity.

            - **MetricIntervalUpperBound** *(float) --*

              The upper bound for the difference between the alarm threshold and the CloudWatch
              metric. If the metric value is above the breach threshold, the upper bound is
              exclusive (the metric must be less than the threshold plus the upper bound).
              Otherwise, it is inclusive (the metric must be less than or equal to the threshold
              plus the upper bound). A null value indicates positive infinity.

              The upper bound must be greater than the lower bound.

            - **ScalingAdjustment** *(integer) --*

              The amount by which to scale, based on the specified adjustment type. A positive
              value adds to the current capacity while a negative number removes from the current
              capacity.

        - **MetricAggregationType** *(string) --*

          The aggregation type for the CloudWatch metrics. The valid values are ``Minimum`` ,
          ``Maximum`` , and ``Average`` .

        - **EstimatedInstanceWarmup** *(integer) --*

          The estimated time, in seconds, until a newly launched instance can contribute to the
          CloudWatch metrics.

        - **Alarms** *(list) --*

          The CloudWatch alarms related to the policy.

          - *(dict) --*

            Describes an alarm.

            - **AlarmName** *(string) --*

              The name of the alarm.

            - **AlarmARN** *(string) --*

              The Amazon Resource Name (ARN) of the alarm.

        - **TargetTrackingConfiguration** *(dict) --*

          A target tracking scaling policy.

          - **PredefinedMetricSpecification** *(dict) --*

            A predefined metric. You must specify either a predefined metric or a customized metric.

            - **PredefinedMetricType** *(string) --*

              The metric type. The following predefined metrics are available:

              * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.

              * ``ASGAverageNetworkIn`` - Average number of bytes received on all network
              interfaces by the Auto Scaling group.

              * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network
              interfaces by the Auto Scaling group.

              * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an
              Application Load Balancer target group.

            - **ResourceLabel** *(string) --*

              Identifies the resource associated with the metric type. You can't specify a resource
              label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
              group attached to the Auto Scaling group.

              The format is ``app/*load-balancer-name* /*load-balancer-id*
              /targetgroup/*target-group-name* /*target-group-id* `` , where

              * ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load
              balancer ARN, and

              * ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the
              target group ARN.

          - **CustomizedMetricSpecification** *(dict) --*

            A customized metric. You must specify either a predefined metric or a customized metric.

            - **MetricName** *(string) --*

              The name of the metric.

            - **Namespace** *(string) --*

              The namespace of the metric.

            - **Dimensions** *(list) --*

              The dimensions of the metric.

              Conditional: If you published your metric with dimensions, you must specify the same
              dimensions in your scaling policy.

              - *(dict) --*

                Describes the dimension of a metric.

                - **Name** *(string) --*

                  The name of the dimension.

                - **Value** *(string) --*

                  The value of the dimension.

            - **Statistic** *(string) --*

              The statistic of the metric.

            - **Unit** *(string) --*

              The unit of the metric.

          - **TargetValue** *(float) --*

            The target value for the metric.

          - **DisableScaleIn** *(boolean) --*

            Indicates whether scaling in by the target tracking scaling policy is disabled. If
            scaling in is disabled, the target tracking scaling policy doesn't remove instances
            from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove
            instances from the Auto Scaling group. The default is ``false`` .

    - **NextToken** *(string) --*

      A string that indicates that the response contains more items than can be returned in a
      single response. To receive additional items, specify this string for the ``NextToken`` value
      when requesting the next set of items. This value is null when there are no more items to
      return.
    """


_ClientDescribeScalingActivitiesResponseActivitiesTypeDef = TypedDict(
    "_ClientDescribeScalingActivitiesResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": str,
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)


class ClientDescribeScalingActivitiesResponseActivitiesTypeDef(
    _ClientDescribeScalingActivitiesResponseActivitiesTypeDef
):
    """
    Type definition for `ClientDescribeScalingActivitiesResponse` `Activities`

    Describes scaling activity, which is a long-running process that represents a change to
    your Auto Scaling group, such as changing its size or replacing an instance.

    - **ActivityId** *(string) --*

      The ID of the activity.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **Description** *(string) --*

      A friendly, more verbose description of the activity.

    - **Cause** *(string) --*

      The reason the activity began.

    - **StartTime** *(datetime) --*

      The start time of the activity.

    - **EndTime** *(datetime) --*

      The end time of the activity.

    - **StatusCode** *(string) --*

      The current status of the activity.

    - **StatusMessage** *(string) --*

      A friendly, more verbose description of the activity status.

    - **Progress** *(integer) --*

      A value between 0 and 100 that indicates the progress of the activity.

    - **Details** *(string) --*

      The details about the activity.
    """


_ClientDescribeScalingActivitiesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingActivitiesResponseTypeDef",
    {
        "Activities": List[ClientDescribeScalingActivitiesResponseActivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingActivitiesResponseTypeDef(
    _ClientDescribeScalingActivitiesResponseTypeDef
):
    """
    Type definition for `ClientDescribeScalingActivities` `Response`

    - **Activities** *(list) --*

      The scaling activities. Activities are sorted by start time. Activities still in progress are
      described first.

      - *(dict) --*

        Describes scaling activity, which is a long-running process that represents a change to
        your Auto Scaling group, such as changing its size or replacing an instance.

        - **ActivityId** *(string) --*

          The ID of the activity.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **Description** *(string) --*

          A friendly, more verbose description of the activity.

        - **Cause** *(string) --*

          The reason the activity began.

        - **StartTime** *(datetime) --*

          The start time of the activity.

        - **EndTime** *(datetime) --*

          The end time of the activity.

        - **StatusCode** *(string) --*

          The current status of the activity.

        - **StatusMessage** *(string) --*

          A friendly, more verbose description of the activity status.

        - **Progress** *(integer) --*

          A value between 0 and 100 that indicates the progress of the activity.

        - **Details** *(string) --*

          The details about the activity.

    - **NextToken** *(string) --*

      A string that indicates that the response contains more items than can be returned in a
      single response. To receive additional items, specify this string for the ``NextToken`` value
      when requesting the next set of items. This value is null when there are no more items to
      return.
    """


_ClientDescribeScalingProcessTypesResponseProcessesTypeDef = TypedDict(
    "_ClientDescribeScalingProcessTypesResponseProcessesTypeDef",
    {"ProcessName": str},
    total=False,
)


class ClientDescribeScalingProcessTypesResponseProcessesTypeDef(
    _ClientDescribeScalingProcessTypesResponseProcessesTypeDef
):
    """
    Type definition for `ClientDescribeScalingProcessTypesResponse` `Processes`

    Describes a process type.

    For more information, see `Scaling Processes
    <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#process-types>`__
    in the *Amazon EC2 Auto Scaling User Guide* .

    - **ProcessName** *(string) --*

      One of the following processes:

      * ``Launch``

      * ``Terminate``

      * ``AddToLoadBalancer``

      * ``AlarmNotification``

      * ``AZRebalance``

      * ``HealthCheck``

      * ``ReplaceUnhealthy``

      * ``ScheduledActions``
    """


_ClientDescribeScalingProcessTypesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingProcessTypesResponseTypeDef",
    {"Processes": List[ClientDescribeScalingProcessTypesResponseProcessesTypeDef]},
    total=False,
)


class ClientDescribeScalingProcessTypesResponseTypeDef(
    _ClientDescribeScalingProcessTypesResponseTypeDef
):
    """
    Type definition for `ClientDescribeScalingProcessTypes` `Response`

    - **Processes** *(list) --*

      The names of the process types.

      - *(dict) --*

        Describes a process type.

        For more information, see `Scaling Processes
        <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#process-types>`__
        in the *Amazon EC2 Auto Scaling User Guide* .

        - **ProcessName** *(string) --*

          One of the following processes:

          * ``Launch``

          * ``Terminate``

          * ``AddToLoadBalancer``

          * ``AlarmNotification``

          * ``AZRebalance``

          * ``HealthCheck``

          * ``ReplaceUnhealthy``

          * ``ScheduledActions``
    """


_ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "Time": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
    },
    total=False,
)


class ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef(
    _ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef
):
    """
    Type definition for `ClientDescribeScheduledActionsResponse` `ScheduledUpdateGroupActions`

    Describes a scheduled scaling action. Used in response to  DescribeScheduledActions .

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **ScheduledActionName** *(string) --*

      The name of the scheduled action.

    - **ScheduledActionARN** *(string) --*

      The Amazon Resource Name (ARN) of the scheduled action.

    - **Time** *(datetime) --*

      This parameter is no longer used.

    - **StartTime** *(datetime) --*

      The date and time in UTC for this action to start. For example,
      ``"2019-06-01T00:00:00Z"`` .

    - **EndTime** *(datetime) --*

      The date and time in UTC for the recurring schedule to end. For example,
      ``"2019-06-01T00:00:00Z"`` .

    - **Recurrence** *(string) --*

      The recurring schedule for the action, in Unix cron syntax format.

      When ``StartTime`` and ``EndTime`` are specified with ``Recurrence`` , they form the
      boundaries of when the recurring action starts and stops.

    - **MinSize** *(integer) --*

      The minimum number of instances in the Auto Scaling group.

    - **MaxSize** *(integer) --*

      The maximum number of instances in the Auto Scaling group.

    - **DesiredCapacity** *(integer) --*

      The number of instances you prefer to maintain in the group.
    """


_ClientDescribeScheduledActionsResponseTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledUpdateGroupActions": List[
            ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScheduledActionsResponseTypeDef(
    _ClientDescribeScheduledActionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeScheduledActions` `Response`

    - **ScheduledUpdateGroupActions** *(list) --*

      The scheduled actions.

      - *(dict) --*

        Describes a scheduled scaling action. Used in response to  DescribeScheduledActions .

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **ScheduledActionName** *(string) --*

          The name of the scheduled action.

        - **ScheduledActionARN** *(string) --*

          The Amazon Resource Name (ARN) of the scheduled action.

        - **Time** *(datetime) --*

          This parameter is no longer used.

        - **StartTime** *(datetime) --*

          The date and time in UTC for this action to start. For example,
          ``"2019-06-01T00:00:00Z"`` .

        - **EndTime** *(datetime) --*

          The date and time in UTC for the recurring schedule to end. For example,
          ``"2019-06-01T00:00:00Z"`` .

        - **Recurrence** *(string) --*

          The recurring schedule for the action, in Unix cron syntax format.

          When ``StartTime`` and ``EndTime`` are specified with ``Recurrence`` , they form the
          boundaries of when the recurring action starts and stops.

        - **MinSize** *(integer) --*

          The minimum number of instances in the Auto Scaling group.

        - **MaxSize** *(integer) --*

          The maximum number of instances in the Auto Scaling group.

        - **DesiredCapacity** *(integer) --*

          The number of instances you prefer to maintain in the group.

    - **NextToken** *(string) --*

      A string that indicates that the response contains more items than can be returned in a
      single response. To receive additional items, specify this string for the ``NextToken`` value
      when requesting the next set of items. This value is null when there are no more items to
      return.
    """


_ClientDescribeTagsFiltersTypeDef = TypedDict(
    "_ClientDescribeTagsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientDescribeTagsFiltersTypeDef(_ClientDescribeTagsFiltersTypeDef):
    """
    Type definition for `ClientDescribeTags` `Filters`

    Describes a filter.

    - **Name** *(string) --*

      The name of the filter. The valid values are: ``"auto-scaling-group"`` , ``"key"`` ,
      ``"value"`` , and ``"propagate-at-launch"`` .

    - **Values** *(list) --*

      The value of the filter.

      - *(string) --*
    """


_ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagsTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "Key": str,
        "Value": str,
        "PropagateAtLaunch": bool,
    },
    total=False,
)


class ClientDescribeTagsResponseTagsTypeDef(_ClientDescribeTagsResponseTagsTypeDef):
    """
    Type definition for `ClientDescribeTagsResponse` `Tags`

    Describes a tag for an Auto Scaling group.

    - **ResourceId** *(string) --*

      The name of the group.

    - **ResourceType** *(string) --*

      The type of resource. The only supported value is ``auto-scaling-group`` .

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The tag value.

    - **PropagateAtLaunch** *(boolean) --*

      Determines whether the tag is added to new instances as they are launched in the group.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"Tags": List[ClientDescribeTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    Type definition for `ClientDescribeTags` `Response`

    - **Tags** *(list) --*

      One or more tags.

      - *(dict) --*

        Describes a tag for an Auto Scaling group.

        - **ResourceId** *(string) --*

          The name of the group.

        - **ResourceType** *(string) --*

          The type of resource. The only supported value is ``auto-scaling-group`` .

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The tag value.

        - **PropagateAtLaunch** *(boolean) --*

          Determines whether the tag is added to new instances as they are launched in the group.

    - **NextToken** *(string) --*

      A string that indicates that the response contains more items than can be returned in a
      single response. To receive additional items, specify this string for the ``NextToken`` value
      when requesting the next set of items. This value is null when there are no more items to
      return.
    """


_ClientDescribeTerminationPolicyTypesResponseTypeDef = TypedDict(
    "_ClientDescribeTerminationPolicyTypesResponseTypeDef",
    {"TerminationPolicyTypes": List[str]},
    total=False,
)


class ClientDescribeTerminationPolicyTypesResponseTypeDef(
    _ClientDescribeTerminationPolicyTypesResponseTypeDef
):
    """
    Type definition for `ClientDescribeTerminationPolicyTypes` `Response`

    - **TerminationPolicyTypes** *(list) --*

      The termination policies supported by Amazon EC2 Auto Scaling: ``OldestInstance`` ,
      ``OldestLaunchConfiguration`` , ``NewestInstance`` , ``ClosestToNextInstanceHour`` ,
      ``Default`` , ``OldestLaunchTemplate`` , and ``AllocationStrategy`` .

      - *(string) --*
    """


_ClientDetachInstancesResponseActivitiesTypeDef = TypedDict(
    "_ClientDetachInstancesResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": str,
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)


class ClientDetachInstancesResponseActivitiesTypeDef(
    _ClientDetachInstancesResponseActivitiesTypeDef
):
    """
    Type definition for `ClientDetachInstancesResponse` `Activities`

    Describes scaling activity, which is a long-running process that represents a change to
    your Auto Scaling group, such as changing its size or replacing an instance.

    - **ActivityId** *(string) --*

      The ID of the activity.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **Description** *(string) --*

      A friendly, more verbose description of the activity.

    - **Cause** *(string) --*

      The reason the activity began.

    - **StartTime** *(datetime) --*

      The start time of the activity.

    - **EndTime** *(datetime) --*

      The end time of the activity.

    - **StatusCode** *(string) --*

      The current status of the activity.

    - **StatusMessage** *(string) --*

      A friendly, more verbose description of the activity status.

    - **Progress** *(integer) --*

      A value between 0 and 100 that indicates the progress of the activity.

    - **Details** *(string) --*

      The details about the activity.
    """


_ClientDetachInstancesResponseTypeDef = TypedDict(
    "_ClientDetachInstancesResponseTypeDef",
    {"Activities": List[ClientDetachInstancesResponseActivitiesTypeDef]},
    total=False,
)


class ClientDetachInstancesResponseTypeDef(_ClientDetachInstancesResponseTypeDef):
    """
    Type definition for `ClientDetachInstances` `Response`

    - **Activities** *(list) --*

      The activities related to detaching the instances from the Auto Scaling group.

      - *(dict) --*

        Describes scaling activity, which is a long-running process that represents a change to
        your Auto Scaling group, such as changing its size or replacing an instance.

        - **ActivityId** *(string) --*

          The ID of the activity.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **Description** *(string) --*

          A friendly, more verbose description of the activity.

        - **Cause** *(string) --*

          The reason the activity began.

        - **StartTime** *(datetime) --*

          The start time of the activity.

        - **EndTime** *(datetime) --*

          The end time of the activity.

        - **StatusCode** *(string) --*

          The current status of the activity.

        - **StatusMessage** *(string) --*

          A friendly, more verbose description of the activity status.

        - **Progress** *(integer) --*

          A value between 0 and 100 that indicates the progress of the activity.

        - **Details** *(string) --*

          The details about the activity.
    """


_ClientEnterStandbyResponseActivitiesTypeDef = TypedDict(
    "_ClientEnterStandbyResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": str,
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)


class ClientEnterStandbyResponseActivitiesTypeDef(
    _ClientEnterStandbyResponseActivitiesTypeDef
):
    """
    Type definition for `ClientEnterStandbyResponse` `Activities`

    Describes scaling activity, which is a long-running process that represents a change to
    your Auto Scaling group, such as changing its size or replacing an instance.

    - **ActivityId** *(string) --*

      The ID of the activity.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **Description** *(string) --*

      A friendly, more verbose description of the activity.

    - **Cause** *(string) --*

      The reason the activity began.

    - **StartTime** *(datetime) --*

      The start time of the activity.

    - **EndTime** *(datetime) --*

      The end time of the activity.

    - **StatusCode** *(string) --*

      The current status of the activity.

    - **StatusMessage** *(string) --*

      A friendly, more verbose description of the activity status.

    - **Progress** *(integer) --*

      A value between 0 and 100 that indicates the progress of the activity.

    - **Details** *(string) --*

      The details about the activity.
    """


_ClientEnterStandbyResponseTypeDef = TypedDict(
    "_ClientEnterStandbyResponseTypeDef",
    {"Activities": List[ClientEnterStandbyResponseActivitiesTypeDef]},
    total=False,
)


class ClientEnterStandbyResponseTypeDef(_ClientEnterStandbyResponseTypeDef):
    """
    Type definition for `ClientEnterStandby` `Response`

    - **Activities** *(list) --*

      The activities related to moving instances into ``Standby`` mode.

      - *(dict) --*

        Describes scaling activity, which is a long-running process that represents a change to
        your Auto Scaling group, such as changing its size or replacing an instance.

        - **ActivityId** *(string) --*

          The ID of the activity.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **Description** *(string) --*

          A friendly, more verbose description of the activity.

        - **Cause** *(string) --*

          The reason the activity began.

        - **StartTime** *(datetime) --*

          The start time of the activity.

        - **EndTime** *(datetime) --*

          The end time of the activity.

        - **StatusCode** *(string) --*

          The current status of the activity.

        - **StatusMessage** *(string) --*

          A friendly, more verbose description of the activity status.

        - **Progress** *(integer) --*

          A value between 0 and 100 that indicates the progress of the activity.

        - **Details** *(string) --*

          The details about the activity.
    """


_ClientExitStandbyResponseActivitiesTypeDef = TypedDict(
    "_ClientExitStandbyResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": str,
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)


class ClientExitStandbyResponseActivitiesTypeDef(
    _ClientExitStandbyResponseActivitiesTypeDef
):
    """
    Type definition for `ClientExitStandbyResponse` `Activities`

    Describes scaling activity, which is a long-running process that represents a change to
    your Auto Scaling group, such as changing its size or replacing an instance.

    - **ActivityId** *(string) --*

      The ID of the activity.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **Description** *(string) --*

      A friendly, more verbose description of the activity.

    - **Cause** *(string) --*

      The reason the activity began.

    - **StartTime** *(datetime) --*

      The start time of the activity.

    - **EndTime** *(datetime) --*

      The end time of the activity.

    - **StatusCode** *(string) --*

      The current status of the activity.

    - **StatusMessage** *(string) --*

      A friendly, more verbose description of the activity status.

    - **Progress** *(integer) --*

      A value between 0 and 100 that indicates the progress of the activity.

    - **Details** *(string) --*

      The details about the activity.
    """


_ClientExitStandbyResponseTypeDef = TypedDict(
    "_ClientExitStandbyResponseTypeDef",
    {"Activities": List[ClientExitStandbyResponseActivitiesTypeDef]},
    total=False,
)


class ClientExitStandbyResponseTypeDef(_ClientExitStandbyResponseTypeDef):
    """
    Type definition for `ClientExitStandby` `Response`

    - **Activities** *(list) --*

      The activities related to moving instances out of ``Standby`` mode.

      - *(dict) --*

        Describes scaling activity, which is a long-running process that represents a change to
        your Auto Scaling group, such as changing its size or replacing an instance.

        - **ActivityId** *(string) --*

          The ID of the activity.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **Description** *(string) --*

          A friendly, more verbose description of the activity.

        - **Cause** *(string) --*

          The reason the activity began.

        - **StartTime** *(datetime) --*

          The start time of the activity.

        - **EndTime** *(datetime) --*

          The end time of the activity.

        - **StatusCode** *(string) --*

          The current status of the activity.

        - **StatusMessage** *(string) --*

          A friendly, more verbose description of the activity status.

        - **Progress** *(integer) --*

          A value between 0 and 100 that indicates the progress of the activity.

        - **Details** *(string) --*

          The details about the activity.
    """


_ClientPutScalingPolicyResponseAlarmsTypeDef = TypedDict(
    "_ClientPutScalingPolicyResponseAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)


class ClientPutScalingPolicyResponseAlarmsTypeDef(
    _ClientPutScalingPolicyResponseAlarmsTypeDef
):
    """
    Type definition for `ClientPutScalingPolicyResponse` `Alarms`

    Describes an alarm.

    - **AlarmName** *(string) --*

      The name of the alarm.

    - **AlarmARN** *(string) --*

      The Amazon Resource Name (ARN) of the alarm.
    """


_ClientPutScalingPolicyResponseTypeDef = TypedDict(
    "_ClientPutScalingPolicyResponseTypeDef",
    {"PolicyARN": str, "Alarms": List[ClientPutScalingPolicyResponseAlarmsTypeDef]},
    total=False,
)


class ClientPutScalingPolicyResponseTypeDef(_ClientPutScalingPolicyResponseTypeDef):
    """
    Type definition for `ClientPutScalingPolicy` `Response`

    Contains the output of PutScalingPolicy.

    - **PolicyARN** *(string) --*

      The Amazon Resource Name (ARN) of the policy.

    - **Alarms** *(list) --*

      The CloudWatch alarms created for the target tracking scaling policy.

      - *(dict) --*

        Describes an alarm.

        - **AlarmName** *(string) --*

          The name of the alarm.

        - **AlarmARN** *(string) --*

          The Amazon Resource Name (ARN) of the alarm.
    """


_RequiredClientPutScalingPolicyStepAdjustmentsTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyStepAdjustmentsTypeDef", {"ScalingAdjustment": int}
)
_OptionalClientPutScalingPolicyStepAdjustmentsTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyStepAdjustmentsTypeDef",
    {"MetricIntervalLowerBound": float, "MetricIntervalUpperBound": float},
    total=False,
)


class ClientPutScalingPolicyStepAdjustmentsTypeDef(
    _RequiredClientPutScalingPolicyStepAdjustmentsTypeDef,
    _OptionalClientPutScalingPolicyStepAdjustmentsTypeDef,
):
    """
    Type definition for `ClientPutScalingPolicy` `StepAdjustments`

    Describes an adjustment based on the difference between the value of the aggregated CloudWatch
    metric and the breach threshold that you've defined for the alarm. Used in combination with
    PutScalingPolicy .

    For the following examples, suppose that you have an alarm with a breach threshold of 50:

    * To trigger the adjustment when the metric is greater than or equal to 50 and less than 60,
    specify a lower bound of 0 and an upper bound of 10.

    * To trigger the adjustment when the metric is greater than 40 and less than or equal to 50,
    specify a lower bound of -10 and an upper bound of 0.

    There are a few rules for the step adjustments for your step policy:

    * The ranges of your step adjustments can't overlap or have a gap.

    * At most, one step adjustment can have a null lower bound. If one step adjustment has a
    negative lower bound, then there must be a step adjustment with a null lower bound.

    * At most, one step adjustment can have a null upper bound. If one step adjustment has a
    positive upper bound, then there must be a step adjustment with a null upper bound.

    * The upper and lower bound can't be null in the same step adjustment.

    - **MetricIntervalLowerBound** *(float) --*

      The lower bound for the difference between the alarm threshold and the CloudWatch metric. If
      the metric value is above the breach threshold, the lower bound is inclusive (the metric must
      be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive
      (the metric must be greater than the threshold plus the lower bound). A null value indicates
      negative infinity.

    - **MetricIntervalUpperBound** *(float) --*

      The upper bound for the difference between the alarm threshold and the CloudWatch metric. If
      the metric value is above the breach threshold, the upper bound is exclusive (the metric must
      be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must
      be less than or equal to the threshold plus the upper bound). A null value indicates positive
      infinity.

      The upper bound must be greater than the lower bound.

    - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

      The amount by which to scale, based on the specified adjustment type. A positive value adds
      to the current capacity while a negative number removes from the current capacity.
    """


_ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
)


class ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecification` `Dimensions`

    Describes the dimension of a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the dimension.
    """


_RequiredClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    {"MetricName": str, "Namespace": str, "Statistic": str},
)
_OptionalClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "Dimensions": List[
            ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Unit": str,
    },
    total=False,
)


class ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef(
    _RequiredClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
    _OptionalClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientPutScalingPolicyTargetTrackingConfiguration` `CustomizedMetricSpecification`

    A customized metric. You must specify either a predefined metric or a customized metric.

    - **MetricName** *(string) --* **[REQUIRED]**

      The name of the metric.

    - **Namespace** *(string) --* **[REQUIRED]**

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the same
      dimensions in your scaling policy.

      - *(dict) --*

        Describes the dimension of a metric.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the dimension.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the dimension.

    - **Statistic** *(string) --* **[REQUIRED]**

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_RequiredClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {"PredefinedMetricType": str},
)
_OptionalClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {"ResourceLabel": str},
    total=False,
)


class ClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef(
    _RequiredClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
    _OptionalClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientPutScalingPolicyTargetTrackingConfiguration` `PredefinedMetricSpecification`

    A predefined metric. You must specify either a predefined metric or a customized metric.

    - **PredefinedMetricType** *(string) --* **[REQUIRED]**

      The metric type. The following predefined metrics are available:

      * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.

      * ``ASGAverageNetworkIn`` - Average number of bytes received on all network interfaces by the
      Auto Scaling group.

      * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network interfaces by
      the Auto Scaling group.

      * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an Application
      Load Balancer target group.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a resource label
      unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group attached
      to the Auto Scaling group.

      The format is ``app/*load-balancer-name* /*load-balancer-id* /targetgroup/*target-group-name*
      /*target-group-id* `` , where

      * ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load balancer
      ARN, and

      * ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the target
      group ARN.
    """


_RequiredClientPutScalingPolicyTargetTrackingConfigurationTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyTargetTrackingConfigurationTypeDef",
    {"TargetValue": float},
)
_OptionalClientPutScalingPolicyTargetTrackingConfigurationTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "DisableScaleIn": bool,
    },
    total=False,
)


class ClientPutScalingPolicyTargetTrackingConfigurationTypeDef(
    _RequiredClientPutScalingPolicyTargetTrackingConfigurationTypeDef,
    _OptionalClientPutScalingPolicyTargetTrackingConfigurationTypeDef,
):
    """
    Type definition for `ClientPutScalingPolicy` `TargetTrackingConfiguration`

    A target tracking scaling policy. Includes support for predefined or customized metrics.

    For more information, see `TargetTrackingConfiguration
    <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TargetTrackingConfiguration.html>`__
    in the *Amazon EC2 Auto Scaling API Reference* .

    Conditional: If you specify ``TargetTrackingScaling`` for the policy type, you must specify this
    parameter. (Not used with any other policy type.)

    - **PredefinedMetricSpecification** *(dict) --*

      A predefined metric. You must specify either a predefined metric or a customized metric.

      - **PredefinedMetricType** *(string) --* **[REQUIRED]**

        The metric type. The following predefined metrics are available:

        * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.

        * ``ASGAverageNetworkIn`` - Average number of bytes received on all network interfaces by the
        Auto Scaling group.

        * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network interfaces by
        the Auto Scaling group.

        * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an Application
        Load Balancer target group.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a resource label
        unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group attached
        to the Auto Scaling group.

        The format is ``app/*load-balancer-name* /*load-balancer-id* /targetgroup/*target-group-name*
        /*target-group-id* `` , where

        * ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load balancer
        ARN, and

        * ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the target
        group ARN.

    - **CustomizedMetricSpecification** *(dict) --*

      A customized metric. You must specify either a predefined metric or a customized metric.

      - **MetricName** *(string) --* **[REQUIRED]**

        The name of the metric.

      - **Namespace** *(string) --* **[REQUIRED]**

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the same
        dimensions in your scaling policy.

        - *(dict) --*

          Describes the dimension of a metric.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the dimension.

          - **Value** *(string) --* **[REQUIRED]**

            The value of the dimension.

      - **Statistic** *(string) --* **[REQUIRED]**

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **TargetValue** *(float) --* **[REQUIRED]**

      The target value for the metric.

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scaling in by the target tracking scaling policy is disabled. If scaling in
      is disabled, the target tracking scaling policy doesn't remove instances from the Auto Scaling
      group. Otherwise, the target tracking scaling policy can remove instances from the Auto Scaling
      group. The default is ``false`` .
    """


_ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef = TypedDict(
    "_ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": str,
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)


class ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef(
    _ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef
):
    """
    Type definition for `ClientTerminateInstanceInAutoScalingGroupResponse` `Activity`

    A scaling activity.

    - **ActivityId** *(string) --*

      The ID of the activity.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **Description** *(string) --*

      A friendly, more verbose description of the activity.

    - **Cause** *(string) --*

      The reason the activity began.

    - **StartTime** *(datetime) --*

      The start time of the activity.

    - **EndTime** *(datetime) --*

      The end time of the activity.

    - **StatusCode** *(string) --*

      The current status of the activity.

    - **StatusMessage** *(string) --*

      A friendly, more verbose description of the activity status.

    - **Progress** *(integer) --*

      A value between 0 and 100 that indicates the progress of the activity.

    - **Details** *(string) --*

      The details about the activity.
    """


_ClientTerminateInstanceInAutoScalingGroupResponseTypeDef = TypedDict(
    "_ClientTerminateInstanceInAutoScalingGroupResponseTypeDef",
    {"Activity": ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef},
    total=False,
)


class ClientTerminateInstanceInAutoScalingGroupResponseTypeDef(
    _ClientTerminateInstanceInAutoScalingGroupResponseTypeDef
):
    """
    Type definition for `ClientTerminateInstanceInAutoScalingGroup` `Response`

    - **Activity** *(dict) --*

      A scaling activity.

      - **ActivityId** *(string) --*

        The ID of the activity.

      - **AutoScalingGroupName** *(string) --*

        The name of the Auto Scaling group.

      - **Description** *(string) --*

        A friendly, more verbose description of the activity.

      - **Cause** *(string) --*

        The reason the activity began.

      - **StartTime** *(datetime) --*

        The start time of the activity.

      - **EndTime** *(datetime) --*

        The end time of the activity.

      - **StatusCode** *(string) --*

        The current status of the activity.

      - **StatusMessage** *(string) --*

        A friendly, more verbose description of the activity status.

      - **Progress** *(integer) --*

        A value between 0 and 100 that indicates the progress of the activity.

      - **Details** *(string) --*

        The details about the activity.
    """


_ClientUpdateAutoScalingGroupLaunchTemplateTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientUpdateAutoScalingGroupLaunchTemplateTypeDef(
    _ClientUpdateAutoScalingGroupLaunchTemplateTypeDef
):
    """
    Type definition for `ClientUpdateAutoScalingGroup` `LaunchTemplate`

    The launch template and version to use to specify the updates. If you specify ``LaunchTemplate``
    in your update request, you can't specify ``LaunchConfigurationName`` or ``MixedInstancesPolicy``
    .

    For more information, see `LaunchTemplateSpecification
    <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_LaunchTemplateSpecification.html>`__
    in the *Amazon EC2 Auto Scaling API Reference* .

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a template ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2
      Auto Scaling selects the latest version of the launch template when launching instances. If the
      value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch
      template when launching instances. The default value is ``$Default`` .
    """


_ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)


class ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef(
    _ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef
):
    """
    Type definition for `ClientUpdateAutoScalingGroupMixedInstancesPolicy` `InstancesDistribution`

    The instances distribution to use.

    If you leave this parameter unspecified, the value for each parameter in
    ``InstancesDistribution`` uses a default value.

    - **OnDemandAllocationStrategy** *(string) --*

      Indicates how to allocate instance types to fulfill On-Demand capacity.

      The only valid value is ``prioritized`` , which is also the default value. This strategy uses
      the order of instance type overrides for the  LaunchTemplate to define the launch priority of
      each instance type. The first instance type in the array is prioritized higher than the last.
      If all your On-Demand capacity cannot be fulfilled using your highest priority instance, then
      the Auto Scaling groups launches the remaining capacity using the second priority instance
      type, and so on.

    - **OnDemandBaseCapacity** *(integer) --*

      The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand
      Instances. This base portion is provisioned first as your group scales.

      Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched as a
      percentage of the Auto Scaling group's desired capacity, per the
      ``OnDemandPercentageAboveBaseCapacity`` setting.

      .. note::

        An update to this setting means a gradual replacement of instances to maintain the
        specified number of On-Demand Instances for your base capacity. When replacing instances,
        Amazon EC2 Auto Scaling launches new instances before terminating the old ones.

    - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

      Controls the percentages of On-Demand Instances and Spot Instances for your additional
      capacity beyond ``OnDemandBaseCapacity`` .

      Default if not set is 100. If you leave it set to 100, the percentages are 100% for On-Demand
      Instances and 0% for Spot Instances.

      .. note::

        An update to this setting means a gradual replacement of instances to maintain the
        percentage of On-Demand Instances for your additional capacity above the base capacity.
        When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating
        the old ones.

      Valid Range: Minimum value of 0. Maximum value of 100.

    - **SpotAllocationStrategy** *(string) --*

      Indicates how to allocate instances across Spot Instance pools.

      If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches instances
      using the Spot pools with the lowest price, and evenly allocates your instances across the
      number of Spot pools that you specify. If the allocation strategy is ``capacity-optimized`` ,
      the Auto Scaling group launches instances using Spot pools that are optimally chosen based on
      the available Spot capacity.

      The default Spot allocation strategy for calls that you make through the API, the AWS CLI, or
      the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for the AWS
      Management Console is ``capacity-optimized`` .

      Valid values: ``lowest-price`` | ``capacity-optimized``

    - **SpotInstancePools** *(integer) --*

      The number of Spot Instance pools across which to allocate your Spot Instances. The Spot
      pools are determined from the different instance types in the Overrides array of
      LaunchTemplate . Default if not set is 2.

      Used only when the Spot allocation strategy is ``lowest-price`` .

      Valid Range: Minimum value of 1. Maximum value of 20.

    - **SpotMaxPrice** *(string) --*

      The maximum price per unit hour that you are willing to pay for a Spot Instance. If you leave
      the value of this parameter blank (which is the default), the maximum Spot price is set at
      the On-Demand price.

      To remove a value that you previously set, include the parameter but leave the value blank.
    """


_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(
    _ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
):
    """
    Type definition for `ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplate` `LaunchTemplateSpecification`

    The launch template to use. You must specify either the launch template ID or launch template
    name in the request.

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a template ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon
      EC2 Auto Scaling selects the latest version of the launch template when launching
      instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default
      version of the launch template when launching instances. The default value is ``$Default`` .
    """


_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)


class ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef(
    _ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
):
    """
    Type definition for `ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplate` `Overrides`

    Describes an override for a launch template.

    - **InstanceType** *(string) --*

      The instance type.

      For information about available instance types, see `Available Instance Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
      in the *Amazon Elastic Compute Cloud User Guide.*

    - **WeightedCapacity** *(string) --*

      The number of capacity units, which gives the instance type a proportional weight to
      other instance types. For example, larger instance types are generally weighted more than
      smaller instance types. These are the same units that you chose to set the desired
      capacity in terms of instances, or a performance attribute such as vCPUs, memory, or I/O.

      Valid Range: Minimum value of 1. Maximum value of 999.
    """


_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef(
    _ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef
):
    """
    Type definition for `ClientUpdateAutoScalingGroupMixedInstancesPolicy` `LaunchTemplate`

    The launch template and instance types (overrides).

    This parameter must be specified when creating a mixed instances policy.

    - **LaunchTemplateSpecification** *(dict) --*

      The launch template to use. You must specify either the launch template ID or launch template
      name in the request.

      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template name.

      - **LaunchTemplateName** *(string) --*

        The name of the launch template. You must specify either a template name or a template ID.

      - **Version** *(string) --*

        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon
        EC2 Auto Scaling selects the latest version of the launch template when launching
        instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default
        version of the launch template when launching instances. The default value is ``$Default`` .

    - **Overrides** *(list) --*

      An optional setting. Any parameters that you specify override the same parameters in the
      launch template. Currently, the only supported override is instance type. You can specify
      between 1 and 20 instance types.

      - *(dict) --*

        Describes an override for a launch template.

        - **InstanceType** *(string) --*

          The instance type.

          For information about available instance types, see `Available Instance Types
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
          in the *Amazon Elastic Compute Cloud User Guide.*

        - **WeightedCapacity** *(string) --*

          The number of capacity units, which gives the instance type a proportional weight to
          other instance types. For example, larger instance types are generally weighted more than
          smaller instance types. These are the same units that you chose to set the desired
          capacity in terms of instances, or a performance attribute such as vCPUs, memory, or I/O.

          Valid Range: Minimum value of 1. Maximum value of 999.
    """


_ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef = TypedDict(
    "_ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)


class ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef(
    _ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef
):
    """
    Type definition for `ClientUpdateAutoScalingGroup` `MixedInstancesPolicy`

    An embedded object that specifies a mixed instances policy.

    In your call to ``UpdateAutoScalingGroup`` , you can make changes to the policy that is
    specified. All optional parameters are left unchanged if not specified.

    For more information, see `MixedInstancesPolicy
    <https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_MixedInstancesPolicy.html>`__ in
    the *Amazon EC2 Auto Scaling API Reference* and `Auto Scaling Groups with Multiple Instance Types
    and Purchase Options
    <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html>`__ in the
    *Amazon EC2 Auto Scaling User Guide* .

    - **LaunchTemplate** *(dict) --*

      The launch template and instance types (overrides).

      This parameter must be specified when creating a mixed instances policy.

      - **LaunchTemplateSpecification** *(dict) --*

        The launch template to use. You must specify either the launch template ID or launch template
        name in the request.

        - **LaunchTemplateId** *(string) --*

          The ID of the launch template. You must specify either a template ID or a template name.

        - **LaunchTemplateName** *(string) --*

          The name of the launch template. You must specify either a template name or a template ID.

        - **Version** *(string) --*

          The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon
          EC2 Auto Scaling selects the latest version of the launch template when launching
          instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default
          version of the launch template when launching instances. The default value is ``$Default`` .

      - **Overrides** *(list) --*

        An optional setting. Any parameters that you specify override the same parameters in the
        launch template. Currently, the only supported override is instance type. You can specify
        between 1 and 20 instance types.

        - *(dict) --*

          Describes an override for a launch template.

          - **InstanceType** *(string) --*

            The instance type.

            For information about available instance types, see `Available Instance Types
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
            in the *Amazon Elastic Compute Cloud User Guide.*

          - **WeightedCapacity** *(string) --*

            The number of capacity units, which gives the instance type a proportional weight to
            other instance types. For example, larger instance types are generally weighted more than
            smaller instance types. These are the same units that you chose to set the desired
            capacity in terms of instances, or a performance attribute such as vCPUs, memory, or I/O.

            Valid Range: Minimum value of 1. Maximum value of 999.

    - **InstancesDistribution** *(dict) --*

      The instances distribution to use.

      If you leave this parameter unspecified, the value for each parameter in
      ``InstancesDistribution`` uses a default value.

      - **OnDemandAllocationStrategy** *(string) --*

        Indicates how to allocate instance types to fulfill On-Demand capacity.

        The only valid value is ``prioritized`` , which is also the default value. This strategy uses
        the order of instance type overrides for the  LaunchTemplate to define the launch priority of
        each instance type. The first instance type in the array is prioritized higher than the last.
        If all your On-Demand capacity cannot be fulfilled using your highest priority instance, then
        the Auto Scaling groups launches the remaining capacity using the second priority instance
        type, and so on.

      - **OnDemandBaseCapacity** *(integer) --*

        The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand
        Instances. This base portion is provisioned first as your group scales.

        Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched as a
        percentage of the Auto Scaling group's desired capacity, per the
        ``OnDemandPercentageAboveBaseCapacity`` setting.

        .. note::

          An update to this setting means a gradual replacement of instances to maintain the
          specified number of On-Demand Instances for your base capacity. When replacing instances,
          Amazon EC2 Auto Scaling launches new instances before terminating the old ones.

      - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

        Controls the percentages of On-Demand Instances and Spot Instances for your additional
        capacity beyond ``OnDemandBaseCapacity`` .

        Default if not set is 100. If you leave it set to 100, the percentages are 100% for On-Demand
        Instances and 0% for Spot Instances.

        .. note::

          An update to this setting means a gradual replacement of instances to maintain the
          percentage of On-Demand Instances for your additional capacity above the base capacity.
          When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating
          the old ones.

        Valid Range: Minimum value of 0. Maximum value of 100.

      - **SpotAllocationStrategy** *(string) --*

        Indicates how to allocate instances across Spot Instance pools.

        If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches instances
        using the Spot pools with the lowest price, and evenly allocates your instances across the
        number of Spot pools that you specify. If the allocation strategy is ``capacity-optimized`` ,
        the Auto Scaling group launches instances using Spot pools that are optimally chosen based on
        the available Spot capacity.

        The default Spot allocation strategy for calls that you make through the API, the AWS CLI, or
        the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for the AWS
        Management Console is ``capacity-optimized`` .

        Valid values: ``lowest-price`` | ``capacity-optimized``

      - **SpotInstancePools** *(integer) --*

        The number of Spot Instance pools across which to allocate your Spot Instances. The Spot
        pools are determined from the different instance types in the Overrides array of
        LaunchTemplate . Default if not set is 2.

        Used only when the Spot allocation strategy is ``lowest-price`` .

        Valid Range: Minimum value of 1. Maximum value of 20.

      - **SpotMaxPrice** *(string) --*

        The maximum price per unit hour that you are willing to pay for a Spot Instance. If you leave
        the value of this parameter blank (which is the default), the maximum Spot price is set at
        the On-Demand price.

        To remove a value that you previously set, include the parameter but leave the value blank.
    """


_DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef(
    _DescribeAutoScalingGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef",
    {"Metric": str, "Granularity": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroups` `EnabledMetrics`

    Describes an enabled metric.

    - **Metric** *(string) --*

      One of the following metrics:

      * ``GroupMinSize``

      * ``GroupMaxSize``

      * ``GroupDesiredCapacity``

      * ``GroupInServiceInstances``

      * ``GroupPendingInstances``

      * ``GroupStandbyInstances``

      * ``GroupTerminatingInstances``

      * ``GroupTotalInstances``

    - **Granularity** *(string) --*

      The granularity of the metric. The only valid value is ``1Minute`` .
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstances` `LaunchTemplate`

    The launch template for the instance.

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template
      name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a
      template ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
      Amazon EC2 Auto Scaling selects the latest version of the launch template when
      launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
      the default version of the launch template when launching instances. The default
      value is ``$Default`` .
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef,
        "ProtectedFromScaleIn": bool,
        "WeightedCapacity": str,
    },
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroups` `Instances`

    Describes an EC2 instance.

    - **InstanceId** *(string) --*

      The ID of the instance.

    - **InstanceType** *(string) --*

      The instance type of the EC2 instance.

    - **AvailabilityZone** *(string) --*

      The Availability Zone in which the instance is running.

    - **LifecycleState** *(string) --*

      A description of the current lifecycle state. The ``Quarantined`` state is not used.

    - **HealthStatus** *(string) --*

      The last reported health status of the instance. "Healthy" means that the instance is
      healthy and should remain in service. "Unhealthy" means that the instance is
      unhealthy and that Amazon EC2 Auto Scaling should terminate and replace it.

    - **LaunchConfigurationName** *(string) --*

      The launch configuration associated with the instance.

    - **LaunchTemplate** *(dict) --*

      The launch template for the instance.

      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template
        name.

      - **LaunchTemplateName** *(string) --*

        The name of the launch template. You must specify either a template name or a
        template ID.

      - **Version** *(string) --*

        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
        Amazon EC2 Auto Scaling selects the latest version of the launch template when
        launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
        the default version of the launch template when launching instances. The default
        value is ``$Default`` .

    - **ProtectedFromScaleIn** *(boolean) --*

      Indicates whether the instance is protected from termination by Amazon EC2 Auto
      Scaling when scaling in.

    - **WeightedCapacity** *(string) --*

      The number of capacity units contributed by the instance based on its instance type.

      Valid Range: Minimum value of 1. Maximum value of 999.
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroups` `LaunchTemplate`

    The launch template for the group.

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a template
      ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
      Amazon EC2 Auto Scaling selects the latest version of the launch template when
      launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
      default version of the launch template when launching instances. The default value is
      ``$Default`` .
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicy` `InstancesDistribution`

    The instances distribution to use.

    If you leave this parameter unspecified, the value for each parameter in
    ``InstancesDistribution`` uses a default value.

    - **OnDemandAllocationStrategy** *(string) --*

      Indicates how to allocate instance types to fulfill On-Demand capacity.

      The only valid value is ``prioritized`` , which is also the default value. This
      strategy uses the order of instance type overrides for the  LaunchTemplate to define
      the launch priority of each instance type. The first instance type in the array is
      prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled
      using your highest priority instance, then the Auto Scaling groups launches the
      remaining capacity using the second priority instance type, and so on.

    - **OnDemandBaseCapacity** *(integer) --*

      The minimum amount of the Auto Scaling group's capacity that must be fulfilled by
      On-Demand Instances. This base portion is provisioned first as your group scales.

      Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched
      as a percentage of the Auto Scaling group's desired capacity, per the
      ``OnDemandPercentageAboveBaseCapacity`` setting.

      .. note::

        An update to this setting means a gradual replacement of instances to maintain the
        specified number of On-Demand Instances for your base capacity. When replacing
        instances, Amazon EC2 Auto Scaling launches new instances before terminating the
        old ones.

    - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

      Controls the percentages of On-Demand Instances and Spot Instances for your
      additional capacity beyond ``OnDemandBaseCapacity`` .

      Default if not set is 100. If you leave it set to 100, the percentages are 100% for
      On-Demand Instances and 0% for Spot Instances.

      .. note::

        An update to this setting means a gradual replacement of instances to maintain the
        percentage of On-Demand Instances for your additional capacity above the base
        capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances
        before terminating the old ones.

      Valid Range: Minimum value of 0. Maximum value of 100.

    - **SpotAllocationStrategy** *(string) --*

      Indicates how to allocate instances across Spot Instance pools.

      If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches
      instances using the Spot pools with the lowest price, and evenly allocates your
      instances across the number of Spot pools that you specify. If the allocation
      strategy is ``capacity-optimized`` , the Auto Scaling group launches instances using
      Spot pools that are optimally chosen based on the available Spot capacity.

      The default Spot allocation strategy for calls that you make through the API, the AWS
      CLI, or the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for
      the AWS Management Console is ``capacity-optimized`` .

      Valid values: ``lowest-price`` | ``capacity-optimized``

    - **SpotInstancePools** *(integer) --*

      The number of Spot Instance pools across which to allocate your Spot Instances. The
      Spot pools are determined from the different instance types in the Overrides array of
       LaunchTemplate . Default if not set is 2.

      Used only when the Spot allocation strategy is ``lowest-price`` .

      Valid Range: Minimum value of 1. Maximum value of 20.

    - **SpotMaxPrice** *(string) --*

      The maximum price per unit hour that you are willing to pay for a Spot Instance. If
      you leave the value of this parameter blank (which is the default), the maximum Spot
      price is set at the On-Demand price.

      To remove a value that you previously set, include the parameter but leave the value
      blank.
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplate` `LaunchTemplateSpecification`

    The launch template to use. You must specify either the launch template ID or launch
    template name in the request.

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template
      name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a
      template ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
      Amazon EC2 Auto Scaling selects the latest version of the launch template when
      launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
      the default version of the launch template when launching instances. The default
      value is ``$Default`` .
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplate` `Overrides`

    Describes an override for a launch template.

    - **InstanceType** *(string) --*

      The instance type.

      For information about available instance types, see `Available Instance Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
      in the *Amazon Elastic Compute Cloud User Guide.*

    - **WeightedCapacity** *(string) --*

      The number of capacity units, which gives the instance type a proportional weight
      to other instance types. For example, larger instance types are generally
      weighted more than smaller instance types. These are the same units that you
      chose to set the desired capacity in terms of instances, or a performance
      attribute such as vCPUs, memory, or I/O.

      Valid Range: Minimum value of 1. Maximum value of 999.
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicy` `LaunchTemplate`

    The launch template and instance types (overrides).

    This parameter must be specified when creating a mixed instances policy.

    - **LaunchTemplateSpecification** *(dict) --*

      The launch template to use. You must specify either the launch template ID or launch
      template name in the request.

      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template
        name.

      - **LaunchTemplateName** *(string) --*

        The name of the launch template. You must specify either a template name or a
        template ID.

      - **Version** *(string) --*

        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
        Amazon EC2 Auto Scaling selects the latest version of the launch template when
        launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
        the default version of the launch template when launching instances. The default
        value is ``$Default`` .

    - **Overrides** *(list) --*

      An optional setting. Any parameters that you specify override the same parameters in
      the launch template. Currently, the only supported override is instance type. You can
      specify between 1 and 20 instance types.

      - *(dict) --*

        Describes an override for a launch template.

        - **InstanceType** *(string) --*

          The instance type.

          For information about available instance types, see `Available Instance Types
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
          in the *Amazon Elastic Compute Cloud User Guide.*

        - **WeightedCapacity** *(string) --*

          The number of capacity units, which gives the instance type a proportional weight
          to other instance types. For example, larger instance types are generally
          weighted more than smaller instance types. These are the same units that you
          chose to set the desired capacity in terms of instances, or a performance
          attribute such as vCPUs, memory, or I/O.

          Valid Range: Minimum value of 1. Maximum value of 999.
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroups` `MixedInstancesPolicy`

    The mixed instances policy for the group.

    - **LaunchTemplate** *(dict) --*

      The launch template and instance types (overrides).

      This parameter must be specified when creating a mixed instances policy.

      - **LaunchTemplateSpecification** *(dict) --*

        The launch template to use. You must specify either the launch template ID or launch
        template name in the request.

        - **LaunchTemplateId** *(string) --*

          The ID of the launch template. You must specify either a template ID or a template
          name.

        - **LaunchTemplateName** *(string) --*

          The name of the launch template. You must specify either a template name or a
          template ID.

        - **Version** *(string) --*

          The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
          Amazon EC2 Auto Scaling selects the latest version of the launch template when
          launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
          the default version of the launch template when launching instances. The default
          value is ``$Default`` .

      - **Overrides** *(list) --*

        An optional setting. Any parameters that you specify override the same parameters in
        the launch template. Currently, the only supported override is instance type. You can
        specify between 1 and 20 instance types.

        - *(dict) --*

          Describes an override for a launch template.

          - **InstanceType** *(string) --*

            The instance type.

            For information about available instance types, see `Available Instance Types
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
            in the *Amazon Elastic Compute Cloud User Guide.*

          - **WeightedCapacity** *(string) --*

            The number of capacity units, which gives the instance type a proportional weight
            to other instance types. For example, larger instance types are generally
            weighted more than smaller instance types. These are the same units that you
            chose to set the desired capacity in terms of instances, or a performance
            attribute such as vCPUs, memory, or I/O.

            Valid Range: Minimum value of 1. Maximum value of 999.

    - **InstancesDistribution** *(dict) --*

      The instances distribution to use.

      If you leave this parameter unspecified, the value for each parameter in
      ``InstancesDistribution`` uses a default value.

      - **OnDemandAllocationStrategy** *(string) --*

        Indicates how to allocate instance types to fulfill On-Demand capacity.

        The only valid value is ``prioritized`` , which is also the default value. This
        strategy uses the order of instance type overrides for the  LaunchTemplate to define
        the launch priority of each instance type. The first instance type in the array is
        prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled
        using your highest priority instance, then the Auto Scaling groups launches the
        remaining capacity using the second priority instance type, and so on.

      - **OnDemandBaseCapacity** *(integer) --*

        The minimum amount of the Auto Scaling group's capacity that must be fulfilled by
        On-Demand Instances. This base portion is provisioned first as your group scales.

        Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched
        as a percentage of the Auto Scaling group's desired capacity, per the
        ``OnDemandPercentageAboveBaseCapacity`` setting.

        .. note::

          An update to this setting means a gradual replacement of instances to maintain the
          specified number of On-Demand Instances for your base capacity. When replacing
          instances, Amazon EC2 Auto Scaling launches new instances before terminating the
          old ones.

      - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

        Controls the percentages of On-Demand Instances and Spot Instances for your
        additional capacity beyond ``OnDemandBaseCapacity`` .

        Default if not set is 100. If you leave it set to 100, the percentages are 100% for
        On-Demand Instances and 0% for Spot Instances.

        .. note::

          An update to this setting means a gradual replacement of instances to maintain the
          percentage of On-Demand Instances for your additional capacity above the base
          capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances
          before terminating the old ones.

        Valid Range: Minimum value of 0. Maximum value of 100.

      - **SpotAllocationStrategy** *(string) --*

        Indicates how to allocate instances across Spot Instance pools.

        If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches
        instances using the Spot pools with the lowest price, and evenly allocates your
        instances across the number of Spot pools that you specify. If the allocation
        strategy is ``capacity-optimized`` , the Auto Scaling group launches instances using
        Spot pools that are optimally chosen based on the available Spot capacity.

        The default Spot allocation strategy for calls that you make through the API, the AWS
        CLI, or the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for
        the AWS Management Console is ``capacity-optimized`` .

        Valid values: ``lowest-price`` | ``capacity-optimized``

      - **SpotInstancePools** *(integer) --*

        The number of Spot Instance pools across which to allocate your Spot Instances. The
        Spot pools are determined from the different instance types in the Overrides array of
         LaunchTemplate . Default if not set is 2.

        Used only when the Spot allocation strategy is ``lowest-price`` .

        Valid Range: Minimum value of 1. Maximum value of 20.

      - **SpotMaxPrice** *(string) --*

        The maximum price per unit hour that you are willing to pay for a Spot Instance. If
        you leave the value of this parameter blank (which is the default), the maximum Spot
        price is set at the On-Demand price.

        To remove a value that you previously set, include the parameter but leave the value
        blank.
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    {"ProcessName": str, "SuspensionReason": str},
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroups` `SuspendedProcesses`

    Describes an automatic scaling process that has been suspended. For more information,
    see  ProcessType .

    - **ProcessName** *(string) --*

      The name of the suspended process.

    - **SuspensionReason** *(string) --*

      The reason that the process was suspended.
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "Key": str,
        "Value": str,
        "PropagateAtLaunch": bool,
    },
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponseAutoScalingGroups` `Tags`

    Describes a tag for an Auto Scaling group.

    - **ResourceId** *(string) --*

      The name of the group.

    - **ResourceType** *(string) --*

      The type of resource. The only supported value is ``auto-scaling-group`` .

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The tag value.

    - **PropagateAtLaunch** *(boolean) --*

      Determines whether the tag is added to new instances as they are launched in the
      group.
    """


_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef",
    {
        "AutoScalingGroupName": str,
        "AutoScalingGroupARN": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsLaunchTemplateTypeDef,
        "MixedInstancesPolicy": DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsMixedInstancesPolicyTypeDef,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "LoadBalancerNames": List[str],
        "TargetGroupARNs": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "Instances": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsInstancesTypeDef
        ],
        "CreatedTime": datetime,
        "SuspendedProcesses": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsSuspendedProcessesTypeDef
        ],
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "EnabledMetrics": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsEnabledMetricsTypeDef
        ],
        "Status": str,
        "Tags": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTagsTypeDef
        ],
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
    },
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginateResponse` `AutoScalingGroups`

    Describes an Auto Scaling group.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **AutoScalingGroupARN** *(string) --*

      The Amazon Resource Name (ARN) of the Auto Scaling group.

    - **LaunchConfigurationName** *(string) --*

      The name of the associated launch configuration.

    - **LaunchTemplate** *(dict) --*

      The launch template for the group.

      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template name.

      - **LaunchTemplateName** *(string) --*

        The name of the launch template. You must specify either a template name or a template
        ID.

      - **Version** *(string) --*

        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
        Amazon EC2 Auto Scaling selects the latest version of the launch template when
        launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
        default version of the launch template when launching instances. The default value is
        ``$Default`` .

    - **MixedInstancesPolicy** *(dict) --*

      The mixed instances policy for the group.

      - **LaunchTemplate** *(dict) --*

        The launch template and instance types (overrides).

        This parameter must be specified when creating a mixed instances policy.

        - **LaunchTemplateSpecification** *(dict) --*

          The launch template to use. You must specify either the launch template ID or launch
          template name in the request.

          - **LaunchTemplateId** *(string) --*

            The ID of the launch template. You must specify either a template ID or a template
            name.

          - **LaunchTemplateName** *(string) --*

            The name of the launch template. You must specify either a template name or a
            template ID.

          - **Version** *(string) --*

            The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
            Amazon EC2 Auto Scaling selects the latest version of the launch template when
            launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
            the default version of the launch template when launching instances. The default
            value is ``$Default`` .

        - **Overrides** *(list) --*

          An optional setting. Any parameters that you specify override the same parameters in
          the launch template. Currently, the only supported override is instance type. You can
          specify between 1 and 20 instance types.

          - *(dict) --*

            Describes an override for a launch template.

            - **InstanceType** *(string) --*

              The instance type.

              For information about available instance types, see `Available Instance Types
              <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
              in the *Amazon Elastic Compute Cloud User Guide.*

            - **WeightedCapacity** *(string) --*

              The number of capacity units, which gives the instance type a proportional weight
              to other instance types. For example, larger instance types are generally
              weighted more than smaller instance types. These are the same units that you
              chose to set the desired capacity in terms of instances, or a performance
              attribute such as vCPUs, memory, or I/O.

              Valid Range: Minimum value of 1. Maximum value of 999.

      - **InstancesDistribution** *(dict) --*

        The instances distribution to use.

        If you leave this parameter unspecified, the value for each parameter in
        ``InstancesDistribution`` uses a default value.

        - **OnDemandAllocationStrategy** *(string) --*

          Indicates how to allocate instance types to fulfill On-Demand capacity.

          The only valid value is ``prioritized`` , which is also the default value. This
          strategy uses the order of instance type overrides for the  LaunchTemplate to define
          the launch priority of each instance type. The first instance type in the array is
          prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled
          using your highest priority instance, then the Auto Scaling groups launches the
          remaining capacity using the second priority instance type, and so on.

        - **OnDemandBaseCapacity** *(integer) --*

          The minimum amount of the Auto Scaling group's capacity that must be fulfilled by
          On-Demand Instances. This base portion is provisioned first as your group scales.

          Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched
          as a percentage of the Auto Scaling group's desired capacity, per the
          ``OnDemandPercentageAboveBaseCapacity`` setting.

          .. note::

            An update to this setting means a gradual replacement of instances to maintain the
            specified number of On-Demand Instances for your base capacity. When replacing
            instances, Amazon EC2 Auto Scaling launches new instances before terminating the
            old ones.

        - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

          Controls the percentages of On-Demand Instances and Spot Instances for your
          additional capacity beyond ``OnDemandBaseCapacity`` .

          Default if not set is 100. If you leave it set to 100, the percentages are 100% for
          On-Demand Instances and 0% for Spot Instances.

          .. note::

            An update to this setting means a gradual replacement of instances to maintain the
            percentage of On-Demand Instances for your additional capacity above the base
            capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances
            before terminating the old ones.

          Valid Range: Minimum value of 0. Maximum value of 100.

        - **SpotAllocationStrategy** *(string) --*

          Indicates how to allocate instances across Spot Instance pools.

          If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches
          instances using the Spot pools with the lowest price, and evenly allocates your
          instances across the number of Spot pools that you specify. If the allocation
          strategy is ``capacity-optimized`` , the Auto Scaling group launches instances using
          Spot pools that are optimally chosen based on the available Spot capacity.

          The default Spot allocation strategy for calls that you make through the API, the AWS
          CLI, or the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for
          the AWS Management Console is ``capacity-optimized`` .

          Valid values: ``lowest-price`` | ``capacity-optimized``

        - **SpotInstancePools** *(integer) --*

          The number of Spot Instance pools across which to allocate your Spot Instances. The
          Spot pools are determined from the different instance types in the Overrides array of
           LaunchTemplate . Default if not set is 2.

          Used only when the Spot allocation strategy is ``lowest-price`` .

          Valid Range: Minimum value of 1. Maximum value of 20.

        - **SpotMaxPrice** *(string) --*

          The maximum price per unit hour that you are willing to pay for a Spot Instance. If
          you leave the value of this parameter blank (which is the default), the maximum Spot
          price is set at the On-Demand price.

          To remove a value that you previously set, include the parameter but leave the value
          blank.

    - **MinSize** *(integer) --*

      The minimum size of the group.

    - **MaxSize** *(integer) --*

      The maximum size of the group.

    - **DesiredCapacity** *(integer) --*

      The desired size of the group.

    - **DefaultCooldown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes before another scaling
      activity can start.

    - **AvailabilityZones** *(list) --*

      One or more Availability Zones for the group.

      - *(string) --*

    - **LoadBalancerNames** *(list) --*

      One or more load balancers associated with the group.

      - *(string) --*

    - **TargetGroupARNs** *(list) --*

      The Amazon Resource Names (ARN) of the target groups for your load balancer.

      - *(string) --*

    - **HealthCheckType** *(string) --*

      The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` . If
      you configure an Auto Scaling group to use ELB health checks, it considers the instance
      unhealthy if it fails either the EC2 status checks or the load balancer health checks.

    - **HealthCheckGracePeriod** *(integer) --*

      The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the
      health status of an EC2 instance that has come into service.

    - **Instances** *(list) --*

      The EC2 instances associated with the group.

      - *(dict) --*

        Describes an EC2 instance.

        - **InstanceId** *(string) --*

          The ID of the instance.

        - **InstanceType** *(string) --*

          The instance type of the EC2 instance.

        - **AvailabilityZone** *(string) --*

          The Availability Zone in which the instance is running.

        - **LifecycleState** *(string) --*

          A description of the current lifecycle state. The ``Quarantined`` state is not used.

        - **HealthStatus** *(string) --*

          The last reported health status of the instance. "Healthy" means that the instance is
          healthy and should remain in service. "Unhealthy" means that the instance is
          unhealthy and that Amazon EC2 Auto Scaling should terminate and replace it.

        - **LaunchConfigurationName** *(string) --*

          The launch configuration associated with the instance.

        - **LaunchTemplate** *(dict) --*

          The launch template for the instance.

          - **LaunchTemplateId** *(string) --*

            The ID of the launch template. You must specify either a template ID or a template
            name.

          - **LaunchTemplateName** *(string) --*

            The name of the launch template. You must specify either a template name or a
            template ID.

          - **Version** *(string) --*

            The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
            Amazon EC2 Auto Scaling selects the latest version of the launch template when
            launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
            the default version of the launch template when launching instances. The default
            value is ``$Default`` .

        - **ProtectedFromScaleIn** *(boolean) --*

          Indicates whether the instance is protected from termination by Amazon EC2 Auto
          Scaling when scaling in.

        - **WeightedCapacity** *(string) --*

          The number of capacity units contributed by the instance based on its instance type.

          Valid Range: Minimum value of 1. Maximum value of 999.

    - **CreatedTime** *(datetime) --*

      The date and time the group was created.

    - **SuspendedProcesses** *(list) --*

      The suspended processes associated with the group.

      - *(dict) --*

        Describes an automatic scaling process that has been suspended. For more information,
        see  ProcessType .

        - **ProcessName** *(string) --*

          The name of the suspended process.

        - **SuspensionReason** *(string) --*

          The reason that the process was suspended.

    - **PlacementGroup** *(string) --*

      The name of the placement group into which to launch your instances, if any.

    - **VPCZoneIdentifier** *(string) --*

      One or more subnet IDs, if applicable, separated by commas.

    - **EnabledMetrics** *(list) --*

      The metrics enabled for the group.

      - *(dict) --*

        Describes an enabled metric.

        - **Metric** *(string) --*

          One of the following metrics:

          * ``GroupMinSize``

          * ``GroupMaxSize``

          * ``GroupDesiredCapacity``

          * ``GroupInServiceInstances``

          * ``GroupPendingInstances``

          * ``GroupStandbyInstances``

          * ``GroupTerminatingInstances``

          * ``GroupTotalInstances``

        - **Granularity** *(string) --*

          The granularity of the metric. The only valid value is ``1Minute`` .

    - **Status** *(string) --*

      The current state of the group when  DeleteAutoScalingGroup is in progress.

    - **Tags** *(list) --*

      The tags for the group.

      - *(dict) --*

        Describes a tag for an Auto Scaling group.

        - **ResourceId** *(string) --*

          The name of the group.

        - **ResourceType** *(string) --*

          The type of resource. The only supported value is ``auto-scaling-group`` .

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The tag value.

        - **PropagateAtLaunch** *(boolean) --*

          Determines whether the tag is added to new instances as they are launched in the
          group.

    - **TerminationPolicies** *(list) --*

      The termination policies for the group.

      - *(string) --*

    - **NewInstancesProtectedFromScaleIn** *(boolean) --*

      Indicates whether newly launched instances are protected from termination by Amazon EC2
      Auto Scaling when scaling in.

    - **ServiceLinkedRoleARN** *(string) --*

      The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group
      uses to call other AWS services on your behalf.

    - **MaxInstanceLifetime** *(integer) --*

      The maximum amount of time, in seconds, that an instance can be in service.

      Valid Range: Minimum value of 604800.
    """


_DescribeAutoScalingGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeAutoScalingGroupsPaginateResponseTypeDef",
    {
        "AutoScalingGroups": List[
            DescribeAutoScalingGroupsPaginateResponseAutoScalingGroupsTypeDef
        ]
    },
    total=False,
)


class DescribeAutoScalingGroupsPaginateResponseTypeDef(
    _DescribeAutoScalingGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeAutoScalingGroupsPaginate` `Response`

    - **AutoScalingGroups** *(list) --*

      The groups.

      - *(dict) --*

        Describes an Auto Scaling group.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **AutoScalingGroupARN** *(string) --*

          The Amazon Resource Name (ARN) of the Auto Scaling group.

        - **LaunchConfigurationName** *(string) --*

          The name of the associated launch configuration.

        - **LaunchTemplate** *(dict) --*

          The launch template for the group.

          - **LaunchTemplateId** *(string) --*

            The ID of the launch template. You must specify either a template ID or a template name.

          - **LaunchTemplateName** *(string) --*

            The name of the launch template. You must specify either a template name or a template
            ID.

          - **Version** *(string) --*

            The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
            Amazon EC2 Auto Scaling selects the latest version of the launch template when
            launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
            default version of the launch template when launching instances. The default value is
            ``$Default`` .

        - **MixedInstancesPolicy** *(dict) --*

          The mixed instances policy for the group.

          - **LaunchTemplate** *(dict) --*

            The launch template and instance types (overrides).

            This parameter must be specified when creating a mixed instances policy.

            - **LaunchTemplateSpecification** *(dict) --*

              The launch template to use. You must specify either the launch template ID or launch
              template name in the request.

              - **LaunchTemplateId** *(string) --*

                The ID of the launch template. You must specify either a template ID or a template
                name.

              - **LaunchTemplateName** *(string) --*

                The name of the launch template. You must specify either a template name or a
                template ID.

              - **Version** *(string) --*

                The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
                Amazon EC2 Auto Scaling selects the latest version of the launch template when
                launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
                the default version of the launch template when launching instances. The default
                value is ``$Default`` .

            - **Overrides** *(list) --*

              An optional setting. Any parameters that you specify override the same parameters in
              the launch template. Currently, the only supported override is instance type. You can
              specify between 1 and 20 instance types.

              - *(dict) --*

                Describes an override for a launch template.

                - **InstanceType** *(string) --*

                  The instance type.

                  For information about available instance types, see `Available Instance Types
                  <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
                  in the *Amazon Elastic Compute Cloud User Guide.*

                - **WeightedCapacity** *(string) --*

                  The number of capacity units, which gives the instance type a proportional weight
                  to other instance types. For example, larger instance types are generally
                  weighted more than smaller instance types. These are the same units that you
                  chose to set the desired capacity in terms of instances, or a performance
                  attribute such as vCPUs, memory, or I/O.

                  Valid Range: Minimum value of 1. Maximum value of 999.

          - **InstancesDistribution** *(dict) --*

            The instances distribution to use.

            If you leave this parameter unspecified, the value for each parameter in
            ``InstancesDistribution`` uses a default value.

            - **OnDemandAllocationStrategy** *(string) --*

              Indicates how to allocate instance types to fulfill On-Demand capacity.

              The only valid value is ``prioritized`` , which is also the default value. This
              strategy uses the order of instance type overrides for the  LaunchTemplate to define
              the launch priority of each instance type. The first instance type in the array is
              prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled
              using your highest priority instance, then the Auto Scaling groups launches the
              remaining capacity using the second priority instance type, and so on.

            - **OnDemandBaseCapacity** *(integer) --*

              The minimum amount of the Auto Scaling group's capacity that must be fulfilled by
              On-Demand Instances. This base portion is provisioned first as your group scales.

              Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched
              as a percentage of the Auto Scaling group's desired capacity, per the
              ``OnDemandPercentageAboveBaseCapacity`` setting.

              .. note::

                An update to this setting means a gradual replacement of instances to maintain the
                specified number of On-Demand Instances for your base capacity. When replacing
                instances, Amazon EC2 Auto Scaling launches new instances before terminating the
                old ones.

            - **OnDemandPercentageAboveBaseCapacity** *(integer) --*

              Controls the percentages of On-Demand Instances and Spot Instances for your
              additional capacity beyond ``OnDemandBaseCapacity`` .

              Default if not set is 100. If you leave it set to 100, the percentages are 100% for
              On-Demand Instances and 0% for Spot Instances.

              .. note::

                An update to this setting means a gradual replacement of instances to maintain the
                percentage of On-Demand Instances for your additional capacity above the base
                capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances
                before terminating the old ones.

              Valid Range: Minimum value of 0. Maximum value of 100.

            - **SpotAllocationStrategy** *(string) --*

              Indicates how to allocate instances across Spot Instance pools.

              If the allocation strategy is ``lowest-price`` , the Auto Scaling group launches
              instances using the Spot pools with the lowest price, and evenly allocates your
              instances across the number of Spot pools that you specify. If the allocation
              strategy is ``capacity-optimized`` , the Auto Scaling group launches instances using
              Spot pools that are optimally chosen based on the available Spot capacity.

              The default Spot allocation strategy for calls that you make through the API, the AWS
              CLI, or the AWS SDKs is ``lowest-price`` . The default Spot allocation strategy for
              the AWS Management Console is ``capacity-optimized`` .

              Valid values: ``lowest-price`` | ``capacity-optimized``

            - **SpotInstancePools** *(integer) --*

              The number of Spot Instance pools across which to allocate your Spot Instances. The
              Spot pools are determined from the different instance types in the Overrides array of
               LaunchTemplate . Default if not set is 2.

              Used only when the Spot allocation strategy is ``lowest-price`` .

              Valid Range: Minimum value of 1. Maximum value of 20.

            - **SpotMaxPrice** *(string) --*

              The maximum price per unit hour that you are willing to pay for a Spot Instance. If
              you leave the value of this parameter blank (which is the default), the maximum Spot
              price is set at the On-Demand price.

              To remove a value that you previously set, include the parameter but leave the value
              blank.

        - **MinSize** *(integer) --*

          The minimum size of the group.

        - **MaxSize** *(integer) --*

          The maximum size of the group.

        - **DesiredCapacity** *(integer) --*

          The desired size of the group.

        - **DefaultCooldown** *(integer) --*

          The amount of time, in seconds, after a scaling activity completes before another scaling
          activity can start.

        - **AvailabilityZones** *(list) --*

          One or more Availability Zones for the group.

          - *(string) --*

        - **LoadBalancerNames** *(list) --*

          One or more load balancers associated with the group.

          - *(string) --*

        - **TargetGroupARNs** *(list) --*

          The Amazon Resource Names (ARN) of the target groups for your load balancer.

          - *(string) --*

        - **HealthCheckType** *(string) --*

          The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` . If
          you configure an Auto Scaling group to use ELB health checks, it considers the instance
          unhealthy if it fails either the EC2 status checks or the load balancer health checks.

        - **HealthCheckGracePeriod** *(integer) --*

          The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the
          health status of an EC2 instance that has come into service.

        - **Instances** *(list) --*

          The EC2 instances associated with the group.

          - *(dict) --*

            Describes an EC2 instance.

            - **InstanceId** *(string) --*

              The ID of the instance.

            - **InstanceType** *(string) --*

              The instance type of the EC2 instance.

            - **AvailabilityZone** *(string) --*

              The Availability Zone in which the instance is running.

            - **LifecycleState** *(string) --*

              A description of the current lifecycle state. The ``Quarantined`` state is not used.

            - **HealthStatus** *(string) --*

              The last reported health status of the instance. "Healthy" means that the instance is
              healthy and should remain in service. "Unhealthy" means that the instance is
              unhealthy and that Amazon EC2 Auto Scaling should terminate and replace it.

            - **LaunchConfigurationName** *(string) --*

              The launch configuration associated with the instance.

            - **LaunchTemplate** *(dict) --*

              The launch template for the instance.

              - **LaunchTemplateId** *(string) --*

                The ID of the launch template. You must specify either a template ID or a template
                name.

              - **LaunchTemplateName** *(string) --*

                The name of the launch template. You must specify either a template name or a
                template ID.

              - **Version** *(string) --*

                The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
                Amazon EC2 Auto Scaling selects the latest version of the launch template when
                launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects
                the default version of the launch template when launching instances. The default
                value is ``$Default`` .

            - **ProtectedFromScaleIn** *(boolean) --*

              Indicates whether the instance is protected from termination by Amazon EC2 Auto
              Scaling when scaling in.

            - **WeightedCapacity** *(string) --*

              The number of capacity units contributed by the instance based on its instance type.

              Valid Range: Minimum value of 1. Maximum value of 999.

        - **CreatedTime** *(datetime) --*

          The date and time the group was created.

        - **SuspendedProcesses** *(list) --*

          The suspended processes associated with the group.

          - *(dict) --*

            Describes an automatic scaling process that has been suspended. For more information,
            see  ProcessType .

            - **ProcessName** *(string) --*

              The name of the suspended process.

            - **SuspensionReason** *(string) --*

              The reason that the process was suspended.

        - **PlacementGroup** *(string) --*

          The name of the placement group into which to launch your instances, if any.

        - **VPCZoneIdentifier** *(string) --*

          One or more subnet IDs, if applicable, separated by commas.

        - **EnabledMetrics** *(list) --*

          The metrics enabled for the group.

          - *(dict) --*

            Describes an enabled metric.

            - **Metric** *(string) --*

              One of the following metrics:

              * ``GroupMinSize``

              * ``GroupMaxSize``

              * ``GroupDesiredCapacity``

              * ``GroupInServiceInstances``

              * ``GroupPendingInstances``

              * ``GroupStandbyInstances``

              * ``GroupTerminatingInstances``

              * ``GroupTotalInstances``

            - **Granularity** *(string) --*

              The granularity of the metric. The only valid value is ``1Minute`` .

        - **Status** *(string) --*

          The current state of the group when  DeleteAutoScalingGroup is in progress.

        - **Tags** *(list) --*

          The tags for the group.

          - *(dict) --*

            Describes a tag for an Auto Scaling group.

            - **ResourceId** *(string) --*

              The name of the group.

            - **ResourceType** *(string) --*

              The type of resource. The only supported value is ``auto-scaling-group`` .

            - **Key** *(string) --*

              The tag key.

            - **Value** *(string) --*

              The tag value.

            - **PropagateAtLaunch** *(boolean) --*

              Determines whether the tag is added to new instances as they are launched in the
              group.

        - **TerminationPolicies** *(list) --*

          The termination policies for the group.

          - *(string) --*

        - **NewInstancesProtectedFromScaleIn** *(boolean) --*

          Indicates whether newly launched instances are protected from termination by Amazon EC2
          Auto Scaling when scaling in.

        - **ServiceLinkedRoleARN** *(string) --*

          The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group
          uses to call other AWS services on your behalf.

        - **MaxInstanceLifetime** *(integer) --*

          The maximum amount of time, in seconds, that an instance can be in service.

          Valid Range: Minimum value of 604800.
    """


_DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef(
    _DescribeAutoScalingInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAutoScalingInstancesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef = TypedDict(
    "_DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)


class DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef(
    _DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef
):
    """
    Type definition for `DescribeAutoScalingInstancesPaginateResponseAutoScalingInstances` `LaunchTemplate`

    The launch template for the instance.

    - **LaunchTemplateId** *(string) --*

      The ID of the launch template. You must specify either a template ID or a template name.

    - **LaunchTemplateName** *(string) --*

      The name of the launch template. You must specify either a template name or a template
      ID.

    - **Version** *(string) --*

      The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
      Amazon EC2 Auto Scaling selects the latest version of the launch template when
      launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
      default version of the launch template when launching instances. The default value is
      ``$Default`` .
    """


_DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef = TypedDict(
    "_DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "AutoScalingGroupName": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesLaunchTemplateTypeDef,
        "ProtectedFromScaleIn": bool,
        "WeightedCapacity": str,
    },
    total=False,
)


class DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef(
    _DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef
):
    """
    Type definition for `DescribeAutoScalingInstancesPaginateResponse` `AutoScalingInstances`

    Describes an EC2 instance associated with an Auto Scaling group.

    - **InstanceId** *(string) --*

      The ID of the instance.

    - **InstanceType** *(string) --*

      The instance type of the EC2 instance.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group for the instance.

    - **AvailabilityZone** *(string) --*

      The Availability Zone for the instance.

    - **LifecycleState** *(string) --*

      The lifecycle state for the instance.

    - **HealthStatus** *(string) --*

      The last reported health status of this instance. "Healthy" means that the instance is
      healthy and should remain in service. "Unhealthy" means that the instance is unhealthy
      and Amazon EC2 Auto Scaling should terminate and replace it.

    - **LaunchConfigurationName** *(string) --*

      The launch configuration used to launch the instance. This value is not available if you
      attached the instance to the Auto Scaling group.

    - **LaunchTemplate** *(dict) --*

      The launch template for the instance.

      - **LaunchTemplateId** *(string) --*

        The ID of the launch template. You must specify either a template ID or a template name.

      - **LaunchTemplateName** *(string) --*

        The name of the launch template. You must specify either a template name or a template
        ID.

      - **Version** *(string) --*

        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
        Amazon EC2 Auto Scaling selects the latest version of the launch template when
        launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
        default version of the launch template when launching instances. The default value is
        ``$Default`` .

    - **ProtectedFromScaleIn** *(boolean) --*

      Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling
      when scaling in.

    - **WeightedCapacity** *(string) --*

      The number of capacity units contributed by the instance based on its instance type.

      Valid Range: Minimum value of 1. Maximum value of 999.
    """


_DescribeAutoScalingInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeAutoScalingInstancesPaginateResponseTypeDef",
    {
        "AutoScalingInstances": List[
            DescribeAutoScalingInstancesPaginateResponseAutoScalingInstancesTypeDef
        ]
    },
    total=False,
)


class DescribeAutoScalingInstancesPaginateResponseTypeDef(
    _DescribeAutoScalingInstancesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeAutoScalingInstancesPaginate` `Response`

    - **AutoScalingInstances** *(list) --*

      The instances.

      - *(dict) --*

        Describes an EC2 instance associated with an Auto Scaling group.

        - **InstanceId** *(string) --*

          The ID of the instance.

        - **InstanceType** *(string) --*

          The instance type of the EC2 instance.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group for the instance.

        - **AvailabilityZone** *(string) --*

          The Availability Zone for the instance.

        - **LifecycleState** *(string) --*

          The lifecycle state for the instance.

        - **HealthStatus** *(string) --*

          The last reported health status of this instance. "Healthy" means that the instance is
          healthy and should remain in service. "Unhealthy" means that the instance is unhealthy
          and Amazon EC2 Auto Scaling should terminate and replace it.

        - **LaunchConfigurationName** *(string) --*

          The launch configuration used to launch the instance. This value is not available if you
          attached the instance to the Auto Scaling group.

        - **LaunchTemplate** *(dict) --*

          The launch template for the instance.

          - **LaunchTemplateId** *(string) --*

            The ID of the launch template. You must specify either a template ID or a template name.

          - **LaunchTemplateName** *(string) --*

            The name of the launch template. You must specify either a template name or a template
            ID.

          - **Version** *(string) --*

            The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` ,
            Amazon EC2 Auto Scaling selects the latest version of the launch template when
            launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the
            default version of the launch template when launching instances. The default value is
            ``$Default`` .

        - **ProtectedFromScaleIn** *(boolean) --*

          Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling
          when scaling in.

        - **WeightedCapacity** *(string) --*

          The number of capacity units contributed by the instance based on its instance type.

          Valid Range: Minimum value of 1. Maximum value of 999.
    """


_DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeLaunchConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeLaunchConfigurationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef(
    _DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef
):
    """
    Type definition for `DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappings` `Ebs`

    The information about the Amazon EBS volume.

    - **SnapshotId** *(string) --*

      The snapshot ID of the volume to use.

      Conditional: This parameter is optional if you specify a volume size. If you
      specify both ``SnapshotId`` and ``VolumeSize`` , ``VolumeSize`` must be equal or
      greater than the size of the snapshot.

    - **VolumeSize** *(integer) --*

      The volume size, in Gibibytes (GiB).

      This can be a number from 1-1,024 for ``standard`` , 4-16,384 for ``io1`` ,
      1-16,384 for ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a
      snapshot, the volume size must be equal to or larger than the snapshot size.

      Default: If you create a volume from a snapshot and you don't specify a volume
      size, the default is the snapshot size.

      .. note::

        At least one of VolumeSize or SnapshotId is required.

    - **VolumeType** *(string) --*

      The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned
      IOPS SSD, ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or
      ``sc1`` for Cold HDD. For more information, see `Amazon EBS Volume Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

      Valid Values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``

    - **DeleteOnTermination** *(boolean) --*

      Indicates whether the volume is deleted on instance termination. For Amazon EC2
      Auto Scaling, the default value is ``true`` .

    - **Iops** *(integer) --*

      The number of I/O operations per second (IOPS) to provision for the volume. The
      maximum ratio of IOPS to volume size (in GiB) is 50:1. For more information, see
      `Amazon EBS Volume Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

      Conditional: This parameter is required when the volume type is ``io1`` . (Not used
      with ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.)

    - **Encrypted** *(boolean) --*

      Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be
      attached to instances that support Amazon EBS encryption. For more information, see
      `Supported Instance Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances>`__
      . If your AMI uses encrypted volumes, you can also only launch it on supported
      instance types.

      .. note::

        If you are creating a volume from a snapshot, you cannot specify an encryption
        value. Volumes that are created from encrypted snapshots are automatically
        encrypted, and volumes that are created from unencrypted snapshots are
        automatically unencrypted. By default, encrypted snapshots use the AWS managed
        CMK that is used for EBS encryption, but you can specify a custom CMK when you
        create the snapshot. The ability to encrypt a snapshot during copying also allows
        you to apply a new CMK to an already-encrypted snapshot. Volumes restored from
        the resulting copy are only accessible using the new CMK.

        Enabling `encryption by default
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default>`__
        results in all EBS volumes being encrypted with the AWS managed CMK or a customer
        managed CMK, whether or not the snapshot was encrypted.

      For more information, see `Using Encryption with EBS-Backed AMIs
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* and `Required CMK Key Policy for Use
      with Encrypted Volumes
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html>`__
      in the *Amazon EC2 Auto Scaling User Guide* .
    """


_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "DeviceName": str,
        "Ebs": DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)


class DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef(
    _DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef
):
    """
    Type definition for `DescribeLaunchConfigurationsPaginateResponseLaunchConfigurations` `BlockDeviceMappings`

    Describes a block device mapping.

    - **VirtualName** *(string) --*

      The name of the virtual device (for example, ``ephemeral0`` ).

    - **DeviceName** *(string) --*

      The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ).
      For more information, see `Device Naming on Linux Instances
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

    - **Ebs** *(dict) --*

      The information about the Amazon EBS volume.

      - **SnapshotId** *(string) --*

        The snapshot ID of the volume to use.

        Conditional: This parameter is optional if you specify a volume size. If you
        specify both ``SnapshotId`` and ``VolumeSize`` , ``VolumeSize`` must be equal or
        greater than the size of the snapshot.

      - **VolumeSize** *(integer) --*

        The volume size, in Gibibytes (GiB).

        This can be a number from 1-1,024 for ``standard`` , 4-16,384 for ``io1`` ,
        1-16,384 for ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a
        snapshot, the volume size must be equal to or larger than the snapshot size.

        Default: If you create a volume from a snapshot and you don't specify a volume
        size, the default is the snapshot size.

        .. note::

          At least one of VolumeSize or SnapshotId is required.

      - **VolumeType** *(string) --*

        The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned
        IOPS SSD, ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or
        ``sc1`` for Cold HDD. For more information, see `Amazon EBS Volume Types
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
        *Amazon EC2 User Guide for Linux Instances* .

        Valid Values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``

      - **DeleteOnTermination** *(boolean) --*

        Indicates whether the volume is deleted on instance termination. For Amazon EC2
        Auto Scaling, the default value is ``true`` .

      - **Iops** *(integer) --*

        The number of I/O operations per second (IOPS) to provision for the volume. The
        maximum ratio of IOPS to volume size (in GiB) is 50:1. For more information, see
        `Amazon EBS Volume Types
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
        *Amazon EC2 User Guide for Linux Instances* .

        Conditional: This parameter is required when the volume type is ``io1`` . (Not used
        with ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.)

      - **Encrypted** *(boolean) --*

        Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be
        attached to instances that support Amazon EBS encryption. For more information, see
        `Supported Instance Types
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances>`__
        . If your AMI uses encrypted volumes, you can also only launch it on supported
        instance types.

        .. note::

          If you are creating a volume from a snapshot, you cannot specify an encryption
          value. Volumes that are created from encrypted snapshots are automatically
          encrypted, and volumes that are created from unencrypted snapshots are
          automatically unencrypted. By default, encrypted snapshots use the AWS managed
          CMK that is used for EBS encryption, but you can specify a custom CMK when you
          create the snapshot. The ability to encrypt a snapshot during copying also allows
          you to apply a new CMK to an already-encrypted snapshot. Volumes restored from
          the resulting copy are only accessible using the new CMK.

          Enabling `encryption by default
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default>`__
          results in all EBS volumes being encrypted with the AWS managed CMK or a customer
          managed CMK, whether or not the snapshot was encrypted.

        For more information, see `Using Encryption with EBS-Backed AMIs
        <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html>`__ in the
        *Amazon EC2 User Guide for Linux Instances* and `Required CMK Key Policy for Use
        with Encrypted Volumes
        <https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html>`__
        in the *Amazon EC2 Auto Scaling User Guide* .

    - **NoDevice** *(boolean) --*

      Suppresses a device mapping.

      If this parameter is true for the root device, the instance might fail the EC2 health
      check. In that case, Amazon EC2 Auto Scaling launches a replacement instance.
    """


_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    {"Enabled": bool},
    total=False,
)


class DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef(
    _DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef
):
    """
    Type definition for `DescribeLaunchConfigurationsPaginateResponseLaunchConfigurations` `InstanceMonitoring`

    Controls whether instances in this group are launched with detailed (``true`` ) or basic
    (``false`` ) monitoring.

    For more information, see `Configure Monitoring for Auto Scaling Instances
    <https://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html#enable-as-instance-metrics>`__
    in the *Amazon EC2 Auto Scaling User Guide* .

    - **Enabled** *(boolean) --*

      If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
    """


_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef",
    {
        "LaunchConfigurationName": str,
        "LaunchConfigurationARN": str,
        "ImageId": str,
        "KeyName": str,
        "SecurityGroups": List[str],
        "ClassicLinkVPCId": str,
        "ClassicLinkVPCSecurityGroups": List[str],
        "UserData": str,
        "InstanceType": str,
        "KernelId": str,
        "RamdiskId": str,
        "BlockDeviceMappings": List[
            DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsBlockDeviceMappingsTypeDef
        ],
        "InstanceMonitoring": DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsInstanceMonitoringTypeDef,
        "SpotPrice": str,
        "IamInstanceProfile": str,
        "CreatedTime": datetime,
        "EbsOptimized": bool,
        "AssociatePublicIpAddress": bool,
        "PlacementTenancy": str,
    },
    total=False,
)


class DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef(
    _DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef
):
    """
    Type definition for `DescribeLaunchConfigurationsPaginateResponse` `LaunchConfigurations`

    Describes a launch configuration.

    - **LaunchConfigurationName** *(string) --*

      The name of the launch configuration.

    - **LaunchConfigurationARN** *(string) --*

      The Amazon Resource Name (ARN) of the launch configuration.

    - **ImageId** *(string) --*

      The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances.

      For more information, see `Finding an AMI
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

    - **KeyName** *(string) --*

      The name of the key pair.

      For more information, see `Amazon EC2 Key Pairs
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* .

    - **SecurityGroups** *(list) --*

      A list that contains the security groups to assign to the instances in the Auto Scaling
      group.

      For more information, see `Security Groups for Your VPC
      <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`__ in
      the *Amazon Virtual Private Cloud User Guide* .

      - *(string) --*

    - **ClassicLinkVPCId** *(string) --*

      The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.

      For more information, see `ClassicLink
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__
      in the *Amazon EC2 Auto Scaling User Guide* .

    - **ClassicLinkVPCSecurityGroups** *(list) --*

      The IDs of one or more security groups for the VPC specified in ``ClassicLinkVPCId`` .

      For more information, see `ClassicLink
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the
      *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__
      in the *Amazon EC2 Auto Scaling User Guide* .

      - *(string) --*

    - **UserData** *(string) --*

      The Base64-encoded user data to make available to the launched EC2 instances.

      For more information, see `Instance Metadata and User Data
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html>`__ in
      the *Amazon EC2 User Guide for Linux Instances* .

    - **InstanceType** *(string) --*

      The instance type for the instances.

      For information about available instance types, see `Available Instance Types
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
      in the *Amazon EC2 User Guide for Linux Instances.*

    - **KernelId** *(string) --*

      The ID of the kernel associated with the AMI.

    - **RamdiskId** *(string) --*

      The ID of the RAM disk associated with the AMI.

    - **BlockDeviceMappings** *(list) --*

      A block device mapping, which specifies the block devices for the instance.

      For more information, see `Block Device Mapping
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html>`__
      in the *Amazon EC2 User Guide for Linux Instances* .

      - *(dict) --*

        Describes a block device mapping.

        - **VirtualName** *(string) --*

          The name of the virtual device (for example, ``ephemeral0`` ).

        - **DeviceName** *(string) --*

          The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ).
          For more information, see `Device Naming on Linux Instances
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html>`__ in the
          *Amazon EC2 User Guide for Linux Instances* .

        - **Ebs** *(dict) --*

          The information about the Amazon EBS volume.

          - **SnapshotId** *(string) --*

            The snapshot ID of the volume to use.

            Conditional: This parameter is optional if you specify a volume size. If you
            specify both ``SnapshotId`` and ``VolumeSize`` , ``VolumeSize`` must be equal or
            greater than the size of the snapshot.

          - **VolumeSize** *(integer) --*

            The volume size, in Gibibytes (GiB).

            This can be a number from 1-1,024 for ``standard`` , 4-16,384 for ``io1`` ,
            1-16,384 for ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a
            snapshot, the volume size must be equal to or larger than the snapshot size.

            Default: If you create a volume from a snapshot and you don't specify a volume
            size, the default is the snapshot size.

            .. note::

              At least one of VolumeSize or SnapshotId is required.

          - **VolumeType** *(string) --*

            The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned
            IOPS SSD, ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or
            ``sc1`` for Cold HDD. For more information, see `Amazon EBS Volume Types
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
            *Amazon EC2 User Guide for Linux Instances* .

            Valid Values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``

          - **DeleteOnTermination** *(boolean) --*

            Indicates whether the volume is deleted on instance termination. For Amazon EC2
            Auto Scaling, the default value is ``true`` .

          - **Iops** *(integer) --*

            The number of I/O operations per second (IOPS) to provision for the volume. The
            maximum ratio of IOPS to volume size (in GiB) is 50:1. For more information, see
            `Amazon EBS Volume Types
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
            *Amazon EC2 User Guide for Linux Instances* .

            Conditional: This parameter is required when the volume type is ``io1`` . (Not used
            with ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.)

          - **Encrypted** *(boolean) --*

            Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be
            attached to instances that support Amazon EBS encryption. For more information, see
            `Supported Instance Types
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances>`__
            . If your AMI uses encrypted volumes, you can also only launch it on supported
            instance types.

            .. note::

              If you are creating a volume from a snapshot, you cannot specify an encryption
              value. Volumes that are created from encrypted snapshots are automatically
              encrypted, and volumes that are created from unencrypted snapshots are
              automatically unencrypted. By default, encrypted snapshots use the AWS managed
              CMK that is used for EBS encryption, but you can specify a custom CMK when you
              create the snapshot. The ability to encrypt a snapshot during copying also allows
              you to apply a new CMK to an already-encrypted snapshot. Volumes restored from
              the resulting copy are only accessible using the new CMK.

              Enabling `encryption by default
              <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default>`__
              results in all EBS volumes being encrypted with the AWS managed CMK or a customer
              managed CMK, whether or not the snapshot was encrypted.

            For more information, see `Using Encryption with EBS-Backed AMIs
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html>`__ in the
            *Amazon EC2 User Guide for Linux Instances* and `Required CMK Key Policy for Use
            with Encrypted Volumes
            <https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html>`__
            in the *Amazon EC2 Auto Scaling User Guide* .

        - **NoDevice** *(boolean) --*

          Suppresses a device mapping.

          If this parameter is true for the root device, the instance might fail the EC2 health
          check. In that case, Amazon EC2 Auto Scaling launches a replacement instance.

    - **InstanceMonitoring** *(dict) --*

      Controls whether instances in this group are launched with detailed (``true`` ) or basic
      (``false`` ) monitoring.

      For more information, see `Configure Monitoring for Auto Scaling Instances
      <https://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html#enable-as-instance-metrics>`__
      in the *Amazon EC2 Auto Scaling User Guide* .

      - **Enabled** *(boolean) --*

        If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

    - **SpotPrice** *(string) --*

      The maximum hourly price to be paid for any Spot Instance launched to fulfill the
      request. Spot Instances are launched when the price you specify exceeds the current Spot
      price.

      For more information, see `Launching Spot Instances in Your Auto Scaling Group
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-launch-spot-instances.html>`__
      in the *Amazon EC2 Auto Scaling User Guide* .

    - **IamInstanceProfile** *(string) --*

      The name or the Amazon Resource Name (ARN) of the instance profile associated with the
      IAM role for the instance. The instance profile contains the IAM role.

      For more information, see `IAM Role for Applications That Run on Amazon EC2 Instances
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html>`__ in the
      *Amazon EC2 Auto Scaling User Guide* .

    - **CreatedTime** *(datetime) --*

      The creation date and time for the launch configuration.

    - **EbsOptimized** *(boolean) --*

      Specifies whether the launch configuration is optimized for EBS I/O (``true`` ) or not
      (``false`` ).

      For more information, see `Amazon EBS-Optimized Instances
      <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html>`__ in the *Amazon
      EC2 User Guide for Linux Instances* .

    - **AssociatePublicIpAddress** *(boolean) --*

      For Auto Scaling groups that are running in a VPC, specifies whether to assign a public
      IP address to the group's instances.

      For more information, see `Launching Auto Scaling Instances in a VPC
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html>`__ in the *Amazon
      EC2 Auto Scaling User Guide* .

    - **PlacementTenancy** *(string) --*

      The tenancy of the instance, either ``default`` or ``dedicated`` . An instance with
      ``dedicated`` tenancy runs on isolated, single-tenant hardware and can only be launched
      into a VPC.

      For more information, see `Instance Placement Tenancy
      <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-vpc-tenancy>`__
      in the *Amazon EC2 Auto Scaling User Guide* .
    """


_DescribeLaunchConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeLaunchConfigurationsPaginateResponseTypeDef",
    {
        "LaunchConfigurations": List[
            DescribeLaunchConfigurationsPaginateResponseLaunchConfigurationsTypeDef
        ]
    },
    total=False,
)


class DescribeLaunchConfigurationsPaginateResponseTypeDef(
    _DescribeLaunchConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeLaunchConfigurationsPaginate` `Response`

    - **LaunchConfigurations** *(list) --*

      The launch configurations.

      - *(dict) --*

        Describes a launch configuration.

        - **LaunchConfigurationName** *(string) --*

          The name of the launch configuration.

        - **LaunchConfigurationARN** *(string) --*

          The Amazon Resource Name (ARN) of the launch configuration.

        - **ImageId** *(string) --*

          The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances.

          For more information, see `Finding an AMI
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html>`__ in the
          *Amazon EC2 User Guide for Linux Instances* .

        - **KeyName** *(string) --*

          The name of the key pair.

          For more information, see `Amazon EC2 Key Pairs
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the
          *Amazon EC2 User Guide for Linux Instances* .

        - **SecurityGroups** *(list) --*

          A list that contains the security groups to assign to the instances in the Auto Scaling
          group.

          For more information, see `Security Groups for Your VPC
          <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`__ in
          the *Amazon Virtual Private Cloud User Guide* .

          - *(string) --*

        - **ClassicLinkVPCId** *(string) --*

          The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.

          For more information, see `ClassicLink
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the
          *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__
          in the *Amazon EC2 Auto Scaling User Guide* .

        - **ClassicLinkVPCSecurityGroups** *(list) --*

          The IDs of one or more security groups for the VPC specified in ``ClassicLinkVPCId`` .

          For more information, see `ClassicLink
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the
          *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__
          in the *Amazon EC2 Auto Scaling User Guide* .

          - *(string) --*

        - **UserData** *(string) --*

          The Base64-encoded user data to make available to the launched EC2 instances.

          For more information, see `Instance Metadata and User Data
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html>`__ in
          the *Amazon EC2 User Guide for Linux Instances* .

        - **InstanceType** *(string) --*

          The instance type for the instances.

          For information about available instance types, see `Available Instance Types
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__
          in the *Amazon EC2 User Guide for Linux Instances.*

        - **KernelId** *(string) --*

          The ID of the kernel associated with the AMI.

        - **RamdiskId** *(string) --*

          The ID of the RAM disk associated with the AMI.

        - **BlockDeviceMappings** *(list) --*

          A block device mapping, which specifies the block devices for the instance.

          For more information, see `Block Device Mapping
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html>`__
          in the *Amazon EC2 User Guide for Linux Instances* .

          - *(dict) --*

            Describes a block device mapping.

            - **VirtualName** *(string) --*

              The name of the virtual device (for example, ``ephemeral0`` ).

            - **DeviceName** *(string) --*

              The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ).
              For more information, see `Device Naming on Linux Instances
              <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html>`__ in the
              *Amazon EC2 User Guide for Linux Instances* .

            - **Ebs** *(dict) --*

              The information about the Amazon EBS volume.

              - **SnapshotId** *(string) --*

                The snapshot ID of the volume to use.

                Conditional: This parameter is optional if you specify a volume size. If you
                specify both ``SnapshotId`` and ``VolumeSize`` , ``VolumeSize`` must be equal or
                greater than the size of the snapshot.

              - **VolumeSize** *(integer) --*

                The volume size, in Gibibytes (GiB).

                This can be a number from 1-1,024 for ``standard`` , 4-16,384 for ``io1`` ,
                1-16,384 for ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a
                snapshot, the volume size must be equal to or larger than the snapshot size.

                Default: If you create a volume from a snapshot and you don't specify a volume
                size, the default is the snapshot size.

                .. note::

                  At least one of VolumeSize or SnapshotId is required.

              - **VolumeType** *(string) --*

                The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned
                IOPS SSD, ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or
                ``sc1`` for Cold HDD. For more information, see `Amazon EBS Volume Types
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
                *Amazon EC2 User Guide for Linux Instances* .

                Valid Values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``

              - **DeleteOnTermination** *(boolean) --*

                Indicates whether the volume is deleted on instance termination. For Amazon EC2
                Auto Scaling, the default value is ``true`` .

              - **Iops** *(integer) --*

                The number of I/O operations per second (IOPS) to provision for the volume. The
                maximum ratio of IOPS to volume size (in GiB) is 50:1. For more information, see
                `Amazon EBS Volume Types
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the
                *Amazon EC2 User Guide for Linux Instances* .

                Conditional: This parameter is required when the volume type is ``io1`` . (Not used
                with ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.)

              - **Encrypted** *(boolean) --*

                Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be
                attached to instances that support Amazon EBS encryption. For more information, see
                `Supported Instance Types
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances>`__
                . If your AMI uses encrypted volumes, you can also only launch it on supported
                instance types.

                .. note::

                  If you are creating a volume from a snapshot, you cannot specify an encryption
                  value. Volumes that are created from encrypted snapshots are automatically
                  encrypted, and volumes that are created from unencrypted snapshots are
                  automatically unencrypted. By default, encrypted snapshots use the AWS managed
                  CMK that is used for EBS encryption, but you can specify a custom CMK when you
                  create the snapshot. The ability to encrypt a snapshot during copying also allows
                  you to apply a new CMK to an already-encrypted snapshot. Volumes restored from
                  the resulting copy are only accessible using the new CMK.

                  Enabling `encryption by default
                  <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default>`__
                  results in all EBS volumes being encrypted with the AWS managed CMK or a customer
                  managed CMK, whether or not the snapshot was encrypted.

                For more information, see `Using Encryption with EBS-Backed AMIs
                <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html>`__ in the
                *Amazon EC2 User Guide for Linux Instances* and `Required CMK Key Policy for Use
                with Encrypted Volumes
                <https://docs.aws.amazon.com/autoscaling/ec2/userguide/key-policy-requirements-EBS-encryption.html>`__
                in the *Amazon EC2 Auto Scaling User Guide* .

            - **NoDevice** *(boolean) --*

              Suppresses a device mapping.

              If this parameter is true for the root device, the instance might fail the EC2 health
              check. In that case, Amazon EC2 Auto Scaling launches a replacement instance.

        - **InstanceMonitoring** *(dict) --*

          Controls whether instances in this group are launched with detailed (``true`` ) or basic
          (``false`` ) monitoring.

          For more information, see `Configure Monitoring for Auto Scaling Instances
          <https://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html#enable-as-instance-metrics>`__
          in the *Amazon EC2 Auto Scaling User Guide* .

          - **Enabled** *(boolean) --*

            If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

        - **SpotPrice** *(string) --*

          The maximum hourly price to be paid for any Spot Instance launched to fulfill the
          request. Spot Instances are launched when the price you specify exceeds the current Spot
          price.

          For more information, see `Launching Spot Instances in Your Auto Scaling Group
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-launch-spot-instances.html>`__
          in the *Amazon EC2 Auto Scaling User Guide* .

        - **IamInstanceProfile** *(string) --*

          The name or the Amazon Resource Name (ARN) of the instance profile associated with the
          IAM role for the instance. The instance profile contains the IAM role.

          For more information, see `IAM Role for Applications That Run on Amazon EC2 Instances
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html>`__ in the
          *Amazon EC2 Auto Scaling User Guide* .

        - **CreatedTime** *(datetime) --*

          The creation date and time for the launch configuration.

        - **EbsOptimized** *(boolean) --*

          Specifies whether the launch configuration is optimized for EBS I/O (``true`` ) or not
          (``false`` ).

          For more information, see `Amazon EBS-Optimized Instances
          <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html>`__ in the *Amazon
          EC2 User Guide for Linux Instances* .

        - **AssociatePublicIpAddress** *(boolean) --*

          For Auto Scaling groups that are running in a VPC, specifies whether to assign a public
          IP address to the group's instances.

          For more information, see `Launching Auto Scaling Instances in a VPC
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html>`__ in the *Amazon
          EC2 Auto Scaling User Guide* .

        - **PlacementTenancy** *(string) --*

          The tenancy of the instance, either ``default`` or ``dedicated`` . An instance with
          ``dedicated`` tenancy runs on isolated, single-tenant hardware and can only be launched
          into a VPC.

          For more information, see `Instance Placement Tenancy
          <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-vpc-tenancy>`__
          in the *Amazon EC2 Auto Scaling User Guide* .
    """


_DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef(
    _DescribeLoadBalancerTargetGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeLoadBalancerTargetGroupsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef = TypedDict(
    "_DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef",
    {"LoadBalancerTargetGroupARN": str, "State": str},
    total=False,
)


class DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef(
    _DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef
):
    """
    Type definition for `DescribeLoadBalancerTargetGroupsPaginateResponse` `LoadBalancerTargetGroups`

    Describes the state of a target group.

    If you attach a target group to an existing Auto Scaling group, the initial state is
    ``Adding`` . The state transitions to ``Added`` after all Auto Scaling instances are
    registered with the target group. If Elastic Load Balancing health checks are enabled, the
    state transitions to ``InService`` after at least one Auto Scaling instance passes the
    health check. If EC2 health checks are enabled instead, the target group remains in the
    ``Added`` state.

    - **LoadBalancerTargetGroupARN** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **State** *(string) --*

      The state of the target group.

      * ``Adding`` - The Auto Scaling instances are being registered with the target group.

      * ``Added`` - All Auto Scaling instances are registered with the target group.

      * ``InService`` - At least one Auto Scaling instance passed an ELB health check.

      * ``Removing`` - The Auto Scaling instances are being deregistered from the target group.
      If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to
      complete before deregistering the instances.

      * ``Removed`` - All Auto Scaling instances are deregistered from the target group.
    """


_DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List[
            DescribeLoadBalancerTargetGroupsPaginateResponseLoadBalancerTargetGroupsTypeDef
        ]
    },
    total=False,
)


class DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef(
    _DescribeLoadBalancerTargetGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeLoadBalancerTargetGroupsPaginate` `Response`

    - **LoadBalancerTargetGroups** *(list) --*

      Information about the target groups.

      - *(dict) --*

        Describes the state of a target group.

        If you attach a target group to an existing Auto Scaling group, the initial state is
        ``Adding`` . The state transitions to ``Added`` after all Auto Scaling instances are
        registered with the target group. If Elastic Load Balancing health checks are enabled, the
        state transitions to ``InService`` after at least one Auto Scaling instance passes the
        health check. If EC2 health checks are enabled instead, the target group remains in the
        ``Added`` state.

        - **LoadBalancerTargetGroupARN** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **State** *(string) --*

          The state of the target group.

          * ``Adding`` - The Auto Scaling instances are being registered with the target group.

          * ``Added`` - All Auto Scaling instances are registered with the target group.

          * ``InService`` - At least one Auto Scaling instance passed an ELB health check.

          * ``Removing`` - The Auto Scaling instances are being deregistered from the target group.
          If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to
          complete before deregistering the instances.

          * ``Removed`` - All Auto Scaling instances are deregistered from the target group.
    """


_DescribeLoadBalancersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLoadBalancersPaginatePaginationConfigTypeDef(
    _DescribeLoadBalancersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef",
    {"LoadBalancerName": str, "State": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponse` `LoadBalancers`

    Describes the state of a Classic Load Balancer.

    If you specify a load balancer when creating the Auto Scaling group, the state of the load
    balancer is ``InService`` .

    If you attach a load balancer to an existing Auto Scaling group, the initial state is
    ``Adding`` . The state transitions to ``Added`` after all instances in the group are
    registered with the load balancer. If Elastic Load Balancing health checks are enabled for
    the load balancer, the state transitions to ``InService`` after at least one instance in
    the group passes the health check. If EC2 health checks are enabled instead, the load
    balancer remains in the ``Added`` state.

    - **LoadBalancerName** *(string) --*

      The name of the load balancer.

    - **State** *(string) --*

      One of the following load balancer states:

      * ``Adding`` - The instances in the group are being registered with the load balancer.

      * ``Added`` - All instances in the group are registered with the load balancer.

      * ``InService`` - At least one instance in the group passed an ELB health check.

      * ``Removing`` - The instances in the group are being deregistered from the load
      balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight
      requests to complete before deregistering the instances.

      * ``Removed`` - All instances in the group are deregistered from the load balancer.
    """


_DescribeLoadBalancersPaginateResponseTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseTypeDef",
    {"LoadBalancers": List[DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef]},
    total=False,
)


class DescribeLoadBalancersPaginateResponseTypeDef(
    _DescribeLoadBalancersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginate` `Response`

    - **LoadBalancers** *(list) --*

      The load balancers.

      - *(dict) --*

        Describes the state of a Classic Load Balancer.

        If you specify a load balancer when creating the Auto Scaling group, the state of the load
        balancer is ``InService`` .

        If you attach a load balancer to an existing Auto Scaling group, the initial state is
        ``Adding`` . The state transitions to ``Added`` after all instances in the group are
        registered with the load balancer. If Elastic Load Balancing health checks are enabled for
        the load balancer, the state transitions to ``InService`` after at least one instance in
        the group passes the health check. If EC2 health checks are enabled instead, the load
        balancer remains in the ``Added`` state.

        - **LoadBalancerName** *(string) --*

          The name of the load balancer.

        - **State** *(string) --*

          One of the following load balancer states:

          * ``Adding`` - The instances in the group are being registered with the load balancer.

          * ``Added`` - All instances in the group are registered with the load balancer.

          * ``InService`` - At least one instance in the group passed an ELB health check.

          * ``Removing`` - The instances in the group are being deregistered from the load
          balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight
          requests to complete before deregistering the instances.

          * ``Removed`` - All instances in the group are deregistered from the load balancer.
    """


_DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeNotificationConfigurationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeNotificationConfigurationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef = TypedDict(
    "_DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef",
    {"AutoScalingGroupName": str, "TopicARN": str, "NotificationType": str},
    total=False,
)


class DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef(
    _DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef
):
    """
    Type definition for `DescribeNotificationConfigurationsPaginateResponse` `NotificationConfigurations`

    Describes a notification.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **TopicARN** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS)
      topic.

    - **NotificationType** *(string) --*

      One of the following event notification types:

      * ``autoscaling:EC2_INSTANCE_LAUNCH``

      * ``autoscaling:EC2_INSTANCE_LAUNCH_ERROR``

      * ``autoscaling:EC2_INSTANCE_TERMINATE``

      * ``autoscaling:EC2_INSTANCE_TERMINATE_ERROR``

      * ``autoscaling:TEST_NOTIFICATION``
    """


_DescribeNotificationConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeNotificationConfigurationsPaginateResponseTypeDef",
    {
        "NotificationConfigurations": List[
            DescribeNotificationConfigurationsPaginateResponseNotificationConfigurationsTypeDef
        ]
    },
    total=False,
)


class DescribeNotificationConfigurationsPaginateResponseTypeDef(
    _DescribeNotificationConfigurationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeNotificationConfigurationsPaginate` `Response`

    - **NotificationConfigurations** *(list) --*

      The notification configurations.

      - *(dict) --*

        Describes a notification.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **TopicARN** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS)
          topic.

        - **NotificationType** *(string) --*

          One of the following event notification types:

          * ``autoscaling:EC2_INSTANCE_LAUNCH``

          * ``autoscaling:EC2_INSTANCE_LAUNCH_ERROR``

          * ``autoscaling:EC2_INSTANCE_TERMINATE``

          * ``autoscaling:EC2_INSTANCE_TERMINATE_ERROR``

          * ``autoscaling:TEST_NOTIFICATION``
    """


_DescribePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePoliciesPaginatePaginationConfigTypeDef(
    _DescribePoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribePoliciesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef
):
    """
    Type definition for `DescribePoliciesPaginateResponseScalingPolicies` `Alarms`

    Describes an alarm.

    - **AlarmName** *(string) --*

      The name of the alarm.

    - **AlarmARN** *(string) --*

      The Amazon Resource Name (ARN) of the alarm.
    """


_DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef
):
    """
    Type definition for `DescribePoliciesPaginateResponseScalingPolicies` `StepAdjustments`

    Describes an adjustment based on the difference between the value of the aggregated
    CloudWatch metric and the breach threshold that you've defined for the alarm. Used in
    combination with  PutScalingPolicy .

    For the following examples, suppose that you have an alarm with a breach threshold of
    50:

    * To trigger the adjustment when the metric is greater than or equal to 50 and less
    than 60, specify a lower bound of 0 and an upper bound of 10.

    * To trigger the adjustment when the metric is greater than 40 and less than or equal
    to 50, specify a lower bound of -10 and an upper bound of 0.

    There are a few rules for the step adjustments for your step policy:

    * The ranges of your step adjustments can't overlap or have a gap.

    * At most, one step adjustment can have a null lower bound. If one step adjustment has
    a negative lower bound, then there must be a step adjustment with a null lower bound.

    * At most, one step adjustment can have a null upper bound. If one step adjustment has
    a positive upper bound, then there must be a step adjustment with a null upper bound.

    * The upper and lower bound can't be null in the same step adjustment.

    - **MetricIntervalLowerBound** *(float) --*

      The lower bound for the difference between the alarm threshold and the CloudWatch
      metric. If the metric value is above the breach threshold, the lower bound is
      inclusive (the metric must be greater than or equal to the threshold plus the lower
      bound). Otherwise, it is exclusive (the metric must be greater than the threshold
      plus the lower bound). A null value indicates negative infinity.

    - **MetricIntervalUpperBound** *(float) --*

      The upper bound for the difference between the alarm threshold and the CloudWatch
      metric. If the metric value is above the breach threshold, the upper bound is
      exclusive (the metric must be less than the threshold plus the upper bound).
      Otherwise, it is inclusive (the metric must be less than or equal to the threshold
      plus the upper bound). A null value indicates positive infinity.

      The upper bound must be greater than the lower bound.

    - **ScalingAdjustment** *(integer) --*

      The amount by which to scale, based on the specified adjustment type. A positive
      value adds to the current capacity while a negative number removes from the current
      capacity.
    """


_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecification` `Dimensions`

    Describes the dimension of a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value of the dimension.
    """


_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef
):
    """
    Type definition for `DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfiguration` `CustomizedMetricSpecification`

    A customized metric. You must specify either a predefined metric or a customized metric.

    - **MetricName** *(string) --*

      The name of the metric.

    - **Namespace** *(string) --*

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the same
      dimensions in your scaling policy.

      - *(dict) --*

        Describes the dimension of a metric.

        - **Name** *(string) --*

          The name of the dimension.

        - **Value** *(string) --*

          The value of the dimension.

    - **Statistic** *(string) --*

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {"PredefinedMetricType": str, "ResourceLabel": str},
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef
):
    """
    Type definition for `DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfiguration` `PredefinedMetricSpecification`

    A predefined metric. You must specify either a predefined metric or a customized metric.

    - **PredefinedMetricType** *(string) --*

      The metric type. The following predefined metrics are available:

      * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.

      * ``ASGAverageNetworkIn`` - Average number of bytes received on all network
      interfaces by the Auto Scaling group.

      * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network
      interfaces by the Auto Scaling group.

      * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an
      Application Load Balancer target group.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a resource
      label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
      group attached to the Auto Scaling group.

      The format is ``app/*load-balancer-name* /*load-balancer-id*
      /targetgroup/*target-group-name* /*target-group-id* `` , where

      * ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load
      balancer ARN, and

      * ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the
      target group ARN.
    """


_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
    },
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef
):
    """
    Type definition for `DescribePoliciesPaginateResponseScalingPolicies` `TargetTrackingConfiguration`

    A target tracking scaling policy.

    - **PredefinedMetricSpecification** *(dict) --*

      A predefined metric. You must specify either a predefined metric or a customized metric.

      - **PredefinedMetricType** *(string) --*

        The metric type. The following predefined metrics are available:

        * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.

        * ``ASGAverageNetworkIn`` - Average number of bytes received on all network
        interfaces by the Auto Scaling group.

        * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network
        interfaces by the Auto Scaling group.

        * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an
        Application Load Balancer target group.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a resource
        label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
        group attached to the Auto Scaling group.

        The format is ``app/*load-balancer-name* /*load-balancer-id*
        /targetgroup/*target-group-name* /*target-group-id* `` , where

        * ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load
        balancer ARN, and

        * ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the
        target group ARN.

    - **CustomizedMetricSpecification** *(dict) --*

      A customized metric. You must specify either a predefined metric or a customized metric.

      - **MetricName** *(string) --*

        The name of the metric.

      - **Namespace** *(string) --*

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the same
        dimensions in your scaling policy.

        - *(dict) --*

          Describes the dimension of a metric.

          - **Name** *(string) --*

            The name of the dimension.

          - **Value** *(string) --*

            The value of the dimension.

      - **Statistic** *(string) --*

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **TargetValue** *(float) --*

      The target value for the metric.

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scaling in by the target tracking scaling policy is disabled. If
      scaling in is disabled, the target tracking scaling policy doesn't remove instances
      from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove
      instances from the Auto Scaling group. The default is ``false`` .
    """


_DescribePoliciesPaginateResponseScalingPoliciesTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseScalingPoliciesTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "PolicyARN": str,
        "PolicyType": str,
        "AdjustmentType": str,
        "MinAdjustmentStep": int,
        "MinAdjustmentMagnitude": int,
        "ScalingAdjustment": int,
        "Cooldown": int,
        "StepAdjustments": List[
            DescribePoliciesPaginateResponseScalingPoliciesStepAdjustmentsTypeDef
        ],
        "MetricAggregationType": str,
        "EstimatedInstanceWarmup": int,
        "Alarms": List[DescribePoliciesPaginateResponseScalingPoliciesAlarmsTypeDef],
        "TargetTrackingConfiguration": DescribePoliciesPaginateResponseScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)


class DescribePoliciesPaginateResponseScalingPoliciesTypeDef(
    _DescribePoliciesPaginateResponseScalingPoliciesTypeDef
):
    """
    Type definition for `DescribePoliciesPaginateResponse` `ScalingPolicies`

    Describes a scaling policy.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **PolicyName** *(string) --*

      The name of the scaling policy.

    - **PolicyARN** *(string) --*

      The Amazon Resource Name (ARN) of the policy.

    - **PolicyType** *(string) --*

      The policy type. The valid values are ``SimpleScaling`` , ``StepScaling`` , and
      ``TargetTrackingScaling`` .

    - **AdjustmentType** *(string) --*

      The adjustment type, which specifies how ``ScalingAdjustment`` is interpreted. The valid
      values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .

    - **MinAdjustmentStep** *(integer) --*

      Available for backward compatibility. Use ``MinAdjustmentMagnitude`` instead.

    - **MinAdjustmentMagnitude** *(integer) --*

      The minimum number of instances to scale. If the value of ``AdjustmentType`` is
      ``PercentChangeInCapacity`` , the scaling policy changes the ``DesiredCapacity`` of the
      Auto Scaling group by at least this many instances. Otherwise, the error is
      ``ValidationError`` .

    - **ScalingAdjustment** *(integer) --*

      The amount by which to scale, based on the specified adjustment type. A positive value
      adds to the current capacity while a negative number removes from the current capacity.

    - **Cooldown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes before any further
      dynamic scaling activities can start.

    - **StepAdjustments** *(list) --*

      A set of adjustments that enable you to scale based on the size of the alarm breach.

      - *(dict) --*

        Describes an adjustment based on the difference between the value of the aggregated
        CloudWatch metric and the breach threshold that you've defined for the alarm. Used in
        combination with  PutScalingPolicy .

        For the following examples, suppose that you have an alarm with a breach threshold of
        50:

        * To trigger the adjustment when the metric is greater than or equal to 50 and less
        than 60, specify a lower bound of 0 and an upper bound of 10.

        * To trigger the adjustment when the metric is greater than 40 and less than or equal
        to 50, specify a lower bound of -10 and an upper bound of 0.

        There are a few rules for the step adjustments for your step policy:

        * The ranges of your step adjustments can't overlap or have a gap.

        * At most, one step adjustment can have a null lower bound. If one step adjustment has
        a negative lower bound, then there must be a step adjustment with a null lower bound.

        * At most, one step adjustment can have a null upper bound. If one step adjustment has
        a positive upper bound, then there must be a step adjustment with a null upper bound.

        * The upper and lower bound can't be null in the same step adjustment.

        - **MetricIntervalLowerBound** *(float) --*

          The lower bound for the difference between the alarm threshold and the CloudWatch
          metric. If the metric value is above the breach threshold, the lower bound is
          inclusive (the metric must be greater than or equal to the threshold plus the lower
          bound). Otherwise, it is exclusive (the metric must be greater than the threshold
          plus the lower bound). A null value indicates negative infinity.

        - **MetricIntervalUpperBound** *(float) --*

          The upper bound for the difference between the alarm threshold and the CloudWatch
          metric. If the metric value is above the breach threshold, the upper bound is
          exclusive (the metric must be less than the threshold plus the upper bound).
          Otherwise, it is inclusive (the metric must be less than or equal to the threshold
          plus the upper bound). A null value indicates positive infinity.

          The upper bound must be greater than the lower bound.

        - **ScalingAdjustment** *(integer) --*

          The amount by which to scale, based on the specified adjustment type. A positive
          value adds to the current capacity while a negative number removes from the current
          capacity.

    - **MetricAggregationType** *(string) --*

      The aggregation type for the CloudWatch metrics. The valid values are ``Minimum`` ,
      ``Maximum`` , and ``Average`` .

    - **EstimatedInstanceWarmup** *(integer) --*

      The estimated time, in seconds, until a newly launched instance can contribute to the
      CloudWatch metrics.

    - **Alarms** *(list) --*

      The CloudWatch alarms related to the policy.

      - *(dict) --*

        Describes an alarm.

        - **AlarmName** *(string) --*

          The name of the alarm.

        - **AlarmARN** *(string) --*

          The Amazon Resource Name (ARN) of the alarm.

    - **TargetTrackingConfiguration** *(dict) --*

      A target tracking scaling policy.

      - **PredefinedMetricSpecification** *(dict) --*

        A predefined metric. You must specify either a predefined metric or a customized metric.

        - **PredefinedMetricType** *(string) --*

          The metric type. The following predefined metrics are available:

          * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.

          * ``ASGAverageNetworkIn`` - Average number of bytes received on all network
          interfaces by the Auto Scaling group.

          * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network
          interfaces by the Auto Scaling group.

          * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an
          Application Load Balancer target group.

        - **ResourceLabel** *(string) --*

          Identifies the resource associated with the metric type. You can't specify a resource
          label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
          group attached to the Auto Scaling group.

          The format is ``app/*load-balancer-name* /*load-balancer-id*
          /targetgroup/*target-group-name* /*target-group-id* `` , where

          * ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load
          balancer ARN, and

          * ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the
          target group ARN.

      - **CustomizedMetricSpecification** *(dict) --*

        A customized metric. You must specify either a predefined metric or a customized metric.

        - **MetricName** *(string) --*

          The name of the metric.

        - **Namespace** *(string) --*

          The namespace of the metric.

        - **Dimensions** *(list) --*

          The dimensions of the metric.

          Conditional: If you published your metric with dimensions, you must specify the same
          dimensions in your scaling policy.

          - *(dict) --*

            Describes the dimension of a metric.

            - **Name** *(string) --*

              The name of the dimension.

            - **Value** *(string) --*

              The value of the dimension.

        - **Statistic** *(string) --*

          The statistic of the metric.

        - **Unit** *(string) --*

          The unit of the metric.

      - **TargetValue** *(float) --*

        The target value for the metric.

      - **DisableScaleIn** *(boolean) --*

        Indicates whether scaling in by the target tracking scaling policy is disabled. If
        scaling in is disabled, the target tracking scaling policy doesn't remove instances
        from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove
        instances from the Auto Scaling group. The default is ``false`` .
    """


_DescribePoliciesPaginateResponseTypeDef = TypedDict(
    "_DescribePoliciesPaginateResponseTypeDef",
    {"ScalingPolicies": List[DescribePoliciesPaginateResponseScalingPoliciesTypeDef]},
    total=False,
)


class DescribePoliciesPaginateResponseTypeDef(_DescribePoliciesPaginateResponseTypeDef):
    """
    Type definition for `DescribePoliciesPaginate` `Response`

    - **ScalingPolicies** *(list) --*

      The scaling policies.

      - *(dict) --*

        Describes a scaling policy.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **PolicyName** *(string) --*

          The name of the scaling policy.

        - **PolicyARN** *(string) --*

          The Amazon Resource Name (ARN) of the policy.

        - **PolicyType** *(string) --*

          The policy type. The valid values are ``SimpleScaling`` , ``StepScaling`` , and
          ``TargetTrackingScaling`` .

        - **AdjustmentType** *(string) --*

          The adjustment type, which specifies how ``ScalingAdjustment`` is interpreted. The valid
          values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .

        - **MinAdjustmentStep** *(integer) --*

          Available for backward compatibility. Use ``MinAdjustmentMagnitude`` instead.

        - **MinAdjustmentMagnitude** *(integer) --*

          The minimum number of instances to scale. If the value of ``AdjustmentType`` is
          ``PercentChangeInCapacity`` , the scaling policy changes the ``DesiredCapacity`` of the
          Auto Scaling group by at least this many instances. Otherwise, the error is
          ``ValidationError`` .

        - **ScalingAdjustment** *(integer) --*

          The amount by which to scale, based on the specified adjustment type. A positive value
          adds to the current capacity while a negative number removes from the current capacity.

        - **Cooldown** *(integer) --*

          The amount of time, in seconds, after a scaling activity completes before any further
          dynamic scaling activities can start.

        - **StepAdjustments** *(list) --*

          A set of adjustments that enable you to scale based on the size of the alarm breach.

          - *(dict) --*

            Describes an adjustment based on the difference between the value of the aggregated
            CloudWatch metric and the breach threshold that you've defined for the alarm. Used in
            combination with  PutScalingPolicy .

            For the following examples, suppose that you have an alarm with a breach threshold of
            50:

            * To trigger the adjustment when the metric is greater than or equal to 50 and less
            than 60, specify a lower bound of 0 and an upper bound of 10.

            * To trigger the adjustment when the metric is greater than 40 and less than or equal
            to 50, specify a lower bound of -10 and an upper bound of 0.

            There are a few rules for the step adjustments for your step policy:

            * The ranges of your step adjustments can't overlap or have a gap.

            * At most, one step adjustment can have a null lower bound. If one step adjustment has
            a negative lower bound, then there must be a step adjustment with a null lower bound.

            * At most, one step adjustment can have a null upper bound. If one step adjustment has
            a positive upper bound, then there must be a step adjustment with a null upper bound.

            * The upper and lower bound can't be null in the same step adjustment.

            - **MetricIntervalLowerBound** *(float) --*

              The lower bound for the difference between the alarm threshold and the CloudWatch
              metric. If the metric value is above the breach threshold, the lower bound is
              inclusive (the metric must be greater than or equal to the threshold plus the lower
              bound). Otherwise, it is exclusive (the metric must be greater than the threshold
              plus the lower bound). A null value indicates negative infinity.

            - **MetricIntervalUpperBound** *(float) --*

              The upper bound for the difference between the alarm threshold and the CloudWatch
              metric. If the metric value is above the breach threshold, the upper bound is
              exclusive (the metric must be less than the threshold plus the upper bound).
              Otherwise, it is inclusive (the metric must be less than or equal to the threshold
              plus the upper bound). A null value indicates positive infinity.

              The upper bound must be greater than the lower bound.

            - **ScalingAdjustment** *(integer) --*

              The amount by which to scale, based on the specified adjustment type. A positive
              value adds to the current capacity while a negative number removes from the current
              capacity.

        - **MetricAggregationType** *(string) --*

          The aggregation type for the CloudWatch metrics. The valid values are ``Minimum`` ,
          ``Maximum`` , and ``Average`` .

        - **EstimatedInstanceWarmup** *(integer) --*

          The estimated time, in seconds, until a newly launched instance can contribute to the
          CloudWatch metrics.

        - **Alarms** *(list) --*

          The CloudWatch alarms related to the policy.

          - *(dict) --*

            Describes an alarm.

            - **AlarmName** *(string) --*

              The name of the alarm.

            - **AlarmARN** *(string) --*

              The Amazon Resource Name (ARN) of the alarm.

        - **TargetTrackingConfiguration** *(dict) --*

          A target tracking scaling policy.

          - **PredefinedMetricSpecification** *(dict) --*

            A predefined metric. You must specify either a predefined metric or a customized metric.

            - **PredefinedMetricType** *(string) --*

              The metric type. The following predefined metrics are available:

              * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group.

              * ``ASGAverageNetworkIn`` - Average number of bytes received on all network
              interfaces by the Auto Scaling group.

              * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network
              interfaces by the Auto Scaling group.

              * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an
              Application Load Balancer target group.

            - **ResourceLabel** *(string) --*

              Identifies the resource associated with the metric type. You can't specify a resource
              label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
              group attached to the Auto Scaling group.

              The format is ``app/*load-balancer-name* /*load-balancer-id*
              /targetgroup/*target-group-name* /*target-group-id* `` , where

              * ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load
              balancer ARN, and

              * ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the
              target group ARN.

          - **CustomizedMetricSpecification** *(dict) --*

            A customized metric. You must specify either a predefined metric or a customized metric.

            - **MetricName** *(string) --*

              The name of the metric.

            - **Namespace** *(string) --*

              The namespace of the metric.

            - **Dimensions** *(list) --*

              The dimensions of the metric.

              Conditional: If you published your metric with dimensions, you must specify the same
              dimensions in your scaling policy.

              - *(dict) --*

                Describes the dimension of a metric.

                - **Name** *(string) --*

                  The name of the dimension.

                - **Value** *(string) --*

                  The value of the dimension.

            - **Statistic** *(string) --*

              The statistic of the metric.

            - **Unit** *(string) --*

              The unit of the metric.

          - **TargetValue** *(float) --*

            The target value for the metric.

          - **DisableScaleIn** *(boolean) --*

            Indicates whether scaling in by the target tracking scaling policy is disabled. If
            scaling in is disabled, the target tracking scaling policy doesn't remove instances
            from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove
            instances from the Auto Scaling group. The default is ``false`` .
    """


_DescribeScalingActivitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalingActivitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalingActivitiesPaginatePaginationConfigTypeDef(
    _DescribeScalingActivitiesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeScalingActivitiesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeScalingActivitiesPaginateResponseActivitiesTypeDef = TypedDict(
    "_DescribeScalingActivitiesPaginateResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": str,
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)


class DescribeScalingActivitiesPaginateResponseActivitiesTypeDef(
    _DescribeScalingActivitiesPaginateResponseActivitiesTypeDef
):
    """
    Type definition for `DescribeScalingActivitiesPaginateResponse` `Activities`

    Describes scaling activity, which is a long-running process that represents a change to
    your Auto Scaling group, such as changing its size or replacing an instance.

    - **ActivityId** *(string) --*

      The ID of the activity.

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **Description** *(string) --*

      A friendly, more verbose description of the activity.

    - **Cause** *(string) --*

      The reason the activity began.

    - **StartTime** *(datetime) --*

      The start time of the activity.

    - **EndTime** *(datetime) --*

      The end time of the activity.

    - **StatusCode** *(string) --*

      The current status of the activity.

    - **StatusMessage** *(string) --*

      A friendly, more verbose description of the activity status.

    - **Progress** *(integer) --*

      A value between 0 and 100 that indicates the progress of the activity.

    - **Details** *(string) --*

      The details about the activity.
    """


_DescribeScalingActivitiesPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingActivitiesPaginateResponseTypeDef",
    {"Activities": List[DescribeScalingActivitiesPaginateResponseActivitiesTypeDef]},
    total=False,
)


class DescribeScalingActivitiesPaginateResponseTypeDef(
    _DescribeScalingActivitiesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeScalingActivitiesPaginate` `Response`

    - **Activities** *(list) --*

      The scaling activities. Activities are sorted by start time. Activities still in progress are
      described first.

      - *(dict) --*

        Describes scaling activity, which is a long-running process that represents a change to
        your Auto Scaling group, such as changing its size or replacing an instance.

        - **ActivityId** *(string) --*

          The ID of the activity.

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **Description** *(string) --*

          A friendly, more verbose description of the activity.

        - **Cause** *(string) --*

          The reason the activity began.

        - **StartTime** *(datetime) --*

          The start time of the activity.

        - **EndTime** *(datetime) --*

          The end time of the activity.

        - **StatusCode** *(string) --*

          The current status of the activity.

        - **StatusMessage** *(string) --*

          A friendly, more verbose description of the activity status.

        - **Progress** *(integer) --*

          A value between 0 and 100 that indicates the progress of the activity.

        - **Details** *(string) --*

          The details about the activity.
    """


_DescribeScheduledActionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScheduledActionsPaginatePaginationConfigTypeDef(
    _DescribeScheduledActionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeScheduledActionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "Time": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
    },
    total=False,
)


class DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef(
    _DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef
):
    """
    Type definition for `DescribeScheduledActionsPaginateResponse` `ScheduledUpdateGroupActions`

    Describes a scheduled scaling action. Used in response to  DescribeScheduledActions .

    - **AutoScalingGroupName** *(string) --*

      The name of the Auto Scaling group.

    - **ScheduledActionName** *(string) --*

      The name of the scheduled action.

    - **ScheduledActionARN** *(string) --*

      The Amazon Resource Name (ARN) of the scheduled action.

    - **Time** *(datetime) --*

      This parameter is no longer used.

    - **StartTime** *(datetime) --*

      The date and time in UTC for this action to start. For example,
      ``"2019-06-01T00:00:00Z"`` .

    - **EndTime** *(datetime) --*

      The date and time in UTC for the recurring schedule to end. For example,
      ``"2019-06-01T00:00:00Z"`` .

    - **Recurrence** *(string) --*

      The recurring schedule for the action, in Unix cron syntax format.

      When ``StartTime`` and ``EndTime`` are specified with ``Recurrence`` , they form the
      boundaries of when the recurring action starts and stops.

    - **MinSize** *(integer) --*

      The minimum number of instances in the Auto Scaling group.

    - **MaxSize** *(integer) --*

      The maximum number of instances in the Auto Scaling group.

    - **DesiredCapacity** *(integer) --*

      The number of instances you prefer to maintain in the group.
    """


_DescribeScheduledActionsPaginateResponseTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseTypeDef",
    {
        "ScheduledUpdateGroupActions": List[
            DescribeScheduledActionsPaginateResponseScheduledUpdateGroupActionsTypeDef
        ]
    },
    total=False,
)


class DescribeScheduledActionsPaginateResponseTypeDef(
    _DescribeScheduledActionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeScheduledActionsPaginate` `Response`

    - **ScheduledUpdateGroupActions** *(list) --*

      The scheduled actions.

      - *(dict) --*

        Describes a scheduled scaling action. Used in response to  DescribeScheduledActions .

        - **AutoScalingGroupName** *(string) --*

          The name of the Auto Scaling group.

        - **ScheduledActionName** *(string) --*

          The name of the scheduled action.

        - **ScheduledActionARN** *(string) --*

          The Amazon Resource Name (ARN) of the scheduled action.

        - **Time** *(datetime) --*

          This parameter is no longer used.

        - **StartTime** *(datetime) --*

          The date and time in UTC for this action to start. For example,
          ``"2019-06-01T00:00:00Z"`` .

        - **EndTime** *(datetime) --*

          The date and time in UTC for the recurring schedule to end. For example,
          ``"2019-06-01T00:00:00Z"`` .

        - **Recurrence** *(string) --*

          The recurring schedule for the action, in Unix cron syntax format.

          When ``StartTime`` and ``EndTime`` are specified with ``Recurrence`` , they form the
          boundaries of when the recurring action starts and stops.

        - **MinSize** *(integer) --*

          The minimum number of instances in the Auto Scaling group.

        - **MaxSize** *(integer) --*

          The maximum number of instances in the Auto Scaling group.

        - **DesiredCapacity** *(integer) --*

          The number of instances you prefer to maintain in the group.
    """


_DescribeTagsPaginateFiltersTypeDef = TypedDict(
    "_DescribeTagsPaginateFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class DescribeTagsPaginateFiltersTypeDef(_DescribeTagsPaginateFiltersTypeDef):
    """
    Type definition for `DescribeTagsPaginate` `Filters`

    Describes a filter.

    - **Name** *(string) --*

      The name of the filter. The valid values are: ``"auto-scaling-group"`` , ``"key"`` ,
      ``"value"`` , and ``"propagate-at-launch"`` .

    - **Values** *(list) --*

      The value of the filter.

      - *(string) --*
    """


_DescribeTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTagsPaginatePaginationConfigTypeDef(
    _DescribeTagsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeTagsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeTagsPaginateResponseTagsTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTagsTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "Key": str,
        "Value": str,
        "PropagateAtLaunch": bool,
    },
    total=False,
)


class DescribeTagsPaginateResponseTagsTypeDef(_DescribeTagsPaginateResponseTagsTypeDef):
    """
    Type definition for `DescribeTagsPaginateResponse` `Tags`

    Describes a tag for an Auto Scaling group.

    - **ResourceId** *(string) --*

      The name of the group.

    - **ResourceType** *(string) --*

      The type of resource. The only supported value is ``auto-scaling-group`` .

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The tag value.

    - **PropagateAtLaunch** *(boolean) --*

      Determines whether the tag is added to new instances as they are launched in the group.
    """


_DescribeTagsPaginateResponseTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTypeDef",
    {"Tags": List[DescribeTagsPaginateResponseTagsTypeDef]},
    total=False,
)


class DescribeTagsPaginateResponseTypeDef(_DescribeTagsPaginateResponseTypeDef):
    """
    Type definition for `DescribeTagsPaginate` `Response`

    - **Tags** *(list) --*

      One or more tags.

      - *(dict) --*

        Describes a tag for an Auto Scaling group.

        - **ResourceId** *(string) --*

          The name of the group.

        - **ResourceType** *(string) --*

          The type of resource. The only supported value is ``auto-scaling-group`` .

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The tag value.

        - **PropagateAtLaunch** *(boolean) --*

          Determines whether the tag is added to new instances as they are launched in the group.
    """
