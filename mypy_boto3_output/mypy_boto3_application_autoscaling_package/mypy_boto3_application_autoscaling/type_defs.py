"Main interface for application-autoscaling type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef",
    "ClientDescribeScalableTargetsResponseScalableTargetsTypeDef",
    "ClientDescribeScalableTargetsResponseTypeDef",
    "ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef",
    "ClientDescribeScalingActivitiesResponseTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
    "ClientDescribeScalingPoliciesResponseTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
    "ClientDescribeScheduledActionsResponseTypeDef",
    "ClientPutScalingPolicyResponseAlarmsTypeDef",
    "ClientPutScalingPolicyResponseTypeDef",
    "ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    "ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef",
    "ClientPutScheduledActionScalableTargetActionTypeDef",
    "ClientRegisterScalableTargetSuspendedStateTypeDef",
    "DescribeScalableTargetsPaginatePaginationConfigTypeDef",
    "DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef",
    "DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef",
    "DescribeScalableTargetsPaginateResponseTypeDef",
    "DescribeScalingActivitiesPaginatePaginationConfigTypeDef",
    "DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef",
    "DescribeScalingActivitiesPaginateResponseTypeDef",
    "DescribeScalingPoliciesPaginatePaginationConfigTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    "DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef",
    "DescribeScalingPoliciesPaginateResponseTypeDef",
    "DescribeScheduledActionsPaginatePaginationConfigTypeDef",
    "DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef",
    "DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef",
    "DescribeScheduledActionsPaginateResponseTypeDef",
)


_ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef = TypedDict(
    "_ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)


class ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef(
    _ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef
):
    """
    Type definition for `ClientDescribeScalableTargetsResponseScalableTargets` `SuspendedState`

    Specifies whether the scaling activities for a scalable target are in a suspended state.

    - **DynamicScalingInSuspended** *(boolean) --*

      Whether scale in by a target tracking scaling policy or a step scaling policy is
      suspended. Set the value to ``true`` if you don't want Application Auto Scaling to
      remove capacity when a scaling policy is triggered. The default is ``false`` .

    - **DynamicScalingOutSuspended** *(boolean) --*

      Whether scale out by a target tracking scaling policy or a step scaling policy is
      suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add
      capacity when a scaling policy is triggered. The default is ``false`` .

    - **ScheduledScalingSuspended** *(boolean) --*

      Whether scheduled scaling is suspended. Set the value to ``true`` if you don't want
      Application Auto Scaling to add or remove capacity by initiating scheduled actions. The
      default is ``false`` .
    """


_ClientDescribeScalableTargetsResponseScalableTargetsTypeDef = TypedDict(
    "_ClientDescribeScalableTargetsResponseScalableTargetsTypeDef",
    {
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
        "SuspendedState": ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef,
    },
    total=False,
)


class ClientDescribeScalableTargetsResponseScalableTargetsTypeDef(
    _ClientDescribeScalableTargetsResponseScalableTargetsTypeDef
):
    """
    Type definition for `ClientDescribeScalableTargetsResponse` `ScalableTargets`

    Represents a scalable target.

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service that provides the resource or ``custom-resource`` for a
      resource provided by your own application or service. For more information, see `AWS
      Service Namespaces
      <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *Amazon Web Services General Reference* .

    - **ResourceId** *(string) --*

      The identifier of the resource associated with the scalable target. This string consists
      of the resource type and unique identifier.

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
      cluster ID and instance group ID. Example:
      ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

      * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
      fleet name. Example: ``fleet/sample-fleet`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

      * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
      identifier is the resource ID. Example:
      ``endpoint/my-end-point/variant/KMeansClustering`` .

      * Custom resources are not supported with a resource type. This parameter must specify
      the ``OutputValue`` from the CloudFormation template stack used to access the resources.
      The unique identifier is defined by the service provider. More information is available
      in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

    - **ScalableDimension** *(string) --*

      The scalable dimension associated with the scalable target. This string consists of the
      service namespace, resource type, and scaling property.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
      Instance Group.

      * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

      * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
      SageMaker model endpoint variant.

      * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
      resource provided by your own application or service.

    - **MinCapacity** *(integer) --*

      The minimum value to scale to in response to a scale-in event.

    - **MaxCapacity** *(integer) --*

      The maximum value to scale to in response to a scale-out event.

    - **RoleARN** *(string) --*

      The ARN of an IAM role that allows Application Auto Scaling to modify the scalable target
      on your behalf.

    - **CreationTime** *(datetime) --*

      The Unix timestamp for when the scalable target was created.

    - **SuspendedState** *(dict) --*

      Specifies whether the scaling activities for a scalable target are in a suspended state.

      - **DynamicScalingInSuspended** *(boolean) --*

        Whether scale in by a target tracking scaling policy or a step scaling policy is
        suspended. Set the value to ``true`` if you don't want Application Auto Scaling to
        remove capacity when a scaling policy is triggered. The default is ``false`` .

      - **DynamicScalingOutSuspended** *(boolean) --*

        Whether scale out by a target tracking scaling policy or a step scaling policy is
        suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add
        capacity when a scaling policy is triggered. The default is ``false`` .

      - **ScheduledScalingSuspended** *(boolean) --*

        Whether scheduled scaling is suspended. Set the value to ``true`` if you don't want
        Application Auto Scaling to add or remove capacity by initiating scheduled actions. The
        default is ``false`` .
    """


_ClientDescribeScalableTargetsResponseTypeDef = TypedDict(
    "_ClientDescribeScalableTargetsResponseTypeDef",
    {
        "ScalableTargets": List[
            ClientDescribeScalableTargetsResponseScalableTargetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalableTargetsResponseTypeDef(
    _ClientDescribeScalableTargetsResponseTypeDef
):
    """
    Type definition for `ClientDescribeScalableTargets` `Response`

    - **ScalableTargets** *(list) --*

      The scalable targets that match the request parameters.

      - *(dict) --*

        Represents a scalable target.

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        - **ResourceId** *(string) --*

          The identifier of the resource associated with the scalable target. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example:
          ``endpoint/my-end-point/variant/KMeansClustering`` .

          * Custom resources are not supported with a resource type. This parameter must specify
          the ``OutputValue`` from the CloudFormation template stack used to access the resources.
          The unique identifier is defined by the service provider. More information is available
          in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

        - **ScalableDimension** *(string) --*

          The scalable dimension associated with the scalable target. This string consists of the
          service namespace, resource type, and scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
          Instance Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
          resource provided by your own application or service.

        - **MinCapacity** *(integer) --*

          The minimum value to scale to in response to a scale-in event.

        - **MaxCapacity** *(integer) --*

          The maximum value to scale to in response to a scale-out event.

        - **RoleARN** *(string) --*

          The ARN of an IAM role that allows Application Auto Scaling to modify the scalable target
          on your behalf.

        - **CreationTime** *(datetime) --*

          The Unix timestamp for when the scalable target was created.

        - **SuspendedState** *(dict) --*

          Specifies whether the scaling activities for a scalable target are in a suspended state.

          - **DynamicScalingInSuspended** *(boolean) --*

            Whether scale in by a target tracking scaling policy or a step scaling policy is
            suspended. Set the value to ``true`` if you don't want Application Auto Scaling to
            remove capacity when a scaling policy is triggered. The default is ``false`` .

          - **DynamicScalingOutSuspended** *(boolean) --*

            Whether scale out by a target tracking scaling policy or a step scaling policy is
            suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add
            capacity when a scaling policy is triggered. The default is ``false`` .

          - **ScheduledScalingSuspended** *(boolean) --*

            Whether scheduled scaling is suspended. Set the value to ``true`` if you don't want
            Application Auto Scaling to add or remove capacity by initiating scheduled actions. The
            default is ``false`` .

    - **NextToken** *(string) --*

      The token required to get the next set of results. This value is ``null`` if there are no
      more results to return.
    """


_ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef = TypedDict(
    "_ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": str,
        "StatusMessage": str,
        "Details": str,
    },
    total=False,
)


class ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef(
    _ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef
):
    """
    Type definition for `ClientDescribeScalingActivitiesResponse` `ScalingActivities`

    Represents a scaling activity.

    - **ActivityId** *(string) --*

      The unique identifier of the scaling activity.

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service that provides the resource or ``custom-resource`` for a
      resource provided by your own application or service. For more information, see `AWS
      Service Namespaces
      <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *Amazon Web Services General Reference* .

    - **ResourceId** *(string) --*

      The identifier of the resource associated with the scaling activity. This string consists
      of the resource type and unique identifier.

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
      cluster ID and instance group ID. Example:
      ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

      * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
      fleet name. Example: ``fleet/sample-fleet`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

      * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
      identifier is the resource ID. Example:
      ``endpoint/my-end-point/variant/KMeansClustering`` .

      * Custom resources are not supported with a resource type. This parameter must specify
      the ``OutputValue`` from the CloudFormation template stack used to access the resources.
      The unique identifier is defined by the service provider. More information is available
      in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

    - **ScalableDimension** *(string) --*

      The scalable dimension. This string consists of the service namespace, resource type, and
      scaling property.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
      Instance Group.

      * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

      * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
      SageMaker model endpoint variant.

      * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
      resource provided by your own application or service.

    - **Description** *(string) --*

      A simple description of what action the scaling activity intends to accomplish.

    - **Cause** *(string) --*

      A simple description of what caused the scaling activity to happen.

    - **StartTime** *(datetime) --*

      The Unix timestamp for when the scaling activity began.

    - **EndTime** *(datetime) --*

      The Unix timestamp for when the scaling activity ended.

    - **StatusCode** *(string) --*

      Indicates the status of the scaling activity.

    - **StatusMessage** *(string) --*

      A simple message about the current status of the scaling activity.

    - **Details** *(string) --*

      The details about the scaling activity.
    """


_ClientDescribeScalingActivitiesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingActivitiesResponseTypeDef",
    {
        "ScalingActivities": List[
            ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingActivitiesResponseTypeDef(
    _ClientDescribeScalingActivitiesResponseTypeDef
):
    """
    Type definition for `ClientDescribeScalingActivities` `Response`

    - **ScalingActivities** *(list) --*

      A list of scaling activity objects.

      - *(dict) --*

        Represents a scaling activity.

        - **ActivityId** *(string) --*

          The unique identifier of the scaling activity.

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        - **ResourceId** *(string) --*

          The identifier of the resource associated with the scaling activity. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example:
          ``endpoint/my-end-point/variant/KMeansClustering`` .

          * Custom resources are not supported with a resource type. This parameter must specify
          the ``OutputValue`` from the CloudFormation template stack used to access the resources.
          The unique identifier is defined by the service provider. More information is available
          in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

        - **ScalableDimension** *(string) --*

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
          Instance Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
          resource provided by your own application or service.

        - **Description** *(string) --*

          A simple description of what action the scaling activity intends to accomplish.

        - **Cause** *(string) --*

          A simple description of what caused the scaling activity to happen.

        - **StartTime** *(datetime) --*

          The Unix timestamp for when the scaling activity began.

        - **EndTime** *(datetime) --*

          The Unix timestamp for when the scaling activity ended.

        - **StatusCode** *(string) --*

          Indicates the status of the scaling activity.

        - **StatusMessage** *(string) --*

          A simple message about the current status of the scaling activity.

        - **Details** *(string) --*

          The details about the scaling activity.

    - **NextToken** *(string) --*

      The token required to get the next set of results. This value is ``null`` if there are no
      more results to return.
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef
):
    """
    Type definition for `ClientDescribeScalingPoliciesResponseScalingPolicies` `Alarms`

    Represents a CloudWatch alarm associated with a scaling policy.

    - **AlarmName** *(string) --*

      The name of the alarm.

    - **AlarmARN** *(string) --*

      The Amazon Resource Name (ARN) of the alarm.
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef
):
    """
    Type definition for `ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfiguration` `StepAdjustments`

    Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an
    adjustment based on the difference between the value of the aggregated CloudWatch
    metric and the breach threshold that you've defined for the alarm.

    For the following examples, suppose that you have an alarm with a breach threshold of
    50:

    * To trigger the adjustment when the metric is greater than or equal to 50 and less
    than 60, specify a lower bound of 0 and an upper bound of 10.

    * To trigger the adjustment when the metric is greater than 40 and less than or equal
    to 50, specify a lower bound of -10 and an upper bound of 0.

    There are a few rules for the step adjustments for your step policy:

    * The ranges of your step adjustments can't overlap or have a gap.

    * At most one step adjustment can have a null lower bound. If one step adjustment has
    a negative lower bound, then there must be a step adjustment with a null lower bound.

    * At most one step adjustment can have a null upper bound. If one step adjustment has
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
      value adds to the current scalable dimension while a negative number removes from
      the current scalable dimension.
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": str,
        "StepAdjustments": List[
            ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef
        ],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": str,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPoliciesResponseScalingPolicies` `StepScalingPolicyConfiguration`

    A step scaling policy.

    - **AdjustmentType** *(string) --*

      Specifies whether the ``ScalingAdjustment`` value in a  StepAdjustment is an absolute
      number or a percentage of the current capacity.

    - **StepAdjustments** *(list) --*

      A set of adjustments that enable you to scale based on the size of the alarm breach.

      - *(dict) --*

        Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an
        adjustment based on the difference between the value of the aggregated CloudWatch
        metric and the breach threshold that you've defined for the alarm.

        For the following examples, suppose that you have an alarm with a breach threshold of
        50:

        * To trigger the adjustment when the metric is greater than or equal to 50 and less
        than 60, specify a lower bound of 0 and an upper bound of 10.

        * To trigger the adjustment when the metric is greater than 40 and less than or equal
        to 50, specify a lower bound of -10 and an upper bound of 0.

        There are a few rules for the step adjustments for your step policy:

        * The ranges of your step adjustments can't overlap or have a gap.

        * At most one step adjustment can have a null lower bound. If one step adjustment has
        a negative lower bound, then there must be a step adjustment with a null lower bound.

        * At most one step adjustment can have a null upper bound. If one step adjustment has
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
          value adds to the current scalable dimension while a negative number removes from
          the current scalable dimension.

    - **MinAdjustmentMagnitude** *(integer) --*

      The minimum number to adjust your scalable dimension as a result of a scaling activity.
      If the adjustment type is ``PercentChangeInCapacity`` , the scaling policy changes the
      scalable dimension of the scalable target by this amount.

      For example, suppose that you create a step scaling policy to scale out an Amazon ECS
      service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service
      has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because
      you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out
      the service by 2 tasks.

    - **Cooldown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes where previous
      trigger-related scaling activities can influence future scaling events.

      For scale-out policies, while the cooldown period is in effect, the capacity that has
      been added by the previous scale-out event that initiated the cooldown is calculated as
      part of the desired capacity for the next scale out. The intention is to continuously
      (but not excessively) scale out. For example, an alarm triggers a step scaling policy
      to scale out an Amazon ECS service by 2 tasks, the scaling activity completes
      successfully, and a cooldown period of 5 minutes starts. During the cooldown period, if
      the alarm triggers the same policy again but at a more aggressive step adjustment to
      scale out the service by 3 tasks, the 2 tasks that were added in the previous scale-out
      event are considered part of that capacity and only 1 additional task is added to the
      desired count.

      For scale-in policies, the cooldown period is used to block subsequent scale-in
      requests until it has expired. The intention is to scale in conservatively to protect
      your application's availability. However, if another alarm triggers a scale-out policy
      during the cooldown period after a scale-in, Application Auto Scaling scales out your
      scalable target immediately.

    - **MetricAggregationType** *(string) --*

      The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` ,
      ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated
      as ``Average`` .
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification` `Dimensions`

    Describes the dimension names and values associated with a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value of the dimension.
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfiguration` `CustomizedMetricSpecification`

    A customized metric. You can specify either a predefined metric or a customized metric.

    - **MetricName** *(string) --*

      The name of the metric.

    - **Namespace** *(string) --*

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the same
      dimensions in your scaling policy.

      - *(dict) --*

        Describes the dimension names and values associated with a metric.

        - **Name** *(string) --*

          The name of the dimension.

        - **Value** *(string) --*

          The value of the dimension.

    - **Statistic** *(string) --*

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    {"PredefinedMetricType": str, "ResourceLabel": str},
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfiguration` `PredefinedMetricSpecification`

    A predefined metric. You can specify either a predefined metric or a customized metric.

    - **PredefinedMetricType** *(string) --*

      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot
      Fleet requests and ECS services.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a resource
      label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
      group attached to the Spot Fleet request or ECS service.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
      balancer ARN

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
      target group ARN.
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeScalingPoliciesResponseScalingPolicies` `TargetTrackingScalingPolicyConfiguration`

    A target tracking scaling policy.

    - **TargetValue** *(float) --*

      The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10)
      or 2e-360 to 2e360 (Base 2).

    - **PredefinedMetricSpecification** *(dict) --*

      A predefined metric. You can specify either a predefined metric or a customized metric.

      - **PredefinedMetricType** *(string) --*

        The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot
        Fleet requests and ECS services.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a resource
        label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
        group attached to the Spot Fleet request or ECS service.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
        balancer ARN

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
        target group ARN.

    - **CustomizedMetricSpecification** *(dict) --*

      A customized metric. You can specify either a predefined metric or a customized metric.

      - **MetricName** *(string) --*

        The name of the metric.

      - **Namespace** *(string) --*

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the same
        dimensions in your scaling policy.

        - *(dict) --*

          Describes the dimension names and values associated with a metric.

          - **Name** *(string) --*

            The name of the dimension.

          - **Value** *(string) --*

            The value of the dimension.

      - **Statistic** *(string) --*

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **ScaleOutCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-out activity completes before another
      scale-out activity can start.

      While the cooldown period is in effect, the capacity that has been added by the
      previous scale-out event that initiated the cooldown is calculated as part of the
      desired capacity for the next scale out. The intention is to continuously (but not
      excessively) scale out.

    - **ScaleInCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-in activity completes before another
      scale in activity can start.

      The cooldown period is used to block subsequent scale-in requests until it has expired.
      The intention is to scale in conservatively to protect your application's availability.
      However, if another alarm triggers a scale-out policy during the cooldown period after
      a scale-in, Application Auto Scaling scales out your scalable target immediately.

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scale in by the target tracking scaling policy is disabled. If the
      value is ``true`` , scale in is disabled and the target tracking scaling policy won't
      remove capacity from the scalable resource. Otherwise, scale in is enabled and the
      target tracking scaling policy can remove capacity from the scalable resource. The
      default value is ``false`` .
    """


_ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "PolicyType": str,
        "StepScalingPolicyConfiguration": ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
        "Alarms": List[
            ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef
        ],
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef(
    _ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeScalingPoliciesResponse` `ScalingPolicies`

    Represents a scaling policy to use with Application Auto Scaling.

    - **PolicyARN** *(string) --*

      The Amazon Resource Name (ARN) of the scaling policy.

    - **PolicyName** *(string) --*

      The name of the scaling policy.

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service that provides the resource or ``custom-resource`` for a
      resource provided by your own application or service. For more information, see `AWS
      Service Namespaces
      <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *Amazon Web Services General Reference* .

    - **ResourceId** *(string) --*

      The identifier of the resource associated with the scaling policy. This string consists
      of the resource type and unique identifier.

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
      cluster ID and instance group ID. Example:
      ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

      * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
      fleet name. Example: ``fleet/sample-fleet`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

      * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
      identifier is the resource ID. Example:
      ``endpoint/my-end-point/variant/KMeansClustering`` .

      * Custom resources are not supported with a resource type. This parameter must specify
      the ``OutputValue`` from the CloudFormation template stack used to access the resources.
      The unique identifier is defined by the service provider. More information is available
      in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

    - **ScalableDimension** *(string) --*

      The scalable dimension. This string consists of the service namespace, resource type, and
      scaling property.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
      Instance Group.

      * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

      * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
      SageMaker model endpoint variant.

      * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
      resource provided by your own application or service.

    - **PolicyType** *(string) --*

      The scaling policy type.

    - **StepScalingPolicyConfiguration** *(dict) --*

      A step scaling policy.

      - **AdjustmentType** *(string) --*

        Specifies whether the ``ScalingAdjustment`` value in a  StepAdjustment is an absolute
        number or a percentage of the current capacity.

      - **StepAdjustments** *(list) --*

        A set of adjustments that enable you to scale based on the size of the alarm breach.

        - *(dict) --*

          Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an
          adjustment based on the difference between the value of the aggregated CloudWatch
          metric and the breach threshold that you've defined for the alarm.

          For the following examples, suppose that you have an alarm with a breach threshold of
          50:

          * To trigger the adjustment when the metric is greater than or equal to 50 and less
          than 60, specify a lower bound of 0 and an upper bound of 10.

          * To trigger the adjustment when the metric is greater than 40 and less than or equal
          to 50, specify a lower bound of -10 and an upper bound of 0.

          There are a few rules for the step adjustments for your step policy:

          * The ranges of your step adjustments can't overlap or have a gap.

          * At most one step adjustment can have a null lower bound. If one step adjustment has
          a negative lower bound, then there must be a step adjustment with a null lower bound.

          * At most one step adjustment can have a null upper bound. If one step adjustment has
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
            value adds to the current scalable dimension while a negative number removes from
            the current scalable dimension.

      - **MinAdjustmentMagnitude** *(integer) --*

        The minimum number to adjust your scalable dimension as a result of a scaling activity.
        If the adjustment type is ``PercentChangeInCapacity`` , the scaling policy changes the
        scalable dimension of the scalable target by this amount.

        For example, suppose that you create a step scaling policy to scale out an Amazon ECS
        service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service
        has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because
        you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out
        the service by 2 tasks.

      - **Cooldown** *(integer) --*

        The amount of time, in seconds, after a scaling activity completes where previous
        trigger-related scaling activities can influence future scaling events.

        For scale-out policies, while the cooldown period is in effect, the capacity that has
        been added by the previous scale-out event that initiated the cooldown is calculated as
        part of the desired capacity for the next scale out. The intention is to continuously
        (but not excessively) scale out. For example, an alarm triggers a step scaling policy
        to scale out an Amazon ECS service by 2 tasks, the scaling activity completes
        successfully, and a cooldown period of 5 minutes starts. During the cooldown period, if
        the alarm triggers the same policy again but at a more aggressive step adjustment to
        scale out the service by 3 tasks, the 2 tasks that were added in the previous scale-out
        event are considered part of that capacity and only 1 additional task is added to the
        desired count.

        For scale-in policies, the cooldown period is used to block subsequent scale-in
        requests until it has expired. The intention is to scale in conservatively to protect
        your application's availability. However, if another alarm triggers a scale-out policy
        during the cooldown period after a scale-in, Application Auto Scaling scales out your
        scalable target immediately.

      - **MetricAggregationType** *(string) --*

        The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` ,
        ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated
        as ``Average`` .

    - **TargetTrackingScalingPolicyConfiguration** *(dict) --*

      A target tracking scaling policy.

      - **TargetValue** *(float) --*

        The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10)
        or 2e-360 to 2e360 (Base 2).

      - **PredefinedMetricSpecification** *(dict) --*

        A predefined metric. You can specify either a predefined metric or a customized metric.

        - **PredefinedMetricType** *(string) --*

          The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot
          Fleet requests and ECS services.

        - **ResourceLabel** *(string) --*

          Identifies the resource associated with the metric type. You can't specify a resource
          label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
          group attached to the Spot Fleet request or ECS service.

          The format is
          app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
          where:

          * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
          balancer ARN

          * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
          target group ARN.

      - **CustomizedMetricSpecification** *(dict) --*

        A customized metric. You can specify either a predefined metric or a customized metric.

        - **MetricName** *(string) --*

          The name of the metric.

        - **Namespace** *(string) --*

          The namespace of the metric.

        - **Dimensions** *(list) --*

          The dimensions of the metric.

          Conditional: If you published your metric with dimensions, you must specify the same
          dimensions in your scaling policy.

          - *(dict) --*

            Describes the dimension names and values associated with a metric.

            - **Name** *(string) --*

              The name of the dimension.

            - **Value** *(string) --*

              The value of the dimension.

        - **Statistic** *(string) --*

          The statistic of the metric.

        - **Unit** *(string) --*

          The unit of the metric.

      - **ScaleOutCooldown** *(integer) --*

        The amount of time, in seconds, after a scale-out activity completes before another
        scale-out activity can start.

        While the cooldown period is in effect, the capacity that has been added by the
        previous scale-out event that initiated the cooldown is calculated as part of the
        desired capacity for the next scale out. The intention is to continuously (but not
        excessively) scale out.

      - **ScaleInCooldown** *(integer) --*

        The amount of time, in seconds, after a scale-in activity completes before another
        scale in activity can start.

        The cooldown period is used to block subsequent scale-in requests until it has expired.
        The intention is to scale in conservatively to protect your application's availability.
        However, if another alarm triggers a scale-out policy during the cooldown period after
        a scale-in, Application Auto Scaling scales out your scalable target immediately.

      - **DisableScaleIn** *(boolean) --*

        Indicates whether scale in by the target tracking scaling policy is disabled. If the
        value is ``true`` , scale in is disabled and the target tracking scaling policy won't
        remove capacity from the scalable resource. Otherwise, scale in is enabled and the
        target tracking scaling policy can remove capacity from the scalable resource. The
        default value is ``false`` .

    - **Alarms** *(list) --*

      The CloudWatch alarms associated with the scaling policy.

      - *(dict) --*

        Represents a CloudWatch alarm associated with a scaling policy.

        - **AlarmName** *(string) --*

          The name of the alarm.

        - **AlarmARN** *(string) --*

          The Amazon Resource Name (ARN) of the alarm.

    - **CreationTime** *(datetime) --*

      The Unix timestamp for when the scaling policy was created.
    """


_ClientDescribeScalingPoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[
            ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeScalingPoliciesResponseTypeDef(
    _ClientDescribeScalingPoliciesResponseTypeDef
):
    """
    Type definition for `ClientDescribeScalingPolicies` `Response`

    - **ScalingPolicies** *(list) --*

      Information about the scaling policies.

      - *(dict) --*

        Represents a scaling policy to use with Application Auto Scaling.

        - **PolicyARN** *(string) --*

          The Amazon Resource Name (ARN) of the scaling policy.

        - **PolicyName** *(string) --*

          The name of the scaling policy.

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        - **ResourceId** *(string) --*

          The identifier of the resource associated with the scaling policy. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example:
          ``endpoint/my-end-point/variant/KMeansClustering`` .

          * Custom resources are not supported with a resource type. This parameter must specify
          the ``OutputValue`` from the CloudFormation template stack used to access the resources.
          The unique identifier is defined by the service provider. More information is available
          in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

        - **ScalableDimension** *(string) --*

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
          Instance Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
          resource provided by your own application or service.

        - **PolicyType** *(string) --*

          The scaling policy type.

        - **StepScalingPolicyConfiguration** *(dict) --*

          A step scaling policy.

          - **AdjustmentType** *(string) --*

            Specifies whether the ``ScalingAdjustment`` value in a  StepAdjustment is an absolute
            number or a percentage of the current capacity.

          - **StepAdjustments** *(list) --*

            A set of adjustments that enable you to scale based on the size of the alarm breach.

            - *(dict) --*

              Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an
              adjustment based on the difference between the value of the aggregated CloudWatch
              metric and the breach threshold that you've defined for the alarm.

              For the following examples, suppose that you have an alarm with a breach threshold of
              50:

              * To trigger the adjustment when the metric is greater than or equal to 50 and less
              than 60, specify a lower bound of 0 and an upper bound of 10.

              * To trigger the adjustment when the metric is greater than 40 and less than or equal
              to 50, specify a lower bound of -10 and an upper bound of 0.

              There are a few rules for the step adjustments for your step policy:

              * The ranges of your step adjustments can't overlap or have a gap.

              * At most one step adjustment can have a null lower bound. If one step adjustment has
              a negative lower bound, then there must be a step adjustment with a null lower bound.

              * At most one step adjustment can have a null upper bound. If one step adjustment has
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
                value adds to the current scalable dimension while a negative number removes from
                the current scalable dimension.

          - **MinAdjustmentMagnitude** *(integer) --*

            The minimum number to adjust your scalable dimension as a result of a scaling activity.
            If the adjustment type is ``PercentChangeInCapacity`` , the scaling policy changes the
            scalable dimension of the scalable target by this amount.

            For example, suppose that you create a step scaling policy to scale out an Amazon ECS
            service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service
            has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because
            you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out
            the service by 2 tasks.

          - **Cooldown** *(integer) --*

            The amount of time, in seconds, after a scaling activity completes where previous
            trigger-related scaling activities can influence future scaling events.

            For scale-out policies, while the cooldown period is in effect, the capacity that has
            been added by the previous scale-out event that initiated the cooldown is calculated as
            part of the desired capacity for the next scale out. The intention is to continuously
            (but not excessively) scale out. For example, an alarm triggers a step scaling policy
            to scale out an Amazon ECS service by 2 tasks, the scaling activity completes
            successfully, and a cooldown period of 5 minutes starts. During the cooldown period, if
            the alarm triggers the same policy again but at a more aggressive step adjustment to
            scale out the service by 3 tasks, the 2 tasks that were added in the previous scale-out
            event are considered part of that capacity and only 1 additional task is added to the
            desired count.

            For scale-in policies, the cooldown period is used to block subsequent scale-in
            requests until it has expired. The intention is to scale in conservatively to protect
            your application's availability. However, if another alarm triggers a scale-out policy
            during the cooldown period after a scale-in, Application Auto Scaling scales out your
            scalable target immediately.

          - **MetricAggregationType** *(string) --*

            The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` ,
            ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated
            as ``Average`` .

        - **TargetTrackingScalingPolicyConfiguration** *(dict) --*

          A target tracking scaling policy.

          - **TargetValue** *(float) --*

            The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10)
            or 2e-360 to 2e360 (Base 2).

          - **PredefinedMetricSpecification** *(dict) --*

            A predefined metric. You can specify either a predefined metric or a customized metric.

            - **PredefinedMetricType** *(string) --*

              The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot
              Fleet requests and ECS services.

            - **ResourceLabel** *(string) --*

              Identifies the resource associated with the metric type. You can't specify a resource
              label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
              group attached to the Spot Fleet request or ECS service.

              The format is
              app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
              where:

              * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
              balancer ARN

              * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
              target group ARN.

          - **CustomizedMetricSpecification** *(dict) --*

            A customized metric. You can specify either a predefined metric or a customized metric.

            - **MetricName** *(string) --*

              The name of the metric.

            - **Namespace** *(string) --*

              The namespace of the metric.

            - **Dimensions** *(list) --*

              The dimensions of the metric.

              Conditional: If you published your metric with dimensions, you must specify the same
              dimensions in your scaling policy.

              - *(dict) --*

                Describes the dimension names and values associated with a metric.

                - **Name** *(string) --*

                  The name of the dimension.

                - **Value** *(string) --*

                  The value of the dimension.

            - **Statistic** *(string) --*

              The statistic of the metric.

            - **Unit** *(string) --*

              The unit of the metric.

          - **ScaleOutCooldown** *(integer) --*

            The amount of time, in seconds, after a scale-out activity completes before another
            scale-out activity can start.

            While the cooldown period is in effect, the capacity that has been added by the
            previous scale-out event that initiated the cooldown is calculated as part of the
            desired capacity for the next scale out. The intention is to continuously (but not
            excessively) scale out.

          - **ScaleInCooldown** *(integer) --*

            The amount of time, in seconds, after a scale-in activity completes before another
            scale in activity can start.

            The cooldown period is used to block subsequent scale-in requests until it has expired.
            The intention is to scale in conservatively to protect your application's availability.
            However, if another alarm triggers a scale-out policy during the cooldown period after
            a scale-in, Application Auto Scaling scales out your scalable target immediately.

          - **DisableScaleIn** *(boolean) --*

            Indicates whether scale in by the target tracking scaling policy is disabled. If the
            value is ``true`` , scale in is disabled and the target tracking scaling policy won't
            remove capacity from the scalable resource. Otherwise, scale in is enabled and the
            target tracking scaling policy can remove capacity from the scalable resource. The
            default value is ``false`` .

        - **Alarms** *(list) --*

          The CloudWatch alarms associated with the scaling policy.

          - *(dict) --*

            Represents a CloudWatch alarm associated with a scaling policy.

            - **AlarmName** *(string) --*

              The name of the alarm.

            - **AlarmARN** *(string) --*

              The Amazon Resource Name (ARN) of the alarm.

        - **CreationTime** *(datetime) --*

          The Unix timestamp for when the scaling policy was created.

    - **NextToken** *(string) --*

      The token required to get the next set of results. This value is ``null`` if there are no
      more results to return.
    """


_ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef(
    _ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef
):
    """
    Type definition for `ClientDescribeScheduledActionsResponseScheduledActions` `ScalableTargetAction`

    The new minimum and maximum capacity. You can set both values or just one. During the
    scheduled time, if the current capacity is below the minimum capacity, Application Auto
    Scaling scales out to the minimum capacity. If the current capacity is above the maximum
    capacity, Application Auto Scaling scales in to the maximum capacity.

    - **MinCapacity** *(integer) --*

      The minimum capacity.

    - **MaxCapacity** *(integer) --*

      The maximum capacity.
    """


_ClientDescribeScheduledActionsResponseScheduledActionsTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": str,
        "Schedule": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class ClientDescribeScheduledActionsResponseScheduledActionsTypeDef(
    _ClientDescribeScheduledActionsResponseScheduledActionsTypeDef
):
    """
    Type definition for `ClientDescribeScheduledActionsResponse` `ScheduledActions`

    Represents a scheduled action.

    - **ScheduledActionName** *(string) --*

      The name of the scheduled action.

    - **ScheduledActionARN** *(string) --*

      The Amazon Resource Name (ARN) of the scheduled action.

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service that provides the resource or ``custom-resource`` for a
      resource provided by your own application or service. For more information, see `AWS
      Service Namespaces
      <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *Amazon Web Services General Reference* .

    - **Schedule** *(string) --*

      The schedule for this action. The following formats are supported:

      * At expressions - "``at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* )`` "

      * Rate expressions - "``rate(*value*  *unit* )`` "

      * Cron expressions - "``cron(*fields* )`` "

      At expressions are useful for one-time schedules. Specify the time, in UTC.

      For rate expressions, *value* is a positive integer and *unit* is ``minute`` |
      ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` .

      For more information about cron expressions, see `Cron Expressions
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`__
      in the *Amazon CloudWatch Events User Guide* .

    - **ResourceId** *(string) --*

      The identifier of the resource associated with the scaling policy. This string consists
      of the resource type and unique identifier.

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
      cluster ID and instance group ID. Example:
      ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

      * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
      fleet name. Example: ``fleet/sample-fleet`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

      * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
      identifier is the resource ID. Example:
      ``endpoint/my-end-point/variant/KMeansClustering`` .

      * Custom resources are not supported with a resource type. This parameter must specify
      the ``OutputValue`` from the CloudFormation template stack used to access the resources.
      The unique identifier is defined by the service provider. More information is available
      in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

    - **ScalableDimension** *(string) --*

      The scalable dimension. This string consists of the service namespace, resource type, and
      scaling property.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
      Instance Group.

      * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

      * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
      SageMaker model endpoint variant.

      * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
      resource provided by your own application or service.

    - **StartTime** *(datetime) --*

      The date and time that the action is scheduled to begin.

    - **EndTime** *(datetime) --*

      The date and time that the action is scheduled to end.

    - **ScalableTargetAction** *(dict) --*

      The new minimum and maximum capacity. You can set both values or just one. During the
      scheduled time, if the current capacity is below the minimum capacity, Application Auto
      Scaling scales out to the minimum capacity. If the current capacity is above the maximum
      capacity, Application Auto Scaling scales in to the maximum capacity.

      - **MinCapacity** *(integer) --*

        The minimum capacity.

      - **MaxCapacity** *(integer) --*

        The maximum capacity.

    - **CreationTime** *(datetime) --*

      The date and time that the scheduled action was created.
    """


_ClientDescribeScheduledActionsResponseTypeDef = TypedDict(
    "_ClientDescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledActions": List[
            ClientDescribeScheduledActionsResponseScheduledActionsTypeDef
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

    - **ScheduledActions** *(list) --*

      Information about the scheduled actions.

      - *(dict) --*

        Represents a scheduled action.

        - **ScheduledActionName** *(string) --*

          The name of the scheduled action.

        - **ScheduledActionARN** *(string) --*

          The Amazon Resource Name (ARN) of the scheduled action.

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        - **Schedule** *(string) --*

          The schedule for this action. The following formats are supported:

          * At expressions - "``at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* )`` "

          * Rate expressions - "``rate(*value*  *unit* )`` "

          * Cron expressions - "``cron(*fields* )`` "

          At expressions are useful for one-time schedules. Specify the time, in UTC.

          For rate expressions, *value* is a positive integer and *unit* is ``minute`` |
          ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` .

          For more information about cron expressions, see `Cron Expressions
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`__
          in the *Amazon CloudWatch Events User Guide* .

        - **ResourceId** *(string) --*

          The identifier of the resource associated with the scaling policy. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example:
          ``endpoint/my-end-point/variant/KMeansClustering`` .

          * Custom resources are not supported with a resource type. This parameter must specify
          the ``OutputValue`` from the CloudFormation template stack used to access the resources.
          The unique identifier is defined by the service provider. More information is available
          in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

        - **ScalableDimension** *(string) --*

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
          Instance Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
          resource provided by your own application or service.

        - **StartTime** *(datetime) --*

          The date and time that the action is scheduled to begin.

        - **EndTime** *(datetime) --*

          The date and time that the action is scheduled to end.

        - **ScalableTargetAction** *(dict) --*

          The new minimum and maximum capacity. You can set both values or just one. During the
          scheduled time, if the current capacity is below the minimum capacity, Application Auto
          Scaling scales out to the minimum capacity. If the current capacity is above the maximum
          capacity, Application Auto Scaling scales in to the maximum capacity.

          - **MinCapacity** *(integer) --*

            The minimum capacity.

          - **MaxCapacity** *(integer) --*

            The maximum capacity.

        - **CreationTime** *(datetime) --*

          The date and time that the scheduled action was created.

    - **NextToken** *(string) --*

      The token required to get the next set of results. This value is ``null`` if there are no
      more results to return.
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

    Represents a CloudWatch alarm associated with a scaling policy.

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

    - **PolicyARN** *(string) --*

      The Amazon Resource Name (ARN) of the resulting scaling policy.

    - **Alarms** *(list) --*

      The CloudWatch alarms created for the target tracking scaling policy.

      - *(dict) --*

        Represents a CloudWatch alarm associated with a scaling policy.

        - **AlarmName** *(string) --*

          The name of the alarm.

        - **AlarmARN** *(string) --*

          The Amazon Resource Name (ARN) of the alarm.
    """


_RequiredClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {"ScalingAdjustment": int},
)
_OptionalClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {"MetricIntervalLowerBound": float, "MetricIntervalUpperBound": float},
    total=False,
)


class ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef(
    _RequiredClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef,
    _OptionalClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef,
):
    """
    Type definition for `ClientPutScalingPolicyStepScalingPolicyConfiguration` `StepAdjustments`

    Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an adjustment
    based on the difference between the value of the aggregated CloudWatch metric and the breach
    threshold that you've defined for the alarm.

    For the following examples, suppose that you have an alarm with a breach threshold of 50:

    * To trigger the adjustment when the metric is greater than or equal to 50 and less than 60,
    specify a lower bound of 0 and an upper bound of 10.

    * To trigger the adjustment when the metric is greater than 40 and less than or equal to 50,
    specify a lower bound of -10 and an upper bound of 0.

    There are a few rules for the step adjustments for your step policy:

    * The ranges of your step adjustments can't overlap or have a gap.

    * At most one step adjustment can have a null lower bound. If one step adjustment has a
    negative lower bound, then there must be a step adjustment with a null lower bound.

    * At most one step adjustment can have a null upper bound. If one step adjustment has a
    positive upper bound, then there must be a step adjustment with a null upper bound.

    * The upper and lower bound can't be null in the same step adjustment.

    - **MetricIntervalLowerBound** *(float) --*

      The lower bound for the difference between the alarm threshold and the CloudWatch metric.
      If the metric value is above the breach threshold, the lower bound is inclusive (the metric
      must be greater than or equal to the threshold plus the lower bound). Otherwise, it is
      exclusive (the metric must be greater than the threshold plus the lower bound). A null
      value indicates negative infinity.

    - **MetricIntervalUpperBound** *(float) --*

      The upper bound for the difference between the alarm threshold and the CloudWatch metric.
      If the metric value is above the breach threshold, the upper bound is exclusive (the metric
      must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the
      metric must be less than or equal to the threshold plus the upper bound). A null value
      indicates positive infinity.

      The upper bound must be greater than the lower bound.

    - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

      The amount by which to scale, based on the specified adjustment type. A positive value adds
      to the current scalable dimension while a negative number removes from the current scalable
      dimension.
    """


_ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef = TypedDict(
    "_ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": str,
        "StepAdjustments": List[
            ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef
        ],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": str,
    },
    total=False,
)


class ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef(
    _ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef
):
    """
    Type definition for `ClientPutScalingPolicy` `StepScalingPolicyConfiguration`

    A step scaling policy.

    This parameter is required if you are creating a policy and the policy type is ``StepScaling`` .

    - **AdjustmentType** *(string) --*

      Specifies whether the ``ScalingAdjustment`` value in a  StepAdjustment is an absolute number or
      a percentage of the current capacity.

    - **StepAdjustments** *(list) --*

      A set of adjustments that enable you to scale based on the size of the alarm breach.

      - *(dict) --*

        Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an adjustment
        based on the difference between the value of the aggregated CloudWatch metric and the breach
        threshold that you've defined for the alarm.

        For the following examples, suppose that you have an alarm with a breach threshold of 50:

        * To trigger the adjustment when the metric is greater than or equal to 50 and less than 60,
        specify a lower bound of 0 and an upper bound of 10.

        * To trigger the adjustment when the metric is greater than 40 and less than or equal to 50,
        specify a lower bound of -10 and an upper bound of 0.

        There are a few rules for the step adjustments for your step policy:

        * The ranges of your step adjustments can't overlap or have a gap.

        * At most one step adjustment can have a null lower bound. If one step adjustment has a
        negative lower bound, then there must be a step adjustment with a null lower bound.

        * At most one step adjustment can have a null upper bound. If one step adjustment has a
        positive upper bound, then there must be a step adjustment with a null upper bound.

        * The upper and lower bound can't be null in the same step adjustment.

        - **MetricIntervalLowerBound** *(float) --*

          The lower bound for the difference between the alarm threshold and the CloudWatch metric.
          If the metric value is above the breach threshold, the lower bound is inclusive (the metric
          must be greater than or equal to the threshold plus the lower bound). Otherwise, it is
          exclusive (the metric must be greater than the threshold plus the lower bound). A null
          value indicates negative infinity.

        - **MetricIntervalUpperBound** *(float) --*

          The upper bound for the difference between the alarm threshold and the CloudWatch metric.
          If the metric value is above the breach threshold, the upper bound is exclusive (the metric
          must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the
          metric must be less than or equal to the threshold plus the upper bound). A null value
          indicates positive infinity.

          The upper bound must be greater than the lower bound.

        - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

          The amount by which to scale, based on the specified adjustment type. A positive value adds
          to the current scalable dimension while a negative number removes from the current scalable
          dimension.

    - **MinAdjustmentMagnitude** *(integer) --*

      The minimum number to adjust your scalable dimension as a result of a scaling activity. If the
      adjustment type is ``PercentChangeInCapacity`` , the scaling policy changes the scalable
      dimension of the scalable target by this amount.

      For example, suppose that you create a step scaling policy to scale out an Amazon ECS service
      by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service has 4 tasks and
      the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a
      ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out the service by 2 tasks.

    - **Cooldown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes where previous
      trigger-related scaling activities can influence future scaling events.

      For scale-out policies, while the cooldown period is in effect, the capacity that has been
      added by the previous scale-out event that initiated the cooldown is calculated as part of the
      desired capacity for the next scale out. The intention is to continuously (but not excessively)
      scale out. For example, an alarm triggers a step scaling policy to scale out an Amazon ECS
      service by 2 tasks, the scaling activity completes successfully, and a cooldown period of 5
      minutes starts. During the cooldown period, if the alarm triggers the same policy again but at
      a more aggressive step adjustment to scale out the service by 3 tasks, the 2 tasks that were
      added in the previous scale-out event are considered part of that capacity and only 1
      additional task is added to the desired count.

      For scale-in policies, the cooldown period is used to block subsequent scale-in requests until
      it has expired. The intention is to scale in conservatively to protect your application's
      availability. However, if another alarm triggers a scale-out policy during the cooldown period
      after a scale-in, Application Auto Scaling scales out your scalable target immediately.

    - **MetricAggregationType** *(string) --*

      The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` , ``Maximum`` ,
      and ``Average`` . If the aggregation type is null, the value is treated as ``Average`` .
    """


_ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
)


class ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification` `Dimensions`

    Describes the dimension names and values associated with a metric.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the dimension.

    - **Value** *(string) --* **[REQUIRED]**

      The value of the dimension.
    """


_RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    {"MetricName": str, "Namespace": str, "Statistic": str},
)
_OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "Dimensions": List[
            ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Unit": str,
    },
    total=False,
)


class ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef(
    _RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef,
    _OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientPutScalingPolicyTargetTrackingScalingPolicyConfiguration` `CustomizedMetricSpecification`

    A customized metric. You can specify either a predefined metric or a customized metric.

    - **MetricName** *(string) --* **[REQUIRED]**

      The name of the metric.

    - **Namespace** *(string) --* **[REQUIRED]**

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the same
      dimensions in your scaling policy.

      - *(dict) --*

        Describes the dimension names and values associated with a metric.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the dimension.

        - **Value** *(string) --* **[REQUIRED]**

          The value of the dimension.

    - **Statistic** *(string) --* **[REQUIRED]**

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    {"PredefinedMetricType": str},
)
_OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    {"ResourceLabel": str},
    total=False,
)


class ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef(
    _RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef,
    _OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef,
):
    """
    Type definition for `ClientPutScalingPolicyTargetTrackingScalingPolicyConfiguration` `PredefinedMetricSpecification`

    A predefined metric. You can specify either a predefined metric or a customized metric.

    - **PredefinedMetricType** *(string) --* **[REQUIRED]**

      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot Fleet
      requests and ECS services.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a resource label
      unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group attached
      to the Spot Fleet request or ECS service.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group
      ARN.
    """


_RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef",
    {"TargetValue": float},
)
_OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)


class ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef(
    _RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef,
    _OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef,
):
    """
    Type definition for `ClientPutScalingPolicy` `TargetTrackingScalingPolicyConfiguration`

    A target tracking scaling policy. Includes support for predefined or customized metrics.

    This parameter is required if you are creating a policy and the policy type is
    ``TargetTrackingScaling`` .

    - **TargetValue** *(float) --* **[REQUIRED]**

      The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or
      2e-360 to 2e360 (Base 2).

    - **PredefinedMetricSpecification** *(dict) --*

      A predefined metric. You can specify either a predefined metric or a customized metric.

      - **PredefinedMetricType** *(string) --* **[REQUIRED]**

        The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot Fleet
        requests and ECS services.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a resource label
        unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group attached
        to the Spot Fleet request or ECS service.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group
        ARN.

    - **CustomizedMetricSpecification** *(dict) --*

      A customized metric. You can specify either a predefined metric or a customized metric.

      - **MetricName** *(string) --* **[REQUIRED]**

        The name of the metric.

      - **Namespace** *(string) --* **[REQUIRED]**

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the same
        dimensions in your scaling policy.

        - *(dict) --*

          Describes the dimension names and values associated with a metric.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the dimension.

          - **Value** *(string) --* **[REQUIRED]**

            The value of the dimension.

      - **Statistic** *(string) --* **[REQUIRED]**

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **ScaleOutCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-out activity completes before another scale-out
      activity can start.

      While the cooldown period is in effect, the capacity that has been added by the previous
      scale-out event that initiated the cooldown is calculated as part of the desired capacity for
      the next scale out. The intention is to continuously (but not excessively) scale out.

    - **ScaleInCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-in activity completes before another scale in
      activity can start.

      The cooldown period is used to block subsequent scale-in requests until it has expired. The
      intention is to scale in conservatively to protect your application's availability. However, if
      another alarm triggers a scale-out policy during the cooldown period after a scale-in,
      Application Auto Scaling scales out your scalable target immediately.

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scale in by the target tracking scaling policy is disabled. If the value is
      ``true`` , scale in is disabled and the target tracking scaling policy won't remove capacity
      from the scalable resource. Otherwise, scale in is enabled and the target tracking scaling
      policy can remove capacity from the scalable resource. The default value is ``false`` .
    """


