"Main interface for autoscaling-plans type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef",
    "ClientCreateScalingPlanApplicationSourceTypeDef",
    "ClientCreateScalingPlanResponseTypeDef",
    "ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef",
    "ClientDescribeScalingPlanResourcesResponseTypeDef",
    "ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef",
    "ClientDescribeScalingPlansApplicationSourcesTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansTypeDef",
    "ClientDescribeScalingPlansResponseTypeDef",
    "ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef",
    "ClientGetScalingPlanResourceForecastDataResponseTypeDef",
    "ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef",
    "ClientUpdateScalingPlanApplicationSourceTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTypeDef",
    "DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef",
    "DescribeScalingPlanResourcesPaginateResponseTypeDef",
    "DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef",
    "DescribeScalingPlansPaginateApplicationSourcesTypeDef",
    "DescribeScalingPlansPaginatePaginationConfigTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef",
    "DescribeScalingPlansPaginateResponseScalingPlansTypeDef",
    "DescribeScalingPlansPaginateResponseTypeDef",
)


_ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef = TypedDict(
    "_ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef(
    _ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef
):
    """
    Type definition for `ClientCreateScalingPlanApplicationSource` `TagFilters`

    Represents a tag.

    - **Key** *(string) --*

      The tag key.

    - **Values** *(list) --*

      The tag values (0 to 20).

      - *(string) --*
    """


_ClientCreateScalingPlanApplicationSourceTypeDef = TypedDict(
    "_ClientCreateScalingPlanApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef],
    },
    total=False,
)


class ClientCreateScalingPlanApplicationSourceTypeDef(
    _ClientCreateScalingPlanApplicationSourceTypeDef
):
    """
    Type definition for `ClientCreateScalingPlan` `ApplicationSource`

    A CloudFormation stack or set of tags. You can create one scaling plan per application source.

    - **CloudFormationStackARN** *(string) --*

      The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

    - **TagFilters** *(list) --*

      A set of tags (up to 50).

      - *(dict) --*

        Represents a tag.

        - **Key** *(string) --*

          The tag key.

        - **Values** *(list) --*

          The tag values (0 to 20).

          - *(string) --*
    """


_ClientCreateScalingPlanResponseTypeDef = TypedDict(
    "_ClientCreateScalingPlanResponseTypeDef", {"ScalingPlanVersion": int}, total=False
)


class ClientCreateScalingPlanResponseTypeDef(_ClientCreateScalingPlanResponseTypeDef):
    """
    Type definition for `ClientCreateScalingPlan` `Response`

    - **ScalingPlanVersion** *(integer) --*

      The version number of the scaling plan. This value is always 1.

      Currently, you cannot specify multiple scaling plan versions.
    """


_ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
)


class ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef(
    _ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecification` `Dimensions`

    Represents a dimension for a customized metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the dimension.
    """


_RequiredClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {"MetricName": str, "Namespace": str, "Statistic": str},
)
_OptionalClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "Dimensions": List[
            ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Unit": str,
    },
    total=False,
)


class ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef(
    _RequiredClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
    _OptionalClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientCreateScalingPlanScalingInstructions` `CustomizedLoadMetricSpecification`

    The customized load metric to use for predictive scaling. This parameter or a
    **PredefinedLoadMetricSpecification** is required when configuring predictive scaling, and
    cannot be used otherwise.

    - **MetricName** *(string) --* **[REQUIRED]**

      The name of the metric.

    - **Namespace** *(string) --* **[REQUIRED]**

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the same
      dimensions in your customized load metric specification.

      - *(dict) --*

        Represents a dimension for a customized metric.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the dimension.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the dimension.

    - **Statistic** *(string) --* **[REQUIRED]**

      The statistic of the metric. Currently, the value must always be ``Sum`` .

    - **Unit** *(string) --*

      The unit of the metric.
    """


_RequiredClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {"PredefinedLoadMetricType": str},
)
_OptionalClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {"ResourceLabel": str},
    total=False,
)


class ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef(
    _RequiredClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
    _OptionalClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientCreateScalingPlanScalingInstructions` `PredefinedLoadMetricSpecification`

    The predefined load metric to use for predictive scaling. This parameter or a
    **CustomizedLoadMetricSpecification** is required when configuring predictive scaling, and
    cannot be used otherwise.

    - **PredefinedLoadMetricType** *(string) --* **[REQUIRED]**

      The metric type.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a resource label
      unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group for an
      Application Load Balancer attached to the Auto Scaling group.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN.

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
      group ARN.
    """


_ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
)


class ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecification` `Dimensions`

    Represents a dimension for a customized metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the dimension.
    """


_RequiredClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {"MetricName": str, "Namespace": str, "Statistic": str},
)
_OptionalClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "Dimensions": List[
            ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Unit": str,
    },
    total=False,
)


class ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef(
    _RequiredClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
    _OptionalClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurations` `CustomizedScalingMetricSpecification`

    A customized metric. You can specify either a predefined metric or a customized metric.

    - **MetricName** *(string) --* **[REQUIRED]**

      The name of the metric.

    - **Namespace** *(string) --* **[REQUIRED]**

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the same
      dimensions in your customized scaling metric specification.

      - *(dict) --*

        Represents a dimension for a customized metric.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the dimension.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the dimension.

    - **Statistic** *(string) --* **[REQUIRED]**

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_RequiredClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {"PredefinedScalingMetricType": str},
)
_OptionalClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {"ResourceLabel": str},
    total=False,
)


class ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef(
    _RequiredClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
    _OptionalClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurations` `PredefinedScalingMetricSpecification`

    A predefined metric. You can specify either a predefined metric or a customized metric.

    - **PredefinedScalingMetricType** *(string) --* **[REQUIRED]**

      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Auto
      Scaling groups, Spot Fleet requests, and ECS services.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a resource
      label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
      group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet
      request, or ECS service.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer
      ARN.

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
      group ARN.
    """


_RequiredClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "_RequiredClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {"TargetValue": float},
)
_OptionalClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "_OptionalClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)


class ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef(
    _RequiredClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef,
    _OptionalClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef,
):
    """
    Type definition for `ClientCreateScalingPlanScalingInstructions` `TargetTrackingConfigurations`

    Describes a target tracking configuration to use with AWS Auto Scaling. Used with
    ScalingInstruction and  ScalingPolicy .

    - **PredefinedScalingMetricSpecification** *(dict) --*

      A predefined metric. You can specify either a predefined metric or a customized metric.

      - **PredefinedScalingMetricType** *(string) --* **[REQUIRED]**

        The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Auto
        Scaling groups, Spot Fleet requests, and ECS services.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a resource
        label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
        group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet
        request, or ECS service.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer
        ARN.

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
        group ARN.

    - **CustomizedScalingMetricSpecification** *(dict) --*

      A customized metric. You can specify either a predefined metric or a customized metric.

      - **MetricName** *(string) --* **[REQUIRED]**

        The name of the metric.

      - **Namespace** *(string) --* **[REQUIRED]**

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the same
        dimensions in your customized scaling metric specification.

        - *(dict) --*

          Represents a dimension for a customized metric.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the dimension.

          - **Value** *(string) --* **[REQUIRED]**

            The value of the dimension.

      - **Statistic** *(string) --* **[REQUIRED]**

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **TargetValue** *(float) --* **[REQUIRED]**

      The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or
      2e-360 to 2e360 (Base 2).

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scale in by the target tracking scaling policy is disabled. If the
      value is ``true`` , scale in is disabled and the target tracking scaling policy doesn't
      remove capacity from the scalable resource. Otherwise, scale in is enabled and the target
      tracking scaling policy can remove capacity from the scalable resource.

      The default value is ``false`` .

    - **ScaleOutCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-out activity completes before another
      scale-out activity can start. This value is not used if the scalable resource is an Auto
      Scaling group.

      While the cooldown period is in effect, the capacity that has been added by the previous
      scale-out event that initiated the cooldown is calculated as part of the desired capacity
      for the next scale out. The intention is to continuously (but not excessively) scale out.

    - **ScaleInCooldown** *(integer) --*

      The amount of time, in seconds, after a scale in activity completes before another scale
      in activity can start. This value is not used if the scalable resource is an Auto Scaling
      group.

      The cooldown period is used to block subsequent scale in requests until it has expired.
      The intention is to scale in conservatively to protect your application's availability.
      However, if another alarm triggers a scale-out policy during the cooldown period after a
      scale-in, AWS Auto Scaling scales out your scalable target immediately.

    - **EstimatedInstanceWarmup** *(integer) --*

      The estimated time, in seconds, until a newly launched instance can contribute to the
      CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.
    """


_RequiredClientCreateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_RequiredClientCreateScalingPlanScalingInstructionsTypeDef",
    {
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
    },
)
_OptionalClientCreateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_OptionalClientCreateScalingPlanScalingInstructionsTypeDef",
    {
        "PredefinedLoadMetricSpecification": ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": str,
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": str,
        "ScalingPolicyUpdateBehavior": str,
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class ClientCreateScalingPlanScalingInstructionsTypeDef(
    _RequiredClientCreateScalingPlanScalingInstructionsTypeDef,
    _OptionalClientCreateScalingPlanScalingInstructionsTypeDef,
):
    """
    Type definition for `ClientCreateScalingPlan` `ScalingInstructions`

    Describes a scaling instruction for a scalable resource.

    The scaling instruction is used in combination with a scaling plan, which is a set of
    instructions for configuring dynamic scaling and predictive scaling for the scalable resources
    in your application. Each scaling instruction applies to one resource.

    AWS Auto Scaling creates target tracking scaling policies based on the scaling instructions.
    Target tracking scaling policies adjust the capacity of your scalable resource as required to
    maintain resource utilization at the target value that you specified.

    AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling groups
    using a subset of parameters, including the load metric, the scaling metric, the target value
    for the scaling metric, the predictive scaling mode (forecast and scale or forecast only), and
    the desired behavior when the forecast capacity exceeds the maximum capacity of the resource.
    With predictive scaling, AWS Auto Scaling generates forecasts with traffic predictions for the
    two days ahead and schedules scaling actions that proactively add and remove resource capacity
    to match the forecast.

    We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to configure
    predictive scaling. At minimum, there must be 24 hours of historical data to generate a
    forecast.

    For more information, see `Getting Started with AWS Auto Scaling
    <https://docs.aws.amazon.com/autoscaling/plans/userguide/auto-scaling-getting-started.html>`__ .

    - **ServiceNamespace** *(string) --* **[REQUIRED]**

      The namespace of the AWS service.

    - **ResourceId** *(string) --* **[REQUIRED]**

      The ID of the resource. This string consists of the resource type and unique identifier.

      * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique identifier is
      the name of the Auto Scaling group. Example: ``autoScalingGroup/my-asg`` .

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique identifier
      is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the resource
      ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique identifier
      is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

    - **ScalableDimension** *(string) --* **[REQUIRED]**

      The scalable dimension associated with the resource.

      * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto Scaling
      group.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.

      * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.

      * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global
      secondary index.

      * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
      global secondary index.

      * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
      Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

    - **MinCapacity** *(integer) --* **[REQUIRED]**

      The minimum capacity of the resource.

    - **MaxCapacity** *(integer) --* **[REQUIRED]**

      The maximum capacity of the resource. The exception to this upper limit is if you specify a
      non-default setting for **PredictiveScalingMaxCapacityBehavior** .

    - **TargetTrackingConfigurations** *(list) --* **[REQUIRED]**

      The structure that defines new target tracking configurations (up to 10). Each of these
      structures includes a specific scaling metric and a target value for the metric, along with
      various parameters to use with dynamic scaling.

      With predictive scaling and dynamic scaling, the resource scales based on the target tracking
      configuration that provides the largest capacity for both scale in and scale out.

      Condition: The scaling metric must be unique across target tracking configurations.

      - *(dict) --*

        Describes a target tracking configuration to use with AWS Auto Scaling. Used with
        ScalingInstruction and  ScalingPolicy .

        - **PredefinedScalingMetricSpecification** *(dict) --*

          A predefined metric. You can specify either a predefined metric or a customized metric.

          - **PredefinedScalingMetricType** *(string) --* **[REQUIRED]**

            The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Auto
            Scaling groups, Spot Fleet requests, and ECS services.

          - **ResourceLabel** *(string) --*

            Identifies the resource associated with the metric type. You can't specify a resource
            label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
            group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet
            request, or ECS service.

            The format is
            app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
            where:

            * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer
            ARN.

            * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
            group ARN.

        - **CustomizedScalingMetricSpecification** *(dict) --*

          A customized metric. You can specify either a predefined metric or a customized metric.

          - **MetricName** *(string) --* **[REQUIRED]**

            The name of the metric.

          - **Namespace** *(string) --* **[REQUIRED]**

            The namespace of the metric.

          - **Dimensions** *(list) --*

            The dimensions of the metric.

            Conditional: If you published your metric with dimensions, you must specify the same
            dimensions in your customized scaling metric specification.

            - *(dict) --*

              Represents a dimension for a customized metric.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the dimension.

              - **Value** *(string) --* **[REQUIRED]**

                The value of the dimension.

          - **Statistic** *(string) --* **[REQUIRED]**

            The statistic of the metric.

          - **Unit** *(string) --*

            The unit of the metric.

        - **TargetValue** *(float) --* **[REQUIRED]**

          The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or
          2e-360 to 2e360 (Base 2).

        - **DisableScaleIn** *(boolean) --*

          Indicates whether scale in by the target tracking scaling policy is disabled. If the
          value is ``true`` , scale in is disabled and the target tracking scaling policy doesn't
          remove capacity from the scalable resource. Otherwise, scale in is enabled and the target
          tracking scaling policy can remove capacity from the scalable resource.

          The default value is ``false`` .

        - **ScaleOutCooldown** *(integer) --*

          The amount of time, in seconds, after a scale-out activity completes before another
          scale-out activity can start. This value is not used if the scalable resource is an Auto
          Scaling group.

          While the cooldown period is in effect, the capacity that has been added by the previous
          scale-out event that initiated the cooldown is calculated as part of the desired capacity
          for the next scale out. The intention is to continuously (but not excessively) scale out.

        - **ScaleInCooldown** *(integer) --*

          The amount of time, in seconds, after a scale in activity completes before another scale
          in activity can start. This value is not used if the scalable resource is an Auto Scaling
          group.

          The cooldown period is used to block subsequent scale in requests until it has expired.
          The intention is to scale in conservatively to protect your application's availability.
          However, if another alarm triggers a scale-out policy during the cooldown period after a
          scale-in, AWS Auto Scaling scales out your scalable target immediately.

        - **EstimatedInstanceWarmup** *(integer) --*

          The estimated time, in seconds, until a newly launched instance can contribute to the
          CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.

    - **PredefinedLoadMetricSpecification** *(dict) --*

      The predefined load metric to use for predictive scaling. This parameter or a
      **CustomizedLoadMetricSpecification** is required when configuring predictive scaling, and
      cannot be used otherwise.

      - **PredefinedLoadMetricType** *(string) --* **[REQUIRED]**

        The metric type.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a resource label
        unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group for an
        Application Load Balancer attached to the Auto Scaling group.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN.

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
        group ARN.

    - **CustomizedLoadMetricSpecification** *(dict) --*

      The customized load metric to use for predictive scaling. This parameter or a
      **PredefinedLoadMetricSpecification** is required when configuring predictive scaling, and
      cannot be used otherwise.

      - **MetricName** *(string) --* **[REQUIRED]**

        The name of the metric.

      - **Namespace** *(string) --* **[REQUIRED]**

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the same
        dimensions in your customized load metric specification.

        - *(dict) --*

          Represents a dimension for a customized metric.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the dimension.

          - **Value** *(string) --* **[REQUIRED]**

            The value of the dimension.

      - **Statistic** *(string) --* **[REQUIRED]**

        The statistic of the metric. Currently, the value must always be ``Sum`` .

      - **Unit** *(string) --*

        The unit of the metric.

    - **ScheduledActionBufferTime** *(integer) --*

      The amount of time, in seconds, to buffer the run time of scheduled scaling actions when
      scaling out. For example, if the forecast says to add capacity at 10:00 AM, and the buffer
      time is 5 minutes, then the run time of the corresponding scheduled scaling action will be
      9:55 AM. The intention is to give resources time to be provisioned. For example, it can take
      a few minutes to launch an EC2 instance. The actual amount of time required depends on
      several factors, such as the size of the instance and whether there are startup scripts to
      complete.

      The value must be less than the forecast interval duration of 3600 seconds (60 minutes). The
      default is 300 seconds.

      Only valid when configuring predictive scaling.

    - **PredictiveScalingMaxCapacityBehavior** *(string) --*

      Defines the behavior that should be applied if the forecast capacity approaches or exceeds
      the maximum capacity specified for the resource. The default value is
      ``SetForecastCapacityToMaxCapacity`` .

      The following are possible values:

      * ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource capacity
      higher than the maximum capacity. The maximum capacity is enforced as a hard limit.

      * ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling may scale resource capacity higher
      than the maximum capacity to equal but not exceed forecast capacity.

      * ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling may scale resource capacity
      higher than the maximum capacity by a specified buffer value. The intention is to give the
      target tracking scaling policy extra capacity if unexpected traffic occurs.

      Only valid when configuring predictive scaling.

    - **PredictiveScalingMaxCapacityBuffer** *(integer) --*

      The size of the capacity buffer to use when the forecast capacity is close to or exceeds the
      maximum capacity. The value is specified as a percentage relative to the forecast capacity.
      For example, if the buffer is 10, this means a 10 percent buffer, such that if the forecast
      capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55.

      Only valid when configuring predictive scaling. Required if the
      **PredictiveScalingMaxCapacityBehavior** is set to ``SetMaxCapacityAboveForecastCapacity`` ,
      and cannot be used otherwise.

      The range is 1-100.

    - **PredictiveScalingMode** *(string) --*

      The predictive scaling mode. The default value is ``ForecastAndScale`` . Otherwise, AWS Auto
      Scaling forecasts capacity but does not create any scheduled scaling actions based on the
      capacity forecast.

    - **ScalingPolicyUpdateBehavior** *(string) --*

      Controls whether a resource's externally created scaling policies are kept or replaced.

      The default value is ``KeepExternalPolicies`` . If the parameter is set to
      ``ReplaceExternalPolicies`` , any scaling policies that are external to AWS Auto Scaling are
      deleted and new target tracking scaling policies created.

      Only valid when configuring dynamic scaling.

      Condition: The number of existing policies to be replaced must be less than or equal to 50.
      If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all existing
      policies and does not create new ones.

    - **DisableDynamicScaling** *(boolean) --*

      Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic scaling is
      enabled, AWS Auto Scaling creates target tracking scaling policies based on the specified
      target tracking configurations.

      The default is enabled (``false`` ).
    """


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecification` `Dimensions`

    Represents a dimension for a customized metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value of the dimension.
    """


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfiguration` `CustomizedScalingMetricSpecification`

    A customized metric. You can specify either a predefined metric or a customized
    metric.

    - **MetricName** *(string) --*

      The name of the metric.

    - **Namespace** *(string) --*

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the
      same dimensions in your customized scaling metric specification.

      - *(dict) --*

        Represents a dimension for a customized metric.

        - **Name** *(string) --*

          The name of the dimension.

        - **Value** *(string) --*

          The value of the dimension.

    - **Statistic** *(string) --*

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
    {"PredefinedScalingMetricType": str, "ResourceLabel": str},
    total=False,
)


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfiguration` `PredefinedScalingMetricSpecification`

    A predefined metric. You can specify either a predefined metric or a customized
    metric.

    - **PredefinedScalingMetricType** *(string) --*

      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
      Auto Scaling groups, Spot Fleet requests, and ECS services.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a
      resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
      is a target group for an Application Load Balancer attached to the Auto Scaling
      group, Spot Fleet request, or ECS service.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
      balancer ARN.

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
      target group ARN.
    """


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPolicies` `TargetTrackingConfiguration`

    The target tracking scaling policy. Includes support for predefined or customized
    metrics.

    - **PredefinedScalingMetricSpecification** *(dict) --*

      A predefined metric. You can specify either a predefined metric or a customized
      metric.

      - **PredefinedScalingMetricType** *(string) --*

        The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
        Auto Scaling groups, Spot Fleet requests, and ECS services.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a
        resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
        is a target group for an Application Load Balancer attached to the Auto Scaling
        group, Spot Fleet request, or ECS service.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
        balancer ARN.

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
        target group ARN.

    - **CustomizedScalingMetricSpecification** *(dict) --*

      A customized metric. You can specify either a predefined metric or a customized
      metric.

      - **MetricName** *(string) --*

        The name of the metric.

      - **Namespace** *(string) --*

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the
        same dimensions in your customized scaling metric specification.

        - *(dict) --*

          Represents a dimension for a customized metric.

          - **Name** *(string) --*

            The name of the dimension.

          - **Value** *(string) --*

            The value of the dimension.

      - **Statistic** *(string) --*

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **TargetValue** *(float) --*

      The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base
      10) or 2e-360 to 2e360 (Base 2).

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scale in by the target tracking scaling policy is disabled. If
      the value is ``true`` , scale in is disabled and the target tracking scaling policy
      doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled
      and the target tracking scaling policy can remove capacity from the scalable
      resource.

      The default value is ``false`` .

    - **ScaleOutCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-out activity completes before another
      scale-out activity can start. This value is not used if the scalable resource is an
      Auto Scaling group.

      While the cooldown period is in effect, the capacity that has been added by the
      previous scale-out event that initiated the cooldown is calculated as part of the
      desired capacity for the next scale out. The intention is to continuously (but not
      excessively) scale out.

    - **ScaleInCooldown** *(integer) --*

      The amount of time, in seconds, after a scale in activity completes before another
      scale in activity can start. This value is not used if the scalable resource is an
      Auto Scaling group.

      The cooldown period is used to block subsequent scale in requests until it has
      expired. The intention is to scale in conservatively to protect your application's
      availability. However, if another alarm triggers a scale-out policy during the
      cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target
      immediately.

    - **EstimatedInstanceWarmup** *(integer) --*

      The estimated time, in seconds, until a newly launched instance can contribute to
      the CloudWatch metrics. This value is used only if the resource is an Auto Scaling
      group.
    """


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": str,
        "TargetTrackingConfiguration": ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlanResourcesResponseScalingPlanResources` `ScalingPolicies`

    Represents a scaling policy.

    - **PolicyName** *(string) --*

      The name of the scaling policy.

    - **PolicyType** *(string) --*

      The type of scaling policy.

    - **TargetTrackingConfiguration** *(dict) --*

      The target tracking scaling policy. Includes support for predefined or customized
      metrics.

      - **PredefinedScalingMetricSpecification** *(dict) --*

        A predefined metric. You can specify either a predefined metric or a customized
        metric.

        - **PredefinedScalingMetricType** *(string) --*

          The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
          Auto Scaling groups, Spot Fleet requests, and ECS services.

        - **ResourceLabel** *(string) --*

          Identifies the resource associated with the metric type. You can't specify a
          resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
          is a target group for an Application Load Balancer attached to the Auto Scaling
          group, Spot Fleet request, or ECS service.

          The format is
          app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
          where:

          * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
          balancer ARN.

          * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
          target group ARN.

      - **CustomizedScalingMetricSpecification** *(dict) --*

        A customized metric. You can specify either a predefined metric or a customized
        metric.

        - **MetricName** *(string) --*

          The name of the metric.

        - **Namespace** *(string) --*

          The namespace of the metric.

        - **Dimensions** *(list) --*

          The dimensions of the metric.

          Conditional: If you published your metric with dimensions, you must specify the
          same dimensions in your customized scaling metric specification.

          - *(dict) --*

            Represents a dimension for a customized metric.

            - **Name** *(string) --*

              The name of the dimension.

            - **Value** *(string) --*

              The value of the dimension.

        - **Statistic** *(string) --*

          The statistic of the metric.

        - **Unit** *(string) --*

          The unit of the metric.

      - **TargetValue** *(float) --*

        The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base
        10) or 2e-360 to 2e360 (Base 2).

      - **DisableScaleIn** *(boolean) --*

        Indicates whether scale in by the target tracking scaling policy is disabled. If
        the value is ``true`` , scale in is disabled and the target tracking scaling policy
        doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled
        and the target tracking scaling policy can remove capacity from the scalable
        resource.

        The default value is ``false`` .

      - **ScaleOutCooldown** *(integer) --*

        The amount of time, in seconds, after a scale-out activity completes before another
        scale-out activity can start. This value is not used if the scalable resource is an
        Auto Scaling group.

        While the cooldown period is in effect, the capacity that has been added by the
        previous scale-out event that initiated the cooldown is calculated as part of the
        desired capacity for the next scale out. The intention is to continuously (but not
        excessively) scale out.

      - **ScaleInCooldown** *(integer) --*

        The amount of time, in seconds, after a scale in activity completes before another
        scale in activity can start. This value is not used if the scalable resource is an
        Auto Scaling group.

        The cooldown period is used to block subsequent scale in requests until it has
        expired. The intention is to scale in conservatively to protect your application's
        availability. However, if another alarm triggers a scale-out policy during the
        cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target
        immediately.

      - **EstimatedInstanceWarmup** *(integer) --*

        The estimated time, in seconds, until a newly launched instance can contribute to
        the CloudWatch metrics. This value is used only if the resource is an Auto Scaling
        group.
    """


_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "ScalingPolicies": List[
            ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef
        ],
        "ScalingStatusCode": str,
        "ScalingStatusMessage": str,
    },
    total=False,
)


class ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef(
    _ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlanResourcesResponse` `ScalingPlanResources`

    Represents a scalable resource.

    - **ScalingPlanName** *(string) --*

      The name of the scaling plan.

    - **ScalingPlanVersion** *(integer) --*

      The version number of the scaling plan.

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service.

    - **ResourceId** *(string) --*

      The ID of the resource. This string consists of the resource type and unique identifier.

      * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique
      identifier is the name of the Auto Scaling group. Example: ``autoScalingGroup/my-asg`` .

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

    - **ScalableDimension** *(string) --*

      The scalable dimension for the resource.

      * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto
      Scaling group.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
      table.

      * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
      table.

      * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
      global secondary index.

      * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
      global secondary index.

      * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
      cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible
      edition.

    - **ScalingPolicies** *(list) --*

      The scaling policies.

      - *(dict) --*

        Represents a scaling policy.

        - **PolicyName** *(string) --*

          The name of the scaling policy.

        - **PolicyType** *(string) --*

          The type of scaling policy.

        - **TargetTrackingConfiguration** *(dict) --*

          The target tracking scaling policy. Includes support for predefined or customized
          metrics.

          - **PredefinedScalingMetricSpecification** *(dict) --*

            A predefined metric. You can specify either a predefined metric or a customized
            metric.

            - **PredefinedScalingMetricType** *(string) --*

              The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
              Auto Scaling groups, Spot Fleet requests, and ECS services.

            - **ResourceLabel** *(string) --*

              Identifies the resource associated with the metric type. You can't specify a
              resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
              is a target group for an Application Load Balancer attached to the Auto Scaling
              group, Spot Fleet request, or ECS service.

              The format is
              app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
              where:

              * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
              balancer ARN.

              * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
              target group ARN.

          - **CustomizedScalingMetricSpecification** *(dict) --*

            A customized metric. You can specify either a predefined metric or a customized
            metric.

            - **MetricName** *(string) --*

              The name of the metric.

            - **Namespace** *(string) --*

              The namespace of the metric.

            - **Dimensions** *(list) --*

              The dimensions of the metric.

              Conditional: If you published your metric with dimensions, you must specify the
              same dimensions in your customized scaling metric specification.

              - *(dict) --*

                Represents a dimension for a customized metric.

                - **Name** *(string) --*

                  The name of the dimension.

                - **Value** *(string) --*

                  The value of the dimension.

            - **Statistic** *(string) --*

              The statistic of the metric.

            - **Unit** *(string) --*

              The unit of the metric.

          - **TargetValue** *(float) --*

            The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base
            10) or 2e-360 to 2e360 (Base 2).

          - **DisableScaleIn** *(boolean) --*

            Indicates whether scale in by the target tracking scaling policy is disabled. If
            the value is ``true`` , scale in is disabled and the target tracking scaling policy
            doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled
            and the target tracking scaling policy can remove capacity from the scalable
            resource.

            The default value is ``false`` .

          - **ScaleOutCooldown** *(integer) --*

            The amount of time, in seconds, after a scale-out activity completes before another
            scale-out activity can start. This value is not used if the scalable resource is an
            Auto Scaling group.

            While the cooldown period is in effect, the capacity that has been added by the
            previous scale-out event that initiated the cooldown is calculated as part of the
            desired capacity for the next scale out. The intention is to continuously (but not
            excessively) scale out.

          - **ScaleInCooldown** *(integer) --*

            The amount of time, in seconds, after a scale in activity completes before another
            scale in activity can start. This value is not used if the scalable resource is an
            Auto Scaling group.

            The cooldown period is used to block subsequent scale in requests until it has
            expired. The intention is to scale in conservatively to protect your application's
            availability. However, if another alarm triggers a scale-out policy during the
            cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target
            immediately.

          - **EstimatedInstanceWarmup** *(integer) --*

            The estimated time, in seconds, until a newly launched instance can contribute to
            the CloudWatch metrics. This value is used only if the resource is an Auto Scaling
            group.

    - **ScalingStatusCode** *(string) --*

      The scaling status of the resource.

      * ``Active`` - The scaling configuration is active.

      * ``Inactive`` - The scaling configuration is not active because the scaling plan is
      being created or the scaling configuration could not be applied. Check the status message
      for more information.

      * ``PartiallyActive`` - The scaling configuration is partially active because the scaling
      plan is being created or deleted or the scaling configuration could not be fully applied.
      Check the status message for more information.

    - **ScalingStatusMessage** *(string) --*

      A simple message about the current scaling status of the resource.
    """


_ClientDescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingPlanResourcesResponseTypeDef",
    {
        "ScalingPlanResources": List[
            ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingPlanResourcesResponseTypeDef(
    _ClientDescribeScalingPlanResourcesResponseTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlanResources` `Response`

    - **ScalingPlanResources** *(list) --*

      Information about the scalable resources.

      - *(dict) --*

        Represents a scalable resource.

        - **ScalingPlanName** *(string) --*

          The name of the scaling plan.

        - **ScalingPlanVersion** *(integer) --*

          The version number of the scaling plan.

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service.

        - **ResourceId** *(string) --*

          The ID of the resource. This string consists of the resource type and unique identifier.

          * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique
          identifier is the name of the Auto Scaling group. Example: ``autoScalingGroup/my-asg`` .

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

        - **ScalableDimension** *(string) --*

          The scalable dimension for the resource.

          * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto
          Scaling group.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
          cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible
          edition.

        - **ScalingPolicies** *(list) --*

          The scaling policies.

          - *(dict) --*

            Represents a scaling policy.

            - **PolicyName** *(string) --*

              The name of the scaling policy.

            - **PolicyType** *(string) --*

              The type of scaling policy.

            - **TargetTrackingConfiguration** *(dict) --*

              The target tracking scaling policy. Includes support for predefined or customized
              metrics.

              - **PredefinedScalingMetricSpecification** *(dict) --*

                A predefined metric. You can specify either a predefined metric or a customized
                metric.

                - **PredefinedScalingMetricType** *(string) --*

                  The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
                  Auto Scaling groups, Spot Fleet requests, and ECS services.

                - **ResourceLabel** *(string) --*

                  Identifies the resource associated with the metric type. You can't specify a
                  resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
                  is a target group for an Application Load Balancer attached to the Auto Scaling
                  group, Spot Fleet request, or ECS service.

                  The format is
                  app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
                  where:

                  * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
                  balancer ARN.

                  * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
                  target group ARN.

              - **CustomizedScalingMetricSpecification** *(dict) --*

                A customized metric. You can specify either a predefined metric or a customized
                metric.

                - **MetricName** *(string) --*

                  The name of the metric.

                - **Namespace** *(string) --*

                  The namespace of the metric.

                - **Dimensions** *(list) --*

                  The dimensions of the metric.

                  Conditional: If you published your metric with dimensions, you must specify the
                  same dimensions in your customized scaling metric specification.

                  - *(dict) --*

                    Represents a dimension for a customized metric.

                    - **Name** *(string) --*

                      The name of the dimension.

                    - **Value** *(string) --*

                      The value of the dimension.

                - **Statistic** *(string) --*

                  The statistic of the metric.

                - **Unit** *(string) --*

                  The unit of the metric.

              - **TargetValue** *(float) --*

                The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base
                10) or 2e-360 to 2e360 (Base 2).

              - **DisableScaleIn** *(boolean) --*

                Indicates whether scale in by the target tracking scaling policy is disabled. If
                the value is ``true`` , scale in is disabled and the target tracking scaling policy
                doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled
                and the target tracking scaling policy can remove capacity from the scalable
                resource.

                The default value is ``false`` .

              - **ScaleOutCooldown** *(integer) --*

                The amount of time, in seconds, after a scale-out activity completes before another
                scale-out activity can start. This value is not used if the scalable resource is an
                Auto Scaling group.

                While the cooldown period is in effect, the capacity that has been added by the
                previous scale-out event that initiated the cooldown is calculated as part of the
                desired capacity for the next scale out. The intention is to continuously (but not
                excessively) scale out.

              - **ScaleInCooldown** *(integer) --*

                The amount of time, in seconds, after a scale in activity completes before another
                scale in activity can start. This value is not used if the scalable resource is an
                Auto Scaling group.

                The cooldown period is used to block subsequent scale in requests until it has
                expired. The intention is to scale in conservatively to protect your application's
                availability. However, if another alarm triggers a scale-out policy during the
                cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target
                immediately.

              - **EstimatedInstanceWarmup** *(integer) --*

                The estimated time, in seconds, until a newly launched instance can contribute to
                the CloudWatch metrics. This value is used only if the resource is an Auto Scaling
                group.

        - **ScalingStatusCode** *(string) --*

          The scaling status of the resource.

          * ``Active`` - The scaling configuration is active.

          * ``Inactive`` - The scaling configuration is not active because the scaling plan is
          being created or the scaling configuration could not be applied. Check the status message
          for more information.

          * ``PartiallyActive`` - The scaling configuration is partially active because the scaling
          plan is being created or deleted or the scaling configuration could not be fully applied.
          Check the status message for more information.

        - **ScalingStatusMessage** *(string) --*

          A simple message about the current scaling status of the resource.

    - **NextToken** *(string) --*

      The token required to get the next set of results. This value is ``null`` if there are no
      more results to return.
    """


_ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef = TypedDict(
    "_ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef(
    _ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansApplicationSources` `TagFilters`

    Represents a tag.

    - **Key** *(string) --*

      The tag key.

    - **Values** *(list) --*

      The tag values (0 to 20).

      - *(string) --*
    """


_ClientDescribeScalingPlansApplicationSourcesTypeDef = TypedDict(
    "_ClientDescribeScalingPlansApplicationSourcesTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[
            ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeScalingPlansApplicationSourcesTypeDef(
    _ClientDescribeScalingPlansApplicationSourcesTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlans` `ApplicationSources`

    Represents an application source.

    - **CloudFormationStackARN** *(string) --*

      The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

    - **TagFilters** *(list) --*

      A set of tags (up to 50).

      - *(dict) --*

        Represents a tag.

        - **Key** *(string) --*

          The tag key.

        - **Values** *(list) --*

          The tag values (0 to 20).

          - *(string) --*
    """


_ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponseScalingPlansApplicationSource` `TagFilters`

    Represents a tag.

    - **Key** *(string) --*

      The tag key.

    - **Values** *(list) --*

      The tag values (0 to 20).

      - *(string) --*
    """


_ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[
            ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponseScalingPlans` `ApplicationSource`

    The application source.

    - **CloudFormationStackARN** *(string) --*

      The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

    - **TagFilters** *(list) --*

      A set of tags (up to 50).

      - *(dict) --*

        Represents a tag.

        - **Key** *(string) --*

          The tag key.

        - **Values** *(list) --*

          The tag values (0 to 20).

          - *(string) --*
    """


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecification` `Dimensions`

    Represents a dimension for a customized metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value of the dimension.
    """


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponseScalingPlansScalingInstructions` `CustomizedLoadMetricSpecification`

    The customized load metric to use for predictive scaling. This parameter or a
    **PredefinedLoadMetricSpecification** is required when configuring predictive
    scaling, and cannot be used otherwise.

    - **MetricName** *(string) --*

      The name of the metric.

    - **Namespace** *(string) --*

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the
      same dimensions in your customized load metric specification.

      - *(dict) --*

        Represents a dimension for a customized metric.

        - **Name** *(string) --*

          The name of the dimension.

        - **Value** *(string) --*

          The value of the dimension.

    - **Statistic** *(string) --*

      The statistic of the metric. Currently, the value must always be ``Sum`` .

    - **Unit** *(string) --*

      The unit of the metric.
    """


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {"PredefinedLoadMetricType": str, "ResourceLabel": str},
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponseScalingPlansScalingInstructions` `PredefinedLoadMetricSpecification`

    The predefined load metric to use for predictive scaling. This parameter or a
    **CustomizedLoadMetricSpecification** is required when configuring predictive
    scaling, and cannot be used otherwise.

    - **PredefinedLoadMetricType** *(string) --*

      The metric type.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a
      resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is
      a target group for an Application Load Balancer attached to the Auto Scaling group.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
      balancer ARN.

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
      target group ARN.
    """


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecification` `Dimensions`

    Represents a dimension for a customized metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value of the dimension.
    """


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurations` `CustomizedScalingMetricSpecification`

    A customized metric. You can specify either a predefined metric or a customized
    metric.

    - **MetricName** *(string) --*

      The name of the metric.

    - **Namespace** *(string) --*

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the
      same dimensions in your customized scaling metric specification.

      - *(dict) --*

        Represents a dimension for a customized metric.

        - **Name** *(string) --*

          The name of the dimension.

        - **Value** *(string) --*

          The value of the dimension.

    - **Statistic** *(string) --*

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {"PredefinedScalingMetricType": str, "ResourceLabel": str},
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurations` `PredefinedScalingMetricSpecification`

    A predefined metric. You can specify either a predefined metric or a customized
    metric.

    - **PredefinedScalingMetricType** *(string) --*

      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
      Auto Scaling groups, Spot Fleet requests, and ECS services.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a
      resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
      is a target group for an Application Load Balancer attached to the Auto Scaling
      group, Spot Fleet request, or ECS service.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
      balancer ARN.

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
      target group ARN.
    """


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponseScalingPlansScalingInstructions` `TargetTrackingConfigurations`

    Describes a target tracking configuration to use with AWS Auto Scaling. Used with
    ScalingInstruction and  ScalingPolicy .

    - **PredefinedScalingMetricSpecification** *(dict) --*

      A predefined metric. You can specify either a predefined metric or a customized
      metric.

      - **PredefinedScalingMetricType** *(string) --*

        The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
        Auto Scaling groups, Spot Fleet requests, and ECS services.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a
        resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
        is a target group for an Application Load Balancer attached to the Auto Scaling
        group, Spot Fleet request, or ECS service.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
        balancer ARN.

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
        target group ARN.

    - **CustomizedScalingMetricSpecification** *(dict) --*

      A customized metric. You can specify either a predefined metric or a customized
      metric.

      - **MetricName** *(string) --*

        The name of the metric.

      - **Namespace** *(string) --*

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the
        same dimensions in your customized scaling metric specification.

        - *(dict) --*

          Represents a dimension for a customized metric.

          - **Name** *(string) --*

            The name of the dimension.

          - **Value** *(string) --*

            The value of the dimension.

      - **Statistic** *(string) --*

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **TargetValue** *(float) --*

      The target value for the metric. The range is 8.515920e-109 to 1.174271e+108
      (Base 10) or 2e-360 to 2e360 (Base 2).

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scale in by the target tracking scaling policy is disabled. If
      the value is ``true`` , scale in is disabled and the target tracking scaling
      policy doesn't remove capacity from the scalable resource. Otherwise, scale in is
      enabled and the target tracking scaling policy can remove capacity from the
      scalable resource.

      The default value is ``false`` .

    - **ScaleOutCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-out activity completes before
      another scale-out activity can start. This value is not used if the scalable
      resource is an Auto Scaling group.

      While the cooldown period is in effect, the capacity that has been added by the
      previous scale-out event that initiated the cooldown is calculated as part of the
      desired capacity for the next scale out. The intention is to continuously (but
      not excessively) scale out.

    - **ScaleInCooldown** *(integer) --*

      The amount of time, in seconds, after a scale in activity completes before
      another scale in activity can start. This value is not used if the scalable
      resource is an Auto Scaling group.

      The cooldown period is used to block subsequent scale in requests until it has
      expired. The intention is to scale in conservatively to protect your
      application's availability. However, if another alarm triggers a scale-out policy
      during the cooldown period after a scale-in, AWS Auto Scaling scales out your
      scalable target immediately.

    - **EstimatedInstanceWarmup** *(integer) --*

      The estimated time, in seconds, until a newly launched instance can contribute to
      the CloudWatch metrics. This value is used only if the resource is an Auto
      Scaling group.
    """


_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef",
    {
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
        "PredefinedLoadMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": str,
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": str,
        "ScalingPolicyUpdateBehavior": str,
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponseScalingPlans` `ScalingInstructions`

    Describes a scaling instruction for a scalable resource.

    The scaling instruction is used in combination with a scaling plan, which is a set of
    instructions for configuring dynamic scaling and predictive scaling for the scalable
    resources in your application. Each scaling instruction applies to one resource.

    AWS Auto Scaling creates target tracking scaling policies based on the scaling
    instructions. Target tracking scaling policies adjust the capacity of your scalable
    resource as required to maintain resource utilization at the target value that you
    specified.

    AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling
    groups using a subset of parameters, including the load metric, the scaling metric, the
    target value for the scaling metric, the predictive scaling mode (forecast and scale or
    forecast only), and the desired behavior when the forecast capacity exceeds the maximum
    capacity of the resource. With predictive scaling, AWS Auto Scaling generates forecasts
    with traffic predictions for the two days ahead and schedules scaling actions that
    proactively add and remove resource capacity to match the forecast.

    We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to
    configure predictive scaling. At minimum, there must be 24 hours of historical data to
    generate a forecast.

    For more information, see `Getting Started with AWS Auto Scaling
    <https://docs.aws.amazon.com/autoscaling/plans/userguide/auto-scaling-getting-started.html>`__
    .

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service.

    - **ResourceId** *(string) --*

      The ID of the resource. This string consists of the resource type and unique
      identifier.

      * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique
      identifier is the name of the Auto Scaling group. Example:
      ``autoScalingGroup/my-asg`` .

      * ECS service - The resource type is ``service`` and the unique identifier is the
      cluster name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is
      the cluster name. Example: ``cluster:my-db-cluster`` .

    - **ScalableDimension** *(string) --*

      The scalable dimension associated with the resource.

      * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto
      Scaling group.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet
      request.

      * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
      table.

      * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a
      DynamoDB table.

      * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
      global secondary index.

      * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a
      DynamoDB global secondary index.

      * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
      cluster. Available for Aurora MySQL-compatible edition and Aurora
      PostgreSQL-compatible edition.

    - **MinCapacity** *(integer) --*

      The minimum capacity of the resource.

    - **MaxCapacity** *(integer) --*

      The maximum capacity of the resource. The exception to this upper limit is if you
      specify a non-default setting for **PredictiveScalingMaxCapacityBehavior** .

    - **TargetTrackingConfigurations** *(list) --*

      The structure that defines new target tracking configurations (up to 10). Each of
      these structures includes a specific scaling metric and a target value for the
      metric, along with various parameters to use with dynamic scaling.

      With predictive scaling and dynamic scaling, the resource scales based on the target
      tracking configuration that provides the largest capacity for both scale in and scale
      out.

      Condition: The scaling metric must be unique across target tracking configurations.

      - *(dict) --*

        Describes a target tracking configuration to use with AWS Auto Scaling. Used with
        ScalingInstruction and  ScalingPolicy .

        - **PredefinedScalingMetricSpecification** *(dict) --*

          A predefined metric. You can specify either a predefined metric or a customized
          metric.

          - **PredefinedScalingMetricType** *(string) --*

            The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
            Auto Scaling groups, Spot Fleet requests, and ECS services.

          - **ResourceLabel** *(string) --*

            Identifies the resource associated with the metric type. You can't specify a
            resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
            is a target group for an Application Load Balancer attached to the Auto Scaling
            group, Spot Fleet request, or ECS service.

            The format is
            app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
            where:

            * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
            balancer ARN.

            * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
            target group ARN.

        - **CustomizedScalingMetricSpecification** *(dict) --*

          A customized metric. You can specify either a predefined metric or a customized
          metric.

          - **MetricName** *(string) --*

            The name of the metric.

          - **Namespace** *(string) --*

            The namespace of the metric.

          - **Dimensions** *(list) --*

            The dimensions of the metric.

            Conditional: If you published your metric with dimensions, you must specify the
            same dimensions in your customized scaling metric specification.

            - *(dict) --*

              Represents a dimension for a customized metric.

              - **Name** *(string) --*

                The name of the dimension.

              - **Value** *(string) --*

                The value of the dimension.

          - **Statistic** *(string) --*

            The statistic of the metric.

          - **Unit** *(string) --*

            The unit of the metric.

        - **TargetValue** *(float) --*

          The target value for the metric. The range is 8.515920e-109 to 1.174271e+108
          (Base 10) or 2e-360 to 2e360 (Base 2).

        - **DisableScaleIn** *(boolean) --*

          Indicates whether scale in by the target tracking scaling policy is disabled. If
          the value is ``true`` , scale in is disabled and the target tracking scaling
          policy doesn't remove capacity from the scalable resource. Otherwise, scale in is
          enabled and the target tracking scaling policy can remove capacity from the
          scalable resource.

          The default value is ``false`` .

        - **ScaleOutCooldown** *(integer) --*

          The amount of time, in seconds, after a scale-out activity completes before
          another scale-out activity can start. This value is not used if the scalable
          resource is an Auto Scaling group.

          While the cooldown period is in effect, the capacity that has been added by the
          previous scale-out event that initiated the cooldown is calculated as part of the
          desired capacity for the next scale out. The intention is to continuously (but
          not excessively) scale out.

        - **ScaleInCooldown** *(integer) --*

          The amount of time, in seconds, after a scale in activity completes before
          another scale in activity can start. This value is not used if the scalable
          resource is an Auto Scaling group.

          The cooldown period is used to block subsequent scale in requests until it has
          expired. The intention is to scale in conservatively to protect your
          application's availability. However, if another alarm triggers a scale-out policy
          during the cooldown period after a scale-in, AWS Auto Scaling scales out your
          scalable target immediately.

        - **EstimatedInstanceWarmup** *(integer) --*

          The estimated time, in seconds, until a newly launched instance can contribute to
          the CloudWatch metrics. This value is used only if the resource is an Auto
          Scaling group.

    - **PredefinedLoadMetricSpecification** *(dict) --*

      The predefined load metric to use for predictive scaling. This parameter or a
      **CustomizedLoadMetricSpecification** is required when configuring predictive
      scaling, and cannot be used otherwise.

      - **PredefinedLoadMetricType** *(string) --*

        The metric type.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a
        resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is
        a target group for an Application Load Balancer attached to the Auto Scaling group.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
        balancer ARN.

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
        target group ARN.

    - **CustomizedLoadMetricSpecification** *(dict) --*

      The customized load metric to use for predictive scaling. This parameter or a
      **PredefinedLoadMetricSpecification** is required when configuring predictive
      scaling, and cannot be used otherwise.

      - **MetricName** *(string) --*

        The name of the metric.

      - **Namespace** *(string) --*

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the
        same dimensions in your customized load metric specification.

        - *(dict) --*

          Represents a dimension for a customized metric.

          - **Name** *(string) --*

            The name of the dimension.

          - **Value** *(string) --*

            The value of the dimension.

      - **Statistic** *(string) --*

        The statistic of the metric. Currently, the value must always be ``Sum`` .

      - **Unit** *(string) --*

        The unit of the metric.

    - **ScheduledActionBufferTime** *(integer) --*

      The amount of time, in seconds, to buffer the run time of scheduled scaling actions
      when scaling out. For example, if the forecast says to add capacity at 10:00 AM, and
      the buffer time is 5 minutes, then the run time of the corresponding scheduled
      scaling action will be 9:55 AM. The intention is to give resources time to be
      provisioned. For example, it can take a few minutes to launch an EC2 instance. The
      actual amount of time required depends on several factors, such as the size of the
      instance and whether there are startup scripts to complete.

      The value must be less than the forecast interval duration of 3600 seconds (60
      minutes). The default is 300 seconds.

      Only valid when configuring predictive scaling.

    - **PredictiveScalingMaxCapacityBehavior** *(string) --*

      Defines the behavior that should be applied if the forecast capacity approaches or
      exceeds the maximum capacity specified for the resource. The default value is
      ``SetForecastCapacityToMaxCapacity`` .

      The following are possible values:

      * ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource
      capacity higher than the maximum capacity. The maximum capacity is enforced as a hard
      limit.

      * ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling may scale resource capacity
      higher than the maximum capacity to equal but not exceed forecast capacity.

      * ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling may scale resource
      capacity higher than the maximum capacity by a specified buffer value. The intention
      is to give the target tracking scaling policy extra capacity if unexpected traffic
      occurs.

      Only valid when configuring predictive scaling.

    - **PredictiveScalingMaxCapacityBuffer** *(integer) --*

      The size of the capacity buffer to use when the forecast capacity is close to or
      exceeds the maximum capacity. The value is specified as a percentage relative to the
      forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer,
      such that if the forecast capacity is 50, and the maximum capacity is 40, then the
      effective maximum capacity is 55.

      Only valid when configuring predictive scaling. Required if the
      **PredictiveScalingMaxCapacityBehavior** is set to
      ``SetMaxCapacityAboveForecastCapacity`` , and cannot be used otherwise.

      The range is 1-100.

    - **PredictiveScalingMode** *(string) --*

      The predictive scaling mode. The default value is ``ForecastAndScale`` . Otherwise,
      AWS Auto Scaling forecasts capacity but does not create any scheduled scaling actions
      based on the capacity forecast.

    - **ScalingPolicyUpdateBehavior** *(string) --*

      Controls whether a resource's externally created scaling policies are kept or
      replaced.

      The default value is ``KeepExternalPolicies`` . If the parameter is set to
      ``ReplaceExternalPolicies`` , any scaling policies that are external to AWS Auto
      Scaling are deleted and new target tracking scaling policies created.

      Only valid when configuring dynamic scaling.

      Condition: The number of existing policies to be replaced must be less than or equal
      to 50. If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all
      existing policies and does not create new ones.

    - **DisableDynamicScaling** *(boolean) --*

      Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic
      scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based
      on the specified target tracking configurations.

      The default is enabled (``false`` ).
    """


_ClientDescribeScalingPlansResponseScalingPlansTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseScalingPlansTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef,
        "ScalingInstructions": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef
        ],
        "StatusCode": str,
        "StatusMessage": str,
        "StatusStartTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeScalingPlansResponseScalingPlansTypeDef(
    _ClientDescribeScalingPlansResponseScalingPlansTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlansResponse` `ScalingPlans`

    Represents a scaling plan.

    - **ScalingPlanName** *(string) --*

      The name of the scaling plan.

    - **ScalingPlanVersion** *(integer) --*

      The version number of the scaling plan.

    - **ApplicationSource** *(dict) --*

      The application source.

      - **CloudFormationStackARN** *(string) --*

        The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

      - **TagFilters** *(list) --*

        A set of tags (up to 50).

        - *(dict) --*

          Represents a tag.

          - **Key** *(string) --*

            The tag key.

          - **Values** *(list) --*

            The tag values (0 to 20).

            - *(string) --*

    - **ScalingInstructions** *(list) --*

      The scaling instructions.

      - *(dict) --*

        Describes a scaling instruction for a scalable resource.

        The scaling instruction is used in combination with a scaling plan, which is a set of
        instructions for configuring dynamic scaling and predictive scaling for the scalable
        resources in your application. Each scaling instruction applies to one resource.

        AWS Auto Scaling creates target tracking scaling policies based on the scaling
        instructions. Target tracking scaling policies adjust the capacity of your scalable
        resource as required to maintain resource utilization at the target value that you
        specified.

        AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling
        groups using a subset of parameters, including the load metric, the scaling metric, the
        target value for the scaling metric, the predictive scaling mode (forecast and scale or
        forecast only), and the desired behavior when the forecast capacity exceeds the maximum
        capacity of the resource. With predictive scaling, AWS Auto Scaling generates forecasts
        with traffic predictions for the two days ahead and schedules scaling actions that
        proactively add and remove resource capacity to match the forecast.

        We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to
        configure predictive scaling. At minimum, there must be 24 hours of historical data to
        generate a forecast.

        For more information, see `Getting Started with AWS Auto Scaling
        <https://docs.aws.amazon.com/autoscaling/plans/userguide/auto-scaling-getting-started.html>`__
        .

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service.

        - **ResourceId** *(string) --*

          The ID of the resource. This string consists of the resource type and unique
          identifier.

          * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique
          identifier is the name of the Auto Scaling group. Example:
          ``autoScalingGroup/my-asg`` .

          * ECS service - The resource type is ``service`` and the unique identifier is the
          cluster name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is
          the cluster name. Example: ``cluster:my-db-cluster`` .

        - **ScalableDimension** *(string) --*

          The scalable dimension associated with the resource.

          * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto
          Scaling group.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet
          request.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a
          DynamoDB table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a
          DynamoDB global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
          cluster. Available for Aurora MySQL-compatible edition and Aurora
          PostgreSQL-compatible edition.

        - **MinCapacity** *(integer) --*

          The minimum capacity of the resource.

        - **MaxCapacity** *(integer) --*

          The maximum capacity of the resource. The exception to this upper limit is if you
          specify a non-default setting for **PredictiveScalingMaxCapacityBehavior** .

        - **TargetTrackingConfigurations** *(list) --*

          The structure that defines new target tracking configurations (up to 10). Each of
          these structures includes a specific scaling metric and a target value for the
          metric, along with various parameters to use with dynamic scaling.

          With predictive scaling and dynamic scaling, the resource scales based on the target
          tracking configuration that provides the largest capacity for both scale in and scale
          out.

          Condition: The scaling metric must be unique across target tracking configurations.

          - *(dict) --*

            Describes a target tracking configuration to use with AWS Auto Scaling. Used with
            ScalingInstruction and  ScalingPolicy .

            - **PredefinedScalingMetricSpecification** *(dict) --*

              A predefined metric. You can specify either a predefined metric or a customized
              metric.

              - **PredefinedScalingMetricType** *(string) --*

                The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
                Auto Scaling groups, Spot Fleet requests, and ECS services.

              - **ResourceLabel** *(string) --*

                Identifies the resource associated with the metric type. You can't specify a
                resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
                is a target group for an Application Load Balancer attached to the Auto Scaling
                group, Spot Fleet request, or ECS service.

                The format is
                app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
                where:

                * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
                balancer ARN.

                * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
                target group ARN.

            - **CustomizedScalingMetricSpecification** *(dict) --*

              A customized metric. You can specify either a predefined metric or a customized
              metric.

              - **MetricName** *(string) --*

                The name of the metric.

              - **Namespace** *(string) --*

                The namespace of the metric.

              - **Dimensions** *(list) --*

                The dimensions of the metric.

                Conditional: If you published your metric with dimensions, you must specify the
                same dimensions in your customized scaling metric specification.

                - *(dict) --*

                  Represents a dimension for a customized metric.

                  - **Name** *(string) --*

                    The name of the dimension.

                  - **Value** *(string) --*

                    The value of the dimension.

              - **Statistic** *(string) --*

                The statistic of the metric.

              - **Unit** *(string) --*

                The unit of the metric.

            - **TargetValue** *(float) --*

              The target value for the metric. The range is 8.515920e-109 to 1.174271e+108
              (Base 10) or 2e-360 to 2e360 (Base 2).

            - **DisableScaleIn** *(boolean) --*

              Indicates whether scale in by the target tracking scaling policy is disabled. If
              the value is ``true`` , scale in is disabled and the target tracking scaling
              policy doesn't remove capacity from the scalable resource. Otherwise, scale in is
              enabled and the target tracking scaling policy can remove capacity from the
              scalable resource.

              The default value is ``false`` .

            - **ScaleOutCooldown** *(integer) --*

              The amount of time, in seconds, after a scale-out activity completes before
              another scale-out activity can start. This value is not used if the scalable
              resource is an Auto Scaling group.

              While the cooldown period is in effect, the capacity that has been added by the
              previous scale-out event that initiated the cooldown is calculated as part of the
              desired capacity for the next scale out. The intention is to continuously (but
              not excessively) scale out.

            - **ScaleInCooldown** *(integer) --*

              The amount of time, in seconds, after a scale in activity completes before
              another scale in activity can start. This value is not used if the scalable
              resource is an Auto Scaling group.

              The cooldown period is used to block subsequent scale in requests until it has
              expired. The intention is to scale in conservatively to protect your
              application's availability. However, if another alarm triggers a scale-out policy
              during the cooldown period after a scale-in, AWS Auto Scaling scales out your
              scalable target immediately.

            - **EstimatedInstanceWarmup** *(integer) --*

              The estimated time, in seconds, until a newly launched instance can contribute to
              the CloudWatch metrics. This value is used only if the resource is an Auto
              Scaling group.

        - **PredefinedLoadMetricSpecification** *(dict) --*

          The predefined load metric to use for predictive scaling. This parameter or a
          **CustomizedLoadMetricSpecification** is required when configuring predictive
          scaling, and cannot be used otherwise.

          - **PredefinedLoadMetricType** *(string) --*

            The metric type.

          - **ResourceLabel** *(string) --*

            Identifies the resource associated with the metric type. You can't specify a
            resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is
            a target group for an Application Load Balancer attached to the Auto Scaling group.

            The format is
            app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
            where:

            * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
            balancer ARN.

            * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
            target group ARN.

        - **CustomizedLoadMetricSpecification** *(dict) --*

          The customized load metric to use for predictive scaling. This parameter or a
          **PredefinedLoadMetricSpecification** is required when configuring predictive
          scaling, and cannot be used otherwise.

          - **MetricName** *(string) --*

            The name of the metric.

          - **Namespace** *(string) --*

            The namespace of the metric.

          - **Dimensions** *(list) --*

            The dimensions of the metric.

            Conditional: If you published your metric with dimensions, you must specify the
            same dimensions in your customized load metric specification.

            - *(dict) --*

              Represents a dimension for a customized metric.

              - **Name** *(string) --*

                The name of the dimension.

              - **Value** *(string) --*

                The value of the dimension.

          - **Statistic** *(string) --*

            The statistic of the metric. Currently, the value must always be ``Sum`` .

          - **Unit** *(string) --*

            The unit of the metric.

        - **ScheduledActionBufferTime** *(integer) --*

          The amount of time, in seconds, to buffer the run time of scheduled scaling actions
          when scaling out. For example, if the forecast says to add capacity at 10:00 AM, and
          the buffer time is 5 minutes, then the run time of the corresponding scheduled
          scaling action will be 9:55 AM. The intention is to give resources time to be
          provisioned. For example, it can take a few minutes to launch an EC2 instance. The
          actual amount of time required depends on several factors, such as the size of the
          instance and whether there are startup scripts to complete.

          The value must be less than the forecast interval duration of 3600 seconds (60
          minutes). The default is 300 seconds.

          Only valid when configuring predictive scaling.

        - **PredictiveScalingMaxCapacityBehavior** *(string) --*

          Defines the behavior that should be applied if the forecast capacity approaches or
          exceeds the maximum capacity specified for the resource. The default value is
          ``SetForecastCapacityToMaxCapacity`` .

          The following are possible values:

          * ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource
          capacity higher than the maximum capacity. The maximum capacity is enforced as a hard
          limit.

          * ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling may scale resource capacity
          higher than the maximum capacity to equal but not exceed forecast capacity.

          * ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling may scale resource
          capacity higher than the maximum capacity by a specified buffer value. The intention
          is to give the target tracking scaling policy extra capacity if unexpected traffic
          occurs.

          Only valid when configuring predictive scaling.

        - **PredictiveScalingMaxCapacityBuffer** *(integer) --*

          The size of the capacity buffer to use when the forecast capacity is close to or
          exceeds the maximum capacity. The value is specified as a percentage relative to the
          forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer,
          such that if the forecast capacity is 50, and the maximum capacity is 40, then the
          effective maximum capacity is 55.

          Only valid when configuring predictive scaling. Required if the
          **PredictiveScalingMaxCapacityBehavior** is set to
          ``SetMaxCapacityAboveForecastCapacity`` , and cannot be used otherwise.

          The range is 1-100.

        - **PredictiveScalingMode** *(string) --*

          The predictive scaling mode. The default value is ``ForecastAndScale`` . Otherwise,
          AWS Auto Scaling forecasts capacity but does not create any scheduled scaling actions
          based on the capacity forecast.

        - **ScalingPolicyUpdateBehavior** *(string) --*

          Controls whether a resource's externally created scaling policies are kept or
          replaced.

          The default value is ``KeepExternalPolicies`` . If the parameter is set to
          ``ReplaceExternalPolicies`` , any scaling policies that are external to AWS Auto
          Scaling are deleted and new target tracking scaling policies created.

          Only valid when configuring dynamic scaling.

          Condition: The number of existing policies to be replaced must be less than or equal
          to 50. If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all
          existing policies and does not create new ones.

        - **DisableDynamicScaling** *(boolean) --*

          Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic
          scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based
          on the specified target tracking configurations.

          The default is enabled (``false`` ).

    - **StatusCode** *(string) --*

      The status of the scaling plan.

      * ``Active`` - The scaling plan is active.

      * ``ActiveWithProblems`` - The scaling plan is active, but the scaling configuration for
      one or more resources could not be applied.

      * ``CreationInProgress`` - The scaling plan is being created.

      * ``CreationFailed`` - The scaling plan could not be created.

      * ``DeletionInProgress`` - The scaling plan is being deleted.

      * ``DeletionFailed`` - The scaling plan could not be deleted.

      * ``UpdateInProgress`` - The scaling plan is being updated.

      * ``UpdateFailed`` - The scaling plan could not be updated.

    - **StatusMessage** *(string) --*

      A simple message about the current status of the scaling plan.

    - **StatusStartTime** *(datetime) --*

      The Unix time stamp when the scaling plan entered the current status.

    - **CreationTime** *(datetime) --*

      The Unix time stamp when the scaling plan was created.
    """


_ClientDescribeScalingPlansResponseTypeDef = TypedDict(
    "_ClientDescribeScalingPlansResponseTypeDef",
    {
        "ScalingPlans": List[ClientDescribeScalingPlansResponseScalingPlansTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingPlansResponseTypeDef(
    _ClientDescribeScalingPlansResponseTypeDef
):
    """
    Type definition for `ClientDescribeScalingPlans` `Response`

    - **ScalingPlans** *(list) --*

      Information about the scaling plans.

      - *(dict) --*

        Represents a scaling plan.

        - **ScalingPlanName** *(string) --*

          The name of the scaling plan.

        - **ScalingPlanVersion** *(integer) --*

          The version number of the scaling plan.

        - **ApplicationSource** *(dict) --*

          The application source.

          - **CloudFormationStackARN** *(string) --*

            The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

          - **TagFilters** *(list) --*

            A set of tags (up to 50).

            - *(dict) --*

              Represents a tag.

              - **Key** *(string) --*

                The tag key.

              - **Values** *(list) --*

                The tag values (0 to 20).

                - *(string) --*

        - **ScalingInstructions** *(list) --*

          The scaling instructions.

          - *(dict) --*

            Describes a scaling instruction for a scalable resource.

            The scaling instruction is used in combination with a scaling plan, which is a set of
            instructions for configuring dynamic scaling and predictive scaling for the scalable
            resources in your application. Each scaling instruction applies to one resource.

            AWS Auto Scaling creates target tracking scaling policies based on the scaling
            instructions. Target tracking scaling policies adjust the capacity of your scalable
            resource as required to maintain resource utilization at the target value that you
            specified.

            AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling
            groups using a subset of parameters, including the load metric, the scaling metric, the
            target value for the scaling metric, the predictive scaling mode (forecast and scale or
            forecast only), and the desired behavior when the forecast capacity exceeds the maximum
            capacity of the resource. With predictive scaling, AWS Auto Scaling generates forecasts
            with traffic predictions for the two days ahead and schedules scaling actions that
            proactively add and remove resource capacity to match the forecast.

            We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to
            configure predictive scaling. At minimum, there must be 24 hours of historical data to
            generate a forecast.

            For more information, see `Getting Started with AWS Auto Scaling
            <https://docs.aws.amazon.com/autoscaling/plans/userguide/auto-scaling-getting-started.html>`__
            .

            - **ServiceNamespace** *(string) --*

              The namespace of the AWS service.

            - **ResourceId** *(string) --*

              The ID of the resource. This string consists of the resource type and unique
              identifier.

              * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique
              identifier is the name of the Auto Scaling group. Example:
              ``autoScalingGroup/my-asg`` .

              * ECS service - The resource type is ``service`` and the unique identifier is the
              cluster name and service name. Example: ``service/default/sample-webapp`` .

              * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
              identifier is the Spot Fleet request ID. Example:
              ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

              * DynamoDB table - The resource type is ``table`` and the unique identifier is the
              resource ID. Example: ``table/my-table`` .

              * DynamoDB global secondary index - The resource type is ``index`` and the unique
              identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

              * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is
              the cluster name. Example: ``cluster:my-db-cluster`` .

            - **ScalableDimension** *(string) --*

              The scalable dimension associated with the resource.

              * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto
              Scaling group.

              * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

              * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet
              request.

              * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
              table.

              * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a
              DynamoDB table.

              * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
              global secondary index.

              * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a
              DynamoDB global secondary index.

              * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
              cluster. Available for Aurora MySQL-compatible edition and Aurora
              PostgreSQL-compatible edition.

            - **MinCapacity** *(integer) --*

              The minimum capacity of the resource.

            - **MaxCapacity** *(integer) --*

              The maximum capacity of the resource. The exception to this upper limit is if you
              specify a non-default setting for **PredictiveScalingMaxCapacityBehavior** .

            - **TargetTrackingConfigurations** *(list) --*

              The structure that defines new target tracking configurations (up to 10). Each of
              these structures includes a specific scaling metric and a target value for the
              metric, along with various parameters to use with dynamic scaling.

              With predictive scaling and dynamic scaling, the resource scales based on the target
              tracking configuration that provides the largest capacity for both scale in and scale
              out.

              Condition: The scaling metric must be unique across target tracking configurations.

              - *(dict) --*

                Describes a target tracking configuration to use with AWS Auto Scaling. Used with
                ScalingInstruction and  ScalingPolicy .

                - **PredefinedScalingMetricSpecification** *(dict) --*

                  A predefined metric. You can specify either a predefined metric or a customized
                  metric.

                  - **PredefinedScalingMetricType** *(string) --*

                    The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
                    Auto Scaling groups, Spot Fleet requests, and ECS services.

                  - **ResourceLabel** *(string) --*

                    Identifies the resource associated with the metric type. You can't specify a
                    resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
                    is a target group for an Application Load Balancer attached to the Auto Scaling
                    group, Spot Fleet request, or ECS service.

                    The format is
                    app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
                    where:

                    * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
                    balancer ARN.

                    * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
                    target group ARN.

                - **CustomizedScalingMetricSpecification** *(dict) --*

                  A customized metric. You can specify either a predefined metric or a customized
                  metric.

                  - **MetricName** *(string) --*

                    The name of the metric.

                  - **Namespace** *(string) --*

                    The namespace of the metric.

                  - **Dimensions** *(list) --*

                    The dimensions of the metric.

                    Conditional: If you published your metric with dimensions, you must specify the
                    same dimensions in your customized scaling metric specification.

                    - *(dict) --*

                      Represents a dimension for a customized metric.

                      - **Name** *(string) --*

                        The name of the dimension.

                      - **Value** *(string) --*

                        The value of the dimension.

                  - **Statistic** *(string) --*

                    The statistic of the metric.

                  - **Unit** *(string) --*

                    The unit of the metric.

                - **TargetValue** *(float) --*

                  The target value for the metric. The range is 8.515920e-109 to 1.174271e+108
                  (Base 10) or 2e-360 to 2e360 (Base 2).

                - **DisableScaleIn** *(boolean) --*

                  Indicates whether scale in by the target tracking scaling policy is disabled. If
                  the value is ``true`` , scale in is disabled and the target tracking scaling
                  policy doesn't remove capacity from the scalable resource. Otherwise, scale in is
                  enabled and the target tracking scaling policy can remove capacity from the
                  scalable resource.

                  The default value is ``false`` .

                - **ScaleOutCooldown** *(integer) --*

                  The amount of time, in seconds, after a scale-out activity completes before
                  another scale-out activity can start. This value is not used if the scalable
                  resource is an Auto Scaling group.

                  While the cooldown period is in effect, the capacity that has been added by the
                  previous scale-out event that initiated the cooldown is calculated as part of the
                  desired capacity for the next scale out. The intention is to continuously (but
                  not excessively) scale out.

                - **ScaleInCooldown** *(integer) --*

                  The amount of time, in seconds, after a scale in activity completes before
                  another scale in activity can start. This value is not used if the scalable
                  resource is an Auto Scaling group.

                  The cooldown period is used to block subsequent scale in requests until it has
                  expired. The intention is to scale in conservatively to protect your
                  application's availability. However, if another alarm triggers a scale-out policy
                  during the cooldown period after a scale-in, AWS Auto Scaling scales out your
                  scalable target immediately.

                - **EstimatedInstanceWarmup** *(integer) --*

                  The estimated time, in seconds, until a newly launched instance can contribute to
                  the CloudWatch metrics. This value is used only if the resource is an Auto
                  Scaling group.

            - **PredefinedLoadMetricSpecification** *(dict) --*

              The predefined load metric to use for predictive scaling. This parameter or a
              **CustomizedLoadMetricSpecification** is required when configuring predictive
              scaling, and cannot be used otherwise.

              - **PredefinedLoadMetricType** *(string) --*

                The metric type.

              - **ResourceLabel** *(string) --*

                Identifies the resource associated with the metric type. You can't specify a
                resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is
                a target group for an Application Load Balancer attached to the Auto Scaling group.

                The format is
                app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
                where:

                * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
                balancer ARN.

                * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
                target group ARN.

            - **CustomizedLoadMetricSpecification** *(dict) --*

              The customized load metric to use for predictive scaling. This parameter or a
              **PredefinedLoadMetricSpecification** is required when configuring predictive
              scaling, and cannot be used otherwise.

              - **MetricName** *(string) --*

                The name of the metric.

              - **Namespace** *(string) --*

                The namespace of the metric.

              - **Dimensions** *(list) --*

                The dimensions of the metric.

                Conditional: If you published your metric with dimensions, you must specify the
                same dimensions in your customized load metric specification.

                - *(dict) --*

                  Represents a dimension for a customized metric.

                  - **Name** *(string) --*

                    The name of the dimension.

                  - **Value** *(string) --*

                    The value of the dimension.

              - **Statistic** *(string) --*

                The statistic of the metric. Currently, the value must always be ``Sum`` .

              - **Unit** *(string) --*

                The unit of the metric.

            - **ScheduledActionBufferTime** *(integer) --*

              The amount of time, in seconds, to buffer the run time of scheduled scaling actions
              when scaling out. For example, if the forecast says to add capacity at 10:00 AM, and
              the buffer time is 5 minutes, then the run time of the corresponding scheduled
              scaling action will be 9:55 AM. The intention is to give resources time to be
              provisioned. For example, it can take a few minutes to launch an EC2 instance. The
              actual amount of time required depends on several factors, such as the size of the
              instance and whether there are startup scripts to complete.

              The value must be less than the forecast interval duration of 3600 seconds (60
              minutes). The default is 300 seconds.

              Only valid when configuring predictive scaling.

            - **PredictiveScalingMaxCapacityBehavior** *(string) --*

              Defines the behavior that should be applied if the forecast capacity approaches or
              exceeds the maximum capacity specified for the resource. The default value is
              ``SetForecastCapacityToMaxCapacity`` .

              The following are possible values:

              * ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource
              capacity higher than the maximum capacity. The maximum capacity is enforced as a hard
              limit.

              * ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling may scale resource capacity
              higher than the maximum capacity to equal but not exceed forecast capacity.

              * ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling may scale resource
              capacity higher than the maximum capacity by a specified buffer value. The intention
              is to give the target tracking scaling policy extra capacity if unexpected traffic
              occurs.

              Only valid when configuring predictive scaling.

            - **PredictiveScalingMaxCapacityBuffer** *(integer) --*

              The size of the capacity buffer to use when the forecast capacity is close to or
              exceeds the maximum capacity. The value is specified as a percentage relative to the
              forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer,
              such that if the forecast capacity is 50, and the maximum capacity is 40, then the
              effective maximum capacity is 55.

              Only valid when configuring predictive scaling. Required if the
              **PredictiveScalingMaxCapacityBehavior** is set to
              ``SetMaxCapacityAboveForecastCapacity`` , and cannot be used otherwise.

              The range is 1-100.

            - **PredictiveScalingMode** *(string) --*

              The predictive scaling mode. The default value is ``ForecastAndScale`` . Otherwise,
              AWS Auto Scaling forecasts capacity but does not create any scheduled scaling actions
              based on the capacity forecast.

            - **ScalingPolicyUpdateBehavior** *(string) --*

              Controls whether a resource's externally created scaling policies are kept or
              replaced.

              The default value is ``KeepExternalPolicies`` . If the parameter is set to
              ``ReplaceExternalPolicies`` , any scaling policies that are external to AWS Auto
              Scaling are deleted and new target tracking scaling policies created.

              Only valid when configuring dynamic scaling.

              Condition: The number of existing policies to be replaced must be less than or equal
              to 50. If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all
              existing policies and does not create new ones.

            - **DisableDynamicScaling** *(boolean) --*

              Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic
              scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based
              on the specified target tracking configurations.

              The default is enabled (``false`` ).

        - **StatusCode** *(string) --*

          The status of the scaling plan.

          * ``Active`` - The scaling plan is active.

          * ``ActiveWithProblems`` - The scaling plan is active, but the scaling configuration for
          one or more resources could not be applied.

          * ``CreationInProgress`` - The scaling plan is being created.

          * ``CreationFailed`` - The scaling plan could not be created.

          * ``DeletionInProgress`` - The scaling plan is being deleted.

          * ``DeletionFailed`` - The scaling plan could not be deleted.

          * ``UpdateInProgress`` - The scaling plan is being updated.

          * ``UpdateFailed`` - The scaling plan could not be updated.

        - **StatusMessage** *(string) --*

          A simple message about the current status of the scaling plan.

        - **StatusStartTime** *(datetime) --*

          The Unix time stamp when the scaling plan entered the current status.

        - **CreationTime** *(datetime) --*

          The Unix time stamp when the scaling plan was created.

    - **NextToken** *(string) --*

      The token required to get the next set of results. This value is ``null`` if there are no
      more results to return.
    """


_ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef = TypedDict(
    "_ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef",
    {"Timestamp": datetime, "Value": float},
    total=False,
)


class ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef(
    _ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef
):
    """
    Type definition for `ClientGetScalingPlanResourceForecastDataResponse` `Datapoints`

    Represents a single value in the forecast data used for predictive scaling.

    - **Timestamp** *(datetime) --*

      The time stamp for the data point in UTC format.

    - **Value** *(float) --*

      The value of the data point.
    """


_ClientGetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "_ClientGetScalingPlanResourceForecastDataResponseTypeDef",
    {
        "Datapoints": List[
            ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef
        ]
    },
    total=False,
)


class ClientGetScalingPlanResourceForecastDataResponseTypeDef(
    _ClientGetScalingPlanResourceForecastDataResponseTypeDef
):
    """
    Type definition for `ClientGetScalingPlanResourceForecastData` `Response`

    - **Datapoints** *(list) --*

      The data points to return.

      - *(dict) --*

        Represents a single value in the forecast data used for predictive scaling.

        - **Timestamp** *(datetime) --*

          The time stamp for the data point in UTC format.

        - **Value** *(float) --*

          The value of the data point.
    """


_ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef = TypedDict(
    "_ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef(
    _ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef
):
    """
    Type definition for `ClientUpdateScalingPlanApplicationSource` `TagFilters`

    Represents a tag.

    - **Key** *(string) --*

      The tag key.

    - **Values** *(list) --*

      The tag values (0 to 20).

      - *(string) --*
    """


_ClientUpdateScalingPlanApplicationSourceTypeDef = TypedDict(
    "_ClientUpdateScalingPlanApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef],
    },
    total=False,
)


class ClientUpdateScalingPlanApplicationSourceTypeDef(
    _ClientUpdateScalingPlanApplicationSourceTypeDef
):
    """
    Type definition for `ClientUpdateScalingPlan` `ApplicationSource`

    A CloudFormation stack or set of tags.

    - **CloudFormationStackARN** *(string) --*

      The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

    - **TagFilters** *(list) --*

      A set of tags (up to 50).

      - *(dict) --*

        Represents a tag.

        - **Key** *(string) --*

          The tag key.

        - **Values** *(list) --*

          The tag values (0 to 20).

          - *(string) --*
    """


_ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
)


class ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef(
    _ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecification` `Dimensions`

    Represents a dimension for a customized metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the dimension.
    """


_RequiredClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {"MetricName": str, "Namespace": str, "Statistic": str},
)
_OptionalClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "Dimensions": List[
            ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Unit": str,
    },
    total=False,
)


class ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef(
    _RequiredClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
    _OptionalClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientUpdateScalingPlanScalingInstructions` `CustomizedLoadMetricSpecification`

    The customized load metric to use for predictive scaling. This parameter or a
    **PredefinedLoadMetricSpecification** is required when configuring predictive scaling, and
    cannot be used otherwise.

    - **MetricName** *(string) --* **[REQUIRED]**

      The name of the metric.

    - **Namespace** *(string) --* **[REQUIRED]**

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the same
      dimensions in your customized load metric specification.

      - *(dict) --*

        Represents a dimension for a customized metric.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the dimension.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the dimension.

    - **Statistic** *(string) --* **[REQUIRED]**

      The statistic of the metric. Currently, the value must always be ``Sum`` .

    - **Unit** *(string) --*

      The unit of the metric.
    """


_RequiredClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {"PredefinedLoadMetricType": str},
)
_OptionalClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {"ResourceLabel": str},
    total=False,
)


class ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef(
    _RequiredClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
    _OptionalClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientUpdateScalingPlanScalingInstructions` `PredefinedLoadMetricSpecification`

    The predefined load metric to use for predictive scaling. This parameter or a
    **CustomizedLoadMetricSpecification** is required when configuring predictive scaling, and
    cannot be used otherwise.

    - **PredefinedLoadMetricType** *(string) --* **[REQUIRED]**

      The metric type.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a resource label
      unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group for an
      Application Load Balancer attached to the Auto Scaling group.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN.

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
      group ARN.
    """


_ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
)


class ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecification` `Dimensions`

    Represents a dimension for a customized metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the dimension.
    """


_RequiredClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {"MetricName": str, "Namespace": str, "Statistic": str},
)
_OptionalClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "Dimensions": List[
            ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Unit": str,
    },
    total=False,
)


class ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef(
    _RequiredClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
    _OptionalClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurations` `CustomizedScalingMetricSpecification`

    A customized metric. You can specify either a predefined metric or a customized metric.

    - **MetricName** *(string) --* **[REQUIRED]**

      The name of the metric.

    - **Namespace** *(string) --* **[REQUIRED]**

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the same
      dimensions in your customized scaling metric specification.

      - *(dict) --*

        Represents a dimension for a customized metric.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the dimension.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the dimension.

    - **Statistic** *(string) --* **[REQUIRED]**

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_RequiredClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {"PredefinedScalingMetricType": str},
)
_OptionalClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {"ResourceLabel": str},
    total=False,
)


class ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef(
    _RequiredClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
    _OptionalClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurations` `PredefinedScalingMetricSpecification`

    A predefined metric. You can specify either a predefined metric or a customized metric.

    - **PredefinedScalingMetricType** *(string) --* **[REQUIRED]**

      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Auto
      Scaling groups, Spot Fleet requests, and ECS services.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a resource
      label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
      group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet
      request, or ECS service.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer
      ARN.

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
      group ARN.
    """


_RequiredClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "_RequiredClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {"TargetValue": float},
)
_OptionalClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "_OptionalClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)


class ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef(
    _RequiredClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef,
    _OptionalClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef,
):
    """
    Type definition for `ClientUpdateScalingPlanScalingInstructions` `TargetTrackingConfigurations`

    Describes a target tracking configuration to use with AWS Auto Scaling. Used with
    ScalingInstruction and  ScalingPolicy .

    - **PredefinedScalingMetricSpecification** *(dict) --*

      A predefined metric. You can specify either a predefined metric or a customized metric.

      - **PredefinedScalingMetricType** *(string) --* **[REQUIRED]**

        The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Auto
        Scaling groups, Spot Fleet requests, and ECS services.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a resource
        label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
        group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet
        request, or ECS service.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer
        ARN.

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
        group ARN.

    - **CustomizedScalingMetricSpecification** *(dict) --*

      A customized metric. You can specify either a predefined metric or a customized metric.

      - **MetricName** *(string) --* **[REQUIRED]**

        The name of the metric.

      - **Namespace** *(string) --* **[REQUIRED]**

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the same
        dimensions in your customized scaling metric specification.

        - *(dict) --*

          Represents a dimension for a customized metric.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the dimension.

          - **Value** *(string) --* **[REQUIRED]**

            The value of the dimension.

      - **Statistic** *(string) --* **[REQUIRED]**

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **TargetValue** *(float) --* **[REQUIRED]**

      The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or
      2e-360 to 2e360 (Base 2).

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scale in by the target tracking scaling policy is disabled. If the
      value is ``true`` , scale in is disabled and the target tracking scaling policy doesn't
      remove capacity from the scalable resource. Otherwise, scale in is enabled and the target
      tracking scaling policy can remove capacity from the scalable resource.

      The default value is ``false`` .

    - **ScaleOutCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-out activity completes before another
      scale-out activity can start. This value is not used if the scalable resource is an Auto
      Scaling group.

      While the cooldown period is in effect, the capacity that has been added by the previous
      scale-out event that initiated the cooldown is calculated as part of the desired capacity
      for the next scale out. The intention is to continuously (but not excessively) scale out.

    - **ScaleInCooldown** *(integer) --*

      The amount of time, in seconds, after a scale in activity completes before another scale
      in activity can start. This value is not used if the scalable resource is an Auto Scaling
      group.

      The cooldown period is used to block subsequent scale in requests until it has expired.
      The intention is to scale in conservatively to protect your application's availability.
      However, if another alarm triggers a scale-out policy during the cooldown period after a
      scale-in, AWS Auto Scaling scales out your scalable target immediately.

    - **EstimatedInstanceWarmup** *(integer) --*

      The estimated time, in seconds, until a newly launched instance can contribute to the
      CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.
    """


_RequiredClientUpdateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_RequiredClientUpdateScalingPlanScalingInstructionsTypeDef",
    {
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
    },
)
_OptionalClientUpdateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_OptionalClientUpdateScalingPlanScalingInstructionsTypeDef",
    {
        "PredefinedLoadMetricSpecification": ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": str,
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": str,
        "ScalingPolicyUpdateBehavior": str,
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class ClientUpdateScalingPlanScalingInstructionsTypeDef(
    _RequiredClientUpdateScalingPlanScalingInstructionsTypeDef,
    _OptionalClientUpdateScalingPlanScalingInstructionsTypeDef,
):
    """
    Type definition for `ClientUpdateScalingPlan` `ScalingInstructions`

    Describes a scaling instruction for a scalable resource.

    The scaling instruction is used in combination with a scaling plan, which is a set of
    instructions for configuring dynamic scaling and predictive scaling for the scalable resources
    in your application. Each scaling instruction applies to one resource.

    AWS Auto Scaling creates target tracking scaling policies based on the scaling instructions.
    Target tracking scaling policies adjust the capacity of your scalable resource as required to
    maintain resource utilization at the target value that you specified.

    AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling groups
    using a subset of parameters, including the load metric, the scaling metric, the target value
    for the scaling metric, the predictive scaling mode (forecast and scale or forecast only), and
    the desired behavior when the forecast capacity exceeds the maximum capacity of the resource.
    With predictive scaling, AWS Auto Scaling generates forecasts with traffic predictions for the
    two days ahead and schedules scaling actions that proactively add and remove resource capacity
    to match the forecast.

    We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to configure
    predictive scaling. At minimum, there must be 24 hours of historical data to generate a
    forecast.

    For more information, see `Getting Started with AWS Auto Scaling
    <https://docs.aws.amazon.com/autoscaling/plans/userguide/auto-scaling-getting-started.html>`__ .

    - **ServiceNamespace** *(string) --* **[REQUIRED]**

      The namespace of the AWS service.

    - **ResourceId** *(string) --* **[REQUIRED]**

      The ID of the resource. This string consists of the resource type and unique identifier.

      * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique identifier is
      the name of the Auto Scaling group. Example: ``autoScalingGroup/my-asg`` .

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique identifier
      is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the resource
      ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique identifier
      is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

    - **ScalableDimension** *(string) --* **[REQUIRED]**

      The scalable dimension associated with the resource.

      * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto Scaling
      group.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.

      * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.

      * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global
      secondary index.

      * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
      global secondary index.

      * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
      Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

    - **MinCapacity** *(integer) --* **[REQUIRED]**

      The minimum capacity of the resource.

    - **MaxCapacity** *(integer) --* **[REQUIRED]**

      The maximum capacity of the resource. The exception to this upper limit is if you specify a
      non-default setting for **PredictiveScalingMaxCapacityBehavior** .

    - **TargetTrackingConfigurations** *(list) --* **[REQUIRED]**

      The structure that defines new target tracking configurations (up to 10). Each of these
      structures includes a specific scaling metric and a target value for the metric, along with
      various parameters to use with dynamic scaling.

      With predictive scaling and dynamic scaling, the resource scales based on the target tracking
      configuration that provides the largest capacity for both scale in and scale out.

      Condition: The scaling metric must be unique across target tracking configurations.

      - *(dict) --*

        Describes a target tracking configuration to use with AWS Auto Scaling. Used with
        ScalingInstruction and  ScalingPolicy .

        - **PredefinedScalingMetricSpecification** *(dict) --*

          A predefined metric. You can specify either a predefined metric or a customized metric.

          - **PredefinedScalingMetricType** *(string) --* **[REQUIRED]**

            The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Auto
            Scaling groups, Spot Fleet requests, and ECS services.

          - **ResourceLabel** *(string) --*

            Identifies the resource associated with the metric type. You can't specify a resource
            label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
            group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet
            request, or ECS service.

            The format is
            app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
            where:

            * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer
            ARN.

            * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
            group ARN.

        - **CustomizedScalingMetricSpecification** *(dict) --*

          A customized metric. You can specify either a predefined metric or a customized metric.

          - **MetricName** *(string) --* **[REQUIRED]**

            The name of the metric.

          - **Namespace** *(string) --* **[REQUIRED]**

            The namespace of the metric.

          - **Dimensions** *(list) --*

            The dimensions of the metric.

            Conditional: If you published your metric with dimensions, you must specify the same
            dimensions in your customized scaling metric specification.

            - *(dict) --*

              Represents a dimension for a customized metric.

              - **Name** *(string) --* **[REQUIRED]**

                The name of the dimension.

              - **Value** *(string) --* **[REQUIRED]**

                The value of the dimension.

          - **Statistic** *(string) --* **[REQUIRED]**

            The statistic of the metric.

          - **Unit** *(string) --*

            The unit of the metric.

        - **TargetValue** *(float) --* **[REQUIRED]**

          The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or
          2e-360 to 2e360 (Base 2).

        - **DisableScaleIn** *(boolean) --*

          Indicates whether scale in by the target tracking scaling policy is disabled. If the
          value is ``true`` , scale in is disabled and the target tracking scaling policy doesn't
          remove capacity from the scalable resource. Otherwise, scale in is enabled and the target
          tracking scaling policy can remove capacity from the scalable resource.

          The default value is ``false`` .

        - **ScaleOutCooldown** *(integer) --*

          The amount of time, in seconds, after a scale-out activity completes before another
          scale-out activity can start. This value is not used if the scalable resource is an Auto
          Scaling group.

          While the cooldown period is in effect, the capacity that has been added by the previous
          scale-out event that initiated the cooldown is calculated as part of the desired capacity
          for the next scale out. The intention is to continuously (but not excessively) scale out.

        - **ScaleInCooldown** *(integer) --*

          The amount of time, in seconds, after a scale in activity completes before another scale
          in activity can start. This value is not used if the scalable resource is an Auto Scaling
          group.

          The cooldown period is used to block subsequent scale in requests until it has expired.
          The intention is to scale in conservatively to protect your application's availability.
          However, if another alarm triggers a scale-out policy during the cooldown period after a
          scale-in, AWS Auto Scaling scales out your scalable target immediately.

        - **EstimatedInstanceWarmup** *(integer) --*

          The estimated time, in seconds, until a newly launched instance can contribute to the
          CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.

    - **PredefinedLoadMetricSpecification** *(dict) --*

      The predefined load metric to use for predictive scaling. This parameter or a
      **CustomizedLoadMetricSpecification** is required when configuring predictive scaling, and
      cannot be used otherwise.

      - **PredefinedLoadMetricType** *(string) --* **[REQUIRED]**

        The metric type.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a resource label
        unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group for an
        Application Load Balancer attached to the Auto Scaling group.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN.

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
        group ARN.

    - **CustomizedLoadMetricSpecification** *(dict) --*

      The customized load metric to use for predictive scaling. This parameter or a
      **PredefinedLoadMetricSpecification** is required when configuring predictive scaling, and
      cannot be used otherwise.

      - **MetricName** *(string) --* **[REQUIRED]**

        The name of the metric.

      - **Namespace** *(string) --* **[REQUIRED]**

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the same
        dimensions in your customized load metric specification.

        - *(dict) --*

          Represents a dimension for a customized metric.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the dimension.

          - **Value** *(string) --* **[REQUIRED]**

            The value of the dimension.

      - **Statistic** *(string) --* **[REQUIRED]**

        The statistic of the metric. Currently, the value must always be ``Sum`` .

      - **Unit** *(string) --*

        The unit of the metric.

    - **ScheduledActionBufferTime** *(integer) --*

      The amount of time, in seconds, to buffer the run time of scheduled scaling actions when
      scaling out. For example, if the forecast says to add capacity at 10:00 AM, and the buffer
      time is 5 minutes, then the run time of the corresponding scheduled scaling action will be
      9:55 AM. The intention is to give resources time to be provisioned. For example, it can take
      a few minutes to launch an EC2 instance. The actual amount of time required depends on
      several factors, such as the size of the instance and whether there are startup scripts to
      complete.

      The value must be less than the forecast interval duration of 3600 seconds (60 minutes). The
      default is 300 seconds.

      Only valid when configuring predictive scaling.

    - **PredictiveScalingMaxCapacityBehavior** *(string) --*

      Defines the behavior that should be applied if the forecast capacity approaches or exceeds
      the maximum capacity specified for the resource. The default value is
      ``SetForecastCapacityToMaxCapacity`` .

      The following are possible values:

      * ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource capacity
      higher than the maximum capacity. The maximum capacity is enforced as a hard limit.

      * ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling may scale resource capacity higher
      than the maximum capacity to equal but not exceed forecast capacity.

      * ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling may scale resource capacity
      higher than the maximum capacity by a specified buffer value. The intention is to give the
      target tracking scaling policy extra capacity if unexpected traffic occurs.

      Only valid when configuring predictive scaling.

    - **PredictiveScalingMaxCapacityBuffer** *(integer) --*

      The size of the capacity buffer to use when the forecast capacity is close to or exceeds the
      maximum capacity. The value is specified as a percentage relative to the forecast capacity.
      For example, if the buffer is 10, this means a 10 percent buffer, such that if the forecast
      capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55.

      Only valid when configuring predictive scaling. Required if the
      **PredictiveScalingMaxCapacityBehavior** is set to ``SetMaxCapacityAboveForecastCapacity`` ,
      and cannot be used otherwise.

      The range is 1-100.

    - **PredictiveScalingMode** *(string) --*

      The predictive scaling mode. The default value is ``ForecastAndScale`` . Otherwise, AWS Auto
      Scaling forecasts capacity but does not create any scheduled scaling actions based on the
      capacity forecast.

    - **ScalingPolicyUpdateBehavior** *(string) --*

      Controls whether a resource's externally created scaling policies are kept or replaced.

      The default value is ``KeepExternalPolicies`` . If the parameter is set to
      ``ReplaceExternalPolicies`` , any scaling policies that are external to AWS Auto Scaling are
      deleted and new target tracking scaling policies created.

      Only valid when configuring dynamic scaling.

      Condition: The number of existing policies to be replaced must be less than or equal to 50.
      If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all existing
      policies and does not create new ones.

    - **DisableDynamicScaling** *(boolean) --*

      Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic scaling is
      enabled, AWS Auto Scaling creates target tracking scaling policies based on the specified
      target tracking configurations.

      The default is enabled (``false`` ).
    """


_DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef(
    _DescribeScalingPlanResourcesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeScalingPlanResourcesPaginate` `PaginationConfig`

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


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecification` `Dimensions`

    Represents a dimension for a customized metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value of the dimension.
    """


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef
):
    """
    Type definition for `DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfiguration` `CustomizedScalingMetricSpecification`

    A customized metric. You can specify either a predefined metric or a customized
    metric.

    - **MetricName** *(string) --*

      The name of the metric.

    - **Namespace** *(string) --*

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the
      same dimensions in your customized scaling metric specification.

      - *(dict) --*

        Represents a dimension for a customized metric.

        - **Name** *(string) --*

          The name of the dimension.

        - **Value** *(string) --*

          The value of the dimension.

    - **Statistic** *(string) --*

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
    {"PredefinedScalingMetricType": str, "ResourceLabel": str},
    total=False,
)


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef
):
    """
    Type definition for `DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfiguration` `PredefinedScalingMetricSpecification`

    A predefined metric. You can specify either a predefined metric or a customized
    metric.

    - **PredefinedScalingMetricType** *(string) --*

      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
      Auto Scaling groups, Spot Fleet requests, and ECS services.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a
      resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
      is a target group for an Application Load Balancer attached to the Auto Scaling
      group, Spot Fleet request, or ECS service.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
      balancer ARN.

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
      target group ARN.
    """


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedScalingMetricSpecification": DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef
):
    """
    Type definition for `DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPolicies` `TargetTrackingConfiguration`

    The target tracking scaling policy. Includes support for predefined or customized
    metrics.

    - **PredefinedScalingMetricSpecification** *(dict) --*

      A predefined metric. You can specify either a predefined metric or a customized
      metric.

      - **PredefinedScalingMetricType** *(string) --*

        The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
        Auto Scaling groups, Spot Fleet requests, and ECS services.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a
        resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
        is a target group for an Application Load Balancer attached to the Auto Scaling
        group, Spot Fleet request, or ECS service.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
        balancer ARN.

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
        target group ARN.

    - **CustomizedScalingMetricSpecification** *(dict) --*

      A customized metric. You can specify either a predefined metric or a customized
      metric.

      - **MetricName** *(string) --*

        The name of the metric.

      - **Namespace** *(string) --*

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the
        same dimensions in your customized scaling metric specification.

        - *(dict) --*

          Represents a dimension for a customized metric.

          - **Name** *(string) --*

            The name of the dimension.

          - **Value** *(string) --*

            The value of the dimension.

      - **Statistic** *(string) --*

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **TargetValue** *(float) --*

      The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base
      10) or 2e-360 to 2e360 (Base 2).

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scale in by the target tracking scaling policy is disabled. If
      the value is ``true`` , scale in is disabled and the target tracking scaling policy
      doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled
      and the target tracking scaling policy can remove capacity from the scalable
      resource.

      The default value is ``false`` .

    - **ScaleOutCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-out activity completes before another
      scale-out activity can start. This value is not used if the scalable resource is an
      Auto Scaling group.

      While the cooldown period is in effect, the capacity that has been added by the
      previous scale-out event that initiated the cooldown is calculated as part of the
      desired capacity for the next scale out. The intention is to continuously (but not
      excessively) scale out.

    - **ScaleInCooldown** *(integer) --*

      The amount of time, in seconds, after a scale in activity completes before another
      scale in activity can start. This value is not used if the scalable resource is an
      Auto Scaling group.

      The cooldown period is used to block subsequent scale in requests until it has
      expired. The intention is to scale in conservatively to protect your application's
      availability. However, if another alarm triggers a scale-out policy during the
      cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target
      immediately.

    - **EstimatedInstanceWarmup** *(integer) --*

      The estimated time, in seconds, until a newly launched instance can contribute to
      the CloudWatch metrics. This value is used only if the resource is an Auto Scaling
      group.
    """


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": str,
        "TargetTrackingConfiguration": DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef
):
    """
    Type definition for `DescribeScalingPlanResourcesPaginateResponseScalingPlanResources` `ScalingPolicies`

    Represents a scaling policy.

    - **PolicyName** *(string) --*

      The name of the scaling policy.

    - **PolicyType** *(string) --*

      The type of scaling policy.

    - **TargetTrackingConfiguration** *(dict) --*

      The target tracking scaling policy. Includes support for predefined or customized
      metrics.

      - **PredefinedScalingMetricSpecification** *(dict) --*

        A predefined metric. You can specify either a predefined metric or a customized
        metric.

        - **PredefinedScalingMetricType** *(string) --*

          The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
          Auto Scaling groups, Spot Fleet requests, and ECS services.

        - **ResourceLabel** *(string) --*

          Identifies the resource associated with the metric type. You can't specify a
          resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
          is a target group for an Application Load Balancer attached to the Auto Scaling
          group, Spot Fleet request, or ECS service.

          The format is
          app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
          where:

          * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
          balancer ARN.

          * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
          target group ARN.

      - **CustomizedScalingMetricSpecification** *(dict) --*

        A customized metric. You can specify either a predefined metric or a customized
        metric.

        - **MetricName** *(string) --*

          The name of the metric.

        - **Namespace** *(string) --*

          The namespace of the metric.

        - **Dimensions** *(list) --*

          The dimensions of the metric.

          Conditional: If you published your metric with dimensions, you must specify the
          same dimensions in your customized scaling metric specification.

          - *(dict) --*

            Represents a dimension for a customized metric.

            - **Name** *(string) --*

              The name of the dimension.

            - **Value** *(string) --*

              The value of the dimension.

        - **Statistic** *(string) --*

          The statistic of the metric.

        - **Unit** *(string) --*

          The unit of the metric.

      - **TargetValue** *(float) --*

        The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base
        10) or 2e-360 to 2e360 (Base 2).

      - **DisableScaleIn** *(boolean) --*

        Indicates whether scale in by the target tracking scaling policy is disabled. If
        the value is ``true`` , scale in is disabled and the target tracking scaling policy
        doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled
        and the target tracking scaling policy can remove capacity from the scalable
        resource.

        The default value is ``false`` .

      - **ScaleOutCooldown** *(integer) --*

        The amount of time, in seconds, after a scale-out activity completes before another
        scale-out activity can start. This value is not used if the scalable resource is an
        Auto Scaling group.

        While the cooldown period is in effect, the capacity that has been added by the
        previous scale-out event that initiated the cooldown is calculated as part of the
        desired capacity for the next scale out. The intention is to continuously (but not
        excessively) scale out.

      - **ScaleInCooldown** *(integer) --*

        The amount of time, in seconds, after a scale in activity completes before another
        scale in activity can start. This value is not used if the scalable resource is an
        Auto Scaling group.

        The cooldown period is used to block subsequent scale in requests until it has
        expired. The intention is to scale in conservatively to protect your application's
        availability. However, if another alarm triggers a scale-out policy during the
        cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target
        immediately.

      - **EstimatedInstanceWarmup** *(integer) --*

        The estimated time, in seconds, until a newly launched instance can contribute to
        the CloudWatch metrics. This value is used only if the resource is an Auto Scaling
        group.
    """


_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "ScalingPolicies": List[
            DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesScalingPoliciesTypeDef
        ],
        "ScalingStatusCode": str,
        "ScalingStatusMessage": str,
    },
    total=False,
)


class DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef
):
    """
    Type definition for `DescribeScalingPlanResourcesPaginateResponse` `ScalingPlanResources`

    Represents a scalable resource.

    - **ScalingPlanName** *(string) --*

      The name of the scaling plan.

    - **ScalingPlanVersion** *(integer) --*

      The version number of the scaling plan.

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service.

    - **ResourceId** *(string) --*

      The ID of the resource. This string consists of the resource type and unique identifier.

      * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique
      identifier is the name of the Auto Scaling group. Example: ``autoScalingGroup/my-asg`` .

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

    - **ScalableDimension** *(string) --*

      The scalable dimension for the resource.

      * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto
      Scaling group.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
      table.

      * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
      table.

      * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
      global secondary index.

      * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
      global secondary index.

      * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
      cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible
      edition.

    - **ScalingPolicies** *(list) --*

      The scaling policies.

      - *(dict) --*

        Represents a scaling policy.

        - **PolicyName** *(string) --*

          The name of the scaling policy.

        - **PolicyType** *(string) --*

          The type of scaling policy.

        - **TargetTrackingConfiguration** *(dict) --*

          The target tracking scaling policy. Includes support for predefined or customized
          metrics.

          - **PredefinedScalingMetricSpecification** *(dict) --*

            A predefined metric. You can specify either a predefined metric or a customized
            metric.

            - **PredefinedScalingMetricType** *(string) --*

              The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
              Auto Scaling groups, Spot Fleet requests, and ECS services.

            - **ResourceLabel** *(string) --*

              Identifies the resource associated with the metric type. You can't specify a
              resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
              is a target group for an Application Load Balancer attached to the Auto Scaling
              group, Spot Fleet request, or ECS service.

              The format is
              app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
              where:

              * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
              balancer ARN.

              * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
              target group ARN.

          - **CustomizedScalingMetricSpecification** *(dict) --*

            A customized metric. You can specify either a predefined metric or a customized
            metric.

            - **MetricName** *(string) --*

              The name of the metric.

            - **Namespace** *(string) --*

              The namespace of the metric.

            - **Dimensions** *(list) --*

              The dimensions of the metric.

              Conditional: If you published your metric with dimensions, you must specify the
              same dimensions in your customized scaling metric specification.

              - *(dict) --*

                Represents a dimension for a customized metric.

                - **Name** *(string) --*

                  The name of the dimension.

                - **Value** *(string) --*

                  The value of the dimension.

            - **Statistic** *(string) --*

              The statistic of the metric.

            - **Unit** *(string) --*

              The unit of the metric.

          - **TargetValue** *(float) --*

            The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base
            10) or 2e-360 to 2e360 (Base 2).

          - **DisableScaleIn** *(boolean) --*

            Indicates whether scale in by the target tracking scaling policy is disabled. If
            the value is ``true`` , scale in is disabled and the target tracking scaling policy
            doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled
            and the target tracking scaling policy can remove capacity from the scalable
            resource.

            The default value is ``false`` .

          - **ScaleOutCooldown** *(integer) --*

            The amount of time, in seconds, after a scale-out activity completes before another
            scale-out activity can start. This value is not used if the scalable resource is an
            Auto Scaling group.

            While the cooldown period is in effect, the capacity that has been added by the
            previous scale-out event that initiated the cooldown is calculated as part of the
            desired capacity for the next scale out. The intention is to continuously (but not
            excessively) scale out.

          - **ScaleInCooldown** *(integer) --*

            The amount of time, in seconds, after a scale in activity completes before another
            scale in activity can start. This value is not used if the scalable resource is an
            Auto Scaling group.

            The cooldown period is used to block subsequent scale in requests until it has
            expired. The intention is to scale in conservatively to protect your application's
            availability. However, if another alarm triggers a scale-out policy during the
            cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target
            immediately.

          - **EstimatedInstanceWarmup** *(integer) --*

            The estimated time, in seconds, until a newly launched instance can contribute to
            the CloudWatch metrics. This value is used only if the resource is an Auto Scaling
            group.

    - **ScalingStatusCode** *(string) --*

      The scaling status of the resource.

      * ``Active`` - The scaling configuration is active.

      * ``Inactive`` - The scaling configuration is not active because the scaling plan is
      being created or the scaling configuration could not be applied. Check the status message
      for more information.

      * ``PartiallyActive`` - The scaling configuration is partially active because the scaling
      plan is being created or deleted or the scaling configuration could not be fully applied.
      Check the status message for more information.

    - **ScalingStatusMessage** *(string) --*

      A simple message about the current scaling status of the resource.
    """


_DescribeScalingPlanResourcesPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingPlanResourcesPaginateResponseTypeDef",
    {
        "ScalingPlanResources": List[
            DescribeScalingPlanResourcesPaginateResponseScalingPlanResourcesTypeDef
        ]
    },
    total=False,
)


class DescribeScalingPlanResourcesPaginateResponseTypeDef(
    _DescribeScalingPlanResourcesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeScalingPlanResourcesPaginate` `Response`

    - **ScalingPlanResources** *(list) --*

      Information about the scalable resources.

      - *(dict) --*

        Represents a scalable resource.

        - **ScalingPlanName** *(string) --*

          The name of the scaling plan.

        - **ScalingPlanVersion** *(integer) --*

          The version number of the scaling plan.

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service.

        - **ResourceId** *(string) --*

          The ID of the resource. This string consists of the resource type and unique identifier.

          * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique
          identifier is the name of the Auto Scaling group. Example: ``autoScalingGroup/my-asg`` .

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

        - **ScalableDimension** *(string) --*

          The scalable dimension for the resource.

          * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto
          Scaling group.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
          cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible
          edition.

        - **ScalingPolicies** *(list) --*

          The scaling policies.

          - *(dict) --*

            Represents a scaling policy.

            - **PolicyName** *(string) --*

              The name of the scaling policy.

            - **PolicyType** *(string) --*

              The type of scaling policy.

            - **TargetTrackingConfiguration** *(dict) --*

              The target tracking scaling policy. Includes support for predefined or customized
              metrics.

              - **PredefinedScalingMetricSpecification** *(dict) --*

                A predefined metric. You can specify either a predefined metric or a customized
                metric.

                - **PredefinedScalingMetricType** *(string) --*

                  The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
                  Auto Scaling groups, Spot Fleet requests, and ECS services.

                - **ResourceLabel** *(string) --*

                  Identifies the resource associated with the metric type. You can't specify a
                  resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
                  is a target group for an Application Load Balancer attached to the Auto Scaling
                  group, Spot Fleet request, or ECS service.

                  The format is
                  app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
                  where:

                  * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
                  balancer ARN.

                  * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
                  target group ARN.

              - **CustomizedScalingMetricSpecification** *(dict) --*

                A customized metric. You can specify either a predefined metric or a customized
                metric.

                - **MetricName** *(string) --*

                  The name of the metric.

                - **Namespace** *(string) --*

                  The namespace of the metric.

                - **Dimensions** *(list) --*

                  The dimensions of the metric.

                  Conditional: If you published your metric with dimensions, you must specify the
                  same dimensions in your customized scaling metric specification.

                  - *(dict) --*

                    Represents a dimension for a customized metric.

                    - **Name** *(string) --*

                      The name of the dimension.

                    - **Value** *(string) --*

                      The value of the dimension.

                - **Statistic** *(string) --*

                  The statistic of the metric.

                - **Unit** *(string) --*

                  The unit of the metric.

              - **TargetValue** *(float) --*

                The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base
                10) or 2e-360 to 2e360 (Base 2).

              - **DisableScaleIn** *(boolean) --*

                Indicates whether scale in by the target tracking scaling policy is disabled. If
                the value is ``true`` , scale in is disabled and the target tracking scaling policy
                doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled
                and the target tracking scaling policy can remove capacity from the scalable
                resource.

                The default value is ``false`` .

              - **ScaleOutCooldown** *(integer) --*

                The amount of time, in seconds, after a scale-out activity completes before another
                scale-out activity can start. This value is not used if the scalable resource is an
                Auto Scaling group.

                While the cooldown period is in effect, the capacity that has been added by the
                previous scale-out event that initiated the cooldown is calculated as part of the
                desired capacity for the next scale out. The intention is to continuously (but not
                excessively) scale out.

              - **ScaleInCooldown** *(integer) --*

                The amount of time, in seconds, after a scale in activity completes before another
                scale in activity can start. This value is not used if the scalable resource is an
                Auto Scaling group.

                The cooldown period is used to block subsequent scale in requests until it has
                expired. The intention is to scale in conservatively to protect your application's
                availability. However, if another alarm triggers a scale-out policy during the
                cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target
                immediately.

              - **EstimatedInstanceWarmup** *(integer) --*

                The estimated time, in seconds, until a newly launched instance can contribute to
                the CloudWatch metrics. This value is used only if the resource is an Auto Scaling
                group.

        - **ScalingStatusCode** *(string) --*

          The scaling status of the resource.

          * ``Active`` - The scaling configuration is active.

          * ``Inactive`` - The scaling configuration is not active because the scaling plan is
          being created or the scaling configuration could not be applied. Check the status message
          for more information.

          * ``PartiallyActive`` - The scaling configuration is partially active because the scaling
          plan is being created or deleted or the scaling configuration could not be fully applied.
          Check the status message for more information.

        - **ScalingStatusMessage** *(string) --*

          A simple message about the current scaling status of the resource.
    """


_DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef(
    _DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateApplicationSources` `TagFilters`

    Represents a tag.

    - **Key** *(string) --*

      The tag key.

    - **Values** *(list) --*

      The tag values (0 to 20).

      - *(string) --*
    """


_DescribeScalingPlansPaginateApplicationSourcesTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateApplicationSourcesTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[
            DescribeScalingPlansPaginateApplicationSourcesTagFiltersTypeDef
        ],
    },
    total=False,
)


class DescribeScalingPlansPaginateApplicationSourcesTypeDef(
    _DescribeScalingPlansPaginateApplicationSourcesTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginate` `ApplicationSources`

    Represents an application source.

    - **CloudFormationStackARN** *(string) --*

      The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

    - **TagFilters** *(list) --*

      A set of tags (up to 50).

      - *(dict) --*

        Represents a tag.

        - **Key** *(string) --*

          The tag key.

        - **Values** *(list) --*

          The tag values (0 to 20).

          - *(string) --*
    """


_DescribeScalingPlansPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalingPlansPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalingPlansPaginatePaginationConfigTypeDef(
    _DescribeScalingPlansPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginate` `PaginationConfig`

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


_DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponseScalingPlansApplicationSource` `TagFilters`

    Represents a tag.

    - **Key** *(string) --*

      The tag key.

    - **Values** *(list) --*

      The tag values (0 to 20).

      - *(string) --*
    """


_DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[
            DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTagFiltersTypeDef
        ],
    },
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponseScalingPlans` `ApplicationSource`

    The application source.

    - **CloudFormationStackARN** *(string) --*

      The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

    - **TagFilters** *(list) --*

      A set of tags (up to 50).

      - *(dict) --*

        Represents a tag.

        - **Key** *(string) --*

          The tag key.

        - **Values** *(list) --*

          The tag values (0 to 20).

          - *(string) --*
    """


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecification` `Dimensions`

    Represents a dimension for a customized metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value of the dimension.
    """


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponseScalingPlansScalingInstructions` `CustomizedLoadMetricSpecification`

    The customized load metric to use for predictive scaling. This parameter or a
    **PredefinedLoadMetricSpecification** is required when configuring predictive
    scaling, and cannot be used otherwise.

    - **MetricName** *(string) --*

      The name of the metric.

    - **Namespace** *(string) --*

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the
      same dimensions in your customized load metric specification.

      - *(dict) --*

        Represents a dimension for a customized metric.

        - **Name** *(string) --*

          The name of the dimension.

        - **Value** *(string) --*

          The value of the dimension.

    - **Statistic** *(string) --*

      The statistic of the metric. Currently, the value must always be ``Sum`` .

    - **Unit** *(string) --*

      The unit of the metric.
    """


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {"PredefinedLoadMetricType": str, "ResourceLabel": str},
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponseScalingPlansScalingInstructions` `PredefinedLoadMetricSpecification`

    The predefined load metric to use for predictive scaling. This parameter or a
    **CustomizedLoadMetricSpecification** is required when configuring predictive
    scaling, and cannot be used otherwise.

    - **PredefinedLoadMetricType** *(string) --*

      The metric type.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a
      resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is
      a target group for an Application Load Balancer attached to the Auto Scaling group.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
      balancer ARN.

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
      target group ARN.
    """


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecification` `Dimensions`

    Represents a dimension for a customized metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value of the dimension.
    """


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurations` `CustomizedScalingMetricSpecification`

    A customized metric. You can specify either a predefined metric or a customized
    metric.

    - **MetricName** *(string) --*

      The name of the metric.

    - **Namespace** *(string) --*

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the
      same dimensions in your customized scaling metric specification.

      - *(dict) --*

        Represents a dimension for a customized metric.

        - **Name** *(string) --*

          The name of the dimension.

        - **Value** *(string) --*

          The value of the dimension.

    - **Statistic** *(string) --*

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {"PredefinedScalingMetricType": str, "ResourceLabel": str},
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurations` `PredefinedScalingMetricSpecification`

    A predefined metric. You can specify either a predefined metric or a customized
    metric.

    - **PredefinedScalingMetricType** *(string) --*

      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
      Auto Scaling groups, Spot Fleet requests, and ECS services.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a
      resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
      is a target group for an Application Load Balancer attached to the Auto Scaling
      group, Spot Fleet request, or ECS service.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
      balancer ARN.

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
      target group ARN.
    """


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponseScalingPlansScalingInstructions` `TargetTrackingConfigurations`

    Describes a target tracking configuration to use with AWS Auto Scaling. Used with
    ScalingInstruction and  ScalingPolicy .

    - **PredefinedScalingMetricSpecification** *(dict) --*

      A predefined metric. You can specify either a predefined metric or a customized
      metric.

      - **PredefinedScalingMetricType** *(string) --*

        The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
        Auto Scaling groups, Spot Fleet requests, and ECS services.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a
        resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
        is a target group for an Application Load Balancer attached to the Auto Scaling
        group, Spot Fleet request, or ECS service.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
        balancer ARN.

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
        target group ARN.

    - **CustomizedScalingMetricSpecification** *(dict) --*

      A customized metric. You can specify either a predefined metric or a customized
      metric.

      - **MetricName** *(string) --*

        The name of the metric.

      - **Namespace** *(string) --*

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the
        same dimensions in your customized scaling metric specification.

        - *(dict) --*

          Represents a dimension for a customized metric.

          - **Name** *(string) --*

            The name of the dimension.

          - **Value** *(string) --*

            The value of the dimension.

      - **Statistic** *(string) --*

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **TargetValue** *(float) --*

      The target value for the metric. The range is 8.515920e-109 to 1.174271e+108
      (Base 10) or 2e-360 to 2e360 (Base 2).

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scale in by the target tracking scaling policy is disabled. If
      the value is ``true`` , scale in is disabled and the target tracking scaling
      policy doesn't remove capacity from the scalable resource. Otherwise, scale in is
      enabled and the target tracking scaling policy can remove capacity from the
      scalable resource.

      The default value is ``false`` .

    - **ScaleOutCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-out activity completes before
      another scale-out activity can start. This value is not used if the scalable
      resource is an Auto Scaling group.

      While the cooldown period is in effect, the capacity that has been added by the
      previous scale-out event that initiated the cooldown is calculated as part of the
      desired capacity for the next scale out. The intention is to continuously (but
      not excessively) scale out.

    - **ScaleInCooldown** *(integer) --*

      The amount of time, in seconds, after a scale in activity completes before
      another scale in activity can start. This value is not used if the scalable
      resource is an Auto Scaling group.

      The cooldown period is used to block subsequent scale in requests until it has
      expired. The intention is to scale in conservatively to protect your
      application's availability. However, if another alarm triggers a scale-out policy
      during the cooldown period after a scale-in, AWS Auto Scaling scales out your
      scalable target immediately.

    - **EstimatedInstanceWarmup** *(integer) --*

      The estimated time, in seconds, until a newly launched instance can contribute to
      the CloudWatch metrics. This value is used only if the resource is an Auto
      Scaling group.
    """


_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef",
    {
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
        "PredefinedLoadMetricSpecification": DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": str,
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": str,
        "ScalingPolicyUpdateBehavior": str,
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponseScalingPlans` `ScalingInstructions`

    Describes a scaling instruction for a scalable resource.

    The scaling instruction is used in combination with a scaling plan, which is a set of
    instructions for configuring dynamic scaling and predictive scaling for the scalable
    resources in your application. Each scaling instruction applies to one resource.

    AWS Auto Scaling creates target tracking scaling policies based on the scaling
    instructions. Target tracking scaling policies adjust the capacity of your scalable
    resource as required to maintain resource utilization at the target value that you
    specified.

    AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling
    groups using a subset of parameters, including the load metric, the scaling metric, the
    target value for the scaling metric, the predictive scaling mode (forecast and scale or
    forecast only), and the desired behavior when the forecast capacity exceeds the maximum
    capacity of the resource. With predictive scaling, AWS Auto Scaling generates forecasts
    with traffic predictions for the two days ahead and schedules scaling actions that
    proactively add and remove resource capacity to match the forecast.

    We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to
    configure predictive scaling. At minimum, there must be 24 hours of historical data to
    generate a forecast.

    For more information, see `Getting Started with AWS Auto Scaling
    <https://docs.aws.amazon.com/autoscaling/plans/userguide/auto-scaling-getting-started.html>`__
    .

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service.

    - **ResourceId** *(string) --*

      The ID of the resource. This string consists of the resource type and unique
      identifier.

      * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique
      identifier is the name of the Auto Scaling group. Example:
      ``autoScalingGroup/my-asg`` .

      * ECS service - The resource type is ``service`` and the unique identifier is the
      cluster name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is
      the cluster name. Example: ``cluster:my-db-cluster`` .

    - **ScalableDimension** *(string) --*

      The scalable dimension associated with the resource.

      * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto
      Scaling group.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet
      request.

      * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
      table.

      * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a
      DynamoDB table.

      * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
      global secondary index.

      * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a
      DynamoDB global secondary index.

      * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
      cluster. Available for Aurora MySQL-compatible edition and Aurora
      PostgreSQL-compatible edition.

    - **MinCapacity** *(integer) --*

      The minimum capacity of the resource.

    - **MaxCapacity** *(integer) --*

      The maximum capacity of the resource. The exception to this upper limit is if you
      specify a non-default setting for **PredictiveScalingMaxCapacityBehavior** .

    - **TargetTrackingConfigurations** *(list) --*

      The structure that defines new target tracking configurations (up to 10). Each of
      these structures includes a specific scaling metric and a target value for the
      metric, along with various parameters to use with dynamic scaling.

      With predictive scaling and dynamic scaling, the resource scales based on the target
      tracking configuration that provides the largest capacity for both scale in and scale
      out.

      Condition: The scaling metric must be unique across target tracking configurations.

      - *(dict) --*

        Describes a target tracking configuration to use with AWS Auto Scaling. Used with
        ScalingInstruction and  ScalingPolicy .

        - **PredefinedScalingMetricSpecification** *(dict) --*

          A predefined metric. You can specify either a predefined metric or a customized
          metric.

          - **PredefinedScalingMetricType** *(string) --*

            The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
            Auto Scaling groups, Spot Fleet requests, and ECS services.

          - **ResourceLabel** *(string) --*

            Identifies the resource associated with the metric type. You can't specify a
            resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
            is a target group for an Application Load Balancer attached to the Auto Scaling
            group, Spot Fleet request, or ECS service.

            The format is
            app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
            where:

            * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
            balancer ARN.

            * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
            target group ARN.

        - **CustomizedScalingMetricSpecification** *(dict) --*

          A customized metric. You can specify either a predefined metric or a customized
          metric.

          - **MetricName** *(string) --*

            The name of the metric.

          - **Namespace** *(string) --*

            The namespace of the metric.

          - **Dimensions** *(list) --*

            The dimensions of the metric.

            Conditional: If you published your metric with dimensions, you must specify the
            same dimensions in your customized scaling metric specification.

            - *(dict) --*

              Represents a dimension for a customized metric.

              - **Name** *(string) --*

                The name of the dimension.

              - **Value** *(string) --*

                The value of the dimension.

          - **Statistic** *(string) --*

            The statistic of the metric.

          - **Unit** *(string) --*

            The unit of the metric.

        - **TargetValue** *(float) --*

          The target value for the metric. The range is 8.515920e-109 to 1.174271e+108
          (Base 10) or 2e-360 to 2e360 (Base 2).

        - **DisableScaleIn** *(boolean) --*

          Indicates whether scale in by the target tracking scaling policy is disabled. If
          the value is ``true`` , scale in is disabled and the target tracking scaling
          policy doesn't remove capacity from the scalable resource. Otherwise, scale in is
          enabled and the target tracking scaling policy can remove capacity from the
          scalable resource.

          The default value is ``false`` .

        - **ScaleOutCooldown** *(integer) --*

          The amount of time, in seconds, after a scale-out activity completes before
          another scale-out activity can start. This value is not used if the scalable
          resource is an Auto Scaling group.

          While the cooldown period is in effect, the capacity that has been added by the
          previous scale-out event that initiated the cooldown is calculated as part of the
          desired capacity for the next scale out. The intention is to continuously (but
          not excessively) scale out.

        - **ScaleInCooldown** *(integer) --*

          The amount of time, in seconds, after a scale in activity completes before
          another scale in activity can start. This value is not used if the scalable
          resource is an Auto Scaling group.

          The cooldown period is used to block subsequent scale in requests until it has
          expired. The intention is to scale in conservatively to protect your
          application's availability. However, if another alarm triggers a scale-out policy
          during the cooldown period after a scale-in, AWS Auto Scaling scales out your
          scalable target immediately.

        - **EstimatedInstanceWarmup** *(integer) --*

          The estimated time, in seconds, until a newly launched instance can contribute to
          the CloudWatch metrics. This value is used only if the resource is an Auto
          Scaling group.

    - **PredefinedLoadMetricSpecification** *(dict) --*

      The predefined load metric to use for predictive scaling. This parameter or a
      **CustomizedLoadMetricSpecification** is required when configuring predictive
      scaling, and cannot be used otherwise.

      - **PredefinedLoadMetricType** *(string) --*

        The metric type.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a
        resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is
        a target group for an Application Load Balancer attached to the Auto Scaling group.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
        balancer ARN.

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
        target group ARN.

    - **CustomizedLoadMetricSpecification** *(dict) --*

      The customized load metric to use for predictive scaling. This parameter or a
      **PredefinedLoadMetricSpecification** is required when configuring predictive
      scaling, and cannot be used otherwise.

      - **MetricName** *(string) --*

        The name of the metric.

      - **Namespace** *(string) --*

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the
        same dimensions in your customized load metric specification.

        - *(dict) --*

          Represents a dimension for a customized metric.

          - **Name** *(string) --*

            The name of the dimension.

          - **Value** *(string) --*

            The value of the dimension.

      - **Statistic** *(string) --*

        The statistic of the metric. Currently, the value must always be ``Sum`` .

      - **Unit** *(string) --*

        The unit of the metric.

    - **ScheduledActionBufferTime** *(integer) --*

      The amount of time, in seconds, to buffer the run time of scheduled scaling actions
      when scaling out. For example, if the forecast says to add capacity at 10:00 AM, and
      the buffer time is 5 minutes, then the run time of the corresponding scheduled
      scaling action will be 9:55 AM. The intention is to give resources time to be
      provisioned. For example, it can take a few minutes to launch an EC2 instance. The
      actual amount of time required depends on several factors, such as the size of the
      instance and whether there are startup scripts to complete.

      The value must be less than the forecast interval duration of 3600 seconds (60
      minutes). The default is 300 seconds.

      Only valid when configuring predictive scaling.

    - **PredictiveScalingMaxCapacityBehavior** *(string) --*

      Defines the behavior that should be applied if the forecast capacity approaches or
      exceeds the maximum capacity specified for the resource. The default value is
      ``SetForecastCapacityToMaxCapacity`` .

      The following are possible values:

      * ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource
      capacity higher than the maximum capacity. The maximum capacity is enforced as a hard
      limit.

      * ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling may scale resource capacity
      higher than the maximum capacity to equal but not exceed forecast capacity.

      * ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling may scale resource
      capacity higher than the maximum capacity by a specified buffer value. The intention
      is to give the target tracking scaling policy extra capacity if unexpected traffic
      occurs.

      Only valid when configuring predictive scaling.

    - **PredictiveScalingMaxCapacityBuffer** *(integer) --*

      The size of the capacity buffer to use when the forecast capacity is close to or
      exceeds the maximum capacity. The value is specified as a percentage relative to the
      forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer,
      such that if the forecast capacity is 50, and the maximum capacity is 40, then the
      effective maximum capacity is 55.

      Only valid when configuring predictive scaling. Required if the
      **PredictiveScalingMaxCapacityBehavior** is set to
      ``SetMaxCapacityAboveForecastCapacity`` , and cannot be used otherwise.

      The range is 1-100.

    - **PredictiveScalingMode** *(string) --*

      The predictive scaling mode. The default value is ``ForecastAndScale`` . Otherwise,
      AWS Auto Scaling forecasts capacity but does not create any scheduled scaling actions
      based on the capacity forecast.

    - **ScalingPolicyUpdateBehavior** *(string) --*

      Controls whether a resource's externally created scaling policies are kept or
      replaced.

      The default value is ``KeepExternalPolicies`` . If the parameter is set to
      ``ReplaceExternalPolicies`` , any scaling policies that are external to AWS Auto
      Scaling are deleted and new target tracking scaling policies created.

      Only valid when configuring dynamic scaling.

      Condition: The number of existing policies to be replaced must be less than or equal
      to 50. If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all
      existing policies and does not create new ones.

    - **DisableDynamicScaling** *(boolean) --*

      Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic
      scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based
      on the specified target tracking configurations.

      The default is enabled (``false`` ).
    """


_DescribeScalingPlansPaginateResponseScalingPlansTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseScalingPlansTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": DescribeScalingPlansPaginateResponseScalingPlansApplicationSourceTypeDef,
        "ScalingInstructions": List[
            DescribeScalingPlansPaginateResponseScalingPlansScalingInstructionsTypeDef
        ],
        "StatusCode": str,
        "StatusMessage": str,
        "StatusStartTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)


class DescribeScalingPlansPaginateResponseScalingPlansTypeDef(
    _DescribeScalingPlansPaginateResponseScalingPlansTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginateResponse` `ScalingPlans`

    Represents a scaling plan.

    - **ScalingPlanName** *(string) --*

      The name of the scaling plan.

    - **ScalingPlanVersion** *(integer) --*

      The version number of the scaling plan.

    - **ApplicationSource** *(dict) --*

      The application source.

      - **CloudFormationStackARN** *(string) --*

        The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

      - **TagFilters** *(list) --*

        A set of tags (up to 50).

        - *(dict) --*

          Represents a tag.

          - **Key** *(string) --*

            The tag key.

          - **Values** *(list) --*

            The tag values (0 to 20).

            - *(string) --*

    - **ScalingInstructions** *(list) --*

      The scaling instructions.

      - *(dict) --*

        Describes a scaling instruction for a scalable resource.

        The scaling instruction is used in combination with a scaling plan, which is a set of
        instructions for configuring dynamic scaling and predictive scaling for the scalable
        resources in your application. Each scaling instruction applies to one resource.

        AWS Auto Scaling creates target tracking scaling policies based on the scaling
        instructions. Target tracking scaling policies adjust the capacity of your scalable
        resource as required to maintain resource utilization at the target value that you
        specified.

        AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling
        groups using a subset of parameters, including the load metric, the scaling metric, the
        target value for the scaling metric, the predictive scaling mode (forecast and scale or
        forecast only), and the desired behavior when the forecast capacity exceeds the maximum
        capacity of the resource. With predictive scaling, AWS Auto Scaling generates forecasts
        with traffic predictions for the two days ahead and schedules scaling actions that
        proactively add and remove resource capacity to match the forecast.

        We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to
        configure predictive scaling. At minimum, there must be 24 hours of historical data to
        generate a forecast.

        For more information, see `Getting Started with AWS Auto Scaling
        <https://docs.aws.amazon.com/autoscaling/plans/userguide/auto-scaling-getting-started.html>`__
        .

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service.

        - **ResourceId** *(string) --*

          The ID of the resource. This string consists of the resource type and unique
          identifier.

          * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique
          identifier is the name of the Auto Scaling group. Example:
          ``autoScalingGroup/my-asg`` .

          * ECS service - The resource type is ``service`` and the unique identifier is the
          cluster name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is
          the cluster name. Example: ``cluster:my-db-cluster`` .

        - **ScalableDimension** *(string) --*

          The scalable dimension associated with the resource.

          * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto
          Scaling group.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet
          request.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a
          DynamoDB table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a
          DynamoDB global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
          cluster. Available for Aurora MySQL-compatible edition and Aurora
          PostgreSQL-compatible edition.

        - **MinCapacity** *(integer) --*

          The minimum capacity of the resource.

        - **MaxCapacity** *(integer) --*

          The maximum capacity of the resource. The exception to this upper limit is if you
          specify a non-default setting for **PredictiveScalingMaxCapacityBehavior** .

        - **TargetTrackingConfigurations** *(list) --*

          The structure that defines new target tracking configurations (up to 10). Each of
          these structures includes a specific scaling metric and a target value for the
          metric, along with various parameters to use with dynamic scaling.

          With predictive scaling and dynamic scaling, the resource scales based on the target
          tracking configuration that provides the largest capacity for both scale in and scale
          out.

          Condition: The scaling metric must be unique across target tracking configurations.

          - *(dict) --*

            Describes a target tracking configuration to use with AWS Auto Scaling. Used with
            ScalingInstruction and  ScalingPolicy .

            - **PredefinedScalingMetricSpecification** *(dict) --*

              A predefined metric. You can specify either a predefined metric or a customized
              metric.

              - **PredefinedScalingMetricType** *(string) --*

                The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
                Auto Scaling groups, Spot Fleet requests, and ECS services.

              - **ResourceLabel** *(string) --*

                Identifies the resource associated with the metric type. You can't specify a
                resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
                is a target group for an Application Load Balancer attached to the Auto Scaling
                group, Spot Fleet request, or ECS service.

                The format is
                app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
                where:

                * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
                balancer ARN.

                * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
                target group ARN.

            - **CustomizedScalingMetricSpecification** *(dict) --*

              A customized metric. You can specify either a predefined metric or a customized
              metric.

              - **MetricName** *(string) --*

                The name of the metric.

              - **Namespace** *(string) --*

                The namespace of the metric.

              - **Dimensions** *(list) --*

                The dimensions of the metric.

                Conditional: If you published your metric with dimensions, you must specify the
                same dimensions in your customized scaling metric specification.

                - *(dict) --*

                  Represents a dimension for a customized metric.

                  - **Name** *(string) --*

                    The name of the dimension.

                  - **Value** *(string) --*

                    The value of the dimension.

              - **Statistic** *(string) --*

                The statistic of the metric.

              - **Unit** *(string) --*

                The unit of the metric.

            - **TargetValue** *(float) --*

              The target value for the metric. The range is 8.515920e-109 to 1.174271e+108
              (Base 10) or 2e-360 to 2e360 (Base 2).

            - **DisableScaleIn** *(boolean) --*

              Indicates whether scale in by the target tracking scaling policy is disabled. If
              the value is ``true`` , scale in is disabled and the target tracking scaling
              policy doesn't remove capacity from the scalable resource. Otherwise, scale in is
              enabled and the target tracking scaling policy can remove capacity from the
              scalable resource.

              The default value is ``false`` .

            - **ScaleOutCooldown** *(integer) --*

              The amount of time, in seconds, after a scale-out activity completes before
              another scale-out activity can start. This value is not used if the scalable
              resource is an Auto Scaling group.

              While the cooldown period is in effect, the capacity that has been added by the
              previous scale-out event that initiated the cooldown is calculated as part of the
              desired capacity for the next scale out. The intention is to continuously (but
              not excessively) scale out.

            - **ScaleInCooldown** *(integer) --*

              The amount of time, in seconds, after a scale in activity completes before
              another scale in activity can start. This value is not used if the scalable
              resource is an Auto Scaling group.

              The cooldown period is used to block subsequent scale in requests until it has
              expired. The intention is to scale in conservatively to protect your
              application's availability. However, if another alarm triggers a scale-out policy
              during the cooldown period after a scale-in, AWS Auto Scaling scales out your
              scalable target immediately.

            - **EstimatedInstanceWarmup** *(integer) --*

              The estimated time, in seconds, until a newly launched instance can contribute to
              the CloudWatch metrics. This value is used only if the resource is an Auto
              Scaling group.

        - **PredefinedLoadMetricSpecification** *(dict) --*

          The predefined load metric to use for predictive scaling. This parameter or a
          **CustomizedLoadMetricSpecification** is required when configuring predictive
          scaling, and cannot be used otherwise.

          - **PredefinedLoadMetricType** *(string) --*

            The metric type.

          - **ResourceLabel** *(string) --*

            Identifies the resource associated with the metric type. You can't specify a
            resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is
            a target group for an Application Load Balancer attached to the Auto Scaling group.

            The format is
            app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
            where:

            * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
            balancer ARN.

            * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
            target group ARN.

        - **CustomizedLoadMetricSpecification** *(dict) --*

          The customized load metric to use for predictive scaling. This parameter or a
          **PredefinedLoadMetricSpecification** is required when configuring predictive
          scaling, and cannot be used otherwise.

          - **MetricName** *(string) --*

            The name of the metric.

          - **Namespace** *(string) --*

            The namespace of the metric.

          - **Dimensions** *(list) --*

            The dimensions of the metric.

            Conditional: If you published your metric with dimensions, you must specify the
            same dimensions in your customized load metric specification.

            - *(dict) --*

              Represents a dimension for a customized metric.

              - **Name** *(string) --*

                The name of the dimension.

              - **Value** *(string) --*

                The value of the dimension.

          - **Statistic** *(string) --*

            The statistic of the metric. Currently, the value must always be ``Sum`` .

          - **Unit** *(string) --*

            The unit of the metric.

        - **ScheduledActionBufferTime** *(integer) --*

          The amount of time, in seconds, to buffer the run time of scheduled scaling actions
          when scaling out. For example, if the forecast says to add capacity at 10:00 AM, and
          the buffer time is 5 minutes, then the run time of the corresponding scheduled
          scaling action will be 9:55 AM. The intention is to give resources time to be
          provisioned. For example, it can take a few minutes to launch an EC2 instance. The
          actual amount of time required depends on several factors, such as the size of the
          instance and whether there are startup scripts to complete.

          The value must be less than the forecast interval duration of 3600 seconds (60
          minutes). The default is 300 seconds.

          Only valid when configuring predictive scaling.

        - **PredictiveScalingMaxCapacityBehavior** *(string) --*

          Defines the behavior that should be applied if the forecast capacity approaches or
          exceeds the maximum capacity specified for the resource. The default value is
          ``SetForecastCapacityToMaxCapacity`` .

          The following are possible values:

          * ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource
          capacity higher than the maximum capacity. The maximum capacity is enforced as a hard
          limit.

          * ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling may scale resource capacity
          higher than the maximum capacity to equal but not exceed forecast capacity.

          * ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling may scale resource
          capacity higher than the maximum capacity by a specified buffer value. The intention
          is to give the target tracking scaling policy extra capacity if unexpected traffic
          occurs.

          Only valid when configuring predictive scaling.

        - **PredictiveScalingMaxCapacityBuffer** *(integer) --*

          The size of the capacity buffer to use when the forecast capacity is close to or
          exceeds the maximum capacity. The value is specified as a percentage relative to the
          forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer,
          such that if the forecast capacity is 50, and the maximum capacity is 40, then the
          effective maximum capacity is 55.

          Only valid when configuring predictive scaling. Required if the
          **PredictiveScalingMaxCapacityBehavior** is set to
          ``SetMaxCapacityAboveForecastCapacity`` , and cannot be used otherwise.

          The range is 1-100.

        - **PredictiveScalingMode** *(string) --*

          The predictive scaling mode. The default value is ``ForecastAndScale`` . Otherwise,
          AWS Auto Scaling forecasts capacity but does not create any scheduled scaling actions
          based on the capacity forecast.

        - **ScalingPolicyUpdateBehavior** *(string) --*

          Controls whether a resource's externally created scaling policies are kept or
          replaced.

          The default value is ``KeepExternalPolicies`` . If the parameter is set to
          ``ReplaceExternalPolicies`` , any scaling policies that are external to AWS Auto
          Scaling are deleted and new target tracking scaling policies created.

          Only valid when configuring dynamic scaling.

          Condition: The number of existing policies to be replaced must be less than or equal
          to 50. If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all
          existing policies and does not create new ones.

        - **DisableDynamicScaling** *(boolean) --*

          Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic
          scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based
          on the specified target tracking configurations.

          The default is enabled (``false`` ).

    - **StatusCode** *(string) --*

      The status of the scaling plan.

      * ``Active`` - The scaling plan is active.

      * ``ActiveWithProblems`` - The scaling plan is active, but the scaling configuration for
      one or more resources could not be applied.

      * ``CreationInProgress`` - The scaling plan is being created.

      * ``CreationFailed`` - The scaling plan could not be created.

      * ``DeletionInProgress`` - The scaling plan is being deleted.

      * ``DeletionFailed`` - The scaling plan could not be deleted.

      * ``UpdateInProgress`` - The scaling plan is being updated.

      * ``UpdateFailed`` - The scaling plan could not be updated.

    - **StatusMessage** *(string) --*

      A simple message about the current status of the scaling plan.

    - **StatusStartTime** *(datetime) --*

      The Unix time stamp when the scaling plan entered the current status.

    - **CreationTime** *(datetime) --*

      The Unix time stamp when the scaling plan was created.
    """


_DescribeScalingPlansPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingPlansPaginateResponseTypeDef",
    {"ScalingPlans": List[DescribeScalingPlansPaginateResponseScalingPlansTypeDef]},
    total=False,
)


class DescribeScalingPlansPaginateResponseTypeDef(
    _DescribeScalingPlansPaginateResponseTypeDef
):
    """
    Type definition for `DescribeScalingPlansPaginate` `Response`

    - **ScalingPlans** *(list) --*

      Information about the scaling plans.

      - *(dict) --*

        Represents a scaling plan.

        - **ScalingPlanName** *(string) --*

          The name of the scaling plan.

        - **ScalingPlanVersion** *(integer) --*

          The version number of the scaling plan.

        - **ApplicationSource** *(dict) --*

          The application source.

          - **CloudFormationStackARN** *(string) --*

            The Amazon Resource Name (ARN) of a AWS CloudFormation stack.

          - **TagFilters** *(list) --*

            A set of tags (up to 50).

            - *(dict) --*

              Represents a tag.

              - **Key** *(string) --*

                The tag key.

              - **Values** *(list) --*

                The tag values (0 to 20).

                - *(string) --*

        - **ScalingInstructions** *(list) --*

          The scaling instructions.

          - *(dict) --*

            Describes a scaling instruction for a scalable resource.

            The scaling instruction is used in combination with a scaling plan, which is a set of
            instructions for configuring dynamic scaling and predictive scaling for the scalable
            resources in your application. Each scaling instruction applies to one resource.

            AWS Auto Scaling creates target tracking scaling policies based on the scaling
            instructions. Target tracking scaling policies adjust the capacity of your scalable
            resource as required to maintain resource utilization at the target value that you
            specified.

            AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling
            groups using a subset of parameters, including the load metric, the scaling metric, the
            target value for the scaling metric, the predictive scaling mode (forecast and scale or
            forecast only), and the desired behavior when the forecast capacity exceeds the maximum
            capacity of the resource. With predictive scaling, AWS Auto Scaling generates forecasts
            with traffic predictions for the two days ahead and schedules scaling actions that
            proactively add and remove resource capacity to match the forecast.

            We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to
            configure predictive scaling. At minimum, there must be 24 hours of historical data to
            generate a forecast.

            For more information, see `Getting Started with AWS Auto Scaling
            <https://docs.aws.amazon.com/autoscaling/plans/userguide/auto-scaling-getting-started.html>`__
            .

            - **ServiceNamespace** *(string) --*

              The namespace of the AWS service.

            - **ResourceId** *(string) --*

              The ID of the resource. This string consists of the resource type and unique
              identifier.

              * Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique
              identifier is the name of the Auto Scaling group. Example:
              ``autoScalingGroup/my-asg`` .

              * ECS service - The resource type is ``service`` and the unique identifier is the
              cluster name and service name. Example: ``service/default/sample-webapp`` .

              * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
              identifier is the Spot Fleet request ID. Example:
              ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

              * DynamoDB table - The resource type is ``table`` and the unique identifier is the
              resource ID. Example: ``table/my-table`` .

              * DynamoDB global secondary index - The resource type is ``index`` and the unique
              identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

              * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is
              the cluster name. Example: ``cluster:my-db-cluster`` .

            - **ScalableDimension** *(string) --*

              The scalable dimension associated with the resource.

              * ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto
              Scaling group.

              * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

              * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet
              request.

              * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
              table.

              * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a
              DynamoDB table.

              * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
              global secondary index.

              * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a
              DynamoDB global secondary index.

              * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
              cluster. Available for Aurora MySQL-compatible edition and Aurora
              PostgreSQL-compatible edition.

            - **MinCapacity** *(integer) --*

              The minimum capacity of the resource.

            - **MaxCapacity** *(integer) --*

              The maximum capacity of the resource. The exception to this upper limit is if you
              specify a non-default setting for **PredictiveScalingMaxCapacityBehavior** .

            - **TargetTrackingConfigurations** *(list) --*

              The structure that defines new target tracking configurations (up to 10). Each of
              these structures includes a specific scaling metric and a target value for the
              metric, along with various parameters to use with dynamic scaling.

              With predictive scaling and dynamic scaling, the resource scales based on the target
              tracking configuration that provides the largest capacity for both scale in and scale
              out.

              Condition: The scaling metric must be unique across target tracking configurations.

              - *(dict) --*

                Describes a target tracking configuration to use with AWS Auto Scaling. Used with
                ScalingInstruction and  ScalingPolicy .

                - **PredefinedScalingMetricSpecification** *(dict) --*

                  A predefined metric. You can specify either a predefined metric or a customized
                  metric.

                  - **PredefinedScalingMetricType** *(string) --*

                    The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
                    Auto Scaling groups, Spot Fleet requests, and ECS services.

                  - **ResourceLabel** *(string) --*

                    Identifies the resource associated with the metric type. You can't specify a
                    resource label unless the metric type is ``ALBRequestCountPerTarget`` and there
                    is a target group for an Application Load Balancer attached to the Auto Scaling
                    group, Spot Fleet request, or ECS service.

                    The format is
                    app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
                    where:

                    * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
                    balancer ARN.

                    * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
                    target group ARN.

                - **CustomizedScalingMetricSpecification** *(dict) --*

                  A customized metric. You can specify either a predefined metric or a customized
                  metric.

                  - **MetricName** *(string) --*

                    The name of the metric.

                  - **Namespace** *(string) --*

                    The namespace of the metric.

                  - **Dimensions** *(list) --*

                    The dimensions of the metric.

                    Conditional: If you published your metric with dimensions, you must specify the
                    same dimensions in your customized scaling metric specification.

                    - *(dict) --*

                      Represents a dimension for a customized metric.

                      - **Name** *(string) --*

                        The name of the dimension.

                      - **Value** *(string) --*

                        The value of the dimension.

                  - **Statistic** *(string) --*

                    The statistic of the metric.

                  - **Unit** *(string) --*

                    The unit of the metric.

                - **TargetValue** *(float) --*

                  The target value for the metric. The range is 8.515920e-109 to 1.174271e+108
                  (Base 10) or 2e-360 to 2e360 (Base 2).

                - **DisableScaleIn** *(boolean) --*

                  Indicates whether scale in by the target tracking scaling policy is disabled. If
                  the value is ``true`` , scale in is disabled and the target tracking scaling
                  policy doesn't remove capacity from the scalable resource. Otherwise, scale in is
                  enabled and the target tracking scaling policy can remove capacity from the
                  scalable resource.

                  The default value is ``false`` .

                - **ScaleOutCooldown** *(integer) --*

                  The amount of time, in seconds, after a scale-out activity completes before
                  another scale-out activity can start. This value is not used if the scalable
                  resource is an Auto Scaling group.

                  While the cooldown period is in effect, the capacity that has been added by the
                  previous scale-out event that initiated the cooldown is calculated as part of the
                  desired capacity for the next scale out. The intention is to continuously (but
                  not excessively) scale out.

                - **ScaleInCooldown** *(integer) --*

                  The amount of time, in seconds, after a scale in activity completes before
                  another scale in activity can start. This value is not used if the scalable
                  resource is an Auto Scaling group.

                  The cooldown period is used to block subsequent scale in requests until it has
                  expired. The intention is to scale in conservatively to protect your
                  application's availability. However, if another alarm triggers a scale-out policy
                  during the cooldown period after a scale-in, AWS Auto Scaling scales out your
                  scalable target immediately.

                - **EstimatedInstanceWarmup** *(integer) --*

                  The estimated time, in seconds, until a newly launched instance can contribute to
                  the CloudWatch metrics. This value is used only if the resource is an Auto
                  Scaling group.

            - **PredefinedLoadMetricSpecification** *(dict) --*

              The predefined load metric to use for predictive scaling. This parameter or a
              **CustomizedLoadMetricSpecification** is required when configuring predictive
              scaling, and cannot be used otherwise.

              - **PredefinedLoadMetricType** *(string) --*

                The metric type.

              - **ResourceLabel** *(string) --*

                Identifies the resource associated with the metric type. You can't specify a
                resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is
                a target group for an Application Load Balancer attached to the Auto Scaling group.

                The format is
                app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
                where:

                * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
                balancer ARN.

                * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
                target group ARN.

            - **CustomizedLoadMetricSpecification** *(dict) --*

              The customized load metric to use for predictive scaling. This parameter or a
              **PredefinedLoadMetricSpecification** is required when configuring predictive
              scaling, and cannot be used otherwise.

              - **MetricName** *(string) --*

                The name of the metric.

              - **Namespace** *(string) --*

                The namespace of the metric.

              - **Dimensions** *(list) --*

                The dimensions of the metric.

                Conditional: If you published your metric with dimensions, you must specify the
                same dimensions in your customized load metric specification.

                - *(dict) --*

                  Represents a dimension for a customized metric.

                  - **Name** *(string) --*

                    The name of the dimension.

                  - **Value** *(string) --*

                    The value of the dimension.

              - **Statistic** *(string) --*

                The statistic of the metric. Currently, the value must always be ``Sum`` .

              - **Unit** *(string) --*

                The unit of the metric.

            - **ScheduledActionBufferTime** *(integer) --*

              The amount of time, in seconds, to buffer the run time of scheduled scaling actions
              when scaling out. For example, if the forecast says to add capacity at 10:00 AM, and
              the buffer time is 5 minutes, then the run time of the corresponding scheduled
              scaling action will be 9:55 AM. The intention is to give resources time to be
              provisioned. For example, it can take a few minutes to launch an EC2 instance. The
              actual amount of time required depends on several factors, such as the size of the
              instance and whether there are startup scripts to complete.

              The value must be less than the forecast interval duration of 3600 seconds (60
              minutes). The default is 300 seconds.

              Only valid when configuring predictive scaling.

            - **PredictiveScalingMaxCapacityBehavior** *(string) --*

              Defines the behavior that should be applied if the forecast capacity approaches or
              exceeds the maximum capacity specified for the resource. The default value is
              ``SetForecastCapacityToMaxCapacity`` .

              The following are possible values:

              * ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource
              capacity higher than the maximum capacity. The maximum capacity is enforced as a hard
              limit.

              * ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling may scale resource capacity
              higher than the maximum capacity to equal but not exceed forecast capacity.

              * ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling may scale resource
              capacity higher than the maximum capacity by a specified buffer value. The intention
              is to give the target tracking scaling policy extra capacity if unexpected traffic
              occurs.

              Only valid when configuring predictive scaling.

            - **PredictiveScalingMaxCapacityBuffer** *(integer) --*

              The size of the capacity buffer to use when the forecast capacity is close to or
              exceeds the maximum capacity. The value is specified as a percentage relative to the
              forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer,
              such that if the forecast capacity is 50, and the maximum capacity is 40, then the
              effective maximum capacity is 55.

              Only valid when configuring predictive scaling. Required if the
              **PredictiveScalingMaxCapacityBehavior** is set to
              ``SetMaxCapacityAboveForecastCapacity`` , and cannot be used otherwise.

              The range is 1-100.

            - **PredictiveScalingMode** *(string) --*

              The predictive scaling mode. The default value is ``ForecastAndScale`` . Otherwise,
              AWS Auto Scaling forecasts capacity but does not create any scheduled scaling actions
              based on the capacity forecast.

            - **ScalingPolicyUpdateBehavior** *(string) --*

              Controls whether a resource's externally created scaling policies are kept or
              replaced.

              The default value is ``KeepExternalPolicies`` . If the parameter is set to
              ``ReplaceExternalPolicies`` , any scaling policies that are external to AWS Auto
              Scaling are deleted and new target tracking scaling policies created.

              Only valid when configuring dynamic scaling.

              Condition: The number of existing policies to be replaced must be less than or equal
              to 50. If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all
              existing policies and does not create new ones.

            - **DisableDynamicScaling** *(boolean) --*

              Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic
              scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based
              on the specified target tracking configurations.

              The default is enabled (``false`` ).

        - **StatusCode** *(string) --*

          The status of the scaling plan.

          * ``Active`` - The scaling plan is active.

          * ``ActiveWithProblems`` - The scaling plan is active, but the scaling configuration for
          one or more resources could not be applied.

          * ``CreationInProgress`` - The scaling plan is being created.

          * ``CreationFailed`` - The scaling plan could not be created.

          * ``DeletionInProgress`` - The scaling plan is being deleted.

          * ``DeletionFailed`` - The scaling plan could not be deleted.

          * ``UpdateInProgress`` - The scaling plan is being updated.

          * ``UpdateFailed`` - The scaling plan could not be updated.

        - **StatusMessage** *(string) --*

          A simple message about the current status of the scaling plan.

        - **StatusStartTime** *(datetime) --*

          The Unix time stamp when the scaling plan entered the current status.

        - **CreationTime** *(datetime) --*

          The Unix time stamp when the scaling plan was created.
    """