_ClientPutScheduledActionScalableTargetActionTypeDef = TypedDict(
    "_ClientPutScheduledActionScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class ClientPutScheduledActionScalableTargetActionTypeDef(
    _ClientPutScheduledActionScalableTargetActionTypeDef
):
    """
    Type definition for `ClientPutScheduledAction` `ScalableTargetAction`

    The new minimum and maximum capacity. You can set both values or just one. During the scheduled
    time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out
    to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto
    Scaling scales in to the maximum capacity.

    - **MinCapacity** *(integer) --*

      The minimum capacity.

    - **MaxCapacity** *(integer) --*

      The maximum capacity.
    """


_ClientRegisterScalableTargetSuspendedStateTypeDef = TypedDict(
    "_ClientRegisterScalableTargetSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)


class ClientRegisterScalableTargetSuspendedStateTypeDef(
    _ClientRegisterScalableTargetSuspendedStateTypeDef
):
    """
    Type definition for `ClientRegisterScalableTarget` `SuspendedState`

    An embedded object that contains attributes and attribute values that are used to suspend and
    resume automatic scaling. Setting the value of an attribute to ``true`` suspends the specified
    scaling activities. Setting it to ``false`` (default) resumes the specified scaling activities.

     **Suspension Outcomes**

    * For ``DynamicScalingInSuspended`` , while a suspension is in effect, all scale-in activities
    that are triggered by a scaling policy are suspended.

    * For ``DynamicScalingOutSuspended`` , while a suspension is in effect, all scale-out activities
    that are triggered by a scaling policy are suspended.

    * For ``ScheduledScalingSuspended`` , while a suspension is in effect, all scaling activities
    that involve scheduled actions are suspended.

    For more information, see `Suspend and Resume Application Auto Scaling
    <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html>`__
    in the *Application Auto Scaling User Guide* .

    - **DynamicScalingInSuspended** *(boolean) --*

      Whether scale in by a target tracking scaling policy or a step scaling policy is suspended. Set
      the value to ``true`` if you don't want Application Auto Scaling to remove capacity when a
      scaling policy is triggered. The default is ``false`` .

    - **DynamicScalingOutSuspended** *(boolean) --*

      Whether scale out by a target tracking scaling policy or a step scaling policy is suspended.
      Set the value to ``true`` if you don't want Application Auto Scaling to add capacity when a
      scaling policy is triggered. The default is ``false`` .

    - **ScheduledScalingSuspended** *(boolean) --*

      Whether scheduled scaling is suspended. Set the value to ``true`` if you don't want Application
      Auto Scaling to add or remove capacity by initiating scheduled actions. The default is
      ``false`` .
    """


_DescribeScalableTargetsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalableTargetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalableTargetsPaginatePaginationConfigTypeDef(
    _DescribeScalableTargetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeScalableTargetsPaginate` `PaginationConfig`

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


_DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef = TypedDict(
    "_DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)


class DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef(
    _DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef
):
    """
    Type definition for `DescribeScalableTargetsPaginateResponseScalableTargets` `SuspendedState`

    Specifies whether the scaling activities for a scalable target are in a suspended state.

    - **DynamicScalingInSuspended** *(boolean) --*

      Whether scale in by a target tracking scaling policy or a step scaling policy is
      suspended. Set the value to ``true`` if you don't want Application Auto Scaling to
      remove capacity when a scaling policy is triggered. The default is ``false`` .

    - **DynamicScalingOutSuspended** *(boolean) --*

      Whether scale out by a target tracking scaling policy or a step scaling policy is
      suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add
      capacity when a scaling policy is triggered. The default is ``false`` .

    - **ScheduledScalingSuspended** *(boolean) --*

      Whether scheduled scaling is suspended. Set the value to ``true`` if you don't want
      Application Auto Scaling to add or remove capacity by initiating scheduled actions. The
      default is ``false`` .
    """


_DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef = TypedDict(
    "_DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef",
    {
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
        "SuspendedState": DescribeScalableTargetsPaginateResponseScalableTargetsSuspendedStateTypeDef,
    },
    total=False,
)


class DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef(
    _DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef
):
    """
    Type definition for `DescribeScalableTargetsPaginateResponse` `ScalableTargets`

    Represents a scalable target.

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service that provides the resource or ``custom-resource`` for a
      resource provided by your own application or service. For more information, see `AWS
      Service Namespaces
      <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *Amazon Web Services General Reference* .

    - **ResourceId** *(string) --*

      The identifier of the resource associated with the scalable target. This string consists
      of the resource type and unique identifier.

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
      cluster ID and instance group ID. Example:
      ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

      * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
      fleet name. Example: ``fleet/sample-fleet`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

      * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
      identifier is the resource ID. Example:
      ``endpoint/my-end-point/variant/KMeansClustering`` .

      * Custom resources are not supported with a resource type. This parameter must specify
      the ``OutputValue`` from the CloudFormation template stack used to access the resources.
      The unique identifier is defined by the service provider. More information is available
      in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

    - **ScalableDimension** *(string) --*

      The scalable dimension associated with the scalable target. This string consists of the
      service namespace, resource type, and scaling property.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
      Instance Group.

      * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

      * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
      SageMaker model endpoint variant.

      * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
      resource provided by your own application or service.

    - **MinCapacity** *(integer) --*

      The minimum value to scale to in response to a scale-in event.

    - **MaxCapacity** *(integer) --*

      The maximum value to scale to in response to a scale-out event.

    - **RoleARN** *(string) --*

      The ARN of an IAM role that allows Application Auto Scaling to modify the scalable target
      on your behalf.

    - **CreationTime** *(datetime) --*

      The Unix timestamp for when the scalable target was created.

    - **SuspendedState** *(dict) --*

      Specifies whether the scaling activities for a scalable target are in a suspended state.

      - **DynamicScalingInSuspended** *(boolean) --*

        Whether scale in by a target tracking scaling policy or a step scaling policy is
        suspended. Set the value to ``true`` if you don't want Application Auto Scaling to
        remove capacity when a scaling policy is triggered. The default is ``false`` .

      - **DynamicScalingOutSuspended** *(boolean) --*

        Whether scale out by a target tracking scaling policy or a step scaling policy is
        suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add
        capacity when a scaling policy is triggered. The default is ``false`` .

      - **ScheduledScalingSuspended** *(boolean) --*

        Whether scheduled scaling is suspended. Set the value to ``true`` if you don't want
        Application Auto Scaling to add or remove capacity by initiating scheduled actions. The
        default is ``false`` .
    """


_DescribeScalableTargetsPaginateResponseTypeDef = TypedDict(
    "_DescribeScalableTargetsPaginateResponseTypeDef",
    {
        "ScalableTargets": List[
            DescribeScalableTargetsPaginateResponseScalableTargetsTypeDef
        ]
    },
    total=False,
)


class DescribeScalableTargetsPaginateResponseTypeDef(
    _DescribeScalableTargetsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeScalableTargetsPaginate` `Response`

    - **ScalableTargets** *(list) --*

      The scalable targets that match the request parameters.

      - *(dict) --*

        Represents a scalable target.

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        - **ResourceId** *(string) --*

          The identifier of the resource associated with the scalable target. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example:
          ``endpoint/my-end-point/variant/KMeansClustering`` .

          * Custom resources are not supported with a resource type. This parameter must specify
          the ``OutputValue`` from the CloudFormation template stack used to access the resources.
          The unique identifier is defined by the service provider. More information is available
          in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

        - **ScalableDimension** *(string) --*

          The scalable dimension associated with the scalable target. This string consists of the
          service namespace, resource type, and scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
          Instance Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
          resource provided by your own application or service.

        - **MinCapacity** *(integer) --*

          The minimum value to scale to in response to a scale-in event.

        - **MaxCapacity** *(integer) --*

          The maximum value to scale to in response to a scale-out event.

        - **RoleARN** *(string) --*

          The ARN of an IAM role that allows Application Auto Scaling to modify the scalable target
          on your behalf.

        - **CreationTime** *(datetime) --*

          The Unix timestamp for when the scalable target was created.

        - **SuspendedState** *(dict) --*

          Specifies whether the scaling activities for a scalable target are in a suspended state.

          - **DynamicScalingInSuspended** *(boolean) --*

            Whether scale in by a target tracking scaling policy or a step scaling policy is
            suspended. Set the value to ``true`` if you don't want Application Auto Scaling to
            remove capacity when a scaling policy is triggered. The default is ``false`` .

          - **DynamicScalingOutSuspended** *(boolean) --*

            Whether scale out by a target tracking scaling policy or a step scaling policy is
            suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add
            capacity when a scaling policy is triggered. The default is ``false`` .

          - **ScheduledScalingSuspended** *(boolean) --*

            Whether scheduled scaling is suspended. Set the value to ``true`` if you don't want
            Application Auto Scaling to add or remove capacity by initiating scheduled actions. The
            default is ``false`` .
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


_DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef = TypedDict(
    "_DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": str,
        "StatusMessage": str,
        "Details": str,
    },
    total=False,
)


class DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef(
    _DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef
):
    """
    Type definition for `DescribeScalingActivitiesPaginateResponse` `ScalingActivities`

    Represents a scaling activity.

    - **ActivityId** *(string) --*

      The unique identifier of the scaling activity.

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service that provides the resource or ``custom-resource`` for a
      resource provided by your own application or service. For more information, see `AWS
      Service Namespaces
      <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *Amazon Web Services General Reference* .

    - **ResourceId** *(string) --*

      The identifier of the resource associated with the scaling activity. This string consists
      of the resource type and unique identifier.

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
      cluster ID and instance group ID. Example:
      ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

      * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
      fleet name. Example: ``fleet/sample-fleet`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

      * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
      identifier is the resource ID. Example:
      ``endpoint/my-end-point/variant/KMeansClustering`` .

      * Custom resources are not supported with a resource type. This parameter must specify
      the ``OutputValue`` from the CloudFormation template stack used to access the resources.
      The unique identifier is defined by the service provider. More information is available
      in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

    - **ScalableDimension** *(string) --*

      The scalable dimension. This string consists of the service namespace, resource type, and
      scaling property.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
      Instance Group.

      * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

      * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
      SageMaker model endpoint variant.

      * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
      resource provided by your own application or service.

    - **Description** *(string) --*

      A simple description of what action the scaling activity intends to accomplish.

    - **Cause** *(string) --*

      A simple description of what caused the scaling activity to happen.

    - **StartTime** *(datetime) --*

      The Unix timestamp for when the scaling activity began.

    - **EndTime** *(datetime) --*

      The Unix timestamp for when the scaling activity ended.

    - **StatusCode** *(string) --*

      Indicates the status of the scaling activity.

    - **StatusMessage** *(string) --*

      A simple message about the current status of the scaling activity.

    - **Details** *(string) --*

      The details about the scaling activity.
    """


_DescribeScalingActivitiesPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingActivitiesPaginateResponseTypeDef",
    {
        "ScalingActivities": List[
            DescribeScalingActivitiesPaginateResponseScalingActivitiesTypeDef
        ]
    },
    total=False,
)


class DescribeScalingActivitiesPaginateResponseTypeDef(
    _DescribeScalingActivitiesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeScalingActivitiesPaginate` `Response`

    - **ScalingActivities** *(list) --*

      A list of scaling activity objects.

      - *(dict) --*

        Represents a scaling activity.

        - **ActivityId** *(string) --*

          The unique identifier of the scaling activity.

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        - **ResourceId** *(string) --*

          The identifier of the resource associated with the scaling activity. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example:
          ``endpoint/my-end-point/variant/KMeansClustering`` .

          * Custom resources are not supported with a resource type. This parameter must specify
          the ``OutputValue`` from the CloudFormation template stack used to access the resources.
          The unique identifier is defined by the service provider. More information is available
          in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

        - **ScalableDimension** *(string) --*

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
          Instance Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
          resource provided by your own application or service.

        - **Description** *(string) --*

          A simple description of what action the scaling activity intends to accomplish.

        - **Cause** *(string) --*

          A simple description of what caused the scaling activity to happen.

        - **StartTime** *(datetime) --*

          The Unix timestamp for when the scaling activity began.

        - **EndTime** *(datetime) --*

          The Unix timestamp for when the scaling activity ended.

        - **StatusCode** *(string) --*

          Indicates the status of the scaling activity.

        - **StatusMessage** *(string) --*

          A simple message about the current status of the scaling activity.

        - **Details** *(string) --*

          The details about the scaling activity.
    """


_DescribeScalingPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeScalingPoliciesPaginatePaginationConfigTypeDef(
    _DescribeScalingPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginate` `PaginationConfig`

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


_DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginateResponseScalingPolicies` `Alarms`

    Represents a CloudWatch alarm associated with a scaling policy.

    - **AlarmName** *(string) --*

      The name of the alarm.

    - **AlarmARN** *(string) --*

      The Amazon Resource Name (ARN) of the alarm.
    """


_DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfiguration` `StepAdjustments`

    Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an
    adjustment based on the difference between the value of the aggregated CloudWatch
    metric and the breach threshold that you've defined for the alarm.

    For the following examples, suppose that you have an alarm with a breach threshold of
    50:

    * To trigger the adjustment when the metric is greater than or equal to 50 and less
    than 60, specify a lower bound of 0 and an upper bound of 10.

    * To trigger the adjustment when the metric is greater than 40 and less than or equal
    to 50, specify a lower bound of -10 and an upper bound of 0.

    There are a few rules for the step adjustments for your step policy:

    * The ranges of your step adjustments can't overlap or have a gap.

    * At most one step adjustment can have a null lower bound. If one step adjustment has
    a negative lower bound, then there must be a step adjustment with a null lower bound.

    * At most one step adjustment can have a null upper bound. If one step adjustment has
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
      value adds to the current scalable dimension while a negative number removes from
      the current scalable dimension.
    """


_DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": str,
        "StepAdjustments": List[
            DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef
        ],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": str,
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginateResponseScalingPolicies` `StepScalingPolicyConfiguration`

    A step scaling policy.

    - **AdjustmentType** *(string) --*

      Specifies whether the ``ScalingAdjustment`` value in a  StepAdjustment is an absolute
      number or a percentage of the current capacity.

    - **StepAdjustments** *(list) --*

      A set of adjustments that enable you to scale based on the size of the alarm breach.

      - *(dict) --*

        Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an
        adjustment based on the difference between the value of the aggregated CloudWatch
        metric and the breach threshold that you've defined for the alarm.

        For the following examples, suppose that you have an alarm with a breach threshold of
        50:

        * To trigger the adjustment when the metric is greater than or equal to 50 and less
        than 60, specify a lower bound of 0 and an upper bound of 10.

        * To trigger the adjustment when the metric is greater than 40 and less than or equal
        to 50, specify a lower bound of -10 and an upper bound of 0.

        There are a few rules for the step adjustments for your step policy:

        * The ranges of your step adjustments can't overlap or have a gap.

        * At most one step adjustment can have a null lower bound. If one step adjustment has
        a negative lower bound, then there must be a step adjustment with a null lower bound.

        * At most one step adjustment can have a null upper bound. If one step adjustment has
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
          value adds to the current scalable dimension while a negative number removes from
          the current scalable dimension.

    - **MinAdjustmentMagnitude** *(integer) --*

      The minimum number to adjust your scalable dimension as a result of a scaling activity.
      If the adjustment type is ``PercentChangeInCapacity`` , the scaling policy changes the
      scalable dimension of the scalable target by this amount.

      For example, suppose that you create a step scaling policy to scale out an Amazon ECS
      service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service
      has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because
      you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out
      the service by 2 tasks.

    - **Cooldown** *(integer) --*

      The amount of time, in seconds, after a scaling activity completes where previous
      trigger-related scaling activities can influence future scaling events.

      For scale-out policies, while the cooldown period is in effect, the capacity that has
      been added by the previous scale-out event that initiated the cooldown is calculated as
      part of the desired capacity for the next scale out. The intention is to continuously
      (but not excessively) scale out. For example, an alarm triggers a step scaling policy
      to scale out an Amazon ECS service by 2 tasks, the scaling activity completes
      successfully, and a cooldown period of 5 minutes starts. During the cooldown period, if
      the alarm triggers the same policy again but at a more aggressive step adjustment to
      scale out the service by 3 tasks, the 2 tasks that were added in the previous scale-out
      event are considered part of that capacity and only 1 additional task is added to the
      desired count.

      For scale-in policies, the cooldown period is used to block subsequent scale-in
      requests until it has expired. The intention is to scale in conservatively to protect
      your application's availability. However, if another alarm triggers a scale-out policy
      during the cooldown period after a scale-in, Application Auto Scaling scales out your
      scalable target immediately.

    - **MetricAggregationType** *(string) --*

      The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` ,
      ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated
      as ``Average`` .
    """


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification` `Dimensions`

    Describes the dimension names and values associated with a metric.

    - **Name** *(string) --*

      The name of the dimension.

    - **Value** *(string) --*

      The value of the dimension.
    """


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfiguration` `CustomizedMetricSpecification`

    A customized metric. You can specify either a predefined metric or a customized metric.

    - **MetricName** *(string) --*

      The name of the metric.

    - **Namespace** *(string) --*

      The namespace of the metric.

    - **Dimensions** *(list) --*

      The dimensions of the metric.

      Conditional: If you published your metric with dimensions, you must specify the same
      dimensions in your scaling policy.

      - *(dict) --*

        Describes the dimension names and values associated with a metric.

        - **Name** *(string) --*

          The name of the dimension.

        - **Value** *(string) --*

          The value of the dimension.

    - **Statistic** *(string) --*

      The statistic of the metric.

    - **Unit** *(string) --*

      The unit of the metric.
    """


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    {"PredefinedMetricType": str, "ResourceLabel": str},
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfiguration` `PredefinedMetricSpecification`

    A predefined metric. You can specify either a predefined metric or a customized metric.

    - **PredefinedMetricType** *(string) --*

      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot
      Fleet requests and ECS services.

    - **ResourceLabel** *(string) --*

      Identifies the resource associated with the metric type. You can't specify a resource
      label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
      group attached to the Spot Fleet request or ECS service.

      The format is
      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
      where:

      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
      balancer ARN

      * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
      target group ARN.
    """


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginateResponseScalingPolicies` `TargetTrackingScalingPolicyConfiguration`

    A target tracking scaling policy.

    - **TargetValue** *(float) --*

      The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10)
      or 2e-360 to 2e360 (Base 2).

    - **PredefinedMetricSpecification** *(dict) --*

      A predefined metric. You can specify either a predefined metric or a customized metric.

      - **PredefinedMetricType** *(string) --*

        The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot
        Fleet requests and ECS services.

      - **ResourceLabel** *(string) --*

        Identifies the resource associated with the metric type. You can't specify a resource
        label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
        group attached to the Spot Fleet request or ECS service.

        The format is
        app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
        where:

        * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
        balancer ARN

        * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
        target group ARN.

    - **CustomizedMetricSpecification** *(dict) --*

      A customized metric. You can specify either a predefined metric or a customized metric.

      - **MetricName** *(string) --*

        The name of the metric.

      - **Namespace** *(string) --*

        The namespace of the metric.

      - **Dimensions** *(list) --*

        The dimensions of the metric.

        Conditional: If you published your metric with dimensions, you must specify the same
        dimensions in your scaling policy.

        - *(dict) --*

          Describes the dimension names and values associated with a metric.

          - **Name** *(string) --*

            The name of the dimension.

          - **Value** *(string) --*

            The value of the dimension.

      - **Statistic** *(string) --*

        The statistic of the metric.

      - **Unit** *(string) --*

        The unit of the metric.

    - **ScaleOutCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-out activity completes before another
      scale-out activity can start.

      While the cooldown period is in effect, the capacity that has been added by the
      previous scale-out event that initiated the cooldown is calculated as part of the
      desired capacity for the next scale out. The intention is to continuously (but not
      excessively) scale out.

    - **ScaleInCooldown** *(integer) --*

      The amount of time, in seconds, after a scale-in activity completes before another
      scale in activity can start.

      The cooldown period is used to block subsequent scale-in requests until it has expired.
      The intention is to scale in conservatively to protect your application's availability.
      However, if another alarm triggers a scale-out policy during the cooldown period after
      a scale-in, Application Auto Scaling scales out your scalable target immediately.

    - **DisableScaleIn** *(boolean) --*

      Indicates whether scale in by the target tracking scaling policy is disabled. If the
      value is ``true`` , scale in is disabled and the target tracking scaling policy won't
      remove capacity from the scalable resource. Otherwise, scale in is enabled and the
      target tracking scaling policy can remove capacity from the scalable resource. The
      default value is ``false`` .
    """


_DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "PolicyType": str,
        "StepScalingPolicyConfiguration": DescribeScalingPoliciesPaginateResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef,
        "TargetTrackingScalingPolicyConfiguration": DescribeScalingPoliciesPaginateResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
        "Alarms": List[
            DescribeScalingPoliciesPaginateResponseScalingPoliciesAlarmsTypeDef
        ],
        "CreationTime": datetime,
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef(
    _DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginateResponse` `ScalingPolicies`

    Represents a scaling policy to use with Application Auto Scaling.

    - **PolicyARN** *(string) --*

      The Amazon Resource Name (ARN) of the scaling policy.

    - **PolicyName** *(string) --*

      The name of the scaling policy.

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service that provides the resource or ``custom-resource`` for a
      resource provided by your own application or service. For more information, see `AWS
      Service Namespaces
      <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *Amazon Web Services General Reference* .

    - **ResourceId** *(string) --*

      The identifier of the resource associated with the scaling policy. This string consists
      of the resource type and unique identifier.

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
      cluster ID and instance group ID. Example:
      ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

      * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
      fleet name. Example: ``fleet/sample-fleet`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

      * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
      identifier is the resource ID. Example:
      ``endpoint/my-end-point/variant/KMeansClustering`` .

      * Custom resources are not supported with a resource type. This parameter must specify
      the ``OutputValue`` from the CloudFormation template stack used to access the resources.
      The unique identifier is defined by the service provider. More information is available
      in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

    - **ScalableDimension** *(string) --*

      The scalable dimension. This string consists of the service namespace, resource type, and
      scaling property.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
      Instance Group.

      * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

      * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
      SageMaker model endpoint variant.

      * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
      resource provided by your own application or service.

    - **PolicyType** *(string) --*

      The scaling policy type.

    - **StepScalingPolicyConfiguration** *(dict) --*

      A step scaling policy.

      - **AdjustmentType** *(string) --*

        Specifies whether the ``ScalingAdjustment`` value in a  StepAdjustment is an absolute
        number or a percentage of the current capacity.

      - **StepAdjustments** *(list) --*

        A set of adjustments that enable you to scale based on the size of the alarm breach.

        - *(dict) --*

          Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an
          adjustment based on the difference between the value of the aggregated CloudWatch
          metric and the breach threshold that you've defined for the alarm.

          For the following examples, suppose that you have an alarm with a breach threshold of
          50:

          * To trigger the adjustment when the metric is greater than or equal to 50 and less
          than 60, specify a lower bound of 0 and an upper bound of 10.

          * To trigger the adjustment when the metric is greater than 40 and less than or equal
          to 50, specify a lower bound of -10 and an upper bound of 0.

          There are a few rules for the step adjustments for your step policy:

          * The ranges of your step adjustments can't overlap or have a gap.

          * At most one step adjustment can have a null lower bound. If one step adjustment has
          a negative lower bound, then there must be a step adjustment with a null lower bound.

          * At most one step adjustment can have a null upper bound. If one step adjustment has
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
            value adds to the current scalable dimension while a negative number removes from
            the current scalable dimension.

      - **MinAdjustmentMagnitude** *(integer) --*

        The minimum number to adjust your scalable dimension as a result of a scaling activity.
        If the adjustment type is ``PercentChangeInCapacity`` , the scaling policy changes the
        scalable dimension of the scalable target by this amount.

        For example, suppose that you create a step scaling policy to scale out an Amazon ECS
        service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service
        has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because
        you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out
        the service by 2 tasks.

      - **Cooldown** *(integer) --*

        The amount of time, in seconds, after a scaling activity completes where previous
        trigger-related scaling activities can influence future scaling events.

        For scale-out policies, while the cooldown period is in effect, the capacity that has
        been added by the previous scale-out event that initiated the cooldown is calculated as
        part of the desired capacity for the next scale out. The intention is to continuously
        (but not excessively) scale out. For example, an alarm triggers a step scaling policy
        to scale out an Amazon ECS service by 2 tasks, the scaling activity completes
        successfully, and a cooldown period of 5 minutes starts. During the cooldown period, if
        the alarm triggers the same policy again but at a more aggressive step adjustment to
        scale out the service by 3 tasks, the 2 tasks that were added in the previous scale-out
        event are considered part of that capacity and only 1 additional task is added to the
        desired count.

        For scale-in policies, the cooldown period is used to block subsequent scale-in
        requests until it has expired. The intention is to scale in conservatively to protect
        your application's availability. However, if another alarm triggers a scale-out policy
        during the cooldown period after a scale-in, Application Auto Scaling scales out your
        scalable target immediately.

      - **MetricAggregationType** *(string) --*

        The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` ,
        ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated
        as ``Average`` .

    - **TargetTrackingScalingPolicyConfiguration** *(dict) --*

      A target tracking scaling policy.

      - **TargetValue** *(float) --*

        The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10)
        or 2e-360 to 2e360 (Base 2).

      - **PredefinedMetricSpecification** *(dict) --*

        A predefined metric. You can specify either a predefined metric or a customized metric.

        - **PredefinedMetricType** *(string) --*

          The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot
          Fleet requests and ECS services.

        - **ResourceLabel** *(string) --*

          Identifies the resource associated with the metric type. You can't specify a resource
          label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
          group attached to the Spot Fleet request or ECS service.

          The format is
          app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
          where:

          * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
          balancer ARN

          * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
          target group ARN.

      - **CustomizedMetricSpecification** *(dict) --*

        A customized metric. You can specify either a predefined metric or a customized metric.

        - **MetricName** *(string) --*

          The name of the metric.

        - **Namespace** *(string) --*

          The namespace of the metric.

        - **Dimensions** *(list) --*

          The dimensions of the metric.

          Conditional: If you published your metric with dimensions, you must specify the same
          dimensions in your scaling policy.

          - *(dict) --*

            Describes the dimension names and values associated with a metric.

            - **Name** *(string) --*

              The name of the dimension.

            - **Value** *(string) --*

              The value of the dimension.

        - **Statistic** *(string) --*

          The statistic of the metric.

        - **Unit** *(string) --*

          The unit of the metric.

      - **ScaleOutCooldown** *(integer) --*

        The amount of time, in seconds, after a scale-out activity completes before another
        scale-out activity can start.

        While the cooldown period is in effect, the capacity that has been added by the
        previous scale-out event that initiated the cooldown is calculated as part of the
        desired capacity for the next scale out. The intention is to continuously (but not
        excessively) scale out.

      - **ScaleInCooldown** *(integer) --*

        The amount of time, in seconds, after a scale-in activity completes before another
        scale in activity can start.

        The cooldown period is used to block subsequent scale-in requests until it has expired.
        The intention is to scale in conservatively to protect your application's availability.
        However, if another alarm triggers a scale-out policy during the cooldown period after
        a scale-in, Application Auto Scaling scales out your scalable target immediately.

      - **DisableScaleIn** *(boolean) --*

        Indicates whether scale in by the target tracking scaling policy is disabled. If the
        value is ``true`` , scale in is disabled and the target tracking scaling policy won't
        remove capacity from the scalable resource. Otherwise, scale in is enabled and the
        target tracking scaling policy can remove capacity from the scalable resource. The
        default value is ``false`` .

    - **Alarms** *(list) --*

      The CloudWatch alarms associated with the scaling policy.

      - *(dict) --*

        Represents a CloudWatch alarm associated with a scaling policy.

        - **AlarmName** *(string) --*

          The name of the alarm.

        - **AlarmARN** *(string) --*

          The Amazon Resource Name (ARN) of the alarm.

    - **CreationTime** *(datetime) --*

      The Unix timestamp for when the scaling policy was created.
    """


_DescribeScalingPoliciesPaginateResponseTypeDef = TypedDict(
    "_DescribeScalingPoliciesPaginateResponseTypeDef",
    {
        "ScalingPolicies": List[
            DescribeScalingPoliciesPaginateResponseScalingPoliciesTypeDef
        ]
    },
    total=False,
)


class DescribeScalingPoliciesPaginateResponseTypeDef(
    _DescribeScalingPoliciesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeScalingPoliciesPaginate` `Response`

    - **ScalingPolicies** *(list) --*

      Information about the scaling policies.

      - *(dict) --*

        Represents a scaling policy to use with Application Auto Scaling.

        - **PolicyARN** *(string) --*

          The Amazon Resource Name (ARN) of the scaling policy.

        - **PolicyName** *(string) --*

          The name of the scaling policy.

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        - **ResourceId** *(string) --*

          The identifier of the resource associated with the scaling policy. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example:
          ``endpoint/my-end-point/variant/KMeansClustering`` .

          * Custom resources are not supported with a resource type. This parameter must specify
          the ``OutputValue`` from the CloudFormation template stack used to access the resources.
          The unique identifier is defined by the service provider. More information is available
          in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

        - **ScalableDimension** *(string) --*

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
          Instance Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
          resource provided by your own application or service.

        - **PolicyType** *(string) --*

          The scaling policy type.

        - **StepScalingPolicyConfiguration** *(dict) --*

          A step scaling policy.

          - **AdjustmentType** *(string) --*

            Specifies whether the ``ScalingAdjustment`` value in a  StepAdjustment is an absolute
            number or a percentage of the current capacity.

          - **StepAdjustments** *(list) --*

            A set of adjustments that enable you to scale based on the size of the alarm breach.

            - *(dict) --*

              Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an
              adjustment based on the difference between the value of the aggregated CloudWatch
              metric and the breach threshold that you've defined for the alarm.

              For the following examples, suppose that you have an alarm with a breach threshold of
              50:

              * To trigger the adjustment when the metric is greater than or equal to 50 and less
              than 60, specify a lower bound of 0 and an upper bound of 10.

              * To trigger the adjustment when the metric is greater than 40 and less than or equal
              to 50, specify a lower bound of -10 and an upper bound of 0.

              There are a few rules for the step adjustments for your step policy:

              * The ranges of your step adjustments can't overlap or have a gap.

              * At most one step adjustment can have a null lower bound. If one step adjustment has
              a negative lower bound, then there must be a step adjustment with a null lower bound.

              * At most one step adjustment can have a null upper bound. If one step adjustment has
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
                value adds to the current scalable dimension while a negative number removes from
                the current scalable dimension.

          - **MinAdjustmentMagnitude** *(integer) --*

            The minimum number to adjust your scalable dimension as a result of a scaling activity.
            If the adjustment type is ``PercentChangeInCapacity`` , the scaling policy changes the
            scalable dimension of the scalable target by this amount.

            For example, suppose that you create a step scaling policy to scale out an Amazon ECS
            service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service
            has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because
            you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out
            the service by 2 tasks.

          - **Cooldown** *(integer) --*

            The amount of time, in seconds, after a scaling activity completes where previous
            trigger-related scaling activities can influence future scaling events.

            For scale-out policies, while the cooldown period is in effect, the capacity that has
            been added by the previous scale-out event that initiated the cooldown is calculated as
            part of the desired capacity for the next scale out. The intention is to continuously
            (but not excessively) scale out. For example, an alarm triggers a step scaling policy
            to scale out an Amazon ECS service by 2 tasks, the scaling activity completes
            successfully, and a cooldown period of 5 minutes starts. During the cooldown period, if
            the alarm triggers the same policy again but at a more aggressive step adjustment to
            scale out the service by 3 tasks, the 2 tasks that were added in the previous scale-out
            event are considered part of that capacity and only 1 additional task is added to the
            desired count.

            For scale-in policies, the cooldown period is used to block subsequent scale-in
            requests until it has expired. The intention is to scale in conservatively to protect
            your application's availability. However, if another alarm triggers a scale-out policy
            during the cooldown period after a scale-in, Application Auto Scaling scales out your
            scalable target immediately.

          - **MetricAggregationType** *(string) --*

            The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` ,
            ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated
            as ``Average`` .

        - **TargetTrackingScalingPolicyConfiguration** *(dict) --*

          A target tracking scaling policy.

          - **TargetValue** *(float) --*

            The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10)
            or 2e-360 to 2e360 (Base 2).

          - **PredefinedMetricSpecification** *(dict) --*

            A predefined metric. You can specify either a predefined metric or a customized metric.

            - **PredefinedMetricType** *(string) --*

              The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot
              Fleet requests and ECS services.

            - **ResourceLabel** *(string) --*

              Identifies the resource associated with the metric type. You can't specify a resource
              label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
              group attached to the Spot Fleet request or ECS service.

              The format is
              app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
              where:

              * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
              balancer ARN

              * targetgroup/<target-group-name>/<target-group-id> is the final portion of the
              target group ARN.

          - **CustomizedMetricSpecification** *(dict) --*

            A customized metric. You can specify either a predefined metric or a customized metric.

            - **MetricName** *(string) --*

              The name of the metric.

            - **Namespace** *(string) --*

              The namespace of the metric.

            - **Dimensions** *(list) --*

              The dimensions of the metric.

              Conditional: If you published your metric with dimensions, you must specify the same
              dimensions in your scaling policy.

              - *(dict) --*

                Describes the dimension names and values associated with a metric.

                - **Name** *(string) --*

                  The name of the dimension.

                - **Value** *(string) --*

                  The value of the dimension.

            - **Statistic** *(string) --*

              The statistic of the metric.

            - **Unit** *(string) --*

              The unit of the metric.

          - **ScaleOutCooldown** *(integer) --*

            The amount of time, in seconds, after a scale-out activity completes before another
            scale-out activity can start.

            While the cooldown period is in effect, the capacity that has been added by the
            previous scale-out event that initiated the cooldown is calculated as part of the
            desired capacity for the next scale out. The intention is to continuously (but not
            excessively) scale out.

          - **ScaleInCooldown** *(integer) --*

            The amount of time, in seconds, after a scale-in activity completes before another
            scale in activity can start.

            The cooldown period is used to block subsequent scale-in requests until it has expired.
            The intention is to scale in conservatively to protect your application's availability.
            However, if another alarm triggers a scale-out policy during the cooldown period after
            a scale-in, Application Auto Scaling scales out your scalable target immediately.

          - **DisableScaleIn** *(boolean) --*

            Indicates whether scale in by the target tracking scaling policy is disabled. If the
            value is ``true`` , scale in is disabled and the target tracking scaling policy won't
            remove capacity from the scalable resource. Otherwise, scale in is enabled and the
            target tracking scaling policy can remove capacity from the scalable resource. The
            default value is ``false`` .

        - **Alarms** *(list) --*

          The CloudWatch alarms associated with the scaling policy.

          - *(dict) --*

            Represents a CloudWatch alarm associated with a scaling policy.

            - **AlarmName** *(string) --*

              The name of the alarm.

            - **AlarmARN** *(string) --*

              The Amazon Resource Name (ARN) of the alarm.

        - **CreationTime** *(datetime) --*

          The Unix timestamp for when the scaling policy was created.
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


_DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)


class DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef(
    _DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef
):
    """
    Type definition for `DescribeScheduledActionsPaginateResponseScheduledActions` `ScalableTargetAction`

    The new minimum and maximum capacity. You can set both values or just one. During the
    scheduled time, if the current capacity is below the minimum capacity, Application Auto
    Scaling scales out to the minimum capacity. If the current capacity is above the maximum
    capacity, Application Auto Scaling scales in to the maximum capacity.

    - **MinCapacity** *(integer) --*

      The minimum capacity.

    - **MaxCapacity** *(integer) --*

      The maximum capacity.
    """


_DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": str,
        "Schedule": str,
        "ResourceId": str,
        "ScalableDimension": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": DescribeScheduledActionsPaginateResponseScheduledActionsScalableTargetActionTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)


class DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef(
    _DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef
):
    """
    Type definition for `DescribeScheduledActionsPaginateResponse` `ScheduledActions`

    Represents a scheduled action.

    - **ScheduledActionName** *(string) --*

      The name of the scheduled action.

    - **ScheduledActionARN** *(string) --*

      The Amazon Resource Name (ARN) of the scheduled action.

    - **ServiceNamespace** *(string) --*

      The namespace of the AWS service that provides the resource or ``custom-resource`` for a
      resource provided by your own application or service. For more information, see `AWS
      Service Namespaces
      <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *Amazon Web Services General Reference* .

    - **Schedule** *(string) --*

      The schedule for this action. The following formats are supported:

      * At expressions - "``at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* )`` "

      * Rate expressions - "``rate(*value*  *unit* )`` "

      * Cron expressions - "``cron(*fields* )`` "

      At expressions are useful for one-time schedules. Specify the time, in UTC.

      For rate expressions, *value* is a positive integer and *unit* is ``minute`` |
      ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` .

      For more information about cron expressions, see `Cron Expressions
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`__
      in the *Amazon CloudWatch Events User Guide* .

    - **ResourceId** *(string) --*

      The identifier of the resource associated with the scaling policy. This string consists
      of the resource type and unique identifier.

      * ECS service - The resource type is ``service`` and the unique identifier is the cluster
      name and service name. Example: ``service/default/sample-webapp`` .

      * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
      identifier is the Spot Fleet request ID. Example:
      ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

      * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
      cluster ID and instance group ID. Example:
      ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

      * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
      fleet name. Example: ``fleet/sample-fleet`` .

      * DynamoDB table - The resource type is ``table`` and the unique identifier is the
      resource ID. Example: ``table/my-table`` .

      * DynamoDB global secondary index - The resource type is ``index`` and the unique
      identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

      * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
      cluster name. Example: ``cluster:my-db-cluster`` .

      * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
      identifier is the resource ID. Example:
      ``endpoint/my-end-point/variant/KMeansClustering`` .

      * Custom resources are not supported with a resource type. This parameter must specify
      the ``OutputValue`` from the CloudFormation template stack used to access the resources.
      The unique identifier is defined by the service provider. More information is available
      in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

    - **ScalableDimension** *(string) --*

      The scalable dimension. This string consists of the service namespace, resource type, and
      scaling property.

      * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

      * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

      * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
      Instance Group.

      * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

      * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
      SageMaker model endpoint variant.

      * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
      resource provided by your own application or service.

    - **StartTime** *(datetime) --*

      The date and time that the action is scheduled to begin.

    - **EndTime** *(datetime) --*

      The date and time that the action is scheduled to end.

    - **ScalableTargetAction** *(dict) --*

      The new minimum and maximum capacity. You can set both values or just one. During the
      scheduled time, if the current capacity is below the minimum capacity, Application Auto
      Scaling scales out to the minimum capacity. If the current capacity is above the maximum
      capacity, Application Auto Scaling scales in to the maximum capacity.

      - **MinCapacity** *(integer) --*

        The minimum capacity.

      - **MaxCapacity** *(integer) --*

        The maximum capacity.

    - **CreationTime** *(datetime) --*

      The date and time that the scheduled action was created.
    """


_DescribeScheduledActionsPaginateResponseTypeDef = TypedDict(
    "_DescribeScheduledActionsPaginateResponseTypeDef",
    {
        "ScheduledActions": List[
            DescribeScheduledActionsPaginateResponseScheduledActionsTypeDef
        ]
    },
    total=False,
)


class DescribeScheduledActionsPaginateResponseTypeDef(
    _DescribeScheduledActionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeScheduledActionsPaginate` `Response`

    - **ScheduledActions** *(list) --*

      Information about the scheduled actions.

      - *(dict) --*

        Represents a scheduled action.

        - **ScheduledActionName** *(string) --*

          The name of the scheduled action.

        - **ScheduledActionARN** *(string) --*

          The Amazon Resource Name (ARN) of the scheduled action.

        - **ServiceNamespace** *(string) --*

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        - **Schedule** *(string) --*

          The schedule for this action. The following formats are supported:

          * At expressions - "``at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* )`` "

          * Rate expressions - "``rate(*value*  *unit* )`` "

          * Cron expressions - "``cron(*fields* )`` "

          At expressions are useful for one-time schedules. Specify the time, in UTC.

          For rate expressions, *value* is a positive integer and *unit* is ``minute`` |
          ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` .

          For more information about cron expressions, see `Cron Expressions
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`__
          in the *Amazon CloudWatch Events User Guide* .

        - **ResourceId** *(string) --*

          The identifier of the resource associated with the scaling policy. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the
          resource ID. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variants - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example:
          ``endpoint/my-end-point/variant/KMeansClustering`` .

          * Custom resources are not supported with a resource type. This parameter must specify
          the ``OutputValue`` from the CloudFormation template stack used to access the resources.
          The unique identifier is defined by the service provider. More information is available
          in our `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

        - **ScalableDimension** *(string) --*

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
          Instance Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

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

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
          resource provided by your own application or service.

        - **StartTime** *(datetime) --*

          The date and time that the action is scheduled to begin.

        - **EndTime** *(datetime) --*

          The date and time that the action is scheduled to end.

        - **ScalableTargetAction** *(dict) --*

          The new minimum and maximum capacity. You can set both values or just one. During the
          scheduled time, if the current capacity is below the minimum capacity, Application Auto
          Scaling scales out to the minimum capacity. If the current capacity is above the maximum
          capacity, Application Auto Scaling scales in to the maximum capacity.

          - **MinCapacity** *(integer) --*

            The minimum capacity.

          - **MaxCapacity** *(integer) --*

            The maximum capacity.

        - **CreationTime** *(datetime) --*

          The date and time that the scheduled action was created.
    """
